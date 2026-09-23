<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-09-23 05:32 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +7 | BULLISH | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | +4 | NEUTRALE / COSTRUTTIVO | HOLD / TRANCHE PICCOLE, NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +2 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+7**, spot = **ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+4**, spot = **HOLD / TRANCHE PICCOLE, NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+2**, spot = **STAI ALLA FINESTRA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+7**
- Confluenza: **POSITIVA FORTE**
- Bias Global: **Rialzista**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA**
- Long leva: **LONG PRUDENTE**
- Short leva: **NO SHORT**
- Rischio: **MEDIO**
- Conferme: Prima resistenza sopra 82.262; conferma del doppio minimo sopra 82.262.
- Invalidazioni: Sotto 74.945 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+4**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / TRANCHE PICCOLE, NO LEVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 107,12; milestone analogiche 166,95 / 179,63, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 113,00 / 96,23 / 62,19.

### DOGE

- Global Confluence: **+2**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **STAI ALLA FINESTRA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.11825 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.07841 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 1; EMA200 circa 111,29 $; upside verso EMA200 -6,44%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-09-23T05:33:20+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-17T17:30:04+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-17T17:30:04+00:00 | 2026-09-17T17:30:04+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-17T17:00:00+00:00 | 2026-09-17T17:00:00+00:00 | 15,3 min | 25,0 min | OK |
| 60m | 12 | 2026-09-17T16:00:00+00:00 | 2026-09-17T16:00:00+00:00 | 30,3 min | 45,0 min | OK |
| 240m | 12 | 2026-09-17T12:00:00+00:00 | 2026-09-17T12:00:00+00:00 | 1,50 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Balanced V3 Long Only V1 | ZEC | 60m | LONG | 6,75 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Balanced V3 Long Only V1 | NEAR | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 Short Only V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 Short Only V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 Short Only V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend Side Regime Guard V1 | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh Regime Guard V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh Regime Guard V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh Regime Guard V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh Regime Guard V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Side Regime Guard V1 | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Partial 1R V1 | ZEC | 60m | LONG | 6,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Partial 1R V1 | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Quality7 V1 | BR | 60m | LONG | 7,75 | 7,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive Quality7 V1 | ARB | 60m | LONG | 8,25 | 7,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Adaptive | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Trend | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Btc 2 3 V1 | ZEC | 60m | LONG | 6,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Btc 2 3 V1 | NEAR | 60m | LONG | 7,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Btc 2 3 V1 | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | ZEC | 60m | LONG | 6,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | NEAR | 60m | LONG | 7,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | ZEC | 60m | LONG | 6,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | NEAR | 60m | LONG | 7,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark trend following EMA 1H | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Bollinger mean reversion 1H | ZEC | 60m | LONG | 6,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Donchian 1H Gb20 120R V1 | NEAR | 60m | LONG | 7,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Donchian breakout 1H | NEAR | 60m | LONG | 7,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | BR | 60m | LONG | 7,75 | 5,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | NEAR | 60m | LONG | 7,25 | 4,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | BR | 60m | LONG | 7,75 | 4,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Stress Guard V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Stress Guard V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Stress Guard V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | BR | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Long Btc 1 3 Cap75 V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Long Btc 1 3 Cap75 V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Long Btc 1 3 Cap75 V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 V1 | ZEC | 60m | LONG | 6,75 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 V1 | NEAR | 60m | LONG | 7,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 V1 | HYPE | 60m | LONG | 4,96 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Cost Aware V1 | ZEC | 60m | LONG | 6,75 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | 60m | LONG | 6,75 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 No Trend Up V1 | NEAR | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | ZEC | 60m | LONG | 6,75 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | NEAR | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V3 Filtered | ZEC | 60m | LONG | 6,75 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V3 Filtered | NEAR | 60m | LONG | 7,25 | 6,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | BR | 60m | LONG | 7,75 | 5,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V1 | NEAR | 60m | LONG | 7,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V1 | BR | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | NEAR | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | ARB | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | BR | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 5,87 | 6,00 | 0,13 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | POWER | 240m | LONG | 4,25 | 6,00 | 1,75 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -3,54 | 6,00 | 2,46 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 2,85 | 6,00 | 3,15 | STALE_CANDLE | 1,50 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 2,25 | 6,00 | 3,75 | STALE_CANDLE | 1,50 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 1,75 | 6,00 | 4,25 | STALE_CANDLE | 1,50 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -1,11 | 6,00 | 4,89 | STALE_CANDLE | 1,50 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 90.3 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | ARB | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | ARB | 60m | LONG | 8,25 | 5,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | ARB | 60m | LONG | 8,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | ARB | 60m | LONG | 8,25 | 4,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | ARB | 60m | LONG | 8,25 | 4,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | ARB | 60m | LONG | 8,25 | 5,50 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | ARB | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | ARB | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Btc 2 3 V1 | ARB | 60m | LONG | 8,25 | 5,00 | 0,00 | OPENED | 30,3 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.723,97 | -2,76% | €-84,59 | €3.000,00 | -2,82% | 6 | 64 | 40,62% | 0,78 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 64 | 3853 | PRIME INDICAZIONI | 100 (mancano 36) |

- Trade del Principale 4H chiusi: **64**; win rate **40,62%**; profit factor **0,78**.
- Expectancy: **€-5,90** per trade; P&L netto: **€-377,40**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.723,97 | €712,23 | €2.136,68 | €194,09 | €102,67 |
| TEST | Benchmark Donchian breakout 1H | 2 | €12.001,47 | €1.978,78 | €3.957,56 | €119,87 | €35,47 |
| TEST | Donchian 1H Gb20 120R V1 | 2 | €11.718,91 | €1.932,19 | €3.864,39 | €117,05 | €34,63 |
| TEST | Combo Trend Side Regime Guard V1 | 4 | €11.170,76 | €1.851,39 | €3.702,77 | €110,65 | €221,28 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 3 | €11.111,19 | €1.519,40 | €4.558,19 | €111,13 | €41,67 |
| TEST | Main Side Regime Guard V1 | 2 | €10.997,72 | €377,83 | €1.133,50 | €68,97 | €-2,49 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 4 | €10.878,29 | €2.474,36 | €7.423,07 | €163,23 | €34,08 |
| TEST | Rapida 1H V2 | 0 | €10.617,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 1 | €10.599,64 | €43,70 | €87,39 | €0,00 | €7,49 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 5 | €10.584,83 | €1.614,98 | €4.844,93 | €159,37 | €39,53 |
| TEST | Combo Adaptive | 5 | €10.565,78 | €1.413,33 | €2.826,66 | €55,43 | €120,56 |
| TEST | 1H Fast No Pepe V1 | 4 | €10.498,96 | €1.270,67 | €3.812,02 | €209,78 | €-42,29 |
| TEST | Scanner Top15 Long | 4 | €10.483,87 | €1.904,73 | €3.809,46 | €209,68 | €-0,76 |
| TEST | Scanner Top20 Long | 4 | €10.483,87 | €1.904,73 | €3.809,46 | €209,68 | €-0,76 |
| TEST | Combo Adaptive Long Only V1 | 0 | €10.452,65 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €10.328,16 | €1.575,31 | €4.725,92 | €155,46 | €38,61 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 5 | €10.298,42 | €1.377,32 | €2.754,64 | €53,64 | €112,75 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.264,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.261,81 | €1.565,18 | €4.695,55 | €154,46 | €38,36 |
| TEST | Combo Adaptive Partial 1R V1 | 4 | €10.247,80 | €1.856,83 | €3.713,66 | €102,49 | €114,26 |
| TEST | 1H Fast Tp2 V1 | 4 | €10.242,39 | €1.239,27 | €3.717,81 | €204,52 | €-41,16 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.235,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.205,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.203,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.202,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.180,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.175,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €10.138,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 0 | €10.110,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.101,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 1 | €10.054,87 | €50,00 | €750,00 | €16,81 | €-6,04 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.040,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.019,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 1 | €10.016,21 | €50,00 | €750,00 | €16,81 | €-6,04 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 1 | €10.010,97 | €10,00 | €150,00 | €3,36 | €-1,21 |
| TEST | 1H Fast V3 Nohigh V1 | 4 | €10.009,40 | €1.520,29 | €4.560,86 | €150,17 | €37,67 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 1 | €10.007,47 | €50,00 | €750,00 | €16,81 | €-6,04 |
| TEST | Sol Ema 4H | 0 | €10.005,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 1 | €10.003,24 | €10,00 | €150,00 | €3,36 | €-1,21 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.002,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 1 | €10.001,49 | €10,00 | €150,00 | €3,36 | €-1,21 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.997,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.993,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 1 | €9.992,97 | €89,18 | €445,89 | €10,00 | €-3,59 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.988,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.985,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 4 | €9.982,65 | €286,89 | €573,77 | €54,81 | €-2,05 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 1 | €9.973,01 | €47,66 | €95,32 | €0,00 | €8,17 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.966,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.964,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 1 | €9.964,67 | €35,25 | €70,50 | €0,00 | €6,05 |
| TEST | Forza relativa 1H V2 | 3 | €9.963,40 | €1.253,06 | €2.506,12 | €99,64 | €100,89 |
| TEST | 1H Fast Nohigh Cap75 V1 | 5 | €9.961,68 | €1.513,13 | €4.539,38 | €149,77 | €-1,93 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 1 | €9.957,95 | €88,87 | €444,33 | €9,96 | €-3,58 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.955,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 1 | €9.952,79 | €88,82 | €444,10 | €9,96 | €-3,58 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.940,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.939,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.935,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.934,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.927,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.914,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.912,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 5 | €9.894,26 | €1.509,13 | €4.527,38 | €148,93 | €36,99 |
| TEST | Sol Ema 1H | 0 | €9.874,85 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.868,16 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.810,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.808,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €9.793,92 | €1.174,50 | €3.523,50 | €97,95 | €47,75 |
| TEST | Eth Ema 4H | 0 | €9.783,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.779,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.775,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 4 | €9.772,40 | €1.619,63 | €3.239,26 | €96,80 | €193,58 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.761,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 5 | €9.713,57 | €1.475,44 | €4.426,32 | €146,04 | €-1,88 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.684,07 | €1.477,07 | €4.431,20 | €145,77 | €36,20 |
| TEST | Eth Donchian 1H | 0 | €9.676,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.605,65 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.595,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.546,20 | €1.456,04 | €4.368,12 | €143,69 | €35,69 |
| TEST | Combo Adaptive Regime V1 | 0 | €9.543,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 1 | €9.540,84 | €199,57 | €399,13 | €47,90 | €-38,14 |
| TEST | Scanner Bottom15 Short | 1 | €9.540,84 | €199,57 | €399,13 | €47,90 | €-38,14 |
| TEST | Scanner Bottom20 Short | 1 | €9.540,84 | €199,57 | €399,13 | €47,90 | €-38,14 |
| TEST | Bilanciata 1H V2 | 2 | €9.518,32 | €439,62 | €1.318,87 | €95,19 | €-0,26 |
| TEST | Combo Adaptive Quality7 V1 | 3 | €9.496,47 | €1.234,41 | €2.468,82 | €94,97 | €78,28 |
| TEST | Combo Trend | 4 | €9.476,65 | €1.570,61 | €3.141,23 | €93,87 | €187,72 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 1 | €9.474,72 | €198,18 | €396,37 | €47,56 | €-37,87 |
| TEST | Scanner Top5 Btc Tp3 V1 | 1 | €9.471,84 | €356,44 | €712,87 | €0,00 | €61,12 |
| TEST | Scanner Top5 Btc Runner25 V1 | 1 | €9.466,30 | €356,23 | €712,46 | €0,00 | €61,09 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 1 | €9.460,31 | €197,88 | €395,77 | €47,49 | €-37,81 |
| TEST | Eth Adaptive 1H | 0 | €9.459,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 3 | €9.425,94 | €1.288,95 | €3.866,84 | €94,28 | €35,35 |
| TEST | Eth Ema 1H | 0 | €9.414,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 0 | €9.401,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 1 | €9.387,51 | €196,36 | €392,72 | €47,13 | €-37,52 |
| TEST | 1H Fast Score 6 75 V1 | 3 | €9.387,06 | €1.283,63 | €3.850,89 | €93,89 | €35,20 |
| TEST | Btc Ema 1H | 0 | €9.353,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 0 | €9.351,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 1 | €9.341,39 | €33,05 | €66,09 | €0,00 | €5,67 |
| TEST | 1H Balanced V3 Long Only V1 | 4 | €9.266,08 | €1.111,20 | €3.333,60 | €92,67 | €45,17 |
| TEST | Master Adaptive Gb20 Be V1 | 1 | €9.207,83 | €435,60 | €871,21 | €44,29 | €75,41 |
| TEST | Master Adaptive Gb20 Partial V1 | 1 | €9.198,03 | €435,14 | €870,28 | €44,25 | €75,33 |
| TEST | Bilanciata 1H V1 | 4 | €9.183,29 | €1.066,41 | €3.199,23 | €137,77 | €71,45 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 0 | €9.182,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.172,73 | €389,09 | €778,18 | €39,56 | €67,35 |
| TEST | Master Adaptive V1 | 1 | €9.162,46 | €433,46 | €866,91 | €44,08 | €75,03 |
| TEST | Combo Adaptive Runner25 V1 | 3 | €9.043,82 | €117,83 | €235,66 | €7,15 | €1,20 |
| TEST | Master Adaptive Gb20 V1 | 1 | €9.041,56 | €427,66 | €855,33 | €43,49 | €74,03 |
| TEST | Combo Adaptive Mfe Trail | 1 | €9.040,47 | €31,44 | €62,87 | €0,00 | €5,39 |
| TEST | Master Adaptive Expanded V1 | 0 | €8.985,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 4 | €8.977,51 | €1.631,05 | €3.262,10 | €179,56 | €-0,65 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €8.930,52 | €2.039,57 | €6.118,70 | €134,00 | €32,85 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 0 | €8.928,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 3 | €8.928,44 | €1.679,96 | €5.039,89 | €133,97 | €-1,01 |
| TEST | Combo Adaptive Tp3 V1 | 3 | €8.874,63 | €115,65 | €231,30 | €7,01 | €1,17 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 1 | €8.664,18 | €368,96 | €737,91 | €0,00 | €63,27 |
| TEST | Forza relativa 1H V1 | 6 | €8.624,96 | €1.478,48 | €2.956,96 | €172,50 | €-32,80 |
| TEST | Combo Mean Reversion | 1 | €8.555,31 | €653,10 | €1.306,20 | €43,35 | €24,41 |
| TEST | Master Adaptive Strict3 V1 | 0 | €8.448,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €8.413,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 1 | €8.257,45 | €366,47 | €732,95 | €0,00 | €62,85 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 1 | €8.221,92 | €341,89 | €683,78 | €0,00 | €58,63 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €8.144,60 | €1.123,08 | €2.246,17 | €80,78 | €22,35 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.723,97 | €-377,40 | 64 | 64 | 40,62% | 0,78 | €-5,90 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €12.001,47 | €1.968,38 | 171 | 171 | 45,03% | 1,56 | €11,51 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.718,91 | €1.686,60 | 139 | 139 | 43,88% | 1,64 | €12,13 | 6,75% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.170,76 | €1.070,58 | 163 | 163 | 50,31% | 1,35 | €6,57 | 10,10% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.111,19 | €1.152,82 | 216 | 216 | 49,54% | 1,27 | €5,34 | 7,95% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.997,72 | €1.000,64 | 63 | 63 | 55,56% | 1,94 | €15,88 | 7,33% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.878,29 | €927,10 | 186 | 186 | 48,92% | 1,25 | €4,98 | 5,29% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.617,99 | €617,99 | 92 | 82 | 48,91% | 1,28 | €6,72 | 3,89% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.599,64 | €592,20 | 198 | 198 | 44,44% | 1,17 | €2,99 | 8,85% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.584,83 | €624,83 | 185 | 185 | 49,19% | 1,22 | €3,38 | 5,24% |
| TEST | Combo Adaptive | Combo Adaptive | €10.565,78 | €655,55 | 233 | 233 | 46,78% | 1,19 | €2,81 | 8,17% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.498,96 | €620,41 | 301 | 301 | 44,19% | 1,13 | €2,06 | 9,28% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.483,87 | €486,92 | 222 | 222 | 47,75% | 1,14 | €2,19 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.483,87 | €486,92 | 222 | 222 | 47,75% | 1,14 | €2,19 | 10,31% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.452,65 | €452,65 | 194 | 194 | 44,85% | 1,14 | €2,33 | 7,78% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.328,16 | €367,23 | 240 | 240 | 49,17% | 1,09 | €1,53 | 9,50% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.298,42 | €387,82 | 183 | 183 | 44,26% | 1,13 | €2,12 | 11,68% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.264,13 | €264,13 | 26 | 26 | 38,46% | 1,36 | €10,16 | 3,39% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.261,81 | €300,63 | 284 | 284 | 44,72% | 1,06 | €1,06 | 9,48% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.247,80 | €333,37 | 191 | 191 | 45,55% | 1,12 | €1,75 | 8,69% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.242,39 | €325,01 | 293 | 293 | 40,27% | 1,07 | €1,11 | 6,56% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.235,99 | €235,99 | 23 | 23 | 56,52% | 1,56 | €10,26 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.205,57 | €205,57 | 121 | 121 | 42,15% | 1,08 | €1,70 | 7,07% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.203,50 | €203,50 | 9 | 9 | 77,78% | 2,77 | €22,61 | 0,85% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.202,44 | €202,44 | 20 | 20 | 60,00% | 1,43 | €10,12 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Doge Ema 1H | Trend following EMA | €10.180,44 | €180,44 | 31 | 31 | 61,29% | 1,28 | €5,82 | 2,77% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.175,88 | €175,88 | 77 | 77 | 44,16% | 1,11 | €2,28 | 6,49% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.138,72 | €138,72 | 10 | 10 | 50,00% | 1,64 | €13,87 | 1,37% |
| TEST | Combo Scanner | Combo Scanner | €10.110,81 | €110,81 | 197 | 197 | 43,65% | 1,03 | €0,56 | 11,38% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.101,88 | €101,88 | 4 | 4 | 75,00% | 2,86 | €25,47 | 0,91% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.054,87 | €61,36 | 33 | 33 | 48,48% | 1,43 | €1,86 | 0,33% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.040,14 | €40,14 | 9 | 9 | 33,33% | 1,15 | €4,46 | 2,25% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.019,53 | €19,53 | 12 | 12 | 50,00% | 1,39 | €1,63 | 0,36% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.016,21 | €22,70 | 6 | 6 | 66,67% | 1,87 | €3,78 | 0,31% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.010,97 | €12,27 | 33 | 33 | 48,48% | 1,43 | €0,37 | 0,07% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €10.009,40 | €47,47 | 211 | 211 | 45,02% | 1,02 | €0,22 | 7,10% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.007,47 | €13,96 | 18 | 18 | 44,44% | 1,25 | €0,78 | 0,53% |
| TEST | Sol Ema 4H | Trend following EMA | €10.005,51 | €5,51 | 11 | 11 | 36,36% | 1,02 | €0,50 | 2,27% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,24 | €4,54 | 6 | 6 | 66,67% | 1,87 | €0,76 | 0,06% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.002,17 | €2,17 | 15 | 15 | 40,00% | 1,01 | €0,14 | 1,80% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,49 | €2,79 | 18 | 18 | 44,44% | 1,25 | €0,16 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.997,71 | €-2,29 | 12 | 12 | 33,33% | 0,62 | €-0,19 | 0,04% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.993,20 | €-6,80 | 5 | 5 | 20,00% | 0,05 | €-1,36 | 0,07% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.992,97 | €-3,17 | 6 | 6 | 66,67% | 0,86 | €-0,53 | 0,30% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.988,57 | €-11,43 | 12 | 12 | 33,33% | 0,62 | €-0,95 | 0,21% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.985,57 | €-14,43 | 22 | 22 | 36,36% | 0,31 | €-0,66 | 0,17% |
| TEST | Ampia 4H | Confluenza trend | €9.982,65 | €-14,92 | 65 | 65 | 33,85% | 0,99 | €-0,23 | 4,45% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.973,01 | €-35,11 | 205 | 205 | 44,88% | 0,99 | €-0,17 | 10,31% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.966,02 | €-33,98 | 5 | 5 | 20,00% | 0,05 | €-6,80 | 0,34% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.964,84 | €-35,16 | 4 | 4 | 25,00% | 0,77 | €-8,79 | 1,10% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.964,67 | €-41,33 | 164 | 164 | 44,51% | 0,99 | €-0,25 | 11,27% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.963,40 | €-29,08 | 153 | 146 | 41,18% | 0,99 | €-0,19 | 10,88% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.961,68 | €38,77 | 227 | 227 | 42,29% | 1,01 | €0,17 | 10,86% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.957,95 | €-38,20 | 33 | 33 | 48,48% | 0,78 | €-1,16 | 0,84% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.955,89 | €-44,11 | 5 | 5 | 20,00% | 0,09 | €-8,82 | 0,45% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.952,79 | €-43,37 | 18 | 18 | 38,89% | 0,56 | €-2,41 | 0,89% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.940,92 | €-59,08 | 22 | 22 | 31,82% | 0,53 | €-2,69 | 0,73% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.939,78 | €-60,22 | 16 | 16 | 50,00% | 0,85 | €-3,76 | 1,98% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.935,18 | €-64,82 | 58 | 58 | 50,00% | 0,95 | €-1,12 | 4,27% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.934,84 | €-65,16 | 14 | 14 | 50,00% | 0,80 | €-4,65 | 2,06% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.927,87 | €-72,13 | 22 | 22 | 36,36% | 0,31 | €-3,28 | 0,86% |
| TEST | Btc Ema 4H | Trend following EMA | €9.914,14 | €-85,86 | 5 | 5 | 20,00% | 0,58 | €-17,17 | 1,76% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.912,62 | €-87,38 | 29 | 29 | 44,83% | 0,89 | €-3,01 | 4,59% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.894,26 | €-68,31 | 274 | 274 | 41,97% | 0,99 | €-0,25 | 10,60% |
| TEST | Sol Ema 1H | Trend following EMA | €9.874,85 | €-125,15 | 31 | 31 | 38,71% | 0,87 | €-4,04 | 4,45% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.868,16 | €-131,84 | 12 | 12 | 50,00% | 0,70 | €-10,99 | 4,16% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.810,21 | €-189,79 | 58 | 58 | 46,55% | 0,86 | €-3,27 | 5,41% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.808,89 | €-191,11 | 7 | 7 | 14,29% | 0,41 | €-27,30 | 2,43% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.793,92 | €-156,51 | 230 | 230 | 41,74% | 0,96 | €-0,68 | 14,04% |
| TEST | Eth Ema 4H | Trend following EMA | €9.783,14 | €-216,86 | 9 | 9 | 22,22% | 0,41 | €-24,10 | 2,32% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.779,96 | €-220,04 | 23 | 23 | 39,13% | 0,66 | €-9,57 | 3,93% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.775,84 | €-224,16 | 20 | 20 | 40,00% | 0,67 | €-11,21 | 3,48% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.772,40 | €-315,23 | 165 | 165 | 40,61% | 0,89 | €-1,91 | 12,31% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.761,07 | €-238,93 | 19 | 19 | 47,37% | 0,58 | €-12,58 | 3,13% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.713,57 | €-211,27 | 190 | 190 | 41,05% | 0,93 | €-1,11 | 10,86% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.684,07 | €-279,30 | 247 | 247 | 42,91% | 0,94 | €-1,13 | 10,92% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.676,47 | €-323,53 | 23 | 23 | 34,78% | 0,61 | €-14,07 | 4,65% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.605,65 | €-394,35 | 199 | 199 | 45,73% | 0,93 | €-1,98 | 8,44% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.595,38 | €-404,62 | 201 | 201 | 43,28% | 0,92 | €-2,01 | 6,64% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.546,20 | €-417,69 | 277 | 277 | 41,52% | 0,92 | €-1,51 | 12,52% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.543,88 | €-456,12 | 91 | 91 | 46,15% | 0,79 | €-5,01 | 6,28% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.540,84 | €-420,79 | 75 | 75 | 34,67% | 0,78 | €-5,61 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.540,84 | €-420,79 | 75 | 75 | 34,67% | 0,78 | €-5,61 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.540,84 | €-420,79 | 75 | 75 | 34,67% | 0,78 | €-5,61 | 9,06% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.518,32 | €-480,63 | 182 | 168 | 44,51% | 0,87 | €-2,64 | 11,82% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.496,47 | €-463,26 | 108 | 108 | 38,89% | 0,83 | €-4,29 | 8,88% |
| TEST | Combo Trend | Combo Trend | €9.476,65 | €-608,34 | 199 | 199 | 40,70% | 0,86 | €-3,06 | 14,08% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.474,72 | €-487,17 | 66 | 66 | 34,85% | 0,72 | €-7,38 | 9,08% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.471,84 | €-588,86 | 176 | 176 | 41,48% | 0,85 | €-3,35 | 11,91% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.466,30 | €-594,36 | 180 | 180 | 41,67% | 0,85 | €-3,30 | 12,06% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.460,31 | €-501,64 | 67 | 67 | 34,33% | 0,71 | €-7,49 | 9,08% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.459,83 | €-540,17 | 26 | 26 | 34,62% | 0,42 | €-20,78 | 5,44% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.425,94 | €-538,75 | 214 | 214 | 43,46% | 0,90 | €-2,52 | 15,94% |
| TEST | Eth Ema 1H | Trend following EMA | €9.414,26 | €-585,74 | 34 | 34 | 35,29% | 0,50 | €-17,23 | 5,86% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.401,39 | €-598,61 | 169 | 169 | 36,69% | 0,83 | €-3,54 | 7,34% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.387,51 | €-574,73 | 94 | 94 | 34,04% | 0,75 | €-6,11 | 10,17% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.387,06 | €-577,77 | 252 | 252 | 42,06% | 0,91 | €-2,29 | 15,64% |
| TEST | Btc Ema 1H | Trend following EMA | €9.353,69 | €-646,31 | 28 | 28 | 25,00% | 0,36 | €-23,08 | 6,56% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.351,06 | €-648,94 | 145 | 145 | 43,45% | 0,75 | €-4,48 | 9,26% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.341,39 | €-664,23 | 156 | 156 | 43,59% | 0,79 | €-4,26 | 12,28% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.266,08 | €-687,02 | 185 | 185 | 42,16% | 0,78 | €-3,71 | 13,79% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.207,83 | €-779,76 | 124 | 124 | 31,45% | 0,76 | €-6,29 | 10,08% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.198,03 | €-789,56 | 119 | 119 | 33,61% | 0,76 | €-6,63 | 9,87% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.183,29 | €-886,24 | 212 | 212 | 40,09% | 0,77 | €-4,18 | 15,68% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.182,76 | €-817,24 | 186 | 186 | 37,63% | 0,79 | €-4,39 | 8,78% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.172,73 | €-894,15 | 110 | 110 | 30,91% | 0,72 | €-8,13 | 9,31% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.162,46 | €-825,19 | 121 | 121 | 33,06% | 0,76 | €-6,82 | 9,87% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.043,82 | €-957,27 | 163 | 163 | 36,20% | 0,69 | €-5,87 | 14,10% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.041,56 | €-946,25 | 155 | 155 | 41,94% | 0,74 | €-6,10 | 10,69% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.040,47 | €-964,89 | 240 | 240 | 40,83% | 0,77 | €-4,02 | 15,45% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €8.985,64 | €-1.014,36 | 99 | 99 | 33,33% | 0,63 | €-10,25 | 10,40% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €8.977,51 | €-1.019,89 | 66 | 66 | 28,79% | 0,49 | €-15,45 | 12,43% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €8.930,52 | €-1.034,19 | 269 | 269 | 40,15% | 0,83 | €-3,84 | 19,03% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €8.928,71 | €-1.071,29 | 113 | 113 | 25,66% | 0,68 | €-9,48 | 12,03% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €8.928,44 | €-1.067,53 | 161 | 161 | 38,51% | 0,74 | €-6,63 | 12,78% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.874,63 | €-1.126,43 | 143 | 143 | 35,66% | 0,60 | €-7,88 | 14,10% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.664,18 | €-1.398,65 | 137 | 137 | 37,23% | 0,63 | €-10,21 | 16,24% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.624,96 | €-1.340,59 | 180 | 180 | 34,44% | 0,63 | €-7,45 | 19,11% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.555,31 | €-1.468,36 | 85 | 85 | 36,47% | 0,51 | €-17,27 | 16,19% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.448,19 | €-1.551,81 | 88 | 88 | 26,14% | 0,56 | €-17,63 | 15,70% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €8.413,97 | €-1.586,03 | 126 | 126 | 30,95% | 0,61 | €-12,59 | 16,10% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €8.257,45 | €-1.804,95 | 160 | 160 | 38,12% | 0,59 | €-11,28 | 18,17% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.221,92 | €-1.836,30 | 137 | 137 | 35,77% | 0,50 | €-13,40 | 20,25% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.144,60 | €-1.876,44 | 149 | 149 | 41,61% | 0,56 | €-12,59 | 20,43% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | UNI | LONG | Confluenza trend | 240m | 3,0x | 6,93739 | 6,93739 | 6,33086 | 4,65961 | 8,15044 | €18,73 | €56,20 | €4,91 | €0,00 |
| Principale 4H | BR | LONG | Confluenza trend | 240m | 3,0x | 0,64695 | 0,66728 | 0,56932 | 0,43453 | 0,80222 | €133,65 | €400,94 | €48,11 | €12,60 |
| Principale 4H | NEAR | LONG | Confluenza trend | 240m | 3,0x | 2,86857 | 2,98600 | 2,65907 | 1,92673 | 3,28758 | €219,58 | €658,74 | €48,11 | €26,97 |
| Principale 4H | ARB | LONG | Confluenza trend | 240m | 3,0x | 0,16607 | 0,17192 | 0,14920 | 0,11155 | 0,19981 | €157,86 | €473,57 | €48,11 | €16,67 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 1362,57246 | 1485,04000 | 1248,37180 | 915,19450 | 1590,97378 | €171,74 | €515,21 | €43,18 | €46,31 |
| Principale 4H | PEPE | LONG | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €10,67 | €32,02 | €1,66 | €0,12 |
| Bilanciata 1H V1 | ZEC | LONG | Confluenza trend | 60m | 3,0x | 1367,76350 | 1485,04000 | 1417,55549 | 918,68115 | 1515,93042 | €279,62 | €838,86 | €0,00 | €71,93 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,17195 | 0,17192 | 0,16308 | 0,11550 | 0,18970 | €296,63 | €889,88 | €45,93 | €-0,18 |
| Bilanciata 1H V1 | BR | LONG | Confluenza trend | 60m | 3,0x | 0,66741 | 0,66728 | 0,58732 | 0,44828 | 0,82759 | €127,56 | €382,69 | €45,92 | €-0,08 |
| Bilanciata 1H V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,98660 | 2,98600 | 2,86052 | 2,00600 | 3,23875 | €362,60 | €1.087,80 | €45,92 | €-0,22 |
| Bilanciata 1H V2 | ARB | LONG | Confluenza trend V2 | 60m | 3,0x | 0,17195 | 0,17192 | 0,16308 | 0,11550 | 0,18970 | €307,42 | €922,26 | €47,60 | €-0,18 |
| Bilanciata 1H V2 | BR | LONG | Confluenza trend V2 | 60m | 3,0x | 0,66741 | 0,66728 | 0,58732 | 0,44828 | 0,82759 | €132,20 | €396,61 | €47,59 | €-0,08 |
| Bilanciata 1H V3 Filtered | BR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,63674 | 0,66728 | 0,63674 | 0,42768 | 0,78955 | €134,14 | €402,41 | €0,00 | €19,30 |
| Bilanciata 1H V3 Filtered | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16668 | 0,11196 | 0,18419 | €306,48 | €919,44 | €0,00 | €28,89 |
| Bilanciata 1H V3 Filtered | NEAR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,86052 | 2,00600 | 3,23875 | €386,74 | €1.160,23 | €48,98 | €-0,23 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1415,48789 | 997,65136 | 1625,03524 | €347,14 | €1.041,42 | €48,97 | €-0,21 |
| 1H Fast Score 6 75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €379,23 | €1.137,68 | €0,00 | €35,74 |
| 1H Fast Score 6 75 V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €476,61 | €1.429,83 | €46,95 | €-0,29 |
| 1H Fast Score 6 75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €427,79 | €1.283,38 | €46,94 | €-0,26 |
| 1H Fast Score 6 75 No Trend Up V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €380,80 | €1.142,39 | €0,00 | €35,89 |
| 1H Fast Score 6 75 No Trend Up V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €478,58 | €1.435,75 | €47,14 | €-0,29 |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €429,57 | €1.288,70 | €47,13 | €-0,26 |
| 1H Fast Score 6 75 Cost Aware V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €448,88 | €1.346,64 | €0,00 | €42,31 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €564,15 | €1.692,45 | €55,57 | €-0,34 |
| 1H Fast Score 6 75 Cost Aware V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €506,37 | €1.519,10 | €55,56 | €-0,30 |
| 1H Fast Nohigh Cap75 V1 | POWER | SHORT | Momentum / breakout | 60m | 3,0x | 0,12177 | 0,13340 | 0,13638 | 0,16175 | 0,09985 | €137,41 | €412,22 | €49,47 | €-39,39 |
| 1H Fast Nohigh Cap75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €403,64 | €1.210,92 | €0,00 | €38,04 |
| 1H Fast Nohigh Cap75 V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €505,79 | €1.517,36 | €49,82 | €-0,30 |
| 1H Fast Nohigh Cap75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €453,98 | €1.361,95 | €49,81 | €-0,27 |
| 1H Fast Nohigh Cap75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €12,31 | €36,94 | €0,67 | €-0,01 |
| 1H Fast Long Btc 1 3 Cap75 V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €453,42 | €1.360,27 | €44,66 | €-0,27 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €406,98 | €1.220,95 | €44,66 | €-0,24 |
| 1H Fast Long Btc 1 3 Cap75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €819,56 | €2.458,67 | €44,65 | €-0,49 |
| 1H Fast No Pepe V1 | POWER | SHORT | Momentum / breakout | 60m | 3,0x | 0,12177 | 0,13340 | 0,13638 | 0,16175 | 0,09985 | €145,18 | €435,55 | €52,27 | €-41,62 |
| 1H Fast No Pepe V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,17195 | 0,17192 | 0,16505 | 0,11550 | 0,18231 | €436,04 | €1.308,12 | €52,51 | €-0,26 |
| 1H Fast No Pepe V1 | BR | LONG | Momentum / breakout | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €156,44 | €469,33 | €52,50 | €-0,09 |
| 1H Fast No Pepe V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €533,01 | €1.599,02 | €52,50 | €-0,32 |
| 1H Fast Tp2 V1 | POWER | SHORT | Momentum / breakout | 60m | 3,0x | 0,12177 | 0,13340 | 0,13638 | 0,16175 | 0,09254 | €141,28 | €423,85 | €50,86 | €-40,50 |
| 1H Fast Tp2 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,17195 | 0,17192 | 0,16505 | 0,11550 | 0,18576 | €425,39 | €1.276,16 | €51,23 | €-0,26 |
| 1H Fast Tp2 V1 | BR | LONG | Momentum / breakout | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,81674 | €152,62 | €457,86 | €51,22 | €-0,09 |
| 1H Fast Tp2 V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,18272 | €519,98 | €1.559,94 | €51,22 | €-0,31 |
| Rapida 1H V3 Filtered | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €414,35 | €1.243,04 | €0,00 | €39,05 |
| Rapida 1H V3 Filtered | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €152,93 | €458,78 | €51,32 | €-0,09 |
| Rapida 1H V3 Filtered | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €521,03 | €1.563,08 | €51,32 | €-0,31 |
| Rapida 1H V3 Filtered | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €467,66 | €1.402,98 | €51,31 | €-0,28 |
| Rapida 1H V3 Filtered | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €9,23 | €27,68 | €0,50 | €-0,01 |
| 1H Fast V3 Cap75 V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €359,21 | €1.077,64 | €0,00 | €33,86 |
| 1H Fast V3 Cap75 V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €453,53 | €1.360,59 | €44,67 | €-0,27 |
| 1H Fast V3 Cap75 V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €407,08 | €1.221,23 | €44,67 | €-0,24 |
| 1H Fast V3 Cap75 V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €819,75 | €2.459,24 | €44,66 | €-0,49 |
| 1H Fast V3 Nohigh V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €406,76 | €1.220,27 | €0,00 | €38,34 |
| 1H Fast V3 Nohigh V1 | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €149,16 | €447,49 | €50,06 | €-0,09 |
| 1H Fast V3 Nohigh V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €508,21 | €1.524,63 | €50,06 | €-0,30 |
| 1H Fast V3 Nohigh V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €456,16 | €1.368,47 | €50,05 | €-0,27 |
| 1H Fast V3 Long Only V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €385,45 | €1.156,36 | €0,00 | €36,33 |
| 1H Fast V3 Long Only V1 | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €142,26 | €426,79 | €47,74 | €-0,09 |
| 1H Fast V3 Long Only V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €484,69 | €1.454,08 | €47,74 | €-0,29 |
| 1H Fast V3 Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €435,05 | €1.305,14 | €47,74 | €-0,26 |
| 1H Fast V3 Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €8,59 | €25,76 | €0,47 | €-0,01 |
| 1H Fast V3 No Esports V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €391,02 | €1.173,06 | €0,00 | €36,85 |
| 1H Fast V3 No Esports V1 | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €144,32 | €432,95 | €48,43 | €-0,09 |
| 1H Fast V3 No Esports V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €491,69 | €1.475,08 | €48,43 | €-0,29 |
| 1H Fast V3 No Esports V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €441,33 | €1.323,99 | €48,43 | €-0,26 |
| 1H Fast V3 No Esports V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €8,71 | €26,13 | €0,47 | €-0,01 |
| 1H Fast V3 No Esports Long Only V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €399,51 | €1.198,52 | €0,00 | €37,65 |
| 1H Fast V3 No Esports Long Only V1 | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €147,45 | €442,35 | €49,48 | €-0,09 |
| 1H Fast V3 No Esports Long Only V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €502,36 | €1.507,09 | €49,48 | €-0,30 |
| 1H Fast V3 No Esports Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €450,91 | €1.352,73 | €49,48 | €-0,27 |
| 1H Fast V3 No Esports Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €8,90 | €26,70 | €0,48 | €-0,01 |
| 1H Fast V3 No Esports Mfe Lock V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €417,03 | €1.251,08 | €0,00 | €39,31 |
| 1H Fast V3 No Esports Mfe Lock V1 | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €153,92 | €461,75 | €51,65 | €-0,09 |
| 1H Fast V3 No Esports Mfe Lock V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €524,39 | €1.573,18 | €51,65 | €-0,31 |
| 1H Fast V3 No Esports Mfe Lock V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €470,68 | €1.412,05 | €51,65 | €-0,28 |
| 1H Fast V3 No Esports Mfe Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €9,29 | €27,86 | €0,51 | €-0,01 |
| 1H Fast V3 No Esports Stress Guard V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16731 | 0,17192 | 0,16731 | 0,11238 | 0,17779 | €427,51 | €1.282,54 | €0,00 | €35,31 |
| 1H Fast V3 No Esports Stress Guard V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €552,45 | €1.657,34 | €54,42 | €-0,33 |
| 1H Fast V3 No Esports Stress Guard V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €495,86 | €1.487,59 | €54,41 | €-0,30 |
| 1H Fast V3 No Esports Stress Guard V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €998,53 | €2.995,60 | €54,40 | €-0,60 |
| Ampia 4H | UNI | LONG | Confluenza trend | 240m | 2,0x | 6,98040 | 6,98040 | 6,22147 | 3,52510 | 9,10539 | €214,19 | €428,38 | €46,57 | €0,00 |
| Ampia 4H | SUI | SHORT | Confluenza trend | 240m | 2,0x | 0,72745 | 0,72745 | 0,78235 | 1,08754 | 0,57376 | €23,11 | €46,21 | €3,49 | €-0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08143 | 0,08205 | 0,08517 | 0,12174 | 0,07096 | €31,75 | €63,49 | €2,92 | €-0,48 |
| Ampia 4H | SOL | SHORT | Confluenza trend | 240m | 2,0x | 97,48250 | 101,77000 | 102,49471 | 145,73634 | 83,44831 | €17,85 | €35,69 | €1,84 | €-1,57 |
| Forza relativa 1H V1 | SUI | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,72256 | 0,72256 | 0,74546 | 1,08022 | 0,67216 | €672,88 | €1.345,76 | €42,66 | €-0,00 |
| Forza relativa 1H V1 | POWER | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,12177 | 0,13340 | 0,13638 | 0,18204 | 0,08962 | €173,42 | €346,84 | €41,62 | €-33,14 |
| Forza relativa 1H V1 | HYPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 81,62032 | 82,70900 | 79,97846 | 41,21826 | 85,23242 | €21,85 | €43,70 | €0,88 | €0,58 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,17195 | 0,17192 | 0,16308 | 0,08684 | 0,19148 | €417,85 | €835,70 | €43,13 | €-0,17 |
| Forza relativa 1H V1 | BR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,84361 | €179,69 | €359,39 | €43,13 | €-0,07 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,98660 | 2,98600 | 2,86052 | 1,50823 | 3,26397 | €12,79 | €25,58 | €1,08 | €-0,01 |
| Forza relativa 1H V2 | ZEC | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1362,57246 | 1485,04000 | 1425,82614 | 688,09909 | 1494,00974 | €562,79 | €1.125,57 | €0,00 | €101,17 |
| Forza relativa 1H V2 | ARB | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,17195 | 0,17192 | 0,16308 | 0,08684 | 0,19148 | €482,69 | €965,39 | €49,82 | €-0,19 |
| Forza relativa 1H V2 | BR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,84361 | €207,58 | €415,16 | €49,82 | €-0,08 |
| Scalp RSI Short 85 · €10 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €10,00 | €150,00 | €3,36 | €-1,21 |
| Scalp RSI Short 80 · €10 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €10,00 | €150,00 | €3,36 | €-1,21 |
| Scalp RSI Short 75 · €10 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €10,00 | €150,00 | €3,36 | €-1,21 |
| Scalp RSI Short 85 · €50 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €50,00 | €750,00 | €16,81 | €-6,04 |
| Scalp RSI Short 80 · €50 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €50,00 | €750,00 | €16,81 | €-6,04 |
| Scalp RSI Short 75 · €50 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €50,00 | €750,00 | €16,81 | €-6,04 |
| Scalp RSI Short 85 · prudente · 5x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €89,18 | €445,89 | €10,00 | €-3,59 |
| Scalp RSI Short 80 · prudente · 5x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €88,82 | €444,10 | €9,96 | €-3,58 |
| Scalp RSI Short 75 · prudente · 5x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €88,87 | €444,33 | €9,96 | €-3,58 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 81,62032 | 82,70900 | 79,79603 | 41,21826 | 86,18106 | €1.339,05 | €2.678,11 | €59,86 | €35,72 |
| Benchmark Donchian breakout 1H | NEAR | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2,98660 | 2,98600 | 2,84651 | 1,50823 | 3,33681 | €639,73 | €1.279,45 | €60,01 | €-0,26 |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 81,62032 | 82,70900 | 79,79603 | 41,21826 | 86,18106 | €1.307,53 | €2.615,06 | €58,45 | €34,88 |
| Donchian 1H Gb20 120R V1 | NEAR | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2,98660 | 2,98600 | 2,84651 | 1,50823 | 3,33681 | €624,67 | €1.249,33 | €58,60 | €-0,25 |
| Benchmark Bollinger mean reversion 1H | XRP | LONG | Bollinger mean reversion | 60m | 2,0x | 1,28183 | 1,30578 | 1,23929 | 0,64732 | 1,34563 | €603,45 | €1.206,90 | €40,05 | €22,55 |
| Benchmark Bollinger mean reversion 1H | ZEC | SHORT | Bollinger mean reversion | 60m | 2,0x | 1484,74299 | 1485,04000 | 1542,92731 | 2219,69077 | 1397,46652 | €519,64 | €1.039,27 | €40,73 | €-0,21 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 1349,03975 | 1485,04000 | 1423,61482 | 681,26508 | 1499,54369 | €472,42 | €944,85 | €0,00 | €95,25 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,79556 | 2,98600 | 2,90562 | 1,41176 | 3,07204 | €532,88 | €1.065,76 | €0,00 | €72,60 |
| Benchmark trend following EMA 1H | ARB | LONG | Trend following EMA | 60m | 2,0x | 0,16668 | 0,17192 | 0,15696 | 0,08418 | 0,18808 | €410,73 | €821,46 | €47,94 | €25,81 |
| Benchmark trend following EMA 1H | BR | LONG | Trend following EMA | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,84361 | €203,60 | €407,20 | €48,86 | €-0,08 |
| Scanner Top 5 Long 1H | ZEC | LONG | Scanner Top 5 Long | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1515,93042 | €43,70 | €87,39 | €0,00 | €7,49 |
| Scanner Bottom 5 Short 1H | POWER | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,12177 | 0,13340 | 0,13638 | 0,18204 | 0,09254 | €196,36 | €392,72 | €47,13 | €-37,52 |
| Scanner Top10 Long | ZEC | LONG | Scanner Top10 Long | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1515,93042 | €47,66 | €95,32 | €0,00 | €8,17 |
| Scanner Bottom10 Short | POWER | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,12177 | 0,13340 | 0,13638 | 0,18204 | 0,09254 | €199,57 | €399,13 | €47,90 | €-38,14 |
| Scanner Top15 Long | ZEC | LONG | Scanner Top15 Long | 60m | 2,0x | 1485,33701 | 1485,04000 | 1415,48789 | 750,09519 | 1625,03524 | €557,51 | €1.115,02 | €52,43 | €-0,22 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,98660 | 2,98600 | 2,86052 | 1,50823 | 3,23875 | €621,00 | €1.242,00 | €52,43 | €-0,25 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,17195 | 0,17192 | 0,16308 | 0,08684 | 0,18970 | €507,91 | €1.015,82 | €52,43 | €-0,20 |
| Scanner Top15 Long | BR | LONG | Scanner Top15 Long | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,82759 | €218,31 | €436,62 | €52,39 | €-0,09 |
| Scanner Bottom15 Short | POWER | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,12177 | 0,13340 | 0,13638 | 0,18204 | 0,09254 | €199,57 | €399,13 | €47,90 | €-38,14 |
| Scanner Top20 Long | ZEC | LONG | Scanner Top20 Long | 60m | 2,0x | 1485,33701 | 1485,04000 | 1415,48789 | 750,09519 | 1625,03524 | €557,51 | €1.115,02 | €52,43 | €-0,22 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,98660 | 2,98600 | 2,86052 | 1,50823 | 3,23875 | €621,00 | €1.242,00 | €52,43 | €-0,25 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,17195 | 0,17192 | 0,16308 | 0,08684 | 0,18970 | €507,91 | €1.015,82 | €52,43 | €-0,20 |
| Scanner Top20 Long | BR | LONG | Scanner Top20 Long | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,82759 | €218,31 | €436,62 | €52,39 | €-0,09 |
| Scanner Bottom20 Short | POWER | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,12177 | 0,13340 | 0,13638 | 0,18204 | 0,09254 | €199,57 | €399,13 | €47,90 | €-38,14 |
| Scanner Top 5 + forza BTC 1H | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1530,74711 | €35,25 | €70,50 | €0,00 | €6,05 |
| Scanner Top5 Btc Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1530,74711 | €33,05 | €66,09 | €0,00 | €5,67 |
| Scanner Top5 Btc Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1530,74711 | €341,89 | €683,78 | €0,00 | €58,63 |
| Scanner Top5 Btc Btc 2 3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1485,33701 | 1485,04000 | 1415,48789 | 750,09519 | 1639,00507 | €477,40 | €954,81 | €44,90 | €-0,19 |
| Scanner Top5 Btc Btc 2 3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,98660 | 2,98600 | 2,86052 | 1,50823 | 3,26397 | €531,77 | €1.063,54 | €44,90 | €-0,21 |
| Scanner Top5 Btc Btc 2 3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,17195 | 0,17192 | 0,16308 | 0,08684 | 0,19148 | €434,93 | €869,86 | €44,89 | €-0,17 |
| Scanner Top5 Btc Btc 2 3 V1 | BR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,84361 | €186,94 | €373,89 | €44,87 | €-0,07 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1530,74711 | €368,96 | €737,91 | €0,00 | €63,27 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1530,74711 | €366,47 | €732,95 | €0,00 | €62,85 |
| Scanner Top5 Btc Runner25 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1590,01389 | €356,23 | €712,46 | €0,00 | €61,09 |
| Scanner Top5 Btc Tp3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1367,76350 | 1485,04000 | 1417,55549 | 690,72057 | 1590,01389 | €356,44 | €712,87 | €0,00 | €61,12 |
| Combo Trend | NEAR | LONG | Combo Trend | 60m | 2,0x | 2,79556 | 2,98600 | 2,90562 | 1,41176 | 3,07204 | €516,79 | €1.033,59 | €0,00 | €70,41 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 1349,03975 | 1485,04000 | 1423,61482 | 681,26508 | 1499,54369 | €458,08 | €916,17 | €0,00 | €92,36 |
| Combo Trend | ARB | LONG | Combo Trend | 60m | 2,0x | 0,16668 | 0,17192 | 0,15696 | 0,08418 | 0,18808 | €398,30 | €796,60 | €46,48 | €25,03 |
| Combo Trend | BR | LONG | Combo Trend | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,84361 | €197,44 | €394,87 | €47,38 | €-0,08 |
| Combo Mean Reversion | XRP | LONG | Combo Mean Reversion | 60m | 2,0x | 1,28183 | 1,30578 | 1,23929 | 0,64732 | 1,34989 | €653,10 | €1.306,20 | €43,35 | €24,41 |
| Combo Adaptive | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,30578 | 1,33225 | 1,92042 | 1,18918 | €35,04 | €70,07 | €2,60 | €-1,16 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1366,74329 | 1485,04000 | 1425,55871 | 690,20536 | 1505,72053 | €14,74 | €29,48 | €0,00 | €2,55 |
| Combo Adaptive | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,79556 | 2,98600 | 2,91914 | 1,41176 | 3,02177 | €645,80 | €1.291,60 | €0,00 | €87,99 |
| Combo Adaptive | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,16668 | 0,17192 | 0,16668 | 0,08418 | 0,18419 | €497,62 | €995,25 | €0,00 | €31,27 |
| Combo Adaptive | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,82759 | €220,13 | €440,26 | €52,83 | €-0,09 |
| Combo Adaptive Mfe Trail | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1367,76350 | 1485,04000 | 1441,84940 | 690,72057 | 1515,93042 | €31,44 | €62,87 | €0,00 | €5,39 |
| Combo Adaptive Quality7 V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,79556 | 2,98600 | 2,91914 | 1,41176 | 3,02177 | €576,49 | €1.152,98 | €0,00 | €78,54 |
| Combo Adaptive Quality7 V1 | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,82759 | €197,86 | €395,73 | €47,49 | €-0,08 |
| Combo Adaptive Quality7 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,17195 | 0,17192 | 0,16308 | 0,08684 | 0,18970 | €460,06 | €920,11 | €47,49 | €-0,18 |
| Combo Adaptive Partial 1R V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,79556 | 2,98600 | 2,91914 | 1,41176 | 3,02177 | €620,33 | €1.240,66 | €0,00 | €84,52 |
| Combo Adaptive Partial 1R V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,16668 | 0,17192 | 0,16668 | 0,08418 | 0,18419 | €478,13 | €956,27 | €0,00 | €30,04 |
| Combo Adaptive Partial 1R V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1485,33701 | 1485,04000 | 1415,48789 | 750,09519 | 1625,03524 | €544,86 | €1.089,72 | €51,25 | €-0,22 |
| Combo Adaptive Partial 1R V1 | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,82759 | €213,50 | €427,01 | €51,24 | €-0,09 |
| Combo Adaptive Runner25 V1 | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,73075 | 0,73075 | 0,75468 | 1,09248 | 0,65898 | €73,50 | €146,99 | €4,81 | €-0,00 |
| Combo Adaptive Runner25 V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,30578 | 1,33225 | 1,92042 | 1,14149 | €31,43 | €62,85 | €2,33 | €-1,04 |
| Combo Adaptive Runner25 V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1366,74329 | 1485,04000 | 1425,55871 | 690,20536 | 1575,20916 | €12,91 | €25,81 | €0,00 | €2,23 |
| Combo Adaptive Tp3 V1 | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,73075 | 0,73075 | 0,75468 | 1,09248 | 0,65898 | €72,15 | €144,29 | €4,72 | €-0,00 |
| Combo Adaptive Tp3 V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,30578 | 1,33225 | 1,92042 | 1,14149 | €30,84 | €61,68 | €2,29 | €-1,02 |
| Combo Adaptive Tp3 V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1366,74329 | 1485,04000 | 1425,55871 | 690,20536 | 1575,20916 | €12,67 | €25,33 | €0,00 | €2,19 |
| Master Adaptive V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1485,04000 | 1297,25468 | 690,20536 | 1505,72052 | €433,46 | €866,91 | €44,08 | €75,03 |
| Master Adaptive Gb20 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1485,04000 | 1297,25468 | 690,20536 | 1505,72052 | €427,66 | €855,33 | €43,49 | €74,03 |
| Master Adaptive Runner25 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1485,04000 | 1297,25468 | 690,20536 | 1575,20914 | €389,09 | €778,18 | €39,56 | €67,35 |
| Combo Adaptive Side Regime Guard V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,28456 | 1,30578 | 1,33225 | 1,92042 | 1,18918 | €28,88 | €57,77 | €2,14 | €-0,95 |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1367,76350 | 1485,04000 | 1422,00867 | 690,72057 | 1515,93042 | €18,84 | €37,68 | €0,00 | €3,23 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,80756 | 2,98600 | 2,91919 | 1,41782 | 3,03459 | €630,04 | €1.260,08 | €0,00 | €80,09 |
| Combo Adaptive Side Regime Guard V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,16668 | 0,17192 | 0,16668 | 0,08418 | 0,18419 | €485,00 | €970,00 | €0,00 | €30,47 |
| Combo Adaptive Side Regime Guard V1 | BR | LONG | Combo Adaptive | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,82759 | €214,56 | €429,12 | €51,49 | €-0,09 |
| Master Adaptive Gb20 Be V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1485,04000 | 1297,25468 | 690,20536 | 1505,72052 | €435,60 | €871,21 | €44,29 | €75,41 |
| Master Adaptive Gb20 Partial V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1366,74329 | 1485,04000 | 1297,25468 | 690,20536 | 1505,72052 | €435,14 | €870,28 | €44,25 | €75,33 |
| 1H Fast V3 Nohigh Regime Guard V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €426,97 | €1.280,91 | €0,00 | €40,24 |
| 1H Fast V3 Nohigh Regime Guard V1 | BR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,66741 | 0,66728 | 0,59275 | 0,44828 | 0,77941 | €157,74 | €473,22 | €52,94 | €-0,09 |
| 1H Fast V3 Nohigh Regime Guard V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €537,43 | €1.612,28 | €52,94 | €-0,32 |
| 1H Fast V3 Nohigh Regime Guard V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €482,38 | €1.447,14 | €52,93 | €-0,29 |
| 1H Fast V3 Nohigh Regime Guard V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €10,46 | €31,38 | €0,57 | €-0,01 |
| Main Side Regime Guard V1 | SUI | SHORT | Confluenza trend | 240m | 3,0x | 0,72995 | 0,72995 | 0,77421 | 0,96962 | 0,64144 | €294,19 | €882,58 | €53,51 | €-0,00 |
| Main Side Regime Guard V1 | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,29295 | 1,30578 | 1,37261 | 1,71747 | 1,13364 | €83,64 | €250,92 | €15,46 | €-2,49 |
| Combo Trend Side Regime Guard V1 | NEAR | LONG | Combo Trend | 60m | 2,0x | 2,79556 | 2,98600 | 2,90562 | 1,41176 | 3,07204 | €609,18 | €1.218,36 | €0,00 | €83,00 |
| Combo Trend Side Regime Guard V1 | ZEC | LONG | Combo Trend | 60m | 2,0x | 1349,03975 | 1485,04000 | 1423,61482 | 681,26508 | 1499,54369 | €539,97 | €1.079,95 | €0,00 | €108,87 |
| Combo Trend Side Regime Guard V1 | ARB | LONG | Combo Trend | 60m | 2,0x | 0,16668 | 0,17192 | 0,15696 | 0,08418 | 0,18808 | €469,50 | €939,00 | €54,79 | €29,50 |
| Combo Trend Side Regime Guard V1 | BR | LONG | Combo Trend | 60m | 2,0x | 0,66741 | 0,66728 | 0,58732 | 0,33704 | 0,84361 | €232,73 | €465,46 | €55,86 | €-0,09 |
| 1H Fast Nohigh Cap75 Short Only V1 | POWER | SHORT | Momentum / breakout | 60m | 3,0x | 0,12177 | 0,13340 | 0,13638 | 0,16175 | 0,09985 | €133,98 | €401,95 | €48,23 | €-38,41 |
| 1H Fast Nohigh Cap75 Short Only V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,16668 | 0,17192 | 0,16727 | 0,11196 | 0,17690 | €393,59 | €1.180,76 | €0,00 | €37,10 |
| 1H Fast Nohigh Cap75 Short Only V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,98660 | 2,98600 | 2,88854 | 2,00600 | 3,13369 | €493,19 | €1.479,57 | €48,58 | €-0,30 |
| 1H Fast Nohigh Cap75 Short Only V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 1485,33701 | 1485,04000 | 1431,00992 | 997,65136 | 1566,82765 | €442,67 | €1.328,02 | €48,57 | €-0,27 |
| 1H Fast Nohigh Cap75 Short Only V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,72554 | 82,70900 | 81,22316 | 55,56399 | 84,97912 | €12,01 | €36,02 | €0,65 | €-0,01 |
| 1H Balanced V3 Long Only V1 | BR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,63674 | 0,66728 | 0,63674 | 0,42768 | 0,78955 | €126,91 | €380,72 | €0,00 | €18,26 |
| 1H Balanced V3 Long Only V1 | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,16668 | 0,17192 | 0,16668 | 0,11196 | 0,18419 | €289,96 | €869,88 | €0,00 | €27,33 |
| 1H Balanced V3 Long Only V1 | NEAR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2,98660 | 2,98600 | 2,86052 | 2,00600 | 3,23875 | €365,90 | €1.097,70 | €46,34 | €-0,22 |
| 1H Balanced V3 Long Only V1 | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1485,33701 | 1485,04000 | 1415,48789 | 997,65136 | 1625,03524 | €328,43 | €985,30 | €46,33 | €-0,20 |
| Scanner Bottom5 Short Profit Lock V1 | POWER | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,12177 | 0,13340 | 0,13638 | 0,18204 | 0,09254 | €197,88 | €395,77 | €47,49 | €-37,81 |
| Scanner Bottom5 Short Mfe Trail V1 | POWER | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,12177 | 0,13340 | 0,13638 | 0,18204 | 0,09254 | €198,18 | €396,37 | €47,56 | €-37,87 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive Quality7 V1 | ARB | LONG | 2026-09-17T18:30:00+00:00 | 0,17692 | €25,47 | 0,54 | STOP |
| 1H Fast Tp2 V1 | ARB | LONG | 2026-09-17T18:30:00+00:00 | 0,17745 | €39,23 | 0,77 | STOP |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | 2026-09-17T18:00:00+00:00 | 3,03399 | €100,05 | 1,96 | TARGET |
| Combo Adaptive Side Regime Guard V1 | ARB | LONG | 2026-09-17T18:00:00+00:00 | 0,18415 | €100,45 | 1,97 | TARGET |
| Combo Adaptive Partial 1R V1 | ARB | LONG | 2026-09-17T18:00:00+00:00 | 0,18415 | €99,02 | 1,97 | TARGET |
| Combo Adaptive | ARB | LONG | 2026-09-17T18:00:00+00:00 | 0,18415 | €103,06 | 1,97 | TARGET |
| 1H Fast No Pepe V1 | ARB | LONG | 2026-09-17T18:00:00+00:00 | 0,18227 | €76,87 | 1,46 | TARGET |
| 1H Balanced V3 Long Only V1 | ARB | LONG | 2026-09-17T18:00:00+00:00 | 0,18415 | €90,08 | 1,97 | TARGET |
| Bilanciata 1H V3 Filtered | ARB | LONG | 2026-09-17T18:00:00+00:00 | 0,18415 | €95,21 | 1,97 | TARGET |
| 1H Fast V3 No Esports V1 | ARB | LONG | 2026-09-17T17:45:00+00:00 | 0,17686 | €70,18 | 1,46 | TARGET |
| 1H Fast V3 No Esports Stress Guard V1 | ARB | LONG | 2026-09-17T17:45:00+00:00 | 0,17775 | €78,44 | 1,47 | TARGET |
| 1H Fast V3 No Esports Mfe Lock V1 | ARB | LONG | 2026-09-17T17:45:00+00:00 | 0,17686 | €74,84 | 1,46 | TARGET |

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

Generato: 2026-09-23 05:32 UTC


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

Segnali totali salvati: **213**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-23 | BTC | 86.710,28 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-23 | DOGE | 0.10219 | +2 | -2 | -2 | 0 | +3 | +1 | 0 | STAI ALLA FINESTRA |
| 2026-09-23 | SOL | 118,88 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-22 | BTC | 85.107,65 | +5 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-22 | DOGE | 0.09857 | +2 | -2 | -2 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-22 | SOL | 115,61 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-17 | BTC | 76.325,40 | +2 | +3 | +3 | 0 | 0 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-17 | DOGE | 0.08084 | -6 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-17 | SOL | 99,49 | 0 | +3 | +3 | 0 | -1 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-16 | BTC | 75.786,49 | +2 | +3 | +3 | 0 | 0 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-16 | DOGE | 0.08011 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-16 | SOL | 97,05 | +2 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 71 | 70 | 69 | 69 | 69 | 68 | 65 | 61 | 54 | 45 | 32 | 17 |
| SOL | 71 | 70 | 69 | 69 | 69 | 68 | 65 | 61 | 54 | 45 | 32 | 17 |
| DOGE | 71 | 70 | 69 | 69 | 69 | 68 | 65 | 61 | 54 | 45 | 32 | 17 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-26 | 60g | 2026-09-24 | domani |
| SOL | 2026-07-26 | 60g | 2026-09-24 | domani |
| DOGE | 2026-07-26 | 60g | 2026-09-24 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 67 | 52,24% | +0,42% | +0,40% | UTILE |
| BTC | 2g | 66 | 51,52% | +0,70% | +0,63% | UTILE |
| BTC | 3g | 66 | 46,97% | +0,90% | +0,80% | UTILE |
| BTC | 5g | 66 | 45,45% | +1,86% | +1,67% | UTILE |
| BTC | 7g | 65 | 53,85% | +2,51% | +2,35% | UTILE |
| BTC | 10g | 62 | 59,68% | +3,23% | +3,08% | UTILE |
| BTC | 14g | 58 | 56,90% | +4,63% | +4,57% | PRIMA CALIBRAZIONE |
| BTC | 21g | 51 | 66,67% | +8,53% | +8,40% | PRIMA CALIBRAZIONE |
| BTC | 30g | 42 | 92,86% | +14,93% | +13,90% | PRIMA CALIBRAZIONE |
| BTC | 45g | 30 | 90,00% | +23,48% | +19,07% | PRIMA CALIBRAZIONE |
| BTC | 60g | 15 | 86,67% | +24,03% | +18,33% | FEEDBACK RAPIDO |
| SOL | 1g | 62 | 53,23% | +0,53% | +0,43% | UTILE |
| SOL | 2g | 61 | 47,54% | +1,19% | +1,08% | UTILE |
| SOL | 3g | 61 | 54,10% | +1,92% | +1,78% | UTILE |
| SOL | 5g | 61 | 57,38% | +3,32% | +3,23% | UTILE |
| SOL | 7g | 61 | 62,30% | +4,75% | +4,83% | UTILE |
| SOL | 10g | 58 | 65,52% | +6,08% | +6,21% | PRIMA CALIBRAZIONE |
| SOL | 14g | 54 | 72,22% | +8,52% | +9,19% | PRIMA CALIBRAZIONE |
| SOL | 21g | 47 | 78,72% | +14,62% | +13,87% | PRIMA CALIBRAZIONE |
| SOL | 30g | 38 | 73,68% | +23,38% | +18,18% | PRIMA CALIBRAZIONE |
| SOL | 45g | 25 | 56,00% | +38,13% | +7,34% | FEEDBACK RAPIDO |
| SOL | 60g | 14 | 35,71% | +36,45% | -8,96% | FEEDBACK RAPIDO |
| DOGE | 1g | 66 | 45,45% | +0,45% | +0,06% | UTILE |
| DOGE | 2g | 65 | 46,15% | +0,79% | +0,03% | UTILE |
| DOGE | 3g | 65 | 40,00% | +1,14% | +0,16% | UTILE |
| DOGE | 5g | 65 | 44,62% | +2,23% | +0,32% | UTILE |
| DOGE | 7g | 64 | 51,56% | +2,81% | +0,95% | UTILE |
| DOGE | 10g | 61 | 49,18% | +2,80% | +1,80% | UTILE |
| DOGE | 14g | 57 | 66,67% | +4,47% | +6,18% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 50 | 70,00% | +7,94% | +5,69% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 43 | 81,40% | +13,42% | +8,23% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 30 | 33,33% | +22,55% | -4,09% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 17 | 0,00% | +21,97% | -21,97% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 67 | 52,24% | +0,42% | +0,40% | -0,12% | +0,94% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 70 | 54,29% | +0,40% | +0,40% | -0,13% | +0,91% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 70 | 54,29% | +0,40% | +0,40% | -0,13% | +0,91% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 63 | 41,27% | +0,41% | +0,08% | -0,05% | +0,93% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 28 | 39,29% | +0,86% | +0,16% | +0,02% | +1,38% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 50,00% | +0,17% | +0,17% | -0,29% | +0,65% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 66 | 51,52% | +0,70% | +0,63% | -0,05% | +1,35% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 69 | 53,62% | +0,78% | +0,78% | +0,04% | +1,43% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 69 | 53,62% | +0,78% | +0,78% | +0,04% | +1,43% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 62 | 43,55% | +0,74% | +0,07% | +0,18% | +1,38% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 28 | 42,86% | +1,35% | +0,13% | +0,35% | +2,03% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 66 | 46,97% | +0,90% | +0,80% | -1,14% | +2,62% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 69 | 53,62% | +1,15% | +1,15% | -1,12% | +2,80% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 69 | 53,62% | +1,15% | +1,15% | -1,12% | +2,80% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 62 | 37,10% | +1,22% | -0,14% | -1,02% | +2,87% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 28 | 39,29% | +2,14% | -0,42% | -0,72% | +3,60% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 66 | 45,45% | +1,86% | +1,67% | -1,75% | +4,19% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 69 | 50,72% | +2,06% | +2,06% | -1,72% | +4,43% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 69 | 50,72% | +2,06% | +2,06% | -1,72% | +4,43% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 62 | 41,94% | +2,00% | -0,73% | -1,64% | +4,42% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 28 | 42,86% | +4,36% | -2,17% | -1,11% | +6,49% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 65 | 53,85% | +2,51% | +2,35% | -2,09% | +5,26% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 68 | 58,82% | +2,77% | +2,77% | -2,06% | +5,49% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 68 | 58,82% | +2,77% | +2,77% | -2,06% | +5,49% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 62 | 43,55% | +2,98% | -1,13% | -1,96% | +5,69% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 27 | 40,74% | +5,59% | -3,76% | -1,42% | +8,56% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 62 | 59,68% | +3,23% | +3,08% | -2,41% | +6,18% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 65 | 63,08% | +3,38% | +3,38% | -2,40% | +6,39% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 65 | 63,08% | +3,38% | +3,38% | -2,40% | +6,39% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 60 | 48,33% | +3,76% | -0,68% | -2,25% | +6,82% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 24 | 50,00% | +5,20% | -3,59% | -1,59% | +8,77% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 58 | 56,90% | +4,63% | +4,57% | -2,61% | +8,17% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 61 | 57,38% | +4,73% | +4,73% | -2,59% | +8,30% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 61 | 57,38% | +4,73% | +4,73% | -2,59% | +8,30% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 56 | 53,57% | +5,27% | +0,94% | -2,42% | +8,89% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 24 | 29,17% | +4,78% | -3,41% | -1,84% | +9,24% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 51 | 66,67% | +8,53% | +8,40% | -2,48% | +12,40% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 54 | 72,22% | +8,44% | +8,44% | -2,48% | +12,33% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 54 | 72,22% | +8,44% | +8,44% | -2,48% | +12,33% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 49 | 46,94% | +9,14% | -0,15% | -2,28% | +13,09% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 22 | 50,00% | +9,06% | -5,00% | -2,06% | +12,94% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | -0,54% | -0,54% | -2,98% | +4,64% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 42 | 92,86% | +14,93% | +13,90% | -2,15% | +19,01% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 45 | 88,89% | +14,71% | +14,71% | -2,17% | +18,96% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 45 | 88,89% | +14,71% | +14,71% | -2,17% | +18,96% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 40 | 47,50% | +14,96% | -1,69% | -1,88% | +19,47% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 13 | 38,46% | +18,78% | -9,63% | -0,70% | +23,30% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,87% | +5,87% | -2,41% | +8,88% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 30 | 90,00% | +23,48% | +19,07% | -2,95% | +28,12% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 32 | 100,00% | +23,45% | +23,45% | -3,00% | +28,03% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 32 | 100,00% | +23,45% | +23,45% | -3,00% | +28,03% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 28 | 100,00% | +23,79% | +23,79% | -2,78% | +28,44% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 27 | 37,04% | +23,90% | -4,53% | -2,73% | +28,53% | FEEDBACK RAPIDO |
| BTC | 45g | Classic technical | CALIBRABILE | 4 | 0,00% | +21,70% | -21,70% | -1,55% | +30,01% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 15 | 86,67% | +24,03% | +18,33% | -3,21% | +29,19% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 17 | 100,00% | +24,08% | +24,08% | -3,26% | +29,37% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 17 | 100,00% | +24,08% | +24,08% | -3,26% | +29,37% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 13 | 100,00% | +24,53% | +24,53% | -2,88% | +30,32% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 14 | 28,57% | +24,25% | -12,34% | -2,94% | +30,04% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 66 | 45,45% | +0,45% | +0,06% | -0,34% | +1,41% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 69 | 56,52% | +0,35% | +0,35% | -0,44% | +1,26% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 69 | 56,52% | +0,35% | +0,35% | -0,44% | +1,26% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 63 | 52,38% | +0,28% | +0,34% | -0,55% | +1,17% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 41 | 41,46% | +0,29% | -0,51% | -0,53% | +1,01% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 65 | 46,15% | +0,79% | +0,03% | -0,23% | +2,03% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 68 | 57,35% | +0,62% | +0,66% | -0,38% | +1,78% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 68 | 57,35% | +0,62% | +0,66% | -0,38% | +1,78% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 62 | 54,84% | +0,28% | +0,35% | -0,72% | +1,43% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 41 | 43,90% | +0,59% | -1,27% | -0,53% | +1,59% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 50,00% | +3,46% | +3,20% | +1,88% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 65 | 40,00% | +1,14% | +0,16% | -1,97% | +4,21% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 68 | 54,41% | +0,96% | +0,95% | -2,09% | +3,89% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 68 | 54,41% | +0,96% | +0,95% | -2,09% | +3,89% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 62 | 45,16% | +0,26% | +0,18% | -2,35% | +3,10% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 41 | 31,71% | +0,97% | -2,21% | -2,33% | +4,17% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 50,00% | +3,04% | +2,83% | -0,79% | +6,76% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 65 | 44,62% | +2,23% | +0,32% | -3,01% | +6,88% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 68 | 50,00% | +2,10% | +1,18% | -3,07% | +6,62% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 68 | 50,00% | +2,10% | +1,18% | -3,07% | +6,62% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 62 | 53,23% | +1,24% | -0,43% | -3,48% | +5,81% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 41 | 34,15% | +2,58% | -4,70% | -3,39% | +7,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 40,00% | +2,66% | +2,50% | -2,06% | +9,50% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 64 | 51,56% | +2,81% | +0,95% | -3,68% | +8,71% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 67 | 53,73% | +2,82% | +1,53% | -3,71% | +8,50% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 67 | 53,73% | +2,82% | +1,53% | -3,71% | +8,50% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 61 | 49,18% | +1,76% | -0,49% | -4,21% | +7,40% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 40 | 30,00% | +3,47% | -6,14% | -4,04% | +8,97% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,37% | -0,49% | -2,97% | +7,69% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 61 | 49,18% | +2,80% | +1,80% | -4,40% | +9,92% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 64 | 51,56% | +2,74% | +2,09% | -4,39% | +9,76% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 64 | 51,56% | +2,74% | +2,09% | -4,39% | +9,76% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 58 | 55,17% | +1,20% | -0,09% | -5,00% | +7,97% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 37 | 35,14% | +2,66% | -5,84% | -4,91% | +9,80% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | -0,68% | -1,01% | -4,16% | +8,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 57 | 66,67% | +4,47% | +6,18% | -4,84% | +13,00% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 60 | 68,33% | +4,07% | +4,89% | -4,81% | +12,60% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 60 | 68,33% | +4,07% | +4,89% | -4,81% | +12,60% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 54 | 59,26% | +1,56% | +1,24% | -5,51% | +9,34% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 34 | 50,00% | +3,40% | -3,09% | -5,30% | +11,12% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +5,41% | +1,04% | -4,48% | +13,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 50 | 70,00% | +7,94% | +5,69% | -4,39% | +18,45% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 53 | 73,58% | +8,37% | +8,30% | -4,45% | +18,70% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 53 | 73,58% | +8,37% | +8,30% | -4,45% | +18,70% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 47 | 59,57% | +5,74% | -1,88% | -5,22% | +14,83% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 31 | 48,39% | +5,15% | -7,22% | -4,78% | +14,11% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +6,66% | -0,06% | -3,62% | +19,12% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 43 | 81,40% | +13,42% | +8,23% | -4,09% | +27,04% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 45 | 91,11% | +13,78% | +12,77% | -4,11% | +27,62% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 45 | 91,11% | +13,78% | +12,77% | -4,11% | +27,62% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 38 | 50,00% | +11,94% | -7,12% | -4,89% | +24,74% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 30 | 46,67% | +11,08% | -9,11% | -4,75% | +22,89% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 85,71% | +23,10% | +14,05% | -3,96% | +33,14% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 30 | 33,33% | +22,55% | -4,09% | -4,56% | +40,41% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 32 | 50,00% | +22,50% | +2,73% | -4,56% | +40,39% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 32 | 50,00% | +22,50% | +2,73% | -4,56% | +40,39% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 30 | 53,33% | +22,12% | +4,79% | -4,61% | +40,31% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 30 | 0,00% | +21,64% | -21,64% | -4,76% | +40,02% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 22 | 0,00% | +22,71% | -22,71% | -4,86% | +39,94% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +37,31% | +15,91% | -1,31% | +47,38% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 17 | 0,00% | +21,97% | -21,97% | -6,05% | +39,36% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 17 | 5,88% | +21,97% | -16,43% | -6,05% | +39,36% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 17 | 5,88% | +21,97% | -16,43% | -6,05% | +39,36% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 15 | 6,67% | +19,62% | -13,34% | -6,36% | +38,14% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 17 | 0,00% | +21,97% | -21,97% | -6,05% | +39,36% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 16 | 0,00% | +22,42% | -22,42% | -5,92% | +39,62% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 62 | 53,23% | +0,53% | +0,43% | -0,19% | +1,39% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 65 | 55,38% | +0,48% | +0,47% | -0,35% | +1,33% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 68 | 54,41% | +0,51% | +0,40% | -0,32% | +1,35% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 62 | 48,39% | +0,51% | +0,06% | -0,39% | +1,32% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 44 | 50,00% | +0,83% | +0,19% | -0,23% | +1,74% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 61 | 47,54% | +1,19% | +1,08% | +0,05% | +2,22% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 64 | 45,31% | +1,04% | +0,67% | -0,24% | +1,89% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 67 | 44,78% | +1,01% | +0,62% | -0,24% | +1,93% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 61 | 40,98% | +0,83% | -0,05% | -0,19% | +1,93% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 43 | 48,84% | +1,00% | +0,44% | -0,14% | +2,00% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 61 | 54,10% | +1,92% | +1,78% | -1,63% | +4,32% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 64 | 48,44% | +1,67% | +1,21% | -1,82% | +4,07% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 67 | 47,76% | +1,61% | +1,15% | -1,80% | +4,04% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 61 | 45,90% | +1,20% | -0,26% | -1,84% | +3,54% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 43 | 51,16% | +1,26% | +0,59% | -1,75% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 61 | 57,38% | +3,32% | +3,23% | -2,38% | +6,83% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 64 | 53,12% | +2,98% | +2,13% | -2,56% | +6,48% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 67 | 52,24% | +2,88% | +2,01% | -2,53% | +6,37% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 61 | 45,90% | +2,55% | -0,59% | -2,61% | +5,87% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 43 | 53,49% | +1,81% | +0,92% | -2,55% | +5,09% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 61 | 62,30% | +4,75% | +4,83% | -2,84% | +8,73% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 63 | 58,73% | +4,13% | +3,12% | -3,08% | +8,15% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 66 | 59,09% | +3,94% | +2,99% | -3,06% | +7,95% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 60 | 40,00% | +3,00% | -1,18% | -3,19% | +7,12% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 42 | 47,62% | +1,36% | +1,40% | -3,24% | +5,52% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 58 | 65,52% | +6,08% | +6,21% | -3,24% | +10,49% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 60 | 61,67% | +5,42% | +4,66% | -3,53% | +9,67% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 63 | 60,32% | +5,16% | +4,45% | -3,53% | +9,40% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 60 | 48,33% | +4,34% | -1,26% | -3,67% | +8,74% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 42 | 54,76% | +1,60% | +1,69% | -3,81% | +6,40% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |

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

Generato: 2026-09-23 05:33 UTC

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
| BTC | 71 | UTILE | 70 | 19 | 13 | 0 | Famiglia statistica | 1g | 54,29% | +0,40% | campione utile, valutare con prudenza |
| SOL | 71 | UTILE | 65 | 27 | 12 | 0 | Famiglia statistica | 1g | 55,38% | +0,47% | campione utile, valutare con prudenza |
| DOGE | 71 | UTILE | 69 | 29 | 12 | 0 | Famiglia statistica | 1g | 56,52% | +0,35% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 28 | 39,29% | +0,16% | +0,86% | +0,02% | +1,38% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 70 | 54,29% | +0,40% | +0,40% | -0,13% | +0,91% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 6 | 50,00% | +0,17% | +0,17% | -0,29% | +0,65% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 63 | 41,27% | +0,08% | +0,41% | -0,05% | +0,93% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 28 | 42,86% | +0,13% | +1,35% | +0,35% | +2,03% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 69 | 53,62% | +0,78% | +0,78% | +0,04% | +1,43% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 62 | 43,55% | +0,07% | +0,74% | +0,18% | +1,38% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 28 | 39,29% | -0,42% | +2,14% | -0,72% | +3,60% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 69 | 53,62% | +1,15% | +1,15% | -1,12% | +2,80% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 62 | 37,10% | -0,14% | +1,22% | -1,02% | +2,87% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 28 | 42,86% | -2,17% | +4,36% | -1,11% | +6,49% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 69 | 50,72% | +2,06% | +2,06% | -1,72% | +4,43% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 62 | 41,94% | -0,73% | +2,00% | -1,64% | +4,42% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 27 | 40,74% | -3,76% | +5,59% | -1,42% | +8,56% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 68 | 58,82% | +2,77% | +2,77% | -2,06% | +5,49% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 62 | 43,55% | -1,13% | +2,98% | -1,96% | +5,69% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 24 | 50,00% | -3,59% | +5,20% | -1,59% | +8,77% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 65 | 63,08% | +3,38% | +3,38% | -2,40% | +6,39% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 60 | 48,33% | -0,68% | +3,76% | -2,25% | +6,82% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 24 | 29,17% | -3,41% | +4,78% | -1,84% | +9,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 61 | 57,38% | +4,73% | +4,73% | -2,59% | +8,30% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 56 | 53,57% | +0,94% | +5,27% | -2,42% | +8,89% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 22 | 50,00% | -5,00% | +9,06% | -2,06% | +12,94% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 54 | 72,22% | +8,44% | +8,44% | -2,48% | +12,33% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 3 | 66,67% | -0,54% | -0,54% | -2,98% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 49 | 46,94% | -0,15% | +9,14% | -2,28% | +13,09% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 13 | 38,46% | -9,63% | +18,78% | -0,70% | +23,30% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 45 | 88,89% | +14,71% | +14,71% | -2,17% | +18,96% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +5,87% | +5,87% | -2,41% | +8,88% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 40 | 47,50% | -1,69% | +14,96% | -1,88% | +19,47% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 4 | 0,00% | -21,70% | +21,70% | -1,55% | +30,01% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 32 | 100,00% | +23,45% | +23,45% | -3,00% | +28,03% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 27 | 37,04% | -4,53% | +23,90% | -2,73% | +28,53% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 17 | 100,00% | +24,08% | +24,08% | -3,26% | +29,37% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 14 | 28,57% | -12,34% | +24,25% | -2,94% | +30,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 41 | 41,46% | -0,51% | +0,29% | -0,53% | +1,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 69 | 56,52% | +0,35% | +0,35% | -0,44% | +1,26% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 11 | 63,64% | +2,53% | +2,82% | +0,75% | +3,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 63 | 52,38% | +0,34% | +0,28% | -0,55% | +1,17% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 41 | 43,90% | -1,27% | +0,59% | -0,53% | +1,59% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 68 | 57,35% | +0,66% | +0,62% | -0,38% | +1,78% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 10 | 50,00% | +3,20% | +3,46% | +1,88% | +5,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 62 | 54,84% | +0,35% | +0,28% | -0,72% | +1,43% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 41 | 31,71% | -2,21% | +0,97% | -2,33% | +4,17% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 68 | 54,41% | +0,95% | +0,96% | -2,09% | +3,89% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 10 | 50,00% | +2,83% | +3,04% | -0,79% | +6,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 62 | 45,16% | +0,18% | +0,26% | -2,35% | +3,10% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 41 | 34,15% | -4,70% | +2,58% | -3,39% | +7,30% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 68 | 50,00% | +1,18% | +2,10% | -3,07% | +6,62% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 10 | 40,00% | +2,50% | +2,66% | -2,06% | +9,50% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 62 | 53,23% | -0,43% | +1,24% | -3,48% | +5,81% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 40 | 30,00% | -6,14% | +3,47% | -4,04% | +8,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 67 | 53,73% | +1,53% | +2,82% | -3,71% | +8,50% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 9 | 44,44% | -0,49% | -0,37% | -2,97% | +7,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 61 | 49,18% | -0,49% | +1,76% | -4,21% | +7,40% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 37 | 35,14% | -5,84% | +2,66% | -4,91% | +9,80% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 64 | 51,56% | +2,09% | +2,74% | -4,39% | +9,76% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 9 | 55,56% | -1,01% | -0,68% | -4,16% | +8,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 58 | 55,17% | -0,09% | +1,20% | -5,00% | +7,97% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 34 | 50,00% | -3,09% | +3,40% | -5,30% | +11,12% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 60 | 68,33% | +4,89% | +4,07% | -4,81% | +12,60% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 9 | 44,44% | +1,04% | +5,41% | -4,48% | +13,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 54 | 59,26% | +1,24% | +1,56% | -5,51% | +9,34% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 31 | 48,39% | -7,22% | +5,15% | -4,78% | +14,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 53 | 73,58% | +8,30% | +8,37% | -4,45% | +18,70% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 8 | 62,50% | -0,06% | +6,66% | -3,62% | +19,12% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 47 | 59,57% | -1,88% | +5,74% | -5,22% | +14,83% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 30 | 46,67% | -9,11% | +11,08% | -4,75% | +22,89% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 45 | 91,11% | +12,77% | +13,78% | -4,11% | +27,62% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 7 | 85,71% | +14,05% | +23,10% | -3,96% | +33,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 38 | 50,00% | -7,12% | +11,94% | -4,89% | +24,74% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 22 | 0,00% | -22,71% | +22,71% | -4,86% | +39,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 32 | 50,00% | +2,73% | +22,50% | -4,56% | +40,39% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,91% | +37,31% | -1,31% | +47,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 30 | 0,00% | -21,64% | +21,64% | -4,76% | +40,02% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 16 | 0,00% | -22,42% | +22,42% | -5,92% | +39,62% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 17 | 5,88% | -16,43% | +21,97% | -6,05% | +39,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 17 | 0,00% | -21,97% | +21,97% | -6,05% | +39,36% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 44 | 50,00% | +0,19% | +0,83% | -0,23% | +1,74% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 65 | 55,38% | +0,47% | +0,48% | -0,35% | +1,33% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 62 | 48,39% | +0,06% | +0,51% | -0,39% | +1,32% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 43 | 48,84% | +0,44% | +1,00% | -0,14% | +2,00% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 64 | 45,31% | +0,67% | +1,04% | -0,24% | +1,89% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 61 | 40,98% | -0,05% | +0,83% | -0,19% | +1,93% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 43 | 51,16% | +0,59% | +1,26% | -1,75% | +3,53% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 64 | 48,44% | +1,21% | +1,67% | -1,82% | +4,07% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 61 | 45,90% | -0,26% | +1,20% | -1,84% | +3,54% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 43 | 53,49% | +0,92% | +1,81% | -2,55% | +5,09% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 64 | 53,12% | +2,13% | +2,98% | -2,56% | +6,48% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 61 | 45,90% | -0,59% | +2,55% | -2,61% | +5,87% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 42 | 47,62% | +1,40% | +1,36% | -3,24% | +5,52% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 63 | 58,73% | +3,12% | +4,13% | -3,08% | +8,15% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 60 | 40,00% | -1,18% | +3,00% | -3,19% | +7,12% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 42 | 54,76% | +1,69% | +1,60% | -3,81% | +6,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 60 | 61,67% | +4,66% | +5,42% | -3,53% | +9,67% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 60 | 48,33% | -1,26% | +4,34% | -3,67% | +8,74% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 42 | 52,38% | +2,18% | +3,36% | -4,30% | +8,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 56 | 73,21% | +7,42% | +8,14% | -3,79% | +13,13% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 58 | 43,10% | -2,76% | +6,42% | -4,02% | +11,63% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Classic technical | 35 | 57,14% | -3,42% | +10,00% | -4,22% | +15,23% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 49 | 79,59% | +14,51% | +14,56% | -3,84% | +20,40% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 51 | 47,06% | -8,35% | +12,06% | -4,22% | +17,86% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 26 | 26,92% | -16,45% | +26,41% | -3,55% | +32,17% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 40 | 85,00% | +22,31% | +26,18% | -3,47% | +33,05% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 3 | 100,00% | +22,86% | +22,86% | -3,34% | +27,23% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 42 | 21,43% | -17,20% | +22,92% | -4,00% | +29,36% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 21 | 0,00% | -38,81% | +38,81% | -4,64% | +48,52% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 28 | 71,43% | +21,35% | +38,26% | -5,06% | +46,56% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,56% | +44,56% | -5,94% | +49,24% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 31 | 12,90% | -31,05% | +37,40% | -5,38% | +45,67% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 9 | 0,00% | -42,37% | +42,37% | -6,82% | +50,35% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 13 | 38,46% | -2,83% | +39,15% | -7,74% | +47,27% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +41,93% | +41,93% | -9,62% | +45,82% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 17 | 23,53% | -22,64% | +38,59% | -7,53% | +47,05% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 67 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 70 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 84 | 40,48% | -0,04% |
| BTC | BREVE | Famiglia statistica | 208 | 53,85% | +0,77% |
| BTC | BREVE | Microstruttura exchange | 16 | 43,75% | +0,40% |
| BTC | BREVE | Tecnico | 187 | 40,64% | +0,01% |
| BTC | SETTIMANALE | Classic technical | 79 | 44,30% | -3,15% |
| BTC | SETTIMANALE | Famiglia statistica | 202 | 57,43% | +2,72% |
| BTC | SETTIMANALE | Microstruttura exchange | 15 | 33,33% | -1,25% |
| BTC | SETTIMANALE | Tecnico | 184 | 44,57% | -0,85% |
| BTC | SWING | Classic technical | 46 | 39,13% | -4,17% |
| BTC | SWING | Famiglia statistica | 115 | 64,35% | +6,47% |
| BTC | SWING | Microstruttura exchange | 8 | 50,00% | -0,03% |
| BTC | SWING | Tecnico | 105 | 50,48% | +0,43% |
| BTC | MEDIO | Classic technical | 17 | 29,41% | -12,47% |
| BTC | MEDIO | Famiglia statistica | 94 | 94,68% | +19,38% |
| BTC | MEDIO | Microstruttura exchange | 4 | 100,00% | +14,55% |
| BTC | MEDIO | Tecnico | 81 | 40,74% | -4,48% |
| DOGE | BREVE | Classic technical | 123 | 39,02% | -1,33% |
| DOGE | BREVE | Famiglia statistica | 205 | 56,10% | +0,65% |
| DOGE | BREVE | Microstruttura exchange | 31 | 54,84% | +2,84% |
| DOGE | BREVE | Tecnico | 187 | 50,80% | +0,29% |
| DOGE | SETTIMANALE | Classic technical | 118 | 33,05% | -5,54% |
| DOGE | SETTIMANALE | Famiglia statistica | 199 | 51,76% | +1,59% |
| DOGE | SETTIMANALE | Microstruttura exchange | 28 | 46,43% | +0,41% |
| DOGE | SETTIMANALE | Tecnico | 181 | 52,49% | -0,34% |
| DOGE | SWING | Classic technical | 65 | 49,23% | -5,06% |
| DOGE | SWING | Famiglia statistica | 113 | 70,80% | +6,49% |
| DOGE | SWING | Microstruttura exchange | 17 | 52,94% | +0,53% |
| DOGE | SWING | Tecnico | 101 | 59,41% | -0,21% |
| DOGE | MEDIO | Classic technical | 68 | 20,59% | -16,64% |
| DOGE | MEDIO | Famiglia statistica | 94 | 61,70% | +4,07% |
| DOGE | MEDIO | Microstruttura exchange | 13 | 84,62% | +19,38% |
| DOGE | MEDIO | Tecnico | 85 | 22,35% | -15,21% |
| SOL | BREVE | Classic technical | 130 | 50,00% | +0,41% |
| SOL | BREVE | Famiglia statistica | 193 | 49,74% | +0,78% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 184 | 45,11% | -0,08% |
| SOL | SETTIMANALE | Classic technical | 127 | 51,97% | +1,34% |
| SOL | SETTIMANALE | Famiglia statistica | 187 | 57,75% | +3,28% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 181 | 44,75% | -1,01% |
| SOL | SWING | Classic technical | 77 | 54,55% | -0,37% |
| SOL | SWING | Famiglia statistica | 105 | 76,19% | +10,73% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 109 | 44,95% | -5,38% |
| SOL | MEDIO | Classic technical | 56 | 12,50% | -29,00% |
| SOL | MEDIO | Famiglia statistica | 81 | 72,84% | +17,95% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 6 | 100,00% | +33,27% |
| SOL | MEDIO | Tecnico | 90 | 18,89% | -23,00% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 4 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 2 | in attesa di controlli maturati |
| DOGE | MEDIO | 3 | in attesa di controlli maturati |

## Come leggere le raccomandazioni

- **OSSERVA**: meno di 30 controlli, nessuna modifica.
- **PESO OK / MANTIENI**: il modulo sta aiutando, ma non serve cambiare peso.
- **NON AUMENTARE**: il modulo non dimostra ancora un vantaggio sufficiente.
- **POSSIBILE AUMENTO LEGGERO**: proposta prudente, mai automatica.
- **POSSIBILE RIDUZIONE**: modulo debole con campione già abbastanza maturo.
- **ESCLUSO**: benchmark o diagnostica già inclusa in un'altra famiglia.

Nota decisiva: **non sommare mai una modifica alla Famiglia statistica e altre modifiche separate a Scanner o Market Regime**. Scanner e Market servono soltanto a capire quale parte della famiglia sta funzionando o fallendo.

## Stato attuale

Il campione comincia a essere utile. Le proposte restano prudenti e vanno verificate tra orizzonti diversi.
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

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato            | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:-----------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         71 |              45 |          26 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         71 |              45 |          26 | OSSERVAZIONE 30+ | 2,22%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         71 |              45 |          26 | OSSERVAZIONE 30+ | 11,11%           | 4,44%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | MEDIO          | ALTO           | spot/tranche; se proprio leva, massimo 2x con margine molto largo       |
| SOL     | ALTO           | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| DOGE    | MOLTO ALTO     | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-09-23 05:32 UTC


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
| BTC | +7 | POSITIVA FORTE | Rialzista | MEDIA / ALTA | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA | Prima resistenza sopra 82.262; conferma del doppio minimo sopra 82.262. | Sotto 74.945 il quadro tecnico peggiora. |
| SOL | +4 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | HOLD / TRANCHE PICCOLE, NO LEVA | Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 107,12; milestone analogiche 166,95 / 179,63, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 113,00 / 96,23 / 62,19. |
| DOGE | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.11825 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.07841 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | 0 | +3 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +7 |
| SOL | +1 | 0 | +1 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | +4 |
| DOGE | -2 | 0 | -2 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +2 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **POSITIVA FORTE**
- Bias: **Rialzista**
- Punteggio finale: **+7**
- Affidabilità: **MEDIA / ALTA**
- Azione coerente: **ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA**

BTC ha una confluenza positiva forte. Resta comunque necessario evitare leva eccessiva: la conferma deve arrivare da prezzo e resistenze, non solo dallo score.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 75,00%, return centrale 30g +13,91%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 68. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 12/12, verdetto rialzista tecnico, trend rialzista, struttura volatilità in espansione, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score +1 (rialzista Doppio minimo / ATTIVO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 7/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +1.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.50; exchange 3/3, copertura 93%, consenso bull 1, bear 1, divergenze 0, campioni 4h 8 su 3.50h; candidato +1, peso Global +0 (LOCKED / RACCOLTA 7G). Bias POSITIVA / CANDIDATA, ANCORA NON PESATA; confidenza ALTA; fonti 3/3; KuCoin OK; copertura 93,33%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +1 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — BTC: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: Prima resistenza sopra 82.262; conferma del doppio minimo sopra 82.262.

Invalidazioni: Sotto 74.945 il quadro tecnico peggiora.

### SOL

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+4**
- Affidabilità: **MEDIA**
- Azione coerente: **HOLD / TRANCHE PICCOLE, NO LEVA**

SOL ha una confluenza costruttiva, ma va ancora trattato come setup anticipato. La conferma vera arriva solo sopra le resistenze tecniche e con rientro del gap frattale. Il modulo lifecycle/EMA200 resta utile come contesto, ma non aumenta il punteggio Global.

Dettaglio moduli:

- Famiglia statistica: **+1** — Scanner grezzo +1, Market Regime grezzo 0, match regime 1. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+1** — Casi positivi 52,50%, return centrale 30g +2,40%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 1, positivi 30g 100,00%, return p50 +48,11%.
- Scanner path: **0** — Controlli disponibili 68. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 9/12, verdetto rialzista tecnico, trend rialzista, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Triplo massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 9/12, verdetto CONFERMATO RIALZISTA, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto STRUTTURA ANALOGA, PREZZO NON ADERENTE, somiglianza strutturale +68,63%, aderenza live +69,67%, errore live +15,17%, gap corrente +49,58%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE NON CONFERMATO DAL PREZZO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 69, ma percorso ancorato non aderente: gap +49,58%, errore live +15,17%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 1, bias CONTESTO DA OSSERVARE, EMA200 111,29 $, upside EMA200 -6,44%, gap EMA50/EMA200 -5,16%, hit EMA200 12w +100,00%, trend PEGGIORAMENTO. Peso Global forzato a 0.
- Exchange flow: **0** — Flow -0.25, derivati +1.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 0, campioni 4h 8 su 3.50h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — SOL: cambiamento medio in peggioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 107,12; milestone analogiche 166,95 / 179,63, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 113,00 / 96,23 / 62,19.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **-2** — Scanner grezzo -2, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-2** — Casi positivi 27,50%, return centrale 30g -8,60%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 68. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 10/12, verdetto rialzista tecnico, trend rialzista, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score +1 (rialzista Doppio minimo / ATTIVO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 9/12, verdetto CONFERMATO RIALZISTA, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.50; exchange 3/3, copertura 100%, consenso bull 0, bear 2, divergenze 1, campioni 4h 8 su 3.50h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: Sopra 0.11825 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.

Invalidazioni: Sotto 0.07841 il rischio ribassista aumenta.


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

Generato: 2026-09-23 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 86.710 $ | prezzo corrente |
| Power Law centrale | 125.716 $ | deviazione -31,03% |
| Banda p10-p90 | 78.073 $ / 316.894 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 19,55% | posizione storica nel corridoio |
| Esponente β | 5,7951 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3167 cambiando finestra |
| Ultimo halving | 2024-04-19 | 887 giorni fa |
| Fase ciclo | 60,71% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-09-23 (4389 osservazioni)
- Formula stimata: prezzo ≈ exp(-38.9889) × giorni^5.7951
- Prezzo centrale oggi: **125.716 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 19,55%
- Scarto dal centro: **-31,03%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,7951 | 91,93% |
| 2015 | 5,8762 | 91,48% |
| 2016 | 5,5592 | 87,74% |
| 2017 | 4,8330 | 82,97% |
| 2018 | 4,5595 | 78,51% |

### Backtest walk-forward contro prezzo invariato

| Orizzonte | Controlli | Vittorie vs naive | Errore mediano modello | Errore mediano naive |
| --- | --- | --- | --- | --- |
| 90g | 81 | 28,40% | 50,97% | 20,89% |
| 180g | 81 | 41,98% | 59,41% | 47,18% |
| 365g | 81 | 58,02% | 72,28% | 81,57% |
| 730g | 81 | 58,02% | 72,72% | 108,81% |

## Bitcoin Four-Year Spiral

Nel grafico l'angolo rappresenta il tempo dentro una finestra di quattro anni e il raggio rappresenta il prezzo in scala logaritmica. ATH, bottom storici e halving sono marker descrittivi: la spirale rende visibili le ricorrenze, ma non dimostra che il ciclo futuro debba ripetersi.

![Bitcoin Four-Year Spiral](bitcoin_four_year_spiral.png)

## Stessa fase dei cicli halving precedenti

| Ciclo | Data analoga | +30g | +90g | +180g | +365g |
| --- | --- | --- | --- | --- | --- |
| 2012-11-28 → 2016-07-09 | 2015-02-07 | +27,16% | +7,07% | +22,31% | +65,36% |
| 2016-07-09 → 2020-05-11 | 2018-11-07 | -47,63% | -46,92% | -12,00% | +41,92% |
| 2020-05-11 → 2024-04-19 | 2022-10-02 | +7,57% | -13,11% | +49,54% | +44,56% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 6 | 1 | 11.734521881908599 | 0 |
| DOGE | DOGE/BTC | RELATIVA MISTA / NON CONFERMATA | -1 | 0 | -1.9072182870636722 | 0 |

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

Generato: 2026-09-23 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00137210 | +6 | +1 | 0 | SOVRAPERFORMA BTC | MEDIA | +11,73% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000118 | -1 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | -1,91% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** SOVRAPERFORMA BTC (+6)
- **Candidato futuro:** +1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** CONFERMA FORTE: sale in USD e batte BTC
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g +7,03%; 30g +11,73%; 90g +23,06%; 180g +9,16%
- **Daily:** RSI 62.10; MA50 0.00126308; MA200 0.00118809
- **Weekly:** MA30 0.00119604; RSI 61.02
- **Livelli:** supporto 0.00127800; resistenza 0.00140500; breakout 60g 0.00140500; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00133900; target 0.00140150
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00131154
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; RSI relativo forte; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (-1)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g +11,28%; 30g -1,91%; 90g -5,43%; 180g -11,90%
- **Daily:** RSI 66.62; MA50 0.00000110; MA200 0.00000124
- **Weekly:** MA30 0.00000124; RSI 46.33
- **Livelli:** supporto 0.00000116; resistenza 0.00000119; breakout 60g 0.00000131; breakdown 60g 0.00000099
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** VICINO — 38.2% a 0.00000119
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; RSI relativo forte; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 209 | 52,63% | +1,96% | -1,05% |
| SOL | 30g | 206 | 47,57% | +4,57% | +0,58% |
| SOL | 90g | 200 | 52,50% | +9,74% | +3,06% |
| DOGE | 7g | 295 | 55,59% | +1,83% | -1,68% |
| DOGE | 30g | 294 | 53,06% | +1,97% | -3,49% |
| DOGE | 90g | 287 | 54,01% | +6,88% | -9,23% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 36 | 55,56% | +0,13% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 35 | 54,29% | +0,48% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 35 | 42,86% | +0,55% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 35 | 45,71% | +0,61% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 21 | 28,57% | -5,51% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 54 | 66,67% | -0,02% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 54 | 57,41% | +0,01% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 53 | 54,72% | -0,60% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 46 | 58,70% | +0,14% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 35 | 65,71% | +0,39% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **23 settembre 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 118,95 $ | 2026-09-23T05:30:23Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 118,96 $ | 2026-09-23T05:32:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 1m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | 0,01000 $ | +0,01% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=118.94999694824219
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-09-23T05:30:23Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=118.95999908447266
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-09-23T05:32:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-09-23T05:32:07Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=104.503549
ANCHOR_AGE_HOURS=0.029028763611111112
CURRENT_VS_ANCHOR_GAP_USD=0.01000213623046875
CURRENT_VS_ANCHOR_GAP_PCT=0.008408689774763722
```

## Verdetto: STRUTTURA ANALOGA, PREZZO NON ADERENTE

- **Fase attuale:** FRATTALE NON CONFERMATO DAL PREZZO
- **Somiglianza totale:** +68,63%
- **Somiglianza strutturale:** +68,63%
- **Aderenza prezzo live:** +69,67%
- **Errore medio live:** +15,17%
- **Gap prezzo corrente:** +49,58%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA / NON OPERATIVO
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** La geometria ricorda BTC 2022, ma SOL è troppo distante dal percorso scalato per usarlo come conferma operativa.
- **SOL è al giorno:** 109 dal bottom usato.
- **Giorno BTC equivalente:** 2023-03-10
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Spinta rialzista abbastanza pulita.** Zona bassa **118,95 $** intorno al **23 settembre 2026**; zona alta **166,95 $** intorno al **6 ottobre 2026**; fine step circa **162,00 $** entro il **7 ottobre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=STRUTTURA ANALOGA, PREZZO NON ADERENTE
PRICE_ADHERENCE_FAILED=YES
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=YES
PRICE_ADHERENCE_LAST_GAP_FAILED=YES
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=15.166257035667302
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=49.580726377067165
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 23 settembre 2026 | 83 | +69,67% | +15,17% | +49,58% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 23 settembre 2026 | 110 | +74,16% | +12,92% | +49,58% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: STRUTTURA ANALOGA, PREZZO NON ADERENTE.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: STRUTTURA ANALOGA, PREZZO NON ADERENTE. |
| Aderenza live | +69,67% | Errore medio live +15,17%. |
| Gap corrente | +49,58% | Prezzo non aderente: superata almeno una soglia canonica (15% medio / 18% ultimo). |
| Prima conferma prezzo | 166,95 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 179,63 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 113,00 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 735,08 $ |
| Massimo percorso base | 735,08 $ (21 aprile 2029) |

## Grafici

### Grafico frattale sovrapposto

Scala normalizzata base 100; valori non USD.

![Frattale BTC 2022 vs SOL 2026](btc_2022_vs_sol_2026_fractal_chart.png)

### Grafico proiezione condizionale

Serie e proiezioni ancorate all'input computazionale; riferimento pubblico separato e solo display.

![Proiezione SOL BTC 2022](btc_2022_vs_sol_2026_projection_chart.png)

### Grafico ciclo base

Scenario analogico in USD; non previsione live e non segnale di trading.

![Ciclo base SOL BTC 2025](btc_2022_vs_sol_2026_cycle_base_chart.png)

### Grafico struttura vs aderenza

![Tracking frattale BTC SOL](btc_2022_vs_sol_2026_tracking_chart.png)

## Livelli chiave

| Livello | Prezzo / soglia | Lettura |
| --- | --- | --- |
| Rientro gap | entro ±12% | Condizione necessaria per tornare operativo. |
| Prima conferma | 166,95 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 179,63 $ | Scenario più credibile. |
| Invalidazione soft | 113,00 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 30 settembre 2026 | +35,85% | 161,59 $ | 118,95 $ | 161,59 $ |
| 14 giorni | 7 ottobre 2026 | +36,19% | 162,00 $ | 118,95 $ | 166,95 $ |
| 30 giorni | 23 ottobre 2026 | +40,35% | 166,95 $ | 118,95 $ | 167,80 $ |
| 60 giorni | 22 novembre 2026 | +37,01% | 162,97 $ | 118,95 $ | 179,63 $ |
| 90 giorni | 22 dicembre 2026 | +31,31% | 156,20 $ | 118,95 $ | 179,63 $ |
| 120 giorni | 21 gennaio 2027 | +50,06% | 178,49 $ | 118,95 $ | 183,58 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 23 settembre 2026 -> 7 ottobre 2026 | +36,19% | 118,95 $ (23 settembre 2026) | 166,95 $ (6 ottobre 2026) | 162,00 $ | Spinta rialzista abbastanza pulita. |
| Step 2 - primo mese | 8 ottobre 2026 -> 23 ottobre 2026 | +40,35% | 159,92 $ (10 ottobre 2026) | 167,80 $ (14 ottobre 2026) | 166,95 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 24 ottobre 2026 -> 22 novembre 2026 | +37,01% | 160,72 $ (4 novembre 2026) | 179,63 $ (28 ottobre 2026) | 162,97 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 23 novembre 2026 -> 22 dicembre 2026 | +31,31% | 151,79 $ (19 dicembre 2026) | 165,49 $ (11 dicembre 2026) | 156,20 $ | Spinta rialzista abbastanza pulita. |

Nota: le proiezioni restano condizionali; il prezzo non è aderente secondo le soglie canoniche.

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
| Prezzo SOL | 118,95 $ |  |
| Weekly RSI | 64,32 / linea grezza 51,77 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 50,17 / linea grezza 55,48 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 735,08 $ | Avanzamento +16,18% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 50,2, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Prezzo SOL | 118,95 $ |
| TVL Solana | 6,53 mld $ |
| TVL 7g | +14,00% |
| DEX volume 24h | 3,45 mld $ |
| Fees 24h | 17,84 mln $ |
| Stablecoin su Solana | 16,82 mld $ |
| Stake ratio | 69,32% |
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

| Voce                      | Valore                       |
|:--------------------------|:-----------------------------|
| Lifecycle squeeze score | 1 |
| Bias | CONTESTO DA OSSERVARE |
| Azione coerente | SOLO OSSERVAZIONE |
| Peso suggerito Global | 0 |
| Trend squeeze | PEGGIORAMENTO |
| Trend squeeze score | -1 |
| Confronto precedente | 2026-09-21 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 118,95 $ |
| EMA200 weekly target | 111,29 $ |
| Upside verso EMA200 | -6,44% |
| Distanza prezzo da EMA200 | +6,88% |
| Gap EMA50/EMA200 | -5,16% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 64,32 |
| Età SOL | 6,5 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +100,00% |
| Max gain mediano 12w | +27,43% |
| Drawdown mediano 12w | -17,31% |

Lettura semplice:

**SOLO OSSERVAZIONE**

Autocontrollo: **PEGGIORAMENTO**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-09-23 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-09-23 05:30:24 UTC**

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
- SOL: cambiamento importante in peggioramento rispetto a ieri.
- DOGE: nessun cambiamento forte rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | NESSUN CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +75.00% | +5.00 punti |
| SOL | CAMBIAMENTO MEDIO | peggioramento | NEUTRALE / INCERTO | +52.50% | -2.50 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | miglioramento | RIBASSISTA | +27.50% | -5.00 punti |

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
| BTC | 82.413 $ | 95.426 $ | +47,06% | +15,79% | rimbalzo debole | 95.426 $ | 82.413 $ | +6,67% | -13,64% | spike storicamente più resistente |
| SOL | 113,00 $ | 130,84 $ | +28,00% | +15,79% | rimbalzo poco frequente | 130,84 $ | 113,00 $ | +20,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,09699 $ | 0,11231 $ | +25,00% | +15,79% | rimbalzo poco frequente | 0,11231 $ | 0,09699 $ | +47,62% | -13,64% | scarico possibile |

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

- **BTC: su 40 casi simili, 17 prima sono scesi a -5,00%. Tra quei 17, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +47,06% (8/17). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 2 poi sono scaricati a -5,00%. Percentuale: +6,67% (2/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +28,00% (7/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 5 poi sono scaricati a -5,00%. Percentuale: +20,00% (5/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 36 prima sono scesi a -5,00%. Tra quei 36, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +25,00% (9/36). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 21 prima sono saliti a +10,00%. Tra quei 21, 10 poi sono scaricati a -5,00%. Percentuale: +47,62% (10/21). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-09-23 05:31:53 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [scanner_forecast_tracker_report.md](scanner_forecast_tracker_report.md)

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-09-23 | 2026-09-23T05:30:23Z | 2026-09-23 05:30:24 |
| SOL | 2026-09-23 | 2026-09-23T05:30:23Z | 2026-09-23 05:30:24 |
| DOGE | 2026-09-23 | 2026-09-23T05:30:23Z | 2026-09-23 05:30:24 |

La data di generazione del report non sostituisce la data degli input: se gli snapshot locali sono più vecchi, i valori restano riferiti agli snapshot indicati in tabella.

Questo report trasforma i 40 casi simili dello scanner in un cono previsionale leggibile.

Per ogni asset crea:

- banda larga p10-p90
- banda centrale p25-p75
- scenario centrale p50
- prezzo reale sovrapposto quando sono disponibili dati successivi

Correzione importante: il cono ora viene calcolato dai percorsi reali dei match storici, non solo dai percentili finali a 30 giorni. Quindi il grafico non deve più mostrare solo due puntini.

## Ultimo cono previsionale salvato

| Asset   | Data       | Prezzo iniziale   | Direzione scanner   | Casi positivi   | P10 30g     | P25 30g     | P50 30g     | P75 30g      | P90 30g      |
|:--------|:-----------|:------------------|:--------------------|:----------------|:------------|:------------|:------------|:-------------|:-------------|
| BTC | 2026-09-23 | 86.751 $ | SALITA | 75,00% | 69.196,10 $ | 86.820,07 $ | 98.819,34 $ | 110.155,39 $ | 143.053,32 $ |
| SOL | 2026-09-23 | 118,95 $ | INCERTO | 52,50% | 87,30 $ | 98,42 $ | 121,80 $ | 149,83 $ | 200,60 $ |
| DOGE | 2026-09-23 | 0.10210 $ | DISCESA | 27,50% | 0.04131 $ | 0.08357 $ | 0.09332 $ | 0.10549 $ | 0.13604 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 1 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 98.819,34 $ | n/a | 143.053,32 $ | n/a |
| SOL | INSUFFICIENT_REGIME_MATCHES | NONE | 1 | 2 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 121,80 $ | n/a | 200,60 $ | n/a |
| DOGE | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 0.09332 $ | n/a | 0.13604 $ | n/a |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-08-24**; verificato fino al **2026-09-23**; stato **COMPLETO 30/30g**.
- Reale **86.755,43 $**; p50 previsto **81.546,42 $**; scarto **6,39%**.
- Errore medio assoluto **2,40%**; massimo **6,39%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

<!-- SOL_CONDITIONAL_ANALYSES_START -->
#### SOL — Analisi condizionata -5% → +10%

Queste analisi sono **separate dal cono SOL originale**. Il cono sopra continua a usare normalmente i **40 analoghi più simili a SOL**.

Il filtro condizionato parte proprio da quei 40 casi e conserva soltanto gli episodi che hanno toccato **prima -5%** dal proprio baseline e **successivamente +10% entro 30 giorni**.

##### A. Conditional Successor corrente — dinamico

Questo campione viene ricostruito ad ogni run dai **40 analoghi SOL correnti**. Di conseguenza il numero di episodi qualificati e gli asset possono cambiare giorno per giorno.

**Campione corrente:** 7 episodi qualificati su 40 · 7 asset distinti.

**SMALL SAMPLE / DIAGNOSTIC ONLY:** le frequenze empiriche non sono probabilità calibrate.

![SOL conditional successor corrente](scanner_forecast_SOL_conditional_successor_current.png)

###### Confronto diretto a 30 giorni

| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Cono standard | 2026-09-23 | 40 | 2026-10-23 | 87.30 $ | 98.42 $ | 121.80 $ | 149.83 $ | 200.60 $ |
| Conditional corrente | 2026-09-23 | 7 | 2026-10-23 | 96.39 $ | 116.69 $ | 150.28 $ | 193.17 $ | 220.98 $ |

###### Struttura successiva dei casi correnti

| Classe | Episodi | Frequenza empirica |
| --- | ---: | ---: |
| DIRECT_CONTINUATION | 5 | 71.43% |
| SHALLOW_PULLBACK_THEN_CONTINUATION | 0 | 0.00% |
| DEEP_PULLBACK_THEN_RECOVERY | 1 | 14.29% |
| FAILURE | 1 | 14.29% |
| UNRESOLVED | 0 | 0.00% |

###### Episodi qualificati oggi

| Asset | Match window | -5% hit | +10% anchor | Classe 60d |
| --- | --- | --- | --- | --- |
| THETA-USD | 2023-08-28 → 2023-12-05 | 2023-12-06 | 2023-12-24 | DIRECT_CONTINUATION |
| BTC-USD | 2022-11-10 → 2023-02-17 | 2023-02-24 | 2023-03-17 | DIRECT_CONTINUATION |
| HBAR-USD | 2020-11-09 → 2021-02-16 | 2021-02-23 | 2021-03-04 | DEEP_PULLBACK_THEN_RECOVERY |
| RUNE-USD | 2020-04-02 → 2020-07-10 | 2020-07-13 | 2020-07-20 | DIRECT_CONTINUATION |
| AVAX-USD | 2021-06-11 → 2021-09-18 | 2021-09-20 | 2021-09-23 | FAILURE |
| ADA-USD | 2020-09-13 → 2020-12-21 | 2020-12-23 | 2020-12-28 | DIRECT_CONTINUATION |
| OP-USD | 2023-08-30 → 2023-12-07 | 2023-12-09 | 2023-12-21 | DIRECT_CONTINUATION |

##### B. Vintage originale 18 settembre — congelato

Questo invece **non cambia più**. Conserva gli 8 episodi / 6 asset della nostra analisi originale e serve per verificare fuori campione se quella specifica previsione descrive bene SOL.

Anchor della chat: circa **$112.70** il **2026-09-18**.

**SMALL SAMPLE · SENSITIVITY UNSTABLE · DIAGNOSTIC ONLY.**

![SOL conditional successor vintage](scanner_forecast_SOL_conditional_successor_vintage_20260918.png)

###### Percentili congelati a 30 giorni

| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Conditional vintage | 2026-09-18 | 8 | 2026-10-18 | 96.70 $ | 109.70 $ | 168.54 $ | 188.19 $ | 214.50 $ |

###### Verifica contro SOL reale

- Ultimo close disponibile: **2026-09-23** · SOL **119.03 $**.
- Giorno del vintage: **5/30**.
- P50 condizionato previsto per quel giorno: **110.28 $**.
- SOL reale: **FUORI p10-p90** · **FUORI p25-p75**.

###### Parità con l'analisi originale

| Giorno | Mediana return riprodotta |
| ---: | ---: |
| 7 | -11.51% |
| 14 | 8.85% |
| 21 | 36.80% |
| 30 | 49.55% |

###### Gli 8 episodi congelati

| Asset | Match window | -5% hit | +10% anchor |
| --- | --- | --- | --- |
| BNB-USD | 2023-10-13 → 2024-01-20 | 2024-01-23 | 2024-02-15 |
| HBAR-USD | 2020-11-04 → 2021-02-11 | 2021-02-14 | 2021-02-18 |
| RUNE-USD | 2020-03-28 → 2020-07-05 | 2020-07-06 | 2020-07-20 |
| ETH-USD | 2020-05-11 → 2020-08-18 | 2020-08-21 | 2020-09-01 |
| ADA-USD | 2020-09-08 → 2020-12-16 | 2020-12-21 | 2020-12-29 |
| BCH-USD | 2019-01-17 → 2019-04-26 | 2019-04-29 | 2019-05-03 |
| RUNE-USD | 2023-06-01 → 2023-09-08 | 2023-09-11 | 2023-09-15 |
| HBAR-USD | 2024-09-04 → 2024-12-12 | 2024-12-18 | 2024-12-24 |

**Come leggere la differenza:** il cono standard risponde a "cosa hanno fatto i 40 casi più simili?". Il Conditional Successor risponde a una domanda più stretta: "tra quei casi, cosa è successo dopo che avevano già completato -5% → +10%?". Per questo il secondo può risultare più rialzista ma anche molto più fragile statisticamente.

I due modelli **non vengono mediati**, non sostituiscono l'uno l'altro e non modificano Global Confluence, segnali o decisioni.

<!-- SOL_CONDITIONAL_ANALYSES_END -->


#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-08-24**; verificato fino al **2026-09-23**; stato **COMPLETO 30/30g**.
- Reale **119,03 $**; p50 previsto **95,58 $**; scarto **24,54%**.
- Errore medio assoluto **11,36%**; massimo **26,07%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-08-24**; verificato fino al **2026-09-23**; stato **COMPLETO 30/30g**.
- Reale **0.10233 $**; p50 previsto **0.09383 $**; scarto **9,06%**.
- Errore medio assoluto **9,52%**; massimo **15,85%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 68 | 92,65% | 67,65% | 2,07% | 0,59% |
| BTC | 3g | 65 | 92,31% | 73,85% | 3,29% | 0,97% |
| BTC | 7g | 60 | 91,67% | 68,33% | 5,04% | 2,24% |
| BTC | 14g | 46 | 97,83% | 71,74% | 5,56% | 3,47% |
| BTC | 30g | 23 | 100,00% | 91,30% | 8,90% | 3,16% |
| SOL | 1g | 68 | 80,88% | 60,29% | 2,85% | 1,12% |
| SOL | 3g | 65 | 90,77% | 70,77% | 4,23% | 1,92% |
| SOL | 7g | 60 | 90,00% | 71,67% | 5,82% | 3,89% |
| SOL | 14g | 46 | 84,78% | 71,74% | 8,16% | 7,14% |
| SOL | 30g | 23 | 91,30% | 47,83% | 15,48% | 14,92% |
| DOGE | 1g | 68 | 86,76% | 61,76% | 3,17% | 0,82% |
| DOGE | 3g | 65 | 90,77% | 64,62% | 4,86% | 1,85% |
| DOGE | 7g | 60 | 75,00% | 73,33% | 8,91% | 6,32% |
| DOGE | 14g | 46 | 84,78% | 54,35% | 10,40% | 8,57% |
| DOGE | 30g | 23 | 91,30% | 34,78% | 17,34% | 17,34% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |

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

Generato: 2026-09-23 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +75,00%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +52,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +72,50%       | Nessun lato sopra soglia estrema |                  40 |

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
- Casi positivi / salita storica: **75,00%**
- Casi negativi / discesa storica: **25,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **86.750,58 $**
- Return normale fra 30 giorni: **98.819,34 $** (13,91%)
- Drawdown normale durante il mese: **85.367,51 $** (-1,59%)
- Drawdown brutto da rispettare: **74.285,31 $** (-14,37%)
- Max gain normale durante il mese: **110.170,80 $** (27,00%)
- Max gain buono / take profit ottimistico: **130.713,58 $** (50,68%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **52,50%**
- Casi negativi / discesa storica: **47,50%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **118,95 $**
- Return normale fra 30 giorni: **121,80 $** (2,40%)
- Drawdown normale durante il mese: **103,84 $** (-12,70%)
- Drawdown brutto da rispettare: **86,81 $** (-27,02%)
- Max gain normale durante il mese: **140,91 $** (18,46%)
- Max gain buono / take profit ottimistico: **182,32 $** (53,28%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **27,50%**
- Casi negativi / discesa storica: **72,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,10 $**
- Return normale fra 30 giorni: **0,09 $** (-8,60%)
- Drawdown normale durante il mese: **0,08 $** (-20,36%)
- Drawdown brutto da rispettare: **0,07 $** (-28,45%)
- Max gain normale durante il mese: **0,11 $** (11,31%)
- Max gain buono / take profit ottimistico: **0,13 $** (26,39%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è misto. Alcuni asset possono avere lettura diversa, quindi è meglio valutare asset per asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 86.750,58 $

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

- Se va molto male: **69.196,10 $** (-20,24%)
- Se va male: **86.820,07 $** (0,08%)
- Scenario normale: **98.819,34 $** (13,91%)
- Se va bene: **110.155,39 $** (26,98%)
- Se va molto bene: **143.053,32 $** (64,90%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **85.367,51 $** (-1,59%)
- Discesa brutta: **74.285,31 $** (-14,37%)
- Discesa molto brutta: **62.298,96 $** (-28,19%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **110.170,80 $** (27,00%)
- Rialzo buono: **130.713,58 $** (50,68%)
- Rialzo molto forte: **169.443,38 $** (95,32%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **85.367,51 $** e uno spike normale intorno a **110.170,80 $**.

La chiusura a 30 giorni era più spesso positiva: salita 75,00%, discesa 25,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 118,95 $

**Direzione più probabile a 30 giorni:** **INCERTO**
- Probabilità storica di salita: **52,50%**
- Probabilità storica di discesa: **47,50%**
- Quanto è netto il segnale: **molto debole / quasi pari**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è incerta, con segnale molto debole / quasi pari. Nei casi storici simili non c'è stato un vantaggio chiaro né per salita né per discesa.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **87,30 $** (-26,61%)
- Se va male: **98,42 $** (-17,26%)
- Scenario normale: **121,80 $** (2,40%)
- Se va bene: **149,83 $** (25,96%)
- Se va molto bene: **200,60 $** (68,64%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **103,84 $** (-12,70%)
- Discesa brutta: **86,81 $** (-27,02%)
- Discesa molto brutta: **77,48 $** (-34,86%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **140,91 $** (18,46%)
- Rialzo buono: **182,32 $** (53,28%)
- Rialzo molto forte: **222,23 $** (86,83%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **103,84 $** e uno spike normale intorno a **140,91 $**.

La chiusura a 30 giorni è incerta: salita 52,50%, discesa 47,50%. Non c'è un vantaggio netto.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🔴 ROSSO / Prudenza
**Prezzo attuale:** 0,10 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **27,50%**
- Probabilità storica di discesa: **72,50%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,04 $** (-59,54%)
- Se va male: **0,08 $** (-18,15%)
- Scenario normale: **0,09 $** (-8,60%)
- Se va bene: **0,11 $** (3,32%)
- Se va molto bene: **0,14 $** (33,24%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,08 $** (-20,36%)
- Discesa brutta: **0,07 $** (-28,45%)
- Discesa molto brutta: **0,04 $** (-62,08%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,11 $** (11,31%)
- Rialzo buono: **0,13 $** (26,39%)
- Rialzo molto forte: **0,16 $** (58,27%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,08 $** e uno spike normale intorno a **0,11 $**.

La chiusura a 30 giorni era più spesso negativa: salita 27,50%, discesa 72,50%. Quindi la lettura principale è prudente/debole.

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

- Previsioni già controllate: **30**
- Direzione corretta: **86,96%**
- Errore medio dello scenario centrale: **7,19%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **3,33%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **30**
- Direzione corretta: **92,59%**
- Errore medio dello scenario centrale: **15,19%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **33,33%**
- Prezzo finale dentro lo scenario 10%-90%: **93,33%**

### Solana

- Previsioni già controllate: **30**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **12,32%**
- Zona rischio toccata: **6,67%**
- Zona rialzo media toccata: **36,67%**
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

- Previsioni controllate: **30**
- Previsioni usate per la calibrazione recente: **30**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **86,96%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **13,91%** → **98.819,34 $**
- Correzione imparata dagli errori: **2,01%**
- Calibrato: **15,92%** → **100.561,22 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-1,59%** → **85.367,51 $**
- Correzione imparata dagli errori: **4,72%**
- Calibrato: **3,13%** → **89.465,01 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **27,00%** → **110.170,80 $**
- Correzione imparata dagli errori: **-2,82%**
- Calibrato: **24,17%** → **107.720,16 $**
- Lettura: Lo scanner ha sovrastimato gli spike: nella realtà il prezzo è salito meno del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Solana

- Previsioni controllate: **30**
- Previsioni usate per la calibrazione recente: **30**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **100,00%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **INCERTO**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **2,40%** → **121,80 $**
- Correzione imparata dagli errori: **8,80%**
- Calibrato: **11,20%** → **132,27 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-12,70%** → **103,84 $**
- Correzione imparata dagli errori: **2,99%**
- Calibrato: **-9,71%** → **107,40 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **18,46%** → **140,91 $**
- Correzione imparata dagli errori: **4,02%**
- Calibrato: **22,48%** → **145,69 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Dogecoin

- Previsioni controllate: **30**
- Previsioni usate per la calibrazione recente: **30**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **92,59%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **DISCESA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **-8,60%** → **0,09 $**
- Correzione imparata dagli errori: **15,19%**
- Calibrato: **6,58%** → **0,11 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-20,36%** → **0,08 $**
- Correzione imparata dagli errori: **15,34%**
- Calibrato: **-5,02%** → **0,10 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **11,31%** → **0,11 $**
- Correzione imparata dagli errori: **2,52%**
- Calibrato: **13,84%** → **0,12 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 86.750,58 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **75,00%**
- Casi negativi dopo 30 giorni: **25,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,63%**
- Rendimento medio dopo 30 giorni: **17,76%**
- Rendimento centrale dopo 30 giorni: **13,91%**
- Discesa media durante i 30 giorni: **-9,46%**
- Massimo rialzo medio durante i 30 giorni: **39,49%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **102.158,55 $**
- Scenario centrale a 30 giorni: **98.819,34 $**
- Zona di rischio media: **78.545,69 $**
- Zona di rialzo media: **121.006,32 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -20,24% → **69.196,10 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 0,08% → **86.820,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 13,91% → **98.819,34 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 26,98% → **110.155,39 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 64,90% → **143.053,32 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -28,19% → **62.298,96 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -14,37% → **74.285,31 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -1,59% → **85.367,51 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **86.750,58 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **86.750,58 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,73% → **88.252,53 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 10,51% → **95.864,34 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 27,00% → **110.170,80 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 50,68% → **130.713,58 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 95,32% → **169.443,38 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| RUNE-USD        | 2023-06-06   | 2023-09-13 |        90.38 |         3.73 |           0    |          31.23 |
| BTC-USD         | 2022-11-10   | 2023-02-17 |        90.34 |        14.14 |         -17.82 |          14.14 |
| DASH-USD        | 2020-09-13   | 2020-12-21 |        88.78 |        16.13 |         -16.67 |          42.17 |
| QTUM-USD        | 2023-08-19   | 2023-11-26 |        88.7  |         4.6  |          -5.87 |           8.14 |
| THETA-USD       | 2023-08-28   | 2023-12-05 |        88.69 |         9.3  |          -8.21 |          27.74 |
| INJ-USD         | 2023-08-21   | 2023-11-28 |        88.63 |       114.93 |           0    |         161.2  |
| ALGO-USD        | 2023-08-28   | 2023-12-05 |        88.2  |        35.21 |          -0.54 |          56.22 |
| ATOM-USD        | 2020-05-01   | 2020-08-08 |        88.02 |        14.06 |           0    |          92.34 |
| AVAX-USD        | 2021-06-11   | 2021-09-18 |        87.55 |       -19.62 |         -21.23 |          10.73 |
| ADA-USD         | 2023-08-29   | 2023-12-06 |        87.44 |        22.34 |           0    |          50.37 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 118,95 $

Solana è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **52,50%**
- Casi negativi dopo 30 giorni: **47,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,61%**
- Rendimento medio dopo 30 giorni: **13,04%**
- Rendimento centrale dopo 30 giorni: **2,40%**
- Discesa media durante i 30 giorni: **-15,76%**
- Massimo rialzo medio durante i 30 giorni: **37,19%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **134,46 $**
- Scenario centrale a 30 giorni: **121,80 $**
- Zona di rischio media: **100,21 $**
- Zona di rialzo media: **163,19 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -26,61% → **87,30 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -17,26% → **98,42 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 2,40% → **121,80 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 25,96% → **149,83 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 68,64% → **200,60 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -34,86% → **77,48 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -27,02% → **86,81 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -12,70% → **103,84 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **118,95 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **118,95 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **118,95 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 1,63% → **120,89 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 18,46% → **140,91 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 53,28% → **182,32 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 86,83% → **222,23 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| CRV-USD         | 2022-11-11   | 2023-02-18 |        88.26 |       -23.26 |         -33.1  |           0.85 |
| THETA-USD       | 2023-08-28   | 2023-12-05 |        87.99 |         9.3  |          -8.21 |          27.74 |
| ATOM-USD        | 2023-08-29   | 2023-12-06 |        87.82 |         5.85 |           0    |          23.72 |
| AAVE-USD        | 2022-11-10   | 2023-02-17 |        87.46 |        -7.99 |         -22.1  |           6.22 |
| ALGO-USD        | 2023-08-28   | 2023-12-05 |        87.01 |        35.21 |          -0.54 |          56.22 |
| HBAR-USD        | 2022-11-09   | 2023-02-16 |        86.91 |       -25.52 |         -31.4  |           4.31 |
| VET-USD         | 2023-08-26   | 2023-12-03 |        86.91 |        54.44 |           0    |          68.55 |
| RUNE-USD        | 2023-06-06   | 2023-09-13 |        86.9  |         3.73 |           0    |          31.23 |
| BTC-USD         | 2022-11-10   | 2023-02-17 |        86.51 |        14.14 |         -17.82 |          14.14 |
| NEO-USD         | 2020-11-02   | 2021-02-09 |        86.46 |        34.78 |           0    |          76.16 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🔴 ROSSO / Prudenza

**Prezzo attuale:** 0,10 $

Dogecoin richiede prudenza. La statistica dei casi simili indica più possibilità di discesa che di salita. Con leva, il rischio principale è il drawdown durante il percorso.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **27,50%**
- Casi negativi dopo 30 giorni: **72,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **80,24%**
- Rendimento medio dopo 30 giorni: **-2,17%**
- Rendimento centrale dopo 30 giorni: **-8,60%**
- Discesa media durante i 30 giorni: **-26,04%**
- Massimo rialzo medio durante i 30 giorni: **26,86%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,10 $**
- Scenario centrale a 30 giorni: **0,09 $**
- Zona di rischio media: **0,08 $**
- Zona di rialzo media: **0,13 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -59,54% → **0,04 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -18,15% → **0,08 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -8,60% → **0,09 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 3,32% → **0,11 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 33,24% → **0,14 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -62,08% → **0,04 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -28,45% → **0,07 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -20,36% → **0,08 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -12,25% → **0,09 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -5,50% → **0,10 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,86% → **0,10 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 3,75% → **0,11 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 11,31% → **0,11 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 26,39% → **0,13 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 58,27% → **0,16 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| DASH-USD        | 2019-11-08   | 2020-02-15 |        86.42 |       -64.76 |         -64.76 |           0    |
| MANA-USD        | 2022-11-07   | 2023-02-14 |        84.86 |       -14.97 |         -23.45 |           9.86 |
| RUNE-USD        | 2020-09-09   | 2020-12-17 |        83.58 |        97.38 |         -12.58 |          97.38 |
| NEAR-USD        | 2022-11-07   | 2023-02-14 |        82.92 |       -12.29 |         -20.34 |          20.09 |
| FIL-USD         | 2020-12-06   | 2021-03-15 |        82.33 |       213.76 |           0    |         256.97 |
| EOS-USD         | 2019-11-08   | 2020-02-15 |        82.31 |       -60.27 |         -61.04 |           0    |
| BCH-USD         | 2019-11-08   | 2020-02-15 |        82.15 |       -60.99 |         -65.22 |           0    |
| KAVA-USD        | 2022-01-16   | 2022-04-25 |        82.01 |       -49.55 |         -68.95 |           4.4  |
| QTUM-USD        | 2021-05-31   | 2021-09-07 |        81.12 |         3.03 |         -30.65 |          11.89 |
| ENJ-USD         | 2022-11-07   | 2023-02-14 |        81.07 |       -11.58 |         -20.08 |          23.17 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-09-23 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-23 | RECOVERY | 86.751 $ | True | 45.26% | -2.19% | RECOVERY | 45.26% | -2.19% |
| DOGE-USD | 2026-09-23 | RECOVERY | 0.10210 $ | True | 36.52% | -9.59% | RECOVERY | 45.26% | -2.19% |
| SOL-USD | 2026-09-23 | RECOVERY | 118,95 $ | True | 76.03% | -4.82% | RECOVERY | 45.26% | -2.19% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 75.00% | 13.91% | 26.98% | 64.90% | -1.59% | -28.19% | 27.00% | 50.68% | 95.32% | 65.00% | 9.28% | 32.28% | 118.00% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 16.13% | 16.13% | 16.13% | -16.67% | -16.67% | 42.17% | 42.17% | 42.17% | 100.00% | 211.64% | 211.64% | 211.64% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 27.50% | -8.60% | 3.32% | 33.24% | -20.36% | -62.08% | 11.31% | 26.39% | 58.27% | 60.00% | 3.10% | 18.77% | 63.06% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 50.00% | 19.03% | 37.37% | 48.38% | -9.41% | -16.93% | 31.22% | 43.47% | 50.82% | 50.00% | -2.20% | 5.28% | 9.76% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 52.50% | 2.40% | 25.96% | 68.64% | -12.70% | -34.86% | 18.46% | 53.28% | 86.83% | 47.50% | -0.46% | 29.65% | 141.43% |
| SOL-USD | SAME_BTC_REGIME | 1 | 100.00% | 48.11% | 48.11% | 48.11% | -6.40% | -6.40% | 82.91% | 82.91% | 82.91% | 100.00% | 41.79% | 41.79% | 41.79% |
| SOL-USD | SAME_ASSET_REGIME | 2 | 50.00% | 4.10% | 26.10% | 39.31% | -28.52% | -46.21% | 41.45% | 62.18% | 74.62% | 50.00% | -7.58% | 17.10% | 31.92% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 48.11% | 48.11% | 48.11% | -6.40% | -6.40% | 82.91% | 82.91% | 82.91% | 100.00% | 41.79% | 41.79% | 41.79% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 25 | 72.00% | 13.78% | -1.45% | 45.75% | 56.00% | 1.26% | 56.21% |
| BTC-USD | HISTORICAL_BTC_BULL | 14 | 78.57% | 11.41% | -2.37% | 50.52% | 78.57% | 11.02% | 182.87% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 14.06% | 0.00% | 92.34% | 100.00% | 10.26% | 92.34% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 29 | 17.24% | -14.25% | -21.73% | 21.83% | 51.72% | 0.60% | 30.70% |
| DOGE-USD | HISTORICAL_BTC_BULL | 8 | 62.50% | 23.72% | -7.87% | 67.94% | 87.50% | 32.42% | 210.96% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 33.33% | -2.17% | -25.24% | 6.80% | 66.67% | 0.79% | 31.70% |
| SOL-USD | HISTORICAL_BTC_BEAR | 20 | 40.00% | -8.84% | -19.67% | 32.26% | 35.00% | -6.13% | 52.50% |
| SOL-USD | HISTORICAL_BTC_BULL | 17 | 70.59% | 7.79% | -2.25% | 55.83% | 64.71% | 10.15% | 157.53% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -9.40% | -18.64% | 0.68% | 0.00% | -27.51% | 0.68% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 1 | 100.00% | 48.11% | -6.40% | 82.91% | 100.00% | 41.79% | 82.91% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 32 | 75.00% | 11.54% | -1.17% | 50.42% | 62.50% | 7.67% | 53.58% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 80.00% | 78.30% | -10.65% | 148.83% | 80.00% | 111.45% | 280.80% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -17.13% | -27.45% | 1.89% | 0.00% | -14.77% | 1.89% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 26.20% | -15.55% | 47.22% | 100.00% | 96.56% | 96.56% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 16.13% | -16.67% | 42.17% | 100.00% | 211.64% | 211.64% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 25 | 16.00% | -12.29% | -20.47% | 21.83% | 52.00% | 0.60% | 24.95% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 10 | 60.00% | 13.63% | -17.27% | 59.21% | 90.00% | 26.58% | 161.61% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -29.45% | -32.80% | 16.93% | 50.00% | 7.47% | 36.18% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -49.55% | -68.95% | 4.40% | 0.00% | -65.63% | 4.40% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | 19.03% | -9.41% | 43.47% | 50.00% | -2.20% | 43.47% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 50.00% | 0.30% | -14.50% | 36.86% | 40.00% | -3.10% | 51.09% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 21.28% | -8.10% | 94.33% | 100.00% | 54.32% | 205.19% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | 5.44% | -14.01% | 60.62% | 50.00% | 20.95% | 147.79% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | 4.10% | -28.52% | 62.18% | 50.00% | -7.58% | 62.18% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|
| BTC-USD | NONE | 0 | 1 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | NONE | 1 | 2 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

_No data._

## Interpretation rules

- ALL_MATCHES is the raw view. It can mix bull, bear, recovery and distribution phases.
- SAME_BTC_REGIME is cleaner because BTC had a similar macro background.
- SAME_ASSET_REGIME is cleaner because the matched altcoin had a similar local trend.
- SAME_BTC_AND_ASSET_REGIME is the preferred and most stringent filter.
- Below 5 full-regime matches, the selector falls back first to SAME_ASSET_REGIME and then to SAME_BTC_REGIME.
- A fallback is always labelled as less stringent; groups are never combined.
- If every group is below threshold, the result is INSUFFICIENT_REGIME_MATCHES.
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

Generato: 2026-09-23 05:32 UTC


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
| BTC | 86.751 $ | +7 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI DECRESCENTI | SIGN OF STRENGTH POSSIBILE | BASSO | SPOT OK / LONG SOLO PRUDENTE SU CONFERMA |
| SOL | 118,95 $ | +9 | CONFERMATO RIALZISTA | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI DECRESCENTI | SIGN OF STRENGTH POSSIBILE | BASSO | TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME |
| DOGE | 0.10210 $ | +9 | CONFERMATO RIALZISTA | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI DECRESCENTI | SIGN OF STRENGTH POSSIBILE | MEDIO | SOLO TRADING VELOCE / NO LEVA AGGRESSIVA |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | -2 | +2 | +1 | +3 | 0 | +2 | +7 |
| SOL | +2 | -2 | +2 | +2 | +3 | 0 | +2 | +9 |
| DOGE | +1 | -2 | +2 | +3 | +3 | 0 | +2 | +9 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.206 $ | 87.364 $ | 82.262 $ | 62.227 $ | 2,74% | 11,55% | 42,20% |
| SOL | 98,63 $ | 119,81 $ | 114,06 $ | 70,69 $ | 4,06% | 24,64% | 74,99% |
| DOGE | 0.09818 $ | 0.10653 $ | 0.09998 $ | 0.06797 $ | 4,56% | 9,50% | 34,57% |

## Lettura dettagliata

### BTC

- Prezzo: **86.751 $**
- Score classico: **+7 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **SPOT OK / LONG SOLO PRUDENTE SU CONFERMA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,74%; distanza supporto 9,50%; distanza resistenza 0,73%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+2** — RSI alto 74.0; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+1** — OBV sopra media; CMF neutrale 0.05; volume ratio 1.30
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 74.04 |
| MACD histogram | 636.19571 |
| CMF20 | 0.050 |
| Volume ratio 20 | 1.30 |
| MA20 | 79.386 $ |
| MA50 | 74.137 $ |
| MA100 | 68.721 $ |
| MA200 | 70.676 $ |
| Pendenza MA50 20g | +8,82% |
| Pendenza MA200 60g | -2,39% |
| Bollinger width | 14,22% |
| Bollinger position | 1.10 |

### SOL

- Prezzo: **118,95 $**
- Score classico: **+9 / 12**
- Verdetto: **CONFERMATO RIALZISTA**
- Azione coerente: **TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME**
- Volatilità tecnica locale: **BASSO** — ATR14 4,06%; distanza supporto 20,62%; distanza resistenza 0,71%

Dettaglio:

- Trend: **+2** — prezzo sopra MA200 daily; medie daily allineate rialziste; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+2** — RSI alto 70.2; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.17; volume ratio 1.24
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 70.24 |
| MACD histogram | 1.23279 |
| CMF20 | 0.170 |
| Volume ratio 20 | 1.24 |
| MA20 | 104,93 $ |
| MA50 | 94,08 $ |
| MA100 | 84,55 $ |
| MA200 | 84,09 $ |
| Pendenza MA50 20g | +14,54% |
| Pendenza MA200 60g | -5,18% |
| Bollinger width | 21,28% |
| Bollinger position | 1.05 |

### DOGE

- Prezzo: **0.10210 $**
- Score classico: **+9 / 12**
- Verdetto: **CONFERMATO RIALZISTA**
- Azione coerente: **SOLO TRADING VELOCE / NO LEVA AGGRESSIVA**
- Volatilità tecnica locale: **MEDIO** — ATR14 4,56%; distanza supporto 4,19%; distanza resistenza 4,14%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+2** — RSI alto 72.6; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+3** — OBV sopra media; CMF positivo 0.10; rialzo con volume sopra media
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 72.56 |
| MACD histogram | 0.00146 |
| CMF20 | 0.102 |
| Volume ratio 20 | 1.92 |
| MA20 | 0.08725 $ |
| MA50 | 0.08155 $ |
| MA100 | 0.07820 $ |
| MA200 | 0.08779 $ |
| Pendenza MA50 20g | +8,46% |
| Pendenza MA200 60g | -9,95% |
| Bollinger width | 22,29% |
| Bollinger position | 1.16 |

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

Generato: 2026-09-23 05:32 UTC


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
| BTC | 86.751 $ | Doppio minimo | ATTIVO | rialzista | 2026-09-21 | 89.580 $ | 61,34% | n/a | Fib 78,6% RECUPERATO (+1) @ 80.696 $ | BREAKOUT 60G | 76.248 $ |
| SOL | 118,95 $ | Triplo massimo | CANDIDATO | ribassista | n/a | 62,51 $ | n/a | 68,26% | Fib 78,6% RECUPERATO (+1) @ 107,08 $ | BREAKOUT 60G | 97,45 $ |
| DOGE | 0.10210 $ | Doppio minimo | ATTIVO | rialzista | 2026-09-21 | 0.11001 $ | 49,93% | n/a | Fib 78,6% RECUPERATO (+1) @ 0.09536 $ | BREAKOUT 60G | 0.09818 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **ATTIVO** (+1)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-09-15**
- Età formazione: **8 giorni**
- Breakout pattern: **2026-09-21**
- Età breakout: **2 giorni**
- Neckline: **82.262 $**
- Target teorico: **89.580 $**
- Progresso verso target: **61,34%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% RECUPERATO (+1) @ 80.696 $** — Swing DOWN 2026-09-03 82.262 -> 2026-09-15 74.945; livello più vicino 78.6% a 80.696; stato RECUPERATO; confluenza: resistenza tecnica, neckline rialzista, invalidazione rialzista.
- Invalidazione: **80.617 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due minimi simili vicino a 74.945 tra 2026-09-02 e 2026-09-15. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (2 giorni fa). Stato: ATTIVO. Target teorico: 89.580; progresso corrente: 61,34%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **76.248 $**
- Resistenza: **87.364 $**
- Breakout 60g: **82.262 $**
- Breakdown 60g: **62.227 $**
- RSI14: **74.06**
- ATR14: **2,74%**
- Volume ratio 20g: **1.30**
- Rendimento 30g: **+11,57%**
- Rendimento 90g: **+42,23%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | ATTIVO | +1 | rialzista | 82.262 $ | 2026-09-21 | 2g | 89.580 $ | 61,34% | n/a | 80.617 $ | Due minimi simili a 76.248 $ e 74.945 $. Neckline circa 82.262 $. Breakout neckline: 2026-09-21 (2 giorni fa). Stato: ATTIVO. Target teorico: 89.580 $; progresso: 61,34%; prezzo sopra neckline. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 39,41% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 45 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **45 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **70,69 $**
- Target teorico: **62,51 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **68,26%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% RECUPERATO (+1) @ 107,08 $** — Swing DOWN 2026-08-27 110,04 -> 2026-09-16 96,23; livello più vicino 78.6% a 107,08; stato RECUPERATO; confluenza: resistenza tecnica, neckline rialzista, invalidazione rialzista.
- Invalidazione: **72,11 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 45 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **97,45 $**
- Resistenza: **119,81 $**
- Breakout 60g: **114,06 $**
- Breakdown 60g: **70,69 $**
- RSI14: **70.24**
- ATR14: **4,06%**
- Volume ratio 20g: **1.24**
- Rendimento 30g: **+24,63%**
- Rendimento 90g: **+74,97%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,51 $ | n/a | 68,26% | 72,11 $ | Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 45 giorni. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 68,26% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 45 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 107,12 $ | 2026-09-18 | 5g | 118,01 $ | 108,66% | n/a | 104,97 $ | Due minimi simili a 97,45 $ e 96,23 $. Neckline circa 107,12 $. Breakout neckline: 2026-09-18 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01 $; progresso: 108,66%; prezzo sopra neckline. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 35g | 85,65 $ | 545,37% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (35 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 545,37%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **ATTIVO** (+1)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-09-16**
- Età formazione: **7 giorni**
- Breakout pattern: **2026-09-21**
- Età breakout: **2 giorni**
- Neckline: **0.09421 $**
- Target teorico: **0.11001 $**
- Progresso verso target: **49,93%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% RECUPERATO (+1) @ 0.09536 $** — Swing DOWN 2026-08-22 0.09998 -> 2026-09-16 0.07841; livello più vicino 78.6% a 0.09536; stato RECUPERATO; confluenza: neckline rialzista, invalidazione rialzista.
- Invalidazione: **0.09232 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due minimi simili vicino a 0.07841 tra 2026-09-02 e 2026-09-16. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (2 giorni fa). Stato: ATTIVO. Target teorico: 0.11001; progresso corrente: 49,93%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **0.09818 $**
- Resistenza: **0.10402 $**
- Breakout 60g: **0.09998 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **72.43**
- ATR14: **4,57%**
- Volume ratio 20g: **1.92**
- Rendimento 30g: **+9,29%**
- Rendimento 90g: **+34,32%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | ATTIVO | +1 | rialzista | 0.09421 $ | 2026-09-21 | 2g | 0.11001 $ | 49,93% | n/a | 0.09232 $ | Due minimi simili a 0.08028 $ e 0.07841 $. Neckline circa 0.09421 $. Breakout neckline: 2026-09-21 (2 giorni fa). Stato: ATTIVO. Target teorico: 0.11001 $; progresso: 49,93%; prezzo sopra neckline. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.04174 $ | n/a | 50,21% | 0.06933 $ | Due massimi simili a 0.09169 $ e 0.09421 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 18 giorni. |

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

Generato: 2026-09-23 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-23**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-10**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **118,95 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+68,63%**
- Aderenza live principale: **+69,67%**
- Errore medio live principale: **15,17%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **109**
- Osservazioni inclusive dal bottom: **110**
- Osservazioni da inizio programma/scanner: **83**
- Errore assoluto medio dal bottom: **12,92%**
- Errore assoluto medio da inizio programma: **15,17%**
- Gap firmato medio ultimi 7 giorni: **+33,12%**
- Errore assoluto medio ultimi 7 giorni: **33,12%**
- Gap ultimo giorno: **+49,58%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+49,58%**
- Gap firmato medio 7g: **+33,12%**
- Errore assoluto medio 7g: **33,12%**
- Variazione recente gap: **+22,61%**
- Stato gap: **DISALLINEATO SOPRA IL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 100 | 2026-09-14 | 2023-03-01 | 102,50 $ | 93,15 $ | +10,03% | da inizio programma |
| 101 | 2026-09-15 | 2023-03-02 | 96,89 $ | 92,48 $ | +4,77% | da inizio programma |
| 102 | 2026-09-16 | 2023-03-03 | 98,64 $ | 88,09 $ | +11,98% | da inizio programma |
| 103 | 2026-09-17 | 2023-03-04 | 101,60 $ | 88,06 $ | +15,39% | da inizio programma |
| 104 | 2026-09-18 | 2023-03-05 | 112,60 $ | 88,38 $ | +27,41% | da inizio programma |
| 105 | 2026-09-19 | 2023-03-06 | 111,01 $ | 88,36 $ | +25,64% | da inizio programma |
| 106 | 2026-09-20 | 2023-03-07 | 111,13 $ | 87,53 $ | +26,97% | da inizio programma |
| 107 | 2026-09-21 | 2023-03-08 | 118,75 $ | 85,55 $ | +38,80% | da inizio programma |
| 108 | 2026-09-22 | 2023-03-09 | 118,75 $ | 80,21 $ | +48,04% | da inizio programma |
| 109 | 2026-09-23 | 2023-03-10 | 118,95 $ | 79,52 $ | +49,58% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-30 | 108,03 $ | 161,59 $ | 118,95 $ / 161,59 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-07 | 108,30 $ | 162,00 $ | 118,95 $ / 166,95 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-14 | 112,18 $ | 167,80 $ | 118,95 $ / 167,80 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-21 | 110,01 $ | 164,55 $ | 118,95 $ / 167,80 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-28 | 120,09 $ | 179,63 $ | 118,95 $ / 179,63 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-04 | 107,45 $ | 160,72 $ | 118,95 $ / 179,63 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-11 | 115,58 $ | 172,88 $ | 118,95 $ / 179,63 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-18 | 116,34 $ | 174,03 $ | 118,95 $ / 179,63 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-25 | 105,59 $ | 157,94 $ | 118,95 $ / 179,63 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-02 | 105,93 $ | 158,45 $ | 118,95 $ / 179,63 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-09 | 105,25 $ | 157,44 $ | 118,95 $ / 179,63 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-16 | 107,34 $ | 160,56 $ | 118,95 $ / 179,63 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-23 | 104,31 $ | 156,03 $ | 118,95 $ / 179,63 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-30 | 103,71 $ | 155,13 $ | 118,95 $ / 179,63 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-06 | 120,92 $ | 180,87 $ | 118,95 $ / 180,87 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-13 | 120,06 $ | 179,58 $ | 118,95 $ / 180,87 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-20 | 119,53 $ | 178,79 $ | 118,95 $ / 183,58 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-27 | 119,49 $ | 178,74 $ | 118,95 $ / 185,47 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 69 | 36,23% | 11,22% | 14,57% |
| 14g | 62 | 24,19% | 17,50% | 13,86% |
| 21g | 55 | 23,64% | 23,86% | 15,36% |
| 28g | 48 | 22,92% | 26,76% | 15,46% |
| 35g | 41 | 31,71% | 26,43% | 15,11% |
| 42g | 35 | 57,14% | 19,64% | 14,10% |
| 49g | 29 | 68,97% | 17,01% | 16,09% |
| 56g | 22 | 72,73% | 12,80% | 17,40% |
| 63g | 15 | 73,33% | 10,95% | 22,12% |
| 70g | 8 | 62,50% | 12,65% | 36,07% |
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

Generato: 2026-09-23 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 86.922 $ | 3 | +1 | 0 | POSITIVA / CANDIDATA, ANCORA NON PESATA | ALTA | 93% | +0,0018% | +4,23% | 38,81 | -0,65% | 0 $ | 0 $ |
| SOL | 119,17 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0013% | +2,24% | 0,86 | -1,74% | 0 $ | 0 $ |
| DOGE | 0.10292 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0059% | +1,51% | 1,09 | +0,83% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0071% | 199,31 mln $ | n/a | +4,80% |
| BTC | Bitget | OK | +0,0012% | 3,01 mld $ | 3,48 | -30,27% |
| BTC | Kucoin | OK | +0,0012% | 1,02 mld $ | 1,83 | -9,80% |
| SOL | Kraken | OK | +0,0084% | 33,54 mln $ | 0,07 | +4,69% |
| SOL | Bitget | OK | +0,0031% | 481,10 mln $ | 2,02 | -59,34% |
| SOL | Kucoin | OK | +0,0082% | 136,71 mln $ | 0,82 | -1,43% |
| DOGE | Kraken | OK | +0,0023% | 5,52 mln $ | 0,55 | +5,78% |
| DOGE | Bitget | OK | +0,0100% | 135,40 mln $ | 3,61 | -46,30% |
| DOGE | Kucoin | OK | +0,0100% | 64,64 mln $ | 0,41 | -4,69% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+3,50**; candidato: **+1**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +40,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+1,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci recuperato con acquisti/assorbimento coerenti: conferma positiva. Confluenza tecnica dichiarata: resistenza tecnica, neckline rialzista, invalidazione rialzista.
- **RSI:** RSI alto ma sostenuto da acquisti e leva non estrema: momentum ancora credibile.
- **Pattern:** Doppio minimo attivo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+0,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 0.
- Flusso taker/order book: **-0,25**.
- OI/funding/basis: **+1,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci recuperato; nessuna conferma exchange netta. Confluenza tecnica dichiarata: resistenza tecnica, neckline rialzista, invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+2,50**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 9, accuratezza +44,44%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci recuperato con acquisti/assorbimento coerenti: conferma positiva. Confluenza tecnica dichiarata: neckline rialzista, invalidazione rialzista.
- **RSI:** RSI alto ma sostenuto da acquisti e leva non estrema: momentum ancora credibile.
- **Pattern:** Doppio minimo attivo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +75,00% | +13,91% | 2 | +50,00% | RACCOLTA DATI | 0,00 | +75,00% | +13,91% |
| SOL | +52,50% | +2,40% | 3 | +100,00% | RACCOLTA DATI | 0,00 | +52,50% | +2,40% |
| DOGE | +27,50% | -8,60% | 7 | +71,43% | RACCOLTA DATI | 0,00 | +27,50% | -8,60% |

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

Generato: 2026-09-23 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-23 | BTC | 86.922,40 | V2.1.3 | OK | 1 | 0 | 3,50 | ALTA | 38,81 | +4,23% | -0,65% |
| 2026-09-23 | DOGE | 0.10292 | V2.1.3 | OK | 0 | 0 | 2,50 | MEDIA | 1,09 | +1,51% | +0,83% |
| 2026-09-23 | SOL | 119,17 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,86 | +2,24% | -1,74% |
| 2026-09-22 | BTC | 85.448,20 | V2.1.3 | OK | 1 | 0 | 3,25 | ALTA | 3,84 | +9,38% | -2,93% |
| 2026-09-22 | DOGE | 0.10000 | V2.1.3 | OK | 1 | 0 | 3,50 | MEDIA | 1,33 | +7,63% | +6,45% |
| 2026-09-22 | SOL | 116,52 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 2,53 | +1,94% | +0,44% |
| 2026-09-17 | BTC | 76.462,50 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,37 | +0,81% | +0,39% |
| 2026-09-17 | DOGE | 0.08097 | V2.1.3 | OK | 1 | 0 | 2,62 | MEDIA | 1,51 | -1,67% | +9,25% |
| 2026-09-17 | SOL | 99,73 | V2.1.3 | OK | 0 | 0 | 2,25 | BASSA | 1,78 | +1,38% | +9,50% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 6 | +50,00% | +0,03% | -0,60% | +0,85% | FEEDBACK RAPIDO |
| BTC | 3g | 5 | +40,00% | +0,25% | -2,11% | +2,12% | FEEDBACK RAPIDO |
| BTC | 7g | 5 | +40,00% | -1,30% | -3,40% | +2,47% | FEEDBACK RAPIDO |
| BTC | 14g | 5 | +40,00% | +0,20% | -4,71% | +3,32% | FEEDBACK RAPIDO |
| BTC | 30g | 2 | +50,00% | +5,45% | -2,78% | +8,46% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 3 | +100,00% | +22,94% | -4,64% | +27,31% | FEEDBACK RAPIDO |
| DOGE | 1g | 11 | +54,55% | +1,55% | -0,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 3g | 10 | +40,00% | +1,88% | -2,95% | +6,44% | FEEDBACK RAPIDO |
| DOGE | 7g | 9 | +44,44% | -1,43% | -4,92% | +7,35% | FEEDBACK RAPIDO |
| DOGE | 14g | 9 | +33,33% | +0,11% | -6,27% | +13,00% | FEEDBACK RAPIDO |
| DOGE | 30g | 7 | +71,43% | +12,59% | -5,89% | +31,59% | FEEDBACK RAPIDO |

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

**BTC** — BTC: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**SOL** — SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**DOGE** — DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 86.751 $ | +0.0020% | -12.36% | 1.10 | Misto | 1/5 |
| SOL | 118,95 $ | +0.0035% | -23.90% | 1.99 | Misto | 1/5 |
| DOGE | 0.10210 $ | +0.0100% | -11.50% | 3.13 | Rischio sotto | 2/5 |

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

Generato: 2026-09-23 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily              | Stato D   | Weekly             | Stato W    | Lettura weekly                                                                                                              |   Peso |
|:--------|:-------------------|:----------|:-------------------|:-----------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Conferma rialzista | CONTESTO  | Conferma rialzista | CONTESTO   | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| SOL     | Conferma rialzista | CONTESTO  | Conferma rialzista | CONTESTO   | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| DOGE    | Conferma rialzista | CONTESTO  | Hidden bearish     | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo               | Stato      | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:-------------------|:-----------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Conferma rialzista | CONTESTO   | 86.709 $ / 74,00  | n/a                                                                 | +10,54%             | 13,92            |      0 |
| BTC     | 1W   | Conferma rialzista | CONTESTO   | 86.709 $ / 63,27  | n/a                                                                 | +38,03%             | 24,47            |      0 |
| SOL     | 1D   | Conferma rialzista | CONTESTO   | 118,91 $ / 70,21  | n/a                                                                 | +15,08%             | 8,16             |      0 |
| SOL     | 1W   | Conferma rialzista | CONTESTO   | 118,91 $ / 64,30  | n/a                                                                 | +59,53%             | 24,58            |      0 |
| DOGE    | 1D   | Conferma rialzista | CONTESTO   | 0.10221 $ / 72,51 | n/a                                                                 | +13,57%             | 10,50            |      0 |
| DOGE    | 1W   | Hidden bearish     | CONFERMATA | 0.10221 $ / 54,85 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 49,72 | n/a                 | n/a              |      0 |

### BTC

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### SOL

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### DOGE

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **9**.
- Soglie di lettura: **30 / 60 / 100 controlli**.
- Anche oltre le soglie il peso resta **0** finché non viene presa una decisione esplicita.

| Asset   | TF   | Tipo             |   Orizzonte |   Controlli | Accuratezza   | Return corretto   | Stato         |   Peso |
|:--------|:-----|:-----------------|------------:|------------:|:--------------|:------------------|:--------------|-------:|
| BTC     | 1D   | Bullish regolare |          30 |           1 | 0,00%         | -1,52%            | RACCOLTA DATI |      0 |
| BTC     | 1D   | Bullish regolare |          60 |           1 | +100,00%      | +21,03%           | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bearish   |          30 |           1 | 0,00%         | -1,37%            | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bearish   |          60 |           1 | 0,00%         | -23,44%           | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bullish   |          30 |           1 | +100,00%      | +25,83%           | RACCOLTA DATI |      0 |
| BTC     | 1W   | Bullish regolare |          30 |           1 | +100,00%      | +1,03%            | RACCOLTA DATI |      0 |
| BTC     | 1W   | Bullish regolare |          60 |           1 | +100,00%      | +22,85%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Bullish regolare |          30 |           1 | +100,00%      | +22,35%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          30 |           2 | +50,00%       | -8,18%            | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          60 |           1 | 0,00%         | -16,95%           | RACCOLTA DATI |      0 |
| SOL     | 1W   | Hidden bearish   |          30 |           1 | +100,00%      | +1,11%            | RACCOLTA DATI |      0 |
| SOL     | 1W   | Hidden bearish   |          60 |           1 | 0,00%         | -30,59%           | RACCOLTA DATI |      0 |

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

Generato: 2026-09-23 05:32 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto          | Trend           | Momentum                  | Struttura                                             |   Pattern score | Fibonacci       | Pattern rialzista                | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:------------------|:----------------|:--------------------------|:------------------------------------------------------|----------------:|:----------------|:---------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 86.751 $ | 12 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Volatilità in espansione | +1 | +1 / RECUPERATO | Doppio minimo / ATTIVO | Doppio massimo / CANDIDATO | 74.945 | 82.262 |
| SOL | 118,95 $ | 9 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Struttura ribassista con massimi e minimi decrescenti | 0 | +1 / RECUPERATO | Doppio minimo / TARGET RAGGIUNTO | Triplo massimo / CANDIDATO | 96,23 | 107,12 |
| DOGE | 0.10210 $ | 10 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Struttura ribassista con massimi e minimi decrescenti | +1 | +1 / RECUPERATO | Doppio minimo / ATTIVO | Doppio massimo / CANDIDATO | 0.07841 | 0.11825 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | ATTIVO | TARGET RAGGIUNTO | Eve and Adam Bottom — ATTIVO | CANDIDATO | CANDIDATO | ASSENTE | 1 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | INVALIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | ATTIVO | TARGET RAGGIUNTO | Adam and Eve Bottom — ATTIVO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 1 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 74.06 | 637.317 | 79.387 | 74.137 | 70.676 | 8,29% | -2,19% | 9,86% | 45,26% |
| SOL | 70.24 | 1.23215 | 104,93 | 94,08 | 84,09 | 13,80% | -4,82% | 20,69% | 76,03% |
| DOGE | 72.43 | 0.00145 | 0.08724 | 0.08155 | 0.08779 | 8,06% | -9,59% | 13,56% | 36,52% |

## Dettaglio asset

### BTC

- Prezzo: **86.751 $**
- Punteggio tecnico: **12 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 7.625e+04 -> 7.494e+04. Ultimi massimi: 8.135e+04 -> 8.226e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **RECUPERATO** (+1)
  - Swing DOWN 2026-09-03 82.262 -> 2026-09-15 74.945; livello più vicino 78.6% a 80.696; stato RECUPERATO; confluenza: resistenza tecnica, neckline rialzista, invalidazione rialzista.
- Punteggio pattern: **+1**
  - rialzista dominante: Doppio minimo (ATTIVO, +1); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **74.945**
- Resistenza più vicina: **82.262**

Pattern classici e ciclo di vita:

- Doppio minimo: **ATTIVO** (+1)
  - Due minimi simili vicino a 74.945 tra 2026-09-02 e 2026-09-15. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (2 giorni fa). Stato: ATTIVO. Target teorico: 89.580; progresso corrente: 61,34%. Relazione prezzo/neckline: sopra neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (2g); progresso 61,34%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (35 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 421,34%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (35g); progresso 421,34%; prezzo sopra neckline.
- Eve and Adam Bottom: **ATTIVO** (+1)
  - Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (2 giorni fa). Stato: ATTIVO. Target teorico: 89.580; progresso corrente: 61,34%. Relazione prezzo/neckline: sopra neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (2g); progresso 61,34%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.508 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 62.227. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 45 giorni.
  - neckline 62.227; target 58.946; distanza dalla neckline 39,41%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 45 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 50,22%; prezzo sopra neckline.
- Adam/Eve Top: **ASSENTE** (0)

### SOL

- Prezzo: **118,95 $**
- Punteggio tecnico: **9 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 97.45 -> 96.23. Ultimi massimi: 110 -> 107.1.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **RECUPERATO** (+1)
  - Swing DOWN 2026-08-27 110,04 -> 2026-09-16 96,23; livello più vicino 78.6% a 107,08; stato RECUPERATO; confluenza: resistenza tecnica, neckline rialzista, invalidazione rialzista.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Triplo massimo (CANDIDATO, 0).
- Supporto più vicino: **96,23**
- Resistenza più vicina: **107,12**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 96,23 tra 2026-09-02 e 2026-09-16. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: 108,66%. Relazione prezzo/neckline: sopra neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (5g); progresso 108,66%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (35 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 500,81%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (35g); progresso 500,81%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 96,23 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: 108,66%. Relazione prezzo/neckline: sopra neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (5g); progresso 108,66%; prezzo sopra neckline.
- Doppio massimo: **INVALIDATO** (0)
  - Due massimi simili vicino a 110,04 tra 2026-08-27 e 2026-09-06. Neckline ribassista stimata: 97,45. Breakout neckline: 2026-09-15 (8 giorni fa). Stato: INVALIDATO. Target teorico: 84,86; progresso corrente: -170,79%. Relazione prezzo/neckline: sopra neckline.
  - neckline 97,45; target 84,86; breakout 2026-09-15 (8g); progresso -170,79%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 45 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 68,26%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 83,81 dal 2026-07-04 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 45 giorni.
  - neckline 70,69; target 57,58; distanza dalla neckline 68,26%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.10210 $**
- Punteggio tecnico: **10 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 0.08028 -> 0.07841. Ultimi massimi: 0.09998 -> 0.09421.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **RECUPERATO** (+1)
  - Swing DOWN 2026-08-22 0.09998 -> 2026-09-16 0.07841; livello più vicino 78.6% a 0.09536; stato RECUPERATO; confluenza: neckline rialzista, invalidazione rialzista.
- Punteggio pattern: **+1**
  - rialzista dominante: Doppio minimo (ATTIVO, +1); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.07841**
- Resistenza più vicina: **0.11825**

Pattern classici e ciclo di vita:

- Doppio minimo: **ATTIVO** (+1)
  - Due minimi simili vicino a 0.07841 tra 2026-09-02 e 2026-09-16. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (2 giorni fa). Stato: ATTIVO. Target teorico: 0.11001; progresso corrente: 49,93%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.09421; target 0.11001; breakout 2026-09-21 (2g); progresso 49,93%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06835 dal 2026-07-13 al 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (35 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07926; progresso corrente: 518,72%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07926; breakout 2026-08-19 (35g); progresso 518,72%; prezzo sopra neckline.
- Adam and Eve Bottom: **ATTIVO** (+1)
  - Pattern Adam and Eve Bottom vicino a 0.07841 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (2 giorni fa). Stato: ATTIVO. Target teorico: 0.11001; progresso corrente: 49,93%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.09421; target 0.11001; breakout 2026-09-21 (2g); progresso 49,93%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 43 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 50,21%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 43 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 50,21%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 43 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 50,21%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                                                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:----------------------------------------------------------------|--------:|
| BTC | DOWN 2026-09-03 -> 2026-09-15 | 76.672 | 77.740 | 78.603 | 79.467 | 80.696 | 78.6% / 80.696 | RECUPERATO | resistenza tecnica, neckline rialzista, invalidazione rialzista | +1 |
| SOL | DOWN 2026-08-27 -> 2026-09-16 | 99,49 | 101,50 | 103,13 | 104,76 | 107,08 | 78.6% / 107,08 | RECUPERATO | resistenza tecnica, neckline rialzista, invalidazione rialzista | +1 |
| DOGE | DOWN 2026-08-22 -> 2026-09-16 | 0.08350 | 0.08665 | 0.08919 | 0.09174 | 0.09536 | 78.6% / 0.09536 | RECUPERATO | neckline rialzista, invalidazione rialzista | +1 |

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

- **BTC**: 30/30 previsioni controllate su 77 fatte. Stato: **ATTIVA**.
- **SOL**: 30/30 previsioni controllate su 77 fatte. Stato: **ATTIVA**.
- **DOGE**: 30/30 previsioni controllate su 77 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 77 | 30 | 30/30 [██████████] | 47 | ATTIVA | 2026-09-24 / tra 1 giorno |
| SOL | 77 | 30 | 30/30 [██████████] | 47 | ATTIVA | 2026-09-24 / tra 1 giorno |
| DOGE | 77 | 30 | 30/30 [██████████] | 47 | ATTIVA | 2026-09-24 / tra 1 giorno |

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

Generato: 2026-09-23 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 1 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 86.751 $          | 86.751 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.10210 $         | 0.10210 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 118,95 $          | 118,95 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 86.751 $          | 86.751 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 118,95 $          | 118,95 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.10210 $         | 0.10210 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 86.751 $          | 86.751 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 118,95 $          | 118,95 $        | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.10210 $         | 0.10210 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 86.751 $          | 86.751 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 118,95 $          | 118,95 $        | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.10210 $         | 0.10210 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 86.751 $          | 86.751 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 118,95 $          | 118,95 $        | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.10210 $         | 0.10210 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 86.751 $          | 86.922 $        | +0,1981%     |
| Exchange Microstructure | SOL     | price             | OK      | 118,95 $          | 119,17 $        | +0,1866%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.10210 $         | 0.10292 $       | +0,8031%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 118,95 $          | 118,95 $        | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 118,95 $          | 118,95 $        | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 118,95 $          | 118,95 $        | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 118,95 $          | 118,95 $        | +0,0000%     |

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


<!-- SOL_LONG_TERM_CONE_HISTORY_START -->
## SOL Long-Term Cone History

[SOL Long-Term Cone History](sol_long_term_history/README.md)
<!-- SOL_LONG_TERM_CONE_HISTORY_END -->
