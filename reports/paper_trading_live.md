# Paper trading automatico KuCoin

Generato: 2026-07-12T11:17:37+00:00

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-12T11:17:37+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-12T11:17:37+00:00 | 2026-07-12T11:17:37+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Età massima | Limite | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 0 | n/a | n/a | n/a | 40,0 min | NO_DATA |
| 60m | 0 | n/a | n/a | n/a | 1,42 h | NO_DATA |
| 240m | 0 | n/a | n/a | n/a | 4,42 h | NO_DATA |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Età candela | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAIN | AAVE | 240m | n/a | n/a | 6,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| MAIN | ADA | 240m | n/a | n/a | 6,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| MAIN | BTC | 240m | n/a | n/a | 6,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| MAIN | ETH | 240m | n/a | n/a | 6,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| MAIN | EVAA | 240m | n/a | n/a | 6,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| MAIN | HYPE | 240m | n/a | n/a | 6,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| MAIN | LAB | 240m | n/a | n/a | 6,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| MAIN | PEPE | 240m | n/a | n/a | 6,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| MAIN | SOL | 240m | n/a | n/a | 6,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| MAIN | T | 240m | n/a | n/a | 6,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| MAIN | XRP | 240m | n/a | n/a | 6,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| MAIN | ZEC | 240m | n/a | n/a | 6,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| SHADOW_1H_BALANCED | AAVE | 60m | n/a | n/a | 5,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| SHADOW_1H_FAST | AAVE | 60m | n/a | n/a | 4,50 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| SHADOW_4H_WIDE | AAVE | 240m | n/a | n/a | 5,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| SHADOW_RELATIVE_STRENGTH | AAVE | 60m | n/a | n/a | 4,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| SHADOW_1H_BALANCED | ADA | 60m | n/a | n/a | 5,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| SHADOW_1H_FAST | ADA | 60m | n/a | n/a | 4,50 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| SHADOW_4H_WIDE | ADA | 240m | n/a | n/a | 5,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |
| SHADOW_RELATIVE_STRENGTH | ADA | 60m | n/a | n/a | 4,00 | n/a | NO_FEATURES | n/a | Dati insufficienti: servono almeno 60 candele utilizzabili. |

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
| OMBRA | SHADOW_1H_BALANCED | confluence_trend | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| OMBRA | SHADOW_1H_FAST | momentum_breakout | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| OMBRA | SHADOW_4H_WIDE | confluence_trend | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| OMBRA | SHADOW_RELATIVE_STRENGTH | relative_strength | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |

**Eventi indip.** conta gli eventi di mercato distinti; le varianti di stop, target e timeframe restano collegate allo stesso evento sperimentale.

## Posizioni aperte

_Nessuna posizione virtuale aperta._

## Ultime operazioni chiuse

_Nessuna operazione virtuale chiusa._

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e quelli ombra hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
