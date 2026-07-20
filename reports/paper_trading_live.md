# Paper trading automatico KuCoin

Generato: 2026-07-20T04:08:35+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-20T04:08:24+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-20T04:08:24+00:00 | 2026-07-20T04:08:24+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-20T03:45:00+00:00 | 2026-07-20T03:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-20T03:00:00+00:00 | 2026-07-20T03:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-20T00:00:00+00:00 | 2026-07-20T00:00:00+00:00 | 8,5 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | PEPE | 240m | LONG | 8,01 | 6,00 | 0,00 | RISK_GATE | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | RISK_GATE | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | HYPE | 240m | SHORT | -7,75 | 6,00 | 0,00 | RISK_GATE | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | AKE | 240m | LONG | 5,75 | 6,00 | 0,25 | BELOW_SCORE | 8,5 min | D: n/a | W: n/a | peso 0 | Punteggio +5.75; soglia ±6.00; mancano 0.25 punti. |
| Principale 4H | ETH | 240m | LONG | 5,47 | 6,00 | 0,53 | BELOW_SCORE | 8,5 min | D: n/a | W: n/a | peso 0 | Punteggio +5.47; soglia ±6.00; mancano 0.53 punti. |
| Principale 4H | BTC | 240m | LONG | 4,75 | 6,00 | 1,25 | BELOW_SCORE | 8,5 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Punteggio +4.75; soglia ±6.00; mancano 1.25 punti. |
| Ampia 4H | PEPE | 240m | LONG | 8,01 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Ampia 4H | BANK | 240m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive MFE Trail | PEPE | 60m | LONG | 7,07 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Bottom 5 Short 1H | HYPE | 60m | SHORT | -5,96 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Ampia 4H | AKE | 240m | LONG | 5,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Ampia 4H | ETH | 240m | LONG | 5,47 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | PEPE | 60m | LONG | 7,07 | 5,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | PEPE | 60m | LONG | 7,07 | 5,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Bilanciata 1H V2 | ETH | 60m | LONG | 6,27 | 5,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 | ETH | 60m | LONG | 6,27 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.94%. |
| Rapida 1H V2 | ETH | 60m | LONG | 6,27 | 5,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Forza relativa 1H V1 | ETH | 60m | LONG | 6,27 | 4,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=+0.09%. |
| Bilanciata 1H V2 | HYPE | 60m | SHORT | -5,96 | 5,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 | HYPE | 60m | SHORT | -5,96 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.92%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.908,26 | -0,92% | €-91,74 | €3.000,00 | -3,06% | 4 | 15 | 33,33% | 0,89 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 15 | 184 | CAMPIONE INSUFFICIENTE | 30 (mancano 15) |

- Trade del Principale 4H chiusi: **15**; win rate **33,33%**; profit factor **0,89**.
- Expectancy: **€-3,37** per trade; P&L netto: **€-50,49**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.908,26 | €1.317,93 | €3.953,78 | €197,45 | €-40,67 |
| TEST | Forza relativa 1H V2 | 3 | €10.381,65 | €2.242,62 | €4.485,24 | €152,64 | €-11,12 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.343,68 | €2.024,87 | €4.049,74 | €51,81 | €73,88 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.334,86 | €1.866,89 | €3.733,78 | €101,31 | €66,37 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.294,97 | €3.169,51 | €6.339,03 | €101,94 | €65,43 |
| TEST | Combo Adaptive | 3 | €10.259,10 | €3.522,36 | €7.044,73 | €153,58 | €11,18 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.221,13 | €3.232,64 | €9.697,93 | €201,84 | €0,44 |
| TEST | Bilanciata 1H V1 | 4 | €10.213,34 | €2.535,42 | €7.606,25 | €150,97 | €3,01 |
| TEST | Rapida 1H V1 | 4 | €10.155,02 | €2.761,39 | €8.284,16 | €202,97 | €8,70 |
| TEST | Ampia 4H | 4 | €10.139,08 | €1.846,89 | €3.693,78 | €200,81 | €0,16 |
| TEST | Combo Mean Reversion | 1 | €10.120,96 | €281,61 | €563,22 | €50,37 | €0,00 |
| TEST | Forza relativa 1H V1 | 4 | €10.100,89 | €2.679,07 | €5.358,15 | €100,88 | €45,73 |
| TEST | Benchmark Bollinger mean reversion 1H | 3 | €10.090,89 | €3.609,24 | €7.218,48 | €147,84 | €24,50 |
| TEST | Btc Bollinger 1H | 0 | €10.068,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €10.062,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 3 | €10.061,79 | €2.096,20 | €4.192,40 | €100,32 | €51,84 |
| TEST | Combo Scanner | 3 | €10.044,33 | €2.570,72 | €5.141,43 | €100,41 | €43,93 |
| TEST | Doge Donchian 1H | 0 | €10.026,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €10.009,52 | €1.302,08 | €3.906,25 | €50,00 | €12,27 |
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
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.995,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €9.995,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.990,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 2 | €9.985,74 | €709,89 | €2.129,66 | €99,11 | €0,00 |
| TEST | Eth Bollinger 1H | 1 | €9.983,18 | €1.388,89 | €4.166,67 | €50,00 | €-14,76 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.982,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.981,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.979,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €9.965,66 | €1.155,81 | €3.467,44 | €49,93 | €-19,86 |
| TEST | Eth Adaptive 1H | 1 | €9.953,51 | €1.151,05 | €3.453,16 | €49,73 | €10,84 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.952,69 | €3.459,61 | €6.919,22 | €99,92 | €-20,07 |
| TEST | Eth Ema 1H | 1 | €9.945,67 | €1.152,05 | €3.456,15 | €49,77 | €-5,98 |
| TEST | Btc Adaptive 1H | 0 | €9.945,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.944,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.939,46 | €1.151,09 | €3.453,28 | €49,73 | €-3,92 |
| TEST | Rapida 1H V3 Filtered | 3 | €9.927,82 | €2.015,45 | €6.046,35 | €149,18 | €-15,25 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.927,60 | €2.193,79 | €4.387,58 | €149,10 | €4,47 |
| TEST | Global Confluence puro 1H | 1 | €9.910,29 | €1.551,38 | €3.102,75 | €49,64 | €-18,21 |
| TEST | Combo Adaptive MFE Trail | 3 | €9.783,93 | €4.167,67 | €8.335,35 | €146,59 | €-3,86 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.908,26 | €-50,49 | 15 | 15 | 33,33% | 0,89 | €-3,37 | 4,26% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.381,65 | €395,30 | 14 | 14 | 42,86% | 2,51 | €28,24 | 2,32% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.343,68 | €272,29 | 17 | 17 | 47,06% | 1,77 | €16,02 | 2,19% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.334,86 | €270,73 | 13 | 13 | 46,15% | 2,00 | €20,83 | 1,62% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.294,97 | €234,28 | 11 | 11 | 54,55% | 2,08 | €21,30 | 1,98% |
| TEST | Combo Adaptive | Combo Adaptive | €10.259,10 | €252,59 | 14 | 14 | 42,86% | 2,15 | €18,04 | 1,01% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.221,13 | €224,87 | 16 | 16 | 43,75% | 1,54 | €14,05 | 2,20% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.213,34 | €214,36 | 15 | 15 | 46,67% | 1,97 | €14,29 | 1,12% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.155,02 | €151,19 | 39 | 39 | 41,03% | 1,17 | €3,88 | 2,83% |
| TEST | Ampia 4H | Confluenza trend | €10.139,08 | €139,54 | 11 | 11 | 27,27% | 1,50 | €12,69 | 2,08% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.120,96 | €121,64 | 5 | 5 | 60,00% | 2,15 | €24,33 | 0,59% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €10.100,89 | €58,37 | 11 | 11 | 45,45% | 1,31 | €5,31 | 1,84% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.090,89 | €70,65 | 11 | 11 | 45,45% | 1,32 | €6,42 | 2,06% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.068,69 | €68,69 | 1 | 1 | 100,00% | ∞ | €68,69 | 0,31% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.062,78 | €62,78 | 2 | 1 | 50,00% | 11,45 | €31,39 | 0,93% |
| TEST | Combo Trend | Combo Trend | €10.061,79 | €12,52 | 11 | 11 | 36,36% | 1,04 | €1,14 | 1,99% |
| TEST | Combo Scanner | Combo Scanner | €10.044,33 | €1,79 | 11 | 11 | 36,36% | 1,01 | €0,16 | 1,69% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.026,22 | €26,22 | 1 | 1 | 100,00% | ∞ | €26,22 | 0,36% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €10.009,52 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,38% |
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
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.995,97 | €-4,03 | 4 | 4 | 25,00% | 0,18 | €-1,01 | 0,04% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.995,51 | €-4,49 | 1 | 1 | 0,00% | 0,00 | €-4,49 | 0,43% |
| TEST | Sol Ema 1H | Trend following EMA | €9.990,84 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 0,87% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.985,74 | €-13,16 | 15 | 13 | 46,67% | 0,97 | €-0,88 | 2,10% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.983,18 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,51% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.982,18 | €-17,82 | 4 | 4 | 25,00% | 0,30 | €-4,46 | 0,18% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.981,55 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 0,89% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.979,87 | €-20,13 | 4 | 4 | 25,00% | 0,18 | €-5,03 | 0,20% |
| TEST | Doge Ema 1H | Trend following EMA | €9.965,66 | €-13,78 | 2 | 2 | 50,00% | 0,75 | €-6,89 | 1,17% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.953,51 | €-54,90 | 1 | 1 | 0,00% | 0,00 | €-54,90 | 0,77% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.952,69 | €-25,03 | 7 | 7 | 42,86% | 0,84 | €-3,58 | 2,43% |
| TEST | Eth Ema 1H | Trend following EMA | €9.945,67 | €-46,28 | 2 | 2 | 50,00% | 0,16 | €-23,14 | 0,61% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.945,45 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,65% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.944,88 | €-55,12 | 1 | 1 | 0,00% | 0,00 | €-55,12 | 0,67% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Btc Ema 1H | Trend following EMA | €9.939,46 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,71% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.927,82 | €-53,30 | 25 | 25 | 32,00% | 0,89 | €-2,13 | 2,24% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.927,60 | €-74,23 | 6 | 6 | 33,33% | 0,65 | €-12,37 | 1,45% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.910,29 | €-71,19 | 3 | 3 | 33,33% | 0,35 | €-23,73 | 1,19% |
| TEST | Combo Adaptive MFE Trail | Combo Adaptive | €9.783,93 | €-207,55 | 15 | 15 | 26,67% | 0,31 | €-13,84 | 2,87% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07257 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €8,16 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 59,36013 | 60,30900 | 62,47190 | 78,85003 | 53,13657 | €313,25 | €939,76 | €49,26 | €-15,02 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,19982 | 0,23699 | 0,13559 | €136,26 | €408,77 | €49,05 | €-0,00 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 556,07119 | 534,75000 | 524,63715 | 373,49448 | 618,93927 | €293,97 | €881,92 | €49,85 | €-33,82 |
| Bilanciata 1H V1 | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €143,84 | €431,52 | €50,35 | €-0,00 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,37613 | 0,37613 | 0,36189 | 0,25263 | 0,40460 | €442,89 | €1.328,68 | €50,30 | €0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,07253 | 0,07257 | 0,07357 | 0,09634 | 0,07044 | €1.164,82 | €3.494,46 | €50,32 | €-2,10 |
| Bilanciata 1H V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €783,86 | €2.351,59 | €0,00 | €5,11 |
| Bilanciata 1H V2 | LAB | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €139,69 | €419,08 | €48,90 | €-0,00 |
| Bilanciata 1H V2 | GRAM | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,49240 | 1,49240 | 1,53621 | 1,98241 | 1,40478 | €570,19 | €1.710,58 | €50,21 | €-0,00 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,07217 | 0,07257 | 0,07321 | 0,09586 | 0,07009 | €1.157,41 | €3.472,22 | €50,00 | €-19,41 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1867,19336 | 1873,99000 | 1840,30578 | 1254,13154 | 1920,96853 | €1.152,16 | €3.456,47 | €49,77 | €12,58 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €780,89 | €2.342,68 | €50,88 | €-6,57 |
| Bilanciata 1H V3 Filtered | BANK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,24392 | 0,25183 | 0,21465 | 0,16383 | 0,30246 | €142,18 | €426,55 | €51,19 | €13,83 |
| Rapida 1H V1 | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,18833 | 0,18833 | 0,20479 | 0,25016 | 0,16363 | €195,85 | €587,54 | €51,37 | €-0,00 |
| Rapida 1H V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,37292 | 0,37292 | 0,36188 | 0,25048 | 0,38949 | €580,83 | €1.742,48 | €51,60 | €0,00 |
| Rapida 1H V1 | GRAM | SHORT | Momentum / breakout | 60m | 3,0x | 1,49240 | 1,49240 | 1,52648 | 1,98241 | 1,44129 | €757,31 | €2.271,94 | €51,87 | €-0,00 |
| Rapida 1H V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 60,45191 | 60,30900 | 61,24207 | 80,30028 | 59,26667 | €1.227,40 | €3.682,20 | €48,13 | €8,70 |
| Rapida 1H V3 Filtered | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €941,89 | €2.825,68 | €49,73 | €-42,13 |
| Rapida 1H V3 Filtered | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24392 | 0,25183 | 0,21465 | 0,16383 | 0,28782 | €138,12 | €414,35 | €49,72 | €13,44 |
| Rapida 1H V3 Filtered | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 537,32251 | 534,75000 | 546,84245 | 713,74341 | 523,04261 | €935,44 | €2.806,32 | €49,72 | €13,44 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07257 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-3,65 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 534,75000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €15,77 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 59,36013 | 60,30900 | 63,40544 | 88,74339 | 48,03325 | €367,70 | €735,40 | €50,12 | €-11,76 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €-0,20 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H V1 | ALLO | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Forza relativa 1H V1 | PEPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.157,54 | €2.315,07 | €0,00 | €7,22 |
| Forza relativa 1H V1 | BANK | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,23050 | 0,25183 | 0,23050 | 0,11640 | 0,29135 | €208,05 | €416,10 | €0,00 | €38,51 |
| Forza relativa 1H V2 | LAB | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18833 | 0,18833 | 0,20950 | 0,28155 | 0,14176 | €222,78 | €445,56 | €50,08 | €-0,00 |
| Forza relativa 1H V2 | GRAM | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,47771 | 1,47771 | 1,52060 | 2,20918 | 1,38336 | €871,54 | €1.743,07 | €50,59 | €-0,00 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.148,31 | €2.296,61 | €51,97 | €-11,12 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1868,12355 | 1873,99000 | 1838,23357 | 943,40239 | 1942,84849 | €1.585,47 | €3.170,93 | €50,73 | €9,96 |
| Benchmark Donchian breakout 1H | BANK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,22677 | 0,25183 | 0,22677 | 0,11452 | 0,29479 | €213,00 | €426,01 | €0,00 | €47,09 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 60,49390 | 60,30900 | 61,62348 | 90,43838 | 57,66993 | €1.371,04 | €2.742,09 | €51,20 | €8,38 |
| Benchmark Bollinger mean reversion 1H | LAB | LONG | Bollinger mean reversion | 60m | 2,0x | 0,18881 | 0,18881 | 0,17193 | 0,09535 | 0,21414 | €277,38 | €554,76 | €49,61 | €0,00 |
| Benchmark Bollinger mean reversion 1H | ETH | SHORT | Bollinger mean reversion | 60m | 2,0x | 1867,37645 | 1873,99000 | 1889,78497 | 2791,72779 | 1833,76367 | €1.999,85 | €3.999,71 | €48,00 | €-14,17 |
| Benchmark Bollinger mean reversion 1H | PEPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.332,01 | €2.664,02 | €50,24 | €38,67 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Benchmark trend following EMA 1H | PEPE | LONG | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.028,07 | €2.056,13 | €49,62 | €4,47 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €625,48 | €1.250,97 | €51,81 | €0,00 |
| Scanner Top 5 Long 1H | BANK | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,21801 | 0,25183 | 0,21801 | 0,11010 | 0,27034 | €214,35 | €428,71 | €0,00 | €66,50 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.185,03 | €2.370,06 | €0,00 | €7,39 |
| Scanner Bottom 5 Short 1H | LAB | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,22091 | 0,22091 | 0,20335 | 0,33025 | 0,16789 | €209,34 | €418,67 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,07217 | 0,07257 | 0,07321 | 0,10789 | 0,07009 | €1.741,23 | €3.482,46 | €50,15 | €-19,46 |
| Scanner Bottom 5 Short 1H | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 60,29694 | 60,30900 | 61,29138 | 90,14392 | 58,30805 | €1.509,04 | €3.018,08 | €49,78 | €-0,60 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37613 | 0,37613 | 0,36189 | 0,18994 | 0,40745 | €677,81 | €1.355,62 | €51,32 | €0,00 |
| Scanner Top 5 + forza BTC 1H | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,21801 | 0,25183 | 0,21801 | 0,11010 | 0,27557 | €213,93 | €427,86 | €0,00 | €66,37 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07215 | 0,07257 | 0,07330 | 0,10786 | 0,06926 | €1.551,38 | €3.102,75 | €49,64 | €-18,21 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,35567 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €50,24 | €0,00 |
| Combo Trend | BANK | LONG | Combo Trend | 60m | 2,0x | 0,22714 | 0,25183 | 0,22714 | 0,11470 | 0,28710 | €209,25 | €418,49 | €0,00 | €45,50 |
| Combo Trend | HYPE | SHORT | Combo Trend | 60m | 2,0x | 60,45191 | 60,30900 | 61,58071 | 90,37560 | 57,96854 | €1.341,10 | €2.682,20 | €50,08 | €6,34 |
| Combo Mean Reversion | LAB | LONG | Combo Mean Reversion | 60m | 2,0x | 0,18881 | 0,18881 | 0,17193 | 0,09535 | 0,21583 | €281,61 | €563,22 | €50,37 | €0,00 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40679 | €599,14 | €1.198,28 | €49,63 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,07215 | 0,07257 | 0,07319 | 0,10786 | 0,06986 | €1.763,29 | €3.526,57 | €50,78 | €-20,69 |
| Combo Scanner | BANK | LONG | Combo Scanner | 60m | 2,0x | 0,21801 | 0,25183 | 0,21801 | 0,11010 | 0,27557 | €208,29 | €416,59 | €0,00 | €64,62 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €613,42 | €1.226,85 | €50,81 | €0,00 |
| Combo Adaptive | GRAM | SHORT | Combo Adaptive | 60m | 2,0x | 1,48181 | 1,48181 | 1,51561 | 2,21531 | 1,41422 | €1.129,35 | €2.258,70 | €51,51 | €-0,00 |
| Combo Adaptive | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1868,12355 | 1873,99000 | 1841,22257 | 943,40239 | 1921,92551 | €1.779,59 | €3.559,18 | €51,25 | €11,18 |
| Combo Adaptive MFE Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07231 | 0,07257 | 0,07335 | 0,10810 | 0,07022 | €1.693,88 | €3.387,77 | €48,78 | €-12,34 |
| Combo Adaptive MFE Trail | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 60,49390 | 60,30900 | 61,51053 | 90,43838 | 58,46064 | €1.454,10 | €2.908,20 | €48,87 | €8,89 |
| Combo Adaptive MFE Trail | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.019,69 | €2.039,38 | €48,93 | €-0,41 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 64774,99241 | 64701,50000 | 63842,23252 | 43507,20323 | 66640,51219 | €1.151,09 | €3.453,28 | €49,73 | €-3,92 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1877,23537 | 1873,99000 | 1850,20318 | 1260,87642 | 1931,29975 | €1.152,05 | €3.456,15 | €49,77 | €-5,98 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 1868,12355 | 1873,99000 | 1844,21157 | 1254,75632 | 1915,94751 | €1.302,08 | €3.906,25 | €50,00 | €12,27 |
| Eth Bollinger 1H | ETH | SHORT | Bollinger mean reversion | 60m | 3,0x | 1867,37645 | 1873,99000 | 1889,78497 | 2480,49838 | 1833,76367 | €1.388,89 | €4.166,67 | €50,00 | €-14,76 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1868,12355 | 1873,99000 | 1841,22257 | 1254,75632 | 1921,92551 | €1.151,05 | €3.453,16 | €49,73 | €10,84 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07216 | 0,07257 | 0,07320 | 0,09585 | 0,07008 | €1.155,81 | €3.467,44 | €49,93 | €-19,86 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Mean Reversion | ZEC | LONG | 2026-07-20T03:38:29+00:00 | 532,81430 | €-54,64 | -1,07 | STOP |
| Combo Adaptive MFE Trail | PEPE | LONG | 2026-07-20T03:38:29+00:00 | 0,00000 | €-0,45 | -0,01 | STOP |
| Forza relativa 1H V2 | PEPE | LONG | 2026-07-20T03:23:29+00:00 | 0,00000 | €106,02 | 2,10 | TARGET |
| Forza relativa 1H V2 | BANK | LONG | 2026-07-20T02:53:29+00:00 | 0,24704 | €110,09 | 2,17 | TARGET |
| Rapida 1H V3 Filtered | BANK | LONG | 2026-07-20T02:53:29+00:00 | 0,26753 | €74,28 | 1,49 | TARGET |
| Bilanciata 1H V3 Filtered | BANK | LONG | 2026-07-20T02:53:29+00:00 | 0,24294 | €98,56 | 1,97 | TARGET |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | 2026-07-20T02:38:29+00:00 | 0,02544 | €-53,44 | -1,07 | STOP_STRESS_SLIPPAGE |
| Rapida 1H V3 Filtered | ESPORTS | SHORT | 2026-07-20T02:38:29+00:00 | 0,02544 | €-53,35 | -1,07 | STOP_STRESS_SLIPPAGE |
| Benchmark trend following EMA 1H | ESPORTS | SHORT | 2026-07-20T02:23:30+00:00 | 0,02519 | €-52,17 | -1,05 | STOP_STRESS_SLIPPAGE |
| Combo Trend | ESPORTS | SHORT | 2026-07-20T02:23:30+00:00 | 0,02519 | €-52,78 | -1,05 | STOP_STRESS_SLIPPAGE |
| Rapida 1H V1 | ESPORTS | SHORT | 2026-07-20T02:23:30+00:00 | 0,02519 | €-51,41 | -1,05 | STOP_STRESS_SLIPPAGE |
| Bilanciata 1H V1 | ESPORTS | SHORT | 2026-07-20T02:23:30+00:00 | 0,02519 | €-53,77 | -1,05 | STOP_STRESS_SLIPPAGE |

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
| MAIN | Principale 4H | 27/30 | 15/30 | 0,81 | 0,89 | -0,14R | €-3,37 | 4,26% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 5/30 | 4/30 | 0,32 | 0,30 | -0,55R | €-4,46 | 0,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 95/30 | 15/30 | 1,11 | 1,97 | 0,07R | €14,29 | 1,12% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 13/30 | 13/30 | 1,85 | 0,97 | 0,45R | €-0,88 | 2,10% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 20/30 | 16/30 | 1,88 | 1,54 | 0,46R | €14,05 | 2,20% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 | 102/30 | 39/30 | 1,02 | 1,17 | 0,01R | €3,88 | 2,83% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 1/30 | 1/30 | 1,19 | 11,45 | 0,11R | €31,39 | 0,93% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered | 22/30 | 25/30 | 2,03 | 0,89 | 0,44R | €-2,13 | 2,24% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 24/30 | 11/30 | 1,12 | 1,50 | 0,09R | €12,69 | 2,08% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 20/30 | 11/30 | 0,72 | 1,32 | -0,20R | €6,42 | 2,06% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,55 | 0,65% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 1/30 | 1/30 | ∞ | ∞ | 1,37R | €68,69 | 0,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,12R | €-55,12 | 0,67% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,55 | 0,71% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive | 47/30 | 14/30 | 1,78 | 2,15 | 0,42R | €18,04 | 1,01% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive MFE Trail | 17/30 | 15/30 | 2,17 | 0,31 | 0,56R | €-13,84 | 2,87% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 7/30 | 5/30 | 1,94 | 2,15 | 0,42R | €24,33 | 0,59% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 32/30 | 11/30 | 2,08 | 1,01 | 0,56R | €0,16 | 1,69% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_TREND | Combo Trend | 38/30 | 11/30 | 1,35 | 1,04 | 0,22R | €1,14 | 1,99% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 0/30 | 1/30 | 0,00 | ∞ | 0,00R | €26,22 | 0,36% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 0/30 | 2/30 | 0,00 | 0,75 | 0,00R | €-6,89 | 1,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 19/30 | 11/30 | 0,82 | 2,08 | -0,14R | €21,30 | 1,98% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 44/30 | 6/30 | 1,18 | 0,65 | 0,12R | €-12,37 | 1,45% | DIVERGENTE | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,90 | 0,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 1/30 | 0/30 | 0,00 | 0,00 | -1,13R | €0,00 | 0,51% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,38% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 1/30 | 2/30 | 0,00 | 0,16 | -1,11R | €-23,14 | 0,61% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 1/30 | 3/30 | 0,00 | 0,35 | -1,10R | €-23,73 | 1,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 60/30 | 11/30 | 1,30 | 1,31 | 0,19R | €5,31 | 1,84% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 17/30 | 14/30 | 2,65 | 2,51 | 0,75R | €28,24 | 2,32% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 15/30 | 7/30 | 0,72 | 0,84 | -0,20R | €-3,58 | 2,43% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 34/30 | 13/30 | 2,08 | 2,00 | 0,56R | €20,83 | 1,62% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 44/30 | 17/30 | 1,78 | 1,77 | 0,41R | €16,02 | 2,19% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
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
- Prezzo DOGE: **0.07257**
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
| BTC sotto filtro | 64701.5 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick**
- High **0.07276**; close **0.0727**; wick alta **11.8%**; volume **x0.20**

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

- Regime: **TREND_UP_HIGH_VOL**
- Famiglia: **TREND_UP**
- Confidenza: **71,00%**
- Volatilità: **HIGH**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +3.0, 67% sopra EMA50, ADX 23.4.
- BTC trend score: **3,00**; ADX: **23,39**; breadth sopra EMA50: **66,67%**
- Mediana alt vs BTC: **0,18%**; dispersione: **37,68%**

- Aperti in questo ciclo: **7**
- Chiusi in questo ciclo: **11**
- Posizioni research aperte: **148**
- Trade research chiusi: **720**
- Eventi di mercato indipendenti chiusi: **278**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **2087**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 8 | 27 | 27 | 29,63% | 0,81 | -0,14R | €-36,86 |
| RSI_EXTREME_SHORT_15M | 0 | 5 | 5 | 20,00% | 0,32 | -0,55R | €-27,64 |
| Bilanciata 1H V1 | 14 | 95 | 95 | 36,84% | 1,11 | 0,07R | €66,07 |
| Bilanciata 1H V2 | 4 | 14 | 13 | 50,00% | 1,85 | 0,45R | €63,47 |
| Bilanciata 1H V3 Filtered | 6 | 20 | 20 | 50,00% | 1,88 | 0,46R | €92,27 |
| Rapida 1H V1 | 9 | 102 | 102 | 42,16% | 1,02 | 0,01R | €12,94 |
| Rapida 1H V2 | 0 | 2 | 1 | 50,00% | 1,19 | 0,11R | €2,14 |
| Rapida 1H V3 Filtered | 5 | 22 | 22 | 59,09% | 2,03 | 0,44R | €96,12 |
| SHADOW_4H_WIDE | 16 | 24 | 24 | 29,17% | 1,12 | 0,09R | €21,20 |
| SHADOW_BOLLINGER_MR_1H | 2 | 20 | 20 | 35,00% | 0,72 | -0,20R | €-39,83 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_EMA_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_ADAPTIVE | 11 | 47 | 47 | 48,94% | 1,78 | 0,42R | €197,56 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 7 | 17 | 17 | 52,94% | 2,17 | 0,56R | €95,36 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 7 | 7 | 57,14% | 1,94 | 0,42R | €29,44 |
| SHADOW_COMBO_SCANNER | 4 | 32 | 32 | 50,00% | 2,08 | 0,56R | €180,46 |
| SHADOW_COMBO_TREND | 8 | 38 | 38 | 39,47% | 1,35 | 0,22R | €84,08 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_EMA_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | 5 | 19 | 19 | 26,32% | 0,82 | -0,14R | €-26,97 |
| SHADOW_EMA_TREND_1H | 11 | 44 | 44 | 36,36% | 1,18 | 0,12R | €52,30 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_GLOBAL_PURE | 1 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| Forza relativa 1H V1 | 12 | 60 | 60 | 38,33% | 1,30 | 0,19R | €114,88 |
| Forza relativa 1H V2 | 3 | 18 | 17 | 55,56% | 2,65 | 0,75R | €135,46 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 7 | 15 | 15 | 26,67% | 0,72 | -0,20R | €-30,61 |
| SHADOW_SCANNER_TOP5_BTC | 4 | 34 | 34 | 50,00% | 2,08 | 0,56R | €191,65 |
| SHADOW_SCANNER_TOP5_LONG | 5 | 44 | 44 | 47,73% | 1,78 | 0,41R | €181,10 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_SOL_EMA_1H | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | ALT_ROTATION_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| MAIN | RANGE | 0 | 14 | 14 | 28,57% | 0,77 | -0,17R | €-23,82 |
| MAIN | TRANSITION | 4 | 4 | 4 | 25,00% | 0,65 | -0,27R | €-10,68 |
| MAIN | TREND_UP | 3 | 7 | 7 | 42,86% | 1,43 | 0,26R | €17,90 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 3 | 3 | 33,33% | 0,50 | -0,42R | €-12,61 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 13 | 13 | 53,85% | 2,16 | 0,56R | €72,85 |
| Bilanciata 1H V1 | RANGE | 3 | 25 | 25 | 32,00% | 0,91 | -0,06R | €-15,30 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 9 | 9 | 0,00% | 0,00 | -1,08R | €-97,25 |
| Bilanciata 1H V1 | TRANSITION | 4 | 19 | 19 | 42,11% | 1,33 | 0,20R | €38,33 |
| Bilanciata 1H V1 | TREND_UP | 3 | 29 | 29 | 41,38% | 1,40 | 0,23R | €67,44 |
| Bilanciata 1H V1 | TREND_UP_HIGH_VOL | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 1 | 2 | 2 | 100,00% | ∞ | 1,94R | €38,87 |
| Bilanciata 1H V2 | RANGE | 2 | 4 | 4 | 50,00% | 1,79 | 0,44R | €17,51 |
| Bilanciata 1H V2 | TRANSITION | 1 | 8 | 7 | 37,50% | 1,14 | 0,09R | €7,09 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 1 | 5 | 5 | 40,00% | 1,24 | 0,15R | €7,67 |
| Bilanciata 1H V3 Filtered | TREND_UP | 1 | 14 | 14 | 57,14% | 2,52 | 0,68R | €94,73 |
| Bilanciata 1H V3 Filtered | TREND_UP_HIGH_VOL | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 8 | 8 | 50,00% | 1,40 | 0,21R | €16,81 |
| Rapida 1H V1 | RANGE | 2 | 33 | 33 | 42,42% | 1,05 | 0,03R | €8,73 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 10 | 10 | 0,00% | 0,00 | -1,10R | €-109,76 |
| Rapida 1H V1 | TRANSITION | 1 | 18 | 18 | 55,56% | 1,94 | 0,39R | €70,56 |
| Rapida 1H V1 | TREND_UP | 1 | 33 | 33 | 45,45% | 1,14 | 0,08R | €26,60 |
| Rapida 1H V1 | TREND_UP_HIGH_VOL | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Rapida 1H V2 | RANGE | 0 | 2 | 1 | 50,00% | 1,19 | 0,11R | €2,14 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,48R | €14,83 |
| Rapida 1H V3 Filtered | TRANSITION | 0 | 4 | 4 | 50,00% | 1,41 | 0,22R | €8,66 |
| Rapida 1H V3 Filtered | TREND_UP | 1 | 17 | 17 | 58,82% | 2,00 | 0,43R | €72,63 |
| Rapida 1H V3 Filtered | TREND_UP_HIGH_VOL | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_4H_WIDE | RANGE | 6 | 11 | 11 | 27,27% | 1,02 | 0,01R | €1,48 |
| SHADOW_4H_WIDE | TRANSITION | 5 | 5 | 5 | 20,00% | 0,69 | -0,25R | €-12,67 |
| SHADOW_4H_WIDE | TREND_UP | 4 | 6 | 6 | 50,00% | 2,70 | 0,88R | €52,66 |
| SHADOW_4H_WIDE | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,30 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,98 | -0,01R | €-0,83 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 8 | 8 | 37,50% | 0,77 | -0,16R | €-12,56 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP_HIGH_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_EMA_1H | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,94 | -0,04R | €-1,21 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 4 | 8 | 8 | 37,50% | 1,07 | 0,05R | €3,79 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 2 | 14 | 14 | 50,00% | 1,87 | 0,45R | €63,52 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 1 | 22 | 22 | 54,55% | 2,26 | 0,60R | €131,46 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP_HIGH_VOL | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 0,94 | -0,04R | €-1,21 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 1 | 14 | 14 | 57,14% | 2,57 | 0,69R | €96,57 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP_HIGH_VOL | 5 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 4 | 4 | 75,00% | 4,46 | 0,88R | €35,25 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 2 | 2 | 50,00% | 1,50 | 0,25R | €5,04 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP_HIGH_VOL | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,85 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 0 | 3 | 3 | 66,67% | 4,32 | 1,12R | €33,60 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 11 | 11 | 36,36% | 1,20 | 0,13R | €14,31 |
| SHADOW_COMBO_SCANNER | TREND_UP | 1 | 17 | 17 | 52,94% | 2,32 | 0,65R | €110,68 |
| SHADOW_COMBO_SCANNER | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,73 |
| SHADOW_COMBO_TREND | RANGE | 2 | 6 | 6 | 16,67% | 0,41 | -0,53R | €-31,81 |
| SHADOW_COMBO_TREND | TRANSITION | 2 | 13 | 13 | 46,15% | 1,77 | 0,44R | €56,72 |
| SHADOW_COMBO_TREND | TREND_UP | 2 | 17 | 17 | 41,18% | 1,45 | 0,28R | €47,45 |
| SHADOW_COMBO_TREND | TREND_UP_HIGH_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_EMA_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | RANGE | 2 | 6 | 6 | 16,67% | 0,45 | -0,49R | €-29,56 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 4 | 4 | 25,00% | 0,78 | -0,17R | €-6,95 |
| SHADOW_DONCHIAN_1H | TREND_UP | 2 | 8 | 8 | 37,50% | 1,36 | 0,25R | €19,66 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,73 |
| SHADOW_EMA_TREND_1H | RANGE | 3 | 7 | 7 | 14,29% | 0,34 | -0,60R | €-41,95 |
| SHADOW_EMA_TREND_1H | TRANSITION | 2 | 13 | 13 | 46,15% | 1,77 | 0,44R | €56,70 |
| SHADOW_EMA_TREND_1H | TREND_UP | 3 | 22 | 22 | 36,36% | 1,17 | 0,12R | €25,81 |
| SHADOW_EMA_TREND_1H | TREND_UP_HIGH_VOL | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 10 | 10 | 30,00% | 0,88 | -0,09R | €-8,74 |
| Forza relativa 1H V1 | RANGE | 4 | 16 | 16 | 25,00% | 0,69 | -0,24R | €-38,67 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| Forza relativa 1H V1 | TRANSITION | 1 | 11 | 11 | 54,55% | 2,55 | 0,72R | €78,82 |
| Forza relativa 1H V1 | TREND_UP | 4 | 21 | 21 | 47,62% | 1,91 | 0,49R | €103,80 |
| Forza relativa 1H V1 | TREND_UP_HIGH_VOL | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 2,10R | €21,00 |
| Forza relativa 1H V2 | RANGE | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,72 |
| Forza relativa 1H V2 | TRANSITION | 1 | 7 | 7 | 42,86% | 1,57 | 0,34R | €23,81 |
| Forza relativa 1H V2 | TREND_UP | 0 | 8 | 7 | 62,50% | 3,60 | 0,99R | €78,93 |
| Forza relativa 1H V2 | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 1 | 6 | 6 | 0,00% | 0,00 | -1,09R | €-65,18 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 4 | 5 | 5 | 60,00% | 2,60 | 0,70R | €35,18 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 1 | 3 | 3 | 0,00% | 0,00 | -0,68R | €-20,48 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 4 | 4 | 50,00% | 2,12 | 0,58R | €23,08 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 2 | 3 | 3 | 100,00% | ∞ | 2,14R | €64,28 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 11 | 11 | 36,36% | 1,20 | 0,13R | €14,31 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 1 | 16 | 16 | 50,00% | 2,07 | 0,56R | €89,97 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP_HIGH_VOL | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 5 | 5 | 40,00% | 1,24 | 0,15R | €7,55 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 5 | 5 | 80,00% | 125,19 | 1,55R | €77,53 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 11 | 11 | 36,36% | 1,09 | 0,06R | €6,31 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 23 | 23 | 47,83% | 1,70 | 0,39R | €89,71 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP_HIGH_VOL | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-20T04:08:35+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **85**
- Scenari virtuali ancora attivi: **1151**
- Gruppi in attesa dell'uscita originale: **70**
- Gruppi con originale chiuso ma Shadow ancora attive: **15**
- Confronti completati: **628**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 14 | 36 | +€12,23 | 47,2% | 9 | 0 | PRELIMINARY_SAMPLE |
| GB30_R050 | 14 | 36 | +€9,21 | 47,2% | 9 | 0 | PRELIMINARY_SAMPLE |
| GB40_R050 | 14 | 36 | +€6,88 | 47,2% | 9 | 0 | PRELIMINARY_SAMPLE |
| TP_R050 | 14 | 36 | +€5,42 | 47,2% | 9 | 0 | PRELIMINARY_SAMPLE |
| GB50_R050 | 14 | 36 | +€4,09 | 47,2% | 9 | 0 | PRELIMINARY_SAMPLE |
| TP_R150 | 13 | 32 | +€9,10 | 40,6% | 5 | 1 | PRELIMINARY_SAMPLE |
| GB20_R100 | 13 | 34 | +€6,42 | 44,1% | 8 | 1 | PRELIMINARY_SAMPLE |
| GB30_R100 | 13 | 34 | +€3,16 | 44,1% | 8 | 1 | PRELIMINARY_SAMPLE |
| TP_R100 | 13 | 34 | +€0,76 | 44,1% | 8 | 1 | PRELIMINARY_SAMPLE |
| GB40_R100 | 13 | 34 | €-0,10 | 44,1% | 7 | 2 | PRELIMINARY_SAMPLE |
| GB50_R100 | 13 | 34 | €-3,01 | 41,2% | 7 | 3 | PRELIMINARY_SAMPLE |
| TIME_6H | 13 | 35 | €-6,52 | 51,4% | 11 | 3 | PRELIMINARY_SAMPLE |
| TP_R200 | 12 | 30 | +€17,21 | 46,7% | 2 | 1 | PRELIMINARY_SAMPLE |
| BE_R050 | 12 | 30 | €-1,97 | 33,3% | 8 | 0 | PRELIMINARY_SAMPLE |
| ATR15_R100 | 10 | 28 | €-3,67 | 50,0% | 2 | 2 | PRELIMINARY_SAMPLE |
| TIME_12H | 9 | 28 | +€8,32 | 60,7% | 6 | 1 | COLLECTING |
| TIME_24H | 9 | 24 | +€3,61 | 66,7% | 2 | 2 | COLLECTING |
| ATR20_R100 | 9 | 24 | +€2,38 | 50,0% | 0 | 1 | COLLECTING |
| BE_R100 | 9 | 23 | +€1,92 | 43,5% | 0 | 1 | COLLECTING |
| ATR30_R100 | 9 | 24 | +€1,55 | 41,7% | 1 | 1 | COLLECTING |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-20T04:08:35+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **628**
- Valutazioni prodotte: **1114**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TP_R050 | 9 | 1,125 | 1,535 | 0,707 | 88,9% | 80,3 | INSUFFICIENT_DATA |
| GB20_R050 | 9 | 1,147 | 1,560 | 0,713 | 88,9% | 80,2 | INSUFFICIENT_DATA |
| GB30_R050 | 9 | 1,096 | 1,494 | 0,686 | 88,9% | 80,2 | INSUFFICIENT_DATA |
| GB40_R050 | 9 | 1,044 | 1,429 | 0,653 | 88,9% | 80,2 | INSUFFICIENT_DATA |
| GB50_R050 | 9 | 0,993 | 1,363 | 0,611 | 88,9% | 80,2 | INSUFFICIENT_DATA |
| BE_R050 | 9 | 0,735 | 1,034 | 0,428 | 77,8% | 80,2 | INSUFFICIENT_DATA |
| ATR15_R100 | 8 | 0,084 | 0,033 | 0,025 | 87,5% | 76,6 | INSUFFICIENT_DATA |
| ATR20_R100 | 8 | 0,084 | 0,033 | 0,025 | 87,5% | 76,6 | INSUFFICIENT_DATA |
| ATR30_R100 | 8 | 0,084 | 0,033 | 0,026 | 87,5% | 76,6 | INSUFFICIENT_DATA |
| BE_R100 | 8 | 0,084 | 0,033 | 0,026 | 87,5% | 76,6 | INSUFFICIENT_DATA |
| GB20_R100 | 8 | 0,084 | 0,033 | 0,025 | 87,5% | 76,6 | INSUFFICIENT_DATA |
| GB30_R100 | 8 | 0,084 | 0,033 | 0,026 | 87,5% | 76,6 | INSUFFICIENT_DATA |
| GB40_R100 | 8 | 0,084 | 0,033 | 0,026 | 87,5% | 76,6 | INSUFFICIENT_DATA |
| GB50_R100 | 8 | 0,084 | 0,033 | 0,025 | 87,5% | 76,6 | INSUFFICIENT_DATA |
| TIME_12H | 8 | 0,084 | 0,033 | 0,025 | 87,5% | 76,6 | INSUFFICIENT_DATA |
| TIME_24H | 8 | 0,084 | 0,033 | 0,026 | 87,5% | 76,6 | INSUFFICIENT_DATA |
| TIME_6H | 8 | 0,084 | 0,033 | 0,026 | 87,5% | 76,6 | INSUFFICIENT_DATA |
| TP_R100 | 8 | 0,084 | 0,033 | 0,026 | 87,5% | 76,6 | INSUFFICIENT_DATA |
| TP_R150 | 8 | 0,084 | 0,033 | 0,025 | 87,5% | 76,6 | INSUFFICIENT_DATA |
| TP_R200 | 8 | 0,084 | 0,033 | 0,025 | 87,5% | 76,6 | INSUFFICIENT_DATA |

## Stati di evidenza

- **INSUFFICIENT_DATA**: meno di 30 trade completi.
- **EARLY_SIGNAL**: da 30 a 49 trade completi.
- **VALIDATING**: campione maggiore, ma robustezza non ancora dimostrata.
- **ROBUST**: test di effetto, stabilità, qualità e outlier superati.
- **ELIGIBLE_FOR_MUTATION**: evidenza sufficiente per proporre una variante al Blocco 5.
- **UNDERPERFORMING**: intervallo statistico stabilmente negativo.

## Protezioni statistiche

Sono utilizzati solo trade osservati integralmente dall'entrata. Il controllo comprende media e mediana normalizzate per rischio, media tagliata, bootstrap deterministico, quattro segmenti temporali, concentrazione dei migliori outlier, ambiguità intrabar e gap di candele.

# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-20T04:08:30+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **0**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **3.03 R**
- Profitto virtuale mancato: **0.00 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 36 | 0 | 6191.27 |
| DOWN_20 | 36 | 0 | 12382.53 |
| DOWN_30 | 36 | 0 | 18573.80 |
| DOWN_40 | 36 | 13 | 22762.44 |
| UP_10 | 31 | 0 | 6622.15 |
| UP_20 | 31 | 0 | 13244.30 |
| UP_30 | 31 | 0 | 19866.45 |
| UP_40 | 31 | 14 | 24516.47 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.

# Blocco 5 — Candidati evolutivi controllati

Generato: 2026-07-20T04:08:12+00:00

> Paper-only. Nessuna promozione, sostituzione del MASTER, modifica live o ordine reale.

## Stato

- Candidati attivi: **0**
- Nuovi candidati nel ciclo: **0**
- Evidenze rifiutate nel ciclo: **0**
- Promozioni automatiche: **0**
- Pensionamenti automatici: **0**

## Regola di mutazione

Ogni candidato è una copia indipendente del genitore e cambia un solo parametro scalare. Il file principale paper_trading_config.json non viene riscritto.

## Candidati attivi

| Candidato | Genitore | Parametro | Vecchio | Nuovo | Scenario |
| --- | --- | --- | ---: | ---: | --- |
| — | — | — | — | — | — |

## Vincoli v1

- Supportati: FIXED_R, TIME_EXIT e ATR_TRAIL solo quando richiede una singola variazione.
- MFE_GIVEBACK e BREAKEVEN non vengono approssimati: restano evidenze da implementare in una versione successiva.
- Nessun candidato può diventare MASTER nel Blocco 5.

# Blocco 6 — Validazione Champion/Challenger

Generato: 2026-07-20T04:08:35+00:00

> Paper-only. Confronto sulle stesse entrate tramite `experiment_group_id`. Nessuna promozione, sostituzione, pensione o modifica live automatica.

## Stato

- Candidati valutati: **0**
- Pronti per revisione promozione: **0**
- Promozioni automatiche: **0**
- Pensionamenti automatici: **0**

## Confronto

| Candidato | Genitore | Stato | Coppie | Δ medio R | CI basso | PF cand. | PF gen. | DD cand. | DD gen. | Score |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| — | — | Nessun candidato attivo | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Gate di sicurezza

- Solo trade chiusi dopo la creazione della candidata.
- Solo coppie con lo stesso evento d’ingresso.
- Solo dati `FULL_FROM_ENTRY` e risk model `block4_5_v1`.
- Campione, bootstrap, stabilità temporale, dipendenza dai migliori trade, PF, drawdown e liquidazioni.
- `PROMOTION_REVIEW_READY` è soltanto una raccomandazione: richiede approvazione umana e un blocco successivo.

# Blocco 7 — Governance promozioni Paper

Generato: 2026-07-20T04:08:35+00:00

> Nessuna promozione automatica. Approvazione umana e comando di esecuzione separato sono obbligatori.

## Stato

- Piani totali: **0**
- In attesa di approvazione: **0**
- Approvati ma non eseguiti: **0**
- Promozioni Paper attive: **0**
- Promozioni automatiche: **0**
- Rollback automatici: **0**

## Piani

| Piano | Candidata | Genitore | Stato | Review hash |
| --- | --- | --- | --- | --- |
| — | — | — | Nessun piano | — |

## Sicurezza

- Il piano è legato all’hash esatto della valutazione Block 6.
- Approvazione e esecuzione sono due azioni manuali distinte.
- Prima della promozione candidata e genitore devono essere senza posizioni aperte.
- Il genitore diventa `EX_MASTER` ma resta attivo in Paper.
- Ogni transazione ha backup e rollback esplicito.

# Blocco 8 — Sorveglianza post-promozione

Generato: 2026-07-20T04:08:35+00:00

> Paper-only. Il nuovo MASTER viene confrontato con l’EX_MASTER sugli stessi eventi successivi alla promozione. Nessun rollback automatico.

## Stato

- Promozioni attive monitorate: **0**
- Rollback raccomandati: **0**
- Critici: **0**
- Rollback automatici: **0**

## Confronto MASTER / EX_MASTER

| Famiglia | MASTER | EX_MASTER | Stato | Coppie | Δ medio R | CI alto | PF M | PF EX | DD ratio | Liq M/EX | Score |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| — | — | — | Nessuna promozione attiva | 0 | 0 | 0 | 0 | 0 | 0 | 0/0 | 0 |

## Sicurezza

- Solo trade chiusi dopo l’esecuzione della promozione.
- Solo coppie con lo stesso `experiment_group_id`, asset e lato.
- Solo dati `FULL_FROM_ENTRY` con risk model `block4_5_v1`.
- `ROLLBACK_RECOMMENDED` non esegue nulla: richiede il comando umano del Blocco 7.
- MASTER, EX_MASTER, stato promozione e live non vengono modificati.
