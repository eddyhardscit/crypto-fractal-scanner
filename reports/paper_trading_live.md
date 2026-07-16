# Paper trading automatico KuCoin

Generato: 2026-07-16T20:29:49+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-16T20:29:39+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-16T20:29:39+00:00 | 2026-07-16T20:29:39+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-16T20:00:00+00:00 | 2026-07-16T20:00:00+00:00 | 14,7 min | 25,0 min | OK |
| 60m | 12 | 2026-07-16T19:00:00+00:00 | 2026-07-16T19:00:00+00:00 | 29,7 min | 45,0 min | OK |
| 240m | 12 | 2026-07-16T16:00:00+00:00 | 2026-07-16T16:00:00+00:00 | 29,7 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | HYPE | 240m | SHORT | -7,50 | 6,00 | 0,00 | RISK_GATE | 29,7 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | AKE | 240m | LONG | 6,25 | 6,00 | 0,00 | RISK_GATE | 29,7 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | LAB | 240m | SHORT | -6,25 | 6,00 | 0,00 | RISK_GATE | 29,7 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | DOGE | 240m | SHORT | -5,84 | 6,00 | 0,16 | BELOW_SCORE | 29,7 min | D: Hidden bearish [CONFERMATA] | W: Misto / nessuna divergenza [CONTESTO] | peso 0 | Punteggio -5.84; soglia ±6.00; mancano 0.16 punti. |
| Principale 4H | SOL | 240m | SHORT | -4,94 | 6,00 | 1,06 | BELOW_SCORE | 29,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Punteggio -4.94; soglia ±6.00; mancano 1.06 punti. |
| Principale 4H | ETH | 240m | LONG | 4,85 | 6,00 | 1,15 | BELOW_SCORE | 29,7 min | D: n/a | W: n/a | peso 0 | Punteggio +4.85; soglia ±6.00; mancano 1.15 punti. |
| Principale 4H | ADA | 240m | SHORT | -4,82 | 6,00 | 1,18 | BELOW_SCORE | 29,7 min | D: n/a | W: n/a | peso 0 | Punteggio -4.82; soglia ±6.00; mancano 1.18 punti. |
| Sol Adaptive 1H | SOL | 60m | SHORT | -8,00 | 5,00 | 0,00 | OPENED | 29,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H | SOL | 60m | SHORT | -8,00 | 4,50 | 0,00 | STRATEGY_FILTER | 29,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.71%. |
| Forza relativa 1H | SOL | 60m | SHORT | -8,00 | 4,00 | 0,00 | STRATEGY_FILTER | 29,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=-1.25%. |
| Rapida 1H | DOGE | 60m | SHORT | -5,22 | 4,50 | 0,00 | STRATEGY_FILTER | 29,7 min | D: Hidden bearish [CONFERMATA] | W: Misto / nessuna divergenza [CONTESTO] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.54%. |
| Forza relativa 1H | DOGE | 60m | SHORT | -5,22 | 4,00 | 0,00 | STRATEGY_FILTER | 29,7 min | D: Hidden bearish [CONFERMATA] | W: Misto / nessuna divergenza [CONTESTO] | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=-0.28%. |
| Bilanciata 1H | SOL | 60m | SHORT | -8,00 | 5,00 | 0,00 | RISK_GATE | 29,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Benchmark trend following EMA 1H | SOL | 60m | SHORT | -8,00 | 5,00 | 0,00 | RISK_GATE | 29,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Scanner Bottom 5 Short 1H | SOL | 60m | SHORT | -8,00 | 5,00 | 0,00 | RISK_GATE | 29,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Combo Trend | SOL | 60m | SHORT | -8,00 | 5,00 | 0,00 | RISK_GATE | 29,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Combo Adaptive | SOL | 60m | SHORT | -8,00 | 5,00 | 0,00 | RISK_GATE | 29,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Sol Ema 1H | SOL | 60m | SHORT | -8,00 | 5,00 | 0,00 | RISK_GATE | 29,7 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Ampia 4H | HYPE | 240m | SHORT | -7,50 | 5,00 | 0,00 | RISK_GATE | 29,7 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Ampia 4H | AKE | 240m | LONG | 6,25 | 5,00 | 0,00 | RISK_GATE | 29,7 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.893,16 | -1,07% | €-106,84 | €3.000,00 | -3,56% | 4 | 9 | 33,33% | 0,86 | 3,34% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 9 | 52 | CAMPIONE INSUFFICIENTE | 30 (mancano 21) |

- Trade del Principale 4H chiusi: **9**; win rate **33,33%**; profit factor **0,86**.
- Expectancy: **€-3,97** per trade; P&L netto: **€-35,75**; max drawdown: **3,34%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.893,16 | €2.193,60 | €6.580,80 | €197,75 | €-65,51 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.358,54 | €2.769,20 | €5.538,41 | €153,73 | €-2,26 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.289,88 | €2.349,98 | €4.699,96 | €101,59 | €29,46 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.172,35 | €1.728,73 | €3.457,46 | €102,03 | €50,46 |
| TEST | Combo Adaptive | 3 | €10.156,76 | €2.902,62 | €5.805,24 | €152,02 | €-2,88 |
| TEST | Forza relativa 1H | 4 | €10.087,26 | €2.607,73 | €5.215,46 | €200,81 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €10.076,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H | 4 | €10.073,31 | €1.737,28 | €5.211,83 | €200,67 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €10.072,32 | €1.583,68 | €3.167,36 | €100,77 | €-9,34 |
| TEST | Rapida 1H | 4 | €10.058,09 | €2.598,20 | €7.794,61 | €150,39 | €40,24 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €10.056,28 | €1.964,02 | €3.928,04 | €150,30 | €9,48 |
| TEST | Ampia 4H | 4 | €10.052,85 | €2.257,17 | €4.514,33 | €200,61 | €-31,03 |
| TEST | Combo Trend | 3 | €10.042,73 | €2.583,02 | €5.166,05 | €150,31 | €-2,56 |
| TEST | Sol Ema 1H | 1 | €10.005,04 | €1.157,41 | €3.472,22 | €50,00 | €7,12 |
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
| TEST | Btc Ema 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.998,01 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.997,22 | €1.157,41 | €3.472,22 | €50,00 | €-0,69 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.996,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.990,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.933,83 | €1.553,81 | €3.107,63 | €49,72 | €-8,72 |
| TEST | Combo Scanner | 3 | €9.931,73 | €3.451,56 | €6.903,11 | €149,32 | €-11,89 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.914,18 | €2.720,15 | €5.440,31 | €149,22 | €-30,12 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.893,16 | €-35,75 | 9 | 9 | 33,33% | 0,86 | €-3,97 | 3,34% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.358,54 | €364,12 | 7 | 7 | 85,71% | 7,49 | €52,02 | 0,44% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.289,88 | €263,41 | 5 | 5 | 80,00% | 5,90 | €52,68 | 0,81% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.172,35 | €123,26 | 3 | 3 | 66,67% | 3,27 | €41,09 | 1,22% |
| TEST | Combo Adaptive | Combo Adaptive | €10.156,76 | €163,12 | 7 | 7 | 57,14% | 2,49 | €23,30 | 0,75% |
| TEST | Forza relativa 1H | Forza relativa vs BTC | €10.087,26 | €88,40 | 7 | 7 | 57,14% | 1,56 | €12,63 | 1,36% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.076,46 | €76,46 | 1 | 1 | 100,00% | ∞ | €76,46 | 0,02% |
| TEST | Bilanciata 1H | Confluenza trend | €10.073,31 | €74,45 | 8 | 8 | 50,00% | 1,47 | €9,31 | 1,06% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.072,32 | €83,39 | 4 | 4 | 50,00% | 2,38 | €20,85 | 0,85% |
| TEST | Rapida 1H | Momentum / breakout | €10.058,09 | €22,15 | 22 | 22 | 40,91% | 1,05 | €1,01 | 2,34% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €10.056,28 | €48,53 | 2 | 2 | 50,00% | 1,96 | €24,27 | 0,51% |
| TEST | Ampia 4H | Confluenza trend | €10.052,85 | €87,07 | 3 | 3 | 33,33% | 2,66 | €29,02 | 1,66% |
| TEST | Combo Trend | Combo Trend | €10.042,73 | €48,40 | 5 | 5 | 40,00% | 1,45 | €9,68 | 1,48% |
| TEST | Sol Ema 1H | Trend following EMA | €10.005,04 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,34% |
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
| TEST | Btc Ema 1H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Ema 1H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Doge Ema 1H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.998,01 | €-1,99 | 2 | 2 | 50,00% | 0,31 | €-1,00 | 0,04% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.997,22 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,03% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.996,80 | €-3,20 | 2 | 2 | 50,00% | 0,70 | €-1,60 | 0,16% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.990,05 | €-9,95 | 2 | 2 | 50,00% | 0,31 | €-4,98 | 0,18% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.933,83 | €-55,58 | 1 | 1 | 0,00% | 0,00 | €-55,58 | 1,18% |
| TEST | Combo Scanner | Combo Scanner | €9.931,73 | €-52,24 | 3 | 3 | 33,33% | 0,51 | €-17,41 | 1,56% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.914,18 | €-50,62 | 1 | 1 | 0,00% | 0,00 | €-50,62 | 0,94% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | BTC | LONG | Confluenza trend | 240m | 3,0x | 64799,97740 | 64172,10000 | 63375,06284 | 43523,98482 | 67649,80654 | €755,98 | €2.267,94 | €49,87 | €-21,98 |
| Principale 4H | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €334,65 | €1.003,96 | €49,15 | €-37,82 |
| Principale 4H | ETH | LONG | Confluenza trend | 240m | 3,0x | 1874,64485 | 1872,77000 | 1816,18750 | 1259,13646 | 1991,55955 | €528,52 | €1.585,57 | €49,44 | €-1,59 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07309 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €-4,13 |
| Bilanciata 1H | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,47752 | €716,68 | €2.150,03 | €49,99 | €0,00 |
| Bilanciata 1H | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00663 | €146,15 | €438,46 | €49,94 | €0,00 |
| Bilanciata 1H | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,02421 | 2,02421 | 1,97233 | 1,35960 | 2,12798 | €655,13 | €1.965,38 | €50,37 | €0,00 |
| Bilanciata 1H | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,37581 | 0,37581 | 0,40458 | 0,49921 | 0,31828 | €219,32 | €657,96 | €50,37 | €-0,00 |
| Rapida 1H | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,02421 | 2,02421 | 1,98386 | 1,35960 | 2,08474 | €844,18 | €2.532,55 | €50,49 | €0,00 |
| Rapida 1H | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,21674 | 0,21118 | 0,24275 | 0,28790 | 0,17772 | €139,85 | €419,55 | €50,35 | €10,76 |
| Rapida 1H | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00086 | 0,00092 | 0,00086 | 0,00058 | 0,00101 | €139,26 | €417,77 | €0,00 | €30,98 |
| Rapida 1H | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,07307 | 0,07309 | 0,07388 | 0,09706 | 0,07184 | €1.474,91 | €4.424,73 | €49,56 | €-1,49 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07309 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-12,99 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 544,97000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €28,78 |
| Ampia 4H | BTC | LONG | Confluenza trend | 240m | 2,0x | 64799,97740 | 64172,10000 | 62947,58840 | 32723,98859 | 69986,66609 | €879,97 | €1.759,95 | €50,31 | €-17,05 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €395,18 | €790,36 | €50,30 | €-29,77 |
| Forza relativa 1H | AAVE | LONG | Forza relativa vs BTC | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H | T | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H | NEAR | LONG | Forza relativa vs BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H | ALLO | SHORT | Forza relativa vs BTC | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Benchmark Donchian breakout 1H | LAB | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,26148 | 0,21118 | 0,25197 | 0,39091 | 0,18303 | €211,57 | €423,15 | €0,00 | €81,40 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,16194 | 0,16245 | 0,16511 | 0,24210 | 0,15403 | €1.304,57 | €2.609,14 | €51,00 | €-8,17 |
| Benchmark Donchian breakout 1H | AKE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00097 | 0,00092 | 0,00086 | 0,00049 | 0,00126 | €212,59 | €425,17 | €51,02 | €-22,76 |
| Benchmark Bollinger mean reversion 1H | AKE | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,00090 | 0,00092 | 0,00101 | 0,00135 | 0,00074 | €210,07 | €420,14 | €50,42 | €-9,05 |
| Benchmark Bollinger mean reversion 1H | HYPE | LONG | Bollinger mean reversion | 60m | 2,0x | 62,39648 | 62,39000 | 61,25294 | 31,51022 | 64,11178 | €1.373,61 | €2.747,22 | €50,35 | €-0,29 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 64799,97740 | 64172,10000 | 63763,17777 | 32723,98859 | 67080,93661 | €1.554,43 | €3.108,85 | €49,74 | €-30,12 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Scanner Top 5 Long 1H | NEAR | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,12798 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 Long 1H | XLM | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,18989 | 0,18971 | 0,18567 | 0,09590 | 0,19833 | €1.168,57 | €2.337,14 | €51,93 | €-2,26 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €625,48 | €1.250,97 | €51,81 | €0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31828 | €324,92 | €649,84 | €49,75 | €-0,00 |
| Scanner Bottom 5 Short 1H | LAB | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,22091 | 0,21118 | 0,24741 | 0,33025 | 0,16789 | €209,34 | €418,67 | €50,24 | €18,43 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16194 | 0,16245 | 0,16479 | 0,24210 | 0,15624 | €1.429,76 | €2.859,53 | €50,31 | €-8,96 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00086 | 0,00092 | 0,00086 | 0,00043 | 0,00108 | €213,80 | €427,59 | €0,00 | €31,71 |
| Scanner Top 5 + forza BTC 1H | XLM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,18989 | 0,18971 | 0,18567 | 0,09590 | 0,19918 | €1.161,04 | €2.322,07 | €51,60 | €-2,25 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07289 | 0,07309 | 0,07405 | 0,10896 | 0,06997 | €1.553,81 | €3.107,63 | €49,72 | €-8,72 |
| Combo Trend | XLM | LONG | Combo Trend | 60m | 2,0x | 0,18989 | 0,18971 | 0,18521 | 0,09590 | 0,20021 | €1.009,39 | €2.018,78 | €49,84 | €-1,95 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,35567 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €50,24 | €0,00 |
| Combo Trend | HYPE | SHORT | Combo Trend | 60m | 2,0x | 62,37152 | 62,39000 | 63,89563 | 93,24543 | 59,01849 | €1.027,78 | €2.055,56 | €50,23 | €-0,61 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,07289 | 0,07309 | 0,07393 | 0,10896 | 0,07058 | €1.730,98 | €3.461,95 | €49,85 | €-9,72 |
| Combo Scanner | XLM | LONG | Combo Scanner | 60m | 2,0x | 0,18989 | 0,18971 | 0,18567 | 0,09590 | 0,19918 | €1.121,44 | €2.242,88 | €49,84 | €-2,17 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40679 | €599,14 | €1.198,28 | €49,63 | €0,00 |
| Combo Adaptive | XLM | LONG | Combo Adaptive | 60m | 2,0x | 0,18989 | 0,18971 | 0,18567 | 0,09590 | 0,19833 | €1.134,22 | €2.268,44 | €50,41 | €-2,20 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €613,42 | €1.226,85 | €50,81 | €0,00 |
| Combo Adaptive | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 62,37152 | 62,39000 | 63,74322 | 93,24543 | 59,62813 | €1.154,98 | €2.309,96 | €50,80 | €-0,68 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 75,94281 | 75,78700 | 77,03638 | 100,87736 | 73,75566 | €1.157,41 | €3.472,22 | €50,00 | €7,12 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 75,77184 | 75,78700 | 76,86296 | 100,65026 | 73,58961 | €1.157,41 | €3.472,22 | €50,00 | €-0,69 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Top 5 Long 1H | AKE | LONG | 2026-07-16T17:54:54+00:00 | 0,00093 | €56,73 | 1,10 | STOP |
| Combo Trend | HYPE | SHORT | 2026-07-16T17:54:54+00:00 | 62,81175 | €106,01 | 2,13 | TARGET |
| Combo Trend | AKE | LONG | 2026-07-16T17:54:54+00:00 | 0,00092 | €48,85 | 0,98 | STOP |
| Combo Scanner | AKE | LONG | 2026-07-16T17:54:54+00:00 | 0,00093 | €54,51 | 1,10 | STOP |
| Combo Adaptive | HYPE | SHORT | 2026-07-16T17:54:54+00:00 | 63,29852 | €96,70 | 1,92 | TARGET |
| Combo Adaptive | AKE | LONG | 2026-07-16T17:54:54+00:00 | 0,00094 | €60,82 | 1,21 | STOP |
| Global Confluence puro 1H | BTC | LONG | 2026-07-16T12:54:01+00:00 | 63960,43040 | €-55,58 | -1,11 | STOP |
| Scanner Top 5 Long 1H | ETH | LONG | 2026-07-16T09:22:55+00:00 | 1892,02053 | €-56,09 | -1,09 | STOP |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | 2026-07-16T09:22:55+00:00 | 557,65511 | €-53,72 | -1,06 | STOP |
| Combo Trend | ZEC | LONG | 2026-07-16T09:22:55+00:00 | 549,27606 | €-52,70 | -1,05 | STOP |
| Combo Scanner | ZEC | LONG | 2026-07-16T09:22:55+00:00 | 550,85746 | €-53,00 | -1,06 | STOP |
| Combo Adaptive | ETH | LONG | 2026-07-16T09:22:55+00:00 | 1893,00242 | €-55,15 | -1,10 | STOP |

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
| MAIN | Principale 4H | 13/30 | 9/30 | 0,58 | 0,86 | -0,33R | €-3,97 | 3,34% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 2/30 | 2/30 | 1,18 | 0,70 | 0,10R | €-1,60 | 0,16% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H | 48/30 | 8/30 | 0,83 | 1,47 | -0,13R | €9,31 | 1,06% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H | 53/30 | 22/30 | 0,58 | 1,05 | -0,31R | €1,01 | 2,34% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 9/30 | 3/30 | 0,34 | 2,66 | -0,60R | €29,02 | 1,66% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 8/30 | 4/30 | 0,78 | 2,38 | -0,15R | €20,85 | 0,85% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive | 9/30 | 7/30 | 2,27 | 2,49 | 0,60R | €23,30 | 0,75% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 1/30 | 1/30 | ∞ | ∞ | 1,52R | €76,46 | 0,02% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 8/30 | 3/30 | 1,20 | 0,51 | 0,14R | €-17,41 | 1,56% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_TREND | Combo Trend | 6/30 | 5/30 | 2,06 | 1,45 | 0,56R | €9,68 | 1,48% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 5/30 | 3/30 | 1,55 | 3,27 | 0,34R | €41,09 | 1,22% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 12/30 | 1/30 | 1,02 | 0,00 | 0,01R | €-50,62 | 0,94% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,10R | €-55,58 | 1,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H | 32/30 | 7/30 | 0,69 | 1,56 | -0,24R | €12,63 | 1,36% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 5/30 | 2/30 | 1,25 | 1,96 | 0,15R | €24,27 | 0,51% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 10/30 | 5/30 | 1,34 | 5,90 | 0,22R | €52,68 | 0,81% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 13/30 | 7/30 | 1,14 | 7,49 | 0,09R | €52,02 | 0,44% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,03% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,34% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07309**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 29.8 min | OK |
| Global DOGE | -5.0 | OK |
| Classic raw | -6.0 | OK |
| DOGE/BTC raw | -8.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 64172.1 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased**
- High **0.07315**; close **0.07308**; wick alta **37.5%**; volume **x0.75**

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
- BTC trend score: **2,00**; ADX: **26,99**; breadth sopra EMA50: **16,67%**
- Mediana alt vs BTC: **-0,31%**; dispersione: **11,58%**

- Aperti in questo ciclo: **7**
- Chiusi in questo ciclo: **2**
- Posizioni research aperte: **92**
- Trade research chiusi: **235**
- Eventi di mercato indipendenti chiusi: **104**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **556**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 9 | 13 | 13 | 23,08% | 0,58 | -0,33R | €-43,22 |
| RSI_EXTREME_SHORT_15M | 0 | 2 | 2 | 50,00% | 1,18 | 0,10R | €1,96 |
| SHADOW_1H_BALANCED | 10 | 48 | 48 | 31,25% | 0,83 | -0,13R | €-61,42 |
| SHADOW_1H_FAST | 7 | 53 | 53 | 30,19% | 0,58 | -0,31R | €-166,56 |
| SHADOW_4H_WIDE | 11 | 9 | 9 | 11,11% | 0,34 | -0,60R | €-54,26 |
| SHADOW_BOLLINGER_MR_1H | 1 | 8 | 8 | 37,50% | 0,78 | -0,15R | €-12,01 |
| SHADOW_COMBO_ADAPTIVE | 6 | 9 | 9 | 55,56% | 2,27 | 0,60R | €54,33 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 1 | 1 | 100,00% | ∞ | 1,52R | €15,18 |
| SHADOW_COMBO_SCANNER | 3 | 8 | 8 | 37,50% | 1,20 | 0,14R | €10,86 |
| SHADOW_COMBO_TREND | 7 | 6 | 6 | 50,00% | 2,06 | 0,56R | €33,41 |
| SHADOW_DONCHIAN_1H | 5 | 5 | 5 | 40,00% | 1,55 | 0,34R | €17,16 |
| SHADOW_EMA_TREND_1H | 9 | 12 | 12 | 33,33% | 1,02 | 0,01R | €1,36 |
| SHADOW_GLOBAL_PURE | 1 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_RELATIVE_STRENGTH | 8 | 32 | 32 | 25,00% | 0,69 | -0,24R | €-78,38 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 6 | 5 | 5 | 40,00% | 1,25 | 0,15R | €7,73 |
| SHADOW_SCANNER_TOP5_BTC | 3 | 10 | 10 | 40,00% | 1,34 | 0,22R | €22,05 |
| SHADOW_SCANNER_TOP5_LONG | 4 | 13 | 13 | 38,46% | 1,14 | 0,09R | €11,69 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | RANGE | 0 | 10 | 10 | 20,00% | 0,48 | -0,43R | €-42,62 |
| MAIN | TRANSITION | 5 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| MAIN | TREND_UP | 4 | 2 | 2 | 50,00% | 1,92 | 0,48R | €9,54 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,86 |
| SHADOW_1H_BALANCED | ALT_ROTATION_UP | 0 | 9 | 9 | 55,56% | 2,27 | 0,60R | €54,20 |
| SHADOW_1H_BALANCED | RANGE | 1 | 15 | 15 | 40,00% | 1,23 | 0,15R | €21,89 |
| SHADOW_1H_BALANCED | RANGE_HIGH_VOL | 0 | 9 | 9 | 0,00% | 0,00 | -1,08R | €-97,25 |
| SHADOW_1H_BALANCED | TRANSITION | 7 | 3 | 3 | 66,67% | 3,57 | 0,93R | €28,00 |
| SHADOW_1H_BALANCED | TREND_UP | 2 | 12 | 12 | 16,67% | 0,37 | -0,57R | €-68,26 |
| SHADOW_1H_FAST | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,38 | 0,20R | €12,11 |
| SHADOW_1H_FAST | RANGE | 1 | 19 | 19 | 42,11% | 1,01 | 0,00R | €0,76 |
| SHADOW_1H_FAST | RANGE_HIGH_VOL | 0 | 10 | 10 | 0,00% | 0,00 | -1,10R | €-109,76 |
| SHADOW_1H_FAST | TRANSITION | 5 | 4 | 4 | 50,00% | 1,27 | 0,15R | €6,04 |
| SHADOW_1H_FAST | TREND_UP | 1 | 14 | 14 | 21,43% | 0,37 | -0,54R | €-75,71 |
| SHADOW_4H_WIDE | RANGE | 2 | 8 | 8 | 12,50% | 0,39 | -0,55R | €-44,12 |
| SHADOW_4H_WIDE | TRANSITION | 4 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | TREND_UP | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 2 | 2 | 50,00% | 1,27 | 0,15R | €2,97 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 5 | 5 | 40,00% | 0,85 | -0,10R | €-4,84 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 4 | 2 | 2 | 100,00% | ∞ | 1,95R | €38,91 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 7 | 7 | 42,86% | 1,36 | 0,22R | €15,42 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,52R | €15,18 |
| SHADOW_COMBO_SCANNER | TRANSITION | 3 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 7 | 7 | 28,57% | 0,80 | -0,16R | €-11,00 |
| SHADOW_COMBO_TREND | TRANSITION | 4 | 2 | 2 | 100,00% | ∞ | 2,15R | €43,01 |
| SHADOW_COMBO_TREND | TREND_UP | 3 | 4 | 4 | 25,00% | 0,70 | -0,24R | €-9,59 |
| SHADOW_DONCHIAN_1H | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,44R | €24,45 |
| SHADOW_DONCHIAN_1H | TRANSITION | 2 | 2 | 2 | 50,00% | 2,38 | 0,70R | €14,01 |
| SHADOW_DONCHIAN_1H | TREND_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,29 |
| SHADOW_EMA_TREND_1H | RANGE | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_EMA_TREND_1H | TRANSITION | 4 | 2 | 2 | 100,00% | ∞ | 2,15R | €42,99 |
| SHADOW_EMA_TREND_1H | TREND_UP | 4 | 9 | 9 | 22,22% | 0,58 | -0,35R | €-31,50 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | ALT_ROTATION_UP | 0 | 8 | 8 | 25,00% | 0,68 | -0,26R | €-20,48 |
| SHADOW_RELATIVE_STRENGTH | RANGE | 1 | 14 | 14 | 21,43% | 0,56 | -0,36R | €-49,93 |
| SHADOW_RELATIVE_STRENGTH | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| SHADOW_RELATIVE_STRENGTH | TRANSITION | 3 | 1 | 1 | 100,00% | ∞ | 2,10R | €21,04 |
| SHADOW_RELATIVE_STRENGTH | TREND_UP | 4 | 7 | 7 | 28,57% | 0,83 | -0,12R | €-8,69 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 4 | 2 | 2 | 50,00% | 1,75 | 0,41R | €8,13 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 1 | 2 | 2 | 100,00% | ∞ | 2,12R | €42,42 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 2 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 6 | 6 | 16,67% | 0,41 | -0,53R | €-31,71 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 2 | 2 | 100,00% | ∞ | 1,92R | €38,42 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 2 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 10 | 10 | 20,00% | 0,46 | -0,47R | €-46,60 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_1H | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
