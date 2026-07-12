# Paper trading automatico KuCoin

Generato: 2026-07-12T14:17:20+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-12T14:17:19+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-12T14:17:19+00:00 | 2026-07-12T14:17:19+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Età massima | Limite | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-12T14:00:00+00:00 | 2026-07-12T14:00:00+00:00 | 17,3 min | 40,0 min | OK |
| 60m | 12 | 2026-07-12T13:00:00+00:00 | 2026-07-12T13:00:00+00:00 | 1,29 h | 1,42 h | OK |
| 240m | 12 | 2026-07-12T08:00:00+00:00 | 2026-07-12T08:00:00+00:00 | 6,29 h | 4,42 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Età candela | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SHADOW_RELATIVE_STRENGTH | T | 60m | LONG | 6,25 | 4,00 | 0,00 | OPENED | 1,29 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| SHADOW_RELATIVE_STRENGTH | LAB | 60m | SHORT | -6,25 | 4,00 | 0,00 | OPENED | 1,29 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| SHADOW_1H_FAST | T | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 1,29 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| SHADOW_1H_BALANCED | T | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 1,29 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| MAIN | ZEC | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 6,29 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 377.3 minuti; limite 265. |
| MAIN | AAVE | 240m | LONG | 6,99 | 6,00 | 0,00 | STALE_CANDLE | 6,29 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 377.3 minuti; limite 265. |
| MAIN | LAB | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 6,29 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 377.3 minuti; limite 265. |
| MAIN | BTC | 240m | LONG | 6,67 | 6,00 | 0,00 | STALE_CANDLE | 6,29 h | D: Hidden bearish [IN_FORMAZIONE] | W: Bullish regolare [IN_FORMAZIONE] | peso 0 | Ultima candela chiusa troppo vecchia: 377.3 minuti; limite 265. |
| MAIN | T | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 6,29 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 377.3 minuti; limite 265. |
| MAIN | ETH | 240m | LONG | 6,23 | 6,00 | 0,00 | STALE_CANDLE | 6,29 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 377.3 minuti; limite 265. |
| MAIN | XRP | 240m | SHORT | -5,42 | 6,00 | 0,58 | STALE_CANDLE | 6,29 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 377.3 minuti; limite 265. |
| MAIN | PEPE | 240m | LONG | 3,86 | 6,00 | 2,14 | STALE_CANDLE | 6,29 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 377.3 minuti; limite 265. |
| MAIN | ADA | 240m | SHORT | -3,65 | 6,00 | 2,35 | STALE_CANDLE | 6,29 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 377.3 minuti; limite 265. |
| MAIN | SOL | 240m | SHORT | -3,36 | 6,00 | 2,64 | STALE_CANDLE | 6,29 h | D: Conferma rialzista [CONTESTO] | W: Hidden bearish [IN_FORMAZIONE] | peso 0 | Ultima candela chiusa troppo vecchia: 377.3 minuti; limite 265. |
| MAIN | HYPE | 240m | SHORT | -3,18 | 6,00 | 2,82 | STALE_CANDLE | 6,29 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 377.3 minuti; limite 265. |
| MAIN | EVAA | 240m | SHORT | -2,75 | 6,00 | 3,25 | STALE_CANDLE | 6,29 h | D: n/a | W: n/a | peso 0 | Ultima candela chiusa troppo vecchia: 377.3 minuti; limite 265. |
| SHADOW_1H_BALANCED | ZEC | 60m | LONG | 7,67 | 5,00 | 0,00 | OPENED | 1,29 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| SHADOW_1H_FAST | ZEC | 60m | LONG | 7,67 | 4,50 | 0,00 | OPENED | 1,29 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| SHADOW_RELATIVE_STRENGTH | ZEC | 60m | LONG | 7,67 | 4,00 | 0,00 | OPENED | 1,29 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| SHADOW_1H_BALANCED | AAVE | 60m | LONG | 6,88 | 5,00 | 0,00 | OPENED | 1,29 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| SHADOW_1H_FAST | AAVE | 60m | LONG | 6,88 | 4,50 | 0,00 | OPENED | 1,29 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| SHADOW_RELATIVE_STRENGTH | AAVE | 60m | LONG | 6,88 | 4,00 | 0,00 | OPENED | 1,29 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| SHADOW_1H_BALANCED | LAB | 60m | SHORT | -6,25 | 5,00 | 0,00 | OPENED | 1,29 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| SHADOW_1H_FAST | LAB | 60m | SHORT | -6,25 | 4,50 | 0,00 | OPENED | 1,29 h | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €10.000,00 | 0,00% | €0,00 | €3.000,00 | 0,00% | 0 | 0 | 0,00% | 0,00 | 0,00% |

## Stato del campione statistico

| MAIN eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 0 | 0 | CAMPIONE INSUFFICIENTE | 30 (mancano 30) |

- Trade MAIN chiusi: **0**; win rate **0,00%**; profit factor **0,00**.
- Expectancy: **€0,00** per trade; P&L netto: **€0,00**; max drawdown: **0,00%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del MAIN**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Confronto portafogli

| Tipo | Portafoglio | Strategia | Equity | P&L chiuso | Trade | Eventi indip. | Win rate | PF | Expectancy | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAIN | MAIN | confluence_trend | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| OMBRA | SHADOW_4H_WIDE | confluence_trend | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| OMBRA | SHADOW_1H_BALANCED | confluence_trend | €9.994,96 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,05% |
| OMBRA | SHADOW_RELATIVE_STRENGTH | relative_strength | €9.994,96 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,05% |
| OMBRA | SHADOW_1H_FAST | momentum_breakout | €9.993,61 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,06% |

**Eventi indip.** conta gli eventi di mercato distinti; le varianti di stop, target e timeframe restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Strategia | TF | Entry | Mark | Stop | Target | Margine | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SHADOW_1H_BALANCED | ZEC | LONG | confluence_trend | 60m | 526,49528 | 526,39000 | 513,38607 | 552,71370 | €669,37 | €-0,40 |
| SHADOW_1H_BALANCED | AAVE | LONG | confluence_trend | 60m | 98,87929 | 98,82000 | 96,58018 | 103,47752 | €716,68 | €-1,29 |
| SHADOW_1H_BALANCED | LAB | SHORT | confluence_trend | 60m | 0,47334 | 0,47343 | 0,53014 | 0,35973 | €138,83 | €-0,08 |
| SHADOW_1H_BALANCED | T | LONG | confluence_trend | 60m | 0,00540 | 0,00540 | 0,00479 | 0,00663 | €146,15 | €-0,26 |
| SHADOW_1H_FAST | ZEC | LONG | momentum_breakout | 60m | 526,49528 | 526,39000 | 516,29923 | 541,78936 | €860,62 | €-0,52 |
| SHADOW_1H_FAST | AAVE | LONG | momentum_breakout | 60m | 98,87929 | 98,82000 | 97,09109 | 101,56159 | €921,40 | €-1,66 |
| SHADOW_1H_FAST | LAB | SHORT | momentum_breakout | 60m | 0,47334 | 0,47343 | 0,53014 | 0,38813 | €138,81 | €-0,08 |
| SHADOW_1H_FAST | T | LONG | momentum_breakout | 60m | 0,00540 | 0,00540 | 0,00492 | 0,00612 | €187,85 | €-0,34 |
| SHADOW_RELATIVE_STRENGTH | ZEC | LONG | relative_strength | 60m | 526,49528 | 526,39000 | 513,38607 | 555,33554 | €1.004,06 | €-0,40 |
| SHADOW_RELATIVE_STRENGTH | AAVE | LONG | relative_strength | 60m | 98,87929 | 98,82000 | 96,58018 | 103,93735 | €1.075,02 | €-1,29 |
| SHADOW_RELATIVE_STRENGTH | LAB | SHORT | relative_strength | 60m | 0,47334 | 0,47343 | 0,53014 | 0,34837 | €208,25 | €-0,08 |
| SHADOW_RELATIVE_STRENGTH | T | LONG | relative_strength | 60m | 0,00540 | 0,00540 | 0,00479 | 0,00676 | €219,23 | €-0,26 |

## Ultime operazioni chiuse

_Nessuna operazione virtuale chiusa._

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e quelli ombra hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
