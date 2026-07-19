# Paper trading automatico KuCoin

Generato: 2026-07-19T20:53:35+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-19T20:53:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-19T20:53:25+00:00 | 2026-07-19T20:53:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-19T20:30:00+00:00 | 2026-07-19T20:30:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-19T19:00:00+00:00 | 2026-07-19T19:00:00+00:00 | 53,5 min | 45,0 min | STALE_CANDLE |
| 240m | 12 | 2026-07-19T16:00:00+00:00 | 2026-07-19T16:00:00+00:00 | 53,5 min | 1,00 h | OK |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | RISK_GATE | 53,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | DOGE | 240m | SHORT | -7,46 | 6,00 | 0,00 | RISK_GATE | 53,5 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | AKE | 240m | LONG | 6,25 | 6,00 | 0,00 | RISK_GATE | 53,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Principale 4H | PEPE | 240m | LONG | 5,74 | 6,00 | 0,26 | BELOW_SCORE | 53,5 min | D: n/a | W: n/a | peso 0 | Punteggio +5.74; soglia ±6.00; mancano 0.26 punti. |
| Principale 4H | HYPE | 240m | SHORT | -4,73 | 6,00 | 1,27 | BELOW_SCORE | 53,5 min | D: n/a | W: n/a | peso 0 | Punteggio -4.73; soglia ±6.00; mancano 1.27 punti. |
| Ampia 4H | BANK | 240m | LONG | 7,75 | 5,00 | 0,00 | RISK_GATE | 53,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Ampia 4H | DOGE | 240m | SHORT | -7,46 | 5,00 | 0,00 | RISK_GATE | 53,5 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Ampia 4H | AKE | 240m | LONG | 6,25 | 5,00 | 0,00 | RISK_GATE | 53,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Ampia 4H | PEPE | 240m | LONG | 5,74 | 5,00 | 0,00 | RISK_GATE | 53,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |
| Ampia 4H | HYPE | 240m | SHORT | -4,73 | 5,00 | 0,27 | BELOW_SCORE | 53,5 min | D: n/a | W: n/a | peso 0 | Punteggio -4.73; soglia ±5.00; mancano 0.27 punti. |
| Ampia 4H | ZEC | 240m | LONG | 3,90 | 5,00 | 1,10 | BELOW_SCORE | 53,5 min | D: n/a | W: n/a | peso 0 | Punteggio +3.90; soglia ±5.00; mancano 1.10 punti. |
| Bilanciata 1H V1 | BANK | 60m | LONG | 6,75 | 5,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Bilanciata 1H V2 | BANK | 60m | LONG | 6,75 | 5,50 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Bilanciata 1H V3 Filtered | BANK | 60m | LONG | 6,75 | 6,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Rapida 1H V1 | BANK | 60m | LONG | 6,75 | 4,50 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Rapida 1H V2 | BANK | 60m | LONG | 6,75 | 5,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Rapida 1H V3 Filtered | BANK | 60m | LONG | 6,75 | 4,50 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Forza relativa 1H V1 | BANK | 60m | LONG | 6,75 | 4,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Forza relativa 1H V2 | BANK | 60m | LONG | 6,75 | 5,50 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |
| Benchmark Donchian breakout 1H | BANK | 60m | LONG | 6,75 | 5,00 | 0,00 | STALE_CANDLE | 53,5 min | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 53.5 minuti; tolleranza 45 minuti. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.922,11 | -0,78% | €-77,89 | €3.000,00 | -2,60% | 4 | 15 | 33,33% | 0,89 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 15 | 167 | CAMPIONE INSUFFICIENTE | 30 (mancano 15) |

- Trade del Principale 4H chiusi: **15**; win rate **33,33%**; profit factor **0,89**.
- Expectancy: **€-3,37** per trade; P&L netto: **€-50,49**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.922,11 | €1.317,93 | €3.953,78 | €197,45 | €-26,74 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.311,01 | €2.000,60 | €4.001,21 | €155,31 | €-37,34 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.301,47 | €2.809,27 | €5.618,54 | €152,93 | €-20,71 |
| TEST | Forza relativa 1H V2 | 4 | €10.263,21 | €2.879,58 | €5.759,15 | €151,05 | €87,62 |
| TEST | Bilanciata 1H V1 | 4 | €10.262,81 | €1.892,86 | €5.678,58 | €150,97 | €98,97 |
| TEST | Combo Adaptive | 3 | €10.239,96 | €3.522,36 | €7.044,73 | €153,58 | €-8,14 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.232,80 | €1.798,47 | €3.596,94 | €101,86 | €0,85 |
| TEST | Rapida 1H V1 | 4 | €10.189,66 | €1.666,59 | €4.999,78 | €154,84 | €60,95 |
| TEST | Combo Mean Reversion | 1 | €10.175,60 | €281,61 | €563,22 | €50,37 | €0,00 |
| TEST | Ampia 4H | 4 | €10.168,83 | €1.561,79 | €3.123,57 | €201,01 | €12,14 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.112,71 | €3.432,06 | €10.296,18 | €149,89 | €87,21 |
| TEST | Combo Trend | 3 | €10.092,03 | €3.048,77 | €6.097,54 | €151,18 | €-77,29 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €10.075,35 | €2.277,23 | €4.554,46 | €97,61 | €7,55 |
| TEST | Btc Bollinger 1H | 0 | €10.068,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €10.062,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V1 | 4 | €10.060,32 | €3.004,75 | €6.009,51 | €201,64 | €-21,81 |
| TEST | Doge Donchian 1H | 0 | €10.026,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 4 | €10.022,75 | €2.917,04 | €8.751,11 | €199,51 | €-4,10 |
| TEST | Combo Scanner | 3 | €10.022,21 | €3.487,82 | €6.975,64 | €150,65 | €-30,09 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €10.018,81 | €1.950,57 | €3.901,13 | €50,15 | €-8,85 |
| TEST | Eth Bollinger 1H | 1 | €10.005,60 | €1.388,89 | €4.166,67 | €50,00 | €7,87 |
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
| TEST | Rapida 1H V3 Filtered | 2 | €9.998,94 | €1.621,09 | €4.863,28 | €99,76 | €-2,25 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.995,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €9.995,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.990,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €9.988,51 | €1.302,08 | €3.906,25 | €50,00 | €-8,94 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.982,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.981,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.979,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.978,00 | €2.089,95 | €4.179,90 | €149,62 | €-50,21 |
| TEST | Doge Ema 1H | 1 | €9.975,89 | €1.155,81 | €3.467,44 | €49,93 | €-9,29 |
| TEST | Eth Ema 1H | 1 | €9.950,34 | €1.151,05 | €3.453,16 | €49,73 | €7,53 |
| TEST | Btc Ema 1H | 0 | €9.945,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.945,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.944,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 1 | €9.934,94 | €1.151,05 | €3.453,16 | €49,73 | €-7,90 |
| TEST | Global Confluence puro 1H | 1 | €9.919,45 | €1.551,38 | €3.102,75 | €49,64 | €-8,74 |
| TEST | Combo Adaptive MFE Trail | 3 | €9.741,33 | €4.836,25 | €9.672,50 | €146,78 | €-6,40 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.922,11 | €-50,49 | 15 | 15 | 33,33% | 0,89 | €-3,37 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.311,01 | €350,95 | 15 | 15 | 53,33% | 2,28 | €23,40 | 2,12% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.301,47 | €325,68 | 12 | 12 | 50,00% | 2,51 | €27,14 | 1,62% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.263,21 | €179,19 | 12 | 12 | 33,33% | 1,69 | €14,93 | 2,32% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.262,81 | €167,06 | 13 | 13 | 46,15% | 1,99 | €12,85 | 1,12% |
| TEST | Combo Adaptive | Combo Adaptive | €10.239,96 | €252,59 | 14 | 14 | 42,86% | 2,15 | €18,04 | 1,01% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.232,80 | €234,28 | 11 | 11 | 54,55% | 2,08 | €21,30 | 1,98% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.189,66 | €131,62 | 37 | 37 | 40,54% | 1,16 | €3,56 | 2,83% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.175,60 | €176,28 | 4 | 4 | 75,00% | 4,42 | €44,07 | 0,59% |
| TEST | Ampia 4H | Confluenza trend | €10.168,83 | €157,06 | 10 | 10 | 30,00% | 1,60 | €15,71 | 2,08% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.112,71 | €30,29 | 14 | 14 | 35,71% | 1,07 | €2,16 | 2,20% |
| TEST | Combo Trend | Combo Trend | €10.092,03 | €170,64 | 8 | 8 | 50,00% | 2,07 | €21,33 | 1,48% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.075,35 | €70,65 | 11 | 11 | 45,45% | 1,32 | €6,42 | 2,06% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.068,69 | €68,69 | 1 | 1 | 100,00% | ∞ | €68,69 | 0,31% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.062,78 | €62,78 | 2 | 1 | 50,00% | 11,45 | €31,39 | 0,93% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €10.060,32 | €85,74 | 9 | 9 | 55,56% | 1,53 | €9,53 | 1,84% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.026,22 | €26,22 | 1 | 1 | 100,00% | ∞ | €26,22 | 0,36% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.022,75 | €32,23 | 13 | 11 | 46,15% | 1,10 | €2,48 | 2,10% |
| TEST | Combo Scanner | Combo Scanner | €10.022,21 | €55,26 | 10 | 10 | 40,00% | 1,21 | €5,53 | 1,69% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €10.018,81 | €28,41 | 6 | 6 | 50,00% | 1,26 | €4,73 | 1,90% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.005,60 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,26% |
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
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.998,94 | €4,35 | 21 | 21 | 33,33% | 1,01 | €0,21 | 2,24% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.995,97 | €-4,03 | 4 | 4 | 25,00% | 0,18 | €-1,01 | 0,04% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.995,51 | €-4,49 | 1 | 1 | 0,00% | 0,00 | €-4,49 | 0,43% |
| TEST | Sol Ema 1H | Trend following EMA | €9.990,84 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 0,87% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.988,51 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,38% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.982,18 | €-17,82 | 4 | 4 | 25,00% | 0,30 | €-4,46 | 0,18% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.981,55 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 0,89% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.979,87 | €-20,13 | 4 | 4 | 25,00% | 0,18 | €-5,03 | 0,20% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.978,00 | €30,25 | 4 | 4 | 50,00% | 1,28 | €7,56 | 1,10% |
| TEST | Doge Ema 1H | Trend following EMA | €9.975,89 | €-13,78 | 2 | 2 | 50,00% | 0,75 | €-6,89 | 1,17% |
| TEST | Eth Ema 1H | Trend following EMA | €9.950,34 | €-54,90 | 1 | 1 | 0,00% | 0,00 | €-54,90 | 0,61% |
| TEST | Btc Ema 1H | Trend following EMA | €9.945,45 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,65% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.945,45 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,65% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.944,88 | €-55,12 | 1 | 1 | 0,00% | 0,00 | €-55,12 | 0,67% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.934,94 | €-54,90 | 1 | 1 | 0,00% | 0,00 | €-54,90 | 0,77% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.919,45 | €-71,19 | 3 | 3 | 33,33% | 0,35 | €-23,73 | 1,19% |
| TEST | Combo Adaptive MFE Trail | Combo Adaptive | €9.741,33 | €-246,28 | 12 | 12 | 25,00% | 0,18 | €-20,52 | 2,83% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07235 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €13,36 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 59,36013 | 61,41200 | 62,47190 | 78,85003 | 53,13657 | €313,25 | €939,76 | €49,26 | €-32,48 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,19982 | 0,23699 | 0,13559 | €136,26 | €408,77 | €49,05 | €-0,00 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 556,07119 | 551,27000 | 524,63715 | 373,49448 | 618,93927 | €293,97 | €881,92 | €49,85 | €-7,61 |
| Bilanciata 1H V1 | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €143,84 | €431,52 | €50,35 | €-0,00 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,37613 | 0,37613 | 0,36189 | 0,25263 | 0,40460 | €442,89 | €1.328,68 | €50,30 | €0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,07253 | 0,07235 | 0,07357 | 0,09634 | 0,07044 | €1.164,82 | €3.494,46 | €50,32 | €8,50 |
| Bilanciata 1H V1 | BANK | LONG | Confluenza trend | 60m | 3,0x | 0,19044 | 0,23108 | 0,19871 | 0,12791 | 0,23614 | €141,31 | €423,92 | €0,00 | €90,47 |
| Bilanciata 1H V2 | LAB | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €139,69 | €419,08 | €48,90 | €-0,00 |
| Bilanciata 1H V2 | GRAM | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,49240 | 1,49240 | 1,53621 | 1,98241 | 1,40478 | €570,19 | €1.710,58 | €50,21 | €-0,00 |
| Bilanciata 1H V2 | PEPE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.047,96 | €3.143,89 | €50,32 | €10,54 |
| Bilanciata 1H V2 | DOGE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,07205 | 0,07235 | 0,07308 | 0,09570 | 0,06997 | €1.159,19 | €3.477,56 | €50,08 | €-14,64 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,07217 | 0,07235 | 0,07321 | 0,09586 | 0,07009 | €1.157,41 | €3.472,22 | €50,00 | €-8,82 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1867,19336 | 1863,85000 | 1840,30578 | 1254,13154 | 1920,96853 | €1.152,16 | €3.456,47 | €49,77 | €-6,19 |
| Bilanciata 1H V3 Filtered | BANK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,19596 | 0,23108 | 0,19871 | 0,13162 | 0,24299 | €139,22 | €417,67 | €0,00 | €74,86 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €983,27 | €2.949,82 | €50,11 | €27,36 |
| Rapida 1H V1 | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,18833 | 0,18833 | 0,20479 | 0,25016 | 0,16363 | €195,85 | €587,54 | €51,37 | €-0,00 |
| Rapida 1H V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,37292 | 0,37292 | 0,36188 | 0,25048 | 0,38949 | €580,83 | €1.742,48 | €51,60 | €0,00 |
| Rapida 1H V1 | GRAM | SHORT | Momentum / breakout | 60m | 3,0x | 1,49240 | 1,49240 | 1,52648 | 1,98241 | 1,44129 | €757,31 | €2.271,94 | €51,87 | €-0,00 |
| Rapida 1H V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,20038 | 0,23108 | 0,20423 | 0,13459 | 0,23645 | €132,61 | €397,82 | €0,00 | €60,95 |
| Rapida 1H V3 Filtered | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1868,12355 | 1863,85000 | 1847,20057 | 1254,75632 | 1899,50803 | €1.482,34 | €4.447,03 | €49,81 | €-10,17 |
| Rapida 1H V3 Filtered | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,22677 | 0,23108 | 0,19955 | 0,15231 | 0,26758 | €138,75 | €416,26 | €49,95 | €7,92 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07235 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €0,30 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 551,27000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €36,80 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 59,36013 | 61,41200 | 63,40544 | 88,74339 | 48,03325 | €367,70 | €735,40 | €50,12 | €-25,42 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00188 | 0,00188 | 0,00165 | 0,00095 | 0,00251 | €212,07 | €424,14 | €50,90 | €0,46 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H V1 | ALLO | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Forza relativa 1H V1 | PEPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.481,55 | €2.963,10 | €50,42 | €-5,69 |
| Forza relativa 1H V1 | AKE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00195 | 0,00188 | 0,00172 | 0,00099 | 0,00247 | €209,72 | €419,44 | €50,33 | €-16,12 |
| Forza relativa 1H V2 | LAB | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18833 | 0,18833 | 0,20950 | 0,28155 | 0,14176 | €222,78 | €445,56 | €50,08 | €-0,00 |
| Forza relativa 1H V2 | GRAM | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,47771 | 1,47771 | 1,52060 | 2,20918 | 1,38336 | €871,54 | €1.743,07 | €50,59 | €-0,00 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.573,66 | €3.147,32 | €50,37 | €10,55 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,19548 | 0,23108 | 0,19752 | 0,09872 | 0,24709 | €211,61 | €423,21 | €0,00 | €77,08 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1868,12355 | 1863,85000 | 1838,23357 | 943,40239 | 1942,84849 | €1.585,47 | €3.170,93 | €50,73 | €-7,25 |
| Benchmark Donchian breakout 1H | BANK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,22677 | 0,23108 | 0,19955 | 0,11452 | 0,29479 | €213,00 | €426,01 | €51,12 | €8,11 |
| Benchmark Bollinger mean reversion 1H | LAB | LONG | Bollinger mean reversion | 60m | 2,0x | 0,18881 | 0,18881 | 0,17193 | 0,09535 | 0,21414 | €277,38 | €554,76 | €49,61 | €0,00 |
| Benchmark Bollinger mean reversion 1H | ETH | SHORT | Bollinger mean reversion | 60m | 2,0x | 1867,37645 | 1863,85000 | 1889,78497 | 2791,72779 | 1833,76367 | €1.999,85 | €3.999,71 | €48,00 | €7,55 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 59,78804 | 61,41200 | 61,40996 | 89,38312 | 56,21982 | €924,22 | €1.848,44 | €50,14 | €-50,21 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €625,48 | €1.250,97 | €51,81 | €0,00 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 556,25123 | 551,27000 | 543,83554 | 280,90687 | 581,08261 | €1.159,54 | €2.319,07 | €51,76 | €-20,77 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00195 | 0,00188 | 0,00172 | 0,00099 | 0,00242 | €215,58 | €431,17 | €51,74 | €-16,57 |
| Scanner Bottom 5 Short 1H | LAB | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,22091 | 0,22091 | 0,20335 | 0,33025 | 0,16789 | €209,34 | €418,67 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,07217 | 0,07235 | 0,07321 | 0,10789 | 0,07009 | €1.741,23 | €3.482,46 | €50,15 | €-8,85 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37613 | 0,37613 | 0,36189 | 0,18994 | 0,40745 | €677,81 | €1.355,62 | €51,32 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 556,25123 | 551,27000 | 543,83554 | 280,90687 | 583,56574 | €1.156,31 | €2.312,63 | €51,62 | €-20,71 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07215 | 0,07235 | 0,07330 | 0,10786 | 0,06926 | €1.551,38 | €3.102,75 | €49,64 | €-8,74 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,35567 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €50,24 | €0,00 |
| Combo Trend | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,08689 | 1,09605 | 1,10428 | 1,62490 | 1,04863 | €1.565,99 | €3.131,98 | €50,11 | €-26,39 |
| Combo Trend | HYPE | SHORT | Combo Trend | 60m | 2,0x | 59,78804 | 61,41200 | 61,40996 | 89,38312 | 56,21982 | €936,92 | €1.873,85 | €50,83 | €-50,90 |
| Combo Mean Reversion | LAB | LONG | Combo Mean Reversion | 60m | 2,0x | 0,18881 | 0,18881 | 0,17193 | 0,09535 | 0,21583 | €281,61 | €563,22 | €50,37 | €0,00 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40679 | €599,14 | €1.198,28 | €49,63 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,07215 | 0,07235 | 0,07319 | 0,10786 | 0,06986 | €1.763,29 | €3.526,57 | €50,78 | €-9,94 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 556,25123 | 551,27000 | 543,83554 | 280,90687 | 583,56574 | €1.125,40 | €2.250,79 | €50,24 | €-20,16 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €613,42 | €1.226,85 | €50,81 | €0,00 |
| Combo Adaptive | GRAM | SHORT | Combo Adaptive | 60m | 2,0x | 1,48181 | 1,48181 | 1,51561 | 2,21531 | 1,41422 | €1.129,35 | €2.258,70 | €51,51 | €-0,00 |
| Combo Adaptive | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1868,12355 | 1863,85000 | 1841,22257 | 943,40239 | 1921,92551 | €1.779,59 | €3.559,18 | €51,25 | €-8,14 |
| Combo Adaptive MFE Trail | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1868,12355 | 1863,85000 | 1841,22257 | 943,40239 | 1921,92551 | €1.710,41 | €3.420,83 | €49,26 | €-7,83 |
| Combo Adaptive MFE Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07231 | 0,07235 | 0,07335 | 0,10810 | 0,07022 | €1.693,88 | €3.387,77 | €48,78 | €-2,03 |
| Combo Adaptive MFE Trail | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.431,95 | €2.863,90 | €48,73 | €3,46 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1859,79188 | 1863,85000 | 1833,01088 | 1249,16022 | 1913,35389 | €1.151,05 | €3.453,16 | €49,73 | €7,53 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 1868,12355 | 1863,85000 | 1844,21157 | 1254,75632 | 1915,94751 | €1.302,08 | €3.906,25 | €50,00 | €-8,94 |
| Eth Bollinger 1H | ETH | SHORT | Bollinger mean reversion | 60m | 3,0x | 1867,37645 | 1863,85000 | 1889,78497 | 2480,49838 | 1833,76367 | €1.388,89 | €4.166,67 | €50,00 | €7,87 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1868,12355 | 1863,85000 | 1841,22257 | 1254,75632 | 1921,92551 | €1.151,05 | €3.453,16 | €49,73 | €-7,90 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07216 | 0,07235 | 0,07320 | 0,09585 | 0,07008 | €1.155,81 | €3.467,44 | €49,93 | €-9,29 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Benchmark Bollinger mean reversion 1H | PEPE | SHORT | 2026-07-19T20:08:29+00:00 | 0,00000 | €-4,14 | -0,08 | STOP |
| Rapida 1H V3 Filtered | BANK | LONG | 2026-07-19T19:38:30+00:00 | 0,23119 | €74,14 | 1,49 | TARGET |
| Rapida 1H V3 Filtered | PEPE | LONG | 2026-07-19T18:23:29+00:00 | 0,00000 | €-55,07 | -1,11 | STOP |
| Rapida 1H V1 | PEPE | LONG | 2026-07-19T18:23:29+00:00 | 0,00000 | €-53,96 | -1,11 | STOP |
| Forza relativa 1H V2 | BANK | LONG | 2026-07-19T18:00:13+00:00 | 0,19818 | €110,22 | 2,19 | TARGET |
| Rapida 1H V3 Filtered | BANK | LONG | 2026-07-19T17:23:30+00:00 | 0,19159 | €73,77 | 1,49 | TARGET |
| Bilanciata 1H V3 Filtered | BANK | LONG | 2026-07-19T17:23:30+00:00 | 0,19442 | €97,32 | 1,99 | TARGET |
| Bilanciata 1H V1 | BANK | LONG | 2026-07-19T17:08:29+00:00 | 0,18501 | €100,00 | 1,99 | TARGET |
| Bilanciata 1H V3 Filtered | ZEC | LONG | 2026-07-19T16:23:31+00:00 | 548,95732 | €-53,48 | -1,07 | STOP |
| Bilanciata 1H V2 | ZEC | LONG | 2026-07-19T16:23:31+00:00 | 548,95732 | €-54,15 | -1,07 | STOP |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | 2026-07-19T16:08:30+00:00 | 0,37604 | €-1,17 | -0,02 | TIME_EXIT_NO_CANDLES |
| Bilanciata 1H V1 | ALLO | SHORT | 2026-07-19T16:08:30+00:00 | 0,37604 | €-1,18 | -0,02 | TIME_EXIT_NO_CANDLES |

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
| MAIN | Principale 4H | 25/30 | 15/30 | 0,91 | 0,89 | -0,06R | €-3,37 | 4,26% | COERENTE − | RACCOLTA RESEARCH |
| RSI_EXTREME_LONG_15M | Scalp RSI Long 25 · prudente · 5x (riferimento tra 9 varianti) | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| RSI_EXTREME_SHORT_15M | Scalp RSI Short 75 · prudente · 5x (riferimento tra 9 varianti) | 5/30 | 4/30 | 0,32 | 0,30 | -0,55R | €-4,46 | 0,18% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED | Bilanciata 1H V1 | 88/30 | 13/30 | 1,09 | 1,99 | 0,06R | €12,85 | 1,12% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_BALANCED_V2 | Bilanciata 1H V2 | 10/30 | 11/30 | 1,86 | 1,10 | 0,46R | €2,48 | 2,10% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_BALANCED_V3 | Bilanciata 1H V3 Filtered | 17/30 | 14/30 | 1,67 | 1,07 | 0,37R | €2,16 | 2,20% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST | Rapida 1H V1 | 96/30 | 37/30 | 1,00 | 1,16 | 0,00R | €3,56 | 2,83% | COERENTE + | BOCCIATA RESEARCH |
| SHADOW_1H_FAST_V2 | Rapida 1H V2 | 1/30 | 1/30 | 1,19 | 11,45 | 0,11R | €31,39 | 0,93% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_1H_FAST_V3 | Rapida 1H V3 Filtered | 15/30 | 21/30 | 2,13 | 1,01 | 0,47R | €0,21 | 2,24% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_4H_WIDE | Ampia 4H | 23/30 | 10/30 | 1,19 | 1,60 | 0,14R | €15,71 | 2,08% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BOLLINGER_MR_1H | Benchmark Bollinger mean reversion 1H | 18/30 | 11/30 | 0,85 | 1,32 | -0,10R | €6,42 | 2,06% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_1H | Btc Adaptive 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,55 | 0,65% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_ADAPTIVE_4H | Btc Adaptive 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_1H | Btc Bollinger 1H | 1/30 | 1/30 | ∞ | ∞ | 1,37R | €68,69 | 0,31% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_BTC_BOLLINGER_4H | Btc Bollinger 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_1H | Btc Donchian 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,12R | €-55,12 | 0,67% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_DONCHIAN_4H | Btc Donchian 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_1H | Btc Ema 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,55 | 0,65% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_BTC_EMA_4H | Btc Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_COMBO_ADAPTIVE | Combo Adaptive | 42/30 | 14/30 | 1,86 | 2,15 | 0,45R | €18,04 | 1,01% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | Combo Adaptive MFE Trail | 12/30 | 12/30 | 1,94 | 0,18 | 0,48R | €-20,52 | 2,83% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_COMBO_MEAN_REVERSION | Combo Mean Reversion | 6/30 | 4/30 | 2,98 | 4,42 | 0,67R | €44,07 | 0,59% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_SCANNER | Combo Scanner | 28/30 | 10/30 | 1,81 | 1,21 | 0,45R | €5,53 | 1,69% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_COMBO_TREND | Combo Trend | 32/30 | 8/30 | 1,42 | 2,07 | 0,26R | €21,33 | 1,48% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_DOGE_BOLLINGER_1H | Doge Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_DONCHIAN_1H | Doge Donchian 1H | 0/30 | 1/30 | 0,00 | ∞ | 0,00R | €26,22 | 0,36% | n/a | RACCOLTA RESEARCH |
| SHADOW_DOGE_EMA_1H | Doge Ema 1H | 0/30 | 2/30 | 0,00 | 0,75 | 0,00R | €-6,89 | 1,17% | n/a | RACCOLTA RESEARCH |
| SHADOW_DONCHIAN_1H | Benchmark Donchian breakout 1H | 17/30 | 11/30 | 0,71 | 2,08 | -0,24R | €21,30 | 1,98% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_EMA_TREND_1H | Benchmark trend following EMA 1H | 38/30 | 4/30 | 1,21 | 1,28 | 0,14R | €7,56 | 1,10% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_ETH_ADAPTIVE_1H | Eth Adaptive 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,90 | 0,77% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_BOLLINGER_1H | Eth Bollinger 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,26% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_DONCHIAN_1H | Eth Donchian 1H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,38% | n/a | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_1H | Eth Ema 1H | 1/30 | 1/30 | 0,00 | 0,00 | -1,11R | €-54,90 | 0,61% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_ETH_EMA_4H | Eth Ema 4H | 0/30 | 0/30 | 0,00 | 0,00 | 0,00R | €0,00 | 0,00% | n/a | RACCOLTA RESEARCH |
| SHADOW_GLOBAL_PURE | Global Confluence puro 1H | 1/30 | 3/30 | 0,00 | 0,35 | -1,10R | €-23,73 | 1,19% | COERENTE − | RACCOLTA RESEARCH |
| SHADOW_RELATIVE_STRENGTH | Forza relativa 1H V1 | 55/30 | 9/30 | 1,19 | 1,53 | 0,13R | €9,53 | 1,84% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_RELATIVE_STRENGTH_V2 | Forza relativa 1H V2 | 14/30 | 12/30 | 2,44 | 1,69 | 0,69R | €14,93 | 2,32% | COERENTE + | RACCOLTA RESEARCH |
| SHADOW_SCANNER_BOTTOM5_SHORT | Scanner Bottom 5 Short 1H | 13/30 | 6/30 | 0,89 | 1,26 | -0,07R | €4,73 | 1,90% | DIVERGENTE | RACCOLTA RESEARCH |
| SHADOW_SCANNER_TOP5_BTC | Scanner Top 5 + forza BTC 1H | 30/30 | 12/30 | 1,82 | 2,51 | 0,46R | €27,14 | 1,62% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
| SHADOW_SCANNER_TOP5_LONG | Scanner Top 5 Long 1H | 40/30 | 15/30 | 1,60 | 2,28 | 0,33R | €23,40 | 2,12% | COERENTE + | SEGNALE VALIDATO · PAPER IN RACCOLTA |
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
- Prezzo DOGE: **0.07235**
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
| BTC sotto filtro | 64454.8 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, bearish_confirmation**
- High **0.07235**; close **0.07229**; wick alta **100.0%**; volume **x0.07**

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
- Confidenza: **73,10%**
- Volatilità: **NORMAL**
- Rotazione strategie: **SOLO OSSERVAZIONE — nessun peso operativo viene ancora modificato**
- Motivo: Trend BTC rialzista confermato dalla breadth: score +3.0, 75% sopra EMA50, ADX 22.5.
- BTC trend score: **3,00**; ADX: **22,53**; breadth sopra EMA50: **75,00%**
- Mediana alt vs BTC: **0,23%**; dispersione: **32,85%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **163**
- Trade research chiusi: **640**
- Eventi di mercato indipendenti chiusi: **248**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **1903**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 10 | 25 | 25 | 32,00% | 0,91 | -0,06R | €-16,19 |
| RSI_EXTREME_SHORT_15M | 0 | 5 | 5 | 20,00% | 0,32 | -0,55R | €-27,64 |
| Bilanciata 1H V1 | 13 | 88 | 88 | 36,36% | 1,09 | 0,06R | €49,38 |
| Bilanciata 1H V2 | 8 | 10 | 10 | 50,00% | 1,86 | 0,46R | €45,94 |
| Bilanciata 1H V3 Filtered | 4 | 17 | 17 | 47,06% | 1,67 | 0,37R | €63,48 |
| Rapida 1H V1 | 8 | 96 | 96 | 41,67% | 1,00 | 0,00R | €0,85 |
| Rapida 1H V2 | 0 | 2 | 1 | 50,00% | 1,19 | 0,11R | €2,14 |
| Rapida 1H V3 Filtered | 6 | 15 | 15 | 60,00% | 2,13 | 0,47R | €70,34 |
| SHADOW_4H_WIDE | 16 | 23 | 23 | 30,43% | 1,19 | 0,14R | €31,33 |
| SHADOW_BOLLINGER_MR_1H | 2 | 18 | 18 | 38,89% | 0,85 | -0,10R | €-17,24 |
| SHADOW_BTC_ADAPTIVE_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_BOLLINGER_1H | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_DONCHIAN_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_EMA_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_ADAPTIVE | 11 | 42 | 42 | 50,00% | 1,86 | 0,45R | €190,59 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | 6 | 12 | 12 | 50,00% | 1,94 | 0,48R | €57,42 |
| SHADOW_COMBO_MEAN_REVERSION | 0 | 6 | 6 | 66,67% | 2,98 | 0,67R | €40,29 |
| SHADOW_COMBO_SCANNER | 6 | 28 | 28 | 46,43% | 1,81 | 0,45R | €126,56 |
| SHADOW_COMBO_TREND | 10 | 32 | 32 | 40,62% | 1,42 | 0,26R | €84,11 |
| SHADOW_DOGE_DONCHIAN_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_EMA_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | 7 | 17 | 17 | 23,53% | 0,71 | -0,24R | €-39,97 |
| SHADOW_EMA_TREND_1H | 12 | 38 | 38 | 36,84% | 1,21 | 0,14R | €52,20 |
| SHADOW_ETH_ADAPTIVE_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_BOLLINGER_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_DONCHIAN_1H | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_1H | 1 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_GLOBAL_PURE | 1 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| Forza relativa 1H V1 | 13 | 55 | 55 | 36,36% | 1,19 | 0,13R | €70,46 |
| Forza relativa 1H V2 | 5 | 15 | 14 | 53,33% | 2,44 | 0,69R | €103,22 |
| SHADOW_SCANNER_BOTTOM5_SHORT | 7 | 13 | 13 | 30,77% | 0,89 | -0,07R | €-9,36 |
| SHADOW_SCANNER_TOP5_BTC | 6 | 30 | 30 | 46,67% | 1,82 | 0,46R | €137,74 |
| SHADOW_SCANNER_TOP5_LONG | 6 | 40 | 40 | 45,00% | 1,60 | 0,33R | €133,02 |
| SHADOW_SOL_ADAPTIVE_1H | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |
| SHADOW_SOL_BOLLINGER_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_DONCHIAN_1H | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_SOL_EMA_1H | 0 | 2 | 2 | 50,00% | 1,70 | 0,39R | €7,78 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | ALT_ROTATION_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| MAIN | RANGE | 1 | 13 | 13 | 30,77% | 0,86 | -0,10R | €-13,29 |
| MAIN | TRANSITION | 5 | 3 | 3 | 33,33% | 0,97 | -0,02R | €-0,54 |
| MAIN | TREND_UP | 3 | 7 | 7 | 42,86% | 1,43 | 0,26R | €17,90 |
| RSI_EXTREME_SHORT_15M | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,09R | €-10,90 |
| RSI_EXTREME_SHORT_15M | TRANSITION | 0 | 1 | 1 | 0,00% | 0,00 | -0,41R | €-4,13 |
| RSI_EXTREME_SHORT_15M | TREND_UP | 0 | 3 | 3 | 33,33% | 0,50 | -0,42R | €-12,61 |
| Bilanciata 1H V1 | ALT_ROTATION_UP | 2 | 11 | 11 | 45,45% | 1,54 | 0,31R | €33,93 |
| Bilanciata 1H V1 | RANGE | 4 | 24 | 24 | 33,33% | 0,97 | -0,02R | €-4,19 |
| Bilanciata 1H V1 | RANGE_HIGH_VOL | 0 | 9 | 9 | 0,00% | 0,00 | -1,08R | €-97,25 |
| Bilanciata 1H V1 | TRANSITION | 5 | 18 | 18 | 44,44% | 1,46 | 0,27R | €49,04 |
| Bilanciata 1H V1 | TREND_UP | 2 | 26 | 26 | 42,31% | 1,45 | 0,26R | €67,84 |
| Bilanciata 1H V2 | ALT_ROTATION_UP | 3 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Bilanciata 1H V2 | RANGE | 2 | 4 | 4 | 50,00% | 1,79 | 0,44R | €17,51 |
| Bilanciata 1H V2 | TRANSITION | 3 | 6 | 6 | 50,00% | 1,91 | 0,47R | €28,43 |
| Bilanciata 1H V3 Filtered | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| Bilanciata 1H V3 Filtered | TRANSITION | 1 | 5 | 5 | 40,00% | 1,24 | 0,15R | €7,67 |
| Bilanciata 1H V3 Filtered | TREND_UP | 3 | 11 | 11 | 54,55% | 2,26 | 0,60R | €65,94 |
| Rapida 1H V1 | ALT_ROTATION_UP | 0 | 8 | 8 | 50,00% | 1,40 | 0,21R | €16,81 |
| Rapida 1H V1 | RANGE | 2 | 33 | 33 | 42,42% | 1,05 | 0,03R | €8,73 |
| Rapida 1H V1 | RANGE_HIGH_VOL | 0 | 10 | 10 | 0,00% | 0,00 | -1,10R | €-109,76 |
| Rapida 1H V1 | TRANSITION | 2 | 17 | 17 | 58,82% | 2,27 | 0,48R | €81,49 |
| Rapida 1H V1 | TREND_UP | 4 | 28 | 28 | 42,86% | 1,02 | 0,01R | €3,58 |
| Rapida 1H V2 | RANGE | 0 | 2 | 1 | 50,00% | 1,19 | 0,11R | €2,14 |
| Rapida 1H V3 Filtered | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,48R | €14,83 |
| Rapida 1H V3 Filtered | TRANSITION | 1 | 3 | 3 | 66,67% | 2,93 | 0,65R | €19,60 |
| Rapida 1H V3 Filtered | TREND_UP | 5 | 11 | 11 | 54,55% | 1,69 | 0,33R | €35,91 |
| SHADOW_4H_WIDE | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_4H_WIDE | RANGE | 6 | 11 | 11 | 27,27% | 1,02 | 0,01R | €1,48 |
| SHADOW_4H_WIDE | TRANSITION | 6 | 4 | 4 | 25,00% | 0,92 | -0,06R | €-2,53 |
| SHADOW_4H_WIDE | TREND_UP | 4 | 6 | 6 | 50,00% | 2,70 | 0,88R | €52,66 |
| SHADOW_BOLLINGER_MR_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,30 |
| SHADOW_BOLLINGER_MR_1H | RANGE | 0 | 7 | 7 | 42,86% | 0,98 | -0,01R | €-0,83 |
| SHADOW_BOLLINGER_MR_1H | TRANSITION | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,14 |
| SHADOW_BOLLINGER_MR_1H | TREND_UP | 2 | 6 | 6 | 50,00% | 1,31 | 0,17R | €10,03 |
| SHADOW_BTC_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_BTC_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 100,00% | ∞ | 1,37R | €13,67 |
| SHADOW_BTC_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_BTC_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_COMBO_ADAPTIVE | ALT_ROTATION_UP | 1 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_COMBO_ADAPTIVE | RANGE | 5 | 7 | 7 | 42,86% | 1,34 | 0,21R | €14,90 |
| SHADOW_COMBO_ADAPTIVE | TRANSITION | 3 | 13 | 13 | 53,85% | 2,19 | 0,57R | €74,23 |
| SHADOW_COMBO_ADAPTIVE | TREND_UP | 2 | 20 | 20 | 55,00% | 2,29 | 0,61R | €121,73 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | ALT_ROTATION_UP | 2 | 2 | 2 | 0,00% | 0,00 | -1,01R | €-20,27 |
| SHADOW_COMBO_ADAPTIVE_MFE_TRAIL | TREND_UP | 4 | 10 | 10 | 60,00% | 2,92 | 0,78R | €77,69 |
| SHADOW_COMBO_MEAN_REVERSION | RANGE | 0 | 4 | 4 | 75,00% | 4,46 | 0,88R | €35,25 |
| SHADOW_COMBO_MEAN_REVERSION | TREND_UP | 0 | 2 | 2 | 50,00% | 1,50 | 0,25R | €5,04 |
| SHADOW_COMBO_SCANNER | ALT_ROTATION_UP | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,73 |
| SHADOW_COMBO_SCANNER | RANGE | 1 | 1 | 1 | 100,00% | ∞ | 2,19R | €21,87 |
| SHADOW_COMBO_SCANNER | TRANSITION | 2 | 10 | 10 | 40,00% | 1,40 | 0,25R | €25,03 |
| SHADOW_COMBO_SCANNER | TREND_UP | 2 | 15 | 15 | 46,67% | 1,81 | 0,45R | €67,93 |
| SHADOW_COMBO_TREND | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,73 |
| SHADOW_COMBO_TREND | RANGE | 3 | 5 | 5 | 20,00% | 0,51 | -0,42R | €-20,81 |
| SHADOW_COMBO_TREND | TRANSITION | 3 | 12 | 12 | 50,00% | 2,09 | 0,56R | €67,72 |
| SHADOW_COMBO_TREND | TREND_UP | 4 | 13 | 13 | 38,46% | 1,30 | 0,20R | €25,47 |
| SHADOW_DOGE_DONCHIAN_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DOGE_EMA_1H | RANGE | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_DONCHIAN_1H | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_DONCHIAN_1H | RANGE | 3 | 5 | 5 | 20,00% | 0,57 | -0,37R | €-18,56 |
| SHADOW_DONCHIAN_1H | TRANSITION | 1 | 4 | 4 | 25,00% | 0,78 | -0,17R | €-6,95 |
| SHADOW_DONCHIAN_1H | TREND_UP | 3 | 7 | 7 | 28,57% | 0,92 | -0,06R | €-4,34 |
| SHADOW_EMA_TREND_1H | ALT_ROTATION_UP | 0 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,73 |
| SHADOW_EMA_TREND_1H | RANGE | 4 | 6 | 6 | 16,67% | 0,41 | -0,52R | €-30,95 |
| SHADOW_EMA_TREND_1H | TRANSITION | 3 | 12 | 12 | 50,00% | 2,09 | 0,56R | €67,70 |
| SHADOW_EMA_TREND_1H | TREND_UP | 5 | 18 | 18 | 33,33% | 1,03 | 0,02R | €3,71 |
| SHADOW_ETH_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_ADAPTIVE_1H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_BOLLINGER_1H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_DONCHIAN_1H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_ETH_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_ETH_EMA_1H | TREND_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_GLOBAL_PURE | ALT_ROTATION_UP | 0 | 1 | 1 | 0,00% | 0,00 | -1,10R | €-11,00 |
| SHADOW_GLOBAL_PURE | TRANSITION | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V1 | ALT_ROTATION_UP | 0 | 10 | 10 | 30,00% | 0,88 | -0,09R | €-8,74 |
| Forza relativa 1H V1 | RANGE | 4 | 16 | 16 | 25,00% | 0,69 | -0,24R | €-38,67 |
| Forza relativa 1H V1 | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |
| Forza relativa 1H V1 | TRANSITION | 1 | 11 | 11 | 54,55% | 2,55 | 0,72R | €78,82 |
| Forza relativa 1H V1 | TREND_UP | 8 | 16 | 16 | 43,75% | 1,63 | 0,37R | €59,38 |
| Forza relativa 1H V2 | ALT_ROTATION_UP | 1 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| Forza relativa 1H V2 | RANGE | 1 | 2 | 2 | 50,00% | 2,16 | 0,59R | €11,72 |
| Forza relativa 1H V2 | TRANSITION | 2 | 6 | 6 | 50,00% | 2,10 | 0,57R | €34,43 |
| Forza relativa 1H V2 | TREND_UP | 1 | 7 | 6 | 57,14% | 2,88 | 0,82R | €57,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT | ALT_ROTATION_UP | 0 | 1 | 1 | 100,00% | ∞ | 1,99R | €19,87 |
| SHADOW_SCANNER_BOTTOM5_SHORT | RANGE | 2 | 5 | 5 | 0,00% | 0,00 | -1,08R | €-54,07 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TRANSITION | 4 | 5 | 5 | 60,00% | 2,60 | 0,70R | €35,18 |
| SHADOW_SCANNER_BOTTOM5_SHORT | TREND_UP | 1 | 2 | 2 | 0,00% | 0,00 | -0,52R | €-10,34 |
| SHADOW_SCANNER_TOP5_BTC | ALT_ROTATION_UP | 1 | 3 | 3 | 33,33% | 1,06 | 0,04R | €1,21 |
| SHADOW_SCANNER_TOP5_BTC | RANGE | 2 | 3 | 3 | 100,00% | ∞ | 2,14R | €64,28 |
| SHADOW_SCANNER_TOP5_BTC | TRANSITION | 1 | 10 | 10 | 40,00% | 1,40 | 0,25R | €25,03 |
| SHADOW_SCANNER_TOP5_BTC | TREND_UP | 2 | 14 | 14 | 42,86% | 1,56 | 0,34R | €47,22 |
| SHADOW_SCANNER_TOP5_LONG | ALT_ROTATION_UP | 2 | 3 | 3 | 0,00% | 0,00 | -1,05R | €-31,38 |
| SHADOW_SCANNER_TOP5_LONG | RANGE | 1 | 5 | 5 | 80,00% | 125,19 | 1,55R | €77,53 |
| SHADOW_SCANNER_TOP5_LONG | TRANSITION | 1 | 10 | 10 | 40,00% | 1,27 | 0,17R | €17,03 |
| SHADOW_SCANNER_TOP5_LONG | TREND_UP | 2 | 22 | 22 | 45,45% | 1,55 | 0,32R | €69,85 |
| SHADOW_SOL_ADAPTIVE_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_ADAPTIVE_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |
| SHADOW_SOL_BOLLINGER_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,13R | €-11,33 |
| SHADOW_SOL_DONCHIAN_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,12R | €-11,25 |
| SHADOW_SOL_EMA_1H | RANGE | 0 | 1 | 1 | 0,00% | 0,00 | -1,11R | €-11,11 |
| SHADOW_SOL_EMA_1H | TRANSITION | 0 | 1 | 1 | 100,00% | ∞ | 1,89R | €18,89 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.

# Block 3 — Shadow Exit Engine

Generato: 2026-07-19T20:53:35+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **70**
- Scenari virtuali ancora attivi: **1146**
- Gruppi in attesa dell'uscita originale: **68**
- Gruppi con originale chiuso ma Shadow ancora attive: **2**
- Confronti completati: **59**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 0 | 3 | +€13,27 | 66,7% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR15_R100 | 0 | 2 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR20_R100 | 0 | 2 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| ATR30_R100 | 0 | 2 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| BE_R100 | 0 | 2 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| TIME_12H | 0 | 2 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| TIME_24H | 0 | 2 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| TP_R150 | 0 | 3 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| TP_R200 | 0 | 2 | €0,00 | 0,0% | 0 | 0 | WAITING_FULL_SAMPLE |
| GB20_R050 | 0 | 4 | €-2,92 | 25,0% | 1 | 0 | WAITING_FULL_SAMPLE |
| GB20_R100 | 0 | 3 | €-3,88 | 0,0% | 1 | 0 | WAITING_FULL_SAMPLE |
| GB30_R050 | 0 | 4 | €-4,92 | 25,0% | 1 | 0 | WAITING_FULL_SAMPLE |
| TP_R050 | 0 | 4 | €-6,41 | 25,0% | 1 | 0 | WAITING_FULL_SAMPLE |
| GB30_R100 | 0 | 3 | €-6,51 | 0,0% | 1 | 0 | WAITING_FULL_SAMPLE |
| GB40_R050 | 0 | 4 | €-6,92 | 25,0% | 1 | 0 | WAITING_FULL_SAMPLE |
| TP_R100 | 0 | 3 | €-8,30 | 0,0% | 1 | 0 | WAITING_FULL_SAMPLE |
| GB40_R100 | 0 | 3 | €-8,35 | 0,0% | 0 | 1 | WAITING_FULL_SAMPLE |
| GB50_R050 | 0 | 4 | €-8,92 | 25,0% | 1 | 0 | WAITING_FULL_SAMPLE |
| GB50_R100 | 0 | 3 | €-11,11 | 0,0% | 0 | 1 | WAITING_FULL_SAMPLE |
| BE_R050 | 0 | 4 | €-18,93 | 0,0% | 2 | 0 | WAITING_FULL_SAMPLE |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.

# Blocco 4 — Valutazione statistica Shadow

Generato: 2026-07-19T20:53:35+00:00

> Modulo esclusivamente valutativo. Non modifica strategie, uscite, posizioni o capitale. Le candidature vengono consegnate al futuro Blocco 5, senza applicazione automatica.

## Stato

- Risultati Block 3 disponibili: **59**
- Valutazioni prodotte: **146**
- Candidature al Blocco 5: **0**
- Mutazioni create automaticamente: **0**

## Classifica complessiva

| Scenario | Campione pieno | Δ medio (R) | Mediana (R) | CI bootstrap basso | Migliora | Score | Stato |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ATR15_R100 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| ATR20_R100 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| ATR30_R100 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| BE_R050 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| BE_R100 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| GB20_R050 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| GB20_R100 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| GB30_R050 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| GB30_R100 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| GB40_R050 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| GB40_R100 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| GB50_R050 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| GB50_R100 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| TIME_12H | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| TIME_24H | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| TIME_6H | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| TP_R050 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| TP_R100 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| TP_R150 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |
| TP_R200 | 0 | 0,000 | 0,000 | 0,000 | 0,0% | 25,0 | INSUFFICIENT_DATA |

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

Generato: 2026-07-19T20:53:30+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **0**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **0.00 R**
- Profitto virtuale mancato: **0.00 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 39 | 0 | 7212.19 |
| DOWN_20 | 39 | 0 | 14424.38 |
| DOWN_30 | 39 | 0 | 21636.56 |
| DOWN_40 | 39 | 11 | 26820.85 |
| UP_10 | 29 | 0 | 5906.83 |
| UP_20 | 29 | 0 | 11813.66 |
| UP_30 | 29 | 1 | 17751.81 |
| UP_40 | 29 | 13 | 21855.93 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
