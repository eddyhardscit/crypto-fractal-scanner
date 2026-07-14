# Paper trading automatico KuCoin

Generato: 2026-07-14T03:20:29+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-14T03:20:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-14T03:20:25+00:00 | 2026-07-14T03:20:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Età massima | Limite | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-14T03:00:00+00:00 | 2026-07-14T03:00:00+00:00 | 20,4 min | 40,0 min | OK |
| 60m | 12 | 2026-07-14T02:00:00+00:00 | 2026-07-14T02:00:00+00:00 | 1,34 h | 1,42 h | OK |
| 240m | 12 | 2026-07-13T20:00:00+00:00 | 2026-07-13T20:00:00+00:00 | 7,34 h | 4,42 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Età candela | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | 240m | SHORT | -8,52 | 6,00 | 0,00 | STALE_CANDLE | 7,34 h | D: Hidden bearish [CONFERMATA] | W: Conferma ribassista [CONTESTO] | peso 0 | Ultima candela chiusa troppo vecchia: 440.4 minuti; limite 265. |
| Principale 4H | ALLO | 240m | LONG | 7,50 | 6,00 | 0,00 | STALE_CANDLE | 7,34 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 440.4 minuti; limite 265. |
| Principale 4H | EVAA | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 7,34 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 440.4 minuti; limite 265. |
| Principale 4H | XRP | 240m | SHORT | -6,55 | 6,00 | 0,00 | STALE_CANDLE | 7,34 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 440.4 minuti; limite 265. |
| Principale 4H | LAB | 240m | SHORT | -6,25 | 6,00 | 0,00 | STALE_CANDLE | 7,34 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 440.4 minuti; limite 265. |
| Principale 4H | SOL | 240m | SHORT | -5,73 | 6,00 | 0,27 | STALE_CANDLE | 7,34 h | D: Momentum in indebolimento, divergenza non confermata [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 440.4 minuti; limite 265. |
| Principale 4H | HYPE | 240m | SHORT | -4,18 | 6,00 | 1,82 | STALE_CANDLE | 7,34 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 440.4 minuti; limite 265. |
| Principale 4H | PEPE | 240m | LONG | 3,24 | 6,00 | 2,76 | STALE_CANDLE | 7,34 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 440.4 minuti; limite 265. |
| Principale 4H | ETH | 240m | LONG | 2,38 | 6,00 | 3,62 | STALE_CANDLE | 7,34 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 440.4 minuti; limite 265. |
| Principale 4H | BTC | 240m | SHORT | -0,58 | 6,00 | 5,42 | STALE_CANDLE | 7,34 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 440.4 minuti; limite 265. |
| Principale 4H | ZEC | 240m | LONG | 0,36 | 6,00 | 5,64 | STALE_CANDLE | 7,34 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 440.4 minuti; limite 265. |
| Principale 4H | VELVET | 240m | LONG | 0,21 | 6,00 | 5,79 | STALE_CANDLE | 7,34 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 440.4 minuti; limite 265. |
| Rapida 1H | EVAA | 60m | SHORT | -7,00 | 4,50 | 0,00 | STRATEGY_FILTER | 1,34 h | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.39%. |
| Rapida 1H | HYPE | 60m | SHORT | -6,57 | 4,50 | 0,00 | STRATEGY_FILTER | 1,34 h | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.49%. |
| Rapida 1H | SOL | 60m | SHORT | -6,06 | 4,50 | 0,00 | STRATEGY_FILTER | 1,34 h | D: Momentum in indebolimento, divergenza non confermata [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.35%. |
| Forza relativa 1H | SOL | 60m | SHORT | -6,06 | 4,00 | 0,00 | STRATEGY_FILTER | 1,34 h | D: Momentum in indebolimento, divergenza non confermata [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=-0.72%. |
| Rapida 1H | DOGE | 60m | SHORT | -5,55 | 4,50 | 0,00 | STRATEGY_FILTER | 1,34 h | D: Hidden bearish [CONFERMATA] | W: Conferma ribassista [CONTESTO] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.06%. |
| Forza relativa 1H | DOGE | 60m | SHORT | -5,55 | 4,00 | 0,00 | STRATEGY_FILTER | 1,34 h | D: Hidden bearish [CONFERMATA] | W: Conferma ribassista [CONTESTO] | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=-0.25%. |
| Rapida 1H | XRP | 60m | SHORT | -4,58 | 4,50 | 0,00 | STRATEGY_FILTER | 1,34 h | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.32%. |
| Forza relativa 1H | XRP | 60m | SHORT | -4,58 | 4,00 | 0,00 | STRATEGY_FILTER | 1,34 h | D: n/a | W: n/a | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=-0.40%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €10.160,17 | +1,60% | €160,17 | €3.000,00 | 5,34% | 3 | 4 | 50,00% | 1,94 | 0,55% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 4 | 14 | CAMPIONE INSUFFICIENTE | 30 (mancano 26) |

- Trade del Principale 4H chiusi: **4**; win rate **50,00%**; profit factor **1,94**.
- Expectancy: **€24,05** per trade; P&L netto: **€96,20**; max drawdown: **0,55%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 3 | €10.160,17 | €1.119,04 | €3.357,11 | €151,35 | €65,59 |
| TEST | Rapida 1H | 4 | €10.224,54 | €3.775,25 | €11.325,75 | €100,65 | €123,14 |
| TEST | Forza relativa 1H | 4 | €10.215,48 | €2.940,20 | €5.880,40 | €201,29 | €74,75 |
| TEST | Bilanciata 1H | 4 | €10.170,76 | €2.183,15 | €6.549,44 | €201,18 | €47,70 |
| TEST | Ampia 4H | 3 | €10.131,11 | €1.190,22 | €2.380,44 | €99,99 | €44,42 |
| TEST | Scalp RSI Long €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long prudente 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short prudente 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |

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
| TEST | Scalp RSI Long €10 · 15x | Inversione RSI estrema 15m | Scalp long 15m dopo capitolazione RSI confermata; margine fisso €10 e leva paper 15x. |
| TEST | Scalp RSI Long €50 · 15x | Inversione RSI estrema 15m | Scalp long 15m sullo stesso segnale; margine fisso €50 e leva paper 15x. |
| TEST | Scalp RSI Long prudente 5x | Inversione RSI estrema 15m | Versione prudente long dello scalp RSI 15m, leva 5x e rischio ridotto. |
| TEST | Scalp RSI Short €10 · 15x | Inversione RSI estrema 15m | Scalp short 15m dopo euforia RSI confermata; margine fisso €10 e leva paper 15x. |
| TEST | Scalp RSI Short €50 · 15x | Inversione RSI estrema 15m | Scalp short 15m sullo stesso segnale; margine fisso €50 e leva paper 15x. |
| TEST | Scalp RSI Short prudente 5x | Inversione RSI estrema 15m | Versione prudente short dello scalp RSI 15m, leva 5x e rischio ridotto. |

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €10.160,17 | €96,20 | 4 | 4 | 50,00% | 1,94 | €24,05 | 0,55% |
| TEST | Rapida 1H | Momentum / breakout | €10.224,54 | €108,02 | 9 | 9 | 44,44% | 1,69 | €12,00 | 1,07% |
| TEST | Forza relativa 1H | Forza relativa vs BTC | €10.215,48 | €142,33 | 5 | 5 | 60,00% | 2,37 | €28,47 | 0,86% |
| TEST | Bilanciata 1H | Confluenza trend | €10.170,76 | €125,00 | 6 | 6 | 50,00% | 2,20 | €20,83 | 0,86% |
| TEST | Ampia 4H | Confluenza trend | €10.131,11 | €88,07 | 2 | 2 | 50,00% | 2,71 | €44,04 | 0,76% |
| TEST | Scalp RSI Long €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long prudente 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short prudente 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07237 | 0,07150 | 0,07451 | 0,09613 | 0,06808 | €562,89 | €1.688,66 | €50,00 | €20,22 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 63,85923 | 62,72100 | 66,45178 | 84,82634 | 58,67412 | €415,02 | €1.245,07 | €50,55 | €22,19 |
| Principale 4H | EVAA | SHORT | Confluenza trend | 240m | 3,0x | 0,84263 | 0,79650 | 0,94375 | 1,11930 | 0,64040 | €141,12 | €423,37 | €50,80 | €23,18 |
| Bilanciata 1H | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,47752 | €716,68 | €2.150,03 | €49,99 | €0,00 |
| Bilanciata 1H | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00663 | €146,15 | €438,46 | €49,94 | €0,00 |
| Bilanciata 1H | VELVET | LONG | Confluenza trend | 60m | 3,0x | 0,59035 | 0,64649 | 0,53330 | 0,39652 | 0,70445 | €174,63 | €523,89 | €50,63 | €49,82 |
| Bilanciata 1H | SOL | SHORT | Confluenza trend | 60m | 3,0x | 74,63707 | 74,68300 | 75,73639 | 99,14291 | 72,43843 | €1.145,69 | €3.437,06 | €50,62 | €-2,12 |
| Rapida 1H | AAVE | LONG | Momentum / breakout | 60m | 3,0x | 98,87929 | 98,87929 | 97,09109 | n/a | 101,56159 | €921,40 | €2.764,20 | €49,99 | €0,00 |
| Rapida 1H | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 63,85923 | 62,72100 | 63,50447 | 84,82634 | 62,46328 | €1.155,23 | €3.465,70 | €0,00 | €61,77 |
| Rapida 1H | VELVET | LONG | Momentum / breakout | 60m | 3,0x | 0,59035 | 0,64649 | 0,60484 | 0,39652 | 0,65691 | €224,67 | €674,00 | €0,00 | €64,09 |
| Rapida 1H | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 74,63707 | 74,68300 | 75,49210 | 99,14291 | 73,35453 | €1.473,95 | €4.421,85 | €50,66 | €-2,72 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07150 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €15,55 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 499,63000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €-28,94 |
| Ampia 4H | EVAA | SHORT | Confluenza trend | 240m | 2,0x | 0,92491 | 0,79650 | 0,92491 | 1,38275 | 0,61414 | €208,21 | €416,41 | €0,00 | €57,81 |
| Forza relativa 1H | AAVE | LONG | Forza relativa vs BTC | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H | T | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H | VELVET | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,59490 | 0,64649 | 0,54062 | 0,30042 | 0,71431 | €277,68 | €555,36 | €50,67 | €48,16 |
| Forza relativa 1H | HYPE | SHORT | Forza relativa vs BTC | 60m | 2,0x | 63,33633 | 62,72100 | 64,50951 | 94,68781 | 60,75532 | €1.368,27 | €2.736,55 | €50,69 | €26,59 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
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
| Rapida 1H | HYPE | SHORT | 2026-07-13T13:40:28+00:00 | 64,20455 | €69,99 | 1,40 | TARGET |
| Forza relativa 1H | EVAA | SHORT | 2026-07-13T11:23:10+00:00 | 0,68087 | €109,88 | 2,19 | TARGET |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.0715**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 20.5 min | OK |
| Global DOGE | -7.0 | OK |
| Classic raw | -9.0 | OK |
| DOGE/BTC raw | -8.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 62405.7 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased**
- High **0.07185**; close **0.07172**; wick alta **42.9%**; volume **x0.18**

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
- Motivo: Direzione poco definita: score BTC +0.0, breadth EMA50 8%, ADX 24.7.
- BTC trend score: **0,00**; ADX: **24,71**; breadth sopra EMA50: **8,33%**
- Mediana alt vs BTC: **-0,05%**; dispersione: **14,35%**

- Aperti in questo ciclo: **1**
- Chiusi in questo ciclo: **9**
- Posizioni research aperte: **36**
- Trade research chiusi: **52**
- Eventi di mercato indipendenti chiusi: **30**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **121**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 6 | 4 | 4 | 50,00% | 1,95 | 0,48R | €19,32 |
| SHADOW_1H_BALANCED | 10 | 16 | 16 | 37,50% | 1,10 | 0,07R | €10,45 |
| SHADOW_1H_FAST | 5 | 21 | 21 | 28,57% | 0,55 | -0,35R | €-72,64 |
| SHADOW_4H_WIDE | 9 | 1 | 1 | 100,00% | ∞ | 2,79R | €27,87 |
| SHADOW_RELATIVE_STRENGTH | 6 | 10 | 10 | 20,00% | 0,52 | -0,40R | €-39,59 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | RANGE | 6 | 4 | 4 | 50,00% | 1,95 | 0,48R | €19,32 |
| SHADOW_1H_BALANCED | ALT_ROTATION_UP | 0 | 7 | 7 | 42,86% | 1,35 | 0,22R | €15,08 |
| SHADOW_1H_BALANCED | RANGE | 5 | 5 | 5 | 60,00% | 2,85 | 0,75R | €37,53 |
| SHADOW_1H_BALANCED | RANGE_HIGH_VOL | 5 | 4 | 4 | 0,00% | 0,00 | -1,05R | €-42,16 |
| SHADOW_1H_FAST | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,12 |
| SHADOW_1H_FAST | RANGE | 4 | 9 | 9 | 55,56% | 1,78 | 0,36R | €32,01 |
| SHADOW_1H_FAST | RANGE_HIGH_VOL | 1 | 9 | 9 | 0,00% | 0,00 | -1,09R | €-98,53 |
| SHADOW_4H_WIDE | RANGE | 9 | 1 | 1 | 100,00% | ∞ | 2,79R | €27,87 |
| SHADOW_RELATIVE_STRENGTH | ALT_ROTATION_UP | 0 | 5 | 5 | 20,00% | 0,51 | -0,42R | €-20,82 |
| SHADOW_RELATIVE_STRENGTH | RANGE | 6 | 3 | 3 | 33,33% | 1,08 | 0,05R | €1,56 |
| SHADOW_RELATIVE_STRENGTH | RANGE_HIGH_VOL | 0 | 2 | 2 | 0,00% | 0,00 | -1,02R | €-20,33 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
