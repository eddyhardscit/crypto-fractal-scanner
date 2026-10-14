<!-- LAB_REDUCTION_START -->
# Laboratorio ridotto — 13 ottobre 2026

**Solo diagnostica: nessuna affidabilità operativa certificata.**

Calibrazione rischio in quarantena; frattale BTC→SOL, tracking frattale, RSI top-cycle, on-chain SOL e percorsi estremi sospesi. Storici conservati.

Coni BTC/SOL/DOGE e valutazioni continuano; priorità di analisi SOL a 7 giorni. Nessun nuovo sviluppo BTC/DOGE a 30 giorni.

Top50: verifica separata sulle previsioni dal 14 ottobre, confronto con prezzo invariato a 7 giorni. Revisione entro il 13 novembre 2026: almeno 3 settimane complete con 30 asset ciascuna, riduzione errore almeno 5% e vantaggio in almeno 2 settimane. Criterio esplorativo, nessuna promozione automatica; se manca, proposta di sospensione dell'espansione.

Stato verifica: **COLLECTING_FIXED_VALIDATION**.
<!-- LAB_REDUCTION_END -->

<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-10-14 05:33 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 0 | NEUTRALE / COSTRUTTIVO | HOLD / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | +2 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +2 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **0**, spot = **HOLD / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **+2**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
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
- Conferme: Prima resistenza sopra 87.146; conferma del eve and adam bottom sopra 82.262.
- Invalidazioni: Sotto 80.337 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+2**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **HOLD LEGGERO / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 123,48.
- Invalidazioni: Allarmi sotto 96,23.

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
- Invalidazioni: Sotto 0.08122 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 2; EMA200 circa 111,38 $; upside verso EMA200 +3,87%. Non autorizza leva e non aggiunge punti automatici.
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

Generato: 2026-10-14 05:33 UTC

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

Segnali totali salvati: **270**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-14 | BTC | 83.488,21 | 0 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-14 | DOGE | 0.08470 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-10-14 | SOL | 107,30 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-13 | BTC | 83.581,21 | +1 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-13 | DOGE | 0.08464 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-13 | SOL | 108,05 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-12 | BTC | 83.714,71 | -3 | -1 | -1 | 0 | -1 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-12 | DOGE | 0.08732 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-12 | SOL | 112,31 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-11 | BTC | 83.006,99 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-11 | DOGE | 0.08535 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-11 | SOL | 109,56 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 90 | 89 | 88 | 87 | 85 | 83 | 80 | 77 | 71 | 66 | 51 | 36 |
| SOL | 90 | 89 | 88 | 87 | 85 | 83 | 80 | 77 | 71 | 66 | 51 | 36 |
| DOGE | 90 | 89 | 88 | 87 | 85 | 83 | 80 | 77 | 71 | 66 | 51 | 36 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-16 | 60g | 2026-10-15 | domani |
| SOL | 2026-08-16 | 60g | 2026-10-15 | domani |
| DOGE | 2026-08-16 | 60g | 2026-10-15 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 80 | 52,50% | +0,30% | +0,29% | UTILE |
| BTC | 2g | 79 | 51,90% | +0,55% | +0,50% | UTILE |
| BTC | 3g | 78 | 46,15% | +0,69% | +0,60% | UTILE |
| BTC | 5g | 78 | 43,59% | +1,42% | +1,25% | UTILE |
| BTC | 7g | 77 | 51,95% | +2,13% | +1,99% | UTILE |
| BTC | 10g | 75 | 57,33% | +3,09% | +2,97% | UTILE |
| BTC | 14g | 72 | 62,50% | +4,67% | +4,62% | UTILE |
| BTC | 21g | 68 | 72,06% | +8,08% | +7,98% | UTILE |
| BTC | 30g | 63 | 95,24% | +12,23% | +11,55% | UTILE |
| BTC | 45g | 48 | 93,75% | +21,34% | +18,59% | PRIMA CALIBRAZIONE |
| BTC | 60g | 34 | 91,18% | +28,15% | +23,74% | PRIMA CALIBRAZIONE |
| SOL | 1g | 81 | 46,91% | +0,19% | +0,12% | UTILE |
| SOL | 2g | 80 | 45,00% | +0,66% | +0,57% | UTILE |
| SOL | 3g | 79 | 49,37% | +1,17% | +1,06% | UTILE |
| SOL | 5g | 77 | 51,95% | +2,10% | +2,03% | UTILE |
| SOL | 7g | 75 | 57,33% | +3,21% | +3,28% | UTILE |
| SOL | 10g | 72 | 59,72% | +5,15% | +5,26% | UTILE |
| SOL | 14g | 69 | 68,12% | +7,89% | +8,41% | UTILE |
| SOL | 21g | 63 | 80,95% | +14,49% | +13,93% | UTILE |
| SOL | 30g | 59 | 83,05% | +19,95% | +16,60% | PRIMA CALIBRAZIONE |
| SOL | 45g | 44 | 75,00% | +36,59% | +19,09% | PRIMA CALIBRAZIONE |
| SOL | 60g | 29 | 62,07% | +47,03% | +16,81% | FEEDBACK RAPIDO |
| DOGE | 1g | 81 | 49,38% | +0,06% | +0,05% | UTILE |
| DOGE | 2g | 80 | 45,00% | +0,29% | -0,03% | UTILE |
| DOGE | 3g | 80 | 41,25% | +0,52% | +0,16% | UTILE |
| DOGE | 5g | 78 | 46,15% | +1,25% | +0,24% | UTILE |
| DOGE | 7g | 77 | 49,35% | +1,80% | +0,40% | UTILE |
| DOGE | 10g | 75 | 41,33% | +2,40% | -0,13% | UTILE |
| DOGE | 14g | 73 | 52,05% | +4,02% | +2,20% | UTILE |
| DOGE | 21g | 67 | 58,21% | +7,75% | +1,97% | UTILE |
| DOGE | 30g | 62 | 67,74% | +11,14% | +4,93% | UTILE |
| DOGE | 45g | 48 | 45,83% | +20,69% | +4,08% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 34 | 41,18% | +26,50% | -1,66% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 80 | 52,50% | +0,30% | +0,29% | -0,28% | +0,82% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 87 | 49,43% | +0,23% | +0,29% | -0,30% | +0,73% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 87 | 49,43% | +0,23% | +0,29% | -0,30% | +0,73% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 82 | 46,34% | +0,25% | +0,01% | -0,25% | +0,77% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 35 | 42,86% | +0,53% | -0,02% | -0,31% | +1,07% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 79 | 51,90% | +0,55% | +0,50% | -0,23% | +1,24% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 86 | 52,33% | +0,52% | +0,61% | -0,22% | +1,20% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 86 | 52,33% | +0,52% | +0,61% | -0,22% | +1,20% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 81 | 45,68% | +0,51% | +0,01% | -0,13% | +1,18% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 35 | 42,86% | +0,85% | -0,11% | -0,05% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 78 | 46,15% | +0,69% | +0,60% | -1,25% | +2,46% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 85 | 49,41% | +0,85% | +0,84% | -1,29% | +2,52% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 85 | 49,41% | +0,85% | +0,84% | -1,29% | +2,52% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 80 | 38,75% | +0,87% | -0,19% | -1,22% | +2,54% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,44% | -0,66% | -1,08% | +3,10% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 78 | 43,59% | +1,42% | +1,25% | -1,91% | +3,84% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 83 | 46,99% | +1,62% | +1,60% | -1,89% | +3,96% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 83 | 46,99% | +1,62% | +1,60% | -1,89% | +3,96% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 78 | 42,31% | +1,48% | -0,69% | -1,85% | +3,90% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 34 | 35,29% | +3,06% | -2,33% | -1,68% | +5,50% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 77 | 51,95% | +2,13% | +1,99% | -2,27% | +4,96% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 81 | 56,79% | +2,35% | +2,36% | -2,24% | +5,09% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 81 | 56,79% | +2,35% | +2,36% | -2,24% | +5,09% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 76 | 43,42% | +2,31% | -1,05% | -2,22% | +5,05% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 34 | 32,35% | +4,23% | -3,81% | -2,10% | +7,38% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 75 | 57,33% | +3,09% | +2,97% | -2,52% | +6,18% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 78 | 65,38% | +3,28% | +3,29% | -2,44% | +6,35% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 78 | 65,38% | +3,28% | +3,29% | -2,44% | +6,35% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 73 | 46,58% | +3,26% | -0,39% | -2,44% | +6,39% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 32 | 37,50% | +4,84% | -4,17% | -2,09% | +8,44% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -1,47% | -1,47% | -4,23% | +1,69% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 72 | 62,50% | +4,67% | +4,62% | -2,66% | +8,35% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 76 | 60,53% | +4,65% | +4,69% | -2,68% | +8,37% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 76 | 60,53% | +4,65% | +4,69% | -2,68% | +8,37% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 70 | 57,14% | +4,83% | +1,37% | -2,65% | +8,60% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 29 | 24,14% | +5,09% | -4,15% | -1,91% | +9,57% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,11% | -0,11% | -4,30% | +2,85% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 68 | 72,06% | +8,08% | +7,98% | -2,91% | +11,95% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 71 | 76,06% | +8,03% | +8,03% | -2,89% | +11,92% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 71 | 76,06% | +8,03% | +8,03% | -2,89% | +11,92% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 64 | 56,25% | +8,48% | +1,36% | -2,86% | +12,38% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 29 | 44,83% | +8,60% | -4,88% | -2,40% | +12,46% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 63 | 95,24% | +12,23% | +11,55% | -3,00% | +16,38% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 66 | 92,42% | +12,21% | +12,21% | -2,97% | +16,46% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 66 | 92,42% | +12,21% | +12,21% | -2,97% | +16,46% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 61 | 65,57% | +12,17% | +1,25% | -2,85% | +16,59% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 25 | 64,00% | +13,14% | -2,25% | -2,64% | +17,41% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 48 | 93,75% | +21,34% | +18,59% | -2,52% | +26,08% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 51 | 100,00% | +21,67% | +21,67% | -2,52% | +26,30% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 51 | 100,00% | +21,67% | +21,67% | -2,52% | +26,30% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 46 | 52,17% | +21,75% | -2,13% | -2,31% | +26,41% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 19 | 57,89% | +16,51% | -6,34% | -2,09% | +22,16% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 34 | 91,18% | +28,15% | +23,74% | -2,81% | +33,29% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 36 | 100,00% | +27,95% | +27,95% | -2,85% | +33,15% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 36 | 100,00% | +27,95% | +27,95% | -2,85% | +33,15% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 32 | 100,00% | +28,61% | +28,61% | -2,65% | +34,01% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 31 | 38,71% | +28,33% | -7,29% | -2,59% | +33,71% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 6 | 0,00% | +33,38% | -33,38% | -1,17% | +38,35% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 81 | 49,38% | +0,06% | +0,05% | -0,73% | +1,10% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 88 | 59,09% | +0,00% | +0,53% | -0,83% | +0,98% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 88 | 59,09% | +0,00% | +0,53% | -0,83% | +0,98% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 82 | 50,00% | -0,08% | +0,13% | -0,94% | +0,89% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 50 | 40,00% | -0,06% | -0,58% | -1,00% | +0,64% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 80 | 45,00% | +0,29% | -0,03% | -0,88% | +1,63% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 87 | 58,62% | +0,10% | +0,83% | -1,02% | +1,37% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 87 | 58,62% | +0,10% | +0,83% | -1,02% | +1,37% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 81 | 53,09% | -0,20% | +0,10% | -1,33% | +1,07% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 49 | 42,86% | +0,20% | -1,18% | -1,06% | +1,11% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 80 | 41,25% | +0,52% | +0,16% | -2,55% | +3,71% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 86 | 56,98% | +0,30% | +1,20% | -2,67% | +3,45% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 86 | 56,98% | +0,30% | +1,20% | -2,67% | +3,45% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 80 | 45,00% | -0,30% | -0,17% | -2,92% | +2,81% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 48 | 33,33% | +0,50% | -2,08% | -2,72% | +3,62% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 78 | 46,15% | +1,25% | +0,24% | -3,64% | +6,04% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 84 | 54,76% | +0,92% | +1,72% | -3,86% | +5,75% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 84 | 54,76% | +0,92% | +1,72% | -3,86% | +5,75% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 78 | 50,00% | +0,15% | -0,99% | -4,25% | +5,04% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 46 | 34,78% | +1,76% | -4,54% | -3,81% | +6,54% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 77 | 49,35% | +1,80% | +0,40% | -4,30% | +7,94% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 82 | 58,54% | +1,61% | +1,94% | -4,53% | +7,68% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 82 | 58,54% | +1,61% | +1,94% | -4,53% | +7,68% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 76 | 43,42% | +0,66% | -1,46% | -4,99% | +6,73% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 44 | 27,27% | +3,07% | -6,50% | -4,35% | +8,81% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 75 | 41,33% | +2,40% | -0,13% | -5,03% | +9,93% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 79 | 55,70% | +2,23% | +1,68% | -5,10% | +9,73% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 79 | 55,70% | +2,23% | +1,68% | -5,10% | +9,73% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 73 | 43,84% | +0,97% | -2,08% | -5,64% | +8,31% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 44 | 29,55% | +3,40% | -7,10% | -5,16% | +10,81% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 73 | 52,05% | +4,02% | +2,20% | -5,81% | +13,32% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 76 | 64,47% | +3,72% | +3,35% | -5,75% | +12,99% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 76 | 64,47% | +3,72% | +3,35% | -5,75% | +12,99% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 70 | 45,71% | +1,76% | -1,78% | -6,36% | +10,51% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 43 | 39,53% | +4,51% | -5,45% | -5,57% | +13,12% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 67 | 58,21% | +7,75% | +1,97% | -5,60% | +19,02% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 70 | 58,57% | +8,09% | +4,53% | -5,59% | +19,19% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 70 | 58,57% | +8,09% | +4,53% | -5,59% | +19,19% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 64 | 54,69% | +6,13% | -2,39% | -6,26% | +16,39% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 42 | 42,86% | +5,67% | -7,44% | -5,73% | +16,02% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +4,84% | -0,04% | -5,47% | +18,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 62 | 67,74% | +11,14% | +4,93% | -5,62% | +25,51% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 65 | 69,23% | +11,42% | +7,05% | -5,60% | +25,97% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 65 | 69,23% | +11,42% | +7,05% | -5,60% | +25,97% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 59 | 57,63% | +10,00% | -2,49% | -6,35% | +23,84% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 38 | 47,37% | +9,03% | -7,21% | -5,94% | +22,34% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 88,89% | +19,48% | +12,44% | -5,48% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 48 | 45,83% | +20,69% | +4,08% | -4,71% | +38,32% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 50 | 62,00% | +20,73% | +8,17% | -4,72% | +38,36% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 50 | 62,00% | +20,73% | +8,17% | -4,72% | +38,36% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 44 | 11,36% | +17,74% | -13,34% | -5,60% | +36,20% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 31 | 3,23% | +21,52% | -22,01% | -5,10% | +38,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +21,73% | +11,03% | -4,45% | +35,73% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 34 | 41,18% | +26,50% | -1,66% | -4,14% | +44,75% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 36 | 55,56% | +26,93% | +8,80% | -4,16% | +44,90% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 36 | 55,56% | +26,93% | +8,80% | -4,16% | +44,90% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 34 | 58,82% | +26,19% | +11,65% | -4,18% | +44,69% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 31 | 3,23% | +27,11% | -25,77% | -4,65% | +43,94% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 23 | 0,00% | +25,36% | -25,36% | -4,66% | +43,08% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +38,20% | +19,48% | -1,31% | +51,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 81 | 46,91% | +0,19% | +0,12% | -0,59% | +1,05% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 83 | 54,22% | +0,18% | +0,46% | -0,69% | +1,02% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 86 | 53,49% | +0,22% | +0,40% | -0,65% | +1,05% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 81 | 45,68% | +0,18% | -0,11% | -0,75% | +1,00% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 58 | 44,83% | +0,45% | -0,03% | -0,53% | +1,39% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 80 | 45,00% | +0,66% | +0,57% | -0,60% | +1,70% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 82 | 50,00% | +0,56% | +0,75% | -0,81% | +1,47% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 85 | 49,41% | +0,55% | +0,71% | -0,78% | +1,51% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 80 | 43,75% | +0,38% | -0,12% | -0,78% | +1,48% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 58 | 48,28% | +0,59% | +0,18% | -0,66% | +1,66% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 79 | 49,37% | +1,17% | +1,06% | -2,13% | +3,72% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 81 | 53,09% | +1,02% | +1,38% | -2,26% | +3,55% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 84 | 52,38% | +0,99% | +1,32% | -2,23% | +3,55% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 79 | 43,04% | +0,61% | -0,50% | -2,29% | +3,12% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 58 | 46,55% | +0,60% | +0,10% | -2,28% | +3,11% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 77 | 51,95% | +2,10% | +2,03% | -3,06% | +5,83% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 79 | 55,70% | +1,89% | +2,29% | -3,19% | +5,62% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 82 | 54,88% | +1,85% | +2,18% | -3,15% | +5,56% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 77 | 44,16% | +1,49% | -0,92% | -3,24% | +5,07% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 57 | 49,12% | +0,81% | +0,14% | -3,23% | +4,42% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 75 | 57,33% | +3,21% | +3,28% | -3,58% | +7,59% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 77 | 63,64% | +2,96% | +3,48% | -3,71% | +7,36% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 80 | 63,75% | +2,85% | +3,36% | -3,68% | +7,23% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 75 | 38,67% | +1,99% | -1,83% | -3,80% | +6,46% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 57 | 43,86% | +0,46% | -0,12% | -4,03% | +5,07% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 72 | 59,72% | +5,15% | +5,26% | -3,85% | +9,88% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 74 | 68,92% | +4,97% | +5,59% | -4,00% | +9,49% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 77 | 67,53% | +4,77% | +5,38% | -3,98% | +9,27% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 72 | 43,06% | +3,32% | -1,94% | -4,17% | +8,12% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 54 | 46,30% | +0,86% | +0,13% | -4,44% | +6,09% | PRIMA CALIBRAZIONE |

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

Generato: 2026-10-14 05:33 UTC

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
| BTC | 90 | UTILE | 87 | 28 | 18 | 0 | Famiglia statistica | 1g | 49,43% | +0,29% | campione utile, valutare con prudenza |
| SOL | 90 | UTILE | 83 | 32 | 18 | 0 | Famiglia statistica | 1g | 54,22% | +0,46% | campione utile, valutare con prudenza |
| DOGE | 90 | UTILE | 88 | 32 | 17 | 0 | Famiglia statistica | 1g | 59,09% | +0,53% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 35 | 42,86% | -0,02% | +0,53% | -0,31% | +1,07% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 87 | 49,43% | +0,29% | +0,23% | -0,30% | +0,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 82 | 46,34% | +0,01% | +0,25% | -0,25% | +0,77% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 35 | 42,86% | -0,11% | +0,85% | -0,05% | +1,57% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 86 | 52,33% | +0,61% | +0,52% | -0,22% | +1,20% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 81 | 45,68% | +0,01% | +0,51% | -0,13% | +1,18% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 34 | 35,29% | -0,66% | +1,44% | -1,08% | +3,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Famiglia statistica | 85 | 49,41% | +0,84% | +0,85% | -1,29% | +2,52% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 80 | 38,75% | -0,19% | +0,87% | -1,22% | +2,54% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 34 | 35,29% | -2,33% | +3,06% | -1,68% | +5,50% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 83 | 46,99% | +1,60% | +1,62% | -1,89% | +3,96% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 78 | 42,31% | -0,69% | +1,48% | -1,85% | +3,90% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 34 | 32,35% | -3,81% | +4,23% | -2,10% | +7,38% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 81 | 56,79% | +2,36% | +2,35% | -2,24% | +5,09% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 76 | 43,42% | -1,05% | +2,31% | -2,22% | +5,05% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 32 | 37,50% | -4,17% | +4,84% | -2,09% | +8,44% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 78 | 65,38% | +3,29% | +3,28% | -2,44% | +6,35% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | -1,47% | -1,47% | -4,23% | +1,69% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 73 | 46,58% | -0,39% | +3,26% | -2,44% | +6,39% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 29 | 24,14% | -4,15% | +5,09% | -1,91% | +9,57% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 76 | 60,53% | +4,69% | +4,65% | -2,68% | +8,37% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 7 | 42,86% | -0,11% | -0,11% | -4,30% | +2,85% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 70 | 57,14% | +1,37% | +4,83% | -2,65% | +8,60% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 29 | 44,83% | -4,88% | +8,60% | -2,40% | +12,46% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 71 | 76,06% | +8,03% | +8,03% | -2,89% | +11,92% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 64 | 56,25% | +1,36% | +8,48% | -2,86% | +12,38% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 25 | 64,00% | -2,25% | +13,14% | -2,64% | +17,41% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 66 | 92,42% | +12,21% | +12,21% | -2,97% | +16,46% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 61 | 65,57% | +1,25% | +12,17% | -2,85% | +16,59% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Classic technical | 19 | 57,89% | -6,34% | +16,51% | -2,09% | +22,16% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 51 | 100,00% | +21,67% | +21,67% | -2,52% | +26,30% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 46 | 52,17% | -2,13% | +21,75% | -2,31% | +26,41% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 6 | 0,00% | -33,38% | +33,38% | -1,17% | +38,35% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 36 | 100,00% | +27,95% | +27,95% | -2,85% | +33,15% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 31 | 38,71% | -7,29% | +28,33% | -2,59% | +33,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Classic technical | 50 | 40,00% | -0,58% | -0,06% | -1,00% | +0,64% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 88 | 59,09% | +0,53% | +0,00% | -0,83% | +0,98% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 11 | 63,64% | +2,53% | +2,82% | +0,75% | +3,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 82 | 50,00% | +0,13% | -0,08% | -0,94% | +0,89% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 49 | 42,86% | -1,18% | +0,20% | -1,06% | +1,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 87 | 58,62% | +0,83% | +0,10% | -1,02% | +1,37% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 11 | 45,45% | +2,65% | +2,89% | +1,08% | +5,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 81 | 53,09% | +0,10% | -0,20% | -1,33% | +1,07% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 48 | 33,33% | -2,08% | +0,50% | -2,72% | +3,62% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 86 | 56,98% | +1,20% | +0,30% | -2,67% | +3,45% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 11 | 54,55% | +2,62% | +2,81% | -1,35% | +6,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 80 | 45,00% | -0,17% | -0,30% | -2,92% | +2,81% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 46 | 34,78% | -4,54% | +1,76% | -3,81% | +6,54% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 84 | 54,76% | +1,72% | +0,92% | -3,86% | +5,75% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 11 | 36,36% | +2,02% | +2,17% | -2,50% | +9,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 78 | 50,00% | -0,99% | +0,15% | -4,25% | +5,04% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 44 | 27,27% | -6,50% | +3,07% | -4,35% | +8,81% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 82 | 58,54% | +1,94% | +1,61% | -4,53% | +7,68% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 11 | 45,45% | +0,78% | +0,88% | -3,00% | +9,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 76 | 43,42% | -1,46% | +0,66% | -4,99% | +6,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 44 | 29,55% | -7,10% | +3,40% | -5,16% | +10,81% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 79 | 55,70% | +1,68% | +2,23% | -5,10% | +9,73% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 73 | 43,84% | -2,08% | +0,97% | -5,64% | +8,31% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 43 | 39,53% | -5,45% | +4,51% | -5,57% | +13,12% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 76 | 64,47% | +3,35% | +3,72% | -5,75% | +12,99% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 11 | 45,45% | +2,03% | +5,60% | -4,35% | +14,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 70 | 45,71% | -1,78% | +1,76% | -6,36% | +10,51% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 42 | 42,86% | -7,44% | +5,67% | -5,73% | +16,02% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 70 | 58,57% | +4,53% | +8,09% | -5,59% | +19,19% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 11 | 63,64% | -0,04% | +4,84% | -5,47% | +18,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 64 | 54,69% | -2,39% | +6,13% | -6,26% | +16,39% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Classic technical | 38 | 47,37% | -7,21% | +9,03% | -5,94% | +22,34% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 65 | 69,23% | +7,05% | +11,42% | -5,60% | +25,97% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 9 | 88,89% | +12,44% | +19,48% | -5,48% | +30,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 59 | 57,63% | -2,49% | +10,00% | -6,35% | +23,84% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 31 | 3,23% | -22,01% | +21,52% | -5,10% | +38,53% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Famiglia statistica | 50 | 62,00% | +8,17% | +20,73% | -4,72% | +38,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 8 | 62,50% | +11,03% | +21,73% | -4,45% | +35,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 44 | 11,36% | -13,34% | +17,74% | -5,60% | +36,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 23 | 0,00% | -25,36% | +25,36% | -4,66% | +43,08% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 36 | 55,56% | +8,80% | +26,93% | -4,16% | +44,90% | PESO OK | 0,0 | MEDIA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 4 | 75,00% | +19,48% | +38,20% | -1,31% | +51,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 31 | 3,23% | -25,77% | +27,11% | -4,65% | +43,94% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 1g | BREVE | Classic technical | 58 | 44,83% | -0,03% | +0,45% | -0,53% | +1,39% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 83 | 54,22% | +0,46% | +0,18% | -0,69% | +1,02% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 81 | 45,68% | -0,11% | +0,18% | -0,75% | +1,00% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 58 | 48,28% | +0,18% | +0,59% | -0,66% | +1,66% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 82 | 50,00% | +0,75% | +0,56% | -0,81% | +1,47% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 80 | 43,75% | -0,12% | +0,38% | -0,78% | +1,48% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 58 | 46,55% | +0,10% | +0,60% | -2,28% | +3,11% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 81 | 53,09% | +1,38% | +1,02% | -2,26% | +3,55% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 79 | 43,04% | -0,50% | +0,61% | -2,29% | +3,12% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 57 | 49,12% | +0,14% | +0,81% | -3,23% | +4,42% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 79 | 55,70% | +2,29% | +1,89% | -3,19% | +5,62% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 77 | 44,16% | -0,92% | +1,49% | -3,24% | +5,07% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 57 | 43,86% | -0,12% | +0,46% | -4,03% | +5,07% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 77 | 63,64% | +3,48% | +2,96% | -3,71% | +7,36% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 75 | 38,67% | -1,83% | +1,99% | -3,80% | +6,46% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 54 | 46,30% | +0,13% | +0,86% | -4,44% | +6,09% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 74 | 68,92% | +5,59% | +4,97% | -4,00% | +9,49% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 72 | 43,06% | -1,94% | +3,32% | -4,17% | +8,12% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 51 | 45,10% | +0,50% | +2,22% | -5,04% | +7,85% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 71 | 77,46% | +8,66% | +7,95% | -4,30% | +13,30% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 69 | 40,58% | -2,80% | +5,47% | -4,65% | +11,18% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 45 | 60,00% | -1,01% | +10,15% | -4,85% | +15,58% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 66 | 81,82% | +14,43% | +14,48% | -4,34% | +20,23% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 63 | 52,38% | -5,03% | +12,00% | -4,72% | +17,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Classic technical | 42 | 54,76% | -4,29% | +22,25% | -4,70% | +27,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 61 | 90,16% | +19,36% | +21,90% | -4,40% | +28,89% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 60 | 45,00% | -7,68% | +20,40% | -4,74% | +26,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 45g | MEDIO | Classic technical | 32 | 34,38% | -19,31% | +31,63% | -4,07% | +41,70% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Famiglia statistica | 46 | 76,09% | +22,43% | +36,65% | -3,84% | +45,14% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +28,91% | +28,91% | -3,55% | +37,55% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 48 | 31,25% | -23,08% | +35,40% | -4,29% | +43,98% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 21 | 0,00% | -53,73% | +53,73% | -4,64% | +60,15% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 32 | 75,00% | +33,10% | +50,15% | -4,69% | +58,81% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +47,10% | +47,10% | -5,94% | +54,98% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 34 | 11,76% | -40,68% | +48,66% | -5,09% | +57,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 81 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 88 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 104 | 40,38% | -0,26% |
| BTC | BREVE | Famiglia statistica | 258 | 50,39% | +0,58% |
| BTC | BREVE | Microstruttura exchange | 27 | 37,04% | -0,30% |
| BTC | BREVE | Tecnico | 243 | 43,62% | -0,06% |
| BTC | SETTIMANALE | Classic technical | 100 | 35,00% | -3,42% |
| BTC | SETTIMANALE | Famiglia statistica | 242 | 56,20% | +2,40% |
| BTC | SETTIMANALE | Microstruttura exchange | 24 | 25,00% | -1,73% |
| BTC | SETTIMANALE | Tecnico | 227 | 44,05% | -0,71% |
| BTC | SWING | Classic technical | 58 | 34,48% | -4,52% |
| BTC | SWING | Famiglia statistica | 147 | 68,03% | +6,30% |
| BTC | SWING | Microstruttura exchange | 14 | 50,00% | +0,11% |
| BTC | SWING | Tecnico | 134 | 56,72% | +1,36% |
| BTC | MEDIO | Classic technical | 50 | 54,00% | -7,54% |
| BTC | MEDIO | Famiglia statistica | 153 | 96,73% | +19,07% |
| BTC | MEDIO | Microstruttura exchange | 9 | 100,00% | +9,68% |
| BTC | MEDIO | Tecnico | 138 | 55,07% | -1,79% |
| DOGE | BREVE | Classic technical | 147 | 38,78% | -1,27% |
| DOGE | BREVE | Famiglia statistica | 261 | 58,24% | +0,85% |
| DOGE | BREVE | Microstruttura exchange | 33 | 54,55% | +2,60% |
| DOGE | BREVE | Tecnico | 243 | 49,38% | +0,02% |
| DOGE | SETTIMANALE | Classic technical | 134 | 30,60% | -6,03% |
| DOGE | SETTIMANALE | Famiglia statistica | 245 | 56,33% | +1,78% |
| DOGE | SETTIMANALE | Microstruttura exchange | 33 | 45,45% | +1,16% |
| DOGE | SETTIMANALE | Tecnico | 227 | 45,81% | -1,50% |
| DOGE | SWING | Classic technical | 85 | 41,18% | -6,43% |
| DOGE | SWING | Famiglia statistica | 146 | 61,64% | +3,92% |
| DOGE | SWING | Microstruttura exchange | 22 | 54,55% | +0,99% |
| DOGE | SWING | Tecnico | 134 | 50,00% | -2,07% |
| DOGE | MEDIO | Classic technical | 92 | 20,65% | -16,74% |
| DOGE | MEDIO | Famiglia statistica | 151 | 63,58% | +7,84% |
| DOGE | MEDIO | Microstruttura exchange | 21 | 76,19% | +13,25% |
| DOGE | MEDIO | Tecnico | 134 | 29,85% | -11,44% |
| SOL | BREVE | Classic technical | 174 | 46,55% | +0,08% |
| SOL | BREVE | Famiglia statistica | 246 | 52,44% | +0,86% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 240 | 44,17% | -0,24% |
| SOL | SETTIMANALE | Classic technical | 168 | 46,43% | +0,05% |
| SOL | SETTIMANALE | Famiglia statistica | 230 | 62,61% | +3,75% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 224 | 41,96% | -1,55% |
| SOL | SWING | Classic technical | 96 | 52,08% | -0,21% |
| SOL | SWING | Famiglia statistica | 137 | 79,56% | +11,44% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 132 | 46,21% | -3,86% |
| SOL | MEDIO | Classic technical | 95 | 35,79% | -20,28% |
| SOL | MEDIO | Famiglia statistica | 139 | 82,01% | +23,54% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 12 | 100,00% | +28,96% |
| SOL | MEDIO | Tecnico | 142 | 32,39% | -20,79% |

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

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-10-14 05:33 UTC

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
| BTC | 0 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD / ATTESA CONFERME | Prima resistenza sopra 87.146; conferma del eve and adam bottom sopra 82.262. | Sotto 80.337 il quadro tecnico peggiora. |
| SOL | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 123,48. | Allarmi sotto 96,23. |
| DOGE | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.10528 migliora; sopra 0.07997 viene invalidato il pattern ribassista dominante. | Sotto 0.08122 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | 0 | +1 | 0 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| SOL | +3 | 0 | +3 | 0 | -2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +2 |
| DOGE | +3 | 0 | +3 | 0 | -2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +2 |

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

- Famiglia statistica: **+1** — Scanner grezzo +1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+1** — Casi positivi 52,50%, return centrale 30g +2,89%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 88. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-1** — Score tecnico -2/12, verdetto neutrale / misto, trend rialzista, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score -1 (rialzista Eve and Adam Bottom / MATURO; ribassista Doppio massimo / CONFERMATO RECENTE). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff DISTRIBUZIONE POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Fractal path: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- RSI top-cycle: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — BTC: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Prima resistenza sopra 87.146; conferma del eve and adam bottom sopra 82.262.

Invalidazioni: Sotto 80.337 il quadro tecnico peggiora.

### SOL

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**

SOL è ancora in zona mista. Il frattale resta soltanto uno scenario contestuale: non è confermato dal prezzo e vale 0 punti operativi finché il gap non rientra. Meglio evitare leva e ragionare solo a tranche piccole.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 3. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 75,00%, return centrale 30g +8,47%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 3, positivi 30g 33,33%, return p50 -4,58%.
- Scanner path: **0** — Controlli disponibili 88. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -6/12, verdetto debole, trend misto, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff range / fase non chiara, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Triplo massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 2 / MARKUP, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff RANGE / FASE NON CHIARA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Fractal path: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- RSI top-cycle: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 2, bias CONTESTO DA OSSERVARE, EMA200 111,38 $, upside EMA200 +3,87%, gap EMA50/EMA200 -4,37%, hit EMA200 12w +86,67%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 2, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **+1** — SOL: cambiamento medio in miglioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 123,48.

Invalidazioni: Allarmi sotto 96,23.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 1. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 85,00%, return centrale 30g +13,91%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 1, positivi 30g 100,00%, return p50 +6,52%.
- Scanner path: **0** — Controlli disponibili 88. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -6/12, verdetto debole, trend ribassista, struttura volatilità in espansione, divergenza nessuna, Wyckoff range / fase non chiara, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -4/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Fractal path: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- RSI top-cycle: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow -0.25, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — DOGE: cambiamento medio in miglioramento rispetto a ieri.

Conferme: Sopra 0.10528 migliora; sopra 0.07997 viene invalidato il pattern ribassista dominante.

Invalidazioni: Sotto 0.08122 il rischio ribassista aumenta.


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

Generato: 2026-10-14 05:33 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 83.479 $ | prezzo corrente |
| Power Law centrale | 126.791 $ | deviazione -34,16% |
| Banda p10-p90 | 79.063 $ / 320.342 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 15,71% | posizione storica nel corridoio |
| Esponente β | 5,7835 | R² log-log 91,94% |
| Stabilità β | BASSA | range 1,3154 cambiando finestra |
| Ultimo halving | 2024-04-19 | 908 giorni fa |
| Fase ciclo | 62,15% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-10-14 (4410 osservazioni)
- Formula stimata: prezzo ≈ exp(-38.8947) × giorni^5.7835
- Prezzo centrale oggi: **126.791 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 15,71%
- Scarto dal centro: **-34,16%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,7835 | 91,94% |
| 2015 | 5,8631 | 91,49% |
| 2016 | 5,5449 | 87,78% |
| 2017 | 4,8216 | 83,07% |
| 2018 | 4,5477 | 78,66% |

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
| 2012-11-28 → 2016-07-09 | 2015-02-26 | +6,92% | +0,36% | -6,27% | +82,79% |
| 2016-07-09 → 2020-05-11 | 2018-11-27 | -4,34% | +1,62% | +127,00% | +97,13% |
| 2020-05-11 → 2024-04-19 | 2022-10-22 | -17,81% | +18,06% | +47,05% | +56,15% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | 2 | 0 | -0.47987082584149965 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -6 | -1 | -5.41035562375437 | 0 |

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

Generato: 2026-10-14 05:33 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00128580 | +2 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | -0,48% | RIBASSISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000101 | -6 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -5,41% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

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
- **Rendimenti relativi:** 7g -8,94%; 30g -0,48%; 90g +7,69%; 180g +8,60%
- **Daily:** RSI 33.71; MA50 0.00134552; MA200 0.00120126
- **Weekly:** MA30 0.00120669; RSI 50.84
- **Livelli:** supporto 0.00127800; resistenza 0.00129400; breakout 60g 0.00146600; breakdown 60g 0.00117400
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00133900; target 0.00140150
- **Fibonacci:** VICINO — 38.2% a 0.00129143
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in salita; struttura con massimi/minimi crescenti; RSI relativo debole; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-6)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g -7,40%; 30g -5,41%; 90g -11,32%; 180g -23,13%
- **Daily:** RSI 35.26; MA50 0.00000109; MA200 0.00000121
- **Weekly:** MA30 0.00000121; RSI 36.62
- **Livelli:** supporto 0.00000100; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000097
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000110
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; prezzo sotto MA30 weekly; MA30 weekly in discesa; RSI relativo debole; MACD relativo negativo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 212 | 52,36% | +1,92% | -1,06% |
| SOL | 30g | 209 | 47,85% | +4,56% | +0,63% |
| SOL | 90g | 202 | 52,97% | +9,80% | +3,12% |
| DOGE | 7g | 296 | 55,41% | +1,80% | -1,66% |
| DOGE | 30g | 295 | 52,88% | +1,96% | -3,48% |
| DOGE | 90g | 290 | 54,48% | +6,90% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 52 | 48,08% | -0,01% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 52 | 44,23% | +0,06% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 50 | 38,00% | -0,43% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 44 | 40,91% | -0,54% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 35 | 57,14% | -0,22% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 63 | 66,67% | +0,14% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 61 | 62,30% | +0,26% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 57 | 56,14% | -0,24% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 54 | 50,00% | -0,66% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 51 | 54,90% | -0,04% | LOCKED / RACCOLTA LIVE | 0 |

Gate prudente: almeno 30 controlli live a 7 giorni, accuratezza almeno 55% e return corretto direzione positivo. Anche dopo il gate, il contributo futuro non dovrà superare ±1 e dovrà restare dentro la famiglia tecnica.

## File prodotti

- `reports/relative_strength_btc_metrics.csv`
- `reports/relative_strength_btc_history.csv`
- `reports/relative_strength_btc_tracker_metrics.csv`
- `reports/relative_strength_btc_backtest.csv`
<!-- RELATIVE_STRENGTH_BTC_END -->

</details>
<!-- COMPACT_SECTION_END:relative_strength_btc -->

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
| Confronto precedente | 2026-10-12 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 107,38 $ |
| EMA200 weekly target | 111,38 $ |
| Upside verso EMA200 | +3,87% |
| Distanza prezzo da EMA200 | -3,73% |
| Gap EMA50/EMA200 | -4,37% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 55,32 |
| Età SOL | 6,5 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +86,67% |
| Max gain mediano 12w | +31,01% |
| Drawdown mediano 12w | -25,22% |

Lettura semplice:

**SOLO OSSERVAZIONE**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-10-14 05:33 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-10-14 05:30:22 UTC**

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
- SOL: cambiamento importante in miglioramento rispetto a ieri.
- DOGE: cambiamento importante in miglioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | NESSUN CAMBIAMENTO FORTE | peggioramento | NEUTRALE / INCERTO | +52.50% | -2.50 punti |
| SOL | CAMBIAMENTO MEDIO | miglioramento | RIALZISTA | +75.00% | +5.00 punti |
| DOGE | CAMBIAMENTO MEDIO | miglioramento | RIALZISTA | +85.00% | +5.00 punti |

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
| BTC | 79.348 $ | 91.877 $ | +33,33% | +15,79% | rimbalzo poco frequente | 91.877 $ | 79.348 $ | +28,00% | -13,64% | spike storicamente più resistente |
| SOL | 102,01 $ | 118,12 $ | +44,00% | +15,79% | rimbalzo debole | 118,12 $ | 102,01 $ | +19,35% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08056 $ | 0,09328 $ | +50,00% | +15,79% | rimbalzo possibile | 0,09328 $ | 0,08056 $ | +13,89% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 10 poi sono rimbalzati fino a +10,00%. Percentuale: +33,33% (10/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 7 poi sono scaricati a -5,00%. Percentuale: +28,00% (7/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +44,00% (11/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **SOL: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 6 poi sono scaricati a -5,00%. Percentuale: +19,35% (6/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 18 prima sono scesi a -5,00%. Tra quei 18, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +50,00% (9/18). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **DOGE: su 40 casi simili, 36 prima sono saliti a +10,00%. Tra quei 36, 5 poi sono scaricati a -5,00%. Percentuale: +13,89% (5/36). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-10-14 05:32:25 UTC

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-10-14 | 2026-10-14T05:30:21Z | 2026-10-14 05:30:22 |
| SOL | 2026-10-14 | 2026-10-14T05:30:21Z | 2026-10-14 05:30:22 |
| DOGE | 2026-10-14 | 2026-10-14T05:30:21Z | 2026-10-14 05:30:22 |

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
| BTC | 2026-10-14 | 83.524 $ | INCERTO | 52,50% | 65.633,98 $ | 72.055,54 $ | 85.942,23 $ | 93.648,08 $ | 101.871,32 $ |
| SOL | 2026-10-14 | 107,38 $ | SALITA | 75,00% | 93,55 $ | 108,36 $ | 116,47 $ | 128,24 $ | 139,73 $ |
| DOGE | 2026-10-14 | 0.08480 $ | SALITA | 85,00% | 0.07779 $ | 0.09021 $ | 0.09659 $ | 0.10602 $ | 0.11487 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | AVAILABLE | SAME_BTC_REGIME | 0 | 0 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 85.942,23 $ | 88.733,66 $ | 101.871,32 $ | 114.235,01 $ |
| SOL | AVAILABLE | SAME_BTC_REGIME | 3 | 4 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 116,47 $ | 113,03 $ | 139,73 $ | 145,52 $ |
| DOGE | AVAILABLE | SAME_BTC_REGIME | 1 | 2 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.09659 $ | 0.09009 $ | 0.11487 $ | 0.12389 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-09-14**; verificato fino al **2026-10-14**; stato **COMPLETO 30/30g**.
- Reale **83.476,82 $**; p50 previsto **106.139,56 $**; scarto **-21,35%**.
- Errore medio assoluto **5,45%**; massimo **21,35%**; DENTRO p10-p90; FUORI p25-p75.

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

**Campione corrente:** 11 episodi qualificati su 40 · 10 asset distinti.

![SOL conditional successor corrente](scanner_forecast_SOL_conditional_successor_current.png)

###### Confronto diretto a 30 giorni

| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Cono standard | 2026-10-14 | 40 | 2026-11-13 | 93.55 $ | 108.36 $ | 116.47 $ | 128.24 $ | 139.73 $ |
| Conditional corrente | 2026-10-14 | 11 | 2026-11-13 | 94.84 $ | 103.57 $ | 115.76 $ | 160.90 $ | 240.55 $ |

###### Struttura successiva dei casi correnti

| Classe | Episodi | Frequenza empirica |
| --- | ---: | ---: |
| DIRECT_CONTINUATION | 4 | 36.36% |
| SHALLOW_PULLBACK_THEN_CONTINUATION | 2 | 18.18% |
| DEEP_PULLBACK_THEN_RECOVERY | 1 | 9.09% |
| FAILURE | 4 | 36.36% |
| UNRESOLVED | 0 | 0.00% |

###### Episodi qualificati oggi

| Asset | Match window | -5% hit | +10% anchor | Classe 60d |
| --- | --- | --- | --- | --- |
| XTZ-USD | 2019-09-24 → 2020-01-01 | 2020-01-02 | 2020-01-20 | SHALLOW_PULLBACK_THEN_CONTINUATION |
| HBAR-USD | 2022-11-29 → 2023-03-08 | 2023-03-09 | 2023-03-29 | FAILURE |
| AVAX-USD | 2021-07-01 → 2021-10-08 | 2021-10-10 | 2021-10-25 | DEEP_PULLBACK_THEN_RECOVERY |
| RUNE-USD | 2023-07-01 → 2023-10-08 | 2023-10-09 | 2023-10-23 | DIRECT_CONTINUATION |
| ETC-USD | 2023-09-18 → 2023-12-26 | 2024-01-07 | 2024-01-10 | DIRECT_CONTINUATION |
| VET-USD | 2022-11-29 → 2023-03-08 | 2023-03-09 | 2023-03-17 | FAILURE |
| SNX-USD | 2020-11-17 → 2021-02-24 | 2021-02-26 | 2021-03-02 | FAILURE |
| ZIL-USD | 2022-11-29 → 2023-03-08 | 2023-03-09 | 2023-03-14 | SHALLOW_PULLBACK_THEN_CONTINUATION |
| ETH-USD | 2021-06-15 → 2021-09-22 | 2021-09-28 | 2021-10-02 | DIRECT_CONTINUATION |
| ETH-USD | 2022-11-27 → 2023-03-06 | 2023-03-09 | 2023-03-17 | DIRECT_CONTINUATION |
| FIL-USD | 2022-12-01 → 2023-03-10 | 2023-03-11 | 2023-03-13 | FAILURE |

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

- Ultimo close disponibile: **2026-10-14** · SOL **107.29 $**.
- Giorno del vintage: **26/30**.
- P50 condizionato previsto per quel giorno: **172.78 $**.
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

- Cono congelato il **2026-09-14**; verificato fino al **2026-10-14**; stato **COMPLETO 30/30g**.
- Reale **107,29 $**; p50 previsto **132,72 $**; scarto **-19,16%**.
- Errore medio assoluto **7,97%**; massimo **19,52%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted SOL](scanner_forecast_SOL_regime_adjusted.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-09-14**; verificato fino al **2026-10-14**; stato **COMPLETO 30/30g**.
- Reale **0.08475 $**; p50 previsto **0.07323 $**; scarto **15,73%**.
- Errore medio assoluto **14,53%**; massimo **25,05%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted DOGE](scanner_forecast_DOGE_regime_adjusted.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 88 | 94,32% | 71,59% | 1,81% | 0,38% |
| BTC | 3g | 84 | 94,05% | 78,57% | 3,10% | 0,63% |
| BTC | 7g | 76 | 93,42% | 71,05% | 4,81% | 1,30% |
| BTC | 14g | 63 | 98,41% | 76,19% | 5,62% | 0,97% |
| BTC | 30g | 37 | 100,00% | 72,97% | 11,49% | -3,53% |
| SOL | 1g | 88 | 85,23% | 63,64% | 2,61% | 0,60% |
| SOL | 3g | 84 | 91,67% | 72,62% | 3,76% | 1,51% |
| SOL | 7g | 76 | 92,11% | 76,32% | 5,73% | 2,61% |
| SOL | 14g | 63 | 88,89% | 79,37% | 7,83% | 5,27% |
| SOL | 30g | 37 | 94,59% | 67,57% | 14,55% | 6,23% |
| DOGE | 1g | 88 | 88,64% | 61,36% | 2,94% | 0,34% |
| DOGE | 3g | 84 | 92,86% | 64,29% | 4,49% | 1,24% |
| DOGE | 7g | 76 | 77,63% | 75,00% | 8,30% | 4,62% |
| DOGE | 14g | 63 | 85,71% | 53,97% | 10,02% | 8,28% |
| DOGE | 30g | 37 | 94,59% | 37,84% | 16,81% | 16,81% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |

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
- Casi positivi / salita storica: **52,50%**
- Casi negativi / discesa storica: **47,50%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **83.524,31 $**
- Return normale fra 30 giorni: **85.942,23 $** (2,89%)
- Drawdown normale durante il mese: **75.286,86 $** (-9,86%)
- Drawdown brutto da rispettare: **66.787,93 $** (-20,04%)
- Max gain normale durante il mese: **94.786,26 $** (13,48%)
- Max gain buono / take profit ottimistico: **101.869,22 $** (21,96%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **75,00%**
- Casi negativi / discesa storica: **25,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **107,38 $**
- Return normale fra 30 giorni: **116,47 $** (8,47%)
- Drawdown normale durante il mese: **99,63 $** (-7,21%)
- Drawdown brutto da rispettare: **94,00 $** (-12,46%)
- Max gain normale durante il mese: **126,08 $** (17,41%)
- Max gain buono / take profit ottimistico: **138,59 $** (29,06%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **85,00%**
- Casi negativi / discesa storica: **15,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,08 $**
- Return normale fra 30 giorni: **0,10 $** (13,91%)
- Drawdown normale durante il mese: **0,08 $** (-4,50%)
- Drawdown brutto da rispettare: **0,08 $** (-8,31%)
- Max gain normale durante il mese: **0,10 $** (20,71%)
- Max gain buono / take profit ottimistico: **0,11 $** (33,95%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 83.524,31 $

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

- Se va molto male: **65.633,98 $** (-21,42%)
- Se va male: **72.055,54 $** (-13,73%)
- Scenario normale: **85.942,23 $** (2,89%)
- Se va bene: **93.648,08 $** (12,12%)
- Se va molto bene: **101.871,32 $** (21,97%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **75.286,86 $** (-9,86%)
- Discesa brutta: **66.787,93 $** (-20,04%)
- Discesa molto brutta: **63.776,55 $** (-23,64%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **94.786,26 $** (13,48%)
- Rialzo buono: **101.869,22 $** (21,96%)
- Rialzo molto forte: **112.209,13 $** (34,34%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **75.286,86 $** e uno spike normale intorno a **94.786,26 $**.

La chiusura a 30 giorni è incerta: salita 52,50%, discesa 47,50%. Non c'è un vantaggio netto.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 107,38 $

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

- Se va molto male: **93,55 $** (-12,88%)
- Se va male: **108,36 $** (0,91%)
- Scenario normale: **116,47 $** (8,47%)
- Se va bene: **128,24 $** (19,42%)
- Se va molto bene: **139,73 $** (30,13%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **99,63 $** (-7,21%)
- Discesa brutta: **94,00 $** (-12,46%)
- Discesa molto brutta: **84,27 $** (-21,53%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **126,08 $** (17,41%)
- Rialzo buono: **138,59 $** (29,06%)
- Rialzo molto forte: **152,56 $** (42,07%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **99,63 $** e uno spike normale intorno a **126,08 $**.

La chiusura a 30 giorni era più spesso positiva: salita 75,00%, discesa 25,00%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 0,08 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **85,00%**
- Probabilità storica di discesa: **15,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,08 $** (-8,27%)
- Se va male: **0,09 $** (6,38%)
- Scenario normale: **0,10 $** (13,91%)
- Se va bene: **0,11 $** (25,02%)
- Se va molto bene: **0,11 $** (35,46%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,08 $** (-4,50%)
- Discesa brutta: **0,08 $** (-8,31%)
- Discesa molto brutta: **0,07 $** (-16,68%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,10 $** (20,71%)
- Rialzo buono: **0,11 $** (33,95%)
- Rialzo molto forte: **0,12 $** (43,54%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,08 $** e uno spike normale intorno a **0,10 $**.

La chiusura a 30 giorni era più spesso positiva: salita 85,00%, discesa 15,00%. Quindi la lettura principale è favorevole.

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

- Previsioni già controllate: **44**
- Direzione corretta: **91,89%**
- Errore medio dello scenario centrale: **9,92%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **2,27%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **44**
- Direzione corretta: **73,68%**
- Errore medio dello scenario centrale: **15,45%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **27,27%**
- Prezzo finale dentro lo scenario 10%-90%: **95,45%**

### Solana

- Previsioni già controllate: **44**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **12,54%**
- Zona rischio toccata: **4,55%**
- Zona rialzo media toccata: **25,00%**
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

- Previsioni controllate: **44**
- Previsioni usate per la calibrazione recente: **44**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **91,89%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **INCERTO**
- Direzione calibrata oggi: **INCERTO**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **2,89%** → **85.942,23 $**
- Correzione imparata dagli errori: **-3,24%**
- Calibrato: **-0,35%** → **83.236,09 $**
- Lettura: Lo scanner è stato troppo ottimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-9,86%** → **75.286,86 $**
- Correzione imparata dagli errori: **4,84%**
- Calibrato: **-5,02%** → **79.330,97 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **13,48%** → **94.786,26 $**
- Correzione imparata dagli errori: **-7,66%**
- Calibrato: **5,82%** → **88.385,32 $**
- Lettura: Lo scanner ha sovrastimato gli spike: nella realtà il prezzo è salito meno del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Solana

- Previsioni controllate: **44**
- Previsioni usate per la calibrazione recente: **44**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **100,00%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **8,47%** → **116,47 $**
- Correzione imparata dagli errori: **3,46%**
- Calibrato: **11,93%** → **120,19 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-7,21%** → **99,63 $**
- Correzione imparata dagli errori: **3,48%**
- Calibrato: **-3,73%** → **103,37 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **17,41%** → **126,08 $**
- Correzione imparata dagli errori: **-1,50%**
- Calibrato: **15,91%** → **124,46 $**
- Lettura: Lo scanner è stato abbastanza centrato sul max gain.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Dogecoin

- Previsioni controllate: **44**
- Previsioni usate per la calibrazione recente: **44**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **73,68%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **13,91%** → **0,10 $**
- Correzione imparata dagli errori: **15,45%**
- Calibrato: **29,36%** → **0,11 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-4,50%** → **0,08 $**
- Correzione imparata dagli errori: **13,67%**
- Calibrato: **9,16%** → **0,09 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **20,71%** → **0,10 $**
- Correzione imparata dagli errori: **2,95%**
- Calibrato: **23,65%** → **0,10 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 83.524,31 $

Bitcoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **52,50%**
- Casi negativi dopo 30 giorni: **47,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,62%**
- Rendimento medio dopo 30 giorni: **2,39%**
- Rendimento centrale dopo 30 giorni: **2,89%**
- Discesa media durante i 30 giorni: **-12,22%**
- Massimo rialzo medio durante i 30 giorni: **17,18%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **85.522,60 $**
- Scenario centrale a 30 giorni: **85.942,23 $**
- Zona di rischio media: **73.319,14 $**
- Zona di rialzo media: **97.873,74 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -21,42% → **65.633,98 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -13,73% → **72.055,54 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 2,89% → **85.942,23 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 12,12% → **93.648,08 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 21,97% → **101.871,32 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -23,64% → **63.776,55 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -20,04% → **66.787,93 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -9,86% → **75.286,86 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -5,03% → **79.319,77 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,37% → **83.214,93 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,94% → **85.146,81 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 6,72% → **89.138,84 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 13,48% → **94.786,26 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 21,96% → **101.869,22 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 34,34% → **112.209,13 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| BTC-USD         | 2022-12-01   | 2023-03-10 |        90.46 |        40.35 |           0    |          41.07 |
| RUNE-USD        | 2023-07-01   | 2023-10-08 |        89.2  |        95.43 |         -12.18 |         104.76 |
| QTUM-USD        | 2023-09-13   | 2023-12-21 |        88.1  |        -7.79 |         -10.59 |          12.02 |
| XTZ-USD         | 2019-09-24   | 2020-01-01 |        87.58 |        21.02 |          -9.43 |          22.45 |
| THETA-USD       | 2023-09-17   | 2023-12-25 |        87.53 |       -31.86 |         -33.99 |           0    |
| XTZ-USD         | 2023-09-18   | 2023-12-26 |        86.9  |       -10.73 |         -16.39 |          11.38 |
| ETH-USD         | 2022-11-27   | 2023-03-06 |        86.76 |        21.8  |          -8.82 |          21.8  |
| MANA-USD        | 2023-09-13   | 2023-12-21 |        86.66 |        -9.26 |         -18.18 |           7.58 |
| CRV-USD         | 2022-12-01   | 2023-03-10 |        86.55 |        14.31 |          -2.49 |          15.59 |
| MKR-USD         | 2020-11-23   | 2021-03-02 |        86.5  |         5.95 |         -15.96 |           5.95 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 107,38 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **75,00%**
- Casi negativi dopo 30 giorni: **25,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **87,51%**
- Rendimento medio dopo 30 giorni: **9,93%**
- Rendimento centrale dopo 30 giorni: **8,47%**
- Discesa media durante i 30 giorni: **-9,74%**
- Massimo rialzo medio durante i 30 giorni: **22,73%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **118,04 $**
- Scenario centrale a 30 giorni: **116,47 $**
- Zona di rischio media: **96,92 $**
- Zona di rialzo media: **131,79 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -12,88% → **93,55 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 0,91% → **108,36 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 8,47% → **116,47 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 19,42% → **128,24 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 30,13% → **139,73 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -21,53% → **84,27 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -12,46% → **94,00 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -7,21% → **99,63 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -2,34% → **104,87 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **107,38 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 5,04% → **112,79 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 10,26% → **118,40 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 17,41% → **126,08 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 29,06% → **138,59 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 42,07% → **152,56 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| BTC-USD         | 2022-12-01   | 2023-03-10 |        90.88 |        40.35 |           0    |          41.07 |
| XTZ-USD         | 2019-09-24   | 2020-01-01 |        90.72 |        21.02 |          -9.43 |          22.45 |
| CRV-USD         | 2022-12-01   | 2023-03-10 |        90.01 |        14.31 |          -2.49 |          15.59 |
| MKR-USD         | 2020-11-23   | 2021-03-02 |        89.76 |         5.95 |         -15.96 |           5.95 |
| HBAR-USD        | 2022-11-29   | 2023-03-08 |        89.43 |         6.98 |          -5.35 |          20.94 |
| MKR-USD         | 2019-01-03   | 2019-04-12 |        89.33 |       -12.6  |         -21.33 |           5.99 |
| THETA-USD       | 2022-12-01   | 2023-03-10 |        89.08 |        15.44 |          -0.02 |          20.13 |
| AVAX-USD        | 2021-07-01   | 2021-10-08 |        89.03 |        44.92 |         -10.18 |          44.92 |
| ENJ-USD         | 2022-12-02   | 2023-03-11 |        88.81 |        23.45 |           0    |          33.6  |
| RUNE-USD        | 2023-07-01   | 2023-10-08 |        88.38 |        95.43 |         -12.18 |         104.76 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 0,08 $

Dogecoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **85,00%**
- Casi negativi dopo 30 giorni: **15,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **83,71%**
- Rendimento medio dopo 30 giorni: **15,18%**
- Rendimento centrale dopo 30 giorni: **13,91%**
- Discesa media durante i 30 giorni: **-7,00%**
- Massimo rialzo medio durante i 30 giorni: **26,65%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,10 $**
- Scenario centrale a 30 giorni: **0,10 $**
- Zona di rischio media: **0,08 $**
- Zona di rialzo media: **0,11 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -8,27% → **0,08 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 6,38% → **0,09 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 13,91% → **0,10 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 25,02% → **0,11 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 35,46% → **0,11 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -16,68% → **0,07 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -8,31% → **0,08 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -4,50% → **0,08 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -0,02% → **0,08 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **0,08 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 9,91% → **0,09 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 13,49% → **0,10 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 20,71% → **0,10 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 33,95% → **0,11 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 43,54% → **0,12 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XTZ-USD         | 2019-09-24   | 2020-01-01 |        91.09 |        21.02 |          -9.43 |          22.45 |
| BTC-USD         | 2022-12-01   | 2023-03-10 |        87.42 |        40.35 |           0    |          41.07 |
| AAVE-USD        | 2022-11-30   | 2023-03-09 |        86.18 |        11.15 |          -1.88 |          17.43 |
| ENJ-USD         | 2022-12-02   | 2023-03-11 |        85.82 |        23.45 |           0    |          33.6  |
| THETA-USD       | 2022-12-01   | 2023-03-10 |        85.7  |        15.44 |          -0.02 |          20.13 |
| CRV-USD         | 2022-12-01   | 2023-03-10 |        85.7  |        14.31 |          -2.49 |          15.59 |
| LINK-USD        | 2019-08-25   | 2019-12-02 |        85.6  |       -13.76 |         -16.16 |           8.39 |
| MKR-USD         | 2020-11-23   | 2021-03-02 |        85.6  |         5.95 |         -15.96 |           5.95 |
| SOL-USD         | 2022-11-30   | 2023-03-09 |        85.17 |        15.76 |           0    |          30.68 |
| ICP-USD         | 2022-11-30   | 2023-03-09 |        85.07 |         3.07 |          -0.41 |          18.47 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report

Generated: 2026-10-14 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-14 | BULL | 83.524 $ | True | 30.94% | 3.98% | BULL | 30.94% | 3.98% |
| DOGE-USD | 2026-10-14 | RECOVERY | 0.08480 $ | False | 17.22% | -3.22% | BULL | 30.94% | 3.98% |
| SOL-USD | 2026-10-14 | BULL | 107,38 $ | True | 42.66% | 6.08% | BULL | 30.94% | 3.98% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 52.50% | 2.89% | 12.12% | 21.97% | -9.86% | -23.64% | 13.48% | 21.96% | 34.34% | 47.50% | -0.55% | 19.36% | 50.30% |
| BTC-USD | SAME_BTC_REGIME | 8 | 75.00% | 6.24% | 10.16% | 36.77% | -8.15% | -18.14% | 11.71% | 13.62% | 40.99% | 37.50% | -7.82% | 30.03% | 166.60% |
| BTC-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 85.00% | 13.91% | 25.02% | 35.46% | -4.50% | -16.68% | 20.71% | 33.95% | 43.54% | 60.00% | 4.42% | 35.34% | 65.41% |
| DOGE-USD | SAME_BTC_REGIME | 8 | 75.00% | 6.24% | 12.79% | 46.10% | -9.49% | -18.29% | 13.36% | 20.62% | 52.89% | 62.50% | 38.33% | 68.76% | 166.60% |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 50.00% | -0.63% | 2.94% | 5.09% | -8.70% | -10.21% | 12.81% | 13.21% | 13.45% | 50.00% | -15.96% | -7.30% | -2.11% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 6.52% | 6.52% | 6.52% | -6.80% | -6.80% | 13.61% | 13.61% | 13.61% | 0.00% | -33.27% | -33.27% | -33.27% |
| SOL-USD | ALL_MATCHES | 40 | 75.00% | 8.47% | 19.42% | 30.13% | -7.21% | -21.53% | 17.41% | 29.06% | 42.07% | 50.00% | 0.06% | 20.85% | 42.55% |
| SOL-USD | SAME_BTC_REGIME | 13 | 69.23% | 5.27% | 8.74% | 35.52% | -9.50% | -20.31% | 13.11% | 17.27% | 37.16% | 38.46% | -11.19% | 15.36% | 104.23% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 50.00% | -1.58% | 8.31% | 20.72% | -12.76% | -19.86% | 4.85% | 12.57% | 26.05% | 50.00% | 1.62% | 21.20% | 31.71% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 3 | 33.33% | -4.58% | -1.58% | 0.22% | -16.72% | -20.31% | 4.61% | 4.85% | 4.99% | 33.33% | -12.12% | 1.62% | 9.87% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 24 | 58.33% | 7.35% | -9.50% | 24.98% | 50.00% | 0.06% | 41.99% |
| BTC-USD | HISTORICAL_BTC_BULL | 8 | 75.00% | 6.24% | -8.15% | 13.62% | 37.50% | -7.82% | 50.64% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 21.02% | -9.43% | 22.45% | 100.00% | 91.44% | 163.75% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 7 | 0.00% | -9.54% | -18.18% | 12.69% | 42.86% | -0.57% | 16.42% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 29 | 89.66% | 14.31% | -2.49% | 35.03% | 55.17% | 3.42% | 46.53% |
| DOGE-USD | HISTORICAL_BTC_BULL | 8 | 75.00% | 6.24% | -9.49% | 20.62% | 62.50% | 38.33% | 68.76% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 25.98% | -6.31% | 42.79% | 100.00% | 78.98% | 144.43% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -7.79% | -10.59% | 12.02% | 100.00% | 1.35% | 12.02% |
| SOL-USD | HISTORICAL_BTC_BEAR | 26 | 76.92% | 11.38% | -5.09% | 32.87% | 53.85% | 2.07% | 42.85% |
| SOL-USD | HISTORICAL_BTC_BULL | 13 | 69.23% | 5.27% | -9.50% | 17.27% | 38.46% | -11.19% | 42.76% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 21.02% | -9.43% | 22.45% | 100.00% | 91.44% | 163.75% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 33 | 54.55% | 3.07% | -9.54% | 22.51% | 48.48% | -0.52% | 41.71% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -0.40% | -19.60% | 6.71% | 50.00% | 57.69% | 96.76% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 40.00% | -4.66% | -9.50% | 12.02% | 40.00% | -12.41% | 13.61% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 33 | 90.91% | 15.44% | -3.12% | 40.91% | 57.58% | 3.50% | 51.03% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | 7.61% | -12.48% | 28.37% | 100.00% | 36.76% | 52.02% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 5.95% | -15.96% | 12.12% | 66.67% | 41.88% | 81.29% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | -0.63% | -8.70% | 13.21% | 50.00% | -15.96% | 13.21% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 79.31% | 11.15% | -5.52% | 30.68% | 51.72% | 0.65% | 42.87% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | -1.58% | -12.76% | 12.57% | 50.00% | 1.62% | 32.42% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | -0.40% | -15.87% | 17.42% | 50.00% | 18.71% | 62.03% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 41.98% | 0.00% | 41.98% | 100.00% | 11.39% | 52.04% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 8.10% | -8.15% | 12.79% | 0.00% | -26.57% | 12.79% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 0 | 0 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 1 | 2 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 3 | 4 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-01 | 89.20% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| BTC-USD | MKR-USD | 2020-11-23 | 86.50% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| BTC-USD | ADA-USD | 2025-05-30 | 85.63% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| BTC-USD | ONE-USD | 2023-07-25 | 85.41% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -0.10% | -0.87% | 1.16% | 0.10% | -0.87% | 1.16% |
| BTC-USD | ETH-USD | 2025-05-30 | 84.62% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 9.67% | -9.50% | 10.32% | -19.86% | -22.97% | 10.32% |
| BTC-USD | LRC-USD | 2020-11-22 | 84.45% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| BTC-USD | XLM-USD | 2025-05-25 | 84.07% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 11.63% | -1.79% | 13.66% | -14.48% | -16.25% | 14.61% |
| BTC-USD | HBAR-USD | 2025-05-27 | 83.97% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 2.72% | -5.52% | 13.11% | -11.19% | -25.89% | 13.11% |
| DOGE-USD | LINK-USD | 2019-08-25 | 85.60% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -13.76% | -16.16% | 8.39% | 34.79% | -16.89% | 39.05% |
| DOGE-USD | MKR-USD | 2020-11-23 | 85.60% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| DOGE-USD | ADA-USD | 2025-05-30 | 84.66% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| DOGE-USD | LRC-USD | 2020-11-22 | 83.82% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| DOGE-USD | RUNE-USD | 2023-07-01 | 83.51% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| DOGE-USD | ZEC-USD | 2024-05-30 | 82.52% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 8.74% | -4.86% | 17.27% | 41.88% | -4.86% | 42.76% |
| DOGE-USD | HBAR-USD | 2025-05-27 | 82.11% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 2.72% | -5.52% | 13.11% | -11.19% | -25.89% | 13.11% |
| DOGE-USD | MKR-USD | 2023-05-17 | 81.78% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 24.95% | -1.75% | 30.65% | 51.74% | -1.75% | 51.74% |
| SOL-USD | MKR-USD | 2020-11-23 | 89.76% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| SOL-USD | RUNE-USD | 2023-07-01 | 88.38% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| SOL-USD | ADA-USD | 2025-05-30 | 88.20% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| SOL-USD | LRC-USD | 2020-11-22 | 88.14% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| SOL-USD | ETH-USD | 2025-05-30 | 87.89% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 9.67% | -9.50% | 10.32% | -19.86% | -22.97% | 10.32% |
| SOL-USD | LINK-USD | 2025-05-30 | 87.73% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -9.44% | 13.20% | -31.77% | -33.69% | 13.20% |
| SOL-USD | HBAR-USD | 2025-05-27 | 87.30% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 2.72% | -5.52% | 13.11% | -11.19% | -25.89% | 13.11% |
| SOL-USD | LINK-USD | 2019-08-20 | 86.86% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -15.37% | -21.21% | 5.09% | 15.36% | -21.89% | 24.45% |
| SOL-USD | ZEC-USD | 2024-05-30 | 86.76% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 8.74% | -4.86% | 17.27% | 41.88% | -4.86% | 42.76% |
| SOL-USD | BNB-USD | 2025-05-30 | 86.68% | BULL | MIXED | SAME_BTC_ONLY | BULLISH_30D | 41.98% | 0.00% | 41.98% | 11.39% | 0.00% | 52.04% |

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

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Percorsi dei casi estremi

**SOSPESO dal 13 ottobre 2026.** Nessun nuovo calcolo o segnale.

Storico e ultime metriche conservati come archivio, non come dati correnti.
Gli input archiviati non contribuiscono a Global Confluence.
<!-- EXTREME_CASES_PATH_END -->

</details>
<!-- COMPACT_SECTION_END:extreme_cases -->

<!-- COMPACT_SECTION_START:classic_technical -->
<details>
<summary><strong>📐 Conferma tecnica classica</strong></summary>

<!-- CLASSIC_TECHNICAL_CONFIRMATION_START -->
# Classic technical confirmation report

Generato: 2026-10-14 05:32 UTC

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
| BTC | 83.524 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI DECRESCENTI | DISTRIBUZIONE POSSIBILE | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 107,38 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 2 / MARKUP | MASSIMI E MINIMI DECRESCENTI | RANGE / FASE NON CHIARA | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.08480 $ | -4 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | VOLATILITÀ IN ESPANSIONE | ACCUMULO POSSIBILE / RANGE BASSO | MEDIO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | -2 | +2 | -2 | 0 | 0 | -2 | -2 |
| SOL | +4 | -2 | -2 | -2 | 0 | 0 | 0 | -2 |
| DOGE | -3 | 0 | +1 | -2 | 0 | 0 | 0 | -4 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 82.571 $ | 87.146 $ | 87.364 $ | 62.488 $ | 2,46% | 8,61% | 28,96% |
| SOL | 105,84 $ | 110,04 $ | 124,62 $ | 74,20 $ | 3,92% | 8,05% | 38,80% |
| DOGE | 0.08189 $ | 0.08494 $ | 0.10528 $ | 0.06895 $ | 4,57% | 2,77% | 14,39% |

## Lettura dettagliata

### BTC

- Prezzo: **83.524 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,46%; distanza supporto 1,07%; distanza resistenza 4,42%

Dettaglio:

- Trend: **+2** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in salita; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+2** — RSI sano 53.0; RSI in miglioramento; MACD sotto signal; istogramma MACD in miglioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.11; volume ratio 0.95
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — DISTRIBUZIONE POSSIBILE. Prezzo alto nel range ma CMF negativo: possibile distribuzione.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 53.03 |
| MACD histogram | -502.27691 |
| CMF20 | -0.114 |
| Volume ratio 20 | 0.95 |
| MA20 | 83.960 $ |
| MA50 | 81.112 $ |
| MA100 | 73.287 $ |
| MA200 | 72.131 $ |
| Pendenza MA50 20g | +8,83% |
| Pendenza MA200 60g | +3,78% |
| Bollinger width | 5,92% |
| Bollinger position | 0.40 |

### SOL

- Prezzo: **107,38 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 3,92%; distanza supporto 1,32%; distanza resistenza 2,61%

Dettaglio:

- Trend: **+4** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in salita; STAGE 2 / MARKUP
- Stage weekly: **STAGE 2 / MARKUP** — Prezzo sopra MA30 weekly con MA30 in salita.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **-2** — RSI neutrale 41.8; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.07; volume ratio 0.86
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 41.81 |
| MACD histogram | -2.13090 |
| CMF20 | -0.072 |
| Volume ratio 20 | 0.86 |
| MA20 | 116,35 $ |
| MA50 | 109,26 $ |
| MA100 | 93,50 $ |
| MA200 | 87,02 $ |
| Pendenza MA50 20g | +15,13% |
| Pendenza MA200 60g | +5,75% |
| Bollinger width | 20,22% |
| Bollinger position | 0.08 |

### DOGE

- Prezzo: **0.08480 $**
- Score classico: **-4 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **MEDIO** — ATR14 4,57%; distanza supporto 3,43%; distanza resistenza 0,29%

Dettaglio:

- Trend: **-3** — prezzo sotto MA200 daily; MA50 daily in salita; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **+1** — RSI neutrale 42.6; RSI in miglioramento; MACD sotto signal; istogramma MACD in miglioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.12; volume ratio 0.61
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 42.58 |
| MACD histogram | -0.00145 |
| CMF20 | -0.123 |
| Volume ratio 20 | 0.61 |
| MA20 | 0.09168 $ |
| MA50 | 0.08861 $ |
| MA100 | 0.08091 $ |
| MA200 | 0.08753 $ |
| Pendenza MA50 20g | +8,11% |
| Pendenza MA200 60g | -3,52% |
| Bollinger width | 24,04% |
| Bollinger position | 0.16 |

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

Generato: 2026-10-14 05:33 UTC

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
| BTC | 83.524 $ | Doppio massimo | CONFERMATO RECENTE | ribassista | 2026-10-08 | 77.778 $ | -19,90% | n/a | Fib 50,0% REJECTION (-1) @ 83.742 $ | NEL RANGE | 82.571 $ |
| SOL | 107,38 $ | Triplo massimo | CANDIDATO | ribassista | n/a | 62,51 $ | n/a | 51,89% | Fib 23,6% PERSO (0) @ 111,02 $ | NEL RANGE | 97,45 $ |
| DOGE | 0.08480 $ | Doppio minimo | CANDIDATO | rialzista | n/a | 0.13028 $ | n/a | 24,15% | Fib 23,6% REJECTION (0) @ 0.08689 $ | NEL RANGE | 0.08122 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CONFERMATO RECENTE** (-2)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-21 -> 2026-10-02**
- Età formazione: **12 giorni**
- Breakout pattern: **2026-10-08**
- Età breakout: **6 giorni**
- Neckline: **82.571 $**
- Target teorico: **77.778 $**
- Progresso verso target: **-19,90%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 50,0% REJECTION (-1) @ 83.742 $** — Swing DOWN 2026-10-02 87.146 -> 2026-10-08 80.337; livello più vicino 50.0% a 83.742; stato REJECTION; confluenza: neckline rialzista, neckline ribassista, invalidazione ribassista.
- Invalidazione: **84.222 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 87.364 tra 2026-09-21 e 2026-10-02. Neckline ribassista stimata: 82.571. Breakout neckline: 2026-10-08 (6 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 77.778; progresso corrente: -19,90%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **82.571 $**
- Resistenza: **87.146 $**
- Breakout 60g: **87.364 $**
- Breakdown 60g: **62.488 $**
- RSI14: **53.25**
- ATR14: **2,45%**
- Volume ratio 20g: **0.95**
- Rendimento 30g: **+8,70%**
- Rendimento 90g: **+29,07%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CONFERMATO RECENTE | -2 | ribassista | 82.571 $ | 2026-10-08 | 6g | 77.778 $ | -19,90% | n/a | 84.222 $ | Due massimi simili a 87.364 $ e 87.146 $. Neckline circa 82.571 $. Breakout neckline: 2026-10-08 (6 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 77.778 $; progresso: -19,90%; prezzo sopra neckline. |
| Doppio minimo | MATURO | +1 | rialzista | 82.262 $ | 2026-09-21 | 23g | 89.580 $ | 17,25% | n/a | 80.617 $ | Due minimi simili a 76.248 $ e 74.945 $. Neckline circa 82.262 $. Breakout neckline: 2026-09-21 (23 giorni fa). Stato: MATURO. Target teorico: 89.580 $; progresso: 17,25%; prezzo sopra neckline. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **66 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **70,69 $**
- Target teorico: **62,51 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **51,89%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% PERSO (0) @ 111,02 $** — Swing UP 2026-08-01 70,69 -> 2026-10-02 123,48; livello più vicino 23.6% a 111,02; stato PERSO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **72,11 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 66 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **97,45 $**
- Resistenza: **110,04 $**
- Breakout 60g: **124,62 $**
- Breakdown 60g: **74,20 $**
- RSI14: **42.07**
- ATR14: **3,91%**
- Volume ratio 20g: **0.86**
- Rendimento 30g: **+8,20%**
- Rendimento 90g: **+38,98%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,51 $ | n/a | 51,89% | 72,11 $ | Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 66 giorni. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 51,89% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 66 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 107,12 $ | 2026-09-18 | 26g | 118,01 $ | 2,42% | n/a | 104,97 $ | Due minimi simili a 97,45 $ e 96,23 $. Neckline circa 107,12 $. Breakout neckline: 2026-09-18 (26 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01 $; progresso: 2,42%; prezzo vicino alla neckline. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 56g | 85,65 $ | 390,63% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (56 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 390,63%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-10-08**
- Età formazione: **6 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.10528 $**
- Target teorico: **0.13028 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **24,15%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% REJECTION (0) @ 0.08689 $** — Swing DOWN 2026-09-22 0.10528 -> 2026-10-08 0.08122; livello più vicino 23.6% a 0.08689; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.10318 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 0.08028 tra 2026-09-02 e 2026-10-08. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.08122 $**
- Resistenza: **0.09169 $**
- Breakout 60g: **0.10528 $**
- Breakdown 60g: **0.06895 $**
- RSI14: **42.76**
- ATR14: **4,57%**
- Volume ratio 20g: **0.61**
- Rendimento 30g: **+2,89%**
- Rendimento 90g: **+14,53%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.10528 $ | n/a | n/a | 0.13028 $ | n/a | 24,15% | 0.10318 $ | Due minimi simili a 0.08028 $ e 0.08122 $. Neckline circa 0.10528 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 6 giorni. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.07841 $ | n/a | n/a | 0.05153 $ | n/a | 8,16% | 0.07997 $ | Due massimi simili a 0.09998 $ e 0.10528 $. Neckline circa 0.07841 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 22 giorni. |

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

<!-- COMPACT_SECTION_START:btc_sol_fractal -->
<details>
<summary><strong>🧬 Frattale mirato BTC 2022 / SOL 2026</strong></summary>

<!-- BTC_SOL_FRACTAL_START -->
# Frattale BTC 2022 / SOL 2026

**SOSPESO dal 13 ottobre 2026.** Nessun nuovo calcolo o segnale.

Storico e ultime metriche conservati come archivio, non come dati correnti.
Gli input archiviati non contribuiscono a Global Confluence.
<!-- BTC_SOL_FRACTAL_END -->

</details>
<!-- COMPACT_SECTION_END:btc_sol_fractal -->

<!-- COMPACT_SECTION_START:fractal_path -->
<details>
<summary><strong>🛤️ Tracking percorso frattale SOL/BTC</strong></summary>

<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking frattale SOL/BTC

**SOSPESO dal 13 ottobre 2026.** Nessun nuovo calcolo o segnale.

Storico e ultime metriche conservati come archivio, non come dati correnti.
Gli input archiviati non contribuiscono a Global Confluence.
<!-- FRACTAL_PATH_TRACKER_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:rsi_top_cycle -->
<details>
<summary><strong>📈 RSI top-cycle SOL</strong></summary>

<!-- RSI_TOP_CYCLE_START -->
# RSI top-cycle SOL

**SOSPESO dal 13 ottobre 2026.** Nessun nuovo calcolo o segnale.

Storico e ultime metriche conservati come archivio, non come dati correnti.
Gli input archiviati non contribuiscono a Global Confluence.
<!-- RSI_TOP_CYCLE_END -->

</details>
<!-- COMPACT_SECTION_END:rsi_top_cycle -->

<!-- COMPACT_SECTION_START:sol_onchain -->
<details>
<summary><strong>⛓️ Metriche on-chain SOL</strong></summary>

<!-- SOL_ONCHAIN_METRICS_START -->
# Metriche on-chain SOL

**SOSPESO dal 13 ottobre 2026.** Nessun nuovo calcolo o segnale.

Storico e ultime metriche conservati come archivio, non come dati correnti.
Gli input archiviati non contribuiscono a Global Confluence.
<!-- SOL_ONCHAIN_METRICS_END -->

</details>
<!-- COMPACT_SECTION_END:sol_onchain -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-10-14 05:33 UTC

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 83.548 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0035% | -2,90% | 1,71 | +0,59% | 0 $ | 0 $ |
| SOL | 107,53 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0051% | -0,48% | 2,68 | +3,03% | 0 $ | 0 $ |
| DOGE | 0.08493 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0060% | -0,28% | 0,90 | -3,58% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0090% | 174,75 mln $ | 6,42 | -1,77% |
| BTC | Bitget | OK | +0,0020% | 2,69 mld $ | 1,56 | +14,17% |
| BTC | Kucoin | OK | +0,0027% | 803,59 mln $ | 1,36 | -0,72% |
| SOL | Kraken | OK | +0,0155% | 35,42 mln $ | 1,22 | +16,58% |
| SOL | Bitget | OK | +0,0100% | 431,28 mln $ | 1,17 | +49,83% |
| SOL | Kucoin | OK | +0,0097% | 133,66 mln $ | 2,24 | +5,33% |
| DOGE | Kraken | OK | -0,0030% | 4,69 mln $ | 0,91 | -5,98% |
| DOGE | Bitget | OK | +0,0043% | 116,76 mln $ | 1,23 | +4,42% |
| DOGE | Kucoin | OK | +0,0079% | 56,46 mln $ | 1,38 | -17,54% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 9, accuratezza +33,33%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci rejection; nessuna conferma exchange netta. Confluenza tecnica dichiarata: neckline rialzista, neckline ribassista, invalidazione ribassista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** Eve and Adam Bottom maturo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+1,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 2, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci perso; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **-0,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 11, accuratezza +45,45%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **-0,25**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci rejection; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +52,50% | +2,89% | 5 | +80,00% | RACCOLTA DATI | 0,00 | +52,50% | +2,89% |
| SOL | +75,00% | +8,47% | 5 | +100,00% | RACCOLTA DATI | 0,00 | +75,00% | +8,47% |
| DOGE | +85,00% | +13,91% | 9 | +77,78% | RACCOLTA DATI | 0,00 | +85,00% | +13,91% |

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

Generato: 2026-10-14 05:33 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-14 | BTC | 83.547,70 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,71 | -2,90% | +0,59% |
| 2026-10-14 | DOGE | 0.08493 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,90 | -0,28% | -3,58% |
| 2026-10-14 | SOL | 107,53 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 2,68 | -0,48% | +3,03% |
| 2026-10-13 | BTC | 83.468,90 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,23 | -1,31% | -1,54% |
| 2026-10-13 | DOGE | 0.08465 | V2.1.3 | OK | 0 | 0 | 0,00 | BASSA | 1,00 | -2,24% | -5,28% |
| 2026-10-13 | SOL | 108,16 | V2.1.3 | OK | 0 | 0 | 2,25 | BASSA | 2,46 | -5,94% | +2,32% |
| 2026-10-12 | BTC | 84.123,15 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,90 | -1,01% | -1,73% |
| 2026-10-12 | DOGE | 0.08793 | V2.1.3 | OK | 0 | 0 | 2,75 | BASSA | 1,16 | +3,80% | -3,71% |
| 2026-10-12 | SOL | 113,18 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,19 | +0,99% | +10,18% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 10 | +40,00% | -0,44% | -1,18% | +0,59% | FEEDBACK RAPIDO |
| BTC | 3g | 10 | +40,00% | -0,44% | -2,45% | +1,64% | FEEDBACK RAPIDO |
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

**SOL** — SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**DOGE** — DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 83.524 $ | +0.0032% | -10.79% | 1.55 | Misto | 1/5 |
| SOL | 107,38 $ | +0.0100% | -14.76% | 2.05 | Rischio sotto | 2/5 |
| DOGE | 0.08480 $ | +0.0067% | -3.62% | 4.23 | Misto | 1/5 |

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

Generato: 2026-10-14 05:33 UTC

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                      | Stato D       | Weekly                     | Stato W       | Lettura weekly                                                                                              |   Peso |
|:--------|:---------------------------|:--------------|:---------------------------|:--------------|:------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Misto / nessuna divergenza | CONTESTO      | Misto / nessuna divergenza | CONTESTO      | Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.                        |      0 |
| SOL     | Hidden bullish             | IN_FORMAZIONE | Hidden bullish             | IN_FORMAZIONE | Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0. |      0 |
| DOGE    | Conferma ribassista        | CONTESTO      | Conferma ribassista        | CONTESTO      | Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.   |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                       | Stato         | Prezzo / RSI      | Pivot confrontati                                                | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:---------------------------|:--------------|:------------------|:-----------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Misto / nessuna divergenza | CONTESTO      | 83.460 $ / 53,05  | n/a                                                              | -0,19%              | -8,21            |      0 |
| BTC     | 1W   | Misto / nessuna divergenza | CONTESTO      | 83.460 $ / 59,07  | n/a                                                              | +3,87%              | 0,04             |      0 |
| SOL     | 1D   | Hidden bullish             | IN_FORMAZIONE | 107,25 $ / 41,83  | 2026-09-16 96,23 $ / RSI 51,17 → 2026-10-12 105,41 $ / RSI 38,59 | n/a                 | n/a              |      0 |
| SOL     | 1W   | Hidden bullish             | IN_FORMAZIONE | 107,25 $ / 55,33  | 2026-09-20 96,23 $ / RSI 61,01 → 2026-10-18 105,41 $ / RSI 55,33 | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Conferma ribassista        | CONTESTO      | 0.08470 $ / 42,58 | n/a                                                              | -9,76%              | -13,25           |      0 |
| DOGE    | 1W   | Conferma ribassista        | CONTESTO      | 0.08470 $ / 46,06 | n/a                                                              | -6,74%              | -2,82            |      0 |

### BTC

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.

### SOL

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.

### DOGE

- **1D — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.
- **1W — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **9**.
- Soglie di lettura: **30 / 60 / 100 controlli**.
- Anche oltre le soglie il peso resta **0** finché non viene presa una decisione esplicita.

| Asset   | TF   | Tipo             |   Orizzonte |   Controlli | Accuratezza   | Return corretto   | Stato         |   Peso |
|:--------|:-----|:-----------------|------------:|------------:|:--------------|:------------------|:--------------|-------:|
| BTC     | 1D   | Bullish regolare |          30 |           1 | 0,00%         | -1,52%            | RACCOLTA DATI |      0 |
| BTC     | 1D   | Bullish regolare |          60 |           1 | +100,00%      | +21,03%           | RACCOLTA DATI |      0 |
| BTC     | 1D   | Bullish regolare |          90 |           1 | +100,00%      | +30,34%           | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bearish   |          30 |           1 | 0,00%         | -1,37%            | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bearish   |          60 |           1 | 0,00%         | -23,44%           | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bearish   |          90 |           1 | 0,00%         | -33,97%           | RACCOLTA DATI |      0 |
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

Generato: 2026-10-14 05:33 UTC

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

| Asset   | Prezzo   |   Punteggio | Verdetto         | Trend            | Momentum        | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista                | Pattern ribassista                  | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-----------------|:-----------------|:----------------|:------------------------------------------------------|----------------:|:---------------|:---------------------------------|:------------------------------------|:-----------|:-------------|
| BTC | 83.524 $ | -2 | NEUTRALE / MISTO | Trend rialzista | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | -1 | -1 / REJECTION | Eve and Adam Bottom / MATURO | Doppio massimo / CONFERMATO RECENTE | 80.337 | 87.146 |
| SOL | 107,38 $ | -6 | DEBOLE | Trend misto | Momentum debole | Struttura ribassista con massimi e minimi decrescenti | 0 | 0 / PERSO | Doppio minimo / TARGET RAGGIUNTO | Triplo massimo / CANDIDATO | 96,23 | 123,48 |
| DOGE | 0.08480 $ | -6 | DEBOLE | Trend ribassista | Momentum misto | Volatilità in espansione | 0 | 0 / REJECTION | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 0.08122 | 0.10528 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo     | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-------------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Eve and Adam Bottom — MATURO | CONFERMATO RECENTE | CANDIDATO | Adam and Eve Top — CANDIDATO | -1 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | INVALIDATO | CANDIDATO | ASSENTE | 0 |
| DOGE | CANDIDATO | CANDIDATO | Adam and Eve Bottom — INVALIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 53.25 | -497.79 | 83.964 | 81.113 | 72.131 | 8,26% | 3,98% | 6,86% | 30,94% |
| SOL | 42.07 | -2.12196 | 116,36 | 109,26 | 87,02 | 14,10% | 6,08% | 4,77% | 42,66% |
| DOGE | 42.76 | -0.00145 | 0.09168 | 0.08861 | 0.08753 | 7,43% | -3,22% | 1,40% | 17,22% |

## Dettaglio asset

### BTC

- Prezzo: **83.524 $**
- Punteggio tecnico: **-2 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum misto** (-1)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 8.257e+04 -> 8.034e+04. Ultimi massimi: 8.736e+04 -> 8.715e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **REJECTION** (-1)
  - Swing DOWN 2026-10-02 87.146 -> 2026-10-08 80.337; livello più vicino 50.0% a 83.742; stato REJECTION; confluenza: neckline rialzista, neckline ribassista, invalidazione ribassista.
- Punteggio pattern: **-1**
  - rialzista dominante: Eve and Adam Bottom (MATURO, +1); ribassista dominante: Doppio massimo (CONFERMATO RECENTE, -2).
- Supporto più vicino: **80.337**
- Resistenza più vicina: **87.146**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 76.248 tra 2026-09-02 e 2026-10-08. Neckline stimata: 87.364. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 87.364; target 98.479; distanza dalla neckline 4,60%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 74.945 dal 2026-09-02 al 2026-10-08. Neckline stimata: 87.364. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 87.364; target 99.783; distanza dalla neckline 4,60%; prezzo sotto neckline.
- Eve and Adam Bottom: **MATURO** (+1)
  - Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (23 giorni fa). Stato: MATURO. Target teorico: 89.580; progresso corrente: 17,25%. Relazione prezzo/neckline: sopra neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (23g); progresso 17,25%; prezzo sopra neckline.
- Doppio massimo: **CONFERMATO RECENTE** (-2)
  - Due massimi simili vicino a 87.364 tra 2026-09-21 e 2026-10-02. Neckline ribassista stimata: 82.571. Breakout neckline: 2026-10-08 (6 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 77.778; progresso corrente: -19,90%. Relazione prezzo/neckline: sopra neckline.
  - neckline 82.571; target 77.778; breakout 2026-10-08 (6g); progresso -19,90%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 87.364 dal 2026-09-03 al 2026-10-02. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 74.945; target 62.525; distanza dalla neckline 11,45%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 87.146 dal 2026-09-03 al 2026-10-02. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 74.945; target 62.743; distanza dalla neckline 11,45%; prezzo sopra neckline.

### SOL

- Prezzo: **107,38 $**
- Punteggio tecnico: **-6 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend misto** (1)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 97.45 -> 96.23. Ultimi massimi: 124.6 -> 123.5.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 71,37%. Fase non abbastanza chiara.
- Fibonacci automatico: **PERSO** (0)
  - Swing UP 2026-08-01 70,69 -> 2026-10-02 123,48; livello più vicino 23.6% a 111,02; stato PERSO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Triplo massimo (CANDIDATO, 0).
- Supporto più vicino: **96,23**
- Resistenza più vicina: **123,48**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 96,23 tra 2026-09-02 e 2026-09-16. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (26 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: 2,42%. Relazione prezzo/neckline: vicino alla neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (26g); progresso 2,42%; prezzo vicino alla neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (56 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 356,76%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (56g); progresso 356,76%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 96,23 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (26 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: 2,42%. Relazione prezzo/neckline: vicino alla neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (26g); progresso 2,42%; prezzo vicino alla neckline.
- Doppio massimo: **INVALIDATO** (0)
  - Due massimi simili vicino a 110,04 tra 2026-08-27 e 2026-09-06. Neckline ribassista stimata: 97,45. Breakout neckline: 2026-09-15 (29 giorni fa). Stato: INVALIDATO. Target teorico: 84,86; progresso corrente: -78,88%. Relazione prezzo/neckline: sopra neckline.
  - neckline 97,45; target 84,86; breakout 2026-09-15 (29g); progresso -78,88%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 66 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 51,89%; prezzo sopra neckline.
- Adam/Eve Top: **ASSENTE** (0)

### DOGE

- Prezzo: **0.08480 $**
- Punteggio tecnico: **-6 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (-1)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 0.09053 -> 0.08122. Ultimi massimi: 0.09421 -> 0.1053.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 45,10%. Fase non abbastanza chiara.
- Fibonacci automatico: **REJECTION** (0)
  - Swing DOWN 2026-09-22 0.10528 -> 2026-10-08 0.08122; livello più vicino 23.6% a 0.08689; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.08122**
- Resistenza più vicina: **0.10528**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.08028 tra 2026-09-02 e 2026-10-08. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 0.10528; target 0.13028; distanza dalla neckline 24,15%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 0.07841 dal 2026-09-02 al 2026-10-08. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 0.10528; target 0.13216; distanza dalla neckline 24,15%; prezzo sotto neckline.
- Adam and Eve Bottom: **INVALIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.07841 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (23 giorni fa). Stato: INVALIDATO. Target teorico: 0.11001; progresso corrente: -59,54%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.09421; target 0.11001; breakout 2026-09-21 (23g); progresso -59,54%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.10528 tra 2026-08-22 e 2026-09-22. Neckline ribassista stimata: 0.07841. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 22 giorni.
  - neckline 0.07841; target 0.05153; distanza dalla neckline 8,16%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 64 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 24,76%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07380 dal 2026-07-26 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 64 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 24,76%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato     | Confluenza                                                        |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:----------|:------------------------------------------------------------------|--------:|
| BTC | DOWN 2026-10-02 -> 2026-10-08 | 81.944 | 82.938 | 83.742 | 84.545 | 85.689 | 50.0% / 83.742 | REJECTION | neckline rialzista, neckline ribassista, invalidazione ribassista | -1 |
| SOL | UP 2026-08-01 -> 2026-10-02 | 111,02 | 103,32 | 97,09 | 90,86 | 81,99 | 23.6% / 111,02 | PERSO | nessuna confluenza indipendente | 0 |
| DOGE | DOWN 2026-09-22 -> 2026-10-08 | 0.08689 | 0.09041 | 0.09325 | 0.09609 | 0.10013 | 23.6% / 0.08689 | REJECTION | nessuna confluenza indipendente | 0 |

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

<!-- COMPACT_SECTION_START:risk_calibration -->
<details>
<summary><strong>🛡️ Calibrazione rischio spot / leva</strong></summary>

<!-- RISK_CALIBRATION_START -->
# Calibrazione del rischio sospesa

**QUARANTENA: errore nella lettura dei prezzi dal testo.**

Le vecchie statistiche non misurano affidabilmente il rischio e non vengono utilizzate. Il diario originale e le metriche precedenti sono conservati per audit. Nessuna correzione retroattiva, nessun nuovo snapshot di rischio.
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

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

- **BTC**: 44/30 previsioni controllate su 97 fatte. Stato: **ATTIVA**.
- **SOL**: 44/30 previsioni controllate su 97 fatte. Stato: **ATTIVA**.
- **DOGE**: 44/30 previsioni controllate su 97 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 97 | 44 | 30/30 [██████████] | 53 | ATTIVA | 2026-10-15 / tra 1 giorno |
| SOL | 97 | 44 | 30/30 [██████████] | 53 | ATTIVA | 2026-10-15 / tra 1 giorno |
| DOGE | 97 | 44 | 30/30 [██████████] | 53 | ATTIVA | 2026-10-15 / tra 1 giorno |

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

Generato: 2026-10-14 05:33 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- Calibrazione rischio in quarantena; moduli sospesi esclusi dalla verifica prezzi correnti. Consultare lab_reduction_status.md.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo         | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:--------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price | OK      | 83.524 $          | 83.524 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price | OK      | 0.08480 $         | 0.08480 $       | -0,0000%     |
| Scanner                 | SOL     | current_price | OK      | 107,38 $          | 107,38 $        | -0,0000%     |
| Scanner Forecast        | BTC     | current_price | OK      | 83.524 $          | 83.524 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price | OK      | 107,38 $          | 107,38 $        | -0,0000%     |
| Scanner Forecast        | DOGE    | current_price | OK      | 0.08480 $         | 0.08480 $       | -0,0000%     |
| Technical Structure     | BTC     | price         | OK      | 83.524 $          | 83.524 $        | +0,0000%     |
| Technical Structure     | SOL     | price         | OK      | 107,38 $          | 107,38 $        | -0,0000%     |
| Technical Structure     | DOGE    | price         | OK      | 0.08480 $         | 0.08480 $       | -0,0000%     |
| Classic Technical       | BTC     | price         | OK      | 83.524 $          | 83.524 $        | +0,0000%     |
| Classic Technical       | SOL     | price         | OK      | 107,38 $          | 107,38 $        | -0,0000%     |
| Classic Technical       | DOGE    | price         | OK      | 0.08480 $         | 0.08480 $       | -0,0000%     |
| Classic Visual          | BTC     | price         | OK      | 83.524 $          | 83.524 $        | +0,0000%     |
| Classic Visual          | SOL     | price         | OK      | 107,38 $          | 107,38 $        | -0,0000%     |
| Classic Visual          | DOGE    | price         | OK      | 0.08480 $         | 0.08480 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price         | OK      | 83.524 $          | 83.548 $        | +0,0280%     |
| Exchange Microstructure | SOL     | price         | OK      | 107,38 $          | 107,53 $        | +0,1388%     |
| Exchange Microstructure | DOGE    | price         | OK      | 0.08480 $         | 0.08493 $       | +0,1533%     |

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
