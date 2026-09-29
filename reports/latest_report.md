<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-09-29 05:33 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | NEUTRALE / COSTRUTTIVO | HOLD / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | +1 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +2 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+1**, spot = **HOLD / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **+1**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+2**, spot = **STAI ALLA FINESTRA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+1**
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

- Global Confluence: **+1**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **HOLD LEGGERO / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 107,12; milestone analogiche 133,31 / 143,36, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 111,92 / 96,23 / 62,19.

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
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 1; EMA200 circa 111,39 $; upside verso EMA200 -5,28%. Non autorizza leva e non aggiunge punti automatici.
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

Generato: 2026-09-29 05:33 UTC

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

Segnali totali salvati: **228**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-29 | BTC | 83.140,92 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-29 | DOGE | 0.09319 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-29 | SOL | 117,59 | +1 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-28 | BTC | 82.981,23 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-28 | DOGE | 0.09299 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-28 | SOL | 118,67 | +4 | 0 | 0 | 0 | +2 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-27 | BTC | 84.404,98 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-27 | DOGE | 0.09592 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-27 | SOL | 120,66 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-26 | BTC | 83.890,58 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-26 | DOGE | 0.09735 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-26 | SOL | 120,35 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 76 | 75 | 74 | 73 | 71 | 70 | 69 | 67 | 60 | 51 | 36 | 23 |
| SOL | 76 | 75 | 74 | 73 | 71 | 70 | 69 | 67 | 60 | 51 | 36 | 23 |
| DOGE | 76 | 75 | 74 | 73 | 71 | 70 | 69 | 67 | 60 | 51 | 36 | 23 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-01 | 60g | 2026-09-30 | domani |
| SOL | 2026-08-01 | 60g | 2026-09-30 | domani |
| DOGE | 2026-08-01 | 60g | 2026-09-30 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 70 | 51,43% | +0,36% | +0,34% | UTILE |
| BTC | 2g | 69 | 50,72% | +0,62% | +0,55% | UTILE |
| BTC | 3g | 69 | 44,93% | +0,78% | +0,68% | UTILE |
| BTC | 5g | 68 | 44,12% | +1,73% | +1,55% | UTILE |
| BTC | 7g | 67 | 53,73% | +2,56% | +2,40% | UTILE |
| BTC | 10g | 66 | 62,12% | +3,62% | +3,48% | UTILE |
| BTC | 14g | 64 | 60,94% | +4,96% | +4,91% | UTILE |
| BTC | 21g | 57 | 70,18% | +8,22% | +8,11% | PRIMA CALIBRAZIONE |
| BTC | 30g | 48 | 93,75% | +13,82% | +12,93% | PRIMA CALIBRAZIONE |
| BTC | 45g | 34 | 91,18% | +24,41% | +20,52% | PRIMA CALIBRAZIONE |
| BTC | 60g | 21 | 85,71% | +25,88% | +18,73% | FEEDBACK RAPIDO |
| SOL | 1g | 67 | 50,75% | +0,41% | +0,32% | UTILE |
| SOL | 2g | 66 | 46,97% | +1,08% | +0,98% | UTILE |
| SOL | 3g | 65 | 53,85% | +1,83% | +1,70% | UTILE |
| SOL | 5g | 63 | 57,14% | +3,28% | +3,20% | UTILE |
| SOL | 7g | 62 | 62,90% | +4,70% | +4,78% | UTILE |
| SOL | 10g | 61 | 67,21% | +6,78% | +6,90% | UTILE |
| SOL | 14g | 60 | 75,00% | +9,47% | +10,08% | UTILE |
| SOL | 21g | 53 | 81,13% | +14,71% | +14,04% | PRIMA CALIBRAZIONE |
| SOL | 30g | 44 | 77,27% | +22,44% | +17,95% | PRIMA CALIBRAZIONE |
| SOL | 45g | 29 | 62,07% | +40,71% | +14,16% | FEEDBACK RAPIDO |
| SOL | 60g | 17 | 35,29% | +40,88% | -10,68% | FEEDBACK RAPIDO |
| DOGE | 1g | 71 | 43,66% | +0,24% | -0,12% | UTILE |
| DOGE | 2g | 70 | 42,86% | +0,50% | -0,20% | UTILE |
| DOGE | 3g | 69 | 39,13% | +0,86% | -0,06% | UTILE |
| DOGE | 5g | 67 | 43,28% | +1,99% | +0,13% | UTILE |
| DOGE | 7g | 66 | 50,00% | +2,92% | +0,56% | UTILE |
| DOGE | 10g | 65 | 46,15% | +3,76% | +0,55% | UTILE |
| DOGE | 14g | 63 | 60,32% | +5,33% | +4,30% | UTILE |
| DOGE | 21g | 56 | 67,86% | +8,09% | +4,51% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 48 | 81,25% | +13,04% | +7,85% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 34 | 41,18% | +24,19% | +0,68% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 22 | 18,18% | +24,79% | -12,16% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 70 | 51,43% | +0,36% | +0,34% | -0,19% | +0,88% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 75 | 52,00% | +0,32% | +0,34% | -0,20% | +0,85% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 75 | 52,00% | +0,32% | +0,34% | -0,20% | +0,85% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 68 | 41,18% | +0,32% | +0,02% | -0,14% | +0,86% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 29 | 37,93% | +0,73% | +0,06% | -0,13% | +1,26% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,24% | -0,24% | -0,87% | +0,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 69 | 50,72% | +0,62% | +0,55% | -0,14% | +1,31% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 74 | 54,05% | +0,65% | +0,72% | -0,09% | +1,35% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 74 | 54,05% | +0,65% | +0,72% | -0,09% | +1,35% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 67 | 41,79% | +0,59% | -0,02% | +0,02% | +1,30% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 29 | 41,38% | +1,20% | +0,02% | +0,19% | +1,90% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,04% | -0,04% | -0,90% | +1,02% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 69 | 44,93% | +0,78% | +0,68% | -1,21% | +2,52% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 73 | 52,05% | +0,99% | +1,02% | -1,18% | +2,69% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 73 | 52,05% | +0,99% | +1,02% | -1,18% | +2,69% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 66 | 34,85% | +1,04% | -0,23% | -1,10% | +2,74% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 29 | 37,93% | +1,95% | -0,51% | -0,85% | +3,41% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 68 | 44,12% | +1,73% | +1,55% | -1,80% | +4,08% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 71 | 49,30% | +1,93% | +1,93% | -1,77% | +4,31% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 71 | 49,30% | +1,93% | +1,93% | -1,77% | +4,31% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 64 | 40,62% | +1,85% | -0,79% | -1,69% | +4,29% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 29 | 41,38% | +4,06% | -2,25% | -1,22% | +6,21% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 14,29% | -1,43% | -1,43% | -2,57% | +1,68% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 67 | 53,73% | +2,56% | +2,40% | -2,07% | +5,36% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 70 | 58,57% | +2,80% | +2,80% | -2,05% | +5,58% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 70 | 58,57% | +2,80% | +2,80% | -2,05% | +5,58% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 63 | 42,86% | +2,90% | -1,15% | -1,97% | +5,64% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 28 | 39,29% | +5,77% | -4,00% | -1,37% | +8,77% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 33,33% | -1,39% | -1,39% | -2,98% | +2,35% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 66 | 62,12% | +3,62% | +3,48% | -2,36% | +6,64% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 69 | 65,22% | +3,74% | +3,74% | -2,35% | +6,82% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 69 | 65,22% | +3,74% | +3,74% | -2,35% | +6,82% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 62 | 50,00% | +3,92% | -0,37% | -2,28% | +7,01% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 28 | 42,86% | +5,84% | -4,46% | -1,59% | +9,49% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 64 | 60,94% | +4,96% | +4,91% | -2,67% | +8,60% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 67 | 61,19% | +5,04% | +5,04% | -2,65% | +8,69% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 67 | 61,19% | +5,04% | +5,04% | -2,65% | +8,69% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 62 | 58,06% | +5,55% | +1,64% | -2,50% | +9,26% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 26 | 26,92% | +4,97% | -3,71% | -1,95% | +9,52% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 57 | 70,18% | +8,22% | +8,11% | -2,81% | +12,15% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 60 | 75,00% | +8,16% | +8,16% | -2,79% | +12,10% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 60 | 75,00% | +8,16% | +8,16% | -2,79% | +12,10% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 55 | 52,73% | +8,75% | +0,47% | -2,64% | +12,76% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 24 | 54,17% | +8,85% | -4,04% | -2,32% | +12,73% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 48 | 93,75% | +13,82% | +12,93% | -2,52% | +17,96% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 51 | 90,20% | +13,70% | +13,70% | -2,52% | +17,97% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 51 | 90,20% | +13,70% | +13,70% | -2,52% | +17,97% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 46 | 54,35% | +13,81% | -0,68% | -2,31% | +18,32% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 19 | 57,89% | +14,77% | -4,67% | -2,09% | +19,29% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +5,40% | +5,40% | -4,01% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 34 | 91,18% | +24,41% | +20,52% | -2,81% | +29,20% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 36 | 100,00% | +24,33% | +24,33% | -2,85% | +29,06% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 36 | 100,00% | +24,33% | +24,33% | -2,85% | +29,06% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 32 | 100,00% | +24,74% | +24,74% | -2,65% | +29,54% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 31 | 38,71% | +24,87% | -4,03% | -2,59% | +29,66% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 6 | 0,00% | +25,15% | -25,15% | -1,17% | +32,97% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 21 | 85,71% | +25,88% | +18,73% | -3,18% | +31,15% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 23 | 100,00% | +25,76% | +25,76% | -3,22% | +31,11% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 23 | 100,00% | +25,76% | +25,76% | -3,22% | +31,11% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 19 | 100,00% | +26,42% | +26,42% | -2,95% | +32,13% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 18 | 27,78% | +25,82% | -13,12% | -2,87% | +31,52% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 2 | 0,00% | +32,21% | -32,21% | -2,23% | +37,27% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 71 | 43,66% | +0,24% | -0,12% | -0,56% | +1,28% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 74 | 58,11% | +0,16% | +0,49% | -0,65% | +1,14% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 74 | 58,11% | +0,16% | +0,49% | -0,65% | +1,14% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 68 | 50,00% | +0,07% | +0,14% | -0,76% | +1,05% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 43 | 39,53% | +0,09% | -0,68% | -0,78% | +0,85% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 70 | 42,86% | +0,50% | -0,20% | -0,62% | +1,88% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 73 | 60,27% | +0,35% | +0,84% | -0,75% | +1,65% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 73 | 60,27% | +0,35% | +0,84% | -0,75% | +1,65% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 67 | 50,75% | +0,01% | +0,08% | -1,10% | +1,31% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 43 | 41,86% | +0,42% | -1,35% | -0,82% | +1,40% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 69 | 39,13% | +0,86% | -0,06% | -2,26% | +4,03% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 72 | 55,56% | +0,71% | +1,10% | -2,36% | +3,74% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 72 | 55,56% | +0,71% | +1,10% | -2,36% | +3,74% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 66 | 43,94% | +0,02% | -0,05% | -2,63% | +2,98% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 43 | 30,23% | +0,67% | -2,36% | -2,59% | +3,92% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 67 | 43,28% | +1,99% | +0,13% | -3,18% | +6,72% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 70 | 51,43% | +1,87% | +1,32% | -3,22% | +6,48% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 70 | 51,43% | +1,87% | +1,32% | -3,22% | +6,48% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 64 | 51,56% | +1,02% | -0,60% | -3,64% | +5,68% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 42 | 33,33% | +2,31% | -4,80% | -3,56% | +7,06% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 66 | 50,00% | +2,92% | +0,56% | -3,66% | +8,99% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 69 | 53,62% | +2,93% | +1,29% | -3,69% | +8,77% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 69 | 53,62% | +2,93% | +1,29% | -3,69% | +8,77% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 63 | 47,62% | +1,91% | -0,85% | -4,17% | +7,74% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 41 | 29,27% | +3,84% | -6,44% | -3,92% | +9,49% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 65 | 46,15% | +3,76% | +0,55% | -4,30% | +11,06% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 68 | 48,53% | +3,66% | +0,88% | -4,30% | +10,86% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 68 | 48,53% | +3,66% | +0,88% | -4,30% | +10,86% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 62 | 51,61% | +2,31% | -1,27% | -4,85% | +9,30% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 41 | 31,71% | +4,20% | -7,07% | -4,70% | +11,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 60,00% | +1,26% | +0,96% | -3,68% | +10,47% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 63 | 60,32% | +5,33% | +4,30% | -5,05% | +14,13% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 66 | 62,12% | +4,93% | +3,22% | -5,01% | +13,72% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 66 | 62,12% | +4,93% | +3,22% | -5,01% | +13,72% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 60 | 53,33% | +2,76% | -0,24% | -5,66% | +10,90% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 39 | 43,59% | +4,76% | -4,49% | -5,47% | +12,94% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +5,41% | +1,04% | -4,48% | +13,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 56 | 67,86% | +8,09% | +4,51% | -5,04% | +18,64% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 59 | 66,10% | +8,47% | +6,51% | -5,06% | +18,85% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 59 | 66,10% | +8,47% | +6,51% | -5,06% | +18,85% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 53 | 64,15% | +6,15% | -0,61% | -5,81% | +15,44% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 34 | 52,94% | +5,05% | -6,23% | -5,53% | +14,31% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 66,67% | +6,54% | +0,57% | -4,75% | +18,76% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 48 | 81,25% | +13,04% | +7,85% | -4,71% | +26,39% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 50 | 84,00% | +13,29% | +10,72% | -4,72% | +26,92% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 50 | 84,00% | +13,29% | +10,72% | -4,72% | +26,92% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 44 | 56,82% | +11,64% | -4,82% | -5,60% | +24,19% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 31 | 48,39% | +10,82% | -8,72% | -5,10% | +22,58% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 87,50% | +21,36% | +13,45% | -4,45% | +31,96% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 34 | 41,18% | +24,19% | +0,68% | -4,14% | +41,64% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 36 | 55,56% | +24,05% | +6,48% | -4,16% | +41,55% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 36 | 55,56% | +24,05% | +6,48% | -4,16% | +41,55% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 34 | 58,82% | +23,81% | +8,52% | -4,18% | +41,55% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 31 | 3,23% | +22,00% | -19,88% | -4,65% | +40,34% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 23 | 0,00% | +23,20% | -23,20% | -4,66% | +40,46% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +37,31% | +15,91% | -1,31% | +47,38% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 22 | 18,18% | +24,79% | -12,16% | -5,55% | +41,52% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 23 | 30,43% | +25,27% | -3,11% | -5,61% | +41,65% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 23 | 30,43% | +25,27% | -3,11% | -5,61% | +41,65% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 21 | 33,33% | +23,91% | +0,37% | -5,78% | +41,00% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 23 | 0,00% | +25,27% | -25,27% | -5,61% | +41,65% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 19 | 0,00% | +24,44% | -24,44% | -5,42% | +41,36% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 67 | 50,75% | +0,41% | +0,32% | -0,32% | +1,31% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 69 | 55,07% | +0,39% | +0,46% | -0,44% | +1,28% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 72 | 54,17% | +0,42% | +0,40% | -0,41% | +1,30% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 67 | 46,27% | +0,39% | -0,02% | -0,51% | +1,25% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 49 | 46,94% | +0,64% | +0,07% | -0,41% | +1,61% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 66 | 46,97% | +1,08% | +0,98% | -0,16% | +2,15% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 69 | 49,28% | +0,95% | +0,75% | -0,42% | +1,85% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 72 | 48,61% | +0,92% | +0,70% | -0,41% | +1,89% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 66 | 40,91% | +0,75% | -0,07% | -0,38% | +1,89% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 48 | 47,92% | +0,87% | +0,37% | -0,41% | +1,93% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 65 | 53,85% | +1,83% | +1,70% | -1,73% | +4,25% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 68 | 51,47% | +1,60% | +1,32% | -1,91% | +4,02% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 71 | 50,70% | +1,55% | +1,25% | -1,88% | +3,99% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 65 | 46,15% | +1,16% | -0,22% | -1,93% | +3,52% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 47 | 51,06% | +1,19% | +0,57% | -1,88% | +3,50% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 63 | 57,14% | +3,28% | +3,20% | -2,43% | +6,76% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 66 | 53,03% | +2,96% | +2,13% | -2,59% | +6,43% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 69 | 52,17% | +2,86% | +2,01% | -2,57% | +6,32% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 63 | 46,03% | +2,54% | -0,50% | -2,65% | +5,83% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 45 | 53,33% | +1,82% | +0,98% | -2,60% | +5,07% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 62 | 62,90% | +4,70% | +4,78% | -2,84% | +8,71% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 65 | 60,00% | +4,30% | +3,32% | -3,00% | +8,33% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 68 | 60,29% | +4,11% | +3,18% | -2,99% | +8,13% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 62 | 40,32% | +3,21% | -1,40% | -3,11% | +7,34% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 44 | 47,73% | +1,74% | +0,98% | -3,11% | +5,91% | PRIMA CALIBRAZIONE |
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

Generato: 2026-09-29 05:33 UTC

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
| BTC | 76 | UTILE | 75 | 20 | 15 | 0 | Famiglia statistica | 1g | 52,00% | +0,34% | campione utile, valutare con prudenza |
| SOL | 76 | UTILE | 69 | 29 | 14 | 0 | Famiglia statistica | 1g | 55,07% | +0,46% | campione utile, valutare con prudenza |
| DOGE | 76 | UTILE | 74 | 29 | 14 | 0 | Famiglia statistica | 1g | 58,11% | +0,49% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 29 | 37,93% | +0,06% | +0,73% | -0,13% | +1,26% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 75 | 52,00% | +0,34% | +0,32% | -0,20% | +0,85% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 7 | 42,86% | -0,24% | -0,24% | -0,87% | +0,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 68 | 41,18% | +0,02% | +0,32% | -0,14% | +0,86% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 29 | 41,38% | +0,02% | +1,20% | +0,19% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 74 | 54,05% | +0,72% | +0,65% | -0,09% | +1,35% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 7 | 28,57% | -0,04% | -0,04% | -0,90% | +1,02% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 67 | 41,79% | -0,02% | +0,59% | +0,02% | +1,30% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 29 | 37,93% | -0,51% | +1,95% | -0,85% | +3,41% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 73 | 52,05% | +1,02% | +0,99% | -1,18% | +2,69% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 66 | 34,85% | -0,23% | +1,04% | -1,10% | +2,74% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 29 | 41,38% | -2,25% | +4,06% | -1,22% | +6,21% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 71 | 49,30% | +1,93% | +1,93% | -1,77% | +4,31% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 7 | 14,29% | -1,43% | -1,43% | -2,57% | +1,68% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 64 | 40,62% | -0,79% | +1,85% | -1,69% | +4,29% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 28 | 39,29% | -4,00% | +5,77% | -1,37% | +8,77% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 70 | 58,57% | +2,80% | +2,80% | -2,05% | +5,58% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 6 | 33,33% | -1,39% | -1,39% | -2,98% | +2,35% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 63 | 42,86% | -1,15% | +2,90% | -1,97% | +5,64% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 28 | 42,86% | -4,46% | +5,84% | -1,59% | +9,49% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 69 | 65,22% | +3,74% | +3,74% | -2,35% | +6,82% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 62 | 50,00% | -0,37% | +3,92% | -2,28% | +7,01% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 26 | 26,92% | -3,71% | +4,97% | -1,95% | +9,52% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 67 | 61,19% | +5,04% | +5,04% | -2,65% | +8,69% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 62 | 58,06% | +1,64% | +5,55% | -2,50% | +9,26% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 24 | 54,17% | -4,04% | +8,85% | -2,32% | +12,73% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 60 | 75,00% | +8,16% | +8,16% | -2,79% | +12,10% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 55 | 52,73% | +0,47% | +8,75% | -2,64% | +12,76% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 19 | 57,89% | -4,67% | +14,77% | -2,09% | +19,29% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 51 | 90,20% | +13,70% | +13,70% | -2,52% | +17,97% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 3 | 100,00% | +5,40% | +5,40% | -4,01% | +8,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 46 | 54,35% | -0,68% | +13,81% | -2,31% | +18,32% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 6 | 0,00% | -25,15% | +25,15% | -1,17% | +32,97% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 36 | 100,00% | +24,33% | +24,33% | -2,85% | +29,06% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 31 | 38,71% | -4,03% | +24,87% | -2,59% | +29,66% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 2 | 0,00% | -32,21% | +32,21% | -2,23% | +37,27% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 23 | 100,00% | +25,76% | +25,76% | -3,22% | +31,11% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 18 | 27,78% | -13,12% | +25,82% | -2,87% | +31,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 43 | 39,53% | -0,68% | +0,09% | -0,78% | +0,85% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 74 | 58,11% | +0,49% | +0,16% | -0,65% | +1,14% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 11 | 63,64% | +2,53% | +2,82% | +0,75% | +3,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 68 | 50,00% | +0,14% | +0,07% | -0,76% | +1,05% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 43 | 41,86% | -1,35% | +0,42% | -0,82% | +1,40% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 73 | 60,27% | +0,84% | +0,35% | -0,75% | +1,65% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 11 | 45,45% | +2,65% | +2,89% | +1,08% | +5,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 67 | 50,75% | +0,08% | +0,01% | -1,10% | +1,31% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 43 | 30,23% | -2,36% | +0,67% | -2,59% | +3,92% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 72 | 55,56% | +1,10% | +0,71% | -2,36% | +3,74% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 11 | 54,55% | +2,62% | +2,81% | -1,35% | +6,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 66 | 43,94% | -0,05% | +0,02% | -2,63% | +2,98% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 42 | 33,33% | -4,80% | +2,31% | -3,56% | +7,06% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 70 | 51,43% | +1,32% | +1,87% | -3,22% | +6,48% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 11 | 36,36% | +2,02% | +2,17% | -2,50% | +9,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 64 | 51,56% | -0,60% | +1,02% | -3,64% | +5,68% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 41 | 29,27% | -6,44% | +3,84% | -3,92% | +9,49% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 69 | 53,62% | +1,29% | +2,93% | -3,69% | +8,77% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 11 | 45,45% | +0,78% | +0,88% | -3,00% | +9,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 63 | 47,62% | -0,85% | +1,91% | -4,17% | +7,74% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 41 | 31,71% | -7,07% | +4,20% | -4,70% | +11,63% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 68 | 48,53% | +0,88% | +3,66% | -4,30% | +10,86% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 10 | 60,00% | +0,96% | +1,26% | -3,68% | +10,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 62 | 51,61% | -1,27% | +2,31% | -4,85% | +9,30% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 39 | 43,59% | -4,49% | +4,76% | -5,47% | +12,94% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 66 | 62,12% | +3,22% | +4,93% | -5,01% | +13,72% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 9 | 44,44% | +1,04% | +5,41% | -4,48% | +13,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 60 | 53,33% | -0,24% | +2,76% | -5,66% | +10,90% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 34 | 52,94% | -6,23% | +5,05% | -5,53% | +14,31% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 59 | 66,10% | +6,51% | +8,47% | -5,06% | +18,85% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 9 | 66,67% | +0,57% | +6,54% | -4,75% | +18,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 53 | 64,15% | -0,61% | +6,15% | -5,81% | +15,44% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 31 | 48,39% | -8,72% | +10,82% | -5,10% | +22,58% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 50 | 84,00% | +10,72% | +13,29% | -4,72% | +26,92% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 8 | 87,50% | +13,45% | +21,36% | -4,45% | +31,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 44 | 56,82% | -4,82% | +11,64% | -5,60% | +24,19% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 23 | 0,00% | -23,20% | +23,20% | -4,66% | +40,46% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 36 | 55,56% | +6,48% | +24,05% | -4,16% | +41,55% | PESO OK | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,91% | +37,31% | -1,31% | +47,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 31 | 3,23% | -19,88% | +22,00% | -4,65% | +40,34% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 19 | 0,00% | -24,44% | +24,44% | -5,42% | +41,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 23 | 30,43% | -3,11% | +25,27% | -5,61% | +41,65% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 23 | 0,00% | -25,27% | +25,27% | -5,61% | +41,65% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 49 | 46,94% | +0,07% | +0,64% | -0,41% | +1,61% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 69 | 55,07% | +0,46% | +0,39% | -0,44% | +1,28% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 67 | 46,27% | -0,02% | +0,39% | -0,51% | +1,25% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 48 | 47,92% | +0,37% | +0,87% | -0,41% | +1,93% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 69 | 49,28% | +0,75% | +0,95% | -0,42% | +1,85% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 66 | 40,91% | -0,07% | +0,75% | -0,38% | +1,89% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 47 | 51,06% | +0,57% | +1,19% | -1,88% | +3,50% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 68 | 51,47% | +1,32% | +1,60% | -1,91% | +4,02% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 65 | 46,15% | -0,22% | +1,16% | -1,93% | +3,52% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 45 | 53,33% | +0,98% | +1,82% | -2,60% | +5,07% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 66 | 53,03% | +2,13% | +2,96% | -2,59% | +6,43% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 63 | 46,03% | -0,50% | +2,54% | -2,65% | +5,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 44 | 47,73% | +0,98% | +1,74% | -3,11% | +5,91% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 65 | 60,00% | +3,32% | +4,30% | -3,00% | +8,33% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 62 | 40,32% | -1,40% | +3,21% | -3,11% | +7,34% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 43 | 53,49% | +1,15% | +2,06% | -3,69% | +6,79% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 64 | 64,06% | +5,66% | +6,37% | -3,41% | +10,47% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 61 | 47,54% | -1,59% | +4,62% | -3,59% | +8,98% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 42 | 52,38% | +2,18% | +3,36% | -4,30% | +8,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 62 | 75,81% | +8,45% | +9,10% | -3,90% | +13,90% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 60 | 45,00% | -2,12% | +6,76% | -4,07% | +11,88% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 41 | 63,41% | -0,67% | +10,79% | -4,62% | +15,70% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 55 | 81,82% | +14,60% | +14,66% | -4,18% | +20,18% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 57 | 52,63% | -5,85% | +12,41% | -4,51% | +17,92% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 32 | 40,62% | -10,28% | +24,55% | -4,07% | +29,78% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 46 | 86,96% | +21,55% | +24,92% | -3,84% | +31,28% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 48 | 31,25% | -12,99% | +22,11% | -4,29% | +28,12% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 21 | 0,00% | -38,81% | +38,81% | -4,64% | +48,52% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 32 | 75,00% | +25,78% | +40,58% | -4,69% | +48,45% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,56% | +44,56% | -5,94% | +49,24% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 34 | 11,76% | -33,19% | +38,98% | -5,09% | +47,07% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 15 | 0,00% | -49,72% | +49,72% | -6,02% | +56,18% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 19 | 57,89% | +17,25% | +45,97% | -6,82% | +52,85% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +41,93% | +41,93% | -9,62% | +45,82% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 23 | 17,39% | -32,58% | +44,37% | -6,82% | +51,71% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 71 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 75 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 87 | 39,08% | -0,14% |
| BTC | BREVE | Famiglia statistica | 222 | 52,70% | +0,69% |
| BTC | BREVE | Microstruttura exchange | 21 | 33,33% | -0,22% |
| BTC | BREVE | Tecnico | 201 | 39,30% | -0,08% |
| BTC | SETTIMANALE | Classic technical | 85 | 41,18% | -3,55% |
| BTC | SETTIMANALE | Famiglia statistica | 210 | 57,62% | +2,82% |
| BTC | SETTIMANALE | Microstruttura exchange | 18 | 27,78% | -1,45% |
| BTC | SETTIMANALE | Tecnico | 189 | 44,44% | -0,77% |
| BTC | SWING | Classic technical | 50 | 40,00% | -3,87% |
| BTC | SWING | Famiglia statistica | 127 | 67,72% | +6,51% |
| BTC | SWING | Microstruttura exchange | 10 | 60,00% | +0,93% |
| BTC | SWING | Tecnico | 117 | 55,56% | +1,09% |
| BTC | MEDIO | Classic technical | 27 | 40,74% | -11,26% |
| BTC | MEDIO | Famiglia statistica | 110 | 95,45% | +19,70% |
| BTC | MEDIO | Microstruttura exchange | 5 | 100,00% | +12,53% |
| BTC | MEDIO | Tecnico | 95 | 44,21% | -4,13% |
| DOGE | BREVE | Classic technical | 129 | 37,21% | -1,46% |
| DOGE | BREVE | Famiglia statistica | 219 | 57,99% | +0,81% |
| DOGE | BREVE | Microstruttura exchange | 33 | 54,55% | +2,60% |
| DOGE | BREVE | Tecnico | 201 | 48,26% | +0,06% |
| DOGE | SETTIMANALE | Classic technical | 124 | 31,45% | -6,09% |
| DOGE | SETTIMANALE | Famiglia statistica | 207 | 51,21% | +1,17% |
| DOGE | SETTIMANALE | Microstruttura exchange | 32 | 46,88% | +1,26% |
| DOGE | SETTIMANALE | Tecnico | 189 | 50,26% | -0,90% |
| DOGE | SWING | Classic technical | 73 | 47,95% | -5,30% |
| DOGE | SWING | Famiglia statistica | 125 | 64,00% | +4,77% |
| DOGE | SWING | Microstruttura exchange | 18 | 55,56% | +0,80% |
| DOGE | SWING | Tecnico | 113 | 58,41% | -0,41% |
| DOGE | MEDIO | Classic technical | 73 | 20,55% | -17,37% |
| DOGE | MEDIO | Famiglia statistica | 109 | 63,30% | +6,40% |
| DOGE | MEDIO | Microstruttura exchange | 14 | 85,71% | +18,65% |
| DOGE | MEDIO | Tecnico | 98 | 26,53% | -14,39% |
| SOL | BREVE | Classic technical | 144 | 48,61% | +0,33% |
| SOL | BREVE | Famiglia statistica | 206 | 51,94% | +0,84% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 198 | 44,44% | -0,10% |
| SOL | SETTIMANALE | Classic technical | 132 | 51,52% | +1,04% |
| SOL | SETTIMANALE | Famiglia statistica | 195 | 58,97% | +3,69% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 186 | 44,62% | -1,16% |
| SOL | SWING | Classic technical | 83 | 57,83% | +0,77% |
| SOL | SWING | Famiglia statistica | 117 | 78,63% | +11,34% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 117 | 48,72% | -3,94% |
| SOL | MEDIO | Classic technical | 68 | 19,12% | -27,79% |
| SOL | MEDIO | Famiglia statistica | 97 | 77,32% | +22,11% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 8 | 100,00% | +29,97% |
| SOL | MEDIO | Tecnico | 105 | 21,90% | -23,82% |

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
| BTC     |         76 |              51 |          25 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         76 |              51 |          25 | OSSERVAZIONE 30+ | 1,96%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         76 |              51 |          25 | OSSERVAZIONE 30+ | 17,65%           | 5,88%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | MEDIO          | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo       |
| SOL     | ALTO           | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo       |
| DOGE    | ALTO           | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-09-29 05:33 UTC

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
| BTC | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD / ATTESA CONFERME | Prima resistenza sopra 87.364; conferma del doppio minimo sopra 82.262. | Sotto 74.945 il quadro tecnico peggiora. |
| SOL | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 107,12; milestone analogiche 133,31 / 143,36, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 111,92 / 96,23 / 62,19. |
| DOGE | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.10528 migliora; sopra 0.07997 viene invalidato il pattern ribassista dominante. | Sotto 0.07841 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -1 | 0 | -1 | 0 | +2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 |
| SOL | -1 | 0 | -1 | 0 | +2 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | +1 |
| DOGE | -1 | 0 | -1 | 0 | +3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +2 |

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

- Famiglia statistica: **-1** — Scanner grezzo -1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-1** — Casi positivi 42,50%, return centrale 30g -2,32%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 74. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+2** — Score tecnico 6/12, verdetto costruttivo ma non confermato, trend rialzista, struttura volatilità in espansione, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score +2 (rialzista Doppio minimo / CONFERMATO RECENTE; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 3/12, verdetto ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — BTC: nessun cambiamento forte in misto rispetto a ieri.

Conferme: Prima resistenza sopra 87.364; conferma del doppio minimo sopra 82.262.

Invalidazioni: Sotto 74.945 il quadro tecnico peggiora.

### SOL

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**

SOL è ancora in zona mista. Il frattale resta soltanto uno scenario contestuale: non è confermato dal prezzo e vale 0 punti operativi finché il gap non rientra. Meglio evitare leva e ragionare solo a tranche piccole.

Dettaglio moduli:

- Famiglia statistica: **-1** — Scanner grezzo -1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-1** — Casi positivi 45,00%, return centrale 30g -1,92%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 74. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+2** — Score tecnico 6/12, verdetto costruttivo ma non confermato, trend rialzista, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Triplo massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 8/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto STRUTTURA ANALOGA, PREZZO NON ADERENTE, somiglianza strutturale +70,73%, aderenza live +67,72%, errore live +16,14%, gap corrente +19,38%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE NON CONFERMATO DAL PREZZO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 71, ma percorso ancorato non aderente: gap +19,38%, errore live +16,14%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 1, bias CONTESTO DA OSSERVARE, EMA200 111,39 $, upside EMA200 -5,28%, gap EMA50/EMA200 -4,71%, hit EMA200 12w +100,00%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — SOL: cambiamento medio in peggioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 107,12; milestone analogiche 133,31 / 143,36, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 111,92 / 96,23 / 62,19.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **-1** — Scanner grezzo -1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-1** — Casi positivi 40,00%, return centrale 30g -11,04%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 74. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 9/12, verdetto rialzista tecnico, trend rialzista, struttura volatilità in espansione, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score +2 (rialzista Doppio minimo / CONFERMATO RECENTE; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 3/12, verdetto ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff RANGE / FASE NON CHIARA, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow -1.25, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 0, bear 3, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE NEGATIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in peggioramento rispetto a ieri.

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

Generato: 2026-09-29 05:33 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 83.141 $ | prezzo corrente |
| Power Law centrale | 126.001 $ | deviazione -34,02% |
| Banda p10-p90 | 78.371 $ / 317.995 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 16,11% | posizione storica nel corridoio |
| Esponente β | 5,7918 | R² log-log 91,94% |
| Stabilità β | BASSA | range 1,3163 cambiando finestra |
| Ultimo halving | 2024-04-19 | 893 giorni fa |
| Fase ciclo | 61,12% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-09-29 (4395 osservazioni)
- Formula stimata: prezzo ≈ exp(-38.9622) × giorni^5.7918
- Prezzo centrale oggi: **126.001 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 16,11%
- Scarto dal centro: **-34,02%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,7918 | 91,94% |
| 2015 | 5,8725 | 91,48% |
| 2016 | 5,5551 | 87,75% |
| 2017 | 4,8298 | 83,00% |
| 2018 | 4,5562 | 78,55% |

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
| 2012-11-28 → 2016-07-09 | 2015-02-12 | +27,11% | +6,59% | +21,93% | +73,28% |
| 2016-07-09 → 2020-05-11 | 2018-11-13 | -47,89% | -42,63% | +9,64% | +38,51% |
| 2020-05-11 → 2024-04-19 | 2022-10-08 | +6,11% | -12,69% | +44,43% | +43,87% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 7 | 1 | 4.807400771893922 | 0 |
| DOGE | DOGE/BTC | RELATIVA MISTA / NON CONFERMATA | 0 | 0 | 2.840095872856252 | 0 |

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

Generato: 2026-09-29 05:32 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00141490 | +7 | +1 | 0 | SOVRAPERFORMA BTC | MEDIA | +4,81% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000112 | 0 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +2,84% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** SOVRAPERFORMA BTC (+7)
- **Candidato futuro:** +1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** CONFERMA FORTE: sale in USD e batte BTC
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g +3,20%; 30g +4,81%; 90g +12,65%; 180g +18,70%
- **Daily:** RSI 61.61; MA50 0.00129502; MA200 0.00119356
- **Weekly:** MA30 0.00120440; RSI 62.30
- **Livelli:** supporto 0.00127800; resistenza 0.00146600; breakout 60g 0.00145900; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00133900; target 0.00140150
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00135815
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; struttura con massimi/minimi crescenti; RSI relativo forte; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (0)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g -2,56%; 30g +2,84%; 90g -8,83%; 180g -17,23%
- **Daily:** RSI 51.33; MA50 0.00000111; MA200 0.00000123
- **Weekly:** MA30 0.00000123; RSI 42.48
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
| SOL | 7g | 210 | 52,86% | +1,98% | -1,04% |
| SOL | 30g | 207 | 47,83% | +4,57% | +0,63% |
| SOL | 90g | 201 | 52,74% | +9,80% | +3,09% |
| DOGE | 7g | 296 | 55,41% | +1,80% | -1,66% |
| DOGE | 30g | 294 | 53,06% | +1,97% | -3,49% |
| DOGE | 90g | 288 | 54,17% | +6,90% | -9,24% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 42 | 57,14% | +0,32% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 40 | 57,50% | +0,86% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 36 | 44,44% | +0,65% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 35 | 45,71% | +0,59% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 27 | 44,44% | -2,13% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 54 | 66,67% | -0,02% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 54 | 57,41% | +0,01% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 54 | 53,70% | -0,56% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 52 | 51,92% | -0,45% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 40 | 57,50% | -0,21% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **29 settembre 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 117,81 $ | 2026-09-29T05:30:21Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 117,65 $ | 2026-09-29T05:32:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 1m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | -0,16000 $ | -0,14% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=117.80999755859375
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-09-29T05:30:21Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=117.6500015258789
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-09-29T05:32:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-09-29T05:32:13Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=112.621077
ANCHOR_AGE_HOURS=0.0312836325
CURRENT_VS_ANCHOR_GAP_USD=-0.15999603271484375
CURRENT_VS_ANCHOR_GAP_PCT=-0.13580853580381635
```

## Verdetto: STRUTTURA ANALOGA, PREZZO NON ADERENTE

- **Fase attuale:** FRATTALE NON CONFERMATO DAL PREZZO
- **Somiglianza totale:** +70,73%
- **Somiglianza strutturale:** +70,73%
- **Aderenza prezzo live:** +67,72%
- **Errore medio live:** +16,14%
- **Gap prezzo corrente:** +19,38%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA / NON OPERATIVO
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** La geometria ricorda BTC 2022, ma SOL è troppo distante dal percorso scalato per usarlo come conferma operativa.
- **SOL è al giorno:** 115 dal bottom usato.
- **Giorno BTC equivalente:** 2023-03-16
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Spinta rialzista abbastanza pulita.** Zona bassa **117,81 $** intorno al **29 settembre 2026**; zona alta **133,31 $** intorno al **12 ottobre 2026**; fine step circa **131,83 $** entro il **13 ottobre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=STRUTTURA ANALOGA, PREZZO NON ADERENTE
PRICE_ADHERENCE_FAILED=YES
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=YES
PRICE_ADHERENCE_LAST_GAP_FAILED=YES
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=16.13819788479942
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=19.375252490792306
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 29 settembre 2026 | 89 | +67,72% | +16,14% | +19,38% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 29 settembre 2026 | 116 | +72,43% | +13,78% | +19,38% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: STRUTTURA ANALOGA, PREZZO NON ADERENTE.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: STRUTTURA ANALOGA, PREZZO NON ADERENTE. |
| Aderenza live | +67,72% | Errore medio live +16,14%. |
| Gap corrente | +19,38% | Prezzo non aderente: superata almeno una soglia canonica (15% medio / 18% ultimo). |
| Prima conferma prezzo | 133,31 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 143,36 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 111,92 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 586,65 $ |
| Massimo percorso base | 586,65 $ (21 aprile 2029) |

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
| Prima conferma | 133,31 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 143,36 $ | Scenario più credibile. |
| Invalidazione soft | 111,92 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 6 ottobre 2026 | +13,10% | 133,24 $ | 117,81 $ | 133,24 $ |
| 14 giorni | 13 ottobre 2026 | +11,90% | 131,83 $ | 117,81 $ | 133,31 $ |
| 30 giorni | 29 ottobre 2026 | +21,02% | 142,57 $ | 117,81 $ | 143,36 $ |
| 60 giorni | 28 novembre 2026 | +8,54% | 127,87 $ | 117,81 $ | 143,36 $ |
| 90 giorni | 28 dicembre 2026 | +0,29% | 118,15 $ | 117,81 $ | 143,36 $ |
| 120 giorni | 27 gennaio 2027 | +21,08% | 142,65 $ | 117,81 $ | 148,02 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 29 settembre 2026 -> 13 ottobre 2026 | +11,90% | 117,81 $ (29 settembre 2026) | 133,31 $ (12 ottobre 2026) | 131,83 $ | Spinta rialzista abbastanza pulita. |
| Step 2 - primo mese | 14 ottobre 2026 -> 29 ottobre 2026 | +21,02% | 130,68 $ (17 ottobre 2026) | 143,36 $ (28 ottobre 2026) | 142,57 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 30 ottobre 2026 -> 28 novembre 2026 | +8,54% | 125,95 $ (26 novembre 2026) | 142,94 $ (1 novembre 2026) | 127,87 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 29 novembre 2026 -> 28 dicembre 2026 | +0,29% | 118,15 $ (28 dicembre 2026) | 132,07 $ (11 dicembre 2026) | 118,15 $ | Spike poco sostenuto. |

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
| Prezzo SOL | 117,81 $ |  |
| Weekly RSI | 62,48 / linea grezza 51,53 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 49,95 / linea grezza 55,48 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 586,65 $ | Avanzamento +20,08% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 50,0, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Score on-chain | -1 |
| Bias | NEUTRALE / MISTA |
| Azione coerente | NESSUNA CONFERMA FORTE / LEGGERE INSIEME AL FRATTALE |
| Prezzo SOL | 117,81 $ |
| TVL Solana | 6,44 mld $ |
| TVL 7g | -0,28% |
| DEX volume 24h | 2,29 mld $ |
| Fees 24h | 17,45 mln $ |
| Stablecoin su Solana | 16,60 mld $ |
| Stake ratio | 69,50% |
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

| Voce                      | Valore                       |
|:--------------------------|:-----------------------------|
| Lifecycle squeeze score | 1 |
| Bias | CONTESTO DA OSSERVARE |
| Azione coerente | SOLO OSSERVAZIONE |
| Peso suggerito Global | 0 |
| Trend squeeze | STABILE / DA CONFERMARE |
| Trend squeeze score | 0 |
| Confronto precedente | 2026-09-28 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 117,81 $ |
| EMA200 weekly target | 111,39 $ |
| Upside verso EMA200 | -5,28% |
| Distanza prezzo da EMA200 | +5,58% |
| Gap EMA50/EMA200 | -4,71% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 62,34 |
| Età SOL | 6,5 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +100,00% |
| Max gain mediano 12w | +36,72% |
| Drawdown mediano 12w | -31,00% |

Lettura semplice:

**SOLO OSSERVAZIONE**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-09-29 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-09-29 05:30:22 UTC**

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
| BTC | NESSUN CAMBIAMENTO FORTE | misto | NEUTRALE / INCERTO | +42.50% | -2.50 punti |
| SOL | CAMBIAMENTO MEDIO | peggioramento | NEUTRALE / INCERTO | +45.00% | -5.00 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | peggioramento | NEUTRALE / INCERTO | +40.00% | -2.50 punti |

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
| BTC | 79.081 $ | 91.567 $ | +42,31% | +15,79% | rimbalzo debole | 91.567 $ | 79.081 $ | +33,33% | -13,64% | spike storicamente più resistente |
| SOL | 111,92 $ | 129,59 $ | +35,71% | +15,79% | rimbalzo debole | 129,59 $ | 111,92 $ | +25,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08877 $ | 0,10278 $ | +30,00% | +15,79% | rimbalzo poco frequente | 0,10278 $ | 0,08877 $ | +30,00% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 26 prima sono scesi a -5,00%. Tra quei 26, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +42,31% (11/26). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 27 prima sono saliti a +10,00%. Tra quei 27, 9 poi sono scaricati a -5,00%. Percentuale: +33,33% (9/27). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 10 poi sono rimbalzati fino a +10,00%. Percentuale: +35,71% (10/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **SOL: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 6 poi sono scaricati a -5,00%. Percentuale: +25,00% (6/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +30,00% (9/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 20 prima sono saliti a +10,00%. Tra quei 20, 6 poi sono scaricati a -5,00%. Percentuale: +30,00% (6/20). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-09-29 05:31:57 UTC

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-09-29 | 2026-09-29T05:30:21Z | 2026-09-29 05:30:22 |
| SOL | 2026-09-29 | 2026-09-29T05:30:21Z | 2026-09-29 05:30:22 |
| DOGE | 2026-09-29 | 2026-09-29T05:30:21Z | 2026-09-29 05:30:22 |

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
| BTC | 2026-09-29 | 83.243 $ | INCERTO | 42,50% | 69.097,84 $ | 71.388,57 $ | 81.312,25 $ | 96.761,66 $ | 112.715,59 $ |
| SOL | 2026-09-29 | 117,81 $ | INCERTO | 45,00% | 91,89 $ | 100,46 $ | 115,55 $ | 135,81 $ | 185,25 $ |
| DOGE | 2026-09-29 | 0.09344 $ | DISCESA | 40,00% | 0.06892 $ | 0.07886 $ | 0.08312 $ | 0.10532 $ | 0.15157 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | AVAILABLE | SAME_BTC_REGIME | 0 | 1 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 81.312,25 $ | 86.661,15 $ | 112.715,59 $ | 96.387,34 $ |
| SOL | AVAILABLE | SAME_BTC_REGIME | 0 | 3 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 115,55 $ | 127,21 $ | 185,25 $ | 153,30 $ |
| DOGE | AVAILABLE | SAME_BTC_REGIME | 0 | 1 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.08312 $ | 0.09854 $ | 0.15157 $ | 0.12269 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-08-30**; verificato fino al **2026-09-29**; stato **COMPLETO 30/30g**.
- Reale **83.193,77 $**; p50 previsto **83.155,92 $**; scarto **0,05%**.
- Errore medio assoluto **3,39%**; massimo **10,26%**; DENTRO p10-p90; DENTRO p25-p75.

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

**Campione corrente:** 10 episodi qualificati su 40 · 10 asset distinti.

![SOL conditional successor corrente](scanner_forecast_SOL_conditional_successor_current.png)

###### Confronto diretto a 30 giorni

| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Cono standard | 2026-09-29 | 40 | 2026-10-29 | 91.89 $ | 100.46 $ | 115.55 $ | 135.81 $ | 185.25 $ |
| Conditional corrente | 2026-09-29 | 10 | 2026-10-29 | 86.42 $ | 98.60 $ | 116.24 $ | 143.01 $ | 213.57 $ |

###### Struttura successiva dei casi correnti

| Classe | Episodi | Frequenza empirica |
| --- | ---: | ---: |
| DIRECT_CONTINUATION | 7 | 70.00% |
| SHALLOW_PULLBACK_THEN_CONTINUATION | 0 | 0.00% |
| DEEP_PULLBACK_THEN_RECOVERY | 1 | 10.00% |
| FAILURE | 2 | 20.00% |
| UNRESOLVED | 0 | 0.00% |

###### Episodi qualificati oggi

| Asset | Match window | -5% hit | +10% anchor | Classe 60d |
| --- | --- | --- | --- | --- |
| RUNE-USD | 2023-06-16 → 2023-09-23 | 2023-10-09 | 2023-10-23 | DIRECT_CONTINUATION |
| EGLD-USD | 2023-09-03 → 2023-12-11 | 2023-12-15 | 2023-12-24 | FAILURE |
| BTC-USD | 2022-11-16 → 2023-02-23 | 2023-03-03 | 2023-03-17 | DIRECT_CONTINUATION |
| VET-USD | 2023-09-05 → 2023-12-13 | 2023-12-15 | 2023-12-20 | FAILURE |
| THETA-USD | 2023-09-02 → 2023-12-10 | 2023-12-11 | 2023-12-24 | DIRECT_CONTINUATION |
| KSM-USD | 2023-09-01 → 2023-12-09 | 2023-12-11 | 2023-12-23 | DIRECT_CONTINUATION |
| HBAR-USD | 2020-11-14 → 2021-02-21 | 2021-02-22 | 2021-03-08 | DIRECT_CONTINUATION |
| SOL-USD | 2020-11-05 → 2021-02-12 | 2021-02-13 | 2021-02-19 | DEEP_PULLBACK_THEN_RECOVERY |
| BNB-USD | 2025-05-15 → 2025-08-22 | 2025-08-25 | 2025-09-17 | DIRECT_CONTINUATION |
| OP-USD | 2023-09-04 → 2023-12-12 | 2023-12-15 | 2023-12-22 | DIRECT_CONTINUATION |

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

- Ultimo close disponibile: **2026-09-29** · SOL **117.73 $**.
- Giorno del vintage: **11/30**.
- P50 condizionato previsto per quel giorno: **106.27 $**.
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

- Cono congelato il **2026-08-30**; verificato fino al **2026-09-29**; stato **COMPLETO 30/30g**.
- Reale **117,73 $**; p50 previsto **112,31 $**; scarto **4,83%**.
- Errore medio assoluto **3,39%**; massimo **8,68%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted SOL](scanner_forecast_SOL_regime_adjusted.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-08-30**; verificato fino al **2026-09-29**; stato **COMPLETO 30/30g**.
- Reale **0.09329 $**; p50 previsto **0.08111 $**; scarto **15,02%**.
- Errore medio assoluto **7,34%**; massimo **19,20%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted DOGE](scanner_forecast_DOGE_regime_adjusted.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 74 | 93,24% | 67,57% | 2,00% | 0,45% |
| BTC | 3g | 70 | 92,86% | 74,29% | 3,37% | 0,58% |
| BTC | 7g | 62 | 91,94% | 67,74% | 5,05% | 2,06% |
| BTC | 14g | 52 | 98,08% | 71,15% | 5,63% | 2,36% |
| BTC | 30g | 23 | 100,00% | 91,30% | 8,90% | 3,16% |
| SOL | 1g | 74 | 82,43% | 62,16% | 2,74% | 0,93% |
| SOL | 3g | 70 | 91,43% | 72,86% | 4,01% | 1,73% |
| SOL | 7g | 62 | 90,32% | 70,97% | 5,82% | 3,95% |
| SOL | 14g | 52 | 86,54% | 75,00% | 7,90% | 6,99% |
| SOL | 30g | 23 | 91,30% | 47,83% | 15,48% | 14,92% |
| DOGE | 1g | 74 | 87,84% | 60,81% | 3,12% | 0,55% |
| DOGE | 3g | 70 | 91,43% | 62,86% | 4,82% | 1,41% |
| DOGE | 7g | 62 | 74,19% | 72,58% | 8,99% | 6,29% |
| DOGE | 14g | 52 | 84,62% | 48,08% | 11,03% | 9,41% |
| DOGE | 30g | 23 | 91,30% | 34,78% | 17,34% | 17,34% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
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

Generato: 2026-09-29 05:32 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +57,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +55,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +60,00%       | Nessun lato sopra soglia estrema |                  40 |

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
- Prezzo attuale: **83.242,65 $**
- Return normale fra 30 giorni: **81.312,25 $** (-2,32%)
- Drawdown normale durante il mese: **73.834,51 $** (-11,30%)
- Drawdown brutto da rispettare: **67.419,75 $** (-19,01%)
- Max gain normale durante il mese: **98.212,84 $** (17,98%)
- Max gain buono / take profit ottimistico: **114.752,00 $** (37,85%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **45,00%**
- Casi negativi / discesa storica: **55,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **117,81 $**
- Return normale fra 30 giorni: **115,55 $** (-1,92%)
- Drawdown normale durante il mese: **104,67 $** (-11,15%)
- Drawdown brutto da rispettare: **91,44 $** (-22,38%)
- Max gain normale durante il mese: **141,91 $** (20,46%)
- Max gain buono / take profit ottimistico: **154,20 $** (30,89%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **40,00%**
- Casi negativi / discesa storica: **60,00%**
- Quanto è netto il segnale: **debole**
- Prezzo attuale: **0,09 $**
- Return normale fra 30 giorni: **0,08 $** (-11,04%)
- Drawdown normale durante il mese: **0,08 $** (-18,79%)
- Drawdown brutto da rispettare: **0,07 $** (-26,94%)
- Max gain normale durante il mese: **0,10 $** (10,38%)
- Max gain buono / take profit ottimistico: **0,12 $** (30,02%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è misto. Alcuni asset possono avere lettura diversa, quindi è meglio valutare asset per asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 83.242,65 $

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

- Se va molto male: **69.097,84 $** (-16,99%)
- Se va male: **71.388,57 $** (-14,24%)
- Scenario normale: **81.312,25 $** (-2,32%)
- Se va bene: **96.761,66 $** (16,24%)
- Se va molto bene: **112.715,59 $** (35,41%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **73.834,51 $** (-11,30%)
- Discesa brutta: **67.419,75 $** (-19,01%)
- Discesa molto brutta: **59.196,53 $** (-28,89%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **98.212,84 $** (17,98%)
- Rialzo buono: **114.752,00 $** (37,85%)
- Rialzo molto forte: **141.776,05 $** (70,32%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **73.834,51 $** e uno spike normale intorno a **98.212,84 $**.

La chiusura a 30 giorni è incerta: salita 42,50%, discesa 57,50%. Non c'è un vantaggio netto.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 117,81 $

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

- Se va molto male: **91,89 $** (-22,00%)
- Se va male: **100,46 $** (-14,73%)
- Scenario normale: **115,55 $** (-1,92%)
- Se va bene: **135,81 $** (15,28%)
- Se va molto bene: **185,25 $** (57,24%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **104,67 $** (-11,15%)
- Discesa brutta: **91,44 $** (-22,38%)
- Discesa molto brutta: **83,43 $** (-29,18%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **141,91 $** (20,46%)
- Rialzo buono: **154,20 $** (30,89%)
- Rialzo molto forte: **219,44 $** (86,27%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **104,67 $** e uno spike normale intorno a **141,91 $**.

La chiusura a 30 giorni è incerta: salita 45,00%, discesa 55,00%. Non c'è un vantaggio netto.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 0,09 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **40,00%**
- Probabilità storica di discesa: **60,00%**
- Quanto è netto il segnale: **debole**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale debole. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,07 $** (-26,24%)
- Se va male: **0,08 $** (-15,61%)
- Scenario normale: **0,08 $** (-11,04%)
- Se va bene: **0,11 $** (12,71%)
- Se va molto bene: **0,15 $** (62,21%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,08 $** (-18,79%)
- Discesa brutta: **0,07 $** (-26,94%)
- Discesa molto brutta: **0,06 $** (-32,99%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,10 $** (10,38%)
- Rialzo buono: **0,12 $** (30,02%)
- Rialzo molto forte: **0,18 $** (95,58%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,08 $** e uno spike normale intorno a **0,10 $**.

La chiusura a 30 giorni era più spesso negativa: salita 40,00%, discesa 60,00%. Quindi la lettura principale è prudente/debole.

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

- Grezzo: **-2,32%** → **81.312,25 $**
- Correzione imparata dagli errori: **2,01%**
- Calibrato: **-0,31%** → **82.983,69 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-11,30%** → **73.834,51 $**
- Correzione imparata dagli errori: **4,72%**
- Calibrato: **-6,58%** → **77.766,33 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **17,98%** → **98.212,84 $**
- Correzione imparata dagli errori: **-2,82%**
- Calibrato: **15,16%** → **95.861,30 $**
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

- Grezzo: **-1,92%** → **115,55 $**
- Correzione imparata dagli errori: **8,80%**
- Calibrato: **6,88%** → **125,92 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-11,15%** → **104,67 $**
- Correzione imparata dagli errori: **2,99%**
- Calibrato: **-8,16%** → **108,20 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **20,46%** → **141,91 $**
- Correzione imparata dagli errori: **4,02%**
- Calibrato: **24,47%** → **146,64 $**
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

- Grezzo: **-11,04%** → **0,08 $**
- Correzione imparata dagli errori: **15,19%**
- Calibrato: **4,14%** → **0,10 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-18,79%** → **0,08 $**
- Correzione imparata dagli errori: **15,34%**
- Calibrato: **-3,46%** → **0,09 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **10,38%** → **0,10 $**
- Correzione imparata dagli errori: **2,52%**
- Calibrato: **12,90%** → **0,11 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 83.242,65 $

Bitcoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **42,50%**
- Casi negativi dopo 30 giorni: **57,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **87,20%**
- Rendimento medio dopo 30 giorni: **7,87%**
- Rendimento centrale dopo 30 giorni: **-2,32%**
- Discesa media durante i 30 giorni: **-13,56%**
- Massimo rialzo medio durante i 30 giorni: **31,87%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **89.789,89 $**
- Scenario centrale a 30 giorni: **81.312,25 $**
- Zona di rischio media: **71.957,68 $**
- Zona di rialzo media: **109.772,98 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -16,99% → **69.097,84 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -14,24% → **71.388,57 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -2,32% → **81.312,25 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 16,24% → **96.761,66 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 35,41% → **112.715,59 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -28,89% → **59.196,53 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -19,01% → **67.419,75 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -11,30% → **73.834,51 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,41% → **79.571,98 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -2,29% → **81.338,62 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **83.242,65 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 5,55% → **87.864,08 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 17,98% → **98.212,84 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 37,85% → **114.752,00 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 70,32% → **141.776,05 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| BTC-USD         | 2022-11-16   | 2023-02-23 |        92.24 |        14.81 |         -15.7  |          18.32 |
| RUNE-USD        | 2023-06-11   | 2023-09-18 |        90.33 |       -15.88 |         -17.79 |          12.36 |
| INJ-USD         | 2023-08-26   | 2023-12-03 |        89.09 |       112.1  |          -3.76 |         147.89 |
| QTUM-USD        | 2023-08-29   | 2023-12-06 |        88.89 |        -1.89 |          -4.69 |          16.2  |
| AAVE-USD        | 2022-11-15   | 2023-02-22 |        88.81 |       -14.09 |         -20.79 |           0.55 |
| ETH-USD         | 2022-11-12   | 2023-02-19 |        88.64 |         7.45 |         -15    |           7.45 |
| ATOM-USD        | 2023-09-03   | 2023-12-11 |        88.64 |         5.27 |          -4.59 |          22.25 |
| EGLD-USD        | 2023-09-03   | 2023-12-11 |        88.56 |       -11.15 |         -18.93 |          14.7  |
| THETA-USD       | 2023-09-02   | 2023-12-10 |        88.23 |       -10.94 |         -10.94 |          24.39 |
| XTZ-USD         | 2023-09-03   | 2023-12-11 |        87.96 |         7.98 |          -0.86 |          27.49 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 117,81 $

Solana è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **45,00%**
- Casi negativi dopo 30 giorni: **55,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,51%**
- Rendimento medio dopo 30 giorni: **8,82%**
- Rendimento centrale dopo 30 giorni: **-1,92%**
- Discesa media durante i 30 giorni: **-14,55%**
- Massimo rialzo medio durante i 30 giorni: **32,26%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **128,20 $**
- Scenario centrale a 30 giorni: **115,55 $**
- Zona di rischio media: **100,67 $**
- Zona di rialzo media: **155,82 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -22,00% → **91,89 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -14,73% → **100,46 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -1,92% → **115,55 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 15,28% → **135,81 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 57,24% → **185,25 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -29,18% → **83,43 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -22,38% → **91,44 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -11,15% → **104,67 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,39% → **112,64 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -2,07% → **115,37 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **117,81 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 2,74% → **121,04 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 20,46% → **141,91 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 30,89% → **154,20 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 86,27% → **219,44 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| CRV-USD         | 2022-11-16   | 2023-02-23 |        90.66 |       -15.24 |         -22.38 |           0    |
| RUNE-USD        | 2023-06-16   | 2023-09-23 |        89.81 |        25.2  |         -11.23 |          25.2  |
| ATOM-USD        | 2023-09-08   | 2023-12-16 |        88.54 |       -15.48 |         -21.95 |           0    |
| AAVE-USD        | 2022-11-15   | 2023-02-22 |        88.26 |       -14.09 |         -20.79 |           0.55 |
| MKR-USD         | 2018-12-19   | 2019-03-28 |        88.19 |       -28.88 |         -31.71 |           7.49 |
| EGLD-USD        | 2023-09-03   | 2023-12-11 |        87.8  |       -11.15 |         -18.93 |          14.7  |
| BTC-USD         | 2022-11-16   | 2023-02-23 |        87.8  |        14.81 |         -15.7  |          18.32 |
| HBAR-USD        | 2022-11-14   | 2023-02-21 |        87.74 |       -24.36 |         -30.38 |           0    |
| MKR-USD         | 2020-11-08   | 2021-02-15 |        87.52 |       -14.55 |         -20.8  |           6.42 |
| WAVES-USD       | 2023-09-03   | 2023-12-11 |        87.44 |        13.1  |          -1.28 |          33.18 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 0,09 $

Dogecoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **40,00%**
- Casi negativi dopo 30 giorni: **60,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **83,66%**
- Rendimento medio dopo 30 giorni: **5,68%**
- Rendimento centrale dopo 30 giorni: **-11,04%**
- Discesa media durante i 30 giorni: **-18,89%**
- Massimo rialzo medio durante i 30 giorni: **28,77%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,10 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,08 $**
- Zona di rialzo media: **0,12 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -26,24% → **0,07 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -15,61% → **0,08 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -11,04% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 12,71% → **0,11 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 62,21% → **0,15 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -32,99% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -26,94% → **0,07 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -18,79% → **0,08 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -5,12% → **0,09 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -2,77% → **0,09 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,09 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 0,99% → **0,09 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 10,38% → **0,10 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 30,02% → **0,12 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 95,58% → **0,18 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XTZ-USD         | 2019-09-09   | 2019-12-17 |        86.84 |        -3.06 |         -19.48 |           3.81 |
| ALGO-USD        | 2026-02-03   | 2026-05-13 |        86.21 |       -26.22 |         -26.45 |           7.81 |
| AAVE-USD        | 2022-11-15   | 2023-02-22 |        86.09 |       -14.09 |         -20.79 |           0.55 |
| NEAR-USD        | 2023-09-03   | 2023-12-11 |        85.93 |        60.35 |          -2.23 |          92.31 |
| ENJ-USD         | 2022-11-17   | 2023-02-24 |        85.34 |       -21.74 |         -29.05 |           0    |
| HBAR-USD        | 2023-09-05   | 2023-12-13 |        85.31 |         4.21 |          -2.11 |          26.25 |
| BTC-USD         | 2022-11-16   | 2023-02-23 |        84.83 |        14.81 |         -15.7  |          18.32 |
| SOL-USD         | 2022-11-15   | 2023-02-22 |        84.83 |       -14.48 |         -28.42 |           0    |
| EGLD-USD        | 2023-09-03   | 2023-12-11 |        84.71 |       -11.15 |         -18.93 |          14.7  |
| DOT-USD         | 2023-09-03   | 2023-12-11 |        84.68 |        18.85 |           0    |          37.6  |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report

Generated: 2026-09-29 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-29 | RECOVERY | 83.243 $ | True | 38.73% | -0.45% | RECOVERY | 38.73% | -0.45% |
| DOGE-USD | 2026-09-29 | RECOVERY | 0.09344 $ | True | 29.46% | -7.49% | RECOVERY | 38.73% | -0.45% |
| SOL-USD | 2026-09-29 | RECOVERY | 117,81 $ | True | 52.24% | -1.54% | RECOVERY | 38.73% | -0.45% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 42.50% | -2.32% | 16.24% | 35.41% | -11.30% | -28.89% | 17.98% | 37.85% | 70.32% | 50.00% | -0.66% | 31.68% | 99.55% |
| BTC-USD | SAME_BTC_REGIME | 8 | 62.50% | 4.11% | 8.40% | 15.79% | -4.56% | -13.41% | 23.13% | 28.15% | 32.49% | 37.50% | -3.78% | 5.94% | 22.22% |
| BTC-USD | SAME_ASSET_REGIME | 1 | 0.00% | -2.19% | -2.19% | -2.19% | -19.23% | -19.23% | 37.81% | 37.81% | 37.81% | 100.00% | 121.40% | 121.40% | 121.40% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 40.00% | -11.04% | 12.71% | 62.21% | -18.79% | -32.99% | 10.38% | 30.02% | 95.58% | 37.50% | -10.22% | 15.94% | 78.87% |
| DOGE-USD | SAME_BTC_REGIME | 8 | 75.00% | 5.46% | 13.93% | 31.30% | -3.13% | -12.90% | 25.75% | 37.93% | 54.92% | 37.50% | -1.77% | 10.16% | 23.35% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 100.00% | 4.21% | 4.21% | 4.21% | -2.11% | -2.11% | 26.25% | 26.25% | 26.25% | 100.00% | 1.91% | 1.91% | 1.91% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 45.00% | -1.92% | 15.28% | 57.24% | -11.15% | -29.18% | 20.46% | 30.89% | 86.27% | 42.50% | -1.51% | 20.88% | 78.69% |
| SOL-USD | SAME_BTC_REGIME | 11 | 72.73% | 7.98% | 12.69% | 30.13% | -3.44% | -18.93% | 27.49% | 36.04% | 69.12% | 36.36% | -0.79% | 9.89% | 29.88% |
| SOL-USD | SAME_ASSET_REGIME | 3 | 33.33% | -24.53% | -10.16% | -1.54% | -31.71% | -34.27% | 7.49% | 16.87% | 22.50% | 66.67% | 1.91% | 2.57% | 2.96% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 24 | 45.83% | -6.55% | -14.61% | 38.00% | 54.17% | 11.91% | 69.08% |
| BTC-USD | HISTORICAL_BTC_BULL | 7 | 14.29% | -2.45% | -17.79% | 28.27% | 57.14% | 37.07% | 222.65% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -13.14% | -16.41% | 45.99% | 0.00% | -6.40% | 45.99% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 8 | 62.50% | 4.11% | -4.56% | 28.15% | 37.50% | -3.78% | 34.65% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 26 | 23.08% | -14.86% | -22.63% | 19.44% | 26.92% | -15.57% | 25.78% |
| DOGE-USD | HISTORICAL_BTC_BULL | 6 | 66.67% | 18.61% | -6.05% | 110.03% | 83.33% | 30.01% | 130.35% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 8 | 75.00% | 5.46% | -3.13% | 37.93% | 37.50% | -1.77% | 37.93% |
| SOL-USD | HISTORICAL_BTC_BEAR | 20 | 30.00% | -9.34% | -18.92% | 24.86% | 35.00% | -9.34% | 26.51% |
| SOL-USD | HISTORICAL_BTC_BULL | 8 | 37.50% | -2.40% | -20.14% | 38.87% | 62.50% | 27.36% | 138.29% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 25.20% | -11.23% | 25.20% | 100.00% | 238.16% | 274.03% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 11 | 72.73% | 7.98% | -3.44% | 36.04% | 36.36% | -0.79% | 42.68% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 35 | 42.86% | -2.45% | -11.04% | 28.81% | 45.71% | -3.53% | 46.23% |
| BTC-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 78.89% | -5.22% | 136.47% | 66.67% | 93.83% | 303.30% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -14.55% | -20.80% | 6.42% | 100.00% | 37.07% | 52.86% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -2.19% | -19.23% | 37.81% | 100.00% | 121.40% | 202.07% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 33 | 30.30% | -13.98% | -20.79% | 24.01% | 27.27% | -12.86% | 33.54% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 5 | 100.00% | 78.89% | -4.62% | 132.08% | 80.00% | 22.96% | 147.89% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -14.55% | -20.80% | 6.42% | 100.00% | 37.07% | 52.86% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 4.21% | -2.11% | 26.25% | 100.00% | 1.91% | 26.25% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 33 | 45.45% | -1.74% | -11.08% | 33.18% | 39.39% | -2.76% | 46.46% |
| SOL-USD | HISTORICAL_ASSET_BULL | 1 | 100.00% | 8.88% | 0.00% | 69.12% | 0.00% | -0.21% | 69.12% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -14.55% | -20.80% | 11.55% | 66.67% | 17.65% | 49.32% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -24.53% | -31.71% | 16.87% | 66.67% | 1.91% | 16.87% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 0 | 1 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 1 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 0 | 3 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | ATOM-USD | 2023-09-03 | 88.64% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -4.59% | 22.25% | 1.61% | -9.12% | 22.25% |
| BTC-USD | EGLD-USD | 2023-09-03 | 88.56% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| BTC-USD | XTZ-USD | 2023-09-03 | 87.96% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.98% | -0.86% | 27.49% | 18.94% | -0.86% | 33.54% |
| BTC-USD | XRP-USD | 2023-09-03 | 87.49% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.26% | -11.04% | 4.21% | -15.19% | -18.87% | 4.21% |
| BTC-USD | EOS-USD | 2023-09-03 | 87.15% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| BTC-USD | ETC-USD | 2023-09-03 | 87.01% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 30.13% | -4.53% | 30.13% | 29.88% | -4.53% | 46.46% |
| BTC-USD | OMG-USD | 2023-09-03 | 86.10% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 9.65% | -2.45% | 37.98% | -4.03% | -10.47% | 37.98% |
| BTC-USD | KAVA-USD | 2023-09-03 | 85.37% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.95% | -2.83% | 24.01% | -4.58% | -11.86% | 24.01% |
| DOGE-USD | NEAR-USD | 2023-09-03 | 85.93% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 60.35% | -2.23% | 92.31% | 33.65% | -2.23% | 92.31% |
| DOGE-USD | EGLD-USD | 2023-09-03 | 84.71% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| DOGE-USD | DOT-USD | 2023-09-03 | 84.68% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 18.85% | 0.00% | 37.60% | 7.23% | -5.57% | 37.60% |
| DOGE-USD | KAVA-USD | 2023-09-03 | 84.50% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.95% | -2.83% | 24.01% | -4.58% | -11.86% | 24.01% |
| DOGE-USD | EOS-USD | 2023-09-03 | 83.95% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| DOGE-USD | XTZ-USD | 2023-09-03 | 83.30% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.98% | -0.86% | 27.49% | 18.94% | -0.86% | 33.54% |
| DOGE-USD | ADA-USD | 2023-09-03 | 82.67% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.84% | -10.32% | 20.73% | -1.86% | -15.34% | 20.73% |
| DOGE-USD | LRC-USD | 2023-09-03 | 82.18% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 12.28% | -3.44% | 38.90% | -1.68% | -7.92% | 38.90% |
| SOL-USD | ATOM-USD | 2023-09-08 | 88.54% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.48% | -21.95% | 0.00% | -15.03% | -25.65% | 0.00% |
| SOL-USD | EGLD-USD | 2023-09-03 | 87.80% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -11.15% | -18.93% | 14.70% | -12.91% | -23.48% | 14.70% |
| SOL-USD | WAVES-USD | 2023-09-03 | 87.44% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 13.10% | -1.28% | 33.18% | -0.79% | -8.93% | 33.18% |
| SOL-USD | EOS-USD | 2023-09-03 | 86.31% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -2.10% | -8.74% | 17.65% | -3.53% | -11.96% | 17.65% |
| SOL-USD | NEAR-USD | 2023-09-03 | 86.29% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 60.35% | -2.23% | 92.31% | 33.65% | -2.23% | 92.31% |
| SOL-USD | NEO-USD | 2023-09-03 | 86.21% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 4.75% | -3.97% | 23.99% | 0.84% | -11.34% | 23.99% |
| SOL-USD | ETC-USD | 2023-09-03 | 85.91% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 30.13% | -4.53% | 30.13% | 29.88% | -4.53% | 46.46% |
| SOL-USD | LRC-USD | 2023-09-03 | 85.67% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 12.28% | -3.44% | 38.90% | -1.68% | -7.92% | 38.90% |
| SOL-USD | KAVA-USD | 2023-09-03 | 85.52% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 2.95% | -2.83% | 24.01% | -4.58% | -11.86% | 24.01% |
| SOL-USD | XTZ-USD | 2023-09-03 | 85.39% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 7.98% | -0.86% | 27.49% | 18.94% | -0.86% | 33.54% |

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

Generato: 2026-09-29 05:32 UTC

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
| BTC | 83.243 $ | +3 | ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO | STAGE 3 / DISTRIBUZIONE O PAUSA | VOLATILITÀ IN ESPANSIONE | SIGN OF STRENGTH POSSIBILE | MEDIO | HOLD / ASPETTA ROTTURA RESISTENZA |
| SOL | 117,81 $ | +8 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | VOLATILITÀ IN ESPANSIONE | SIGN OF STRENGTH POSSIBILE | MEDIO | TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME |
| DOGE | 0.09344 $ | +3 | ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO | STAGE 3 / DISTRIBUZIONE O PAUSA | VOLATILITÀ IN ESPANSIONE | RANGE / FASE NON CHIARA | MEDIO | STAI ALLA FINESTRA |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | 0 | 0 | -1 | 0 | 0 | +2 | +3 |
| SOL | +3 | 0 | +1 | +2 | 0 | 0 | +2 | +8 |
| DOGE | +1 | 0 | +1 | +1 | 0 | 0 | 0 | +3 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.206 $ | 87.364 $ | 87.364 $ | 62.227 $ | 2,80% | 6,26% | 41,99% |
| SOL | 98,63 $ | 119,81 $ | 122,75 $ | 70,69 $ | 4,58% | 11,36% | 60,02% |
| DOGE | 0.08189 $ | 0.09421 $ | 0.10528 $ | 0.06797 $ | 6,21% | 9,30% | 29,47% |

## Lettura dettagliata

### BTC

- Prezzo: **83.243 $**
- Score classico: **+3 / 12**
- Verdetto: **ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO**
- Azione coerente: **HOLD / ASPETTA ROTTURA RESISTENZA**
- Volatilità tecnica locale: **MEDIO** — ATR14 2,80%; distanza supporto 4,98%; distanza resistenza 5,07%

Dettaglio:

- Trend: **+2** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **0** — RSI sano 59.5; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale 0.04; volume ratio 1.26
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 59.50 |
| MACD histogram | 51.29889 |
| CMF20 | 0.037 |
| Volume ratio 20 | 1.26 |
| MA20 | 80.665 $ |
| MA50 | 76.471 $ |
| MA100 | 69.894 $ |
| MA200 | 71.136 $ |
| Pendenza MA50 20g | +9,31% |
| Pendenza MA200 60g | -0,64% |
| Bollinger width | 18,17% |
| Bollinger position | 0.66 |

### SOL

- Prezzo: **117,81 $**
- Score classico: **+8 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME**
- Volatilità tecnica locale: **MEDIO** — ATR14 4,58%; distanza supporto 19,29%; distanza resistenza 1,83%

Dettaglio:

- Trend: **+3** — prezzo sopra MA200 daily; medie daily allineate rialziste; MA50 daily in salita; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **+1** — RSI sano 61.5; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.22; volume ratio 0.96
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 61.54 |
| MACD histogram | 0.63043 |
| CMF20 | 0.220 |
| Volume ratio 20 | 0.96 |
| MA20 | 109,52 $ |
| MA50 | 99,46 $ |
| MA100 | 87,38 $ |
| MA200 | 85,11 $ |
| Pendenza MA50 20g | +16,39% |
| Pendenza MA200 60g | -1,92% |
| Bollinger width | 30,94% |
| Bollinger position | 0.72 |

### DOGE

- Prezzo: **0.09344 $**
- Score classico: **+3 / 12**
- Verdetto: **ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO**
- Azione coerente: **STAI ALLA FINESTRA**
- Volatilità tecnica locale: **MEDIO** — ATR14 6,21%; distanza supporto 13,82%; distanza resistenza 1,07%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **+1** — RSI sano 54.9; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+1** — OBV sopra media; CMF neutrale 0.00; volume ratio 1.03
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 54.91 |
| MACD histogram | 0.00048 |
| CMF20 | 0.004 |
| Volume ratio 20 | 1.03 |
| MA20 | 0.08919 $ |
| MA50 | 0.08464 $ |
| MA100 | 0.07881 $ |
| MA200 | 0.08789 $ |
| Pendenza MA50 20g | +9,71% |
| Pendenza MA200 60g | -7,81% |
| Bollinger width | 29,61% |
| Bollinger position | 0.65 |

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

Generato: 2026-09-29 05:32 UTC

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
| BTC | 83.243 $ | Doppio minimo | CONFERMATO RECENTE | rialzista | 2026-09-21 | 89.580 $ | 13,40% | n/a | Fib 23,6% NON ATTIVO (0) @ 80.374 $ | NEL RANGE | 76.248 $ |
| SOL | 117,81 $ | Triplo massimo | CANDIDATO | ribassista | n/a | 62,51 $ | n/a | 66,65% | Fib 78,6% RECUPERATO (+1) @ 107,08 $ | NEL RANGE | 97,45 $ |
| DOGE | 0.09344 $ | Doppio minimo | CONFERMATO RECENTE | rialzista | 2026-09-21 | 0.11001 $ | -4,87% | n/a | Fib 38,2% TENUTO (+1) @ 0.09103 $ | NEL RANGE | 0.09274 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CONFERMATO RECENTE** (+2)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-09-15**
- Età formazione: **14 giorni**
- Breakout pattern: **2026-09-21**
- Età breakout: **8 giorni**
- Neckline: **82.262 $**
- Target teorico: **89.580 $**
- Progresso verso target: **13,40%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 80.374 $** — Swing UP 2026-07-01 57.748 -> 2026-09-21 87.364; livello più vicino 23.6% a 80.374; stato NON ATTIVO; confluenza: invalidazione rialzista.
- Invalidazione: **80.617 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due minimi simili vicino a 74.945 tra 2026-09-02 e 2026-09-15. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (8 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 89.580; progresso corrente: 13,40%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **76.248 $**
- Resistenza: **87.364 $**
- Breakout 60g: **87.364 $**
- Breakdown 60g: **62.227 $**
- RSI14: **59.88**
- ATR14: **2,80%**
- Volume ratio 20g: **1.26**
- Rendimento 30g: **+6,39%**
- Rendimento 90g: **+42,15%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CONFERMATO RECENTE | +2 | rialzista | 82.262 $ | 2026-09-21 | 8g | 89.580 $ | 13,40% | n/a | 80.617 $ | Due minimi simili a 76.248 $ e 74.945 $. Neckline circa 82.262 $. Breakout neckline: 2026-09-21 (8 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 89.580 $; progresso: 13,40%; prezzo sopra neckline. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 33,77% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 51 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **51 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **70,69 $**
- Target teorico: **62,51 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **66,65%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% RECUPERATO (+1) @ 107,08 $** — Swing DOWN 2026-08-27 110,04 -> 2026-09-16 96,23; livello più vicino 78.6% a 107,08; stato RECUPERATO; confluenza: resistenza tecnica, neckline rialzista, invalidazione rialzista.
- Invalidazione: **72,11 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 51 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **97,45 $**
- Resistenza: **124,62 $**
- Breakout 60g: **122,75 $**
- Breakdown 60g: **70,69 $**
- RSI14: **61.79**
- ATR14: **4,57%**
- Volume ratio 20g: **0.96**
- Rendimento 30g: **+11,51%**
- Rendimento 90g: **+60,23%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,51 $ | n/a | 66,65% | 72,11 $ | Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 51 giorni. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 66,65% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 51 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 107,12 $ | 2026-09-18 | 11g | 118,01 $ | 98,19% | n/a | 104,97 $ | Due minimi simili a 97,45 $ e 96,23 $. Neckline circa 107,12 $. Breakout neckline: 2026-09-18 (11 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01 $; progresso: 98,19%; prezzo sopra neckline. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 41g | 85,65 $ | 530,12% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (41 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 530,12%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CONFERMATO RECENTE** (+2)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-09-16**
- Età formazione: **13 giorni**
- Breakout pattern: **2026-09-21**
- Età breakout: **8 giorni**
- Neckline: **0.09421 $**
- Target teorico: **0.11001 $**
- Progresso verso target: **-4,87%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 38,2% TENUTO (+1) @ 0.09103 $** — Swing UP 2026-08-01 0.06797 -> 2026-09-22 0.10528; livello più vicino 38.2% a 0.09103; stato TENUTO; confluenza: neckline rialzista, invalidazione rialzista.
- Invalidazione: **0.09232 $**
- Relazione prezzo/neckline: **vicino alla neckline**
- Dettaglio: Due minimi simili vicino a 0.07841 tra 2026-09-02 e 2026-09-16. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (8 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 0.11001; progresso corrente: -4,87%. Relazione prezzo/neckline: vicino alla neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.09274 $**
- Resistenza: **0.09421 $**
- Breakout 60g: **0.10528 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **55.23**
- ATR14: **6,20%**
- Volume ratio 20g: **1.03**
- Rendimento 30g: **+9,57%**
- Rendimento 90g: **+29,79%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CONFERMATO RECENTE | +2 | rialzista | 0.09421 $ | 2026-09-21 | 8g | 0.11001 $ | -4,87% | n/a | 0.09232 $ | Due minimi simili a 0.08028 $ e 0.07841 $. Neckline circa 0.09421 $. Breakout neckline: 2026-09-21 (8 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 0.11001 $; progresso: -4,87%; prezzo vicino alla neckline. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.07841 $ | n/a | n/a | 0.05153 $ | n/a | 19,18% | 0.07997 $ | Due massimi simili a 0.09998 $ e 0.10528 $. Neckline circa 0.07841 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 7 giorni. |

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

Generato: 2026-09-29 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-29**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-16**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **117,81 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+70,73%**
- Aderenza live principale: **+67,72%**
- Errore medio live principale: **16,14%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **115**
- Osservazioni inclusive dal bottom: **116**
- Osservazioni da inizio programma/scanner: **89**
- Errore assoluto medio dal bottom: **13,78%**
- Errore assoluto medio da inizio programma: **16,14%**
- Gap firmato medio ultimi 7 giorni: **+32,48%**
- Errore assoluto medio ultimi 7 giorni: **32,48%**
- Gap ultimo giorno: **+19,38%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+19,38%**
- Gap firmato medio 7g: **+32,48%**
- Errore assoluto medio 7g: **32,48%**
- Variazione recente gap: **-8,01%**
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
| 106 | 2026-09-20 | 2023-03-07 | 111,13 $ | 87,53 $ | +26,97% | da inizio programma |
| 107 | 2026-09-21 | 2023-03-08 | 118,75 $ | 85,55 $ | +38,80% | da inizio programma |
| 108 | 2026-09-22 | 2023-03-09 | 118,51 $ | 80,21 $ | +47,74% | da inizio programma |
| 109 | 2026-09-23 | 2023-03-10 | 114,98 $ | 79,52 $ | +44,58% | da inizio programma |
| 110 | 2026-09-24 | 2023-03-11 | 117,01 $ | 81,28 $ | +43,97% | da inizio programma |
| 111 | 2026-09-25 | 2023-03-12 | 122,01 $ | 87,31 $ | +39,74% | da inizio programma |
| 112 | 2026-09-26 | 2023-03-13 | 121,43 $ | 95,32 $ | +27,39% | da inizio programma |
| 113 | 2026-09-27 | 2023-03-14 | 122,06 $ | 97,48 $ | +25,21% | da inizio programma |
| 114 | 2026-09-28 | 2023-03-15 | 122,06 $ | 96,02 $ | +27,11% | da inizio programma |
| 115 | 2026-09-29 | 2023-03-16 | 117,81 $ | 98,69 $ | +19,38% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-06 | 111,61 $ | 133,24 $ | 117,81 $ / 133,24 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-13 | 110,43 $ | 131,83 $ | 117,81 $ / 133,31 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-20 | 110,47 $ | 131,88 $ | 117,81 $ / 133,92 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-27 | 119,75 $ | 142,95 $ | 117,81 $ / 142,95 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-03 | 111,27 $ | 132,83 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-10 | 116,10 $ | 138,60 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-17 | 113,64 $ | 135,66 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-24 | 106,36 $ | 126,97 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-01 | 105,70 $ | 126,18 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-08 | 104,30 $ | 124,50 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-15 | 105,65 $ | 126,12 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-22 | 104,42 $ | 124,65 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-29 | 100,75 $ | 120,27 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-05 | 117,83 $ | 140,66 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-12 | 119,93 $ | 143,17 $ | 117,81 $ / 144,34 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-19 | 117,82 $ | 140,65 $ | 117,81 $ / 146,51 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-26 | 123,99 $ | 148,02 $ | 117,81 $ / 148,02 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-02 | 117,36 $ | 140,10 $ | 117,81 $ / 148,02 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 71 | 36,62% | 11,46% | 14,99% |
| 14g | 68 | 22,06% | 17,56% | 15,29% |
| 21g | 61 | 21,31% | 23,53% | 16,81% |
| 28g | 54 | 20,37% | 25,01% | 17,09% |
| 35g | 47 | 27,66% | 26,42% | 17,04% |
| 42g | 40 | 50,00% | 24,19% | 15,89% |
| 49g | 35 | 57,14% | 23,67% | 18,54% |
| 56g | 28 | 57,14% | 19,91% | 20,21% |
| 63g | 21 | 52,38% | 13,25% | 24,48% |
| 70g | 14 | 42,86% | 12,51% | 32,83% |
| 77g | 7 | 0,00% | 13,26% | 27,77% |
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

Generato: 2026-09-29 05:32 UTC

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 83.171 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0081% | +3,24% | 1,99 | -0,62% | 0 $ | 0 $ |
| SOL | 117,58 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0084% | -3,41% | 1,54 | -5,65% | 0 $ | 0 $ |
| DOGE | 0.09305 $ | 3 | 0 | 0 | LEGGERMENTE NEGATIVA / NON PESATA | BASSA | 100% | +0,0083% | -1,10% | 0,67 | -27,14% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0044% | 179,00 mln $ | 0,12 | +0,71% |
| BTC | Bitget | OK | +0,0100% | 2,67 mld $ | 0,60 | -0,65% |
| BTC | Kucoin | OK | +0,0040% | 980,73 mln $ | 0,62 | +0,29% |
| SOL | Kraken | OK | +0,0162% | 30,03 mln $ | 20,10 | +10,60% |
| SOL | Bitget | OK | +0,0100% | 499,22 mln $ | 0,56 | +15,50% |
| SOL | Kucoin | OK | +0,0012% | 135,17 mln $ | 0,95 | -11,64% |
| DOGE | Kraken | OK | +0,0199% | 4,75 mln $ | 0,87 | -28,23% |
| DOGE | Bitget | OK | +0,0100% | 121,46 mln $ | 0,19 | -33,91% |
| DOGE | Kucoin | OK | +0,0080% | 58,63 mln $ | 0,91 | -22,38% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+1,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 6, accuratezza +33,33%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 0.
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

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci recuperato con acquisti/assorbimento coerenti: conferma positiva. Confluenza tecnica dichiarata: resistenza tecnica, neckline rialzista, invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **-1,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 11, accuratezza +45,45%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 3, divergenze 0.
- Flusso taker/order book: **-1,25**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci tenuto; nessuna conferma exchange netta. Confluenza tecnica dichiarata: neckline rialzista, invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +42,50% | -2,32% | 3 | +66,67% | RACCOLTA DATI | 0,00 | +42,50% | -2,32% |
| SOL | +45,00% | -1,92% | 5 | +100,00% | RACCOLTA DATI | 0,00 | +45,00% | -1,92% |
| DOGE | +40,00% | -11,04% | 8 | +75,00% | RACCOLTA DATI | 0,00 | +40,00% | -11,04% |

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

Generato: 2026-09-29 05:32 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-29 | BTC | 83.170,54 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,99 | +3,24% | -0,62% |
| 2026-09-29 | DOGE | 0.09305 | V2.1.3 | OK | 0 | 0 | -1,25 | BASSA | 0,67 | -1,10% | -27,14% |
| 2026-09-29 | SOL | 117,58 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,54 | -3,41% | -5,65% |
| 2026-09-28 | BTC | 83.362,82 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 9,06 | -0,85% | -5,33% |
| 2026-09-28 | DOGE | 0.09429 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,83 | +0,71% | -11,45% |
| 2026-09-28 | SOL | 119,70 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,45 | +4,77% | -6,25% |
| 2026-09-27 | BTC | 84.359,90 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,80 | -0,08% | -0,77% |
| 2026-09-27 | DOGE | 0.09583 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,22 | -2,15% | -11,70% |
| 2026-09-27 | SOL | 120,44 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,99 | +0,57% | -5,38% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 8 | +37,50% | -0,37% | -1,23% | +0,83% | FEEDBACK RAPIDO |
| BTC | 3g | 8 | +37,50% | -0,46% | -2,47% | +1,78% | FEEDBACK RAPIDO |
| BTC | 7g | 6 | +33,33% | -1,53% | -3,35% | +2,42% | FEEDBACK RAPIDO |
| BTC | 14g | 5 | +40,00% | +0,20% | -4,71% | +3,32% | FEEDBACK RAPIDO |
| BTC | 30g | 3 | +66,67% | +5,24% | -4,15% | +8,48% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 5 | +100,00% | +22,07% | -4,32% | +25,38% | FEEDBACK RAPIDO |
| DOGE | 1g | 11 | +54,55% | +1,55% | -0,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 3g | 11 | +36,36% | +1,63% | -3,44% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 7g | 11 | +45,45% | -0,13% | -4,83% | +9,23% | FEEDBACK RAPIDO |
| DOGE | 14g | 9 | +33,33% | +0,11% | -6,27% | +13,00% | FEEDBACK RAPIDO |
| DOGE | 30g | 8 | +75,00% | +12,16% | -6,15% | +30,59% | FEEDBACK RAPIDO |

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
| BTC | 83.243 $ | +0.0043% | -7.69% | 1.18 | Misto | 1/5 |
| SOL | 117,81 $ | +0.0036% | -4.28% | 1.67 | Misto | 1/5 |
| DOGE | 0.09344 $ | +0.0100% | -8.22% | 3.94 | Rischio sotto | 2/5 |

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

Generato: 2026-09-29 05:32 UTC

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                      | Stato D   | Weekly             | Stato W    | Lettura weekly                                                                                                              |   Peso |
|:--------|:---------------------------|:----------|:-------------------|:-----------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Misto / nessuna divergenza | CONTESTO  | Conferma rialzista | CONTESTO   | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| SOL     | Conferma rialzista         | CONTESTO  | Conferma rialzista | CONTESTO   | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| DOGE    | Conferma rialzista         | CONTESTO  | Hidden bearish     | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                       | Stato      | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:---------------------------|:-----------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Misto / nessuna divergenza | CONTESTO   | 83.167 $ / 59,58  | n/a                                                                 | +6,40%              | 1,78             |      0 |
| BTC     | 1W   | Conferma rialzista         | CONTESTO   | 83.167 $ / 59,81  | n/a                                                                 | +6,96%              | 3,17             |      0 |
| SOL     | 1D   | Conferma rialzista         | CONTESTO   | 117,69 $ / 61,60  | n/a                                                                 | +14,83%             | 4,11             |      0 |
| SOL     | 1W   | Conferma rialzista         | CONTESTO   | 117,69 $ / 62,40  | n/a                                                                 | +23,31%             | 7,87             |      0 |
| DOGE    | 1D   | Conferma rialzista         | CONTESTO   | 0.09330 $ / 55,04 | n/a                                                                 | +11,56%             | 5,15             |      0 |
| DOGE    | 1W   | Hidden bearish             | CONFERMATA | 0.09330 $ / 50,57 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 49,72 | n/a                 | n/a              |      0 |

### BTC

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
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
| DOGE    | 1D   | Hidden bearish   |          60 |           2 | 0,00%         | -25,06%           | RACCOLTA DATI |      0 |
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

Generato: 2026-09-29 05:32 UTC

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

| Asset   | Prezzo   |   Punteggio | Verdetto                      | Trend           | Momentum       | Struttura                                             |   Pattern score | Fibonacci       | Pattern rialzista                  | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:------------------------------|:----------------|:---------------|:------------------------------------------------------|----------------:|:----------------|:-----------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 83.243 $ | 6 | COSTRUTTIVO MA NON CONFERMATO | Trend rialzista | Momentum misto | Volatilità in espansione | +2 | 0 / NON ATTIVO | Doppio minimo / CONFERMATO RECENTE | Doppio massimo / CANDIDATO | 74.945 | 87.364 |
| SOL | 117,81 $ | 6 | COSTRUTTIVO MA NON CONFERMATO | Trend rialzista | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | 0 | +1 / RECUPERATO | Doppio minimo / TARGET RAGGIUNTO | Triplo massimo / CANDIDATO | 96,23 | 107,12 |
| DOGE | 0.09344 $ | 9 | RIALZISTA TECNICO | Trend rialzista | Momentum misto | Volatilità in espansione | +2 | +1 / TENUTO | Doppio minimo / CONFERMATO RECENTE | Doppio massimo / CANDIDATO | 0.07841 | 0.10528 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo      | Triplo minimo    | Adam/Eve Bottom                          | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-------------------|:-----------------|:-----------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CONFERMATO RECENTE | TARGET RAGGIUNTO | Eve and Adam Bottom — CONFERMATO RECENTE | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 2 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | INVALIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | CONFERMATO RECENTE | TARGET RAGGIUNTO | Adam and Eve Bottom — CONFERMATO RECENTE | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 2 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 59.88 | 57.4533 | 80.670 | 76.473 | 71.136 | 8,95% | -0,45% | 7,18% | 38,73% |
| SOL | 61.79 | 0.64064 | 109,53 | 99,46 | 85,11 | 15,75% | -1,54% | 15,64% | 52,24% |
| DOGE | 55.23 | 0.00049 | 0.08920 | 0.08464 | 0.08789 | 9,35% | -7,49% | 13,82% | 29,46% |

## Dettaglio asset

### BTC

- Prezzo: **83.243 $**
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
  - Due minimi simili vicino a 74.945 tra 2026-09-02 e 2026-09-15. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (8 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 89.580; progresso corrente: 13,40%. Relazione prezzo/neckline: sopra neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (8g); progresso 13,40%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (41 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 346,84%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (41g); progresso 346,84%; prezzo sopra neckline.
- Eve and Adam Bottom: **CONFERMATO RECENTE** (+2)
  - Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (8 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 89.580; progresso corrente: 13,40%. Relazione prezzo/neckline: sopra neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (8g); progresso 13,40%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 87.364 tra 2026-09-03 e 2026-09-21. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 74.945; target 62.525; distanza dalla neckline 11,07%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 51 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 44,15%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 87.364 dal 2026-09-03 al 2026-09-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 74.945; target 62.525; distanza dalla neckline 11,07%; prezzo sopra neckline.

### SOL

- Prezzo: **117,81 $**
- Punteggio tecnico: **6 / 12**
- Verdetto: **COSTRUTTIVO MA NON CONFERMATO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum misto** (0)
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
  - Due minimi simili vicino a 96,23 tra 2026-09-02 e 2026-09-16. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (11 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: 98,19%. Relazione prezzo/neckline: sopra neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (11g); progresso 98,19%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (41 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 486,62%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (41g); progresso 486,62%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 96,23 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (11 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: 98,19%. Relazione prezzo/neckline: sopra neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (11g); progresso 98,19%; prezzo sopra neckline.
- Doppio massimo: **INVALIDATO** (0)
  - Due massimi simili vicino a 110,04 tra 2026-08-27 e 2026-09-06. Neckline ribassista stimata: 97,45. Breakout neckline: 2026-09-15 (14 giorni fa). Stato: INVALIDATO. Target teorico: 84,86; progresso corrente: -161,73%. Relazione prezzo/neckline: sopra neckline.
  - neckline 97,45; target 84,86; breakout 2026-09-15 (14g); progresso -161,73%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 51 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 66,65%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 83,81 dal 2026-07-04 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 51 giorni.
  - neckline 70,69; target 57,58; distanza dalla neckline 66,65%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.09344 $**
- Punteggio tecnico: **9 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum misto** (0)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 0.08028 -> 0.07841. Ultimi massimi: 0.09421 -> 0.1053.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TENUTO** (+1)
  - Swing UP 2026-08-01 0.06797 -> 2026-09-22 0.10528; livello più vicino 38.2% a 0.09103; stato TENUTO; confluenza: neckline rialzista, invalidazione rialzista.
- Punteggio pattern: **+2**
  - rialzista dominante: Doppio minimo (CONFERMATO RECENTE, +2); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.07841**
- Resistenza più vicina: **0.10528**

Pattern classici e ciclo di vita:

- Doppio minimo: **CONFERMATO RECENTE** (+2)
  - Due minimi simili vicino a 0.07841 tra 2026-09-02 e 2026-09-16. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (8 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 0.11001; progresso corrente: -4,87%. Relazione prezzo/neckline: vicino alla neckline.
  - neckline 0.09421; target 0.11001; breakout 2026-09-21 (8g); progresso -4,87%; prezzo vicino alla neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06835 dal 2026-07-13 al 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (41 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07926; progresso corrente: 359,96%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07926; breakout 2026-08-19 (41g); progresso 359,96%; prezzo sopra neckline.
- Adam and Eve Bottom: **CONFERMATO RECENTE** (+2)
  - Pattern Adam and Eve Bottom vicino a 0.07841 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (8 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 0.11001; progresso corrente: -4,87%. Relazione prezzo/neckline: vicino alla neckline.
  - neckline 0.09421; target 0.11001; breakout 2026-09-21 (8g); progresso -4,87%; prezzo vicino alla neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.10528 tra 2026-08-22 e 2026-09-22. Neckline ribassista stimata: 0.07841. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 0.07841; target 0.05153; distanza dalla neckline 19,18%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 49 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 37,47%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07380 dal 2026-07-26 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 49 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 37,47%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                                                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:----------------------------------------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-09-21 | 80.374 | 76.050 | 72.556 | 69.061 | 64.086 | 23.6% / 80.374 | NON ATTIVO | invalidazione rialzista | 0 |
| SOL | DOWN 2026-08-27 -> 2026-09-16 | 99,49 | 101,50 | 103,13 | 104,76 | 107,08 | 78.6% / 107,08 | RECUPERATO | resistenza tecnica, neckline rialzista, invalidazione rialzista | +1 |
| DOGE | UP 2026-08-01 -> 2026-09-22 | 0.09648 | 0.09103 | 0.08663 | 0.08222 | 0.07596 | 38.2% / 0.09103 | TENUTO | neckline rialzista, invalidazione rialzista | +1 |

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

- **BTC**: 30/30 previsioni controllate su 83 fatte. Stato: **ATTIVA**.
- **SOL**: 30/30 previsioni controllate su 83 fatte. Stato: **ATTIVA**.
- **DOGE**: 30/30 previsioni controllate su 83 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 83 | 30 | 30/30 [██████████] | 53 | ATTIVA | 2026-09-30 / tra 1 giorno |
| SOL | 83 | 30 | 30/30 [██████████] | 53 | ATTIVA | 2026-09-30 / tra 1 giorno |
| DOGE | 83 | 30 | 30/30 [██████████] | 53 | ATTIVA | 2026-09-30 / tra 1 giorno |

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

Generato: 2026-09-29 05:33 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 1 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 83.243 $          | 83.243 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.09344 $         | 0.09344 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 117,81 $          | 117,81 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 83.243 $          | 83.243 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 117,81 $          | 117,81 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.09344 $         | 0.09344 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 83.243 $          | 83.243 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 117,81 $          | 117,81 $        | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.09344 $         | 0.09344 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 83.243 $          | 83.243 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 117,81 $          | 117,81 $        | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.09344 $         | 0.09344 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 83.243 $          | 83.243 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 117,81 $          | 117,81 $        | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.09344 $         | 0.09344 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 83.243 $          | 83.171 $        | -0,0866%     |
| Exchange Microstructure | SOL     | price             | OK      | 117,81 $          | 117,58 $        | -0,1910%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.09344 $         | 0.09305 $       | -0,4134%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 117,81 $          | 117,81 $        | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 117,81 $          | 117,81 $        | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 117,81 $          | 117,81 $        | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 117,81 $          | 117,81 $        | +0,0000%     |

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
