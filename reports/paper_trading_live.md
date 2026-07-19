# Paper trading automatico KuCoin

Generato: 2026-07-19T12:08:34+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-19T12:08:24+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-19T12:08:24+00:00 | 2026-07-19T12:08:24+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-19T11:45:00+00:00 | 2026-07-19T11:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-19T11:00:00+00:00 | 2026-07-19T11:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-19T08:00:00+00:00 | 2026-07-19T08:00:00+00:00 | 8,5 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | AKE | 240m | LONG | 7,75 | 6,00 | 0,00 | RISK_GATE | 8,4 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | RISK_GATE | 8,4 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | ESPORTS | 240m | LONG | 6,75 | 6,00 | 0,00 | RISK_GATE | 8,4 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | ZEC | 240m | LONG | 6,71 | 6,00 | 0,00 | RISK_GATE | 8,4 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | HYPE | 240m | SHORT | -6,25 | 6,00 | 0,00 | RISK_GATE | 8,4 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | PEPE | 240m | LONG | 6,05 | 6,00 | 0,00 | RISK_GATE | 8,4 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | DOGE | 240m | SHORT | -6,01 | 6,00 | 0,00 | RISK_GATE | 8,4 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | ETH | 240m | LONG | 5,20 | 6,00 | 0,80 | BELOW_SCORE | 8,4 min | D: n/a | W: n/a | peso 0 | Punteggio +5.20; soglia ±6.00; mancano 0.80 punti. |
| Bilanciata 1H V2 | PEPE | 60m | LONG | 6,92 | 5,50 | 0,00 | OPENED | 8,4 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | PEPE | 60m | LONG | 6,92 | 5,50 | 0,00 | OPENED | 8,4 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | ETH | 60m | LONG | 5,78 | 5,50 | 0,00 | READY | 8,4 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V2 | PEPE | 60m | LONG | 6,92 | 5,00 | 0,00 | STRATEGY_FILTER | 8,4 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Bilanciata 1H V2 | BANK | 60m | LONG | 6,25 | 5,50 | 0,00 | STRATEGY_FILTER | 8,4 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | BANK | 60m | LONG | 6,25 | 5,00 | 0,00 | STRATEGY_FILTER | 8,4 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 | ETH | 60m | LONG | 5,78 | 4,50 | 0,00 | STRATEGY_FILTER | 8,4 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.15%. |
| Rapida 1H V2 | ETH | 60m | LONG | 5,78 | 5,00 | 0,00 | STRATEGY_FILTER | 8,4 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Forza relativa 1H V1 | ETH | 60m | LONG | 5,78 | 4,00 | 0,00 | STRATEGY_FILTER | 8,4 min | D: n/a | W: n/a | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=+0.15%. |
| Forza relativa 1H V1 | XRP | 60m | LONG | 4,17 | 4,00 | 0,00 | STRATEGY_FILTER | 8,4 min | D: n/a | W: n/a | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=-0.38%. |
| Ampia 4H | AKE | 240m | LONG | 7,75 | 5,00 | 0,00 | RISK_GATE | 8,4 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Ampia 4H | BANK | 240m | LONG | 7,75 | 5,00 | 0,00 | RISK_GATE | 8,4 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.936,13 | -0,64% | €-63,87 | €3.000,00 | -2,13% | 4 | 15 | 33,33% | 0,89 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 15 | 151 | CAMPIONE INSUFFICIENTE | 30 (mancano 15) |

- Trade del Principale 4H chiusi: **15**; win rate **33,33%**; profit factor **0,89**.
- Expectancy: **€-3,37** per trade; P&L netto: **€-50,49**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.936,13 | €1.317,93 | €3.953,78 | €197,45 | €-12,48 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.347,51 | €2.760,17 | €5.520,34 | €153,56 | €-3,26 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.318,75 | €2.809,27 | €5.618,54 | €152,93 | €-3,25 |
| TEST | Combo Adaptive | 3 | €10.246,94 | €3.522,36 | €7.044,73 | €153,58 | €-1,32 |
| TEST | Rapida 1H V1 | 3 | €10.240,03 | €1.533,99 | €4.601,96 | €154,84 | €0,00 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.223,92 | €1.798,51 | €3.597,02 | €101,87 | €10,12 |
| TEST | Ampia 4H | 4 | €10.201,94 | €1.562,36 | €3.124,72 | €150,11 | €44,81 |
| TEST | Combo Mean Reversion | 1 | €10.175,60 | €281,61 | €563,22 | €50,37 | €0,00 |
| TEST | Combo Trend | 3 | €10.114,75 | €3.048,77 | €6.097,54 | €151,18 | €-54,16 |
| TEST | Forza relativa 1H V1 | 4 | €10.087,26 | €2.607,73 | €5.215,46 | €200,81 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 3 | €10.079,13 | €4.251,88 | €8.503,75 | €147,91 | €9,75 |
| TEST | Forza relativa 1H V2 | 4 | €10.078,43 | €2.878,80 | €5.757,60 | €201,64 | €-38,40 |
| TEST | Bilanciata 1H V1 | 4 | €10.069,34 | €1.461,18 | €4.383,54 | €201,39 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.068,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €10.062,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 4 | €10.060,24 | €2.654,06 | €7.962,19 | €199,86 | €-21,55 |
| TEST | Combo Scanner | 3 | €10.034,76 | €3.487,82 | €6.975,64 | €150,65 | €-17,01 |
| TEST | Doge Donchian 1H | 0 | €10.026,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €10.015,38 | €2.275,49 | €4.550,97 | €99,89 | €-12,71 |
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
| TEST | Doge Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €9.997,83 | €2.319,19 | €6.957,56 | €149,66 | €-36,46 |
| TEST | Eth Bollinger 1H | 1 | €9.997,42 | €1.388,89 | €4.166,67 | €50,00 | €-0,12 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.996,43 | €2.089,95 | €4.179,90 | €149,62 | €-31,69 |
| TEST | Eth Donchian 1H | 1 | €9.996,17 | €1.302,08 | €3.906,25 | €50,00 | €-1,45 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.995,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €9.995,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.990,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.982,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.981,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.979,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €9.971,70 | €1.155,81 | €3.467,44 | €49,93 | €-13,13 |
| TEST | Eth Ema 1H | 1 | €9.957,18 | €1.151,05 | €3.453,16 | €49,73 | €14,18 |
| TEST | Btc Ema 1H | 0 | €9.945,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.945,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.944,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 1 | €9.941,71 | €1.151,05 | €3.453,16 | €49,73 | €-1,28 |
| TEST | Global Confluence puro 1H | 1 | €9.915,69 | €1.551,38 | €3.102,75 | €49,64 | €-12,18 |
| TEST | Rapida 1H V3 Filtered | 2 | €9.863,13 | €2.814,46 | €8.443,37 | €99,32 | €-20,19 |
| TEST | Combo Adaptive MFE Trail | 1 | €9.738,77 | €1.710,41 | €3.420,83 | €49,26 | €-1,27 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.936,13 | €-50,49 | 15 | 15 | 33,33% | 0,89 | €-3,37 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.347,51 | €354,46 | 14 | 14 | 57,14% | 2,31 | €25,32 | 1,65% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.318,75 | €325,68 | 12 | 12 | 50,00% | 2,51 | €27,14 | 1,62% |
| TEST | Combo Adaptive | Combo Adaptive | €10.246,94 | €252,59 | 14 | 14 | 42,86% | 2,15 | €18,04 | 0,89% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.240,03 | €242,70 | 35 | 35 | 42,86% | 1,34 | €6,93 | 2,34% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.223,92 | €215,99 | 10 | 10 | 50,00% | 2,00 | €21,60 | 1,98% |
| TEST | Ampia 4H | Confluenza trend | €10.201,94 | €157,76 | 9 | 9 | 33,33% | 1,60 | €17,53 | 2,08% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.175,60 | €176,28 | 4 | 4 | 75,00% | 4,42 | €44,07 | 0,59% |
| TEST | Combo Trend | Combo Trend | €10.114,75 | €170,64 | 8 | 8 | 50,00% | 2,07 | €21,33 | 1,48% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €10.087,26 | €88,40 | 7 | 7 | 57,14% | 1,56 | €12,63 | 1,36% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.079,13 | €74,78 | 10 | 10 | 50,00% | 1,34 | €7,48 | 2,06% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.078,43 | €120,15 | 10 | 10 | 30,00% | 1,57 | €12,02 | 2,32% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.069,34 | €71,78 | 10 | 10 | 50,00% | 1,44 | €7,18 | 1,06% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.068,69 | €68,69 | 1 | 1 | 100,00% | ∞ | €68,69 | 0,31% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.062,78 | €62,78 | 2 | 1 | 50,00% | 11,45 | €31,39 | 0,93% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.060,24 | €86,38 | 12 | 10 | 50,00% | 1,32 | €7,20 | 2,10% |
| TEST | Combo Scanner | Combo Scanner | €10.034,76 | €55,26 | 10 | 10 | 40,00% | 1,21 | €5,53 | 1,69% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.026,22 | €26,22 | 1 | 1 | 100,00% | ∞ | €26,22 | 0,36% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €10.015,38 | €29,58 | 5 | 5 | 60,00% | 1,28 | €5,92 | 1,90% |
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
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.997,83 | €37,46 | 10 | 10 | 40,00% | 1,12 | €3,75 | 2,20% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.997,42 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,26% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.996,43 | €30,25 | 4 | 4 | 50,00% | 1,28 | €7,56 | 1,10% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.996,17 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,18% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.995,97 | €-4,03 | 4 | 4 | 25,00% | 0,18 | €-1,01 | 0,04% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.995,51 | €-4,49 | 1 | 1 | 0,00% | 0,00 | €-4,49 | 0,43% |
| TEST | Sol Ema 1H | Trend following EMA | €9.990,84 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 0,87% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.982,18 | €-17,82 | 4 | 4 | 25,00% | 0,30 | €-4,46 | 0,18% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.981,55 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 0,89% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.979,87 | €-20,13 | 4 | 4 | 25,00% | 0,18 | €-5,03 | 0,20% |
| TEST | Doge Ema 1H | Trend following EMA | €9.971,70 | €-13,78 | 2 | 2 | 50,00% | 0,75 | €-6,89 | 1,17% |
| TEST | Eth Ema 1H | Trend following EMA | €9.957,18 | €-54,90 | 1 | 1 | 0,00% | 0,00 | €-54,90 | 0,59% |
| TEST | Btc Ema 1H | Trend following EMA | €9.945,45 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,65% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.945,45 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,65% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.944,88 | €-55,12 | 1 | 1 | 0,00% | 0,00 | €-55,12 | 0,67% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.941,71 | €-54,90 | 1 | 1 | 0,00% | 0,00 | €-54,90 | 0,64% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.915,69 | €-71,19 | 3 | 3 | 33,33% | 0,35 | €-23,73 | 1,19% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.863,13 | €-111,57 | 16 | 16 | 25,00% | 0,57 | €-6,97 | 2,24% |
| TEST | Combo Adaptive MFE Trail | Combo Adaptive | €9.738,77 | €-257,88 | 11 | 11 | 18,18% | 0,14 | €-23,44 | 2,64% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07243 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €11,47 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 59,36013 | 60,81300 | 62,47190 | 78,85003 | 53,13657 | €313,25 | €939,76 | €49,26 | €-23,00 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,19982 | 0,23699 | 0,13559 | €136,26 | €408,77 | €49,05 | €-0,00 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 556,07119 | 555,47000 | 524,63715 | 373,49448 | 618,93927 | €293,97 | €881,92 | €49,85 | €-0,95 |
| Bilanciata 1H V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,02421 | 2,02421 | 1,97233 | 1,35960 | 2,12798 | €655,13 | €1.965,38 | €50,37 | €0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,37581 | 0,37581 | 0,40458 | 0,49921 | 0,31828 | €219,32 | €657,96 | €50,37 | €-0,00 |
| Bilanciata 1H V1 | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €143,84 | €431,52 | €50,35 | €-0,00 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,37613 | 0,37613 | 0,36189 | 0,25263 | 0,40460 | €442,89 | €1.328,68 | €50,30 | €0,00 |
| Bilanciata 1H V2 | LAB | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €139,69 | €419,08 | €48,90 | €-0,00 |
| Bilanciata 1H V2 | GRAM | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,49240 | 1,49240 | 1,53621 | 1,98241 | 1,40478 | €570,19 | €1.710,58 | €50,21 | €-0,00 |
| Bilanciata 1H V2 | ZEC | LONG | Confluenza trend V2 | 60m | 3,0x | 559,56189 | 555,47000 | 549,06713 | 375,83907 | 580,55140 | €896,22 | €2.688,65 | €50,43 | €-19,66 |
| Bilanciata 1H V2 | PEPE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.047,96 | €3.143,89 | €50,32 | €-1,89 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,07217 | 0,07243 | 0,07321 | 0,09586 | 0,07009 | €1.157,41 | €3.472,22 | €50,00 | €-12,67 |
| Bilanciata 1H V3 Filtered | AKE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00198 | 0,00181 | 0,00174 | 0,00133 | 0,00246 | €138,48 | €415,43 | €49,85 | €-35,97 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 559,56189 | 555,47000 | 549,06713 | 375,83907 | 580,55140 | €885,19 | €2.655,58 | €49,81 | €-19,42 |
| Bilanciata 1H V3 Filtered | BANK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,16778 | 0,18058 | 0,16778 | 0,11269 | 0,20805 | €138,11 | €414,33 | €0,00 | €31,60 |
| Rapida 1H V1 | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,18833 | 0,18833 | 0,20479 | 0,25016 | 0,16363 | €195,85 | €587,54 | €51,37 | €-0,00 |
| Rapida 1H V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,37292 | 0,37292 | 0,36188 | 0,25048 | 0,38949 | €580,83 | €1.742,48 | €51,60 | €0,00 |
| Rapida 1H V1 | GRAM | SHORT | Momentum / breakout | 60m | 3,0x | 1,49240 | 1,49240 | 1,52648 | 1,98241 | 1,44129 | €757,31 | €2.271,94 | €51,87 | €-0,00 |
| Rapida 1H V3 Filtered | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1868,12355 | 1867,43000 | 1847,20057 | 1254,75632 | 1899,50803 | €1.482,34 | €4.447,03 | €49,81 | €-1,65 |
| Rapida 1H V3 Filtered | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.332,11 | €3.996,34 | €49,51 | €-18,54 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07243 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-1,14 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 555,47000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €42,15 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 59,36013 | 60,81300 | 63,40544 | 88,74339 | 48,03325 | €367,70 | €735,40 | €50,12 | €-18,00 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00172 | 0,00181 | 0,00172 | 0,00087 | 0,00230 | €212,64 | €425,29 | €0,00 | €21,80 |
| Forza relativa 1H V1 | AAVE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H V1 | T | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H V1 | ALLO | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Forza relativa 1H V2 | LAB | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18833 | 0,18833 | 0,20950 | 0,28155 | 0,14176 | €222,78 | €445,56 | €50,08 | €-0,00 |
| Forza relativa 1H V2 | GRAM | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,47771 | 1,47771 | 1,52060 | 2,20918 | 1,38336 | €871,54 | €1.743,07 | €50,59 | €-0,00 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00198 | 0,00181 | 0,00174 | 0,00100 | 0,00250 | €210,83 | €421,66 | €50,60 | €-36,51 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.573,66 | €3.147,32 | €50,37 | €-1,89 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1868,12355 | 1867,43000 | 1838,23357 | 943,40239 | 1942,84849 | €1.585,47 | €3.170,93 | €50,73 | €-1,18 |
| Benchmark Donchian breakout 1H | BANK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,17592 | 0,18058 | 0,15481 | 0,08884 | 0,22869 | €213,04 | €426,09 | €51,13 | €11,30 |
| Benchmark Bollinger mean reversion 1H | LAB | LONG | Bollinger mean reversion | 60m | 2,0x | 0,18881 | 0,18881 | 0,17193 | 0,09535 | 0,21414 | €277,38 | €554,76 | €49,61 | €0,00 |
| Benchmark Bollinger mean reversion 1H | ETH | SHORT | Bollinger mean reversion | 60m | 2,0x | 1867,37645 | 1867,43000 | 1889,78497 | 2791,72779 | 1833,76367 | €1.999,85 | €3.999,71 | €48,00 | €-0,11 |
| Benchmark Bollinger mean reversion 1H | PEPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.974,65 | €3.949,29 | €50,31 | €9,87 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 59,78804 | 60,81300 | 61,40996 | 89,38312 | 56,21982 | €924,22 | €1.848,44 | €50,14 | €-31,69 |
| Scanner Top 5 Long 1H | NEAR | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,12798 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €625,48 | €1.250,97 | €51,81 | €0,00 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 556,25123 | 555,47000 | 543,83554 | 280,90687 | 581,08261 | €1.159,54 | €2.319,07 | €51,76 | €-3,26 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31828 | €324,92 | €649,84 | €49,75 | €-0,00 |
| Scanner Bottom 5 Short 1H | LAB | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,22091 | 0,22091 | 0,20335 | 0,33025 | 0,16789 | €209,34 | €418,67 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,07217 | 0,07243 | 0,07321 | 0,10789 | 0,07009 | €1.741,23 | €3.482,46 | €50,15 | €-12,71 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37613 | 0,37613 | 0,36189 | 0,18994 | 0,40745 | €677,81 | €1.355,62 | €51,32 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 556,25123 | 555,47000 | 543,83554 | 280,90687 | 583,56574 | €1.156,31 | €2.312,63 | €51,62 | €-3,25 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07215 | 0,07243 | 0,07330 | 0,10786 | 0,06926 | €1.551,38 | €3.102,75 | €49,64 | €-12,18 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,35567 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €50,24 | €0,00 |
| Combo Trend | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,08689 | 1,09454 | 1,10428 | 1,62490 | 1,04863 | €1.565,99 | €3.131,98 | €50,11 | €-22,04 |
| Combo Trend | HYPE | SHORT | Combo Trend | 60m | 2,0x | 59,78804 | 60,81300 | 61,40996 | 89,38312 | 56,21982 | €936,92 | €1.873,85 | €50,83 | €-32,12 |
| Combo Mean Reversion | LAB | LONG | Combo Mean Reversion | 60m | 2,0x | 0,18881 | 0,18881 | 0,17193 | 0,09535 | 0,21583 | €281,61 | €563,22 | €50,37 | €0,00 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40679 | €599,14 | €1.198,28 | €49,63 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,07215 | 0,07243 | 0,07319 | 0,10786 | 0,06986 | €1.763,29 | €3.526,57 | €50,78 | €-13,85 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 556,25123 | 555,47000 | 543,83554 | 280,90687 | 583,56574 | €1.125,40 | €2.250,79 | €50,24 | €-3,16 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €613,42 | €1.226,85 | €50,81 | €0,00 |
| Combo Adaptive | GRAM | SHORT | Combo Adaptive | 60m | 2,0x | 1,48181 | 1,48181 | 1,51561 | 2,21531 | 1,41422 | €1.129,35 | €2.258,70 | €51,51 | €-0,00 |
| Combo Adaptive | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1868,12355 | 1867,43000 | 1841,22257 | 943,40239 | 1921,92551 | €1.779,59 | €3.559,18 | €51,25 | €-1,32 |
| Combo Adaptive MFE Trail | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1868,12355 | 1867,43000 | 1841,22257 | 943,40239 | 1921,92551 | €1.710,41 | €3.420,83 | €49,26 | €-1,27 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1859,79188 | 1867,43000 | 1833,01088 | 1249,16022 | 1913,35389 | €1.151,05 | €3.453,16 | €49,73 | €14,18 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 1868,12355 | 1867,43000 | 1844,21157 | 1254,75632 | 1915,94751 | €1.302,08 | €3.906,25 | €50,00 | €-1,45 |
| Eth Bollinger 1H | ETH | SHORT | Bollinger mean reversion | 60m | 3,0x | 1867,37645 | 1867,43000 | 1889,78497 | 2480,49838 | 1833,76367 | €1.388,89 | €4.166,67 | €50,00 | €-0,12 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1868,12355 | 1867,43000 | 1841,22257 | 1254,75632 | 1921,92551 | €1.151,05 | €3.453,16 | €49,73 | €-1,28 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07216 | 0,07243 | 0,07320 | 0,09585 | 0,07008 | €1.155,81 | €3.467,44 | €49,93 | €-13,13 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive MFE Trail | BANK | LONG | 2026-07-19T12:08:30+00:00 | 0,17609 | €-0,08 | -0,00 | STOP |
| Rapida 1H V3 Filtered | BANK | LONG | 2026-07-19T12:08:30+00:00 | 0,17588 | €-0,70 | -0,01 | STOP |
| Rapida 1H V1 | BANK | LONG | 2026-07-19T12:08:30+00:00 | 0,17588 | €-0,71 | -0,01 | STOP |
| Rapida 1H V3 Filtered | ZEC | LONG | 2026-07-19T11:38:31+00:00 | 555,66913 | €-3,49 | -0,07 | STOP |
| Benchmark Donchian breakout 1H | BANK | LONG | 2026-07-19T11:23:29+00:00 | 0,18155 | €125,36 | 2,49 | TARGET |
| Combo Adaptive MFE Trail | ESPORTS | LONG | 2026-07-19T11:23:29+00:00 | 0,03808 | €-49,48 | -1,01 | STOP |
| Rapida 1H V3 Filtered | BANK | LONG | 2026-07-19T11:23:29+00:00 | 0,15304 | €45,53 | 0,92 | STOP_SAME_CANDLE_CONSERVATIVE |
| Rapida 1H V1 | ZEC | LONG | 2026-07-19T11:23:29+00:00 | 556,13998 | €-4,43 | -0,09 | STOP |
| Bilanciata 1H V3 Filtered | BANK | LONG | 2026-07-19T11:08:30+00:00 | 0,15346 | €61,45 | 1,24 | STOP |
| Forza relativa 1H V2 | ESPORTS | LONG | 2026-07-19T09:53:30+00:00 | 0,04191 | €-0,76 | -0,01 | STOP |
| Rapida 1H V3 Filtered | ESPORTS | LONG | 2026-07-19T09:53:30+00:00 | 0,04243 | €-50,28 | -1,01 | STOP |
| Bilanciata 1H V3 Filtered | ESPORTS | LONG | 2026-07-19T09:53:30+00:00 | 0,04224 | €-50,73 | -1,01 | STOP |

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
| MAIN | Principale 4H | 23/30 | 15/30 | 1,03 | 0,89 | 0,02R | €-3,37 | 4,26% | DIVERGENTE | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 5/30 | 4/30 | 0,32 | 0,30 | -0,55R | €-4,46 | 0,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 81/30 | 10/30 | 1,08 | 1,44 | 0,05R | €7,18 | 1,06% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 9/30 | 10/30 | 2,35 | 1,32 | 0,63R | €7,20 | 2,10% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 12/30 | 10/30 | 1,88 | 1,12 | 0,46R | €3,75 | 2,20% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 | 92/30 | 35/30 | 0,99 | 1,34 | -0,01R | €6,93 | 2,34% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 1/30 | 1/30 | 1,19 | 11,45 | 0,11R | €31,39 | 0,93% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered | 12/30 | 16/30 | 1,98 | 0,57 | 0,42R | €-6,97 | 2,24% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 21/30 | 9/30 | 1,36 | 1,60 | 0,25R | €17,53 | 2,08% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 17/30 | 10/30 | 0,93 | 1,34 | -0,04R | €7,48 | 2,06% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,55 | 0,65% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 1/30 | 1/30 | ∞ | ∞ | 1,37R | €68,69 | 0,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,12R | €-55,12 | 0,67% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,55 | 0,65% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive | 38/30 | 14/30 | 1,86 | 2,15 | 0,45R | €18,04 | 0,89% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive MFE Trail | 9/30 | 11/30 | 1,57 | 0,14 | 0,32R | €-23,44 | 2,64% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 6/30 | 4/30 | 2,98 | 4,42 | 0,67R | €44,07 | 0,59% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 25/30 | 10/30 | 1,92 | 1,21 | 0,50R | €5,53 | 1,69% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_TREND | Combo Trend | 29/30 | 8/30 | 1,46 | 2,07 | 0,28R | €21,33 | 1,48% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 0/30 | 1/30 | 0,00 | ∞ | 0,00R | €26,22 | 0,36% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 0/30 | 2/30 | 0,00 | 0,75 | 0,00R | €-6,89 | 1,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 15/30 | 10/30 | 0,84 | 2,00 | -0,13R | €21,60 | 1,98% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 35/30 | 4/30 | 1,22 | 1,28 | 0,14R | €7,56 | 1,10% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,90 | 0,64% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,26% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,18% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,90 | 0,59% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 1/30 | 3/30 | 0,00 | 0,35 | -1,10R | €-23,73 | 1,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 51/30 | 7/30 | 1,24 | 1,56 | 0,16R | €12,63 | 1,36% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 12/30 | 10/30 | 2,49 | 1,57 | 0,70R | €12,02 | 2,32% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 12/30 | 5/30 | 0,89 | 1,28 | -0,08R | €5,92 | 1,90% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 27/30 | 12/30 | 1,93 | 2,51 | 0,50R | €27,14 | 1,62% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 34/30 | 14/30 | 1,66 | 2,31 | 0,37R | €25,32 | 1,65% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 2/30 | 2/30 | 1,70 | 0,67 | 0,39R | €-9,23 | 0,89% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,13R | €-55,79 | 0,62% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,12R | €-4,49 | 0,43% | COERENTE − | RACCOLTA RESEARCH |
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
| BTC sotto filtro | 64365.1 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick**
- High **0.07258**; close **0.0725**; wick alta **0.0%**; volume **x0.57**

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

- Regime: **ALT_ROTATION_UP**
- Famiglia: **ALT_ROTATION**
- Confidenza: **77,20%**
- Volatilità: **LOW**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Le altcoin stanno sovraperformando BTC: mediana relativa +1.76%, 55% oltre +1%.
- BTC trend score: **3,00**; ADX: **22,85**; breadth sopra EMA50: **91,67%**
- Mediana alt vs BTC: **1,76%**; dispersione: **47,03%**

- Aperti in questo ciclo: **22**
- Chiusi in questo ciclo: **27**
- Posizioni research aperte: **178**
- Trade research chiusi: **581**
- Eventi di mercato indipendenti chiusi: **231**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **1714**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 11 | 23 | 23 | 34,78% | 1,03 | 0,02R | €4,07 |
| RSI_EXTREME_SHORT_15M | 0 | 5 | 5 | 20,00% | 0,32 | -0,55R | €-27,64 |
| Bilanciata 1H V1 | 16 | 81 | 81 | 37,04% | 1,08 | 0,05R | €42,83 |
| Bilanciata 1H V2 | 8 | 9 | 9 | 55,56% | 2,35 | 0,63R | €57,05 |
| Bilanciata 1H V3 Filtered | 6 | 12 | 12 | 50,00% | 1,88 | 0,46R | €55,76 |
| Rapida 1H V1 | 9 | 92 | 92 | 41,30% | 0,99 | -0,01R | €-7,36 |
| Rapida 1H V2 | 0 | 2 | 1 | 50,00% | 1,19 | 0,11R | €2,14 |
| Rapida 1H V3 Filtered | 6 | 12 | 12 | 58,33% | 1,98 | 0,42R | €50,78 |
| SHADOW_4H_WIDE | 17 | 21 | 21 | 33,33% | 1,36 | 0,25R | €51,60 |
| SHADOW_BOLLINGER_MR_1H | 3 | 17 | 17 | 41,18% | 0,93 | -0,04R | €-7,09 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_EMA_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_ADAPTIVE | 12 | 38 | 38 | 50,00% | 1,86 | 0,45R | €172,11 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 5 | 9 | 9 | 44,44% | 1,57 | 0,32R | €28,80 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 6 | 6 | 66,67% | 2,98 | 0,67R | €40,29 |
| SHADOW_COMBO_SCANNER | 6 | 25 | 25 | 48,00% | 1,92 | 0,50R | €124,96 |
| SHADOW_COMBO_TREND | 11 | 29 | 29 | 41,38% | 1,46 | 0,28R | €82,51 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_EMA_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | 8 | 15 | 15 | 26,67% | 0,84 | -0,13R | €-19,06 |
| SHADOW_EMA_TREND_1H | 13 | 35 | 35 | 37,14% | 1,22 | 0,14R | €50,60 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_GLOBAL_PURE | 1 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| Forza relativa 1H V1 | 13 | 51 | 51 | 37,25% | 1,24 | 0,16R | €79,73 |
| Forza relativa 1H V2 | 5 | 13 | 12 | 53,85% | 2,49 | 0,70R | €91,49 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 8 | 12 | 12 | 33,33% | 0,89 | -0,08R | €-9,16 |
| SHADOW_SCANNER_TOP5_BTC | 6 | 27 | 27 | 48,15% | 1,93 | 0,50R | €136,14 |
| SHADOW_SCANNER_TOP5_LONG | 8 | 34 | 34 | 47,06% | 1,66 | 0,37R | €126,27 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_SOL_EMA_1H | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| MAIN | RANGE | 1 | 13 | 13 | 30,77% | 0,86 | -0,10R | €-13,29 |
| MAIN | TRANSITION | 5 | 3 | 3 | 33,33% | 0,97 | -0,02R | €-0,54 |
| MAIN | TREND_UP | 2 | 7 | 7 | 42,86% | 1,43 | 0,26R | €17,90 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 3 | 3 | 33,33% | 0,50 | -0,42R | €-12,61 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 1 | 10 | 10 | 50,00% | 1,83 | 0,44R | €44,06 |
| Bilanciata 1H V1 | RANGE | 5 | 23 | 23 | 34,78% | 0,98 | -0,02R | €-3,57 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 9 | 9 | 0,00% | 0,00 | -1,08R | €-97,25 |
| Bilanciata 1H V1 | TRANSITION | 5 | 18 | 18 | 44,44% | 1,46 | 0,27R | €49,04 |
| Bilanciata 1H V1 | TREND_UP | 5 | 21 | 21 | 42,86% | 1,40 | 0,24R | €50,54 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Bilanciata 1H V2 | RANGE | 3 | 3 | 3 | 66,67% | 3,58 | 0,95R | €28,62 |
| Bilanciata 1H V2 | TRANSITION | 3 | 6 | 6 | 50,00% | 1,91 | 0,47R | €28,43 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Bilanciata 1H V3 Filtered | TRANSITION | 1 | 5 | 5 | 40,00% | 1,24 | 0,15R | €7,67 |
| Bilanciata 1H V3 Filtered | TREND_UP | 4 | 7 | 7 | 57,14% | 2,53 | 0,69R | €48,09 |
| Rapida 1H V1 | ALT_ROTATION_UP | 1 | 7 | 7 | 42,86% | 1,05 | 0,03R | €1,98 |
| Rapida 1H V1 | RANGE | 2 | 33 | 33 | 42,42% | 1,05 | 0,03R | €8,73 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 10 | 10 | 0,00% | 0,00 | -1,10R | €-109,76 |
| Rapida 1H V1 | TRANSITION | 2 | 17 | 17 | 58,82% | 2,27 | 0,48R | €81,49 |
| Rapida 1H V1 | TREND_UP | 4 | 25 | 25 | 44,00% | 1,07 | 0,04R | €10,21 |
| Rapida 1H V2 | RANGE | 0 | 2 | 1 | 50,00% | 1,19 | 0,11R | €2,14 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Rapida 1H V3 Filtered | TRANSITION | 1 | 3 | 3 | 66,67% | 2,93 | 0,65R | €19,60 |
| Rapida 1H V3 Filtered | TREND_UP | 4 | 9 | 9 | 55,56% | 1,75 | 0,35R | €31,18 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | RANGE | 6 | 11 | 11 | 27,27% | 1,02 | 0,01R | €1,48 |
| SHADOW_4H_WIDE | TRANSITION | 6 | 4 | 4 | 25,00% | 0,92 | -0,06R | €-2,53 |
| SHADOW_4H_WIDE | TREND_UP | 3 | 6 | 6 | 50,00% | 2,70 | 0,88R | €52,66 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,15 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,98 | -0,01R | €-0,83 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 2 | 6 | 6 | 50,00% | 1,31 | 0,17R | €10,03 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 5 | 7 | 7 | 42,86% | 1,34 | 0,21R | €14,90 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 3 | 13 | 13 | 53,85% | 2,19 | 0,57R | €74,23 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 3 | 17 | 17 | 52,94% | 2,11 | 0,55R | €93,11 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 1 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 4 | 8 | 8 | 50,00% | 1,96 | 0,49R | €38,93 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 4 | 4 | 75,00% | 4,46 | 0,88R | €35,25 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 2 | 2 | 50,00% | 1,50 | 0,25R | €5,04 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_COMBO_SCANNER | TRANSITION | 2 | 10 | 10 | 40,00% | 1,40 | 0,25R | €25,03 |
| SHADOW_COMBO_SCANNER | TREND_UP | 2 | 13 | 13 | 46,15% | 1,76 | 0,43R | €56,20 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_COMBO_TREND | RANGE | 3 | 5 | 5 | 20,00% | 0,51 | -0,42R | €-20,81 |
| SHADOW_COMBO_TREND | TRANSITION | 3 | 12 | 12 | 50,00% | 2,09 | 0,56R | €67,72 |
| SHADOW_COMBO_TREND | TREND_UP | 4 | 11 | 11 | 36,36% | 1,19 | 0,12R | €13,74 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_EMA_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | RANGE | 3 | 5 | 5 | 20,00% | 0,57 | -0,37R | €-18,56 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 4 | 4 | 25,00% | 0,78 | -0,17R | €-6,95 |
| SHADOW_DONCHIAN_1H | TREND_UP | 3 | 6 | 6 | 33,33% | 1,15 | 0,11R | €6,44 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_EMA_TREND_1H | RANGE | 4 | 6 | 6 | 16,67% | 0,41 | -0,52R | €-30,95 |
| SHADOW_EMA_TREND_1H | TRANSITION | 3 | 12 | 12 | 50,00% | 2,09 | 0,56R | €67,70 |
| SHADOW_EMA_TREND_1H | TREND_UP | 5 | 16 | 16 | 31,25% | 0,93 | -0,05R | €-8,03 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 1 | 9 | 9 | 33,33% | 1,02 | 0,02R | €1,39 |
| Forza relativa 1H V1 | RANGE | 4 | 16 | 16 | 25,00% | 0,69 | -0,24R | €-38,67 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| Forza relativa 1H V1 | TRANSITION | 1 | 11 | 11 | 54,55% | 2,55 | 0,72R | €78,82 |
| Forza relativa 1H V1 | TREND_UP | 7 | 13 | 13 | 46,15% | 1,80 | 0,45R | €58,51 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V2 | RANGE | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,72 |
| Forza relativa 1H V2 | TRANSITION | 2 | 6 | 6 | 50,00% | 2,10 | 0,57R | €34,43 |
| Forza relativa 1H V2 | TREND_UP | 1 | 5 | 4 | 60,00% | 3,24 | 0,91R | €45,33 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 2 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-54,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 4 | 5 | 5 | 60,00% | 2,60 | 0,70R | €35,18 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 1 | 2 | 2 | 50,00% | 2,08 | 0,57R | €11,35 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 2 | 3 | 3 | 100,00% | ∞ | 2,14R | €64,28 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 1 | 10 | 10 | 40,00% | 1,40 | 0,25R | €25,03 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 12 | 12 | 41,67% | 1,48 | 0,30R | €35,49 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,06R | €-21,24 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 2 | 4 | 4 | 100,00% | ∞ | 1,95R | €78,15 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 1 | 10 | 10 | 40,00% | 1,27 | 0,17R | €17,03 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 4 | 18 | 18 | 44,44% | 1,49 | 0,29R | €52,34 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
