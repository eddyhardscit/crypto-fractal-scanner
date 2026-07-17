# Paper trading automatico KuCoin

Generato: 2026-07-17T16:37:08+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-17T16:36:57+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-17T16:36:57+00:00 | 2026-07-17T16:36:57+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-17T16:15:00+00:00 | 2026-07-17T16:15:00+00:00 | 7,0 min | 25,0 min | OK |
| 60m | 12 | 2026-07-17T15:00:00+00:00 | 2026-07-17T15:00:00+00:00 | 37,0 min | 45,0 min | OK |
| 240m | 12 | 2026-07-17T12:00:00+00:00 | 2026-07-17T12:00:00+00:00 | 37,0 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | AKE | 240m | LONG | 7,75 | 6,00 | 0,00 | OPENED | 37,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | HYPE | 240m | SHORT | -8,02 | 6,00 | 0,00 | RISK_GATE | 37,0 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: asset già aperto nel portafoglio. |
| Principale 4H | DOGE | 240m | SHORT | -7,70 | 6,00 | 0,00 | RISK_GATE | 37,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro rischio/esecuzione: asset già aperto nel portafoglio. |
| Principale 4H | LAB | 240m | SHORT | -6,25 | 6,00 | 0,00 | RISK_GATE | 37,0 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: asset già aperto nel portafoglio. |
| Principale 4H | SOL | 240m | SHORT | -6,00 | 6,00 | 0,00 | RISK_GATE | 37,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro rischio/esecuzione: limite posizioni nella stessa direzione. |
| Principale 4H | ONDO | 240m | LONG | 5,75 | 6,00 | 0,25 | BELOW_SCORE | 37,0 min | D: n/a | W: n/a | peso 0 | Punteggio +5.75; soglia ±6.00; mancano 0.25 punti. |
| Principale 4H | XRP | 240m | SHORT | -5,45 | 6,00 | 0,55 | BELOW_SCORE | 37,0 min | D: n/a | W: n/a | peso 0 | Punteggio -5.45; soglia ±6.00; mancano 0.55 punti. |
| Principale 4H | ZEC | 240m | LONG | 4,62 | 6,00 | 1,38 | BELOW_SCORE | 37,0 min | D: n/a | W: n/a | peso 0 | Punteggio +4.62; soglia ±6.00; mancano 1.38 punti. |
| Ampia 4H | AKE | 240m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 37,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V1 | LAB | 60m | SHORT | -7,00 | 5,00 | 0,00 | OPENED | 37,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | LAB | 60m | SHORT | -7,00 | 5,50 | 0,00 | OPENED | 37,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V1 | ONDO | 60m | LONG | 6,57 | 5,00 | 0,00 | OPENED | 37,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | ONDO | 60m | LONG | 6,57 | 5,00 | 0,00 | OPENED | 37,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V1 | XRP | 60m | SHORT | -6,37 | 5,00 | 0,00 | READY | 37,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V1 | AKE | 60m | LONG | 6,25 | 5,00 | 0,00 | READY | 37,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Ampia 4H | LAB | 240m | SHORT | -6,25 | 5,00 | 0,00 | READY | 37,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Ampia 4H | SOL | 240m | SHORT | -6,00 | 5,00 | 0,00 | READY | 37,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Ampia 4H | ONDO | 240m | LONG | 5,75 | 5,00 | 0,00 | READY | 37,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Ampia 4H | XRP | 240m | SHORT | -5,45 | 5,00 | 0,00 | READY | 37,0 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V2 | LAB | 60m | SHORT | -7,00 | 5,00 | 0,00 | STRATEGY_FILTER | 37,0 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.781,99 | -2,18% | €-218,01 | €3.000,00 | -7,27% | 4 | 12 | 25,00% | 0,54 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 12 | 80 | CAMPIONE INSUFFICIENTE | 30 (mancano 18) |

- Trade del Principale 4H chiusi: **12**; win rate **25,00%**; profit factor **0,54**.
- Expectancy: **€-16,13** per trade; P&L netto: **€-193,57**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.781,99 | €1.157,42 | €3.472,27 | €195,65 | €-22,68 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.375,02 | €1.814,74 | €3.629,47 | €101,80 | €68,77 |
| TEST | Rapida 1H V1 | 3 | €10.328,97 | €919,86 | €2.759,58 | €102,97 | €77,36 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.262,24 | €1.865,58 | €3.731,17 | €101,31 | €57,23 |
| TEST | Benchmark Donchian breakout 1H | 0 | €10.201,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive | 3 | €10.189,57 | €3.334,65 | €6.669,30 | €101,81 | €-14,40 |
| TEST | Combo Mean Reversion | 2 | €10.098,67 | €2.296,90 | €4.593,80 | €98,73 | €25,49 |
| TEST | Combo Trend | 3 | €10.088,51 | €2.322,03 | €4.644,06 | €150,79 | €30,72 |
| TEST | Forza relativa 1H V1 | 4 | €10.087,26 | €2.607,73 | €5.215,46 | €200,81 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €10.085,38 | €2.295,72 | €4.591,44 | €100,48 | €17,33 |
| TEST | Bilanciata 1H V1 | 4 | €10.068,10 | €1.461,18 | €4.383,54 | €201,39 | €-1,06 |
| TEST | Rapida 1H V2 | 0 | €10.062,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 2 | €10.060,01 | €431,11 | €862,22 | €50,08 | €60,53 |
| TEST | Bilanciata 1H V2 | 4 | €10.033,41 | €2.617,80 | €7.853,41 | €149,86 | €-15,32 |
| TEST | Btc Bollinger 1H | 1 | €10.029,70 | €1.388,89 | €4.166,67 | €50,00 | €32,62 |
| TEST | Doge Donchian 1H | 0 | €10.026,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 2 | €10.005,26 | €806,35 | €1.612,70 | €49,63 | €66,45 |
| TEST | Doge Ema 1H | 1 | €10.003,01 | €1.162,19 | €3.486,58 | €50,21 | €-36,25 |
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
| TEST | Eth Donchian 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.998,01 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €9.997,02 | €1.162,73 | €3.488,19 | €50,23 | €-46,88 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.996,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 4 | €9.996,76 | €1.557,35 | €3.114,70 | €199,94 | €16,46 |
| TEST | Sol Donchian 1H | 0 | €9.995,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.990,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.987,72 | €1.161,65 | €3.484,95 | €50,18 | €-46,84 |
| TEST | Btc Ema 1H | 1 | €9.969,68 | €1.157,41 | €3.472,22 | €50,00 | €-28,58 |
| TEST | Btc Adaptive 1H | 1 | €9.969,68 | €1.157,41 | €3.472,22 | €50,00 | €-28,58 |
| TEST | Btc Donchian 1H | 1 | €9.965,89 | €1.302,08 | €3.906,25 | €50,00 | €-32,15 |
| TEST | Eth Ema 1H | 1 | €9.959,75 | €1.157,41 | €3.472,22 | €50,00 | €-38,17 |
| TEST | Eth Adaptive 1H | 1 | €9.959,75 | €1.157,41 | €3.472,22 | €50,00 | €-38,17 |
| TEST | Global Confluence puro 1H | 1 | €9.948,83 | €1.559,86 | €3.119,73 | €49,92 | €-32,43 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €9.946,96 | €2.262,39 | €4.524,79 | €97,25 | €25,10 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.932,47 | €1.372,40 | €2.744,80 | €149,08 | €12,33 |

**Importante:** ogni riga è un conto virtuale separato da €10.000. I margini dei diversi portafogli non vanno sommati come se appartenessero a un unico conto.

**Rischio agli stop** è la perdita residua stimata usando gli stop correnti. Se uno stop protegge già un profitto, il rischio residuo viene mostrato come €0.

## Legenda portafogli

| Tipo | Nome leggibile | Metodo | Significato |
| --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | Riferimento principale: confluenza di trend su 4 ore, soglia più selettiva. |
| TEST | Bilanciata 1H V1 | Confluenza trend | Versione originale V1 a 1 ora basata sulla confluenza di trend. |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | Versione V2 selettiva: esclude i regimi storicamente peggiori, richiede trend e ritorni coerenti e limita i segnali correlati. |
| TEST | Rapida 1H V1 | Momentum / breakout | Versione originale V1 a 1 ora che cerca momentum e breakout. |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | Versione V2 selettiva: richiede vero breakout, volume, ADX, trend tecnico coerente e limita i segnali correlati. |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.781,99 | €-193,57 | 12 | 12 | 25,00% | 0,54 | €-16,13 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.375,02 | €308,49 | 8 | 8 | 75,00% | 3,76 | €38,56 | 1,04% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.328,97 | €253,26 | 28 | 28 | 46,43% | 1,46 | €9,05 | 2,34% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.262,24 | €207,25 | 7 | 7 | 57,14% | 2,89 | €29,61 | 1,62% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.201,66 | €201,66 | 6 | 6 | 66,67% | 2,90 | €33,61 | 1,35% |
| TEST | Combo Adaptive | Combo Adaptive | €10.189,57 | €207,69 | 9 | 9 | 55,56% | 2,27 | €23,08 | 0,75% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.098,67 | €76,46 | 1 | 1 | 100,00% | ∞ | €76,46 | 0,59% |
| TEST | Combo Trend | Combo Trend | €10.088,51 | €60,34 | 7 | 7 | 42,86% | 1,38 | €8,62 | 1,48% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €10.087,26 | €88,40 | 7 | 7 | 57,14% | 1,56 | €12,63 | 1,36% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €10.085,38 | €70,30 | 3 | 3 | 66,67% | 2,39 | €23,43 | 1,05% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.068,10 | €71,78 | 10 | 10 | 50,00% | 1,44 | €7,18 | 1,06% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.062,78 | €62,78 | 2 | 1 | 50,00% | 11,45 | €31,39 | 0,93% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.060,01 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,08% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.033,41 | €53,44 | 3 | 2 | 100,00% | ∞ | €17,81 | 1,29% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.029,70 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,31% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.026,22 | €26,22 | 1 | 1 | 100,00% | ∞ | €26,22 | 0,36% |
| TEST | Combo Scanner | Combo Scanner | €10.005,26 | €-60,17 | 5 | 5 | 40,00% | 0,62 | €-12,03 | 1,69% |
| TEST | Doge Ema 1H | Trend following EMA | €10.003,01 | €41,35 | 1 | 1 | 100,00% | ∞ | €41,35 | 0,70% |
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
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.998,01 | €-1,99 | 2 | 2 | 50,00% | 0,31 | €-1,00 | 0,04% |
| TEST | Sol Ema 1H | Trend following EMA | €9.997,02 | €45,99 | 1 | 1 | 100,00% | ∞ | €45,99 | 0,81% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.996,80 | €-3,20 | 2 | 2 | 50,00% | 0,70 | €-1,60 | 0,16% |
| TEST | Ampia 4H | Confluenza trend | €9.996,76 | €-18,64 | 5 | 5 | 20,00% | 0,88 | €-3,73 | 2,08% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.995,51 | €-4,49 | 1 | 1 | 0,00% | 0,00 | €-4,49 | 0,43% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.990,05 | €-9,95 | 2 | 2 | 50,00% | 0,31 | €-4,98 | 0,18% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.987,72 | €36,65 | 1 | 1 | 100,00% | ∞ | €36,65 | 0,83% |
| TEST | Btc Ema 1H | Trend following EMA | €9.969,68 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,41% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.969,68 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,41% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.965,89 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,46% |
| TEST | Eth Ema 1H | Trend following EMA | €9.959,75 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,40% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.959,75 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,40% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.948,83 | €-16,87 | 2 | 2 | 50,00% | 0,70 | €-8,43 | 1,18% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.946,96 | €-74,92 | 7 | 7 | 28,57% | 0,66 | €-10,70 | 2,06% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.932,47 | €-78,21 | 3 | 3 | 33,33% | 0,27 | €-26,07 | 1,10% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07234 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €13,60 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 59,36013 | 60,43600 | 62,47190 | 78,85003 | 53,13657 | €313,25 | €939,76 | €49,26 | €-17,03 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,18678 | 0,19982 | 0,23699 | 0,13559 | €136,26 | €408,77 | €49,05 | €-19,17 |
| Principale 4H | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00126 | 0,00126 | 0,00111 | 0,00085 | 0,00157 | €133,47 | €400,41 | €48,05 | €-0,08 |
| Bilanciata 1H V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,02421 | 2,02421 | 1,97233 | 1,35960 | 2,12798 | €655,13 | €1.965,38 | €50,37 | €0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,37581 | 0,37581 | 0,40458 | 0,49921 | 0,31828 | €219,32 | €657,96 | €50,37 | €-0,00 |
| Bilanciata 1H V1 | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,18667 | 0,18678 | 0,20845 | 0,24796 | 0,14311 | €143,84 | €431,52 | €50,35 | €-0,26 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,37613 | 0,37590 | 0,36189 | 0,25263 | 0,40460 | €442,89 | €1.328,68 | €50,30 | €-0,80 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00111 | 0,00126 | 0,00111 | 0,00075 | 0,00138 | €141,17 | €423,52 | €0,00 | €57,81 |
| Bilanciata 1H V2 | SOL | SHORT | Confluenza trend V2 | 60m | 3,0x | 73,86722 | 74,86000 | 74,93091 | 98,12030 | 71,73985 | €1.168,63 | €3.505,89 | €50,48 | €-47,12 |
| Bilanciata 1H V2 | XRP | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,07580 | 1,08371 | 1,09130 | 1,42903 | 1,04482 | €1.168,30 | €3.504,91 | €50,47 | €-25,75 |
| Bilanciata 1H V2 | LAB | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18667 | 0,18678 | 0,20845 | 0,24796 | 0,14311 | €139,69 | €419,08 | €48,90 | €-0,25 |
| Rapida 1H V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00111 | 0,00126 | 0,00112 | 0,00075 | 0,00131 | €143,19 | €429,56 | €0,00 | €58,63 |
| Rapida 1H V1 | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,18833 | 0,18678 | 0,20479 | 0,25016 | 0,16363 | €195,85 | €587,54 | €51,37 | €4,83 |
| Rapida 1H V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,37292 | 0,37590 | 0,36188 | 0,25048 | 0,38949 | €580,83 | €1.742,48 | €51,60 | €13,91 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07234 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €0,48 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 545,45000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €29,39 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 59,36013 | 60,43600 | 63,40544 | 88,74339 | 48,03325 | €367,70 | €735,40 | €50,12 | €-13,33 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00126 | 0,00126 | 0,00111 | 0,00064 | 0,00169 | €207,64 | €415,28 | €49,83 | €-0,08 |
| Forza relativa 1H V1 | AAVE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H V1 | T | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H V1 | ALLO | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00111 | 0,00126 | 0,00111 | 0,00056 | 0,00140 | €208,33 | €416,67 | €0,00 | €56,87 |
| Forza relativa 1H V2 | LAB | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18833 | 0,18678 | 0,20950 | 0,28155 | 0,14176 | €222,78 | €445,56 | €50,08 | €3,66 |
| Benchmark Bollinger mean reversion 1H | BTC | LONG | Bollinger mean reversion | 60m | 2,0x | 62931,57380 | 63424,21000 | 62176,39491 | 31780,44477 | 64064,34213 | €1.985,02 | €3.970,03 | €47,64 | €31,08 |
| Benchmark Bollinger mean reversion 1H | LAB | LONG | Bollinger mean reversion | 60m | 2,0x | 0,18881 | 0,18678 | 0,17193 | 0,09535 | 0,21414 | €277,38 | €554,76 | €49,61 | €-5,97 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Benchmark trend following EMA 1H | AKE | LONG | Trend following EMA | 60m | 2,0x | 0,00123 | 0,00126 | 0,00108 | 0,00062 | 0,00155 | €206,67 | €413,35 | €49,60 | €12,33 |
| Scanner Top 5 Long 1H | NEAR | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,12798 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,37282 | 0,37590 | 0,35738 | 0,18828 | 0,40370 | €625,48 | €1.250,97 | €51,81 | €10,32 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00111 | 0,00126 | 0,00111 | 0,00056 | 0,00138 | €214,10 | €428,21 | €0,00 | €58,45 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31828 | €324,92 | €649,84 | €49,75 | €-0,00 |
| Scanner Bottom 5 Short 1H | LAB | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,22091 | 0,18678 | 0,20438 | 0,33025 | 0,16789 | €209,34 | €418,67 | €0,00 | €64,68 |
| Scanner Bottom 5 Short 1H | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 73,86722 | 74,86000 | 74,93091 | 110,43150 | 71,73985 | €1.761,46 | €3.522,93 | €50,73 | €-47,35 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00111 | 0,00126 | 0,00111 | 0,00056 | 0,00140 | €212,63 | €425,25 | €0,00 | €58,04 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37613 | 0,37590 | 0,36189 | 0,18994 | 0,40745 | €677,81 | €1.355,62 | €51,32 | €-0,81 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07160 | 0,07234 | 0,07274 | 0,10704 | 0,06873 | €1.559,86 | €3.119,73 | €49,92 | €-32,43 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37590 | 0,35567 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €50,24 | €9,01 |
| Combo Trend | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,08689 | 1,08371 | 1,10428 | 1,62490 | 1,04863 | €1.565,99 | €3.131,98 | €50,11 | €9,17 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00123 | 0,00126 | 0,00108 | 0,00062 | 0,00155 | €210,18 | €420,37 | €50,44 | €12,54 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 62931,57380 | 63424,21000 | 62176,39491 | 31780,44477 | 64139,86001 | €2.015,29 | €4.030,58 | €48,37 | €31,55 |
| Combo Mean Reversion | LAB | LONG | Combo Mean Reversion | 60m | 2,0x | 0,18881 | 0,18678 | 0,17193 | 0,09535 | 0,21583 | €281,61 | €563,22 | €50,37 | €-6,06 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,37282 | 0,37590 | 0,35738 | 0,18828 | 0,40679 | €599,14 | €1.198,28 | €49,63 | €9,89 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00111 | 0,00126 | 0,00111 | 0,00056 | 0,00140 | €207,21 | €414,42 | €0,00 | €56,56 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,37282 | 0,37590 | 0,35738 | 0,18828 | 0,40370 | €613,42 | €1.226,85 | €50,81 | €10,12 |
| Combo Adaptive | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,08689 | 1,08371 | 1,08600 | 1,62490 | 1,05559 | €1.760,32 | €3.520,63 | €0,00 | €10,31 |
| Combo Adaptive | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 59,36013 | 60,43600 | 60,93558 | 88,74339 | 56,20922 | €960,91 | €1.921,82 | €51,01 | €-34,83 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 62906,40620 | 63424,21000 | 63812,25845 | 83560,67624 | 61094,70170 | €1.157,41 | €3.472,22 | €50,00 | €-28,58 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 62906,40620 | 63424,21000 | 63711,60820 | 83560,67624 | 61296,00220 | €1.302,08 | €3.906,25 | €50,00 | €-32,15 |
| Btc Bollinger 1H | BTC | LONG | Bollinger mean reversion | 60m | 3,0x | 62931,57380 | 63424,21000 | 62176,39491 | 42269,04040 | 64064,34213 | €1.388,89 | €4.166,67 | €50,00 | €32,62 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 62906,40620 | 63424,21000 | 63812,25845 | 83560,67624 | 61094,70170 | €1.157,41 | €3.472,22 | €50,00 | €-28,58 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 73,86722 | 74,86000 | 74,93091 | 98,12030 | 71,73985 | €1.162,73 | €3.488,19 | €50,23 | €-46,88 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 73,86722 | 74,86000 | 74,93091 | 98,12030 | 71,73985 | €1.161,65 | €3.484,95 | €50,18 | €-46,84 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1813,41724 | 1833,35000 | 1839,53045 | 2408,82257 | 1761,19083 | €1.157,41 | €3.472,22 | €50,00 | €-38,17 |
| Eth Adaptive 1H | ETH | SHORT | Combo Adaptive | 60m | 3,0x | 1813,41724 | 1833,35000 | 1839,53045 | 2408,82257 | 1761,19083 | €1.157,41 | €3.472,22 | €50,00 | €-38,17 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07160 | 0,07234 | 0,07263 | 0,09510 | 0,06953 | €1.162,19 | €3.486,58 | €50,21 | €-36,25 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sol Donchian 1H | SOL | SHORT | 2026-07-17T16:37:03+00:00 | 74,66915 | €-4,49 | -0,09 | STOP |
| Rapida 1H V2 | DOGE | SHORT | 2026-07-17T15:20:35+00:00 | 0,07183 | €-6,01 | -0,12 | STOP |
| Rapida 1H V1 | NEAR | LONG | 2026-07-17T15:20:35+00:00 | 2,02300 | €-4,56 | -0,09 | TIME_EXIT_NO_CANDLES |
| Bilanciata 1H V1 | AAVE | LONG | 2026-07-17T15:20:35+00:00 | 98,81996 | €-3,87 | -0,08 | TIME_EXIT_NO_CANDLES |
| Bilanciata 1H V1 | T | LONG | 2026-07-17T15:20:35+00:00 | 0,00540 | €1,21 | 0,02 | TIME_EXIT_NO_CANDLES |
| Sol Bollinger 1H | SOL | LONG | 2026-07-17T13:56:55+00:00 | 73,79174 | €-55,79 | -1,12 | STOP |
| Ampia 4H | PEPE | LONG | 2026-07-17T13:56:55+00:00 | 0,00000 | €-51,78 | -1,03 | STOP |
| Rapida 1H V2 | SOL | SHORT | 2026-07-17T13:56:55+00:00 | 73,43324 | €68,78 | 1,38 | TARGET |
| Principale 4H | ETH | LONG | 2026-07-17T13:56:55+00:00 | 1815,82427 | €-51,85 | -1,05 | STOP |
| Sol Ema 1H | SOL | SHORT | 2026-07-17T11:54:37+00:00 | 74,84621 | €45,99 | 0,92 | STOP |
| Sol Adaptive 1H | SOL | SHORT | 2026-07-17T11:54:37+00:00 | 74,88386 | €36,65 | 0,73 | STOP |
| Bilanciata 1H V2 | LAB | SHORT | 2026-07-17T11:54:37+00:00 | 0,19316 | €8,06 | 0,16 | STOP |

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
| MAIN | Principale 4H | 17/30 | 12/30 | 0,59 | 0,54 | -0,32R | €-16,13 | 4,26% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 2/30 | 2/30 | 1,18 | 0,70 | 0,10R | €-1,60 | 0,16% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 57/30 | 10/30 | 0,98 | 1,44 | -0,01R | €7,18 | 1,06% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 1/30 | 2/30 | ∞ | ∞ | 1,99R | €17,81 | 1,29% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 | 66/30 | 28/30 | 0,78 | 1,46 | -0,15R | €9,05 | 2,34% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 1/30 | 1/30 | ∞ | 11,45 | 1,36R | €31,39 | 0,93% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 14/30 | 5/30 | 0,74 | 0,88 | -0,21R | €-3,73 | 2,08% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 13/30 | 7/30 | 0,59 | 0,66 | -0,31R | €-10,70 | 2,06% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,31% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,46% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,41% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive | 17/30 | 9/30 | 2,05 | 2,27 | 0,53R | €23,08 | 0,75% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 4/30 | 1/30 | 4,51 | ∞ | 0,89R | €76,46 | 0,59% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 10/30 | 5/30 | 0,86 | 0,62 | -0,10R | €-12,03 | 1,69% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_COMBO_TREND | Combo Trend | 14/30 | 7/30 | 1,14 | 1,38 | 0,09R | €8,62 | 1,48% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 0/30 | 1/30 | 0,00 | ∞ | 0,00R | €26,22 | 0,36% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 0/30 | 1/30 | 0,00 | ∞ | 0,00R | €41,35 | 0,70% | n/a | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 9/30 | 6/30 | 1,16 | 2,90 | 0,11R | €33,61 | 1,35% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 20/30 | 3/30 | 0,87 | 0,27 | -0,09R | €-26,07 | 1,10% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,40% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,40% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 1/30 | 2/30 | 0,00 | 0,70 | -1,10R | €-8,43 | 1,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 36/30 | 7/30 | 0,79 | 1,56 | -0,16R | €12,63 | 1,36% | DIVERGENTE | BOCCIATA RESEARCH |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 1/30 | 0/30 | 0,00 | 0,00 | -1,01R | €0,00 | 0,08% | n/a | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 8/30 | 3/30 | 1,84 | 2,39 | 0,44R | €23,43 | 1,05% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 12/30 | 7/30 | 1,01 | 2,89 | 0,01R | €29,61 | 1,62% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 17/30 | 8/30 | 0,99 | 3,76 | -0,00R | €38,56 | 1,04% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_1H | Sol Adaptive 1H | 1/30 | 1/30 | ∞ | ∞ | 1,89R | €36,65 | 0,83% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_ADAPTIVE_4H | Sol Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_1H | Sol Bollinger 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,13R | €-55,79 | 0,62% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_SOL_BOLLINGER_4H | Sol Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_1H | Sol Donchian 1H | 0/30 | 1/30 | 0,00 | 0,00 | 0,00R | €-4,49 | 0,43% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_DONCHIAN_4H | Sol Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_1H | Sol Ema 1H | 1/30 | 1/30 | ∞ | ∞ | 1,89R | €45,99 | 0,81% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SOL_EMA_4H | Sol Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |

Per le famiglie RSI con più configurazioni di leva o margine, il lato paper usa il conto con il maggior numero di eventi indipendenti; i conti duplicati non vengono aggregati.
`PRONTA PER REVISIONE LIVE` non invia ordini e non sposta capitale: abilita soltanto una revisione manuale finale.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07234**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 22.1 min | OK |
| Global DOGE | -6.0 | OK |
| Classic raw | -11.0 | OK |
| DOGE/BTC raw | -6.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 63424.21 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, upper_wick, bearish_confirmation**
- High **0.07233**; close **0.07229**; wick alta **14.8%**; volume **x0.49**

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
- Confidenza: **79,60%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Direzione poco definita: score BTC +0.0, breadth EMA50 33%, ADX 21.9.
- BTC trend score: **0,00**; ADX: **21,91**; breadth sopra EMA50: **33,33%**
- Mediana alt vs BTC: **-0,21%**; dispersione: **9,45%**

- Aperti in questo ciclo: **10**
- Chiusi in questo ciclo: **4**
- Posizioni research aperte: **117**
- Trade research chiusi: **323**
- Eventi di mercato indipendenti chiusi: **144**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **821**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 8 | 17 | 17 | 23,53% | 0,59 | -0,32R | €-54,86 |
| RSI_EXTREME_SHORT_15M | 0 | 2 | 2 | 50,00% | 1,18 | 0,10R | €1,96 |
| Bilanciata 1H V1 | 12 | 57 | 57 | 35,09% | 0,98 | -0,01R | €-6,53 |
| Bilanciata 1H V2 | 5 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| Rapida 1H V1 | 8 | 66 | 66 | 36,36% | 0,78 | -0,15R | €-95,89 |
| Rapida 1H V2 | 1 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_4H_WIDE | 12 | 14 | 14 | 21,43% | 0,74 | -0,21R | €-29,47 |
| SHADOW_BOLLINGER_MR_1H | 1 | 13 | 13 | 30,77% | 0,59 | -0,31R | €-40,34 |
| SHADOW_BTC_ADAPTIVE_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | 9 | 17 | 17 | 52,94% | 2,05 | 0,53R | €89,36 |
| SHADOW_COMBO_MEAN_REVERSION | 1 | 4 | 4 | 75,00% | 4,51 | 0,89R | €35,76 |
| SHADOW_COMBO_SCANNER | 3 | 10 | 10 | 30,00% | 0,86 | -0,10R | €-10,28 |
| SHADOW_COMBO_TREND | 6 | 14 | 14 | 35,71% | 1,14 | 0,09R | €12,92 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_EMA_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | 7 | 9 | 9 | 33,33% | 1,16 | 0,11R | €10,02 |
| SHADOW_EMA_TREND_1H | 8 | 20 | 20 | 30,00% | 0,87 | -0,09R | €-19,00 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_GLOBAL_PURE | 1 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| Forza relativa 1H V1 | 8 | 36 | 36 | 27,78% | 0,79 | -0,16R | €-56,27 |
| Forza relativa 1H V2 | 2 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 8 | 8 | 8 | 50,00% | 1,84 | 0,44R | €35,29 |
| SHADOW_SCANNER_TOP5_BTC | 3 | 12 | 12 | 33,33% | 1,01 | 0,01R | €0,90 |
| SHADOW_SCANNER_TOP5_LONG | 3 | 17 | 17 | 35,29% | 0,99 | -0,00R | €-0,70 |
| SHADOW_SOL_ADAPTIVE_1H | 1 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_DONCHIAN_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_1H | 1 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | RANGE | 3 | 10 | 10 | 20,00% | 0,48 | -0,43R | €-42,62 |
| MAIN | TRANSITION | 3 | 3 | 3 | 33,33% | 0,97 | -0,02R | €-0,54 |
| MAIN | TREND_UP | 2 | 4 | 4 | 25,00% | 0,63 | -0,29R | €-11,70 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,29R | €12,86 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 0 | 9 | 9 | 55,56% | 2,27 | 0,60R | €54,20 |
| Bilanciata 1H V1 | RANGE | 9 | 18 | 18 | 38,89% | 1,18 | 0,12R | €21,01 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 9 | 9 | 0,00% | 0,00 | -1,08R | €-97,25 |
| Bilanciata 1H V1 | TRANSITION | 2 | 8 | 8 | 62,50% | 2,99 | 0,80R | €63,91 |
| Bilanciata 1H V1 | TREND_UP | 1 | 13 | 13 | 23,08% | 0,55 | -0,37R | €-48,39 |
| Bilanciata 1H V2 | RANGE | 5 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 6 | 6 | 50,00% | 1,38 | 0,20R | €12,11 |
| Rapida 1H V1 | RANGE | 7 | 27 | 27 | 44,44% | 1,17 | 0,09R | €24,57 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 10 | 10 | 0,00% | 0,00 | -1,10R | €-109,76 |
| Rapida 1H V1 | TRANSITION | 1 | 8 | 8 | 62,50% | 2,15 | 0,48R | €38,04 |
| Rapida 1H V1 | TREND_UP | 0 | 15 | 15 | 26,67% | 0,49 | -0,41R | €-60,84 |
| Rapida 1H V2 | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 1,36R | €13,57 |
| SHADOW_4H_WIDE | RANGE | 7 | 9 | 9 | 11,11% | 0,34 | -0,60R | €-54,26 |
| SHADOW_4H_WIDE | TRANSITION | 3 | 2 | 2 | 50,00% | 2,75 | 0,89R | €17,73 |
| SHADOW_4H_WIDE | TREND_UP | 2 | 3 | 3 | 33,33% | 1,34 | 0,24R | €7,06 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 1 | 6 | 6 | 33,33% | 0,67 | -0,24R | €-14,49 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 2 | 2 | 0,00% | 0,00 | -1,05R | €-21,01 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 0 | 5 | 5 | 40,00% | 0,85 | -0,10R | €-4,84 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_BTC_EMA_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 9 | 2 | 2 | 50,00% | 1,87 | 0,46R | €9,26 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 0 | 6 | 6 | 66,67% | 3,64 | 0,93R | €55,93 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 0 | 9 | 9 | 44,44% | 1,45 | 0,27R | €24,18 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 1 | 3 | 3 | 66,67% | 3,02 | 0,69R | €20,58 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,52R | €15,18 |
| SHADOW_COMBO_SCANNER | RANGE | 2 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_COMBO_SCANNER | TRANSITION | 1 | 3 | 3 | 33,33% | 1,03 | 0,02R | €0,72 |
| SHADOW_COMBO_SCANNER | TREND_UP | 0 | 7 | 7 | 28,57% | 0,80 | -0,16R | €-11,00 |
| SHADOW_COMBO_TREND | RANGE | 5 | 2 | 2 | 0,00% | 0,00 | -1,03R | €-20,68 |
| SHADOW_COMBO_TREND | TRANSITION | 1 | 5 | 5 | 60,00% | 3,06 | 0,87R | €43,32 |
| SHADOW_COMBO_TREND | TREND_UP | 0 | 7 | 7 | 28,57% | 0,82 | -0,14R | €-9,73 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_EMA_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | RANGE | 5 | 3 | 3 | 33,33% | 1,16 | 0,11R | €3,44 |
| SHADOW_DONCHIAN_1H | TRANSITION | 2 | 2 | 2 | 50,00% | 2,38 | 0,70R | €14,01 |
| SHADOW_DONCHIAN_1H | TREND_UP | 0 | 4 | 4 | 25,00% | 0,77 | -0,19R | €-7,43 |
| SHADOW_EMA_TREND_1H | RANGE | 6 | 3 | 3 | 0,00% | 0,00 | -1,03R | €-30,81 |
| SHADOW_EMA_TREND_1H | TRANSITION | 1 | 5 | 5 | 60,00% | 3,06 | 0,87R | €43,31 |
| SHADOW_EMA_TREND_1H | TREND_UP | 1 | 12 | 12 | 25,00% | 0,67 | -0,26R | €-31,49 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 8 | 8 | 25,00% | 0,68 | -0,26R | €-20,48 |
| Forza relativa 1H V1 | RANGE | 4 | 15 | 15 | 20,00% | 0,52 | -0,40R | €-60,53 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| Forza relativa 1H V1 | TRANSITION | 0 | 4 | 4 | 75,00% | 6,16 | 1,34R | €53,76 |
| Forza relativa 1H V1 | TREND_UP | 4 | 7 | 7 | 28,57% | 0,83 | -0,12R | €-8,69 |
| Forza relativa 1H V2 | RANGE | 2 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,14 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 4 | 2 | 2 | 0,00% | 0,00 | -1,04R | €-20,74 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 2 | 4 | 4 | 75,00% | 5,24 | 1,16R | €46,30 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 2 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,05R | €-10,52 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 3 | 2 | 2 | 100,00% | ∞ | 2,12R | €42,42 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 0 | 3 | 3 | 33,33% | 1,03 | 0,02R | €0,72 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 0 | 6 | 6 | 16,67% | 0,41 | -0,53R | €-31,71 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 3 | 3 | 3 | 100,00% | ∞ | 1,94R | €58,28 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 0 | 3 | 3 | 33,33% | 0,94 | -0,04R | €-1,28 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 0 | 10 | 10 | 20,00% | 0,46 | -0,47R | €-46,60 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
