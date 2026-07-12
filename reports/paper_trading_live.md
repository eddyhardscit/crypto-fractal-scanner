# Paper trading automatico KuCoin

Generato: 2026-07-12T17:31:36+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-12T17:31:33+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-12T17:31:33+00:00 | 2026-07-12T17:31:33+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Età massima | Limite | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-12T17:15:00+00:00 | 2026-07-12T17:15:00+00:00 | 16,6 min | 40,0 min | OK |
| 60m | 12 | 2026-07-12T16:00:00+00:00 | 2026-07-12T16:00:00+00:00 | 1,53 h | 1,42 h | STALE_CANDLE |
| 240m | 12 | 2026-07-12T12:00:00+00:00 | 2026-07-12T12:00:00+00:00 | 5,53 h | 4,42 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Età candela | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | T | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 5,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 331.6 minuti; limite 265. |
| Principale 4H | LAB | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 5,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 331.6 minuti; limite 265. |
| Principale 4H | BTC | 240m | LONG | 6,67 | 6,00 | 0,00 | STALE_CANDLE | 5,53 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [IN_FORMAZIONE] | peso 0 | Ultima candela chiusa troppo vecchia: 331.6 minuti; limite 265. |
| Principale 4H | ETH | 240m | LONG | 6,42 | 6,00 | 0,00 | STALE_CANDLE | 5,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 331.6 minuti; limite 265. |
| Principale 4H | ZEC | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 5,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 331.6 minuti; limite 265. |
| Principale 4H | DOGE | 240m | SHORT | -6,08 | 6,00 | 0,00 | STALE_CANDLE | 5,53 h | D: Hidden bearish [CONFERMATA] | W: Conferma ribassista [CONTESTO] | peso 0 | Ultima candela chiusa troppo vecchia: 331.6 minuti; limite 265. |
| Principale 4H | PEPE | 240m | LONG | 5,52 | 6,00 | 0,48 | STALE_CANDLE | 5,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 331.6 minuti; limite 265. |
| Principale 4H | XRP | 240m | SHORT | -3,92 | 6,00 | 2,08 | STALE_CANDLE | 5,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 331.6 minuti; limite 265. |
| Principale 4H | ADA | 240m | SHORT | -3,81 | 6,00 | 2,19 | STALE_CANDLE | 5,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 331.6 minuti; limite 265. |
| Principale 4H | EVAA | 240m | SHORT | -3,25 | 6,00 | 2,75 | STALE_CANDLE | 5,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 331.6 minuti; limite 265. |
| Principale 4H | SOL | 240m | SHORT | -2,35 | 6,00 | 3,65 | STALE_CANDLE | 5,53 h | D: Conferma rialzista [CONTESTO] | W: Hidden bearish [IN_FORMAZIONE] | peso 0 | Ultima candela chiusa troppo vecchia: 331.6 minuti; limite 265. |
| Principale 4H | HYPE | 240m | LONG | 0,68 | 6,00 | 5,32 | STALE_CANDLE | 5,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 331.6 minuti; limite 265. |
| Ampia 4H | T | 240m | LONG | 8,25 | 5,00 | 0,00 | STALE_CANDLE | 5,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 331.6 minuti; limite 265. |
| Bilanciata 1H | ZEC | 60m | LONG | 8,15 | 5,00 | 0,00 | STALE_CANDLE | 1,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 91.6 minuti; limite 85. |
| Rapida 1H | ZEC | 60m | LONG | 8,15 | 4,50 | 0,00 | STALE_CANDLE | 1,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 91.6 minuti; limite 85. |
| Forza relativa 1H | ZEC | 60m | LONG | 8,15 | 4,00 | 0,00 | STALE_CANDLE | 1,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 91.6 minuti; limite 85. |
| Bilanciata 1H | EVAA | 60m | SHORT | -7,75 | 5,00 | 0,00 | STALE_CANDLE | 1,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 91.6 minuti; limite 85. |
| Rapida 1H | EVAA | 60m | SHORT | -7,75 | 4,50 | 0,00 | STALE_CANDLE | 1,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 91.6 minuti; limite 85. |
| Forza relativa 1H | EVAA | 60m | SHORT | -7,75 | 4,00 | 0,00 | STALE_CANDLE | 1,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 91.6 minuti; limite 85. |
| Bilanciata 1H | LAB | 60m | SHORT | -6,75 | 5,00 | 0,00 | STALE_CANDLE | 1,53 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 91.6 minuti; limite 85. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €10.000,00 | 0,00% | €0,00 | €3.000,00 | 0,00% | 0 | 0 | 0,00% | 0,00 | 0,00% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 0 | 1 | CAMPIONE INSUFFICIENTE | 30 (mancano 30) |

- Trade del Principale 4H chiusi: **0**; win rate **0,00%**; profit factor **0,00**.
- Expectancy: **€0,00** per trade; P&L netto: **€0,00**; max drawdown: **0,00%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H | 4 | €10.069,93 | €2.044,49 | €6.133,48 | €200,23 | €27,99 |
| TEST | Bilanciata 1H | 4 | €10.052,14 | €1.620,10 | €4.860,29 | €200,18 | €25,32 |
| TEST | Forza relativa 1H | 4 | €10.049,26 | €2.429,88 | €4.859,76 | €200,16 | €25,32 |
| TEST | Ampia 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Rapida 1H | Momentum / breakout | €10.069,93 | €45,62 | 1 | 1 | 100,00% | ∞ | €45,62 | 0,06% |
| TEST | Bilanciata 1H | Confluenza trend | €10.052,14 | €29,73 | 1 | 1 | 100,00% | ∞ | €29,73 | 0,05% |
| TEST | Forza relativa 1H | Forza relativa vs BTC | €10.049,26 | €26,85 | 1 | 1 | 100,00% | ∞ | €26,85 | 0,05% |
| TEST | Ampia 4H | Confluenza trend | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
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
| Bilanciata 1H | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,47752 | €716,68 | €2.150,03 | €49,99 | €0,00 |
| Bilanciata 1H | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,47334 | 0,45521 | 0,53014 | n/a | 0,35973 | €138,83 | €416,49 | €49,98 | €15,95 |
| Bilanciata 1H | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00553 | 0,00479 | n/a | 0,00663 | €146,15 | €438,46 | €49,94 | €10,53 |
| Bilanciata 1H | ZEC | LONG | Confluenza trend | 60m | 3,0x | 544,28884 | 543,95000 | 529,54245 | 365,58067 | 573,78162 | €618,44 | €1.855,31 | €50,27 | €-1,15 |
| Rapida 1H | AAVE | LONG | Momentum / breakout | 60m | 3,0x | 98,87929 | 98,87929 | 97,09109 | n/a | 101,56159 | €921,40 | €2.764,20 | €49,99 | €0,00 |
| Rapida 1H | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,47334 | 0,45521 | 0,53014 | n/a | 0,38813 | €138,81 | €416,44 | €49,97 | €15,95 |
| Rapida 1H | T | LONG | Momentum / breakout | 60m | 3,0x | 0,00540 | 0,00553 | 0,00492 | n/a | 0,00612 | €187,85 | €563,56 | €49,92 | €13,53 |
| Rapida 1H | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 544,28884 | 543,95000 | 532,81942 | 365,58067 | 561,49296 | €796,43 | €2.389,29 | €50,35 | €-1,49 |
| Forza relativa 1H | AAVE | LONG | Forza relativa vs BTC | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H | LAB | SHORT | Forza relativa vs BTC | 60m | 2,0x | 0,47334 | 0,45521 | 0,53014 | n/a | 0,34837 | €208,25 | €416,49 | €49,98 | €15,95 |
| Forza relativa 1H | T | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,00540 | 0,00553 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €10,53 |
| Forza relativa 1H | ZEC | LONG | Forza relativa vs BTC | 60m | 2,0x | 544,28884 | 543,95000 | 529,54245 | 274,86586 | 576,73089 | €927,39 | €1.854,78 | €50,25 | €-1,15 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Forza relativa 1H | ZEC | LONG | 2026-07-12T16:28:26+00:00 | 534,17240 | €26,85 | 0,54 | STOP |
| Rapida 1H | ZEC | LONG | 2026-07-12T16:28:26+00:00 | 536,43609 | €45,62 | 0,91 | STOP_SAME_CANDLE_CONSERVATIVE |
| Bilanciata 1H | ZEC | LONG | 2026-07-12T16:28:26+00:00 | 534,92696 | €29,73 | 0,59 | STOP |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
