# Paper trading automatico KuCoin

Generato: 2026-07-20T05:15:00+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-20T05:10:10+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-20T05:10:10+00:00 | 2026-07-20T05:10:10+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-20T04:45:00+00:00 | 2026-07-20T04:45:00+00:00 | 10,2 min | 25,0 min | OK |
| 60m | 12 | 2026-07-20T04:00:00+00:00 | 2026-07-20T04:00:00+00:00 | 10,2 min | 45,0 min | OK |
| 240m | 12 | 2026-07-20T00:00:00+00:00 | 2026-07-20T00:00:00+00:00 | 1,17 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | PEPE | 240m | LONG | 8,01 | 6,00 | 0,00 | STALE_CANDLE | 1,17 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 70.2 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,17 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 70.2 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,17 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 70.2 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,17 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 70.2 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 5,47 | 6,00 | 0,53 | STALE_CANDLE | 1,17 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 70.2 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,17 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 70.2 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -3,97 | 6,00 | 2,03 | STALE_CANDLE | 1,17 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 70.2 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 3,02 | 6,00 | 2,98 | STALE_CANDLE | 1,17 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 70.2 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -1,90 | 6,00 | 4,10 | STALE_CANDLE | 1,17 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 70.2 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 1,56 | 6,00 | 4,44 | STALE_CANDLE | 1,17 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 70.2 minuti; tolleranza 60 minuti. |
| Principale 4H | ESPORTS | 240m | SHORT | -0,75 | 6,00 | 5,25 | STALE_CANDLE | 1,17 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 70.2 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -0,15 | 6,00 | 5,85 | STALE_CANDLE | 1,17 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 70.2 minuti; tolleranza 60 minuti. |
| Rapida 1H V3 Filtered | ESPORTS | 60m | SHORT | -6,75 | 4,50 | 0,00 | READY | 10,2 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | ESPORTS | 60m | SHORT | -6,75 | 5,50 | 0,00 | STRATEGY_FILTER | 10,2 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | ESPORTS | 60m | SHORT | -6,75 | 5,00 | 0,00 | STRATEGY_FILTER | 10,2 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Bilanciata 1H V2 | PEPE | 60m | LONG | 6,40 | 5,50 | 0,00 | STRATEGY_FILTER | 10,2 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | PEPE | 60m | LONG | 6,40 | 5,00 | 0,00 | STRATEGY_FILTER | 10,2 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Bilanciata 1H V2 | HYPE | 60m | SHORT | -5,98 | 5,50 | 0,00 | STRATEGY_FILTER | 10,2 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 | HYPE | 60m | SHORT | -5,98 | 4,50 | 0,00 | STRATEGY_FILTER | 10,2 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-1.44%. |
| Rapida 1H V2 | HYPE | 60m | SHORT | -5,98 | 5,00 | 0,00 | STRATEGY_FILTER | 10,2 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.918,09 | -0,82% | €-81,91 | €3.000,00 | -2,73% | 4 | 15 | 33,33% | 0,89 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 15 | 185 | CAMPIONE INSUFFICIENTE | 30 (mancano 15) |

- Trade del Principale 4H chiusi: **15**; win rate **33,33%**; profit factor **0,89**.
- Expectancy: **€-3,37** per trade; P&L netto: **€-50,49**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.918,09 | €1.317,93 | €3.953,78 | €197,45 | €-31,01 |
| TEST | Forza relativa 1H V2 | 3 | €10.363,91 | €2.242,62 | €4.485,24 | €152,64 | €-28,86 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.344,28 | €1.866,89 | €3.733,78 | €101,31 | €75,79 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.317,49 | €1.918,88 | €3.837,75 | €103,58 | €50,89 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.300,90 | €3.169,51 | €6.339,03 | €101,94 | €71,35 |
| TEST | Combo Adaptive | 3 | €10.239,86 | €3.522,36 | €7.044,73 | €153,58 | €-8,07 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.218,10 | €3.232,64 | €9.697,93 | €201,84 | €-2,49 |
| TEST | Bilanciata 1H V1 | 4 | €10.205,92 | €2.460,54 | €7.381,63 | €202,00 | €-1,25 |
| TEST | Rapida 1H V1 | 4 | €10.173,91 | €2.761,39 | €8.284,16 | €202,97 | €27,59 |
| TEST | Ampia 4H | 4 | €10.138,48 | €1.846,89 | €3.693,78 | €200,81 | €-0,44 |
| TEST | Benchmark Bollinger mean reversion 1H | 3 | €10.132,90 | €3.609,24 | €7.218,48 | €97,61 | €66,51 |
| TEST | Combo Mean Reversion | 1 | €10.120,96 | €281,61 | €563,22 | €50,37 | €0,00 |
| TEST | Combo Trend | 3 | €10.084,39 | €2.096,20 | €4.192,40 | €100,32 | €74,44 |
| TEST | Combo Scanner | 3 | €10.079,41 | €2.570,72 | €5.141,43 | €100,41 | €79,00 |
| TEST | Forza relativa 1H V1 | 4 | €10.074,76 | €2.575,12 | €5.150,25 | €151,44 | €22,72 |
| TEST | Btc Bollinger 1H | 0 | €10.068,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €10.062,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.026,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 1 | €10.005,71 | €1.388,89 | €4.166,67 | €50,00 | €7,78 |
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
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.993,79 | €3.459,61 | €6.919,22 | €99,92 | €21,03 |
| TEST | Doge Ema 1H | 1 | €9.991,13 | €1.155,81 | €3.467,44 | €49,93 | €5,61 |
| TEST | Sol Ema 1H | 0 | €9.990,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €9.988,40 | €1.302,08 | €3.906,25 | €50,00 | €-8,85 |
| TEST | Bilanciata 1H V2 | 2 | €9.985,74 | €709,89 | €2.129,66 | €99,11 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.982,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.981,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.979,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.945,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.944,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 1 | €9.934,84 | €1.151,05 | €3.453,16 | €49,73 | €-7,83 |
| TEST | Global Confluence puro 1H | 1 | €9.933,09 | €1.551,38 | €3.102,75 | €49,64 | €4,59 |
| TEST | Eth Ema 1H | 1 | €9.927,07 | €1.152,05 | €3.456,15 | €49,77 | €-24,57 |
| TEST | Btc Ema 1H | 1 | €9.922,60 | €1.151,09 | €3.453,28 | €49,73 | €-20,78 |
| TEST | Rapida 1H V3 Filtered | 3 | €9.919,28 | €1.959,78 | €5.879,33 | €149,05 | €29,76 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.911,61 | €2.193,79 | €4.387,58 | €149,10 | €-11,53 |
| TEST | Combo Adaptive Mfe Trail | 3 | €9.808,18 | €4.167,67 | €8.335,35 | €146,59 | €20,05 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.918,09 | €-50,49 | 15 | 15 | 33,33% | 0,89 | €-3,37 | 4,26% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.363,91 | €395,30 | 14 | 14 | 42,86% | 2,51 | €28,24 | 2,32% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.344,28 | €270,73 | 13 | 13 | 46,15% | 2,00 | €20,83 | 1,62% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.317,49 | €268,97 | 18 | 18 | 44,44% | 1,75 | €14,94 | 2,19% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.300,90 | €234,28 | 11 | 11 | 54,55% | 2,08 | €21,30 | 1,98% |
| TEST | Combo Adaptive | Combo Adaptive | €10.239,86 | €252,59 | 14 | 14 | 42,86% | 2,15 | €18,04 | 1,01% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.218,10 | €224,87 | 16 | 16 | 43,75% | 1,54 | €14,05 | 2,20% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.205,92 | €211,07 | 16 | 16 | 43,75% | 1,94 | €13,19 | 1,12% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.173,91 | €151,19 | 39 | 39 | 41,03% | 1,17 | €3,88 | 2,83% |
| TEST | Ampia 4H | Confluenza trend | €10.138,48 | €139,54 | 11 | 11 | 27,27% | 1,50 | €12,69 | 2,08% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.132,90 | €70,65 | 11 | 11 | 45,45% | 1,32 | €6,42 | 2,06% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.120,96 | €121,64 | 5 | 5 | 60,00% | 2,15 | €24,33 | 0,59% |
| TEST | Combo Trend | Combo Trend | €10.084,39 | €12,52 | 11 | 11 | 36,36% | 1,04 | €1,14 | 1,99% |
| TEST | Combo Scanner | Combo Scanner | €10.079,41 | €1,79 | 11 | 11 | 36,36% | 1,01 | €0,16 | 1,69% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €10.074,76 | €55,13 | 12 | 12 | 41,67% | 1,29 | €4,59 | 1,84% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.068,69 | €68,69 | 1 | 1 | 100,00% | ∞ | €68,69 | 0,31% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.062,78 | €62,78 | 2 | 1 | 50,00% | 11,45 | €31,39 | 0,93% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.026,22 | €26,22 | 1 | 1 | 100,00% | ∞ | €26,22 | 0,36% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.005,71 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,51% |
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
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.993,79 | €-25,03 | 7 | 7 | 42,86% | 0,84 | €-3,58 | 2,43% |
| TEST | Doge Ema 1H | Trend following EMA | €9.991,13 | €-13,78 | 2 | 2 | 50,00% | 0,75 | €-6,89 | 1,17% |
| TEST | Sol Ema 1H | Trend following EMA | €9.990,84 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 0,87% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.988,40 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,38% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.985,74 | €-13,16 | 15 | 13 | 46,67% | 0,97 | €-0,88 | 2,10% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.982,18 | €-17,82 | 4 | 4 | 25,00% | 0,30 | €-4,46 | 0,18% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.981,55 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 0,89% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.979,87 | €-20,13 | 4 | 4 | 25,00% | 0,18 | €-5,03 | 0,20% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.945,45 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,65% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.944,88 | €-55,12 | 1 | 1 | 0,00% | 0,00 | €-55,12 | 0,67% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.934,84 | €-54,90 | 1 | 1 | 0,00% | 0,00 | €-54,90 | 0,77% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.933,09 | €-71,19 | 3 | 3 | 33,33% | 0,35 | €-23,73 | 1,19% |
| TEST | Eth Ema 1H | Trend following EMA | €9.927,07 | €-46,28 | 2 | 2 | 50,00% | 0,16 | €-23,14 | 0,73% |
| TEST | Btc Ema 1H | Trend following EMA | €9.922,60 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,88% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.919,28 | €-106,95 | 26 | 26 | 30,77% | 0,81 | €-4,11 | 2,24% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.911,61 | €-74,23 | 6 | 6 | 33,33% | 0,65 | €-12,37 | 1,56% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.808,18 | €-207,55 | 15 | 15 | 26,67% | 0,31 | €-13,84 | 2,87% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07204 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €20,69 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 59,36013 | 59,99900 | 62,47190 | 78,85003 | 53,13657 | €313,25 | €939,76 | €49,26 | €-10,11 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,19982 | 0,23699 | 0,13559 | €136,26 | €408,77 | €49,05 | €-0,00 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 556,07119 | 529,85000 | 524,63715 | 373,49448 | 618,93927 | €293,97 | €881,92 | €49,85 | €-41,59 |
| Bilanciata 1H V1 | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €143,84 | €431,52 | €50,35 | €-0,00 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,37613 | 0,37613 | 0,36189 | 0,25263 | 0,40460 | €442,89 | €1.328,68 | €50,30 | €0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,07253 | 0,07204 | 0,07357 | 0,09634 | 0,07044 | €1.164,82 | €3.494,46 | €50,32 | €23,44 |
| Bilanciata 1H V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €708,99 | €2.126,97 | €51,03 | €-24,69 |
| Bilanciata 1H V2 | LAB | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €139,69 | €419,08 | €48,90 | €-0,00 |
| Bilanciata 1H V2 | GRAM | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,49240 | 1,49240 | 1,53621 | 1,98241 | 1,40478 | €570,19 | €1.710,58 | €50,21 | €-0,00 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,07217 | 0,07204 | 0,07321 | 0,09586 | 0,07009 | €1.157,41 | €3.472,22 | €50,00 | €6,09 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1867,19336 | 1863,89000 | 1840,30578 | 1254,13154 | 1920,96853 | €1.152,16 | €3.456,47 | €49,77 | €-6,12 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €780,89 | €2.342,68 | €50,88 | €-24,70 |
| Bilanciata 1H V3 Filtered | BANK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,24392 | 0,25663 | 0,21465 | 0,16383 | 0,30246 | €142,18 | €426,55 | €51,19 | €22,23 |
| Rapida 1H V1 | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,18833 | 0,18833 | 0,20479 | 0,25016 | 0,16363 | €195,85 | €587,54 | €51,37 | €-0,00 |
| Rapida 1H V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,37292 | 0,37292 | 0,36188 | 0,25048 | 0,38949 | €580,83 | €1.742,48 | €51,60 | €0,00 |
| Rapida 1H V1 | GRAM | SHORT | Momentum / breakout | 60m | 3,0x | 1,49240 | 1,49240 | 1,52648 | 1,98241 | 1,44129 | €757,31 | €2.271,94 | €51,87 | €-0,00 |
| Rapida 1H V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 60,45191 | 59,99900 | 61,24207 | 80,30028 | 59,26667 | €1.227,40 | €3.682,20 | €48,13 | €27,59 |
| Rapida 1H V3 Filtered | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,24392 | 0,25663 | 0,21465 | 0,16383 | 0,28782 | €138,12 | €414,35 | €49,72 | €21,59 |
| Rapida 1H V3 Filtered | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 537,32251 | 529,85000 | 546,84245 | 713,74341 | 523,04261 | €935,44 | €2.806,32 | €49,72 | €39,03 |
| Rapida 1H V3 Filtered | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €886,22 | €2.658,66 | €49,61 | €-30,86 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07204 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €5,86 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 529,85000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €9,53 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 59,36013 | 59,99900 | 63,40544 | 88,74339 | 48,03325 | €367,70 | €735,40 | €50,12 | €-7,91 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €-7,91 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H V1 | ALLO | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Forza relativa 1H V1 | BANK | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,23050 | 0,25663 | 0,23050 | 0,11640 | 0,29135 | €208,05 | €416,10 | €0,00 | €47,18 |
| Forza relativa 1H V1 | PEPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.053,59 | €2.107,17 | €50,55 | €-24,46 |
| Forza relativa 1H V2 | LAB | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18833 | 0,18833 | 0,20950 | 0,28155 | 0,14176 | €222,78 | €445,56 | €50,08 | €-0,00 |
| Forza relativa 1H V2 | GRAM | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,47771 | 1,47771 | 1,52060 | 2,20918 | 1,38336 | €871,54 | €1.743,07 | €50,59 | €-0,00 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.148,31 | €2.296,61 | €51,97 | €-28,86 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1868,12355 | 1863,89000 | 1838,23357 | 943,40239 | 1942,84849 | €1.585,47 | €3.170,93 | €50,73 | €-7,19 |
| Benchmark Donchian breakout 1H | BANK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,22677 | 0,25663 | 0,22677 | 0,11452 | 0,29479 | €213,00 | €426,01 | €0,00 | €56,10 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 60,49390 | 59,99900 | 61,62348 | 90,43838 | 57,66993 | €1.371,04 | €2.742,09 | €51,20 | €22,43 |
| Benchmark Bollinger mean reversion 1H | LAB | LONG | Bollinger mean reversion | 60m | 2,0x | 0,18881 | 0,18881 | 0,17193 | 0,09535 | 0,21414 | €277,38 | €554,76 | €49,61 | €0,00 |
| Benchmark Bollinger mean reversion 1H | ETH | SHORT | Bollinger mean reversion | 60m | 2,0x | 1867,37645 | 1863,89000 | 1889,78497 | 2791,72779 | 1833,76367 | €1.999,85 | €3.999,71 | €48,00 | €7,47 |
| Benchmark Bollinger mean reversion 1H | PEPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.332,01 | €2.664,02 | €0,00 | €59,04 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Benchmark trend following EMA 1H | PEPE | LONG | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.028,07 | €2.056,13 | €49,62 | €-11,53 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €625,48 | €1.250,97 | €51,81 | €0,00 |
| Scanner Top 5 Long 1H | BANK | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,21801 | 0,25663 | 0,22693 | 0,11010 | 0,27034 | €214,35 | €428,71 | €0,00 | €75,94 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.079,04 | €2.158,08 | €51,78 | €-25,05 |
| Scanner Bottom 5 Short 1H | LAB | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,22091 | 0,22091 | 0,20335 | 0,33025 | 0,16789 | €209,34 | €418,67 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,07217 | 0,07204 | 0,07321 | 0,10789 | 0,07009 | €1.741,23 | €3.482,46 | €50,15 | €6,11 |
| Scanner Bottom 5 Short 1H | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 60,29694 | 59,99900 | 61,29138 | 90,14392 | 58,30805 | €1.509,04 | €3.018,08 | €49,78 | €14,91 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37613 | 0,37613 | 0,36189 | 0,18994 | 0,40745 | €677,81 | €1.355,62 | €51,32 | €0,00 |
| Scanner Top 5 + forza BTC 1H | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,21801 | 0,25663 | 0,22693 | 0,11010 | 0,27557 | €213,93 | €427,86 | €0,00 | €75,79 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07215 | 0,07204 | 0,07330 | 0,10786 | 0,06926 | €1.551,38 | €3.102,75 | €49,64 | €4,59 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,35567 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €50,24 | €0,00 |
| Combo Trend | BANK | LONG | Combo Trend | 60m | 2,0x | 0,22714 | 0,25663 | 0,22714 | 0,11470 | 0,28710 | €209,25 | €418,49 | €0,00 | €54,34 |
| Combo Trend | HYPE | SHORT | Combo Trend | 60m | 2,0x | 60,45191 | 59,99900 | 61,58071 | 90,37560 | 57,96854 | €1.341,10 | €2.682,20 | €50,08 | €20,10 |
| Combo Mean Reversion | LAB | LONG | Combo Mean Reversion | 60m | 2,0x | 0,18881 | 0,18881 | 0,17193 | 0,09535 | 0,21583 | €281,61 | €563,22 | €50,37 | €0,00 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40679 | €599,14 | €1.198,28 | €49,63 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,07215 | 0,07204 | 0,07319 | 0,10786 | 0,06986 | €1.763,29 | €3.526,57 | €50,78 | €5,21 |
| Combo Scanner | BANK | LONG | Combo Scanner | 60m | 2,0x | 0,21801 | 0,25663 | 0,22693 | 0,11010 | 0,27557 | €208,29 | €416,59 | €0,00 | €73,79 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €613,42 | €1.226,85 | €50,81 | €0,00 |
| Combo Adaptive | GRAM | SHORT | Combo Adaptive | 60m | 2,0x | 1,48181 | 1,48181 | 1,51561 | 2,21531 | 1,41422 | €1.129,35 | €2.258,70 | €51,51 | €-0,00 |
| Combo Adaptive | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1868,12355 | 1863,89000 | 1841,22257 | 943,40239 | 1921,92551 | €1.779,59 | €3.559,18 | €51,25 | €-8,07 |
| Combo Adaptive Mfe Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07231 | 0,07204 | 0,07335 | 0,10810 | 0,07022 | €1.693,88 | €3.387,77 | €48,78 | €12,49 |
| Combo Adaptive Mfe Trail | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 60,49390 | 59,99900 | 61,51053 | 90,43838 | 58,46064 | €1.454,10 | €2.908,20 | €48,87 | €23,79 |
| Combo Adaptive Mfe Trail | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.019,69 | €2.039,38 | €48,93 | €-16,23 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 64774,99241 | 64385,30000 | 63842,23252 | 43507,20323 | 66640,51219 | €1.151,09 | €3.453,28 | €49,73 | €-20,78 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1877,23537 | 1863,89000 | 1850,20318 | 1260,87642 | 1931,29975 | €1.152,05 | €3.456,15 | €49,77 | €-24,57 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 1868,12355 | 1863,89000 | 1844,21157 | 1254,75632 | 1915,94751 | €1.302,08 | €3.906,25 | €50,00 | €-8,85 |
| Eth Bollinger 1H | ETH | SHORT | Bollinger mean reversion | 60m | 3,0x | 1867,37645 | 1863,89000 | 1889,78497 | 2480,49838 | 1833,76367 | €1.388,89 | €4.166,67 | €50,00 | €7,78 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1868,12355 | 1863,89000 | 1841,22257 | 1254,75632 | 1921,92551 | €1.151,05 | €3.453,16 | €49,73 | €-7,83 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07216 | 0,07204 | 0,07320 | 0,09585 | 0,07008 | €1.155,81 | €3.467,44 | €49,93 | €5,61 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Top 5 Long 1H | PEPE | LONG | 2026-07-20T04:23:30+00:00 | 0,00000 | €-3,32 | -0,06 | STOP |
| Forza relativa 1H V1 | PEPE | LONG | 2026-07-20T04:23:30+00:00 | 0,00000 | €-3,24 | -0,06 | STOP |
| Rapida 1H V3 Filtered | PEPE | LONG | 2026-07-20T04:23:30+00:00 | 0,00000 | €-53,65 | -1,08 | STOP |
| Bilanciata 1H V1 | PEPE | LONG | 2026-07-20T04:23:30+00:00 | 0,00000 | €-3,29 | -0,06 | STOP |
| Combo Mean Reversion | ZEC | LONG | 2026-07-20T03:38:29+00:00 | 532,81430 | €-54,64 | -1,07 | STOP |
| Combo Adaptive Mfe Trail | PEPE | LONG | 2026-07-20T03:38:29+00:00 | 0,00000 | €-0,45 | -0,01 | STOP |
| Forza relativa 1H V2 | PEPE | LONG | 2026-07-20T03:23:29+00:00 | 0,00000 | €106,02 | 2,10 | TARGET |
| Forza relativa 1H V2 | BANK | LONG | 2026-07-20T02:53:29+00:00 | 0,24704 | €110,09 | 2,17 | TARGET |
| Rapida 1H V3 Filtered | BANK | LONG | 2026-07-20T02:53:29+00:00 | 0,26753 | €74,28 | 1,49 | TARGET |
| Bilanciata 1H V3 Filtered | BANK | LONG | 2026-07-20T02:53:29+00:00 | 0,24294 | €98,56 | 1,97 | TARGET |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | 2026-07-20T02:38:29+00:00 | 0,02544 | €-53,44 | -1,07 | STOP_STRESS_SLIPPAGE |
| Rapida 1H V3 Filtered | ESPORTS | SHORT | 2026-07-20T02:38:29+00:00 | 0,02544 | €-53,35 | -1,07 | STOP_STRESS_SLIPPAGE |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
