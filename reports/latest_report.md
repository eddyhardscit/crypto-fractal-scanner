<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-08-22 05:32 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +5 | BULLISH | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | +3 | NEUTRALE / COSTRUTTIVO | HOLD / TRANCHE PICCOLE, NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +6 | NEUTRALE / COSTRUTTIVO | SOLO TRANCHE PICCOLE / NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+5**, spot = **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+3**, spot = **HOLD / TRANCHE PICCOLE, NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+6**, spot = **SOLO TRANCHE PICCOLE / NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+5**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**
- Long leva: **LONG PRUDENTE**
- Short leva: **NO SHORT**
- Rischio: **MEDIO**
- Conferme: Prima resistenza sopra 77.991; conferma del doppio minimo sopra 66.910.
- Invalidazioni: Sotto 62.488 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+3**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / TRANCHE PICCOLE, NO LEVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 98,27; milestone analogiche 102,22 / 117,24, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 89,01 / 74,20 / 62,19.

### DOGE

- Global Confluence: **+6**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **SOLO TRANCHE PICCOLE / NO LEVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.09169 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.06895 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 111,46 $; upside verso EMA200 +19,27%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-08-22T05:32:55+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-22T05:05:28+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-22T05:05:28+00:00 | 2026-08-22T05:05:28+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-22T04:45:00+00:00 | 2026-08-22T04:45:00+00:00 | 6,0 min | 25,0 min | OK |
| 60m | 12 | 2026-08-22T04:00:00+00:00 | 2026-08-22T04:00:00+00:00 | 6,0 min | 45,0 min | OK |
| 240m | 12 | 2026-08-22T00:00:00+00:00 | 2026-08-22T00:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Balanced V3 Long Only V1 | PEPE | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Balanced V3 Long Only V1 | ENA | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend Side Regime Guard V1 | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend Side Regime Guard V1 | XRP | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Side Regime Guard V1 | SOL | 60m | LONG | 6,05 | 5,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Doge Bollinger 1H | DOGE | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Sol Bollinger 1H | SOL | 60m | LONG | 6,05 | 5,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Partial 1R V1 | XRP | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Partial 1R V1 | SOL | 60m | LONG | 6,05 | 5,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Long Only V1 | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Long Only V1 | SOL | 60m | LONG | 6,05 | 5,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Quality7 V1 | SUI | 60m | LONG | 7,75 | 7,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Mfe Trail | SUI | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Mfe Trail | SOL | 60m | LONG | 6,05 | 5,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive | SUI | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive | SOL | 60m | LONG | 6,05 | 5,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Scanner | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Scanner | PEPE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | SOL | 60m | LONG | 6,05 | 5,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | DOGE | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard V1 | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard V1 | DOGE | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Mfe V1 | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Mfe V1 | PEPE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 + forza BTC 1H | PEPE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | PEPE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | PEPE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | PEPE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 Long 1H | ZEC | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top 5 Long 1H | PEPE | 60m | LONG | 6,25 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark trend following EMA 1H | XRP | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Donchian 1H Gb20 120R V1 | DOGE | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Donchian breakout 1H | DOGE | 60m | LONG | 5,75 | 5,00 | 0,00 | OPENED | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 75 · prudente · 5x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 80 · prudente · 5x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 85 · prudente · 5x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 75 · €50 · 15x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | XRP | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | SUI | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | SUI | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | PEPE | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | ENA | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | XRP | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | SUI | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | SUI | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | XRP | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | SUI | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | XRP | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | SUI | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | SOL | 60m | LONG | 6,05 | 4,50 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | ADA | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Cost Aware V1 | SOL | 60m | LONG | 6,05 | 6,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Cost Aware V1 | ENA | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V3 Filtered | PEPE | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V3 Filtered | ENA | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 6,0 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ADA | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | ENA | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 5,94 | 6,00 | 0,06 | STALE_CANDLE | 1,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | LINK | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 2,75 | 6,00 | 3,25 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 66.0 minuti; tolleranza 60 minuti. |
| Scalp RSI Short 75 · €10 · 15x | DOGE | 15m | SHORT | 10,00 | 8,00 | 0,00 | READY | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scalp RSI Short 75 · €50 · 15x | DOGE | 15m | SHORT | 10,00 | 8,00 | 0,00 | READY | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scalp RSI Short 75 · prudente · 5x | DOGE | 15m | SHORT | 10,00 | 8,00 | 0,00 | READY | 6,0 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scalp RSI Short 85 · €10 · 15x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 80 · €10 · 15x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 75 · €10 · 15x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 85 · €50 · 15x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scalp RSI Short 80 · €50 · 15x | SOL | 15m | SHORT | 10,00 | 8,00 | 0,00 | OPENED | 6,0 min | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.908,56 | -0,91% | €160,22 | €3.000,00 | 5,34% | 6 | 49 | 38,78% | 0,90 | 6,39% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 49 | 2013 | PRIME INDICAZIONI | 100 (mancano 51) |

- Trade del Principale 4H chiusi: **49**; win rate **38,78%**; profit factor **0,90**.
- Expectancy: **€-2,83** per trade; P&L netto: **€-138,62**; max drawdown: **6,39%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.908,56 | €797,60 | €2.392,80 | €196,89 | €48,36 |
| TEST | Benchmark Donchian breakout 1H | 5 | €11.938,79 | €3.442,55 | €6.885,10 | €121,81 | €127,12 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 7 | €11.698,39 | €2.056,29 | €6.168,86 | €176,27 | €57,51 |
| TEST | Combo Trend Side Regime Guard V1 | 6 | €11.696,40 | €2.573,40 | €5.146,79 | €119,09 | €140,94 |
| TEST | Donchian 1H Gb20 120R V1 | 5 | €11.657,70 | €3.361,50 | €6.722,99 | €118,95 | €124,13 |
| TEST | Scanner Top 5 Long 1H | 5 | €11.401,55 | €1.535,12 | €3.070,24 | €158,04 | €105,62 |
| TEST | 1H Fast No Pepe V1 | 7 | €11.389,39 | €1.950,66 | €5.851,99 | €227,79 | €-3,01 |
| TEST | Combo Adaptive Long Only V1 | 8 | €11.141,94 | €2.858,38 | €5.716,77 | €169,02 | €94,80 |
| TEST | Combo Adaptive Side Regime Guard V1 | 5 | €11.077,72 | €2.927,88 | €5.855,76 | €113,41 | €155,49 |
| TEST | Combo Adaptive | 8 | €11.053,36 | €2.515,55 | €5.031,11 | €111,99 | €127,51 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €10.821,44 | €1.848,77 | €5.546,30 | €216,43 | €-2,54 |
| TEST | Main Side Regime Guard V1 | 2 | €10.791,89 | €288,21 | €864,64 | €103,76 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 6 | €10.751,91 | €1.836,89 | €5.510,67 | €215,04 | €-2,52 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 6 | €10.687,48 | €1.597,92 | €4.793,76 | €213,75 | €-2,70 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.678,54 | €1.500,41 | €3.000,83 | €109,12 | €170,53 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €10.671,88 | €626,24 | €1.252,48 | €52,96 | €107,48 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €10.665,63 | €625,87 | €1.251,75 | €52,93 | €107,42 |
| TEST | 1H Fast V3 No Esports V1 | 6 | €10.536,56 | €1.728,02 | €5.184,06 | €210,40 | €-2,75 |
| TEST | 1H Fast Tp2 V1 | 7 | €10.535,62 | €1.737,71 | €5.213,12 | €164,04 | €44,48 |
| TEST | Scanner Top10 Long | 6 | €10.519,56 | €2.040,96 | €4.081,91 | €157,68 | €73,68 |
| TEST | Combo Adaptive Partial 1R V1 | 6 | €10.437,24 | €2.450,79 | €4.901,58 | €205,04 | €36,96 |
| TEST | Ampia 4H | 6 | €10.397,69 | €1.333,22 | €2.666,45 | €98,36 | €182,72 |
| TEST | Rapida 1H V2 | 2 | €10.397,11 | €894,86 | €2.684,59 | €101,20 | €7,69 |
| TEST | Scanner Top15 Long | 7 | €10.375,67 | €2.024,39 | €4.048,77 | €155,33 | €71,22 |
| TEST | Scanner Top20 Long | 7 | €10.375,67 | €2.024,39 | €4.048,77 | €155,33 | €71,22 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €10.339,88 | €1.420,78 | €4.262,34 | €157,25 | €30,58 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.271,77 | €569,88 | €1.139,76 | €0,00 | €68,06 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 5 | €10.245,16 | €1.439,52 | €2.879,04 | €104,69 | €163,61 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.233,65 | €520,73 | €1.041,47 | €0,00 | €62,19 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.213,35 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.156,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 0 | €10.140,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.126,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 6 | €10.125,27 | €1.407,79 | €2.815,58 | €194,35 | €11,43 |
| TEST | Combo Adaptive Quality7 V1 | 6 | €10.117,63 | €2.182,80 | €4.365,60 | €101,70 | €137,46 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €10.098,77 | €560,28 | €1.120,56 | €0,00 | €66,91 |
| TEST | Btc Adaptive 1H | 0 | €10.083,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.070,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €10.067,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 4 | €10.062,05 | €1.238,28 | €2.476,56 | €49,90 | €92,78 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 1 | €10.040,56 | €201,73 | €403,45 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €10.039,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.029,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 0 | €10.028,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €10.019,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.018,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.013,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 5 | €10.010,60 | €1.406,56 | €2.813,13 | €102,30 | €159,86 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 1 | €10.002,76 | €50,00 | €750,00 | €28,50 | €-0,15 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 1 | €10.000,55 | €10,00 | €150,00 | €5,70 | €-0,03 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 1 | €9.995,13 | €10,00 | €150,00 | €5,70 | €-0,03 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 1 | €9.994,64 | €10,00 | €150,00 | €5,70 | €-0,03 |
| TEST | 1H Fast V3 Long Only V1 | 6 | €9.993,87 | €1.885,78 | €5.657,34 | €151,31 | €49,14 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.987,23 | €689,68 | €2.069,03 | €0,00 | €46,69 |
| TEST | Sol Bollinger 4H | 0 | €9.981,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 1 | €9.979,50 | €52,53 | €262,67 | €9,98 | €-0,05 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 1 | €9.975,65 | €50,00 | €750,00 | €28,50 | €-0,15 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 1 | €9.973,19 | €50,00 | €750,00 | €28,50 | €-0,15 |
| TEST | Doge Bollinger 1H | 1 | €9.972,13 | €452,53 | €1.357,60 | €49,87 | €-0,27 |
| TEST | Eth Adaptive 1H | 1 | €9.971,41 | €646,30 | €1.938,91 | €49,87 | €-1,78 |
| TEST | Btc Donchian 4H | 0 | €9.965,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.964,20 | €495,92 | €991,85 | €49,81 | €2,05 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 1 | €9.940,59 | €52,33 | €261,65 | €9,94 | €-0,05 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 1 | €9.927,80 | €52,26 | €261,31 | €9,93 | €-0,05 |
| TEST | Eth Ema 1H | 1 | €9.918,45 | €642,87 | €1.928,61 | €49,61 | €-1,77 |
| TEST | Combo Adaptive Quality7 Regime V1 | 1 | €9.914,27 | €199,19 | €398,38 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.911,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 6 | €9.908,51 | €1.447,06 | €4.341,18 | €196,00 | €9,08 |
| TEST | Sol Adaptive 1H | 0 | €9.896,74 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 6 | €9.889,79 | €1.375,05 | €2.750,10 | €189,83 | €11,16 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.886,53 | €202,91 | €405,83 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 1 | €9.884,75 | €727,11 | €2.181,32 | €49,48 | €-10,34 |
| TEST | Combo Adaptive Mfe Trail | 6 | €9.850,81 | €2.520,33 | €5.040,66 | €98,08 | €138,40 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 6 | €9.821,93 | €2.387,82 | €4.775,65 | €51,78 | €142,93 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.801,38 | €603,90 | €1.811,71 | €49,01 | €-0,36 |
| TEST | 1H Balanced V3 Long Only V1 | 5 | €9.779,87 | €1.343,83 | €4.031,50 | €148,74 | €28,92 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 0 | €9.779,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 4 | €9.741,78 | €1.174,69 | €3.524,08 | €52,02 | €79,39 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.711,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 1 | €9.642,81 | €755,04 | €2.265,13 | €48,17 | €9,83 |
| TEST | Global Confluence puro 1H | 0 | €9.628,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.626,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 1 | €9.595,22 | €199,19 | €398,38 | €47,81 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.517,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 8 | €9.469,38 | €2.020,42 | €4.040,84 | €92,88 | €82,81 |
| TEST | 1H Fast V3 Nohigh V1 | 0 | €9.435,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 1 | €9.430,59 | €195,77 | €391,54 | €46,99 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.389,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 3 | €9.385,05 | €1.090,11 | €2.180,22 | €97,35 | €0,00 |
| TEST | Scanner Bottom15 Short | 3 | €9.385,05 | €1.090,11 | €2.180,22 | €97,35 | €0,00 |
| TEST | Scanner Bottom20 Short | 3 | €9.385,05 | €1.090,11 | €2.180,22 | €97,35 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.378,18 | €34,77 | €69,54 | €8,34 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 0 | €9.372,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 0 | €9.370,91 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 0 | €9.362,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 0 | €9.355,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €9.354,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 0 | €9.326,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 3 | €9.320,02 | €1.082,57 | €2.165,15 | €96,67 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.319,82 | €197,50 | €395,01 | €47,40 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 3 | €9.305,85 | €1.080,93 | €2.161,86 | €96,53 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 1 | €9.252,08 | €195,70 | €391,41 | €45,67 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 0 | €9.237,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.234,23 | €1.072,61 | €2.145,22 | €95,79 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 0 | €9.202,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 0 | €9.150,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €9.114,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 0 | €9.056,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 0 | €8.796,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €8.740,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V1 | 0 | €8.445,51 | €0,00 | €0,00 | €0,00 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.908,56 | €-138,62 | 49 | 49 | 38,78% | 0,90 | €-2,83 | 6,39% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.938,79 | €1.814,87 | 89 | 89 | 53,93% | 2,04 | €20,39 | 3,63% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.698,39 | €1.644,58 | 119 | 119 | 58,82% | 1,74 | €13,82 | 4,41% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.696,40 | €1.558,76 | 90 | 90 | 61,11% | 2,14 | €17,32 | 4,33% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.657,70 | €1.536,70 | 57 | 57 | 56,14% | 2,75 | €26,96 | 3,63% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.401,55 | €1.297,78 | 120 | 120 | 51,67% | 1,57 | €10,81 | 8,85% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €11.389,39 | €1.395,91 | 176 | 176 | 52,84% | 1,49 | €7,93 | 4,46% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €11.141,94 | €1.050,57 | 97 | 97 | 53,61% | 1,58 | €10,83 | 6,25% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €11.077,72 | €925,75 | 98 | 98 | 52,04% | 1,57 | €9,45 | 8,68% |
| TEST | Combo Adaptive | Combo Adaptive | €11.053,36 | €928,87 | 129 | 129 | 48,06% | 1,47 | €7,20 | 7,91% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.821,44 | €827,31 | 160 | 160 | 53,75% | 1,32 | €5,17 | 9,50% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.791,89 | €792,57 | 33 | 33 | 54,55% | 2,27 | €24,02 | 2,40% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.751,91 | €757,74 | 204 | 204 | 46,57% | 1,21 | €3,71 | 9,48% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.687,48 | €693,06 | 117 | 117 | 48,72% | 1,31 | €5,92 | 10,60% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.678,54 | €509,85 | 107 | 107 | 47,66% | 1,23 | €4,76 | 11,27% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.671,88 | €565,19 | 87 | 87 | 45,98% | 1,29 | €6,50 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.665,63 | €559,01 | 91 | 91 | 46,15% | 1,28 | €6,14 | 12,06% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €10.536,56 | €542,42 | 175 | 175 | 47,43% | 1,17 | €3,10 | 9,00% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.535,62 | €494,26 | 187 | 187 | 41,71% | 1,15 | €2,64 | 6,56% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.519,56 | €448,33 | 102 | 102 | 51,96% | 1,25 | €4,40 | 10,31% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.437,24 | €403,22 | 128 | 128 | 47,66% | 1,19 | €3,15 | 8,69% |
| TEST | Ampia 4H | Confluenza trend | €10.397,69 | €216,96 | 48 | 48 | 31,25% | 1,19 | €4,52 | 4,45% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.397,11 | €391,03 | 41 | 36 | 51,22% | 1,43 | €9,54 | 3,89% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.375,67 | €306,88 | 102 | 102 | 51,96% | 1,17 | €3,01 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.375,67 | €306,88 | 102 | 102 | 51,96% | 1,17 | €3,01 | 10,31% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.339,88 | €311,86 | 139 | 139 | 45,32% | 1,11 | €2,24 | 9,12% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.271,77 | €204,39 | 5 | 5 | 60,00% | 2,93 | €40,88 | 1,05% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Combo Scanner | Combo Scanner | €10.245,16 | €83,32 | 111 | 111 | 46,85% | 1,03 | €0,75 | 11,38% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.233,65 | €172,08 | 5 | 5 | 60,00% | 2,63 | €34,42 | 1,01% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.213,35 | €213,35 | 12 | 12 | 41,67% | 1,74 | €17,78 | 1,54% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.156,88 | €156,88 | 12 | 12 | 50,00% | 1,63 | €13,07 | 2,77% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.140,84 | €140,84 | 63 | 63 | 44,44% | 1,10 | €2,24 | 5,24% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.126,53 | €126,53 | 40 | 40 | 45,00% | 1,13 | €3,16 | 3,73% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €10.125,27 | €115,64 | 87 | 87 | 42,53% | 1,06 | €1,33 | 7,34% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €10.117,63 | €-17,21 | 67 | 67 | 43,28% | 0,99 | €-0,26 | 8,88% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Ema 4H | Trend following EMA | €10.098,77 | €32,52 | 6 | 6 | 33,33% | 1,16 | €5,42 | 2,27% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.083,25 | €83,25 | 6 | 6 | 66,67% | 1,77 | €13,88 | 1,13% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.070,19 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.067,96 | €67,96 | 8 | 8 | 62,50% | 1,41 | €8,50 | 1,49% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.062,05 | €-29,24 | 96 | 91 | 42,71% | 0,99 | €-0,30 | 10,88% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €10.040,56 | €40,78 | 34 | 34 | 50,00% | 1,05 | €1,20 | 4,21% |
| TEST | Sol Ema 1H | Trend following EMA | €10.039,53 | €39,53 | 13 | 13 | 38,46% | 1,10 | €3,04 | 3,33% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.029,45 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,82% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.028,66 | €28,66 | 122 | 122 | 43,44% | 1,01 | €0,23 | 7,10% |
| TEST | Btc Ema 4H | Trend following EMA | €10.019,41 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Doge Ema 1H | Trend following EMA | €10.018,06 | €18,06 | 15 | 15 | 60,00% | 1,05 | €1,20 | 2,77% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.013,82 | €13,82 | 41 | 41 | 48,78% | 1,01 | €0,34 | 4,50% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €10.010,60 | €-147,53 | 99 | 99 | 46,46% | 0,93 | €-1,49 | 12,28% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.002,76 | €3,36 | 27 | 27 | 44,44% | 1,03 | €0,12 | 0,33% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.000,55 | €0,67 | 27 | 27 | 44,44% | 1,03 | €0,02 | 0,07% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €9.995,13 | €-4,75 | 4 | 4 | 50,00% | 0,09 | €-1,19 | 0,06% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,64 | €-5,24 | 14 | 14 | 35,71% | 0,47 | €-0,37 | 0,11% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.993,87 | €-51,88 | 133 | 133 | 42,11% | 0,98 | €-0,39 | 12,52% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Btc Ema 1H | Trend following EMA | €9.987,23 | €-57,80 | 10 | 10 | 40,00% | 0,82 | €-5,78 | 1,94% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.981,72 | €-18,28 | 3 | 3 | 33,33% | 0,83 | €-6,09 | 1,22% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.979,50 | €-20,29 | 4 | 4 | 50,00% | 0,08 | €-5,07 | 0,30% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €9.975,65 | €-23,75 | 4 | 4 | 50,00% | 0,09 | €-5,94 | 0,31% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,19 | €-26,21 | 14 | 14 | 35,71% | 0,47 | €-1,87 | 0,53% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.972,13 | €-26,79 | 8 | 8 | 50,00% | 0,89 | €-3,35 | 1,89% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.971,41 | €-25,65 | 11 | 11 | 45,45% | 0,92 | €-2,33 | 3,14% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.965,81 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Eth Ema 4H | Trend following EMA | €9.964,20 | €-37,26 | 4 | 4 | 25,00% | 0,76 | €-9,32 | 1,83% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.940,59 | €-59,20 | 14 | 14 | 35,71% | 0,32 | €-4,23 | 0,89% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.927,80 | €-71,99 | 27 | 27 | 44,44% | 0,52 | €-2,67 | 0,84% |
| TEST | Eth Ema 1H | Trend following EMA | €9.918,45 | €-78,62 | 15 | 15 | 40,00% | 0,84 | €-5,24 | 4,80% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.914,27 | €-85,51 | 34 | 34 | 44,12% | 0,90 | €-2,52 | 5,41% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.911,95 | €-88,05 | 12 | 12 | 50,00% | 0,75 | €-7,34 | 3,08% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.908,51 | €-97,90 | 84 | 84 | 48,81% | 0,95 | €-1,17 | 9,26% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.896,74 | €-103,26 | 14 | 14 | 35,71% | 0,77 | €-7,38 | 4,59% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.889,79 | €-119,62 | 104 | 104 | 43,27% | 0,95 | €-1,15 | 8,78% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.886,53 | €-113,24 | 48 | 48 | 47,92% | 0,91 | €-2,36 | 5,38% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.884,75 | €-103,61 | 10 | 10 | 30,00% | 0,73 | €-10,36 | 2,63% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.850,81 | €-284,57 | 138 | 138 | 44,20% | 0,89 | €-2,06 | 15,45% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Combo Trend | Combo Trend | €9.821,93 | €-317,97 | 142 | 142 | 40,14% | 0,90 | €-2,24 | 10,85% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.801,38 | €-197,17 | 9 | 9 | 33,33% | 0,51 | €-21,91 | 2,37% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.779,87 | €-246,63 | 95 | 95 | 46,32% | 0,86 | €-2,60 | 8,85% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.779,10 | €-220,90 | 86 | 86 | 41,86% | 0,88 | €-2,57 | 7,10% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.741,78 | €-335,22 | 92 | 85 | 44,57% | 0,83 | €-3,64 | 8,84% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.711,41 | €-288,59 | 13 | 13 | 23,08% | 0,41 | €-22,20 | 4,35% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.642,81 | €-365,67 | 6 | 6 | 16,67% | 0,04 | €-60,94 | 4,16% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.628,04 | €-371,96 | 16 | 16 | 25,00% | 0,32 | €-23,25 | 3,92% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.626,87 | €-373,13 | 130 | 130 | 41,54% | 0,89 | €-2,87 | 10,36% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.595,22 | €-404,43 | 58 | 58 | 39,66% | 0,78 | €-6,97 | 7,74% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.517,55 | €-482,45 | 78 | 78 | 39,74% | 0,78 | €-6,19 | 6,59% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.469,38 | €-610,71 | 110 | 110 | 38,18% | 0,72 | €-5,55 | 12,31% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.435,38 | €-564,62 | 112 | 112 | 40,18% | 0,79 | €-5,04 | 6,91% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.430,59 | €-569,07 | 73 | 73 | 39,73% | 0,73 | €-7,80 | 7,02% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.389,68 | €-610,32 | 83 | 83 | 44,58% | 0,76 | €-7,35 | 7,69% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.385,05 | €-613,68 | 67 | 67 | 32,84% | 0,67 | €-9,16 | 8,28% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.385,05 | €-613,68 | 67 | 67 | 32,84% | 0,67 | €-9,16 | 8,28% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.385,05 | €-613,68 | 67 | 67 | 32,84% | 0,67 | €-9,16 | 8,28% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.378,18 | €-621,78 | 51 | 51 | 31,37% | 0,66 | €-12,19 | 8,18% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.372,49 | €-627,51 | 55 | 55 | 29,09% | 0,62 | €-11,41 | 8,39% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.370,91 | €-629,09 | 88 | 88 | 43,18% | 0,78 | €-7,15 | 10,68% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.362,52 | €-637,48 | 50 | 50 | 34,00% | 0,60 | €-12,75 | 7,98% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.355,17 | €-644,83 | 126 | 126 | 38,10% | 0,80 | €-5,12 | 11,75% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.354,60 | €-645,40 | 58 | 58 | 34,48% | 0,67 | €-11,13 | 7,26% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.326,30 | €-673,70 | 52 | 52 | 32,69% | 0,62 | €-12,96 | 7,80% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.320,02 | €-678,72 | 58 | 58 | 32,76% | 0,60 | €-11,70 | 8,30% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.319,82 | €-679,95 | 61 | 61 | 34,43% | 0,66 | €-11,15 | 7,96% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.305,85 | €-692,90 | 59 | 59 | 32,20% | 0,58 | €-11,74 | 8,30% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.252,08 | €-747,69 | 42 | 42 | 23,81% | 0,53 | €-17,80 | 11,41% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.237,05 | €-762,95 | 59 | 59 | 33,90% | 0,57 | €-12,93 | 11,72% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.234,23 | €-764,52 | 86 | 86 | 32,56% | 0,66 | €-8,89 | 9,40% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.202,39 | €-797,61 | 87 | 87 | 48,28% | 0,60 | €-9,17 | 9,02% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.150,69 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 13,99% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.114,32 | €-885,68 | 38 | 38 | 36,84% | 0,48 | €-23,31 | 10,65% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.056,84 | €-943,16 | 53 | 53 | 28,30% | 0,59 | €-17,80 | 11,51% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.796,64 | €-1.203,36 | 75 | 75 | 29,33% | 0,38 | €-16,04 | 12,67% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.740,52 | €-1.259,48 | 81 | 81 | 38,27% | 0,55 | €-15,55 | 14,60% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.445,51 | €-1.554,49 | 105 | 105 | 27,62% | 0,47 | €-14,80 | 17,39% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | HYPE | LONG | Confluenza trend | 240m | 3,0x | 76,47929 | 81,62700 | 71,48477 | 51,36859 | 86,46833 | €10,44 | €31,32 | €2,05 | €2,11 |
| Principale 4H | ETH | LONG | Confluenza trend | 240m | 3,0x | 2509,93189 | 2515,13000 | 2395,33490 | 1685,83758 | 2739,12586 | €19,82 | €59,45 | €2,71 | €0,12 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,56312 | 1,67216 | 1,44655 | 1,04990 | 1,79626 | €220,42 | €661,27 | €49,31 | €46,13 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | LINK | LONG | Confluenza trend | 60m | 3,0x | 12,23945 | 12,46900 | 11,85665 | 8,22083 | 13,00504 | €43,30 | €129,89 | €4,06 | €2,44 |
| 1H Balanced Long No Rhv V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 81,25625 | 81,62700 | 78,03969 | 54,57711 | 87,68937 | €416,12 | €1.248,35 | €49,42 | €5,70 |
| 1H Balanced Long No Rhv V1 | SUI | LONG | Confluenza trend | 60m | 3,0x | 0,91318 | 0,93920 | 0,91318 | 0,61335 | 0,98923 | €11,03 | €33,10 | €0,00 | €0,94 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | ETH | LONG | Confluenza trend V2 | 60m | 3,0x | 2424,26476 | 2515,13000 | 2481,29397 | 1628,29783 | 2536,04729 | €690,68 | €2.072,04 | €0,00 | €77,66 |
| Bilanciata 1H V2 | LINK | LONG | Confluenza trend V2 | 60m | 3,0x | 12,04941 | 12,46900 | 12,15501 | 8,09319 | 12,82965 | €9,69 | €29,06 | €0,00 | €1,01 |
| Bilanciata 1H V2 | HYPE | LONG | Confluenza trend V2 | 60m | 3,0x | 81,25625 | 81,62700 | 78,03969 | 54,57711 | 87,68937 | €51,94 | €155,82 | €6,17 | €0,71 |
| Bilanciata 1H V3 Filtered | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €137,63 | €412,88 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | LINK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 12,23945 | 12,46900 | 11,85665 | 8,22083 | 13,00504 | €546,46 | €1.639,38 | €51,27 | €30,75 |
| Bilanciata 1H V3 Filtered | ENA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,16026 | 0,16023 | 0,14912 | 0,10764 | 0,18254 | €247,96 | €743,89 | €51,70 | €-0,15 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €28,31 | €84,92 | €5,38 | €-0,02 |
| 1H Fast Score 6 75 Cost Aware V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €624,93 | €1.874,80 | €51,62 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | LINK | LONG | Momentum / breakout | 60m | 3,0x | 12,16543 | 12,46900 | 12,20252 | 8,17112 | 12,62042 | €771,34 | €2.314,02 | €0,00 | €57,74 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16026 | 0,16023 | 0,15160 | 0,10764 | 0,17326 | €360,70 | €1.082,11 | €58,50 | €-0,22 |
| 1H Fast Score 6 75 Cost Aware V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 99,31486 | 99,29500 | 96,80711 | 66,70648 | 103,07649 | €31,62 | €94,86 | €2,40 | €-0,02 |
| 1H Fast No Pepe V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1213,43264 | 1213,43264 | 1179,70743 | 815,02226 | 1264,02045 | €33,31 | €99,94 | €2,78 | €0,00 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 81,73234 | 81,62700 | 79,21443 | 54,89689 | 85,50921 | €608,50 | €1.825,51 | €56,24 | €-2,35 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,93939 | 0,93920 | 0,90768 | 0,63096 | 0,98696 | €562,42 | €1.687,26 | €56,96 | €-0,34 |
| 1H Fast No Pepe V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,25509 | 0,25504 | 0,24572 | 0,17134 | 0,26915 | €516,62 | €1.549,87 | €56,95 | €-0,31 |
| 1H Fast No Pepe V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 99,31486 | 99,29500 | 96,80711 | 66,70648 | 103,07649 | €9,65 | €28,96 | €0,73 | €-0,01 |
| 1H Fast Tp2 V1 | SOXL | SHORT | Momentum / breakout | 60m | 3,0x | 121,01735 | 121,01735 | 127,15573 | 160,75137 | 108,74057 | €315,49 | €946,48 | €48,01 | €-0,00 |
| 1H Fast Tp2 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1204,83092 | 1204,83092 | 1170,97389 | 809,24477 | 1272,54496 | €18,91 | €56,74 | €1,59 | €0,00 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | LINK | LONG | Momentum / breakout | 60m | 3,0x | 12,16543 | 12,46900 | 12,20252 | 8,17112 | 12,77208 | €623,94 | €1.871,81 | €0,00 | €46,71 |
| 1H Fast Tp2 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 81,73234 | 81,62700 | 79,21443 | 54,89689 | 86,76817 | €567,22 | €1.701,67 | €52,42 | €-2,19 |
| 1H Fast Tp2 V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,67249 | 1,67216 | 1,60414 | 1,12336 | 1,80920 | €50,41 | €151,24 | €6,18 | €-0,03 |
| Rapida 1H V2 | SOXL | SHORT | Momentum / breakout V2 | 60m | 3,0x | 121,15726 | 121,15726 | 127,13595 | 160,93723 | 112,18923 | €333,06 | €999,18 | €49,31 | €-0,00 |
| Rapida 1H V2 | HYPE | LONG | Momentum / breakout V2 | 60m | 3,0x | 81,25625 | 81,62700 | 78,75448 | 54,57711 | 85,00890 | €561,80 | €1.685,41 | €51,89 | €7,69 |
| Rapida 1H V3 Filtered | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €21,81 | €65,43 | €1,80 | €0,00 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,73234 | 81,62700 | 79,21443 | 54,89689 | 85,50921 | €578,88 | €1.736,64 | €53,50 | €-2,24 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,67249 | 1,67216 | 1,60414 | 1,12336 | 1,77503 | €438,51 | €1.315,52 | €53,77 | €-0,26 |
| Rapida 1H V3 Filtered | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,93939 | 0,93920 | 0,90768 | 0,63096 | 0,98696 | €35,72 | €107,15 | €3,62 | €-0,02 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | LINK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 12,16543 | 12,46900 | 12,20252 | 8,17112 | 12,62042 | €649,56 | €1.948,68 | €0,00 | €48,63 |
| 1H Fast V3 Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,25625 | 81,62700 | 78,75448 | 54,57711 | 85,00890 | €59,15 | €177,44 | €5,46 | €0,81 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,93939 | 0,93920 | 0,90768 | 0,63096 | 0,98696 | €486,52 | €1.459,56 | €49,27 | €-0,29 |
| 1H Fast V3 No Esports V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €18,11 | €54,34 | €1,50 | €0,00 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,73234 | 81,62700 | 79,21443 | 54,89689 | 85,50921 | €563,48 | €1.690,45 | €52,08 | €-2,18 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,67249 | 1,67216 | 1,60414 | 1,12336 | 1,77503 | €429,77 | €1.289,31 | €52,69 | €-0,26 |
| 1H Fast V3 No Esports V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,93939 | 0,93920 | 0,90768 | 0,63096 | 0,98696 | €520,25 | €1.560,75 | €52,69 | €-0,31 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,73234 | 81,62700 | 79,21443 | 54,89689 | 85,50921 | €560,36 | €1.681,09 | €51,79 | €-2,17 |
| 1H Fast V3 No Esports Long Only V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,93939 | 0,93920 | 0,90768 | 0,63096 | 0,98696 | €527,74 | €1.583,23 | €53,45 | €-0,32 |
| 1H Fast V3 No Esports Long Only V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16026 | 0,16023 | 0,15160 | 0,10764 | 0,17326 | €329,54 | €988,61 | €53,44 | €-0,20 |
| 1H Fast V3 No Esports Long Only V1 | PEPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €37,28 | €111,84 | €5,51 | €-0,02 |
| 1H Fast V3 No Esports Mfe Lock V1 | SKHYNIX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1187,23972 | 820,00702 | 1271,27573 | €21,95 | €65,86 | €1,81 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 81,73234 | 81,62700 | 79,21443 | 54,89689 | 85,50921 | €582,62 | €1.747,87 | €53,85 | €-2,25 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,67249 | 1,67216 | 1,60414 | 1,12336 | 1,77503 | €441,34 | €1.324,02 | €54,11 | €-0,26 |
| 1H Fast V3 No Esports Mfe Lock V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,93939 | 0,93920 | 0,90768 | 0,63096 | 0,98696 | €35,95 | €107,84 | €3,64 | €-0,02 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2258,11153 | 2515,13000 | 2438,47896 | 1140,34632 | 2576,63943 | €502,94 | €1.005,89 | €0,00 | €114,49 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 71,99640 | 81,62700 | 77,25612 | 36,35818 | 87,88866 | €16,69 | €33,38 | €0,00 | €4,47 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 738,20761 | 822,51000 | 764,71329 | 372,79484 | 932,87076 | €274,02 | €548,05 | €0,00 | €62,59 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 12,46900 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €1,18 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | ENA | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,14320 | 0,16023 | 0,15076 | 0,07232 | 0,16554 | €348,56 | €697,12 | €0,00 | €82,91 |
| Forza relativa 1H V2 | LINK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 12,04941 | 12,46900 | 12,13258 | 6,08495 | 12,90767 | €59,04 | €118,08 | €0,00 | €4,11 |
| Forza relativa 1H V2 | HYPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 81,25625 | 81,62700 | 78,03969 | 41,03441 | 88,33268 | €630,31 | €1.260,61 | €49,90 | €5,75 |
| Scalp RSI Short 85 · €10 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 99,27514 | 99,29500 | 103,04694 | 105,39711 | 93,61744 | €10,00 | €150,00 | €5,70 | €-0,03 |
| Scalp RSI Short 80 · €10 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 99,27514 | 99,29500 | 103,04694 | 105,39711 | 93,61744 | €10,00 | €150,00 | €5,70 | €-0,03 |
| Scalp RSI Short 75 · €10 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 99,27514 | 99,29500 | 103,04694 | 105,39711 | 93,61744 | €10,00 | €150,00 | €5,70 | €-0,03 |
| Scalp RSI Short 85 · €50 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 99,27514 | 99,29500 | 103,04694 | 105,39711 | 93,61744 | €50,00 | €750,00 | €28,50 | €-0,15 |
| Scalp RSI Short 80 · €50 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 99,27514 | 99,29500 | 103,04694 | 105,39711 | 93,61744 | €50,00 | €750,00 | €28,50 | €-0,15 |
| Scalp RSI Short 75 · €50 · 15x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 99,27514 | 99,29500 | 103,04694 | 105,39711 | 93,61744 | €50,00 | €750,00 | €28,50 | €-0,15 |
| Scalp RSI Short 85 · prudente · 5x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 99,27514 | 99,29500 | 103,04694 | 118,63379 | 91,73154 | €52,53 | €262,67 | €9,98 | €-0,05 |
| Scalp RSI Short 80 · prudente · 5x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 99,27514 | 99,29500 | 103,04694 | 118,63379 | 91,73154 | €52,33 | €261,65 | €9,94 | €-0,05 |
| Scalp RSI Short 75 · prudente · 5x | SOL | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 99,27514 | 99,29500 | 103,04694 | 118,63379 | 91,73154 | €52,26 | €261,31 | €9,93 | €-0,05 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2527,10532 | 2515,13000 | 2455,44799 | 1276,18819 | 2706,24863 | €1.023,39 | €2.046,77 | €58,04 | €-9,70 |
| Benchmark Donchian breakout 1H | ADA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,24139 | 0,25504 | 0,24541 | 0,12190 | 0,26988 | €624,55 | €1.249,09 | €0,00 | €70,64 |
| Benchmark Donchian breakout 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 96,15423 | 99,29500 | 97,02348 | 48,55788 | 103,02819 | €1.013,85 | €2.027,70 | €0,00 | €66,23 |
| Benchmark Donchian breakout 1H | DOGE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,09885 | 0,09883 | 0,09401 | 0,04992 | 0,11095 | €139,52 | €279,03 | €13,67 | €-0,06 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2527,10532 | 2515,13000 | 2455,44799 | 1276,18819 | 2706,24863 | €999,29 | €1.998,58 | €56,67 | €-9,47 |
| Donchian 1H Gb20 120R V1 | ADA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,24139 | 0,25504 | 0,24541 | 0,12190 | 0,26988 | €609,84 | €1.219,68 | €0,00 | €68,98 |
| Donchian 1H Gb20 120R V1 | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 96,15423 | 99,29500 | 97,02348 | 48,55788 | 103,02819 | €989,98 | €1.979,96 | €0,00 | €64,67 |
| Donchian 1H Gb20 120R V1 | DOGE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,09885 | 0,09883 | 0,09401 | 0,04992 | 0,11095 | €136,23 | €272,46 | €13,34 | €-0,05 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | ETH | LONG | Trend following EMA | 60m | 2,0x | 2396,47920 | 2515,13000 | 2474,82250 | 1210,22200 | 2540,53801 | €28,74 | €57,48 | €0,00 | €2,85 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 76719,31079 | 78450,74000 | 74671,22818 | 38743,25195 | 81225,09269 | €833,14 | €1.666,28 | €44,48 | €37,61 |
| Benchmark trend following EMA 1H | ENA | LONG | Trend following EMA | 60m | 2,0x | 0,14122 | 0,16023 | 0,14959 | 0,07132 | 0,16872 | €12,82 | €25,65 | €0,00 | €3,45 |
| Benchmark trend following EMA 1H | LINK | LONG | Trend following EMA | 60m | 2,0x | 12,11942 | 12,46900 | 12,12605 | 6,12031 | 13,09722 | €12,84 | €25,68 | €0,00 | €0,74 |
| Benchmark trend following EMA 1H | DOGE | LONG | Trend following EMA | 60m | 2,0x | 0,09541 | 0,09883 | 0,09554 | 0,04818 | 0,10474 | €529,56 | €1.059,13 | €0,00 | €37,98 |
| Benchmark trend following EMA 1H | SUI | LONG | Trend following EMA | 60m | 2,0x | 0,92699 | 0,93920 | 0,88400 | 0,46813 | 1,02155 | €13,49 | €26,97 | €1,25 | €0,36 |
| Benchmark trend following EMA 1H | XRP | LONG | Trend following EMA | 60m | 2,0x | 1,67249 | 1,67216 | 1,57484 | 0,84461 | 1,88732 | €403,71 | €807,43 | €47,14 | €-0,16 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | ENA | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,14324 | 0,16023 | 0,15064 | 0,07234 | 0,16528 | €355,74 | €711,48 | €0,00 | €84,40 |
| Scanner Top 5 Long 1H | XRP | LONG | Scanner Top 5 Long | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,71766 | €154,42 | €308,83 | €0,00 | €21,54 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 933,59241 | €422,87 | €845,75 | €57,01 | €-0,17 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €383,86 | €767,72 | €48,65 | €-0,15 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €200,95 | €401,89 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Top10 Long | LINK | LONG | Scanner Top10 Long | 60m | 2,0x | 12,11942 | 12,46900 | 12,14891 | 6,12031 | 12,91944 | €13,86 | €27,72 | €0,00 | €0,80 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 2510,43199 | 2515,13000 | 2447,53198 | 1267,76815 | 2636,23199 | €23,39 | €46,79 | €1,17 | €0,09 |
| Scanner Top10 Long | XRP | LONG | Scanner Top10 Long | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,71766 | €524,07 | €1.048,14 | €0,00 | €73,11 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | ZEC | LONG | Scanner Top10 Long | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 933,59241 | €390,16 | €780,33 | €52,60 | €-0,16 |
| Scanner Top10 Long | PEPE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €411,04 | €822,07 | €52,09 | €-0,16 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top15 Long | BTC | LONG | Scanner Top15 Long | 60m | 2,0x | 76719,31079 | 78450,74000 | 76984,72631 | 38743,25195 | 80405,85934 | €20,59 | €41,19 | €0,00 | €0,93 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 81,73234 | 81,62700 | 78,49502 | 41,27483 | 88,20698 | €646,42 | €1.292,84 | €51,21 | €-1,67 |
| Scanner Top15 Long | XRP | LONG | Scanner Top15 Long | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,71766 | €517,90 | €1.035,79 | €0,00 | €72,25 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | ZEC | LONG | Scanner Top15 Long | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 933,59241 | €384,82 | €769,65 | €51,88 | €-0,15 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €349,33 | €698,65 | €44,27 | €-0,14 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top20 Long | BTC | LONG | Scanner Top20 Long | 60m | 2,0x | 76719,31079 | 78450,74000 | 76984,72631 | 38743,25195 | 80405,85934 | €20,59 | €41,19 | €0,00 | €0,93 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 81,73234 | 81,62700 | 78,49502 | 41,27483 | 88,20698 | €646,42 | €1.292,84 | €51,21 | €-1,67 |
| Scanner Top20 Long | XRP | LONG | Scanner Top20 Long | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,71766 | €517,90 | €1.035,79 | €0,00 | €72,25 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | ZEC | LONG | Scanner Top20 Long | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 933,59241 | €384,82 | €769,65 | €51,88 | €-0,15 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €349,33 | €698,65 | €44,27 | €-0,14 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €204,24 | €408,48 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13881 | 0,16023 | 0,14991 | 0,07010 | 0,16409 | €311,03 | €622,07 | €0,00 | €96,00 |
| Scanner Top 5 + forza BTC 1H | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,73312 | €535,48 | €1.070,95 | €0,00 | €74,71 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 944,68421 | €396,04 | €792,08 | €53,40 | €-0,16 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €54,41 | €108,83 | €6,90 | €-0,02 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13881 | 0,16023 | 0,14991 | 0,07010 | 0,16409 | €291,58 | €583,16 | €0,00 | €90,00 |
| Scanner Top5 Btc Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,73312 | €501,98 | €1.003,96 | €0,00 | €70,03 |
| Scanner Top5 Btc Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 944,68421 | €371,27 | €742,53 | €50,06 | €-0,15 |
| Scanner Top5 Btc Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €51,01 | €102,02 | €6,46 | €-0,02 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €196,77 | €393,54 | €47,23 | €0,00 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14324 | 0,16023 | 0,15064 | 0,07234 | 0,16748 | €13,92 | €27,84 | €0,00 | €3,30 |
| Scanner Top5 Btc Guard V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,73312 | €60,94 | €121,88 | €0,00 | €8,50 |
| Scanner Top5 Btc Guard V1 | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,09885 | 0,09883 | 0,09449 | 0,04992 | 0,10844 | €574,38 | €1.148,75 | €50,63 | €-0,23 |
| Scanner Top5 Btc Guard V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 944,68421 | €364,51 | €729,02 | €49,15 | €-0,15 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €192,20 | €384,39 | €46,13 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,14324 | 0,16023 | 0,15064 | 0,07234 | 0,16748 | €13,59 | €27,19 | €0,00 | €3,23 |
| Scanner Top5 Btc Guard Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,73312 | €59,52 | €119,05 | €0,00 | €8,30 |
| Scanner Top5 Btc Guard Mfe V1 | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,09885 | 0,09883 | 0,09449 | 0,04992 | 0,10844 | €561,02 | €1.122,04 | €49,46 | €-0,22 |
| Scanner Top5 Btc Guard Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 944,68421 | €356,03 | €712,07 | €48,00 | €-0,14 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €199,19 | €398,38 | €47,81 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €195,77 | €391,54 | €46,99 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13881 | 0,16023 | 0,14991 | 0,07010 | 0,17329 | €293,50 | €587,01 | €0,00 | €90,59 |
| Scanner Top5 Btc Runner25 V1 | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,09222 | 0,09883 | 0,09613 | 0,04657 | 0,10194 | €40,59 | €81,17 | €0,00 | €5,82 |
| Scanner Top5 Btc Runner25 V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,86527 | 0,93920 | 0,91071 | 0,43696 | 0,96652 | €63,34 | €126,67 | €0,00 | €10,82 |
| Scanner Top5 Btc Runner25 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 818,21361 | 822,51000 | 764,43439 | 413,19787 | 979,55127 | €17,50 | €35,00 | €2,30 | €0,18 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13881 | 0,16023 | 0,14991 | 0,07010 | 0,17329 | €293,67 | €587,35 | €0,00 | €90,65 |
| Scanner Top5 Btc Tp3 V1 | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,09222 | 0,09883 | 0,09613 | 0,04657 | 0,10194 | €40,61 | €81,22 | €0,00 | €5,82 |
| Scanner Top5 Btc Tp3 V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,86527 | 0,93920 | 0,91071 | 0,43696 | 0,96652 | €63,37 | €126,75 | €0,00 | €10,83 |
| Scanner Top5 Btc Tp3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 818,21361 | 822,51000 | 764,43439 | 413,19787 | 979,55127 | €17,51 | €35,02 | €2,30 | €0,18 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ETH | LONG | Combo Trend | 60m | 2,0x | 2409,96190 | 2515,13000 | 2476,15639 | 1217,03076 | 2551,09900 | €853,83 | €1.707,65 | €0,00 | €74,52 |
| Combo Trend | LINK | LONG | Combo Trend | 60m | 2,0x | 12,23945 | 12,46900 | 11,81412 | 6,18092 | 13,17517 | €38,36 | €76,72 | €2,67 | €1,44 |
| Combo Trend | DOGE | LONG | Combo Trend | 60m | 2,0x | 0,09382 | 0,09883 | 0,09583 | 0,04738 | 0,10217 | €588,05 | €1.176,11 | €0,00 | €62,82 |
| Combo Trend | ENA | LONG | Combo Trend | 60m | 2,0x | 0,15019 | 0,16023 | 0,15131 | 0,07585 | 0,17472 | €33,09 | €66,18 | €0,00 | €4,42 |
| Combo Trend | SOL | LONG | Combo Trend | 60m | 2,0x | 99,31486 | 99,29500 | 95,73235 | 50,15400 | 107,19637 | €680,79 | €1.361,58 | €49,12 | €-0,27 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | ENA | LONG | Combo Scanner | 60m | 2,0x | 0,13881 | 0,16023 | 0,14991 | 0,07010 | 0,16409 | €298,41 | €596,82 | €0,00 | €92,11 |
| Combo Scanner | XRP | LONG | Combo Scanner | 60m | 2,0x | 1,56312 | 1,67216 | 1,60787 | 0,78938 | 1,73312 | €513,74 | €1.027,49 | €0,00 | €71,67 |
| Combo Scanner | ZEC | LONG | Combo Scanner | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 944,68421 | €379,97 | €759,93 | €51,23 | €-0,15 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €52,20 | €104,41 | €6,62 | €-0,02 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | LINK | LONG | Combo Adaptive | 60m | 2,0x | 12,23945 | 12,46900 | 11,85665 | 6,18092 | 13,00504 | €55,31 | €110,62 | €3,46 | €2,07 |
| Combo Adaptive | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2526,20514 | 2515,13000 | 2461,52067 | 1275,73360 | 2655,57408 | €13,07 | €26,15 | €0,67 | €-0,11 |
| Combo Adaptive | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,24533 | 0,25504 | 0,24691 | 0,12389 | 0,26698 | €618,16 | €1.236,31 | €0,00 | €48,94 |
| Combo Adaptive | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,56312 | 1,67216 | 1,61246 | 0,78938 | 1,71766 | €551,63 | €1.103,26 | €0,00 | €76,96 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | SOL | LONG | Combo Adaptive | 60m | 2,0x | 99,31486 | 99,29500 | 96,09061 | 50,15400 | 105,76337 | €851,28 | €1.702,57 | €55,27 | €-0,34 |
| Combo Adaptive | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,93939 | 0,93920 | 0,89861 | 0,47439 | 1,02093 | €17,91 | €35,82 | €1,55 | €-0,01 |
| Combo Adaptive Mfe Trail | LINK | LONG | Combo Adaptive | 60m | 2,0x | 12,23945 | 12,46900 | 12,25413 | 6,18092 | 13,00504 | €65,32 | €130,63 | €0,00 | €2,45 |
| Combo Adaptive Mfe Trail | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09382 | 0,09883 | 0,09783 | 0,04738 | 0,10065 | €637,16 | €1.274,32 | €0,00 | €68,07 |
| Combo Adaptive Mfe Trail | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,56312 | 1,67216 | 1,62966 | 0,78938 | 1,71766 | €490,26 | €980,52 | €0,00 | €68,40 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | SOL | LONG | Combo Adaptive | 60m | 2,0x | 99,31486 | 99,29500 | 96,09061 | 50,15400 | 105,76337 | €758,73 | €1.517,46 | €49,26 | €-0,30 |
| Combo Adaptive Mfe Trail | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,93939 | 0,93920 | 0,89861 | 0,47439 | 1,02093 | €514,57 | €1.029,15 | €44,67 | €-0,21 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 12,16543 | 12,46900 | 12,18031 | 6,14354 | 12,94540 | €13,73 | €27,46 | €0,00 | €0,69 |
| Combo Adaptive Quality7 V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,24139 | 0,25504 | 0,24721 | 0,12190 | 0,26191 | €585,67 | €1.171,34 | €0,00 | €66,24 |
| Combo Adaptive Quality7 V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,56312 | 1,67216 | 1,61246 | 0,78938 | 1,71766 | €505,70 | €1.011,40 | €0,00 | €70,55 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,93939 | 0,93920 | 0,89861 | 0,47439 | 1,02093 | €59,24 | €118,48 | €5,14 | €-0,02 |
| Combo Adaptive Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €202,91 | €405,83 | €0,00 | €-0,00 |
| Combo Adaptive Quality7 Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €199,19 | €398,38 | €0,00 | €-0,00 |
| Combo Adaptive Long Only V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 12,23945 | 12,46900 | 11,85665 | 6,18092 | 13,00504 | €39,66 | €79,32 | €2,48 | €1,49 |
| Combo Adaptive Long Only V1 | DOGE | LONG | Combo Adaptive | 60m | 2,0x | 0,09382 | 0,09883 | 0,09623 | 0,04738 | 0,10065 | €31,85 | €63,70 | €0,00 | €3,40 |
| Combo Adaptive Long Only V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2510,43199 | 2515,13000 | 2447,53198 | 1267,76815 | 2636,23199 | €53,51 | €107,02 | €2,68 | €0,20 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,92699 | 0,93920 | 0,88830 | 0,46813 | 1,00436 | €659,97 | €1.319,94 | €55,08 | €17,39 |
| Combo Adaptive Long Only V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,56312 | 1,67216 | 1,61246 | 0,78938 | 1,71766 | €520,95 | €1.041,89 | €0,00 | €72,68 |
| Combo Adaptive Long Only V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 99,31486 | 99,29500 | 96,09061 | 50,15400 | 105,76337 | €858,11 | €1.716,22 | €55,72 | €-0,34 |
| Combo Adaptive Long Only V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 822,67450 | 822,51000 | 767,21555 | 415,45062 | 933,59241 | €48,86 | €97,72 | €6,59 | €-0,02 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 12,23945 | 12,46900 | 11,85665 | 6,18092 | 13,00504 | €817,60 | €1.635,20 | €51,14 | €30,67 |
| Combo Adaptive Partial 1R V1 | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,91318 | 0,93920 | 0,91318 | 0,46116 | 0,98923 | €44,50 | €89,00 | €0,00 | €2,54 |
| Combo Adaptive Partial 1R V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 818,21361 | 822,51000 | 764,43439 | 413,19787 | 925,77205 | €390,17 | €780,34 | €51,29 | €4,10 |
| Combo Adaptive Partial 1R V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 99,31486 | 99,29500 | 96,09061 | 50,15400 | 105,76337 | €803,84 | €1.607,67 | €52,19 | €-0,32 |
| Combo Adaptive Partial 1R V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,67249 | 1,67216 | 1,58461 | 0,84461 | 1,84826 | €41,98 | €83,96 | €4,41 | €-0,02 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €201,73 | €403,45 | €0,00 | €-0,00 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 76719,31079 | 78450,74000 | 77194,15684 | 51529,80375 | 80405,85934 | €689,68 | €2.069,03 | €0,00 | €46,69 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 93,69974 | 99,29500 | 96,26431 | 47,31837 | 104,18607 | €560,28 | €1.120,56 | €0,00 | €66,91 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 93,69974 | 99,29500 | 96,26431 | 47,31837 | 105,44443 | €569,88 | €1.139,76 | €0,00 | €68,06 |
| Sol Bollinger 1H | SOL | SHORT | Bollinger mean reversion | 60m | 3,0x | 99,27514 | 99,29500 | 101,96094 | 131,87048 | 95,24644 | €603,90 | €1.811,71 | €49,01 | €-0,36 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 93,69974 | 99,29500 | 96,26431 | 47,31837 | 105,13937 | €520,73 | €1.041,47 | €0,00 | €62,19 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2517,44339 | 2515,13000 | 2452,69072 | 1690,88281 | 2646,94876 | €642,87 | €1.928,61 | €49,61 | €-1,77 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2509,93189 | 2515,13000 | 2383,87520 | 1267,51560 | 2825,07361 | €495,92 | €991,85 | €49,81 | €2,05 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 2527,10532 | 2515,13000 | 2469,77945 | 1697,37241 | 2641,75703 | €727,11 | €2.181,32 | €49,48 | €-10,34 |
| Eth Bollinger 1H | ETH | SHORT | Bollinger mean reversion | 60m | 3,0x | 2526,09468 | 2515,13000 | 2579,81618 | 3355,49577 | 2445,51244 | €755,04 | €2.265,13 | €48,17 | €9,83 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 2517,44339 | 2515,13000 | 2452,69072 | 1690,88281 | 2646,94876 | €646,30 | €1.938,91 | €49,87 | €-1,78 |
| Doge Bollinger 1H | DOGE | SHORT | Bollinger mean reversion | 60m | 3,0x | 0,09881 | 0,09883 | 0,10244 | 0,13125 | 0,09337 | €452,53 | €1.357,60 | €49,87 | €-0,27 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 12,23945 | 12,46900 | 11,85665 | 6,18092 | 13,00504 | €838,31 | €1.676,62 | €52,44 | €31,45 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,24533 | 0,25504 | 0,24691 | 0,12389 | 0,26698 | €618,04 | €1.236,07 | €0,00 | €48,93 |
| Combo Adaptive Side Regime Guard V1 | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,56312 | 1,67216 | 1,61246 | 0,78938 | 1,71766 | €540,86 | €1.081,72 | €0,00 | €75,46 |
| Combo Adaptive Side Regime Guard V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 99,31486 | 99,29500 | 96,09061 | 50,15400 | 105,76337 | €853,16 | €1.706,31 | €55,40 | €-0,34 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Combo Trend Side Regime Guard V1 | ETH | LONG | Combo Trend | 60m | 2,0x | 2409,96190 | 2515,13000 | 2476,15639 | 1217,03076 | 2551,09900 | €1.041,25 | €2.082,50 | €0,00 | €90,88 |
| Combo Trend Side Regime Guard V1 | LINK | LONG | Combo Trend | 60m | 2,0x | 12,04941 | 12,46900 | 12,13258 | 6,08495 | 13,00303 | €23,07 | €46,14 | €0,00 | €1,61 |
| Combo Trend Side Regime Guard V1 | SUI | LONG | Combo Trend | 60m | 2,0x | 0,91318 | 0,93920 | 0,87093 | 0,46116 | 1,00613 | €38,14 | €76,28 | €3,53 | €2,17 |
| Combo Trend Side Regime Guard V1 | ADA | LONG | Combo Trend | 60m | 2,0x | 0,24533 | 0,25504 | 0,24566 | 0,12389 | 0,27179 | €589,06 | €1.178,11 | €0,00 | €46,63 |
| Combo Trend Side Regime Guard V1 | XRP | LONG | Combo Trend | 60m | 2,0x | 1,67249 | 1,67216 | 1,57484 | 0,84461 | 1,88732 | €500,88 | €1.001,77 | €58,49 | €-0,20 |
| Combo Trend Side Regime Guard V1 | ZEC | LONG | Combo Trend | 60m | 2,0x | 822,67450 | 822,51000 | 761,05343 | 415,45062 | 958,24084 | €381,00 | €762,00 | €57,08 | €-0,15 |
| 1H Balanced V3 Long Only V1 | BEAT | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,25480 | 0,25480 | 0,25418 | 0,33846 | 0,19365 | €130,17 | €390,52 | €0,00 | €-0,00 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | LINK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 12,23945 | 12,46900 | 11,85665 | 8,22083 | 13,00504 | €516,86 | €1.550,59 | €48,50 | €29,08 |
| 1H Balanced V3 Long Only V1 | ENA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,16026 | 0,16023 | 0,14912 | 0,10764 | 0,18254 | €234,53 | €703,60 | €48,90 | €-0,14 |
| 1H Balanced V3 Long Only V1 | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €26,77 | €80,32 | €5,09 | €-0,02 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,51 | €405,01 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,28257 | 0,25514 | 0,42244 | 0,21475 | €202,81 | €405,63 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sol Ema 1H | SOL | LONG | 2026-08-22T05:07:22+00:00 | 98,56217 | €96,54 | 1,94 | TARGET |
| Sol Donchian 1H | SOL | LONG | 2026-08-22T05:07:22+00:00 | 98,04492 | €97,32 | 1,93 | TARGET |
| Sol Adaptive 1H | SOL | LONG | 2026-08-22T05:07:22+00:00 | 98,56217 | €95,17 | 1,94 | TARGET |
| Scanner Top 5 Long 1H | DOGE | LONG | 2026-08-22T05:07:22+00:00 | 0,09868 | €94,57 | 1,96 | TARGET |
| Scanner Top 5 Long 1H | SUI | LONG | 2026-08-22T05:07:22+00:00 | 0,93258 | €109,06 | 1,96 | TARGET |
| Scanner Top5 Btc Tp3 V1 | PEPE | LONG | 2026-08-22T05:07:22+00:00 | 0,00000 | €151,87 | 2,97 | TARGET |
| Scanner Top5 Btc Tp3 V1 | XRP | LONG | 2026-08-22T05:07:22+00:00 | 1,59503 | €151,15 | 2,96 | TARGET |
| Scanner Top5 Btc Runner25 V1 | XRP | LONG | 2026-08-22T05:07:22+00:00 | 1,59503 | €151,07 | 2,96 | TARGET |
| Scanner Top5 Btc Runner25 V1 | PEPE | LONG | 2026-08-22T05:07:22+00:00 | 0,00000 | €151,78 | 2,97 | TARGET |
| Scanner Top5 Btc Mfe V1 | DOGE | LONG | 2026-08-22T05:07:22+00:00 | 0,09933 | €7,51 | 2,16 | TARGET |
| Scanner Top5 Btc Mfe V1 | SUI | LONG | 2026-08-22T05:07:22+00:00 | 0,93933 | €5,81 | 2,16 | TARGET |
| Scanner Top5 Btc Guard V1 | PEPE | LONG | 2026-08-22T05:07:22+00:00 | 0,00000 | €106,46 | 2,17 | TARGET |

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

Generato: 2026-08-22 05:32 UTC


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

Segnali totali salvati: **129**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-22 | BTC | 77.109,54 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-22 | DOGE | 0.09028 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-22 | SOL | 93,36 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-21 | BTC | 75.089,33 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-21 | DOGE | 0.08259 | +2 | +1 | +1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-21 | SOL | 89,61 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-20 | BTC | 69.558,29 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-20 | DOGE | 0.07454 | +4 | +3 | +3 | 0 | +2 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-20 | SOL | 84,90 | +3 | 0 | 0 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-19 | BTC | 64.293,48 | +5 | +3 | +2 | +2 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-19 | DOGE | 0.06997 | +3 | +4 | +3 | +2 | 0 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-19 | SOL | 76,87 | +2 | +3 | +2 | +2 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 43 | 42 | 41 | 40 | 38 | 36 | 34 | 31 | 24 | 15 | 0 | 0 |
| SOL | 43 | 42 | 41 | 40 | 38 | 36 | 34 | 31 | 24 | 15 | 0 | 0 |
| DOGE | 43 | 42 | 41 | 40 | 38 | 36 | 34 | 31 | 24 | 15 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-09 | 45g | 2026-08-23 | domani |
| SOL | 2026-07-09 | 45g | 2026-08-23 | domani |
| DOGE | 2026-07-09 | 45g | 2026-08-23 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 39 | 53,85% | +0,53% | +0,50% | PRIMA CALIBRAZIONE |
| BTC | 2g | 38 | 52,63% | +0,86% | +0,73% | PRIMA CALIBRAZIONE |
| BTC | 3g | 37 | 45,95% | +0,81% | +0,62% | PRIMA CALIBRAZIONE |
| BTC | 5g | 36 | 36,11% | +1,41% | +1,05% | PRIMA CALIBRAZIONE |
| BTC | 7g | 34 | 44,12% | +1,22% | +0,90% | PRIMA CALIBRAZIONE |
| BTC | 10g | 32 | 43,75% | +0,94% | +0,65% | PRIMA CALIBRAZIONE |
| BTC | 14g | 29 | 51,72% | +1,50% | +1,38% | FEEDBACK RAPIDO |
| BTC | 21g | 22 | 36,36% | +1,71% | +1,41% | FEEDBACK RAPIDO |
| BTC | 30g | 14 | 85,71% | +2,82% | +3,18% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 35 | 57,14% | +0,64% | +0,46% | PRIMA CALIBRAZIONE |
| SOL | 2g | 34 | 50,00% | +1,20% | +0,99% | PRIMA CALIBRAZIONE |
| SOL | 3g | 33 | 51,52% | +1,74% | +1,47% | PRIMA CALIBRAZIONE |
| SOL | 5g | 31 | 54,84% | +1,77% | +1,59% | PRIMA CALIBRAZIONE |
| SOL | 7g | 29 | 58,62% | +1,43% | +1,61% | FEEDBACK RAPIDO |
| SOL | 10g | 27 | 59,26% | +1,08% | +1,36% | FEEDBACK RAPIDO |
| SOL | 14g | 24 | 66,67% | +1,70% | +3,21% | FEEDBACK RAPIDO |
| SOL | 21g | 18 | 55,56% | +1,54% | -0,44% | FEEDBACK RAPIDO |
| SOL | 30g | 14 | 42,86% | +2,59% | +0,37% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 40 | 47,50% | +0,65% | +0,63% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 39 | 48,72% | +1,07% | +1,07% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 38 | 47,37% | +1,14% | +1,44% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 36 | 55,56% | +0,99% | +1,68% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 34 | 61,76% | +0,61% | +1,91% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 32 | 56,25% | -0,43% | +1,51% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 29 | 62,07% | +0,05% | +3,25% | FEEDBACK RAPIDO |
| DOGE | 21g | 23 | 69,57% | -0,47% | +0,53% | FEEDBACK RAPIDO |
| DOGE | 30g | 15 | 80,00% | -0,54% | +0,54% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 39 | 53,85% | +0,53% | +0,50% | +0,13% | +1,10% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 42 | 57,14% | +0,49% | +0,49% | +0,10% | +1,03% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 42 | 57,14% | +0,49% | +0,49% | +0,10% | +1,03% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 37 | 37,84% | +0,68% | +0,13% | +0,27% | +1,23% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 10 | 30,00% | +1,59% | +0,54% | +0,82% | +2,11% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 38 | 52,63% | +0,86% | +0,73% | +0,32% | +1,58% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 41 | 56,10% | +0,98% | +0,98% | +0,45% | +1,69% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 41 | 56,10% | +0,98% | +0,98% | +0,45% | +1,69% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 36 | 41,67% | +1,26% | +0,11% | +0,74% | +1,97% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 9 | 22,22% | +2,05% | +0,36% | +1,71% | +2,86% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 37 | 45,95% | +0,81% | +0,62% | -1,03% | +2,40% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 40 | 57,50% | +1,24% | +1,24% | -1,00% | +2,74% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 40 | 57,50% | +1,24% | +1,24% | -1,00% | +2,74% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 35 | 31,43% | +1,70% | -0,71% | -0,74% | +3,13% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 8 | 12,50% | +2,41% | -2,41% | -0,24% | +3,25% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 36 | 36,11% | +1,41% | +1,05% | -1,88% | +3,42% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 38 | 44,74% | +1,34% | +1,34% | -1,86% | +3,38% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 38 | 44,74% | +1,34% | +1,34% | -1,86% | +3,38% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 47,06% | +1,56% | +1,56% | -1,83% | +3,50% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 33 | 33,33% | +1,71% | -2,28% | -1,62% | +3,78% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 8 | 12,50% | +7,26% | -7,26% | -0,63% | +8,70% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 34 | 44,12% | +1,22% | +0,90% | -2,25% | +3,55% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 36 | 52,78% | +1,12% | +1,12% | -2,24% | +3,50% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 36 | 52,78% | +1,12% | +1,12% | -2,24% | +3,50% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | +1,43% | +1,43% | -2,21% | +3,64% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 31 | 32,26% | +1,66% | -2,15% | -1,99% | +3,88% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 6 | 0,00% | +8,28% | -8,28% | -0,96% | +9,64% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 32 | 43,75% | +0,94% | +0,65% | -2,66% | +3,40% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 34 | 50,00% | +0,75% | +0,75% | -2,68% | +3,36% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 34 | 50,00% | +0,75% | +0,75% | -2,68% | +3,36% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 30 | 56,67% | +1,12% | +1,12% | -2,58% | +3,49% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 29 | 34,48% | +1,07% | +0,49% | -2,43% | +3,73% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,32% | -1,32% | -1,42% | +3,31% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 29 | 51,72% | +1,50% | +1,38% | -2,86% | +4,58% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 31 | 51,61% | +1,30% | +1,30% | -2,88% | +4,45% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 31 | 51,61% | +1,30% | +1,30% | -2,88% | +4,45% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 27 | 59,26% | +1,86% | +1,86% | -2,66% | +4,76% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 26 | 61,54% | +1,80% | +1,74% | -2,58% | +4,99% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 22 | 36,36% | +1,71% | +1,41% | -3,09% | +5,38% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 24 | 50,00% | +1,47% | +1,47% | -3,14% | +5,15% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 24 | 50,00% | +1,47% | +1,47% | -3,14% | +5,15% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 20 | 55,00% | +2,04% | +2,04% | -2,87% | +5,71% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 19 | 21,05% | +1,45% | -1,81% | -2,79% | +5,23% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 3 | 0,00% | +8,03% | -8,03% | -1,93% | +10,14% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 14 | 85,71% | +2,82% | +3,18% | -3,23% | +6,82% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 15 | 66,67% | +2,59% | +2,59% | -3,18% | +6,68% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 15 | 66,67% | +2,59% | +2,59% | -3,18% | +6,68% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 11 | 63,64% | +1,81% | +1,81% | -2,71% | +6,55% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 12 | 41,67% | +1,49% | -1,91% | -2,79% | +6,23% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 40 | 47,50% | +0,65% | +0,63% | +0,15% | +1,63% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 42 | 57,14% | +0,52% | +0,81% | +0,01% | +1,47% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 42 | 57,14% | +0,52% | +0,81% | +0,01% | +1,47% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 35 | 54,29% | +0,45% | +0,69% | -0,08% | +1,36% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 27 | 37,04% | +0,44% | -0,44% | -0,04% | +1,04% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,69% | +3,06% | +2,25% | +3,87% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 39 | 48,72% | +1,07% | +1,07% | +0,41% | +2,39% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 41 | 51,22% | +0,91% | +1,14% | +0,26% | +2,19% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 41 | 51,22% | +0,91% | +1,14% | +0,26% | +2,19% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 34 | 61,76% | +0,35% | +0,89% | -0,23% | +1,57% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 27 | 44,44% | +1,08% | -1,08% | +0,40% | +2,07% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +6,72% | +6,19% | +5,95% | +9,58% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 38 | 47,37% | +1,14% | +1,44% | -1,43% | +3,61% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 40 | 52,50% | +0,98% | +1,29% | -1,54% | +3,39% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 40 | 52,50% | +0,98% | +1,29% | -1,54% | +3,39% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 33 | 48,48% | -0,26% | +0,25% | -1,90% | +1,81% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 27 | 33,33% | +1,97% | -1,97% | -1,30% | +4,60% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,70% | +1,18% | -0,25% | +5,07% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 36 | 55,56% | +0,99% | +1,68% | -2,42% | +4,14% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 38 | 52,63% | +0,83% | +1,50% | -2,49% | +3,92% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 38 | 52,63% | +0,83% | +1,50% | -2,49% | +3,92% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 36 | 52,78% | +0,90% | +1,56% | -2,48% | +3,88% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 33 | 63,64% | +0,95% | +0,56% | -2,69% | +4,03% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 25 | 48,00% | +1,57% | -1,57% | -2,40% | +4,96% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 34 | 61,76% | +0,61% | +1,91% | -2,90% | +4,31% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 36 | 58,33% | +0,45% | +1,64% | -2,99% | +4,13% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 36 | 58,33% | +0,45% | +1,64% | -2,99% | +4,13% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 58,82% | +0,54% | +1,67% | -3,00% | +4,11% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 31 | 64,52% | -0,09% | +1,94% | -3,29% | +3,65% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 23 | 52,17% | -0,04% | +0,04% | -3,05% | +3,58% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,63% | +0,36% | -0,50% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 32 | 56,25% | -0,43% | +1,51% | -3,53% | +3,51% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 34 | 55,88% | -0,51% | +1,35% | -3,58% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 34 | 55,88% | -0,51% | +1,35% | -3,58% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | -0,49% | +1,38% | -3,59% | +3,29% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 30 | 66,67% | -1,40% | +1,40% | -3,88% | +2,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 22 | 59,09% | -1,13% | +1,13% | -3,71% | +2,91% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +0,93% | +0,18% | -1,31% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 29 | 62,07% | +0,05% | +3,25% | -4,33% | +5,08% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 31 | 67,74% | -0,09% | +2,93% | -4,34% | +4,82% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 31 | 67,74% | -0,09% | +2,93% | -4,34% | +4,82% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 29 | 68,97% | +0,01% | +3,02% | -4,38% | +4,84% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 30 | 66,67% | -0,31% | +0,31% | -4,43% | +4,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 21 | 66,67% | -1,05% | +1,05% | -4,58% | +3,86% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +6,85% | -6,24% | -1,27% | +10,97% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 23 | 69,57% | -0,47% | +0,53% | -5,34% | +5,38% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 24 | 79,17% | -0,61% | +4,32% | -5,40% | +5,15% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 24 | 79,17% | -0,61% | +4,32% | -5,40% | +5,15% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 22 | 81,82% | -0,56% | +4,59% | -5,55% | +5,21% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 24 | 79,17% | -0,61% | +0,61% | -5,40% | +5,15% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 20 | 75,00% | +0,03% | -0,03% | -5,18% | +6,01% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 15 | 80,00% | -0,54% | +0,54% | -6,61% | +5,66% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 15 | 80,00% | -0,54% | +0,54% | -6,61% | +5,66% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 15 | 80,00% | -0,54% | +0,54% | -6,61% | +5,66% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 14 | 85,71% | -2,36% | +2,36% | -6,65% | +3,35% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 15 | 80,00% | -0,54% | +0,54% | -6,61% | +5,66% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 14 | 78,57% | -0,15% | +0,15% | -6,50% | +6,03% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 35 | 57,14% | +0,64% | +0,46% | +0,06% | +1,53% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 37 | 59,46% | +0,21% | +0,22% | -0,28% | +1,06% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 40 | 57,50% | +0,28% | +0,12% | -0,23% | +1,12% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 39 | 51,28% | +0,22% | +0,19% | -0,34% | +1,02% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 23 | 52,17% | +0,46% | +0,39% | -0,22% | +1,38% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,51% | +1,51% | +0,99% | +5,02% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 34 | 50,00% | +1,20% | +0,99% | +0,46% | +2,29% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 36 | 52,78% | +0,64% | +0,77% | -0,12% | +1,36% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 39 | 51,28% | +0,62% | +0,69% | -0,11% | +1,47% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 38 | 39,47% | +0,51% | -0,29% | -0,16% | +1,61% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 22 | 50,00% | +0,47% | +0,43% | -0,09% | +1,38% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 33 | 51,52% | +1,74% | +1,47% | -1,33% | +3,70% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 36 | 50,00% | +1,25% | +1,46% | -1,65% | +3,28% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 39 | 48,72% | +1,18% | +1,33% | -1,61% | +3,29% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 37 | 40,54% | +0,73% | -1,05% | -1,85% | +2,61% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 21 | 42,86% | +0,13% | -0,13% | -1,91% | +1,82% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 31 | 54,84% | +1,77% | +1,59% | -2,41% | +4,53% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 34 | 55,88% | +1,40% | +1,60% | -2,68% | +4,10% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 37 | 54,05% | +1,34% | +1,42% | -2,62% | +4,08% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 32 | 53,12% | +1,42% | +1,65% | -2,56% | +4,31% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 36 | 41,67% | +1,34% | -1,80% | -2,69% | +4,21% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 21 | 52,38% | +0,14% | -0,14% | -2,60% | +2,64% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 29 | 58,62% | +1,43% | +1,61% | -2,94% | +4,63% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 32 | 62,50% | +0,96% | +1,68% | -3,21% | +4,24% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 35 | 62,86% | +0,87% | +1,54% | -3,17% | +4,21% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 30 | 56,67% | +1,28% | +1,35% | -3,08% | +4,44% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 34 | 35,29% | +0,94% | -1,54% | -3,25% | +4,35% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 27 | 59,26% | +1,08% | +1,36% | -3,43% | +4,44% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 30 | 63,33% | +0,86% | +1,58% | -3,78% | +4,05% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 33 | 60,61% | +0,76% | +1,45% | -3,75% | +4,04% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 28 | 57,14% | +1,29% | +1,09% | -3,62% | +4,25% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 32 | 46,88% | +0,07% | -0,22% | -3,88% | +3,64% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,08% | +0,08% | -3,74% | +3,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 24 | 66,67% | +1,70% | +3,21% | -4,14% | +6,43% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 27 | 81,48% | +2,03% | +3,41% | -4,32% | +5,99% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 30 | 83,33% | +1,51% | +3,38% | -4,28% | +5,78% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 25 | 64,00% | +2,45% | +2,59% | -3,99% | +6,37% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 31 | 35,48% | +1,33% | -1,99% | -4,36% | +5,71% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,19% | -1,19% | -4,25% | +5,07% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 18 | 55,56% | +1,54% | -0,44% | -6,41% | +6,79% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 20 | 75,00% | +1,76% | +4,56% | -6,27% | +6,31% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 23 | 78,26% | +1,18% | +4,32% | -6,25% | +5,99% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 18 | 50,00% | +2,26% | +3,20% | -5,99% | +6,87% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 24 | 50,00% | +1,16% | -2,87% | -6,28% | +5,89% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 16 | 50,00% | +3,90% | -3,90% | -5,75% | +7,67% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 14 | 42,86% | +2,59% | +0,37% | -7,69% | +6,71% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 11 | 72,73% | +2,91% | +1,96% | -8,12% | +7,29% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 14 | 64,29% | +2,34% | +1,49% | -7,84% | +6,56% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 9 | 66,67% | +2,32% | +2,79% | -7,96% | +6,98% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 15 | 26,67% | +2,26% | -3,51% | -7,78% | +6,36% | FEEDBACK RAPIDO |
| SOL | 30g | Classic technical | CALIBRABILE | 7 | 28,57% | +5,28% | -5,28% | -7,15% | +9,70% | FEEDBACK RAPIDO |
| SOL | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | FEEDBACK RAPIDO |
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

Generato: 2026-08-22 05:32 UTC

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
| BTC | 43 | PRIMA CALIBRAZIONE | 42 | 12 | 0 | 0 | Famiglia statistica | 1g | 57,14% | +0,49% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 43 | PRIMA CALIBRAZIONE | 39 | 13 | 0 | 0 | Tecnico | 1g | 51,28% | +0,19% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 43 | PRIMA CALIBRAZIONE | 42 | 14 | 0 | 0 | Famiglia statistica | 1g | 57,14% | +0,81% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 10 | 30,00% | +0,54% | +1,59% | +0,82% | +2,11% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 42 | 57,14% | +0,49% | +0,49% | +0,10% | +1,03% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 37 | 37,84% | +0,13% | +0,68% | +0,27% | +1,23% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 9 | 22,22% | +0,36% | +2,05% | +1,71% | +2,86% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 41 | 56,10% | +0,98% | +0,98% | +0,45% | +1,69% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 36 | 41,67% | +0,11% | +1,26% | +0,74% | +1,97% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 8 | 12,50% | -2,41% | +2,41% | -0,24% | +3,25% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 40 | 57,50% | +1,24% | +1,24% | -1,00% | +2,74% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 35 | 31,43% | -0,71% | +1,70% | -0,74% | +3,13% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 8 | 12,50% | -7,26% | +7,26% | -0,63% | +8,70% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 38 | 44,74% | +1,34% | +1,34% | -1,86% | +3,38% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 33 | 33,33% | -2,28% | +1,71% | -1,62% | +3,78% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 6 | 0,00% | -8,28% | +8,28% | -0,96% | +9,64% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 36 | 52,78% | +1,12% | +1,12% | -2,24% | +3,50% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 31 | 32,26% | -2,15% | +1,66% | -1,99% | +3,88% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,32% | +1,32% | -1,42% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 34 | 50,00% | +0,75% | +0,75% | -2,68% | +3,36% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 29 | 34,48% | +0,49% | +1,07% | -2,43% | +3,73% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Classic technical | 4 | 50,00% | -0,27% | +0,27% | -1,55% | +3,37% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 31 | 51,61% | +1,30% | +1,30% | -2,88% | +4,45% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 26 | 61,54% | +1,74% | +1,80% | -2,58% | +4,99% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Classic technical | 3 | 0,00% | -8,03% | +8,03% | -1,93% | +10,14% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 24 | 50,00% | +1,47% | +1,47% | -3,14% | +5,15% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 19 | 21,05% | -1,81% | +1,45% | -2,79% | +5,23% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 15 | 66,67% | +2,59% | +2,59% | -3,18% | +6,68% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 12 | 41,67% | -1,91% | +1,49% | -2,79% | +6,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 27 | 37,04% | -0,44% | +0,44% | -0,04% | +1,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 42 | 57,14% | +0,81% | +0,52% | +0,01% | +1,47% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +3,06% | +3,69% | +2,25% | +3,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 35 | 54,29% | +0,69% | +0,45% | -0,08% | +1,36% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 27 | 44,44% | -1,08% | +1,08% | +0,40% | +2,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 41 | 51,22% | +1,14% | +0,91% | +0,26% | +2,19% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 5 | 60,00% | +6,19% | +6,72% | +5,95% | +9,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 34 | 61,76% | +0,89% | +0,35% | -0,23% | +1,57% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 27 | 33,33% | -1,97% | +1,97% | -1,30% | +4,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 40 | 52,50% | +1,29% | +0,98% | -1,54% | +3,39% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,18% | +1,70% | -0,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 33 | 48,48% | +0,25% | -0,26% | -1,90% | +1,81% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 25 | 48,00% | -1,57% | +1,57% | -2,40% | +4,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 38 | 52,63% | +1,50% | +0,83% | -2,49% | +3,92% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,23% | +0,64% | -0,37% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 33 | 63,64% | +0,56% | +0,95% | -2,69% | +4,03% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 23 | 52,17% | +0,04% | -0,04% | -3,05% | +3,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 36 | 58,33% | +1,64% | +0,45% | -2,99% | +4,13% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,36% | +0,63% | -0,50% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 31 | 64,52% | +1,94% | -0,09% | -3,29% | +3,65% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 22 | 59,09% | +1,13% | -1,13% | -3,71% | +2,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 34 | 55,88% | +1,35% | -0,51% | -3,58% | +3,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 4 | 75,00% | +0,18% | +0,93% | -1,31% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 30 | 66,67% | +1,40% | -1,40% | -3,88% | +2,63% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 21 | 66,67% | +1,05% | -1,05% | -4,58% | +3,86% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 31 | 67,74% | +2,93% | -0,09% | -4,34% | +4,82% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 3 | 66,67% | -6,24% | +6,85% | -1,27% | +10,97% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 30 | 66,67% | +0,31% | -0,31% | -4,43% | +4,70% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 20 | 75,00% | -0,03% | +0,03% | -5,18% | +6,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 24 | 79,17% | +4,32% | -0,61% | -5,40% | +5,15% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 24 | 79,17% | +0,61% | -0,61% | -5,40% | +5,15% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 14 | 78,57% | +0,15% | -0,15% | -6,50% | +6,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 15 | 80,00% | +0,54% | -0,54% | -6,61% | +5,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 15 | 80,00% | +0,54% | -0,54% | -6,61% | +5,66% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 23 | 52,17% | +0,39% | +0,46% | -0,22% | +1,38% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 37 | 59,46% | +0,22% | +0,21% | -0,28% | +1,06% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,51% | +1,51% | +0,99% | +5,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 39 | 51,28% | +0,19% | +0,22% | -0,34% | +1,02% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 22 | 50,00% | +0,43% | +0,47% | -0,09% | +1,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 36 | 52,78% | +0,77% | +0,64% | -0,12% | +1,36% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 38 | 39,47% | -0,29% | +0,51% | -0,16% | +1,61% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 21 | 42,86% | -0,13% | +0,13% | -1,91% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 36 | 50,00% | +1,46% | +1,25% | -1,65% | +3,28% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 37 | 40,54% | -1,05% | +0,73% | -1,85% | +2,61% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 21 | 52,38% | -0,14% | +0,14% | -2,60% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 34 | 55,88% | +1,60% | +1,40% | -2,68% | +4,10% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 36 | 41,67% | -1,80% | +1,34% | -2,69% | +4,21% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 32 | 62,50% | +1,68% | +0,96% | -3,21% | +4,24% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 34 | 35,29% | -1,54% | +0,94% | -3,25% | +4,35% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 30 | 63,33% | +1,58% | +0,86% | -3,78% | +4,05% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 32 | 46,88% | -0,22% | +0,07% | -3,88% | +3,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 27 | 81,48% | +3,41% | +2,03% | -4,32% | +5,99% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 31 | 35,48% | -1,99% | +1,33% | -4,36% | +5,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 16 | 50,00% | -3,90% | +3,90% | -5,75% | +7,67% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 20 | 75,00% | +4,56% | +1,76% | -6,27% | +6,31% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 24 | 50,00% | -2,87% | +1,16% | -6,28% | +5,89% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 7 | 28,57% | -5,28% | +5,28% | -7,15% | +9,70% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 11 | 72,73% | +1,96% | +2,91% | -8,12% | +7,29% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 15 | 26,67% | -3,51% | +2,26% | -7,78% | +6,36% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 40 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 42 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 27 | 22,22% | -0,39% |
| BTC | BREVE | Famiglia statistica | 123 | 56,91% | +0,90% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 108 | 37,04% | -0,15% |
| BTC | SETTIMANALE | Classic technical | 18 | 5,56% | -6,28% |
| BTC | SETTIMANALE | Famiglia statistica | 108 | 49,07% | +1,08% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 93 | 33,33% | -1,37% |
| BTC | SWING | Classic technical | 7 | 28,57% | -3,60% |
| BTC | SWING | Famiglia statistica | 55 | 50,91% | +1,38% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 45 | 44,44% | +0,24% |
| BTC | MEDIO | Famiglia statistica | 15 | 66,67% | +2,59% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 12 | 41,67% | -1,91% |
| DOGE | BREVE | Classic technical | 81 | 38,27% | -1,16% |
| DOGE | BREVE | Famiglia statistica | 123 | 53,66% | +1,08% |
| DOGE | BREVE | Microstruttura exchange | 14 | 57,14% | +3,64% |
| DOGE | BREVE | Tecnico | 102 | 54,90% | +0,61% |
| DOGE | SETTIMANALE | Classic technical | 70 | 52,86% | -0,19% |
| DOGE | SETTIMANALE | Famiglia statistica | 108 | 55,56% | +1,50% |
| DOGE | SETTIMANALE | Microstruttura exchange | 12 | 58,33% | +0,26% |
| DOGE | SETTIMANALE | Tecnico | 94 | 64,89% | +1,28% |
| DOGE | SWING | Classic technical | 41 | 70,73% | +0,52% |
| DOGE | SWING | Famiglia statistica | 55 | 72,73% | +3,53% |
| DOGE | SWING | Microstruttura exchange | 5 | 80,00% | -3,44% |
| DOGE | SWING | Tecnico | 54 | 72,22% | +0,45% |
| DOGE | MEDIO | Classic technical | 14 | 78,57% | +0,15% |
| DOGE | MEDIO | Famiglia statistica | 15 | 80,00% | +0,54% |
| DOGE | MEDIO | Tecnico | 15 | 80,00% | +0,54% |
| SOL | BREVE | Classic technical | 66 | 48,48% | +0,24% |
| SOL | BREVE | Famiglia statistica | 109 | 54,13% | +0,81% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 7 | 28,57% | -0,12% |
| SOL | BREVE | Tecnico | 114 | 43,86% | -0,37% |
| SOL | SETTIMANALE | Classic technical | 63 | 49,21% | -0,00% |
| SOL | SETTIMANALE | Famiglia statistica | 96 | 60,42% | +1,62% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 6 | 16,67% | -2,65% |
| SOL | SETTIMANALE | Tecnico | 102 | 41,18% | -1,22% |
| SOL | SWING | Classic technical | 37 | 43,24% | -2,36% |
| SOL | SWING | Famiglia statistica | 47 | 78,72% | +3,90% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 2 | 0,00% | -4,49% |
| SOL | SWING | Tecnico | 55 | 41,82% | -2,38% |
| SOL | MEDIO | Classic technical | 7 | 28,57% | -5,28% |
| SOL | MEDIO | Famiglia statistica | 11 | 72,73% | +1,96% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 15 | 26,67% | -3,51% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 12 | in attesa di controlli maturati |
| SOL | MEDIO | 10 | in attesa di controlli maturati |
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
| BTC     |         43 |              15 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         43 |              15 |          28 | RACCOLTA DATI | 6,67%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         43 |              15 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | MEDIO          | ALTO           | leva da limitare; 2x/3x solo con invalidazione chiara                   |
| SOL     | MEDIO          | MOLTO ALTO     | leva moderata possibile solo con stop e margine                         |
| DOGE    | MEDIO          | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-08-22 05:32 UTC


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
| BTC | +5 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | Prima resistenza sopra 77.991; conferma del doppio minimo sopra 66.910. | Sotto 62.488 il quadro tecnico peggiora. |
| SOL | +3 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | HOLD / TRANCHE PICCOLE, NO LEVA | Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 98,27; milestone analogiche 102,22 / 117,24, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 89,01 / 74,20 / 62,19. |
| DOGE | +6 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | SOLO TRANCHE PICCOLE / NO LEVA | Sopra 0.09169 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.06895 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | 0 | +1 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +5 |
| SOL | -1 | 0 | -1 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +3 |
| DOGE | +1 | 0 | +1 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +6 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+5**
- Affidabilità: **MEDIA**
- Azione coerente: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**

BTC è l'asset messo meglio nel breve, ma lo score statistico ora conta Scanner e Market Regime una sola volta. La struttura macro resta debole: ha più senso accumulare a tranche sui pullback che inseguire il prezzo vicino alle resistenze.

Dettaglio moduli:

- Famiglia statistica: **+1** — Scanner grezzo +1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+1** — Casi positivi 57,50%, return centrale 30g +3,62%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 41. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 10/12, verdetto rialzista tecnico, trend rialzista, struttura compressione / triangolo, divergenza rialzista nascosta rsi, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 9/12, verdetto CONFERMATO RIALZISTA, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff RANGE / FASE NON CHIARA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.00; exchange 3/3, copertura 100%, consenso bull 0, bear 2, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — BTC: nessun cambiamento forte in misto rispetto a ieri.

Conferme: Prima resistenza sopra 77.991; conferma del doppio minimo sopra 66.910.

Invalidazioni: Sotto 62.488 il quadro tecnico peggiora.

### SOL

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+3**
- Affidabilità: **MEDIA**
- Azione coerente: **HOLD / TRANCHE PICCOLE, NO LEVA**

SOL ha una confluenza costruttiva, ma va ancora trattato come setup anticipato. La conferma vera arriva solo sopra le resistenze tecniche e con rientro del gap frattale. Il modulo lifecycle/EMA200 resta utile come contesto, ma non aumenta il punteggio Global.

Dettaglio moduli:

- Famiglia statistica: **-1** — Scanner grezzo -1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-1** — Casi positivi 45,00%, return centrale 30g -1,14%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 41. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 10/12, verdetto rialzista tecnico, trend rialzista, struttura compressione / triangolo, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 11/12, verdetto CONFERMATO RIALZISTA, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +61,86%, aderenza live +70,53%, errore live +14,73%, gap corrente +4,51%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 37, ma percorso ancorato non aderente: gap +4,51%, errore live +14,73%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 111,46 $, upside EMA200 +19,27%, gap EMA50/EMA200 -5,83%, hit EMA200 12w +53,33%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow -0.25, derivati +1.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 0, bear 3, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — SOL: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 98,27; milestone analogiche 102,22 / 117,24, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 89,01 / 74,20 / 62,19.

### DOGE

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+6**
- Affidabilità: **MEDIA**
- Azione coerente: **SOLO TRANCHE PICCOLE / NO LEVA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+1** — Scanner grezzo +1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+1** — Casi positivi 55,00%, return centrale 30g +1,88%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 41. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 7/12, verdetto rialzista tecnico, trend misto, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff range / fase non chiara, pattern score 0 (rialzista Triplo minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 5/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +1.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 2, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +1, peso Global +0 (LOCKED / RACCOLTA 7G). Bias POSITIVA / CANDIDATA, ANCORA NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +1 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **+1** — DOGE: cambiamento medio in miglioramento rispetto a ieri.

Conferme: Sopra 0.09169 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.

Invalidazioni: Sotto 0.06895 il rischio ribassista aumenta.


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

Generato: 2026-08-22 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 77.092 $ | prezzo corrente |
| Power Law centrale | 123.812 $ | deviazione -37,73% |
| Banda p10-p90 | 76.804 $ / 312.654 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 10,40% | posizione storica nel corridoio |
| Esponente β | 5,8146 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3164 cambiando finestra |
| Ultimo halving | 2024-04-19 | 855 giorni fa |
| Fase ciclo | 58,52% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-22 (4357 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.1471) × giorni^5.8146
- Prezzo centrale oggi: **123.812 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 10,40%
- Scarto dal centro: **-37,73%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8146 | 91,93% |
| 2015 | 5,8982 | 91,48% |
| 2016 | 5,5834 | 87,72% |
| 2017 | 4,8538 | 82,85% |
| 2018 | 4,5818 | 78,32% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-09 | -23,07% | -16,09% | -6,76% | +54,13% |
| 2016-07-09 → 2020-05-11 | 2018-10-07 | -2,15% | -41,77% | -23,72% | +24,88% |
| 2020-05-11 → 2024-04-19 | 2022-08-31 | -3,08% | -17,98% | +17,32% | +29,34% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 4 | 1 | 2.909247493935596 | 0 |
| DOGE | DOGE/BTC | RELATIVA MISTA / NON CONFERMATA | 0 | 0 | 6.003677862954526 | 0 |

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

Generato: 2026-08-22 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00121330 | +4 | +1 | 0 | SOVRAPERFORMA BTC | BASSA | +2,91% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000117 | 0 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +6,00% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |

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
- **Lettura combinata USD/BTC:** CONFERMA FORTE: sale in USD e batte BTC
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g +1,45%; 30g +2,91%; 90g +8,62%; 180g -0,87%
- **Daily:** RSI 58.09; MA50 0.00119115; MA200 0.00117787
- **Weekly:** MA30 0.00118304; RSI 49.60
- **Livelli:** supporto 0.00119400; resistenza 0.00134900; breakout 60g 0.00134900; breakdown 60g 0.00108800
- **Pattern:** DOPPIO MASSIMO / CANDIDATO; neckline 0.00112700; target 0.00107050
- **Fibonacci:** VICINO — 38.2% a 0.00121912
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; prezzo sopra MA30 weekly; MA30 weekly in discesa; RSI relativo forte; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (0)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g +5,25%; 30g +6,00%; 90g -12,90%; 180g -17,07%
- **Daily:** RSI 64.16; MA50 0.00000112; MA200 0.00000129
- **Weekly:** MA30 0.00000129; RSI 40.06
- **Livelli:** supporto 0.00000116; resistenza 0.00000121; breakout 60g 0.00000139; breakdown 60g 0.00000104
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000126
- **Fibonacci:** NON ATTIVO — 38.2% a 0.00000120
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; RSI relativo forte; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 204 | 51,96% | +1,94% | -1,18% |
| SOL | 30g | 202 | 47,52% | +4,66% | +0,36% |
| SOL | 90g | 198 | 53,03% | +10,08% | +2,72% |
| DOGE | 7g | 294 | 55,78% | +1,84% | -1,68% |
| DOGE | 30g | 291 | 53,26% | +2,05% | -3,93% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 18 | 61,11% | -0,24% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 17 | 47,06% | -0,54% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 16 | 43,75% | -1,32% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 15 | 6,67% | -3,44% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 35 | 68,57% | +0,02% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 34 | 61,76% | +0,57% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 34 | 64,71% | +0,58% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 29 | 72,41% | +0,82% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 13 | 84,62% | +1,88% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **22 agosto 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +61,86%
- **Somiglianza strutturale:** +61,86%
- **Aderenza prezzo live:** +70,53%
- **Errore medio live:** +14,73%
- **Gap prezzo corrente:** +4,51%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 77 dal bottom usato.
- **Giorno BTC equivalente:** 2023-02-06
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Prima retest / debolezza, poi recupero.** Zona bassa **89,13 $** intorno al **26 agosto 2026**; zona alta **102,22 $** intorno al **5 settembre 2026**; fine step circa **102,22 $** entro il **5 settembre 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 22 agosto 2026 | 51 | +70,53% | +14,73% | +4,51% | DEVIAZIONE MODERATA |
| Totale dal bottom | 6 giugno 2026 -> 22 agosto 2026 | 78 | +76,56% | +11,72% | +4,51% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +70,53% | Errore medio live +14,73%. |
| Gap corrente | +4,51% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 102,22 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 117,24 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 89,01 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 513,59 $ |
| Massimo percorso base | 513,59 $ (21 aprile 2029) |

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
| Prima conferma | 102,22 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 117,24 $ | Scenario più credibile. |
| Invalidazione soft | 89,01 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 29 agosto 2026 | -4,18% | 89,78 $ | 89,13 $ | 95,78 $ |
| 14 giorni | 5 settembre 2026 | +9,09% | 102,22 $ | 89,13 $ | 102,22 $ |
| 30 giorni | 21 settembre 2026 | -4,58% | 89,41 $ | 89,13 $ | 102,22 $ |
| 60 giorni | 21 ottobre 2026 | +22,70% | 114,97 $ | 83,11 $ | 117,24 $ |
| 90 giorni | 20 novembre 2026 | +25,02% | 117,14 $ | 83,11 $ | 125,51 $ |
| 120 giorni | 20 dicembre 2026 | +19,68% | 112,14 $ | 83,11 $ | 125,51 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 22 agosto 2026 -> 5 settembre 2026 | +9,09% | 89,13 $ (26 agosto 2026) | 102,22 $ (5 settembre 2026) | 102,22 $ | Prima retest / debolezza, poi recupero. |
| Step 2 - primo mese | 6 settembre 2026 -> 21 settembre 2026 | -4,58% | 89,41 $ (21 settembre 2026) | 100,60 $ (6 settembre 2026) | 89,41 $ | Prima spike, poi scarico. |
| Step 3 - secondo mese | 22 settembre 2026 -> 21 ottobre 2026 | +22,70% | 83,11 $ (23 settembre 2026) | 117,24 $ (14 ottobre 2026) | 114,97 $ | Prima retest / debolezza, poi recupero. |
| Step 4 - terzo mese | 22 ottobre 2026 -> 20 novembre 2026 | +25,02% | 112,29 $ (4 novembre 2026) | 125,51 $ (28 ottobre 2026) | 117,14 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 93,70 $ |  |
| Weekly RSI | 53,58 / linea grezza 52,95 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 45,08 / linea grezza 55,81 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 513,59 $ | Avanzamento +18,24% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 45,1, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Score on-chain | 5 |
| Bias | POSITIVA FORTE |
| Azione coerente | ON-CHAIN SANO / RAFFORZA IL FRATTALE |
| Prezzo SOL | 93,70 $ |
| TVL Solana | 5,62 mld $ |
| TVL 7g | +16,93% |
| DEX volume 24h | 3,47 mld $ |
| Fees 24h | 13,20 mln $ |
| Stablecoin su Solana | 16,36 mld $ |
| Stake ratio | 68,52% |
| Metriche mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

Lettura semplice:

**ON-CHAIN SANO / RAFFORZA IL FRATTALE**

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
| Confronto precedente | 2026-08-17 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 93,70 $ |
| EMA200 weekly target | 111,46 $ |
| Upside verso EMA200 | +19,27% |
| Distanza prezzo da EMA200 | -16,16% |
| Gap EMA50/EMA200 | -5,83% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 53,44 |
| Età SOL | 6,4 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +53,33% |
| Max gain mediano 12w | +27,63% |
| Drawdown mediano 12w | -32,35% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-08-22 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-08-22 05:30:23 UTC**

Questo report confronta il grafico attuale di Bitcoin, Solana e Dogecoin con tanti grafici storici di altre crypto.

Non è una previsione certa. È uno scanner statistico: guarda situazioni simili già successe e mostra cosa accadde dopo nei 30 giorni successivi.

<!-- COMPACT_SECTION_START:daily_change -->
<details open>
<summary><strong>🗓️ Cambiamenti rispetto a ieri</strong></summary>

<!-- DAILY_CHANGE_START -->

---

# Mini report cambiamenti da ieri

Report separato completo: [daily_change_report.md](daily_change_report.md)

- BTC: nessun cambiamento forte rispetto a ieri.
- SOL: nessun cambiamento forte rispetto a ieri.
- DOGE: cambiamento importante in miglioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | NESSUN CAMBIAMENTO FORTE | misto | NEUTRALE / INCERTO | +57.50% | 0.00 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | peggioramento | NEUTRALE / INCERTO | +45.00% | -2.50 punti |
| DOGE | CAMBIAMENTO MEDIO | miglioramento | NEUTRALE / INCERTO | +55.00% | 0.00 punti |

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
| BTC | 73.377 $ | 84.963 $ | +39,13% | +15,79% | rimbalzo debole | 84.963 $ | 73.377 $ | +35,71% | -13,64% | scarico possibile |
| SOL | 89,01 $ | 103,07 $ | +29,63% | +15,79% | rimbalzo poco frequente | 103,07 $ | 89,01 $ | +26,09% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08608 $ | 0,09967 $ | +55,17% | +15,79% | rimbalzo possibile | 0,09967 $ | 0,08608 $ | +21,88% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 23 prima sono scesi a -5,00%. Tra quei 23, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +39,13% (9/23). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 10 poi sono scaricati a -5,00%. Percentuale: +35,71% (10/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.**
- **SOL: su 40 casi simili, 27 prima sono scesi a -5,00%. Tra quei 27, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +29,63% (8/27). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 6 poi sono scaricati a -5,00%. Percentuale: +26,09% (6/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 16 poi sono rimbalzati fino a +10,00%. Percentuale: +55,17% (16/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **DOGE: su 40 casi simili, 32 prima sono saliti a +10,00%. Tra quei 32, 7 poi sono scaricati a -5,00%. Percentuale: +21,88% (7/32). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-08-22 05:31:40 UTC


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

| Asset   | Data       | Prezzo iniziale   | Direzione scanner   | Casi positivi   | P10 30g     | P25 30g     | P50 30g     | P75 30g     | P90 30g      |
|:--------|:-----------|:------------------|:--------------------|:----------------|:------------|:------------|:------------|:------------|:-------------|
| BTC | 2026-08-22 | 77.239 $ | INCERTO | 57,50% | 67.565,92 $ | 72.087,34 $ | 80.036,29 $ | 86.813,96 $ | 106.740,56 $ |
| SOL | 2026-08-22 | 93,70 $ | INCERTO | 45,00% | 81,86 $ | 86,67 $ | 92,63 $ | 108,22 $ | 135,02 $ |
| DOGE | 2026-08-22 | 0.09061 $ | INCERTO | 55,00% | 0.06234 $ | 0.07926 $ | 0.09231 $ | 0.09916 $ | 0.11994 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-23**; verificato fino al **2026-08-22**; stato **COMPLETO 30/30g**.
- Reale **76.919,51 $**; p50 previsto **71.966,75 $**; scarto **6,88%**.
- Errore medio assoluto **3,30%**; massimo **9,13%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-23**; verificato fino al **2026-08-22**; stato **COMPLETO 30/30g**.
- Reale **92,96 $**; p50 previsto **80,03 $**; scarto **16,15%**.
- Errore medio assoluto **4,28%**; massimo **17,65%**; DENTRO p10-p90; FUORI p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-23**; verificato fino al **2026-08-22**; stato **COMPLETO 30/30g**.
- Reale **0.08926 $**; p50 previsto **0.07155 $**; scarto **24,76%**.
- Errore medio assoluto **4,63%**; massimo **28,64%**; DENTRO p10-p90; FUORI p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 41 | 92,68% | 58,54% | 2,29% | 0,77% |
| BTC | 3g | 39 | 89,74% | 71,79% | 3,28% | 0,93% |
| BTC | 7g | 35 | 100,00% | 80,00% | 3,80% | 0,73% |
| BTC | 14g | 30 | 100,00% | 80,00% | 3,86% | 0,65% |
| BTC | 30g | 14 | 100,00% | 92,86% | 6,29% | -3,14% |
| SOL | 1g | 41 | 75,61% | 58,54% | 2,80% | 0,82% |
| SOL | 3g | 39 | 89,74% | 71,79% | 3,53% | 0,75% |
| SOL | 7g | 35 | 94,29% | 85,71% | 3,10% | 0,96% |
| SOL | 14g | 30 | 93,33% | 80,00% | 4,36% | 3,12% |
| SOL | 30g | 14 | 92,86% | 78,57% | 5,62% | 4,70% |
| DOGE | 1g | 41 | 87,80% | 60,98% | 3,26% | 1,36% |
| DOGE | 3g | 39 | 92,31% | 79,49% | 3,76% | 2,38% |
| DOGE | 7g | 35 | 88,57% | 85,71% | 6,57% | 4,80% |
| DOGE | 14g | 30 | 90,00% | 63,33% | 8,84% | 7,49% |
| DOGE | 30g | 14 | 100,00% | 42,86% | 16,27% | 16,27% |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |

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

<!-- FORECAST_30D_HISTORY_START -->

---

# Storico previsioni 30 giorni

Report separato completo: [forecast_30d_history.md](forecast_30d_history.md)

Righe salvate nello storico: **117**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-22 | BTC | 77.239 $ | INCERTO | 57,50% | 80.036 $ | 71.660 $ | 90.835 $ | 2026-09-21 |
| 2026-08-22 | DOGE | 0,09000 $ | INCERTO | 55,00% | 0,09000 $ | 0,08000 $ | 0,11000 $ | 2026-09-21 |
| 2026-08-22 | SOL | 93,70 $ | INCERTO | 45,00% | 92,63 $ | 84,94 $ | 104,29 $ | 2026-09-21 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-08-22 05:31 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +57,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +55,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +55,00%       | Nessun lato sopra soglia estrema |                  40 |

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
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **57,50%**
- Casi negativi / discesa storica: **42,50%**
- Quanto è netto il segnale: **debole**
- Prezzo attuale: **77.239,39 $**
- Return normale fra 30 giorni: **80.036,29 $** (3,62%)
- Drawdown normale durante il mese: **71.660,38 $** (-7,22%)
- Drawdown brutto da rispettare: **67.445,04 $** (-12,68%)
- Max gain normale durante il mese: **90.834,51 $** (17,60%)
- Max gain buono / take profit ottimistico: **97.704,77 $** (26,50%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **45,00%**
- Casi negativi / discesa storica: **55,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **93,70 $**
- Return normale fra 30 giorni: **92,63 $** (-1,14%)
- Drawdown normale durante il mese: **84,94 $** (-9,35%)
- Drawdown brutto da rispettare: **81,84 $** (-12,65%)
- Max gain normale durante il mese: **104,29 $** (11,30%)
- Max gain buono / take profit ottimistico: **116,91 $** (24,78%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **55,00%**
- Casi negativi / discesa storica: **45,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **0,09 $**
- Return normale fra 30 giorni: **0,09 $** (1,88%)
- Drawdown normale durante il mese: **0,08 $** (-8,71%)
- Drawdown brutto da rispettare: **0,07 $** (-17,46%)
- Max gain normale durante il mese: **0,11 $** (18,73%)
- Max gain buono / take profit ottimistico: **0,12 $** (34,66%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è misto. Alcuni asset possono avere lettura diversa, quindi è meglio valutare asset per asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 77.239,39 $

**Direzione più probabile a 30 giorni:** **INCERTO**
- Probabilità storica di salita: **57,50%**
- Probabilità storica di discesa: **42,50%**
- Quanto è netto il segnale: **debole**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è incerta, con segnale debole. Nei casi storici simili non c'è stato un vantaggio chiaro né per salita né per discesa.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **67.565,92 $** (-12,52%)
- Se va male: **72.087,34 $** (-6,67%)
- Scenario normale: **80.036,29 $** (3,62%)
- Se va bene: **86.813,96 $** (12,40%)
- Se va molto bene: **106.740,56 $** (38,19%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **71.660,38 $** (-7,22%)
- Discesa brutta: **67.445,04 $** (-12,68%)
- Discesa molto brutta: **64.881,45 $** (-16,00%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **90.834,51 $** (17,60%)
- Rialzo buono: **97.704,77 $** (26,50%)
- Rialzo molto forte: **117.672,55 $** (52,35%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **71.660,38 $** e uno spike normale intorno a **90.834,51 $**.

La chiusura a 30 giorni è incerta: salita 57,50%, discesa 42,50%. Non c'è un vantaggio netto.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 93,70 $

**Direzione più probabile a 30 giorni:** **INCERTO**
- Probabilità storica di salita: **45,00%**
- Probabilità storica di discesa: **55,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è incerta, con segnale molto debole / quasi pari. Nei casi storici simili non c'è stato un vantaggio chiaro né per salita né per discesa.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **81,86 $** (-12,64%)
- Se va male: **86,67 $** (-7,51%)
- Scenario normale: **92,63 $** (-1,14%)
- Se va bene: **108,22 $** (15,49%)
- Se va molto bene: **135,02 $** (44,10%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **84,94 $** (-9,35%)
- Discesa brutta: **81,84 $** (-12,65%)
- Discesa molto brutta: **80,03 $** (-14,59%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **104,29 $** (11,30%)
- Rialzo buono: **116,91 $** (24,78%)
- Rialzo molto forte: **142,15 $** (51,71%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **84,94 $** e uno spike normale intorno a **104,29 $**.

La chiusura a 30 giorni è incerta: salita 45,00%, discesa 55,00%. Non c'è un vantaggio netto.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 0,09 $

**Direzione più probabile a 30 giorni:** **INCERTO**
- Probabilità storica di salita: **55,00%**
- Probabilità storica di discesa: **45,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è incerta, con segnale molto debole / quasi pari. Nei casi storici simili non c'è stato un vantaggio chiaro né per salita né per discesa.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,06 $** (-31,20%)
- Se va male: **0,08 $** (-12,53%)
- Scenario normale: **0,09 $** (1,88%)
- Se va bene: **0,10 $** (9,43%)
- Se va molto bene: **0,12 $** (32,37%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,08 $** (-8,71%)
- Discesa brutta: **0,07 $** (-17,46%)
- Discesa molto brutta: **0,06 $** (-32,98%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,11 $** (18,73%)
- Rialzo buono: **0,12 $** (34,66%)
- Rialzo molto forte: **0,14 $** (49,58%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,08 $** e uno spike normale intorno a **0,11 $**.

La chiusura a 30 giorni è incerta: salita 55,00%, discesa 45,00%. Non c'è un vantaggio netto.

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

- Previsioni già controllate: **21**
- Direzione corretta: **78,57%**
- Errore medio dello scenario centrale: **4,93%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **21**
- Direzione corretta: **90,00%**
- Errore medio dello scenario centrale: **13,25%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **4,76%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Solana

- Previsioni già controllate: **21**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **5,02%**
- Zona rischio toccata: **9,52%**
- Zona rialzo media toccata: **9,52%**
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

Dati ancora insufficienti: previsioni controllate **21** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **21** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **21** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 77.239,39 $

Bitcoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **57,50%**
- Casi negativi dopo 30 giorni: **42,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **80,92%**
- Rendimento medio dopo 30 giorni: **10,75%**
- Rendimento centrale dopo 30 giorni: **3,62%**
- Discesa media durante i 30 giorni: **-8,20%**
- Massimo rialzo medio durante i 30 giorni: **25,19%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **85.545,37 $**
- Scenario centrale a 30 giorni: **80.036,29 $**
- Zona di rischio media: **70.909,38 $**
- Zona di rialzo media: **96.694,45 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -12,52% → **67.565,92 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -6,67% → **72.087,34 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 3,62% → **80.036,29 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 12,40% → **86.813,96 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 38,19% → **106.740,56 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -16,00% → **64.881,45 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -12,68% → **67.445,04 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -7,22% → **71.660,38 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -2,68% → **75.172,42 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,11% → **77.151,08 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 4,95% → **81.063,42 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 8,80% → **84.035,82 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 17,60% → **90.834,51 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 26,50% → **97.704,77 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 52,35% → **117.672,55 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XLM-USD         | 2020-08-14   | 2020-11-21 |        88.54 |        53.46 |          -4.5  |          90.41 |
| LTC-USD         | 2023-07-26   | 2023-11-02 |        84.93 |         4.15 |          -4.23 |           8.33 |
| MKR-USD         | 2020-02-22   | 2020-05-31 |        84.67 |        -1.14 |          -7.47 |          49.98 |
| ETC-USD         | 2020-08-14   | 2020-11-21 |        84.65 |        -6.61 |         -12.09 |          10.56 |
| XRP-USD         | 2023-07-25   | 2023-11-01 |        83.61 |         0.55 |          -4.77 |          17.39 |
| DOGE-USD        | 2020-08-14   | 2020-11-21 |        83.28 |        36.5  |         -12.2  |          36.5  |
| THETA-USD       | 2022-04-20   | 2022-07-28 |        83.14 |       -16.53 |         -16.53 |          23.44 |
| XRP-USD         | 2026-01-15   | 2026-04-24 |        83.05 |        -5.83 |          -6.97 |           3.52 |
| LTC-USD         | 2018-10-30   | 2019-02-06 |        82.73 |        70.34 |           0    |          73.65 |
| BNB-USD         | 2018-10-29   | 2019-02-05 |        82.49 |        93.69 |          -1.14 |          93.69 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 93,70 $

Solana è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **45,00%**
- Casi negativi dopo 30 giorni: **55,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **72,99%**
- Rendimento medio dopo 30 giorni: **20,84%**
- Rendimento centrale dopo 30 giorni: **-1,14%**
- Discesa media durante i 30 giorni: **-8,44%**
- Massimo rialzo medio durante i 30 giorni: **34,74%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **113,22 $**
- Scenario centrale a 30 giorni: **92,63 $**
- Zona di rischio media: **85,80 $**
- Zona di rialzo media: **126,25 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -12,64% → **81,86 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -7,51% → **86,67 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -1,14% → **92,63 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 15,49% → **108,22 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 44,10% → **135,02 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -14,59% → **80,03 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -12,65% → **81,84 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -9,35% → **84,94 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -3,01% → **90,88 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **93,70 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 2,09% → **95,66 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 5,41% → **98,77 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 11,30% → **104,29 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 24,78% → **116,91 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 51,71% → **142,15 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| EOS-USD         | 2018-11-13   | 2019-02-20 |        81.37 |        -6.92 |         -16.43 |           8.85 |
| MKR-USD         | 2020-02-22   | 2020-05-31 |        79.23 |        -1.14 |          -7.47 |          49.98 |
| ZIL-USD         | 2020-08-16   | 2020-11-23 |        77.61 |       135.96 |           0    |         135.96 |
| VET-USD         | 2020-02-23   | 2020-06-01 |        77.3  |        41.53 |           0    |          46.55 |
| BNB-USD         | 2020-02-21   | 2020-05-30 |        77.11 |       -12.61 |         -14.42 |           0.97 |
| ZEC-USD         | 2020-02-21   | 2020-05-30 |        76.97 |        -4.23 |          -9.12 |           6.45 |
| BNB-USD         | 2018-11-03   | 2019-02-10 |        76.4  |        67.25 |          -4.66 |          67.25 |
| ONE-USD         | 2020-02-21   | 2020-05-30 |        75.76 |       -22.17 |         -28.41 |           0.73 |
| FTM-USD         | 2020-10-08   | 2021-01-15 |        75.58 |       544.86 |          -0.05 |         603.2  |
| BCH-USD         | 2025-01-15   | 2025-04-24 |        75.45 |        18.36 |          -2.94 |          24.54 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 0,09 $

Dogecoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **55,00%**
- Casi negativi dopo 30 giorni: **45,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **83,91%**
- Rendimento medio dopo 30 giorni: **3,08%**
- Rendimento centrale dopo 30 giorni: **1,88%**
- Discesa media durante i 30 giorni: **-12,56%**
- Massimo rialzo medio durante i 30 giorni: **28,34%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,09 $**
- Scenario centrale a 30 giorni: **0,09 $**
- Zona di rischio media: **0,08 $**
- Zona di rialzo media: **0,12 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -31,20% → **0,06 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -12,53% → **0,08 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 1,88% → **0,09 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 9,43% → **0,10 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 32,37% → **0,12 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -32,98% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -17,46% → **0,07 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -8,71% → **0,08 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,52% → **0,09 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -1,32% → **0,09 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,09 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 12,96% → **0,10 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 18,73% → **0,11 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 34,66% → **0,12 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 49,58% → **0,14 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| SAND-USD        | 2025-01-14   | 2025-04-23 |        88.9  |         3.56 |          -8.98 |          23.97 |
| DOGE-USD        | 2025-01-15   | 2025-04-24 |        87.86 |        23.48 |          -6.52 |          36.3  |
| OP-USD          | 2026-01-11   | 2026-04-20 |        87.41 |         3.89 |          -3.44 |          39.02 |
| MANA-USD        | 2025-01-15   | 2025-04-24 |        86.11 |        -4.31 |         -10.11 |          18.69 |
| HBAR-USD        | 2020-08-16   | 2020-11-23 |        86.01 |       -12.5  |         -12.5  |          13.17 |
| ALGO-USD        | 2025-01-14   | 2025-04-23 |        85.86 |         4.6  |          -6.82 |          18.34 |
| KSM-USD         | 2022-04-19   | 2022-07-27 |        85    |       -28.63 |         -28.63 |           6.88 |
| VET-USD         | 2025-01-17   | 2025-04-26 |        84.97 |         1.03 |          -8.45 |          18.77 |
| SNX-USD         | 2025-10-12   | 2026-01-19 |        84.8  |       -32.4  |         -36.26 |           0    |
| XTZ-USD         | 2020-08-14   | 2020-11-21 |        84.8  |        -7.78 |         -12.24 |          12.32 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-08-22 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | DISTRIBUTION | 77.239 $ | True | -0.00% | -9.79% | DISTRIBUTION | -0.00% | -9.79% |
| DOGE-USD | DISTRIBUTION | 0.09061 $ | True | -12.39% | -16.28% | DISTRIBUTION | -0.00% | -9.79% |
| SOL-USD | MIXED | 93,70 $ | True | 9.43% | -16.13% | DISTRIBUTION | -0.00% | -9.79% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 57.50% | 3.62% | 12.40% | 38.19% | -7.22% | -16.00% | 17.60% | 26.50% | 52.35% | 65.00% | 21.90% | 43.67% | 145.84% |
| BTC-USD | SAME_BTC_REGIME | 1 | 100.00% | 4.15% | 4.15% | 4.15% | -4.23% | -4.23% | 8.33% | 8.33% | 8.33% | 100.00% | 7.69% | 7.69% | 7.69% |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 3.09% | 3.09% | 3.09% | -3.35% | -3.35% | 6.53% | 6.53% | 6.53% | 0.00% | -9.24% | -9.24% | -9.24% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 55.00% | 1.88% | 9.43% | 32.37% | -8.71% | -32.98% | 18.73% | 34.66% | 49.58% | 30.00% | -13.33% | 4.92% | 76.94% |
| DOGE-USD | SAME_BTC_REGIME | 2 | 50.00% | 8.21% | 28.51% | 40.70% | -18.13% | -32.63% | 39.07% | 58.60% | 70.32% | 50.00% | 52.02% | 91.58% | 115.32% |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 45.00% | -1.14% | 15.49% | 44.10% | -9.35% | -14.59% | 11.30% | 24.78% | 51.71% | 77.50% | 23.84% | 37.75% | 115.99% |
| SOL-USD | SAME_BTC_REGIME | 3 | 100.00% | 17.49% | 18.19% | 18.61% | 0.00% | -10.65% | 18.89% | 21.44% | 22.97% | 66.67% | 52.42% | 66.94% | 75.64% |
| SOL-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 15 | 53.33% | 2.09% | -3.35% | 29.12% | 46.67% | -9.24% | 61.19% |
| BTC-USD | HISTORICAL_BTC_BULL | 17 | 82.35% | 9.47% | -10.11% | 26.02% | 82.35% | 29.10% | 123.95% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 4.15% | -4.23% | 8.33% | 100.00% | 7.69% | 12.98% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 7 | 0.00% | -9.13% | -13.19% | 23.54% | 57.14% | 23.44% | 52.57% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 6 | 66.67% | 2.85% | -8.35% | 37.02% | 16.67% | -15.44% | 39.68% |
| DOGE-USD | HISTORICAL_BTC_BULL | 29 | 55.17% | 1.95% | -8.98% | 23.89% | 34.48% | -14.42% | 36.30% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 50.00% | 8.21% | -18.13% | 58.60% | 50.00% | 52.02% | 105.36% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 33.33% | -1.77% | -6.57% | 53.51% | 0.00% | -8.94% | 53.51% |
| SOL-USD | HISTORICAL_BTC_BEAR | 8 | 50.00% | 0.06% | -6.59% | 53.91% | 37.50% | -17.40% | 69.74% |
| SOL-USD | HISTORICAL_BTC_BULL | 7 | 85.71% | 14.83% | -2.94% | 82.41% | 71.43% | 30.01% | 226.72% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 100.00% | 17.49% | 0.00% | 21.44% | 66.67% | 52.42% | 77.63% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 22 | 22.73% | -6.97% | -10.79% | 13.11% | 95.45% | 23.84% | 50.34% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 20 | 55.00% | 3.13% | -5.06% | 24.71% | 55.00% | 7.77% | 55.96% |
| BTC-USD | HISTORICAL_ASSET_BULL | 11 | 81.82% | 9.47% | -4.77% | 31.26% | 72.73% | 29.10% | 157.79% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 3.09% | -3.35% | 6.53% | 0.00% | -9.24% | 12.81% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 8 | 25.00% | -6.28% | -12.64% | 20.03% | 87.50% | 30.22% | 77.13% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 10 | 50.00% | 1.06% | -5.73% | 39.68% | 30.00% | -11.66% | 60.47% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 24 | 58.33% | 1.88% | -8.14% | 24.85% | 29.17% | -13.35% | 29.87% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | -6.35% | -21.13% | 18.04% | 33.33% | -19.17% | 39.90% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 14 | 57.14% | 0.43% | -9.02% | 25.12% | 50.00% | -0.08% | 87.84% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 100.00% | 16.59% | -1.49% | 109.19% | 83.33% | 124.32% | 247.22% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 20 | 20.00% | -6.97% | -11.56% | 12.93% | 95.00% | 23.84% | 50.10% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LTC-USD | 2023-07-26 | 84.93% | DISTRIBUTION | BULL | SAME_BTC_ONLY | MIXED | 4.15% | -4.23% | 8.33% | 7.69% | -4.23% | 12.98% |
| BTC-USD | BNB-USD | 2026-01-15 | 80.59% | BEAR | DISTRIBUTION | SAME_ASSET_ONLY | MIXED | 3.09% | -3.35% | 6.53% | -9.24% | -10.10% | 12.81% |
| BTC-USD | XLM-USD | 2020-08-14 | 88.54% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 53.46% | -4.50% | 90.41% | 171.53% | -4.50% | 214.37% |
| BTC-USD | MKR-USD | 2020-02-22 | 84.67% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -1.14% | -7.47% | 49.98% | 23.44% | -7.47% | 49.98% |
| BTC-USD | ETC-USD | 2020-08-14 | 84.65% | BULL | RECOVERY | DIFFERENT | MIXED | -6.61% | -12.09% | 10.56% | 20.57% | -22.64% | 35.47% |
| BTC-USD | XRP-USD | 2023-07-25 | 83.61% | BULL | BULL | DIFFERENT | MIXED | 0.55% | -4.77% | 17.39% | 0.89% | -4.77% | 17.39% |
| BTC-USD | DOGE-USD | 2020-08-14 | 83.28% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 36.50% | -12.20% | 36.50% | 158.34% | -12.20% | 202.68% |
| BTC-USD | THETA-USD | 2022-04-20 | 83.14% | RECOVERY | BEAR | DIFFERENT | BEARISH_30D | -16.53% | -16.53% | 23.44% | -18.80% | -23.27% | 23.44% |
| BTC-USD | XRP-USD | 2026-01-15 | 83.05% | BEAR | BEAR | DIFFERENT | MIXED | -5.83% | -6.97% | 3.52% | -22.62% | -23.73% | 3.52% |
| BTC-USD | LTC-USD | 2018-10-30 | 82.73% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 70.34% | 0.00% | 73.65% | 180.30% | 0.00% | 181.10% |
| DOGE-USD | SNX-USD | 2025-10-12 | 84.80% | DISTRIBUTION | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -32.40% | -36.26% | 0.00% | -27.09% | -36.26% | 0.00% |
| DOGE-USD | EGLD-USD | 2023-07-15 | 83.68% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 48.82% | 0.00% | 78.14% | 131.14% | 0.00% | 140.49% |
| DOGE-USD | SAND-USD | 2025-01-14 | 88.90% | BULL | BULL | DIFFERENT | MIXED | 3.56% | -8.98% | 23.97% | -21.92% | -21.92% | 23.97% |
| DOGE-USD | DOGE-USD | 2025-01-15 | 87.86% | BULL | BULL | DIFFERENT | BULLISH_30D | 23.48% | -6.52% | 36.30% | -9.92% | -17.06% | 36.30% |
| DOGE-USD | OP-USD | 2026-01-11 | 87.41% | BEAR | BEAR | DIFFERENT | MIXED | 3.89% | -3.44% | 39.02% | -16.51% | -26.63% | 39.02% |
| DOGE-USD | MANA-USD | 2025-01-15 | 86.11% | BULL | BULL | DIFFERENT | MIXED | -4.31% | -10.11% | 18.69% | -19.03% | -26.84% | 18.69% |
| DOGE-USD | HBAR-USD | 2020-08-16 | 86.01% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | -12.50% | -12.50% | 13.17% | 177.04% | -12.50% | 191.62% |
| DOGE-USD | ALGO-USD | 2025-01-14 | 85.86% | BULL | BULL | DIFFERENT | MIXED | 4.60% | -6.82% | 18.34% | -25.30% | -25.30% | 18.34% |
| DOGE-USD | KSM-USD | 2022-04-19 | 85.00% | BEAR | BEAR | DIFFERENT | BEARISH_30D | -28.63% | -28.63% | 6.88% | -34.98% | -36.50% | 6.88% |
| DOGE-USD | VET-USD | 2025-01-17 | 84.97% | BULL | BULL | DIFFERENT | MIXED | 1.03% | -8.45% | 18.77% | -22.61% | -29.05% | 18.77% |
| SOL-USD | VET-USD | 2023-07-27 | 70.65% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 17.49% | 0.00% | 18.85% | 81.45% | 0.00% | 98.04% |
| SOL-USD | 1INCH-USD | 2023-07-27 | 69.14% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 14.34% | 0.00% | 23.99% | 52.42% | 0.00% | 57.23% |
| SOL-USD | CRV-USD | 2023-08-03 | 69.09% | DISTRIBUTION | BEAR | SAME_BTC_ONLY | BULLISH_30D | 18.89% | -13.32% | 18.89% | -13.86% | -14.48% | 18.89% |
| SOL-USD | EOS-USD | 2018-11-13 | 81.37% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -6.92% | -16.43% | 8.85% | 33.78% | -16.43% | 48.92% |
| SOL-USD | MKR-USD | 2020-02-22 | 79.23% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -1.14% | -7.47% | 49.98% | 23.44% | -7.47% | 49.98% |
| SOL-USD | ZIL-USD | 2020-08-16 | 77.61% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 135.96% | 0.00% | 135.96% | 177.93% | 0.00% | 267.71% |
| SOL-USD | VET-USD | 2020-02-23 | 77.30% | RECOVERY | RECOVERY | DIFFERENT | EXPLOSIVE_60D | 41.53% | 0.00% | 46.55% | 159.81% | 0.00% | 201.34% |
| SOL-USD | BNB-USD | 2020-02-21 | 77.11% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -12.61% | -14.42% | 0.97% | 12.13% | -14.42% | 13.70% |
| SOL-USD | ZEC-USD | 2020-02-21 | 76.97% | RECOVERY | RECOVERY | DIFFERENT | MIXED | -4.23% | -9.12% | 6.45% | 32.15% | -9.12% | 32.15% |
| SOL-USD | BNB-USD | 2018-11-03 | 76.40% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 67.25% | -4.66% | 67.25% | 92.16% | -4.66% | 114.84% |

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

Generato: 2026-08-22 05:31 UTC


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
| BTC | 77.239 $ | +9 | CONFERMATO RIALZISTA | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | RANGE / FASE NON CHIARA | BASSO | SPOT OK / LONG SOLO PRUDENTE SU CONFERMA |
| SOL | 93,70 $ | +11 | CONFERMATO RIALZISTA | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | BASSO | TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME |
| DOGE | 0.09061 $ | +5 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | SOLO TRADING VELOCE / NO LEVA AGGRESSIVA |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 0 | +2 | +2 | +2 | +3 | 0 | 0 | +9 |
| SOL | 0 | +2 | +2 | +2 | +3 | 0 | +2 | +11 |
| DOGE | -2 | +2 | +2 | +1 | +3 | -1 | 0 | +5 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 76.029 $ | 77.991 $ | 66.910 $ | 57.748 $ | 2,52% | 16,55% | 0,48% |
| SOL | 85,25 $ | 98,27 $ | 83,81 $ | 64,42 $ | 3,58% | 19,75% | 8,91% |
| DOGE | 0.08930 $ | 0.09169 $ | 0.08643 $ | 0.06797 $ | 4,07% | 23,40% | -12,59% |

## Lettura dettagliata

### BTC

- Prezzo: **77.239 $**
- Score classico: **+9 / 12**
- Verdetto: **CONFERMATO RIALZISTA**
- Azione coerente: **SPOT OK / LONG SOLO PRUDENTE SU CONFERMA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,52%; distanza supporto 1,33%; distanza resistenza 1,24%

Dettaglio:

- Trend: **0** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+2** — RSI alto 85.0; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+2** — OBV sopra media; CMF neutrale 0.01; rialzo con volume sopra media
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 84.96 |
| MACD histogram | 1292.79098 |
| CMF20 | 0.014 |
| Volume ratio 20 | 3.07 |
| MA20 | 65.305 $ |
| MA50 | 64.545 $ |
| MA100 | 66.140 $ |
| MA200 | 68.967 $ |
| Pendenza MA50 20g | +1,85% |
| Pendenza MA200 60g | -9,94% |
| Bollinger width | 18,97% |
| Bollinger position | 1.30 |

### SOL

- Prezzo: **93,70 $**
- Score classico: **+11 / 12**
- Verdetto: **CONFERMATO RIALZISTA**
- Azione coerente: **TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME**
- Volatilità tecnica locale: **BASSO** — ATR14 3,58%; distanza supporto 9,43%; distanza resistenza 5,33%

Dettaglio:

- Trend: **0** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+2** — RSI alto 82.8; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+2** — OBV sopra media; CMF neutrale 0.04; rialzo con volume sopra media
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **0** — Doji / indecisione
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 82.80 |
| MACD histogram | 1.83173 |
| CMF20 | 0.037 |
| Volume ratio 20 | 4.73 |
| MA20 | 77,06 $ |
| MA50 | 76,88 $ |
| MA100 | 76,32 $ |
| MA200 | 81,15 $ |
| Pendenza MA50 20g | +2,67% |
| Pendenza MA200 60g | -16,40% |
| Bollinger width | 22,94% |
| Bollinger position | 1.26 |

### DOGE

- Prezzo: **0.09061 $**
- Score classico: **+5 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **SOLO TRADING VELOCE / NO LEVA AGGRESSIVA**
- Volatilità tecnica locale: **BASSO** — ATR14 4,07%; distanza supporto 0,80%; distanza resistenza 1,86%

Dettaglio:

- Trend: **-2** — prezzo sopra MA200 daily; MA50 daily in discesa; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+2** — RSI alto 82.7; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+1** — OBV sopra media; CMF negativo -0.19; rialzo con volume sopra media
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **-1** — Shooting star / rejection alto
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 82.72 |
| MACD histogram | 0.00194 |
| CMF20 | -0.190 |
| Volume ratio 20 | 5.58 |
| MA20 | 0.07177 $ |
| MA50 | 0.07233 $ |
| MA100 | 0.08136 $ |
| MA200 | 0.08935 $ |
| Pendenza MA50 20g | -4,28% |
| Pendenza MA200 60g | -16,52% |
| Bollinger width | 22,30% |
| Bollinger position | 1.41 |

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

Generato: 2026-08-22 05:32 UTC


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
| BTC | 77.239 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 49.952 $ | n/a | 33,75% | Fib 78,6% REJECTION (-1) @ 78.447 $ | BREAKOUT 60G | 74.959 $ |
| SOL | 93,70 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 51,22 $ | n/a | 45,46% | Fib 78,6% TESTATO (0) @ 93,12 $ | BREAKOUT 60G | 83,52 $ |
| DOGE | 0.09061 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 0.06214 $ | n/a | 33,30% | Fib 38,2% IN AVVICINAMENTO (0) @ 0.08779 $ | BREAKOUT 60G | 0.09044 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **13 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **49.952 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **33,75%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% REJECTION (-1) @ 78.447 $** — Swing DOWN 2026-05-06 82.792 -> 2026-08-14 62.488; livello più vicino 78.6% a 78.447; stato REJECTION; confluenza: resistenza tecnica.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **74.959 $**
- Resistenza: **77.991 $**
- Breakout 60g: **66.910 $**
- Breakdown 60g: **57.748 $**
- RSI14: **85.13**
- ATR14: **2,51%**
- Volume ratio 20g: **3.07**
- Rendimento 30g: **+16,85%**
- Rendimento 90g: **+0,74%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 24,13% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 13 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 65.402 $ | 2026-08-19 | 3g | 68.577 $ | 372,83% | n/a | 64.094 $ | Due minimi simili a 62.227 $ e 62.488 $. Neckline circa 65.402 $. Breakout neckline: 2026-08-19 (3 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 68.577 $; progresso: 372,83%; prezzo sopra neckline. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **13 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **64,42 $**
- Target teorico: **51,22 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **45,46%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% TESTATO (0) @ 93,12 $** — Swing DOWN 2026-05-11 98,27 -> 2026-08-16 74,20; livello più vicino 78.6% a 93,12; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **65,71 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Doji / indecisione**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **83,52 $**
- Resistenza: **93,83 $**
- Breakout 60g: **83,81 $**
- Breakdown 60g: **64,42 $**
- RSI14: **83.07**
- ATR14: **3,57%**
- Volume ratio 20g: **4.73**
- Rendimento 30g: **+20,27%**
- Rendimento 90g: **+9,39%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 32,54% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 13 giorni. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 3g | 85,65 $ | 207,68% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (3 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 207,68%; prezzo sopra neckline. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 78,73 $ | 2026-08-19 | 3g | 84,05 $ | 281,24% | n/a | 77,15 $ | Due minimi simili a 73,40 $ e 74,20 $. Neckline circa 78,73 $. Breakout neckline: 2026-08-19 (3 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05 $; progresso: 281,24%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-26 -> 2026-08-11**
- Età formazione: **11 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.06797 $**
- Target teorico: **0.06214 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **33,30%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 38,2% IN AVVICINAMENTO (0) @ 0.08779 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-08-12 0.06895; livello più vicino 38.2% a 0.08779; stato IN AVVICINAMENTO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.06933 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 11 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Shooting star / rejection alto**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **0.09044 $**
- Resistenza: **0.09169 $**
- Breakout 60g: **0.08643 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **83.08**
- ATR14: **4,04%**
- Volume ratio 20g: **5.58**
- Rendimento 30g: **+24,20%**
- Rendimento 90g: **-12,01%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.06214 $ | n/a | 33,30% | 0.06933 $ | Due massimi simili a 0.07380 $ e 0.07286 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 11 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 0.07923 $ | 2026-08-20 | 2g | 0.08952 $ | 110,63% | n/a | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06895 $. Neckline circa 0.07923 $. Breakout neckline: 2026-08-20 (2 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.08952 $; progresso: 110,63%; prezzo sopra neckline. |

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

Generato: 2026-08-22 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-22**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-06**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **93,70 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+61,86%**
- Aderenza live principale: **+70,53%**
- Errore medio live principale: **14,73%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **77**
- Osservazioni inclusive dal bottom: **78**
- Osservazioni da inizio programma/scanner: **51**
- Errore assoluto medio dal bottom: **11,72%**
- Errore assoluto medio da inizio programma: **14,73%**
- Gap firmato medio ultimi 7 giorni: **-9,21%**
- Errore assoluto medio ultimi 7 giorni: **10,50%**
- Gap ultimo giorno: **+4,51%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+4,51%**
- Gap firmato medio 7g: **-9,21%**
- Errore assoluto medio 7g: **10,50%**
- Variazione recente gap: **+12,08%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 68 | 2026-08-13 | 2023-01-28 | 76,18 $ | 90,72 $ | -16,03% | da inizio programma |
| 69 | 2026-08-14 | 2023-01-29 | 75,33 $ | 93,65 $ | -19,57% | da inizio programma |
| 70 | 2026-08-15 | 2023-01-30 | 75,27 $ | 89,97 $ | -16,34% | da inizio programma |
| 71 | 2026-08-16 | 2023-01-31 | 74,54 $ | 91,15 $ | -18,22% | da inizio programma |
| 72 | 2026-08-17 | 2023-02-01 | 75,94 $ | 93,45 $ | -18,74% | da inizio programma |
| 73 | 2026-08-18 | 2023-02-02 | 77,03 $ | 92,46 $ | -16,69% | da inizio programma |
| 74 | 2026-08-19 | 2023-02-03 | 85,37 $ | 92,37 $ | -7,58% | da inizio programma |
| 75 | 2026-08-20 | 2023-02-04 | 87,64 $ | 91,91 $ | -4,65% | da inizio programma |
| 76 | 2026-08-21 | 2023-02-05 | 87,64 $ | 90,43 $ | -3,09% | da inizio programma |
| 77 | 2026-08-22 | 2023-02-06 | 93,70 $ | 89,66 $ | +4,51% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-29 | 85,91 $ | 89,78 $ | 89,13 $ / 95,78 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-05 | 97,81 $ | 102,22 $ | 89,13 $ / 102,22 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-12 | 92,66 $ | 96,84 $ | 89,13 $ / 102,22 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-19 | 88,36 $ | 92,34 $ | 89,13 $ / 102,22 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-26 | 95,32 $ | 99,62 $ | 83,11 $ / 102,22 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-03 | 109,38 $ | 114,31 $ | 83,11 $ / 115,43 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-10 | 106,91 $ | 111,73 $ | 83,11 $ / 116,65 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-17 | 109,47 $ | 114,41 $ | 83,11 $ / 117,24 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-24 | 116,81 $ | 122,08 $ | 83,11 $ / 122,08 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-31 | 115,99 $ | 121,22 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-07 | 108,43 $ | 113,32 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-14 | 110,66 $ | 115,65 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-21 | 109,09 $ | 114,01 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-28 | 107,12 $ | 111,95 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-05 | 105,77 $ | 110,54 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-12 | 109,30 $ | 114,23 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-19 | 101,48 $ | 106,05 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-26 | 102,04 $ | 106,64 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 37 | 43,24% | 7,71% | 13,40% |
| 14g | 32 | 34,38% | 15,75% | 12,36% |
| 21g | 25 | 24,00% | 22,95% | 13,82% |
| 28g | 18 | 50,00% | 25,62% | 13,94% |
| 35g | 11 | 54,55% | 24,45% | 12,15% |
| 42g | 4 | 100,00% | 16,48% | 3,80% |
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

<!-- SOL_BTC_FRACTAL_HISTORY_START -->

---

# Storico frattale SOL/BTC

Per vedere la tabella giorno per giorno devi aprire/cliccare questo file:

**[sol_btc_fractal_history.md](sol_btc_fractal_history.md)**

Ultima lettura salvata: **2026-08-22** — SOL 93,70 $, gap +4,51%, somiglianza +61,86%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-08-22 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 78.430 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0104% | +0,83% | 3,22 | +1,96% | 0 $ | 0 $ |
| SOL | 99,08 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0116% | +2,53% | 0,82 | -4,64% | 0 $ | 0 $ |
| DOGE | 0.09866 $ | 3 | +1 | 0 | POSITIVA / CANDIDATA, ANCORA NON PESATA | MEDIA | 100% | +0,0101% | +14,08% | 1,28 | -2,18% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0460% | 173,49 mln $ | 0,02 | -19,44% |
| BTC | Bitget | OK | +0,0100% | 2,62 mld $ | 0,22 | +31,63% |
| BTC | Kucoin | OK | +0,0100% | 1,62 mld $ | 0,04 | +3,92% |
| SOL | Kraken | OK | +0,0571% | 31,08 mln $ | 1,02 | -19,30% |
| SOL | Bitget | OK | +0,0100% | 435,99 mln $ | 0,02 | +22,78% |
| SOL | Kucoin | OK | +0,0100% | 222,87 mln $ | 0,45 | -19,11% |
| DOGE | Kraken | OK | +0,0156% | 5,04 mln $ | 3,67 | +21,45% |
| DOGE | Bitget | OK | +0,0100% | 132,95 mln $ | 0,46 | -7,77% |
| DOGE | Kucoin | OK | +0,0100% | 146,10 mln $ | 1,62 | +12,80% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +100,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci rejection; nessuna conferma exchange netta. Confluenza tecnica dichiarata: resistenza tecnica.
- **RSI:** RSI alto ma sostenuto da acquisti e leva non estrema: momentum ancora credibile.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Resistenza vicina con acquisti aggressivi: breakout più credibile, ma serve chiusura sopra il livello.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+0,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 2, accuratezza +0,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 3, divergenze 0.
- Flusso taker/order book: **-0,25**.
- OI/funding/basis: **+1,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+3,00**; candidato: **+1**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 4, accuratezza +50,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 2, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+1,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci in_avvicinamento; nessuna conferma exchange netta.
- **RSI:** RSI alto ma sostenuto da acquisti e leva non estrema: momentum ancora credibile.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +57,50% | +3,62% | 1 | +0,00% | RACCOLTA DATI | 0,00 | +57,50% | +3,62% |
| SOL | +45,00% | -1,14% | 1 | +100,00% | RACCOLTA DATI | 0,00 | +45,00% | -1,14% |
| DOGE | +55,00% | +1,88% | 0 | n/a | RACCOLTA DATI | 0,00 | +55,00% | +1,88% |

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

Generato: 2026-08-22 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-22 | BTC | 78.429,65 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 3,22 | +0,83% | +1,96% |
| 2026-08-22 | DOGE | 0.09866 | V2.1.3 | OK | 1 | 0 | 3,00 | MEDIA | 1,28 | +14,08% | -2,18% |
| 2026-08-22 | SOL | 99,08 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,82 | +2,53% | -4,64% |
| 2026-08-21 | BTC | 75.096,70 | V2.1.3 | OK | 0 | 0 | 0,25 | BASSA | 1,07 | -3,95% | -2,94% |
| 2026-08-21 | DOGE | 0.08238 | V2.1.3 | OK | 0 | 0 | 3,50 | ALTA | 1,46 | +11,21% | -0,84% |
| 2026-08-21 | SOL | 89,44 | V2.1.3 | OK | 1 | 0 | 3,25 | ALTA | 1,57 | +8,30% | -6,87% |
| 2026-08-20 | BTC | 69.515,36 | V2.1.3 | OK | 0 | 0 | 2,25 | ALTA | 1,03 | +8,86% | +1,47% |
| 2026-08-20 | DOGE | 0.07482 | V2.1.3 | OK | 1 | 0 | 3,25 | ALTA | 1,31 | +2,01% | +4,59% |
| 2026-08-20 | SOL | 84,87 | V2.1.3 | OK | 0 | 0 | 2,00 | MEDIA | 1,16 | -13,35% | +3,32% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 3 | +66,67% | +1,62% | +1,05% | +5,09% | FEEDBACK RAPIDO |
| SOL | 3g | 2 | +0,00% | -1,86% | -2,68% | +1,44% | FEEDBACK RAPIDO |
| SOL | 7g | 2 | +0,00% | -3,56% | -4,18% | +1,44% | FEEDBACK RAPIDO |
| SOL | 14g | 1 | +0,00% | -5,72% | -9,55% | +0,73% | FEEDBACK RAPIDO |
| SOL | 30g | 1 | +100,00% | +8,60% | -9,55% | +9,55% | FEEDBACK RAPIDO |
| DOGE | 1g | 5 | +60,00% | +2,90% | +2,11% | +3,72% | FEEDBACK RAPIDO |
| DOGE | 3g | 4 | +50,00% | +1,09% | -0,86% | +4,99% | FEEDBACK RAPIDO |
| DOGE | 7g | 4 | +50,00% | +0,28% | -0,90% | +5,64% | FEEDBACK RAPIDO |
| DOGE | 14g | 3 | +33,33% | -6,28% | -1,38% | +10,89% | FEEDBACK RAPIDO |
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

**SOL** — SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**DOGE** — DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 77.239 $ | +0.0100% | -12.72% | 1.33 | Rischio sotto | 2/5 |
| SOL | 93,70 $ | +0.0100% | -23.06% | 2.29 | Rischio sotto | 2/5 |
| DOGE | 0.09061 $ | +0.0100% | -30.08% | 4.93 | Rischio sotto | 2/5 |

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

Generato: 2026-08-22 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily              | Stato D    | Weekly             | Stato W       | Lettura weekly                                                                                                              |   Peso |
|:--------|:-------------------|:-----------|:-------------------|:--------------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish     | CONFERMATA | Conferma rialzista | CONTESTO      | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| SOL     | Conferma rialzista | CONTESTO   | Hidden bearish     | CONFERMATA    | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| DOGE    | Conferma rialzista | CONTESTO   | Hidden bearish     | IN_FORMAZIONE | Hidden bearish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.                 |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo               | Stato         | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:-------------------|:--------------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish     | CONFERMATA    | 77.105 $ / 85,01  | 2026-08-03 62.227 $ / RSI 47,40 → 2026-08-14 62.488 $ / RSI 42,71   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Conferma rialzista | CONTESTO      | 77.105 $ / 56,09  | n/a                                                                 | +20,93%             | 17,61            |      0 |
| SOL     | 1D   | Conferma rialzista | CONTESTO      | 93,46 $ / 82,91   | n/a                                                                 | +26,91%             | 36,22            |      0 |
| SOL     | 1W   | Hidden bearish     | CONFERMATA    | 93,46 $ / 53,45   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Conferma rialzista | CONTESTO      | 0.09047 $ / 83,00 | n/a                                                                 | +29,94%             | 41,16            |      0 |
| DOGE    | 1W   | Hidden bearish     | IN_FORMAZIONE | 0.09047 $ / 48,09 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09976 $ / RSI 48,09 | n/a                 | n/a              |      0 |

### BTC

- **1D — Hidden bullish / CONFERMATA**: Hidden bullish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### SOL

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Hidden bearish / IN_FORMAZIONE**: Hidden bearish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **8**.
- Soglie di lettura: **30 / 60 / 100 controlli**.
- Anche oltre le soglie il peso resta **0** finché non viene presa una decisione esplicita.

| Asset   | TF   | Tipo             |   Orizzonte |   Controlli | Accuratezza   | Return corretto   | Stato         |   Peso |
|:--------|:-----|:-----------------|------------:|------------:|:--------------|:------------------|:--------------|-------:|
| BTC     | 1D   | Bullish regolare |          30 |           1 | 0,00%         | -1,52%            | RACCOLTA DATI |      0 |
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

Generato: 2026-08-22 05:32 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto          | Trend           | Momentum                  | Struttura                                          |   Pattern score | Fibonacci            | Pattern rialzista                | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:------------------|:----------------|:--------------------------|:---------------------------------------------------|----------------:|:---------------------|:---------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 77.239 $ | 10 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Compressione / triangolo | 0 | -1 / REJECTION | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 62.488 | 77.991 |
| SOL | 93,70 $ | 10 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Compressione / triangolo | 0 | 0 / TESTATO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 74,20 | 98,27 |
| DOGE | 0.09061 $ | 7 | RIALZISTA TECNICO | Trend misto | Momentum in miglioramento | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / IN AVVICINAMENTO | Triplo minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 0.06895 | 0.09169 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 85.13 | 1305.58 | 65.315 | 64.549 | 68.968 | 1,89% | -9,79% | 18,75% | 0,34% |
| SOL | 83.07 | 1.8579 | 77,08 | 76,89 | 81,15 | 2,55% | -16,13% | 23,52% | 9,91% |
| DOGE | 83.08 | 0.00198 | 0.07180 | 0.07234 | 0.08935 | -3,83% | -16,28% | 31,07% | -11,34% |

## Dettaglio asset

### BTC

- Prezzo: **77.239 $**
- Punteggio tecnico: **10 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 6.223e+04 -> 6.249e+04. Ultimi massimi: 6.691e+04 -> 6.54e+04.
- Divergenza: **Divergenza rialzista nascosta RSI** (1)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **REJECTION** (-1)
  - Swing DOWN 2026-05-06 82.792 -> 2026-08-14 62.488; livello più vicino 78.6% a 78.447; stato REJECTION; confluenza: resistenza tecnica.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **62.488**
- Resistenza più vicina: **77.991**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 62.201 tra 2026-06-18 e 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (3 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 219,36%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (3g); progresso 219,36%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (3 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 219,36%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (3g); progresso 219,36%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 59.109 dal 2026-06-05 al 2026-08-14. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Breakout neckline: 2026-08-19 (3 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 75.387; progresso corrente: 122,75%. Relazione prezzo/neckline: sopra neckline.
  - neckline 67.248; target 75.387; breakout 2026-08-19 (3g); progresso 122,75%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 33,75%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 33,75%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 32 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 33,75%; prezzo sopra neckline.

### SOL

- Prezzo: **93,70 $**
- Punteggio tecnico: **10 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 70.69 -> 74.2. Ultimi massimi: 78.73 -> 77.62.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TESTATO** (0)
  - Swing DOWN 2026-05-11 98,27 -> 2026-08-16 74,20; livello più vicino 78.6% a 93,12; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **74,20**
- Resistenza più vicina: **98,27**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 73,40 tra 2026-07-17 e 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (3 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05; progresso corrente: 281,24%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 84,05; breakout 2026-08-19 (3g); progresso 281,24%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (3 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 186,44%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (3g); progresso 186,44%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Breakout neckline: 2026-08-19 (3 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 99,70; progresso corrente: 62,25%. Relazione prezzo/neckline: sopra neckline.
  - neckline 83,81; target 99,70; breakout 2026-08-19 (3g); progresso 62,25%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 45,46%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 32,54%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 77,62 dal 2026-06-15 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 45,46%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.09061 $**
- Punteggio tecnico: **7 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend misto** (1)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 0.06835 -> 0.06895. Ultimi massimi: 0.07117 -> 0.07286.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 45,02%. Fase non abbastanza chiara.
- Fibonacci automatico: **IN AVVICINAMENTO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-08-12 0.06895; livello più vicino 38.2% a 0.08779; stato IN AVVICINAMENTO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Triplo minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.06895**
- Resistenza più vicina: **0.09169**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (3 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 304,95%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (3g); progresso 304,95%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06835 dal 2026-06-30 al 2026-08-12. Neckline stimata: 0.07923. Breakout neckline: 2026-08-20 (2 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.09012; progresso corrente: 104,51%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07923; target 0.09012; breakout 2026-08-20 (2g); progresso 104,51%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-07-24 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (3 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 304,95%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (3g); progresso 304,95%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 11 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 33,30%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 11 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 33,30%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 11 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 33,30%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato            | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------------|:--------------------------------|--------:|
| BTC | DOWN 2026-05-06 -> 2026-08-14 | 67.280 | 70.244 | 72.640 | 75.036 | 78.447 | 78.6% / 78.447 | REJECTION | resistenza tecnica | -1 |
| SOL | DOWN 2026-05-11 -> 2026-08-16 | 79,88 | 83,40 | 86,24 | 89,07 | 93,12 | 78.6% / 93,12 | TESTATO | nessuna confluenza indipendente | 0 |
| DOGE | DOWN 2026-05-14 -> 2026-08-12 | 0.08059 | 0.08779 | 0.09360 | 0.09942 | 0.10770 | 38.2% / 0.08779 | IN AVVICINAMENTO | nessuna confluenza indipendente | 0 |

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

- **BTC**: 21/30 previsioni controllate su 49 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 21/30 previsioni controllate su 49 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 21/30 previsioni controllate su 49 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 49 | 21 | 21/30 [███████░░░] | 28 | RACCOLTA DATI | 2026-08-23 / tra 1 giorno |
| SOL | 49 | 21 | 21/30 [███████░░░] | 28 | RACCOLTA DATI | 2026-08-23 / tra 1 giorno |
| DOGE | 49 | 21 | 21/30 [███████░░░] | 28 | RACCOLTA DATI | 2026-08-23 / tra 1 giorno |

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

Generato: 2026-08-22 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 3 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 77.239 $          | 77.239 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.09061 $         | 0.09061 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 93,70 $           | 93,70 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 77.239 $          | 77.239 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 93,70 $           | 93,70 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.09061 $         | 0.09061 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 77.239 $          | 77.239 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 93,70 $           | 93,70 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.09061 $         | 0.09061 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 77.239 $          | 77.239 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 93,70 $           | 93,70 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.09061 $         | 0.09061 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 77.239 $          | 77.239 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 93,70 $           | 93,70 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.09061 $         | 0.09061 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | WARN    | 77.239 $          | 78.430 $        | +1,5410%     |
| Exchange Microstructure | SOL     | price             | WARN    | 93,70 $           | 99,08 $         | +5,7385%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.09061 $         | 0.09866 $       | +8,8842%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 93,70 $           | 93,70 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 93,70 $           | 93,70 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 93,70 $           | 93,70 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 93,70 $           | 93,70 $         | +0,0000%     |

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

<!-- SOL_SPOT_ADAPTIVE_START -->
# SOL Spot Adaptive Range — paper trading separato

Generato: 2026-08-23T00:30:34+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €43.453,09 | €43.452,45 | 0.006825 | 93.8210 | +8.63% | €3.452,96 | €75,44 | 6.48% | 29 |

**Ultima decisione:** SELL_40_PERCENT — SOL sopra la seconda banda adattiva.

Bande 4H: L2 80.2419 · L1 82.6785 · media 85.7243 · U1 88.7701 · U2 91.2068.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
