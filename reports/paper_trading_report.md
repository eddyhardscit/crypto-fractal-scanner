# Paper trading automatico KuCoin

Generato: 2026-07-17T07:33:26+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-17T06:30:02+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-17T06:30:02+00:00 | 2026-07-17T06:30:02+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-17T06:00:00+00:00 | 2026-07-17T06:00:00+00:00 | 15,1 min | 25,0 min | OK |
| 60m | 12 | 2026-07-17T05:00:00+00:00 | 2026-07-17T05:00:00+00:00 | 30,1 min | 45,0 min | OK |
| 240m | 12 | 2026-07-17T00:00:00+00:00 | 2026-07-17T00:00:00+00:00 | 2,50 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Btc Adaptive 1H | BTC | 60m | SHORT | -5,08 | 5,00 | 0,00 | OPENED | 30,1 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Btc Bollinger 1H | BTC | 60m | SHORT | -5,08 | 5,00 | 0,00 | OPENED | 30,1 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Btc Donchian 1H | BTC | 60m | SHORT | -5,08 | 5,00 | 0,00 | OPENED | 30,1 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Btc Ema 1H | BTC | 60m | SHORT | -5,08 | 5,00 | 0,00 | OPENED | 30,1 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Mean Reversion | BTC | 60m | SHORT | -5,08 | 5,00 | 0,00 | OPENED | 30,1 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Bollinger mean reversion 1H | BTC | 60m | SHORT | -5,08 | 5,00 | 0,00 | OPENED | 30,1 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | AKE | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 2,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 150.1 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -8,00 | 6,00 | 0,00 | STALE_CANDLE | 2,50 h | D: Hidden bearish [CONFERMATA] | W: Conferma ribassista [CONTESTO] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 150.1 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 2,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 150.1 minuti; tolleranza 60 minuti. |
| Principale 4H | LAB | 240m | SHORT | -6,25 | 6,00 | 0,00 | STALE_CANDLE | 2,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 150.1 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | SHORT | -6,21 | 6,00 | 0,00 | STALE_CANDLE | 2,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 150.1 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -5,97 | 6,00 | 0,03 | STALE_CANDLE | 2,50 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 150.1 minuti; tolleranza 60 minuti. |
| Principale 4H | XLM | 240m | SHORT | -4,25 | 6,00 | 1,75 | STALE_CANDLE | 2,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 150.1 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 2,27 | 6,00 | 3,73 | STALE_CANDLE | 2,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 150.1 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -1,77 | 6,00 | 4,23 | STALE_CANDLE | 2,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 150.1 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 1,50 | 6,00 | 4,50 | STALE_CANDLE | 2,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 150.1 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 1,40 | 6,00 | 4,60 | STALE_CANDLE | 2,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 150.1 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -1,08 | 6,00 | 4,92 | STALE_CANDLE | 2,50 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 150.1 minuti; tolleranza 60 minuti. |
| Rapida 1H V2 | DOGE | 60m | SHORT | -9,91 | 5,00 | 0,00 | OPENED | 30,1 min | D: Hidden bearish [CONFERMATA] | W: Conferma ribassista [CONTESTO] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V2 | SOL | 60m | SHORT | -9,62 | 5,00 | 0,00 | OPENED | 30,1 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Bollinger mean reversion 1H | SOL | 60m | SHORT | -9,62 | 5,00 | 0,00 | READY | 30,1 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Sol Donchian 1H | SOL | 60m | SHORT | -9,62 | 5,00 | 0,00 | OPENED | 30,1 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Bollinger 1H | SOL | 60m | SHORT | -9,62 | 5,00 | 0,00 | OPENED | 30,1 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Bollinger mean reversion 1H | LAB | 60m | SHORT | -8,50 | 5,00 | 0,00 | OPENED | 30,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Mean Reversion | LAB | 60m | SHORT | -8,50 | 5,00 | 0,00 | OPENED | 30,1 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Mean Reversion | ADA | 60m | SHORT | -6,65 | 5,00 | 0,00 | READY | 30,1 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.860,88 | -1,39% | €-139,12 | €3.000,00 | -4,64% | 3 | 10 | 30,00% | 0,71 | 3,48% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 10 | 63 | CAMPIONE INSUFFICIENTE | 30 (mancano 20) |

- Trade del Principale 4H chiusi: **10**; win rate **30,00%**; profit factor **0,71**.
- Expectancy: **€-9,03** per trade; P&L netto: **€-90,30**; max drawdown: **3,48%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 3 | €9.860,88 | €1.437,62 | €4.312,86 | €147,88 | €-45,84 |
| TEST | Scanner Top 5 Long 1H | 2 | €10.306,57 | €1.600,63 | €3.201,27 | €101,80 | €0,00 |
| TEST | Rapida 1H V1 | 2 | €10.290,54 | €984,04 | €2.952,11 | €50,49 | €54,27 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.236,46 | €1.516,14 | €3.032,28 | €0,00 | €165,67 |
| TEST | Combo Adaptive | 2 | €10.209,32 | €2.373,74 | €4.747,48 | €101,51 | €4,48 |
| TEST | Scanner Top 5 + forza BTC 1H | 1 | €10.206,08 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €10.160,57 | €1.964,02 | €3.928,04 | €49,75 | €113,53 |
| TEST | Combo Trend | 3 | €10.099,15 | €3.139,62 | €6.279,25 | €100,35 | €107,45 |
| TEST | Forza relativa 1H V1 | 4 | €10.087,26 | €2.607,73 | €5.215,46 | €200,81 | €0,00 |
| TEST | Bilanciata 1H V2 | 3 | €10.083,57 | €2.474,22 | €7.422,66 | €50,12 | €88,03 |
| TEST | Bilanciata 1H V1 | 4 | €10.073,31 | €1.737,28 | €5.211,83 | €200,67 | €0,00 |
| TEST | Combo Mean Reversion | 2 | €10.072,56 | €2.296,90 | €4.593,80 | €98,73 | €-1,14 |
| TEST | Sol Ema 1H | 1 | €10.055,28 | €1.157,41 | €3.472,22 | €0,00 | €57,37 |
| TEST | Sol Adaptive 1H | 1 | €10.047,68 | €1.157,41 | €3.472,22 | €0,00 | €49,67 |
| TEST | Doge Ema 1H | 1 | €10.041,14 | €1.157,41 | €3.472,22 | €0,00 | €43,22 |
| TEST | Ampia 4H | 3 | €10.029,79 | €1.377,19 | €2.754,38 | €150,30 | €-2,21 |
| TEST | Doge Donchian 1H | 1 | €10.025,49 | €1.302,08 | €3.906,25 | €0,00 | €27,84 |
| TEST | Forza relativa 1H V2 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| TEST | Eth Ema 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.998,01 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.997,22 | €1.157,41 | €3.472,22 | €50,00 | €-0,69 |
| TEST | Btc Adaptive 1H | 1 | €9.997,22 | €1.157,41 | €3.472,22 | €50,00 | €-0,69 |
| TEST | Btc Donchian 1H | 1 | €9.996,87 | €1.302,08 | €3.906,25 | €50,00 | €-0,78 |
| TEST | Sol Donchian 1H | 1 | €9.996,87 | €1.302,08 | €3.906,25 | €50,00 | €-0,78 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.996,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 1 | €9.996,67 | €1.388,89 | €4.166,67 | €50,00 | €-0,83 |
| TEST | Sol Bollinger 1H | 1 | €9.996,67 | €1.388,89 | €4.166,67 | €50,00 | €-0,83 |
| TEST | Rapida 1H V2 | 2 | €9.992,86 | €2.975,66 | €8.926,98 | €99,98 | €-1,79 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.990,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.987,95 | €1.553,81 | €3.107,63 | €0,00 | €45,00 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.957,47 | €2.077,18 | €4.154,36 | €99,48 | €66,76 |
| TEST | Combo Scanner | 2 | €9.942,15 | €2.330,11 | €4.660,23 | €49,63 | €50,13 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €9.921,23 | €2.262,39 | €4.524,79 | €97,25 | €-1,13 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.860,88 | €-90,30 | 10 | 10 | 30,00% | 0,71 | €-9,03 | 3,48% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.306,57 | €308,49 | 8 | 8 | 75,00% | 3,76 | €38,56 | 0,75% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.290,54 | €237,82 | 25 | 25 | 48,00% | 1,48 | €9,51 | 2,34% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.236,46 | €71,66 | 4 | 4 | 50,00% | 1,68 | €17,91 | 1,35% |
| TEST | Combo Adaptive | Combo Adaptive | €10.209,32 | €207,69 | 9 | 9 | 55,56% | 2,27 | €23,08 | 0,75% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.206,08 | €207,25 | 7 | 7 | 57,14% | 2,89 | €29,61 | 1,62% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €10.160,57 | €48,53 | 2 | 2 | 50,00% | 1,96 | €24,27 | 0,51% |
| TEST | Combo Trend | Combo Trend | €10.099,15 | €-4,64 | 6 | 6 | 33,33% | 0,97 | €-0,77 | 1,48% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €10.087,26 | €88,40 | 7 | 7 | 57,14% | 1,56 | €12,63 | 1,36% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.083,57 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,06% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.073,31 | €74,45 | 8 | 8 | 50,00% | 1,47 | €9,31 | 1,06% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.072,56 | €76,46 | 1 | 1 | 100,00% | ∞ | €76,46 | 0,04% |
| TEST | Sol Ema 1H | Trend following EMA | €10.055,28 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,34% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.047,68 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,11% |
| TEST | Doge Ema 1H | Trend following EMA | €10.041,14 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,03% |
| TEST | Ampia 4H | Confluenza trend | €10.029,79 | €33,14 | 4 | 4 | 25,00% | 1,31 | €8,29 | 1,75% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.025,49 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,24% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
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
| TEST | Eth Ema 1H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.998,01 | €-1,99 | 2 | 2 | 50,00% | 0,31 | €-1,00 | 0,04% |
| TEST | Btc Ema 1H | Trend following EMA | €9.997,22 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,03% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.997,22 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,03% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.996,87 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,03% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.996,87 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,03% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.996,80 | €-3,20 | 2 | 2 | 50,00% | 0,70 | €-1,60 | 0,16% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €9.996,67 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,03% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.996,67 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,03% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.992,86 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,07% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.990,05 | €-9,95 | 2 | 2 | 50,00% | 0,31 | €-4,98 | 0,18% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.987,95 | €-55,58 | 1 | 1 | 0,00% | 0,00 | €-55,58 | 1,18% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.957,47 | €-106,79 | 2 | 2 | 0,00% | 0,00 | €-53,40 | 1,10% |
| TEST | Combo Scanner | Combo Scanner | €9.942,15 | €-105,63 | 4 | 4 | 25,00% | 0,34 | €-26,41 | 1,69% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.921,23 | €-74,92 | 7 | 7 | 28,57% | 0,66 | €-10,70 | 1,61% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €334,65 | €1.003,96 | €49,15 | €-36,59 |
| Principale 4H | ETH | LONG | Confluenza trend | 240m | 3,0x | 1874,64485 | 1833,38000 | 1816,18750 | 1259,13646 | 1991,55955 | €528,52 | €1.585,57 | €49,44 | €-34,90 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07183 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €25,65 |
| Bilanciata 1H V1 | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,47752 | €716,68 | €2.150,03 | €49,99 | €0,00 |
| Bilanciata 1H V1 | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00663 | €146,15 | €438,46 | €49,94 | €0,00 |
| Bilanciata 1H V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,02421 | 2,02421 | 1,97233 | 1,35960 | 2,12798 | €655,13 | €1.965,38 | €50,37 | €0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,37581 | 0,37581 | 0,40458 | 0,49921 | 0,31828 | €219,32 | €657,96 | €50,37 | €-0,00 |
| Bilanciata 1H V2 | SOL | SHORT | Confluenza trend V2 | 60m | 3,0x | 75,45391 | 74,68800 | 75,45391 | 100,22794 | 73,28083 | €1.157,41 | €3.472,22 | €0,00 | €35,25 |
| Bilanciata 1H V2 | DOGE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,07253 | 0,07183 | 0,07253 | 0,09634 | 0,07044 | €1.157,09 | €3.471,26 | €0,00 | €33,29 |
| Bilanciata 1H V2 | LAB | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,19670 | 0,18870 | 0,21728 | 0,26129 | 0,15555 | €159,73 | €479,18 | €50,12 | €19,49 |
| Rapida 1H V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,02421 | 2,02421 | 1,98386 | 1,35960 | 2,08474 | €844,18 | €2.532,55 | €50,49 | €0,00 |
| Rapida 1H V1 | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,21674 | 0,18870 | 0,20884 | 0,28790 | 0,17772 | €139,85 | €419,55 | €0,00 | €54,27 |
| Rapida 1H V2 | DOGE | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,07182 | 0,07183 | 0,07262 | 0,09540 | 0,07061 | €1.488,10 | €4.464,29 | €50,00 | €-0,89 |
| Rapida 1H V2 | SOL | SHORT | Momentum / breakout V2 | 60m | 3,0x | 74,67306 | 74,68800 | 75,50940 | 99,19072 | 73,41855 | €1.487,56 | €4.462,69 | €49,98 | €-0,89 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07183 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €9,63 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 535,69000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €16,97 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €395,18 | €790,36 | €50,30 | €-28,80 |
| Forza relativa 1H V1 | AAVE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H V1 | T | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H V1 | ALLO | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Benchmark Donchian breakout 1H | LAB | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,26148 | 0,18870 | 0,22833 | 0,39091 | 0,18303 | €211,57 | €423,15 | €0,00 | €117,78 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,16194 | 0,15897 | 0,16146 | 0,24210 | 0,15403 | €1.304,57 | €2.609,14 | €0,00 | €47,90 |
| Benchmark Bollinger mean reversion 1H | BTC | LONG | Bollinger mean reversion | 60m | 2,0x | 62931,57380 | 62918,99000 | 62176,39491 | 31780,44477 | 64064,34213 | €1.985,02 | €3.970,03 | €47,64 | €-0,79 |
| Benchmark Bollinger mean reversion 1H | LAB | LONG | Bollinger mean reversion | 60m | 2,0x | 0,18881 | 0,18870 | 0,17193 | 0,09535 | 0,21414 | €277,38 | €554,76 | €49,61 | €-0,33 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 61,48370 | 59,23200 | 60,43731 | 91,91813 | 57,81372 | €911,45 | €1.822,91 | €0,00 | €66,76 |
| Scanner Top 5 Long 1H | NEAR | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,12798 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €625,48 | €1.250,97 | €51,81 | €0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31828 | €324,92 | €649,84 | €49,75 | €-0,00 |
| Scanner Bottom 5 Short 1H | LAB | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,22091 | 0,18870 | 0,21603 | 0,33025 | 0,16789 | €209,34 | €418,67 | €0,00 | €61,04 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16194 | 0,15897 | 0,16115 | 0,24210 | 0,15624 | €1.429,76 | €2.859,53 | €0,00 | €52,49 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07289 | 0,07183 | 0,07257 | 0,10896 | 0,06997 | €1.553,81 | €3.107,63 | €0,00 | €45,00 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,35567 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €50,24 | €0,00 |
| Combo Trend | HYPE | SHORT | Combo Trend | 60m | 2,0x | 62,37152 | 59,23200 | 60,31754 | 93,24543 | 59,01849 | €1.027,78 | €2.055,56 | €0,00 | €103,47 |
| Combo Trend | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,08689 | 1,08551 | 1,10428 | 1,62490 | 1,04863 | €1.565,99 | €3.131,98 | €50,11 | €3,98 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 62931,57380 | 62918,99000 | 62176,39491 | 31780,44477 | 64139,86001 | €2.015,29 | €4.030,58 | €48,37 | €-0,81 |
| Combo Mean Reversion | LAB | LONG | Combo Mean Reversion | 60m | 2,0x | 0,18881 | 0,18870 | 0,17193 | 0,09535 | 0,21583 | €281,61 | €563,22 | €50,37 | €-0,34 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,07289 | 0,07183 | 0,07252 | 0,10896 | 0,07058 | €1.730,98 | €3.461,95 | €0,00 | €50,13 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40679 | €599,14 | €1.198,28 | €49,63 | €0,00 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €613,42 | €1.226,85 | €50,81 | €0,00 |
| Combo Adaptive | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,08689 | 1,08551 | 1,10254 | 1,62490 | 1,05559 | €1.760,32 | €3.520,63 | €50,70 | €4,48 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 62906,40620 | 62918,99000 | 63812,25845 | 83560,67624 | 61094,70170 | €1.157,41 | €3.472,22 | €50,00 | €-0,69 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 62906,40620 | 62918,99000 | 63711,60820 | 83560,67624 | 61296,00220 | €1.302,08 | €3.906,25 | €50,00 | €-0,78 |
| Btc Bollinger 1H | BTC | LONG | Bollinger mean reversion | 60m | 3,0x | 62931,57380 | 62918,99000 | 62176,39491 | 42269,04040 | 64064,34213 | €1.388,89 | €4.166,67 | €50,00 | €-0,83 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 62906,40620 | 62918,99000 | 63812,25845 | 83560,67624 | 61094,70170 | €1.157,41 | €3.472,22 | €50,00 | €-0,69 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 75,94281 | 74,68800 | 75,34879 | 100,87736 | 73,75566 | €1.157,41 | €3.472,22 | €0,00 | €57,37 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 74,67306 | 74,68800 | 75,62888 | 99,19072 | 72,76143 | €1.302,08 | €3.906,25 | €50,00 | €-0,78 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 74,70294 | 74,68800 | 73,80650 | 50,17547 | 76,04759 | €1.388,89 | €4.166,67 | €50,00 | €-0,83 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 75,77184 | 74,68800 | 75,38669 | 100,65026 | 73,58961 | €1.157,41 | €3.472,22 | €0,00 | €49,67 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07274 | 0,07183 | 0,07246 | 0,09662 | 0,07064 | €1.157,41 | €3.472,22 | €0,00 | €43,22 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,07235 | 0,07183 | 0,07235 | 0,09610 | 0,07049 | €1.302,08 | €3.906,25 | €0,00 | €27,84 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive | HYPE | SHORT | 2026-07-17T06:30:11+00:00 | 59,64006 | €98,57 | 1,94 | TARGET |
| Ampia 4H | BTC | LONG | 2026-07-17T06:30:11+00:00 | 62934,99888 | €-53,93 | -1,07 | STOP |
| Rapida 1H V1 | DOGE | SHORT | 2026-07-17T06:30:11+00:00 | 0,07185 | €69,00 | 1,39 | TARGET |
| Rapida 1H V1 | HYPE | SHORT | 2026-07-17T06:30:11+00:00 | 59,74406 | €72,28 | 1,43 | TARGET |
| Principale 4H | BTC | LONG | 2026-07-17T06:30:11+00:00 | 63362,38782 | €-54,55 | -1,09 | STOP |
| Benchmark Bollinger mean reversion 1H | HYPE | LONG | 2026-07-17T04:17:11+00:00 | 60,24462 | €-53,28 | -1,07 | STOP |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | 2026-07-17T01:26:57+00:00 | 0,00086 | €-0,89 | -0,02 | STOP |
| Benchmark Donchian breakout 1H | AKE | LONG | 2026-07-17T01:26:57+00:00 | 0,00085 | €-51,60 | -1,01 | STOP |
| Scanner Top 5 Long 1H | XLM | LONG | 2026-07-17T00:21:57+00:00 | 0,18556 | €-55,63 | -1,07 | STOP |
| Scanner Top 5 + forza BTC 1H | XLM | LONG | 2026-07-17T00:21:57+00:00 | 0,18556 | €-55,27 | -1,07 | STOP |
| Benchmark trend following EMA 1H | BTC | LONG | 2026-07-17T00:21:57+00:00 | 63750,42513 | €-56,17 | -1,13 | STOP |
| Combo Trend | XLM | LONG | 2026-07-17T00:21:57+00:00 | 0,18509 | €-53,03 | -1,06 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
