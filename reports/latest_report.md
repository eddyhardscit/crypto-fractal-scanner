<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-07-11 19:00 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +4 | BULLISH | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | NO LONG A LEVA / ATTENDI SOPRA 67.248 $ | NO SHORT | nessuna | nessuna | MEDIO |
| SOL | -1 | LEGGERMENTE BEARISH | TAKE PROFIT SU SPIKE / NON INSEGUIRE | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | -5 | BEARISH | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+4**, spot = **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**, long = **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **-1**, spot = **TAKE PROFIT SU SPIKE / NON INSEGUIRE**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **-5**, spot = **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+4**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**
- Long leva: **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**
- Short leva: **NO SHORT**
- Rischio: **MEDIO**
- Conferme: Prima resistenza sopra 65.544; conferma del doppio minimo sopra 67.248.
- Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Global Confluence: **-1**
- Confluenza: **DEBOLE / FRAGILE**
- Bias Global: **Fragile**
- Direzione decisionale: **LEGGERMENTE BEARISH**
- Azione spot dal Global: **TAKE PROFIT SU SPIKE / NON INSEGUIRE**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo confermato recente finché mantiene 75,94; nuova conferma tecnica sopra 83,81; milestone analogiche 81,91 / 114,48, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 74,11 / 64,42 / 62,19.

### DOGE

- Global Confluence: **-5**
- Confluenza: **NEGATIVA**
- Bias Global: **Ribassista**
- Direzione decisionale: **BEARISH**
- Azione spot dal Global: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**
- Long leva: **NO LONG A LEVA**
- Short leva: **SHORT SOLO DOPO SPIKE**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.06961 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 5; EMA200 circa 113,51 $; upside verso EMA200 +45,49%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

</details>
<!-- COMPACT_SECTION_END:decision -->

<!-- COMPACT_SECTION_START:module_accuracy -->
<details>
<summary><strong>🧪 Accuratezza moduli e raccolta dati</strong></summary>

<!-- MODULE_ACCURACY_START -->
# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-11 19:00 UTC

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

Segnali totali salvati: **9**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-11 | BTC | 64.040,99 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-11 | DOGE | 0.07401 | -8 | -4 | -3 | -3 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-11 | SOL | 77,80 | +1 | 0 | -1 | +1 | +1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-10 | BTC | 63.864,39 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-10 | DOGE | 0.07388 | -8 | -4 | -3 | -3 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-10 | SOL | 77,70 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-09 | BTC | 63.234,86 | +6 | +3 | +3 | +3 | -1 | 0 | 0 | ACCUMULA SU PULLBACK / NO SHORT |
| 2026-07-09 | DOGE | 0.07285 | -10 | -3 | -3 | -3 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-09 | SOL | 78,02 | +4 | -1 | -1 | +2 | +1 | 0 | +1 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| SOL | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOGE | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-09 | 3g | 2026-07-12 | domani |
| SOL | 2026-07-09 | 3g | 2026-07-12 | domani |
| DOGE | 2026-07-09 | 3g | 2026-07-12 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 2 | 50,00% | -0,02% | -0,02% | FEEDBACK RAPIDO |
| BTC | 2g | 1 | 100,00% | +1,27% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 5g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 7g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 1 | 0,00% | -0,10% | -0,10% | FEEDBACK RAPIDO |
| SOL | 2g | 1 | 0,00% | -0,28% | -0,28% | FEEDBACK RAPIDO |
| SOL | 3g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 5g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 7g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 2 | 50,00% | +0,03% | -0,03% | FEEDBACK RAPIDO |
| DOGE | 2g | 1 | 0,00% | +1,59% | -1,59% | FEEDBACK RAPIDO |
| DOGE | 3g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 5g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 7g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 2 | 50,00% | -0,02% | -0,02% | -0,06% | +0,17% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 2 | 50,00% | -0,02% | -0,02% | -0,06% | +0,17% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 2 | 50,00% | -0,02% | -0,02% | -0,06% | +0,17% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 2 | 50,00% | -0,02% | -0,02% | -0,06% | +0,17% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 1 | 100,00% | -0,31% | +0,31% | -0,34% | -0,08% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 1 | 100,00% | +1,27% | +1,27% | +1,22% | +1,41% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | +1,27% | +1,27% | +1,22% | +1,41% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | +1,27% | +1,27% | +1,22% | +1,41% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 1 | 100,00% | +1,27% | +1,27% | +1,22% | +1,41% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 1 | 0,00% | +1,27% | -1,27% | +1,22% | +1,41% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 2 | 50,00% | +0,03% | -0,03% | -0,03% | +0,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 2 | 50,00% | +0,03% | -0,03% | -0,03% | +0,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 2 | 50,00% | +0,03% | -0,03% | -0,03% | +0,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 2 | 50,00% | +0,03% | -0,03% | -0,03% | +0,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 2 | 50,00% | +0,03% | -0,03% | -0,03% | +0,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 2 | 50,00% | +0,03% | -0,03% | -0,03% | +0,15% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 1 | 0,00% | +1,59% | -1,59% | +1,49% | +1,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 1 | 0,00% | +1,59% | -1,59% | +1,49% | +1,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 1 | 0,00% | +1,59% | -1,59% | +1,49% | +1,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | +1,59% | -1,59% | +1,49% | +1,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 1 | 0,00% | +1,59% | -1,59% | +1,49% | +1,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 1 | 0,00% | +1,59% | -1,59% | +1,49% | +1,68% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 2 | 50,00% | +0,01% | -0,01% | -0,05% | +0,24% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 2 | 50,00% | +0,01% | -0,01% | -0,05% | +0,24% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 2 | 50,00% | +0,01% | +0,01% | -0,05% | +0,24% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | -0,28% | +0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | -0,28% | +0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |

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

Generato: 2026-07-11 19:00 UTC

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
| BTC | 3 | FEEDBACK RAPIDO | 2 | 0 | 0 | 0 | Famiglia statistica | 1g | 50,00% | -0,02% | feedback rapido: utile da osservare, non da pesare |
| SOL | 3 | FEEDBACK RAPIDO | 2 | 0 | 0 | 0 | Tecnico | 1g | 50,00% | +0,01% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 3 | FEEDBACK RAPIDO | 2 | 0 | 0 | 0 | Famiglia statistica | 1g | 50,00% | -0,03% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 2 | 50,00% | -0,02% | -0,02% | -0,06% | +0,17% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 1 | 100,00% | +0,31% | -0,31% | -0,34% | -0,08% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 1 | 100,00% | +1,27% | +1,27% | +1,22% | +1,41% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 1 | 0,00% | -1,27% | +1,27% | +1,22% | +1,41% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 2 | 50,00% | -0,03% | +0,03% | -0,03% | +0,15% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 2 | 50,00% | -0,03% | +0,03% | -0,03% | +0,15% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 2 | 50,00% | -0,03% | +0,03% | -0,03% | +0,15% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 1 | 0,00% | -1,59% | +1,59% | +1,49% | +1,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 1 | 0,00% | -1,59% | +1,59% | +1,49% | +1,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 1 | 0,00% | -1,59% | +1,59% | +1,49% | +1,68% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 2 | 50,00% | -0,01% | +0,01% | -0,05% | +0,24% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 2 | 50,00% | +0,01% | +0,01% | -0,05% | +0,24% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 1 | 100,00% | +0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 2 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 2 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 2 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 3 | 66,67% | +0,41% |
| BTC | BREVE | Tecnico | 2 | 50,00% | -0,48% |
| DOGE | BREVE | Classic technical | 3 | 33,33% | -0,55% |
| DOGE | BREVE | Famiglia statistica | 3 | 33,33% | -0,55% |
| DOGE | BREVE | Tecnico | 3 | 33,33% | -0,55% |
| SOL | BREVE | Famiglia statistica | 3 | 66,67% | +0,09% |
| SOL | BREVE | Frattale SOL | 2 | 0,00% | -0,19% |
| SOL | BREVE | Tecnico | 3 | 33,33% | -0,09% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 11 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 15 | in attesa di controlli maturati |
| BTC | SWING | 10 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | BREVE | 9 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 15 | in attesa di controlli maturati |
| SOL | SWING | 10 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 9 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 15 | in attesa di controlli maturati |
| DOGE | SWING | 10 | in attesa di controlli maturati |
| DOGE | MEDIO | 15 | in attesa di controlli maturati |

## Come leggere le raccomandazioni

- **OSSERVA**: meno di 30 controlli, nessuna modifica.
- **PESO OK / MANTIENI**: il modulo sta aiutando, ma non serve cambiare peso.
- **NON AUMENTARE**: il modulo non dimostra ancora un vantaggio sufficiente.
- **POSSIBILE AUMENTO LEGGERO**: proposta prudente, mai automatica.
- **POSSIBILE RIDUZIONE**: modulo debole con campione già abbastanza maturo.
- **ESCLUSO**: benchmark o diagnostica già inclusa in un'altra famiglia.

Nota decisiva: **non sommare mai una modifica alla Famiglia statistica e altre modifiche separate a Scanner o Market Regime**. Scanner e Market servono soltanto a capire quale parte della famiglia sta funzionando o fallendo.

## Stato attuale

Siamo ancora in feedback rapido. Non bisogna modificare i pesi del Global. La nuova struttura serve ad accumulare dati corretti senza doppio conteggio.
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

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio   |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:---------------|
| BTC     |          3 |               0 |           3 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| SOL     |          3 |               0 |           3 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| DOGE    |          3 |               0 |           3 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | BASSO          | ALTO           | spot/tranche; se proprio leva, massimo 2x con margine molto largo       |
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

Generato: 2026-07-11 19:00 UTC

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
| BTC | +4 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | Prima resistenza sopra 65.544; conferma del doppio minimo sopra 67.248. | Sotto 57.748 il quadro tecnico peggiora. |
| SOL | -1 | DEBOLE / FRAGILE | Fragile | BASSA / RACCOLTA DATI | TAKE PROFIT SU SPIKE / NON INSEGUIRE | Doppio minimo confermato recente finché mantiene 75,94; nuova conferma tecnica sopra 83,81; milestone analogiche 81,91 / 114,48, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 74,11 / 64,42 / 62,19. |
| DOGE | -5 | NEGATIVA | Ribassista | MEDIA | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante. | Sotto 0.06961 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | +3 | +4 | 0 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | +4 |
| SOL | -2 | 0 | -2 | 0 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -1 |
| DOGE | -3 | -3 | -4 | 0 | -2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | -5 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+4**
- Affidabilità: **MEDIA**
- Azione coerente: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**

BTC è l'asset messo meglio nel breve, ma lo score statistico ora conta Scanner e Market Regime una sola volta. La struttura macro resta debole: ha più senso accumulare a tranche sui pullback che inseguire il prezzo vicino alle resistenze.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +3, match regime 11. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 72,50%, return centrale 30g +7,63%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 11, positivi 30g 100,00%, return p50 +22,02%.
- Scanner path: **0** — Raccolta dati. Controlli disponibili 1. Servono almeno 5 controlli prima di pesare il cono previsionale.
- Tecnico: **+1** — Score tecnico 1/12, verdetto neutrale / misto, trend ribassista, struttura ribassista con massimi e minimi decrescenti, divergenza rialzista rsi, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / TARGET RAGGIUNTO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 0/12, verdetto NEUTRALE / MISTO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff SPRING / TEST POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.00, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.25; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 1, campioni 4h 4 su 3.35h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 4/5.
- Daily change: **-1** — BTC: cambiamento medio in peggioramento rispetto a ieri.

Conferme: Prima resistenza sopra 65.544; conferma del doppio minimo sopra 67.248.

Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Confluenza: **DEBOLE / FRAGILE**
- Bias: **Fragile**
- Punteggio finale: **-1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **TAKE PROFIT SU SPIKE / NON INSEGUIRE**

SOL è fragile nel breve. Il frattale da solo non basta: se non recupera le conferme e il gap non rientra, il rischio è di inseguire uno spike scaricato.

Dettaglio moduli:

- Famiglia statistica: **-2** — Scanner grezzo -2, Market Regime grezzo 0, match regime 21. Regime neutro: resta il punteggio Scanner. Punteggio contato nel Global: -2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-2** — Casi positivi 35,00%, return centrale 30g -1,70%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 21, positivi 30g 47,62%, return p50 +0,00%.
- Scanner path: **0** — Raccolta dati. Controlli disponibili 1. Servono almeno 5 controlli prima di pesare il cono previsionale.
- Tecnico: **+1** — Score tecnico 2/12, verdetto neutrale / misto, trend misto, struttura volatilità in espansione, divergenza nessuna, Wyckoff range / fase non chiara, pattern score +2 (rialzista Doppio minimo / CONFERMATO RECENTE; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 0/12, verdetto NEUTRALE / MISTO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff RANGE / FASE NON CHIARA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto STRUTTURA ANALOGA, PREZZO NON ADERENTE, somiglianza strutturale +65,20%, aderenza live +58,19%, errore live +20,90%, gap corrente +17,04%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE NON CONFERMATO DAL PREZZO, rischio ALTO.
- Fractal path: **0** — Tracking operativo, ma nessuna milestone settimanale ancora verificata. Gap corrente +17,04%, errore live +20,90%. Il modulo non pesa finché non maturano abbastanza controlli.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 5, bias SQUEEZE SETUP FORTE, EMA200 113,51 $, upside EMA200 +45,49%, gap EMA50/EMA200 -1,21%, hit EMA200 12w +26,67%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.00, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 4 su 3.35h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — SOL: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Doppio minimo confermato recente finché mantiene 75,94; nuova conferma tecnica sopra 83,81; milestone analogiche 81,91 / 114,48, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 74,11 / 64,42 / 62,19.

### DOGE

- Confluenza: **NEGATIVA**
- Bias: **Ribassista**
- Punteggio finale: **-5**
- Affidabilità: **MEDIA**
- Azione coerente: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**

DOGE resta l'asset più debole. Anche senza contare due volte Scanner e Market Regime, la confluenza generale resta chiaramente negativa rispetto a BTC e SOL.

Dettaglio moduli:

- Famiglia statistica: **-4** — Scanner grezzo -3, Market Regime grezzo -3, match regime 31. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: -4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-3** — Casi positivi 15,00%, return centrale 30g -20,25%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **-3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 31, positivi 30g 12,90%, return p50 -22,50%.
- Scanner path: **0** — Raccolta dati. Controlli disponibili 1. Servono almeno 5 controlli prima di pesare il cono previsionale.
- Tecnico: **-2** — Score tecnico -4/12, verdetto debole, trend ribassista, struttura ribassista con massimi e minimi decrescenti, divergenza ribassista nascosta rsi, Wyckoff possibile accumulazione, pattern score -1 (rialzista Triplo minimo / CANDIDATO; ribassista Triplo massimo / MATURO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -3/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.00, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.75; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 0, campioni 4h 4 su 3.35h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **+1** — DOGE: cambiamento medio in miglioramento rispetto a ieri.

Conferme: Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante.

Invalidazioni: Sotto 0.06961 il rischio ribassista aumenta.


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

Generato: 2026-07-11 19:00 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 64.272 $ | prezzo corrente |
| Power Law centrale | 122.003 $ | deviazione -47,32% |
| Banda p10-p90 | 76.159 $ / 306.315 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 2,06% | posizione storica nel corridoio |
| Esponente β | 5,8480 | R² log-log 92,00% |
| Stabilità β | BASSA | range 1,3044 cambiando finestra |
| Ultimo halving | 2024-04-19 | 813 giorni fa |
| Fase ciclo | 55,65% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-07-11 (4316 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.4172) × giorni^5.8480
- Prezzo centrale oggi: **122.003 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 2,06%
- Scarto dal centro: **-47,32%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8480 | 92,00% |
| 2015 | 5,9354 | 91,58% |
| 2016 | 5,6264 | 87,82% |
| 2017 | 4,8958 | 82,90% |
| 2018 | 4,6309 | 78,37% |

### Backtest walk-forward contro prezzo invariato

| Orizzonte | Controlli | Vittorie vs naive | Errore mediano modello | Errore mediano naive |
| --- | --- | --- | --- | --- |
| 90g | 79 | 26,58% | 55,14% | 20,89% |
| 180g | 79 | 40,51% | 60,84% | 45,16% |
| 365g | 79 | 56,96% | 73,12% | 81,57% |
| 730g | 79 | 59,49% | 72,50% | 109,89% |

## Bitcoin Four-Year Spiral

Nel grafico l'angolo rappresenta il tempo dentro una finestra di quattro anni e il raggio rappresenta il prezzo in scala logaritmica. ATH, bottom storici e halving sono marker descrittivi: la spirale rende visibili le ricorrenze, ma non dimostra che il ciclo futuro debba ripetersi.

![Bitcoin Four-Year Spiral](bitcoin_four_year_spiral.png)

## Stessa fase dei cicli halving precedenti

| Ciclo | Data analoga | +30g | +90g | +180g | +365g |
| --- | --- | --- | --- | --- | --- |
| 2012-11-28 → 2016-07-09 | 2014-12-02 | -17,59% | -27,71% | -39,63% | -5,80% |
| 2016-07-09 → 2020-05-11 | 2018-08-28 | -5,91% | -46,74% | -46,30% | +37,46% |
| 2020-05-11 → 2024-04-19 | 2022-07-21 | -8,63% | -17,38% | -8,65% | +29,11% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | -1 | 0 | 15.499531957225177 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -8 | -1 | -13.500180629169979 | 0 |

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

Generato: 2026-07-11 19:00 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00121390 | -1 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +15,50% | MISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000117 | -8 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -13,50% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (-1)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g -6,19%; 30g +15,50%; 90g +5,28%; 180g -20,45%
- **Daily:** RSI 51.50; MA50 0.00114614; MA200 0.00123260
- **Weekly:** MA30 0.00123686; RSI 48.23
- **Livelli:** supporto 0.00119400; resistenza 0.00125100; breakout 60g 0.00134900; breakdown 60g 0.00100900
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00113200; target 0.00117200
- **Fibonacci:** VICINO — 38.2% a 0.00121912
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; MA50 daily in salita; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-8)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g -4,86%; 30g -13,50%; 90g -8,86%; 180g -21,86%
- **Daily:** RSI 32.02; MA50 0.00000130; MA200 0.00000136
- **Weekly:** MA30 0.00000136; RSI 33.52
- **Livelli:** supporto 0.00000116; resistenza 0.00000128; breakout 60g 0.00000153; breakdown 60g 0.00000112
- **Pattern:** DOPPIO MASSIMO / TARGET RAGGIUNTO; neckline 0.00000131; target 0.00000113
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000124
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; RSI relativo debole; MACD relativo negativo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 202 | 51,98% | +1,97% | -1,34% |
| SOL | 30g | 199 | 48,24% | +4,85% | +0,36% |
| SOL | 90g | 193 | 54,40% | +10,50% | +0,53% |
| DOGE | 7g | 289 | 55,71% | +1,85% | -1,77% |
| DOGE | 30g | 286 | 52,45% | +1,93% | -3,49% |
| DOGE | 90g | 283 | 53,71% | +6,91% | -8,20% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **11 luglio 2026**

## Verdetto: STRUTTURA ANALOGA, PREZZO NON ADERENTE

- **Fase attuale:** FRATTALE NON CONFERMATO DAL PREZZO
- **Somiglianza totale:** +65,20%
- **Somiglianza strutturale:** +65,20%
- **Aderenza prezzo live:** +58,19%
- **Errore medio live:** +20,90%
- **Gap prezzo corrente:** +17,04%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA / NON OPERATIVO
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** La geometria ricorda BTC 2022, ma SOL è troppo distante dal percorso scalato per usarlo come conferma operativa.
- **SOL è al giorno:** 35 dal bottom usato.
- **Giorno BTC equivalente:** 2022-12-26
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Laterale / movimento non forte.** Zona bassa **76,29 $** intorno al **16 luglio 2026**; zona alta **79,29 $** intorno al **25 luglio 2026**; fine step circa **79,29 $** entro il **25 luglio 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 11 luglio 2026 | 9 | +58,19% | +20,90% | +17,04% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 11 luglio 2026 | 36 | +80,51% | +9,74% | +17,04% | ABBASTANZA ALLINEATO |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +58,19% | Errore medio live +20,90%. |
| Gap corrente | +17,04% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 81,91 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 114,48 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 74,11 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 575,18 $ |
| Massimo percorso base | 575,18 $ (21 aprile 2029) |

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
| Prima conferma | 81,91 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 114,48 $ | Scenario più credibile. |
| Invalidazione soft | 74,11 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 18 luglio 2026 | -1,37% | 76,94 $ | 76,29 $ | 78,01 $ |
| 14 giorni | 25 luglio 2026 | +1,64% | 79,29 $ | 76,29 $ | 79,29 $ |
| 30 giorni | 10 agosto 2026 | +36,63% | 106,59 $ | 76,29 $ | 106,59 $ |
| 60 giorni | 9 settembre 2026 | +37,11% | 106,96 $ | 76,29 $ | 114,48 $ |
| 90 giorni | 9 ottobre 2026 | +65,45% | 129,07 $ | 76,29 $ | 130,64 $ |
| 120 giorni | 8 novembre 2026 | +67,30% | 130,51 $ | 76,29 $ | 140,56 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 11 luglio 2026 -> 25 luglio 2026 | +1,64% | 76,29 $ (16 luglio 2026) | 79,29 $ (25 luglio 2026) | 79,29 $ | Laterale / movimento non forte. |
| Step 2 - primo mese | 26 luglio 2026 -> 10 agosto 2026 | +36,63% | 80,44 $ (26 luglio 2026) | 106,59 $ (10 agosto 2026) | 106,59 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 11 agosto 2026 -> 9 settembre 2026 | +37,11% | 99,82 $ (26 agosto 2026) | 114,48 $ (5 settembre 2026) | 106,96 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 10 settembre 2026 -> 9 ottobre 2026 | +65,45% | 93,07 $ (23 settembre 2026) | 130,64 $ (6 ottobre 2026) | 129,07 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 78,01 $ |  |
| Weekly RSI | 40,61 / linea grezza 54,36 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 41,40 / linea grezza 56,16 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 575,18 $ | Avanzamento +13,56% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 41,4, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Score on-chain | 0 |
| Bias | NEUTRALE / MISTA |
| Azione coerente | NESSUNA CONFERMA FORTE / LEGGERE INSIEME AL FRATTALE |
| Prezzo SOL | 78,01 $ |
| TVL Solana | 4,94 mld $ |
| TVL 7g | -3,52% |
| DEX volume 24h | 1,59 mld $ |
| Fees 24h | 7,69 mln $ |
| Stablecoin su Solana | 15,43 mld $ |
| Stake ratio | 67,94% |
| Metriche mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

Lettura semplice:

**NESSUNA CONFERMA FORTE / LEGGERE INSIEME AL FRATTALE**

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

| Voce                      | Valore                                              |
|:--------------------------|:----------------------------------------------------|
| Lifecycle squeeze score | 5 |
| Bias | SQUEEZE SETUP FORTE |
| Azione coerente | CONTESTO BUONO VERSO EMA200, MA NON PESA NEL GLOBAL |
| Peso suggerito Global | 0 |
| Trend squeeze | STABILE / DA CONFERMARE |
| Trend squeeze score | 0 |
| Confronto precedente | 2026-07-09 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 78,01 $ |
| EMA200 weekly target | 113,51 $ |
| Upside verso EMA200 | +45,49% |
| Distanza prezzo da EMA200 | -31,27% |
| Gap EMA50/EMA200 | -1,21% |
| Stato cross | EMA50/EMA200 SOVRAPPOSTE / INCROCIO IN CORSO |
| RSI weekly | 40,62 |
| Età SOL | 6,2 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +26,67% |
| Max gain mediano 12w | +23,06% |
| Drawdown mediano 12w | -24,14% |

Lettura semplice:

**CONTESTO BUONO VERSO EMA200, MA NON PESA NEL GLOBAL**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-07-11 19:00 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-07-11 18:57:12 UTC**

Questo report confronta il grafico attuale di Bitcoin, Solana e Dogecoin con tanti grafici storici di altre crypto.

Non è una previsione certa. È uno scanner statistico: guarda situazioni simili già successe e mostra cosa accadde dopo nei 30 giorni successivi.

<!-- COMPACT_SECTION_START:daily_change -->
<details open>
<summary><strong>🗓️ Cambiamenti rispetto a ieri</strong></summary>

<!-- DAILY_CHANGE_START -->

---

# Mini report cambiamenti da ieri

Report separato completo: [daily_change_report.md](daily_change_report.md)

- BTC: cambiamento importante in peggioramento rispetto a ieri.
- SOL: nessun cambiamento forte rispetto a ieri.
- DOGE: cambiamento importante in miglioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO MEDIO | peggioramento | RIALZISTA | +72.50% | -5.00 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | peggioramento | NEUTRALE / INCERTO | +35.00% | -2.50 punti |
| DOGE | CAMBIAMENTO MEDIO | miglioramento | RIBASSISTA | +15.00% | 0.00 punti |

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
| BTC | 61.059 $ | 70.700 $ | +5,88% | +15,79% | rimbalzo poco frequente | 70.700 $ | 61.059 $ | +9,52% | -13,64% | spike storicamente più resistente |
| SOL | 74,11 $ | 85,81 $ | +9,68% | +15,79% | rimbalzo poco frequente | 85,81 $ | 74,11 $ | +37,50% | -13,64% | scarico possibile |
| DOGE | 0,07134 $ | 0,08261 $ | +13,16% | +15,79% | rimbalzo poco frequente | 0,08261 $ | 0,07134 $ | +61,54% | -13,64% | attenzione a prendere profitto |

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

- **BTC: su 40 casi simili, 17 prima sono scesi a -5,00%. Tra quei 17, 1 poi sono rimbalzati fino a +10,00%. Percentuale: +5,88% (1/17). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **BTC: su 40 casi simili, 21 prima sono saliti a +10,00%. Tra quei 21, 2 poi sono scaricati a -5,00%. Percentuale: +9,52% (2/21). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +9,68% (3/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 16 prima sono saliti a +10,00%. Tra quei 16, 6 poi sono scaricati a -5,00%. Percentuale: +37,50% (6/16). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.**
- **DOGE: su 40 casi simili, 38 prima sono scesi a -5,00%. Tra quei 38, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +13,16% (5/38). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 13 prima sono saliti a +10,00%. Tra quei 13, 8 poi sono scaricati a -5,00%. Percentuale: +61,54% (8/13). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-07-11 18:59:18 UTC

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
| BTC | 2026-07-11 | 64.273 $ | SALITA | 72,50% | 51.910,01 $ | 61.697,59 $ | 69.178,36 $ | 77.029,49 $ | 88.881,94 $ |
| SOL | 2026-07-11 | 78,01 $ | DISCESA | 35,00% | 61,67 $ | 71,08 $ | 76,69 $ | 83,33 $ | 100,94 $ |
| DOGE | 2026-07-11 | 0.07510 $ | DISCESA | 15,00% | 0.05110 $ | 0.05552 $ | 0.05989 $ | 0.06821 $ | 0.08093 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 1 | 100,00% | 100,00% | 0,83% | -0,83% |
| BTC | 3g | 0 | n/a | n/a | n/a | n/a |
| BTC | 7g | 0 | n/a | n/a | n/a | n/a |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a |
| SOL | 1g | 1 | 100,00% | 100,00% | 0,88% | -0,88% |
| SOL | 3g | 0 | n/a | n/a | n/a | n/a |
| SOL | 7g | 0 | n/a | n/a | n/a | n/a |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 1g | 1 | 100,00% | 100,00% | 1,43% | 1,43% |
| DOGE | 3g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 7g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 14g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a |

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

Generato: 2026-07-11 18:59 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione             | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:----------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO               | NO        | +72,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO               | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NEGATIVO / RIBASSISTA | SI        | +85,00%       | Casi negativi 85.00% >= 80%      |                  40 |

## DOGE — casi ribassisti

- Trigger: **Casi negativi 85.00% >= 80%**
- Casi usati nei grafici: **34**
- Return mediano 7g: **-7,28%**
- Return mediano 14g: **-25,71%**
- Return mediano 30g: **-22,70%**
- Drawdown mediano: **-30,03%**
- Max gain mediano: **+3,80%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+3,20%**
- Spike massimo medio prima del minimo: **+5,72%**
- Spike p75 prima del minimo: **+7,83%**
- Giorno mediano dello spike: **giorno 2**
- Giorno mediano del minimo: **giorno 15**
- Scarico mediano dal picco al minimo: **-32,64%**
- Casi con almeno +5% prima del minimo: **+38,24%**
- Casi con almeno +10% prima del minimo: **+20,59%**
- Casi con almeno +15% prima del minimo: **+11,76%**
- Discesa quasi immediata: **+0,00%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10     | P25     | P50     | P75     | P90    |
|:--------|:--------|:--------|:--------|:-------|
| -34,01% | -27,91% | -22,70% | -14,21% | -8,92% |

### Grafico pulito: bande + mediana

![Extreme clean DOGE](extreme_cases_DOGE_negative_clean_bands.png)

### Grafico asset per asset

![Extreme asset medians DOGE](extreme_cases_DOGE_negative_asset_medians.png)

### Spike massimo prima della discesa

La sigla `g7` sopra una barra significa che il massimo rialzo è avvenuto al giorno 7.

![Extreme spike before dump DOGE](extreme_cases_DOGE_negative_spike_before_dump.png)

### Spike iniziale contro minimo successivo

![Extreme spike vs low DOGE](extreme_cases_DOGE_negative_spike_vs_low.png)

### Casi ordinati per risultato finale

![Extreme ranked DOGE](extreme_cases_DOGE_negative_ranked_returns.png)

### Casi con spike maggiore prima del dump

| Asset storico   | End        | Similarity   | Spike prima del minimo   |   Giorno spike | Minimo 30g   |   Giorno minimo | Dump dal picco   | Return 30g   | Sequenza                      |
|:----------------|:-----------|:-------------|:-------------------------|---------------:|:-------------|----------------:|:-----------------|:-------------|:------------------------------|
| WAVES-USD       | 2022-05-30 | +84,86%      | +28,83%                  |              4 | -42,96%      |              17 | -55,72%          | -29,04%      | SPIKE PRIMA DEL DUMP          |
| LINK-USD        | 2022-05-30 | +84,27%      | +24,39%                  |             10 | -21,06%      |              14 | -36,54%          | -16,73%      | SPIKE PRIMA DEL DUMP          |
| ZEC-USD         | 2019-08-29 | +87,11%      | +17,47%                  |             20 | -21,74%      |              28 | -33,38%          | -9,79%       | SPIKE PRIMA DEL DUMP          |
| ZIL-USD         | 2019-08-16 | +83,63%      | +16,38%                  |              8 | -10,08%      |              21 | -22,74%          | -3,60%       | SPIKE PRIMA DEL DUMP          |
| ADA-USD         | 2022-06-04 | +84,98%      | +13,35%                  |              4 | -20,84%      |              27 | -30,16%          | -17,03%      | SPIKE PRIMA DEL DUMP          |
| AVAX-USD        | 2025-11-21 | +86,16%      | +12,94%                  |              6 | -14,04%      |              27 | -23,89%          | -8,75%       | SPIKE PRIMA DEL DUMP          |
| OMG-USD         | 2022-06-04 | +87,01%      | +11,92%                  |              5 | -29,18%      |              14 | -36,72%          | -22,91%      | SPIKE PRIMA DEL DUMP          |
| LTC-USD         | 2022-05-29 | +84,28%      | +8,43%                   |              1 | -32,07%      |              15 | -37,36%          | -17,15%      | SPIKE PRIMA DEL DUMP          |
| BAT-USD         | 2019-01-01 | +84,60%      | +7,93%                   |              8 | -13,95%      |              27 | -20,27%          | -13,42%      | RIALZO MODESTO PRIMA DEL DUMP |
| AVAX-USD        | 2022-06-05 | +84,85%      | +7,55%                   |              1 | -38,58%      |              13 | -42,89%          | -25,24%      | RIALZO MODESTO PRIMA DEL DUMP |
| CHZ-USD         | 2022-06-03 | +86,65%      | +5,97%                   |              3 | -28,71%      |              15 | -32,73%          | -19,17%      | RIALZO MODESTO PRIMA DEL DUMP |
| BTC-USD         | 2022-06-03 | +83,98%      | +5,61%                   |              3 | -35,98%      |              15 | -39,38%          | -35,04%      | RIALZO MODESTO PRIMA DEL DUMP |
| ENJ-USD         | 2022-06-04 | +86,44%      | +5,00%                   |              2 | -33,46%      |              14 | -36,63%          | -16,55%      | RIALZO MODESTO PRIMA DEL DUMP |
| QTUM-USD        | 2022-06-04 | +86,67%      | +4,84%                   |              2 | -33,01%      |              14 | -36,10%          | -24,73%      | RIALZO MODESTO PRIMA DEL DUMP |
| XTZ-USD         | 2026-03-15 | +87,15%      | +4,26%                   |              5 | -12,14%      |              14 | -15,73%          | -10,41%      | RIALZO MODESTO PRIMA DEL DUMP |
| NEO-USD         | 2022-05-30 | +85,28%      | +3,34%                   |              7 | -27,65%      |              19 | -29,99%          | -26,97%      | RIALZO MODESTO PRIMA DEL DUMP |
| INJ-USD         | 2022-06-01 | +86,30%      | +3,20%                   |              1 | -42,93%      |              30 | -44,70%          | -42,93%      | RIALZO MODESTO PRIMA DEL DUMP |
| ETH-USD         | 2022-06-04 | +86,37%      | +3,20%                   |              2 | -44,85%      |              14 | -46,56%          | -36,11%      | RIALZO MODESTO PRIMA DEL DUMP |
| FIL-USD         | 2022-06-03 | +84,43%      | +2,37%                   |              3 | -30,96%      |              15 | -32,56%          | -28,22%      | PERCORSO RIBASSISTA MISTO     |
| DASH-USD        | 2022-05-30 | +88,29%      | +2,32%                   |              1 | -33,95%      |              19 | -35,45%          | -29,45%      | PERCORSO RIBASSISTA MISTO     |

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
- Prezzo attuale: **64.273,03 $**
- Return normale fra 30 giorni: **69.178,36 $** (7,63%)
- Drawdown normale durante il mese: **61.430,15 $** (-4,42%)
- Drawdown brutto da rispettare: **56.661,41 $** (-11,84%)
- Max gain normale durante il mese: **72.457,84 $** (12,73%)
- Max gain buono / take profit ottimistico: **82.200,89 $** (27,89%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **35,00%**
- Casi negativi / discesa storica: **65,00%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **78,01 $**
- Return normale fra 30 giorni: **76,69 $** (-1,70%)
- Drawdown normale durante il mese: **68,35 $** (-12,39%)
- Drawdown brutto da rispettare: **59,73 $** (-23,44%)
- Max gain normale durante il mese: **83,21 $** (6,66%)
- Max gain buono / take profit ottimistico: **90,07 $** (15,45%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **15,00%**
- Casi negativi / discesa storica: **85,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,08 $**
- Return normale fra 30 giorni: **0,06 $** (-20,25%)
- Drawdown normale durante il mese: **0,05 $** (-28,67%)
- Drawdown brutto da rispettare: **0,05 $** (-33,59%)
- Max gain normale durante il mese: **0,08 $** (5,02%)
- Max gain buono / take profit ottimistico: **0,09 $** (14,11%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è prudente/debole. Lo scanner vede più rischio di discesa che salita pulita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 64.273,03 $

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

- Se va molto male: **51.910,01 $** (-19,24%)
- Se va male: **61.697,59 $** (-4,01%)
- Scenario normale: **69.178,36 $** (7,63%)
- Se va bene: **77.029,49 $** (19,85%)
- Se va molto bene: **88.881,94 $** (38,29%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **61.430,15 $** (-4,42%)
- Discesa brutta: **56.661,41 $** (-11,84%)
- Discesa molto brutta: **48.484,43 $** (-24,56%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **72.457,84 $** (12,73%)
- Rialzo buono: **82.200,89 $** (27,89%)
- Rialzo molto forte: **90.033,85 $** (40,08%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **61.430,15 $** e uno spike normale intorno a **72.457,84 $**.

La chiusura a 30 giorni era più spesso positiva: salita 72,50%, discesa 27,50%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 78,01 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **35,00%**
- Probabilità storica di discesa: **65,00%**
- Quanto è netto il segnale: **medio**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale medio. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **61,67 $** (-20,95%)
- Se va male: **71,08 $** (-8,88%)
- Scenario normale: **76,69 $** (-1,70%)
- Se va bene: **83,33 $** (6,82%)
- Se va molto bene: **100,94 $** (29,40%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **68,35 $** (-12,39%)
- Discesa brutta: **59,73 $** (-23,44%)
- Discesa molto brutta: **53,92 $** (-30,88%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **83,21 $** (6,66%)
- Rialzo buono: **90,07 $** (15,45%)
- Rialzo molto forte: **108,45 $** (39,02%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **68,35 $** e uno spike normale intorno a **83,21 $**.

La chiusura a 30 giorni era più spesso negativa: salita 35,00%, discesa 65,00%. Quindi la lettura principale è prudente/debole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🔴 ROSSO / Prudenza
**Prezzo attuale:** 0,08 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **15,00%**
- Probabilità storica di discesa: **85,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,05 $** (-31,96%)
- Se va male: **0,06 $** (-26,07%)
- Scenario normale: **0,06 $** (-20,25%)
- Se va bene: **0,07 $** (-9,17%)
- Se va molto bene: **0,08 $** (7,77%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,05 $** (-28,67%)
- Discesa brutta: **0,05 $** (-33,59%)
- Discesa molto brutta: **0,04 $** (-42,94%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,08 $** (5,02%)
- Rialzo buono: **0,09 $** (14,11%)
- Rialzo molto forte: **0,10 $** (26,69%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,05 $** e uno spike normale intorno a **0,08 $**.

La chiusura a 30 giorni era più spesso negativa: salita 15,00%, discesa 85,00%. Quindi la lettura principale è prudente/debole.

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

Per ora non ci sono ancora previsioni vecchie di 30 giorni da controllare.
Il controllo vero inizierà automaticamente dopo il primo mese di utilizzo.

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

Dati ancora insufficienti: previsioni controllate **0** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **0** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **0** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 64.273,03 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **72,50%**
- Casi negativi dopo 30 giorni: **27,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **84,88%**
- Rendimento medio dopo 30 giorni: **9,33%**
- Rendimento centrale dopo 30 giorni: **7,63%**
- Discesa media durante i 30 giorni: **-8,72%**
- Massimo rialzo medio durante i 30 giorni: **22,55%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **70.267,23 $**
- Scenario centrale a 30 giorni: **69.178,36 $**
- Zona di rischio media: **58.666,17 $**
- Zona di rialzo media: **78.765,08 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -19,24% → **51.910,01 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -4,01% → **61.697,59 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 7,63% → **69.178,36 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 19,85% → **77.029,49 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 38,29% → **88.881,94 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -24,56% → **48.484,43 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -11,84% → **56.661,41 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -4,42% → **61.430,15 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **64.273,03 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **64.273,03 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 4,69% → **67.289,96 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 8,09% → **69.471,05 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 12,73% → **72.457,84 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 27,89% → **82.200,89 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 40,08% → **90.033,85 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| LRC-USD         | 2018-09-19   | 2018-12-27 |        89.4  |        95.69 |           0    |         178.55 |
| FIL-USD         | 2023-06-19   | 2023-09-26 |        88.95 |        17.86 |           0    |          21.6  |
| XRP-USD         | 2019-09-24   | 2020-01-01 |        88.16 |        24.17 |          -2.4  |          26.46 |
| SAND-USD        | 2023-06-19   | 2023-09-26 |        86.43 |        11.11 |          -6.72 |          11.11 |
| KSM-USD         | 2022-03-10   | 2022-06-17 |        86.08 |        11.02 |          -4.93 |          16.96 |
| XLM-USD         | 2020-07-05   | 2020-10-12 |        86.05 |         3.87 |          -4.69 |           9.98 |
| THETA-USD       | 2023-06-19   | 2023-09-26 |        85.99 |         1.86 |         -11.53 |           5.02 |
| NEAR-USD        | 2024-04-15   | 2024-07-23 |        85.83 |       -25.43 |         -38.83 |           0    |
| ETC-USD         | 2019-05-12   | 2019-08-19 |        85.54 |        15.03 |           0    |          32.2  |
| DOT-USD         | 2023-06-20   | 2023-09-27 |        85.39 |         3.72 |          -8.57 |           8.96 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 78,01 $

Solana è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **35,00%**
- Casi negativi dopo 30 giorni: **65,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **75,99%**
- Rendimento medio dopo 30 giorni: **1,94%**
- Rendimento centrale dopo 30 giorni: **-1,70%**
- Discesa media durante i 30 giorni: **-14,93%**
- Massimo rialzo medio durante i 30 giorni: **15,90%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **79,52 $**
- Scenario centrale a 30 giorni: **76,69 $**
- Zona di rischio media: **66,36 $**
- Zona di rialzo media: **90,42 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -20,95% → **61,67 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -8,88% → **71,08 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -1,70% → **76,69 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 6,82% → **83,33 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 29,40% → **100,94 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -30,88% → **53,92 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -23,44% → **59,73 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -12,39% → **68,35 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -6,11% → **73,24 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **78,01 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **78,01 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 1,40% → **79,10 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 6,66% → **83,21 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 15,45% → **90,07 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 39,02% → **108,45 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| NEAR-USD        | 2024-04-15   | 2024-07-23 |        79.13 |       -25.43 |         -38.83 |           0    |
| DASH-USD        | 2024-04-15   | 2024-07-23 |        79.08 |        -1.21 |         -16.66 |           1.64 |
| TRX-USD         | 2018-09-19   | 2018-12-27 |        78.81 |        55.01 |           0    |          55.01 |
| QTUM-USD        | 2018-09-19   | 2018-12-27 |        78.74 |        -2.21 |          -3.68 |          15.25 |
| VET-USD         | 2020-01-09   | 2020-04-17 |        78.21 |        16.09 |          -3.73 |          26.08 |
| XLM-USD         | 2020-01-07   | 2020-04-15 |        77.98 |        45.24 |           0    |          62.58 |
| SOL-USD         | 2025-12-04   | 2026-03-13 |        77.97 |        -7.51 |         -10.44 |           9.16 |
| ZIL-USD         | 2018-09-21   | 2018-12-29 |        77.88 |        -0.39 |         -12.5  |          14.85 |
| WAVES-USD       | 2019-02-21   | 2019-05-31 |        77.65 |       -30.84 |         -30.84 |           0.49 |
| BNB-USD         | 2025-12-06   | 2026-03-15 |        77.64 |        -8.86 |         -13.44 |           0.84 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🔴 ROSSO / Prudenza

**Prezzo attuale:** 0,08 $

Dogecoin richiede prudenza. La statistica dei casi simili indica più possibilità di discesa che di salita. Con leva, il rischio principale è il drawdown durante il percorso.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **15,00%**
- Casi negativi dopo 30 giorni: **85,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,53%**
- Rendimento medio dopo 30 giorni: **-15,41%**
- Rendimento centrale dopo 30 giorni: **-20,25%**
- Discesa media durante i 30 giorni: **-25,86%**
- Massimo rialzo medio durante i 30 giorni: **9,59%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,06 $**
- Scenario centrale a 30 giorni: **0,06 $**
- Zona di rischio media: **0,06 $**
- Zona di rialzo media: **0,08 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -31,96% → **0,05 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -26,07% → **0,06 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -20,25% → **0,06 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: -9,17% → **0,07 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 7,77% → **0,08 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -42,94% → **0,04 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -33,59% → **0,05 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -28,67% → **0,05 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -14,01% → **0,06 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -8,41% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,08 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 0,99% → **0,08 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 5,02% → **0,08 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 14,11% → **0,09 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 26,69% → **0,10 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XRP-USD         | 2019-09-24   | 2020-01-01 |        88.85 |        24.17 |          -2.4  |          26.46 |
| DASH-USD        | 2022-02-20   | 2022-05-30 |        88.29 |       -29.45 |         -33.95 |           2.32 |
| NEAR-USD        | 2022-03-02   | 2022-06-09 |        88.16 |       -25.05 |         -39.1  |           0    |
| XTZ-USD         | 2025-12-06   | 2026-03-15 |        87.15 |       -10.41 |         -12.14 |           4.26 |
| ZEC-USD         | 2019-05-22   | 2019-08-29 |        87.11 |        -9.79 |         -21.74 |          17.47 |
| VET-USD         | 2022-02-27   | 2022-06-06 |        87.09 |       -25.78 |         -31.87 |           0.17 |
| OMG-USD         | 2022-02-25   | 2022-06-04 |        87.01 |       -22.91 |         -29.18 |          11.92 |
| QTUM-USD        | 2022-02-25   | 2022-06-04 |        86.67 |       -24.73 |         -33.01 |           4.84 |
| CHZ-USD         | 2022-02-24   | 2022-06-03 |        86.65 |       -19.17 |         -28.71 |           5.97 |
| 1INCH-USD       | 2022-02-22   | 2022-06-01 |        86.49 |       -31.62 |         -42.19 |           0    |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report

Generated: 2026-07-11 18:59 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.273 $ | False | -9.15% | -10.24% | BEAR | -9.15% | -10.24% |
| DOGE-USD | BEAR | 0.07510 $ | False | -17.29% | -16.60% | BEAR | -9.15% | -10.24% |
| SOL-USD | BEAR | 78,01 $ | False | -4.31% | -18.58% | BEAR | -9.15% | -10.24% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 72.50% | 7.63% | 19.85% | 38.29% | -4.42% | -24.56% | 12.73% | 27.89% | 40.08% | 67.50% | 22.54% | 43.73% | 57.64% |
| BTC-USD | SAME_BTC_REGIME | 13 | 100.00% | 25.70% | 39.37% | 48.27% | 0.00% | -3.45% | 37.70% | 53.16% | 61.45% | 92.31% | 32.98% | 42.97% | 47.46% |
| BTC-USD | SAME_ASSET_REGIME | 26 | 88.46% | 11.06% | 21.79% | 37.45% | -2.98% | -10.88% | 18.35% | 32.07% | 45.89% | 88.46% | 33.21% | 49.59% | 58.33% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 11 | 100.00% | 22.02% | 37.45% | 49.02% | 0.00% | -3.57% | 34.23% | 45.89% | 62.58% | 90.91% | 14.38% | 41.68% | 46.00% |
| DOGE-USD | ALL_MATCHES | 40 | 15.00% | -20.25% | -9.17% | 7.77% | -28.67% | -42.94% | 5.02% | 14.11% | 26.69% | 37.50% | -2.71% | 6.57% | 25.79% |
| DOGE-USD | SAME_BTC_REGIME | 33 | 12.12% | -22.91% | -16.55% | 0.36% | -30.82% | -42.95% | 4.26% | 8.43% | 27.94% | 33.33% | -3.26% | 1.52% | 14.17% |
| DOGE-USD | SAME_ASSET_REGIME | 35 | 17.14% | -21.33% | -9.86% | 13.85% | -28.71% | -42.95% | 5.00% | 14.87% | 27.88% | 37.14% | -2.16% | 8.16% | 32.01% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 31 | 12.90% | -22.50% | -14.72% | 1.59% | -29.24% | -42.96% | 4.26% | 10.18% | 28.83% | 32.26% | -3.68% | 1.48% | 14.81% |
| SOL-USD | ALL_MATCHES | 40 | 35.00% | -1.70% | 6.82% | 29.40% | -12.39% | -30.88% | 6.66% | 15.45% | 39.02% | 57.50% | 6.73% | 28.98% | 51.09% |
| SOL-USD | SAME_BTC_REGIME | 24 | 45.83% | -0.22% | 14.94% | 42.27% | -8.81% | -22.62% | 10.48% | 25.62% | 51.84% | 75.00% | 10.12% | 31.25% | 50.61% |
| SOL-USD | SAME_ASSET_REGIME | 31 | 41.94% | -0.39% | 8.97% | 35.32% | -10.44% | -23.64% | 9.84% | 18.31% | 44.45% | 67.74% | 8.91% | 31.58% | 50.78% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 21 | 47.62% | 0.00% | 14.56% | 45.24% | -8.00% | -19.37% | 10.51% | 25.47% | 55.01% | 76.19% | 11.32% | 30.91% | 42.97% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 13 | 100.00% | 25.70% | 0.00% | 53.16% | 92.31% | 32.98% | 78.05% |
| BTC-USD | HISTORICAL_BTC_BULL | 14 | 42.86% | -7.09% | -10.83% | 9.66% | 42.86% | -4.13% | 42.87% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 8 | 100.00% | 9.66% | -5.04% | 20.20% | 100.00% | 46.43% | 77.46% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 5 | 40.00% | -7.78% | -12.28% | 16.64% | 20.00% | -24.31% | 32.20% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 33 | 12.12% | -22.91% | -30.82% | 8.43% | 33.33% | -3.26% | 22.22% |
| DOGE-USD | HISTORICAL_BTC_BULL | 2 | 0.00% | -7.70% | -15.78% | 9.71% | 50.00% | -4.03% | 13.92% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 21.44% | -1.83% | 24.78% | 100.00% | 76.22% | 136.08% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 0.00% | -9.79% | -13.95% | 16.93% | 33.33% | -15.37% | 27.23% |
| SOL-USD | HISTORICAL_BTC_BEAR | 24 | 45.83% | -0.22% | -8.81% | 25.62% | 75.00% | 10.12% | 45.66% |
| SOL-USD | HISTORICAL_BTC_BULL | 10 | 0.00% | -7.40% | -25.96% | 2.26% | 10.00% | -4.91% | 2.26% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 75.00% | 5.03% | -9.15% | 11.55% | 100.00% | 42.24% | 68.81% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -16.77% | -29.03% | 11.14% | 0.00% | -35.08% | 11.14% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 26 | 88.46% | 11.06% | -2.98% | 32.07% | 88.46% | 33.21% | 76.98% |
| BTC-USD | HISTORICAL_ASSET_BULL | 6 | 16.67% | -18.39% | -20.49% | 8.15% | 16.67% | -7.51% | 8.15% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 4.40% | -3.37% | 24.00% | 66.67% | 21.58% | 57.57% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 60.00% | 5.95% | -11.70% | 32.20% | 20.00% | -24.31% | 32.20% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 35 | 17.14% | -21.33% | -28.71% | 14.87% | 37.14% | -2.16% | 24.84% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 0.00% | -15.85% | -28.31% | 0.00% | 100.00% | 4.56% | 12.69% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -25.24% | -38.58% | 7.55% | 0.00% | -3.26% | 7.55% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -8.75% | -14.04% | 12.94% | 0.00% | -9.16% | 12.94% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -9.79% | -21.74% | 17.47% | 0.00% | -15.37% | 17.47% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 41.94% | -0.39% | -10.44% | 18.31% | 67.74% | 8.91% | 49.90% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 0.00% | -18.82% | -28.28% | 0.42% | 33.33% | -5.68% | 0.42% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -6.61% | -31.16% | 1.10% | 0.00% | -3.73% | 1.10% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 5 | 20.00% | -6.02% | -30.84% | 4.03% | 20.00% | -4.13% | 4.03% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LRC-USD | 2018-09-19 | 89.40% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 95.69% | 0.00% | 178.55% | 42.97% | 0.00% | 178.55% |
| BTC-USD | KSM-USD | 2022-03-10 | 86.08% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.02% | -4.93% | 16.96% | 14.38% | -4.93% | 37.01% |
| BTC-USD | XLM-USD | 2020-01-07 | 85.30% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 45.24% | 0.00% | 62.58% | 53.88% | 0.00% | 78.05% |
| BTC-USD | ONE-USD | 2020-01-07 | 84.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.92% | 0.00% | 14.92% | -3.06% | -3.06% | 19.26% |
| BTC-USD | TRX-USD | 2020-01-07 | 84.55% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 22.02% | 0.00% | 33.95% | 32.98% | 0.00% | 48.70% |
| BTC-USD | EOS-USD | 2020-01-07 | 84.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.83% | 0.00% | 25.64% | 7.27% | 0.00% | 25.64% |
| BTC-USD | XLM-USD | 2019-10-04 | 84.36% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 49.02% | 0.00% | 53.16% | 5.97% | 0.00% | 80.44% |
| BTC-USD | ZEC-USD | 2020-01-07 | 84.05% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.42% | 0.00% | 34.23% | 46.00% | 0.00% | 56.81% |
| BTC-USD | MKR-USD | 2021-07-21 | 83.92% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 29.66% | -0.21% | 38.63% | 12.58% | -6.23% | 38.63% |
| BTC-USD | LTC-USD | 2020-01-06 | 83.76% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.04% | -3.57% | 20.47% | 9.84% | -3.57% | 20.47% |
| DOGE-USD | DASH-USD | 2022-02-20 | 88.29% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -29.45% | -33.95% | 2.32% | -19.38% | -36.58% | 2.32% |
| DOGE-USD | XTZ-USD | 2025-12-06 | 87.15% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.41% | -12.14% | 4.26% | -2.16% | -12.14% | 4.26% |
| DOGE-USD | VET-USD | 2022-02-27 | 87.09% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -25.78% | -31.87% | 0.17% | -1.26% | -32.57% | 0.17% |
| DOGE-USD | OMG-USD | 2022-02-25 | 87.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.91% | -29.18% | 11.92% | -11.26% | -32.25% | 11.92% |
| DOGE-USD | QTUM-USD | 2022-02-25 | 86.67% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.73% | -33.01% | 4.84% | 1.52% | -33.01% | 21.06% |
| DOGE-USD | CHZ-USD | 2022-02-24 | 86.65% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -19.17% | -28.71% | 5.97% | 11.61% | -28.71% | 22.22% |
| DOGE-USD | 1INCH-USD | 2022-02-22 | 86.49% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -31.62% | -42.19% | 0.00% | -20.09% | -42.19% | 0.00% |
| DOGE-USD | XLM-USD | 2019-09-29 | 86.48% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 39.92% | -5.54% | 39.92% | 24.54% | -5.54% | 74.65% |
| DOGE-USD | ENJ-USD | 2022-02-25 | 86.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -16.55% | -33.46% | 5.00% | 1.45% | -33.46% | 5.00% |
| DOGE-USD | ETH-USD | 2022-02-25 | 86.37% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -36.11% | -44.85% | 3.20% | -10.14% | -44.85% | 3.20% |
| SOL-USD | TRX-USD | 2018-09-19 | 78.81% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 55.01% | 0.00% | 55.01% | 32.25% | 0.00% | 58.38% |
| SOL-USD | QTUM-USD | 2018-09-19 | 78.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.21% | -3.68% | 15.25% | -0.51% | -17.60% | 15.25% |
| SOL-USD | XLM-USD | 2020-01-07 | 77.98% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 45.24% | 0.00% | 62.58% | 53.88% | 0.00% | 78.05% |
| SOL-USD | SOL-USD | 2025-12-04 | 77.97% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -7.51% | -10.44% | 9.16% | 6.95% | -10.44% | 10.43% |
| SOL-USD | LRC-USD | 2018-09-19 | 77.26% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 95.69% | 0.00% | 178.55% | 42.97% | 0.00% | 178.55% |
| SOL-USD | NEAR-USD | 2025-12-01 | 76.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.36% | -9.61% | 16.07% | 21.89% | -9.61% | 24.08% |
| SOL-USD | ENJ-USD | 2018-09-19 | 76.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | -16.11% | -19.37% | 5.11% | 93.16% | -38.09% | 93.16% |
| SOL-USD | APT-USD | 2024-09-06 | 76.59% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.00% | -12.27% | 2.27% | -34.09% | -35.00% | 2.27% |
| SOL-USD | OMG-USD | 2025-12-06 | 75.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.36% | -8.00% | 2.31% | 8.91% | -8.00% | 14.55% |
| SOL-USD | ONE-USD | 2020-04-16 | 75.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.89% | -24.91% | 11.93% | -10.01% | -24.91% | 11.93% |

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

Generato: 2026-07-11 18:59 UTC

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
| BTC | 64.273 $ | 0 | NEUTRALE / MISTO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | SPRING / TEST POSSIBILE | MEDIO | HOLD / ASPETTA ROTTURA RESISTENZA |
| SOL | 78,01 $ | 0 | NEUTRALE / MISTO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | RANGE / FASE NON CHIARA | BASSO | HOLD LEGGERO / ATTESA CONFERME |
| DOGE | 0.07510 $ | -3 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | COMPRESSIONE / TRIANGOLO POSSIBILE | MARKDOWN / DEBOLEZZA | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -4 | -2 | +3 | +2 | 0 | 0 | +1 | 0 |
| SOL | -4 | +2 | 0 | +2 | 0 | 0 | 0 | 0 |
| DOGE | -4 | 0 | +2 | +1 | 0 | 0 | -2 | -3 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.062 $ | 64.598 $ | 82.430 $ | 57.748 $ | 3,00% | 1,13% | -9,15% |
| SOL | 77,45 $ | 83,22 $ | 98,27 $ | 60,41 $ | 4,18% | 16,76% | -4,31% |
| DOGE | 0.07206 $ | 0.07923 $ | 0.11825 $ | 0.06961 $ | 3,78% | -12,61% | -17,29% |

## Lettura dettagliata

### BTC

- Prezzo: **64.273 $**
- Score classico: **0 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **HOLD / ASPETTA ROTTURA RESISTENZA**
- Volatilità tecnica locale: **MEDIO** — ATR14 3,00%; distanza supporto 1,93%; distanza resistenza 0,49%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+3** — RSI sano 54.4; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.14; volume ratio 0.54
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+1** — SPRING / TEST POSSIBILE. Ha bucato un minimo importante e ha recuperato: possibile spring, da confermare.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 54.39 |
| MACD histogram | 619.50099 |
| CMF20 | 0.144 |
| Volume ratio 20 | 0.54 |
| MA20 | 61.867 $ |
| MA50 | 65.144 $ |
| MA100 | 70.763 $ |
| MA200 | 73.987 $ |
| Pendenza MA50 20g | -9,65% |
| Pendenza MA200 60g | -10,24% |
| Bollinger width | 11,48% |
| Bollinger position | 0.83 |

### SOL

- Prezzo: **78,01 $**
- Score classico: **0 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**
- Volatilità tecnica locale: **BASSO** — ATR14 4,18%; distanza supporto 0,74%; distanza resistenza 6,66%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; breve termine sopra MA20/MA50; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **0** — RSI sano 54.4; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.08; volume ratio 0.54
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Doji / indecisione
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 54.42 |
| MACD histogram | 0.14924 |
| CMF20 | 0.084 |
| Volume ratio 20 | 0.54 |
| MA20 | 75,85 $ |
| MA50 | 74,56 $ |
| MA100 | 80,40 $ |
| MA200 | 91,98 $ |
| Pendenza MA50 20g | -6,50% |
| Pendenza MA200 60g | -18,58% |
| Bollinger width | 25,40% |
| Bollinger position | 0.61 |

### DOGE

- Prezzo: **0.07510 $**
- Score classico: **-3 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 3,78%; distanza supporto 4,26%; distanza resistenza 5,46%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; medie daily allineate ribassiste; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **+2** — RSI neutrale 41.2; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+1** — OBV sopra media; CMF neutrale 0.04; volume ratio 0.61
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 41.16 |
| MACD histogram | 0.00059 |
| CMF20 | 0.040 |
| Volume ratio 20 | 0.61 |
| MA20 | 0.07523 $ |
| MA50 | 0.08463 $ |
| MA100 | 0.09313 $ |
| MA200 | 0.10129 $ |
| Pendenza MA50 20g | -13,83% |
| Pendenza MA200 60g | -16,60% |
| Bollinger width | 13,98% |
| Bollinger position | 0.49 |

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

Generato: 2026-07-11 19:00 UTC

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
| BTC | 64.273 $ | Doppio minimo | CANDIDATO | rialzista | n/a | 76.748 $ | n/a | 4,63% | Fib 23,6% TESTATO (0) @ 63.658 $ | NEL RANGE | 62.553 $ |
| SOL | 78,01 $ | Doppio minimo | CONFERMATO RECENTE | rialzista | 2026-07-01 | 91,46 $ | 13,34% | n/a | Fib 23,6% TESTATO (0) @ 78,29 $ | NEL RANGE | 76,82 $ |
| DOGE | 0.07510 $ | Triplo massimo | MATURO | ribassista | 2026-06-24 | 0.05847 $ | 15,26% | n/a | Fib 23,6% NON ATTIVO (0) @ 0.08109 $ | NEL RANGE | 0.06961 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-05 -> 2026-07-01**
- Età formazione: **10 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **67.248 $**
- Target teorico: **76.748 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **4,63%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 63.658 $** — Swing DOWN 2026-05-06 82.792 -> 2026-07-01 57.748; livello più vicino 23.6% a 63.658; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **65.903 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 57.748 tra 2026-06-05 e 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **62.553 $**
- Resistenza: **65.544 $**
- Breakout 60g: **82.430 $**
- Breakdown 60g: **57.748 $**
- RSI14: **54.36**
- ATR14: **3,00%**
- Volume ratio 20g: **0.55**
- Rendimento 30g: **+1,12%**
- Rendimento 90g: **-9,16%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CANDIDATO | 0 | rialzista | 67.248 $ | n/a | n/a | 76.748 $ | n/a | 4,63% | 65.903 $ | Due minimi simili a 59.109 $ e 57.748 $. Neckline circa 67.248 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 10 giorni. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | TARGET RAGGIUNTO | 0 | ribassista | 74.959 $ | 2026-05-27 | 45g | 71.596 $ | 317,82% | n/a | 76.458 $ | Due massimi simili a 78.321 $ e 77.991 $. Neckline circa 74.959 $. Breakout neckline: 2026-05-27 (45 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.596 $; progresso: 317,82%; prezzo sotto neckline. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CONFERMATO RECENTE** (+2)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-06 -> 2026-06-25**
- Età formazione: **16 giorni**
- Breakout pattern: **2026-07-01**
- Età breakout: **10 giorni**
- Neckline: **75,94 $**
- Target teorico: **91,46 $**
- Progresso verso target: **13,34%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 78,29 $** — Swing UP 2026-06-06 60,41 -> 2026-07-04 83,81; livello più vicino 23.6% a 78,29; stato TESTATO; confluenza: neckline rialzista.
- Invalidazione: **74,42 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (10 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 91,46; progresso corrente: 13,34%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Doji / indecisione**
- Stato prezzo: **NEL RANGE**
- Supporto: **76,82 $**
- Resistenza: **83,81 $**
- Breakout 60g: **98,27 $**
- Breakdown 60g: **60,41 $**
- RSI14: **54.39**
- ATR14: **4,18%**
- Volume ratio 20g: **0.54**
- Rendimento 30g: **+16,74%**
- Rendimento 90g: **-4,32%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CONFERMATO RECENTE | +2 | rialzista | 75,94 $ | 2026-07-01 | 10g | 91,46 $ | 13,34% | n/a | 74,42 $ | Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (10 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 91,46; progresso corrente: 13,34%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 60,41 $ | n/a | n/a | 33,04 $ | n/a | 29,12% | 61,62 $ | Due massimi simili a 87,79 $ e 83,81 $. Neckline circa 60,41 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 7 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 98,27 $ | n/a | n/a | 114,91 $ | n/a | 25,97% | 96,30 $ | Due minimi simili a 81,63 $ e 81,69 $. Neckline circa 98,27 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 49 giorni. |
| Testa e spalle | TARGET RAGGIUNTO | 0 | ribassista | 82,57 $ | 2026-05-28 | 44g | 66,88 $ | 29,07% | n/a | 84,22 $ | Spalla sinistra 88,05 $, testa 98,27 $, spalla destra 87,79 $. Neckline circa 82,57 $. Breakout neckline: 2026-05-28 (44 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 66,88 $; progresso: 29,07%; prezzo sotto neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **MATURO** (-1)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-03-25 -> 2026-06-12**
- Età formazione: **29 giorni**
- Breakout pattern: **2026-06-24**
- Età breakout: **17 giorni**
- Neckline: **0.07809 $**
- Target teorico: **0.05847 $**
- Progresso verso target: **15,26%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08109 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-06-30 0.06961; livello più vicino 23.6% a 0.08109; stato NON ATTIVO; confluenza: resistenza tecnica, invalidazione ribassista.
- Invalidazione: **0.07966 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (17 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 15,26%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.06961 $**
- Resistenza: **0.07923 $**
- Breakout 60g: **0.11825 $**
- Breakdown 60g: **0.06961 $**
- RSI14: **41.06**
- ATR14: **3,78%**
- Volume ratio 20g: **0.61**
- Rendimento 30g: **-12,65%**
- Rendimento 90g: **-17,32%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 17g | 0.05847 $ | 15,26% | n/a | 0.07966 $ | Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (17 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 15,26%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 17g | 0.06035 $ | 16,88% | n/a | 0.07966 $ | Due massimi simili a 0.09584 $ e 0.09169 $. Neckline circa 0.07809 $. Breakout neckline: 2026-06-24 (17 giorni fa). Stato: MATURO. Target teorico: 0.06035 $; progresso: 16,88%; prezzo sotto neckline. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.11825 $ | n/a | n/a | 0.14377 $ | n/a | 57,46% | 0.11589 $ | Due minimi simili a 0.09274 $ e 0.09675 $. Neckline circa 0.11825 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 44 giorni. |

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

Generato: 2026-07-11 18:59 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-11**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2022-12-26**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **78,01 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+65,20%**
- Aderenza live principale: **+58,19%**
- Errore medio live principale: **20,90%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **35**
- Osservazioni inclusive dal bottom: **36**
- Osservazioni da inizio programma/scanner: **9**
- Errore assoluto medio dal bottom: **9,74%**
- Errore assoluto medio da inizio programma: **20,90%**
- Gap firmato medio ultimi 7 giorni: **+19,63%**
- Errore assoluto medio ultimi 7 giorni: **19,63%**
- Gap ultimo giorno: **+17,04%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+17,04%**
- Gap firmato medio 7g: **+19,63%**
- Errore assoluto medio 7g: **19,63%**
- Variazione recente gap: **-0,52%**
- Stato gap: **IN DEVIAZIONE SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato con distacco quasi stabile**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 26 | 2026-07-02 | 2022-12-17 | 80,64 $ | 66,16 $ | +21,89% | prima programma |
| 27 | 2026-07-03 | 2022-12-18 | 82,28 $ | 66,01 $ | +24,64% | da inizio programma |
| 28 | 2026-07-04 | 2022-12-19 | 81,65 $ | 64,76 $ | +26,08% | da inizio programma |
| 29 | 2026-07-05 | 2022-12-20 | 81,42 $ | 66,60 $ | +22,26% | da inizio programma |
| 30 | 2026-07-06 | 2022-12-21 | 81,92 $ | 66,25 $ | +23,65% | da inizio programma |
| 31 | 2026-07-07 | 2022-12-22 | 80,65 $ | 66,30 $ | +21,64% | da inizio programma |
| 32 | 2026-07-08 | 2022-12-23 | 77,79 $ | 66,17 $ | +17,56% | da inizio programma |
| 33 | 2026-07-09 | 2022-12-24 | 78,05 $ | 66,37 $ | +17,60% | da inizio programma |
| 34 | 2026-07-10 | 2022-12-25 | 78,07 $ | 66,34 $ | +17,67% | da inizio programma |
| 35 | 2026-07-11 | 2022-12-26 | 78,01 $ | 66,65 $ | +17,04% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-18 | 65,74 $ | 76,94 $ | 76,29 $ / 78,01 $ | no | n/a | n/a | n/a |
| 14g | 2026-07-25 | 67,74 $ | 79,29 $ | 76,29 $ / 79,29 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-01 | 83,39 $ | 97,60 $ | 76,29 $ / 97,60 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-08 | 90,34 $ | 105,74 $ | 76,29 $ / 105,74 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-15 | 89,97 $ | 105,31 $ | 76,29 $ / 109,61 $ | no | n/a | n/a | n/a |
| 42g | 2026-08-22 | 89,66 $ | 104,94 $ | 76,29 $ / 109,61 $ | no | n/a | n/a | n/a |
| 49g | 2026-08-29 | 85,91 $ | 100,55 $ | 76,29 $ / 109,61 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-05 | 97,81 $ | 114,48 $ | 76,29 $ / 114,48 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-12 | 92,66 $ | 108,45 $ | 76,29 $ / 114,48 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-19 | 88,36 $ | 103,41 $ | 76,29 $ / 114,48 $ | no | n/a | n/a | n/a |
| 77g | 2026-09-26 | 95,32 $ | 111,56 $ | 76,29 $ / 114,48 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-03 | 109,38 $ | 128,02 $ | 76,29 $ / 129,27 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-10 | 106,91 $ | 125,13 $ | 76,29 $ / 130,64 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-17 | 109,47 $ | 128,13 $ | 76,29 $ / 131,30 $ | no | n/a | n/a | n/a |
| 105g | 2026-10-24 | 116,81 $ | 136,72 $ | 76,29 $ / 136,72 $ | no | n/a | n/a | n/a |
| 112g | 2026-10-31 | 115,99 $ | 135,76 $ | 76,29 $ / 140,56 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-07 | 108,43 $ | 126,91 $ | 76,29 $ / 140,56 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-14 | 110,66 $ | 129,52 $ | 76,29 $ / 140,56 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 0 | n/a | n/a | n/a |
| 14g | 0 | n/a | n/a | n/a |
| 21g | 0 | n/a | n/a | n/a |
| 28g | 0 | n/a | n/a | n/a |
| 35g | 0 | n/a | n/a | n/a |
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

Generato: 2026-07-11 19:00 UTC

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.321 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0021% | n/a | 3,73 | +0,42% | 0 $ | 0 $ |
| SOL | 78,16 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0108% | n/a | 1,44 | +1,88% | 0 $ | 0 $ |
| DOGE | 0.07514 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0082% | n/a | 1,81 | +3,01% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0030% | 124,63 mln $ | 5,74 | +3,85% |
| BTC | Bitget | OK | +0,0034% | 2,21 mld $ | 8,45 | -18,26% |
| BTC | Kucoin | OK | +0,0006% | 1,93 mld $ | 0,12 | +5,87% |
| SOL | Kraken | OK | +0,0385% | 19,63 mln $ | 1,93 | +1,59% |
| SOL | Bitget | OK | +0,0100% | 322,65 mln $ | 12,01 | -2,69% |
| SOL | Kucoin | OK | +0,0100% | 334,71 mln $ | 0,91 | +7,47% |
| DOGE | Kraken | OK | -0,0012% | 2,92 mln $ | 1,73 | +1,33% |
| DOGE | Bitget | OK | +0,0100% | 82,14 mln $ | 3,04 | +3,55% |
| DOGE | Kucoin | OK | +0,0069% | 99,49 mln $ | 4,49 | +3,55% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+1,62**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 1.
- Flusso taker/order book: **+1,00**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Resistenza vicina con acquisti aggressivi: breakout più credibile, ma serve chiusura sopra il livello.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

### SOL

- Score grezzo exchange: **+1,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+1,00**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso. Confluenza tecnica dichiarata: neckline rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

### DOGE

- Score grezzo exchange: **+1,38**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 0.
- Flusso taker/order book: **+1,00**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta. Confluenza tecnica dichiarata: resistenza tecnica, invalidazione ribassista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +72,50% | +7,63% | 0 | n/a | RACCOLTA DATI | 0,00 | +72,50% | +7,63% |
| SOL | +35,00% | -1,70% | 0 | n/a | RACCOLTA DATI | 0,00 | +35,00% | -1,70% |
| DOGE | +15,00% | -20,25% | 0 | n/a | RACCOLTA DATI | 0,00 | +15,00% | -20,25% |

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
Storage persistente: **OK** — ultimo asset: exchange_state_A.tar.gz.
<!-- EXCHANGE_MICROSTRUCTURE_END -->

</details>
<!-- COMPACT_SECTION_END:exchange_microstructure -->

<!-- COMPACT_SECTION_START:exchange_signal_tracker -->
<details>
<summary><strong>🧠 Accuratezza segnali exchange</strong></summary>

<!-- EXCHANGE_SIGNAL_TRACKER_START -->
# Accuratezza dati exchange e microstruttura

Generato: 2026-07-11 19:00 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **0**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-11 | BTC | 64.152,13 | TRANSITION_PRE_V2.1.3 | ESCLUSA | 0 | 0 | -1,50 | BASSA | 0,06 | +1,72% | +2,84% |
| 2026-07-11 | DOGE | 0.07422 | TRANSITION_PRE_V2.1.3 | ESCLUSA | 0 | 0 | 1,38 | BASSA | 1,14 | -7,68% | +4,98% |
| 2026-07-11 | SOL | 77,77 | TRANSITION_PRE_V2.1.3 | ESCLUSA | 0 | 0 | -3,00 | BASSA | 0,41 | +17,81% | -9,72% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 3g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 3g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 3g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
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
| BTC | 64.273 $ | +0.0065% | +2.06% | 1.44 | Rischio sotto | 4/5 |
| SOL | 78,01 $ | +0.0100% | -22.94% | 2.14 | Rischio sotto | 2/5 |
| DOGE | 0.07510 $ | +0.0100% | -0.01% | 2.34 | Rischio sotto | 2/5 |

## Come usarla insieme al frattale

- Frattale ribassista + futures con rischio sotto = prudenza alta.
- Frattale rialzista + futures con rischio sopra = segnale più interessante.
- Frattale e futures opposti = situazione sporca, meglio non forzare.
- Per posizioni a leva, il futures report serve soprattutto a capire se può arrivare una pulizia violenta prima dei 30 giorni.

<!-- LIQUIDATION_SUMMARY_END -->

</details>
<!-- COMPACT_SECTION_END:liquidations -->

<!-- COMPACT_SECTION_START:technical_structure -->
<details>
<summary><strong>🧱 Struttura tecnica completa e Fibonacci</strong></summary>

<!-- TECHNICAL_STRUCTURE_START -->
# Report struttura tecnica

Generato: 2026-07-11 19:00 UTC

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

| Asset   | Prezzo   |   Punteggio | Verdetto         | Trend            | Momentum       | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista                  | Pattern ribassista                | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-----------------|:-----------------|:---------------|:------------------------------------------------------|----------------:|:---------------|:-----------------------------------|:----------------------------------|:-----------|:-------------|
| BTC | 64.273 $ | 1 | NEUTRALE / MISTO | Trend ribassista | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | 0 | 0 / TESTATO | Doppio minimo / CANDIDATO | Doppio massimo / TARGET RAGGIUNTO | 57.748 | 65.544 |
| SOL | 78,01 $ | 2 | NEUTRALE / MISTO | Trend misto | Momentum misto | Volatilità in espansione | +2 | 0 / TESTATO | Doppio minimo / CONFERMATO RECENTE | Doppio massimo / CANDIDATO | 64,42 | 83,81 |
| DOGE | 0.07510 $ | -4 | DEBOLE | Trend ribassista | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | -1 | 0 / NON ATTIVO | Triplo minimo / CANDIDATO | Triplo massimo / MATURO | 0.06961 | 0.07923 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo      | Triplo minimo   | Adam/Eve Bottom                          | Doppio massimo   | Triplo massimo   | Adam/Eve Top                        |   Punteggio pattern |
|:--------|:-------------------|:----------------|:-----------------------------------------|:-----------------|:-----------------|:------------------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Eve and Adam Top — TARGET RAGGIUNTO | 0 |
| SOL | CONFERMATO RECENTE | CANDIDATO | Adam and Eve Bottom — CONFERMATO RECENTE | CANDIDATO | CANDIDATO | Eve and Adam Top — CANDIDATO | 2 |
| DOGE | ASSENTE | CANDIDATO | Adam and Eve Bottom — CANDIDATO | ASSENTE | MATURO | Eve and Adam Top — MATURO | -1 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 54.36 | 618.929 | 61.867 | 65.144 | 73.987 | -9,28% | -10,07% | 1,15% | -13,71% |
| SOL | 54.39 | 0.1486 | 75,85 | 74,56 | 91,98 | -6,22% | -18,21% | 16,87% | -9,98% |
| DOGE | 41.06 | 0.00059 | 0.07523 | 0.08463 | 0.10129 | -13,38% | -16,31% | -12,64% | -20,21% |

## Dettaglio asset

### BTC

- Prezzo: **64.273 $**
- Punteggio tecnico: **1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 5.808e+04 -> 5.775e+04. Ultimi massimi: 6.725e+04 -> 6.554e+04.
- Divergenza: **Divergenza rialzista RSI** (2)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 54.4.
- Fibonacci automatico: **TESTATO** (0)
  - Swing DOWN 2026-05-06 82.792 -> 2026-07-01 57.748; livello più vicino 23.6% a 63.658; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (TARGET RAGGIUNTO, 0).
- Supporto più vicino: **57.748**
- Resistenza più vicina: **65.544**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 57.748 tra 2026-06-05 e 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 4,63%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 57.748 dal 2026-06-05 al 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 4,63%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 57.748 dal 2026-06-05 al 2026-07-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 4,63%; prezzo sotto neckline.
- Doppio massimo: **TARGET RAGGIUNTO** (0)
  - Due massimi simili vicino a 79.488 tra 2026-04-27 e 2026-05-26. Neckline ribassista stimata: 74.959. Breakout neckline: 2026-05-27 (45 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 70.429; progresso corrente: 235,90%. Relazione prezzo/neckline: sotto neckline.
  - neckline 74.959; target 70.429; breakout 2026-05-27 (45g); progresso 235,90%; prezzo sotto neckline.
- Triplo massimo: **TARGET RAGGIUNTO** (0)
  - Tre massimi simili vicino a 79.468 dal 2026-04-17 al 2026-05-26. Neckline ribassista stimata: 74.959. Breakout neckline: 2026-05-27 (45 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 70.449; progresso corrente: 236,96%. Relazione prezzo/neckline: sotto neckline.
  - neckline 74.959; target 70.449; breakout 2026-05-27 (45g); progresso 236,96%; prezzo sotto neckline.
- Eve and Adam Top: **TARGET RAGGIUNTO** (0)
  - Pattern Eve and Adam Top vicino a 82.792 dal 2026-04-22 al 2026-05-06. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 74.959. Breakout neckline: 2026-05-27 (45 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 67.125; progresso corrente: 136,41%. Relazione prezzo/neckline: sotto neckline.
  - neckline 74.959; target 67.125; breakout 2026-05-27 (45g); progresso 136,41%; prezzo sotto neckline.

### SOL

- Prezzo: **78,01 $**
- Punteggio tecnico: **2 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum misto** (-1)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 67.92 -> 64.42. Ultimi massimi: 74.89 -> 83.81.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 46,48%. Fase non abbastanza chiara.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-06-06 60,41 -> 2026-07-04 83,81; livello più vicino 23.6% a 78,29; stato TESTATO; confluenza: neckline rialzista.
- Punteggio pattern: **+2**
  - rialzista dominante: Doppio minimo (CONFERMATO RECENTE, +2); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **64,42**
- Resistenza più vicina: **83,81**

Pattern classici e ciclo di vita:

- Doppio minimo: **CONFERMATO RECENTE** (+2)
  - Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (10 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 91,46; progresso corrente: 13,34%. Relazione prezzo/neckline: sopra neckline.
  - neckline 75,94; target 91,46; breakout 2026-07-01 (10g); progresso 13,34%; prezzo sopra neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 81,41 dal 2026-04-12 al 2026-05-23. Neckline stimata: 98,27. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 49 giorni.
  - neckline 98,27; target 115,13; distanza dalla neckline 25,97%; prezzo sotto neckline.
- Adam and Eve Bottom: **CONFERMATO RECENTE** (+2)
  - Pattern Adam and Eve Bottom vicino a 60,41 dal 2026-06-06 al 2026-06-25. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (10 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 91,46; progresso corrente: 13,34%. Relazione prezzo/neckline: sopra neckline.
  - neckline 75,94; target 91,46; breakout 2026-07-01 (10g); progresso 13,34%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 87,79 tra 2026-05-21 e 2026-07-04. Neckline ribassista stimata: 60,41. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 60,41; target 33,04; distanza dalla neckline 29,12%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 88,05 dal 2026-04-27 al 2026-07-04. Neckline ribassista stimata: 60,41. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 60,41; target 32,78; distanza dalla neckline 29,12%; prezzo sopra neckline.
- Eve and Adam Top: **CANDIDATO** (0)
  - Pattern Eve and Adam Top vicino a 87,79 dal 2026-05-21 al 2026-07-04. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 60,41. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 60,41; target 33,04; distanza dalla neckline 29,12%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.07510 $**
- Punteggio tecnico: **-4 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 0.07809 -> 0.06961. Ultimi massimi: 0.09169 -> 0.07923.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 41.1.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-06-30 0.06961; livello più vicino 23.6% a 0.08109; stato NON ATTIVO; confluenza: resistenza tecnica, invalidazione ribassista.
- Punteggio pattern: **-1**
  - rialzista dominante: Triplo minimo (CANDIDATO, 0); ribassista dominante: Triplo massimo (MATURO, -1).
- Supporto più vicino: **0.06961**
- Resistenza più vicina: **0.07923**

Pattern classici e ciclo di vita:

- Doppio minimo: **ASSENTE** (0)
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 0.09274 dal 2026-04-19 al 2026-05-28. Neckline stimata: 0.11825. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 44 giorni.
  - neckline 0.11825; target 0.14377; distanza dalla neckline 57,46%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.09274 dal 2026-04-19 al 2026-05-28. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.11825. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 44 giorni.
  - neckline 0.11825; target 0.14377; distanza dalla neckline 57,46%; prezzo sotto neckline.
- Doppio massimo: **ASSENTE** (0)
- Triplo massimo: **MATURO** (-1)
  - Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (17 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 15,26%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.05847; breakout 2026-06-24 (17g); progresso 15,26%; prezzo sotto neckline.
- Eve and Adam Top: **MATURO** (-1)
  - Pattern Eve and Adam Top vicino a 0.09584 dal 2026-04-07 al 2026-06-12. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (17 giorni fa). Stato: MATURO. Target teorico: 0.06035; progresso corrente: 16,88%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.06035; breakout 2026-06-24 (17g); progresso 16,88%; prezzo sotto neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                                   |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:---------------------------------------------|--------:|
| BTC | DOWN 2026-05-06 -> 2026-07-01 | 63.658 | 67.315 | 70.270 | 73.225 | 77.433 | 23.6% / 63.658 | TESTATO | nessuna confluenza indipendente | 0 |
| SOL | UP 2026-06-06 -> 2026-07-04 | 78,29 | 74,87 | 72,11 | 69,35 | 65,42 | 23.6% / 78,29 | TESTATO | neckline rialzista | 0 |
| DOGE | DOWN 2026-05-14 -> 2026-06-30 | 0.08109 | 0.08819 | 0.09393 | 0.09967 | 0.10785 | 23.6% / 0.08109 | NON ATTIVO | resistenza tecnica, invalidazione ribassista | 0 |

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

- **BTC**: 0/30 previsioni controllate su 9 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 0/30 previsioni controllate su 9 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 0/30 previsioni controllate su 9 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 9 | 0 | 0/30 [░░░░░░░░░░] | 9 | RACCOLTA DATI | 2026-08-02 / tra 22 giorni |
| SOL | 9 | 0 | 0/30 [░░░░░░░░░░] | 9 | RACCOLTA DATI | 2026-08-02 / tra 22 giorni |
| DOGE | 9 | 0 | 0/30 [░░░░░░░░░░] | 9 | RACCOLTA DATI | 2026-08-02 / tra 22 giorni |

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

Generato: 2026-07-11 19:00 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 64.273 $          | 64.273 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.07510 $         | 0.07510 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 78,01 $           | 78,01 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 64.273 $          | 64.273 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 78,01 $           | 78,01 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.07510 $         | 0.07510 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 64.273 $          | 64.273 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 78,01 $           | 78,01 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.07510 $         | 0.07510 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 64.273 $          | 64.273 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 78,01 $           | 78,01 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.07510 $         | 0.07510 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 64.273 $          | 64.273 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 78,01 $           | 78,01 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.07510 $         | 0.07510 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 64.273 $          | 64.321 $        | +0,0742%     |
| Exchange Microstructure | SOL     | price             | OK      | 78,01 $           | 78,16 $         | +0,1897%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.07510 $         | 0.07514 $       | +0,0533%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 78,01 $           | 78,01 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 78,01 $           | 78,01 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 78,01 $           | 78,01 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 78,01 $           | 78,01 $         | +0,0000%     |

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

Il workflow è tecnicamente coerente nei controlli disponibili.
<!-- DATA_QUALITY_COHERENCE_END -->

</details>
<!-- COMPACT_SECTION_END:data_quality -->
