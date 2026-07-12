# Paper trading automatico KuCoin

Generato: 2026-07-12T16:28:27+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-12T16:28:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-12T16:28:25+00:00 | 2026-07-12T16:28:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Età massima | Limite | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-12T16:00:00+00:00 | 2026-07-12T16:00:00+00:00 | 28,4 min | 40,0 min | OK |
| 60m | 12 | 2026-07-12T15:00:00+00:00 | 2026-07-12T15:00:00+00:00 | 1,47 h | 1,42 h | STALE_CANDLE |
| 240m | 12 | 2026-07-12T12:00:00+00:00 | 2026-07-12T12:00:00+00:00 | 4,47 h | 4,42 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Età candela | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | T | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 4,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 268.4 minuti; limite 265. |
| Principale 4H | LAB | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 4,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 268.4 minuti; limite 265. |
| Principale 4H | BTC | 240m | LONG | 6,67 | 6,00 | 0,00 | STALE_CANDLE | 4,47 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [IN_FORMAZIONE] | peso 0 | Ultima candela chiusa troppo vecchia: 268.4 minuti; limite 265. |
| Principale 4H | ETH | 240m | LONG | 6,42 | 6,00 | 0,00 | STALE_CANDLE | 4,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 268.4 minuti; limite 265. |
| Principale 4H | ZEC | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 4,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 268.4 minuti; limite 265. |
| Principale 4H | PEPE | 240m | LONG | 5,52 | 6,00 | 0,48 | STALE_CANDLE | 4,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 268.4 minuti; limite 265. |
| Principale 4H | AAVE | 240m | LONG | 5,36 | 6,00 | 0,64 | STALE_CANDLE | 4,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 268.4 minuti; limite 265. |
| Principale 4H | XRP | 240m | SHORT | -3,92 | 6,00 | 2,08 | STALE_CANDLE | 4,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 268.4 minuti; limite 265. |
| Principale 4H | ADA | 240m | SHORT | -3,81 | 6,00 | 2,19 | STALE_CANDLE | 4,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 268.4 minuti; limite 265. |
| Principale 4H | EVAA | 240m | SHORT | -3,25 | 6,00 | 2,75 | STALE_CANDLE | 4,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 268.4 minuti; limite 265. |
| Principale 4H | SOL | 240m | SHORT | -2,35 | 6,00 | 3,65 | STALE_CANDLE | 4,47 h | D: Conferma rialzista [CONTESTO] | W: Hidden bearish [IN_FORMAZIONE] | peso 0 | Ultima candela chiusa troppo vecchia: 268.4 minuti; limite 265. |
| Principale 4H | HYPE | 240m | LONG | 0,68 | 6,00 | 5,32 | STALE_CANDLE | 4,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 268.4 minuti; limite 265. |
| Bilanciata 1H | LAB | 60m | SHORT | -8,25 | 5,00 | 0,00 | STALE_CANDLE | 1,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 88.4 minuti; limite 85. |
| Rapida 1H | LAB | 60m | SHORT | -8,25 | 4,50 | 0,00 | STALE_CANDLE | 1,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 88.4 minuti; limite 85. |
| Forza relativa 1H | LAB | 60m | SHORT | -8,25 | 4,00 | 0,00 | STALE_CANDLE | 1,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 88.4 minuti; limite 85. |
| Ampia 4H | T | 240m | LONG | 8,25 | 5,00 | 0,00 | STALE_CANDLE | 4,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 268.4 minuti; limite 265. |
| Bilanciata 1H | EVAA | 60m | SHORT | -7,75 | 5,00 | 0,00 | STALE_CANDLE | 1,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 88.4 minuti; limite 85. |
| Rapida 1H | EVAA | 60m | SHORT | -7,75 | 4,50 | 0,00 | STALE_CANDLE | 1,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 88.4 minuti; limite 85. |
| Forza relativa 1H | EVAA | 60m | SHORT | -7,75 | 4,00 | 0,00 | STALE_CANDLE | 1,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 88.4 minuti; limite 85. |
| Bilanciata 1H | ZEC | 60m | LONG | 7,28 | 5,00 | 0,00 | STALE_CANDLE | 1,47 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 88.4 minuti; limite 85. |

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
| TEST | Rapida 1H | 3 | €10.055,36 | €1.248,07 | €3.744,20 | €149,89 | €11,99 |
| TEST | Bilanciata 1H | 3 | €10.041,86 | €1.001,66 | €3.004,98 | €149,91 | €13,93 |
| TEST | Forza relativa 1H | 3 | €10.038,98 | €1.502,49 | €3.004,98 | €149,91 | €13,93 |
| TEST | Ampia 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |

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

## Confronto risultati

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Rapida 1H | Momentum / breakout | €10.055,36 | €45,62 | 1 | 1 | 100,00% | ∞ | €45,62 | 0,06% |
| TEST | Bilanciata 1H | Confluenza trend | €10.041,86 | €29,73 | 1 | 1 | 100,00% | ∞ | €29,73 | 0,05% |
| TEST | Forza relativa 1H | Forza relativa vs BTC | €10.038,98 | €26,85 | 1 | 1 | 100,00% | ∞ | €26,85 | 0,05% |
| TEST | Ampia 4H | Confluenza trend | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bilanciata 1H | AAVE | LONG | Confluenza trend | 60m | 3,0x | 98,87929 | 98,84000 | 96,58018 | 103,47752 | €716,68 | €2.150,03 | €49,99 | €-0,85 |
| Bilanciata 1H | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,47334 | 0,44978 | 0,53014 | 0,35973 | €138,83 | €416,49 | €49,98 | €20,73 |
| Bilanciata 1H | T | LONG | Confluenza trend | 60m | 3,0x | 0,00540 | 0,00533 | 0,00479 | 0,00663 | €146,15 | €438,46 | €49,94 | €-5,94 |
| Rapida 1H | AAVE | LONG | Momentum / breakout | 60m | 3,0x | 98,87929 | 98,84000 | 97,09109 | 101,56159 | €921,40 | €2.764,20 | €49,99 | €-1,10 |
| Rapida 1H | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,47334 | 0,44978 | 0,53014 | 0,38813 | €138,81 | €416,44 | €49,97 | €20,72 |
| Rapida 1H | T | LONG | Momentum / breakout | 60m | 3,0x | 0,00540 | 0,00533 | 0,00492 | 0,00612 | €187,85 | €563,56 | €49,92 | €-7,64 |
| Forza relativa 1H | AAVE | LONG | Forza relativa vs BTC | 60m | 2,0x | 98,87929 | 98,84000 | 96,58018 | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €-0,85 |
| Forza relativa 1H | LAB | SHORT | Forza relativa vs BTC | 60m | 2,0x | 0,47334 | 0,44978 | 0,53014 | 0,34837 | €208,25 | €416,49 | €49,98 | €20,73 |
| Forza relativa 1H | T | LONG | Forza relativa vs BTC | 60m | 2,0x | 0,00540 | 0,00533 | 0,00479 | 0,00676 | €219,23 | €438,46 | €49,94 | €-5,94 |

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
