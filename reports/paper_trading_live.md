# Paper trading automatico KuCoin

Generato: 2026-07-13T11:44:27+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-13T11:44:23+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-13T11:44:23+00:00 | 2026-07-13T11:44:23+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Età massima | Limite | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-13T11:15:00+00:00 | 2026-07-13T11:15:00+00:00 | 29,4 min | 40,0 min | OK |
| 60m | 12 | 2026-07-13T10:00:00+00:00 | 2026-07-13T10:00:00+00:00 | 1,74 h | 1,42 h | STALE_CANDLE |
| 240m | 12 | 2026-07-13T04:00:00+00:00 | 2026-07-13T04:00:00+00:00 | 7,74 h | 4,42 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Età candela | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | 240m | SHORT | -7,99 | 6,00 | 0,00 | STALE_CANDLE | 7,74 h | D: Hidden bearish [CONFERMATA] | W: Conferma ribassista [CONTESTO] | peso 0 | Ultima candela chiusa troppo vecchia: 464.4 minuti; limite 265. |
| Principale 4H | LAB | 240m | SHORT | -7,75 | 6,00 | 0,00 | STALE_CANDLE | 7,74 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 464.4 minuti; limite 265. |
| Principale 4H | ZEC | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 7,74 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 464.4 minuti; limite 265. |
| Principale 4H | EVAA | 240m | SHORT | -6,25 | 6,00 | 0,00 | STALE_CANDLE | 7,74 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 464.4 minuti; limite 265. |
| Principale 4H | XRP | 240m | SHORT | -5,48 | 6,00 | 0,52 | STALE_CANDLE | 7,74 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 464.4 minuti; limite 265. |
| Principale 4H | ADA | 240m | SHORT | -4,87 | 6,00 | 1,13 | STALE_CANDLE | 7,74 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 464.4 minuti; limite 265. |
| Principale 4H | HYPE | 240m | SHORT | -4,87 | 6,00 | 1,13 | STALE_CANDLE | 7,74 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 464.4 minuti; limite 265. |
| Principale 4H | SOL | 240m | SHORT | -4,81 | 6,00 | 1,19 | STALE_CANDLE | 7,74 h | D: Momentum in indebolimento, divergenza non confermata [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 464.4 minuti; limite 265. |
| Principale 4H | PEPE | 240m | LONG | 2,90 | 6,00 | 3,10 | STALE_CANDLE | 7,74 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 464.4 minuti; limite 265. |
| Principale 4H | VELVET | 240m | LONG | 2,27 | 6,00 | 3,73 | STALE_CANDLE | 7,74 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 464.4 minuti; limite 265. |
| Principale 4H | ETH | 240m | LONG | 1,43 | 6,00 | 4,57 | STALE_CANDLE | 7,74 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 464.4 minuti; limite 265. |
| Principale 4H | BTC | 240m | LONG | 1,17 | 6,00 | 4,83 | STALE_CANDLE | 7,74 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [CONFERMATA] | peso 0 | Ultima candela chiusa troppo vecchia: 464.4 minuti; limite 265. |
| Bilanciata 1H | EVAA | 60m | SHORT | -9,75 | 5,00 | 0,00 | STALE_CANDLE | 1,74 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 104.4 minuti; limite 85. |
| Rapida 1H | EVAA | 60m | SHORT | -9,75 | 4,50 | 0,00 | STALE_CANDLE | 1,74 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 104.4 minuti; limite 85. |
| Forza relativa 1H | EVAA | 60m | SHORT | -9,75 | 4,00 | 0,00 | STALE_CANDLE | 1,74 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 104.4 minuti; limite 85. |
| Ampia 4H | DOGE | 240m | SHORT | -7,99 | 5,00 | 0,00 | STALE_CANDLE | 7,74 h | D: Hidden bearish [CONFERMATA] | W: Conferma ribassista [CONTESTO] | peso 0 | Ultima candela chiusa troppo vecchia: 464.4 minuti; limite 265. |
| Ampia 4H | LAB | 240m | SHORT | -7,75 | 5,00 | 0,00 | STALE_CANDLE | 7,74 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 464.4 minuti; limite 265. |
| Ampia 4H | ZEC | 240m | LONG | 7,75 | 5,00 | 0,00 | STALE_CANDLE | 7,74 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 464.4 minuti; limite 265. |
| Bilanciata 1H | DOGE | 60m | SHORT | -6,98 | 5,00 | 0,00 | STALE_CANDLE | 1,74 h | D: Hidden bearish [CONFERMATA] | W: Conferma ribassista [CONTESTO] | peso 0 | Ultima candela chiusa troppo vecchia: 104.4 minuti; limite 85. |
| Rapida 1H | DOGE | 60m | SHORT | -6,98 | 4,50 | 0,00 | STALE_CANDLE | 1,74 h | D: Hidden bearish [CONFERMATA] | W: Conferma ribassista [CONTESTO] | peso 0 | Ultima candela chiusa troppo vecchia: 104.4 minuti; limite 85. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €10.086,53 | +0,87% | €86,53 | €3.000,00 | 2,88% | 3 | 1 | 100,00% | ∞ | 0,15% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 1 | 7 | CAMPIONE INSUFFICIENTE | 30 (mancano 29) |

- Trade del Principale 4H chiusi: **1**; win rate **100,00%**; profit factor **∞**.
- Expectancy: **€99,42** per trade; P&L netto: **€99,42**; max drawdown: **0,15%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 3 | €10.086,53 | €989,92 | €2.969,75 | €149,98 | €-11,11 |
| TEST | Forza relativa 1H | 3 | €10.222,94 | €1.571,93 | €3.143,85 | €150,60 | €29,04 |
| TEST | Ampia 4H | 4 | €10.073,53 | €1.398,51 | €2.797,02 | €149,98 | €75,20 |
| TEST | Bilanciata 1H | 4 | €10.049,82 | €1.141,97 | €3.425,90 | €200,42 | €-26,31 |
| TEST | Rapida 1H | 4 | €10.005,72 | €2.428,12 | €7.284,37 | €200,23 | €-4,08 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €10.086,53 | €99,42 | 1 | 1 | 100,00% | ∞ | €99,42 | 0,15% |
| TEST | Forza relativa 1H | Forza relativa vs BTC | €10.222,94 | €193,80 | 4 | 4 | 75,00% | 4,69 | €48,45 | 0,86% |
| TEST | Ampia 4H | Confluenza trend | €10.073,53 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,14% |
| TEST | Bilanciata 1H | Confluenza trend | €10.049,82 | €76,19 | 4 | 4 | 50,00% | 2,43 | €19,05 | 0,86% |
| TEST | Rapida 1H | Momentum / breakout | €10.005,72 | €14,16 | 6 | 6 | 33,33% | 1,13 | €2,36 | 1,07% |
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
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07237 | 0,07229 | 0,07451 | 0,09613 | 0,06808 | €562,89 | €1.688,66 | €50,00 | €1,79 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 522,36445 | 513,26000 | 492,15982 | 350,85479 | 582,77371 | €288,18 | €864,53 | €49,99 | €-15,07 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,34760 | 0,34579 | 0,38931 | 0,46173 | 0,26418 | €138,85 | €416,55 | €49,99 | €2,17 |
| Bilanciata 1H | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,47752 | €716,68 | €2.150,03 | €49,99 | €0,00 |
| Bilanciata 1H | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00663 | €146,15 | €438,46 | €49,94 | €0,00 |
| Bilanciata 1H | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,34760 | 0,34579 | 0,38931 | 0,46173 | 0,26418 | €139,27 | €417,80 | €50,14 | €2,18 |
| Bilanciata 1H | EVAA | SHORT | Confluenza trend | 60m | 3,0x | 0,69296 | 0,74000 | 0,77612 | 0,92048 | 0,52665 | €139,87 | €419,61 | €50,35 | €-28,48 |
| Rapida 1H | AAVE | LONG | Momentum / breakout | 60m | 3,0x | 98,87929 | 98,87929 | 97,09109 | n/a | 101,56159 | €921,40 | €2.764,20 | €49,99 | €0,00 |
| Rapida 1H | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,34760 | 0,34579 | 0,38931 | 0,46173 | 0,28503 | €139,07 | €417,21 | €50,07 | €2,17 |
| Rapida 1H | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 65,52689 | 65,13400 | 66,41701 | 87,04155 | 64,19171 | €1.228,46 | €3.685,37 | €50,06 | €22,10 |
| Rapida 1H | EVAA | SHORT | Momentum / breakout | 60m | 3,0x | 0,69296 | 0,74000 | 0,77612 | 0,92048 | 0,56823 | €139,19 | €417,58 | €50,11 | €-28,35 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07229 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €1,37 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 513,26000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €-11,59 |
| Ampia 4H | LAB | SHORT | Confluenza trend | 240m | 2,0x | 0,34760 | 0,34579 | 0,38931 | 0,51966 | 0,23081 | €208,29 | €416,58 | €49,99 | €2,17 |
| Ampia 4H | EVAA | SHORT | Confluenza trend | 240m | 2,0x | 0,92491 | 0,74000 | 0,92491 | 1,38275 | 0,61414 | €208,21 | €416,41 | €0,00 | €83,25 |
| Forza relativa 1H | AAVE | LONG | Forza relativa vs BTC | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H | T | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H | VELVET | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,59490 | 0,62600 | 0,54062 | 0,30042 | 0,71431 | €277,68 | €555,36 | €50,67 | €29,04 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Forza relativa 1H | EVAA | SHORT | 2026-07-13T11:23:10+00:00 | 0,68087 | €109,88 | 2,19 | TARGET |
| Principale 4H | EVAA | SHORT | 2026-07-13T11:23:10+00:00 | 0,70308 | €99,42 | 1,99 | TARGET |
| Rapida 1H | EVAA | SHORT | 2026-07-13T10:15:55+00:00 | 0,92510 | €-0,58 | -0,01 | STOP |
| Bilanciata 1H | EVAA | SHORT | 2026-07-13T10:15:55+00:00 | 0,92510 | €-0,58 | -0,01 | STOP |
| Forza relativa 1H | LAB | SHORT | 2026-07-13T08:02:23+00:00 | 0,34844 | €109,64 | 2,19 | TARGET |
| Rapida 1H | T | LONG | 2026-07-13T07:47:52+00:00 | 0,00502 | €-51,29 | -1,02 | STOP |
| Rapida 1H | LAB | SHORT | 2026-07-13T07:47:52+00:00 | 0,38821 | €74,62 | 1,49 | TARGET |
| Bilanciata 1H | LAB | SHORT | 2026-07-13T07:47:52+00:00 | 0,35981 | €99,64 | 1,99 | TARGET |
| Forza relativa 1H | ZEC | LONG | 2026-07-13T04:49:53+00:00 | 529,43654 | €-52,58 | -1,05 | STOP |
| Bilanciata 1H | ZEC | LONG | 2026-07-13T04:49:53+00:00 | 529,43654 | €-52,59 | -1,05 | STOP |
| Rapida 1H | ZEC | LONG | 2026-07-13T01:07:33+00:00 | 532,71285 | €-53,65 | -1,07 | STOP |
| Rapida 1H | T | LONG | 2026-07-12T23:30:44+00:00 | 0,00540 | €-0,55 | -0,01 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.

## 🎯 DOGE Rejection Short — conto dedicato €3.600

Simulazione separata **paper only**: capitale/margine iniziale **€3.600**, leva **5x**, esposizione iniziale **€18.000**. Non modifica i conti paper da €10.000 e non invia ordini reali.

- Stato: **WAITING**
- Prezzo DOGE: **0.07229**
- Pre-allarme: **0.0765**; zona armata: **0.0775**; trigger rejection: **0.078**
- Invalidazione prima dell’entrata: chiusura 15m sopra **0.07966**

| Capitale iniziale | Balance | Equity | P&L aperto | Eventi chiusi | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| €3.600,00 | €3.600,00 | €3.600,00 | €0,00 | 0 | 0,00% | 0,00 | 0,00% |

### Filtri correnti

| Filtro | Valore | Stato |
| --- | --- | --- |
| Dati mercato | FRESH | OK |
| Candela 15m | 29.4 min | OK |
| Global DOGE | -7.0 | OK |
| Classic raw | -9.0 | OK |
| DOGE/BTC raw | -8.0 | OK |
| Pattern ribassista | MATURO | OK |
| BTC sotto filtro | 62955 | OK |

### Ultima candela 15m valutata

- Rejection accettata: **NO**; motivo: **trigger_touched, entry_not_chased, bearish_confirmation**
- High **0.07241**; close **0.07237**; wick alta **44.4%**; volume **x0.48**

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
- Motivo: Direzione poco definita: score BTC +0.0, breadth EMA50 8%, ADX 18.1.
- BTC trend score: **0,00**; ADX: **18,08**; breadth sopra EMA50: **8,33%**
- Mediana alt vs BTC: **0,31%**; dispersione: **20,00%**

- Aperti in questo ciclo: **0**
- Chiusi in questo ciclo: **0**
- Posizioni research aperte: **27**
- Trade research chiusi: **14**
- Eventi di mercato indipendenti chiusi: **6**
- Segnali sovrapposti saltati sullo stesso asset/profilo: **23**
- Posizioni Research V1 senza regime scartate durante la migrazione: **28**

### Risultati complessivi per strategia

| Profilo | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_BALANCED | 8 | 5 | 5 | 0,00% | 0,00 | -1,06R | €-52,82 |
| SHADOW_1H_FAST | 4 | 4 | 4 | 25,00% | 0,48 | -0,41R | €-16,25 |
| SHADOW_4H_WIDE | 6 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | 5 | 5 | 5 | 0,00% | 0,00 | -1,06R | €-52,82 |

### Matrice strategia × regime all’entrata

| Profilo | Regime entrata | Aperte | Chiuse | Eventi indip. | Win rate | PF | Expectancy R | P&L norm. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN | RANGE | 4 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_1H_BALANCED | ALT_ROTATION_UP | 3 | 4 | 4 | 0,00% | 0,00 | -1,07R | €-42,68 |
| SHADOW_1H_BALANCED | RANGE | 5 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_1H_FAST | ALT_ROTATION_UP | 0 | 3 | 3 | 33,33% | 0,71 | -0,20R | €-6,12 |
| SHADOW_1H_FAST | RANGE | 4 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |
| SHADOW_4H_WIDE | RANGE | 6 | 0 | 0 | 0,00% | 0,00 | 0,00R | €0,00 |
| SHADOW_RELATIVE_STRENGTH | ALT_ROTATION_UP | 1 | 4 | 4 | 0,00% | 0,00 | -1,07R | €-42,68 |
| SHADOW_RELATIVE_STRENGTH | RANGE | 4 | 1 | 1 | 0,00% | 0,00 | -1,01R | €-10,13 |

Il P&L è normalizzato a **€10 di rischio per evento**, così leva e size non falsano il confronto.
La matrice diventerà utilizzabile per una rotazione automatica soltanto dopo un campione sufficiente per ciascuna coppia strategia-regime.
