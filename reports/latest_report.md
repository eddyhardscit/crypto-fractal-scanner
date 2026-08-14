<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-08-14 10:53 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | NEUTRALE / COSTRUTTIVO | HOLD / ATTESA CONFERME | NO LONG A LEVA / ATTENDI SOPRA 67.248 $ | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | +3 | NEUTRALE / COSTRUTTIVO | HOLD / TRANCHE PICCOLE, NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +2 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+1**, spot = **HOLD / ATTESA CONFERME**, long = **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **+3**, spot = **HOLD / TRANCHE PICCOLE, NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+2**, spot = **STAI ALLA FINESTRA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+1**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**
- Short leva: **NO SHORT**
- Rischio: **MEDIO / ALTO**
- Conferme: Prima resistenza sopra 65.402; conferma del doppio minimo sopra 66.910.
- Invalidazioni: Sotto 62.227 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+3**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / TRANCHE PICCOLE, NO LEVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: conferma del doppio minimo sopra 83,81; nuova conferma tecnica sopra 77,62; milestone analogiche 79,14 / 89,87, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 69,65 / 70,69 / 62,19.

### DOGE

- Global Confluence: **+2**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **STAI ALLA FINESTRA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.07117 migliora; sopra 0.06966 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.06835 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 111,65 $; upside verso EMA200 +48,00%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-08-14T10:55:35+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-14T10:05:49+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-14T10:05:49+00:00 | 2026-08-14T10:05:49+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-14T09:45:00+00:00 | 2026-08-14T09:45:00+00:00 | 6,3 min | 25,0 min | OK |
| 60m | 12 | 2026-08-14T09:00:00+00:00 | 2026-08-14T09:00:00+00:00 | 6,3 min | 45,0 min | OK |
| 240m | 12 | 2026-08-14T04:00:00+00:00 | 2026-08-14T04:00:00+00:00 | 2,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast Nohigh Cap75 Short Only V1 | SNDK | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Expanded V1 | SNDK | 60m | LONG | 6,25 | 0,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive No Alt V1 | SKHYNIX | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Doge Donchian 1H | DOGE | 60m | SHORT | -7,44 | 5,00 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Long Only V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Mfe Trail | SNDK | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Scanner | SNDK | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Mean Reversion | BTC | 60m | SHORT | -6,00 | 5,00 | 0,00 | OPENED | 6,3 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | SNDK | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Btc Le3 V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 Long 1H | SNDK | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Donchian 1H Gb20 120R V1 | DOGE | 60m | SHORT | -7,44 | 5,00 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Donchian breakout 1H | DOGE | 60m | SHORT | -7,44 | 5,00 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | SKHYNIX | 60m | LONG | 7,75 | 5,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SNDK | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | DOGE | 60m | SHORT | -7,44 | 4,50 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | SNDK | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | DOGE | 60m | SHORT | -7,44 | 4,50 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Nohigh Cap75 V1 | SNDK | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | SNDK | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh V1 | SNDK | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | DOGE | 60m | SHORT | -7,44 | 4,50 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | DOGE | 60m | SHORT | -7,44 | 4,50 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | SKHYNIX | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | DOGE | 60m | SHORT | -7,44 | 4,50 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 V1 | SNDK | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Cost Aware V1 | TUT | 60m | SHORT | -6,25 | 6,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 No Trend Up V1 | DOGE | 60m | SHORT | -7,44 | 6,00 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | DOGE | 60m | SHORT | -7,44 | 6,00 | 0,00 | OPENED | 6,3 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Balanced Long No Rhv V1 | SKHYNIX | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | AKE | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | EDEN | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 2,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | TUT | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | SKHYNIX | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -6,15 | 6,00 | 0,00 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -4,86 | 6,00 | 1,14 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -4,62 | 6,00 | 1,38 | STALE_CANDLE | 2,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | SNDK | 240m | LONG | 4,25 | 6,00 | 1,75 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -3,34 | 6,00 | 2,66 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 1,26 | 6,00 | 4,74 | STALE_CANDLE | 2,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 0,99 | 6,00 | 5,01 | STALE_CANDLE | 2,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 126.3 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive V1 | AKE | 60m | LONG | 7,75 | 0,00 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Gb20 V1 | AKE | 60m | LONG | 7,75 | 0,00 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Side Regime Guard V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Gb20 Be V1 | AKE | 60m | LONG | 7,75 | 0,00 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Gb20 Partial V1 | AKE | 60m | LONG | 7,75 | 0,00 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Nohigh Regime Guard V1 | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Trend Side Regime Guard V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 6,3 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.731,82 | -2,68% | €-16,53 | €3.000,00 | -0,55% | 5 | 40 | 35,00% | 0,78 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 40 | 1295 | PRIME INDICAZIONI | 100 (mancano 60) |

- Trade del Principale 4H chiusi: **40**; win rate **35,00%**; profit factor **0,78**.
- Expectancy: **€-7,08** per trade; P&L netto: **€-283,07**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.731,82 | €1.286,74 | €3.860,23 | €194,28 | €14,79 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.678,56 | €4.649,93 | €9.299,86 | €160,67 | €50,21 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 4 | €10.527,70 | €2.028,02 | €6.084,05 | €104,55 | €74,28 |
| TEST | 1H Fast Score 6 75 V1 | 5 | €10.506,14 | €3.438,21 | €10.314,63 | €104,97 | €72,21 |
| TEST | Donchian 1H Gb20 120R V1 | 3 | €10.427,14 | €4.540,45 | €9.080,90 | €156,89 | €49,03 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 4 | €10.420,33 | €3.399,91 | €10.199,73 | €103,61 | €80,56 |
| TEST | Main Side Regime Guard V1 | 5 | €10.411,79 | €2.118,53 | €6.355,60 | €155,48 | €44,72 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 2 | €10.382,24 | €1.685,04 | €5.055,13 | €0,00 | €72,04 |
| TEST | 1H Fast Nohigh Cap75 V1 | 6 | €10.340,80 | €3.503,92 | €10.511,76 | €152,60 | €97,70 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 4 | €10.329,69 | €2.006,67 | €6.020,01 | €152,93 | €73,90 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €10.308,28 | €3.044,20 | €9.132,59 | €157,27 | €52,82 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 5 | €10.226,81 | €3.346,80 | €10.040,39 | €102,18 | €70,29 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 6 | €10.178,68 | €3.367,42 | €10.102,25 | €101,24 | €120,78 |
| TEST | Combo Adaptive Side Regime Guard V1 | 4 | €10.178,25 | €5.432,18 | €10.864,35 | €149,28 | €75,58 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.168,22 | €2.738,64 | €5.477,28 | €203,37 | €57,25 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 1 | €10.130,84 | €139,31 | €417,94 | €50,15 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 5 | €10.106,20 | €3.294,62 | €9.883,86 | €151,79 | €68,22 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 6 | €10.083,47 | €3.416,73 | €10.250,18 | €148,81 | €95,27 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €10.063,01 | €3.574,44 | €7.148,87 | €151,50 | €6,90 |
| TEST | Btc Donchian 1H | 1 | €10.058,10 | €1.301,67 | €3.905,01 | €0,00 | €60,81 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 7 | €10.039,42 | €2.004,50 | €6.013,51 | €150,99 | €97,92 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 1 | €10.013,79 | €1.152,72 | €3.458,17 | €0,00 | €53,85 |
| TEST | Doge Ema 1H | 1 | €10.011,70 | €1.155,63 | €3.466,88 | €49,92 | €28,47 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.007,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive | 8 | €10.007,56 | €3.973,75 | €7.947,50 | €99,11 | €173,42 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.002,03 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.001,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 4 | €10.000,95 | €3.303,34 | €9.910,01 | €149,55 | €62,40 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.999,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 6 | €9.994,09 | €1.980,18 | €5.940,53 | €151,21 | €0,40 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.989,13 | €1.413,45 | €2.826,90 | €49,75 | €38,45 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.971,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 2 | €9.958,96 | €2.980,95 | €8.942,84 | €49,80 | €77,10 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.948,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 1 | €9.944,63 | €1.295,48 | €3.886,44 | €49,75 | €-2,33 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.930,87 | €1.406,00 | €2.812,00 | €49,49 | €32,33 |
| TEST | Btc Ema 1H | 1 | €9.926,82 | €1.141,05 | €3.423,15 | €0,00 | €67,15 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.926,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 5 | €9.901,43 | €2.071,84 | €4.143,68 | €100,29 | €158,82 |
| TEST | Ampia 4H | 5 | €9.886,46 | €1.961,33 | €3.922,65 | €148,09 | €12,12 |
| TEST | Combo Adaptive Regime V1 | 4 | €9.870,59 | €4.759,21 | €9.518,42 | €197,93 | €-23,41 |
| TEST | Bilanciata 1H V2 | 5 | €9.857,34 | €2.605,16 | €7.815,47 | €146,25 | €41,79 |
| TEST | Sol Ema 4H | 0 | €9.845,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.842,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €9.836,81 | €2.673,82 | €5.347,63 | €195,68 | €68,12 |
| TEST | Combo Adaptive Runner25 V1 | 8 | €9.836,12 | €3.904,34 | €7.808,68 | €97,46 | €170,41 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €9.826,20 | €2.725,63 | €8.176,89 | €146,67 | €158,22 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.817,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.813,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 5 | €9.811,17 | €1.238,27 | €3.714,81 | €147,46 | €109,70 |
| TEST | Combo Adaptive Long Only V1 | 6 | €9.785,70 | €2.646,36 | €5.292,73 | €194,66 | €66,67 |
| TEST | Scanner Top5 Btc Guard V1 | 5 | €9.781,27 | €2.046,69 | €4.093,39 | €99,07 | €156,89 |
| TEST | Combo Adaptive Quality7 V1 | 2 | €9.775,94 | €1.230,80 | €2.461,59 | €48,59 | €131,66 |
| TEST | Rapida 1H V2 | 1 | €9.772,66 | €1.461,59 | €4.384,76 | €49,11 | €6,97 |
| TEST | Scanner Bottom10 Short | 6 | €9.771,84 | €4.868,27 | €9.736,53 | €97,72 | €67,61 |
| TEST | Scanner Bottom15 Short | 6 | €9.771,84 | €4.868,27 | €9.736,53 | €97,72 | €67,61 |
| TEST | Scanner Bottom20 Short | 6 | €9.771,84 | €4.868,27 | €9.736,53 | €97,72 | €67,61 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 5 | €9.761,99 | €2.707,82 | €8.123,46 | €145,71 | €157,19 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 1 | €9.757,74 | €206,68 | €413,36 | €0,00 | €120,61 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 5 | €9.753,95 | €1.231,32 | €3.693,95 | €195,08 | €107,46 |
| TEST | 1H Balanced V3 Long Only V1 | 6 | €9.749,98 | €2.879,32 | €8.637,97 | €148,75 | €49,96 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 5 | €9.731,55 | €2.036,29 | €4.072,58 | €98,57 | €156,09 |
| TEST | Combo Mean Reversion | 1 | €9.728,99 | €1.946,42 | €3.892,84 | €46,71 | €-0,78 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 6 | €9.716,12 | €3.221,09 | €9.663,28 | €144,29 | €144,99 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 6 | €9.706,12 | €4.839,94 | €9.679,89 | €96,59 | €67,79 |
| TEST | Global Confluence puro 1H | 1 | €9.700,99 | €1.512,09 | €3.024,18 | €48,39 | €24,84 |
| TEST | Master Adaptive Expanded V1 | 6 | €9.697,12 | €2.449,27 | €4.898,54 | €193,94 | €39,73 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €9.696,17 | €1.935,76 | €3.871,51 | €0,00 | €42,91 |
| TEST | Eth Adaptive 1H | 0 | €9.692,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 6 | €9.691,35 | €4.832,58 | €9.665,16 | €96,44 | €67,69 |
| TEST | Forza relativa 1H V2 | 5 | €9.683,34 | €3.368,25 | €6.736,51 | €145,60 | €54,15 |
| TEST | Sol Adaptive 1H | 0 | €9.674,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 8 | €9.652,37 | €3.831,40 | €7.662,80 | €95,64 | €167,23 |
| TEST | Combo Adaptive Quality7 Regime V1 | 1 | €9.635,01 | €204,08 | €408,16 | €0,00 | €119,09 |
| TEST | Eth Ema 1H | 0 | €9.622,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 6 | €9.616,78 | €4.795,39 | €9.590,79 | €95,70 | €67,17 |
| TEST | Combo Adaptive Partial 1R V1 | 8 | €9.609,71 | €3.815,77 | €7.631,55 | €95,17 | €166,53 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 4 | €9.608,95 | €1.780,13 | €5.340,40 | €143,47 | €71,63 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 6 | €9.574,78 | €2.655,14 | €5.310,27 | €191,50 | €41,11 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.560,90 | €3.213,74 | €9.641,23 | €142,79 | €121,62 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 5 | €9.553,79 | €1.999,09 | €3.998,19 | €96,77 | €153,24 |
| TEST | Master Adaptive Gb20 Be V1 | 5 | €9.515,69 | €4.064,03 | €8.128,06 | €191,14 | €-21,79 |
| TEST | Master Adaptive Gb20 Partial V1 | 5 | €9.505,57 | €4.059,71 | €8.119,42 | €190,93 | €-21,77 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.505,50 | €1.356,82 | €4.070,45 | €142,73 | €54,04 |
| TEST | Combo Trend | 9 | €9.475,09 | €2.667,77 | €5.335,55 | €189,50 | €98,10 |
| TEST | Scanner Top5 Btc Tp3 V1 | 6 | €9.470,38 | €2.574,21 | €5.148,43 | €188,39 | €65,58 |
| TEST | Master Adaptive V1 | 5 | €9.468,81 | €4.044,01 | €8.088,01 | €190,19 | €-21,68 |
| TEST | Scanner Top5 Btc Runner25 V1 | 6 | €9.464,84 | €2.572,71 | €5.145,42 | €188,28 | €65,54 |
| TEST | Benchmark trend following EMA 1H | 7 | €9.450,36 | €3.456,78 | €6.913,56 | €139,67 | €109,65 |
| TEST | Master Adaptive Runner25 V1 | 7 | €9.449,17 | €2.982,76 | €5.965,52 | €188,53 | €73,73 |
| TEST | Forza relativa 1H V1 | 6 | €9.411,34 | €2.803,25 | €5.606,50 | €188,15 | €3,87 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 6 | €9.400,06 | €2.555,10 | €5.110,20 | €186,99 | €65,09 |
| TEST | Master Adaptive Strict3 V1 | 4 | €9.365,36 | €2.164,98 | €4.329,96 | €184,17 | €214,11 |
| TEST | Scanner Top10 Long | 5 | €9.365,21 | €2.525,43 | €5.050,87 | €187,30 | €52,72 |
| TEST | Scanner Top15 Long | 5 | €9.365,21 | €2.525,43 | €5.050,87 | €187,30 | €52,72 |
| TEST | Scanner Top20 Long | 5 | €9.365,21 | €2.525,43 | €5.050,87 | €187,30 | €52,72 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.343,00 | €3.990,28 | €7.980,55 | €187,67 | €-21,39 |
| TEST | Combo Scanner | 5 | €9.281,18 | €2.742,78 | €5.485,56 | €185,62 | €67,34 |
| TEST | Scanner Top5 Btc Mfe V1 | 6 | €9.220,59 | €2.506,32 | €5.012,63 | €183,42 | €63,85 |
| TEST | 1H Fast V3 Long Only V1 | 4 | €9.148,76 | €1.694,88 | €5.084,64 | €136,60 | €68,20 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 1 | €9.101,40 | €192,15 | €384,31 | €46,12 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 6 | €8.948,28 | €3.586,88 | €7.173,75 | €131,96 | €75,03 |

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
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | Portafoglio sperimentale separato. |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.731,82 | €-283,07 | 40 | 40 | 35,00% | 0,78 | €-7,08 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.678,56 | €632,45 | 59 | 59 | 47,46% | 1,44 | €10,72 | 3,63% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.527,70 | €453,69 | 55 | 55 | 50,91% | 1,42 | €8,25 | 3,00% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.506,14 | €436,77 | 103 | 103 | 43,69% | 1,20 | €4,24 | 3,21% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.427,14 | €382,12 | 27 | 27 | 44,44% | 1,67 | €14,15 | 3,63% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.420,33 | €340,71 | 29 | 29 | 48,28% | 1,57 | €11,75 | 3,55% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.411,79 | €367,24 | 20 | 20 | 50,00% | 1,85 | €18,36 | 2,40% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.382,24 | €309,95 | 29 | 29 | 51,72% | 1,42 | €10,69 | 2,31% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.340,80 | €244,16 | 91 | 91 | 41,76% | 1,12 | €2,68 | 6,15% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.329,69 | €256,02 | 37 | 37 | 51,35% | 1,36 | €6,92 | 4,32% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.308,28 | €257,89 | 82 | 82 | 39,02% | 1,16 | €3,15 | 4,31% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.226,81 | €159,28 | 61 | 61 | 47,54% | 1,11 | €2,61 | 3,56% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.178,68 | €58,92 | 94 | 94 | 42,55% | 1,03 | €0,63 | 3,64% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.178,25 | €103,88 | 50 | 50 | 46,00% | 1,11 | €2,08 | 5,79% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.168,22 | €113,82 | 67 | 67 | 43,28% | 1,07 | €1,70 | 7,66% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.130,84 | €131,11 | 28 | 28 | 39,29% | 1,25 | €4,68 | 2,27% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €10.106,20 | €40,71 | 92 | 92 | 41,30% | 1,02 | €0,44 | 5,76% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €10.083,47 | €-10,76 | 55 | 55 | 38,18% | 0,99 | €-0,20 | 6,15% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.063,01 | €57,88 | 42 | 42 | 50,00% | 1,07 | €1,38 | 2,94% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.058,10 | €-3,16 | 5 | 5 | 60,00% | 0,97 | €-0,63 | 1,49% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.039,42 | €-58,14 | 107 | 107 | 35,51% | 0,97 | €-0,54 | 3,95% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.013,79 | €-40,46 | 4 | 4 | 50,00% | 0,63 | €-10,11 | 1,13% |
| TEST | Doge Ema 1H | Trend following EMA | €10.011,70 | €-15,39 | 12 | 12 | 58,33% | 0,94 | €-1,28 | 2,09% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.007,98 | €7,98 | 24 | 24 | 45,83% | 1,09 | €0,33 | 0,33% |
| TEST | Combo Adaptive | Combo Adaptive | €10.007,56 | €-163,51 | 57 | 57 | 36,84% | 0,85 | €-2,87 | 5,27% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.002,03 | €2,03 | 6 | 6 | 50,00% | 1,02 | €0,34 | 1,50% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.001,60 | €1,60 | 24 | 24 | 45,83% | 1,09 | €0,07 | 0,07% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,42 | €1,42 | 3 | 3 | 66,67% | 2,74 | €0,47 | 0,08% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.000,95 | €-56,62 | 2 | 2 | 0,00% | 0,00 | €-28,31 | 1,36% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,28 | €0,28 | 3 | 3 | 66,67% | 2,74 | €0,09 | 0,02% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.999,47 | €-0,53 | 3 | 3 | 66,67% | 0,77 | €-0,18 | 0,16% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,61 | €-5,39 | 12 | 12 | 33,33% | 0,40 | €-0,45 | 0,11% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.994,09 | €-3,47 | 92 | 92 | 42,39% | 1,00 | €-0,04 | 6,27% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,76 | €-10,24 | 14 | 14 | 35,71% | 0,31 | €-0,73 | 0,14% |
| TEST | Btc Ema 4H | Trend following EMA | €9.989,13 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,23% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,06 | €-26,94 | 12 | 12 | 33,33% | 0,40 | €-2,25 | 0,53% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.971,04 | €-28,96 | 14 | 14 | 35,71% | 0,61 | €-2,07 | 0,71% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €9.958,96 | €-117,76 | 30 | 30 | 43,33% | 0,84 | €-3,93 | 3,94% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.948,80 | €-51,20 | 14 | 14 | 35,71% | 0,31 | €-3,66 | 0,72% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.944,63 | €-50,70 | 9 | 9 | 55,56% | 0,77 | €-5,63 | 1,63% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.930,87 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,81% |
| TEST | Btc Ema 1H | Trend following EMA | €9.926,82 | €-141,33 | 7 | 7 | 28,57% | 0,48 | €-20,19 | 1,72% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.926,30 | €-73,70 | 12 | 12 | 33,33% | 0,12 | €-6,14 | 0,89% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.901,43 | €-255,26 | 34 | 34 | 38,24% | 0,76 | €-7,51 | 6,54% |
| TEST | Ampia 4H | Confluenza trend | €9.886,46 | €-125,24 | 34 | 34 | 23,53% | 0,86 | €-3,68 | 4,36% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.870,59 | €-98,48 | 23 | 23 | 43,48% | 0,79 | €-4,28 | 2,18% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.857,34 | €-181,81 | 59 | 55 | 44,07% | 0,87 | €-3,08 | 5,62% |
| TEST | Sol Ema 4H | Trend following EMA | €9.845,78 | €-154,22 | 3 | 3 | 0,00% | 0,00 | €-51,41 | 1,57% |
| TEST | Eth Ema 4H | Trend following EMA | €9.842,00 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,73% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.836,81 | €-228,54 | 55 | 55 | 34,55% | 0,84 | €-4,16 | 8,46% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.836,12 | €-332,00 | 64 | 64 | 32,81% | 0,74 | €-5,19 | 6,25% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €9.826,20 | €-330,30 | 77 | 77 | 48,05% | 0,78 | €-4,29 | 6,78% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.817,19 | €-182,81 | 6 | 6 | 16,67% | 0,34 | €-30,47 | 2,06% |
| TEST | Sol Ema 1H | Trend following EMA | €9.813,68 | €-186,32 | 8 | 8 | 25,00% | 0,43 | €-23,29 | 2,63% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.811,17 | €-296,11 | 60 | 60 | 40,00% | 0,82 | €-4,94 | 4,70% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.785,70 | €-278,21 | 35 | 35 | 31,43% | 0,67 | €-7,95 | 4,45% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.781,27 | €-373,52 | 39 | 39 | 33,33% | 0,69 | €-9,58 | 6,13% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.775,94 | €-354,13 | 35 | 35 | 28,57% | 0,57 | €-10,12 | 4,71% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.772,66 | €-233,44 | 28 | 25 | 35,71% | 0,71 | €-8,34 | 3,89% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.771,84 | €-292,43 | 44 | 44 | 34,09% | 0,72 | €-6,65 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.771,84 | €-292,43 | 44 | 44 | 34,09% | 0,72 | €-6,65 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.771,84 | €-292,43 | 44 | 44 | 34,09% | 0,72 | €-6,65 | 5,27% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.761,99 | €-393,48 | 121 | 121 | 38,02% | 0,85 | €-3,25 | 6,75% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.757,74 | €-362,51 | 15 | 15 | 33,33% | 0,35 | €-24,17 | 3,11% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.753,95 | €-351,10 | 65 | 65 | 44,62% | 0,81 | €-5,40 | 4,93% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.749,98 | €-297,68 | 38 | 38 | 34,21% | 0,60 | €-7,83 | 4,03% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.731,55 | €-422,45 | 49 | 49 | 38,78% | 0,69 | €-8,62 | 5,80% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.728,99 | €-267,90 | 28 | 28 | 35,71% | 0,72 | €-9,57 | 4,71% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.716,12 | €-427,91 | 82 | 82 | 40,24% | 0,79 | €-5,22 | 5,62% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.706,12 | €-358,39 | 36 | 36 | 33,33% | 0,58 | €-9,96 | 5,27% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.700,99 | €-322,64 | 15 | 15 | 26,67% | 0,35 | €-21,51 | 3,52% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.697,12 | €-339,61 | 40 | 40 | 30,00% | 0,74 | €-8,49 | 4,45% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.696,17 | €-344,88 | 66 | 66 | 42,42% | 0,80 | €-5,23 | 6,53% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.692,38 | €-307,62 | 8 | 8 | 25,00% | 0,05 | €-38,45 | 3,11% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.691,35 | €-373,06 | 37 | 37 | 32,43% | 0,53 | €-10,08 | 5,27% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.683,34 | €-365,97 | 68 | 65 | 38,24% | 0,83 | €-5,38 | 8,11% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.674,16 | €-325,84 | 9 | 9 | 22,22% | 0,17 | €-36,20 | 3,94% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.652,37 | €-512,62 | 45 | 45 | 31,11% | 0,50 | €-11,39 | 6,25% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.635,01 | €-483,73 | 15 | 15 | 20,00% | 0,16 | €-32,25 | 4,33% |
| TEST | Eth Ema 1H | Trend following EMA | €9.622,18 | €-377,82 | 10 | 10 | 20,00% | 0,12 | €-37,78 | 3,78% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.616,78 | €-447,14 | 64 | 64 | 32,81% | 0,68 | €-6,99 | 6,41% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.609,71 | €-554,55 | 58 | 58 | 34,48% | 0,55 | €-9,56 | 6,07% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.608,95 | €-459,44 | 52 | 52 | 34,62% | 0,68 | €-8,84 | 8,14% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.574,78 | €-463,04 | 36 | 36 | 25,00% | 0,65 | €-12,86 | 6,03% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.560,90 | €-558,04 | 95 | 95 | 37,89% | 0,74 | €-5,87 | 6,72% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.553,79 | €-597,40 | 56 | 56 | 37,50% | 0,62 | €-10,67 | 7,59% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.515,69 | €-456,42 | 39 | 39 | 20,51% | 0,59 | €-11,70 | 6,68% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.505,57 | €-466,57 | 34 | 34 | 26,47% | 0,57 | €-13,72 | 6,27% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.505,50 | €-545,83 | 39 | 39 | 30,77% | 0,54 | €-14,00 | 7,00% |
| TEST | Combo Trend | Combo Trend | €9.475,09 | €-622,46 | 88 | 88 | 31,82% | 0,74 | €-7,07 | 9,82% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.470,38 | €-592,54 | 40 | 40 | 27,50% | 0,53 | €-14,81 | 9,16% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.468,81 | €-503,45 | 36 | 36 | 25,00% | 0,60 | €-13,98 | 6,08% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.464,84 | €-598,04 | 44 | 44 | 29,55% | 0,53 | €-13,59 | 9,46% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.450,36 | €-657,74 | 58 | 58 | 27,59% | 0,54 | €-11,34 | 7,38% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.449,17 | €-620,05 | 33 | 33 | 21,21% | 0,51 | €-18,79 | 6,64% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.411,34 | €-589,79 | 78 | 78 | 28,21% | 0,67 | €-7,56 | 8,31% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.400,06 | €-662,39 | 36 | 36 | 27,78% | 0,42 | €-18,40 | 8,92% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.365,36 | €-845,83 | 39 | 39 | 23,08% | 0,50 | €-21,69 | 9,06% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.365,21 | €-684,88 | 39 | 39 | 33,33% | 0,42 | €-17,56 | 9,13% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.365,21 | €-684,88 | 39 | 39 | 33,33% | 0,42 | €-17,56 | 9,13% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.365,21 | €-684,88 | 39 | 39 | 33,33% | 0,42 | €-17,56 | 9,13% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.343,00 | €-629,62 | 71 | 71 | 47,89% | 0,57 | €-8,87 | 7,33% |
| TEST | Combo Scanner | Combo Scanner | €9.281,18 | €-784,58 | 64 | 64 | 32,81% | 0,58 | €-12,26 | 10,13% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.220,59 | €-840,67 | 48 | 48 | 29,17% | 0,33 | €-17,51 | 9,50% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.148,76 | €-916,35 | 72 | 72 | 27,78% | 0,56 | €-12,73 | 10,12% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.101,40 | €-898,33 | 31 | 31 | 16,13% | 0,32 | €-28,98 | 10,58% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €8.948,28 | €-1.124,73 | 71 | 71 | 29,58% | 0,37 | €-15,84 | 11,05% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00378 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €14,13 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | CYS | LONG | Confluenza trend | 240m | 3,0x | 1,54541 | 1,54541 | 1,35996 | 1,03800 | 1,91631 | €134,84 | €404,53 | €48,54 | €0,00 |
| Principale 4H | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 62813,56000 | 64418,98882 | 84222,33283 | 61375,57203 | €23,48 | €70,44 | €1,13 | €0,66 |
| Bilanciata 1H V1 | SPCX | LONG | Confluenza trend | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €517,88 | €1.553,64 | €51,53 | €0,00 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.143,13 | €3.429,40 | €49,38 | €-0,00 |
| Bilanciata 1H V1 | CYS | LONG | Confluenza trend | 60m | 3,0x | 1,54541 | 1,54541 | 1,35996 | 1,03800 | 1,91631 | €134,24 | €402,71 | €48,32 | €0,00 |
| Bilanciata 1H V1 | BEAT | SHORT | Confluenza trend | 60m | 3,0x | 1,04289 | 1,04289 | 1,03001 | 1,38531 | 0,79260 | €139,17 | €417,52 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06991 | 0,06956 | 0,07091 | 0,09286 | 0,06789 | €24,68 | €74,04 | €1,07 | €0,37 |
| Bilanciata 1H V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 1,00430 | 1,00378 | 1,01876 | 1,33404 | 0,97538 | €21,08 | €63,23 | €0,91 | €0,03 |
| 1H Balanced Long No Rhv V1 | CYS | LONG | Confluenza trend | 60m | 3,0x | 1,50020 | 1,50020 | 1,50020 | 1,00763 | 1,86025 | €131,62 | €394,86 | €0,00 | €0,00 |
| 1H Balanced Long No Rhv V1 | XOM | LONG | Confluenza trend | 60m | 3,0x | 160,24609 | 160,24609 | 157,58464 | 107,63196 | 165,56900 | €952,03 | €2.856,08 | €47,44 | €0,00 |
| 1H Balanced Long No Rhv V1 | APR | LONG | Confluenza trend | 60m | 3,0x | 0,49291 | 0,49291 | 0,43376 | 0,33107 | 0,61121 | €131,87 | €395,61 | €47,47 | €0,00 |
| 1H Balanced Long No Rhv V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00756 | 0,00860 | 0,00665 | 0,00507 | 0,00937 | €130,81 | €392,43 | €47,09 | €54,06 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1182,39901 | 1181,69000 | 1155,07338 | 794,17800 | 1237,05028 | €10,49 | €31,46 | €0,73 | €-0,02 |
| 1H Balanced Short Trend Down Strict V1 | BEAT | SHORT | Confluenza trend | 60m | 3,0x | 1,03900 | 1,03900 | 1,03001 | 1,38014 | 0,78964 | €138,10 | €414,31 | €0,00 | €-0,00 |
| 1H Balanced Short Trend Down Strict V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 63436,91008 | 62813,56000 | 64350,40159 | 84265,36222 | 61609,92707 | €1.150,82 | €3.452,45 | €49,72 | €33,92 |
| 1H Balanced Short Trend Down Strict V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €858,47 | €2.575,40 | €49,89 | €-0,00 |
| 1H Balanced Short Trend Down Strict V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,07014 | 0,06956 | 0,07115 | 0,09316 | 0,06812 | €1.155,95 | €3.467,86 | €49,94 | €28,48 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.179,68 | €3.539,03 | €50,96 | €-0,00 |
| Bilanciata 1H V2 | BTC | SHORT | Confluenza trend V2 | 60m | 3,0x | 63596,27820 | 62813,56000 | 64512,06461 | 84477,05621 | 61764,70539 | €1.127,13 | €3.381,38 | €48,69 | €41,62 |
| Bilanciata 1H V2 | CYS | LONG | Confluenza trend V2 | 60m | 3,0x | 1,50020 | 1,50020 | 1,50020 | 1,00763 | 1,86025 | €136,27 | €408,82 | €0,00 | €0,00 |
| Bilanciata 1H V2 | XRP | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,00538 | 1,00378 | 1,01986 | 1,33548 | 0,97642 | €37,09 | €111,28 | €1,60 | €0,18 |
| Bilanciata 1H V2 | BEAT | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,96465 | 0,96465 | 1,08040 | 1,28137 | 0,73313 | €124,99 | €374,96 | €45,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €524,66 | €1.573,99 | €52,20 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.207,94 | €3.623,82 | €52,18 | €-0,00 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63106,84706 | 84757,27849 | 61969,58760 | €1.129,53 | €3.388,60 | €0,00 | €52,77 |
| Bilanciata 1H V3 Filtered | CYS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,91879 | €140,87 | €422,61 | €50,71 | €0,00 |
| Bilanciata 1H V3 Filtered | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €26,57 | €79,71 | €1,54 | €-0,00 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,06956 | 0,07064 | 0,09250 | 0,06763 | €14,62 | €43,87 | €0,63 | €0,05 |
| 1H Fast Score 6 75 V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.575,50 | €4.726,51 | €0,00 | €73,61 |
| 1H Fast Score 6 75 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,50020 | 1,50020 | 1,50020 | 1,00763 | 1,77024 | €145,36 | €436,08 | €0,00 | €0,00 |
| 1H Fast Score 6 75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,95921 | 0,95921 | 1,07431 | 1,27415 | 0,78655 | €142,15 | €426,45 | €51,17 | €-0,00 |
| 1H Fast Score 6 75 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €32,86 | €98,57 | €1,97 | €1,38 |
| 1H Fast Score 6 75 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06952 | 0,06956 | 0,07030 | 0,09234 | 0,06835 | €1.542,34 | €4.627,02 | €51,82 | €-2,78 |
| 1H Fast Score 6 75 No Trend Up V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.533,61 | €4.600,84 | €0,00 | €71,65 |
| 1H Fast Score 6 75 No Trend Up V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,50020 | 1,50020 | 1,50020 | 1,00763 | 1,77024 | €141,49 | €424,48 | €0,00 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,95921 | 0,95921 | 1,07431 | 1,27415 | 0,78655 | €138,37 | €415,11 | €49,81 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €31,98 | €95,95 | €1,92 | €1,35 |
| 1H Fast Score 6 75 No Trend Up V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06952 | 0,06956 | 0,07030 | 0,09234 | 0,06835 | €1.501,33 | €4.504,00 | €50,44 | €-2,70 |
| 1H Fast Score 6 75 Range Only V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.542,02 | €4.626,07 | €0,00 | €72,04 |
| 1H Fast Score 6 75 Range Only V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,48830 | 1,48830 | 1,48830 | 0,99964 | 1,75619 | €143,02 | €429,06 | €0,00 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.591,68 | €4.775,04 | €0,00 | €74,36 |
| 1H Fast Score 6 75 Cost Aware V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,50020 | 1,50020 | 1,50020 | 1,00763 | 1,77024 | €145,92 | €437,77 | €0,00 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,95974 | 0,95974 | 1,07491 | 1,27485 | 0,78699 | €145,66 | €436,97 | €52,44 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,03776 | 0,03777 | 0,04229 | 0,05016 | 0,03097 | €144,75 | €434,26 | €52,11 | €-0,09 |
| 1H Fast Nohigh Cap75 V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.585,67 | €4.757,02 | €0,00 | €74,08 |
| 1H Fast Nohigh Cap75 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €200,91 | €602,72 | €51,68 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06991 | 0,06956 | 0,07069 | 0,09286 | 0,06873 | €1.537,89 | €4.613,67 | €51,67 | €22,84 |
| 1H Fast Nohigh Cap75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,73802 | €143,81 | €431,44 | €47,91 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1161,28635 | 1181,69000 | 1161,28781 | 779,99733 | 1196,37370 | €15,47 | €46,40 | €0,00 | €0,82 |
| 1H Fast Nohigh Cap75 V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1618,90076 | 1617,93000 | 1582,80136 | 1087,36168 | 1673,04985 | €20,17 | €60,51 | €1,35 | €-0,04 |
| 1H Fast Long Btc 1 3 Cap75 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,82594 | €139,31 | €417,94 | €50,15 | €0,00 |
| 1H Fast No Pepe V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.518,20 | €4.554,59 | €0,00 | €70,93 |
| 1H Fast No Pepe V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,51880 | 1,51880 | 1,51880 | 1,02013 | 1,79219 | €136,73 | €410,18 | €0,00 | €0,00 |
| 1H Fast No Pepe V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,00538 | 1,00378 | 1,01664 | 1,33548 | 0,98849 | €1.503,80 | €4.511,41 | €50,53 | €7,17 |
| 1H Fast No Pepe V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1161,28635 | 1181,69000 | 1161,28781 | 779,99733 | 1196,37370 | €34,85 | €104,55 | €0,00 | €1,84 |
| 1H Fast No Pepe V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00782 | 0,00860 | 0,00688 | 0,00525 | 0,00923 | €137,46 | €412,39 | €49,49 | €40,90 |
| 1H Fast No Pepe V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06952 | 0,06956 | 0,07030 | 0,09234 | 0,06835 | €36,38 | €109,13 | €1,22 | €-0,07 |
| 1H Fast Tp2 V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62377,95391 | €1.482,17 | €4.446,51 | €0,00 | €69,25 |
| 1H Fast Tp2 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,64299 | 1,64299 | 1,47977 | 1,10354 | 1,96941 | €161,09 | €483,28 | €48,01 | €0,00 |
| 1H Fast Tp2 V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,00538 | 1,00378 | 1,01664 | 1,33548 | 0,98286 | €55,98 | €167,93 | €1,88 | €0,27 |
| 1H Fast Tp2 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,68886 | €146,30 | €438,91 | €48,73 | €-0,00 |
| 1H Fast Tp2 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00803 | 0,00860 | 0,00706 | 0,00539 | 0,00995 | €133,72 | €401,16 | €48,14 | €28,42 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,03778 | 0,03777 | 0,04232 | 0,05019 | 0,02871 | €9,36 | €28,07 | €3,37 | €0,01 |
| 1H Fast Tp2 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1182,39901 | 1181,69000 | 1161,14575 | 794,17800 | 1224,90555 | €15,88 | €47,65 | €0,86 | €-0,03 |
| Rapida 1H V2 | XRP | SHORT | Momentum / breakout V2 | 60m | 3,0x | 1,00538 | 1,00378 | 1,01664 | 1,33548 | 0,98849 | €1.461,59 | €4.384,76 | €49,11 | €6,97 |
| Rapida 1H V3 Filtered | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.474,48 | €4.423,44 | €0,00 | €68,89 |
| Rapida 1H V3 Filtered | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €177,34 | €532,02 | €45,61 | €0,00 |
| Rapida 1H V3 Filtered | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00756 | 0,00860 | 0,00665 | 0,00507 | 0,00892 | €135,20 | €405,61 | €48,67 | €55,87 |
| Rapida 1H V3 Filtered | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €776,07 | €2.328,22 | €46,56 | €32,69 |
| Rapida 1H V3 Filtered | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06952 | 0,06956 | 0,07030 | 0,09234 | 0,06835 | €144,72 | €434,17 | €4,86 | €-0,26 |
| 1H Fast V3 Cap75 V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.501,29 | €4.503,87 | €0,00 | €70,14 |
| 1H Fast V3 Cap75 V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,82594 | €139,51 | €418,54 | €50,22 | €0,00 |
| 1H Fast V3 Cap75 V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,73802 | €152,00 | €456,00 | €50,63 | €-0,00 |
| 1H Fast V3 Cap75 V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €17,79 | €53,38 | €1,07 | €0,75 |
| 1H Fast V3 Cap75 V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06952 | 0,06956 | 0,07030 | 0,09234 | 0,06835 | €1.484,03 | €4.452,08 | €49,86 | €-2,67 |
| 1H Fast V3 Nohigh V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.489,03 | €4.467,09 | €0,00 | €69,57 |
| 1H Fast V3 Nohigh V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €187,10 | €561,31 | €48,13 | €0,00 |
| 1H Fast V3 Nohigh V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06991 | 0,06956 | 0,07069 | 0,09286 | 0,06873 | €1.375,16 | €4.125,47 | €46,21 | €20,42 |
| 1H Fast V3 Nohigh V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00756 | 0,00860 | 0,00665 | 0,00507 | 0,00892 | €131,98 | €395,95 | €47,51 | €54,54 |
| 1H Fast V3 Nohigh V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €11,94 | €35,81 | €0,72 | €0,50 |
| 1H Fast V3 Nohigh V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1617,93000 | 1582,80136 | 1087,36168 | 1673,04985 | €25,88 | €77,64 | €1,73 | €-0,05 |
| 1H Fast V3 Long Only V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,46019 | 1,46019 | 1,46056 | 0,98076 | 1,72303 | €127,65 | €382,94 | €0,00 | €0,00 |
| 1H Fast V3 Long Only V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €757,07 | €2.271,20 | €45,42 | €31,89 |
| 1H Fast V3 Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00782 | 0,00860 | 0,00688 | 0,00525 | 0,00923 | €126,18 | €378,54 | €45,42 | €37,54 |
| 1H Fast V3 Long Only V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1617,93000 | 1582,80136 | 1087,36168 | 1673,04985 | €683,99 | €2.051,96 | €45,76 | €-1,23 |
| 1H Fast V3 Long Nohigh Cap75 V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,82594 | €135,24 | €405,73 | €48,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | APR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,47765 | 0,47765 | 0,42033 | 0,32082 | 0,56362 | €135,15 | €405,45 | €48,65 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00725 | 0,00860 | 0,00758 | 0,00487 | 0,00855 | €135,47 | €406,41 | €0,00 | €75,78 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €806,60 | €2.419,81 | €48,39 | €33,97 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1617,93000 | 1582,80136 | 1087,36168 | 1673,04985 | €25,80 | €77,41 | €1,73 | €-0,05 |
| 1H Fast V3 No Esports V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.444,46 | €4.333,39 | €0,00 | €67,48 |
| 1H Fast V3 No Esports V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €173,73 | €521,19 | €44,69 | €0,00 |
| 1H Fast V3 No Esports V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00756 | 0,00860 | 0,00665 | 0,00507 | 0,00892 | €132,88 | €398,64 | €47,84 | €54,91 |
| 1H Fast V3 No Esports V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €42,36 | €127,08 | €2,54 | €1,78 |
| 1H Fast V3 No Esports V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06952 | 0,06956 | 0,07030 | 0,09234 | 0,06835 | €1.420,31 | €4.260,93 | €47,72 | €-2,56 |
| 1H Fast V3 No Esports Long Only V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,46019 | 1,46019 | 1,46056 | 0,98076 | 1,72303 | €134,07 | €402,21 | €0,00 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €795,15 | €2.385,44 | €47,70 | €33,49 |
| 1H Fast V3 No Esports Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00782 | 0,00860 | 0,00688 | 0,00525 | 0,00923 | €132,53 | €397,58 | €47,71 | €39,43 |
| 1H Fast V3 No Esports Long Only V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1617,93000 | 1582,80136 | 1087,36168 | 1673,04985 | €718,39 | €2.155,18 | €48,06 | €-1,29 |
| 1H Fast V3 No Esports Mfe Lock V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.484,18 | €4.452,53 | €0,00 | €69,34 |
| 1H Fast V3 No Esports Mfe Lock V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €178,51 | €535,52 | €45,91 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00756 | 0,00860 | 0,00665 | 0,00507 | 0,00892 | €136,09 | €408,28 | €48,99 | €56,24 |
| 1H Fast V3 No Esports Mfe Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €781,18 | €2.343,53 | €46,86 | €32,90 |
| 1H Fast V3 No Esports Mfe Lock V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06952 | 0,06956 | 0,07030 | 0,09234 | 0,06835 | €145,68 | €437,03 | €4,89 | €-0,26 |
| 1H Fast V3 No Esports Stress Guard V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.498,86 | €4.496,57 | €0,00 | €70,03 |
| 1H Fast V3 No Esports Stress Guard V1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,00538 | 1,00378 | 1,01664 | 1,33548 | 0,98849 | €1.482,09 | €4.446,28 | €49,80 | €7,07 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,82594 | €136,31 | €408,93 | €49,07 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | APR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,47765 | 0,47765 | 0,42033 | 0,32082 | 0,56362 | €135,37 | €406,10 | €48,73 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00725 | 0,00860 | 0,00638 | 0,00487 | 0,00855 | €131,77 | €395,30 | €47,44 | €73,71 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1165,32878 | 1181,69000 | 1142,02581 | 782,71250 | 1200,28321 | €802,37 | €2.407,11 | €48,13 | €33,80 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SNDK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1618,90076 | 1617,93000 | 1582,80136 | 1087,36168 | 1673,04985 | €25,50 | €76,51 | €1,71 | €-0,05 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 386,58243 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €0,00 | €0,00 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 1,00378 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €11,01 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63404,51656 | 62813,56000 | 64723,33050 | 94789,75226 | 59711,83752 | €59,90 | €119,81 | €2,49 | €1,12 |
| Forza relativa 1H V1 | SPCX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,10 | €1.452,21 | €48,16 | €0,00 |
| Forza relativa 1H V1 | ADA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.677,78 | €3.355,57 | €48,32 | €-0,00 |
| Forza relativa 1H V1 | CYS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1,62778 | 1,62778 | 1,43244 | 0,82203 | 2,05751 | €195,68 | €391,36 | €46,96 | €0,00 |
| Forza relativa 1H V1 | BEAT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,95007 | 0,95007 | 1,06408 | 1,42035 | 0,69925 | €169,57 | €339,13 | €40,70 | €-0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €20,07 | €40,15 | €0,64 | €-0,00 |
| Forza relativa 1H V1 | AKE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00955 | €14,04 | €28,09 | €3,37 | €3,87 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.698,68 | €3.397,35 | €48,92 | €-0,00 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,03900 | 1,03900 | 1,03900 | 1,55331 | 0,76471 | €200,27 | €400,55 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | PEPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.249,32 | €2.498,63 | €48,41 | €-0,00 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00955 | €196,65 | €393,29 | €47,20 | €54,18 |
| Forza relativa 1H V2 | SKHYNIX | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €23,34 | €46,68 | €1,08 | €-0,03 |
| Benchmark Donchian breakout 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63807,23600 | 62813,56000 | 64828,15178 | 95391,81782 | 61254,94656 | €1.676,44 | €3.352,88 | €53,65 | €52,21 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.304,34 | €2.608,68 | €53,61 | €-0,00 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,06956 | 0,07063 | 0,10393 | 0,06674 | €1.669,15 | €3.338,30 | €53,41 | €-2,00 |
| Donchian 1H Gb20 120R V1 | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63807,23600 | 62813,56000 | 64828,15178 | 95391,81782 | 61254,94656 | €1.636,97 | €3.273,94 | €52,38 | €50,99 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.273,63 | €2.547,26 | €52,35 | €-0,00 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,06956 | 0,07063 | 0,10393 | 0,06674 | €1.629,85 | €3.259,70 | €52,16 | €-1,96 |
| Benchmark Bollinger mean reversion 1H | HYPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 57,25563 | 56,62100 | 56,86676 | 85,59716 | 56,22502 | €1.935,76 | €3.871,51 | €0,00 | €42,91 |
| Benchmark trend following EMA 1H | BTC | SHORT | Trend following EMA | 60m | 2,0x | 64070,44335 | 62813,56000 | 63182,46843 | 95785,31281 | 61815,16374 | €1.516,95 | €3.033,89 | €0,00 | €59,52 |
| Benchmark trend following EMA 1H | SPCX | LONG | Trend following EMA | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €658,50 | €1.316,99 | €48,53 | €0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €28,20 | €56,39 | €0,90 | €-0,00 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.036,54 | €2.073,07 | €45,58 | €-0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,07014 | 0,06956 | 0,07126 | 0,10485 | 0,06767 | €23,05 | €46,10 | €0,74 | €0,38 |
| Benchmark trend following EMA 1H | AKE | LONG | Trend following EMA | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00955 | €180,04 | €360,09 | €43,21 | €49,60 |
| Benchmark trend following EMA 1H | SKHYNIX | LONG | Trend following EMA | 60m | 2,0x | 1175,20470 | 1181,69000 | 1144,24012 | 593,47837 | 1243,32677 | €13,51 | €27,03 | €0,71 | €0,15 |
| Scanner Top 5 Long 1H | SPCX | LONG | Scanner Top 5 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €780,60 | €1.561,19 | €51,78 | €0,00 |
| Scanner Top 5 Long 1H | XOM | LONG | Scanner Top 5 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.527,62 | €3.055,23 | €50,74 | €0,00 |
| Scanner Top 5 Long 1H | APR | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €209,11 | €418,21 | €50,19 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00937 | €207,87 | €415,75 | €49,89 | €57,27 |
| Scanner Top 5 Long 1H | SNDK | LONG | Scanner Top 5 Long | 60m | 2,0x | 1618,90076 | 1617,93000 | 1572,48725 | 817,54488 | 1711,72778 | €13,45 | €26,90 | €0,77 | €-0,02 |
| Scanner Bottom 5 Short 1H | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 62813,56000 | 63157,87454 | 95785,31281 | 62225,21458 | €1.717,08 | €3.434,17 | €0,00 | €67,37 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.735,51 | €3.471,03 | €49,98 | €-0,00 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €199,49 | €398,98 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.093,58 | €2.187,15 | €44,19 | €-0,00 |
| Scanner Bottom 5 Short 1H | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00378 | 1,01876 | 1,50143 | 0,97538 | €36,97 | €73,95 | €1,06 | €0,04 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 485,06297 | 489,56000 | 493,83011 | 725,16914 | 467,52868 | €12,76 | €25,52 | €0,46 | €-0,24 |
| Scanner Top10 Long | SPCX | LONG | Scanner Top10 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top10 Long | XOM | LONG | Scanner Top10 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top10 Long | APR | LONG | Scanner Top10 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €192,60 | €385,20 | €46,22 | €0,00 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00937 | €191,43 | €382,85 | €45,94 | €52,74 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €-0,02 |
| Scanner Bottom10 Short | BTC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 64070,44335 | 62813,56000 | 63157,87454 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €0,00 | €67,81 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €202,72 | €405,43 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | PEPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom10 Short | XRP | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,00430 | 1,00378 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,04 |
| Scanner Bottom10 Short | ZEC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 485,06297 | 489,56000 | 493,83011 | 725,16914 | 467,52868 | €12,97 | €25,94 | €0,47 | €-0,24 |
| Scanner Top15 Long | SPCX | LONG | Scanner Top15 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top15 Long | XOM | LONG | Scanner Top15 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top15 Long | APR | LONG | Scanner Top15 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €192,60 | €385,20 | €46,22 | €0,00 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00937 | €191,43 | €382,85 | €45,94 | €52,74 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €-0,02 |
| Scanner Bottom15 Short | BTC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 64070,44335 | 62813,56000 | 63157,87454 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €0,00 | €67,81 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €202,72 | €405,43 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | PEPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom15 Short | XRP | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,00430 | 1,00378 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,04 |
| Scanner Bottom15 Short | ZEC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 485,06297 | 489,56000 | 493,83011 | 725,16914 | 467,52868 | €12,97 | €25,94 | €0,47 | €-0,24 |
| Scanner Top20 Long | SPCX | LONG | Scanner Top20 Long | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €0,00 |
| Scanner Top20 Long | XOM | LONG | Scanner Top20 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top20 Long | APR | LONG | Scanner Top20 Long | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €192,60 | €385,20 | €46,22 | €0,00 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00937 | €191,43 | €382,85 | €45,94 | €52,74 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1237,05028 | €15,36 | €30,73 | €0,71 | €-0,02 |
| Scanner Bottom20 Short | BTC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 64070,44335 | 62813,56000 | 63157,87454 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €0,00 | €67,81 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.763,98 | €3.527,95 | €50,80 | €-0,00 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €202,72 | €405,43 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | PEPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.122,77 | €2.245,54 | €45,37 | €-0,00 |
| Scanner Bottom20 Short | XRP | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,00430 | 1,00378 | 1,01876 | 1,50143 | 0,97538 | €37,54 | €75,07 | €1,08 | €0,04 |
| Scanner Bottom20 Short | ZEC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 485,06297 | 489,56000 | 493,83011 | 725,16914 | 467,52868 | €12,97 | €25,94 | €0,47 | €-0,24 |
| Scanner Top 5 + forza BTC 1H | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €770,70 | €1.541,40 | €51,12 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.470,86 | €2.941,72 | €48,86 | €0,00 |
| Scanner Top 5 + forza BTC 1H | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €192,28 | €384,55 | €46,15 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00739 | 0,00860 | 0,00650 | 0,00373 | 0,00934 | €202,99 | €405,99 | €48,72 | €66,35 |
| Scanner Top 5 + forza BTC 1H | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1639,70939 | €18,79 | €37,58 | €0,00 | €1,79 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €18,20 | €36,40 | €0,84 | €-0,02 |
| Scanner Top5 Btc Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €722,42 | €1.444,84 | €47,92 | €0,00 |
| Scanner Top5 Btc Mfe V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.378,72 | €2.757,43 | €45,80 | €0,00 |
| Scanner Top5 Btc Mfe V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €180,23 | €360,46 | €43,26 | €0,00 |
| Scanner Top5 Btc Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00739 | 0,00860 | 0,00650 | 0,00373 | 0,00934 | €190,28 | €380,55 | €45,67 | €62,20 |
| Scanner Top5 Btc Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1639,70939 | €17,61 | €35,23 | €0,00 | €1,68 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €17,06 | €34,12 | €0,79 | €-0,02 |
| Scanner Top5 Btc Guard V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,33 | €1.460,65 | €48,44 | €0,00 |
| Scanner Top5 Btc Guard V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €200,65 | €401,31 | €48,16 | €0,00 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00725 | 0,00860 | 0,00725 | 0,00366 | 0,00916 | €201,05 | €402,10 | €0,00 | €74,97 |
| Scanner Top5 Btc Guard V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1639,70939 | €861,11 | €1.722,22 | €0,00 | €81,98 |
| Scanner Top5 Btc Guard V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €53,55 | €107,11 | €2,48 | €-0,06 |
| Scanner Top5 Btc Btc Le3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €736,48 | €1.472,96 | €48,85 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.405,55 | €2.811,11 | €46,69 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €183,74 | €367,48 | €44,10 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00739 | 0,00860 | 0,00650 | 0,00373 | 0,00934 | €193,98 | €387,96 | €46,56 | €63,41 |
| Scanner Top5 Btc Btc Le3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1639,70939 | €17,96 | €35,91 | €0,00 | €1,71 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €17,39 | €34,78 | €0,80 | €-0,02 |
| Scanner Top5 Btc Guard Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €713,34 | €1.426,68 | €47,31 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €195,99 | €391,97 | €47,04 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00725 | 0,00860 | 0,00725 | 0,00366 | 0,00916 | €196,38 | €392,75 | €0,00 | €73,23 |
| Scanner Top5 Btc Guard Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1639,70939 | €841,08 | €1.682,17 | €0,00 | €80,07 |
| Scanner Top5 Btc Guard Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €52,31 | €104,62 | €2,42 | €-0,06 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €739,30 | €1.478,60 | €49,04 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €203,12 | €406,24 | €48,75 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00725 | 0,00860 | 0,00725 | 0,00366 | 0,00916 | €203,52 | €407,04 | €0,00 | €75,90 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1639,70939 | €871,69 | €1.743,38 | €0,00 | €82,98 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €54,21 | €108,42 | €2,51 | €-0,07 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €726,61 | €1.453,23 | €48,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €199,63 | €399,27 | €47,91 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00725 | 0,00860 | 0,00725 | 0,00366 | 0,00916 | €200,03 | €400,06 | €0,00 | €74,59 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1639,70939 | €856,73 | €1.713,46 | €0,00 | €81,56 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1242,51540 | €53,28 | €106,56 | €2,46 | €-0,06 |
| Scanner Top5 Btc Runner25 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,55 | €1.483,11 | €49,19 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.415,24 | €2.830,48 | €47,01 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,67036 | €185,01 | €370,01 | €44,40 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00739 | 0,00860 | 0,00650 | 0,00373 | 0,01005 | €195,32 | €390,64 | €46,88 | €63,84 |
| Scanner Top5 Btc Runner25 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1674,36149 | €18,08 | €36,16 | €0,00 | €1,72 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1264,37591 | €17,51 | €35,02 | €0,81 | €-0,02 |
| Scanner Top5 Btc Tp3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €741,99 | €1.483,98 | €49,22 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.416,07 | €2.832,14 | €47,04 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | APR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,67036 | €185,11 | €370,23 | €44,43 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00739 | 0,00860 | 0,00650 | 0,00373 | 0,01005 | €195,43 | €390,86 | €46,90 | €63,88 |
| Scanner Top5 Btc Tp3 V1 | SNDK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1544,41609 | 1617,93000 | 1582,63683 | 779,93013 | 1674,36149 | €18,09 | €36,18 | €0,00 | €1,72 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1264,37591 | €17,52 | €35,04 | €0,81 | €-0,02 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07014 | 0,06956 | 0,07126 | 0,10485 | 0,06733 | €1.512,09 | €3.024,18 | €48,39 | €24,84 |
| Combo Trend | SPCX | LONG | Combo Trend | 60m | 2,0x | 136,85206 | 136,85206 | 131,80916 | 69,11029 | 147,94644 | €646,55 | €1.293,10 | €47,65 | €0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €56,81 | €113,62 | €1,82 | €-0,00 |
| Combo Trend | BTC | SHORT | Combo Trend | 60m | 2,0x | 63807,23600 | 62813,56000 | 64828,15178 | 95391,81782 | 61561,22129 | €1.485,14 | €2.970,29 | €47,52 | €46,26 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,95007 | 0,95007 | 1,06408 | 1,42035 | 0,69925 | €179,75 | €359,50 | €43,14 | €-0,00 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €58,08 | €116,15 | €2,28 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07014 | 0,06956 | 0,07126 | 0,10485 | 0,06767 | €29,09 | €58,19 | €0,93 | €0,48 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00955 | €185,96 | €371,91 | €44,63 | €51,23 |
| Combo Trend | SKHYNIX | LONG | Combo Trend | 60m | 2,0x | 1175,20470 | 1181,69000 | 1144,24012 | 593,47837 | 1243,32677 | €13,54 | €27,08 | €0,71 | €0,15 |
| Combo Trend | SNDK | LONG | Combo Trend | 60m | 2,0x | 1618,90076 | 1617,93000 | 1567,33019 | 817,54488 | 1732,35601 | €12,85 | €25,70 | €0,82 | €-0,02 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 62826,12271 | 62813,56000 | 62072,20924 | 31727,19197 | 64032,38427 | €1.946,42 | €3.892,84 | €46,71 | €-0,78 |
| Combo Scanner | SPCX | LONG | Combo Scanner | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 146,83700 | €730,65 | €1.461,31 | €48,46 | €0,00 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06991 | 0,06956 | 0,07091 | 0,10451 | 0,06769 | €1.619,52 | €3.239,04 | €46,64 | €16,03 |
| Combo Scanner | APR | LONG | Combo Scanner | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,62304 | €186,01 | €372,01 | €44,64 | €0,00 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00756 | 0,00860 | 0,00665 | 0,00382 | 0,00955 | €186,31 | €372,62 | €44,71 | €51,33 |
| Combo Scanner | SNDK | LONG | Combo Scanner | 60m | 2,0x | 1618,90076 | 1617,93000 | 1572,48725 | 817,54488 | 1721,01048 | €20,29 | €40,58 | €1,16 | €-0,02 |
| Combo Adaptive | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €762,24 | €1.524,48 | €50,56 | €0,00 |
| Combo Adaptive | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €13,06 | €26,13 | €0,38 | €-0,00 |
| Combo Adaptive | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 62813,56000 | 63085,89799 | 95391,81782 | 61969,58760 | €1.768,38 | €3.536,76 | €0,00 | €55,08 |
| Combo Adaptive | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.152,18 | €2.304,35 | €46,56 | €-0,00 |
| Combo Adaptive | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06956 | 0,07115 | 0,10485 | 0,06812 | €31,23 | €62,47 | €0,90 | €0,51 |
| Combo Adaptive | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00665 | 0,00860 | 0,00745 | 0,00336 | 0,00825 | €195,39 | €390,77 | €0,00 | €114,02 |
| Combo Adaptive | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1544,41609 | 1617,93000 | 1585,15777 | 779,93013 | 1631,04636 | €36,25 | €72,50 | €0,00 | €3,45 |
| Combo Adaptive | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1181,69000 | 1139,94995 | 589,74924 | 1223,56093 | €15,02 | €30,04 | €0,72 | €0,36 |
| Combo Adaptive Mfe Trail | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €703,43 | €1.406,85 | €46,66 | €0,00 |
| Combo Adaptive Mfe Trail | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 62813,56000 | 63085,89799 | 95391,81782 | 61969,58760 | €1.608,91 | €3.217,82 | €0,00 | €50,11 |
| Combo Adaptive Mfe Trail | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.061,15 | €2.122,31 | €42,88 | €-0,00 |
| Combo Adaptive Mfe Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07030 | 0,06956 | 0,07021 | 0,10509 | 0,06827 | €23,31 | €46,62 | €0,00 | €0,49 |
| Combo Adaptive Mfe Trail | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00803 | 0,00860 | 0,00706 | 0,00405 | 0,00995 | €172,57 | €345,13 | €41,42 | €24,45 |
| Combo Adaptive Mfe Trail | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1618,90076 | 1617,93000 | 1572,48725 | 817,54488 | 1711,72778 | €17,51 | €35,02 | €1,00 | €-0,02 |
| Combo Adaptive Quality7 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00665 | 0,00860 | 0,00745 | 0,00336 | 0,00825 | €206,24 | €412,47 | €0,00 | €120,35 |
| Combo Adaptive Quality7 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1175,20470 | 1181,69000 | 1147,33658 | 593,47837 | 1230,94093 | €1.024,56 | €2.049,12 | €48,59 | €11,31 |
| Combo Adaptive Regime V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 57,00918 | 56,62100 | 56,18825 | 28,78964 | 58,65105 | €1.719,32 | €3.438,64 | €49,52 | €-23,41 |
| Combo Adaptive Regime V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 0,96465 | 0,96465 | 1,08040 | 1,44215 | 0,73313 | €206,23 | €412,46 | €49,50 | €-0,00 |
| Combo Adaptive Regime V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.345,66 | €2.691,31 | €49,49 | €-0,00 |
| Combo Adaptive Regime V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.488,00 | €2.976,01 | €49,43 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00665 | 0,00860 | 0,00745 | 0,00336 | 0,00825 | €204,08 | €408,16 | €0,00 | €119,09 |
| Combo Adaptive Long Only V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €748,66 | €1.497,32 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.463,27 | €2.926,54 | €48,61 | €0,00 |
| Combo Adaptive Long Only V1 | APR | LONG | Combo Adaptive | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €199,74 | €399,48 | €47,94 | €0,00 |
| Combo Adaptive Long Only V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00739 | 0,00860 | 0,00650 | 0,00373 | 0,00916 | €198,58 | €397,17 | €47,66 | €64,91 |
| Combo Adaptive Long Only V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1544,41609 | 1617,93000 | 1585,15777 | 779,93013 | 1631,04636 | €18,74 | €37,47 | €0,00 | €1,78 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1237,05028 | €17,37 | €34,75 | €0,80 | €-0,02 |
| Combo Adaptive Partial 1R V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 145,92928 | €731,94 | €1.463,87 | €48,55 | €0,00 |
| Combo Adaptive Partial 1R V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €12,54 | €25,09 | €0,36 | €-0,00 |
| Combo Adaptive Partial 1R V1 | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 62813,56000 | 63085,89799 | 95391,81782 | 61969,58760 | €1.698,08 | €3.396,15 | €0,00 | €52,89 |
| Combo Adaptive Partial 1R V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.106,37 | €2.212,75 | €44,71 | €-0,00 |
| Combo Adaptive Partial 1R V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06956 | 0,07115 | 0,10485 | 0,06812 | €29,99 | €59,98 | €0,86 | €0,49 |
| Combo Adaptive Partial 1R V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00665 | 0,00860 | 0,00745 | 0,00336 | 0,00825 | €187,62 | €375,24 | €0,00 | €109,49 |
| Combo Adaptive Partial 1R V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1544,41609 | 1617,93000 | 1585,15777 | 779,93013 | 1631,04636 | €34,81 | €69,62 | €0,00 | €3,31 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1181,69000 | 1139,94995 | 589,74924 | 1223,56093 | €14,43 | €28,85 | €0,69 | €0,34 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00665 | 0,00860 | 0,00745 | 0,00336 | 0,00825 | €206,68 | €413,36 | €0,00 | €120,61 |
| Combo Adaptive Runner25 V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €759,21 | €1.518,41 | €50,36 | €0,00 |
| Combo Adaptive Runner25 V1 | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 62813,56000 | 63085,89799 | 95391,81782 | 61050,76340 | €1.736,70 | €3.473,39 | €0,00 | €54,09 |
| Combo Adaptive Runner25 V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €39,17 | €78,35 | €1,21 | €-0,00 |
| Combo Adaptive Runner25 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.096,14 | €2.192,28 | €44,29 | €-0,00 |
| Combo Adaptive Runner25 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06956 | 0,07115 | 0,10485 | 0,06711 | €30,90 | €61,81 | €0,89 | €0,51 |
| Combo Adaptive Runner25 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00665 | 0,00860 | 0,00745 | 0,00336 | 0,00905 | €192,08 | €384,15 | €0,00 | €112,09 |
| Combo Adaptive Runner25 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1544,41609 | 1617,93000 | 1585,15777 | 779,93013 | 1674,36149 | €35,39 | €70,77 | €0,00 | €3,37 |
| Combo Adaptive Runner25 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1181,69000 | 1139,94995 | 589,74924 | 1251,43125 | €14,76 | €29,52 | €0,70 | €0,35 |
| Combo Adaptive Tp3 V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 136,85206 | 132,31345 | 69,11029 | 150,46789 | €745,02 | €1.490,04 | €49,42 | €0,00 |
| Combo Adaptive Tp3 V1 | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 62813,56000 | 63085,89799 | 95391,81782 | 61050,76340 | €1.704,25 | €3.408,50 | €0,00 | €53,08 |
| Combo Adaptive Tp3 V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,18488 | 0,18488 | 0,18774 | 0,27639 | 0,17631 | €38,44 | €76,88 | €1,19 | €-0,00 |
| Combo Adaptive Tp3 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.075,66 | €2.151,32 | €43,47 | €-0,00 |
| Combo Adaptive Tp3 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06956 | 0,07115 | 0,10485 | 0,06711 | €30,33 | €60,65 | €0,87 | €0,50 |
| Combo Adaptive Tp3 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00665 | 0,00860 | 0,00745 | 0,00336 | 0,00905 | €188,49 | €376,98 | €0,00 | €110,00 |
| Combo Adaptive Tp3 V1 | SNDK | LONG | Combo Adaptive | 60m | 2,0x | 1544,41609 | 1617,93000 | 1585,15777 | 779,93013 | 1674,36149 | €34,73 | €69,45 | €0,00 | €3,31 |
| Combo Adaptive Tp3 V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1167,82027 | 1181,69000 | 1139,94995 | 589,74924 | 1251,43125 | €14,48 | €28,97 | €0,69 | €0,34 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64070,44335 | 62813,56000 | 63108,68675 | 85106,90558 | 62225,21458 | €1.141,05 | €3.423,15 | €0,00 | €67,15 |
| Btc Ema 4H | BTC | SHORT | Trend following EMA | 240m | 2,0x | 63679,75150 | 62813,56000 | 64800,51513 | 95201,22850 | 60877,84244 | €1.413,45 | €2.826,90 | €49,75 | €38,45 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62173,77076 | €1.301,67 | €3.905,01 | €0,00 | €60,81 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63544,23861 | 62813,56000 | 64662,61721 | 94998,63672 | 60412,77853 | €1.406,00 | €2.812,00 | €49,49 | €32,33 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 61969,58760 | €1.152,72 | €3.458,17 | €0,00 | €53,85 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07014 | 0,06956 | 0,07115 | 0,09316 | 0,06812 | €1.155,63 | €3.466,88 | €49,92 | €28,47 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,06952 | 0,06956 | 0,07041 | 0,09234 | 0,06774 | €1.295,48 | €3.886,44 | €49,75 | €-2,33 |
| Master Adaptive V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €951,69 | €1.903,38 | €48,77 | €0,00 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1890,77808 | 1875,27000 | 1863,55088 | 954,84293 | 1945,23249 | €1.570,92 | €3.141,85 | €45,24 | €-25,77 |
| Master Adaptive V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.280,33 | €2.560,66 | €46,22 | €0,00 |
| Master Adaptive V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €198,13 | €396,27 | €47,55 | €0,00 |
| Master Adaptive V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1544,41609 | 1617,93000 | 1501,10095 | 779,93013 | 1631,04636 | €42,93 | €85,86 | €2,41 | €4,09 |
| Master Adaptive No Alt V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €952,08 | €1.904,17 | €48,79 | €0,00 |
| Master Adaptive No Alt V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,27 | €2.526,54 | €45,60 | €0,00 |
| Master Adaptive No Alt V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €199,48 | €398,96 | €47,88 | €0,00 |
| Master Adaptive No Alt V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1544,41609 | 1617,93000 | 1501,10095 | 779,93013 | 1631,04636 | €24,83 | €49,66 | €1,39 | €2,36 |
| Master Adaptive No Alt V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00782 | 0,00860 | 0,00688 | 0,00395 | 0,00970 | €195,44 | €390,89 | €46,91 | €38,77 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1182,39901 | 1181,69000 | 1155,07338 | 597,11150 | 1237,05026 | €20,03 | €40,05 | €0,93 | €-0,02 |
| Master Adaptive Strict3 V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,49291 | 0,49291 | 0,43376 | 0,24892 | 0,61121 | €190,97 | €381,94 | €45,83 | €0,00 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00665 | 0,00860 | 0,00586 | 0,00336 | 0,00825 | €193,63 | €387,26 | €46,47 | €113,00 |
| Master Adaptive Strict3 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1544,41609 | 1617,93000 | 1501,10095 | 779,93013 | 1631,04636 | €823,31 | €1.646,62 | €46,18 | €78,38 |
| Master Adaptive Strict3 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1167,82027 | 1181,69000 | 1139,94995 | 589,74924 | 1223,56091 | €957,07 | €1.914,14 | €45,68 | €22,73 |
| Master Adaptive Expanded V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,00 | €1.912,01 | €48,99 | €0,00 |
| Master Adaptive Expanded V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,64799 | 1,64799 | 1,61151 | 0,83223 | 1,72094 | €1.046,99 | €2.093,97 | €46,35 | €0,00 |
| Master Adaptive Expanded V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,97593 | 159,97593 | 156,99846 | 80,78784 | 165,93086 | €27,82 | €55,63 | €1,04 | €0,00 |
| Master Adaptive Expanded V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €202,38 | €404,77 | €48,57 | €0,00 |
| Master Adaptive Expanded V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00782 | 0,00860 | 0,00688 | 0,00395 | 0,00970 | €200,40 | €400,79 | €48,09 | €39,75 |
| Master Adaptive Expanded V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1618,90076 | 1617,93000 | 1572,48725 | 817,54488 | 1711,72778 | €15,69 | €31,37 | €0,90 | €-0,02 |
| Master Adaptive Gb20 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €939,05 | €1.878,09 | €48,12 | €0,00 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1890,77808 | 1875,27000 | 1863,55088 | 954,84293 | 1945,23249 | €1.550,05 | €3.100,10 | €44,64 | €-25,43 |
| Master Adaptive Gb20 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,32 | €2.526,64 | €45,61 | €0,00 |
| Master Adaptive Gb20 V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €195,50 | €391,00 | €46,92 | €0,00 |
| Master Adaptive Gb20 V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1544,41609 | 1617,93000 | 1501,10095 | 779,93013 | 1631,04636 | €42,36 | €84,71 | €2,38 | €4,03 |
| Master Adaptive Runner25 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 147,27511 | €953,33 | €1.906,66 | €48,86 | €0,00 |
| Master Adaptive Runner25 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,31376 | 1,31376 | 1,15611 | 0,66345 | 1,78672 | €188,92 | €377,85 | €45,34 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,85717 | 56,62100 | 55,05283 | 28,20787 | 58,27020 | €24,55 | €49,10 | €0,71 | €0,67 |
| Master Adaptive Runner25 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1890,77808 | 1875,27000 | 1863,55088 | 954,84293 | 1972,45969 | €1.573,63 | €3.147,26 | €45,32 | €-25,81 |
| Master Adaptive Runner25 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 168,61749 | €28,89 | €57,79 | €1,04 | €0,00 |
| Master Adaptive Runner25 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00685 | 0,00860 | 0,00603 | 0,00346 | 0,00931 | €192,44 | €384,89 | €46,19 | €98,28 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1165,32878 | 1181,69000 | 1135,36783 | 588,49103 | 1255,21164 | €20,98 | €41,97 | €1,08 | €0,59 |
| Combo Adaptive Side Regime Guard V1 | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63807,23600 | 62813,56000 | 63085,89799 | 95391,81782 | 61969,58760 | €1.842,32 | €3.684,64 | €0,00 | €57,38 |
| Combo Adaptive Side Regime Guard V1 | VELVET | LONG | Combo Adaptive | 60m | 2,0x | 0,60167 | 0,60167 | 0,52947 | 0,30384 | 0,74607 | €217,28 | €434,56 | €52,15 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06991 | 0,06956 | 0,07091 | 0,10451 | 0,06789 | €1.659,52 | €3.319,05 | €47,79 | €16,43 |
| Combo Adaptive Side Regime Guard V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,00430 | 1,00378 | 1,01876 | 1,50143 | 0,97538 | €1.713,05 | €3.426,11 | €49,34 | €1,77 |
| Master Adaptive Gb20 Be V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €956,40 | €1.912,81 | €49,01 | €0,00 |
| Master Adaptive Gb20 Be V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1890,77808 | 1875,27000 | 1863,55088 | 954,84293 | 1945,23249 | €1.578,70 | €3.157,40 | €45,47 | €-25,90 |
| Master Adaptive Gb20 Be V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.286,67 | €2.573,34 | €46,45 | €0,00 |
| Master Adaptive Gb20 Be V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €199,12 | €398,23 | €47,79 | €0,00 |
| Master Adaptive Gb20 Be V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1544,41609 | 1617,93000 | 1501,10095 | 779,93013 | 1631,04636 | €43,14 | €86,28 | €2,42 | €4,11 |
| Master Adaptive Gb20 Partial V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 136,76201 | 133,25764 | 69,06481 | 143,77074 | €955,39 | €1.910,77 | €48,96 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1890,77808 | 1875,27000 | 1863,55088 | 954,84293 | 1945,23249 | €1.577,02 | €3.154,05 | €45,42 | €-25,87 |
| Master Adaptive Gb20 Partial V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.285,30 | €2.570,60 | €46,40 | €0,00 |
| Master Adaptive Gb20 Partial V1 | APR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,47765 | 0,47765 | 0,42033 | 0,24121 | 0,59228 | €198,90 | €397,81 | €47,74 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SNDK | LONG | Master Adaptive Consensus | 60m | 2,0x | 1544,41609 | 1617,93000 | 1501,10095 | 779,93013 | 1631,04636 | €43,09 | €86,19 | €2,42 | €4,10 |
| Master Adaptive Gb20 Loss Cap V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,46019 | 1,46019 | 1,28497 | 0,73740 | 1,92745 | €192,15 | €384,31 | €46,12 | €0,00 |
| 1H Fast V3 Nohigh Range Only V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.566,03 | €4.698,09 | €0,00 | €73,16 |
| 1H Fast V3 Nohigh Range Only V1 | VELVET | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,60867 | 0,60867 | 0,53563 | 0,40882 | 0,71823 | €143,18 | €429,53 | €51,54 | €0,00 |
| 1H Fast V3 Nohigh Range Only V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,48830 | 1,48830 | 1,48830 | 0,99964 | 1,75619 | €141,11 | €423,32 | €0,00 | €0,00 |
| 1H Fast V3 Nohigh Range Only V1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,00538 | 1,00378 | 1,01664 | 1,33548 | 0,98849 | €1.549,60 | €4.648,80 | €52,07 | €7,39 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.581,87 | €4.745,62 | €0,00 | €73,90 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,60867 | 0,60867 | 0,53563 | 0,40882 | 0,71823 | €144,63 | €433,88 | €52,07 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,54541 | 1,54541 | 1,35996 | 1,03800 | 1,82358 | €144,27 | €432,81 | €51,94 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,93367 | 0,93367 | 1,04571 | 1,24023 | 0,76561 | €135,90 | €407,70 | €48,92 | €-0,00 |
| Main Side Regime Guard V1 | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,00378 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €14,83 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | BTC | SHORT | Confluenza trend | 240m | 3,0x | 63404,51656 | 62813,56000 | 64418,98882 | 84222,33283 | 61375,57203 | €1.068,86 | €3.206,59 | €51,31 | €29,89 |
| Main Side Regime Guard V1 | BEAT | SHORT | Confluenza trend | 240m | 3,0x | 1,03900 | 1,03900 | 1,03900 | 1,38014 | 0,78964 | €144,10 | €432,31 | €0,00 | €-0,00 |
| Main Side Regime Guard V1 | PEPE | SHORT | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,24 | €48,72 | €1,84 | €-0,00 |
| Combo Trend Side Regime Guard V1 | VELVET | LONG | Combo Trend | 60m | 2,0x | 0,60867 | 0,60867 | 0,53563 | 0,30738 | 0,76936 | €210,36 | €420,71 | €50,49 | €0,00 |
| Combo Trend Side Regime Guard V1 | BEAT | SHORT | Combo Trend | 60m | 2,0x | 1,03900 | 1,03900 | 1,03900 | 1,55331 | 0,76471 | €209,53 | €419,07 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06967 | 0,06956 | 0,07078 | 0,10415 | 0,06721 | €1.571,45 | €3.142,90 | €50,29 | €4,78 |
| Combo Trend Side Regime Guard V1 | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,00446 | 1,00378 | 1,02053 | 1,50167 | 0,96910 | €1.563,61 | €3.127,21 | €50,04 | €2,11 |
| Combo Trend Side Regime Guard V1 | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,49 | €38,98 | €0,69 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63807,23600 | 62813,56000 | 63064,94891 | 84757,27849 | 62735,27444 | €1.546,22 | €4.638,65 | €0,00 | €72,24 |
| 1H Fast Nohigh Cap75 Short Only V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,64799 | 1,64799 | 1,50669 | 1,10690 | 1,85993 | €195,91 | €587,73 | €50,39 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06991 | 0,06956 | 0,07069 | 0,09286 | 0,06873 | €1.499,62 | €4.498,86 | €50,39 | €22,27 |
| 1H Fast Nohigh Cap75 Short Only V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 0,88551 | 0,88551 | 0,98383 | 1,17625 | 0,73802 | €140,23 | €420,70 | €46,71 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1161,28635 | 1181,69000 | 1161,28781 | 779,99733 | 1196,37370 | €15,08 | €45,24 | €0,00 | €0,79 |
| 1H Fast Nohigh Cap75 Short Only V1 | SNDK | LONG | Momentum / breakout | 60m | 3,0x | 1618,90076 | 1617,93000 | 1582,80136 | 1087,36168 | 1673,04985 | €19,67 | €59,00 | €1,32 | €-0,04 |
| 1H Balanced V3 Long Only V1 | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 136,85206 | 132,31345 | 91,91897 | 145,92928 | €496,25 | €1.488,74 | €49,37 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,18533 | 0,18533 | 0,18800 | 0,24618 | 0,17999 | €1.142,52 | €3.427,55 | €49,36 | €-0,00 |
| 1H Balanced V3 Long Only V1 | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63807,23600 | 62813,56000 | 63106,84706 | 84757,27849 | 61969,58760 | €1.068,36 | €3.205,08 | €0,00 | €49,91 |
| 1H Balanced V3 Long Only V1 | CYS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,54741 | 1,54741 | 1,36172 | 1,03934 | 1,91879 | €133,24 | €399,72 | €47,97 | €0,00 |
| 1H Balanced V3 Long Only V1 | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €25,13 | €75,39 | €1,46 | €-0,00 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,06956 | 0,07064 | 0,09250 | 0,06763 | €13,83 | €41,49 | €0,60 | €0,05 |
| Scanner Bottom5 Short Profit Lock V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 62813,56000 | 63157,87454 | 95785,31281 | 62225,21458 | €1.730,40 | €3.460,80 | €0,00 | €67,89 |
| Scanner Bottom5 Short Profit Lock V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.748,97 | €3.497,95 | €50,37 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €201,04 | €402,07 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.102,06 | €2.204,11 | €44,53 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00378 | 1,01876 | 1,50143 | 0,97538 | €37,26 | €74,52 | €1,07 | €0,04 |
| Scanner Bottom5 Short Profit Lock V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 485,06297 | 489,56000 | 493,83011 | 725,16914 | 467,52868 | €12,86 | €25,72 | €0,46 | €-0,24 |
| Scanner Bottom5 Short Mfe Trail V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 62813,56000 | 63157,87454 | 95785,31281 | 62225,21458 | €1.733,03 | €3.466,07 | €0,00 | €67,99 |
| Scanner Bottom5 Short Mfe Trail V1 | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17999 | €1.751,64 | €3.503,27 | €50,45 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,04289 | 1,04289 | 1,03001 | 1,55912 | 0,79260 | €201,34 | €402,69 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.103,74 | €2.207,47 | €44,60 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,00430 | 1,00378 | 1,01876 | 1,50143 | 0,97538 | €37,32 | €74,63 | €1,07 | €0,04 |
| Scanner Bottom5 Short Mfe Trail V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 485,06297 | 489,56000 | 493,83011 | 725,16914 | 467,52868 | €12,88 | €25,76 | €0,47 | €-0,24 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive Strict3 V1 | HYPE | LONG | 2026-08-14T07:06:45+00:00 | 56,48760 | €-50,61 | -1,10 | STOP |
| Master Adaptive No Alt V1 | HYPE | LONG | 2026-08-14T07:06:45+00:00 | 56,48760 | €-52,93 | -1,10 | STOP |
| Master Adaptive Expanded V1 | HYPE | LONG | 2026-08-14T07:06:45+00:00 | 56,48760 | €-53,61 | -1,10 | STOP |
| Donchian 1H Gb20 120R V1 | TUT | SHORT | 2026-08-14T07:06:45+00:00 | 0,03995 | €-33,86 | -0,65 | STOP_GAP_STRESS |
| Benchmark Donchian breakout 1H | TUT | SHORT | 2026-08-14T07:06:45+00:00 | 0,03995 | €-34,68 | -0,65 | STOP_GAP_STRESS |
| Combo Adaptive Quality7 V1 | HYPE | LONG | 2026-08-14T07:06:45+00:00 | 56,48760 | €-54,67 | -1,10 | STOP |
| Combo Adaptive Quality7 V1 | TUT | SHORT | 2026-08-14T07:06:45+00:00 | 0,03995 | €-32,04 | -0,65 | STOP_GAP_STRESS |
| Combo Adaptive Quality7 Regime V1 | TUT | SHORT | 2026-08-14T07:06:45+00:00 | 0,03995 | €-62,42 | -1,29 | STOP_GAP_STRESS |
| Combo Adaptive Quality7 Regime V1 | HYPE | LONG | 2026-08-14T07:06:45+00:00 | 56,48760 | €-54,11 | -1,10 | STOP |
| Combo Adaptive Quality7 Regime Partial 1R V1 | HYPE | LONG | 2026-08-14T07:06:45+00:00 | 56,48760 | €-54,80 | -1,10 | STOP |
| Combo Adaptive Quality7 Regime Partial 1R V1 | TUT | SHORT | 2026-08-14T07:06:45+00:00 | 0,03995 | €-63,21 | -1,29 | STOP_GAP_STRESS |
| 1H Fast V3 No Esports V1 | TUT | SHORT | 2026-08-14T07:06:45+00:00 | 0,03995 | €-56,53 | -1,18 | STOP_GAP_STRESS |

## Regole invarianti

- Nessuna martingala e nessuna mediazione automatica in perdita.
- Il target mensile riduce il rischio quando viene avvicinato o raggiunto; non lo aumenta mai.
- Il portafoglio principale e le simulazioni di confronto hanno contabilità separata.
- Commissioni, slippage e funding sono inclusi nella simulazione secondo i parametri configurati.
- Quando stop e target risultano toccati nella stessa candela, prevale lo stop salvo modifica esplicita della configurazione.
<!-- PAPER_TRADING_END -->

</details>
<!-- COMPACT_SECTION_END:decision -->

<!-- COMPACT_SECTION_START:module_accuracy -->
<details>
<summary><strong>🧪 Accuratezza moduli e raccolta dati</strong></summary>

<!-- MODULE_ACCURACY_START -->
# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-14 10:53 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [module_accuracy_report.md](module_accuracy_report.md)

Questo report salva ogni giorno i segnali dei moduli e controlla ogni giorno quali orizzonti sono maturati.

La calibrazione ora controlla questi orizzonti:

- **1g / 2g / 3g** = feedback rapidissimo
- **5g / 7g / 10g** = feedback settimanale
- **14g / 21g** = feedback swing
- **30g / 45g / 60g** = feedback più serio

Moduli controllati:

- Global Confluence = benchmark dell'aggregato finale
- **Famiglia statistica Scanner + Market Regime = modulo calibrabile reale**
- Scanner grezzo = diagnostico, già incluso nella famiglia statistica
- Market Regime grezzo = diagnostico, già incluso nella famiglia statistica
- Struttura tecnica
- Classic technical confirmation
- Microstruttura exchange, OI/funding/taker flow/order book
- Frattale SOL/BTC, solo per SOL

Regola anti-doppio-conteggio: **Scanner e Market Regime continuano a essere misurati separatamente solo per diagnosi, ma non devono ricevere due modifiche di peso autonome**. La calibrazione dei pesi deve agire sulla Famiglia statistica.

Nota: i controlli vengono aggiornati **ogni giorno**, ma i pesi del Global non devono cambiare automaticamente sotto 30 controlli. Prima si osserva, poi si calibra.

Segnali totali salvati: **105**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-14 | BTC | 62.749,25 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-14 | DOGE | 0.06940 | +2 | +4 | +3 | +2 | 0 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-14 | SOL | 75,41 | +3 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-11 | BTC | 63.889,59 | +6 | +4 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-11 | DOGE | 0.06985 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-11 | SOL | 75,73 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-10 | BTC | 64.966,07 | +6 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-10 | DOGE | 0.06975 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-10 | SOL | 76,57 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-09 | BTC | 64.733,97 | +7 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-09 | DOGE | 0.06994 | +4 | +4 | +3 | +3 | 0 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-09 | SOL | 75,92 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 35 | 34 | 34 | 34 | 32 | 30 | 27 | 23 | 16 | 7 | 0 | 0 |
| SOL | 35 | 34 | 34 | 34 | 32 | 30 | 27 | 23 | 16 | 7 | 0 | 0 |
| DOGE | 35 | 34 | 34 | 34 | 32 | 30 | 27 | 23 | 16 | 7 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-16 | 30g | 2026-08-15 | domani |
| SOL | 2026-07-16 | 30g | 2026-08-15 | domani |
| DOGE | 2026-07-16 | 30g | 2026-08-15 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 32 | 46,88% | -0,01% | -0,05% | PRIMA CALIBRAZIONE |
| BTC | 2g | 32 | 43,75% | +0,02% | -0,12% | PRIMA CALIBRAZIONE |
| BTC | 3g | 32 | 37,50% | -0,14% | -0,36% | PRIMA CALIBRAZIONE |
| BTC | 5g | 30 | 30,00% | +0,05% | -0,38% | PRIMA CALIBRAZIONE |
| BTC | 7g | 28 | 42,86% | +0,25% | -0,13% | FEEDBACK RAPIDO |
| BTC | 10g | 25 | 48,00% | +0,53% | +0,17% | FEEDBACK RAPIDO |
| BTC | 14g | 21 | 42,86% | -0,03% | -0,19% | FEEDBACK RAPIDO |
| BTC | 21g | 14 | 28,57% | -0,38% | -0,68% | FEEDBACK RAPIDO |
| BTC | 30g | 7 | 85,71% | +0,76% | +0,76% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 27 | 51,85% | +0,01% | -0,22% | FEEDBACK RAPIDO |
| SOL | 2g | 27 | 44,44% | -0,01% | -0,27% | FEEDBACK RAPIDO |
| SOL | 3g | 27 | 44,44% | +0,09% | -0,24% | FEEDBACK RAPIDO |
| SOL | 5g | 25 | 52,00% | -0,02% | -0,24% | FEEDBACK RAPIDO |
| SOL | 7g | 23 | 60,87% | -0,00% | +0,23% | FEEDBACK RAPIDO |
| SOL | 10g | 20 | 45,00% | -0,52% | -0,14% | FEEDBACK RAPIDO |
| SOL | 14g | 17 | 52,94% | -2,09% | +0,05% | FEEDBACK RAPIDO |
| SOL | 21g | 14 | 57,14% | -2,85% | -0,16% | FEEDBACK RAPIDO |
| SOL | 30g | 6 | 33,33% | -1,55% | -1,41% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 32 | 40,62% | -0,05% | -0,07% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 32 | 43,75% | -0,14% | -0,15% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 32 | 40,62% | -0,35% | -0,00% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 30 | 50,00% | -0,64% | +0,19% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 28 | 60,71% | -0,96% | +0,62% | FEEDBACK RAPIDO |
| DOGE | 10g | 26 | 53,85% | -1,52% | +0,88% | FEEDBACK RAPIDO |
| DOGE | 14g | 22 | 68,18% | -2,39% | +1,87% | FEEDBACK RAPIDO |
| DOGE | 21g | 16 | 93,75% | -3,70% | +3,70% | FEEDBACK RAPIDO |
| DOGE | 30g | 7 | 100,00% | -4,49% | +4,49% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 32 | 46,88% | -0,01% | -0,05% | -0,32% | +0,55% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 34 | 50,00% | -0,02% | -0,02% | -0,33% | +0,51% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 34 | 50,00% | -0,02% | -0,02% | -0,33% | +0,51% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 30 | 50,00% | -0,06% | -0,06% | -0,38% | +0,43% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 29 | 34,48% | +0,14% | -0,40% | -0,19% | +0,67% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 4 | 0,00% | +0,76% | -0,76% | +0,03% | +1,12% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 32 | 43,75% | +0,02% | -0,12% | -0,46% | +0,74% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | -0,00% | -0,00% | -0,47% | +0,71% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,00% | -0,00% | -0,47% | +0,71% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 30 | 46,67% | -0,09% | -0,09% | -0,57% | +0,61% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 29 | 44,83% | +0,18% | -0,38% | -0,27% | +0,89% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 4 | 25,00% | +0,86% | -0,86% | +0,50% | +1,73% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 32 | 37,50% | -0,14% | -0,36% | -1,40% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 34 | 50,00% | -0,06% | -0,06% | -1,37% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 34 | 50,00% | -0,06% | -0,06% | -1,37% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 30 | 50,00% | -0,09% | -0,09% | -1,39% | +1,46% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 29 | 34,48% | +0,27% | -0,46% | -1,13% | +1,83% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,18% | -1,18% | -0,41% | +2,46% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 30 | 30,00% | +0,05% | -0,38% | -2,06% | +2,18% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 32 | 40,62% | +0,05% | +0,05% | -2,02% | +2,21% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 32 | 40,62% | +0,05% | +0,05% | -2,02% | +2,21% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 28 | 42,86% | +0,14% | +0,14% | -2,01% | +2,18% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 27 | 40,74% | +0,27% | -0,64% | -1,76% | +2,48% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,14% | -1,14% | -1,16% | +2,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 28 | 42,86% | +0,25% | -0,13% | -2,25% | +2,63% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 30 | 53,33% | +0,20% | +0,20% | -2,24% | +2,63% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 30 | 53,33% | +0,20% | +0,20% | -2,24% | +2,63% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 26 | 57,69% | +0,43% | +0,43% | -2,19% | +2,67% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 25 | 36,00% | +0,69% | -0,69% | -1,92% | +2,93% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,94% | -1,94% | -1,23% | +3,13% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 25 | 48,00% | +0,53% | +0,17% | -2,53% | +3,08% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 27 | 55,56% | +0,32% | +0,32% | -2,57% | +3,05% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 27 | 55,56% | +0,32% | +0,32% | -2,57% | +3,05% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 23 | 65,22% | +0,73% | +0,73% | -2,42% | +3,17% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 22 | 31,82% | +0,65% | -0,28% | -2,20% | +3,47% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,32% | -1,32% | -1,42% | +3,31% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 21 | 42,86% | -0,03% | -0,19% | -3,07% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 23 | 43,48% | -0,16% | -0,16% | -3,08% | +3,30% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 23 | 43,48% | -0,16% | -0,16% | -3,08% | +3,30% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 19 | 52,63% | +0,33% | +0,33% | -2,80% | +3,50% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 18 | 55,56% | +0,15% | +0,12% | -2,70% | +3,76% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 2 | 50,00% | +0,00% | -0,00% | -2,23% | +2,76% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 14 | 28,57% | -0,38% | -0,68% | -3,23% | +4,06% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 16 | 43,75% | -0,47% | -0,47% | -3,28% | +3,88% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 16 | 43,75% | -0,47% | -0,47% | -3,28% | +3,88% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 12 | 50,00% | -0,16% | -0,16% | -2,88% | +4,39% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 13 | 23,08% | -0,12% | -0,06% | -2,94% | +4,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 7 | 85,71% | +0,76% | +0,76% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 7 | 85,71% | +0,76% | +0,76% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 7 | 85,71% | +0,76% | +0,76% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 7 | 85,71% | +0,76% | +0,76% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 6 | 33,33% | +0,65% | -1,20% | -2,34% | +5,40% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 32 | 40,62% | -0,05% | -0,07% | -0,52% | +0,69% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 34 | 52,94% | -0,16% | +0,19% | -0,65% | +0,56% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 34 | 52,94% | -0,16% | +0,19% | -0,65% | +0,56% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 32 | 53,12% | -0,06% | +0,08% | -0,56% | +0,68% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,12% | +0,12% | -0,60% | +0,51% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 22 | 40,91% | +0,18% | -0,18% | -0,35% | +0,74% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,92% | +1,13% | +0,84% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 32 | 43,75% | -0,14% | -0,15% | -0,79% | +0,96% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | -0,26% | +0,01% | -0,91% | +0,80% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,26% | +0,01% | -0,91% | +0,80% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 32 | 46,88% | -0,36% | +0,09% | -0,96% | +0,77% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 30 | 60,00% | -0,30% | +0,30% | -0,91% | +0,61% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 22 | 50,00% | +0,17% | -0,17% | -0,49% | +1,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +3,12% | +2,46% | +2,21% | +3,52% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 32 | 40,62% | -0,35% | -0,00% | -1,84% | +2,02% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | -0,46% | -0,09% | -1,94% | +1,85% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,46% | -0,09% | -1,94% | +1,85% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 32 | 50,00% | -0,71% | +0,13% | -1,90% | +1,72% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,49% | +0,49% | -2,02% | +1,67% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 22 | 40,91% | -0,10% | +0,10% | -1,86% | +2,37% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,70% | +1,18% | -0,25% | +5,07% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 30 | 50,00% | -0,64% | +0,19% | -2,74% | +2,34% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 32 | 46,88% | -0,73% | +0,07% | -2,80% | +2,19% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 32 | 46,88% | -0,73% | +0,07% | -2,80% | +2,19% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 30 | 46,67% | -0,75% | +0,04% | -2,81% | +2,03% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 30 | 63,33% | -0,75% | +0,75% | -2,89% | +2,13% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 22 | 54,55% | -0,40% | +0,40% | -2,68% | +2,79% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 28 | 60,71% | -0,96% | +0,62% | -3,27% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 30 | 56,67% | -1,05% | +0,38% | -3,35% | +2,37% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 30 | 56,67% | -1,05% | +0,38% | -3,35% | +2,37% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 28 | 57,14% | -1,05% | +0,33% | -3,40% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 29 | 65,52% | -1,09% | +1,09% | -3,41% | +2,31% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,93% | +0,93% | -3,27% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,97% | +0,62% | -0,19% | +6,23% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 26 | 53,85% | -1,52% | +0,88% | -4,06% | +2,59% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 27 | 51,85% | -1,61% | +0,74% | -4,16% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 27 | 51,85% | -1,61% | +0,74% | -4,16% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 25 | 52,00% | -1,67% | +0,73% | -4,21% | +2,25% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 27 | 70,37% | -1,61% | +1,61% | -4,16% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 20 | 65,00% | -1,32% | +1,32% | -4,00% | +2,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 22 | 68,18% | -2,39% | +1,87% | -5,10% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 23 | 65,22% | -2,47% | +1,60% | -5,18% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 23 | 65,22% | -2,47% | +1,60% | -5,18% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 21 | 66,67% | -2,56% | +1,60% | -5,31% | +2,38% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 23 | 78,26% | -2,47% | +2,47% | -5,18% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 19 | 73,68% | -2,20% | +2,20% | -4,92% | +3,02% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 16 | 93,75% | -3,70% | +3,70% | -6,18% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 16 | 93,75% | -3,70% | +3,70% | -6,18% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 16 | 93,75% | -3,70% | +3,70% | -6,18% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 14 | 100,00% | -4,05% | +4,05% | -6,53% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 16 | 93,75% | -3,70% | +3,70% | -6,18% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 15 | 93,33% | -3,58% | +3,58% | -6,05% | +2,70% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,55% | +0,55% | -1,52% | +6,93% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 7 | 100,00% | -4,49% | +4,49% | -7,01% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 7 | 100,00% | -4,49% | +4,49% | -7,01% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 7 | 100,00% | -4,49% | +4,49% | -7,01% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 7 | 100,00% | -4,49% | +4,49% | -7,01% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 7 | 100,00% | -4,49% | +4,49% | -7,01% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 6 | 100,00% | -4,21% | +4,21% | -6,84% | +3,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 27 | 51,85% | +0,01% | -0,22% | -0,48% | +0,72% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 30 | 60,00% | -0,29% | -0,00% | -0,74% | +0,37% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 33 | 57,58% | -0,16% | -0,10% | -0,64% | +0,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 28 | 53,57% | -0,12% | +0,03% | -0,68% | +0,53% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 32 | 50,00% | -0,10% | -0,02% | -0,59% | +0,53% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,04% | -0,04% | -0,54% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 27 | 44,44% | -0,01% | -0,27% | -0,68% | +0,91% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 30 | 50,00% | -0,27% | -0,11% | -0,98% | +0,51% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 33 | 48,48% | -0,21% | -0,13% | -0,90% | +0,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 28 | 46,43% | -0,19% | -0,16% | -0,91% | +0,74% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 32 | 40,62% | -0,15% | -0,20% | -0,81% | +0,78% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,02% | -0,02% | -0,52% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 27 | 44,44% | +0,09% | -0,24% | -1,86% | +2,00% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 30 | 43,33% | -0,33% | -0,07% | -2,19% | +1,67% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 33 | 42,42% | -0,27% | -0,10% | -2,10% | +1,83% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 28 | 42,86% | -0,22% | -0,29% | -2,02% | +1,85% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 32 | 43,75% | -0,20% | -0,17% | -2,04% | +1,90% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 21 | 42,86% | +0,13% | -0,13% | -1,91% | +1,82% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 25 | 52,00% | -0,02% | -0,24% | -2,64% | +2,73% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 28 | 53,57% | -0,28% | -0,02% | -2,95% | +2,40% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 31 | 51,61% | -0,18% | -0,09% | -2,86% | +2,54% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 26 | 50,00% | -0,37% | -0,09% | -2,82% | +2,53% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 31 | 45,16% | -0,24% | -0,29% | -2,89% | +2,61% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 21 | 52,38% | +0,14% | -0,14% | -2,60% | +2,64% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 23 | 60,87% | -0,00% | +0,23% | -3,30% | +3,14% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 26 | 65,38% | -0,41% | +0,47% | -3,59% | +2,84% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 29 | 65,52% | -0,38% | +0,43% | -3,50% | +2,95% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 24 | 58,33% | -0,13% | -0,04% | -3,45% | +2,97% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 30 | 36,67% | -0,35% | -0,33% | -3,49% | +2,97% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 20 | 45,00% | -0,52% | -0,14% | -4,08% | +3,35% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 23 | 52,17% | -0,60% | +0,34% | -4,45% | +2,99% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 26 | 50,00% | -0,55% | +0,33% | -4,34% | +3,09% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 21 | 42,86% | -0,16% | -0,42% | -4,31% | +3,15% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 27 | 55,56% | -0,66% | +0,48% | -4,35% | +3,11% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 19 | 57,89% | -0,40% | +0,40% | -4,09% | +3,44% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 17 | 52,94% | -2,09% | +0,05% | -5,37% | +3,25% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 19 | 73,68% | -1,28% | +0,69% | -5,61% | +3,02% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 22 | 77,27% | -1,53% | +1,02% | -5,38% | +3,14% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 17 | 47,06% | -1,04% | -0,83% | -5,28% | +3,22% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 23 | 47,83% | -1,64% | +0,75% | -5,45% | +3,16% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 15 | 53,33% | -0,95% | +0,95% | -5,47% | +3,60% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 14 | 57,14% | -2,85% | -0,16% | -7,27% | +2,80% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 12 | 66,67% | -3,13% | +1,53% | -7,50% | +2,32% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 15 | 73,33% | -3,05% | +1,77% | -7,22% | +2,64% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 10 | 20,00% | -3,22% | -1,52% | -7,24% | +2,54% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 16 | 68,75% | -2,81% | +0,24% | -7,21% | +2,70% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 8 | 87,50% | -1,29% | +1,29% | -7,09% | +3,06% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 6 | 33,33% | -1,55% | -1,41% | -8,00% | +2,76% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 5 | 80,00% | -2,33% | +1,22% | -8,45% | +2,28% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 7 | 71,43% | -1,65% | +0,86% | -8,15% | +2,58% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | -1,55% | -0,85% | -8,00% | +2,76% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 7 | 28,57% | -1,65% | -1,02% | -8,15% | +2,58% | FEEDBACK RAPIDO |
| SOL | 30g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | FEEDBACK RAPIDO |

## Come leggerlo

- **CALIBRABILE** = modulo reale sul quale, con dati maturi, si può valutare una modifica di peso.
- **DIAGNOSTICO** = resta misurato, ma è già incluso in una famiglia e il suo peso separato deve restare 0.
- **BENCHMARK** = risultato complessivo del Global; serve per confrontare l'aggregato, non è un peso interno.
- **Controlli** = segnali non neutrali già verificati su quell'orizzonte.
- **Accuratezza direzione** = quante volte un segnale positivo ha avuto return positivo o un segnale negativo ha avuto return negativo.
- **Return medio** = rendimento reale medio dell'asset su quell'orizzonte.
- **Return corretto direzione** = return visto dal lato del modulo: se il modulo era ribassista, un calo conta positivo.
- **Drawdown medio** = peggior discesa media durante l'orizzonte.
- **Max gain medio** = massimo rialzo medio durante l'orizzonte.

Regole operative:

- Sotto **30 controlli**: solo osservazione, nessuna modifica ai pesi.
- Da **30 controlli**: possibile calibrazione leggera.
- Da **60 controlli**: lettura più utile.
- Da **100+ controlli**: possibile revisione più seria dei pesi.

Questo report non cambia ancora automaticamente i pesi del Global Confluence. Produce però i metadati `calibratable` e `calibration_role`, così il report di calibrazione può escludere Scanner e Market dalle proposte di peso separate.

Nota tecnica: le colonne data sono forzate come testo, quindi non deve più apparire l'errore `Invalid value 'YYYY-MM-DD' for dtype 'float64'`.
<!-- MODULE_ACCURACY_END -->

</details>
<!-- COMPACT_SECTION_END:module_accuracy -->

<!-- COMPACT_SECTION_START:global_weight_calibration -->
<details>
<summary><strong>⚖️ Calibrazione pesi Global Confluence</strong></summary>

<!-- GLOBAL_WEIGHT_CALIBRATION_START -->
# Calibrazione pesi Global Confluence

Generato: 2026-08-14 10:53 UTC

Report completo: [global_weight_calibration_report.md](global_weight_calibration_report.md)

Questo blocco controlla se, col tempo, i moduli reali del Global Confluence meritano più peso, meno peso o peso invariato.

Correzione anti-doppio-conteggio: **la Famiglia statistica Scanner + Market Regime è il modulo calibrabile**. Scanner grezzo e Market Regime grezzo restano visibili solo come diagnostica e non ricevono proposte di peso separate.

Regola principale:

- sotto **30 controlli**: osservazione, nessuna modifica pesi
- da **30 controlli**: prima calibrazione leggera
- da **60 controlli**: lettura utile
- da **100+ controlli**: possibile proposta prudente di modifica pesi

Il file continua a produrre solo raccomandazioni: **non modifica automaticamente** `global_confluence_report.py`.

## Sintesi per asset

| Asset | Segnali salvati | Stato | Controlli max | Righe 30+ | Righe 60+ | Righe 100+ | Miglior modulo calibrabile | Orizzonte | Accuratezza | Return corretto direzione | Lettura |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 35 | PRIMA CALIBRAZIONE | 34 | 5 | 0 | 0 | Famiglia statistica | 1g | 50,00% | -0,02% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 35 | PRIMA CALIBRAZIONE | 32 | 8 | 0 | 0 | Tecnico | 1g | 50,00% | -0,02% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 35 | PRIMA CALIBRAZIONE | 34 | 9 | 0 | 0 | Famiglia statistica | 1g | 52,94% | +0,19% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 4 | 0,00% | -0,76% | +0,76% | +0,03% | +1,12% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 34 | 50,00% | -0,02% | -0,02% | -0,33% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 29 | 34,48% | -0,40% | +0,14% | -0,19% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 4 | 25,00% | -0,86% | +0,86% | +0,50% | +1,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 34 | 47,06% | -0,00% | -0,00% | -0,47% | +0,71% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 29 | 44,83% | -0,38% | +0,18% | -0,27% | +0,89% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 4 | 25,00% | -1,18% | +1,18% | -0,41% | +2,46% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 34 | 50,00% | -0,06% | -0,06% | -1,37% | +1,56% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 29 | 34,48% | -0,46% | +0,27% | -1,13% | +1,83% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 4 | 25,00% | -1,14% | +1,14% | -1,16% | +2,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 32 | 40,62% | +0,05% | +0,05% | -2,02% | +2,21% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 27 | 40,74% | -0,64% | +0,27% | -1,76% | +2,48% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,94% | +1,94% | -1,23% | +3,13% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 30 | 53,33% | +0,20% | +0,20% | -2,24% | +2,63% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 25 | 36,00% | -0,69% | +0,69% | -1,92% | +2,93% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,32% | +1,32% | -1,42% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 27 | 55,56% | +0,32% | +0,32% | -2,57% | +3,05% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 22 | 31,82% | -0,28% | +0,65% | -2,20% | +3,47% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Classic technical | 2 | 50,00% | -0,00% | +0,00% | -2,23% | +2,76% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 23 | 43,48% | -0,16% | -0,16% | -3,08% | +3,30% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 18 | 55,56% | +0,12% | +0,15% | -2,70% | +3,76% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 16 | 43,75% | -0,47% | -0,47% | -3,28% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 13 | 23,08% | -0,06% | -0,12% | -2,94% | +4,27% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 7 | 85,71% | +0,76% | +0,76% | -2,47% | +5,31% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 6 | 33,33% | -1,20% | +0,65% | -2,34% | +5,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 22 | 40,91% | -0,18% | +0,18% | -0,35% | +0,74% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 34 | 52,94% | +0,19% | -0,16% | -0,65% | +0,56% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,13% | +1,92% | +0,84% | +2,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 30 | 50,00% | +0,12% | -0,12% | -0,60% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 22 | 50,00% | -0,17% | +0,17% | -0,49% | +1,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 34 | 47,06% | +0,01% | -0,26% | -0,91% | +0,80% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 4 | 50,00% | +2,46% | +3,12% | +2,21% | +3,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 30 | 60,00% | +0,30% | -0,30% | -0,91% | +0,61% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 22 | 40,91% | +0,10% | -0,10% | -1,86% | +2,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 34 | 47,06% | -0,09% | -0,46% | -1,94% | +1,85% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,18% | +1,70% | -0,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 30 | 50,00% | +0,49% | -0,49% | -2,02% | +1,67% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 22 | 54,55% | +0,40% | -0,40% | -2,68% | +2,79% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 32 | 46,88% | +0,07% | -0,73% | -2,80% | +2,19% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,23% | +0,64% | -0,37% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 30 | 63,33% | +0,75% | -0,75% | -2,89% | +2,13% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,93% | -0,93% | -3,27% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 30 | 56,67% | +0,38% | -1,05% | -3,35% | +2,37% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,62% | +0,97% | -0,19% | +6,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 29 | 65,52% | +1,09% | -1,09% | -3,41% | +2,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 20 | 65,00% | +1,32% | -1,32% | -4,00% | +2,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 27 | 51,85% | +0,74% | -1,61% | -4,16% | +2,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 27 | 70,37% | +1,61% | -1,61% | -4,16% | +2,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 19 | 73,68% | +2,20% | -2,20% | -4,92% | +3,02% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 23 | 65,22% | +1,60% | -2,47% | -5,18% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 23 | 78,26% | +2,47% | -2,47% | -5,18% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 15 | 93,33% | +3,58% | -3,58% | -6,05% | +2,70% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 16 | 93,75% | +3,70% | -3,70% | -6,18% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +0,55% | +0,55% | -1,52% | +6,93% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 16 | 93,75% | +3,70% | -3,70% | -6,18% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 6 | 100,00% | +4,21% | -4,21% | -6,84% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 7 | 100,00% | +4,49% | -4,49% | -7,01% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 7 | 100,00% | +4,49% | -4,49% | -7,01% | +2,82% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 21 | 47,62% | -0,04% | +0,04% | -0,54% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 30 | 60,00% | -0,00% | -0,29% | -0,74% | +0,37% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 32 | 50,00% | -0,02% | -0,10% | -0,59% | +0,53% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 21 | 47,62% | -0,02% | +0,02% | -0,52% | +0,51% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 30 | 50,00% | -0,11% | -0,27% | -0,98% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 32 | 40,62% | -0,20% | -0,15% | -0,81% | +0,78% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 21 | 42,86% | -0,13% | +0,13% | -1,91% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 30 | 43,33% | -0,07% | -0,33% | -2,19% | +1,67% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 32 | 43,75% | -0,17% | -0,20% | -2,04% | +1,90% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 21 | 52,38% | -0,14% | +0,14% | -2,60% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 28 | 53,57% | -0,02% | -0,28% | -2,95% | +2,40% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 31 | 45,16% | -0,29% | -0,24% | -2,89% | +2,61% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 26 | 65,38% | +0,47% | -0,41% | -3,59% | +2,84% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 30 | 36,67% | -0,33% | -0,35% | -3,49% | +2,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 19 | 57,89% | +0,40% | -0,40% | -4,09% | +3,44% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 23 | 52,17% | +0,34% | -0,60% | -4,45% | +2,99% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 27 | 55,56% | +0,48% | -0,66% | -4,35% | +3,11% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 15 | 53,33% | +0,95% | -0,95% | -5,47% | +3,60% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 19 | 73,68% | +0,69% | -1,28% | -5,61% | +3,02% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 23 | 47,83% | +0,75% | -1,64% | -5,45% | +3,16% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Classic technical | 8 | 87,50% | +1,29% | -1,29% | -7,09% | +3,06% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 12 | 66,67% | +1,53% | -3,13% | -7,50% | +2,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 16 | 68,75% | +0,24% | -2,81% | -7,21% | +2,70% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 5 | 80,00% | +1,22% | -2,33% | -8,45% | +2,28% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 7 | 28,57% | -1,02% | -1,65% | -8,15% | +2,58% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 32 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 32 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 34 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 12 | 16,67% | -0,93% |
| BTC | BREVE | Famiglia statistica | 102 | 49,02% | -0,03% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 87 | 37,93% | -0,41% |
| BTC | SETTIMANALE | Classic technical | 12 | 8,33% | -1,47% |
| BTC | SETTIMANALE | Famiglia statistica | 89 | 49,44% | +0,18% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 74 | 36,49% | -0,55% |
| BTC | SWING | Classic technical | 2 | 50,00% | -0,00% |
| BTC | SWING | Famiglia statistica | 39 | 43,59% | -0,28% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 31 | 41,94% | +0,05% |
| BTC | MEDIO | Famiglia statistica | 7 | 85,71% | +0,76% |
| BTC | MEDIO | Tecnico | 6 | 33,33% | -1,20% |
| DOGE | BREVE | Classic technical | 66 | 43,94% | -0,08% |
| DOGE | BREVE | Famiglia statistica | 102 | 49,02% | +0,04% |
| DOGE | BREVE | Microstruttura exchange | 12 | 50,00% | +1,59% |
| DOGE | BREVE | Tecnico | 90 | 53,33% | +0,31% |
| DOGE | SETTIMANALE | Classic technical | 63 | 57,14% | +0,87% |
| DOGE | SETTIMANALE | Famiglia statistica | 89 | 51,69% | +0,38% |
| DOGE | SETTIMANALE | Microstruttura exchange | 9 | 66,67% | +0,55% |
| DOGE | SETTIMANALE | Tecnico | 86 | 66,28% | +1,13% |
| DOGE | SWING | Classic technical | 34 | 82,35% | +2,81% |
| DOGE | SWING | Famiglia statistica | 39 | 76,92% | +2,46% |
| DOGE | SWING | Microstruttura exchange | 3 | 100,00% | +0,49% |
| DOGE | SWING | Tecnico | 39 | 84,62% | +2,98% |
| DOGE | MEDIO | Classic technical | 6 | 100,00% | +4,21% |
| DOGE | MEDIO | Famiglia statistica | 7 | 100,00% | +4,49% |
| DOGE | MEDIO | Tecnico | 7 | 100,00% | +4,49% |
| SOL | BREVE | Classic technical | 63 | 46,03% | -0,06% |
| SOL | BREVE | Famiglia statistica | 90 | 51,11% | -0,06% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 6 | 16,67% | -0,83% |
| SOL | BREVE | Tecnico | 96 | 44,79% | -0,13% |
| SOL | SETTIMANALE | Classic technical | 61 | 50,82% | +0,09% |
| SOL | SETTIMANALE | Famiglia statistica | 77 | 57,14% | +0,25% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 4 | 0,00% | -4,09% |
| SOL | SETTIMANALE | Tecnico | 88 | 45,45% | -0,07% |
| SOL | SWING | Classic technical | 23 | 65,22% | +1,07% |
| SOL | SWING | Famiglia statistica | 31 | 70,97% | +1,02% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 2 | 0,00% | -4,49% |
| SOL | SWING | Tecnico | 39 | 56,41% | +0,54% |
| SOL | MEDIO | Famiglia statistica | 5 | 80,00% | +1,22% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Tecnico | 7 | 28,57% | -1,02% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 3 | in attesa di controlli maturati |
| BTC | MEDIO | 13 | in attesa di controlli maturati |
| SOL | MEDIO | 12 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 2 | in attesa di controlli maturati |
| DOGE | MEDIO | 12 | in attesa di controlli maturati |

## Come leggere le raccomandazioni

- **OSSERVA**: meno di 30 controlli, nessuna modifica.
- **PESO OK / MANTIENI**: il modulo sta aiutando, ma non serve cambiare peso.
- **NON AUMENTARE**: il modulo non dimostra ancora un vantaggio sufficiente.
- **POSSIBILE AUMENTO LEGGERO**: proposta prudente, mai automatica.
- **POSSIBILE RIDUZIONE**: modulo debole con campione già abbastanza maturo.
- **ESCLUSO**: benchmark o diagnostica già inclusa in un'altra famiglia.

Nota decisiva: **non sommare mai una modifica alla Famiglia statistica e altre modifiche separate a Scanner o Market Regime**. Scanner e Market servono soltanto a capire quale parte della famiglia sta funzionando o fallendo.

## Stato attuale

È iniziata la prima calibrazione, ma sono ammesse solo valutazioni leggere e manuali.
<!-- GLOBAL_WEIGHT_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:global_weight_calibration -->

<!-- COMPACT_SECTION_START:risk_calibration -->
<details>
<summary><strong>🛡️ Calibrazione rischio spot / leva</strong></summary>

<!-- RISK_CALIBRATION_START -->
# Calibrazione rischio spot / leva

Report completo: [risk_calibration_report.md](risk_calibration_report.md)

Questo blocco controlla se le zone di rischio previste dallo scanner vengono davvero toccate nei 30 giorni successivi.

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         35 |               7 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         35 |               7 |          28 | RACCOLTA DATI | 14,29%           | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         35 |               7 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                         |
|:--------|:---------------|:---------------|:------------------------------------------------------------------|
| BTC     | BASSO          | MEDIO          | leva da limitare; 2x/3x solo con invalidazione chiara             |
| SOL     | BASSO          | MEDIO          | leva moderata possibile solo con stop e margine                   |
| DOGE    | MEDIO          | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-08-14 10:53 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [global_confluence_report.md](global_confluence_report.md)

Questo report mette insieme i moduli principali dello scanner e controlla se si confermano o si contraddicono.

Moduli letti:

- Famiglia statistica Scanner + Market Regime, conteggiata una sola volta
- Scanner path / cono previsionale
- Struttura tecnica classica precedente
- Classic technical confirmation, filtro tecnico completo
- Frattale BTC 2022 vs SOL 2026, solo per SOL
- Fractal path tracker, solo per SOL
- RSI top-cycle, soprattutto per SOL
- Major alt lifecycle squeeze / EMA200 weekly, solo per SOL
- Exchange microstructure: OI, funding, taker flow, order book e liquidazioni campionate
- Futures / liquidazioni precedente, mantenuto come diagnostica
- Cambiamento giornaliero

Nota statistica: **Scanner e Market Regime non vengono più sommati come due prove indipendenti**. Lo Scanner è il punteggio principale; il Market Regime può aggiungere al massimo 1 punto di conferma con almeno 10 match. La famiglia statistica è limitata a ±4.

Nota importante: **Lifecycle EMA200 viene letto e mostrato, ma vale sempre 0 punti nel Global Confluence**. Serve come contesto, non come conferma operativa.

Nota Classic technical: **pesa massimo ±1** perché è un filtro di conferma e in parte si sovrappone alla struttura tecnica già esistente.

Nota exchange: **candidato massimo ±1, peso iniziale 0** e più conferme indipendenti. Order book, funding o una singola liquidazione non bastano da soli.

## Sintesi operativa

| Asset | Punteggio | Confluenza | Bias | Affidabilità | Azione coerente | Conferme | Invalidazioni |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD / ATTESA CONFERME | Prima resistenza sopra 65.402; conferma del doppio minimo sopra 66.910. | Sotto 62.227 il quadro tecnico peggiora. |
| SOL | +3 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | HOLD / TRANCHE PICCOLE, NO LEVA | conferma del doppio minimo sopra 83,81; nuova conferma tecnica sopra 77,62; milestone analogiche 79,14 / 89,87, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 69,65 / 70,69 / 62,19. |
| DOGE | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.07117 migliora; sopra 0.06966 viene invalidato il pattern ribassista dominante. | Sotto 0.06835 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | +2 | +4 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 |
| SOL | +3 | +2 | +4 | 0 | -2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +3 |
| DOGE | +3 | +2 | +4 | 0 | 0 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | +2 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD / ATTESA CONFERME**

BTC è in fase mista. Non è abbastanza debole da autorizzare short semplici, ma non ha ancora una conferma piena.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +2, match regime 19. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 72,50%, return centrale 30g +8,71%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 19, positivi 30g 73,68%, return p50 +8,98%.
- Scanner path: **0** — Controlli disponibili 33. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -6/12, verdetto debole, trend ribassista, struttura compressione / triangolo, divergenza nessuna, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -9/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati -1.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — BTC: cambiamento medio in misto rispetto a ieri.

Conferme: Prima resistenza sopra 65.402; conferma del doppio minimo sopra 66.910.

Invalidazioni: Sotto 62.227 il quadro tecnico peggiora.

### SOL

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+3**
- Affidabilità: **MEDIA**
- Azione coerente: **HOLD / TRANCHE PICCOLE, NO LEVA**

SOL ha una confluenza costruttiva, ma va ancora trattato come setup anticipato. La conferma vera arriva solo sopra le resistenze tecniche e con rientro del gap frattale. Il modulo lifecycle/EMA200 resta utile come contesto, ma non aumenta il punteggio Global.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +2, match regime 10. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 75,00%, return centrale 30g +5,21%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 10, positivi 30g 80,00%, return p50 +3,86%.
- Scanner path: **0** — Controlli disponibili 33. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -3/12, verdetto debole, trend misto, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff markdown / fase ribassista, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -3/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +57,44%, aderenza live +69,23%, errore live +15,39%, gap corrente -19,52%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 31, ma percorso ancorato non aderente: gap -19,52%, errore live +15,39%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 111,65 $, upside EMA200 +48,00%, gap EMA50/EMA200 -5,53%, hit EMA200 12w +33,33%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 1, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — SOL: cambiamento forte in miglioramento rispetto a ieri.

Conferme: conferma del doppio minimo sopra 83,81; nuova conferma tecnica sopra 77,62; milestone analogiche 79,14 / 89,87, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 69,65 / 70,69 / 62,19.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +2, match regime 14. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 70,00%, return centrale 30g +13,37%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 14, positivi 30g 78,57%, return p50 +13,66%.
- Scanner path: **0** — Controlli disponibili 33. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **0** — Score tecnico 0/12, verdetto neutrale / misto, trend ribassista, struttura compressione / triangolo, divergenza nessuna, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Adam and Eve Top / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -6/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.25; exchange 3/3, copertura 100%, consenso bull 1, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **-1** — DOGE: cambiamento medio in peggioramento rispetto a ieri.

Conferme: Sopra 0.07117 migliora; sopra 0.06966 viene invalidato il pattern ribassista dominante.

Invalidazioni: Sotto 0.06835 il rischio ribassista aumenta.


## Come leggere il punteggio

- +7 o più: confluenza positiva forte.
- Da +3 a +6: confluenza moderatamente positiva.
- Da 0 a +2: confluenza parziale o mista.
- Da -1 a -3: confluenza debole o fragile.
- -4 o meno: confluenza negativa.

Nota: Scanner path e Fractal path sono già integrati, ma finché hanno pochi controlli restano quasi sempre a punteggio 0.
Servono almeno 5 controlli prima di influire leggermente, e 30+ controlli prima di pesare davvero.

Nota lifecycle EMA200: il modulo Major alt lifecycle squeeze resta nel report, ma pesa **0** nel Global perché EMA50/EMA200 e target EMA200 sono contesto, non conferme dirette di prezzo.

Nota Classic technical: il modulo è utile per capire se il setup è confermato davvero, ma il suo peso resta prudente per evitare doppio conteggio con il modulo tecnico già presente.

Nota exchange: il modulo salva OI, funding, taker flow, order book e liquidazioni campionate. Il candidato è limitato a ±1; il peso Global resta 0 finché il gate storico a 7 giorni non matura.
<!-- GLOBAL_CONFLUENCE_END -->

</details>
<!-- COMPACT_SECTION_END:global_confluence -->

<!-- COMPACT_SECTION_START:btc_macro_cycle -->
<details>
<summary><strong>🌀 Bitcoin Macro Cycle — Power Law e Spiral</strong></summary>

<!-- BTC_MACRO_CYCLE_START -->
# Bitcoin Macro Cycle — Power Law e Four-Year Spiral

Generato: 2026-08-14 10:53 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 62.759 $ | prezzo corrente |
| Power Law centrale | 123.523 $ | deviazione -49,19% |
| Banda p10-p90 | 76.543 $ / 311.045 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 0,25% | posizione storica nel corridoio |
| Esponente β | 5,8200 | R² log-log 91,94% |
| Stabilità β | BASSA | range 1,3148 cambiando finestra |
| Ultimo halving | 2024-04-19 | 847 giorni fa |
| Fase ciclo | 57,98% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-14 (4350 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.1907) × giorni^5.8200
- Prezzo centrale oggi: **123.523 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 0,25%
- Scarto dal centro: **-49,19%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8200 | 91,94% |
| 2015 | 5,9042 | 91,50% |
| 2016 | 5,5903 | 87,73% |
| 2017 | 4,8604 | 82,85% |
| 2018 | 4,5894 | 78,32% |

### Backtest walk-forward contro prezzo invariato

| Orizzonte | Controlli | Vittorie vs naive | Errore mediano modello | Errore mediano naive |
| --- | --- | --- | --- | --- |
| 90g | 80 | 27,50% | 53,06% | 20,63% |
| 180g | 80 | 41,25% | 60,12% | 47,43% |
| 365g | 80 | 57,50% | 72,70% | 78,86% |
| 730g | 80 | 58,75% | 72,61% | 109,35% |

## Bitcoin Four-Year Spiral

Nel grafico l'angolo rappresenta il tempo dentro una finestra di quattro anni e il raggio rappresenta il prezzo in scala logaritmica. ATH, bottom storici e halving sono marker descrittivi: la spirale rende visibili le ricorrenze, ma non dimostra che il ciclo futuro debba ripetersi.

![Bitcoin Four-Year Spiral](bitcoin_four_year_spiral.png)

## Stessa fase dei cicli halving precedenti

| Ciclo | Data analoga | +30g | +90g | +180g | +365g |
| --- | --- | --- | --- | --- | --- |
| 2012-11-28 → 2016-07-09 | 2015-01-02 | -27,95% | -19,69% | -17,91% | +37,59% |
| 2016-07-09 → 2020-05-11 | 2018-09-30 | -4,40% | -42,34% | -38,14% | +25,18% |
| 2020-05-11 → 2024-04-19 | 2022-08-23 | -9,82% | -26,67% | +13,00% | +22,78% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 4 | 1 | 0.5443829997751726 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -4 | -1 | -3.355091126867571 | 0 |

## Tracker live Power Law

| Orizzonte | Controlli | Vittorie vs naive | Errore modello | Errore naive | Stato |
| --- | --- | --- | --- | --- | --- |
| 90g | 0 | n/a | n/a | n/a | RACCOLTA LIVE / PESO 0 |
| 180g | 0 | n/a | n/a | n/a | RACCOLTA LIVE / PESO 0 |
| 365g | 0 | n/a | n/a | n/a | RACCOLTA LIVE / PESO 0 |

Il modulo resta a peso 0 anche con un buon backtest. Prima si osserva la verifica live, poi si decide se usarlo soltanto per il rischio macro di lungo periodo. Le fotografie live della Power Law vengono salvate una sola volta per mese, così non si contano come indipendenti previsioni giornaliere quasi identiche.

## File prodotti

- `reports/btc_power_law_metrics.csv`
- `reports/btc_power_law_backtest.csv`
- `reports/btc_cycle_phase_metrics.csv`
- `reports/btc_macro_cycle_history.csv`
- `reports/btc_macro_cycle_tracker_metrics.csv`
<!-- BTC_MACRO_CYCLE_END -->

</details>
<!-- COMPACT_SECTION_END:btc_macro_cycle -->

<!-- COMPACT_SECTION_START:relative_strength_btc -->
<details>
<summary><strong>₿ Forza relativa SOL/BTC e DOGE/BTC</strong></summary>

<!-- RELATIVE_STRENGTH_BTC_START -->
# Forza relativa SOL/BTC e DOGE/BTC

Generato: 2026-08-14 10:53 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00120050 | +4 | +1 | 0 | SOVRAPERFORMA BTC | BASSA | +0,54% | RIBASSISTA | FORZA RELATIVA NASCOSTA: debole in USD ma migliore di BTC |
| DOGE | DOGE/BTC | 0.00000111 | -4 | -1 | 0 | SOTTOPERFORMA BTC | BASSA | -3,36% | MISTA | FORZA RELATIVA NEGATIVA, USD ANCORA MISTO |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** SOVRAPERFORMA BTC (+4)
- **Candidato futuro:** +1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** FORZA RELATIVA NASCOSTA: debole in USD ma migliore di BTC
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g +5,77%; 30g +0,54%; 90g +8,35%; 180g -3,96%
- **Daily:** RSI 59.83; MA50 0.00119685; MA200 0.00118389
- **Weekly:** MA30 0.00118882; RSI 48.33
- **Livelli:** supporto 0.00119400; resistenza 0.00125100; breakout 60g 0.00134900; breakdown 60g 0.00102800
- **Pattern:** DOPPIO MASSIMO / CANDIDATO; neckline 0.00113300; target 0.00108600
- **Fibonacci:** VICINO — 38.2% a 0.00121912
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; RSI relativo forte; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-4)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** FORZA RELATIVA NEGATIVA, USD ANCORA MISTO
- **Struttura:** COMPRESSIONE / TRIANGOLO POSSIBILE
- **Rendimenti relativi:** 7g +3,05%; 30g -3,36%; 90g -21,00%; 180g -25,90%
- **Daily:** RSI 48.80; MA50 0.00000114; MA200 0.00000130
- **Weekly:** MA30 0.00000130; RSI 33.23
- **Livelli:** supporto 0.00000110; resistenza 0.00000114; breakout 60g 0.00000146; breakdown 60g 0.00000104
- **Pattern:** DOPPIO MASSIMO / CONFERMATO; neckline 0.00000112; target 0.00000099
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000115
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 204 | 51,96% | +1,94% | -1,18% |
| SOL | 30g | 202 | 47,52% | +4,66% | +0,36% |
| SOL | 90g | 197 | 53,30% | +10,17% | +2,42% |
| DOGE | 7g | 294 | 55,78% | +1,84% | -1,68% |
| DOGE | 30g | 290 | 53,10% | +2,05% | -3,94% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 15 | 66,67% | -0,23% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 15 | 46,67% | -0,59% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 14 | 42,86% | -1,33% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 7 | 14,29% | -2,36% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 32 | 68,75% | +0,28% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 32 | 59,38% | +0,50% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 28 | 75,00% | +1,31% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 21 | 76,19% | +1,85% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 5 | 100,00% | +3,99% | LOCKED / RACCOLTA LIVE | 0 |

Gate prudente: almeno 30 controlli live a 7 giorni, accuratezza almeno 55% e return corretto direzione positivo. Anche dopo il gate, il contributo futuro non dovrà superare ±1 e dovrà restare dentro la famiglia tecnica.

## File prodotti

- `reports/relative_strength_btc_metrics.csv`
- `reports/relative_strength_btc_history.csv`
- `reports/relative_strength_btc_tracker_metrics.csv`
- `reports/relative_strength_btc_backtest.csv`
<!-- RELATIVE_STRENGTH_BTC_END -->

</details>
<!-- COMPACT_SECTION_END:relative_strength_btc -->

<!-- COMPACT_SECTION_START:btc_sol_fractal -->
<details>
<summary><strong>🧬 Frattale mirato BTC 2022 / SOL 2026</strong></summary>

<!-- BTC_SOL_FRACTAL_START -->

---

# Frattale mirato: BTC 2022 vs SOL 2026

Report separato completo: [btc_2022_vs_sol_2026_report.md](btc_2022_vs_sol_2026_report.md)

Ultima candela SOL usata: **14 agosto 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +57,44%
- **Somiglianza strutturale:** +57,44%
- **Aderenza prezzo live:** +69,23%
- **Errore medio live:** +15,39%
- **Gap prezzo corrente:** -19,52%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 69 dal bottom usato.
- **Giorno BTC equivalente:** 2023-01-29
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Fase negativa / rischio discesa.** Zona bassa **68,64 $** intorno al **26 agosto 2026**; zona alta **75,37 $** intorno al **14 agosto 2026**; fine step circa **69,07 $** entro il **28 agosto 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 14 agosto 2026 | 43 | +69,23% | +15,39% | -19,52% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 14 agosto 2026 | 70 | +76,45% | +11,78% | -19,52% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +69,23% | Errore medio live +15,39%. |
| Gap corrente | -19,52% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 79,14 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 89,87 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 69,65 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 395,49 $ |
| Massimo percorso base | 395,49 $ (21 aprile 2029) |

## Grafici

### Grafico frattale sovrapposto

![Frattale BTC 2022 vs SOL 2026](btc_2022_vs_sol_2026_fractal_chart.png)

### Grafico proiezione condizionale

![Proiezione SOL BTC 2022](btc_2022_vs_sol_2026_projection_chart.png)

### Grafico ciclo base

![Ciclo base SOL BTC 2025](btc_2022_vs_sol_2026_cycle_base_chart.png)

### Grafico struttura vs aderenza

![Tracking frattale BTC SOL](btc_2022_vs_sol_2026_tracking_chart.png)

## Livelli chiave

| Livello | Prezzo / soglia | Lettura |
| --- | --- | --- |
| Rientro gap | entro ±12% | Condizione necessaria per tornare operativo. |
| Prima conferma | 79,14 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 89,87 $ | Scenario più credibile. |
| Invalidazione soft | 69,65 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 21 agosto 2026 | -3,44% | 72,77 $ | 72,41 $ | 75,37 $ |
| 14 giorni | 28 agosto 2026 | -8,35% | 69,07 $ | 68,64 $ | 75,37 $ |
| 30 giorni | 13 settembre 2026 | -2,64% | 73,38 $ | 68,64 $ | 78,71 $ |
| 60 giorni | 13 ottobre 2026 | +17,91% | 88,87 $ | 64,00 $ | 89,87 $ |
| 90 giorni | 12 novembre 2026 | +23,02% | 92,72 $ | 64,00 $ | 96,65 $ |
| 120 giorni | 12 dicembre 2026 | +16,70% | 87,96 $ | 64,00 $ | 96,65 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 14 agosto 2026 -> 28 agosto 2026 | -8,35% | 68,64 $ (26 agosto 2026) | 75,37 $ (14 agosto 2026) | 69,07 $ | Fase negativa / rischio discesa. |
| Step 2 - primo mese | 29 agosto 2026 -> 13 settembre 2026 | -2,64% | 69,14 $ (29 agosto 2026) | 78,71 $ (5 settembre 2026) | 73,38 $ | Prima retest / debolezza, poi recupero. |
| Step 3 - secondo mese | 14 settembre 2026 -> 13 ottobre 2026 | +17,91% | 64,00 $ (23 settembre 2026) | 89,87 $ (12 ottobre 2026) | 88,87 $ | Prima retest / debolezza, poi recupero. |
| Step 4 - terzo mese | 14 ottobre 2026 -> 12 novembre 2026 | +23,02% | 86,47 $ (4 novembre 2026) | 96,65 $ (28 ottobre 2026) | 92,72 $ | Spinta rialzista abbastanza pulita. |

Nota: le proiezioni restano condizionali. La forma simile non compensa un prezzo non aderente.

<!-- BTC_SOL_FRACTAL_END -->

</details>
<!-- COMPACT_SECTION_END:btc_sol_fractal -->

<!-- COMPACT_SECTION_START:rsi_top_cycle -->
<details>
<summary><strong>📈 RSI top-cycle SOL</strong></summary>

<!-- RSI_TOP_CYCLE_START -->

---

# RSI top-cycle warning - SOL

Report separato completo: [rsi_top_cycle_report.md](rsi_top_cycle_report.md)

Filtro prudente: usa almeno 3 picchi RSI, separa vicinanza matematica e rischio reale, e non proietta la top-line oltre 12 mesi.

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo SOL | 75,37 $ |  |
| Weekly RSI | 40,20 / linea grezza 53,18 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 40,90 / linea grezza 55,81 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 395,49 $ | Avanzamento +19,06% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 40,9, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
- Confluenza prezzo + RSI: **BASSO**

Questo non è un segnale di entrata. RSI bassi o trendline non affidabili restano neutrali e non penalizzano il Global Confluence.

## Grafici RSI

![SOL weekly RSI top-line](rsi_top_cycle_SOL_weekly.png)

![SOL monthly RSI top-line](rsi_top_cycle_SOL_monthly.png)

<!-- RSI_TOP_CYCLE_END -->

</details>
<!-- COMPACT_SECTION_END:rsi_top_cycle -->

<!-- COMPACT_SECTION_START:sol_onchain -->
<details>
<summary><strong>⛓️ Metriche on-chain SOL</strong></summary>

<!-- SOL_ONCHAIN_METRICS_START -->

---

# SOL on-chain metrics

Report separato completo: **[sol_onchain_metrics_report.md](sol_onchain_metrics_report.md)**

| Voce | Valore |
| --- | --- |
| Score on-chain | 3 |
| Bias | POSITIVA |
| Azione coerente | CONFERMA MODERATA / BUONO SE IL FRATTALE REGGE |
| Prezzo SOL | 75,37 $ |
| TVL Solana | 4,83 mld $ |
| TVL 7g | +2,30% |
| DEX volume 24h | 1,98 mld $ |
| Fees 24h | 10,10 mln $ |
| Stablecoin su Solana | 16,03 mld $ |
| Stake ratio | 68,76% |
| Metriche mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

Lettura semplice:

**CONFERMA MODERATA / BUONO SE IL FRATTALE REGGE**

Questo blocco non sostituisce il frattale SOL/BTC: serve come filtro per capire se il movimento è sostenuto anche da attività on-chain.

<!-- SOL_ONCHAIN_METRICS_END -->

</details>
<!-- COMPACT_SECTION_END:sol_onchain -->

<!-- COMPACT_SECTION_START:major_alt_lifecycle -->
<details>
<summary><strong>🔄 Lifecycle squeeze / EMA200 SOL</strong></summary>

<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_START -->

---

# Major alt lifecycle squeeze - SOL

Report separato completo: **[major_alt_lifecycle_squeeze_report.md](major_alt_lifecycle_squeeze_report.md)**

| Voce                      | Valore                                            |
|:--------------------------|:--------------------------------------------------|
| Lifecycle squeeze score | 4 |
| Bias | SQUEEZE SETUP MODERATO |
| Azione coerente | CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO |
| Peso suggerito Global | 0 |
| Trend squeeze | STABILE / DA CONFERMARE |
| Trend squeeze score | 0 |
| Confronto precedente | 2026-08-10 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 75,37 $ |
| EMA200 weekly target | 111,65 $ |
| Upside verso EMA200 | +48,00% |
| Distanza prezzo da EMA200 | -32,43% |
| Gap EMA50/EMA200 | -5,53% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 40,24 |
| Età SOL | 6,3 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +33,33% |
| Max gain mediano 12w | +19,45% |
| Drawdown mediano 12w | -22,88% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-08-14 10:53 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-08-14 10:49:06 UTC**

Questo report confronta il grafico attuale di Bitcoin, Solana e Dogecoin con tanti grafici storici di altre crypto.

Non è una previsione certa. È uno scanner statistico: guarda situazioni simili già successe e mostra cosa accadde dopo nei 30 giorni successivi.

<!-- COMPACT_SECTION_START:daily_change -->
<details open>
<summary><strong>🗓️ Cambiamenti rispetto a ieri</strong></summary>

<!-- DAILY_CHANGE_START -->

---

# Mini report cambiamenti da ieri

Report separato completo: [daily_change_report.md](daily_change_report.md)

- BTC: cambiamento importante, ma lettura mista.
- SOL: cambiamento importante in miglioramento rispetto a ieri.
- DOGE: cambiamento importante in peggioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO MEDIO | misto | RIALZISTA | +72.50% | -7.50 punti |
| SOL | CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +75.00% | +2.50 punti |
| DOGE | CAMBIAMENTO MEDIO | peggioramento | RIALZISTA | +70.00% | -2.50 punti |

<!-- DAILY_CHANGE_END -->

</details>
<!-- COMPACT_SECTION_END:daily_change -->

<!-- COMPACT_SECTION_START:bounce_after_drawdown -->
<details>
<summary><strong>↕️ Sequenze rimbalzo / dump</strong></summary>

<!-- BOUNCE_AFTER_DRAWDOWN_START -->

---

# Sequenze pratiche: rimbalzo / dump

Report separato completo: [bounce_after_drawdown_report.md](bounce_after_drawdown_report.md)

Questa sezione risponde subito a due domande:

- **Se scende, è una zona di rimbalzo?**
- **Se sale forte, è una zona da prendere profitto?**

| Asset | Scende a | Target rimbalzo | % casi rimbalzo | Movimento reale | Lettura discesa | Sale a | Target dump | % casi dump | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.622 $ | 69.036 $ | +42,86% | +15,79% | rimbalzo debole | 69.036 $ | 59.622 $ | +10,71% | -13,64% | spike storicamente più resistente |
| SOL | 71,60 $ | 82,91 $ | +26,67% | +15,79% | rimbalzo poco frequente | 82,91 $ | 71,60 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06586 $ | 0,07626 $ | +67,74% | +15,79% | buona zona storica di rimbalzo | 0,07626 $ | 0,06586 $ | +24,24% | -13,64% | spike storicamente più resistente |

## Spiegazione ultra semplice

`% casi rimbalzo` e `% casi dump` non sono percentuali assolute.

Sono percentuali **condizionate**:

- prima deve succedere la prima cosa;
- solo dopo si controlla se succede la seconda.

Esempio rimbalzo:

- prezzo iniziale 100 $
- scende a -5% = 95 $
- poi target +10% = 110 $
- da 95 $ a 110 $ il movimento reale è circa +15,79%

Quindi `poi +10%` non vuol dire +10% dal minimo. Vuol dire +10% dal prezzo iniziale.

Esempio dump:

- prezzo iniziale 100 $
- sale a +10% = 110 $
- poi target -5% = 95 $
- da 110 $ a 95 $ il movimento reale è circa -13,64%

Quindi `dump -5%` non vuol dire -5% dallo spike. Vuol dire che torna fino a 5% sotto il prezzo iniziale.

Nel report principale vedi solo la sintesi. Nel report separato ci sono anche soglie intermedie: -8%, +5%, +15%, ecc.

## Traduzione veloce

- **BTC: su 40 casi simili, 14 prima sono scesi a -5,00%. Tra quei 14, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +42,86% (6/14). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 3 poi sono scaricati a -5,00%. Percentuale: +10,71% (3/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 15 prima sono scesi a -5,00%. Tra quei 15, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +26,67% (4/15). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 21 poi sono rimbalzati fino a +10,00%. Percentuale: +67,74% (21/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: buona zona storica di rimbalzo.**
- **DOGE: su 40 casi simili, 33 prima sono saliti a +10,00%. Tra quei 33, 8 poi sono scaricati a -5,00%. Percentuale: +24,24% (8/33). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-08-14 10:51:57 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [scanner_forecast_tracker_report.md](scanner_forecast_tracker_report.md)

Questo report trasforma i 40 casi simili dello scanner in un cono previsionale leggibile.

Per ogni asset crea:

- banda larga p10-p90
- banda centrale p25-p75
- scenario centrale p50
- prezzo reale sovrapposto quando sono disponibili dati successivi

Correzione importante: il cono ora viene calcolato dai percorsi reali dei match storici, non solo dai percentili finali a 30 giorni. Quindi il grafico non deve più mostrare solo due puntini.

## Ultimo cono previsionale salvato

| Asset   | Data       | Prezzo iniziale   | Direzione scanner   | Casi positivi   | P10 30g     | P25 30g     | P50 30g     | P75 30g     | P90 30g     |
|:--------|:-----------|:------------------|:--------------------|:----------------|:------------|:------------|:------------|:------------|:------------|
| BTC | 2026-08-14 | 62.760 $ | SALITA | 72,50% | 58.086,00 $ | 61.349,91 $ | 68.227,76 $ | 74.957,59 $ | 93.372,51 $ |
| SOL | 2026-08-14 | 75,37 $ | SALITA | 75,00% | 69,71 $ | 75,00 $ | 79,30 $ | 92,03 $ | 135,21 $ |
| DOGE | 2026-08-14 | 0.06933 $ | SALITA | 70,00% | 0.05450 $ | 0.06685 $ | 0.07860 $ | 0.08937 $ | 0.09900 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-15**; verificato fino al **2026-08-14**; stato **COMPLETO 30/30g**.
- Reale **62.767,72 $**; p50 previsto **69.423,59 $**; scarto **-9,59%**.
- Errore medio assoluto **2,57%**; massimo **9,59%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-15**; verificato fino al **2026-08-14**; stato **COMPLETO 30/30g**.
- Reale **75,41 $**; p50 previsto **79,41 $**; scarto **-5,04%**.
- Errore medio assoluto **2,18%**; massimo **5,92%**; DENTRO p10-p90; DENTRO p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-15**; verificato fino al **2026-08-14**; stato **COMPLETO 30/30g**.
- Reale **0.06936 $**; p50 previsto **0.06178 $**; scarto **12,27%**.
- Errore medio assoluto **10,99%**; massimo **21,51%**; DENTRO p10-p90; FUORI p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 33 | 100,00% | 60,61% | 1,66% | -0,21% |
| BTC | 3g | 33 | 100,00% | 78,79% | 2,13% | -0,66% |
| BTC | 7g | 29 | 100,00% | 89,66% | 2,35% | 0,19% |
| BTC | 14g | 22 | 100,00% | 86,36% | 2,71% | 0,20% |
| BTC | 30g | 6 | 100,00% | 83,33% | 8,60% | -8,60% |
| SOL | 1g | 33 | 78,79% | 63,64% | 1,99% | -0,43% |
| SOL | 3g | 33 | 100,00% | 78,79% | 2,31% | -0,95% |
| SOL | 7g | 29 | 100,00% | 93,10% | 1,91% | 0,10% |
| SOL | 14g | 22 | 100,00% | 90,91% | 1,95% | 0,85% |
| SOL | 30g | 6 | 100,00% | 100,00% | 1,74% | -0,38% |
| DOGE | 1g | 33 | 96,97% | 63,64% | 2,39% | 0,09% |
| DOGE | 3g | 33 | 100,00% | 87,88% | 2,21% | 0,70% |
| DOGE | 7g | 29 | 93,10% | 89,66% | 5,50% | 3,36% |
| DOGE | 14g | 22 | 100,00% | 68,18% | 7,14% | 5,31% |
| DOGE | 30g | 6 | 100,00% | 16,67% | 14,08% | 14,08% |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |

### Confronto fuori campione: grezzo vs shadow

| Asset   | Orizzonte   |   Controlli OOS | MAE grezzo   | MAE shadow   | Miglioramento   | Shadow vince   | Copertura larga grezza   | Copertura larga shadow   |
|:--------|:------------|----------------:|:-------------|:-------------|:----------------|:---------------|:-------------------------|:-------------------------|
| BTC | 1g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC | 3g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC | 7g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE | 1g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE | 3g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE | 7g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE | 14g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL | 1g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL | 3g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL | 7g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | n/a | n/a |

## Come leggerlo

- Se il prezzo resta dentro p10-p90, lo scanner sta ancora descrivendo bene il range largo.
- Se il prezzo resta dentro p25-p75, lo scanner sta descrivendo bene anche il range centrale.
- Se il prezzo segue p50, il percorso reale è vicino allo scenario normale.
- Se il prezzo esce da p10-p90, il modello statistico dei 40 casi sta perdendo aderenza.
- Questo non sostituisce drawdown e max gain: serve soprattutto a vedere il percorso del return previsto.

Nota: servono almeno 5 controlli prima di dare un peso minimo al cono. Sotto 5 controlli resta solo osservazione.
<!-- SCANNER_FORECAST_TRACKER_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-08-14 10:52 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +72,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +75,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
<!-- EXTREME_CASES_PATH_END -->

</details>
<!-- COMPACT_SECTION_END:extreme_cases -->

<!-- COMPACT_SECTION_START:scanner_full_detail -->
<details>
<summary><strong>📚 Scanner statistico completo — percentili, mappe e 40 casi storici</strong></summary>

# Come leggere questo report

Leggilo sempre in questo ordine:

1. **Direzione più probabile**: ti dice se storicamente era più facile salita, discesa o incertezza.
2. **Casi positivi / negativi**: ti dice la percentuale storica di salita o discesa dopo 30 giorni.
3. **Return 30d**: ti dice dove potrebbe stare il prezzo fra 30 giorni.
4. **Drawdown 30d**: ti dice quanto potrebbe scendere durante quei 30 giorni.
5. **Max gain 30d**: ti dice quanto potrebbe salire durante quei 30 giorni.
6. **Scanner autocalibrato**: dopo abbastanza dati, confronta previsione e realtà e corregge la lettura.

La frase più importante è questa:

> **Return = prezzo finale dopo 30 giorni. Drawdown = discesa durante il mese. Max gain = rialzo durante il mese.**

---

# Scheda veloce: cosa sono i percentili

I **percentili** sono solo un modo per trasformare i 40 casi storici simili in scenari semplici.

## Traduzione semplice

- **Percentile 10%** = molto male / scenario brutto.
- **Percentile 25%** = male / scenario negativo.
- **Percentile 50%** = normale / scenario centrale. È il più importante.
- **Percentile 75%** = bene / scenario buono.
- **Percentile 90%** = molto bene / scenario molto forte.

## Cosa guardare davvero

- Per capire la situazione normale: guarda sempre il **Percentile 50%**.
- Per capire il rischio con leva: guarda **Drawdown 25%** e **Drawdown 10%**.
- Per capire un possibile take profit: guarda **Max gain 50%** e **Max gain 75%**.

## I tre tipi di percentili

- **Percentili Return 30d** = dove potrebbe stare il prezzo fra 30 giorni.
- **Percentili Drawdown 30d** = quanto potrebbe scendere durante i 30 giorni.
- **Percentili Max gain 30d** = quanto potrebbe salire durante i 30 giorni.

## Esempio semplice

Se SOL oggi vale 82 $ e il report dice:

- **Return 50% → 81 $**: fra 30 giorni lo scenario normale è circa 81 $.
- **Drawdown 50% → 77 $**: durante il mese può scendere normalmente verso 77 $.
- **Max gain 50% → 92 $**: durante il mese può fare uno spike normale verso 92 $.

Quindi può salire e scendere durante il mese, ma il **return** guarda solo dove finisce dopo 30 giorni.

---

# Lettura velocissima

Questa è la parte da leggere per prima. Ti dice subito se lo scenario è più da salita, discesa o incertezza.

## Bitcoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **72,50%**
- Casi negativi / discesa storica: **27,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **62.760,22 $**
- Return normale fra 30 giorni: **68.227,76 $** (8,71%)
- Drawdown normale durante il mese: **60.243,65 $** (-4,01%)
- Drawdown brutto da rispettare: **58.628,01 $** (-6,58%)
- Max gain normale durante il mese: **75.346,67 $** (20,05%)
- Max gain buono / take profit ottimistico: **85.850,75 $** (36,79%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **75,00%**
- Casi negativi / discesa storica: **25,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **75,37 $**
- Return normale fra 30 giorni: **79,30 $** (5,21%)
- Drawdown normale durante il mese: **72,34 $** (-4,02%)
- Drawdown brutto da rispettare: **70,36 $** (-6,65%)
- Max gain normale durante il mese: **87,55 $** (16,16%)
- Max gain buono / take profit ottimistico: **101,19 $** (34,25%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **70,00%**
- Casi negativi / discesa storica: **30,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,08 $** (13,37%)
- Drawdown normale durante il mese: **0,06 $** (-9,45%)
- Drawdown brutto da rispettare: **0,06 $** (-13,79%)
- Max gain normale durante il mese: **0,09 $** (23,28%)
- Max gain buono / take profit ottimistico: **0,10 $** (40,90%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 62.760,22 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **72,50%**
- Probabilità storica di discesa: **27,50%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **58.086,00 $** (-7,45%)
- Se va male: **61.349,91 $** (-2,25%)
- Scenario normale: **68.227,76 $** (8,71%)
- Se va bene: **74.957,59 $** (19,43%)
- Se va molto bene: **93.372,51 $** (48,78%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **60.243,65 $** (-4,01%)
- Discesa brutta: **58.628,01 $** (-6,58%)
- Discesa molto brutta: **52.342,88 $** (-16,60%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **75.346,67 $** (20,05%)
- Rialzo buono: **85.850,75 $** (36,79%)
- Rialzo molto forte: **108.589,26 $** (73,02%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **60.243,65 $** e uno spike normale intorno a **75.346,67 $**.

La chiusura a 30 giorni era più spesso positiva: salita 72,50%, discesa 27,50%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 75,37 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **75,00%**
- Probabilità storica di discesa: **25,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **69,71 $** (-7,52%)
- Se va male: **75,00 $** (-0,49%)
- Scenario normale: **79,30 $** (5,21%)
- Se va bene: **92,03 $** (22,11%)
- Se va molto bene: **135,21 $** (79,39%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **72,34 $** (-4,02%)
- Discesa brutta: **70,36 $** (-6,65%)
- Discesa molto brutta: **67,37 $** (-10,61%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **87,55 $** (16,16%)
- Rialzo buono: **101,19 $** (34,25%)
- Rialzo molto forte: **154,43 $** (104,89%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **72,34 $** e uno spike normale intorno a **87,55 $**.

La chiusura a 30 giorni era più spesso positiva: salita 75,00%, discesa 25,00%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 0,07 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **70,00%**
- Probabilità storica di discesa: **30,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,05 $** (-21,39%)
- Se va male: **0,07 $** (-3,58%)
- Scenario normale: **0,08 $** (13,37%)
- Se va bene: **0,09 $** (28,91%)
- Se va molto bene: **0,10 $** (42,79%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,06 $** (-9,45%)
- Discesa brutta: **0,06 $** (-13,79%)
- Discesa molto brutta: **0,05 $** (-27,84%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,09 $** (23,28%)
- Rialzo buono: **0,10 $** (40,90%)
- Rialzo molto forte: **0,11 $** (58,08%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,06 $** e uno spike normale intorno a **0,09 $**.

La chiusura a 30 giorni era più spesso positiva: salita 70,00%, discesa 30,00%. Quindi la lettura principale è favorevole.

---

# Come leggere correttamente i 30 giorni

Ogni report giornaliero è una previsione statistica sui **prossimi 30 giorni**.

Ci sono tre dati diversi:

1. **Return 30d** = dove potrebbe stare il prezzo fra 30 giorni.
2. **Drawdown 30d** = quanto potrebbe scendere durante quei 30 giorni.
3. **Max gain 30d** = quanto potrebbe salire al massimo durante quei 30 giorni.

Il prezzo può salire durante il mese e poi chiudere sotto, oppure scendere prima e poi recuperare. Per chi usa leva, il drawdown è spesso più importante del prezzo finale.

# Controllo accuratezza dello scanner

Questa sezione controlla se lo scanner sta funzionando davvero. Ogni giorno viene salvata una previsione. Dopo 30 giorni, lo scanner confronta quella previsione con quello che è successo realmente.

## Come leggerla

- **Previsioni già controllate** = quante vecchie previsioni hanno già compiuto 30 giorni.
- **Direzione corretta** = quante volte lo scanner ha indovinato salita o discesa finale a 30 giorni.
- **Errore medio scenario centrale** = quanto era distante il prezzo reale dal prezzo centrale previsto.
- **Zona rischio toccata** = quante volte il prezzo è sceso fino alla zona di rischio prevista.
- **Zona rialzo toccata** = quante volte il prezzo è salito fino alla zona rialzo prevista.

## Riassunto accuratezza

### Bitcoin

- Previsioni già controllate: **13**
- Direzione corretta: **70,00%**
- Errore medio dello scenario centrale: **5,19%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **13**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **12,18%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Solana

- Previsioni già controllate: **13**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **4,35%**
- Zona rischio toccata: **15,38%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

Spiegazione semplice: se col tempo la direzione corretta è bassa o l'errore medio è alto, lo scanner va preso con più cautela. Se invece molte previsioni finiscono dentro i livelli previsti, allora lo scanner sta diventando più affidabile.

---

# Scanner autocalibrato

Questa è una sezione separata dalla previsione storica grezza. La previsione grezza resta quella basata sui pattern storici. Qui invece lo scanner guarda i propri errori passati e prova a correggere leggermente la lettura.

## Come funziona

Lo scanner confronta le sue vecchie previsioni con la realtà dopo 30 giorni.

- Se in passato è stato troppo ottimista, abbassa la stima.
- Se in passato è stato troppo pessimista, alza la stima.
- Se ha sottostimato il drawdown, rende la zona rischio più prudente.
- Se ha sovrastimato gli spike, riduce la zona rialzo calibrata.

La calibrazione non modifica il codice. Crea solo una seconda lettura: **scanner grezzo** contro **scanner corretto dai suoi errori reali**.

Regola: servono almeno **30 previsioni controllate per asset** prima di applicare la calibrazione. Prima di allora mostra solo dati insufficienti.

## Bitcoin

Dati ancora insufficienti: previsioni controllate **13** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **13** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **13** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 62.760,22 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **72,50%**
- Casi negativi dopo 30 giorni: **27,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,32%**
- Rendimento medio dopo 30 giorni: **16,92%**
- Rendimento centrale dopo 30 giorni: **8,71%**
- Discesa media durante i 30 giorni: **-6,17%**
- Massimo rialzo medio durante i 30 giorni: **32,33%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **73.381,88 $**
- Scenario centrale a 30 giorni: **68.227,76 $**
- Zona di rischio media: **58.888,69 $**
- Zona di rialzo media: **83.049,70 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -7,45% → **58.086,00 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -2,25% → **61.349,91 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 8,71% → **68.227,76 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 19,43% → **74.957,59 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 48,78% → **93.372,51 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -16,60% → **52.342,88 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -6,58% → **58.628,01 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -4,01% → **60.243,65 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **62.760,22 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **62.760,22 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 6,27% → **66.694,91 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 9,40% → **68.658,19 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 20,05% → **75.346,67 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 36,79% → **85.850,75 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 73,02% → **108.589,26 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XLM-USD         | 2020-08-09   | 2020-11-16 |        89.41 |       133.71 |           0    |         152.04 |
| XRP-USD         | 2023-07-20   | 2023-10-27 |        88.66 |        12.95 |          -0.13 |          31.02 |
| NEO-USD         | 2018-10-24   | 2019-01-31 |        88.26 |        27.24 |          -1.02 |          46.91 |
| XRP-USD         | 2026-01-05   | 2026-04-14 |        87.69 |         8.98 |           0    |           8.98 |
| OMG-USD         | 2018-10-24   | 2019-01-31 |        87.22 |        17.35 |          -6.48 |          23.17 |
| ETH-USD         | 2026-01-05   | 2026-04-14 |        86.91 |        -1.82 |          -3.01 |           4.21 |
| BTC-USD         | 2018-10-22   | 2019-01-29 |        86.85 |        11.79 |          -1.41 |          20.14 |
| WAVES-USD       | 2024-05-15   | 2024-08-22 |        86.77 |         6.69 |         -14.17 |           7.19 |
| ETC-USD         | 2018-10-24   | 2019-01-31 |        86.68 |         8.28 |          -4.92 |          22.5  |
| LTC-USD         | 2023-07-23   | 2023-10-30 |        86.52 |         1.07 |          -4.03 |           8.55 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 75,37 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **75,00%**
- Casi negativi dopo 30 giorni: **25,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **78,76%**
- Rendimento medio dopo 30 giorni: **31,11%**
- Rendimento centrale dopo 30 giorni: **5,21%**
- Discesa media durante i 30 giorni: **-5,00%**
- Massimo rialzo medio durante i 30 giorni: **45,78%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **98,82 $**
- Scenario centrale a 30 giorni: **79,30 $**
- Zona di rischio media: **71,60 $**
- Zona di rialzo media: **109,87 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -7,52% → **69,71 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -0,49% → **75,00 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 5,21% → **79,30 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 22,11% → **92,03 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 79,39% → **135,21 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -10,61% → **67,37 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -6,65% → **70,36 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -4,02% → **72,34 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **75,37 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **75,37 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 4,15% → **78,50 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 8,40% → **81,70 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 16,16% → **87,55 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 34,25% → **101,19 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 104,89% → **154,43 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ENJ-USD         | 2018-10-24   | 2019-01-31 |        85.2  |       190.3  |         -13.17 |         193.34 |
| DASH-USD        | 2020-02-11   | 2020-05-20 |        82.67 |       -10.33 |         -10.33 |           2.52 |
| ZIL-USD         | 2020-08-06   | 2020-11-13 |        82.25 |        61.38 |          -1.51 |          75.54 |
| BCH-USD         | 2020-02-11   | 2020-05-20 |        81.78 |        -3    |          -6.13 |           7.4  |
| EOS-USD         | 2018-11-08   | 2019-02-15 |        81.59 |        34.78 |           0    |          52.35 |
| ONE-USD         | 2020-02-11   | 2020-05-20 |        81.37 |       -21.28 |         -21.28 |           3.36 |
| BNB-USD         | 2026-01-10   | 2026-04-19 |        81.21 |         3.72 |          -0.24 |           9.96 |
| EOS-USD         | 2020-02-11   | 2020-05-20 |        81    |        -3.52 |          -4.81 |           8.72 |
| VET-USD         | 2020-02-13   | 2020-05-22 |        80.9  |        85.39 |          -2.6  |         109.53 |
| BNB-USD         | 2020-02-11   | 2020-05-20 |        80.9  |        -5.81 |          -5.81 |           6.08 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 0,07 $

Dogecoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **70,00%**
- Casi negativi dopo 30 giorni: **30,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,96%**
- Rendimento medio dopo 30 giorni: **15,17%**
- Rendimento centrale dopo 30 giorni: **13,37%**
- Discesa media durante i 30 giorni: **-11,10%**
- Massimo rialzo medio durante i 30 giorni: **29,61%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,08 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,06 $**
- Zona di rialzo media: **0,09 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -21,39% → **0,05 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -3,58% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 13,37% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 28,91% → **0,09 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 42,79% → **0,10 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -27,84% → **0,05 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -13,79% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -9,45% → **0,06 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -5,64% → **0,07 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,45% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,23% → **0,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 13,19% → **0,08 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 23,28% → **0,09 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 40,90% → **0,10 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 58,08% → **0,11 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| OP-USD          | 2026-01-06   | 2026-04-15 |        91.38 |        14.03 |          -0.09 |          43.84 |
| ADA-USD         | 2019-06-16   | 2019-09-23 |        89.49 |       -21.3  |         -21.3  |           0    |
| ZEC-USD         | 2019-06-21   | 2019-09-28 |        88.72 |        -6.19 |         -18.51 |           0    |
| AVAX-USD        | 2025-09-13   | 2025-12-21 |        88.39 |        -0.45 |          -0.48 |          21.42 |
| WAVES-USD       | 2022-03-27   | 2022-07-04 |        88.36 |         2.44 |         -14.68 |          13.6  |
| VET-USD         | 2022-03-29   | 2022-07-06 |        88.17 |        33.03 |          -9.15 |          33.03 |
| HBAR-USD        | 2020-08-06   | 2020-11-13 |        88.12 |         8.3  |          -6.49 |          22.39 |
| ADA-USD         | 2022-03-27   | 2022-07-04 |        87.99 |         6.67 |         -11.01 |          11.91 |
| CHZ-USD         | 2022-03-26   | 2022-07-03 |        87.64 |        38.08 |          -1.3  |          51.2  |
| BAT-USD         | 2018-10-24   | 2019-01-31 |        87.59 |        58.23 |          -7.19 |          58.23 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-08-14 10:52 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 62.760 $ | False | -19.64% | -10.35% | BEAR | -19.64% | -10.35% |
| DOGE-USD | BEAR | 0.06933 $ | False | -36.56% | -16.94% | BEAR | -19.64% | -10.35% |
| SOL-USD | BEAR | 75,37 $ | False | -12.81% | -17.16% | BEAR | -19.64% | -10.35% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 72.50% | 8.71% | 19.43% | 48.78% | -4.01% | -16.60% | 20.05% | 36.79% | 73.02% | 60.00% | 16.53% | 65.84% | 112.25% |
| BTC-USD | SAME_BTC_REGIME | 22 | 72.73% | 8.71% | 17.03% | 49.50% | -3.50% | -10.45% | 19.43% | 37.48% | 70.74% | 45.45% | -8.92% | 66.53% | 105.81% |
| BTC-USD | SAME_ASSET_REGIME | 23 | 73.91% | 8.98% | 18.10% | 45.07% | -4.24% | -15.65% | 18.73% | 28.54% | 62.61% | 52.17% | 5.16% | 67.23% | 104.60% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 73.68% | 8.98% | 16.71% | 56.82% | -3.99% | -7.44% | 18.73% | 25.51% | 71.10% | 47.37% | -11.59% | 70.57% | 117.47% |
| DOGE-USD | ALL_MATCHES | 40 | 70.00% | 13.37% | 28.91% | 42.79% | -9.45% | -27.84% | 23.28% | 40.90% | 58.08% | 50.00% | -0.19% | 16.02% | 86.97% |
| DOGE-USD | SAME_BTC_REGIME | 20 | 85.00% | 15.57% | 30.17% | 54.05% | -10.07% | -17.54% | 26.08% | 43.91% | 60.93% | 50.00% | -0.19% | 10.21% | 111.39% |
| DOGE-USD | SAME_ASSET_REGIME | 16 | 81.25% | 14.57% | 25.54% | 35.56% | -9.45% | -20.60% | 23.93% | 33.56% | 47.52% | 50.00% | -0.19% | 6.28% | 16.69% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 14 | 78.57% | 13.66% | 24.05% | 34.92% | -9.96% | -23.99% | 23.28% | 34.32% | 48.99% | 42.86% | -2.61% | 4.50% | 8.34% |
| SOL-USD | ALL_MATCHES | 40 | 75.00% | 5.21% | 22.11% | 79.39% | -4.02% | -10.61% | 16.16% | 34.25% | 104.89% | 57.50% | 13.74% | 61.82% | 185.86% |
| SOL-USD | SAME_BTC_REGIME | 14 | 85.71% | 4.12% | 19.65% | 69.98% | -2.20% | -7.03% | 20.24% | 43.82% | 90.92% | 50.00% | 10.80% | 62.36% | 137.02% |
| SOL-USD | SAME_ASSET_REGIME | 12 | 75.00% | 3.86% | 13.74% | 20.46% | -4.82% | -12.56% | 18.02% | 24.85% | 46.69% | 41.67% | -9.43% | 57.87% | 138.77% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 10 | 80.00% | 3.86% | 14.97% | 37.94% | -4.82% | -7.71% | 20.24% | 27.93% | 63.07% | 40.00% | -9.43% | 60.32% | 174.40% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 22 | 72.73% | 8.71% | -3.50% | 37.48% | 45.45% | -8.92% | 89.45% |
| BTC-USD | HISTORICAL_BTC_BULL | 10 | 90.00% | 14.80% | -0.30% | 35.24% | 90.00% | 21.72% | 93.79% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 30.61% | -14.39% | 37.23% | 100.00% | 66.62% | 144.58% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 7 | 42.86% | -3.52% | -4.81% | 22.81% | 57.14% | 48.71% | 78.63% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 20 | 85.00% | 15.57% | -10.07% | 43.91% | 50.00% | -0.19% | 54.93% |
| DOGE-USD | HISTORICAL_BTC_BULL | 16 | 43.75% | -1.95% | -8.62% | 31.14% | 43.75% | -15.15% | 46.56% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 11.10% | 0.00% | 36.94% | 100.00% | 19.41% | 36.94% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 100.00% | 24.33% | -8.70% | 28.68% | 66.67% | 5.82% | 52.26% |
| SOL-USD | HISTORICAL_BTC_BEAR | 14 | 85.71% | 4.12% | -2.20% | 43.82% | 50.00% | 10.80% | 103.55% |
| SOL-USD | HISTORICAL_BTC_BULL | 8 | 87.50% | 8.39% | -2.96% | 92.25% | 50.00% | 4.67% | 237.88% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 18 | 61.11% | 3.91% | -4.35% | 24.53% | 66.67% | 18.49% | 64.82% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 23 | 73.91% | 8.98% | -4.24% | 28.54% | 52.17% | 5.16% | 90.77% |
| BTC-USD | HISTORICAL_ASSET_BULL | 6 | 100.00% | 17.51% | -0.07% | 64.82% | 100.00% | 82.44% | 226.50% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 3.72% | -0.24% | 9.96% | 0.00% | -6.25% | 16.45% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 36.64% | 0.00% | 104.38% | 100.00% | 55.18% | 104.38% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 9 | 44.44% | -3.52% | -6.59% | 25.65% | 55.56% | 0.92% | 61.71% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 16 | 81.25% | 14.57% | -9.45% | 33.56% | 50.00% | -0.19% | 47.38% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 11 | 63.64% | 11.10% | -5.30% | 41.65% | 72.73% | 14.56% | 74.19% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 51.18% | -11.72% | 54.71% | 100.00% | 82.52% | 130.29% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 11 | 54.55% | 2.44% | -10.96% | 24.62% | 18.18% | -21.46% | 31.65% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 12 | 75.00% | 3.86% | -4.82% | 24.85% | 41.67% | -9.43% | 73.00% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 100.00% | 55.48% | -0.75% | 195.28% | 75.00% | 134.76% | 1021.74% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -2.44% | -4.99% | 7.89% | 0.00% | -3.94% | 12.75% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 4 | 75.00% | 57.68% | -1.30% | 105.67% | 75.00% | 84.05% | 167.40% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 18 | 72.22% | 4.58% | -4.29% | 21.01% | 66.67% | 18.49% | 64.82% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | NEO-USD | 2018-10-24 | 88.26% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 27.24% | -1.02% | 46.91% | 44.33% | -1.02% | 46.91% |
| BTC-USD | XRP-USD | 2026-01-05 | 87.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.98% | 0.00% | 8.98% | -15.55% | -19.71% | 8.98% |
| BTC-USD | OMG-USD | 2018-10-24 | 87.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 17.35% | -6.48% | 23.17% | 67.84% | -6.48% | 81.36% |
| BTC-USD | ETH-USD | 2026-01-05 | 86.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.82% | -3.01% | 4.21% | -27.68% | -32.48% | 4.21% |
| BTC-USD | BTC-USD | 2018-10-22 | 86.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.79% | -1.41% | 20.14% | 19.10% | -1.41% | 20.14% |
| BTC-USD | ETC-USD | 2018-10-24 | 86.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.28% | -4.92% | 22.50% | 22.00% | -4.92% | 23.79% |
| BTC-USD | 1INCH-USD | 2024-07-11 | 86.23% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 11.07% | -15.97% | 17.08% | 73.31% | -15.97% | 124.84% |
| BTC-USD | SOL-USD | 2026-01-08 | 85.92% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.16% | -6.58% | 9.54% | -17.40% | -30.02% | 9.54% |
| BTC-USD | XTZ-USD | 2018-10-24 | 85.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 7.22% | -3.99% | 22.40% | 159.29% | -3.99% | 179.67% |
| BTC-USD | XTZ-USD | 2026-01-10 | 85.39% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.85% | -5.85% | 13.19% | -34.77% | -35.82% | 13.19% |
| DOGE-USD | OP-USD | 2026-01-06 | 91.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.03% | -0.09% | 43.84% | -9.51% | -24.09% | 43.84% |
| DOGE-USD | ADA-USD | 2022-03-27 | 87.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.67% | -11.01% | 11.91% | -3.21% | -11.01% | 21.44% |
| DOGE-USD | CHZ-USD | 2022-03-26 | 87.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 38.08% | -1.30% | 51.20% | 116.30% | -1.30% | 153.33% |
| DOGE-USD | NEO-USD | 2022-03-27 | 87.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.88% | -6.07% | 31.81% | 4.99% | -6.07% | 39.85% |
| DOGE-USD | THETA-USD | 2022-03-26 | 87.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.01% | -10.28% | 22.09% | -4.02% | -10.28% | 37.23% |
| DOGE-USD | QTUM-USD | 2022-07-30 | 87.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.20% | -30.29% | 1.37% | -32.40% | -35.81% | 1.37% |
| DOGE-USD | FTM-USD | 2022-03-27 | 86.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 27.54% | -11.30% | 35.15% | 1.61% | -11.30% | 54.20% |
| DOGE-USD | DASH-USD | 2022-03-27 | 86.80% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.84% | -9.75% | 18.21% | 3.04% | -9.75% | 28.47% |
| DOGE-USD | LINK-USD | 2022-03-27 | 86.55% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.28% | -7.21% | 23.01% | 7.64% | -7.21% | 45.11% |
| DOGE-USD | OMG-USD | 2022-03-27 | 86.14% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.11% | -12.12% | 23.54% | -4.37% | -12.12% | 28.43% |
| SOL-USD | ENJ-USD | 2018-10-24 | 85.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 190.30% | -13.17% | 193.34% | 417.86% | -13.17% | 644.83% |
| SOL-USD | SOL-USD | 2026-01-08 | 79.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.16% | -6.58% | 9.54% | -17.40% | -30.02% | 9.54% |
| SOL-USD | RUNE-USD | 2026-01-11 | 79.79% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.83% | 0.00% | 48.60% | -7.07% | -24.29% | 48.60% |
| SOL-USD | NEAR-USD | 2026-01-05 | 79.41% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 15.59% | -7.11% | 17.95% | 56.65% | -7.11% | 107.36% |
| SOL-USD | KAVA-USD | 2026-01-10 | 78.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.53% | 0.00% | 23.31% | -16.11% | -23.42% | 23.31% |
| SOL-USD | XTZ-USD | 2018-11-03 | 78.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 21.01% | 0.00% | 22.38% | 147.35% | 0.00% | 179.64% |
| SOL-USD | QTUM-USD | 2018-10-24 | 77.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 13.12% | -5.39% | 29.47% | 61.55% | -5.39% | 61.55% |
| SOL-USD | BTC-USD | 2026-01-08 | 77.31% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.39% | -4.24% | 6.50% | -14.94% | -21.08% | 6.50% |
| SOL-USD | LINK-USD | 2026-01-10 | 76.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.18% | 0.00% | 18.10% | -11.79% | -18.96% | 18.10% |
| SOL-USD | ETH-USD | 2026-01-10 | 75.89% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.84% | -6.84% | 4.91% | -24.52% | -30.74% | 4.91% |

## Interpretation rules

- ALL_MATCHES is the raw view. It can mix bull, bear, recovery and distribution phases.
- SAME_BTC_REGIME is cleaner because BTC had a similar macro background.
- SAME_ASSET_REGIME is cleaner because the matched altcoin had a similar local trend.
- SAME_BTC_AND_ASSET_REGIME is the cleanest filter, but it needs enough matches to matter.
- If SAME_BTC_AND_ASSET_REGIME has fewer than 5 matches, treat it as useful context, not a strong statistic.
- If ALL_MATCHES is bullish but SAME_BTC_AND_ASSET_REGIME is bearish, the bullish read is weaker.
- If ALL_MATCHES is uncertain but SAME_BTC_AND_ASSET_REGIME improves, the setup is more interesting.

## Regime definitions

- BULL: price above MA200, MA200 rising, positive 90d trend.
- BEAR: price below MA200, MA200 falling, weak 90d trend.
- RECOVERY: improving 90d trend, but not yet a clean bull structure.
- DISTRIBUTION: price still structurally high, but 90d momentum is weakening.
- MIXED: unclear regime.
- UNKNOWN: not enough historical data.
<!-- MARKET_REGIME_MATCH_END -->

</details>
<!-- COMPACT_SECTION_END:market_regime -->

<!-- COMPACT_SECTION_START:classic_technical -->
<details>
<summary><strong>📐 Conferma tecnica classica</strong></summary>

<!-- CLASSIC_TECHNICAL_CONFIRMATION_START -->
# Classic technical confirmation report

Generato: 2026-08-14 10:52 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [classic_technical_confirmation_report.md](classic_technical_confirmation_report.md)

Questo modulo controlla se il setup è confermato secondo analisi tecnica classica. Non sostituisce lo scanner frattale: serve come filtro di conferma.

Cosa controlla:

- trend daily e weekly
- stage analysis stile Weinstein
- struttura massimi/minimi
- breakout o breakdown con volume
- RSI e MACD
- OBV, CMF e volume relativo
- candele principali
- Wyckoff semplificato
- volatilità tecnica locale tramite ATR e distanza dai livelli

## Sintesi

| Asset | Prezzo | Score | Verdetto | Stage | Struttura | Wyckoff | Volatilità locale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.760 $ | -9 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | MARKDOWN / DEBOLEZZA | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 75,37 $ | -3 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | VOLATILITÀ IN ESPANSIONE | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.06933 $ | -6 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | MARKDOWN / DEBOLEZZA | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -4 | +2 | -3 | -2 | 0 | 0 | -2 | -9 |
| SOL | -3 | 0 | 0 | +1 | 0 | -1 | 0 | -3 |
| DOGE | -4 | +2 | 0 | -1 | 0 | -1 | -2 | -6 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.227 $ | 64.186 $ | 67.248 $ | 57.748 $ | 1,70% | -2,99% | -19,65% |
| SOL | 74,16 $ | 75,94 $ | 83,81 $ | 63,16 $ | 2,40% | -2,35% | -12,81% |
| DOGE | 0.06835 $ | 0.07117 $ | 0.09169 $ | 0.06797 $ | 2,47% | -6,29% | -36,55% |

## Lettura dettagliata

### BTC

- Prezzo: **62.760 $**
- Score classico: **-9 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 1,70%; distanza supporto 0,88%; distanza resistenza 2,24%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-3** — RSI neutrale 41.6; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.09; volume ratio 0.96
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 41.57 |
| MACD histogram | -150.79046 |
| CMF20 | -0.093 |
| Volume ratio 20 | 0.96 |
| MA20 | 63.934 $ |
| MA50 | 63.447 $ |
| MA100 | 67.039 $ |
| MA200 | 69.501 $ |
| Pendenza MA50 20g | +0,43% |
| Pendenza MA200 60g | -10,35% |
| Bollinger width | 4,85% |
| Bollinger position | 0.12 |

### SOL

- Prezzo: **75,37 $**
- Score classico: **-3 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 2,40%; distanza supporto 1,74%; distanza resistenza 0,65%

Dettaglio:

- Trend: **-3** — prezzo sotto MA200 daily; MA50 daily in salita; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **0** — RSI sano 51.5; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+1** — OBV sopra media; CMF neutrale -0.03; volume ratio 0.80
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **-1** — Bearish engulfing
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 51.47 |
| MACD histogram | 0.28471 |
| CMF20 | -0.026 |
| Volume ratio 20 | 0.80 |
| MA20 | 74,47 $ |
| MA50 | 75,90 $ |
| MA100 | 77,16 $ |
| MA200 | 82,29 $ |
| Pendenza MA50 20g | +3,01% |
| Pendenza MA200 60g | -17,16% |
| Bollinger width | 7,51% |
| Bollinger position | 0.67 |

### DOGE

- Prezzo: **0.06933 $**
- Score classico: **-6 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 2,47%; distanza supporto 1,52%; distanza resistenza 2,57%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; medie daily allineate ribassiste; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **0** — RSI neutrale 44.0; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale -0.02; volume ratio 0.60
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **-1** — Bearish engulfing
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 44.02 |
| MACD histogram | 0.00023 |
| CMF20 | -0.022 |
| Volume ratio 20 | 0.60 |
| MA20 | 0.07016 $ |
| MA50 | 0.07211 $ |
| MA100 | 0.08383 $ |
| MA200 | 0.09072 $ |
| Pendenza MA50 20g | -7,04% |
| Pendenza MA200 60g | -16,94% |
| Bollinger width | 5,73% |
| Bollinger position | 0.31 |

## Come leggere lo score

- **+8 a +12**: conferma tecnica rialzista forte.
- **+5 a +7**: setup costruttivo, ma può mancare ancora una rottura pulita.
- **+2 a +4**: setup anticipato, interessante ma non confermato.
- **-1 a +1**: neutrale / misto.
- **-4 a -2**: debole / non confermato.
- **-8 o meno**: conferma tecnica ribassista.

Nota: questo modulo deve pesare poco nel Global finché non viene verificato dalla calibrazione. La funzione principale è evitare di confondere un contesto interessante con una conferma vera.
<!-- CLASSIC_TECHNICAL_CONFIRMATION_END -->

</details>
<!-- COMPACT_SECTION_END:classic_technical -->

<!-- COMPACT_SECTION_START:classic_visual -->
<details>
<summary><strong>🖼️ Grafici e pattern Classic Visual</strong></summary>

<!-- CLASSIC_TECHNICAL_VISUAL_START -->
# Classic technical visual report

Generato: 2026-08-14 10:53 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [classic_technical_visual_report.md](classic_technical_visual_report.md)

Questo report crea grafici visivi dei pattern tecnici principali. Serve per vedere il grafico e il ciclo di vita dei pattern; non aggiunge automaticamente punteggio al Global.

Regola anti-pattern-zombie: dopo il breakout un pattern passa da ATTIVO a CONFERMATO RECENTE, poi a MATURO. Quando raggiunge il target o viene invalidato vale 0 e non resta confermato per sempre.

Pattern controllati:

- doppio minimo
- doppio massimo
- testa e spalle
- testa e spalle inverso
- triangolo / compressione
- candela giornaliera principale
- pivot high / pivot low
- supporto, resistenza, breakout e breakdown 60 giorni
- data breakout, età, target teorico, progresso e invalidazione
- livelli Fibonacci 23,6 / 38,2 / 50 / 61,8 / 78,6 letti dal Technical Structure

## Sintesi visiva

| Asset | Prezzo | Pattern principale | Stato | Famiglia | Breakout | Target | Progresso | Distanza neckline | Fibonacci | Stato prezzo | Supporto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.760 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 49.952 $ | n/a | 8,68% | Fib 38,2% TENUTO (+1) @ 62.478 $ | NEL RANGE | 62.553 $ |
| SOL | 75,37 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 51,22 $ | n/a | 17,00% | Fib 23,6% NON ATTIVO (0) @ 73,56 $ | NEL RANGE | 73,40 $ |
| DOGE | 0.06933 $ | Doppio minimo | CANDIDATO | rialzista | n/a | 0.07931 $ | n/a | 6,45% | Fib 23,6% NON ATTIVO (0) @ 0.08013 $ | NEL RANGE | 0.06835 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **5 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **49.952 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **8,68%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 38,2% TENUTO (+1) @ 62.478 $** — Swing UP 2026-07-01 57.748 -> 2026-08-09 65.402; livello più vicino 38.2% a 62.478; stato TENUTO; confluenza: supporto tecnico.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **62.553 $**
- Resistenza: **65.402 $**
- Breakout 60g: **67.248 $**
- Breakdown 60g: **57.748 $**
- RSI14: **41.48**
- ATR14: **1,71%**
- Volume ratio 20g: **0.96**
- Rendimento 30g: **-3,02%**
- Rendimento 90g: **-19,67%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 0,86% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 5 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 66.910 $ | n/a | n/a | 71.619 $ | n/a | 6,61% | 65.572 $ | Due minimi simili a 62.201 $ e 62.227 $. Neckline circa 66.910 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 11 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **5 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **64,42 $**
- Target teorico: **51,22 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **17,00%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 73,56 $** — Swing UP 2026-06-06 60,41 -> 2026-08-09 77,62; livello più vicino 23.6% a 73,56; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **65,71 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Bearish engulfing**
- Stato prezzo: **NEL RANGE**
- Supporto: **73,40 $**
- Resistenza: **75,94 $**
- Breakout 60g: **83,81 $**
- Breakdown 60g: **63,16 $**
- RSI14: **51.15**
- ATR14: **2,40%**
- Volume ratio 20g: **0.80**
- Rendimento 30g: **-2,45%**
- Rendimento 90g: **-12,90%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 6,61% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 5 giorni. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 78,73 $ | n/a | n/a | 86,76 $ | n/a | 4,45% | 77,15 $ | Due minimi simili a 73,40 $ e 70,69 $. Neckline circa 78,73 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 13 giorni. |
| Testa e spalle inverso | CANDIDATO | 0 | rialzista | 79,35 $ | n/a | n/a | 94,28 $ | n/a | 5,28% | 77,76 $ | Spalla sinistra 67,92 $, testa 64,42 $, spalla destra 73,40 $. Neckline circa 79,35 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 28 giorni. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-24 -> 2026-08-06**
- Età formazione: **8 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.07380 $**
- Target teorico: **0.07931 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **6,45%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08013 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-08-06 0.06835; livello più vicino 23.6% a 0.08013; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.07233 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-06. Neckline stimata: 0.07380. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Bearish engulfing**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.06835 $**
- Resistenza: **0.07117 $**
- Breakout 60g: **0.09169 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **43.84**
- ATR14: **2,47%**
- Volume ratio 20g: **0.60**
- Rendimento 30g: **-6,37%**
- Rendimento 90g: **-36,61%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 51g | 0.06035 $ | 49,40% | n/a | 0.07966 $ | Due massimi simili a 0.09584 $ e 0.09169 $. Neckline circa 0.07809 $. Breakout neckline: 2026-06-24 (51 giorni fa). Stato: MATURO. Target teorico: 0.06035 $; progresso: 49,40%; prezzo sotto neckline. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.07380 $ | n/a | n/a | 0.07931 $ | n/a | 6,45% | 0.07233 $ | Due minimi simili a 0.06829 $ e 0.06835 $. Neckline circa 0.07380 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 8 giorni. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |

## Stati del ciclo di vita

- **CANDIDATO**: geometria presente, ma neckline non ancora rotta; score 0.
- **ATTIVO**: breakout avvenuto da 0 a 3 giorni; score prudente ±1.
- **CONFERMATO RECENTE**: breakout da 4 a 14 giorni; score ±2.
- **MATURO**: breakout più vecchio di 14 giorni e ancora valido; score ridotto ±1.
- **TARGET RAGGIUNTO**: movimento teorico già completato; score 0.
- **INVALIDATO**: due chiusure consecutive oltre la soglia opposta; score 0.

## Come leggerlo

- Il grafico in alto mostra prezzo, MA20, MA50, MA200, supporti, resistenze, neckline, target, invalidazione e livelli Fibonacci.
- Il pannello centrale mostra RSI14.
- Il pannello basso mostra volume e media volume 20 giorni.
- Un pattern CANDIDATO non è un segnale operativo: il progresso target resta n/a e viene mostrata soltanto la distanza dalla neckline.
- TARGET RAGGIUNTO e INVALIDATO restano visibili per memoria storica, ma valgono 0.
- Il pattern principale usa come fonte autorevole il lifecycle di technical_structure_metrics.csv; il detector visuale resta di supporto grafico.
- Fibonacci non crea un segnale autonomo: pesa al massimo ±1 nel Technical Structure solo con una confluenza indipendente.

Nota: questi pattern sono riconosciuti con regole algoritmiche semplici. Sono utili per visualizzare il grafico, ma vanno sempre controllati a occhio.
<!-- CLASSIC_TECHNICAL_VISUAL_END -->

</details>
<!-- COMPACT_SECTION_END:classic_visual -->

<!-- COMPACT_SECTION_START:fractal_path -->
<details>
<summary><strong>🛤️ Tracking percorso frattale SOL/BTC</strong></summary>

<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-14 10:52 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-14**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-29**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,37 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+57,44%**
- Aderenza live principale: **+69,23%**
- Errore medio live principale: **15,39%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **69**
- Osservazioni inclusive dal bottom: **70**
- Osservazioni da inizio programma/scanner: **43**
- Errore assoluto medio dal bottom: **11,78%**
- Errore assoluto medio da inizio programma: **15,39%**
- Gap firmato medio ultimi 7 giorni: **-16,51%**
- Errore assoluto medio ultimi 7 giorni: **16,51%**
- Gap ultimo giorno: **-19,52%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-19,52%**
- Gap firmato medio 7g: **-16,51%**
- Errore assoluto medio 7g: **16,51%**
- Variazione recente gap: **-3,50%**
- Stato gap: **DISALLINEATO SOTTO IL FRATTALE**
- Trend gap: **SOL si sta allontanando sotto il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 60 | 2026-08-05 | 2023-01-20 | 73,96 $ | 89,33 $ | -17,20% | da inizio programma |
| 61 | 2026-08-06 | 2023-01-21 | 72,58 $ | 89,73 $ | -19,11% | da inizio programma |
| 62 | 2026-08-07 | 2023-01-22 | 73,64 $ | 89,50 $ | -17,72% | da inizio programma |
| 63 | 2026-08-08 | 2023-01-23 | 75,97 $ | 90,34 $ | -15,91% | da inizio programma |
| 64 | 2026-08-09 | 2023-01-24 | 76,21 $ | 89,17 $ | -14,53% | da inizio programma |
| 65 | 2026-08-10 | 2023-01-25 | 75,95 $ | 91,07 $ | -16,60% | da inizio programma |
| 66 | 2026-08-11 | 2023-01-26 | 76,20 $ | 90,73 $ | -16,02% | da inizio programma |
| 67 | 2026-08-12 | 2023-01-27 | 75,53 $ | 90,91 $ | -16,93% | da inizio programma |
| 68 | 2026-08-13 | 2023-01-28 | 76,18 $ | 90,72 $ | -16,03% | da inizio programma |
| 69 | 2026-08-14 | 2023-01-29 | 75,37 $ | 93,65 $ | -19,52% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-21 | 90,43 $ | 72,77 $ | 72,41 $ / 75,37 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-28 | 85,83 $ | 69,07 $ | 68,64 $ / 75,37 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-04 | 95,83 $ | 77,12 $ | 68,64 $ / 78,12 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-11 | 92,81 $ | 74,69 $ | 68,64 $ / 78,71 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-18 | 88,38 $ | 71,12 $ | 68,64 $ / 78,71 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-25 | 87,31 $ | 70,26 $ | 64,00 $ / 78,71 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-02 | 110,45 $ | 88,89 $ | 64,00 $ / 88,89 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-09 | 110,28 $ | 88,75 $ | 64,00 $ / 89,82 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-16 | 111,08 $ | 89,40 $ | 64,00 $ / 90,28 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-23 | 111,61 $ | 89,82 $ | 64,00 $ / 90,28 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-30 | 119,42 $ | 96,11 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-06 | 108,69 $ | 87,47 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-13 | 115,30 $ | 92,79 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-20 | 112,09 $ | 90,21 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-27 | 106,09 $ | 85,38 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-04 | 105,39 $ | 84,81 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-11 | 110,64 $ | 89,04 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-18 | 106,83 $ | 85,97 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 31 | 41,94% | 7,44% | 13,50% |
| 14g | 24 | 29,17% | 16,82% | 12,76% |
| 21g | 17 | 17,65% | 26,43% | 15,19% |
| 28g | 10 | 30,00% | 29,04% | 16,66% |
| 35g | 3 | 0,00% | 29,53% | 19,52% |
| 42g | 0 | n/a | n/a | n/a |
| 49g | 0 | n/a | n/a | n/a |
| 56g | 0 | n/a | n/a | n/a |
| 63g | 0 | n/a | n/a | n/a |
| 70g | 0 | n/a | n/a | n/a |
| 77g | 0 | n/a | n/a | n/a |
| 84g | 0 | n/a | n/a | n/a |
| 91g | 0 | n/a | n/a | n/a |
| 98g | 0 | n/a | n/a | n/a |
| 105g | 0 | n/a | n/a | n/a |
| 112g | 0 | n/a | n/a | n/a |
| 119g | 0 | n/a | n/a | n/a |
| 126g | 0 | n/a | n/a | n/a |

## Regola di lettura

- La somiglianza strutturale descrive la forma.
- Il gap ancorato descrive la distanza reale dal percorso.
- Lo scenario riancorato non dimostra che il frattale sia valido.
- Prima di pesare il modulo servono milestone maturate e un errore ancorato accettabile.
<!-- FRACTAL_PATH_TRACKER_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-08-14 10:53 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.903 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0092% | +7,44% | 2,18 | -1,76% | 0 $ | 0 $ |
| SOL | 75,51 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0066% | +1,63% | 2,59 | -3,11% | 0 $ | 0 $ |
| DOGE | 0.06947 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0099% | +2,93% | 1,19 | +3,02% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | -0,0006% | 148,24 mln $ | 0,72 | -7,73% |
| BTC | Bitget | OK | +0,0100% | 2,54 mld $ | 1,76 | +32,69% |
| BTC | Kucoin | OK | +0,0100% | 1,48 mld $ | 2,45 | -1,65% |
| SOL | Kraken | OK | -0,0038% | 21,60 mln $ | 1,90 | -8,67% |
| SOL | Bitget | OK | +0,0100% | 349,37 mln $ | 19,67 | -17,53% |
| SOL | Kucoin | OK | +0,0100% | 275,29 mln $ | 5,24 | +1,10% |
| DOGE | Kraken | OK | +0,0180% | 3,86 mln $ | 0,94 | +19,65% |
| DOGE | Bitget | OK | +0,0100% | 95,12 mln $ | 0,40 | +11,58% |
| DOGE | Kucoin | OK | +0,0100% | 130,93 mln $ | 1,86 | +11,04% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+0,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +100,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **-1,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione ancora neutrale nei dati exchange.
- **Fibonacci:** Fibonacci tenuto; nessuna conferma exchange netta. Confluenza tecnica dichiarata: supporto tecnico.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +0,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 2, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Markdown non pienamente confermato: compare assorbimento compratore.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+2,38**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 3, accuratezza +66,67%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 2, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Supporto vicino con assorbimento/acquisti: tenuta più credibile.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +72,50% | +8,71% | 0 | n/a | RACCOLTA DATI | 0,00 | +72,50% | +8,71% |
| SOL | +75,00% | +5,21% | 0 | n/a | RACCOLTA DATI | 0,00 | +75,00% | +5,21% |
| DOGE | +70,00% | +13,37% | 0 | n/a | RACCOLTA DATI | 0,00 | +70,00% | +13,37% |

## Dati salvati

- `exchange_market_data_snapshot.json`: fotografia derivata Kraken + Bitget + KuCoin, con OKX e Coinbase ausiliari.
- `exchange_market_data_intraday.csv`: memoria operativa mobile degli ultimi 180 giorni, ripristinata da due copie ridondanti su GitHub Releases.
- `exchange_intraday_YYYY-MM.csv.gz`: archivio mensile permanente dei dati intraday, creato dopo la chiusura del mese.
- `exchange_microstructure_metrics.csv`: score e conferme correnti lette dal Global.
- `exchange_microstructure_history.csv`: prima fotografia giornaliera congelata, usata per valutare le previsioni.
- `exchange_signal_tracker_metrics.csv`: accuratezza a 1/3/7/14/30 giorni.
- `exchange_prediction_overlay.csv`: confronto scanner grezzo vs overlay calibrato.

## Regole di prudenza

- Un muro dell'order book può essere cancellato: non è un supporto garantito.
- Funding, OI e flusso misurano pressione/affollamento, non direzione certa.
- OI in aumento conta soltanto insieme alla direzione del prezzo e al taker flow.
- La componente liquidazioni resta neutrale finché non esiste un feed pubblico completo e verificato.
- Prima dei 30 controlli a 7g il modulo non pesa nel Global; prima dei 30 controlli a 30g l'overlay non altera le previsioni.

Salute fonti: **OK** — coppie exchange/asset disponibili: 9/9. Kraken OK; Bitget OK; KuCoin OK.
Fonti ausiliarie non pesate: OKX OK; Coinbase PARZIALE. Copertura ausiliaria: 3/6.
Storage persistente: **OK** — ultimo asset: exchange_state_B.tar.gz.
<!-- EXCHANGE_MICROSTRUCTURE_END -->

</details>
<!-- COMPACT_SECTION_END:exchange_microstructure -->

<!-- COMPACT_SECTION_START:exchange_signal_tracker -->
<details>
<summary><strong>🧠 Accuratezza segnali exchange</strong></summary>

<!-- EXCHANGE_SIGNAL_TRACKER_START -->
# Accuratezza dati exchange e microstruttura

Generato: 2026-08-14 10:53 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **39**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-14 | BTC | 62.903,40 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 2,18 | +7,44% | -1,76% |
| 2026-08-14 | DOGE | 0.06947 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,19 | +2,93% | +3,02% |
| 2026-08-14 | SOL | 75,51 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 2,59 | +1,63% | -3,11% |
| 2026-08-11 | BTC | 64.025,10 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,94 | +4,21% | -7,22% |
| 2026-08-11 | DOGE | 0.07002 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,86 | +1,22% | +10,68% |
| 2026-08-11 | SOL | 76,02 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,13 | +0,02% | +4,16% |
| 2026-08-10 | BTC | 65.017,50 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,64 | +1,08% | -4,44% |
| 2026-08-10 | DOGE | 0.06975 | V2.1.3 | OK | 0 | 0 | 2,62 | MEDIA | 1,96 | +1,46% | +15,23% |
| 2026-08-10 | SOL | 76,63 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,26 | -0,14% | -8,62% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 2 | +50,00% | +0,20% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 3g | 2 | +0,00% | -1,86% | -2,68% | +1,44% | FEEDBACK RAPIDO |
| SOL | 7g | 1 | +0,00% | -6,27% | -6,64% | +0,73% | FEEDBACK RAPIDO |
| SOL | 14g | 1 | +0,00% | -5,72% | -9,55% | +0,73% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 4 | +50,00% | +1,05% | +0,76% | +2,03% | FEEDBACK RAPIDO |
| DOGE | 3g | 4 | +50,00% | +1,09% | -0,86% | +4,99% | FEEDBACK RAPIDO |
| DOGE | 7g | 3 | +66,67% | +0,53% | -0,69% | +6,15% | FEEDBACK RAPIDO |
| DOGE | 14g | 2 | +50,00% | +0,35% | -1,97% | +6,44% | FEEDBACK RAPIDO |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
<!-- EXCHANGE_SIGNAL_TRACKER_END -->

</details>
<!-- COMPACT_SECTION_END:exchange_signal_tracker -->

<!-- COMPACT_SECTION_START:liquidations -->
<details>
<summary><strong>💥 Futures e liquidazioni</strong></summary>

<!-- LIQUIDATION_SUMMARY_START -->

---

# Sintesi semplice futures / liquidazioni

Report separato completo: [liquidation_report.md](liquidation_report.md)

**BTC** — BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**SOL** — SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**DOGE** — DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.760 $ | +0.0100% | -10.14% | 1.26 | Rischio sotto | 2/5 |
| SOL | 75,37 $ | +0.0037% | +0.55% | 2.45 | Misto | 1/5 |
| DOGE | 0.06933 $ | +0.0100% | -14.42% | 3.32 | Rischio sotto | 2/5 |

## Come usarla insieme al frattale

- Frattale ribassista + futures con rischio sotto = prudenza alta.
- Frattale rialzista + futures con rischio sopra = segnale più interessante.
- Frattale e futures opposti = situazione sporca, meglio non forzare.
- Per posizioni a leva, il futures report serve soprattutto a capire se può arrivare una pulizia violenta prima dei 30 giorni.

<!-- LIQUIDATION_SUMMARY_END -->

</details>
<!-- COMPACT_SECTION_END:liquidations -->

<!-- RSI_MULTI_TIMEFRAME_DIVERGENCE_START -->
# Divergenze RSI multi-timeframe — diagnostica

Generato: 2026-08-14 10:53 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                                                | Stato D       | Weekly              | Stato W    | Lettura weekly                                                                                                                |   Peso |
|:--------|:-----------------------------------------------------|:--------------|:--------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish                                       | IN_FORMAZIONE | Bullish regolare    | CONFERMATA | Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| SOL     | Conferma rialzista                                   | CONTESTO      | Hidden bearish      | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.   |      0 |
| DOGE    | Momentum in miglioramento, divergenza non confermata | CONTESTO      | Conferma ribassista | CONTESTO   | Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.                     |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                                                 | Stato         | Prezzo / RSI      | Pivot confrontati                                                 | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:-----------------------------------------------------|:--------------|:------------------|:------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish                                       | IN_FORMAZIONE | 62.761 $ / 41,48  | 2026-08-03 62.227 $ / RSI 47,40 → 2026-08-14 62.691 $ / RSI 41,48 | n/a                 | n/a              |      0 |
| BTC     | 1W   | Bullish regolare                                     | CONFERMATA    | 62.761 $ / 38,75  | 2026-06-07 59.109 $ / RSI 34,23 → 2026-07-05 57.748 $ / RSI 38,20 | n/a                 | n/a              |      0 |
| SOL     | 1D   | Conferma rialzista                                   | CONTESTO      | 75,44 $ / 51,43   | n/a                                                               | +3,64%              | 9,53             |      0 |
| SOL     | 1W   | Hidden bearish                                       | CONFERMATA    | 75,44 $ / 40,24   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25   | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Momentum in miglioramento, divergenza non confermata | CONTESTO      | 0.06940 $ / 44,05 | n/a                                                               | -0,17%              | 5,16             |      0 |
| DOGE    | 1W   | Conferma ribassista                                  | CONTESTO      | 0.06940 $ / 32,52 | n/a                                                               | -10,72%             | -2,61            |      0 |

### BTC

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### SOL

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Momentum in miglioramento, divergenza non confermata / CONTESTO**: Momentum in miglioramento, divergenza non confermata. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **7**.
- Soglie di lettura: **30 / 60 / 100 controlli**.
- Anche oltre le soglie il peso resta **0** finché non viene presa una decisione esplicita.

| Asset   | TF   | Tipo             |   Orizzonte |   Controlli | Accuratezza   | Return corretto   | Stato         |   Peso |
|:--------|:-----|:-----------------|------------:|------------:|:--------------|:------------------|:--------------|-------:|
| BTC     | 1D   | Hidden bearish   |          30 |           1 | 0,00%         | -1,37%            | RACCOLTA DATI |      0 |
| BTC     | 1W   | Bullish regolare |          30 |           1 | +100,00%      | +1,03%            | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          30 |           1 | +100,00%      | +4,98%            | RACCOLTA DATI |      0 |
| SOL     | 1W   | Hidden bearish   |          30 |           1 | +100,00%      | +1,11%            | RACCOLTA DATI |      0 |

## Regole di prudenza

- Una divergenza **in formazione** può scomparire prima che il pivot sia confermato.
- Una divergenza weekly può anticipare il prezzo di diverse settimane.
- Prezzo in calo e RSI in calo non è bullish divergence: è conferma ribassista.
- Le divergenze restano dentro la famiglia tecnica e non vengono sommate come prova indipendente.
- Nessuna statistica di questo modulo autorizza automaticamente il trading reale.
<!-- RSI_MULTI_TIMEFRAME_DIVERGENCE_END -->

<!-- COMPACT_SECTION_START:technical_structure -->
<details>
<summary><strong>🧱 Struttura tecnica completa e Fibonacci</strong></summary>

<!-- TECHNICAL_STRUCTURE_START -->
# Report struttura tecnica

Generato: 2026-08-14 10:53 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [technical_structure_report.md](technical_structure_report.md)

Questo report aggiunge al tuo scanner una lettura classica di analisi tecnica.

Moduli inclusi:

- Struttura trend con MA20 / MA50 / MA200
- Massimi e minimi crescenti oppure decrescenti
- Doppio minimo, triplo minimo, doppio massimo, triplo massimo
- Pattern Adam and Eve Bottom / Top
- Ciclo di vita pattern: candidato, attivo, confermato recente, maturo, target raggiunto, invalidato
- Data breakout, età, target teorico, progresso e recupero della neckline
- Divergenze RSI e divergenze RSI nascoste
- Momentum MACD
- Conferma volume con OBV / CMF
- Candidato fase Wyckoff
- Fibonacci automatico su swing pivot, con lifecycle e confluenza
- Punteggio tecnico di confluenza

Regola anti-pattern-zombie: un pattern vecchio non resta indefinitamente confermato. Dopo il target vale 0; se viene recuperata stabilmente la neckline viene invalidato; se resta valido ma invecchia passa a MATURO con peso ridotto.

## Sintesi

| Asset   | Prezzo   |   Punteggio | Verdetto         | Trend            | Momentum                  | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista         | Pattern ribassista           | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:------------------------------------------------------|----------------:|:---------------|:--------------------------|:-----------------------------|:-----------|:-------------|
| BTC | 62.760 $ | -6 | DEBOLE | Trend ribassista | Momentum debole | Compressione / triangolo | 0 | +1 / TENUTO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 62.227 | 65.402 |
| SOL | 75,37 $ | -3 | DEBOLE | Trend misto | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | 0 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 70,69 | 77,62 |
| DOGE | 0.06933 $ | 0 | NEUTRALE / MISTO | Trend ribassista | Momentum in miglioramento | Compressione / triangolo | 0 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Adam and Eve Top / CANDIDATO | 0.06835 | 0.07117 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom                 | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | ASSENTE | ASSENTE | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 41.48 | -151.867 | 63.933 | 63.446 | 69.501 | 0,29% | -10,20% | -1,61% | -18,95% |
| SOL | 51.15 | 0.2796 | 74,47 | 75,90 | 82,29 | 2,61% | -16,90% | 0,13% | -11,51% |
| DOGE | 43.84 | 0.00023 | 0.07016 | 0.07211 | 0.09072 | -6,84% | -16,70% | -4,16% | -36,26% |

## Dettaglio asset

### BTC

- Prezzo: **62.760 $**
- Punteggio tecnico: **-6 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 5.775e+04 -> 6.223e+04. Ultimi massimi: 6.691e+04 -> 6.54e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 41.5.
- Fibonacci automatico: **TENUTO** (+1)
  - Swing UP 2026-07-01 57.748 -> 2026-08-09 65.402; livello più vicino 38.2% a 62.478; stato TENUTO; confluenza: supporto tecnico.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **62.227**
- Resistenza più vicina: **65.402**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 62.201 tra 2026-06-18 e 2026-08-03. Neckline stimata: 66.910. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 11 giorni.
  - neckline 66.910; target 71.619; distanza dalla neckline 6,61%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-03-29 al 2026-08-03. Neckline stimata: 82.792. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 11 giorni.
  - neckline 82.792; target 103.383; distanza dalla neckline 31,92%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 59.109 dal 2026-06-05 al 2026-08-03. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 11 giorni.
  - neckline 67.248; target 75.387; distanza dalla neckline 7,15%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 8,68%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 8,68%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 24 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 8,68%; prezzo sopra neckline.

### SOL

- Prezzo: **75,37 $**
- Punteggio tecnico: **-3 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 73.4 -> 70.69. Ultimi massimi: 78.73 -> 77.62.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markdown / fase ribassista** (-2)
  - Dettaglio Wyckoff: Prezzo sotto MA200 con trend a 90 giorni ancora debole.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing UP 2026-06-06 60,41 -> 2026-08-09 77,62; livello più vicino 23.6% a 73,56; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **70,69**
- Resistenza più vicina: **77,62**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 67,92 tra 2026-06-19 e 2026-08-01. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 11,20%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 67,92 dal 2026-06-19 al 2026-08-01. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 11,20%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 11,20%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 17,00%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 6,61%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 77,62 dal 2026-06-15 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 17,00%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.06933 $**
- Punteggio tecnico: **0 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 0.06797 -> 0.06835. Ultimi massimi: 0.0738 -> 0.07117.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 43.8.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-08-06 0.06835; livello più vicino 23.6% a 0.08013; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Adam and Eve Top (CANDIDATO, 0).
- Supporto più vicino: **0.06835**
- Resistenza più vicina: **0.07117**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-06. Neckline stimata: 0.07380. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 0.07380; target 0.07931; distanza dalla neckline 6,45%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 0.06829 dal 2026-06-30 al 2026-08-06. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 0.07923; target 0.09017; distanza dalla neckline 14,29%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06835 dal 2026-06-30 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 0.07923; target 0.09012; distanza dalla neckline 14,29%; prezzo sotto neckline.
- Doppio massimo: **ASSENTE** (0)
- Triplo massimo: **ASSENTE** (0)
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-07-26. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06829. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 19 giorni.
  - neckline 0.06829; target 0.05735; distanza dalla neckline 1,52%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-08-09 | 63.595 | 62.478 | 61.575 | 60.672 | 59.386 | 38.2% / 62.478 | TENUTO | supporto tecnico | +1 |
| SOL | UP 2026-06-06 -> 2026-08-09 | 73,56 | 71,05 | 69,02 | 66,99 | 64,10 | 23.6% / 73,56 | NON ATTIVO | nessuna confluenza indipendente | 0 |
| DOGE | DOWN 2026-05-14 -> 2026-08-06 | 0.08013 | 0.08741 | 0.09330 | 0.09919 | 0.10758 | 23.6% / 0.08013 | NON ATTIVO | nessuna confluenza indipendente | 0 |

## Stati del ciclo di vita

- **CANDIDATO**: geometria presente, ma neckline non ancora rotta; punteggio 0.
- **ATTIVO**: breakout avvenuto da 0 a 3 giorni; peso prudente ±1.
- **CONFERMATO RECENTE**: breakout da 4 a 14 giorni; peso massimo prudente ±2.
- **MATURO**: breakout più vecchio di 14 giorni e ancora valido; peso ridotto ±1.
- **TARGET RAGGIUNTO**: movimento teorico già sviluppato; punteggio 0.
- **INVALIDATO**: recupero stabile della neckline contro il pattern; punteggio 0.

Per evitare doppio conteggio, nel punteggio entra soltanto il miglior pattern rialzista e il miglior pattern ribassista. Doppio, triplo e Adam/Eve che descrivono la stessa struttura non vengono più sommati tutti insieme.

## Come leggere il punteggio

- Da +7 a +12: forte confluenza tecnica rialzista.
- Da +3 a +6: struttura costruttiva, ma serve ancora conferma.
- Da -2 a +2: situazione mista / neutrale.
- Da -6 a -3: struttura tecnica debole.
- Da -12 a -7: forte confluenza tecnica ribassista.

Nota importante: questo report non è una previsione da solo. È un filtro tecnico da leggere insieme a scanner frattale, market regime, futures e RSI.
<!-- TECHNICAL_STRUCTURE_END -->

</details>
<!-- COMPACT_SECTION_END:technical_structure -->

<!-- COMPACT_SECTION_START:calibration_readable -->
<details>
<summary><strong>🎯 Stato leggibile accuratezza / calibrazione</strong></summary>

<!-- CALIBRATION_READABLE_START -->

---

# Stato leggibile accuratezza / calibrazione

Report dettagliati:
- [accuracy_report.md](accuracy_report.md)
- [calibration_report.md](calibration_report.md)

## Riassunto semplice

- **BTC**: 13/30 previsioni controllate su 41 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 13/30 previsioni controllate su 41 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 13/30 previsioni controllate su 41 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 41 | 13 | 13/30 [████░░░░░░] | 28 | RACCOLTA DATI | 2026-08-15 / tra 1 giorno |
| SOL | 41 | 13 | 13/30 [████░░░░░░] | 28 | RACCOLTA DATI | 2026-08-15 / tra 1 giorno |
| DOGE | 41 | 13 | 13/30 [████░░░░░░] | 28 | RACCOLTA DATI | 2026-08-15 / tra 1 giorno |

## Traduzione

- **0/30** significa: lo scanner sta ancora raccogliendo dati.
- **30/30** significa: la calibrazione comincia ad attivarsi.
- **60+** significa: la calibrazione diventa più solida.
- L'email non c'entra con la calibrazione: conta solo che il workflow giri e salvi il diario delle previsioni.

<!-- CALIBRATION_READABLE_END -->

</details>
<!-- COMPACT_SECTION_END:calibration_readable -->

<!-- COMPACT_SECTION_START:data_quality -->
<details>
<summary><strong>✅ Controllo qualità e coerenza dati</strong></summary>

<!-- DATA_QUALITY_COHERENCE_START -->
# Data quality / coherence check

Generato: 2026-08-14 10:53 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 2 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 62.760 $          | 62.760 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.06933 $         | 0.06933 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 75,37 $           | 75,37 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 62.760 $          | 62.760 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 75,37 $           | 75,37 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.06933 $         | 0.06933 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 62.760 $          | 62.760 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 75,37 $           | 75,37 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.06933 $         | 0.06933 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 62.760 $          | 62.760 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 75,37 $           | 75,37 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.06933 $         | 0.06933 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 62.760 $          | 62.760 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 75,37 $           | 75,37 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.06933 $         | 0.06933 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | WARN    | 62.760 $          | 62.903 $        | +0,2281%     |
| Exchange Microstructure | SOL     | price             | OK      | 75,37 $           | 75,51 $         | +0,1844%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.06933 $         | 0.06947 $       | +0,2019%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 75,37 $           | 75,37 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 75,37 $           | 75,37 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 75,37 $           | 75,37 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 75,37 $           | 75,37 $         | +0,0000%     |

## Integrità Technical / Classic Visual

- Fibonacci strutturato: **OK**
- Candidati senza falso progresso target: **OK**
- Classic Visual allineato al lifecycle Technical: **OK**

## Controllo codifica UTF-8

Nessun indicatore comune di mojibake trovato.

## File strutturati

- Snapshot condiviso completo: **OK**
- Scanner summary: **OK**
- Price coherence sync: **OK**
- Dati exchange / microstruttura: **OK**

Il workflow può continuare, ma gli avvisi sopra vanno verificati.
<!-- DATA_QUALITY_COHERENCE_END -->

</details>
<!-- COMPACT_SECTION_END:data_quality -->
