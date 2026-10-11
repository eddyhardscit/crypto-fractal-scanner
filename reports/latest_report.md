<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-10-11 05:33 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 0 | NEUTRALE / COSTRUTTIVO | HOLD / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | +2 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +1 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **0**, spot = **HOLD / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **+2**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+1**, spot = **STAI ALLA FINESTRA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

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
- Conferme: Prima resistenza sopra 87.146; conferma del doppio minimo sopra 82.262.
- Invalidazioni: Sotto 82.571 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+2**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **HOLD LEGGERO / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 123,48; milestone analogiche 121,46 / 122,68, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 104,06 / 96,23 / 62,19.

### DOGE

- Global Confluence: **+1**
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
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 2; EMA200 circa 111,41 $; upside verso EMA200 +1,70%. Non autorizza leva e non aggiunge punti automatici.
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

Generato: 2026-10-11 05:33 UTC

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

Segnali totali salvati: **261**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-11 | BTC | 83.006,99 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-11 | DOGE | 0.08535 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-11 | SOL | 109,56 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-10 | BTC | 82.650,00 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-10 | DOGE | 0.08645 | -1 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-10 | SOL | 110,05 | +6 | +3 | +3 | 0 | +1 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-09 | BTC | 82.441,21 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-09 | DOGE | 0.08534 | 0 | +2 | +2 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-09 | SOL | 110,52 | +1 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-08 | BTC | 82.929,12 | +2 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-08 | DOGE | 0.08776 | -3 | -1 | -1 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-08 | SOL | 115,60 | +1 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 87 | 86 | 85 | 84 | 82 | 80 | 77 | 74 | 69 | 63 | 48 | 34 |
| SOL | 87 | 86 | 85 | 84 | 82 | 80 | 77 | 74 | 69 | 63 | 48 | 34 |
| DOGE | 87 | 86 | 85 | 84 | 82 | 80 | 77 | 74 | 69 | 63 | 48 | 34 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-28 | 45g | 2026-10-12 | domani |
| SOL | 2026-08-28 | 45g | 2026-10-12 | domani |
| DOGE | 2026-08-28 | 45g | 2026-10-12 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 78 | 52,56% | +0,31% | +0,29% | UTILE |
| BTC | 2g | 78 | 51,28% | +0,56% | +0,50% | UTILE |
| BTC | 3g | 78 | 46,15% | +0,69% | +0,60% | UTILE |
| BTC | 5g | 77 | 42,86% | +1,42% | +1,26% | UTILE |
| BTC | 7g | 75 | 53,33% | +2,25% | +2,10% | UTILE |
| BTC | 10g | 72 | 59,72% | +3,30% | +3,18% | UTILE |
| BTC | 14g | 69 | 60,87% | +4,85% | +4,80% | UTILE |
| BTC | 21g | 66 | 74,24% | +8,41% | +8,31% | UTILE |
| BTC | 30g | 60 | 95,00% | +12,44% | +11,72% | UTILE |
| BTC | 45g | 45 | 93,33% | +22,33% | +19,39% | PRIMA CALIBRAZIONE |
| BTC | 60g | 32 | 90,62% | +27,86% | +23,17% | PRIMA CALIBRAZIONE |
| SOL | 1g | 78 | 47,44% | +0,23% | +0,15% | UTILE |
| SOL | 2g | 77 | 45,45% | +0,73% | +0,64% | UTILE |
| SOL | 3g | 76 | 50,00% | +1,25% | +1,13% | UTILE |
| SOL | 5g | 74 | 54,05% | +2,39% | +2,31% | UTILE |
| SOL | 7g | 72 | 59,72% | +3,71% | +3,78% | UTILE |
| SOL | 10g | 69 | 62,32% | +5,79% | +5,90% | UTILE |
| SOL | 14g | 66 | 71,21% | +8,60% | +9,15% | UTILE |
| SOL | 21g | 61 | 83,61% | +15,23% | +14,65% | UTILE |
| SOL | 30g | 56 | 82,14% | +20,61% | +17,08% | PRIMA CALIBRAZIONE |
| SOL | 45g | 41 | 73,17% | +38,98% | +20,21% | PRIMA CALIBRAZIONE |
| SOL | 60g | 27 | 59,26% | +47,35% | +14,89% | FEEDBACK RAPIDO |
| DOGE | 1g | 79 | 48,10% | +0,03% | +0,02% | UTILE |
| DOGE | 2g | 78 | 46,15% | +0,30% | -0,01% | UTILE |
| DOGE | 3g | 78 | 41,03% | +0,57% | +0,15% | UTILE |
| DOGE | 5g | 76 | 44,74% | +1,37% | +0,15% | UTILE |
| DOGE | 7g | 75 | 48,00% | +2,08% | +0,19% | UTILE |
| DOGE | 10g | 73 | 41,10% | +2,72% | -0,13% | UTILE |
| DOGE | 14g | 70 | 54,29% | +4,55% | +2,65% | UTILE |
| DOGE | 21g | 65 | 60,00% | +8,47% | +2,51% | UTILE |
| DOGE | 30g | 59 | 69,49% | +11,63% | +5,25% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 46 | 47,83% | +21,61% | +4,28% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 32 | 37,50% | +26,82% | -3,10% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 78 | 52,56% | +0,31% | +0,29% | -0,24% | +0,83% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 84 | 50,00% | +0,23% | +0,31% | -0,28% | +0,74% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 84 | 50,00% | +0,23% | +0,31% | -0,28% | +0,74% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 79 | 44,30% | +0,25% | -0,01% | -0,22% | +0,78% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,55% | -0,03% | -0,23% | +1,11% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,49% | -0,49% | -1,07% | -0,05% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 78 | 51,28% | +0,56% | +0,50% | -0,22% | +1,25% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 83 | 53,01% | +0,52% | +0,65% | -0,20% | +1,21% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 83 | 53,01% | +0,52% | +0,65% | -0,20% | +1,21% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 78 | 43,59% | +0,51% | -0,02% | -0,11% | +1,19% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,89% | -0,12% | -0,02% | +1,61% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,28% | -0,28% | -1,06% | +0,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 78 | 46,15% | +0,69% | +0,60% | -1,25% | +2,46% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 82 | 51,22% | +0,84% | +0,92% | -1,29% | +2,55% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 82 | 51,22% | +0,84% | +0,92% | -1,29% | +2,55% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 77 | 36,36% | +0,86% | -0,23% | -1,22% | +2,57% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,44% | -0,66% | -1,08% | +3,10% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,50% | -0,50% | -1,88% | +1,29% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 77 | 42,86% | +1,42% | +1,26% | -1,91% | +3,87% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 80 | 47,50% | +1,66% | +1,68% | -1,87% | +4,07% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 80 | 47,50% | +1,66% | +1,68% | -1,87% | +4,07% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 75 | 41,33% | +1,52% | -0,74% | -1,82% | +4,01% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 34 | 35,29% | +3,06% | -2,33% | -1,68% | +5,50% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 75 | 53,33% | +2,25% | +2,10% | -2,17% | +5,08% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 78 | 55,13% | +2,51% | +2,38% | -2,11% | +5,27% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 78 | 55,13% | +2,51% | +2,38% | -2,11% | +5,27% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 73 | 45,21% | +2,48% | -1,01% | -2,08% | +5,24% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 32 | 34,38% | +4,64% | -3,91% | -1,85% | +7,80% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 72 | 59,72% | +3,30% | +3,18% | -2,39% | +6,36% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 76 | 65,79% | +3,42% | +3,40% | -2,34% | +6,48% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 76 | 65,79% | +3,42% | +3,40% | -2,34% | +6,48% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 70 | 48,57% | +3,48% | -0,32% | -2,30% | +6,59% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 29 | 41,38% | +5,56% | -4,39% | -1,70% | +9,12% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -1,21% | -1,21% | -3,81% | +1,86% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 69 | 60,87% | +4,85% | +4,80% | -2,63% | +8,51% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 74 | 62,16% | +4,75% | +4,84% | -2,66% | +8,46% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 74 | 62,16% | +4,75% | +4,84% | -2,66% | +8,46% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 67 | 55,22% | +5,03% | +1,41% | -2,61% | +8,78% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 29 | 24,14% | +5,09% | -4,15% | -1,91% | +9,57% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,11% | -0,11% | -4,30% | +2,85% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 66 | 74,24% | +8,41% | +8,31% | -2,80% | +12,27% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 69 | 78,26% | +8,34% | +8,34% | -2,78% | +12,22% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 69 | 78,26% | +8,34% | +8,34% | -2,78% | +12,22% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 62 | 58,06% | +8,84% | +1,49% | -2,74% | +12,73% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 28 | 46,43% | +9,04% | -4,92% | -2,22% | +12,89% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 60 | 95,00% | +12,44% | +11,72% | -2,99% | +16,55% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 63 | 92,06% | +12,40% | +12,40% | -2,97% | +16,63% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 63 | 92,06% | +12,40% | +12,40% | -2,97% | +16,63% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 58 | 63,79% | +12,38% | +0,89% | -2,84% | +16,78% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,37% | -2,02% | -2,62% | +17,60% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 45 | 93,33% | +22,33% | +19,39% | -2,39% | +27,07% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 48 | 100,00% | +22,62% | +22,62% | -2,39% | +27,24% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 48 | 100,00% | +22,62% | +22,62% | -2,39% | +27,24% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 43 | 48,84% | +22,81% | -2,73% | -2,15% | +27,46% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 16 | 50,00% | +18,39% | -8,74% | -1,64% | +24,20% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 32 | 90,62% | +27,86% | +23,17% | -2,96% | +32,94% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 34 | 100,00% | +27,66% | +27,66% | -3,00% | +32,81% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 34 | 100,00% | +27,66% | +27,66% | -3,00% | +32,81% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 30 | 100,00% | +28,33% | +28,33% | -2,80% | +33,68% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 29 | 41,38% | +28,03% | -5,53% | -2,74% | +33,36% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 4 | 0,00% | +33,67% | -33,67% | -1,55% | +38,08% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 79 | 48,10% | +0,03% | +0,02% | -0,75% | +1,08% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 85 | 58,82% | +0,01% | +0,56% | -0,78% | +1,01% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 85 | 58,82% | +0,01% | +0,56% | -0,78% | +1,01% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 79 | 50,63% | -0,07% | +0,12% | -0,88% | +0,92% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 47 | 40,43% | -0,05% | -0,63% | -0,92% | +0,67% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 78 | 46,15% | +0,30% | -0,01% | -0,83% | +1,66% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 84 | 59,52% | +0,14% | +0,89% | -0,95% | +1,44% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 84 | 59,52% | +0,14% | +0,89% | -0,95% | +1,44% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 78 | 52,56% | -0,17% | +0,07% | -1,27% | +1,13% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 46 | 41,30% | +0,27% | -1,32% | -0,93% | +1,22% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 78 | 41,03% | +0,57% | +0,15% | -2,49% | +3,75% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 83 | 57,83% | +0,31% | +1,25% | -2,64% | +3,49% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 83 | 57,83% | +0,31% | +1,25% | -2,64% | +3,49% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 77 | 44,16% | -0,31% | -0,19% | -2,89% | +2,83% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 45 | 31,11% | +0,54% | -2,23% | -2,66% | +3,71% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 76 | 44,74% | +1,37% | +0,15% | -3,50% | +6,21% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 81 | 54,32% | +1,05% | +1,71% | -3,73% | +5,94% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 81 | 54,32% | +1,05% | +1,71% | -3,73% | +5,94% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 75 | 48,00% | +0,26% | -1,13% | -4,12% | +5,21% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 44 | 31,82% | +1,94% | -4,85% | -3,72% | +6,77% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 75 | 48,00% | +2,08% | +0,19% | -4,08% | +8,18% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 79 | 56,96% | +1,99% | +1,70% | -4,20% | +7,98% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 79 | 56,96% | +1,99% | +1,70% | -4,20% | +7,98% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 73 | 43,84% | +1,03% | -1,35% | -4,66% | +7,02% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 44 | 27,27% | +3,07% | -6,50% | -4,35% | +8,81% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 73 | 41,10% | +2,72% | -0,13% | -4,77% | +10,13% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 76 | 53,95% | +2,68% | +1,39% | -4,75% | +9,99% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 76 | 53,95% | +2,68% | +1,39% | -4,75% | +9,99% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 70 | 45,71% | +1,40% | -1,77% | -5,28% | +8,53% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 43 | 30,23% | +3,70% | -7,04% | -4,91% | +11,04% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 70 | 54,29% | +4,55% | +2,65% | -5,49% | +13,70% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 73 | 63,01% | +4,21% | +3,15% | -5,44% | +13,34% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 73 | 63,01% | +4,21% | +3,15% | -5,44% | +13,34% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 67 | 47,76% | +2,21% | -1,49% | -6,06% | +10,78% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 43 | 39,53% | +4,51% | -5,45% | -5,57% | +13,12% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 65 | 60,00% | +8,47% | +2,51% | -5,17% | +19,56% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 68 | 57,35% | +8,79% | +4,21% | -5,19% | +19,71% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 68 | 57,35% | +8,79% | +4,21% | -5,19% | +19,71% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 62 | 56,45% | +6,83% | -1,96% | -5,84% | +16,87% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 41 | 43,90% | +6,23% | -7,20% | -5,36% | +16,47% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 70,00% | +6,74% | +1,36% | -4,20% | +19,90% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 59 | 69,49% | +11,63% | +5,25% | -5,55% | +25,55% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 62 | 70,97% | +11,91% | +7,46% | -5,52% | +26,03% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 62 | 70,97% | +11,91% | +7,46% | -5,52% | +26,03% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 56 | 58,93% | +10,47% | -2,55% | -6,31% | +23,79% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 35 | 48,57% | +9,69% | -7,71% | -5,84% | +22,14% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 88,89% | +19,48% | +12,44% | -5,48% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 46 | 47,83% | +21,61% | +4,28% | -4,57% | +38,95% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 47 | 59,57% | +22,08% | +8,66% | -4,46% | +39,37% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 47 | 59,57% | +22,08% | +8,66% | -4,46% | +39,37% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 41 | 12,20% | +19,07% | -14,29% | -5,37% | +37,20% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 31 | 3,23% | +21,52% | -22,01% | -5,10% | +38,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +24,92% | +12,69% | -3,96% | +37,45% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 32 | 37,50% | +26,82% | -3,10% | -4,35% | +44,37% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 34 | 52,94% | +27,26% | +8,06% | -4,36% | +44,55% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 34 | 52,94% | +27,26% | +8,06% | -4,36% | +44,55% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | +26,49% | +11,04% | -4,40% | +44,30% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 30 | 0,00% | +27,32% | -27,32% | -4,76% | +43,74% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 22 | 0,00% | +25,52% | -25,52% | -4,86% | +42,69% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +38,20% | +19,48% | -1,31% | +51,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 78 | 47,44% | +0,23% | +0,15% | -0,51% | +1,09% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 80 | 55,00% | +0,22% | +0,50% | -0,61% | +1,06% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 83 | 54,22% | +0,25% | +0,44% | -0,58% | +1,09% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 78 | 44,87% | +0,21% | -0,14% | -0,67% | +1,04% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 58 | 44,83% | +0,45% | -0,03% | -0,53% | +1,39% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 77 | 45,45% | +0,73% | +0,64% | -0,49% | +1,79% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 79 | 50,63% | +0,63% | +0,83% | -0,71% | +1,55% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 82 | 50,00% | +0,62% | +0,79% | -0,68% | +1,59% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 77 | 41,56% | +0,45% | -0,23% | -0,68% | +1,56% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 57 | 47,37% | +0,57% | +0,14% | -0,69% | +1,64% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 76 | 50,00% | +1,25% | +1,13% | -2,05% | +3,77% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 78 | 53,85% | +1,09% | +1,46% | -2,20% | +3,59% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 81 | 53,09% | +1,06% | +1,39% | -2,16% | +3,58% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 76 | 43,42% | +0,67% | -0,51% | -2,22% | +3,14% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 57 | 47,37% | +0,64% | +0,14% | -2,20% | +3,12% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 74 | 54,05% | +2,39% | +2,31% | -2,83% | +6,09% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 76 | 55,26% | +2,16% | +2,26% | -2,97% | +5,87% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 79 | 54,43% | +2,10% | +2,15% | -2,93% | +5,80% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 74 | 44,59% | +1,75% | -0,84% | -3,02% | +5,30% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 56 | 50,00% | +0,92% | +0,24% | -3,09% | +4,53% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 72 | 59,72% | +3,71% | +3,78% | -3,21% | +7,90% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 74 | 62,16% | +3,43% | +3,27% | -3,36% | +7,65% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 77 | 62,34% | +3,30% | +3,15% | -3,33% | +7,50% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 72 | 40,28% | +2,43% | -1,54% | -3,44% | +6,72% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 54 | 46,30% | +0,97% | +0,35% | -3,56% | +5,35% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 69 | 62,32% | +5,79% | +5,90% | -3,43% | +10,26% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 71 | 67,61% | +5,58% | +5,43% | -3,60% | +9,85% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 74 | 66,22% | +5,35% | +5,22% | -3,60% | +9,61% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 69 | 44,93% | +3,88% | -1,61% | -3,77% | +8,42% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 51 | 49,02% | +1,47% | +0,70% | -3,91% | +6,38% | PRIMA CALIBRAZIONE |

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

Generato: 2026-10-11 05:33 UTC

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
| BTC | 87 | UTILE | 84 | 26 | 17 | 0 | Famiglia statistica | 1g | 50,00% | +0,31% | campione utile, valutare con prudenza |
| SOL | 87 | UTILE | 80 | 31 | 16 | 0 | Famiglia statistica | 1g | 55,00% | +0,50% | campione utile, valutare con prudenza |
| DOGE | 87 | UTILE | 85 | 32 | 17 | 0 | Famiglia statistica | 1g | 58,82% | +0,56% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 34 | 41,18% | -0,03% | +0,55% | -0,23% | +1,11% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 84 | 50,00% | +0,31% | +0,23% | -0,28% | +0,74% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 8 | 37,50% | -0,49% | -0,49% | -1,07% | -0,05% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 79 | 44,30% | -0,01% | +0,25% | -0,22% | +0,78% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 34 | 41,18% | -0,12% | +0,89% | -0,02% | +1,61% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 83 | 53,01% | +0,65% | +0,52% | -0,20% | +1,21% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 8 | 25,00% | -0,28% | -0,28% | -1,06% | +0,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 78 | 43,59% | -0,02% | +0,51% | -0,11% | +1,19% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 34 | 35,29% | -0,66% | +1,44% | -1,08% | +3,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Famiglia statistica | 82 | 51,22% | +0,92% | +0,84% | -1,29% | +2,55% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 8 | 25,00% | -0,50% | -0,50% | -1,88% | +1,29% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 77 | 36,36% | -0,23% | +0,86% | -1,22% | +2,57% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 34 | 35,29% | -2,33% | +3,06% | -1,68% | +5,50% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 80 | 47,50% | +1,68% | +1,66% | -1,87% | +4,07% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 75 | 41,33% | -0,74% | +1,52% | -1,82% | +4,01% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 32 | 34,38% | -3,91% | +4,64% | -1,85% | +7,80% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 78 | 55,13% | +2,38% | +2,51% | -2,11% | +5,27% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 73 | 45,21% | -1,01% | +2,48% | -2,08% | +5,24% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 29 | 41,38% | -4,39% | +5,56% | -1,70% | +9,12% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 76 | 65,79% | +3,40% | +3,42% | -2,34% | +6,48% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | -1,21% | -1,21% | -3,81% | +1,86% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 70 | 48,57% | -0,32% | +3,48% | -2,30% | +6,59% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 29 | 24,14% | -4,15% | +5,09% | -1,91% | +9,57% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 74 | 62,16% | +4,84% | +4,75% | -2,66% | +8,46% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 7 | 42,86% | -0,11% | -0,11% | -4,30% | +2,85% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 67 | 55,22% | +1,41% | +5,03% | -2,61% | +8,78% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 28 | 46,43% | -4,92% | +9,04% | -2,22% | +12,89% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 69 | 78,26% | +8,34% | +8,34% | -2,78% | +12,22% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 62 | 58,06% | +1,49% | +8,84% | -2,74% | +12,73% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 24 | 66,67% | -2,02% | +13,37% | -2,62% | +17,60% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 63 | 92,06% | +12,40% | +12,40% | -2,97% | +16,63% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 58 | 63,79% | +0,89% | +12,38% | -2,84% | +16,78% | PESO OK | 0,0 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 16 | 50,00% | -8,74% | +18,39% | -1,64% | +24,20% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 48 | 100,00% | +22,62% | +22,62% | -2,39% | +27,24% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 43 | 48,84% | -2,73% | +22,81% | -2,15% | +27,46% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 4 | 0,00% | -33,67% | +33,67% | -1,55% | +38,08% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 34 | 100,00% | +27,66% | +27,66% | -3,00% | +32,81% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 29 | 41,38% | -5,53% | +28,03% | -2,74% | +33,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 47 | 40,43% | -0,63% | -0,05% | -0,92% | +0,67% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 85 | 58,82% | +0,56% | +0,01% | -0,78% | +1,01% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 11 | 63,64% | +2,53% | +2,82% | +0,75% | +3,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 79 | 50,63% | +0,12% | -0,07% | -0,88% | +0,92% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 46 | 41,30% | -1,32% | +0,27% | -0,93% | +1,22% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 84 | 59,52% | +0,89% | +0,14% | -0,95% | +1,44% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 11 | 45,45% | +2,65% | +2,89% | +1,08% | +5,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 78 | 52,56% | +0,07% | -0,17% | -1,27% | +1,13% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 45 | 31,11% | -2,23% | +0,54% | -2,66% | +3,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 83 | 57,83% | +1,25% | +0,31% | -2,64% | +3,49% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 11 | 54,55% | +2,62% | +2,81% | -1,35% | +6,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 77 | 44,16% | -0,19% | -0,31% | -2,89% | +2,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 44 | 31,82% | -4,85% | +1,94% | -3,72% | +6,77% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 81 | 54,32% | +1,71% | +1,05% | -3,73% | +5,94% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 11 | 36,36% | +2,02% | +2,17% | -2,50% | +9,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 75 | 48,00% | -1,13% | +0,26% | -4,12% | +5,21% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 44 | 27,27% | -6,50% | +3,07% | -4,35% | +8,81% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 79 | 56,96% | +1,70% | +1,99% | -4,20% | +7,98% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 11 | 45,45% | +0,78% | +0,88% | -3,00% | +9,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 73 | 43,84% | -1,35% | +1,03% | -4,66% | +7,02% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 43 | 30,23% | -7,04% | +3,70% | -4,91% | +11,04% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 76 | 53,95% | +1,39% | +2,68% | -4,75% | +9,99% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 70 | 45,71% | -1,77% | +1,40% | -5,28% | +8,53% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 43 | 39,53% | -5,45% | +4,51% | -5,57% | +13,12% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 73 | 63,01% | +3,15% | +4,21% | -5,44% | +13,34% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 11 | 45,45% | +2,03% | +5,60% | -4,35% | +14,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 67 | 47,76% | -1,49% | +2,21% | -6,06% | +10,78% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 41 | 43,90% | -7,20% | +6,23% | -5,36% | +16,47% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 68 | 57,35% | +4,21% | +8,79% | -5,19% | +19,71% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 10 | 70,00% | +1,36% | +6,74% | -4,20% | +19,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 62 | 56,45% | -1,96% | +6,83% | -5,84% | +16,87% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Classic technical | 35 | 48,57% | -7,71% | +9,69% | -5,84% | +22,14% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 62 | 70,97% | +7,46% | +11,91% | -5,52% | +26,03% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 9 | 88,89% | +12,44% | +19,48% | -5,48% | +30,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 56 | 58,93% | -2,55% | +10,47% | -6,31% | +23,79% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 31 | 3,23% | -22,01% | +21,52% | -5,10% | +38,53% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Famiglia statistica | 47 | 59,57% | +8,66% | +22,08% | -4,46% | +39,37% | PESO OK | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 7 | 71,43% | +12,69% | +24,92% | -3,96% | +37,45% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 41 | 12,20% | -14,29% | +19,07% | -5,37% | +37,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 22 | 0,00% | -25,52% | +25,52% | -4,86% | +42,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 34 | 52,94% | +8,06% | +27,26% | -4,36% | +44,55% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 4 | 75,00% | +19,48% | +38,20% | -1,31% | +51,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 30 | 0,00% | -27,32% | +27,32% | -4,76% | +43,74% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 1g | BREVE | Classic technical | 58 | 44,83% | -0,03% | +0,45% | -0,53% | +1,39% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 80 | 55,00% | +0,50% | +0,22% | -0,61% | +1,06% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 78 | 44,87% | -0,14% | +0,21% | -0,67% | +1,04% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 57 | 47,37% | +0,14% | +0,57% | -0,69% | +1,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 79 | 50,63% | +0,83% | +0,63% | -0,71% | +1,55% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 77 | 41,56% | -0,23% | +0,45% | -0,68% | +1,56% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 57 | 47,37% | +0,14% | +0,64% | -2,20% | +3,12% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 78 | 53,85% | +1,46% | +1,09% | -2,20% | +3,59% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 76 | 43,42% | -0,51% | +0,67% | -2,22% | +3,14% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 56 | 50,00% | +0,24% | +0,92% | -3,09% | +4,53% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 76 | 55,26% | +2,26% | +2,16% | -2,97% | +5,87% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 74 | 44,59% | -0,84% | +1,75% | -3,02% | +5,30% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 54 | 46,30% | +0,35% | +0,97% | -3,56% | +5,35% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 74 | 62,16% | +3,27% | +3,43% | -3,36% | +7,65% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 72 | 40,28% | -1,54% | +2,43% | -3,44% | +6,72% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 51 | 49,02% | +0,70% | +1,47% | -3,91% | +6,38% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 71 | 67,61% | +5,43% | +5,58% | -3,60% | +9,85% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 69 | 44,93% | -1,61% | +3,88% | -3,77% | +8,42% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 48 | 47,92% | +1,02% | +2,85% | -4,62% | +8,08% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 69 | 76,81% | +8,64% | +8,45% | -4,08% | +13,57% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 66 | 42,42% | -2,57% | +6,08% | -4,32% | +11,49% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 43 | 62,79% | -0,68% | +11,00% | -4,55% | +16,01% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 64 | 84,38% | +15,14% | +15,18% | -4,12% | +20,66% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 61 | 54,10% | -4,93% | +12,66% | -4,50% | +18,21% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Classic technical | 42 | 54,76% | -4,29% | +22,25% | -4,70% | +27,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 58 | 89,66% | +19,97% | +22,63% | -4,36% | +29,21% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 59 | 44,07% | -7,91% | +20,65% | -4,73% | +26,78% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 29 | 27,59% | -21,70% | +34,51% | -3,61% | +44,10% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 43 | 74,42% | +23,73% | +38,94% | -3,51% | +47,00% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +28,91% | +28,91% | -3,55% | +37,55% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 45 | 26,67% | -24,88% | +37,50% | -4,01% | +45,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 21 | 0,00% | -53,73% | +53,73% | -4,64% | +60,15% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 30 | 73,33% | +32,45% | +50,64% | -4,89% | +58,37% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +47,10% | +47,10% | -5,94% | +54,98% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 32 | 12,50% | -40,55% | +49,02% | -5,31% | +56,49% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 79 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 85 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 102 | 39,22% | -0,27% |
| BTC | BREVE | Famiglia statistica | 249 | 51,41% | +0,62% |
| BTC | BREVE | Microstruttura exchange | 24 | 29,17% | -0,42% |
| BTC | BREVE | Tecnico | 234 | 41,45% | -0,09% |
| BTC | SETTIMANALE | Classic technical | 95 | 36,84% | -3,49% |
| BTC | SETTIMANALE | Famiglia statistica | 234 | 55,98% | +2,47% |
| BTC | SETTIMANALE | Microstruttura exchange | 23 | 26,09% | -1,66% |
| BTC | SETTIMANALE | Tecnico | 218 | 44,95% | -0,69% |
| BTC | SWING | Classic technical | 57 | 35,09% | -4,53% |
| BTC | SWING | Famiglia statistica | 143 | 69,93% | +6,53% |
| BTC | SWING | Microstruttura exchange | 12 | 58,33% | +0,59% |
| BTC | SWING | Tecnico | 129 | 56,59% | +1,45% |
| BTC | MEDIO | Classic technical | 44 | 54,55% | -7,34% |
| BTC | MEDIO | Famiglia statistica | 145 | 96,55% | +19,36% |
| BTC | MEDIO | Microstruttura exchange | 9 | 100,00% | +9,68% |
| BTC | MEDIO | Tecnico | 130 | 53,85% | -1,74% |
| DOGE | BREVE | Classic technical | 138 | 37,68% | -1,38% |
| DOGE | BREVE | Famiglia statistica | 252 | 58,73% | +0,90% |
| DOGE | BREVE | Microstruttura exchange | 33 | 54,55% | +2,60% |
| DOGE | BREVE | Tecnico | 234 | 49,15% | +0,00% |
| DOGE | SETTIMANALE | Classic technical | 131 | 29,77% | -6,12% |
| DOGE | SETTIMANALE | Famiglia statistica | 236 | 55,08% | +1,60% |
| DOGE | SETTIMANALE | Microstruttura exchange | 33 | 45,45% | +1,16% |
| DOGE | SETTIMANALE | Tecnico | 218 | 45,87% | -1,41% |
| DOGE | SWING | Classic technical | 84 | 41,67% | -6,31% |
| DOGE | SWING | Famiglia statistica | 141 | 60,28% | +3,66% |
| DOGE | SWING | Microstruttura exchange | 21 | 57,14% | +1,71% |
| DOGE | SWING | Tecnico | 129 | 51,94% | -1,72% |
| DOGE | MEDIO | Classic technical | 88 | 20,45% | -17,20% |
| DOGE | MEDIO | Famiglia statistica | 143 | 62,94% | +8,00% |
| DOGE | MEDIO | Microstruttura exchange | 20 | 80,00% | +13,94% |
| DOGE | MEDIO | Tecnico | 127 | 29,92% | -12,19% |
| SOL | BREVE | Classic technical | 172 | 46,51% | +0,08% |
| SOL | BREVE | Famiglia statistica | 237 | 53,16% | +0,93% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 231 | 43,29% | -0,29% |
| SOL | SETTIMANALE | Classic technical | 161 | 48,45% | +0,43% |
| SOL | SETTIMANALE | Famiglia statistica | 221 | 61,54% | +3,62% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 215 | 43,26% | -1,32% |
| SOL | SWING | Classic technical | 91 | 54,95% | +0,22% |
| SOL | SWING | Famiglia statistica | 133 | 80,45% | +11,77% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 127 | 48,03% | -3,70% |
| SOL | MEDIO | Classic technical | 92 | 33,70% | -21,06% |
| SOL | MEDIO | Famiglia statistica | 131 | 80,92% | +24,06% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 12 | 100,00% | +28,96% |
| SOL | MEDIO | Tecnico | 136 | 30,88% | -21,20% |

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

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato                | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:---------------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         87 |              63 |          24 | CALIBRAZIONE LEGGERA | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         87 |              63 |          24 | CALIBRAZIONE LEGGERA | 1,59%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         87 |              63 |          24 | CALIBRAZIONE LEGGERA | 14,29%           | 4,76%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                             |
|:--------|:---------------|:---------------|:------------------------------------------------------|
| BTC     | ALTO           | MOLTO ALTO     | leva da limitare; 2x/3x solo con invalidazione chiara |
| SOL     | MEDIO          | MOLTO ALTO     | leva da limitare; 2x/3x solo con invalidazione chiara |
| DOGE    | MEDIO          | MOLTO ALTO     | leva da limitare; 2x/3x solo con invalidazione chiara |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-10-11 05:33 UTC

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
| BTC | 0 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD / ATTESA CONFERME | Prima resistenza sopra 87.146; conferma del doppio minimo sopra 82.262. | Sotto 82.571 il quadro tecnico peggiora. |
| SOL | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 123,48; milestone analogiche 121,46 / 122,68, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 104,06 / 96,23 / 62,19. |
| DOGE | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.10528 migliora; sopra 0.07997 viene invalidato il pattern ribassista dominante. | Sotto 0.07841 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -1 | 0 | -1 | 0 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| SOL | +3 | 0 | +3 | 0 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +2 |
| DOGE | +3 | 0 | +3 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +1 |

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

- Famiglia statistica: **-1** — Scanner grezzo -1, Market Regime grezzo 0, match regime 2. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-1** — Casi positivi 45,00%, return centrale 30g -2,05%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 2, positivi 30g 0,00%, return p50 -8,36%.
- Scanner path: **0** — Controlli disponibili 85. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+1** — Score tecnico 2/12, verdetto neutrale / misto, trend rialzista, struttura compressione / triangolo, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / MATURO; ribassista Doppio massimo / ATTIVO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -1/12, verdetto NEUTRALE / MISTO, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff RANGE / FASE NON CHIARA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.50; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 1, campioni 4h 9 su 4.00h; candidato +1, peso Global +0 (LOCKED / RACCOLTA 7G). Bias POSITIVA / CANDIDATA, ANCORA NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +1 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — BTC: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Prima resistenza sopra 87.146; conferma del doppio minimo sopra 82.262.

Invalidazioni: Sotto 82.571 il quadro tecnico peggiora.

### SOL

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**

SOL è ancora in zona mista. Il frattale resta soltanto uno scenario contestuale: non è confermato dal prezzo e vale 0 punti operativi finché il gap non rientra. Meglio evitare leva e ragionare solo a tranche piccole.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 1. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 67,50%, return centrale 30g +2,76%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 1, positivi 30g 0,00%, return p50 -12,15%.
- Scanner path: **0** — Controlli disponibili 85. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-1** — Score tecnico -1/12, verdetto neutrale / misto, trend rialzista, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Triplo massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 2/12, verdetto ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO, stage STAGE 2 / MARKUP, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto STRUTTURA ANALOGA, PREZZO NON ADERENTE, somiglianza strutturale +73,21%, aderenza live +70,00%, errore live +15,00%, gap corrente +1,98%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE NON CONFERMATO DAL PREZZO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 82, ma percorso ancorato non aderente: gap +1,98%, errore live +15,00%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 2, bias CONTESTO DA OSSERVARE, EMA200 111,41 $, upside EMA200 +1,70%, gap EMA50/EMA200 -4,47%, hit EMA200 12w +93,33%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 0, bear 0, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — SOL: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 123,48; milestone analogiche 121,46 / 122,68, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 104,06 / 96,23 / 62,19.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 2. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 72,50%, return centrale 30g +6,66%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 2, positivi 30g 100,00%, return p50 +3,34%.
- Scanner path: **0** — Controlli disponibili 85. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -6/12, verdetto debole, trend ribassista, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff range / fase non chiara, pattern score 0 (rialzista Doppio minimo / INVALIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -6/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff RANGE / FASE NON CHIARA, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +0.00, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — DOGE: cambiamento medio in miglioramento rispetto a ieri.

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

Generato: 2026-10-11 05:33 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 83.007 $ | prezzo corrente |
| Power Law centrale | 126.615 $ | deviazione -34,44% |
| Banda p10-p90 | 78.882 $ / 319.910 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 15,20% | posizione storica nel corridoio |
| Esponente β | 5,7852 | R² log-log 91,94% |
| Stabilità β | BASSA | range 1,3155 cambiando finestra |
| Ultimo halving | 2024-04-19 | 905 giorni fa |
| Fase ciclo | 61,95% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-10-11 (4407 osservazioni)
- Formula stimata: prezzo ≈ exp(-38.9086) × giorni^5.7852
- Prezzo centrale oggi: **126.615 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 15,20%
- Scarto dal centro: **-34,44%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,7852 | 91,94% |
| 2015 | 5,8651 | 91,48% |
| 2016 | 5,5470 | 87,77% |
| 2017 | 4,8233 | 83,06% |
| 2018 | 4,5495 | 78,64% |

### Backtest walk-forward contro prezzo invariato

| Orizzonte | Controlli | Vittorie vs naive | Errore mediano modello | Errore mediano naive |
| --- | --- | --- | --- | --- |
| 90g | 82 | 29,27% | 48,35% | 21,05% |
| 180g | 82 | 42,68% | 57,61% | 46,17% |
| 365g | 82 | 58,54% | 70,14% | 84,45% |
| 730g | 82 | 57,32% | 72,61% | 108,40% |

## Bitcoin Four-Year Spiral

Nel grafico l'angolo rappresenta il tempo dentro una finestra di quattro anni e il raggio rappresenta il prezzo in scala logaritmica. ATH, bottom storici e halving sono marker descrittivi: la spirale rende visibili le ricorrenze, ma non dimostra che il ciclo futuro debba ripetersi.

![Bitcoin Four-Year Spiral](bitcoin_four_year_spiral.png)

## Stessa fase dei cicli halving precedenti

| Ciclo | Data analoga | +30g | +90g | +180g | +365g |
| --- | --- | --- | --- | --- | --- |
| 2012-11-28 → 2016-07-09 | 2015-02-23 | +3,06% | +0,86% | -3,56% | +76,12% |
| 2016-07-09 → 2020-05-11 | 2018-11-24 | +5,10% | +3,22% | +103,10% | +81,61% |
| 2020-05-11 → 2024-04-19 | 2022-10-19 | -12,76% | +10,56% | +53,84% | +50,05% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | 2 | 0 | 2.3894492498753195 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -5 | -1 | -5.046937104513538 | 0 |

## Tracker live Power Law

| Orizzonte | Controlli | Vittorie vs naive | Errore modello | Errore naive | Stato |
| --- | --- | --- | --- | --- | --- |
| 90g | 1 | 0,00% | 47,80% | 28,30% | RACCOLTA LIVE / PESO 0 |
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

Generato: 2026-10-11 05:33 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00131980 | +2 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +2,39% | MISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000103 | -5 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -5,05% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (+2)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g -6,53%; 30g +2,39%; 90g +9,44%; 180g +13,38%
- **Daily:** RSI 38.70; MA50 0.00134114; MA200 0.00120066
- **Weekly:** MA30 0.00120583; RSI 53.63
- **Livelli:** supporto 0.00127800; resistenza 0.00133900; breakout 60g 0.00146600; breakdown 60g 0.00113000
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00133900; target 0.00140150
- **Fibonacci:** NON ATTIVO — 38.2% a 0.00129143
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in salita; struttura con massimi/minimi crescenti; RSI relativo debole; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-5)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g -6,11%; 30g -5,05%; 90g -9,80%; 180g -18,63%
- **Daily:** RSI 35.80; MA50 0.00000110; MA200 0.00000122
- **Weekly:** MA30 0.00000122; RSI 37.35
- **Livelli:** supporto 0.00000100; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000099
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000110
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; RSI relativo debole; MACD relativo negativo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 212 | 52,36% | +1,92% | -1,06% |
| SOL | 30g | 208 | 48,08% | +4,59% | +0,67% |
| SOL | 90g | 202 | 52,97% | +9,80% | +3,12% |
| DOGE | 7g | 296 | 55,41% | +1,80% | -1,66% |
| DOGE | 30g | 295 | 52,88% | +1,96% | -3,48% |
| DOGE | 90g | 290 | 54,48% | +6,90% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 52 | 48,08% | -0,02% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 51 | 45,10% | +0,11% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 47 | 40,43% | +0,06% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 41 | 43,90% | +0,10% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 35 | 57,14% | -0,22% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 60 | 66,67% | +0,09% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 58 | 60,34% | +0,17% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 56 | 55,36% | -0,31% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 54 | 50,00% | -0,66% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 48 | 52,08% | -0,47% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **11 ottobre 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 109,54 $ | 2026-10-11T05:30:21Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 109,53 $ | 2026-10-11T05:32:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 2m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | -0,01000 $ | -0,01% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=109.54000091552734
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-10-11T05:30:21Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=109.52999877929688
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-10-11T05:32:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-10-11T05:32:42Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=141.726101
ANCHOR_AGE_HOURS=0.03936836138888889
CURRENT_VS_ANCHOR_GAP_USD=-0.01000213623046875
CURRENT_VS_ANCHOR_GAP_PCT=-0.009131035372345053
```

## Verdetto: STRUTTURA ANALOGA, PREZZO NON ADERENTE

- **Fase attuale:** FRATTALE NON CONFERMATO DAL PREZZO
- **Somiglianza totale:** +73,21%
- **Somiglianza strutturale:** +73,21%
- **Aderenza prezzo live:** +70,00%
- **Errore medio live:** +15,00%
- **Gap prezzo corrente:** +1,98%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA / NON OPERATIVO
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** La geometria ricorda BTC 2022, ma SOL è troppo distante dal percorso scalato per usarlo come conferma operativa.
- **SOL è al giorno:** 127 dal bottom usato.
- **Giorno BTC equivalente:** 2023-03-28
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Spinta rialzista abbastanza pulita.** Zona bassa **109,54 $** intorno al **11 ottobre 2026**; zona alta **121,46 $** intorno al **25 ottobre 2026**; fine step circa **121,46 $** entro il **25 ottobre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=STRUTTURA ANALOGA, PREZZO NON ADERENTE
PRICE_ADHERENCE_FAILED=YES
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=YES
PRICE_ADHERENCE_LAST_GAP_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=15.000840376169394
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=1.9777929841405362
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 11 ottobre 2026 | 101 | +70,00% | +15,00% | +1,98% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 11 ottobre 2026 | 128 | +73,79% | +13,11% | +1,98% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: STRUTTURA ANALOGA, PREZZO NON ADERENTE.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: STRUTTURA ANALOGA, PREZZO NON ADERENTE. |
| Aderenza live | +70,00% | Errore medio live +15,00%. |
| Gap corrente | +1,98% | Prezzo non aderente: superata almeno una soglia canonica (15% medio / 18% ultimo). |
| Prima conferma prezzo | 121,46 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 122,68 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 104,06 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 501,15 $ |
| Massimo percorso base | 501,15 $ (21 aprile 2029) |

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
| Prima conferma | 121,46 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 122,68 $ | Scenario più credibile. |
| Invalidazione soft | 104,06 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 18 ottobre 2026 | +3,30% | 113,16 $ | 109,54 $ | 114,40 $ |
| 14 giorni | 25 ottobre 2026 | +10,88% | 121,46 $ | 109,54 $ | 121,46 $ |
| 30 giorni | 10 novembre 2026 | +8,09% | 118,40 $ | 109,54 $ | 122,47 $ |
| 60 giorni | 10 dicembre 2026 | -1,47% | 107,93 $ | 105,79 $ | 122,47 $ |
| 90 giorni | 9 gennaio 2027 | +11,01% | 121,60 $ | 100,93 $ | 123,31 $ |
| 120 giorni | 8 febbraio 2027 | +7,65% | 117,92 $ | 100,93 $ | 126,44 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 11 ottobre 2026 -> 25 ottobre 2026 | +10,88% | 109,54 $ (11 ottobre 2026) | 121,46 $ (25 ottobre 2026) | 121,46 $ | Spinta rialzista abbastanza pulita. |
| Step 2 - primo mese | 26 ottobre 2026 -> 10 novembre 2026 | +8,09% | 109,58 $ (4 novembre 2026) | 122,47 $ (28 ottobre 2026) | 118,40 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 11 novembre 2026 -> 10 dicembre 2026 | -1,47% | 105,79 $ (7 dicembre 2026) | 118,64 $ (18 novembre 2026) | 107,93 $ | Prima spike, poi scarico. |
| Step 4 - terzo mese | 11 dicembre 2026 -> 9 gennaio 2027 | +11,01% | 100,93 $ (28 dicembre 2026) | 123,31 $ (6 gennaio 2027) | 121,60 $ | Prima retest / debolezza, poi recupero. |

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
| Prezzo SOL | 109,54 $ |  |
| Weekly RSI | 56,85 / linea grezza 51,29 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 48,32 / linea grezza 55,13 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 501,15 $ | Avanzamento +21,86% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 48,3, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Score on-chain | -2 |
| Bias | NEGATIVA |
| Azione coerente | PRUDENZA / POSSIBILE PRESSIONE |
| Prezzo SOL | 109,54 $ |
| TVL Solana | 6,20 mld $ |
| TVL 7g | -6,18% |
| DEX volume 24h | 1,58 mld $ |
| Fees 24h | 11,84 mln $ |
| Stablecoin su Solana | 16,33 mld $ |
| Stake ratio | 69,03% |
| Metriche mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

Lettura semplice:

**PRUDENZA / POSSIBILE PRESSIONE**

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
| Lifecycle squeeze score | 2 |
| Bias | CONTESTO DA OSSERVARE |
| Azione coerente | SOLO OSSERVAZIONE |
| Peso suggerito Global | 0 |
| Trend squeeze | STABILE / DA CONFERMARE |
| Trend squeeze score | 0 |
| Confronto precedente | 2026-10-05 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 109,54 $ |
| EMA200 weekly target | 111,41 $ |
| Upside verso EMA200 | +1,70% |
| Distanza prezzo da EMA200 | -1,67% |
| Gap EMA50/EMA200 | -4,47% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 56,86 |
| Età SOL | 6,5 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +93,33% |
| Max gain mediano 12w | +28,93% |
| Drawdown mediano 12w | -31,33% |

Lettura semplice:

**SOLO OSSERVAZIONE**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-10-11 05:33 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-10-11 05:30:22 UTC**

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
| BTC | NESSUN CAMBIAMENTO FORTE | peggioramento | NEUTRALE / INCERTO | +45.00% | -2.50 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | peggioramento | RIALZISTA | +67.50% | +2.50 punti |
| DOGE | CAMBIAMENTO MEDIO | miglioramento | RIALZISTA | +72.50% | +7.50 punti |

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
| BTC | 78.828 $ | 91.274 $ | +31,43% | +15,79% | rimbalzo poco frequente | 91.274 $ | 78.828 $ | +47,83% | -13,64% | scarico possibile |
| SOL | 104,06 $ | 120,49 $ | +42,86% | +15,79% | rimbalzo debole | 120,49 $ | 104,06 $ | +37,04% | -13,64% | scarico possibile |
| DOGE | 0,08108 $ | 0,09388 $ | +53,12% | +15,79% | rimbalzo possibile | 0,09388 $ | 0,08108 $ | +21,43% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 35 prima sono scesi a -5,00%. Tra quei 35, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +31,43% (11/35). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **BTC: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 11 poi sono scaricati a -5,00%. Percentuale: +47,83% (11/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.**
- **SOL: su 40 casi simili, 35 prima sono scesi a -5,00%. Tra quei 35, 15 poi sono rimbalzati fino a +10,00%. Percentuale: +42,86% (15/35). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **SOL: su 40 casi simili, 27 prima sono saliti a +10,00%. Tra quei 27, 10 poi sono scaricati a -5,00%. Percentuale: +37,04% (10/27). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.**
- **DOGE: su 40 casi simili, 32 prima sono scesi a -5,00%. Tra quei 32, 17 poi sono rimbalzati fino a +10,00%. Percentuale: +53,12% (17/32). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **DOGE: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 6 poi sono scaricati a -5,00%. Percentuale: +21,43% (6/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-10-11 05:32:20 UTC

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-10-11 | 2026-10-11T05:30:21Z | 2026-10-11 05:30:22 |
| SOL | 2026-10-11 | 2026-10-11T05:30:21Z | 2026-10-11 05:30:22 |
| DOGE | 2026-10-11 | 2026-10-11T05:30:21Z | 2026-10-11 05:30:22 |

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
| BTC | 2026-10-11 | 82.976 $ | INCERTO | 45,00% | 69.839,16 $ | 73.396,30 $ | 81.272,95 $ | 90.736,61 $ | 102.916,66 $ |
| SOL | 2026-10-11 | 109,54 $ | SALITA | 67,50% | 94,32 $ | 99,69 $ | 112,57 $ | 120,40 $ | 132,95 $ |
| DOGE | 2026-10-11 | 0.08535 $ | SALITA | 72,50% | 0.07450 $ | 0.08405 $ | 0.09103 $ | 0.09675 $ | 0.10791 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | AVAILABLE | SAME_BTC_REGIME | 2 | 2 | 7 | 7 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 81.272,95 $ | 83.681,17 $ | 102.916,66 $ | 102.239,83 $ |
| SOL | AVAILABLE | SAME_BTC_REGIME | 1 | 1 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 112,57 $ | 115,62 $ | 132,95 $ | 132,90 $ |
| DOGE | AVAILABLE | SAME_BTC_REGIME | 2 | 2 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.09103 $ | 0.09009 $ | 0.10791 $ | 0.10022 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-09-11**; verificato fino al **2026-10-11**; stato **COMPLETO 30/30g**.
- Reale **83.004,36 $**; p50 previsto **106.889,48 $**; scarto **-22,35%**.
- Errore medio assoluto **6,46%**; massimo **22,35%**; DENTRO p10-p90; FUORI p25-p75.

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

**Campione corrente:** 15 episodi qualificati su 40 · 14 asset distinti.

![SOL conditional successor corrente](scanner_forecast_SOL_conditional_successor_current.png)

###### Confronto diretto a 30 giorni

| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Cono standard | 2026-10-11 | 40 | 2026-11-10 | 94.32 $ | 99.69 $ | 112.57 $ | 120.40 $ | 132.95 $ |
| Conditional corrente | 2026-10-11 | 15 | 2026-11-10 | 91.99 $ | 94.77 $ | 112.16 $ | 132.06 $ | 222.68 $ |

###### Struttura successiva dei casi correnti

| Classe | Episodi | Frequenza empirica |
| --- | ---: | ---: |
| DIRECT_CONTINUATION | 3 | 20.00% |
| SHALLOW_PULLBACK_THEN_CONTINUATION | 2 | 13.33% |
| DEEP_PULLBACK_THEN_RECOVERY | 2 | 13.33% |
| FAILURE | 8 | 53.33% |
| UNRESOLVED | 0 | 0.00% |

###### Episodi qualificati oggi

| Asset | Match window | -5% hit | +10% anchor | Classe 60d |
| --- | --- | --- | --- | --- |
| BTC-USD | 2022-11-28 → 2023-03-07 | 2023-03-09 | 2023-03-14 | DIRECT_CONTINUATION |
| RUNE-USD | 2023-06-26 → 2023-10-03 | 2023-10-06 | 2023-10-24 | DIRECT_CONTINUATION |
| LRC-USD | 2020-11-17 → 2021-02-24 | 2021-02-25 | 2021-03-17 | FAILURE |
| AVAX-USD | 2021-07-01 → 2021-10-08 | 2021-10-10 | 2021-10-25 | DEEP_PULLBACK_THEN_RECOVERY |
| XTZ-USD | 2019-09-19 → 2019-12-27 | 2019-12-29 | 2020-01-20 | SHALLOW_PULLBACK_THEN_CONTINUATION |
| VET-USD | 2022-11-29 → 2023-03-08 | 2023-03-09 | 2023-03-17 | FAILURE |
| HBAR-USD | 2022-11-24 → 2023-03-03 | 2023-03-08 | 2023-03-31 | FAILURE |
| ETH-USD | 2022-11-27 → 2023-03-06 | 2023-03-09 | 2023-03-17 | DIRECT_CONTINUATION |
| SNX-USD | 2020-11-17 → 2021-02-24 | 2021-02-26 | 2021-03-02 | FAILURE |
| OMG-USD | 2022-11-27 → 2023-03-06 | 2023-03-08 | 2023-03-19 | FAILURE |
| XTZ-USD | 2023-09-13 → 2023-12-21 | 2024-01-07 | 2024-01-11 | DEEP_PULLBACK_THEN_RECOVERY |
| DOT-USD | 2022-11-27 → 2023-03-06 | 2023-03-08 | 2023-03-17 | FAILURE |
| BAT-USD | 2022-11-27 → 2023-03-06 | 2023-03-08 | 2023-04-05 | FAILURE |
| ZIL-USD | 2022-11-24 → 2023-03-03 | 2023-03-07 | 2023-04-01 | SHALLOW_PULLBACK_THEN_CONTINUATION |
| QTUM-USD | 2022-11-27 → 2023-03-06 | 2023-03-08 | 2023-03-19 | FAILURE |

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

- Ultimo close disponibile: **2026-10-11** · SOL **109.53 $**.
- Giorno del vintage: **23/30**.
- P50 condizionato previsto per quel giorno: **161.01 $**.
- SOL reale: **DENTRO p10-p90** · **FUORI p25-p75**.

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

- Cono congelato il **2026-09-11**; verificato fino al **2026-10-11**; stato **COMPLETO 30/30g**.
- Reale **109,53 $**; p50 previsto **127,44 $**; scarto **-14,06%**.
- Errore medio assoluto **7,27%**; massimo **14,53%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted SOL](scanner_forecast_SOL_regime_adjusted.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-09-11**; verificato fino al **2026-10-11**; stato **COMPLETO 30/30g**.
- Reale **0.08534 $**; p50 previsto **0.07212 $**; scarto **18,34%**.
- Errore medio assoluto **15,05%**; massimo **27,92%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted DOGE](scanner_forecast_DOGE_regime_adjusted.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 85 | 94,12% | 70,59% | 1,86% | 0,39% |
| BTC | 3g | 81 | 93,83% | 77,78% | 3,15% | 0,59% |
| BTC | 7g | 73 | 93,15% | 69,86% | 4,84% | 1,52% |
| BTC | 14g | 60 | 98,33% | 75,00% | 5,63% | 1,30% |
| BTC | 30g | 34 | 100,00% | 79,41% | 10,00% | -1,34% |
| SOL | 1g | 85 | 84,71% | 64,71% | 2,61% | 0,65% |
| SOL | 3g | 81 | 91,36% | 72,84% | 3,80% | 1,46% |
| SOL | 7g | 73 | 91,78% | 75,34% | 5,60% | 3,08% |
| SOL | 14g | 60 | 88,33% | 78,33% | 7,79% | 5,94% |
| SOL | 30g | 34 | 94,12% | 64,71% | 13,58% | 9,04% |
| DOGE | 1g | 85 | 88,24% | 61,18% | 2,98% | 0,36% |
| DOGE | 3g | 81 | 92,59% | 64,20% | 4,54% | 1,16% |
| DOGE | 7g | 73 | 76,71% | 73,97% | 8,38% | 5,07% |
| DOGE | 14g | 60 | 85,00% | 51,67% | 10,43% | 8,76% |
| DOGE | 30g | 34 | 94,12% | 41,18% | 16,92% | 16,92% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |

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

Generato: 2026-10-11 05:32 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +55,00%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +67,50%       | Nessun lato sopra soglia estrema |                  40 |
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
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **45,00%**
- Casi negativi / discesa storica: **55,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **82.976,46 $**
- Return normale fra 30 giorni: **81.272,95 $** (-2,05%)
- Drawdown normale durante il mese: **71.534,11 $** (-13,79%)
- Drawdown brutto da rispettare: **68.491,29 $** (-17,46%)
- Max gain normale durante il mese: **92.879,57 $** (11,93%)
- Max gain buono / take profit ottimistico: **101.213,36 $** (21,98%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **67,50%**
- Casi negativi / discesa storica: **32,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **109,54 $**
- Return normale fra 30 giorni: **112,57 $** (2,76%)
- Drawdown normale durante il mese: **97,97 $** (-10,56%)
- Drawdown brutto da rispettare: **90,90 $** (-17,02%)
- Max gain normale durante il mese: **123,76 $** (12,98%)
- Max gain buono / take profit ottimistico: **129,28 $** (18,02%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **72,50%**
- Casi negativi / discesa storica: **27,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,09 $**
- Return normale fra 30 giorni: **0,09 $** (6,66%)
- Drawdown normale durante il mese: **0,08 $** (-10,18%)
- Drawdown brutto da rispettare: **0,07 $** (-16,71%)
- Max gain normale durante il mese: **0,10 $** (12,42%)
- Max gain buono / take profit ottimistico: **0,10 $** (20,24%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 82.976,46 $

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

- Se va molto male: **69.839,16 $** (-15,83%)
- Se va male: **73.396,30 $** (-11,55%)
- Scenario normale: **81.272,95 $** (-2,05%)
- Se va bene: **90.736,61 $** (9,35%)
- Se va molto bene: **102.916,66 $** (24,03%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **71.534,11 $** (-13,79%)
- Discesa brutta: **68.491,29 $** (-17,46%)
- Discesa molto brutta: **65.494,58 $** (-21,07%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **92.879,57 $** (11,93%)
- Rialzo buono: **101.213,36 $** (21,98%)
- Rialzo molto forte: **117.407,92 $** (41,50%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **71.534,11 $** e uno spike normale intorno a **92.879,57 $**.

La chiusura a 30 giorni è incerta: salita 45,00%, discesa 55,00%. Non c'è un vantaggio netto.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 109,54 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **67,50%**
- Probabilità storica di discesa: **32,50%**
- Quanto è netto il segnale: **medio**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale medio. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **94,32 $** (-13,90%)
- Se va male: **99,69 $** (-9,00%)
- Scenario normale: **112,57 $** (2,76%)
- Se va bene: **120,40 $** (9,91%)
- Se va molto bene: **132,95 $** (21,37%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **97,97 $** (-10,56%)
- Discesa brutta: **90,90 $** (-17,02%)
- Discesa molto brutta: **86,54 $** (-21,00%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **123,76 $** (12,98%)
- Rialzo buono: **129,28 $** (18,02%)
- Rialzo molto forte: **139,00 $** (26,90%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **97,97 $** e uno spike normale intorno a **123,76 $**.

La chiusura a 30 giorni era più spesso positiva: salita 67,50%, discesa 32,50%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 0,09 $

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

- Se va molto male: **0,07 $** (-12,71%)
- Se va male: **0,08 $** (-1,52%)
- Scenario normale: **0,09 $** (6,66%)
- Se va bene: **0,10 $** (13,35%)
- Se va molto bene: **0,11 $** (26,44%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,08 $** (-10,18%)
- Discesa brutta: **0,07 $** (-16,71%)
- Discesa molto brutta: **0,07 $** (-21,22%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,10 $** (12,42%)
- Rialzo buono: **0,10 $** (20,24%)
- Rialzo molto forte: **0,12 $** (42,44%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,08 $** e uno spike normale intorno a **0,10 $**.

La chiusura a 30 giorni era più spesso positiva: salita 72,50%, discesa 27,50%. Quindi la lettura principale è favorevole.

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

- Previsioni già controllate: **41**
- Direzione corretta: **91,18%**
- Errore medio dello scenario centrale: **8,57%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **2,44%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **41**
- Direzione corretta: **77,14%**
- Errore medio dello scenario centrale: **15,43%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **26,83%**
- Prezzo finale dentro lo scenario 10%-90%: **95,12%**

### Solana

- Previsioni già controllate: **41**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **11,60%**
- Zona rischio toccata: **4,88%**
- Zona rialzo media toccata: **26,83%**
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

- Previsioni controllate: **41**
- Previsioni usate per la calibrazione recente: **41**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **91,18%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **INCERTO**
- Direzione calibrata oggi: **DISCESA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **-2,05%** → **81.272,95 $**
- Correzione imparata dagli errori: **-1,40%**
- Calibrato: **-3,46%** → **80.107,73 $**
- Lettura: Lo scanner è stato abbastanza centrato sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-13,79%** → **71.534,11 $**
- Correzione imparata dagli errori: **5,00%**
- Calibrato: **-8,79%** → **75.683,90 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **11,93%** → **92.879,57 $**
- Correzione imparata dagli errori: **-6,16%**
- Calibrato: **5,77%** → **87.768,31 $**
- Lettura: Lo scanner ha sovrastimato gli spike: nella realtà il prezzo è salito meno del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Solana

- Previsioni controllate: **41**
- Previsioni usate per la calibrazione recente: **41**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **100,00%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **2,76%** → **112,57 $**
- Correzione imparata dagli errori: **5,58%**
- Calibrato: **8,34%** → **118,67 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-10,56%** → **97,97 $**
- Correzione imparata dagli errori: **3,68%**
- Calibrato: **-6,88%** → **102,01 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **12,98%** → **123,76 $**
- Correzione imparata dagli errori: **-0,05%**
- Calibrato: **12,93%** → **123,70 $**
- Lettura: Lo scanner è stato abbastanza centrato sul max gain.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Dogecoin

- Previsioni controllate: **41**
- Previsioni usate per la calibrazione recente: **41**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **77,14%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **6,66%** → **0,09 $**
- Correzione imparata dagli errori: **15,43%**
- Calibrato: **22,09%** → **0,10 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-10,18%** → **0,08 $**
- Correzione imparata dagli errori: **13,70%**
- Calibrato: **3,52%** → **0,09 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **12,42%** → **0,10 $**
- Correzione imparata dagli errori: **2,64%**
- Calibrato: **15,06%** → **0,10 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 82.976,46 $

Bitcoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **45,00%**
- Casi negativi dopo 30 giorni: **55,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,14%**
- Rendimento medio dopo 30 giorni: **1,02%**
- Rendimento centrale dopo 30 giorni: **-2,05%**
- Discesa media durante i 30 giorni: **-13,38%**
- Massimo rialzo medio durante i 30 giorni: **17,39%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **83.821,50 $**
- Scenario centrale a 30 giorni: **81.272,95 $**
- Zona di rischio media: **71.874,64 $**
- Zona di rialzo media: **97.405,04 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -15,83% → **69.839,16 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -11,55% → **73.396,30 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -2,05% → **81.272,95 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 9,35% → **90.736,61 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 24,03% → **102.916,66 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -21,07% → **65.494,58 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -17,46% → **68.491,29 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -13,79% → **71.534,11 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -9,19% → **75.353,96 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -2,07% → **81.255,96 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,01% → **83.812,50 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 7,19% → **88.941,14 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 11,93% → **92.879,57 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 21,98% → **101.213,36 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 41,50% → **117.407,92 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| BTC-USD         | 2022-11-28   | 2023-03-07 |        91.77 |        26.21 |          -9.15 |          28.17 |
| RUNE-USD        | 2023-06-26   | 2023-10-03 |        90.41 |        40.6  |         -23.7  |          48.11 |
| TRX-USD         | 2022-11-27   | 2023-03-06 |        89.66 |        -1.92 |         -14.81 |           0.58 |
| MKR-USD         | 2020-11-18   | 2021-02-25 |        88.74 |         5.55 |         -10.18 |          11.08 |
| QTUM-USD        | 2023-09-08   | 2023-12-16 |        88.55 |        -2.61 |          -6.73 |          16.86 |
| ETH-USD         | 2022-11-27   | 2023-03-06 |        88.08 |        21.8  |          -8.82 |          21.8  |
| XTZ-USD         | 2023-09-13   | 2023-12-21 |        87.99 |        11.21 |          -5.88 |          25.37 |
| LRC-USD         | 2020-11-17   | 2021-02-24 |        87.81 |       -12.15 |         -20.93 |          10.18 |
| AVAX-USD        | 2021-07-01   | 2021-10-08 |        87.18 |        44.92 |         -10.18 |          44.92 |
| CRV-USD         | 2022-11-26   | 2023-03-05 |        87.11 |         7.08 |          -9.73 |           9.83 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 109,54 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **67,50%**
- Casi negativi dopo 30 giorni: **32,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **87,32%**
- Rendimento medio dopo 30 giorni: **3,03%**
- Rendimento centrale dopo 30 giorni: **2,76%**
- Discesa media durante i 30 giorni: **-12,78%**
- Massimo rialzo medio durante i 30 giorni: **15,56%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **112,86 $**
- Scenario centrale a 30 giorni: **112,57 $**
- Zona di rischio media: **95,54 $**
- Zona di rialzo media: **126,59 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -13,90% → **94,32 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -9,00% → **99,69 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 2,76% → **112,57 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 9,91% → **120,40 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 21,37% → **132,95 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -21,00% → **86,54 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -17,02% → **90,90 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -10,56% → **97,97 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -9,22% → **99,44 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -4,81% → **104,27 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 2,81% → **112,62 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 9,53% → **119,97 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 12,98% → **123,76 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 18,02% → **129,28 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 26,90% → **139,00 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| CRV-USD         | 2022-11-26   | 2023-03-05 |        90.06 |         7.08 |          -9.73 |           9.83 |
| MKR-USD         | 2020-11-18   | 2021-02-25 |        89.81 |         5.55 |         -10.18 |          11.08 |
| BTC-USD         | 2022-11-28   | 2023-03-07 |        89.75 |        26.21 |          -9.15 |          28.17 |
| ZEC-USD         | 2024-05-25   | 2024-09-01 |        89.55 |        -9.36 |          -9.36 |           7.51 |
| RUNE-USD        | 2023-06-26   | 2023-10-03 |        89.54 |        40.6  |         -23.7  |          48.11 |
| ETH-USD         | 2025-05-25   | 2025-09-01 |        89.37 |         0.85 |         -10.34 |           9.29 |
| ADA-USD         | 2025-05-25   | 2025-09-01 |        88.8  |         6.23 |          -4.67 |          16.2  |
| ENJ-USD         | 2022-11-27   | 2023-03-06 |        88.79 |         0.49 |         -16.86 |           1.05 |
| LRC-USD         | 2020-11-17   | 2021-02-24 |        88.75 |       -12.15 |         -20.93 |          10.18 |
| AVAX-USD        | 2021-07-01   | 2021-10-08 |        88.73 |        44.92 |         -10.18 |          44.92 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 0,09 $

Dogecoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **72,50%**
- Casi negativi dopo 30 giorni: **27,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **83,86%**
- Rendimento medio dopo 30 giorni: **6,19%**
- Rendimento centrale dopo 30 giorni: **6,66%**
- Discesa media durante i 30 giorni: **-12,33%**
- Massimo rialzo medio durante i 30 giorni: **16,82%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,09 $**
- Scenario centrale a 30 giorni: **0,09 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,10 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -12,71% → **0,07 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -1,52% → **0,08 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 6,66% → **0,09 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 13,35% → **0,10 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 26,44% → **0,11 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -21,22% → **0,07 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -16,71% → **0,07 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -10,18% → **0,08 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -7,89% → **0,08 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -1,66% → **0,08 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 5,30% → **0,09 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 9,17% → **0,09 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 12,42% → **0,10 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 20,24% → **0,10 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 42,44% → **0,12 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XTZ-USD         | 2019-09-19   | 2019-12-27 |        88.05 |        10.07 |         -10.29 |          15.06 |
| LINK-USD        | 2019-08-20   | 2019-11-27 |        86.6  |       -15.37 |         -21.21 |           5.09 |
| BTC-USD         | 2022-11-28   | 2023-03-07 |        86.57 |        26.21 |          -9.15 |          28.17 |
| TRX-USD         | 2022-11-27   | 2023-03-06 |        86.11 |        -1.92 |         -14.81 |           0.58 |
| AVAX-USD        | 2021-07-01   | 2021-10-08 |        85.81 |        44.92 |         -10.18 |          44.92 |
| KSM-USD         | 2022-11-30   | 2023-03-09 |        85.8  |         1.71 |          -4.83 |          16    |
| LRC-USD         | 2020-11-17   | 2021-02-24 |        85.74 |       -12.15 |         -20.93 |          10.18 |
| ENJ-USD         | 2022-11-27   | 2023-03-06 |        85.31 |         0.49 |         -16.86 |           1.05 |
| ALGO-USD        | 2026-02-13   | 2026-05-23 |        85.26 |       -22.03 |         -24.33 |          10.92 |
| ETH-USD         | 2022-11-27   | 2023-03-06 |        85.22 |        21.8  |          -8.82 |          21.8  |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report

Generated: 2026-10-11 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-11 | BULL | 82.976 $ | True | 33.32% | 3.12% | BULL | 33.32% | 3.12% |
| DOGE-USD | 2026-10-11 | RECOVERY | 0.08535 $ | False | 18.79% | -3.92% | BULL | 33.32% | 3.12% |
| SOL-USD | 2026-10-11 | BULL | 109,54 $ | True | 46.32% | 4.78% | BULL | 33.32% | 3.12% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 45.00% | -2.05% | 9.35% | 24.03% | -13.79% | -21.07% | 11.93% | 21.98% | 41.50% | 40.00% | -2.34% | 19.63% | 38.71% |
| BTC-USD | SAME_BTC_REGIME | 7 | 57.14% | 0.85% | 8.59% | 23.22% | -10.34% | -22.04% | 10.18% | 12.37% | 27.44% | 28.57% | -10.83% | 48.29% | 160.67% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 0.00% | -8.36% | -6.47% | -5.34% | -18.83% | -20.51% | 7.19% | 8.69% | 9.58% | 0.00% | -22.42% | -22.08% | -21.88% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 0.00% | -8.36% | -6.47% | -5.34% | -18.83% | -20.51% | 7.19% | 8.69% | 9.58% | 0.00% | -22.42% | -22.08% | -21.88% |
| DOGE-USD | ALL_MATCHES | 40 | 72.50% | 6.66% | 13.35% | 26.44% | -10.18% | -21.22% | 12.42% | 20.24% | 42.44% | 45.00% | -1.22% | 17.88% | 39.71% |
| DOGE-USD | SAME_BTC_REGIME | 9 | 66.67% | 5.55% | 10.07% | 17.42% | -10.29% | -21.71% | 11.81% | 15.06% | 22.58% | 55.56% | 15.36% | 97.72% | 133.95% |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 100.00% | 3.34% | 4.78% | 5.65% | -7.61% | -9.97% | 14.01% | 15.10% | 15.76% | 0.00% | -23.59% | -23.45% | -23.37% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 3.34% | 4.78% | 5.65% | -7.61% | -9.97% | 14.01% | 15.10% | 15.76% | 0.00% | -23.59% | -23.45% | -23.37% |
| SOL-USD | ALL_MATCHES | 40 | 67.50% | 2.76% | 9.91% | 21.37% | -10.56% | -21.00% | 12.98% | 18.02% | 26.90% | 40.00% | -2.67% | 19.50% | 39.16% |
| SOL-USD | SAME_BTC_REGIME | 11 | 72.73% | 5.55% | 8.19% | 21.32% | -10.29% | -20.93% | 14.82% | 17.04% | 23.98% | 54.55% | 25.03% | 67.92% | 103.66% |
| SOL-USD | SAME_ASSET_REGIME | 1 | 0.00% | -12.15% | -12.15% | -12.15% | -20.93% | -20.93% | 10.18% | 10.18% | 10.18% | 0.00% | -23.11% | -23.11% | -23.11% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -12.15% | -12.15% | -12.15% | -20.93% | -20.93% | 10.18% | 10.18% | 10.18% | 0.00% | -23.11% | -23.11% | -23.11% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 16 | 75.00% | 7.40% | -10.38% | 23.39% | 56.25% | 5.66% | 38.22% |
| BTC-USD | HISTORICAL_BTC_BULL | 7 | 57.14% | 0.85% | -10.34% | 12.37% | 28.57% | -10.83% | 66.03% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 17 | 11.76% | -11.35% | -15.58% | 22.51% | 29.41% | -5.57% | 22.51% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 29 | 75.86% | 7.39% | -10.11% | 20.59% | 41.38% | -1.28% | 37.20% |
| DOGE-USD | HISTORICAL_BTC_BULL | 9 | 66.67% | 5.55% | -10.29% | 15.06% | 55.56% | 15.36% | 100.64% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 2 | 50.00% | -1.26% | -10.76% | 22.23% | 50.00% | 6.04% | 22.23% |
| SOL-USD | HISTORICAL_BTC_BEAR | 22 | 77.27% | 3.41% | -11.18% | 17.40% | 27.27% | -4.65% | 22.82% |
| SOL-USD | HISTORICAL_BTC_BULL | 11 | 72.73% | 5.55% | -10.29% | 17.04% | 54.55% | 25.03% | 77.77% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 7 | 28.57% | -9.93% | -11.88% | 23.94% | 57.14% | 0.63% | 26.06% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 31 | 48.39% | -1.34% | -14.81% | 22.16% | 45.16% | -1.15% | 28.84% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 0.00% | -8.36% | -18.83% | 8.69% | 0.00% | -22.42% | 26.39% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 42.86% | -2.61% | -10.34% | 29.77% | 28.57% | -5.63% | 30.55% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 34 | 76.47% | 7.76% | -10.18% | 20.47% | 44.12% | -1.22% | 40.97% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 3 | 33.33% | -12.15% | -20.93% | 22.61% | 66.67% | 15.36% | 43.88% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -9.36% | -9.36% | 7.51% | 100.00% | 25.03% | 30.88% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 3.34% | -7.61% | 15.10% | 0.00% | -23.59% | 15.10% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 32 | 68.75% | 3.41% | -11.18% | 19.30% | 40.62% | -1.64% | 32.39% |
| SOL-USD | HISTORICAL_ASSET_BULL | 1 | 0.00% | -12.15% | -20.93% | 10.18% | 0.00% | -23.11% | 31.41% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -8.87% | -9.36% | 16.35% | 66.67% | 25.03% | 42.87% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 21.32% | -0.24% | 23.98% | 100.00% | 28.74% | 54.90% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 100.00% | 0.85% | -10.34% | 14.01% | 0.00% | -23.31% | 14.01% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 2 | 2 | 7 | 7 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 2 | 2 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 1 | 1 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-06-26 | 90.41% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 40.60% | -23.70% | 48.11% | 255.10% | -23.70% | 255.10% |
| BTC-USD | MKR-USD | 2020-11-18 | 88.74% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.55% | -10.18% | 11.08% | 97.72% | -10.18% | 100.64% |
| BTC-USD | LRC-USD | 2020-11-17 | 87.81% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -12.15% | -20.93% | 10.18% | -23.11% | -23.47% | 31.41% |
| BTC-USD | ETH-USD | 2025-05-25 | 85.51% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 0.85% | -10.34% | 9.29% | -10.83% | -13.07% | 9.29% |
| BTC-USD | ONE-USD | 2023-07-20 | 84.80% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -1.34% | -2.11% | 0.00% | -1.15% | -2.11% | 0.00% |
| BTC-USD | XLM-USD | 2025-05-25 | 84.77% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 11.63% | -1.79% | 13.66% | -14.48% | -16.25% | 14.61% |
| BTC-USD | DOGE-USD | 2024-01-11 | 84.25% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -4.58% | -16.72% | 4.20% | -21.74% | -21.74% | 11.32% |
| DOGE-USD | XTZ-USD | 2019-09-19 | 88.05% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 10.07% | -10.29% | 15.06% | 103.66% | -10.29% | 161.23% |
| DOGE-USD | LINK-USD | 2019-08-20 | 86.60% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -15.37% | -21.21% | 5.09% | 15.36% | -21.89% | 24.45% |
| DOGE-USD | LRC-USD | 2020-11-17 | 85.74% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -12.15% | -20.93% | 10.18% | -23.11% | -23.47% | 31.41% |
| DOGE-USD | MKR-USD | 2020-11-18 | 84.68% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.55% | -10.18% | 11.08% | 97.72% | -10.18% | 100.64% |
| DOGE-USD | ADA-USD | 2025-05-25 | 84.62% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 6.23% | -4.67% | 16.20% | -23.87% | -24.88% | 16.20% |
| DOGE-USD | ZEC-USD | 2024-05-25 | 83.33% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -9.36% | -9.36% | 7.51% | 25.03% | -12.78% | 30.88% |
| DOGE-USD | RUNE-USD | 2023-06-26 | 82.71% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 40.60% | -23.70% | 48.11% | 255.10% | -23.70% | 255.10% |
| DOGE-USD | XLM-USD | 2025-05-25 | 82.27% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 11.63% | -1.79% | 13.66% | -14.48% | -16.25% | 14.61% |
| DOGE-USD | LINK-USD | 2025-05-25 | 82.21% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 0.45% | -10.56% | 11.81% | -23.31% | -26.11% | 11.81% |
| SOL-USD | MKR-USD | 2020-11-18 | 89.81% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.55% | -10.18% | 11.08% | 97.72% | -10.18% | 100.64% |
| SOL-USD | ZEC-USD | 2024-05-25 | 89.55% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -9.36% | -9.36% | 7.51% | 25.03% | -12.78% | 30.88% |
| SOL-USD | RUNE-USD | 2023-06-26 | 89.54% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 40.60% | -23.70% | 48.11% | 255.10% | -23.70% | 255.10% |
| SOL-USD | ETH-USD | 2025-05-25 | 89.37% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 0.85% | -10.34% | 9.29% | -10.83% | -13.07% | 9.29% |
| SOL-USD | ADA-USD | 2025-05-25 | 88.80% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.23% | -4.67% | 16.20% | -23.87% | -24.88% | 16.20% |
| SOL-USD | LRC-USD | 2020-11-17 | 88.75% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -12.15% | -20.93% | 10.18% | -23.11% | -23.47% | 31.41% |
| SOL-USD | XTZ-USD | 2019-09-19 | 88.68% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 10.07% | -10.29% | 15.06% | 103.66% | -10.29% | 161.23% |
| SOL-USD | LINK-USD | 2025-05-25 | 88.66% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 0.45% | -10.56% | 11.81% | -23.31% | -26.11% | 11.81% |
| SOL-USD | LINK-USD | 2020-11-22 | 86.74% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 6.32% | -9.25% | 14.82% | 38.11% | -9.25% | 54.86% |
| SOL-USD | SNX-USD | 2020-11-17 | 86.52% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -8.87% | -15.78% | 17.87% | -26.68% | -28.58% | 17.87% |

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

Generato: 2026-10-11 05:32 UTC

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
| BTC | 82.976 $ | -1 | NEUTRALE / MISTO | STAGE 3 / DISTRIBUZIONE O PAUSA | COMPRESSIONE / TRIANGOLO POSSIBILE | RANGE / FASE NON CHIARA | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 109,54 $ | +2 | ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO | STAGE 2 / MARKUP | COMPRESSIONE / TRIANGOLO POSSIBILE | SIGN OF STRENGTH POSSIBILE | BASSO | HOLD LEGGERO / ATTESA CONFERME |
| DOGE | 0.08535 $ | -6 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | RANGE / FASE NON CHIARA | MEDIO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | 0 | -2 | -1 | 0 | 0 | 0 | -1 |
| SOL | +4 | 0 | -3 | -1 | 0 | 0 | +2 | +2 |
| DOGE | -3 | +2 | -3 | -2 | 0 | 0 | 0 | -6 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 82.571 $ | 87.146 $ | 87.364 $ | 62.488 $ | 2,39% | 8,41% | 30,19% |
| SOL | 98,63 $ | 110,04 $ | 124,62 $ | 72,47 $ | 3,86% | 11,00% | 42,51% |
| DOGE | 0.08189 $ | 0.09169 $ | 0.10528 $ | 0.06887 $ | 4,68% | 2,94% | 17,43% |

## Lettura dettagliata

### BTC

- Prezzo: **82.976 $**
- Score classico: **-1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,39%; distanza supporto 0,53%; distanza resistenza 4,99%

Dettaglio:

- Trend: **+2** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in salita; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **-2** — RSI sano 51.9; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale -0.01; volume ratio 0.38
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 51.86 |
| MACD histogram | -568.63179 |
| CMF20 | -0.011 |
| Volume ratio 20 | 0.38 |
| MA20 | 84.378 $ |
| MA50 | 80.812 $ |
| MA100 | 72.691 $ |
| MA200 | 71.919 $ |
| Pendenza MA50 20g | +10,39% |
| Pendenza MA200 60g | +2,93% |
| Bollinger width | 6,28% |
| Bollinger position | 0.24 |

### SOL

- Prezzo: **109,54 $**
- Score classico: **+2 / 12**
- Verdetto: **ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**
- Volatilità tecnica locale: **BASSO** — ATR14 3,86%; distanza supporto 11,08%; distanza resistenza 0,45%

Dettaglio:

- Trend: **+4** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in salita; STAGE 2 / MARKUP
- Stage weekly: **STAGE 2 / MARKUP** — Prezzo sopra MA30 weekly con MA30 in salita.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **-3** — RSI neutrale 43.5; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale 0.05; volume ratio 0.36
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 43.49 |
| MACD histogram | -2.02812 |
| CMF20 | 0.048 |
| Volume ratio 20 | 0.36 |
| MA20 | 117,74 $ |
| MA50 | 108,53 $ |
| MA100 | 92,71 $ |
| MA200 | 86,71 $ |
| Pendenza MA50 20g | +17,62% |
| Pendenza MA200 60g | +4,46% |
| Bollinger width | 14,82% |
| Bollinger position | -0.00 |

### DOGE

- Prezzo: **0.08535 $**
- Score classico: **-6 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **MEDIO** — ATR14 4,68%; distanza supporto 4,22%; distanza resistenza 7,43%

Dettaglio:

- Trend: **-3** — prezzo sotto MA200 daily; MA50 daily in salita; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-3** — RSI neutrale 41.3; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.09; volume ratio 0.31
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 41.25 |
| MACD histogram | -0.00158 |
| CMF20 | -0.088 |
| Volume ratio 20 | 0.31 |
| MA20 | 0.09361 $ |
| MA50 | 0.08904 $ |
| MA100 | 0.08070 $ |
| MA200 | 0.08765 $ |
| Pendenza MA50 20g | +10,84% |
| Pendenza MA200 60g | -4,21% |
| Bollinger width | 21,45% |
| Bollinger position | 0.05 |

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

Generato: 2026-10-11 05:33 UTC

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
| BTC | 82.976 $ | Doppio massimo | ATTIVO | ribassista | 2026-10-08 | 77.778 $ | -8,47% | n/a | Fib 23,6% TENUTO (+1) @ 80.208 $ | NEL RANGE | 82.571 $ |
| SOL | 109,54 $ | Triplo massimo | CANDIDATO | ribassista | n/a | 62,51 $ | n/a | 54,95% | Fib 23,6% TESTATO (0) @ 111,02 $ | NEL RANGE | 97,45 $ |
| DOGE | 0.08535 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 0.05153 $ | n/a | 8,86% | Fib 23,6% NON ATTIVO (0) @ 0.09401 $ | NEL RANGE | 0.08028 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **ATTIVO** (-1)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-21 -> 2026-10-02**
- Età formazione: **9 giorni**
- Breakout pattern: **2026-10-08**
- Età breakout: **3 giorni**
- Neckline: **82.571 $**
- Target teorico: **77.778 $**
- Progresso verso target: **-8,47%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TENUTO (+1) @ 80.208 $** — Swing UP 2026-07-01 57.748 -> 2026-10-02 87.146; livello più vicino 23.6% a 80.208; stato TENUTO; confluenza: invalidazione rialzista.
- Invalidazione: **84.222 $**
- Relazione prezzo/neckline: **vicino alla neckline**
- Dettaglio: Due massimi simili vicino a 87.364 tra 2026-09-21 e 2026-10-02. Neckline ribassista stimata: 82.571. Breakout neckline: 2026-10-08 (3 giorni fa). Stato: ATTIVO. Target teorico: 77.778; progresso corrente: -8,47%. Relazione prezzo/neckline: vicino alla neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Hammer / rejection basso**
- Stato prezzo: **NEL RANGE**
- Supporto: **82.571 $**
- Resistenza: **87.146 $**
- Breakout 60g: **87.364 $**
- Breakdown 60g: **62.488 $**
- RSI14: **51.76**
- ATR14: **2,39%**
- Volume ratio 20g: **0.38**
- Rendimento 30g: **+8,37%**
- Rendimento 90g: **+30,14%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | ATTIVO | -1 | ribassista | 82.571 $ | 2026-10-08 | 3g | 77.778 $ | -8,47% | n/a | 84.222 $ | Due massimi simili a 87.364 $ e 87.146 $. Neckline circa 82.571 $. Breakout neckline: 2026-10-08 (3 giorni fa). Stato: ATTIVO. Target teorico: 77.778 $; progresso: -8,47%; prezzo vicino alla neckline. |
| Doppio minimo | MATURO | +1 | rialzista | 82.262 $ | 2026-09-21 | 20g | 89.580 $ | 9,76% | n/a | 80.617 $ | Due minimi simili a 76.248 $ e 74.945 $. Neckline circa 82.262 $. Breakout neckline: 2026-09-21 (20 giorni fa). Stato: MATURO. Target teorico: 89.580 $; progresso: 9,76%; prezzo vicino alla neckline. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **63 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **70,69 $**
- Target teorico: **62,51 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **54,95%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 111,02 $** — Swing UP 2026-08-01 70,69 -> 2026-10-02 123,48; livello più vicino 23.6% a 111,02; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **72,11 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 63 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **97,45 $**
- Resistenza: **110,04 $**
- Breakout 60g: **124,62 $**
- Breakdown 60g: **72,47 $**
- RSI14: **43.47**
- ATR14: **3,86%**
- Volume ratio 20g: **0.36**
- Rendimento 30g: **+10,99%**
- Rendimento 90g: **+42,49%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,51 $ | n/a | 54,95% | 72,11 $ | Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 63 giorni. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 54,95% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 63 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 107,12 $ | 2026-09-18 | 23g | 118,01 $ | 22,25% | n/a | 104,97 $ | Due minimi simili a 97,45 $ e 96,23 $. Neckline circa 107,12 $. Breakout neckline: 2026-09-18 (23 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01 $; progresso: 22,25%; prezzo sopra neckline. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 53g | 85,65 $ | 419,52% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (53 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 419,52%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-08-22 -> 2026-09-22**
- Età formazione: **19 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.07841 $**
- Target teorico: **0.05153 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **8,86%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.09401 $** — Swing DOWN 2026-09-22 0.10528 -> 2026-10-02 0.09053; livello più vicino 23.6% a 0.09401; stato NON ATTIVO; confluenza: neckline rialzista, invalidazione rialzista.
- Invalidazione: **0.07997 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 0.10528 tra 2026-08-22 e 2026-09-22. Neckline ribassista stimata: 0.07841. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 19 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.08028 $**
- Resistenza: **0.09169 $**
- Breakout 60g: **0.10528 $**
- Breakdown 60g: **0.06887 $**
- RSI14: **41.25**
- ATR14: **4,68%**
- Volume ratio 20g: **0.31**
- Rendimento 30g: **+2,94%**
- Rendimento 90g: **+17,43%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.07841 $ | n/a | n/a | 0.05153 $ | n/a | 8,86% | 0.07997 $ | Due massimi simili a 0.09998 $ e 0.10528 $. Neckline circa 0.07841 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 19 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 0.07380 $ | 2026-08-19 | 53g | 0.07931 $ | 209,51% | n/a | 0.07233 $ | Due minimi simili a 0.06829 $ e 0.06835 $. Neckline circa 0.07380 $. Breakout neckline: 2026-08-19 (53 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931 $; progresso: 209,51%; prezzo sopra neckline. |

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

Generato: 2026-10-11 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-10-11**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-28**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **109,54 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+73,21%**
- Aderenza live principale: **+70,00%**
- Errore medio live principale: **15,00%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **127**
- Osservazioni inclusive dal bottom: **128**
- Osservazioni da inizio programma/scanner: **101**
- Errore assoluto medio dal bottom: **13,11%**
- Errore assoluto medio da inizio programma: **15,00%**
- Gap firmato medio ultimi 7 giorni: **+4,55%**
- Errore assoluto medio ultimi 7 giorni: **4,85%**
- Gap ultimo giorno: **+1,98%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+1,98%**
- Gap firmato medio 7g: **+4,55%**
- Errore assoluto medio 7g: **4,85%**
- Variazione recente gap: **+0,93%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato con distacco quasi stabile**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 118 | 2026-10-02 | 2023-03-19 | 118,62 $ | 110,45 $ | +7,39% | da inizio programma |
| 119 | 2026-10-03 | 2023-03-20 | 119,65 $ | 109,38 $ | +9,38% | da inizio programma |
| 120 | 2026-10-04 | 2023-03-21 | 121,53 $ | 110,99 $ | +9,49% | da inizio programma |
| 121 | 2026-10-05 | 2023-03-22 | 120,75 $ | 107,57 $ | +12,25% | da inizio programma |
| 122 | 2026-10-06 | 2023-03-23 | 120,79 $ | 111,61 $ | +8,22% | da inizio programma |
| 123 | 2026-10-07 | 2023-03-24 | 116,22 $ | 108,30 $ | +7,31% | da inizio programma |
| 124 | 2026-10-08 | 2023-03-25 | 109,44 $ | 108,31 $ | +1,05% | da inizio programma |
| 125 | 2026-10-09 | 2023-03-26 | 109,14 $ | 110,28 $ | -1,03% | da inizio programma |
| 126 | 2026-10-10 | 2023-03-27 | 109,14 $ | 106,91 $ | +2,09% | da inizio programma |
| 127 | 2026-10-11 | 2023-03-28 | 109,54 $ | 107,42 $ | +1,98% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-18 | 110,96 $ | 113,16 $ | 109,54 $ / 114,40 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-25 | 119,10 $ | 121,46 $ | 109,54 $ / 121,46 $ | no | n/a | n/a | n/a |
| 21g | 2026-11-01 | 119,74 $ | 122,11 $ | 109,54 $ / 122,47 $ | no | n/a | n/a | n/a |
| 28g | 2026-11-08 | 111,51 $ | 113,72 $ | 109,54 $ / 122,47 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-15 | 112,98 $ | 115,21 $ | 109,54 $ / 122,47 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-22 | 108,95 $ | 111,11 $ | 109,54 $ / 122,47 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-29 | 106,50 $ | 108,61 $ | 107,60 $ / 122,47 $ | no | n/a | n/a | n/a |
| 56g | 2026-12-06 | 107,25 $ | 109,37 $ | 107,47 $ / 122,47 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-13 | 109,13 $ | 111,28 $ | 105,79 $ / 122,47 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-20 | 107,30 $ | 109,42 $ | 103,48 $ / 122,47 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-27 | 102,10 $ | 104,12 $ | 103,48 $ / 122,47 $ | no | n/a | n/a | n/a |
| 84g | 2027-01-03 | 111,59 $ | 113,80 $ | 100,93 $ / 122,47 $ | no | n/a | n/a | n/a |
| 91g | 2027-01-10 | 120,89 $ | 123,28 $ | 100,93 $ / 123,31 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-17 | 121,24 $ | 123,64 $ | 100,93 $ / 125,16 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-24 | 120,62 $ | 123,01 $ | 100,93 $ / 125,16 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-31 | 117,61 $ | 119,94 $ | 100,93 $ / 126,44 $ | no | n/a | n/a | n/a |
| 119g | 2027-02-07 | 115,13 $ | 117,41 $ | 100,93 $ / 126,44 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-14 | 116,90 $ | 119,21 $ | 100,93 $ / 126,44 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 82 | 37,80% | 11,64% | 13,94% |
| 14g | 76 | 23,68% | 17,66% | 14,18% |
| 21g | 70 | 28,57% | 20,83% | 15,67% |
| 28g | 66 | 30,30% | 21,36% | 15,12% |
| 35g | 59 | 38,98% | 22,23% | 14,84% |
| 42g | 52 | 50,00% | 21,63% | 13,65% |
| 49g | 45 | 51,11% | 22,99% | 15,58% |
| 56g | 38 | 42,11% | 22,27% | 16,55% |
| 63g | 33 | 33,33% | 16,72% | 17,55% |
| 70g | 26 | 38,46% | 10,46% | 19,70% |
| 77g | 19 | 63,16% | 9,19% | 12,80% |
| 84g | 12 | 100,00% | 8,33% | 6,02% |
| 91g | 5 | 100,00% | 13,74% | 1,70% |
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

Generato: 2026-10-11 05:33 UTC

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 83.007 $ | 3 | +1 | 0 | POSITIVA / CANDIDATA, ANCORA NON PESATA | MEDIA | 100% | +0,0053% | +1,50% | 3,54 | -1,98% | 0 $ | 0 $ |
| SOL | 109,61 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0101% | -1,13% | 1,18 | +6,91% | 0 $ | 0 $ |
| DOGE | 0.08557 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0073% | -1,03% | 0,93 | -2,19% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | -0,0019% | 187,25 mln $ | 2,21 | -4,60% |
| BTC | Bitget | OK | -0,0003% | 2,82 mld $ | 0,02 | +71,90% |
| BTC | Kucoin | OK | -0,0021% | 845,11 mln $ | 8,05 | -10,72% |
| SOL | Kraken | OK | +0,0050% | 33,82 mln $ | 5,53 | +1,00% |
| SOL | Bitget | OK | +0,0100% | 463,57 mln $ | 0,59 | -2,97% |
| SOL | Kucoin | OK | +0,0064% | 137,97 mln $ | 1,04 | -2,22% |
| DOGE | Kraken | OK | -0,0023% | 4,19 mln $ | 0,70 | +12,61% |
| DOGE | Bitget | OK | +0,0100% | 116,18 mln $ | 0,44 | -6,15% |
| DOGE | Kucoin | OK | +0,0016% | 55,63 mln $ | 4,44 | +3,75% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,50**; candidato: **+1**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 9, accuratezza +33,33%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci tenuto con acquisti/assorbimento coerenti: conferma positiva. Confluenza tecnica dichiarata: invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** Doppio minimo maturo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Supporto vicino con assorbimento/acquisti: tenuta più credibile.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+1,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 0, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
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

- Score grezzo exchange: **+0,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 11, accuratezza +45,45%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 1.
- Flusso taker/order book: **+0,00**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta. Confluenza tecnica dichiarata: neckline rialzista, invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +45,00% | -2,05% | 5 | +80,00% | RACCOLTA DATI | 0,00 | +45,00% | -2,05% |
| SOL | +67,50% | +2,76% | 5 | +100,00% | RACCOLTA DATI | 0,00 | +67,50% | +2,76% |
| DOGE | +72,50% | +6,66% | 9 | +77,78% | RACCOLTA DATI | 0,00 | +72,50% | +6,66% |

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

Generato: 2026-10-11 05:33 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-11 | BTC | 83.007,30 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 3,54 | +1,50% | -1,98% |
| 2026-10-11 | DOGE | 0.08557 | V2.1.3 | OK | 0 | 0 | 0,00 | BASSA | 0,93 | -1,03% | -2,19% |
| 2026-10-11 | SOL | 109,61 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,18 | -1,13% | +6,91% |
| 2026-10-10 | BTC | 82.632,80 | V2.1.3 | OK | 0 | 0 | 2,50 | MEDIA | 5,85 | -3,65% | -3,35% |
| 2026-10-10 | DOGE | 0.08626 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,17 | +1,59% | -3,96% |
| 2026-10-10 | SOL | 109,78 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,97 | +3,23% | +1,99% |
| 2026-10-09 | BTC | 82.255,60 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 4,03 | -1,44% | +0,78% |
| 2026-10-09 | DOGE | 0.08493 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,34 | -2,02% | -9,81% |
| 2026-10-09 | SOL | 110,11 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,47 | -2,98% | +13,44% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 9 | +33,33% | -0,58% | -1,37% | +0,50% | FEEDBACK RAPIDO |
| BTC | 3g | 9 | +33,33% | -0,55% | -2,54% | +1,66% | FEEDBACK RAPIDO |
| BTC | 7g | 9 | +33,33% | -1,92% | -3,65% | +1,91% | FEEDBACK RAPIDO |
| BTC | 14g | 8 | +37,50% | -0,43% | -4,26% | +2,82% | FEEDBACK RAPIDO |
| BTC | 30g | 5 | +80,00% | +5,55% | -5,21% | +8,55% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 5 | +100,00% | +22,07% | -4,32% | +25,38% | FEEDBACK RAPIDO |
| DOGE | 1g | 11 | +54,55% | +1,55% | -0,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 3g | 11 | +36,36% | +1,63% | -3,44% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 7g | 11 | +45,45% | -0,13% | -4,83% | +9,23% | FEEDBACK RAPIDO |
| DOGE | 14g | 11 | +36,36% | +1,12% | -6,04% | +13,84% | FEEDBACK RAPIDO |
| DOGE | 30g | 9 | +77,78% | +11,35% | -6,95% | +29,00% | FEEDBACK RAPIDO |

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

**DOGE** — DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 82.976 $ | +0.0002% | -9.89% | 1.59 | Misto | 1/5 |
| SOL | 109,54 $ | +0.0091% | -17.94% | 2.10 | Misto | 1/5 |
| DOGE | 0.08535 $ | -0.0042% | -5.52% | 4.10 | Misto | 1/5 |

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

Generato: 2026-10-11 05:33 UTC

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                      | Stato D       | Weekly                     | Stato W       | Lettura weekly                                                                                              |   Peso |
|:--------|:---------------------------|:--------------|:---------------------------|:--------------|:------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Misto / nessuna divergenza | CONTESTO      | Misto / nessuna divergenza | CONTESTO      | Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.                        |      0 |
| SOL     | Hidden bullish             | IN_FORMAZIONE | Hidden bullish             | IN_FORMAZIONE | Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0. |      0 |
| DOGE    | Conferma ribassista        | CONTESTO      | Misto / nessuna divergenza | CONTESTO      | Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.                        |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                       | Stato         | Prezzo / RSI      | Pivot confrontati                                                | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:---------------------------|:--------------|:------------------|:-----------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Misto / nessuna divergenza | CONTESTO      | 83.007 $ / 51,87  | n/a                                                              | -1,66%              | -13,10           |      0 |
| BTC     | 1W   | Misto / nessuna divergenza | CONTESTO      | 83.007 $ / 58,51  | n/a                                                              | +6,87%              | 1,97             |      0 |
| SOL     | 1D   | Hidden bullish             | IN_FORMAZIONE | 109,54 $ / 43,47  | 2026-09-16 96,23 $ / RSI 51,17 → 2026-10-08 105,84 $ / RSI 43,11 | n/a                 | n/a              |      0 |
| SOL     | 1W   | Hidden bullish             | IN_FORMAZIONE | 109,54 $ / 56,85  | 2026-09-20 96,23 $ / RSI 61,01 → 2026-10-11 105,84 $ / RSI 56,85 | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Conferma ribassista        | CONTESTO      | 0.08535 $ / 41,25 | n/a                                                              | -11,80%             | -19,31           |      0 |
| DOGE    | 1W   | Misto / nessuna divergenza | CONTESTO      | 0.08535 $ / 46,43 | n/a                                                              | +3,96%              | 2,41             |      0 |

### BTC

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.

### SOL

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.

### DOGE

- **1D — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.
- **1W — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.

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
| BTC     | 1W   | Bullish regolare |          90 |           1 | +100,00%      | +32,26%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Bullish regolare |          30 |           1 | +100,00%      | +22,35%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Bullish regolare |          60 |           1 | +100,00%      | +35,62%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          30 |           2 | +50,00%       | -8,18%            | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          60 |           2 | 0,00%         | -25,06%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          90 |           1 | 0,00%         | -17,61%           | RACCOLTA DATI |      0 |
| DOGE    | 1W   | Hidden bearish   |          30 |           1 | 0,00%         | -13,35%           | RACCOLTA DATI |      0 |
| SOL     | 1W   | Hidden bearish   |          30 |           1 | +100,00%      | +1,11%            | RACCOLTA DATI |      0 |
| SOL     | 1W   | Hidden bearish   |          60 |           1 | 0,00%         | -30,59%           | RACCOLTA DATI |      0 |
| SOL     | 1W   | Hidden bearish   |          90 |           1 | 0,00%         | -43,43%           | RACCOLTA DATI |      0 |

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

Generato: 2026-10-11 05:33 UTC

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

| Asset   | Prezzo   |   Punteggio | Verdetto         | Trend            | Momentum        | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista                | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-----------------|:-----------------|:----------------|:------------------------------------------------------|----------------:|:---------------|:---------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 82.976 $ | 2 | NEUTRALE / MISTO | Trend rialzista | Momentum debole | Compressione / triangolo | 0 | +1 / TENUTO | Doppio minimo / MATURO | Doppio massimo / ATTIVO | 82.571 | 87.146 |
| SOL | 109,54 $ | -1 | NEUTRALE / MISTO | Trend rialzista | Momentum debole | Struttura ribassista con massimi e minimi decrescenti | 0 | 0 / TESTATO | Doppio minimo / TARGET RAGGIUNTO | Triplo massimo / CANDIDATO | 96,23 | 123,48 |
| DOGE | 0.08535 $ | -6 | DEBOLE | Trend ribassista | Momentum debole | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / NON ATTIVO | Doppio minimo / INVALIDATO | Doppio massimo / CANDIDATO | 0.07841 | 0.10528 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | MATURO | TARGET RAGGIUNTO | Eve and Adam Bottom — MATURO | ATTIVO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | INVALIDATO | CANDIDATO | ASSENTE | 0 |
| DOGE | INVALIDATO | ASSENTE | Adam and Eve Bottom — INVALIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 51.76 | -570.412 | 84.376 | 80.811 | 71.919 | 9,69% | 3,12% | 7,52% | 33,32% |
| SOL | 43.47 | -2.02876 | 117,73 | 108,53 | 86,71 | 16,48% | 4,78% | 6,98% | 46,32% |
| DOGE | 41.25 | -0.00158 | 0.09361 | 0.08904 | 0.08765 | 10,05% | -3,92% | 1,26% | 18,79% |

## Dettaglio asset

### BTC

- Prezzo: **82.976 $**
- Punteggio tecnico: **2 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 7.494e+04 -> 8.257e+04. Ultimi massimi: 8.736e+04 -> 8.715e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TENUTO** (+1)
  - Swing UP 2026-07-01 57.748 -> 2026-10-02 87.146; livello più vicino 23.6% a 80.208; stato TENUTO; confluenza: invalidazione rialzista.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (MATURO, +1); ribassista dominante: Doppio massimo (ATTIVO, -1).
- Supporto più vicino: **82.571**
- Resistenza più vicina: **87.146**

Pattern classici e ciclo di vita:

- Doppio minimo: **MATURO** (+1)
  - Due minimi simili vicino a 74.945 tra 2026-09-02 e 2026-09-15. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (20 giorni fa). Stato: MATURO. Target teorico: 89.580; progresso corrente: 9,76%. Relazione prezzo/neckline: vicino alla neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (20g); progresso 9,76%; prezzo vicino alla neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 58.076 dal 2026-06-25 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (53 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 75.744; progresso corrente: 181,87%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 75.744; breakout 2026-08-19 (53g); progresso 181,87%; prezzo sopra neckline.
- Eve and Adam Bottom: **MATURO** (+1)
  - Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (20 giorni fa). Stato: MATURO. Target teorico: 89.580; progresso corrente: 9,76%. Relazione prezzo/neckline: vicino alla neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (20g); progresso 9,76%; prezzo vicino alla neckline.
- Doppio massimo: **ATTIVO** (-1)
  - Due massimi simili vicino a 87.364 tra 2026-09-21 e 2026-10-02. Neckline ribassista stimata: 82.571. Breakout neckline: 2026-10-08 (3 giorni fa). Stato: ATTIVO. Target teorico: 77.778; progresso corrente: -8,47%. Relazione prezzo/neckline: vicino alla neckline.
  - neckline 82.571; target 77.778; breakout 2026-10-08 (3g); progresso -8,47%; prezzo vicino alla neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 87.364 dal 2026-09-03 al 2026-10-02. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni.
  - neckline 74.945; target 62.525; distanza dalla neckline 10,72%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 87.146 dal 2026-09-03 al 2026-10-02. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni.
  - neckline 74.945; target 62.743; distanza dalla neckline 10,72%; prezzo sopra neckline.

### SOL

- Prezzo: **109,54 $**
- Punteggio tecnico: **-1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 97.45 -> 96.23. Ultimi massimi: 124.6 -> 123.5.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-08-01 70,69 -> 2026-10-02 123,48; livello più vicino 23.6% a 111,02; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Triplo massimo (CANDIDATO, 0).
- Supporto più vicino: **96,23**
- Resistenza più vicina: **123,48**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 96,23 tra 2026-09-02 e 2026-09-16. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (23 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: 22,25%. Relazione prezzo/neckline: sopra neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (23g); progresso 22,25%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (53 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 383,65%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (53g); progresso 383,65%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 96,23 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (23 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: 22,25%. Relazione prezzo/neckline: sopra neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (23g); progresso 22,25%; prezzo sopra neckline.
- Doppio massimo: **INVALIDATO** (0)
  - Due massimi simili vicino a 110,04 tra 2026-08-27 e 2026-09-06. Neckline ribassista stimata: 97,45. Breakout neckline: 2026-09-15 (26 giorni fa). Stato: INVALIDATO. Target teorico: 84,86; progresso corrente: -96,04%. Relazione prezzo/neckline: sopra neckline.
  - neckline 97,45; target 84,86; breakout 2026-09-15 (26g); progresso -96,04%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 63 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 54,95%; prezzo sopra neckline.
- Adam/Eve Top: **ASSENTE** (0)

### DOGE

- Prezzo: **0.08535 $**
- Punteggio tecnico: **-6 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 0.07841 -> 0.09053. Ultimi massimi: 0.09421 -> 0.1053.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 46,58%. Fase non abbastanza chiara.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-09-22 0.10528 -> 2026-10-02 0.09053; livello più vicino 23.6% a 0.09401; stato NON ATTIVO; confluenza: neckline rialzista, invalidazione rialzista.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (INVALIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.07841**
- Resistenza più vicina: **0.10528**

Pattern classici e ciclo di vita:

- Doppio minimo: **INVALIDATO** (0)
  - Due minimi simili vicino a 0.07841 tra 2026-09-02 e 2026-09-16. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (20 giorni fa). Stato: INVALIDATO. Target teorico: 0.11001; progresso corrente: -56,06%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.09421; target 0.11001; breakout 2026-09-21 (20g); progresso -56,06%; prezzo sotto neckline.
- Triplo minimo: **ASSENTE** (0)
- Adam and Eve Bottom: **INVALIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.07841 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (20 giorni fa). Stato: INVALIDATO. Target teorico: 0.11001; progresso corrente: -56,06%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.09421; target 0.11001; breakout 2026-09-21 (20g); progresso -56,06%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.10528 tra 2026-08-22 e 2026-09-22. Neckline ribassista stimata: 0.07841. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 19 giorni.
  - neckline 0.07841; target 0.05153; distanza dalla neckline 8,86%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 61 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 25,56%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07380 dal 2026-07-26 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 61 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 25,56%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                                  |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-10-02 | 80.208 | 75.916 | 72.447 | 68.978 | 64.039 | 23.6% / 80.208 | TENUTO | invalidazione rialzista | +1 |
| SOL | UP 2026-08-01 -> 2026-10-02 | 111,02 | 103,32 | 97,09 | 90,86 | 81,99 | 23.6% / 111,02 | TESTATO | nessuna confluenza indipendente | 0 |
| DOGE | DOWN 2026-09-22 -> 2026-10-02 | 0.09401 | 0.09616 | 0.09791 | 0.09965 | 0.10212 | 23.6% / 0.09401 | NON ATTIVO | neckline rialzista, invalidazione rialzista | 0 |

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

- **BTC**: 41/30 previsioni controllate su 94 fatte. Stato: **ATTIVA**.
- **SOL**: 41/30 previsioni controllate su 94 fatte. Stato: **ATTIVA**.
- **DOGE**: 41/30 previsioni controllate su 94 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 94 | 41 | 30/30 [██████████] | 53 | ATTIVA | 2026-10-12 / tra 1 giorno |
| SOL | 94 | 41 | 30/30 [██████████] | 53 | ATTIVA | 2026-10-12 / tra 1 giorno |
| DOGE | 94 | 41 | 30/30 [██████████] | 53 | ATTIVA | 2026-10-12 / tra 1 giorno |

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

Generato: 2026-10-11 05:33 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 1 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 82.976 $          | 82.976 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.08535 $         | 0.08535 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 109,54 $          | 109,54 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 82.976 $          | 82.976 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 109,54 $          | 109,54 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.08535 $         | 0.08535 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 82.976 $          | 82.976 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 109,54 $          | 109,54 $        | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.08535 $         | 0.08535 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 82.976 $          | 82.976 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 109,54 $          | 109,54 $        | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.08535 $         | 0.08535 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 82.976 $          | 82.976 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 109,54 $          | 109,54 $        | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.08535 $         | 0.08535 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 82.976 $          | 83.007 $        | +0,0372%     |
| Exchange Microstructure | SOL     | price             | OK      | 109,54 $          | 109,61 $        | +0,0621%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.08535 $         | 0.08557 $       | +0,2578%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 109,54 $          | 109,54 $        | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 109,54 $          | 109,54 $        | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 109,54 $          | 109,54 $        | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 109,54 $          | 109,54 $        | +0,0000%     |

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
