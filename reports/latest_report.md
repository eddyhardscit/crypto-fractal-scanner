<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-09-27 05:32 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 0 | NEUTRALE / COSTRUTTIVO | HOLD / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | +3 | NEUTRALE / COSTRUTTIVO | HOLD / TRANCHE PICCOLE, NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +2 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **0**, spot = **HOLD / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **+3**, spot = **HOLD / TRANCHE PICCOLE, NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+2**, spot = **STAI ALLA FINESTRA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **0**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MEDIO / ALTO**
- Conferme: Prima resistenza sopra 87.364; conferma del doppio minimo sopra 82.262.
- Invalidazioni: Sotto 74.945 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+3**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / TRANCHE PICCOLE, NO LEVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 107,12; milestone analogiche 138,18 / 148,67, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 114,65 / 96,23 / 62,19.

### DOGE

- Global Confluence: **+2**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **STAI ALLA FINESTRA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.10528 migliora; sopra 0.07997 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.07841 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 1; EMA200 circa 111,31 $; upside verso EMA200 -7,76%. Non autorizza leva e non aggiunge punti automatici.
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

Generato: 2026-09-27 05:32 UTC

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

Segnali totali salvati: **222**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-27 | BTC | 84.404,98 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-27 | DOGE | 0.09592 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-27 | SOL | 120,66 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-26 | BTC | 83.890,58 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-26 | DOGE | 0.09735 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-26 | SOL | 120,35 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-25 | BTC | 84.066,00 | +3 | +1 | +1 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-25 | DOGE | 0.09907 | +4 | -1 | -1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-25 | SOL | 122,07 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-23 | BTC | 86.710,28 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-23 | DOGE | 0.10219 | +2 | -2 | -2 | 0 | +3 | +1 | 0 | STAI ALLA FINESTRA |
| 2026-09-23 | SOL | 118,88 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 74 | 73 | 72 | 71 | 70 | 69 | 69 | 65 | 58 | 49 | 34 | 21 |
| SOL | 74 | 73 | 72 | 71 | 70 | 69 | 69 | 65 | 58 | 49 | 34 | 21 |
| DOGE | 74 | 73 | 72 | 71 | 70 | 69 | 69 | 65 | 58 | 49 | 34 | 21 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-30 | 60g | 2026-09-28 | domani |
| SOL | 2026-07-30 | 60g | 2026-09-28 | domani |
| DOGE | 2026-07-30 | 60g | 2026-09-28 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 69 | 50,72% | +0,36% | +0,35% | UTILE |
| BTC | 2g | 69 | 50,72% | +0,62% | +0,55% | UTILE |
| BTC | 3g | 68 | 45,59% | +0,81% | +0,71% | UTILE |
| BTC | 5g | 67 | 44,78% | +1,82% | +1,63% | UTILE |
| BTC | 7g | 66 | 54,55% | +2,63% | +2,47% | UTILE |
| BTC | 10g | 66 | 62,12% | +3,62% | +3,48% | UTILE |
| BTC | 14g | 62 | 59,68% | +4,89% | +4,83% | UTILE |
| BTC | 21g | 55 | 69,09% | +8,35% | +8,23% | PRIMA CALIBRAZIONE |
| BTC | 30g | 46 | 93,48% | +14,14% | +13,20% | PRIMA CALIBRAZIONE |
| BTC | 45g | 32 | 90,62% | +23,93% | +19,80% | PRIMA CALIBRAZIONE |
| BTC | 60g | 19 | 84,21% | +25,50% | +17,59% | FEEDBACK RAPIDO |
| SOL | 1g | 65 | 52,31% | +0,46% | +0,37% | UTILE |
| SOL | 2g | 64 | 48,44% | +1,18% | +1,07% | UTILE |
| SOL | 3g | 63 | 55,56% | +1,97% | +1,83% | UTILE |
| SOL | 5g | 62 | 58,06% | +3,34% | +3,25% | UTILE |
| SOL | 7g | 61 | 62,30% | +4,75% | +4,83% | UTILE |
| SOL | 10g | 61 | 67,21% | +6,78% | +6,90% | UTILE |
| SOL | 14g | 58 | 74,14% | +9,21% | +9,84% | PRIMA CALIBRAZIONE |
| SOL | 21g | 51 | 80,39% | +14,77% | +14,07% | PRIMA CALIBRAZIONE |
| SOL | 30g | 42 | 76,19% | +22,89% | +18,18% | PRIMA CALIBRAZIONE |
| SOL | 45g | 27 | 59,26% | +39,52% | +11,02% | FEEDBACK RAPIDO |
| SOL | 60g | 15 | 40,00% | +38,30% | -4,08% | FEEDBACK RAPIDO |
| DOGE | 1g | 69 | 43,48% | +0,29% | -0,08% | UTILE |
| DOGE | 2g | 68 | 44,12% | +0,62% | -0,10% | UTILE |
| DOGE | 3g | 67 | 40,30% | +1,04% | +0,09% | UTILE |
| DOGE | 5g | 66 | 43,94% | +2,16% | +0,27% | UTILE |
| DOGE | 7g | 65 | 50,77% | +3,05% | +0,65% | UTILE |
| DOGE | 10g | 65 | 46,15% | +3,76% | +0,55% | UTILE |
| DOGE | 14g | 61 | 62,30% | +5,13% | +4,82% | UTILE |
| DOGE | 21g | 54 | 66,67% | +8,27% | +4,55% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 46 | 80,43% | +13,19% | +7,78% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 32 | 37,50% | +23,62% | -1,37% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 20 | 15,00% | +23,94% | -13,40% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 69 | 50,72% | +0,36% | +0,35% | -0,19% | +0,89% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 73 | 52,05% | +0,35% | +0,33% | -0,18% | +0,85% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 73 | 52,05% | +0,35% | +0,33% | -0,18% | +0,85% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 66 | 40,91% | +0,36% | +0,05% | -0,11% | +0,86% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 29 | 37,93% | +0,73% | +0,06% | -0,13% | +1,26% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,24% | -0,24% | -0,87% | +0,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 69 | 50,72% | +0,62% | +0,55% | -0,14% | +1,31% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 72 | 52,78% | +0,70% | +0,70% | -0,05% | +1,39% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 72 | 52,78% | +0,70% | +0,70% | -0,05% | +1,39% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 65 | 43,08% | +0,65% | +0,02% | +0,06% | +1,34% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 29 | 41,38% | +1,20% | +0,02% | +0,19% | +1,90% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,04% | -0,04% | -0,90% | +1,02% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 68 | 45,59% | +0,81% | +0,71% | -1,21% | +2,55% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 71 | 52,11% | +1,05% | +1,05% | -1,18% | +2,73% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 71 | 52,11% | +1,05% | +1,05% | -1,18% | +2,73% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 64 | 35,94% | +1,11% | -0,21% | -1,10% | +2,79% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 29 | 37,93% | +1,95% | -0,51% | -0,85% | +3,41% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 67 | 44,78% | +1,82% | +1,63% | -1,76% | +4,16% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 70 | 50,00% | +2,02% | +2,02% | -1,73% | +4,40% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 70 | 50,00% | +2,02% | +2,02% | -1,73% | +4,40% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 63 | 41,27% | +1,95% | -0,74% | -1,65% | +4,39% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 28 | 42,86% | +4,36% | -2,17% | -1,11% | +6,49% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 16,67% | -0,95% | -0,95% | -2,27% | +2,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 66 | 54,55% | +2,63% | +2,47% | -2,06% | +5,40% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 69 | 59,42% | +2,88% | +2,88% | -2,04% | +5,62% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 69 | 59,42% | +2,88% | +2,88% | -2,04% | +5,62% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 62 | 43,55% | +2,98% | -1,13% | -1,96% | +5,69% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 28 | 39,29% | +5,77% | -4,00% | -1,37% | +8,77% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 66 | 62,12% | +3,62% | +3,48% | -2,36% | +6,64% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 69 | 65,22% | +3,74% | +3,74% | -2,35% | +6,82% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 69 | 65,22% | +3,74% | +3,74% | -2,35% | +6,82% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 62 | 50,00% | +3,92% | -0,37% | -2,28% | +7,01% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 28 | 42,86% | +5,84% | -4,46% | -1,59% | +9,49% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 62 | 59,68% | +4,89% | +4,83% | -2,65% | +8,47% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 65 | 60,00% | +4,97% | +4,97% | -2,63% | +8,57% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 65 | 60,00% | +4,97% | +4,97% | -2,63% | +8,57% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 60 | 56,67% | +5,49% | +1,45% | -2,48% | +9,14% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 24 | 29,17% | +4,78% | -3,41% | -1,84% | +9,24% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 55 | 69,09% | +8,35% | +8,23% | -2,71% | +12,22% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 58 | 74,14% | +8,27% | +8,27% | -2,70% | +12,17% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 58 | 74,14% | +8,27% | +8,27% | -2,70% | +12,17% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 53 | 50,94% | +8,90% | +0,31% | -2,53% | +12,86% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 24 | 54,17% | +8,85% | -4,04% | -2,32% | +12,73% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 46 | 93,48% | +14,14% | +13,20% | -2,47% | +18,21% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 49 | 89,80% | +13,99% | +13,99% | -2,47% | +18,21% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 49 | 89,80% | +13,99% | +13,99% | -2,47% | +18,21% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 44 | 52,27% | +14,13% | -1,01% | -2,24% | +18,60% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 17 | 52,94% | +15,73% | -5,99% | -1,89% | +20,13% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +5,40% | +5,40% | -4,01% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 32 | 90,62% | +23,93% | +19,80% | -2,96% | +28,59% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 34 | 100,00% | +23,88% | +23,88% | -3,00% | +28,48% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 34 | 100,00% | +23,88% | +23,88% | -3,00% | +28,48% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 30 | 100,00% | +24,25% | +24,25% | -2,80% | +28,91% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 29 | 41,38% | +24,37% | -2,10% | -2,74% | +29,02% | FEEDBACK RAPIDO |
| BTC | 45g | Classic technical | CALIBRABILE | 4 | 0,00% | +21,70% | -21,70% | -1,55% | +30,01% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 19 | 84,21% | +25,50% | +17,59% | -3,20% | +30,61% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 21 | 100,00% | +25,40% | +25,40% | -3,24% | +30,62% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 21 | 100,00% | +25,40% | +25,40% | -3,24% | +30,62% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 17 | 100,00% | +26,05% | +26,05% | -2,95% | +31,65% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 17 | 29,41% | +25,58% | -12,13% | -2,88% | +31,21% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 2 | 0,00% | +32,21% | -32,21% | -2,23% | +37,27% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 69 | 43,48% | +0,29% | -0,08% | -0,52% | +1,27% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 72 | 58,33% | +0,20% | +0,47% | -0,61% | +1,13% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 72 | 58,33% | +0,20% | +0,47% | -0,61% | +1,13% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 66 | 50,00% | +0,12% | +0,18% | -0,73% | +1,03% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 43 | 39,53% | +0,09% | -0,68% | -0,78% | +0,85% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 68 | 44,12% | +0,62% | -0,10% | -0,52% | +1,95% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 71 | 59,15% | +0,46% | +0,76% | -0,65% | +1,72% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 71 | 59,15% | +0,46% | +0,76% | -0,65% | +1,72% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 65 | 52,31% | +0,13% | +0,19% | -1,01% | +1,37% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 43 | 41,86% | +0,42% | -1,35% | -0,82% | +1,40% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 67 | 40,30% | +1,04% | +0,09% | -2,17% | +4,13% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 70 | 54,29% | +0,88% | +0,98% | -2,27% | +3,82% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 70 | 54,29% | +0,88% | +0,98% | -2,27% | +3,82% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 64 | 45,31% | +0,18% | +0,11% | -2,54% | +3,05% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 42 | 30,95% | +0,84% | -2,27% | -2,52% | +4,00% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 66 | 43,94% | +2,16% | +0,27% | -3,07% | +6,86% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 69 | 50,72% | +2,03% | +1,20% | -3,12% | +6,61% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 69 | 50,72% | +2,03% | +1,20% | -3,12% | +6,61% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 63 | 52,38% | +1,18% | -0,47% | -3,53% | +5,81% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 41 | 34,15% | +2,58% | -4,70% | -3,39% | +7,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 65 | 50,77% | +3,05% | +0,65% | -3,61% | +9,04% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 68 | 52,94% | +3,05% | +1,23% | -3,64% | +8,82% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 68 | 52,94% | +3,05% | +1,23% | -3,64% | +8,82% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 62 | 48,39% | +2,03% | -0,78% | -4,13% | +7,77% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 41 | 29,27% | +3,84% | -6,44% | -3,92% | +9,49% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 50,00% | +1,51% | +1,40% | -2,60% | +9,95% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 65 | 46,15% | +3,76% | +0,55% | -4,30% | +11,06% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 68 | 48,53% | +3,66% | +0,88% | -4,30% | +10,86% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 68 | 48,53% | +3,66% | +0,88% | -4,30% | +10,86% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 62 | 51,61% | +2,31% | -1,27% | -4,85% | +9,30% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 41 | 31,71% | +4,20% | -7,07% | -4,70% | +11,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 60,00% | +1,26% | +0,96% | -3,68% | +10,47% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 61 | 62,30% | +5,13% | +4,82% | -5,01% | +13,74% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 64 | 64,06% | +4,72% | +3,68% | -4,98% | +13,33% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 64 | 64,06% | +4,72% | +3,68% | -4,98% | +13,33% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 58 | 55,17% | +2,45% | +0,15% | -5,64% | +10,37% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 37 | 45,95% | +4,39% | -4,10% | -5,44% | +12,23% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +5,41% | +1,04% | -4,48% | +13,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 54 | 66,67% | +8,27% | +4,55% | -4,75% | +18,71% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 57 | 68,42% | +8,65% | +6,85% | -4,78% | +18,92% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 57 | 68,42% | +8,65% | +6,85% | -4,78% | +18,92% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 51 | 62,75% | +6,26% | -0,76% | -5,53% | +15,38% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 32 | 50,00% | +5,16% | -6,82% | -5,06% | +14,16% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 66,67% | +6,54% | +0,57% | -4,75% | +18,76% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 46 | 80,43% | +13,19% | +7,78% | -4,57% | +26,51% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 48 | 87,50% | +13,45% | +11,56% | -4,59% | +27,05% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 48 | 87,50% | +13,45% | +11,56% | -4,59% | +27,05% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 42 | 54,76% | +11,75% | -5,50% | -5,49% | +24,21% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 31 | 48,39% | +10,82% | -8,72% | -5,10% | +22,58% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 85,71% | +23,10% | +14,05% | -3,96% | +33,14% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 32 | 37,50% | +23,62% | -1,37% | -4,35% | +41,06% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 34 | 52,94% | +23,50% | +4,89% | -4,36% | +41,00% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 34 | 52,94% | +23,50% | +4,89% | -4,36% | +41,00% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | +23,21% | +6,96% | -4,40% | +40,96% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 30 | 0,00% | +21,64% | -21,64% | -4,76% | +40,02% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 22 | 0,00% | +22,71% | -22,71% | -4,86% | +39,94% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +37,31% | +15,91% | -1,31% | +47,38% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 20 | 15,00% | +23,94% | -13,40% | -5,84% | +40,60% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 21 | 23,81% | +24,51% | -6,57% | -5,88% | +40,79% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 21 | 23,81% | +24,51% | -6,57% | -5,88% | +40,79% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 19 | 26,32% | +22,93% | -3,09% | -6,11% | +39,97% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 21 | 0,00% | +24,51% | -24,51% | -5,88% | +40,79% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 17 | 0,00% | +23,40% | -23,40% | -5,74% | +40,26% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 65 | 52,31% | +0,46% | +0,37% | -0,28% | +1,32% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 68 | 54,41% | +0,42% | +0,45% | -0,43% | +1,27% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 71 | 53,52% | +0,45% | +0,38% | -0,40% | +1,30% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 65 | 47,69% | +0,44% | +0,01% | -0,48% | +1,26% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 47 | 48,94% | +0,72% | +0,12% | -0,36% | +1,63% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 64 | 48,44% | +1,18% | +1,07% | -0,10% | +2,21% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 67 | 47,76% | +1,04% | +0,71% | -0,37% | +1,90% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 70 | 47,14% | +1,01% | +0,67% | -0,35% | +1,94% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 64 | 42,19% | +0,83% | -0,01% | -0,32% | +1,94% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 46 | 50,00% | +0,99% | +0,47% | -0,33% | +2,00% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 63 | 55,56% | +1,97% | +1,83% | -1,70% | +4,32% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 66 | 50,00% | +1,73% | +1,28% | -1,88% | +4,08% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 69 | 49,28% | +1,66% | +1,21% | -1,85% | +4,05% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 63 | 47,62% | +1,27% | -0,14% | -1,90% | +3,57% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 45 | 53,33% | +1,35% | +0,71% | -1,84% | +3,57% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 62 | 58,06% | +3,34% | +3,25% | -2,38% | +6,82% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 65 | 53,85% | +3,01% | +2,17% | -2,55% | +6,48% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 68 | 52,94% | +2,90% | +2,04% | -2,53% | +6,37% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 62 | 46,77% | +2,58% | -0,51% | -2,61% | +5,87% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 44 | 54,55% | +1,87% | +1,00% | -2,54% | +5,12% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 61 | 62,30% | +4,75% | +4,83% | -2,84% | +8,73% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 64 | 59,38% | +4,34% | +3,35% | -3,01% | +8,34% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 67 | 59,70% | +4,14% | +3,20% | -3,00% | +8,14% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 61 | 39,34% | +3,24% | -1,45% | -3,12% | +7,34% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 43 | 46,51% | +1,74% | +0,96% | -3,13% | +5,86% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 61 | 67,21% | +6,78% | +6,90% | -3,21% | +11,06% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 64 | 64,06% | +6,37% | +5,66% | -3,41% | +10,47% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 67 | 62,69% | +6,08% | +5,41% | -3,41% | +10,17% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 61 | 47,54% | +4,62% | -1,59% | -3,59% | +8,98% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 43 | 53,49% | +2,06% | +1,15% | -3,69% | +6,79% | PRIMA CALIBRAZIONE |

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

Generato: 2026-09-27 05:32 UTC

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
| BTC | 74 | UTILE | 73 | 19 | 14 | 0 | Famiglia statistica | 1g | 52,05% | +0,33% | campione utile, valutare con prudenza |
| SOL | 74 | UTILE | 68 | 29 | 14 | 0 | Famiglia statistica | 1g | 54,41% | +0,45% | campione utile, valutare con prudenza |
| DOGE | 74 | UTILE | 72 | 29 | 13 | 0 | Famiglia statistica | 1g | 58,33% | +0,47% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 29 | 37,93% | +0,06% | +0,73% | -0,13% | +1,26% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 73 | 52,05% | +0,33% | +0,35% | -0,18% | +0,85% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 7 | 42,86% | -0,24% | -0,24% | -0,87% | +0,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 66 | 40,91% | +0,05% | +0,36% | -0,11% | +0,86% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 29 | 41,38% | +0,02% | +1,20% | +0,19% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 72 | 52,78% | +0,70% | +0,70% | -0,05% | +1,39% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 7 | 28,57% | -0,04% | -0,04% | -0,90% | +1,02% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 65 | 43,08% | +0,02% | +0,65% | +0,06% | +1,34% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 29 | 37,93% | -0,51% | +1,95% | -0,85% | +3,41% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 71 | 52,11% | +1,05% | +1,05% | -1,18% | +2,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 64 | 35,94% | -0,21% | +1,11% | -1,10% | +2,79% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 28 | 42,86% | -2,17% | +4,36% | -1,11% | +6,49% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 70 | 50,00% | +2,02% | +2,02% | -1,73% | +4,40% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 6 | 16,67% | -0,95% | -0,95% | -2,27% | +2,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 63 | 41,27% | -0,74% | +1,95% | -1,65% | +4,39% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 28 | 39,29% | -4,00% | +5,77% | -1,37% | +8,77% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 69 | 59,42% | +2,88% | +2,88% | -2,04% | +5,62% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 62 | 43,55% | -1,13% | +2,98% | -1,96% | +5,69% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 28 | 42,86% | -4,46% | +5,84% | -1,59% | +9,49% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 69 | 65,22% | +3,74% | +3,74% | -2,35% | +6,82% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 62 | 50,00% | -0,37% | +3,92% | -2,28% | +7,01% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 24 | 29,17% | -3,41% | +4,78% | -1,84% | +9,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 65 | 60,00% | +4,97% | +4,97% | -2,63% | +8,57% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 60 | 56,67% | +1,45% | +5,49% | -2,48% | +9,14% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 24 | 54,17% | -4,04% | +8,85% | -2,32% | +12,73% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 58 | 74,14% | +8,27% | +8,27% | -2,70% | +12,17% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 53 | 50,94% | +0,31% | +8,90% | -2,53% | +12,86% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 17 | 52,94% | -5,99% | +15,73% | -1,89% | +20,13% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 49 | 89,80% | +13,99% | +13,99% | -2,47% | +18,21% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 3 | 100,00% | +5,40% | +5,40% | -4,01% | +8,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 44 | 52,27% | -1,01% | +14,13% | -2,24% | +18,60% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 4 | 0,00% | -21,70% | +21,70% | -1,55% | +30,01% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 34 | 100,00% | +23,88% | +23,88% | -3,00% | +28,48% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 29 | 41,38% | -2,10% | +24,37% | -2,74% | +29,02% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Classic technical | 2 | 0,00% | -32,21% | +32,21% | -2,23% | +37,27% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 21 | 100,00% | +25,40% | +25,40% | -3,24% | +30,62% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 17 | 29,41% | -12,13% | +25,58% | -2,88% | +31,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 43 | 39,53% | -0,68% | +0,09% | -0,78% | +0,85% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 72 | 58,33% | +0,47% | +0,20% | -0,61% | +1,13% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 11 | 63,64% | +2,53% | +2,82% | +0,75% | +3,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 66 | 50,00% | +0,18% | +0,12% | -0,73% | +1,03% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 43 | 41,86% | -1,35% | +0,42% | -0,82% | +1,40% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 71 | 59,15% | +0,76% | +0,46% | -0,65% | +1,72% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 11 | 45,45% | +2,65% | +2,89% | +1,08% | +5,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 65 | 52,31% | +0,19% | +0,13% | -1,01% | +1,37% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 42 | 30,95% | -2,27% | +0,84% | -2,52% | +4,00% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 70 | 54,29% | +0,98% | +0,88% | -2,27% | +3,82% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 11 | 54,55% | +2,62% | +2,81% | -1,35% | +6,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 64 | 45,31% | +0,11% | +0,18% | -2,54% | +3,05% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 41 | 34,15% | -4,70% | +2,58% | -3,39% | +7,30% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 69 | 50,72% | +1,20% | +2,03% | -3,12% | +6,61% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 11 | 36,36% | +2,02% | +2,17% | -2,50% | +9,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 63 | 52,38% | -0,47% | +1,18% | -3,53% | +5,81% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 41 | 29,27% | -6,44% | +3,84% | -3,92% | +9,49% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 68 | 52,94% | +1,23% | +3,05% | -3,64% | +8,82% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 10 | 50,00% | +1,40% | +1,51% | -2,60% | +9,95% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 62 | 48,39% | -0,78% | +2,03% | -4,13% | +7,77% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 41 | 31,71% | -7,07% | +4,20% | -4,70% | +11,63% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 68 | 48,53% | +0,88% | +3,66% | -4,30% | +10,86% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 10 | 60,00% | +0,96% | +1,26% | -3,68% | +10,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 62 | 51,61% | -1,27% | +2,31% | -4,85% | +9,30% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 37 | 45,95% | -4,10% | +4,39% | -5,44% | +12,23% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 64 | 64,06% | +3,68% | +4,72% | -4,98% | +13,33% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 9 | 44,44% | +1,04% | +5,41% | -4,48% | +13,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 58 | 55,17% | +0,15% | +2,45% | -5,64% | +10,37% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 32 | 50,00% | -6,82% | +5,16% | -5,06% | +14,16% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 57 | 68,42% | +6,85% | +8,65% | -4,78% | +18,92% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 9 | 66,67% | +0,57% | +6,54% | -4,75% | +18,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 51 | 62,75% | -0,76% | +6,26% | -5,53% | +15,38% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 31 | 48,39% | -8,72% | +10,82% | -5,10% | +22,58% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 48 | 87,50% | +11,56% | +13,45% | -4,59% | +27,05% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 7 | 85,71% | +14,05% | +23,10% | -3,96% | +33,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 42 | 54,76% | -5,50% | +11,75% | -5,49% | +24,21% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 22 | 0,00% | -22,71% | +22,71% | -4,86% | +39,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 34 | 52,94% | +4,89% | +23,50% | -4,36% | +41,00% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,91% | +37,31% | -1,31% | +47,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 30 | 0,00% | -21,64% | +21,64% | -4,76% | +40,02% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 17 | 0,00% | -23,40% | +23,40% | -5,74% | +40,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 21 | 23,81% | -6,57% | +24,51% | -5,88% | +40,79% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 21 | 0,00% | -24,51% | +24,51% | -5,88% | +40,79% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 47 | 48,94% | +0,12% | +0,72% | -0,36% | +1,63% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 68 | 54,41% | +0,45% | +0,42% | -0,43% | +1,27% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 65 | 47,69% | +0,01% | +0,44% | -0,48% | +1,26% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 46 | 50,00% | +0,47% | +0,99% | -0,33% | +2,00% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 67 | 47,76% | +0,71% | +1,04% | -0,37% | +1,90% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 64 | 42,19% | -0,01% | +0,83% | -0,32% | +1,94% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 45 | 53,33% | +0,71% | +1,35% | -1,84% | +3,57% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 66 | 50,00% | +1,28% | +1,73% | -1,88% | +4,08% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 63 | 47,62% | -0,14% | +1,27% | -1,90% | +3,57% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 44 | 54,55% | +1,00% | +1,87% | -2,54% | +5,12% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 65 | 53,85% | +2,17% | +3,01% | -2,55% | +6,48% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 62 | 46,77% | -0,51% | +2,58% | -2,61% | +5,87% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 43 | 46,51% | +0,96% | +1,74% | -3,13% | +5,86% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 64 | 59,38% | +3,35% | +4,34% | -3,01% | +8,34% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 61 | 39,34% | -1,45% | +3,24% | -3,12% | +7,34% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 43 | 53,49% | +1,15% | +2,06% | -3,69% | +6,79% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 64 | 64,06% | +5,66% | +6,37% | -3,41% | +10,47% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 61 | 47,54% | -1,59% | +4,62% | -3,59% | +8,98% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 42 | 52,38% | +2,18% | +3,36% | -4,30% | +8,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 60 | 75,00% | +8,16% | +8,84% | -3,87% | +13,61% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 60 | 45,00% | -2,12% | +6,76% | -4,07% | +11,88% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 39 | 61,54% | -1,37% | +10,67% | -4,45% | +15,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 53 | 81,13% | +14,66% | +14,71% | -4,04% | +20,24% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 55 | 50,91% | -6,54% | +12,38% | -4,39% | +17,90% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 30 | 36,67% | -11,83% | +25,32% | -3,81% | +30,55% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 44 | 86,36% | +21,94% | +25,45% | -3,66% | +31,86% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 46 | 28,26% | -14,12% | +22,51% | -4,13% | +28,54% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 21 | 0,00% | -38,81% | +38,81% | -4,64% | +48,52% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 30 | 73,33% | +23,72% | +39,51% | -4,89% | +47,41% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,56% | +44,56% | -5,94% | +49,24% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 32 | 12,50% | -31,73% | +37,88% | -5,31% | +46,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 13 | 0,00% | -48,10% | +48,10% | -6,31% | +54,40% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 17 | 52,94% | +12,20% | +44,29% | -7,13% | +51,09% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +41,93% | +41,93% | -9,62% | +45,82% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 21 | 19,05% | -29,95% | +42,86% | -7,08% | +50,18% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 69 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 73 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 87 | 39,08% | -0,14% |
| BTC | BREVE | Famiglia statistica | 216 | 52,31% | +0,69% |
| BTC | BREVE | Microstruttura exchange | 21 | 33,33% | -0,22% |
| BTC | BREVE | Tecnico | 195 | 40,00% | -0,05% |
| BTC | SETTIMANALE | Classic technical | 84 | 41,67% | -3,55% |
| BTC | SETTIMANALE | Famiglia statistica | 208 | 58,17% | +2,88% |
| BTC | SETTIMANALE | Microstruttura exchange | 16 | 31,25% | -1,22% |
| BTC | SETTIMANALE | Tecnico | 187 | 44,92% | -0,75% |
| BTC | SWING | Classic technical | 48 | 41,67% | -3,73% |
| BTC | SWING | Famiglia statistica | 123 | 66,67% | +6,53% |
| BTC | SWING | Microstruttura exchange | 10 | 60,00% | +0,93% |
| BTC | SWING | Tecnico | 113 | 53,98% | +0,92% |
| BTC | MEDIO | Classic technical | 23 | 39,13% | -11,01% |
| BTC | MEDIO | Famiglia statistica | 104 | 95,19% | +19,52% |
| BTC | MEDIO | Microstruttura exchange | 5 | 100,00% | +12,53% |
| BTC | MEDIO | Tecnico | 90 | 44,44% | -3,46% |
| DOGE | BREVE | Classic technical | 128 | 37,50% | -1,42% |
| DOGE | BREVE | Famiglia statistica | 213 | 57,28% | +0,73% |
| DOGE | BREVE | Microstruttura exchange | 33 | 54,55% | +2,60% |
| DOGE | BREVE | Tecnico | 195 | 49,23% | +0,16% |
| DOGE | SETTIMANALE | Classic technical | 123 | 31,71% | -6,07% |
| DOGE | SETTIMANALE | Famiglia statistica | 205 | 50,73% | +1,11% |
| DOGE | SETTIMANALE | Microstruttura exchange | 31 | 48,39% | +1,48% |
| DOGE | SETTIMANALE | Tecnico | 187 | 50,80% | -0,84% |
| DOGE | SWING | Classic technical | 69 | 47,83% | -5,36% |
| DOGE | SWING | Famiglia statistica | 121 | 66,12% | +5,17% |
| DOGE | SWING | Microstruttura exchange | 18 | 55,56% | +0,80% |
| DOGE | SWING | Tecnico | 109 | 58,72% | -0,28% |
| DOGE | MEDIO | Classic technical | 70 | 21,43% | -16,68% |
| DOGE | MEDIO | Famiglia statistica | 103 | 63,11% | +5,66% |
| DOGE | MEDIO | Microstruttura exchange | 13 | 84,62% | +19,38% |
| DOGE | MEDIO | Tecnico | 93 | 24,73% | -15,00% |
| SOL | BREVE | Classic technical | 138 | 50,72% | +0,43% |
| SOL | BREVE | Famiglia statistica | 201 | 50,75% | +0,81% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 192 | 45,83% | -0,04% |
| SOL | SETTIMANALE | Classic technical | 130 | 51,54% | +1,04% |
| SOL | SETTIMANALE | Famiglia statistica | 193 | 59,07% | +3,72% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 184 | 44,57% | -1,18% |
| SOL | SWING | Classic technical | 81 | 56,79% | +0,47% |
| SOL | SWING | Famiglia statistica | 113 | 77,88% | +11,21% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 115 | 47,83% | -4,23% |
| SOL | MEDIO | Classic technical | 64 | 17,19% | -28,05% |
| SOL | MEDIO | Famiglia statistica | 91 | 75,82% | +20,71% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 8 | 100,00% | +29,97% |
| SOL | MEDIO | Tecnico | 99 | 21,21% | -23,17% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 3 | in attesa di controlli maturati |
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
| BTC     |         74 |              49 |          25 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         74 |              49 |          25 | OSSERVAZIONE 30+ | 2,04%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         74 |              49 |          25 | OSSERVAZIONE 30+ | 18,37%           | 6,12%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | ALTO           | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo       |
| SOL     | ALTO           | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| DOGE    | ALTO           | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-09-27 05:32 UTC

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
| BTC | 0 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD / ATTESA CONFERME | Prima resistenza sopra 87.364; conferma del doppio minimo sopra 82.262. | Sotto 74.945 il quadro tecnico peggiora. |
| SOL | +3 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | HOLD / TRANCHE PICCOLE, NO LEVA | Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 107,12; milestone analogiche 138,18 / 148,67, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 114,65 / 96,23 / 62,19. |
| DOGE | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.10528 migliora; sopra 0.07997 viene invalidato il pattern ribassista dominante. | Sotto 0.07841 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -1 | 0 | -1 | 0 | +2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | 0 |
| SOL | -1 | 0 | -1 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +3 |
| DOGE | -1 | 0 | -1 | 0 | +3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +2 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **0**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD / ATTESA CONFERME**

BTC è in fase mista. Non è abbastanza debole da autorizzare short semplici, ma non ha ancora una conferma piena.

Dettaglio moduli:

- Famiglia statistica: **-1** — Scanner grezzo -1, Market Regime grezzo 0, match regime 1. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-1** — Casi positivi 42,50%, return centrale 30g -3,50%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 1, positivi 30g 0,00%, return p50 -15,67%.
- Scanner path: **0** — Controlli disponibili 72. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+2** — Score tecnico 6/12, verdetto costruttivo ma non confermato, trend rialzista, struttura volatilità in espansione, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score +2 (rialzista Doppio minimo / CONFERMATO RECENTE; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 1/12, verdetto NEUTRALE / MISTO, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff RANGE / FASE NON CHIARA, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — BTC: cambiamento medio in peggioramento rispetto a ieri.

Conferme: Prima resistenza sopra 87.364; conferma del doppio minimo sopra 82.262.

Invalidazioni: Sotto 74.945 il quadro tecnico peggiora.

### SOL

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+3**
- Affidabilità: **MEDIA**
- Azione coerente: **HOLD / TRANCHE PICCOLE, NO LEVA**

SOL ha una confluenza costruttiva, ma va ancora trattato come setup anticipato. La conferma vera arriva solo sopra le resistenze tecniche e con rientro del gap frattale. Il modulo lifecycle/EMA200 resta utile come contesto, ma non aumenta il punteggio Global.

Dettaglio moduli:

- Famiglia statistica: **-1** — Scanner grezzo -1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-1** — Casi positivi 45,00%, return centrale 30g -4,92%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 72. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 8/12, verdetto rialzista tecnico, trend rialzista, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Triplo massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 10/12, verdetto CONFERMATO RIALZISTA, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto STRUTTURA ANALOGA, PREZZO NON ADERENTE, somiglianza strutturale +70,86%, aderenza live +68,07%, errore live +15,97%, gap corrente +23,80%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE NON CONFERMATO DAL PREZZO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 70, ma percorso ancorato non aderente: gap +23,80%, errore live +15,97%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 1, bias CONTESTO DA OSSERVARE, EMA200 111,31 $, upside EMA200 -7,76%, gap EMA50/EMA200 -5,11%, hit EMA200 12w +100,00%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +0.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — SOL: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 107,12; milestone analogiche 138,18 / 148,67, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 114,65 / 96,23 / 62,19.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **-1** — Scanner grezzo -1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-1** — Casi positivi 42,50%, return centrale 30g -7,33%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 72. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 10/12, verdetto rialzista tecnico, trend rialzista, struttura volatilità in espansione, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score +2 (rialzista Doppio minimo / CONFERMATO RECENTE; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 2/12, verdetto ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff RANGE / FASE NON CHIARA, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +0.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in misto rispetto a ieri.

Conferme: Sopra 0.10528 migliora; sopra 0.07997 viene invalidato il pattern ribassista dominante.

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

Generato: 2026-09-27 05:32 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 84.405 $ | prezzo corrente |
| Power Law centrale | 125.883 $ | deviazione -32,95% |
| Banda p10-p90 | 78.289 $ / 317.615 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 17,39% | posizione storica nel corridoio |
| Esponente β | 5,7929 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3164 cambiando finestra |
| Ultimo halving | 2024-04-19 | 891 giorni fa |
| Fase ciclo | 60,99% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-09-27 (4393 osservazioni)
- Formula stimata: prezzo ≈ exp(-38.9712) × giorni^5.7929
- Prezzo centrale oggi: **125.883 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 17,39%
- Scarto dal centro: **-32,95%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,7929 | 91,93% |
| 2015 | 5,8738 | 91,48% |
| 2016 | 5,5565 | 87,75% |
| 2017 | 4,8309 | 82,99% |
| 2018 | 4,5573 | 78,54% |

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
| 2012-11-28 → 2016-07-09 | 2015-02-10 | +33,90% | +10,15% | +20,58% | +73,60% |
| 2016-07-09 → 2020-05-11 | 2018-11-11 | -46,58% | -42,74% | -0,51% | +36,60% |
| 2020-05-11 → 2024-04-19 | 2022-10-06 | +6,65% | -15,50% | +41,15% | +40,04% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 8 | 1 | 4.819987783661839 | 0 |
| DOGE | DOGE/BTC | RELATIVA MISTA / NON CONFERMATA | 0 | 0 | 2.31507118899803 | 0 |

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

Generato: 2026-09-27 05:32 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00142660 | +8 | +1 | 0 | SOVRAPERFORMA BTC | MEDIA | +4,82% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000114 | 0 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +2,32% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** SOVRAPERFORMA BTC (+8)
- **Candidato futuro:** +1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** CONFERMA FORTE: sale in USD e batte BTC
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g +4,36%; 30g +4,82%; 90g +18,98%; 180g +15,42%
- **Daily:** RSI 65.35; MA50 0.00128449; MA200 0.00119153
- **Weekly:** MA30 0.00119785; RSI 64.41
- **Livelli:** supporto 0.00127800; resistenza 0.00145900; breakout 60g 0.00140500; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00133900; target 0.00140150
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00135280
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; struttura con massimi/minimi crescenti; RSI relativo forte; MACD relativo positivo; breakout relativo 60g

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (0)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g +5,24%; 30g +2,32%; 90g -7,44%; 180g -16,45%
- **Daily:** RSI 54.31; MA50 0.00000110; MA200 0.00000124
- **Weekly:** MA30 0.00000124; RSI 43.25
- **Livelli:** supporto 0.00000112; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000099
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** VICINO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 210 | 52,86% | +1,97% | -1,04% |
| SOL | 30g | 206 | 47,57% | +4,57% | +0,58% |
| SOL | 90g | 201 | 52,74% | +9,80% | +3,09% |
| DOGE | 7g | 296 | 55,41% | +1,80% | -1,66% |
| DOGE | 30g | 294 | 53,06% | +1,97% | -3,49% |
| DOGE | 90g | 288 | 54,17% | +6,90% | -9,24% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 40 | 57,50% | +0,33% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 38 | 57,89% | +0,83% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 35 | 42,86% | +0,55% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 35 | 45,71% | +0,59% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 25 | 40,00% | -2,83% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 54 | 66,67% | -0,02% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 54 | 57,41% | +0,01% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 54 | 53,70% | -0,56% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 50 | 54,00% | -0,26% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 38 | 60,53% | -0,02% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **27 settembre 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 120,68 $ | 2026-09-27T05:30:21Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 120,65 $ | 2026-09-27T05:32:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 1m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | -0,03000 $ | -0,02% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=120.68000030517578
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-09-27T05:30:21Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=120.6500015258789
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-09-27T05:32:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-09-27T05:32:08Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=107.918706
ANCHOR_AGE_HOURS=0.029977418333333332
CURRENT_VS_ANCHOR_GAP_USD=-0.029998779296875
CURRENT_VS_ANCHOR_GAP_PCT=-0.024858120004156437
```

## Verdetto: STRUTTURA ANALOGA, PREZZO NON ADERENTE

- **Fase attuale:** FRATTALE NON CONFERMATO DAL PREZZO
- **Somiglianza totale:** +70,86%
- **Somiglianza strutturale:** +70,86%
- **Aderenza prezzo live:** +68,07%
- **Errore medio live:** +15,97%
- **Gap prezzo corrente:** +23,80%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA / NON OPERATIVO
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** La geometria ricorda BTC 2022, ma SOL è troppo distante dal percorso scalato per usarlo come conferma operativa.
- **SOL è al giorno:** 113 dal bottom usato.
- **Giorno BTC equivalente:** 2023-03-14
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Spinta rialzista abbastanza pulita.** Zona bassa **118,88 $** intorno al **28 settembre 2026**; zona alta **138,18 $** intorno al **6 ottobre 2026**; fine step circa **132,98 $** entro il **11 ottobre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=STRUTTURA ANALOGA, PREZZO NON ADERENTE
PRICE_ADHERENCE_FAILED=YES
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=YES
PRICE_ADHERENCE_LAST_GAP_FAILED=YES
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=15.96561221802387
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=23.799026450927308
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 27 settembre 2026 | 87 | +68,07% | +15,97% | +23,80% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 27 settembre 2026 | 114 | +72,78% | +13,61% | +23,80% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: STRUTTURA ANALOGA, PREZZO NON ADERENTE.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: STRUTTURA ANALOGA, PREZZO NON ADERENTE. |
| Aderenza live | +68,07% | Errore medio live +15,97%. |
| Gap corrente | +23,80% | Prezzo non aderente: superata almeno una soglia canonica (15% medio / 18% ultimo). |
| Prima conferma prezzo | 138,18 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 148,67 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 114,65 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 608,38 $ |
| Massimo percorso base | 608,38 $ (21 aprile 2029) |

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
| Prima conferma | 138,18 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 148,67 $ | Scenario più credibile. |
| Invalidazione soft | 114,65 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 4 ottobre 2026 | +13,86% | 137,41 $ | 118,88 $ | 137,41 $ |
| 14 giorni | 11 ottobre 2026 | +10,19% | 132,98 $ | 118,88 $ | 138,18 $ |
| 30 giorni | 27 ottobre 2026 | +22,84% | 148,25 $ | 118,88 $ | 148,25 $ |
| 60 giorni | 26 novembre 2026 | +8,24% | 130,62 $ | 118,88 $ | 148,67 $ |
| 90 giorni | 26 dicembre 2026 | +4,67% | 126,32 $ | 118,88 $ | 148,67 $ |
| 120 giorni | 25 gennaio 2027 | +22,81% | 148,21 $ | 118,88 $ | 151,94 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 27 settembre 2026 -> 11 ottobre 2026 | +10,19% | 118,88 $ (28 settembre 2026) | 138,18 $ (6 ottobre 2026) | 132,98 $ | Spinta rialzista abbastanza pulita. |
| Step 2 - primo mese | 12 ottobre 2026 -> 27 ottobre 2026 | +22,84% | 135,53 $ (17 ottobre 2026) | 148,25 $ (27 ottobre 2026) | 148,25 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 28 ottobre 2026 -> 26 novembre 2026 | +8,24% | 130,62 $ (26 novembre 2026) | 148,67 $ (28 ottobre 2026) | 130,62 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 27 novembre 2026 -> 26 dicembre 2026 | +4,67% | 125,63 $ (19 dicembre 2026) | 136,97 $ (11 dicembre 2026) | 126,32 $ | Leggera continuazione rialzista. |

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
| Prezzo SOL | 120,68 $ |  |
| Weekly RSI | 64,97 / linea grezza 51,77 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 50,49 / linea grezza 55,48 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 608,38 $ | Avanzamento +19,84% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 50,5, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Prezzo SOL | 120,68 $ |
| TVL Solana | 6,62 mld $ |
| TVL 7g | +7,26% |
| DEX volume 24h | 2,35 mld $ |
| Fees 24h | 18,28 mln $ |
| Stablecoin su Solana | 16,74 mld $ |
| Stake ratio | 68,93% |
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

| Voce                      | Valore                       |
|:--------------------------|:-----------------------------|
| Lifecycle squeeze score | 1 |
| Bias | CONTESTO DA OSSERVARE |
| Azione coerente | SOLO OSSERVAZIONE |
| Peso suggerito Global | 0 |
| Trend squeeze | STABILE / DA CONFERMARE |
| Trend squeeze score | 0 |
| Confronto precedente | 2026-09-21 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 120,68 $ |
| EMA200 weekly target | 111,31 $ |
| Upside verso EMA200 | -7,76% |
| Distanza prezzo da EMA200 | +8,41% |
| Gap EMA50/EMA200 | -5,11% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 64,97 |
| Età SOL | 6,5 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +100,00% |
| Max gain mediano 12w | +27,43% |
| Drawdown mediano 12w | -18,94% |

Lettura semplice:

**SOLO OSSERVAZIONE**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-09-27 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-09-27 05:30:21 UTC**

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
- DOGE: nessun cambiamento forte rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO MEDIO | peggioramento | NEUTRALE / INCERTO | +42.50% | -5.00 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | miglioramento | NEUTRALE / INCERTO | +45.00% | +2.50 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | misto | NEUTRALE / INCERTO | +42.50% | +2.50 punti |

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
| BTC | 80.158 $ | 92.815 $ | +42,86% | +15,79% | rimbalzo debole | 92.815 $ | 80.158 $ | +42,86% | -13,64% | scarico possibile |
| SOL | 114,65 $ | 132,75 $ | +44,83% | +15,79% | rimbalzo debole | 132,75 $ | 114,65 $ | +30,77% | -13,64% | spike storicamente più resistente |
| DOGE | 0,09111 $ | 0,10550 $ | +28,12% | +15,79% | rimbalzo poco frequente | 0,10550 $ | 0,09111 $ | +31,58% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +42,86% (12/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 12 poi sono scaricati a -5,00%. Percentuale: +42,86% (12/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.**
- **SOL: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 13 poi sono rimbalzati fino a +10,00%. Percentuale: +44,83% (13/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **SOL: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 8 poi sono scaricati a -5,00%. Percentuale: +30,77% (8/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 32 prima sono scesi a -5,00%. Tra quei 32, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +28,12% (9/32). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 19 prima sono saliti a +10,00%. Tra quei 19, 6 poi sono scaricati a -5,00%. Percentuale: +31,58% (6/19). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-09-27 05:31:53 UTC

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-09-27 | 2026-09-27T05:30:21Z | 2026-09-27 05:30:21 |
| SOL | 2026-09-27 | 2026-09-27T05:30:21Z | 2026-09-27 05:30:21 |
| DOGE | 2026-09-27 | 2026-09-27T05:30:21Z | 2026-09-27 05:30:21 |

La data di generazione del report non sostituisce la data degli input: se gli snapshot locali sono più vecchi, i valori restano riferiti agli snapshot indicati in tabella.

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
| BTC | 2026-09-27 | 84.377 $ | INCERTO | 42,50% | 64.485,51 $ | 72.361,42 $ | 81.425,31 $ | 92.632,64 $ | 113.771,42 $ |
| SOL | 2026-09-27 | 120,68 $ | INCERTO | 45,00% | 88,53 $ | 101,50 $ | 114,74 $ | 140,15 $ | 187,37 $ |
| DOGE | 2026-09-27 | 0.09591 $ | INCERTO | 42,50% | 0.05629 $ | 0.07334 $ | 0.08888 $ | 0.11072 $ | 0.15102 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | AVAILABLE | SAME_BTC_REGIME | 1 | 2 | 7 | 7 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 81.425,31 $ | 86.769,82 $ | 113.771,42 $ | 98.585,09 $ |
| SOL | AVAILABLE | SAME_BTC_REGIME | 0 | 2 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 114,74 $ | 130,31 $ | 187,37 $ | 161,79 $ |
| DOGE | AVAILABLE | SAME_BTC_REGIME | 0 | 1 | 5 | 5 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.08888 $ | 0.09863 $ | 0.15102 $ | 0.10789 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-08-28**; verificato fino al **2026-09-27**; stato **COMPLETO 30/30g**.
- Reale **84.375,82 $**; p50 previsto **84.787,03 $**; scarto **-0,48%**.
- Errore medio assoluto **2,36%**; massimo **6,68%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted BTC](scanner_forecast_BTC_regime_adjusted.png)

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

<!-- SOL_CONDITIONAL_ANALYSES_START -->
#### SOL — Analisi condizionata -5% → +10%

Queste analisi sono **separate dal cono SOL originale**. Il cono sopra continua a usare normalmente i **40 analoghi più simili a SOL**.

Il filtro condizionato parte proprio da quei 40 casi e conserva soltanto gli episodi che hanno toccato **prima -5%** dal proprio baseline e **successivamente +10% entro 30 giorni**.

##### A. Conditional Successor corrente — dinamico

Questo campione viene ricostruito ad ogni run dai **40 analoghi SOL correnti**. Di conseguenza il numero di episodi qualificati e gli asset possono cambiare giorno per giorno.

**Campione corrente:** 13 episodi qualificati su 40 · 13 asset distinti.

![SOL conditional successor corrente](scanner_forecast_SOL_conditional_successor_current.png)

###### Confronto diretto a 30 giorni

| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Cono standard | 2026-09-27 | 40 | 2026-10-27 | 88.53 $ | 101.50 $ | 114.74 $ | 140.15 $ | 187.37 $ |
| Conditional corrente | 2026-09-27 | 13 | 2026-10-27 | 72.90 $ | 89.41 $ | 107.11 $ | 133.40 $ | 165.02 $ |

###### Struttura successiva dei casi correnti

| Classe | Episodi | Frequenza empirica |
| --- | ---: | ---: |
| DIRECT_CONTINUATION | 6 | 46.15% |
| SHALLOW_PULLBACK_THEN_CONTINUATION | 0 | 0.00% |
| DEEP_PULLBACK_THEN_RECOVERY | 1 | 7.69% |
| FAILURE | 6 | 46.15% |
| UNRESOLVED | 0 | 0.00% |

###### Episodi qualificati oggi

| Asset | Match window | -5% hit | +10% anchor | Classe 60d |
| --- | --- | --- | --- | --- |
| THETA-USD | 2023-09-02 → 2023-12-10 | 2023-12-11 | 2023-12-24 | DIRECT_CONTINUATION |
| RUNE-USD | 2023-06-11 → 2023-09-18 | 2023-09-21 | 2023-10-01 | FAILURE |
| EGLD-USD | 2023-09-03 → 2023-12-11 | 2023-12-15 | 2023-12-24 | FAILURE |
| KSM-USD | 2023-09-01 → 2023-12-09 | 2023-12-11 | 2023-12-23 | DIRECT_CONTINUATION |
| BTC-USD | 2022-11-14 → 2023-02-21 | 2023-02-24 | 2023-03-17 | DIRECT_CONTINUATION |
| HBAR-USD | 2020-11-14 → 2021-02-21 | 2021-02-22 | 2021-03-08 | DIRECT_CONTINUATION |
| ALGO-USD | 2023-09-02 → 2023-12-10 | 2023-12-17 | 2023-12-21 | FAILURE |
| OP-USD | 2023-09-04 → 2023-12-12 | 2023-12-15 | 2023-12-22 | DIRECT_CONTINUATION |
| NEO-USD | 2020-11-07 → 2021-02-14 | 2021-02-15 | 2021-02-21 | FAILURE |
| VET-USD | 2020-04-03 → 2020-07-11 | 2020-07-20 | 2020-08-08 | FAILURE |
| SOL-USD | 2020-11-05 → 2021-02-12 | 2021-02-13 | 2021-02-19 | DEEP_PULLBACK_THEN_RECOVERY |
| XRP-USD | 2021-01-31 → 2021-05-10 | 2021-05-12 | 2021-05-18 | FAILURE |
| BNB-USD | 2025-05-15 → 2025-08-22 | 2025-08-25 | 2025-09-17 | DIRECT_CONTINUATION |

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

- Ultimo close disponibile: **2026-09-27** · SOL **120.64 $**.
- Giorno del vintage: **9/30**.
- P50 condizionato previsto per quel giorno: **104.57 $**.
- SOL reale: **DENTRO p10-p90** · **DENTRO p25-p75**.

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

- Cono congelato il **2026-08-28**; verificato fino al **2026-09-27**; stato **COMPLETO 30/30g**.
- Reale **120,64 $**; p50 previsto **113,68 $**; scarto **6,12%**.
- Errore medio assoluto **2,97%**; massimo **7,43%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted SOL](scanner_forecast_SOL_regime_adjusted.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-08-28**; verificato fino al **2026-09-27**; stato **COMPLETO 30/30g**.
- Reale **0.09594 $**; p50 previsto **0.08353 $**; scarto **14,85%**.
- Errore medio assoluto **7,35%**; massimo **17,65%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted DOGE](scanner_forecast_DOGE_regime_adjusted.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 72 | 93,06% | 68,06% | 2,02% | 0,49% |
| BTC | 3g | 68 | 92,65% | 73,53% | 3,35% | 0,71% |
| BTC | 7g | 61 | 91,80% | 68,85% | 4,98% | 2,23% |
| BTC | 14g | 50 | 98,00% | 74,00% | 5,56% | 2,75% |
| BTC | 30g | 23 | 100,00% | 91,30% | 8,90% | 3,16% |
| SOL | 1g | 72 | 81,94% | 61,11% | 2,77% | 1,00% |
| SOL | 3g | 68 | 91,18% | 72,06% | 4,11% | 1,77% |
| SOL | 7g | 61 | 90,16% | 70,49% | 5,92% | 4,02% |
| SOL | 14g | 50 | 86,00% | 74,00% | 7,98% | 7,04% |
| SOL | 30g | 23 | 91,30% | 47,83% | 15,48% | 14,92% |
| DOGE | 1g | 72 | 87,50% | 61,11% | 3,17% | 0,60% |
| DOGE | 3g | 68 | 91,18% | 64,71% | 4,83% | 1,58% |
| DOGE | 7g | 61 | 73,77% | 72,13% | 9,04% | 6,49% |
| DOGE | 14g | 50 | 84,00% | 50,00% | 10,90% | 9,22% |
| DOGE | 30g | 23 | 91,30% | 34,78% | 17,34% | 17,34% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
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

Generato: 2026-09-27 05:32 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +57,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +55,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +57,50%       | Nessun lato sopra soglia estrema |                  40 |

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
- Casi positivi / salita storica: **42,50%**
- Casi negativi / discesa storica: **57,50%**
- Quanto è netto il segnale: **debole**
- Prezzo attuale: **84.377,03 $**
- Return normale fra 30 giorni: **81.425,31 $** (-3,50%)
- Drawdown normale durante il mese: **72.809,54 $** (-13,71%)
- Drawdown brutto da rispettare: **67.146,47 $** (-20,42%)
- Max gain normale durante il mese: **99.722,03 $** (18,19%)
- Max gain buono / take profit ottimistico: **108.126,23 $** (28,15%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **45,00%**
- Casi negativi / discesa storica: **55,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **120,68 $**
- Return normale fra 30 giorni: **114,74 $** (-4,92%)
- Drawdown normale durante il mese: **99,88 $** (-17,24%)
- Drawdown brutto da rispettare: **89,70 $** (-25,67%)
- Max gain normale durante il mese: **142,11 $** (17,76%)
- Max gain buono / take profit ottimistico: **157,96 $** (30,89%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **42,50%**
- Casi negativi / discesa storica: **57,50%**
- Quanto è netto il segnale: **debole**
- Prezzo attuale: **0,10 $**
- Return normale fra 30 giorni: **0,09 $** (-7,33%)
- Drawdown normale durante il mese: **0,08 $** (-19,13%)
- Drawdown brutto da rispettare: **0,07 $** (-30,57%)
- Max gain normale durante il mese: **0,10 $** (8,58%)
- Max gain buono / take profit ottimistico: **0,12 $** (25,95%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è misto. Alcuni asset possono avere lettura diversa, quindi è meglio valutare asset per asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 84.377,03 $

**Direzione più probabile a 30 giorni:** **INCERTO**
- Probabilità storica di salita: **42,50%**
- Probabilità storica di discesa: **57,50%**
- Quanto è netto il segnale: **debole**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è incerta, con segnale debole. Nei casi storici simili non c'è stato un vantaggio chiaro né per salita né per discesa.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **64.485,51 $** (-23,57%)
- Se va male: **72.361,42 $** (-14,24%)
- Scenario normale: **81.425,31 $** (-3,50%)
- Se va bene: **92.632,64 $** (9,78%)
- Se va molto bene: **113.771,42 $** (34,84%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **72.809,54 $** (-13,71%)
- Discesa brutta: **67.146,47 $** (-20,42%)
- Discesa molto brutta: **59.970,68 $** (-28,93%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **99.722,03 $** (18,19%)
- Rialzo buono: **108.126,23 $** (28,15%)
- Rialzo molto forte: **138.461,18 $** (64,10%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **72.809,54 $** e uno spike normale intorno a **99.722,03 $**.

La chiusura a 30 giorni è incerta: salita 42,50%, discesa 57,50%. Non c'è un vantaggio netto.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 120,68 $

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

- Se va molto male: **88,53 $** (-26,64%)
- Se va male: **101,50 $** (-15,90%)
- Scenario normale: **114,74 $** (-4,92%)
- Se va bene: **140,15 $** (16,13%)
- Se va molto bene: **187,37 $** (55,27%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **99,88 $** (-17,24%)
- Discesa brutta: **89,70 $** (-25,67%)
- Discesa molto brutta: **83,86 $** (-30,51%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **142,11 $** (17,76%)
- Rialzo buono: **157,96 $** (30,89%)
- Rialzo molto forte: **225,97 $** (87,24%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **99,88 $** e uno spike normale intorno a **142,11 $**.

La chiusura a 30 giorni è incerta: salita 45,00%, discesa 55,00%. Non c'è un vantaggio netto.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 0,10 $

**Direzione più probabile a 30 giorni:** **INCERTO**
- Probabilità storica di salita: **42,50%**
- Probabilità storica di discesa: **57,50%**
- Quanto è netto il segnale: **debole**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è incerta, con segnale debole. Nei casi storici simili non c'è stato un vantaggio chiaro né per salita né per discesa.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,06 $** (-41,31%)
- Se va male: **0,07 $** (-23,54%)
- Scenario normale: **0,09 $** (-7,33%)
- Se va bene: **0,11 $** (15,44%)
- Se va molto bene: **0,15 $** (57,47%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,08 $** (-19,13%)
- Discesa brutta: **0,07 $** (-30,57%)
- Discesa molto brutta: **0,04 $** (-58,39%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,10 $** (8,58%)
- Rialzo buono: **0,12 $** (25,95%)
- Rialzo molto forte: **0,18 $** (92,06%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,08 $** e uno spike normale intorno a **0,10 $**.

La chiusura a 30 giorni è incerta: salita 42,50%, discesa 57,50%. Non c'è un vantaggio netto.

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

- Direzione grezza oggi: **INCERTO**
- Direzione calibrata oggi: **INCERTO**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **-3,50%** → **81.425,31 $**
- Correzione imparata dagli errori: **2,01%**
- Calibrato: **-1,49%** → **83.119,53 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-13,71%** → **72.809,54 $**
- Correzione imparata dagli errori: **4,72%**
- Calibrato: **-8,99%** → **76.794,93 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **18,19%** → **99.722,03 $**
- Correzione imparata dagli errori: **-2,82%**
- Calibrato: **15,36%** → **97.338,45 $**
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

- Grezzo: **-4,92%** → **114,74 $**
- Correzione imparata dagli errori: **8,80%**
- Calibrato: **3,88%** → **125,36 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-17,24%** → **99,88 $**
- Correzione imparata dagli errori: **2,99%**
- Calibrato: **-14,25%** → **103,49 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **17,76%** → **142,11 $**
- Correzione imparata dagli errori: **4,02%**
- Calibrato: **21,77%** → **146,96 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Dogecoin

- Previsioni controllate: **30**
- Previsioni usate per la calibrazione recente: **30**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **92,59%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **INCERTO**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **-7,33%** → **0,09 $**
- Correzione imparata dagli errori: **15,19%**
- Calibrato: **7,86%** → **0,10 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-19,13%** → **0,08 $**
- Correzione imparata dagli errori: **15,34%**
- Calibrato: **-3,79%** → **0,09 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **8,58%** → **0,10 $**
- Correzione imparata dagli errori: **2,52%**
- Calibrato: **11,10%** → **0,11 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 84.377,03 $

Bitcoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **42,50%**
- Casi negativi dopo 30 giorni: **57,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **87,05%**
- Rendimento medio dopo 30 giorni: **3,39%**
- Rendimento centrale dopo 30 giorni: **-3,50%**
- Discesa media durante i 30 giorni: **-14,67%**
- Massimo rialzo medio durante i 30 giorni: **26,45%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **87.233,94 $**
- Scenario centrale a 30 giorni: **81.425,31 $**
- Zona di rischio media: **72.002,28 $**
- Zona di rialzo media: **106.695,25 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -23,57% → **64.485,51 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -14,24% → **72.361,42 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -3,50% → **81.425,31 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 9,78% → **92.632,64 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 34,84% → **113.771,42 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -28,93% → **59.970,68 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -20,42% → **67.146,47 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -13,71% → **72.809,54 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,34% → **80.716,06 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,24% → **84.175,77 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,00% → **85.224,61 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 7,15% → **90.406,39 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 18,19% → **99.722,03 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 28,15% → **108.126,23 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 64,10% → **138.461,18 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| BTC-USD         | 2022-11-14   | 2023-02-21 |        91.83 |        15.95 |         -17.39 |          15.95 |
| RUNE-USD        | 2023-06-11   | 2023-09-18 |        91.32 |       -15.88 |         -17.79 |          12.36 |
| ETH-USD         | 2022-11-12   | 2023-02-19 |        89.32 |         7.45 |         -15    |           7.45 |
| THETA-USD       | 2023-09-02   | 2023-12-10 |        89.21 |       -10.94 |         -10.94 |          24.39 |
| TRX-USD         | 2022-11-12   | 2023-02-19 |        88.81 |        -4.55 |         -18.42 |           2.21 |
| INJ-USD         | 2023-08-26   | 2023-12-03 |        88.58 |       112.1  |          -3.76 |         147.89 |
| DASH-USD        | 2020-09-18   | 2020-12-26 |        88.31 |        -2.19 |         -19.23 |          37.81 |
| ATOM-USD        | 2020-05-06   | 2020-08-13 |        88.2  |        -8.76 |         -19.86 |          38.61 |
| AVAX-USD        | 2021-06-16   | 2021-09-23 |        88.04 |       -14.34 |         -28.87 |           0    |
| QTUM-USD        | 2023-08-24   | 2023-12-01 |        87.86 |        21.69 |          -0.19 |          21.69 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 120,68 $

Solana è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **45,00%**
- Casi negativi dopo 30 giorni: **55,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,20%**
- Rendimento medio dopo 30 giorni: **6,85%**
- Rendimento centrale dopo 30 giorni: **-4,92%**
- Discesa media durante i 30 giorni: **-16,94%**
- Massimo rialzo medio durante i 30 giorni: **30,46%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **128,94 $**
- Scenario centrale a 30 giorni: **114,74 $**
- Zona di rischio media: **100,24 $**
- Zona di rialzo media: **157,44 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -26,64% → **88,53 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -15,90% → **101,50 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -4,92% → **114,74 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 16,13% → **140,15 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 55,27% → **187,37 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -30,51% → **83,86 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -25,67% → **89,70 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -17,24% → **99,88 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,57% → **115,16 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,83% → **119,68 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **120,68 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 4,28% → **125,84 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 17,76% → **142,11 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 30,89% → **157,96 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 87,24% → **225,97 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| THETA-USD       | 2023-09-02   | 2023-12-10 |        88.75 |       -10.94 |         -10.94 |          24.39 |
| ATOM-USD        | 2023-09-03   | 2023-12-11 |        88.75 |         5.27 |          -4.59 |          22.25 |
| RUNE-USD        | 2023-06-11   | 2023-09-18 |        88.69 |       -15.88 |         -17.79 |          12.36 |
| HBAR-USD        | 2022-11-14   | 2023-02-21 |        88.51 |       -24.36 |         -30.38 |           0    |
| CRV-USD         | 2022-11-16   | 2023-02-23 |        88.24 |       -15.24 |         -22.38 |           0    |
| VET-USD         | 2023-08-31   | 2023-12-08 |        88.06 |         6.53 |           0    |          41.87 |
| AAVE-USD        | 2022-11-15   | 2023-02-22 |        87.72 |       -14.09 |         -20.79 |           0.55 |
| EGLD-USD        | 2023-09-03   | 2023-12-11 |        87.36 |       -11.15 |         -18.93 |          14.7  |
| KSM-USD         | 2023-09-01   | 2023-12-09 |        87.24 |        33.29 |         -10.47 |          86.17 |
| KSM-USD         | 2022-11-15   | 2023-02-22 |        87.22 |       -19.09 |         -26.94 |           0.46 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 0,10 $

Dogecoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **42,50%**
- Casi negativi dopo 30 giorni: **57,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **82,65%**
- Rendimento medio dopo 30 giorni: **2,22%**
- Rendimento centrale dopo 30 giorni: **-7,33%**
- Discesa media durante i 30 giorni: **-23,33%**
- Massimo rialzo medio durante i 30 giorni: **28,06%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,10 $**
- Scenario centrale a 30 giorni: **0,09 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,12 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -41,31% → **0,06 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -23,54% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -7,33% → **0,09 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 15,44% → **0,11 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 57,47% → **0,15 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -58,39% → **0,04 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -30,57% → **0,07 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -19,13% → **0,08 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -7,87% → **0,09 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -3,42% → **0,09 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,10 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 0,98% → **0,10 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 8,58% → **0,10 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 25,95% → **0,12 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 92,06% → **0,18 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| DASH-USD        | 2019-11-13   | 2020-02-20 |        86.24 |       -32.46 |         -59.31 |           2.46 |
| KAVA-USD        | 2022-01-21   | 2022-04-30 |        84.95 |       -38.08 |         -61.9  |           4.77 |
| MANA-USD        | 2022-11-12   | 2023-02-19 |        84.78 |       -13.69 |         -27.97 |           3.36 |
| FIL-USD         | 2020-12-11   | 2021-03-20 |        84.61 |        87.82 |          -6.88 |         132.08 |
| RUNE-USD        | 2020-09-14   | 2020-12-22 |        84.1  |        78.89 |          -5.22 |         125.06 |
| DOT-USD         | 2023-09-03   | 2023-12-11 |        83.98 |        18.85 |           0    |          37.6  |
| AVAX-USD        | 2021-06-16   | 2021-09-23 |        83.6  |       -14.34 |         -28.87 |           0    |
| NEAR-USD        | 2022-11-12   | 2023-02-19 |        83.59 |       -19.33 |         -30.47 |           4.82 |
| ENJ-USD         | 2022-11-17   | 2023-02-24 |        83.57 |       -21.74 |         -29.05 |           0    |
| EGLD-USD        | 2023-09-03   | 2023-12-11 |        83.35 |       -11.15 |         -18.93 |          14.7  |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report

Generated: 2026-09-27 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-27 | RECOVERY | 84.377 $ | True | 40.30% | -1.01% | RECOVERY | 40.30% | -1.01% |
| DOGE-USD | 2026-09-27 | RECOVERY | 0.09591 $ | True | 30.87% | -8.16% | RECOVERY | 40.30% | -1.01% |
| SOL-USD | 2026-09-27 | RECOVERY | 120,68 $ | True | 61.02% | -2.67% | RECOVERY | 40.30% | -1.01% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 42.50% | -3.50% | 9.78% | 34.84% | -13.71% | -28.93% | 18.19% | 28.15% | 64.10% | 40.00% | -5.03% | 20.61% | 91.65% |
| BTC-USD | SAME_BTC_REGIME | 7 | 57.14% | 2.84% | 6.62% | 16.84% | -8.74% | -22.04% | 22.25% | 25.72% | 28.54% | 42.86% | -1.86% | 10.28% | 23.32% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 0.00% | -8.93% | -5.56% | -3.54% | -22.96% | -25.94% | 30.88% | 34.34% | 36.42% | 50.00% | 48.08% | 84.74% | 106.74% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -15.67% | -15.67% | -15.67% | -26.69% | -26.69% | 23.95% | 23.95% | 23.95% | 0.00% | -25.25% | -25.25% | -25.25% |
| DOGE-USD | ALL_MATCHES | 40 | 42.50% | -7.33% | 15.44% | 57.47% | -19.13% | -58.39% | 8.58% | 25.95% | 92.06% | 42.50% | -4.21% | 15.48% | 76.24% |
| DOGE-USD | SAME_BTC_REGIME | 5 | 60.00% | 2.84% | 2.95% | 12.49% | -8.74% | -15.49% | 20.73% | 24.01% | 32.17% | 20.00% | -3.53% | -1.86% | 3.59% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 100.00% | 1.28% | 1.28% | 1.28% | -4.43% | -4.43% | 30.62% | 30.62% | 30.62% | 100.00% | 0.91% | 0.91% | 0.91% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 45.00% | -4.92% | 16.13% | 55.27% | -17.24% | -30.51% | 17.76% | 30.89% | 87.24% | 45.00% | -4.06% | 21.99% | 74.08% |
| SOL-USD | SAME_BTC_REGIME | 9 | 77.78% | 7.98% | 18.85% | 34.06% | -3.55% | -10.78% | 27.49% | 33.18% | 52.03% | 55.56% | 1.61% | 18.94% | 32.28% |
| SOL-USD | SAME_ASSET_REGIME | 2 | 0.00% | -31.03% | -29.95% | -29.31% | -34.92% | -37.49% | 3.75% | 5.62% | 6.74% | 50.00% | -5.97% | -1.37% | 1.39% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 23 | 43.48% | -7.74% | -15.00% | 23.04% | 43.48% | -5.17% | 44.84% |
| BTC-USD | HISTORICAL_BTC_BULL | 9 | 33.33% | -2.45% | -9.97% | 37.65% | 33.33% | -8.85% | 202.07% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -8.76% | -19.86% | 38.61% | 0.00% | -2.68% | 38.61% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 7 | 57.14% | 2.84% | -8.74% | 25.72% | 42.86% | -1.86% | 28.74% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 28 | 28.57% | -14.22% | -28.42% | 16.61% | 35.71% | -17.54% | 26.22% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 80.00% | 78.89% | -5.22% | 132.08% | 80.00% | 48.30% | 458.70% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 8.83% | -8.55% | 12.80% | 100.00% | 45.29% | 62.15% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 5 | 60.00% | 2.84% | -8.74% | 24.01% | 20.00% | -3.53% | 24.01% |
| SOL-USD | HISTORICAL_BTC_BEAR | 19 | 31.58% | -14.09% | -20.79% | 21.85% | 36.84% | -14.25% | 33.31% |
| SOL-USD | HISTORICAL_BTC_BULL | 12 | 41.67% | -8.80% | -19.42% | 39.24% | 50.00% | 4.65% | 110.73% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 9 | 77.78% | 7.98% | -3.55% | 33.18% | 55.56% | 1.61% | 37.60% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 33 | 45.45% | -2.45% | -13.21% | 24.39% | 39.39% | -4.88% | 37.65% |
| BTC-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 34.46% | -7.60% | 130.76% | 50.00% | 40.90% | 225.60% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -15.45% | -22.78% | 8.44% | 0.00% | -9.99% | 8.44% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 0.00% | -8.93% | -22.96% | 34.34% | 50.00% | 48.08% | 157.54% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 32 | 31.25% | -13.89% | -26.63% | 19.13% | 31.25% | -12.88% | 27.94% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 6 | 83.33% | 45.40% | -7.54% | 130.33% | 83.33% | 29.69% | 377.05% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 2.39% | -3.49% | 5.41% | 100.00% | 12.61% | 14.68% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 1.28% | -4.43% | 30.62% | 100.00% | 0.91% | 30.62% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 50.00% | 0.92% | -13.67% | 32.42% | 43.33% | -4.06% | 45.31% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 25.00% | -8.80% | -19.07% | 44.57% | 50.00% | 7.66% | 78.98% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | 0.61% | -14.65% | 48.90% | 50.00% | 3.83% | 76.12% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 0.00% | -31.03% | -34.92% | 5.62% | 50.00% | -5.97% | 5.62% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 1 | 2 | 7 | 7 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 1 | 5 | 5 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 0 | 2 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | ATOM-USD | 2023-09-03 | 87.59% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -4.59% | 22.25% | 1.61% | -9.12% | 22.25% |
| BTC-USD | EGLD-USD | 2023-09-03 | 87.32% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| BTC-USD | ETC-USD | 2023-09-03 | 87.22% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 30.13% | -4.53% | 30.13% | 29.88% | -4.53% | 46.46% |
| BTC-USD | XTZ-USD | 2023-09-03 | 87.05% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.98% | -0.86% | 27.49% | 18.94% | -0.86% | 33.54% |
| BTC-USD | EOS-USD | 2023-09-03 | 86.28% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| BTC-USD | ADA-USD | 2023-09-03 | 85.58% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.84% | -10.32% | 20.73% | -1.86% | -15.34% | 20.73% |
| BTC-USD | ETH-USD | 2019-03-13 | 85.08% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BEARISH_30D | -15.67% | -26.69% | 23.95% | -25.25% | -31.75% | 23.95% |
| DOGE-USD | DOT-USD | 2023-09-03 | 83.98% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 18.85% | 0.00% | 37.60% | 7.23% | -5.57% | 37.60% |
| DOGE-USD | EGLD-USD | 2023-09-03 | 83.35% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| DOGE-USD | KAVA-USD | 2023-09-03 | 82.64% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.95% | -2.83% | 24.01% | -4.58% | -11.86% | 24.01% |
| DOGE-USD | ADA-USD | 2023-09-03 | 82.11% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.84% | -10.32% | 20.73% | -1.86% | -15.34% | 20.73% |
| DOGE-USD | EOS-USD | 2023-09-03 | 82.06% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| SOL-USD | ATOM-USD | 2023-09-03 | 88.75% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -4.59% | 22.25% | 1.61% | -9.12% | 22.25% |
| SOL-USD | EGLD-USD | 2023-09-03 | 87.36% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| SOL-USD | WAVES-USD | 2023-09-03 | 86.79% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 13.10% | -1.28% | 33.18% | -0.79% | -8.93% | 33.18% |
| SOL-USD | ETC-USD | 2023-09-03 | 85.88% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 30.13% | -4.53% | 30.13% | 29.88% | -4.53% | 46.46% |
| SOL-USD | EOS-USD | 2023-09-03 | 85.66% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| SOL-USD | DOT-USD | 2023-09-03 | 85.12% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 18.85% | 0.00% | 37.60% | 7.23% | -5.57% | 37.60% |
| SOL-USD | LINK-USD | 2019-03-13 | 84.79% | RECOVERY | BULL | SAME_BTC_ONLY | HIGH_SPIKE_60D | 49.79% | -3.55% | 109.74% | 41.89% | -3.55% | 109.74% |
| SOL-USD | KAVA-USD | 2023-09-03 | 84.64% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.95% | -2.83% | 24.01% | -4.58% | -11.86% | 24.01% |
| SOL-USD | XTZ-USD | 2023-09-03 | 84.38% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.98% | -0.86% | 27.49% | 18.94% | -0.86% | 33.54% |

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

Generato: 2026-09-27 05:32 UTC

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
| BTC | 84.377 $ | +1 | NEUTRALE / MISTO | STAGE 3 / DISTRIBUZIONE O PAUSA | VOLATILITÀ IN ESPANSIONE | RANGE / FASE NON CHIARA | MEDIO | HOLD / ASPETTA ROTTURA RESISTENZA |
| SOL | 120,68 $ | +10 | CONFERMATO RIALZISTA | STAGE 3 / DISTRIBUZIONE O PAUSA | VOLATILITÀ IN ESPANSIONE | SIGN OF STRENGTH POSSIBILE | BASSO | TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME |
| DOGE | 0.09591 $ | +2 | ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO | STAGE 3 / DISTRIBUZIONE O PAUSA | VOLATILITÀ IN ESPANSIONE | RANGE / FASE NON CHIARA | MEDIO | STAI ALLA FINESTRA |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | 0 | 0 | -1 | 0 | 0 | 0 | +1 |
| SOL | +2 | 0 | +3 | +2 | +1 | 0 | +2 | +10 |
| DOGE | +1 | 0 | 0 | +1 | 0 | 0 | 0 | +2 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.206 $ | 87.364 $ | 87.364 $ | 62.227 $ | 2,87% | 5,13% | 41,74% |
| SOL | 98,63 $ | 122,75 $ | 119,81 $ | 70,69 $ | 4,35% | 10,48% | 69,18% |
| DOGE | 0.08189 $ | 0.09998 $ | 0.10528 $ | 0.06797 $ | 5,88% | 7,58% | 31,20% |

## Lettura dettagliata

### BTC

- Prezzo: **84.377 $**
- Score classico: **+1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **HOLD / ASPETTA ROTTURA RESISTENZA**
- Volatilità tecnica locale: **MEDIO** — ATR14 2,87%; distanza supporto 6,53%; distanza resistenza 3,54%

Dettaglio:

- Trend: **+2** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **0** — RSI sano 64.9; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale 0.00; volume ratio 0.47
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 64.90 |
| MACD histogram | 303.33446 |
| CMF20 | 0.002 |
| Volume ratio 20 | 0.47 |
| MA20 | 80.161 $ |
| MA50 | 75.713 $ |
| MA100 | 69.495 $ |
| MA200 | 71.001 $ |
| Pendenza MA50 20g | +9,09% |
| Pendenza MA200 60g | -1,19% |
| Bollinger width | 17,28% |
| Bollinger position | 0.79 |

### SOL

- Prezzo: **120,68 $**
- Score classico: **+10 / 12**
- Verdetto: **CONFERMATO RIALZISTA**
- Azione coerente: **TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME**
- Volatilità tecnica locale: **BASSO** — ATR14 4,35%; distanza supporto 22,33%; distanza resistenza 1,74%

Dettaglio:

- Trend: **+2** — prezzo sopra MA200 daily; medie daily allineate rialziste; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **+3** — RSI sano 67.3; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.19; volume ratio 0.66
- Conferma prezzo: **+1** — Breakout sopra resistenza 60g, ma volume non forte.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 67.33 |
| MACD histogram | 1.10057 |
| CMF20 | 0.192 |
| Volume ratio 20 | 0.66 |
| MA20 | 107,86 $ |
| MA50 | 97,69 $ |
| MA100 | 86,40 $ |
| MA200 | 84,78 $ |
| Pendenza MA50 20g | +15,76% |
| Pendenza MA200 60g | -3,02% |
| Bollinger width | 27,92% |
| Bollinger position | 0.88 |

### DOGE

- Prezzo: **0.09591 $**
- Score classico: **+2 / 12**
- Verdetto: **ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO**
- Azione coerente: **STAI ALLA FINESTRA**
- Volatilità tecnica locale: **MEDIO** — ATR14 5,88%; distanza supporto 17,11%; distanza resistenza 4,25%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **0** — RSI sano 59.3; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+1** — OBV sopra media; CMF neutrale 0.02; volume ratio 0.55
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 59.30 |
| MACD histogram | 0.00100 |
| CMF20 | 0.017 |
| Volume ratio 20 | 0.55 |
| MA20 | 0.08866 $ |
| MA50 | 0.08361 $ |
| MA100 | 0.07857 $ |
| MA200 | 0.08787 $ |
| Pendenza MA50 20g | +9,40% |
| Pendenza MA200 60g | -8,49% |
| Bollinger width | 27,26% |
| Bollinger position | 0.78 |

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

Generato: 2026-09-27 05:32 UTC

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
| BTC | 84.377 $ | Doppio minimo | CONFERMATO RECENTE | rialzista | 2026-09-21 | 89.580 $ | 28,90% | n/a | Fib 23,6% NON ATTIVO (0) @ 80.374 $ | NEL RANGE | 76.248 $ |
| SOL | 120,68 $ | Triplo massimo | CANDIDATO | ribassista | n/a | 62,51 $ | n/a | 70,71% | Fib 78,6% RECUPERATO (+1) @ 107,08 $ | BREAKOUT 60G | 97,45 $ |
| DOGE | 0.09591 $ | Doppio minimo | CONFERMATO RECENTE | rialzista | 2026-09-21 | 0.11001 $ | 10,76% | n/a | Fib 23,6% TESTATO (0) @ 0.09648 $ | NEL RANGE | 0.09274 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CONFERMATO RECENTE** (+2)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-09-15**
- Età formazione: **12 giorni**
- Breakout pattern: **2026-09-21**
- Età breakout: **6 giorni**
- Neckline: **82.262 $**
- Target teorico: **89.580 $**
- Progresso verso target: **28,90%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 80.374 $** — Swing UP 2026-07-01 57.748 -> 2026-09-21 87.364; livello più vicino 23.6% a 80.374; stato NON ATTIVO; confluenza: invalidazione rialzista.
- Invalidazione: **80.617 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due minimi simili vicino a 74.945 tra 2026-09-02 e 2026-09-15. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (6 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 89.580; progresso corrente: 28,90%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **76.248 $**
- Resistenza: **87.364 $**
- Breakout 60g: **87.364 $**
- Breakdown 60g: **62.227 $**
- RSI14: **64.90**
- ATR14: **2,87%**
- Volume ratio 20g: **0.47**
- Rendimento 30g: **+5,13%**
- Rendimento 90g: **+41,73%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CONFERMATO RECENTE | +2 | rialzista | 82.262 $ | 2026-09-21 | 6g | 89.580 $ | 28,90% | n/a | 80.617 $ | Due minimi simili a 76.248 $ e 74.945 $. Neckline circa 82.262 $. Breakout neckline: 2026-09-21 (6 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 89.580 $; progresso: 28,90%; prezzo sopra neckline. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 35,60% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 49 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **49 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **70,69 $**
- Target teorico: **62,51 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **70,71%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% RECUPERATO (+1) @ 107,08 $** — Swing DOWN 2026-08-27 110,04 -> 2026-09-16 96,23; livello più vicino 78.6% a 107,08; stato RECUPERATO; confluenza: resistenza tecnica, neckline rialzista, invalidazione rialzista.
- Invalidazione: **72,11 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 49 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **97,45 $**
- Resistenza: **122,75 $**
- Breakout 60g: **119,81 $**
- Breakdown 60g: **70,69 $**
- RSI14: **67.38**
- ATR14: **4,35%**
- Volume ratio 20g: **0.66**
- Rendimento 30g: **+10,50%**
- Rendimento 90g: **+69,23%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,51 $ | n/a | 70,71% | 72,11 $ | Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 49 giorni. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 70,71% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 49 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 107,12 $ | 2026-09-18 | 9g | 118,01 $ | 124,54% | n/a | 104,97 $ | Due minimi simili a 97,45 $ e 96,23 $. Neckline circa 107,12 $. Breakout neckline: 2026-09-18 (9 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01 $; progresso: 124,54%; prezzo sopra neckline. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 39g | 85,65 $ | 568,50% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (39 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 568,50%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CONFERMATO RECENTE** (+2)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-09-16**
- Età formazione: **11 giorni**
- Breakout pattern: **2026-09-21**
- Età breakout: **6 giorni**
- Neckline: **0.09421 $**
- Target teorico: **0.11001 $**
- Progresso verso target: **10,76%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 0.09648 $** — Swing UP 2026-08-01 0.06797 -> 2026-09-22 0.10528; livello più vicino 23.6% a 0.09648; stato TESTATO; confluenza: neckline rialzista, invalidazione rialzista.
- Invalidazione: **0.09232 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due minimi simili vicino a 0.07841 tra 2026-09-02 e 2026-09-16. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (6 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 0.11001; progresso corrente: 10,76%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.09274 $**
- Resistenza: **0.09772 $**
- Breakout 60g: **0.10528 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **59.32**
- ATR14: **5,88%**
- Volume ratio 20g: **0.55**
- Rendimento 30g: **+7,59%**
- Rendimento 90g: **+31,22%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CONFERMATO RECENTE | +2 | rialzista | 0.09421 $ | 2026-09-21 | 6g | 0.11001 $ | 10,76% | n/a | 0.09232 $ | Due minimi simili a 0.08028 $ e 0.07841 $. Neckline circa 0.09421 $. Breakout neckline: 2026-09-21 (6 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 0.11001 $; progresso: 10,76%; prezzo sopra neckline. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.07841 $ | n/a | n/a | 0.05153 $ | n/a | 22,33% | 0.07997 $ | Due massimi simili a 0.09998 $ e 0.10528 $. Neckline circa 0.07841 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 5 giorni. |

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

Generato: 2026-09-27 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-27**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-14**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **120,68 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+70,86%**
- Aderenza live principale: **+68,07%**
- Errore medio live principale: **15,97%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **113**
- Osservazioni inclusive dal bottom: **114**
- Osservazioni da inizio programma/scanner: **87**
- Errore assoluto medio dal bottom: **13,61%**
- Errore assoluto medio da inizio programma: **15,97%**
- Gap firmato medio ultimi 7 giorni: **+38,09%**
- Errore assoluto medio ultimi 7 giorni: **38,09%**
- Gap ultimo giorno: **+23,80%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+23,80%**
- Gap firmato medio 7g: **+38,09%**
- Errore assoluto medio 7g: **38,09%**
- Variazione recente gap: **-20,17%**
- Stato gap: **DISALLINEATO SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 104 | 2026-09-18 | 2023-03-05 | 112,60 $ | 88,38 $ | +27,41% | da inizio programma |
| 105 | 2026-09-19 | 2023-03-06 | 111,01 $ | 88,36 $ | +25,64% | da inizio programma |
| 106 | 2026-09-20 | 2023-03-07 | 111,13 $ | 87,53 $ | +26,97% | da inizio programma |
| 107 | 2026-09-21 | 2023-03-08 | 118,75 $ | 85,55 $ | +38,80% | da inizio programma |
| 108 | 2026-09-22 | 2023-03-09 | 118,51 $ | 80,21 $ | +47,74% | da inizio programma |
| 109 | 2026-09-23 | 2023-03-10 | 114,98 $ | 79,52 $ | +44,58% | da inizio programma |
| 110 | 2026-09-24 | 2023-03-11 | 117,01 $ | 81,28 $ | +43,97% | da inizio programma |
| 111 | 2026-09-25 | 2023-03-12 | 122,01 $ | 87,31 $ | +39,74% | da inizio programma |
| 112 | 2026-09-26 | 2023-03-13 | 122,01 $ | 95,32 $ | +28,00% | da inizio programma |
| 113 | 2026-09-27 | 2023-03-14 | 120,68 $ | 97,48 $ | +23,80% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-04 | 110,99 $ | 137,41 $ | 118,88 $ / 137,41 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-11 | 107,42 $ | 132,98 $ | 118,88 $ / 138,18 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-18 | 110,96 $ | 137,37 $ | 118,88 $ / 138,88 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-25 | 119,10 $ | 147,45 $ | 118,88 $ / 147,45 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-01 | 119,74 $ | 148,24 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-08 | 111,51 $ | 138,05 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-15 | 112,98 $ | 139,87 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-22 | 108,95 $ | 134,88 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-29 | 106,50 $ | 131,85 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-06 | 107,25 $ | 132,77 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-13 | 109,13 $ | 135,10 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-20 | 107,30 $ | 132,84 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-27 | 102,10 $ | 126,40 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-03 | 111,59 $ | 138,15 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-10 | 120,89 $ | 149,66 $ | 118,88 $ / 149,69 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-17 | 121,24 $ | 150,09 $ | 118,88 $ / 151,94 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-24 | 120,62 $ | 149,33 $ | 118,88 $ / 151,94 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-31 | 117,61 $ | 145,60 $ | 118,88 $ / 153,50 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 70 | 35,71% | 11,38% | 14,93% |
| 14g | 66 | 22,73% | 17,68% | 15,03% |
| 21g | 59 | 22,03% | 23,91% | 16,57% |
| 28g | 52 | 21,15% | 25,47% | 16,83% |
| 35g | 45 | 28,89% | 27,08% | 16,73% |
| 42g | 38 | 52,63% | 22,72% | 15,46% |
| 49g | 33 | 60,61% | 22,23% | 18,22% |
| 56g | 26 | 61,54% | 18,46% | 19,92% |
| 63g | 19 | 57,89% | 12,57% | 24,58% |
| 70g | 12 | 50,00% | 13,50% | 34,67% |
| 77g | 5 | 0,00% | 16,00% | 30,51% |
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

Generato: 2026-09-27 05:32 UTC

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 84.360 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0023% | -0,08% | 1,80 | -0,77% | 0 $ | 0 $ |
| SOL | 120,44 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0070% | +0,57% | 0,99 | -5,38% | 0 $ | 0 $ |
| DOGE | 0.09583 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0097% | -2,15% | 1,22 | -11,70% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | -0,0015% | 180,90 mln $ | 0,99 | +3,90% |
| BTC | Bitget | OK | +0,0037% | 2,68 mld $ | 4,64 | -70,55% |
| BTC | Kucoin | OK | +0,0029% | 881,83 mln $ | 4,16 | +5,04% |
| SOL | Kraken | OK | -0,0025% | 32,58 mln $ | 0,69 | +3,22% |
| SOL | Bitget | OK | +0,0100% | 485,53 mln $ | 6,65 | -66,31% |
| SOL | Kucoin | OK | +0,0016% | 138,51 mln $ | 1,42 | -17,86% |
| DOGE | Kraken | OK | -0,0057% | 5,62 mln $ | 1,41 | -9,88% |
| DOGE | Bitget | OK | +0,0100% | 119,59 mln $ | 2,34 | -8,28% |
| DOGE | Kucoin | OK | +0,0100% | 60,35 mln $ | 1,16 | -8,21% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+1,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +40,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta. Confluenza tecnica dichiarata: invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+0,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+0,75**.
- OI/funding/basis: **+0,00**.
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

- Score grezzo exchange: **+0,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 10, accuratezza +50,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 2, divergenze 0.
- Flusso taker/order book: **+0,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso. Confluenza tecnica dichiarata: neckline rialzista, invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +42,50% | -3,50% | 3 | +66,67% | RACCOLTA DATI | 0,00 | +42,50% | -3,50% |
| SOL | +45,00% | -4,92% | 5 | +100,00% | RACCOLTA DATI | 0,00 | +45,00% | -4,92% |
| DOGE | +42,50% | -7,33% | 7 | +71,43% | RACCOLTA DATI | 0,00 | +42,50% | -7,33% |

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

Generato: 2026-09-27 05:32 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-27 | BTC | 84.359,90 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,80 | -0,08% | -0,77% |
| 2026-09-27 | DOGE | 0.09583 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,22 | -2,15% | -11,70% |
| 2026-09-27 | SOL | 120,44 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,99 | +0,57% | -5,38% |
| 2026-09-26 | BTC | 83.964,60 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,76 | -3,00% | -2,39% |
| 2026-09-26 | DOGE | 0.09793 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,14 | -0,20% | -5,11% |
| 2026-09-26 | SOL | 120,60 | V2.1.3 | OK | 0 | 0 | 2,50 | MEDIA | 1,14 | +3,84% | -3,36% |
| 2026-09-25 | BTC | 84.171,00 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 4,19 | +0,14% | -0,53% |
| 2026-09-25 | DOGE | 0.09510 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,47 | -2,94% | -7,62% |
| 2026-09-25 | SOL | 116,33 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,15 | +0,81% | -11,76% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 8 | +37,50% | -0,37% | -1,23% | +0,83% | FEEDBACK RAPIDO |
| BTC | 3g | 8 | +37,50% | -0,46% | -2,47% | +1,78% | FEEDBACK RAPIDO |
| BTC | 7g | 5 | +40,00% | -1,30% | -3,40% | +2,47% | FEEDBACK RAPIDO |
| BTC | 14g | 5 | +40,00% | +0,20% | -4,71% | +3,32% | FEEDBACK RAPIDO |
| BTC | 30g | 3 | +66,67% | +5,24% | -4,15% | +8,48% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 5 | +100,00% | +22,07% | -4,32% | +25,38% | FEEDBACK RAPIDO |
| DOGE | 1g | 11 | +54,55% | +1,55% | -0,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 3g | 11 | +36,36% | +1,63% | -3,44% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 7g | 10 | +50,00% | +0,54% | -4,49% | +9,62% | FEEDBACK RAPIDO |
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
| BTC | 84.377 $ | +0.0003% | -6.99% | 1.00 | Misto | 1/5 |
| SOL | 120,68 $ | +0.0064% | -0.96% | 1.16 | Misto | 1/5 |
| DOGE | 0.09591 $ | +0.0100% | -8.49% | 3.59 | Rischio sotto | 2/5 |

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

Generato: 2026-09-27 05:32 UTC

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
| BTC     | 1D   | Conferma rialzista | CONTESTO   | 84.398 $ / 64,95  | n/a                                                                 | +9,22%              | 9,85             |      0 |
| BTC     | 1W   | Conferma rialzista | CONTESTO   | 84.398 $ / 61,50  | n/a                                                                 | +34,35%             | 22,70            |      0 |
| SOL     | 1D   | Conferma rialzista | CONTESTO   | 120,65 $ / 67,33  | n/a                                                                 | +18,53%             | 9,93             |      0 |
| SOL     | 1W   | Conferma rialzista | CONTESTO   | 120,65 $ / 64,96  | n/a                                                                 | +61,86%             | 25,25            |      0 |
| DOGE    | 1D   | Conferma rialzista | CONTESTO   | 0.09591 $ / 59,32 | n/a                                                                 | +13,03%             | 7,36             |      0 |
| DOGE    | 1W   | Hidden bearish     | CONFERMATA | 0.09591 $ / 52,03 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 49,72 | n/a                 | n/a              |      0 |

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

Generato: 2026-09-27 05:32 UTC

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

| Asset   | Prezzo   |   Punteggio | Verdetto                      | Trend           | Momentum                  | Struttura                                             |   Pattern score | Fibonacci       | Pattern rialzista                  | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:------------------------------|:----------------|:--------------------------|:------------------------------------------------------|----------------:|:----------------|:-----------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 84.377 $ | 6 | COSTRUTTIVO MA NON CONFERMATO | Trend rialzista | Momentum misto | Volatilità in espansione | +2 | 0 / NON ATTIVO | Doppio minimo / CONFERMATO RECENTE | Doppio massimo / CANDIDATO | 74.945 | 87.364 |
| SOL | 120,68 $ | 8 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Struttura ribassista con massimi e minimi decrescenti | 0 | +1 / RECUPERATO | Doppio minimo / TARGET RAGGIUNTO | Triplo massimo / CANDIDATO | 96,23 | 107,12 |
| DOGE | 0.09591 $ | 10 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Volatilità in espansione | +2 | 0 / TESTATO | Doppio minimo / CONFERMATO RECENTE | Doppio massimo / CANDIDATO | 0.07841 | 0.10528 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo      | Triplo minimo    | Adam/Eve Bottom                          | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-------------------|:-----------------|:-----------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CONFERMATO RECENTE | TARGET RAGGIUNTO | Eve and Adam Bottom — CONFERMATO RECENTE | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 2 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | INVALIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | CONFERMATO RECENTE | TARGET RAGGIUNTO | Adam and Eve Bottom — CONFERMATO RECENTE | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 2 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 64.9 | 303.262 | 80.161 | 75.713 | 71.001 | 8,64% | -1,01% | 8,41% | 40,30% |
| SOL | 67.38 | 1.10248 | 107,86 | 97,69 | 84,78 | 15,01% | -2,67% | 15,90% | 61,02% |
| DOGE | 59.32 | 0.001 | 0.08866 | 0.08361 | 0.08787 | 8,88% | -8,16% | 12,55% | 30,87% |

## Dettaglio asset

### BTC

- Prezzo: **84.377 $**
- Punteggio tecnico: **6 / 12**
- Verdetto: **COSTRUTTIVO MA NON CONFERMATO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum misto** (0)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 7.625e+04 -> 7.494e+04. Ultimi massimi: 8.226e+04 -> 8.736e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-09-21 87.364; livello più vicino 23.6% a 80.374; stato NON ATTIVO; confluenza: invalidazione rialzista.
- Punteggio pattern: **+2**
  - rialzista dominante: Doppio minimo (CONFERMATO RECENTE, +2); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **74.945**
- Resistenza più vicina: **87.364**

Pattern classici e ciclo di vita:

- Doppio minimo: **CONFERMATO RECENTE** (+2)
  - Due minimi simili vicino a 74.945 tra 2026-09-02 e 2026-09-15. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (6 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 89.580; progresso corrente: 28,90%. Relazione prezzo/neckline: sopra neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (6g); progresso 28,90%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (39 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 370,93%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (39g); progresso 370,93%; prezzo sopra neckline.
- Eve and Adam Bottom: **CONFERMATO RECENTE** (+2)
  - Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (6 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 89.580; progresso corrente: 28,90%. Relazione prezzo/neckline: sopra neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (6g); progresso 28,90%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 87.364 tra 2026-09-03 e 2026-09-21. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 74.945; target 62.525; distanza dalla neckline 12,59%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 49 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 46,11%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 87.364 dal 2026-09-03 al 2026-09-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 74.945; target 62.525; distanza dalla neckline 12,59%; prezzo sopra neckline.

### SOL

- Prezzo: **120,68 $**
- Punteggio tecnico: **8 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (2)
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
  - Due minimi simili vicino a 96,23 tra 2026-09-02 e 2026-09-16. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (9 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: 124,54%. Relazione prezzo/neckline: sopra neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (9g); progresso 124,54%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (39 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 522,35%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (39g); progresso 522,35%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 96,23 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (9 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: 124,54%. Relazione prezzo/neckline: sopra neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (9g); progresso 124,54%; prezzo sopra neckline.
- Doppio massimo: **INVALIDATO** (0)
  - Due massimi simili vicino a 110,04 tra 2026-08-27 e 2026-09-06. Neckline ribassista stimata: 97,45. Breakout neckline: 2026-09-15 (12 giorni fa). Stato: INVALIDATO. Target teorico: 84,86; progresso corrente: -184,53%. Relazione prezzo/neckline: sopra neckline.
  - neckline 97,45; target 84,86; breakout 2026-09-15 (12g); progresso -184,53%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 49 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 70,71%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 83,81 dal 2026-07-04 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 49 giorni.
  - neckline 70,69; target 57,58; distanza dalla neckline 70,71%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.09591 $**
- Punteggio tecnico: **10 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (2)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 0.08028 -> 0.07841. Ultimi massimi: 0.09421 -> 0.1053.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-08-01 0.06797 -> 2026-09-22 0.10528; livello più vicino 23.6% a 0.09648; stato TESTATO; confluenza: neckline rialzista, invalidazione rialzista.
- Punteggio pattern: **+2**
  - rialzista dominante: Doppio minimo (CONFERMATO RECENTE, +2); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.07841**
- Resistenza più vicina: **0.10528**

Pattern classici e ciclo di vita:

- Doppio minimo: **CONFERMATO RECENTE** (+2)
  - Due minimi simili vicino a 0.07841 tra 2026-09-02 e 2026-09-16. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (6 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 0.11001; progresso corrente: 10,76%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.09421; target 0.11001; breakout 2026-09-21 (6g); progresso 10,76%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06835 dal 2026-07-13 al 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (39 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07926; progresso corrente: 405,24%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07926; breakout 2026-08-19 (39g); progresso 405,24%; prezzo sopra neckline.
- Adam and Eve Bottom: **CONFERMATO RECENTE** (+2)
  - Pattern Adam and Eve Bottom vicino a 0.07841 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (6 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 0.11001; progresso corrente: 10,76%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.09421; target 0.11001; breakout 2026-09-21 (6g); progresso 10,76%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.10528 tra 2026-08-22 e 2026-09-22. Neckline ribassista stimata: 0.07841. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 0.07841; target 0.05153; distanza dalla neckline 22,33%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 47 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 41,10%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07380 dal 2026-07-26 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 47 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 41,10%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                                                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:----------------------------------------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-09-21 | 80.374 | 76.050 | 72.556 | 69.061 | 64.086 | 23.6% / 80.374 | NON ATTIVO | invalidazione rialzista | 0 |
| SOL | DOWN 2026-08-27 -> 2026-09-16 | 99,49 | 101,50 | 103,13 | 104,76 | 107,08 | 78.6% / 107,08 | RECUPERATO | resistenza tecnica, neckline rialzista, invalidazione rialzista | +1 |
| DOGE | UP 2026-08-01 -> 2026-09-22 | 0.09648 | 0.09103 | 0.08663 | 0.08222 | 0.07596 | 23.6% / 0.09648 | TESTATO | neckline rialzista, invalidazione rialzista | 0 |

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

- **BTC**: 30/30 previsioni controllate su 81 fatte. Stato: **ATTIVA**.
- **SOL**: 30/30 previsioni controllate su 81 fatte. Stato: **ATTIVA**.
- **DOGE**: 30/30 previsioni controllate su 81 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 81 | 30 | 30/30 [██████████] | 51 | ATTIVA | 2026-09-28 / tra 1 giorno |
| SOL | 81 | 30 | 30/30 [██████████] | 51 | ATTIVA | 2026-09-28 / tra 1 giorno |
| DOGE | 81 | 30 | 30/30 [██████████] | 51 | ATTIVA | 2026-09-28 / tra 1 giorno |

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

Generato: 2026-09-27 05:33 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 84.377 $          | 84.377 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.09591 $         | 0.09591 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 84.377 $          | 84.377 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.09591 $         | 0.09591 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 84.377 $          | 84.377 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.09591 $         | 0.09591 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 84.377 $          | 84.377 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.09591 $         | 0.09591 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 84.377 $          | 84.377 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.09591 $         | 0.09591 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 84.377 $          | 84.360 $        | -0,0203%     |
| Exchange Microstructure | SOL     | price             | OK      | 120,68 $          | 120,44 $        | -0,1947%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.09591 $         | 0.09583 $       | -0,0847%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 120,68 $          | 120,68 $        | +0,0000%     |

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


<!-- SOL_LONG_TERM_CONE_HISTORY_START -->
## SOL Long-Term Cone History

[SOL Long-Term Cone History](sol_long_term_history/README.md)
<!-- SOL_LONG_TERM_CONE_HISTORY_END -->
