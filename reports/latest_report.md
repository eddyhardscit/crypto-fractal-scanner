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

Generato: 2026-10-15 05:34 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -2 | LEGGERMENTE BEARISH | NON INSEGUIRE / RIDUCI RISCHIO | NO LONG A LEVA | NO SHORT | nessuna | nessuna | ALTO |
| SOL | +1 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | -2 | LEGGERMENTE BEARISH | EVITA LONG / SOLO RIMBALZI VELOCI | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **-2**, spot = **NON INSEGUIRE / RIDUCI RISCHIO**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **ALTO**.
- **SOL**: Global = **+1**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **-2**, spot = **EVITA LONG / SOLO RIMBALZI VELOCI**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **-2**
- Confluenza: **DEBOLE / FRAGILE**
- Bias Global: **Fragile**
- Direzione decisionale: **LEGGERMENTE BEARISH**
- Azione spot dal Global: **NON INSEGUIRE / RIDUCI RISCHIO**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **ALTO**
- Conferme: Prima resistenza sopra 87.146; conferma del eve and adam bottom sopra 82.262.
- Invalidazioni: Sotto 80.337 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+1**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **HOLD LEGGERO / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: conferma del doppio minimo sopra 107,12; nuova conferma tecnica sopra 123,48.
- Invalidazioni: Allarmi sotto 96,23.

### DOGE

- Global Confluence: **-2**
- Confluenza: **DEBOLE / FRAGILE**
- Bias Global: **Fragile**
- Direzione decisionale: **LEGGERMENTE BEARISH**
- Azione spot dal Global: **EVITA LONG / SOLO RIMBALZI VELOCI**
- Long leva: **NO LONG A LEVA**
- Short leva: **SHORT SOLO DOPO SPIKE**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.10528 migliora; sopra 0.07997 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.07841 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 3; EMA200 circa 111,33 $; upside verso EMA200 +8,95%. Non autorizza leva e non aggiunge punti automatici.
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

Generato: 2026-10-15 05:34 UTC

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

Segnali totali salvati: **273**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-15 | BTC | 80.946,10 | -2 | +1 | +1 | 0 | -2 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-15 | DOGE | 0.07966 | -2 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-15 | SOL | 102,12 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-14 | BTC | 83.488,21 | 0 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-14 | DOGE | 0.08470 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-10-14 | SOL | 107,30 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-13 | BTC | 83.581,21 | +1 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-13 | DOGE | 0.08464 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-13 | SOL | 108,05 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-12 | BTC | 83.714,71 | -3 | -1 | -1 | 0 | -1 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-12 | DOGE | 0.08732 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-12 | SOL | 112,31 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 91 | 90 | 89 | 88 | 86 | 84 | 81 | 77 | 71 | 67 | 52 | 37 |
| SOL | 91 | 90 | 89 | 88 | 86 | 84 | 81 | 77 | 71 | 67 | 52 | 37 |
| DOGE | 91 | 90 | 89 | 88 | 86 | 84 | 81 | 77 | 71 | 67 | 52 | 37 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-17 | 60g | 2026-10-16 | domani |
| SOL | 2026-08-17 | 60g | 2026-10-16 | domani |
| DOGE | 2026-08-17 | 60g | 2026-10-16 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 80 | 52,50% | +0,30% | +0,29% | UTILE |
| BTC | 2g | 80 | 51,25% | +0,51% | +0,46% | UTILE |
| BTC | 3g | 79 | 46,84% | +0,64% | +0,64% | UTILE |
| BTC | 5g | 78 | 43,59% | +1,42% | +1,25% | UTILE |
| BTC | 7g | 78 | 51,28% | +2,07% | +1,93% | UTILE |
| BTC | 10g | 76 | 56,58% | +2,98% | +2,86% | UTILE |
| BTC | 14g | 72 | 62,50% | +4,67% | +4,62% | UTILE |
| BTC | 21g | 68 | 72,06% | +8,08% | +7,98% | UTILE |
| BTC | 30g | 64 | 95,31% | +12,11% | +11,44% | UTILE |
| BTC | 45g | 49 | 93,88% | +20,98% | +18,28% | PRIMA CALIBRAZIONE |
| BTC | 60g | 35 | 91,43% | +28,16% | +23,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | 82 | 46,34% | +0,13% | +0,06% | UTILE |
| SOL | 2g | 81 | 44,44% | +0,58% | +0,50% | UTILE |
| SOL | 3g | 80 | 48,75% | +1,04% | +0,93% | UTILE |
| SOL | 5g | 78 | 51,28% | +1,98% | +1,91% | UTILE |
| SOL | 7g | 76 | 56,58% | +3,02% | +3,09% | UTILE |
| SOL | 10g | 73 | 58,90% | +4,88% | +4,98% | UTILE |
| SOL | 14g | 69 | 68,12% | +7,89% | +8,41% | UTILE |
| SOL | 21g | 63 | 80,95% | +14,49% | +13,93% | UTILE |
| SOL | 30g | 60 | 83,33% | +19,64% | +16,34% | UTILE |
| SOL | 45g | 45 | 73,33% | +35,76% | +18,66% | PRIMA CALIBRAZIONE |
| SOL | 60g | 30 | 63,33% | +46,65% | +17,44% | PRIMA CALIBRAZIONE |
| DOGE | 1g | 82 | 48,78% | -0,01% | -0,03% | UTILE |
| DOGE | 2g | 81 | 44,44% | +0,22% | -0,10% | UTILE |
| DOGE | 3g | 80 | 41,25% | +0,52% | +0,16% | UTILE |
| DOGE | 5g | 79 | 46,84% | +1,13% | +0,33% | UTILE |
| DOGE | 7g | 78 | 50,00% | +1,66% | +0,52% | UTILE |
| DOGE | 10g | 75 | 41,33% | +2,40% | -0,13% | UTILE |
| DOGE | 14g | 73 | 52,05% | +4,02% | +2,20% | UTILE |
| DOGE | 21g | 67 | 58,21% | +7,75% | +1,97% | UTILE |
| DOGE | 30g | 63 | 68,25% | +10,90% | +4,91% | UTILE |
| DOGE | 45g | 48 | 45,83% | +20,69% | +4,08% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 35 | 42,86% | +26,15% | -1,20% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 80 | 52,50% | +0,30% | +0,29% | -0,28% | +0,82% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 88 | 48,86% | +0,19% | +0,25% | -0,34% | +0,70% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 88 | 48,86% | +0,19% | +0,25% | -0,34% | +0,70% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 83 | 46,99% | +0,21% | +0,04% | -0,28% | +0,73% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 35 | 42,86% | +0,53% | -0,02% | -0,31% | +1,07% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 80 | 51,25% | +0,51% | +0,46% | -0,27% | +1,20% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 87 | 51,72% | +0,48% | +0,56% | -0,26% | +1,16% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 87 | 51,72% | +0,48% | +0,56% | -0,26% | +1,16% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 82 | 46,34% | +0,47% | +0,05% | -0,17% | +1,14% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 35 | 42,86% | +0,85% | -0,11% | -0,05% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 79 | 46,84% | +0,64% | +0,64% | -1,28% | +2,43% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 86 | 50,00% | +0,80% | +0,87% | -1,32% | +2,49% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 86 | 50,00% | +0,80% | +0,87% | -1,32% | +2,49% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 81 | 39,51% | +0,82% | -0,14% | -1,25% | +2,52% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 35 | 37,14% | +1,31% | -0,55% | -1,15% | +3,03% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 78 | 43,59% | +1,42% | +1,25% | -1,91% | +3,84% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 84 | 47,62% | +1,57% | +1,60% | -1,90% | +3,94% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 84 | 47,62% | +1,57% | +1,60% | -1,90% | +3,94% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 79 | 41,77% | +1,44% | -0,71% | -1,86% | +3,88% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 34 | 35,29% | +3,06% | -2,33% | -1,68% | +5,50% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 78 | 51,28% | +2,07% | +1,93% | -2,28% | +4,92% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 82 | 57,32% | +2,29% | +2,36% | -2,25% | +5,04% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 82 | 57,32% | +2,29% | +2,36% | -2,25% | +5,04% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 77 | 42,86% | +2,25% | -1,06% | -2,22% | +5,01% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 34 | 32,35% | +4,23% | -3,81% | -2,10% | +7,38% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 76 | 56,58% | +2,98% | +2,86% | -2,57% | +6,12% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 79 | 65,82% | +3,17% | +3,31% | -2,48% | +6,29% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 79 | 65,82% | +3,17% | +3,31% | -2,48% | +6,29% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 74 | 45,95% | +3,14% | -0,45% | -2,49% | +6,33% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 33 | 36,36% | +4,54% | -4,21% | -2,21% | +8,23% | PRIMA CALIBRAZIONE |
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
| BTC | 30g | Global confluence | BENCHMARK | 64 | 95,31% | +12,11% | +11,44% | -3,00% | +16,32% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 67 | 92,54% | +12,09% | +12,09% | -2,97% | +16,41% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 67 | 92,54% | +12,09% | +12,09% | -2,97% | +16,41% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 62 | 66,13% | +12,05% | +1,30% | -2,85% | +16,53% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 26 | 61,54% | +12,81% | -2,34% | -2,66% | +17,23% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 49 | 93,88% | +20,98% | +18,28% | -2,55% | +25,79% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 52 | 100,00% | +21,33% | +21,33% | -2,55% | +26,03% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 52 | 100,00% | +21,33% | +21,33% | -2,55% | +26,03% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 47 | 53,19% | +21,37% | -2,00% | -2,34% | +26,10% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 20 | 60,00% | +15,88% | -5,83% | -2,18% | +21,66% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 35 | 91,43% | +28,16% | +23,87% | -2,74% | +33,44% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 37 | 100,00% | +27,96% | +27,96% | -2,79% | +33,29% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 37 | 100,00% | +27,96% | +27,96% | -2,79% | +33,29% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 33 | 100,00% | +28,61% | +28,61% | -2,58% | +34,15% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 32 | 37,50% | +28,34% | -7,95% | -2,53% | +33,87% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 7 | 0,00% | +32,68% | -32,68% | -1,07% | +38,39% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 82 | 48,78% | -0,01% | -0,03% | -0,80% | +1,04% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 89 | 58,43% | -0,06% | +0,46% | -0,89% | +0,93% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 89 | 58,43% | -0,06% | +0,46% | -0,89% | +0,93% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 83 | 50,60% | -0,15% | +0,20% | -1,00% | +0,84% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 50 | 40,00% | -0,06% | -0,58% | -1,00% | +0,64% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 81 | 44,44% | +0,22% | -0,10% | -0,95% | +1,57% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 88 | 57,95% | +0,03% | +0,75% | -1,08% | +1,32% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 88 | 57,95% | +0,03% | +0,75% | -1,08% | +1,32% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 82 | 53,66% | -0,27% | +0,17% | -1,39% | +1,02% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 50 | 44,00% | +0,08% | -1,04% | -1,17% | +1,03% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 80 | 41,25% | +0,52% | +0,16% | -2,55% | +3,71% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 87 | 56,32% | +0,19% | +1,09% | -2,75% | +3,38% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 87 | 56,32% | +0,19% | +1,09% | -2,75% | +3,38% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 81 | 45,68% | -0,41% | -0,06% | -3,00% | +2,74% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 49 | 34,69% | +0,31% | -1,86% | -2,85% | +3,50% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 79 | 46,84% | +1,13% | +0,33% | -3,70% | +5,98% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 85 | 54,12% | +0,82% | +1,60% | -3,91% | +5,70% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 85 | 54,12% | +0,82% | +1,60% | -3,91% | +5,70% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 79 | 50,63% | +0,05% | -0,88% | -4,30% | +4,99% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 47 | 36,17% | +1,56% | -4,28% | -3,91% | +6,43% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 78 | 50,00% | +1,66% | +0,52% | -4,37% | +7,84% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 83 | 59,04% | +1,48% | +2,03% | -4,59% | +7,59% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 83 | 59,04% | +1,48% | +2,03% | -4,59% | +7,59% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 77 | 44,16% | +0,53% | -1,32% | -5,05% | +6,65% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 45 | 28,89% | +2,80% | -6,15% | -4,47% | +8,62% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 75 | 41,33% | +2,40% | -0,13% | -5,03% | +9,93% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 80 | 56,25% | +2,00% | +1,86% | -5,24% | +9,63% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 80 | 56,25% | +2,00% | +1,86% | -5,24% | +9,63% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 74 | 43,24% | +0,74% | -2,27% | -5,78% | +8,22% | UTILE |
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
| DOGE | 30g | Global confluence | BENCHMARK | 63 | 68,25% | +10,90% | +4,91% | -5,62% | +25,54% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 66 | 69,70% | +11,19% | +7,00% | -5,59% | +25,99% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 66 | 69,70% | +11,19% | +7,00% | -5,59% | +25,99% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 60 | 58,33% | +9,77% | -2,39% | -6,33% | +23,90% | UTILE |
| DOGE | 30g | Classic technical | CALIBRABILE | 39 | 48,72% | +8,70% | -6,93% | -5,92% | +22,47% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 88,89% | +19,48% | +12,44% | -5,48% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 48 | 45,83% | +20,69% | +4,08% | -4,71% | +38,32% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 51 | 62,75% | +20,25% | +8,08% | -4,73% | +38,14% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 51 | 62,75% | +20,25% | +8,08% | -4,73% | +38,14% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 45 | 11,11% | +17,26% | -13,13% | -5,59% | +36,00% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 31 | 3,23% | +21,52% | -22,01% | -5,10% | +38,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +21,73% | +11,03% | -4,45% | +35,73% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 35 | 42,86% | +26,15% | -1,20% | -4,03% | +44,93% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 37 | 56,76% | +26,59% | +8,95% | -4,05% | +45,07% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 37 | 56,76% | +26,59% | +8,95% | -4,05% | +45,07% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +25,85% | +11,72% | -4,07% | +44,87% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 32 | 6,25% | +26,71% | -24,52% | -4,51% | +44,17% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 24 | 0,00% | +24,90% | -24,90% | -4,47% | +43,41% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +38,20% | +19,48% | -1,31% | +51,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 82 | 46,34% | +0,13% | +0,06% | -0,65% | +1,00% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 84 | 53,57% | +0,12% | +0,40% | -0,74% | +0,98% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 87 | 52,87% | +0,16% | +0,34% | -0,71% | +1,01% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 82 | 46,34% | +0,11% | -0,05% | -0,80% | +0,95% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 58 | 44,83% | +0,45% | -0,03% | -0,53% | +1,39% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 81 | 44,44% | +0,58% | +0,50% | -0,66% | +1,64% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 83 | 49,40% | +0,49% | +0,68% | -0,87% | +1,41% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 86 | 48,84% | +0,48% | +0,64% | -0,84% | +1,46% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 81 | 44,44% | +0,31% | -0,05% | -0,84% | +1,42% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 58 | 48,28% | +0,59% | +0,18% | -0,66% | +1,66% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 80 | 48,75% | +1,04% | +0,93% | -2,22% | +3,64% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 82 | 52,44% | +0,89% | +1,25% | -2,35% | +3,47% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 85 | 51,76% | +0,87% | +1,19% | -2,31% | +3,47% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 80 | 43,75% | +0,49% | -0,38% | -2,38% | +3,05% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 58 | 46,55% | +0,60% | +0,10% | -2,28% | +3,11% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 78 | 51,28% | +1,98% | +1,91% | -3,12% | +5,79% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 80 | 55,00% | +1,78% | +2,17% | -3,24% | +5,59% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 83 | 54,22% | +1,74% | +2,07% | -3,20% | +5,53% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 78 | 43,59% | +1,38% | -1,00% | -3,30% | +5,04% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 58 | 48,28% | +0,68% | +0,02% | -3,30% | +4,39% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 76 | 56,58% | +3,02% | +3,09% | -3,69% | +7,46% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 78 | 64,10% | +2,77% | +3,59% | -3,82% | +7,23% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 81 | 64,20% | +2,67% | +3,46% | -3,78% | +7,11% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 76 | 38,16% | +1,81% | -1,96% | -3,91% | +6,35% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 57 | 43,86% | +0,46% | -0,12% | -4,03% | +5,07% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 73 | 58,90% | +4,88% | +4,98% | -4,00% | +9,76% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 75 | 69,33% | +4,70% | +5,72% | -4,15% | +9,38% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 78 | 67,95% | +4,52% | +5,51% | -4,12% | +9,17% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 73 | 42,47% | +3,07% | -2,12% | -4,32% | +8,03% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 55 | 45,45% | +0,57% | -0,14% | -4,63% | +6,00% | PRIMA CALIBRAZIONE |

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

Generato: 2026-10-15 05:34 UTC

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
| BTC | 91 | UTILE | 88 | 28 | 18 | 0 | Famiglia statistica | 1g | 48,86% | +0,25% | campione utile, valutare con prudenza |
| SOL | 91 | UTILE | 84 | 32 | 18 | 0 | Famiglia statistica | 1g | 53,57% | +0,40% | campione utile, valutare con prudenza |
| DOGE | 91 | UTILE | 89 | 32 | 18 | 0 | Famiglia statistica | 1g | 58,43% | +0,46% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 35 | 42,86% | -0,02% | +0,53% | -0,31% | +1,07% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 88 | 48,86% | +0,25% | +0,19% | -0,34% | +0,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 83 | 46,99% | +0,04% | +0,21% | -0,28% | +0,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 35 | 42,86% | -0,11% | +0,85% | -0,05% | +1,57% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 87 | 51,72% | +0,56% | +0,48% | -0,26% | +1,16% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 82 | 46,34% | +0,05% | +0,47% | -0,17% | +1,14% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 35 | 37,14% | -0,55% | +1,31% | -1,15% | +3,03% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Famiglia statistica | 86 | 50,00% | +0,87% | +0,80% | -1,32% | +2,49% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 81 | 39,51% | -0,14% | +0,82% | -1,25% | +2,52% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 34 | 35,29% | -2,33% | +3,06% | -1,68% | +5,50% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 84 | 47,62% | +1,60% | +1,57% | -1,90% | +3,94% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 79 | 41,77% | -0,71% | +1,44% | -1,86% | +3,88% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 34 | 32,35% | -3,81% | +4,23% | -2,10% | +7,38% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 82 | 57,32% | +2,36% | +2,29% | -2,25% | +5,04% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 77 | 42,86% | -1,06% | +2,25% | -2,22% | +5,01% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 33 | 36,36% | -4,21% | +4,54% | -2,21% | +8,23% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 79 | 65,82% | +3,31% | +3,17% | -2,48% | +6,29% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | -1,47% | -1,47% | -4,23% | +1,69% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 74 | 45,95% | -0,45% | +3,14% | -2,49% | +6,33% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 29 | 24,14% | -4,15% | +5,09% | -1,91% | +9,57% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 76 | 60,53% | +4,69% | +4,65% | -2,68% | +8,37% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 7 | 42,86% | -0,11% | -0,11% | -4,30% | +2,85% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 70 | 57,14% | +1,37% | +4,83% | -2,65% | +8,60% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 29 | 44,83% | -4,88% | +8,60% | -2,40% | +12,46% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 71 | 76,06% | +8,03% | +8,03% | -2,89% | +11,92% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 64 | 56,25% | +1,36% | +8,48% | -2,86% | +12,38% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 26 | 61,54% | -2,34% | +12,81% | -2,66% | +17,23% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 67 | 92,54% | +12,09% | +12,09% | -2,97% | +16,41% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 62 | 66,13% | +1,30% | +12,05% | -2,85% | +16,53% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Classic technical | 20 | 60,00% | -5,83% | +15,88% | -2,18% | +21,66% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 52 | 100,00% | +21,33% | +21,33% | -2,55% | +26,03% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 47 | 53,19% | -2,00% | +21,37% | -2,34% | +26,10% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 7 | 0,00% | -32,68% | +32,68% | -1,07% | +38,39% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 37 | 100,00% | +27,96% | +27,96% | -2,79% | +33,29% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 32 | 37,50% | -7,95% | +28,34% | -2,53% | +33,87% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Classic technical | 50 | 40,00% | -0,58% | -0,06% | -1,00% | +0,64% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 89 | 58,43% | +0,46% | -0,06% | -0,89% | +0,93% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 11 | 63,64% | +2,53% | +2,82% | +0,75% | +3,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 83 | 50,60% | +0,20% | -0,15% | -1,00% | +0,84% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 50 | 44,00% | -1,04% | +0,08% | -1,17% | +1,03% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 88 | 57,95% | +0,75% | +0,03% | -1,08% | +1,32% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 11 | 45,45% | +2,65% | +2,89% | +1,08% | +5,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 82 | 53,66% | +0,17% | -0,27% | -1,39% | +1,02% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 49 | 34,69% | -1,86% | +0,31% | -2,85% | +3,50% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 87 | 56,32% | +1,09% | +0,19% | -2,75% | +3,38% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 11 | 54,55% | +2,62% | +2,81% | -1,35% | +6,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 81 | 45,68% | -0,06% | -0,41% | -3,00% | +2,74% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 47 | 36,17% | -4,28% | +1,56% | -3,91% | +6,43% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 85 | 54,12% | +1,60% | +0,82% | -3,91% | +5,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 11 | 36,36% | +2,02% | +2,17% | -2,50% | +9,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 79 | 50,63% | -0,88% | +0,05% | -4,30% | +4,99% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 45 | 28,89% | -6,15% | +2,80% | -4,47% | +8,62% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 83 | 59,04% | +2,03% | +1,48% | -4,59% | +7,59% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 11 | 45,45% | +0,78% | +0,88% | -3,00% | +9,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 77 | 44,16% | -1,32% | +0,53% | -5,05% | +6,65% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 44 | 29,55% | -7,10% | +3,40% | -5,16% | +10,81% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 80 | 56,25% | +1,86% | +2,00% | -5,24% | +9,63% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 74 | 43,24% | -2,27% | +0,74% | -5,78% | +8,22% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 43 | 39,53% | -5,45% | +4,51% | -5,57% | +13,12% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 76 | 64,47% | +3,35% | +3,72% | -5,75% | +12,99% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 11 | 45,45% | +2,03% | +5,60% | -4,35% | +14,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 70 | 45,71% | -1,78% | +1,76% | -6,36% | +10,51% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 42 | 42,86% | -7,44% | +5,67% | -5,73% | +16,02% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 70 | 58,57% | +4,53% | +8,09% | -5,59% | +19,19% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 11 | 63,64% | -0,04% | +4,84% | -5,47% | +18,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 64 | 54,69% | -2,39% | +6,13% | -6,26% | +16,39% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Classic technical | 39 | 48,72% | -6,93% | +8,70% | -5,92% | +22,47% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 66 | 69,70% | +7,00% | +11,19% | -5,59% | +25,99% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 9 | 88,89% | +12,44% | +19,48% | -5,48% | +30,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 60 | 58,33% | -2,39% | +9,77% | -6,33% | +23,90% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 45g | MEDIO | Classic technical | 31 | 3,23% | -22,01% | +21,52% | -5,10% | +38,53% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Famiglia statistica | 51 | 62,75% | +8,08% | +20,25% | -4,73% | +38,14% | PESO OK | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 8 | 62,50% | +11,03% | +21,73% | -4,45% | +35,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 45 | 11,11% | -13,13% | +17,26% | -5,59% | +36,00% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 24 | 0,00% | -24,90% | +24,90% | -4,47% | +43,41% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 37 | 56,76% | +8,95% | +26,59% | -4,05% | +45,07% | PESO OK | 0,0 | MEDIA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 4 | 75,00% | +19,48% | +38,20% | -1,31% | +51,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 32 | 6,25% | -24,52% | +26,71% | -4,51% | +44,17% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 1g | BREVE | Classic technical | 58 | 44,83% | -0,03% | +0,45% | -0,53% | +1,39% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 84 | 53,57% | +0,40% | +0,12% | -0,74% | +0,98% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 82 | 46,34% | -0,05% | +0,11% | -0,80% | +0,95% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 58 | 48,28% | +0,18% | +0,59% | -0,66% | +1,66% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 83 | 49,40% | +0,68% | +0,49% | -0,87% | +1,41% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 81 | 44,44% | -0,05% | +0,31% | -0,84% | +1,42% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 58 | 46,55% | +0,10% | +0,60% | -2,28% | +3,11% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 82 | 52,44% | +1,25% | +0,89% | -2,35% | +3,47% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 80 | 43,75% | -0,38% | +0,49% | -2,38% | +3,05% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 58 | 48,28% | +0,02% | +0,68% | -3,30% | +4,39% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 80 | 55,00% | +2,17% | +1,78% | -3,24% | +5,59% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 78 | 43,59% | -1,00% | +1,38% | -3,30% | +5,04% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 57 | 43,86% | -0,12% | +0,46% | -4,03% | +5,07% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 78 | 64,10% | +3,59% | +2,77% | -3,82% | +7,23% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 76 | 38,16% | -1,96% | +1,81% | -3,91% | +6,35% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 55 | 45,45% | -0,14% | +0,57% | -4,63% | +6,00% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 75 | 69,33% | +5,72% | +4,70% | -4,15% | +9,38% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 73 | 42,47% | -2,12% | +3,07% | -4,32% | +8,03% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
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
| SOL | 30g | MEDIO | Famiglia statistica | 62 | 90,32% | +19,07% | +21,56% | -4,40% | +28,81% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 60 | 45,00% | -7,68% | +20,40% | -4,74% | +26,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 45g | MEDIO | Classic technical | 33 | 33,33% | -18,74% | +30,66% | -4,13% | +41,08% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Famiglia statistica | 47 | 74,47% | +21,94% | +35,86% | -3,89% | +44,64% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +28,91% | +28,91% | -3,55% | +37,55% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 49 | 30,61% | -22,62% | +34,67% | -4,33% | +43,52% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 21 | 0,00% | -53,73% | +53,73% | -4,64% | +60,15% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 33 | 75,76% | +33,17% | +49,71% | -4,58% | +59,01% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +47,10% | +47,10% | -5,94% | +54,98% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 35 | 11,43% | -40,53% | +48,28% | -4,98% | +57,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 82 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 89 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 105 | 40,95% | -0,23% |
| BTC | BREVE | Famiglia statistica | 261 | 50,19% | +0,56% |
| BTC | BREVE | Microstruttura exchange | 27 | 37,04% | -0,30% |
| BTC | BREVE | Tecnico | 246 | 44,31% | -0,02% |
| BTC | SETTIMANALE | Classic technical | 101 | 34,65% | -3,44% |
| BTC | SETTIMANALE | Famiglia statistica | 245 | 56,73% | +2,41% |
| BTC | SETTIMANALE | Microstruttura exchange | 24 | 25,00% | -1,73% |
| BTC | SETTIMANALE | Tecnico | 230 | 43,48% | -0,74% |
| BTC | SWING | Classic technical | 58 | 34,48% | -4,52% |
| BTC | SWING | Famiglia statistica | 147 | 68,03% | +6,30% |
| BTC | SWING | Microstruttura exchange | 14 | 50,00% | +0,11% |
| BTC | SWING | Tecnico | 134 | 56,72% | +1,36% |
| BTC | MEDIO | Classic technical | 53 | 52,83% | -7,66% |
| BTC | MEDIO | Famiglia statistica | 156 | 96,79% | +18,94% |
| BTC | MEDIO | Microstruttura exchange | 9 | 100,00% | +9,68% |
| BTC | MEDIO | Tecnico | 141 | 55,32% | -1,90% |
| DOGE | BREVE | Classic technical | 149 | 39,60% | -1,15% |
| DOGE | BREVE | Famiglia statistica | 264 | 57,58% | +0,76% |
| DOGE | BREVE | Microstruttura exchange | 33 | 54,55% | +2,60% |
| DOGE | BREVE | Tecnico | 246 | 50,00% | +0,10% |
| DOGE | SETTIMANALE | Classic technical | 136 | 31,62% | -5,81% |
| DOGE | SETTIMANALE | Famiglia statistica | 248 | 56,45% | +1,83% |
| DOGE | SETTIMANALE | Microstruttura exchange | 33 | 45,45% | +1,16% |
| DOGE | SETTIMANALE | Tecnico | 230 | 46,09% | -1,47% |
| DOGE | SWING | Classic technical | 85 | 41,18% | -6,43% |
| DOGE | SWING | Famiglia statistica | 146 | 61,64% | +3,92% |
| DOGE | SWING | Microstruttura exchange | 22 | 54,55% | +0,99% |
| DOGE | SWING | Tecnico | 134 | 50,00% | -2,07% |
| DOGE | MEDIO | Classic technical | 94 | 21,28% | -16,49% |
| DOGE | MEDIO | Famiglia statistica | 154 | 64,29% | +7,83% |
| DOGE | MEDIO | Microstruttura exchange | 21 | 76,19% | +13,25% |
| DOGE | MEDIO | Tecnico | 137 | 30,66% | -11,08% |
| SOL | BREVE | Classic technical | 174 | 46,55% | +0,08% |
| SOL | BREVE | Famiglia statistica | 249 | 51,81% | +0,77% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 243 | 44,86% | -0,16% |
| SOL | SETTIMANALE | Classic technical | 170 | 45,88% | -0,08% |
| SOL | SETTIMANALE | Famiglia statistica | 233 | 62,66% | +3,79% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 227 | 41,41% | -1,68% |
| SOL | SWING | Classic technical | 96 | 52,08% | -0,21% |
| SOL | SWING | Famiglia statistica | 137 | 79,56% | +11,44% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 132 | 46,21% | -3,86% |
| SOL | MEDIO | Classic technical | 96 | 35,42% | -20,07% |
| SOL | MEDIO | Famiglia statistica | 142 | 81,69% | +23,30% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 12 | 100,00% | +28,96% |
| SOL | MEDIO | Tecnico | 144 | 31,94% | -20,75% |

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

Generato: 2026-10-15 05:34 UTC

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
| BTC | -2 | DEBOLE / FRAGILE | Fragile | BASSA / RACCOLTA DATI | NON INSEGUIRE / RIDUCI RISCHIO | Prima resistenza sopra 87.146; conferma del eve and adam bottom sopra 82.262. | Sotto 80.337 il quadro tecnico peggiora. |
| SOL | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | conferma del doppio minimo sopra 107,12; nuova conferma tecnica sopra 123,48. | Allarmi sotto 96,23. |
| DOGE | -2 | DEBOLE / FRAGILE | Fragile | BASSA / RACCOLTA DATI | EVITA LONG / SOLO RIMBALZI VELOCI | Sopra 0.10528 migliora; sopra 0.07997 viene invalidato il pattern ribassista dominante. | Sotto 0.07841 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | 0 | +1 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -2 |
| SOL | +3 | 0 | +3 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +1 |
| DOGE | +3 | 0 | +3 | 0 | -3 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | -2 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **DEBOLE / FRAGILE**
- Bias: **Fragile**
- Punteggio finale: **-2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **NON INSEGUIRE / RIDUCI RISCHIO**

BTC si è indebolito. In questo caso conta più proteggere il rischio che inseguire un recupero non confermato.

Dettaglio moduli:

- Famiglia statistica: **+1** — Scanner grezzo +1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+1** — Casi positivi 52,50%, return centrale 30g +4,51%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 89. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -5/12, verdetto debole, trend misto, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score -1 (rialzista Eve and Adam Bottom / MATURO; ribassista Doppio massimo / CONFERMATO RECENTE). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -8/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff DISTRIBUZIONE POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Fractal path: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- RSI top-cycle: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati -1.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — BTC: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: Prima resistenza sopra 87.146; conferma del eve and adam bottom sopra 82.262.

Invalidazioni: Sotto 80.337 il quadro tecnico peggiora.

### SOL

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**

SOL è ancora in zona mista. Il frattale resta soltanto uno scenario contestuale: non è confermato dal prezzo e vale 0 punti operativi finché il gap non rientra. Meglio evitare leva e ragionare solo a tranche piccole.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 2. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 77,50%, return centrale 30g +10,41%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 2, positivi 30g 50,00%, return p50 -6,98%.
- Scanner path: **0** — Controlli disponibili 89. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -4/12, verdetto debole, trend misto, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Triplo massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -6/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff RANGE / FASE NON CHIARA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Fractal path: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- RSI top-cycle: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 3, bias SQUEEZE SETUP MODERATO, EMA200 111,33 $, upside EMA200 +8,95%, gap EMA50/EMA200 -4,50%, hit EMA200 12w +76,67%, trend MIGLIORAMENTO. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +2.00, derivati +0.50, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — SOL: cambiamento medio in miglioramento rispetto a ieri.

Conferme: conferma del doppio minimo sopra 107,12; nuova conferma tecnica sopra 123,48.

Invalidazioni: Allarmi sotto 96,23.

### DOGE

- Confluenza: **DEBOLE / FRAGILE**
- Bias: **Fragile**
- Punteggio finale: **-2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **EVITA LONG / SOLO RIMBALZI VELOCI**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 2. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 77,50%, return centrale 30g +14,16%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 2, positivi 30g 50,00%, return p50 +0,73%.
- Scanner path: **0** — Controlli disponibili 89. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-3** — Score tecnico -8/12, verdetto ribassista tecnico, trend ribassista, struttura volatilità in espansione, divergenza nessuna, Wyckoff range / fase non chiara, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -11/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Fractal path: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- RSI top-cycle: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +0.75, derivati +0.50, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — DOGE: cambiamento medio in peggioramento rispetto a ieri.

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

Generato: 2026-10-15 05:34 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 80.946 $ | prezzo corrente |
| Power Law centrale | 126.823 $ | deviazione -36,17% |
| Banda p10-p90 | 79.127 $ / 320.487 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 12,06% | posizione storica nel corridoio |
| Esponente β | 5,7829 | R² log-log 91,94% |
| Stabilità β | BASSA | range 1,3154 cambiando finestra |
| Ultimo halving | 2024-04-19 | 909 giorni fa |
| Fase ciclo | 62,22% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-10-15 (4411 osservazioni)
- Formula stimata: prezzo ≈ exp(-38.8899) × giorni^5.7829
- Prezzo centrale oggi: **126.823 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 12,06%
- Scarto dal centro: **-36,17%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,7829 | 91,94% |
| 2015 | 5,8625 | 91,49% |
| 2016 | 5,5442 | 87,78% |
| 2017 | 4,8209 | 83,07% |
| 2018 | 4,5470 | 78,67% |

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
| 2012-11-28 → 2016-07-09 | 2015-02-27 | -4,38% | -6,47% | -11,03% | +70,40% |
| 2016-07-09 → 2020-05-11 | 2018-11-28 | -7,83% | -9,47% | +106,83% | +75,30% |
| 2020-05-11 → 2024-04-19 | 2022-10-23 | -17,26% | +16,41% | +39,40% | +69,09% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | 2 | 0 | -3.737606785086478 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -6 | -1 | -8.023851184625808 | 0 |

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

Generato: 2026-10-15 05:33 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00126200 | +2 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | -3,74% | RIBASSISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000098 | -6 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -8,02% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

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
- **Rendimenti relativi:** 7g -9,60%; 30g -3,74%; 90g +6,95%; 180g +9,55%
- **Daily:** RSI 30.34; MA50 0.00134612; MA200 0.00120138
- **Weekly:** MA30 0.00120590; RSI 49.08
- **Livelli:** supporto 0.00117400; resistenza 0.00129400; breakout 60g 0.00146600; breakdown 60g 0.00117400
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00133900; target 0.00140150
- **Fibonacci:** VICINO — 50.0% a 0.00123750
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in salita; struttura con massimi/minimi crescenti; RSI relativo debole; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-6)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g -7,89%; 30g -8,02%; 90g -13,22%; 180g -23,75%
- **Daily:** RSI 30.81; MA50 0.00000109; MA200 0.00000121
- **Weekly:** MA30 0.00000121; RSI 35.13
- **Livelli:** supporto 0.00000097; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000097
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000109
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
| DOGE | 90g | 291 | 54,64% | +6,92% | -9,23% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 52 | 48,08% | -0,01% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 52 | 44,23% | +0,06% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 51 | 37,25% | -0,64% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 44 | 40,91% | -0,58% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 35 | 57,14% | -0,22% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 64 | 68,75% | +0,23% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 62 | 62,90% | +0,40% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 58 | 56,90% | -0,06% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 54 | 50,00% | -0,66% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 52 | 55,77% | +0,17% | LOCKED / RACCOLTA LIVE | 0 |

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

| Voce                      | Valore                                            |
|:--------------------------|:--------------------------------------------------|
| Lifecycle squeeze score | 3 |
| Bias | SQUEEZE SETUP MODERATO |
| Azione coerente | CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO |
| Peso suggerito Global | 0 |
| Trend squeeze | MIGLIORAMENTO |
| Trend squeeze score | 1 |
| Confronto precedente | 2026-10-12 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 102,21 $ |
| EMA200 weekly target | 111,33 $ |
| Upside verso EMA200 | +8,95% |
| Distanza prezzo da EMA200 | -8,21% |
| Gap EMA50/EMA200 | -4,50% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 52,40 |
| Età SOL | 6,5 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +76,67% |
| Max gain mediano 12w | +36,63% |
| Drawdown mediano 12w | -30,75% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **MIGLIORAMENTO**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-10-15 05:33 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-10-15 05:30:22 UTC**

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
- DOGE: cambiamento importante in peggioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | NESSUN CAMBIAMENTO FORTE | miglioramento | NEUTRALE / INCERTO | +52.50% | 0.00 punti |
| SOL | CAMBIAMENTO MEDIO | miglioramento | RIALZISTA | +77.50% | +2.50 punti |
| DOGE | CAMBIAMENTO MEDIO | peggioramento | RIALZISTA | +77.50% | -7.50 punti |

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
| BTC | 76.945 $ | 89.094 $ | +32,14% | +15,79% | rimbalzo poco frequente | 89.094 $ | 76.945 $ | +24,00% | -13,64% | spike storicamente più resistente |
| SOL | 97,10 $ | 112,43 $ | +33,33% | +15,79% | rimbalzo poco frequente | 112,43 $ | 97,10 $ | +25,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07581 $ | 0,08778 $ | +31,25% | +15,79% | rimbalzo poco frequente | 0,08778 $ | 0,07581 $ | +14,71% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +32,14% (9/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 6 poi sono scaricati a -5,00%. Percentuale: +24,00% (6/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 21 prima sono scesi a -5,00%. Tra quei 21, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +33,33% (7/21). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 32 prima sono saliti a +10,00%. Tra quei 32, 8 poi sono scaricati a -5,00%. Percentuale: +25,00% (8/32). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 16 prima sono scesi a -5,00%. Tra quei 16, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +31,25% (5/16). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 34 prima sono saliti a +10,00%. Tra quei 34, 5 poi sono scaricati a -5,00%. Percentuale: +14,71% (5/34). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-10-15 05:32:57 UTC

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-10-15 | 2026-10-15T05:30:21Z | 2026-10-15 05:30:22 |
| SOL | 2026-10-15 | 2026-10-15T05:30:21Z | 2026-10-15 05:30:22 |
| DOGE | 2026-10-15 | 2026-10-15T05:30:21Z | 2026-10-15 05:30:22 |

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
| BTC | 2026-10-15 | 80.995 $ | INCERTO | 52,50% | 60.629,42 $ | 67.052,08 $ | 84.647,98 $ | 92.877,95 $ | 105.608,34 $ |
| SOL | 2026-10-15 | 102,21 $ | SALITA | 77,50% | 90,68 $ | 104,66 $ | 112,85 $ | 122,06 $ | 138,62 $ |
| DOGE | 2026-10-15 | 0.07980 $ | SALITA | 77,50% | 0.07433 $ | 0.08296 $ | 0.09110 $ | 0.09735 $ | 0.10697 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | AVAILABLE | SAME_BTC_REGIME | 0 | 0 | 6 | 6 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 84.647,98 $ | 86.046,41 $ | 105.608,34 $ | 123.561,49 $ |
| SOL | AVAILABLE | SAME_BTC_REGIME | 2 | 2 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 112,85 $ | 108,30 $ | 138,62 $ | 139,61 $ |
| DOGE | AVAILABLE | SAME_BTC_REGIME | 2 | 3 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.09110 $ | 0.08478 $ | 0.10697 $ | 0.11658 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-09-15**; verificato fino al **2026-10-15**; stato **COMPLETO 30/30g**.
- Reale **80.925,56 $**; p50 previsto **96.378,73 $**; scarto **-16,03%**.
- Errore medio assoluto **6,26%**; massimo **16,03%**; DENTRO p10-p90; FUORI p25-p75.

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

**Campione corrente:** 7 episodi qualificati su 40 · 7 asset distinti.

**SMALL SAMPLE / DIAGNOSTIC ONLY:** le frequenze empiriche non sono probabilità calibrate.

![SOL conditional successor corrente](scanner_forecast_SOL_conditional_successor_current.png)

###### Confronto diretto a 30 giorni

| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Cono standard | 2026-10-15 | 40 | 2026-11-14 | 90.68 $ | 104.66 $ | 112.85 $ | 122.06 $ | 138.62 $ |
| Conditional corrente | 2026-10-15 | 7 | 2026-11-14 | 79.26 $ | 96.14 $ | 108.18 $ | 176.54 $ | 247.80 $ |

###### Struttura successiva dei casi correnti

| Classe | Episodi | Frequenza empirica |
| --- | ---: | ---: |
| DIRECT_CONTINUATION | 2 | 28.57% |
| SHALLOW_PULLBACK_THEN_CONTINUATION | 4 | 57.14% |
| DEEP_PULLBACK_THEN_RECOVERY | 0 | 0.00% |
| FAILURE | 1 | 14.29% |
| UNRESOLVED | 0 | 0.00% |

###### Episodi qualificati oggi

| Asset | Match window | -5% hit | +10% anchor | Classe 60d |
| --- | --- | --- | --- | --- |
| XTZ-USD | 2019-09-24 → 2020-01-01 | 2020-01-02 | 2020-01-20 | SHALLOW_PULLBACK_THEN_CONTINUATION |
| HBAR-USD | 2022-11-29 → 2023-03-08 | 2023-03-09 | 2023-03-29 | FAILURE |
| RUNE-USD | 2023-07-01 → 2023-10-08 | 2023-10-09 | 2023-10-23 | DIRECT_CONTINUATION |
| VET-USD | 2020-04-23 → 2020-07-31 | 2020-08-02 | 2020-08-06 | SHALLOW_PULLBACK_THEN_CONTINUATION |
| ZIL-USD | 2022-11-29 → 2023-03-08 | 2023-03-09 | 2023-03-14 | SHALLOW_PULLBACK_THEN_CONTINUATION |
| ETC-USD | 2023-09-18 → 2023-12-26 | 2024-01-07 | 2024-01-10 | DIRECT_CONTINUATION |
| LINK-USD | 2020-11-27 → 2021-03-06 | 2021-03-24 | 2021-04-02 | SHALLOW_PULLBACK_THEN_CONTINUATION |

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

- Ultimo close disponibile: **2026-10-15** · SOL **102.06 $**.
- Giorno del vintage: **27/30**.
- P50 condizionato previsto per quel giorno: **179.83 $**.
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

- Cono congelato il **2026-09-15**; verificato fino al **2026-10-15**; stato **COMPLETO 30/30g**.
- Reale **102,06 $**; p50 previsto **126,68 $**; scarto **-19,43%**.
- Errore medio assoluto **8,87%**; massimo **23,00%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted SOL](scanner_forecast_SOL_regime_adjusted.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-09-15**; verificato fino al **2026-10-15**; stato **COMPLETO 30/30g**.
- Reale **0.07962 $**; p50 previsto **0.07589 $**; scarto **4,92%**.
- Errore medio assoluto **13,95%**; massimo **26,43%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted DOGE](scanner_forecast_DOGE_regime_adjusted.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 89 | 94,38% | 70,79% | 1,83% | 0,34% |
| BTC | 3g | 85 | 94,12% | 78,82% | 3,09% | 0,59% |
| BTC | 7g | 77 | 93,51% | 71,43% | 4,83% | 1,20% |
| BTC | 14g | 63 | 98,41% | 76,19% | 5,62% | 0,97% |
| BTC | 30g | 38 | 100,00% | 71,05% | 11,72% | -3,97% |
| SOL | 1g | 89 | 85,39% | 62,92% | 2,65% | 0,53% |
| SOL | 3g | 85 | 91,76% | 71,76% | 3,82% | 1,39% |
| SOL | 7g | 77 | 92,21% | 75,32% | 5,79% | 2,45% |
| SOL | 14g | 63 | 88,89% | 79,37% | 7,83% | 5,27% |
| SOL | 30g | 38 | 94,74% | 68,42% | 14,81% | 5,42% |
| DOGE | 1g | 89 | 88,76% | 60,67% | 2,99% | 0,25% |
| DOGE | 3g | 85 | 92,94% | 63,53% | 4,53% | 1,14% |
| DOGE | 7g | 77 | 77,92% | 75,32% | 8,32% | 4,44% |
| DOGE | 14g | 63 | 85,71% | 53,97% | 10,02% | 8,28% |
| DOGE | 30g | 38 | 94,74% | 39,47% | 16,49% | 16,49% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
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
- Prezzo attuale: **80.994,83 $**
- Return normale fra 30 giorni: **84.647,98 $** (4,51%)
- Drawdown normale durante il mese: **72.859,92 $** (-10,04%)
- Drawdown brutto da rispettare: **63.942,98 $** (-21,05%)
- Max gain normale durante il mese: **91.915,71 $** (13,48%)
- Max gain buono / take profit ottimistico: **101.230,12 $** (24,98%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **77,50%**
- Casi negativi / discesa storica: **22,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **102,21 $**
- Return normale fra 30 giorni: **112,85 $** (10,41%)
- Drawdown normale durante il mese: **96,65 $** (-5,44%)
- Drawdown brutto da rispettare: **92,22 $** (-9,77%)
- Max gain normale durante il mese: **120,01 $** (17,41%)
- Max gain buono / take profit ottimistico: **131,46 $** (28,62%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **77,50%**
- Casi negativi / discesa storica: **22,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,08 $**
- Return normale fra 30 giorni: **0,09 $** (14,16%)
- Drawdown normale durante il mese: **0,08 $** (-3,15%)
- Drawdown brutto da rispettare: **0,07 $** (-9,54%)
- Max gain normale durante il mese: **0,10 $** (19,89%)
- Max gain buono / take profit ottimistico: **0,10 $** (30,66%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 80.994,83 $

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

- Se va molto male: **60.629,42 $** (-25,14%)
- Se va male: **67.052,08 $** (-17,21%)
- Scenario normale: **84.647,98 $** (4,51%)
- Se va bene: **92.877,95 $** (14,67%)
- Se va molto bene: **105.608,34 $** (30,39%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **72.859,92 $** (-10,04%)
- Discesa brutta: **63.942,98 $** (-21,05%)
- Discesa molto brutta: **58.841,94 $** (-27,35%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **91.915,71 $** (13,48%)
- Rialzo buono: **101.230,12 $** (24,98%)
- Rialzo molto forte: **114.941,06 $** (41,91%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **72.859,92 $** e uno spike normale intorno a **91.915,71 $**.

La chiusura a 30 giorni è incerta: salita 52,50%, discesa 47,50%. Non c'è un vantaggio netto.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 102,21 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **77,50%**
- Probabilità storica di discesa: **22,50%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **90,68 $** (-11,28%)
- Se va male: **104,66 $** (2,40%)
- Scenario normale: **112,85 $** (10,41%)
- Se va bene: **122,06 $** (19,42%)
- Se va molto bene: **138,62 $** (35,62%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **96,65 $** (-5,44%)
- Discesa brutta: **92,22 $** (-9,77%)
- Discesa molto brutta: **80,52 $** (-21,22%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **120,01 $** (17,41%)
- Rialzo buono: **131,46 $** (28,62%)
- Rialzo molto forte: **146,11 $** (42,95%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **96,65 $** e uno spike normale intorno a **120,01 $**.

La chiusura a 30 giorni era più spesso positiva: salita 77,50%, discesa 22,50%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 0,08 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **77,50%**
- Probabilità storica di discesa: **22,50%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,07 $** (-6,85%)
- Se va male: **0,08 $** (3,96%)
- Scenario normale: **0,09 $** (14,16%)
- Se va bene: **0,10 $** (22,00%)
- Se va molto bene: **0,11 $** (34,05%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,08 $** (-3,15%)
- Discesa brutta: **0,07 $** (-9,54%)
- Discesa molto brutta: **0,07 $** (-16,84%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,10 $** (19,89%)
- Rialzo buono: **0,10 $** (30,66%)
- Rialzo molto forte: **0,12 $** (44,33%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,08 $** e uno spike normale intorno a **0,10 $**.

La chiusura a 30 giorni era più spesso positiva: salita 77,50%, discesa 22,50%. Quindi la lettura principale è favorevole.

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

- Previsioni già controllate: **45**
- Direzione corretta: **92,11%**
- Errore medio dello scenario centrale: **10,14%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **2,22%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **45**
- Direzione corretta: **74,36%**
- Errore medio dello scenario centrale: **15,21%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **26,67%**
- Prezzo finale dentro lo scenario 10%-90%: **95,56%**

### Solana

- Previsioni già controllate: **45**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **12,80%**
- Zona rischio toccata: **4,44%**
- Zona rialzo media toccata: **24,44%**
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

- Previsioni controllate: **45**
- Previsioni usate per la calibrazione recente: **45**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **92,11%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **INCERTO**
- Direzione calibrata oggi: **INCERTO**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **4,51%** → **84.647,98 $**
- Correzione imparata dagli errori: **-3,61%**
- Calibrato: **0,90%** → **81.724,68 $**
- Lettura: Lo scanner è stato troppo ottimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-10,04%** → **72.859,92 $**
- Correzione imparata dagli errori: **4,77%**
- Calibrato: **-5,27%** → **76.725,69 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **13,48%** → **91.915,71 $**
- Correzione imparata dagli errori: **-8,06%**
- Calibrato: **5,43%** → **85.389,37 $**
- Lettura: Lo scanner ha sovrastimato gli spike: nella realtà il prezzo è salito meno del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Solana

- Previsioni controllate: **45**
- Previsioni usate per la calibrazione recente: **45**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **100,00%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **10,41%** → **112,85 $**
- Correzione imparata dagli errori: **2,85%**
- Calibrato: **13,26%** → **115,76 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-5,44%** → **96,65 $**
- Correzione imparata dagli errori: **3,39%**
- Calibrato: **-2,05%** → **100,12 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **17,41%** → **120,01 $**
- Correzione imparata dagli errori: **-1,83%**
- Calibrato: **15,58%** → **118,14 $**
- Lettura: Lo scanner è stato abbastanza centrato sul max gain.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Dogecoin

- Previsioni controllate: **45**
- Previsioni usate per la calibrazione recente: **45**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **74,36%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **14,16%** → **0,09 $**
- Correzione imparata dagli errori: **15,21%**
- Calibrato: **29,37%** → **0,10 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-3,15%** → **0,08 $**
- Correzione imparata dagli errori: **13,70%**
- Calibrato: **10,55%** → **0,09 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **19,89%** → **0,10 $**
- Correzione imparata dagli errori: **3,11%**
- Calibrato: **22,99%** → **0,10 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 80.994,83 $

Bitcoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **52,50%**
- Casi negativi dopo 30 giorni: **47,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,66%**
- Rendimento medio dopo 30 giorni: **4,48%**
- Rendimento centrale dopo 30 giorni: **4,51%**
- Discesa media durante i 30 giorni: **-12,58%**
- Massimo rialzo medio durante i 30 giorni: **19,46%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **84.622,87 $**
- Scenario centrale a 30 giorni: **84.647,98 $**
- Zona di rischio media: **70.805,12 $**
- Zona di rialzo media: **96.756,57 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -25,14% → **60.629,42 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -17,21% → **67.052,08 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 4,51% → **84.647,98 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 14,67% → **92.877,95 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 30,39% → **105.608,34 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -27,35% → **58.841,94 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -21,05% → **63.942,98 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -10,04% → **72.859,92 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -3,68% → **78.016,71 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **80.994,83 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,07% → **81.862,19 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 5,48% → **85.432,15 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 13,48% → **91.915,71 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 24,98% → **101.230,12 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 41,91% → **114.941,06 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| BTC-USD         | 2022-12-02   | 2023-03-11 |        90.65 |        43.72 |           0    |          43.72 |
| RUNE-USD        | 2023-07-01   | 2023-10-08 |        90.33 |        95.43 |         -12.18 |         104.76 |
| QTUM-USD        | 2023-09-13   | 2023-12-21 |        89.13 |        -7.79 |         -10.59 |          12.02 |
| LRC-USD         | 2020-11-22   | 2021-03-01 |        87.74 |        -6.75 |         -23.24 |           6.97 |
| XTZ-USD         | 2019-09-24   | 2020-01-01 |        87.64 |        21.02 |          -9.43 |          22.45 |
| MKR-USD         | 2020-11-23   | 2021-03-02 |        87.59 |         5.95 |         -15.96 |           5.95 |
| CRV-USD         | 2022-12-01   | 2023-03-10 |        87.53 |        14.31 |          -2.49 |          15.59 |
| TRX-USD         | 2022-12-02   | 2023-03-11 |        87.11 |        13.61 |           0    |          14.38 |
| AAVE-USD        | 2022-11-30   | 2023-03-09 |        86.71 |        11.15 |          -1.88 |          17.43 |
| ADA-USD         | 2025-05-30   | 2025-09-06 |        86.67 |         6.52 |          -6.8  |          13.61 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 102,21 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **77,50%**
- Casi negativi dopo 30 giorni: **22,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **87,84%**
- Rendimento medio dopo 30 giorni: **12,50%**
- Rendimento centrale dopo 30 giorni: **10,41%**
- Discesa media durante i 30 giorni: **-7,56%**
- Massimo rialzo medio durante i 30 giorni: **24,05%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **114,99 $**
- Scenario centrale a 30 giorni: **112,85 $**
- Zona di rischio media: **94,48 $**
- Zona di rialzo media: **126,79 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -11,28% → **90,68 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 2,40% → **104,66 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 10,41% → **112,85 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 19,42% → **122,06 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 35,62% → **138,62 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -21,22% → **80,52 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -9,77% → **92,22 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -5,44% → **96,65 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **102,21 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **102,21 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 5,99% → **108,33 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 11,10% → **113,55 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 17,41% → **120,01 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 28,62% → **131,46 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 42,95% → **146,11 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| BTC-USD         | 2022-12-02   | 2023-03-11 |        91.29 |        43.72 |           0    |          43.72 |
| XTZ-USD         | 2019-09-24   | 2020-01-01 |        91.24 |        21.02 |          -9.43 |          22.45 |
| MKR-USD         | 2020-11-23   | 2021-03-02 |        90.92 |         5.95 |         -15.96 |           5.95 |
| CRV-USD         | 2022-12-01   | 2023-03-10 |        90.75 |        14.31 |          -2.49 |          15.59 |
| ENJ-USD         | 2022-12-02   | 2023-03-11 |        89.95 |        23.45 |           0    |          33.6  |
| AVAX-USD        | 2021-07-06   | 2021-10-13 |        89.85 |        53.62 |           0    |          65.33 |
| LRC-USD         | 2020-11-22   | 2021-03-01 |        89.59 |        -6.75 |         -23.24 |           6.97 |
| ADA-USD         | 2025-05-30   | 2025-09-06 |        89.29 |         6.52 |          -6.8  |          13.61 |
| THETA-USD       | 2022-12-01   | 2023-03-10 |        89.07 |        15.44 |          -0.02 |          20.13 |
| ZEC-USD         | 2024-05-30   | 2024-09-06 |        88.89 |         8.74 |          -4.86 |          17.27 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 0,08 $

Dogecoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **77,50%**
- Casi negativi dopo 30 giorni: **22,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **84,27%**
- Rendimento medio dopo 30 giorni: **14,21%**
- Rendimento centrale dopo 30 giorni: **14,16%**
- Discesa media durante i 30 giorni: **-6,87%**
- Massimo rialzo medio durante i 30 giorni: **25,71%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,09 $**
- Scenario centrale a 30 giorni: **0,09 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,10 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -6,85% → **0,07 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 3,96% → **0,08 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 14,16% → **0,09 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 22,00% → **0,10 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 34,05% → **0,11 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -16,84% → **0,07 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -9,54% → **0,07 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -3,15% → **0,08 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **0,08 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **0,08 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 8,24% → **0,09 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 11,41% → **0,09 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 19,89% → **0,10 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 30,66% → **0,10 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 44,33% → **0,12 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XTZ-USD         | 2019-09-24   | 2020-01-01 |        91.38 |        21.02 |          -9.43 |          22.45 |
| LINK-USD        | 2019-08-25   | 2019-12-02 |        87.91 |       -13.76 |         -16.16 |           8.39 |
| BTC-USD         | 2022-12-02   | 2023-03-11 |        87.75 |        43.72 |           0    |          43.72 |
| LRC-USD         | 2020-11-22   | 2021-03-01 |        86.68 |        -6.75 |         -23.24 |           6.97 |
| CRV-USD         | 2022-12-01   | 2023-03-10 |        86.59 |        14.31 |          -2.49 |          15.59 |
| ENJ-USD         | 2022-12-02   | 2023-03-11 |        86.36 |        23.45 |           0    |          33.6  |
| ALGO-USD        | 2026-02-18   | 2026-05-28 |        86.34 |       -25.56 |         -28.07 |          10.34 |
| TRX-USD         | 2022-12-02   | 2023-03-11 |        86.24 |        13.61 |           0    |          14.38 |
| THETA-USD       | 2022-12-01   | 2023-03-10 |        85.8  |        15.44 |          -0.02 |          20.13 |
| ETH-USD         | 2022-12-02   | 2023-03-11 |        85.77 |        28.91 |           0    |          28.91 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report

Generated: 2026-10-15 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-15 | BULL | 80.995 $ | True | 26.75% | 4.28% | BULL | 26.75% | 4.28% |
| DOGE-USD | 2026-10-15 | RECOVERY | 0.07980 $ | False | 10.05% | -2.99% | BULL | 26.75% | 4.28% |
| SOL-USD | 2026-10-15 | BULL | 102,21 $ | True | 36.26% | 6.53% | BULL | 26.75% | 4.28% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 52.50% | 4.51% | 14.67% | 30.39% | -10.04% | -27.35% | 13.48% | 24.98% | 41.91% | 50.00% | -0.21% | 20.58% | 67.90% |
| BTC-USD | SAME_BTC_REGIME | 6 | 66.67% | 6.24% | 8.89% | 52.55% | -10.84% | -19.60% | 8.64% | 12.79% | 59.19% | 50.00% | -2.18% | 89.89% | 197.79% |
| BTC-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 77.50% | 14.16% | 22.00% | 34.05% | -3.15% | -16.84% | 19.89% | 30.66% | 44.33% | 52.50% | 1.43% | 26.67% | 60.43% |
| DOGE-USD | SAME_BTC_REGIME | 8 | 62.50% | 6.24% | 12.79% | 46.10% | -10.87% | -18.29% | 12.52% | 20.62% | 52.89% | 62.50% | 38.33% | 68.76% | 166.60% |
| DOGE-USD | SAME_ASSET_REGIME | 3 | 33.33% | -5.07% | 0.73% | 4.20% | -9.57% | -10.39% | 12.02% | 12.81% | 13.29% | 33.33% | -20.75% | -9.70% | -3.07% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 50.00% | 0.73% | 3.62% | 5.36% | -8.18% | -9.29% | 12.52% | 13.06% | 13.39% | 0.00% | -27.01% | -23.88% | -22.00% |
| SOL-USD | ALL_MATCHES | 40 | 77.50% | 10.41% | 19.42% | 35.62% | -5.44% | -21.22% | 17.41% | 28.62% | 42.95% | 57.50% | 2.50% | 18.89% | 61.33% |
| SOL-USD | SAME_BTC_REGIME | 13 | 76.92% | 5.95% | 9.67% | 36.59% | -9.50% | -21.58% | 13.11% | 15.51% | 37.04% | 46.15% | -4.45% | 41.88% | 110.96% |
| SOL-USD | SAME_ASSET_REGIME | 2 | 50.00% | -6.98% | -2.78% | -0.26% | -13.89% | -19.75% | 4.85% | 4.97% | 5.04% | 50.00% | 1.62% | 8.49% | 12.61% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 50.00% | -6.98% | -2.78% | -0.26% | -13.89% | -19.75% | 4.85% | 4.97% | 5.04% | 50.00% | 1.62% | 8.49% | 12.61% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 27 | 59.26% | 7.72% | -7.63% | 28.72% | 51.85% | 0.65% | 42.90% |
| BTC-USD | HISTORICAL_BTC_BULL | 6 | 66.67% | 6.24% | -10.84% | 12.79% | 50.00% | -2.18% | 96.76% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 21.02% | -9.43% | 22.45% | 100.00% | 91.44% | 163.75% |
| BTC-USD | HISTORICAL_BTC_MIXED | 1 | 0.00% | -23.26% | -27.07% | 0.00% | 0.00% | -15.30% | 0.00% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 5 | 0.00% | -9.26% | -18.18% | 12.02% | 40.00% | -0.57% | 13.36% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 29 | 82.76% | 14.31% | -0.41% | 30.68% | 44.83% | -0.68% | 42.82% |
| DOGE-USD | HISTORICAL_BTC_BULL | 8 | 62.50% | 6.24% | -10.87% | 20.62% | 62.50% | 38.33% | 68.76% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 25.98% | -6.31% | 42.79% | 100.00% | 78.98% | 144.43% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -7.79% | -10.59% | 12.02% | 100.00% | 1.35% | 12.02% |
| SOL-USD | HISTORICAL_BTC_BEAR | 25 | 80.00% | 13.61% | -0.93% | 33.60% | 60.00% | 3.50% | 42.82% |
| SOL-USD | HISTORICAL_BTC_BULL | 13 | 76.92% | 5.95% | -9.50% | 15.51% | 46.15% | -4.45% | 52.04% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 21.02% | -9.43% | 22.45% | 100.00% | 91.44% | 163.75% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -7.79% | -10.59% | 12.02% | 100.00% | 1.35% | 12.02% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 30 | 56.67% | 7.35% | -8.60% | 27.93% | 53.33% | 0.37% | 42.95% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -0.40% | -19.60% | 6.71% | 50.00% | 57.69% | 96.76% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 2 | 0.00% | -25.34% | -29.19% | 0.00% | 0.00% | -26.38% | 0.00% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | 0.75% | -8.15% | 13.21% | 50.00% | -5.53% | 17.58% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 32 | 84.38% | 15.60% | -1.35% | 31.41% | 50.00% | 0.49% | 46.84% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | 10.09% | -10.24% | 34.91% | 100.00% | 36.08% | 57.76% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 5.95% | -15.96% | 12.12% | 66.67% | 41.88% | 81.29% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -5.07% | -9.57% | 12.81% | 33.33% | -20.75% | 12.81% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 82.76% | 13.61% | -2.49% | 33.60% | 58.62% | 3.50% | 42.87% |
| SOL-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | -6.98% | -13.89% | 4.97% | 50.00% | 1.62% | 19.49% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 5 | 60.00% | 5.95% | -15.96% | 15.51% | 60.00% | 41.88% | 75.50% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 41.98% | 0.00% | 41.98% | 100.00% | 11.39% | 52.04% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 66.67% | 6.52% | -9.50% | 12.81% | 33.33% | -19.86% | 12.81% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 0 | 0 | 6 | 6 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 2 | 3 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 2 | 2 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-01 | 90.33% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| BTC-USD | LRC-USD | 2020-11-22 | 87.74% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| BTC-USD | MKR-USD | 2020-11-23 | 87.59% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| BTC-USD | ADA-USD | 2025-05-30 | 86.67% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| BTC-USD | ONE-USD | 2023-07-25 | 85.64% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -0.10% | -0.87% | 1.16% | 0.10% | -0.87% | 1.16% |
| BTC-USD | ETH-USD | 2025-05-30 | 85.51% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 9.67% | -9.50% | 10.32% | -19.86% | -22.97% | 10.32% |
| DOGE-USD | LINK-USD | 2019-08-25 | 87.91% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -13.76% | -16.16% | 8.39% | 34.79% | -16.89% | 39.05% |
| DOGE-USD | LRC-USD | 2020-11-22 | 86.68% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| DOGE-USD | ADA-USD | 2025-05-30 | 84.99% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| DOGE-USD | ZEC-USD | 2024-05-30 | 84.98% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 8.74% | -4.86% | 17.27% | 41.88% | -4.86% | 42.76% |
| DOGE-USD | MKR-USD | 2020-11-23 | 84.69% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| DOGE-USD | RUNE-USD | 2023-07-01 | 82.87% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| DOGE-USD | ZEC-USD | 2021-09-08 | 81.79% | BULL | RECOVERY | SAME_BTC_AND_ASSET | MIXED | -5.07% | -9.57% | 11.42% | -20.75% | -41.73% | 11.42% |
| DOGE-USD | MKR-USD | 2023-05-17 | 81.57% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 24.95% | -1.75% | 30.65% | 51.74% | -1.75% | 51.74% |
| SOL-USD | MKR-USD | 2020-11-23 | 90.92% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| SOL-USD | LRC-USD | 2020-11-22 | 89.59% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| SOL-USD | ADA-USD | 2025-05-30 | 89.29% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| SOL-USD | ZEC-USD | 2024-05-30 | 88.89% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 8.74% | -4.86% | 17.27% | 41.88% | -4.86% | 42.76% |
| SOL-USD | ETH-USD | 2025-05-30 | 88.75% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 9.67% | -9.50% | 10.32% | -19.86% | -22.97% | 10.32% |
| SOL-USD | LINK-USD | 2025-05-30 | 88.66% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 5.27% | -9.44% | 13.20% | -31.77% | -33.69% | 13.20% |
| SOL-USD | RUNE-USD | 2023-07-01 | 88.60% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 95.43% | -12.18% | 104.76% | 275.76% | -12.18% | 308.71% |
| SOL-USD | HBAR-USD | 2025-05-27 | 86.87% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 2.72% | -5.52% | 13.11% | -11.19% | -25.89% | 13.11% |
| SOL-USD | SNX-USD | 2020-11-22 | 86.61% | BULL | DISTRIBUTION | SAME_BTC_ONLY | BEARISH_30D | -14.46% | -21.67% | 9.63% | -11.74% | -33.57% | 9.63% |
| SOL-USD | LINK-USD | 2019-08-20 | 86.42% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -15.37% | -21.21% | 5.09% | 15.36% | -21.89% | 24.45% |

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

Generato: 2026-10-15 05:33 UTC

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
| BTC | 80.995 $ | -8 | RIBASSISTA / FRAGILE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI DECRESCENTI | DISTRIBUZIONE POSSIBILE | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 102,21 $ | -6 | RIBASSISTA / FRAGILE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI DECRESCENTI | RANGE / FASE NON CHIARA | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.07980 $ | -11 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | VOLATILITÀ IN ESPANSIONE | MARKDOWN / DEBOLEZZA | MEDIO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | -2 | -3 | -3 | 0 | 0 | -2 | -8 |
| SOL | +2 | -2 | -3 | -3 | 0 | 0 | 0 | -6 |
| DOGE | -3 | 0 | -3 | -3 | 0 | 0 | -2 | -11 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 80.337 $ | 81.347 $ | 87.364 $ | 62.488 $ | 2,60% | 3,57% | 26,91% |
| SOL | 98,63 $ | 105,49 $ | 124,62 $ | 74,20 $ | 4,34% | -0,31% | 35,75% |
| DOGE | 0.07841 $ | 0.08494 $ | 0.10528 $ | 0.06895 $ | 5,04% | -4,73% | 10,15% |

## Lettura dettagliata

### BTC

- Prezzo: **80.995 $**
- Score classico: **-8 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,60%; distanza supporto 0,77%; distanza resistenza 0,49%

Dettaglio:

- Trend: **+2** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in salita; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **-3** — RSI neutrale 44.7; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-3** — OBV sotto media; CMF negativo -0.16; discesa con volume sopra media
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — DISTRIBUZIONE POSSIBILE. Prezzo alto nel range ma CMF negativo: possibile distribuzione.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 44.74 |
| MACD histogram | -607.35943 |
| CMF20 | -0.156 |
| Volume ratio 20 | 1.45 |
| MA20 | 83.771 $ |
| MA50 | 81.153 $ |
| MA100 | 73.453 $ |
| MA200 | 72.202 $ |
| Pendenza MA50 20g | +8,31% |
| Pendenza MA200 60g | +4,08% |
| Bollinger width | 6,96% |
| Bollinger position | -0.00 |

### SOL

- Prezzo: **102,21 $**
- Score classico: **-6 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 4,34%; distanza supporto 3,60%; distanza resistenza 3,24%

Dettaglio:

- Trend: **+2** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in salita; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **-3** — RSI debole 35.4; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-3** — OBV sotto media; CMF negativo -0.13; discesa con volume sopra media
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 35.37 |
| MACD histogram | -2.35183 |
| CMF20 | -0.131 |
| Volume ratio 20 | 1.21 |
| MA20 | 115,58 $ |
| MA50 | 109,36 $ |
| MA100 | 93,70 $ |
| MA200 | 87,12 $ |
| Pendenza MA50 20g | +14,20% |
| Pendenza MA200 60g | +6,20% |
| Bollinger width | 24,70% |
| Bollinger position | -0.03 |

### DOGE

- Prezzo: **0.07980 $**
- Score classico: **-11 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **MEDIO** — ATR14 5,04%; distanza supporto 1,63%; distanza resistenza 6,60%

Dettaglio:

- Trend: **-3** — prezzo sotto MA200 daily; MA50 daily in salita; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **-3** — RSI debole 36.1; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-3** — OBV sotto media; CMF negativo -0.17; discesa con volume sopra media
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 36.11 |
| MACD histogram | -0.00162 |
| CMF20 | -0.170 |
| Volume ratio 20 | 1.21 |
| MA20 | 0.09085 $ |
| MA50 | 0.08848 $ |
| MA100 | 0.08094 $ |
| MA200 | 0.08747 $ |
| Pendenza MA50 20g | +7,27% |
| Pendenza MA200 60g | -3,28% |
| Bollinger width | 28,50% |
| Bollinger position | 0.01 |

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

Generato: 2026-10-15 05:33 UTC

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
| BTC | 80.995 $ | Doppio massimo | CONFERMATO RECENTE | ribassista | 2026-10-08 | 77.778 $ | 32,88% | n/a | Fib 23,6% TESTATO (0) @ 81.944 $ | NEL RANGE | 80.337 $ |
| SOL | 102,21 $ | Triplo massimo | CANDIDATO | ribassista | n/a | 62,51 $ | n/a | 44,58% | Fib 38,2% TESTATO (0) @ 103,32 $ | NEL RANGE | 97,45 $ |
| DOGE | 0.07980 $ | Doppio minimo | CANDIDATO | rialzista | n/a | 0.13028 $ | n/a | 31,93% | Fib 23,6% REJECTION (0) @ 0.08689 $ | NEL RANGE | 0.07841 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CONFERMATO RECENTE** (-2)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-21 -> 2026-10-02**
- Età formazione: **13 giorni**
- Breakout pattern: **2026-10-08**
- Età breakout: **7 giorni**
- Neckline: **82.571 $**
- Target teorico: **77.778 $**
- Progresso verso target: **32,88%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 81.944 $** — Swing DOWN 2026-10-02 87.146 -> 2026-10-08 80.337; livello più vicino 23.6% a 81.944; stato TESTATO; confluenza: neckline rialzista, invalidazione rialzista, neckline ribassista.
- Invalidazione: **84.222 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due massimi simili vicino a 87.364 tra 2026-09-21 e 2026-10-02. Neckline ribassista stimata: 82.571. Breakout neckline: 2026-10-08 (7 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 77.778; progresso corrente: 32,88%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **80.337 $**
- Resistenza: **81.347 $**
- Breakout 60g: **87.364 $**
- Breakdown 60g: **62.488 $**
- RSI14: **44.86**
- ATR14: **2,60%**
- Volume ratio 20g: **1.45**
- Rendimento 30g: **+3,62%**
- Rendimento 90g: **+26,97%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CONFERMATO RECENTE | -2 | ribassista | 82.571 $ | 2026-10-08 | 7g | 77.778 $ | 32,88% | n/a | 84.222 $ | Due massimi simili a 87.364 $ e 87.146 $. Neckline circa 82.571 $. Breakout neckline: 2026-10-08 (7 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 77.778 $; progresso: 32,88%; prezzo sotto neckline. |
| Doppio minimo | MATURO | +1 | rialzista | 82.262 $ | 2026-09-21 | 24g | 89.580 $ | -17,32% | n/a | 80.617 $ | Due minimi simili a 76.248 $ e 74.945 $. Neckline circa 82.262 $. Breakout neckline: 2026-09-21 (24 giorni fa). Stato: MATURO. Target teorico: 89.580 $; progresso: -17,32%; prezzo sotto neckline. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **67 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **70,69 $**
- Target teorico: **62,51 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **44,58%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 38,2% TESTATO (0) @ 103,32 $** — Swing UP 2026-08-01 70,69 -> 2026-10-02 123,48; livello più vicino 38.2% a 103,32; stato TESTATO; confluenza: invalidazione rialzista.
- Invalidazione: **72,11 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 67 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **97,45 $**
- Resistenza: **107,12 $**
- Breakout 60g: **124,62 $**
- Breakdown 60g: **74,20 $**
- RSI14: **35.40**
- ATR14: **4,34%**
- Volume ratio 20g: **1.21**
- Rendimento 30g: **-0,28%**
- Rendimento 90g: **+35,79%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,51 $ | n/a | 44,58% | 72,11 $ | Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 67 giorni. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 44,58% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 67 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 107,12 $ | 2026-09-18 | 27g | 118,01 $ | -45,05% | n/a | 104,97 $ | Due minimi simili a 97,45 $ e 96,23 $. Neckline circa 107,12 $. Breakout neckline: 2026-09-18 (27 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01 $; progresso: -45,05%; prezzo sotto neckline. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 57g | 85,65 $ | 321,49% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (57 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 321,49%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-10-08**
- Età formazione: **7 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.10528 $**
- Target teorico: **0.13028 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **31,93%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% REJECTION (0) @ 0.08689 $** — Swing DOWN 2026-09-22 0.10528 -> 2026-10-08 0.08122; livello più vicino 23.6% a 0.08689; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.10318 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 0.08028 tra 2026-09-02 e 2026-10-08. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.07841 $**
- Resistenza: **0.09169 $**
- Breakout 60g: **0.10528 $**
- Breakdown 60g: **0.06895 $**
- RSI14: **36.24**
- ATR14: **5,04%**
- Volume ratio 20g: **1.21**
- Rendimento 30g: **-4,58%**
- Rendimento 90g: **+10,31%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | ATTIVO | -1 | ribassista | 0.08028 $ | 2026-10-15 | 0g | 0.06059 $ | 2,45% | n/a | 0.08189 $ | Due massimi simili a 0.09998 $ e 0.09421 $. Neckline circa 0.08028 $. Breakout neckline: 2026-10-15 (0 giorni fa). Stato: ATTIVO. Target teorico: 0.06059 $; progresso: 2,45%; prezzo vicino alla neckline. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.10528 $ | n/a | n/a | 0.13028 $ | n/a | 31,93% | 0.10318 $ | Due minimi simili a 0.08028 $ e 0.08122 $. Neckline circa 0.10528 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 7 giorni. |

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

Generato: 2026-10-15 05:33 UTC

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 81.453 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0081% | +5,23% | 5,82 | +0,79% | 0 $ | 0 $ |
| SOL | 103,29 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0022% | -5,91% | 1,14 | +8,22% | 0 $ | 0 $ |
| DOGE | 0.08033 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0066% | -5,64% | 0,95 | -1,85% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0148% | 185,46 mln $ | 0,07 | +6,03% |
| BTC | Bitget | OK | +0,0100% | 2,86 mld $ | 0,15 | +17,49% |
| BTC | Kucoin | OK | +0,0100% | 811,18 mln $ | 0,15 | -3,57% |
| SOL | Kraken | OK | +0,0181% | 29,44 mln $ | 0,42 | +25,45% |
| SOL | Bitget | OK | +0,0100% | 419,49 mln $ | 0,31 | +48,66% |
| SOL | Kucoin | OK | +0,0079% | 115,93 mln $ | 0,43 | +18,37% |
| DOGE | Kraken | OK | +0,0139% | 4,49 mln $ | 0,72 | +25,85% |
| DOGE | Bitget | OK | -0,0048% | 108,64 mln $ | 0,39 | +8,40% |
| DOGE | Kucoin | OK | +0,0022% | 54,73 mln $ | 0,58 | +8,29% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+0,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 9, accuratezza +33,33%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 2, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **-1,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso. Confluenza tecnica dichiarata: neckline rialzista, invalidazione rialzista, neckline ribassista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** Nessun pattern attivo con conferma exchange sufficiente.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,50**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 2, divergenze 0.
- Flusso taker/order book: **+2,00**.
- OI/funding/basis: **+0,50**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso. Confluenza tecnica dichiarata: invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+1,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 11, accuratezza +45,45%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+0,75**.
- OI/funding/basis: **+0,50**.
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
| BTC | +52,50% | +4,51% | 5 | +80,00% | RACCOLTA DATI | 0,00 | +52,50% | +4,51% |
| SOL | +77,50% | +10,41% | 5 | +100,00% | RACCOLTA DATI | 0,00 | +77,50% | +10,41% |
| DOGE | +77,50% | +14,16% | 9 | +77,78% | RACCOLTA DATI | 0,00 | +77,50% | +14,16% |

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

Generato: 2026-10-15 05:33 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-15 | BTC | 81.453,00 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 5,82 | +5,23% | +0,79% |
| 2026-10-15 | DOGE | 0.08033 | V2.1.3 | OK | 0 | 0 | 1,25 | BASSA | 0,95 | -5,64% | -1,85% |
| 2026-10-15 | SOL | 103,29 | V2.1.3 | OK | 0 | 0 | 2,50 | BASSA | 1,14 | -5,91% | +8,22% |
| 2026-10-14 | BTC | 83.547,70 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,71 | -2,90% | +0,59% |
| 2026-10-14 | DOGE | 0.08493 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,90 | -0,28% | -3,58% |
| 2026-10-14 | SOL | 107,53 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 2,68 | -0,48% | +3,03% |
| 2026-10-13 | BTC | 83.468,90 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,23 | -1,31% | -1,54% |
| 2026-10-13 | DOGE | 0.08465 | V2.1.3 | OK | 0 | 0 | 0,00 | BASSA | 1,00 | -2,24% | -5,28% |
| 2026-10-13 | SOL | 108,16 | V2.1.3 | OK | 0 | 0 | 2,25 | BASSA | 2,46 | -5,94% | +2,32% |

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

**SOL** — SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**DOGE** — DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 80.995 $ | +0.0025% | -17.03% | 1.47 | Misto | 1/5 |
| SOL | 102,21 $ | +0.0069% | -15.01% | 2.07 | Misto | 1/5 |
| DOGE | 0.07980 $ | +0.0056% | -5.64% | 4.52 | Misto | 1/5 |

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

Generato: 2026-10-15 05:33 UTC

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily               | Stato D       | Weekly                                               | Stato W       | Lettura weekly                                                                                                 |   Peso |
|:--------|:--------------------|:--------------|:-----------------------------------------------------|:--------------|:---------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish      | IN_FORMAZIONE | Momentum in indebolimento, divergenza non confermata | CONTESTO      | Momentum in indebolimento, divergenza non confermata. Non esiste una divergenza confermata sugli ultimi pivot. |      0 |
| SOL     | Hidden bullish      | IN_FORMAZIONE | Hidden bullish                                       | IN_FORMAZIONE | Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.    |      0 |
| DOGE    | Conferma ribassista | CONTESTO      | Hidden bullish                                       | IN_FORMAZIONE | Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.    |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                                                 | Stato         | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:-----------------------------------------------------|:--------------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish                                       | IN_FORMAZIONE | 80.957 $ / 44,75  | 2026-10-08 80.337 $ / RSI 46,86 → 2026-10-15 80.643 $ / RSI 44,75   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Momentum in indebolimento, divergenza non confermata | CONTESTO      | 80.957 $ / 55,81  | n/a                                                                 | +0,76%              | -3,21            |      0 |
| SOL     | 1D   | Hidden bullish                                       | IN_FORMAZIONE | 102,14 $ / 35,33  | 2026-09-16 96,23 $ / RSI 51,17 → 2026-10-15 101,80 $ / RSI 35,33    | n/a                 | n/a              |      0 |
| SOL     | 1W   | Hidden bullish                                       | IN_FORMAZIONE | 102,14 $ / 52,37  | 2026-09-20 96,23 $ / RSI 61,01 → 2026-10-18 101,80 $ / RSI 52,37    | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Conferma ribassista                                  | CONTESTO      | 0.07966 $ / 36,09 | n/a                                                                 | -15,68%             | -20,54           |      0 |
| DOGE    | 1W   | Hidden bullish                                       | IN_FORMAZIONE | 0.07966 $ / 43,70 | 2026-09-20 0.07841 $ / RSI 47,54 → 2026-10-18 0.07916 $ / RSI 43,70 | n/a                 | n/a              |      0 |

### BTC

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Momentum in indebolimento, divergenza non confermata / CONTESTO**: Momentum in indebolimento, divergenza non confermata. Non esiste una divergenza confermata sugli ultimi pivot.

### SOL

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.

### DOGE

- **1D — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.
- **1W — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.

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

Generato: 2026-10-15 05:33 UTC

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

| Asset   | Prezzo   |   Punteggio | Verdetto           | Trend            | Momentum        | Struttura                                             |   Pattern score | Fibonacci     | Pattern rialzista                | Pattern ribassista                  | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-------------------|:-----------------|:----------------|:------------------------------------------------------|----------------:|:--------------|:---------------------------------|:------------------------------------|:-----------|:-------------|
| BTC | 80.995 $ | -5 | DEBOLE | Trend misto | Momentum debole | Struttura ribassista con massimi e minimi decrescenti | -1 | 0 / TESTATO | Eve and Adam Bottom / MATURO | Doppio massimo / CONFERMATO RECENTE | 80.337 | 87.146 |
| SOL | 102,21 $ | -4 | DEBOLE | Trend misto | Momentum debole | Struttura ribassista con massimi e minimi decrescenti | 0 | 0 / TESTATO | Doppio minimo / TARGET RAGGIUNTO | Triplo massimo / CANDIDATO | 96,23 | 123,48 |
| DOGE | 0.07980 $ | -8 | RIBASSISTA TECNICO | Trend ribassista | Momentum debole | Volatilità in espansione | 0 | 0 / REJECTION | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 0.07841 | 0.10528 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo     | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-------------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Eve and Adam Bottom — MATURO | CONFERMATO RECENTE | CANDIDATO | Adam and Eve Top — CANDIDATO | -1 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | INVALIDATO | CANDIDATO | ASSENTE | 0 |
| DOGE | CANDIDATO | CANDIDATO | Adam and Eve Bottom — INVALIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 44.86 | -604.746 | 83.773 | 81.153 | 72.202 | 7,74% | 4,28% | 7,12% | 26,75% |
| SOL | 35.4 | -2.34992 | 115,58 | 109,36 | 87,12 | 13,04% | 6,53% | 5,49% | 36,26% |
| DOGE | 36.24 | -0.00162 | 0.09086 | 0.08848 | 0.08747 | 6,50% | -2,99% | -0,34% | 10,05% |

## Dettaglio asset

### BTC

- Prezzo: **80.995 $**
- Punteggio tecnico: **-5 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend misto** (1)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 8.257e+04 -> 8.034e+04. Ultimi massimi: 8.736e+04 -> 8.715e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TESTATO** (0)
  - Swing DOWN 2026-10-02 87.146 -> 2026-10-08 80.337; livello più vicino 23.6% a 81.944; stato TESTATO; confluenza: neckline rialzista, invalidazione rialzista, neckline ribassista.
- Punteggio pattern: **-1**
  - rialzista dominante: Eve and Adam Bottom (MATURO, +1); ribassista dominante: Doppio massimo (CONFERMATO RECENTE, -2).
- Supporto più vicino: **80.337**
- Resistenza più vicina: **87.146**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 76.248 tra 2026-09-02 e 2026-10-08. Neckline stimata: 87.364. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 87.364; target 98.479; distanza dalla neckline 7,86%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 74.945 dal 2026-09-02 al 2026-10-08. Neckline stimata: 87.364. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 87.364; target 99.783; distanza dalla neckline 7,86%; prezzo sotto neckline.
- Eve and Adam Bottom: **MATURO** (+1)
  - Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (24 giorni fa). Stato: MATURO. Target teorico: 89.580; progresso corrente: -17,32%. Relazione prezzo/neckline: sotto neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (24g); progresso -17,32%; prezzo sotto neckline.
- Doppio massimo: **CONFERMATO RECENTE** (-2)
  - Due massimi simili vicino a 87.364 tra 2026-09-21 e 2026-10-02. Neckline ribassista stimata: 82.571. Breakout neckline: 2026-10-08 (7 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 77.778; progresso corrente: 32,88%. Relazione prezzo/neckline: sotto neckline.
  - neckline 82.571; target 77.778; breakout 2026-10-08 (7g); progresso 32,88%; prezzo sotto neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 87.364 dal 2026-09-03 al 2026-10-02. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 74.945; target 62.525; distanza dalla neckline 8,07%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 87.146 dal 2026-09-03 al 2026-10-02. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 74.945; target 62.743; distanza dalla neckline 8,07%; prezzo sopra neckline.

### SOL

- Prezzo: **102,21 $**
- Punteggio tecnico: **-4 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend misto** (1)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 97.45 -> 96.23. Ultimi massimi: 124.6 -> 123.5.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-08-01 70,69 -> 2026-10-02 123,48; livello più vicino 38.2% a 103,32; stato TESTATO; confluenza: invalidazione rialzista.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Triplo massimo (CANDIDATO, 0).
- Supporto più vicino: **96,23**
- Resistenza più vicina: **123,48**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 96,23 tra 2026-09-02 e 2026-09-16. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (27 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: -45,05%. Relazione prezzo/neckline: sotto neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (27g); progresso -45,05%; prezzo sotto neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (57 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 292,39%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (57g); progresso 292,39%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 96,23 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (27 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: -45,05%. Relazione prezzo/neckline: sotto neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (27g); progresso -45,05%; prezzo sotto neckline.
- Doppio massimo: **INVALIDATO** (0)
  - Due massimi simili vicino a 110,04 tra 2026-08-27 e 2026-09-06. Neckline ribassista stimata: 97,45. Breakout neckline: 2026-09-15 (30 giorni fa). Stato: INVALIDATO. Target teorico: 84,86; progresso corrente: -37,81%. Relazione prezzo/neckline: sopra neckline.
  - neckline 97,45; target 84,86; breakout 2026-09-15 (30g); progresso -37,81%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 67 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 44,58%; prezzo sopra neckline.
- Adam/Eve Top: **ASSENTE** (0)

### DOGE

- Prezzo: **0.07980 $**
- Punteggio tecnico: **-8 / 12**
- Verdetto: **RIBASSISTA TECNICO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 0.09053 -> 0.08122. Ultimi massimi: 0.09421 -> 0.1053.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 31,70%. Fase non abbastanza chiara.
- Fibonacci automatico: **REJECTION** (0)
  - Swing DOWN 2026-09-22 0.10528 -> 2026-10-08 0.08122; livello più vicino 23.6% a 0.08689; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.07841**
- Resistenza più vicina: **0.10528**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.08028 tra 2026-09-02 e 2026-10-08. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 0.10528; target 0.13028; distanza dalla neckline 31,93%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 0.07841 dal 2026-09-02 al 2026-10-08. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 0.10528; target 0.13216; distanza dalla neckline 31,93%; prezzo sotto neckline.
- Adam and Eve Bottom: **INVALIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.07841 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (24 giorni fa). Stato: INVALIDATO. Target teorico: 0.11001; progresso corrente: -91,17%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.09421; target 0.11001; breakout 2026-09-21 (24g); progresso -91,17%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.10528 tra 2026-08-22 e 2026-09-22. Neckline ribassista stimata: 0.07841. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 23 giorni.
  - neckline 0.07841; target 0.05153; distanza dalla neckline 1,78%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 65 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 17,40%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07380 dal 2026-07-26 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 65 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 17,40%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato     | Confluenza                                                       |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:----------|:-----------------------------------------------------------------|--------:|
| BTC | DOWN 2026-10-02 -> 2026-10-08 | 81.944 | 82.938 | 83.742 | 84.545 | 85.689 | 23.6% / 81.944 | TESTATO | neckline rialzista, invalidazione rialzista, neckline ribassista | 0 |
| SOL | UP 2026-08-01 -> 2026-10-02 | 111,02 | 103,32 | 97,09 | 90,86 | 81,99 | 38.2% / 103,32 | TESTATO | invalidazione rialzista | 0 |
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

- **BTC**: 45/30 previsioni controllate su 98 fatte. Stato: **ATTIVA**.
- **SOL**: 45/30 previsioni controllate su 98 fatte. Stato: **ATTIVA**.
- **DOGE**: 45/30 previsioni controllate su 98 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 98 | 45 | 30/30 [██████████] | 53 | ATTIVA | 2026-10-16 / tra 1 giorno |
| SOL | 98 | 45 | 30/30 [██████████] | 53 | ATTIVA | 2026-10-16 / tra 1 giorno |
| DOGE | 98 | 45 | 30/30 [██████████] | 53 | ATTIVA | 2026-10-16 / tra 1 giorno |

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

Generato: 2026-10-15 05:34 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- Calibrazione rischio in quarantena; moduli sospesi esclusi dalla verifica prezzi correnti. Consultare lab_reduction_status.md.
- 3 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo         | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:--------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price | OK      | 80.995 $          | 80.995 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price | OK      | 0.07980 $         | 0.07980 $       | -0,0000%     |
| Scanner                 | SOL     | current_price | OK      | 102,21 $          | 102,21 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price | OK      | 80.995 $          | 80.995 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price | OK      | 102,21 $          | 102,21 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price | OK      | 0.07980 $         | 0.07980 $       | -0,0000%     |
| Technical Structure     | BTC     | price         | OK      | 80.995 $          | 80.995 $        | +0,0000%     |
| Technical Structure     | SOL     | price         | OK      | 102,21 $          | 102,21 $        | +0,0000%     |
| Technical Structure     | DOGE    | price         | OK      | 0.07980 $         | 0.07980 $       | -0,0000%     |
| Classic Technical       | BTC     | price         | OK      | 80.995 $          | 80.995 $        | +0,0000%     |
| Classic Technical       | SOL     | price         | OK      | 102,21 $          | 102,21 $        | +0,0000%     |
| Classic Technical       | DOGE    | price         | OK      | 0.07980 $         | 0.07980 $       | -0,0000%     |
| Classic Visual          | BTC     | price         | OK      | 80.995 $          | 80.995 $        | +0,0000%     |
| Classic Visual          | SOL     | price         | OK      | 102,21 $          | 102,21 $        | +0,0000%     |
| Classic Visual          | DOGE    | price         | OK      | 0.07980 $         | 0.07980 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price         | WARN    | 80.995 $          | 81.453 $        | +0,5657%     |
| Exchange Microstructure | SOL     | price         | WARN    | 102,21 $          | 103,29 $        | +1,0606%     |
| Exchange Microstructure | DOGE    | price         | WARN    | 0.07980 $         | 0.08033 $       | +0,6642%     |

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
