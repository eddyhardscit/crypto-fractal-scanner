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

Generato: 2026-10-18 05:33 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | BULLISH | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | -1 | LEGGERMENTE BEARISH | TAKE PROFIT SU SPIKE / NON INSEGUIRE | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | -2 | LEGGERMENTE BEARISH | EVITA LONG / SOLO RIMBALZI VELOCI | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+3**, spot = **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **-1**, spot = **TAKE PROFIT SU SPIKE / NON INSEGUIRE**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **-2**, spot = **EVITA LONG / SOLO RIMBALZI VELOCI**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+3**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**
- Long leva: **LONG PRUDENTE**
- Short leva: **NO SHORT**
- Rischio: **MEDIO**
- Conferme: Prima resistenza sopra 84.249; conferma del eve and adam bottom sopra 82.262.
- Invalidazioni: Sotto 80.337 il quadro tecnico peggiora.

### SOL

- Global Confluence: **-1**
- Confluenza: **DEBOLE / FRAGILE**
- Bias Global: **Fragile**
- Direzione decisionale: **LEGGERMENTE BEARISH**
- Azione spot dal Global: **TAKE PROFIT SU SPIKE / NON INSEGUIRE**
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
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 3; EMA200 circa 111,34 $; upside verso EMA200 +7,74%. Non autorizza leva e non aggiunge punti automatici.
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

Generato: 2026-10-18 05:33 UTC

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

Segnali totali salvati: **279**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-18 | BTC | 81.614,92 | +3 | +2 | +2 | 0 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-10-18 | DOGE | 0.07904 | -2 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-18 | SOL | 103,34 | -1 | +2 | +2 | 0 | -2 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-10-16 | BTC | 82.086,63 | +2 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-16 | DOGE | 0.08216 | -1 | +3 | +3 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-16 | SOL | 105,81 | 0 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-15 | BTC | 80.946,10 | -2 | +1 | +1 | 0 | -2 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-15 | DOGE | 0.07966 | -2 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-15 | SOL | 102,12 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-14 | BTC | 83.488,21 | 0 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-14 | DOGE | 0.08470 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-10-14 | SOL | 107,30 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 93 | 92 | 92 | 91 | 89 | 87 | 84 | 80 | 74 | 69 | 55 | 40 |
| SOL | 93 | 92 | 92 | 91 | 89 | 87 | 84 | 80 | 74 | 69 | 55 | 40 |
| DOGE | 93 | 92 | 92 | 91 | 89 | 87 | 84 | 80 | 74 | 69 | 55 | 40 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-20 | 60g | 2026-10-19 | domani |
| SOL | 2026-08-20 | 60g | 2026-10-19 | domani |
| DOGE | 2026-08-20 | 60g | 2026-10-19 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 82 | 51,22% | +0,30% | +0,26% | UTILE |
| BTC | 2g | 82 | 50,00% | +0,50% | +0,43% | UTILE |
| BTC | 3g | 81 | 45,68% | +0,62% | +0,59% | UTILE |
| BTC | 5g | 80 | 43,75% | +1,32% | +1,22% | UTILE |
| BTC | 7g | 78 | 51,28% | +2,07% | +1,93% | UTILE |
| BTC | 10g | 78 | 55,13% | +2,83% | +2,71% | UTILE |
| BTC | 14g | 75 | 60,00% | +4,31% | +4,27% | UTILE |
| BTC | 21g | 69 | 71,01% | +7,93% | +7,83% | UTILE |
| BTC | 30g | 66 | 95,45% | +11,98% | +11,32% | UTILE |
| BTC | 45g | 52 | 94,23% | +20,05% | +17,51% | PRIMA CALIBRAZIONE |
| BTC | 60g | 37 | 91,89% | +28,16% | +24,10% | PRIMA CALIBRAZIONE |
| SOL | 1g | 83 | 46,99% | +0,18% | +0,10% | UTILE |
| SOL | 2g | 83 | 44,58% | +0,57% | +0,48% | UTILE |
| SOL | 3g | 83 | 48,19% | +0,95% | +0,84% | UTILE |
| SOL | 5g | 81 | 49,38% | +1,71% | +1,65% | UTILE |
| SOL | 7g | 79 | 54,43% | +2,70% | +2,77% | UTILE |
| SOL | 10g | 76 | 56,58% | +4,22% | +4,32% | UTILE |
| SOL | 14g | 72 | 65,28% | +6,99% | +7,49% | UTILE |
| SOL | 21g | 66 | 77,27% | +13,20% | +12,66% | UTILE |
| SOL | 30g | 61 | 83,61% | +19,46% | +16,22% | UTILE |
| SOL | 45g | 48 | 75,00% | +33,69% | +17,66% | PRIMA CALIBRAZIONE |
| SOL | 60g | 33 | 66,67% | +45,78% | +19,23% | PRIMA CALIBRAZIONE |
| DOGE | 1g | 84 | 48,81% | -0,02% | -0,02% | UTILE |
| DOGE | 2g | 84 | 45,24% | +0,12% | -0,08% | UTILE |
| DOGE | 3g | 83 | 40,96% | +0,37% | +0,05% | UTILE |
| DOGE | 5g | 81 | 45,68% | +0,98% | +0,20% | UTILE |
| DOGE | 7g | 80 | 50,00% | +1,42% | +0,52% | UTILE |
| DOGE | 10g | 78 | 43,59% | +1,85% | +0,33% | UTILE |
| DOGE | 14g | 75 | 52,00% | +3,51% | +2,14% | UTILE |
| DOGE | 21g | 70 | 55,71% | +6,66% | +1,12% | UTILE |
| DOGE | 30g | 65 | 67,69% | +10,57% | +4,75% | UTILE |
| DOGE | 45g | 51 | 49,02% | +19,30% | +4,02% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 38 | 47,37% | +25,24% | +0,04% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 82 | 51,22% | +0,30% | +0,26% | -0,27% | +0,81% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 90 | 48,89% | +0,20% | +0,25% | -0,33% | +0,70% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 90 | 48,89% | +0,20% | +0,25% | -0,33% | +0,70% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 85 | 47,06% | +0,22% | +0,03% | -0,28% | +0,73% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,55% | -0,06% | -0,27% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 82 | 50,00% | +0,50% | +0,43% | -0,28% | +1,19% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 90 | 51,11% | +0,45% | +0,53% | -0,29% | +1,13% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 90 | 51,11% | +0,45% | +0,53% | -0,29% | +1,13% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 85 | 47,06% | +0,43% | +0,06% | -0,21% | +1,11% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,85% | -0,13% | -0,05% | +1,59% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 81 | 45,68% | +0,62% | +0,59% | -1,29% | +2,41% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 89 | 49,44% | +0,74% | +0,81% | -1,35% | +2,43% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 89 | 49,44% | +0,74% | +0,81% | -1,35% | +2,43% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 84 | 40,48% | +0,75% | -0,10% | -1,29% | +2,45% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 36 | 36,11% | +1,29% | -0,55% | -1,13% | +3,01% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 80 | 43,75% | +1,32% | +1,22% | -1,98% | +3,75% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 87 | 48,28% | +1,45% | +1,56% | -1,97% | +3,83% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 87 | 48,28% | +1,45% | +1,56% | -1,97% | +3,83% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 82 | 42,68% | +1,31% | -0,63% | -1,93% | +3,77% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 35 | 37,14% | +2,90% | -2,19% | -1,77% | +5,36% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 78 | 51,28% | +2,07% | +1,93% | -2,28% | +4,92% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 85 | 58,82% | +2,17% | +2,31% | -2,28% | +4,93% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 85 | 58,82% | +2,17% | +2,31% | -2,28% | +4,93% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 80 | 41,25% | +2,12% | -1,06% | -2,26% | +4,89% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 34 | 32,35% | +4,23% | -3,81% | -2,10% | +7,38% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 78 | 55,13% | +2,83% | +2,71% | -2,63% | +5,98% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 82 | 67,07% | +2,95% | +3,30% | -2,58% | +6,08% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 82 | 67,07% | +2,95% | +3,30% | -2,58% | +6,08% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 77 | 44,16% | +2,90% | -0,55% | -2,59% | +6,10% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 34 | 35,29% | +4,28% | -4,21% | -2,33% | +7,98% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -1,47% | -1,47% | -4,23% | +1,69% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 75 | 60,00% | +4,31% | +4,27% | -2,81% | +8,09% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 78 | 60,26% | +4,41% | +4,55% | -2,78% | +8,19% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 78 | 60,26% | +4,41% | +4,55% | -2,78% | +8,19% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 73 | 54,79% | +4,46% | +1,14% | -2,80% | +8,33% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 32 | 21,88% | +4,22% | -4,16% | -2,32% | +8,86% | PRIMA CALIBRAZIONE |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,75% | -0,75% | -4,66% | +2,55% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 69 | 71,01% | +7,93% | +7,83% | -2,93% | +11,83% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 74 | 75,68% | +7,59% | +7,75% | -2,97% | +11,58% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 74 | 75,68% | +7,59% | +7,75% | -2,97% | +11,58% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 67 | 53,73% | +7,97% | +1,17% | -2,95% | +11,98% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 29 | 44,83% | +8,60% | -4,88% | -2,40% | +12,46% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 66 | 95,45% | +11,98% | +11,32% | -2,91% | +16,28% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 69 | 92,75% | +11,96% | +11,96% | -2,89% | +16,36% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 69 | 92,75% | +11,96% | +11,96% | -2,89% | +16,36% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 62 | 66,13% | +12,05% | +1,30% | -2,85% | +16,53% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 28 | 57,14% | +12,44% | -2,72% | -2,47% | +17,06% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 52 | 94,23% | +20,05% | +17,51% | -2,63% | +25,00% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 55 | 100,00% | +20,43% | +20,43% | -2,62% | +25,26% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 55 | 100,00% | +20,43% | +20,43% | -2,62% | +25,26% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 50 | 56,00% | +20,37% | -1,59% | -2,43% | +25,26% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 23 | 65,22% | +14,44% | -4,44% | -2,41% | +20,40% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 37 | 91,89% | +28,16% | +24,10% | -2,38% | +33,63% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 40 | 100,00% | +27,95% | +27,95% | -2,38% | +33,54% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 40 | 100,00% | +27,95% | +27,95% | -2,38% | +33,54% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +28,58% | +28,58% | -2,21% | +34,30% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 35 | 37,14% | +28,30% | -8,12% | -2,09% | +34,10% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 8 | 0,00% | +32,27% | -32,27% | -0,83% | +38,31% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 84 | 48,81% | -0,02% | -0,02% | -0,80% | +1,02% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 91 | 58,24% | -0,07% | +0,44% | -0,89% | +0,92% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 91 | 58,24% | -0,07% | +0,44% | -0,89% | +0,92% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 85 | 50,59% | -0,15% | +0,20% | -1,00% | +0,83% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 52 | 40,38% | -0,07% | -0,55% | -1,01% | +0,63% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 58,33% | +2,27% | +2,00% | +0,38% | +3,14% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 84 | 45,24% | +0,12% | -0,08% | -1,02% | +1,49% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 91 | 56,04% | -0,05% | +0,65% | -1,14% | +1,26% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 91 | 56,04% | -0,05% | +0,65% | -1,14% | +1,26% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 85 | 55,29% | -0,35% | +0,25% | -1,45% | +0,96% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 52 | 46,15% | -0,01% | -0,91% | -1,21% | +1,01% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 41,67% | +2,33% | +2,11% | +0,69% | +4,97% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 83 | 40,96% | +0,37% | +0,05% | -2,61% | +3,61% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 90 | 54,44% | +0,07% | +0,94% | -2,80% | +3,30% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 90 | 54,44% | +0,07% | +0,94% | -2,80% | +3,30% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 84 | 47,62% | -0,52% | +0,06% | -3,04% | +2,67% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 51 | 37,25% | +0,23% | -1,71% | -2,84% | +3,45% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 81 | 45,68% | +0,98% | +0,20% | -3,77% | +5,88% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 88 | 52,27% | +0,56% | +1,32% | -4,05% | +5,53% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 88 | 52,27% | +0,56% | +1,32% | -4,05% | +5,53% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 82 | 52,44% | -0,20% | -0,60% | -4,43% | +4,83% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 50 | 40,00% | +1,07% | -3,63% | -4,14% | +6,08% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 80 | 50,00% | +1,42% | +0,52% | -4,48% | +7,70% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 86 | 56,98% | +1,20% | +1,73% | -4,70% | +7,42% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 86 | 56,98% | +1,20% | +1,73% | -4,70% | +7,42% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 80 | 46,25% | +0,27% | -1,03% | -5,15% | +6,50% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 48 | 33,33% | +2,21% | -5,36% | -4,67% | +8,24% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 78 | 43,59% | +1,85% | +0,33% | -5,34% | +9,53% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 83 | 57,83% | +1,50% | +2,23% | -5,52% | +9,26% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 83 | 57,83% | +1,50% | +2,23% | -5,52% | +9,26% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 77 | 44,16% | +0,24% | -2,06% | -6,07% | +7,88% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 45 | 31,11% | +3,10% | -6,72% | -5,29% | +10,57% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 75 | 52,00% | +3,51% | +2,14% | -6,09% | +13,04% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 79 | 65,82% | +3,01% | +3,79% | -6,14% | +12,62% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 79 | 65,82% | +3,01% | +3,79% | -6,14% | +12,62% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 73 | 43,84% | +1,07% | -2,33% | -6,76% | +10,22% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 44 | 38,64% | +4,07% | -5,67% | -5,83% | +12,84% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 70 | 55,71% | +6,66% | +1,12% | -6,16% | +18,26% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 73 | 60,27% | +7,02% | +5,08% | -6,13% | +18,45% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 73 | 60,27% | +7,02% | +5,08% | -6,13% | +18,45% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 67 | 52,24% | +5,06% | -3,08% | -6,82% | +15,71% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 43 | 41,86% | +5,14% | -7,66% | -6,03% | +15,65% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +4,84% | -0,04% | -5,47% | +18,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 65 | 67,69% | +10,57% | +4,75% | -5,49% | +25,70% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 68 | 69,12% | +10,87% | +6,79% | -5,47% | +26,13% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 68 | 69,12% | +10,87% | +6,79% | -5,47% | +26,13% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 62 | 58,06% | +9,46% | -2,31% | -6,17% | +24,12% | UTILE |
| DOGE | 30g | Classic technical | CALIBRABILE | 41 | 48,78% | +8,28% | -6,60% | -5,70% | +22,87% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 80,00% | +17,31% | +10,98% | -5,24% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 51 | 49,02% | +19,30% | +4,02% | -4,73% | +37,68% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 54 | 64,81% | +18,96% | +7,80% | -4,75% | +37,55% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 54 | 64,81% | +18,96% | +7,80% | -4,75% | +37,55% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 48 | 10,42% | +15,99% | -12,50% | -5,56% | +35,47% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 31 | 3,23% | +21,52% | -22,01% | -5,10% | +38,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +21,73% | +11,03% | -4,45% | +35,73% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 38 | 47,37% | +25,24% | +0,04% | -3,55% | +45,38% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 40 | 60,00% | +25,69% | +9,37% | -3,60% | +45,49% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 40 | 60,00% | +25,69% | +9,37% | -3,60% | +45,49% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +24,96% | +11,95% | -3,59% | +45,33% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 33 | 6,06% | +26,42% | -24,30% | -4,39% | +44,35% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 27 | 0,00% | +23,75% | -23,75% | -3,76% | +44,21% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +38,20% | +19,48% | -1,31% | +51,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 83 | 46,99% | +0,18% | +0,10% | -0,61% | +1,04% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 86 | 53,49% | +0,14% | +0,40% | -0,73% | +0,99% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 89 | 52,81% | +0,17% | +0,35% | -0,69% | +1,02% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 84 | 46,43% | +0,13% | -0,06% | -0,79% | +0,96% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 59 | 44,07% | +0,51% | -0,09% | -0,48% | +1,43% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 83 | 44,58% | +0,57% | +0,48% | -0,67% | +1,64% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 86 | 48,84% | +0,44% | +0,62% | -0,89% | +1,39% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 89 | 48,31% | +0,44% | +0,59% | -0,86% | +1,44% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 84 | 45,24% | +0,27% | -0,02% | -0,87% | +1,40% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,60% | +0,15% | -0,64% | +1,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 83 | 48,19% | +0,95% | +0,84% | -2,25% | +3,56% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 85 | 51,76% | +0,81% | +1,15% | -2,38% | +3,41% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 88 | 51,14% | +0,79% | +1,10% | -2,34% | +3,41% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 83 | 44,58% | +0,42% | -0,31% | -2,41% | +2,99% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 59 | 45,76% | +0,61% | +0,08% | -2,23% | +3,14% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 81 | 49,38% | +1,71% | +1,65% | -3,29% | +5,58% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 83 | 53,01% | +1,52% | +1,90% | -3,40% | +5,39% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 86 | 52,33% | +1,49% | +1,81% | -3,35% | +5,34% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 81 | 45,68% | +1,13% | -0,77% | -3,46% | +4,86% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 58 | 48,28% | +0,68% | +0,02% | -3,30% | +4,39% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 79 | 54,43% | +2,70% | +2,77% | -3,85% | +7,29% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 81 | 61,73% | +2,47% | +3,26% | -3,96% | +7,07% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 84 | 61,90% | +2,38% | +3,14% | -3,92% | +6,96% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 79 | 39,24% | +1,54% | -1,83% | -4,06% | +6,21% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 58 | 43,10% | +0,35% | -0,23% | -4,10% | +5,03% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 76 | 56,58% | +4,22% | +4,32% | -4,40% | +9,33% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 78 | 70,51% | +4,07% | +5,95% | -4,53% | +8,98% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 81 | 69,14% | +3,91% | +5,74% | -4,49% | +8,80% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 76 | 40,79% | +2,49% | -2,50% | -4,70% | +7,67% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 57 | 43,86% | +0,11% | -0,57% | -4,99% | +5,77% | PRIMA CALIBRAZIONE |

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

Generato: 2026-10-18 05:33 UTC

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
| BTC | 93 | UTILE | 90 | 29 | 18 | 0 | Famiglia statistica | 2g | 51,11% | +0,53% | campione utile, valutare con prudenza |
| SOL | 93 | UTILE | 86 | 32 | 18 | 0 | Famiglia statistica | 1g | 53,49% | +0,40% | campione utile, valutare con prudenza |
| DOGE | 93 | UTILE | 91 | 32 | 18 | 0 | Famiglia statistica | 1g | 58,24% | +0,44% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 36 | 41,67% | -0,06% | +0,55% | -0,27% | +1,09% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 90 | 48,89% | +0,25% | +0,20% | -0,33% | +0,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 85 | 47,06% | +0,03% | +0,22% | -0,28% | +0,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 36 | 41,67% | -0,13% | +0,85% | -0,05% | +1,59% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 90 | 51,11% | +0,53% | +0,45% | -0,29% | +1,13% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 85 | 47,06% | +0,06% | +0,43% | -0,21% | +1,11% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 36 | 36,11% | -0,55% | +1,29% | -1,13% | +3,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Famiglia statistica | 89 | 49,44% | +0,81% | +0,74% | -1,35% | +2,43% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 84 | 40,48% | -0,10% | +0,75% | -1,29% | +2,45% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 35 | 37,14% | -2,19% | +2,90% | -1,77% | +5,36% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 87 | 48,28% | +1,56% | +1,45% | -1,97% | +3,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 82 | 42,68% | -0,63% | +1,31% | -1,93% | +3,77% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 34 | 32,35% | -3,81% | +4,23% | -2,10% | +7,38% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 85 | 58,82% | +2,31% | +2,17% | -2,28% | +4,93% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 80 | 41,25% | -1,06% | +2,12% | -2,26% | +4,89% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 34 | 35,29% | -4,21% | +4,28% | -2,33% | +7,98% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 82 | 67,07% | +3,30% | +2,95% | -2,58% | +6,08% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | -1,47% | -1,47% | -4,23% | +1,69% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 77 | 44,16% | -0,55% | +2,90% | -2,59% | +6,10% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 32 | 21,88% | -4,16% | +4,22% | -2,32% | +8,86% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Famiglia statistica | 78 | 60,26% | +4,55% | +4,41% | -2,78% | +8,19% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 8 | 37,50% | -0,75% | -0,75% | -4,66% | +2,55% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 73 | 54,79% | +1,14% | +4,46% | -2,80% | +8,33% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 29 | 44,83% | -4,88% | +8,60% | -2,40% | +12,46% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 74 | 75,68% | +7,75% | +7,59% | -2,97% | +11,58% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 67 | 53,73% | +1,17% | +7,97% | -2,95% | +11,98% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 28 | 57,14% | -2,72% | +12,44% | -2,47% | +17,06% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 69 | 92,75% | +11,96% | +11,96% | -2,89% | +16,36% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 62 | 66,13% | +1,30% | +12,05% | -2,85% | +16,53% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Classic technical | 23 | 65,22% | -4,44% | +14,44% | -2,41% | +20,40% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 55 | 100,00% | +20,43% | +20,43% | -2,62% | +25,26% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 50 | 56,00% | -1,59% | +20,37% | -2,43% | +25,26% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 8 | 0,00% | -32,27% | +32,27% | -0,83% | +38,31% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 40 | 100,00% | +27,95% | +27,95% | -2,38% | +33,54% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 35 | 37,14% | -8,12% | +28,30% | -2,09% | +34,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Classic technical | 52 | 40,38% | -0,55% | -0,07% | -1,01% | +0,63% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 91 | 58,24% | +0,44% | -0,07% | -0,89% | +0,92% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 12 | 58,33% | +2,00% | +2,27% | +0,38% | +3,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 85 | 50,59% | +0,20% | -0,15% | -1,00% | +0,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 52 | 46,15% | -0,91% | -0,01% | -1,21% | +1,01% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 91 | 56,04% | +0,65% | -0,05% | -1,14% | +1,26% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 12 | 41,67% | +2,11% | +2,33% | +0,69% | +4,97% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 85 | 55,29% | +0,25% | -0,35% | -1,45% | +0,96% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 51 | 37,25% | -1,71% | +0,23% | -2,84% | +3,45% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 90 | 54,44% | +0,94% | +0,07% | -2,80% | +3,30% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 11 | 54,55% | +2,62% | +2,81% | -1,35% | +6,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 84 | 47,62% | +0,06% | -0,52% | -3,04% | +2,67% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 50 | 40,00% | -3,63% | +1,07% | -4,14% | +6,08% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 88 | 52,27% | +1,32% | +0,56% | -4,05% | +5,53% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 11 | 36,36% | +2,02% | +2,17% | -2,50% | +9,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 82 | 52,44% | -0,60% | -0,20% | -4,43% | +4,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 48 | 33,33% | -5,36% | +2,21% | -4,67% | +8,24% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 86 | 56,98% | +1,73% | +1,20% | -4,70% | +7,42% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 11 | 45,45% | +0,78% | +0,88% | -3,00% | +9,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 80 | 46,25% | -1,03% | +0,27% | -5,15% | +6,50% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 45 | 31,11% | -6,72% | +3,10% | -5,29% | +10,57% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 83 | 57,83% | +2,23% | +1,50% | -5,52% | +9,26% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 77 | 44,16% | -2,06% | +0,24% | -6,07% | +7,88% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 44 | 38,64% | -5,67% | +4,07% | -5,83% | +12,84% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 79 | 65,82% | +3,79% | +3,01% | -6,14% | +12,62% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 11 | 45,45% | +2,03% | +5,60% | -4,35% | +14,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 73 | 43,84% | -2,33% | +1,07% | -6,76% | +10,22% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 43 | 41,86% | -7,66% | +5,14% | -6,03% | +15,65% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 73 | 60,27% | +5,08% | +7,02% | -6,13% | +18,45% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 11 | 63,64% | -0,04% | +4,84% | -5,47% | +18,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 67 | 52,24% | -3,08% | +5,06% | -6,82% | +15,71% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Classic technical | 41 | 48,78% | -6,60% | +8,28% | -5,70% | +22,87% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 68 | 69,12% | +6,79% | +10,87% | -5,47% | +26,13% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 10 | 80,00% | +10,98% | +17,31% | -5,24% | +30,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 62 | 58,06% | -2,31% | +9,46% | -6,17% | +24,12% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 45g | MEDIO | Classic technical | 31 | 3,23% | -22,01% | +21,52% | -5,10% | +38,53% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Famiglia statistica | 54 | 64,81% | +7,80% | +18,96% | -4,75% | +37,55% | PESO OK | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 8 | 62,50% | +11,03% | +21,73% | -4,45% | +35,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 48 | 10,42% | -12,50% | +15,99% | -5,56% | +35,47% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 27 | 0,00% | -23,75% | +23,75% | -3,76% | +44,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 40 | 60,00% | +9,37% | +25,69% | -3,60% | +45,49% | PESO OK | 0,0 | MEDIA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 4 | 75,00% | +19,48% | +38,20% | -1,31% | +51,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 33 | 6,06% | -24,30% | +26,42% | -4,39% | +44,35% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 1g | BREVE | Classic technical | 59 | 44,07% | -0,09% | +0,51% | -0,48% | +1,43% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 86 | 53,49% | +0,40% | +0,14% | -0,73% | +0,99% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 84 | 46,43% | -0,06% | +0,13% | -0,79% | +0,96% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 59 | 47,46% | +0,15% | +0,60% | -0,64% | +1,71% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 86 | 48,84% | +0,62% | +0,44% | -0,89% | +1,39% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 84 | 45,24% | -0,02% | +0,27% | -0,87% | +1,40% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 59 | 45,76% | +0,08% | +0,61% | -2,23% | +3,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 85 | 51,76% | +1,15% | +0,81% | -2,38% | +3,41% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 83 | 44,58% | -0,31% | +0,42% | -2,41% | +2,99% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 58 | 48,28% | +0,02% | +0,68% | -3,30% | +4,39% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 83 | 53,01% | +1,90% | +1,52% | -3,40% | +5,39% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 81 | 45,68% | -0,77% | +1,13% | -3,46% | +4,86% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 58 | 43,10% | -0,23% | +0,35% | -4,10% | +5,03% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 81 | 61,73% | +3,26% | +2,47% | -3,96% | +7,07% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 79 | 39,24% | -1,83% | +1,54% | -4,06% | +6,21% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 57 | 43,86% | -0,57% | +0,11% | -4,99% | +5,77% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 78 | 70,51% | +5,95% | +4,07% | -4,53% | +8,98% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 76 | 40,79% | -2,50% | +2,49% | -4,70% | +7,67% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 54 | 42,59% | -0,29% | +1,33% | -5,64% | +7,48% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 74 | 78,38% | +8,86% | +7,07% | -4,77% | +12,81% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 72 | 38,89% | -3,25% | +4,67% | -5,11% | +10,76% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 48 | 56,25% | -1,82% | +8,64% | -5,55% | +14,77% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 69 | 82,61% | +14,41% | +13,24% | -4,85% | +19,46% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 66 | 50,00% | -5,44% | +10,83% | -5,23% | +17,14% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Classic technical | 43 | 53,49% | -4,28% | +21,82% | -4,56% | +27,59% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 64 | 90,62% | +18,67% | +21,09% | -4,22% | +28,74% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 61 | 44,26% | -7,62% | +20,13% | -4,64% | +26,68% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 45g | MEDIO | Classic technical | 36 | 38,89% | -16,95% | +28,32% | -4,22% | +39,56% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Famiglia statistica | 50 | 76,00% | +20,79% | +33,87% | -3,97% | +43,33% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +28,91% | +28,91% | -3,55% | +37,55% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 52 | 34,62% | -21,16% | +32,82% | -4,38% | +42,33% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 21 | 0,00% | -53,73% | +53,73% | -4,64% | +60,15% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 36 | 77,78% | +33,50% | +48,66% | -3,91% | +59,43% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +47,10% | +47,10% | -5,94% | +54,98% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 37 | 10,81% | -40,42% | +47,75% | -4,69% | +57,67% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 84 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 91 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 108 | 39,81% | -0,25% |
| BTC | BREVE | Famiglia statistica | 269 | 49,81% | +0,53% |
| BTC | BREVE | Microstruttura exchange | 27 | 37,04% | -0,30% |
| BTC | BREVE | Tecnico | 254 | 44,88% | -0,00% |
| BTC | SETTIMANALE | Classic technical | 103 | 34,95% | -3,39% |
| BTC | SETTIMANALE | Famiglia statistica | 254 | 57,87% | +2,37% |
| BTC | SETTIMANALE | Microstruttura exchange | 26 | 23,08% | -1,70% |
| BTC | SETTIMANALE | Tecnico | 239 | 42,68% | -0,75% |
| BTC | SWING | Classic technical | 61 | 32,79% | -4,50% |
| BTC | SWING | Famiglia statistica | 152 | 67,76% | +6,11% |
| BTC | SWING | Microstruttura exchange | 15 | 46,67% | -0,24% |
| BTC | SWING | Tecnico | 140 | 54,29% | +1,16% |
| BTC | MEDIO | Classic technical | 59 | 52,54% | -7,40% |
| BTC | MEDIO | Famiglia statistica | 164 | 96,95% | +18,70% |
| BTC | MEDIO | Microstruttura exchange | 9 | 100,00% | +9,68% |
| BTC | MEDIO | Tecnico | 147 | 55,78% | -1,92% |
| DOGE | BREVE | Classic technical | 155 | 41,29% | -1,05% |
| DOGE | BREVE | Famiglia statistica | 272 | 56,25% | +0,67% |
| DOGE | BREVE | Microstruttura exchange | 35 | 51,43% | +2,23% |
| DOGE | BREVE | Tecnico | 254 | 51,18% | +0,17% |
| DOGE | SETTIMANALE | Classic technical | 143 | 34,97% | -5,18% |
| DOGE | SETTIMANALE | Famiglia statistica | 257 | 55,64% | +1,75% |
| DOGE | SETTIMANALE | Microstruttura exchange | 33 | 45,45% | +1,16% |
| DOGE | SETTIMANALE | Tecnico | 239 | 47,70% | -1,21% |
| DOGE | SWING | Classic technical | 87 | 40,23% | -6,65% |
| DOGE | SWING | Famiglia statistica | 152 | 63,16% | +4,41% |
| DOGE | SWING | Microstruttura exchange | 22 | 54,55% | +0,99% |
| DOGE | SWING | Tecnico | 140 | 47,86% | -2,69% |
| DOGE | MEDIO | Classic technical | 99 | 21,21% | -16,10% |
| DOGE | MEDIO | Famiglia statistica | 162 | 65,43% | +7,76% |
| DOGE | MEDIO | Microstruttura exchange | 22 | 72,73% | +12,54% |
| DOGE | MEDIO | Tecnico | 143 | 30,07% | -10,81% |
| SOL | BREVE | Classic technical | 177 | 45,76% | +0,05% |
| SOL | BREVE | Famiglia statistica | 257 | 51,36% | +0,72% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 251 | 45,42% | -0,13% |
| SOL | SETTIMANALE | Classic technical | 173 | 45,09% | -0,26% |
| SOL | SETTIMANALE | Famiglia statistica | 242 | 61,57% | +3,66% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 236 | 41,95% | -1,68% |
| SOL | SWING | Classic technical | 102 | 49,02% | -1,01% |
| SOL | SWING | Famiglia statistica | 143 | 80,42% | +11,54% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 138 | 44,20% | -4,30% |
| SOL | MEDIO | Classic technical | 100 | 37,00% | -19,23% |
| SOL | MEDIO | Famiglia statistica | 150 | 82,67% | +22,94% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 12 | 100,00% | +28,96% |
| SOL | MEDIO | Tecnico | 150 | 32,67% | -20,40% |

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

Generato: 2026-10-18 05:33 UTC

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
| BTC | +3 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | Prima resistenza sopra 84.249; conferma del eve and adam bottom sopra 82.262. | Sotto 80.337 il quadro tecnico peggiora. |
| SOL | -1 | DEBOLE / FRAGILE | Fragile | BASSA / RACCOLTA DATI | TAKE PROFIT SU SPIKE / NON INSEGUIRE | conferma del doppio minimo sopra 107,12; nuova conferma tecnica sopra 123,48. | Allarmi sotto 96,23. |
| DOGE | -2 | DEBOLE / FRAGILE | Fragile | BASSA / RACCOLTA DATI | EVITA LONG / SOLO RIMBALZI VELOCI | Sopra 0.10528 migliora; sopra 0.07997 viene invalidato il pattern ribassista dominante. | Sotto 0.07841 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | 0 | +2 | 0 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +3 |
| SOL | +2 | 0 | +2 | 0 | -2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | -1 |
| DOGE | +3 | 0 | +3 | 0 | -3 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | -2 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+3**
- Affidabilità: **MEDIA**
- Azione coerente: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**

BTC è l'asset messo meglio nel breve, ma lo score statistico ora conta Scanner e Market Regime una sola volta. La struttura macro resta debole: ha più senso accumulare a tranche sui pullback che inseguire il prezzo vicino alle resistenze.

Dettaglio moduli:

- Famiglia statistica: **+2** — Scanner grezzo +2, Market Regime grezzo 0, match regime 1. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+2** — Casi positivi 60,00%, return centrale 30g +6,96%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 1, positivi 30g 100,00%, return p50 +8,23%.
- Scanner path: **0** — Controlli disponibili 91. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+1** — Score tecnico 1/12, verdetto neutrale / misto, trend rialzista, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff range / fase non chiara, pattern score +1 (rialzista Eve and Adam Bottom / MATURO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 2 / MARKUP, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff DISTRIBUZIONE POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Fractal path: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- RSI top-cycle: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.00; exchange 3/3, copertura 100%, consenso bull 0, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — BTC: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Prima resistenza sopra 84.249; conferma del eve and adam bottom sopra 82.262.

Invalidazioni: Sotto 80.337 il quadro tecnico peggiora.

### SOL

- Confluenza: **DEBOLE / FRAGILE**
- Bias: **Fragile**
- Punteggio finale: **-1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **TAKE PROFIT SU SPIKE / NON INSEGUIRE**

SOL è fragile nel breve. Il frattale da solo non basta: se non recupera le conferme e il gap non rientra, il rischio è di inseguire uno spike scaricato.

Dettaglio moduli:

- Famiglia statistica: **+2** — Scanner grezzo +2, Market Regime grezzo 0, match regime 3. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+2** — Casi positivi 60,00%, return centrale 30g +6,24%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 3, positivi 30g 66,67%, return p50 +8,23%.
- Scanner path: **0** — Controlli disponibili 91. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -4/12, verdetto debole, trend misto, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff range / fase non chiara, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Triplo massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -1/12, verdetto NEUTRALE / MISTO, stage STAGE 2 / MARKUP, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff RANGE / FASE NON CHIARA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Fractal path: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- RSI top-cycle: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 3, bias SQUEEZE SETUP MODERATO, EMA200 111,34 $, upside EMA200 +7,74%, gap EMA50/EMA200 -4,47%, hit EMA200 12w +80,00%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 0, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — SOL: cambiamento forte in peggioramento rispetto a ieri.

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

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 75,00%, return centrale 30g +11,17%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 91. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-3** — Score tecnico -7/12, verdetto ribassista tecnico, trend ribassista, struttura volatilità in espansione, divergenza nessuna, Wyckoff range / fase non chiara, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -11/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Fractal path: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- RSI top-cycle: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
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

Generato: 2026-10-18 05:33 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 81.615 $ | prezzo corrente |
| Power Law centrale | 126.894 $ | deviazione -35,68% |
| Banda p10-p90 | 79.290 $ / 321.059 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 12,69% | posizione storica nel corridoio |
| Esponente β | 5,7811 | R² log-log 91,94% |
| Stabilità β | BASSA | range 1,3154 cambiando finestra |
| Ultimo halving | 2024-04-19 | 912 giorni fa |
| Fase ciclo | 62,42% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-10-18 (4414 osservazioni)
- Formula stimata: prezzo ≈ exp(-38.8757) × giorni^5.7811
- Prezzo centrale oggi: **126.894 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 12,69%
- Scarto dal centro: **-35,68%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,7811 | 91,94% |
| 2015 | 5,8605 | 91,49% |
| 2016 | 5,5420 | 87,78% |
| 2017 | 4,8191 | 83,09% |
| 2018 | 4,5451 | 78,69% |

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
| 2012-11-28 → 2016-07-09 | 2015-03-01 | -6,14% | -10,32% | -11,07% | +68,21% |
| 2016-07-09 → 2020-05-11 | 2018-12-01 | -11,20% | -8,43% | +97,39% | +76,15% |
| 2020-05-11 → 2024-04-19 | 2022-10-26 | -20,46% | +8,98% | +32,52% | +64,45% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | 1 | 0 | -4.733284277380534 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -7 | -1 | -9.44146679002812 | 0 |

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

Generato: 2026-10-18 05:33 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00126800 | +1 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | -4,73% | RIBASSISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000097 | -7 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -9,44% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (+1)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g -4,45%; 30g -4,73%; 90g +7,37%; 180g +12,71%
- **Daily:** RSI 31.76; MA50 0.00134316; MA200 0.00120216
- **Weekly:** MA30 0.00120610; RSI 49.51
- **Livelli:** supporto 0.00126200; resistenza 0.00129400; breakout 60g 0.00146600; breakdown 60g 0.00117400
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00133900; target 0.00140150
- **Fibonacci:** VICINO — 38.2% a 0.00129143
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in salita; RSI relativo debole; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-7)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g -6,31%; 30g -9,44%; 90g -13,35%; 180g -22,84%
- **Daily:** RSI 29.21; MA50 0.00000108; MA200 0.00000121
- **Weekly:** MA30 0.00000121; RSI 34.42
- **Livelli:** supporto 0.00000095; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000096
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000109
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; RSI relativo debole; MACD relativo negativo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 212 | 52,36% | +1,92% | -1,06% |
| SOL | 30g | 209 | 47,85% | +4,56% | +0,63% |
| SOL | 90g | 202 | 52,97% | +9,80% | +3,12% |
| DOGE | 7g | 297 | 55,56% | +1,81% | -1,68% |
| DOGE | 30g | 296 | 53,04% | +1,99% | -3,49% |
| DOGE | 90g | 291 | 54,64% | +6,92% | -9,23% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 52 | 48,08% | -0,01% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 52 | 44,23% | +0,06% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 52 | 36,54% | -0,67% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 47 | 38,30% | -1,17% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 35 | 57,14% | -0,22% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 66 | 68,18% | +0,23% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 65 | 64,62% | +0,48% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 61 | 59,02% | +0,19% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 56 | 51,79% | -0,22% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 54 | 57,41% | +0,40% | LOCKED / RACCOLTA LIVE | 0 |

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
| Trend squeeze | STABILE / DA CONFERMARE |
| Trend squeeze score | 0 |
| Confronto precedente | 2026-10-12 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 103,44 $ |
| EMA200 weekly target | 111,34 $ |
| Upside verso EMA200 | +7,74% |
| Distanza prezzo da EMA200 | -7,19% |
| Gap EMA50/EMA200 | -4,47% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 53,04 |
| Età SOL | 6,5 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +80,00% |
| Max gain mediano 12w | +33,33% |
| Drawdown mediano 12w | -36,42% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-10-18 05:33 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-10-18 05:30:22 UTC**

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
- DOGE: cambiamento importante in peggioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | NESSUN CAMBIAMENTO FORTE | peggioramento | RIALZISTA | +60.00% | 0.00 punti |
| SOL | CAMBIAMENTO FORTE | peggioramento | RIALZISTA | +60.00% | -12.50 punti |
| DOGE | CAMBIAMENTO MEDIO | peggioramento | RIALZISTA | +75.00% | 0.00 punti |

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
| BTC | 77.560 $ | 89.806 $ | +30,77% | +15,79% | rimbalzo poco frequente | 89.806 $ | 77.560 $ | +16,00% | -13,64% | spike storicamente più resistente |
| SOL | 98,27 $ | 113,78 $ | +24,00% | +15,79% | rimbalzo poco frequente | 113,78 $ | 98,27 $ | +20,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07519 $ | 0,08706 $ | +37,50% | +15,79% | rimbalzo debole | 0,08706 $ | 0,07519 $ | +3,23% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 26 prima sono scesi a -5,00%. Tra quei 26, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +30,77% (8/26). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 4 poi sono scaricati a -5,00%. Percentuale: +16,00% (4/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +24,00% (6/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 5 poi sono scaricati a -5,00%. Percentuale: +20,00% (5/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 16 prima sono scesi a -5,00%. Tra quei 16, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +37,50% (6/16). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **DOGE: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 1 poi sono scaricati a -5,00%. Percentuale: +3,23% (1/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-10-18 05:32:55 UTC

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-10-18 | 2026-10-18T05:30:21Z | 2026-10-18 05:30:22 |
| SOL | 2026-10-18 | 2026-10-18T05:30:21Z | 2026-10-18 05:30:22 |
| DOGE | 2026-10-18 | 2026-10-18T05:30:21Z | 2026-10-18 05:30:22 |

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
| BTC | 2026-10-18 | 81.642 $ | SALITA | 60,00% | 66.963,94 $ | 78.407,37 $ | 87.321,03 $ | 97.265,24 $ | 107.922,78 $ |
| SOL | 2026-10-18 | 103,44 $ | SALITA | 60,00% | 79,04 $ | 100,43 $ | 109,89 $ | 117,83 $ | 133,86 $ |
| DOGE | 2026-10-18 | 0.07915 $ | SALITA | 75,00% | 0.07098 $ | 0.08048 $ | 0.08799 $ | 0.09454 $ | 0.10262 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | AVAILABLE | SAME_BTC_REGIME | 1 | 2 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 87.321,03 $ | 87.661,06 $ | 107.922,78 $ | 141.384,19 $ |
| SOL | AVAILABLE | SAME_BTC_REGIME | 3 | 4 | 14 | 14 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 109,89 $ | 111,07 $ | 133,86 $ | 126,09 $ |
| DOGE | AVAILABLE | SAME_BTC_REGIME | 0 | 0 | 5 | 5 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.08799 $ | 0.08141 $ | 0.10262 $ | 0.18138 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-09-17**; verificato fino al **2026-10-17**; stato **COMPLETO 30/30g**.
- Reale **81.629,35 $**; p50 previsto **95.088,83 $**; scarto **-14,15%**.
- Errore medio assoluto **6,73%**; massimo **17,03%**; DENTRO p10-p90; FUORI p25-p75.

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

**Campione corrente:** 6 episodi qualificati su 40 · 6 asset distinti.

**SMALL SAMPLE / DIAGNOSTIC ONLY:** le frequenze empiriche non sono probabilità calibrate.

![SOL conditional successor corrente](scanner_forecast_SOL_conditional_successor_current.png)

###### Confronto diretto a 30 giorni

| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Cono standard | 2026-10-18 | 40 | 2026-11-17 | 79.04 $ | 100.43 $ | 109.89 $ | 117.83 $ | 133.86 $ |
| Conditional corrente | 2026-10-18 | 6 | 2026-11-17 | 69.49 $ | 76.65 $ | 85.02 $ | 101.63 $ | 191.60 $ |

###### Struttura successiva dei casi correnti

| Classe | Episodi | Frequenza empirica |
| --- | ---: | ---: |
| DIRECT_CONTINUATION | 1 | 16.67% |
| SHALLOW_PULLBACK_THEN_CONTINUATION | 1 | 16.67% |
| DEEP_PULLBACK_THEN_RECOVERY | 0 | 0.00% |
| FAILURE | 4 | 66.67% |
| UNRESOLVED | 0 | 0.00% |

###### Episodi qualificati oggi

| Asset | Match window | -5% hit | +10% anchor | Classe 60d |
| --- | --- | --- | --- | --- |
| MKR-USD | 2019-01-08 → 2019-04-17 | 2019-04-21 | 2019-05-15 | FAILURE |
| HBAR-USD | 2022-12-04 → 2023-03-13 | 2023-03-15 | 2023-03-31 | FAILURE |
| DOGE-USD | 2024-01-16 → 2024-04-24 | 2024-04-29 | 2024-05-21 | FAILURE |
| ENJ-USD | 2022-12-07 → 2023-03-16 | 2023-03-27 | 2023-04-07 | FAILURE |
| VET-USD | 2020-04-23 → 2020-07-31 | 2020-08-02 | 2020-08-06 | SHALLOW_PULLBACK_THEN_CONTINUATION |
| RUNE-USD | 2023-07-06 → 2023-10-13 | 2023-10-17 | 2023-10-22 | DIRECT_CONTINUATION |

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

- Ultimo close disponibile: **2026-10-18** · SOL **103.35 $**.
- Giorno del vintage: **30/30**.
- P50 condizionato previsto per quel giorno: **168.54 $**.
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

- Cono congelato il **2026-09-17**; verificato fino al **2026-10-17**; stato **COMPLETO 30/30g**.
- Reale **103,35 $**; p50 previsto **120,71 $**; scarto **-14,39%**.
- Errore medio assoluto **11,24%**; massimo **17,80%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted SOL](scanner_forecast_SOL_regime_adjusted.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-09-17**; verificato fino al **2026-10-17**; stato **COMPLETO 30/30g**.
- Reale **0.07911 $**; p50 previsto **0.06760 $**; scarto **17,02%**.
- Errore medio assoluto **18,56%**; massimo **31,62%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted DOGE](scanner_forecast_DOGE_regime_adjusted.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 91 | 94,51% | 71,43% | 1,82% | 0,32% |
| BTC | 3g | 88 | 94,32% | 79,55% | 3,03% | 0,55% |
| BTC | 7g | 80 | 93,75% | 72,50% | 4,82% | 0,99% |
| BTC | 14g | 66 | 98,48% | 77,27% | 5,90% | 0,39% |
| BTC | 30g | 40 | 100,00% | 67,50% | 12,00% | -4,64% |
| SOL | 1g | 91 | 85,71% | 62,64% | 2,65% | 0,50% |
| SOL | 3g | 88 | 92,05% | 72,73% | 3,81% | 1,22% |
| SOL | 7g | 80 | 92,50% | 73,75% | 5,78% | 2,14% |
| SOL | 14g | 66 | 89,39% | 77,27% | 8,17% | 4,34% |
| SOL | 30g | 40 | 95,00% | 70,00% | 14,89% | 4,33% |
| DOGE | 1g | 91 | 89,01% | 60,44% | 3,00% | 0,20% |
| DOGE | 3g | 88 | 92,05% | 63,64% | 4,62% | 0,85% |
| DOGE | 7g | 80 | 78,75% | 73,75% | 8,24% | 4,04% |
| DOGE | 14g | 66 | 86,36% | 53,03% | 10,33% | 7,14% |
| DOGE | 30g | 40 | 95,00% | 42,50% | 16,34% | 16,34% |

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
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **60,00%**
- Casi negativi / discesa storica: **40,00%**
- Quanto è netto il segnale: **debole**
- Prezzo attuale: **81.641,88 $**
- Return normale fra 30 giorni: **87.321,03 $** (6,96%)
- Drawdown normale durante il mese: **74.986,47 $** (-8,15%)
- Drawdown brutto da rispettare: **70.000,97 $** (-14,26%)
- Max gain normale durante il mese: **92.354,41 $** (13,12%)
- Max gain buono / take profit ottimistico: **103.284,30 $** (26,51%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **60,00%**
- Casi negativi / discesa storica: **40,00%**
- Quanto è netto il segnale: **debole**
- Prezzo attuale: **103,44 $**
- Return normale fra 30 giorni: **109,89 $** (6,24%)
- Drawdown normale durante il mese: **94,94 $** (-8,22%)
- Drawdown brutto da rispettare: **87,79 $** (-15,13%)
- Max gain normale durante il mese: **116,17 $** (12,31%)
- Max gain buono / take profit ottimistico: **124,20 $** (20,06%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **75,00%**
- Casi negativi / discesa storica: **25,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,08 $**
- Return normale fra 30 giorni: **0,09 $** (11,17%)
- Drawdown normale durante il mese: **0,08 $** (-4,25%)
- Drawdown brutto da rispettare: **0,07 $** (-9,33%)
- Max gain normale durante il mese: **0,09 $** (15,56%)
- Max gain buono / take profit ottimistico: **0,10 $** (24,15%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 81.641,88 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **60,00%**
- Probabilità storica di discesa: **40,00%**
- Quanto è netto il segnale: **debole**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale debole. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **66.963,94 $** (-17,98%)
- Se va male: **78.407,37 $** (-3,96%)
- Scenario normale: **87.321,03 $** (6,96%)
- Se va bene: **97.265,24 $** (19,14%)
- Se va molto bene: **107.922,78 $** (32,19%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **74.986,47 $** (-8,15%)
- Discesa brutta: **70.000,97 $** (-14,26%)
- Discesa molto brutta: **61.988,16 $** (-24,07%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **92.354,41 $** (13,12%)
- Rialzo buono: **103.284,30 $** (26,51%)
- Rialzo molto forte: **109.899,03 $** (34,61%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **74.986,47 $** e uno spike normale intorno a **92.354,41 $**.

La chiusura a 30 giorni era più spesso positiva: salita 60,00%, discesa 40,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 103,44 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **60,00%**
- Probabilità storica di discesa: **40,00%**
- Quanto è netto il segnale: **debole**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale debole. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **79,04 $** (-23,59%)
- Se va male: **100,43 $** (-2,91%)
- Scenario normale: **109,89 $** (6,24%)
- Se va bene: **117,83 $** (13,91%)
- Se va molto bene: **133,86 $** (29,41%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **94,94 $** (-8,22%)
- Discesa brutta: **87,79 $** (-15,13%)
- Discesa molto brutta: **57,85 $** (-44,08%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **116,17 $** (12,31%)
- Rialzo buono: **124,20 $** (20,06%)
- Rialzo molto forte: **136,50 $** (31,96%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **94,94 $** e uno spike normale intorno a **116,17 $**.

La chiusura a 30 giorni era più spesso positiva: salita 60,00%, discesa 40,00%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 0,08 $

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

- Se va molto male: **0,07 $** (-10,32%)
- Se va male: **0,08 $** (1,69%)
- Scenario normale: **0,09 $** (11,17%)
- Se va bene: **0,09 $** (19,44%)
- Se va molto bene: **0,10 $** (29,65%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,08 $** (-4,25%)
- Discesa brutta: **0,07 $** (-9,33%)
- Discesa molto brutta: **0,06 $** (-22,69%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,09 $** (15,56%)
- Rialzo buono: **0,10 $** (24,15%)
- Rialzo molto forte: **0,12 $** (45,78%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,08 $** e uno spike normale intorno a **0,09 $**.

La chiusura a 30 giorni era più spesso positiva: salita 75,00%, discesa 25,00%. Quindi la lettura principale è favorevole.

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

- Previsioni già controllate: **47**
- Direzione corretta: **92,50%**
- Errore medio dello scenario centrale: **10,45%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **2,13%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **47**
- Direzione corretta: **73,17%**
- Errore medio dello scenario centrale: **15,14%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **29,79%**
- Prezzo finale dentro lo scenario 10%-90%: **95,74%**

### Solana

- Previsioni già controllate: **47**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **12,96%**
- Zona rischio toccata: **4,26%**
- Zona rialzo media toccata: **23,40%**
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

- Previsioni controllate: **47**
- Previsioni usate per la calibrazione recente: **47**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **92,50%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **6,96%** → **87.321,03 $**
- Correzione imparata dagli errori: **-4,20%**
- Calibrato: **2,75%** → **83.888,69 $**
- Lettura: Lo scanner è stato troppo ottimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-8,15%** → **74.986,47 $**
- Correzione imparata dagli errori: **4,70%**
- Calibrato: **-3,45%** → **78.824,79 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **13,12%** → **92.354,41 $**
- Correzione imparata dagli errori: **-8,75%**
- Calibrato: **4,38%** → **85.213,81 $**
- Lettura: Lo scanner ha sovrastimato gli spike: nella realtà il prezzo è salito meno del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Solana

- Previsioni controllate: **47**
- Previsioni usate per la calibrazione recente: **47**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **100,00%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **6,24%** → **109,89 $**
- Correzione imparata dagli errori: **2,03%**
- Calibrato: **8,26%** → **111,99 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-8,22%** → **94,94 $**
- Correzione imparata dagli errori: **3,54%**
- Calibrato: **-4,67%** → **98,61 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **12,31%** → **116,17 $**
- Correzione imparata dagli errori: **-2,16%**
- Calibrato: **10,15%** → **113,94 $**
- Lettura: Lo scanner ha sovrastimato gli spike: nella realtà il prezzo è salito meno del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Dogecoin

- Previsioni controllate: **47**
- Previsioni usate per la calibrazione recente: **47**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **73,17%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **11,17%** → **0,09 $**
- Correzione imparata dagli errori: **15,14%**
- Calibrato: **26,31%** → **0,10 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-4,25%** → **0,08 $**
- Correzione imparata dagli errori: **14,01%**
- Calibrato: **9,76%** → **0,09 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **15,56%** → **0,09 $**
- Correzione imparata dagli errori: **3,56%**
- Calibrato: **19,12%** → **0,09 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 81.641,88 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **60,00%**
- Casi negativi dopo 30 giorni: **40,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,08%**
- Rendimento medio dopo 30 giorni: **12,12%**
- Rendimento centrale dopo 30 giorni: **6,96%**
- Discesa media durante i 30 giorni: **-9,98%**
- Massimo rialzo medio durante i 30 giorni: **21,77%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **91.540,52 $**
- Scenario centrale a 30 giorni: **87.321,03 $**
- Zona di rischio media: **73.497,09 $**
- Zona di rialzo media: **99.417,13 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -17,98% → **66.963,94 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -3,96% → **78.407,37 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 6,96% → **87.321,03 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 19,14% → **97.265,24 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 32,19% → **107.922,78 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -24,07% → **61.988,16 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -14,26% → **70.000,97 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -8,15% → **74.986,47 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -1,99% → **80.017,70 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **81.641,88 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 2,02% → **83.294,22 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 6,16% → **86.670,01 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 13,12% → **92.354,41 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 26,51% → **103.284,30 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 34,61% → **109.899,03 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| BTC-USD         | 2022-12-05   | 2023-03-14 |        89.89 |        22.84 |          -1.5  |          22.84 |
| AVAX-USD        | 2021-07-06   | 2021-10-13 |        87.75 |        53.62 |           0    |          65.33 |
| RUNE-USD        | 2023-07-06   | 2023-10-13 |        87.56 |       209.44 |          -8.28 |         209.44 |
| ETH-USD         | 2022-12-02   | 2023-03-11 |        86.95 |        28.91 |           0    |          28.91 |
| XTZ-USD         | 2019-09-29   | 2020-01-06 |        86.79 |        64.01 |          -1.99 |          64.01 |
| QTUM-USD        | 2023-09-13   | 2023-12-21 |        86.57 |        -7.79 |         -10.59 |          12.02 |
| MKR-USD         | 2019-01-08   | 2019-04-17 |        86.54 |        -2.87 |         -22.97 |          10.6  |
| VET-USD         | 2020-04-23   | 2020-07-31 |        86.07 |        -0.71 |          -7.67 |          26.65 |
| LRC-USD         | 2020-11-22   | 2021-03-01 |        85.97 |        -6.75 |         -23.24 |           6.97 |
| CRV-USD         | 2022-12-01   | 2023-03-10 |        85.8  |        14.31 |          -2.49 |          15.59 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 103,44 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **60,00%**
- Casi negativi dopo 30 giorni: **40,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **88,04%**
- Rendimento medio dopo 30 giorni: **9,68%**
- Rendimento centrale dopo 30 giorni: **6,24%**
- Discesa media durante i 30 giorni: **-13,52%**
- Massimo rialzo medio durante i 30 giorni: **20,24%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **113,45 $**
- Scenario centrale a 30 giorni: **109,89 $**
- Zona di rischio media: **89,46 $**
- Zona di rialzo media: **124,37 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -23,59% → **79,04 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -2,91% → **100,43 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 6,24% → **109,89 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 13,91% → **117,83 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 29,41% → **133,86 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -44,08% → **57,85 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -15,13% → **87,79 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -8,22% → **94,94 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -2,96% → **100,38 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,92% → **102,49 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,78% → **105,28 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 6,78% → **110,45 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 12,31% → **116,17 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 20,06% → **124,20 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 31,96% → **136,50 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| AVAX-USD        | 2021-07-06   | 2021-10-13 |        91.16 |        53.62 |           0    |          65.33 |
| XTZ-USD         | 2019-09-29   | 2020-01-06 |        90.94 |        64.01 |          -1.99 |          64.01 |
| MKR-USD         | 2019-01-08   | 2019-04-17 |        90.27 |        -2.87 |         -22.97 |          10.6  |
| BTC-USD         | 2022-12-05   | 2023-03-14 |        90.1  |        22.84 |          -1.5  |          22.84 |
| HBAR-USD        | 2022-12-04   | 2023-03-13 |        89.95 |        -0.27 |          -8.15 |          13.87 |
| MKR-USD         | 2020-11-23   | 2021-03-02 |        89.26 |         5.95 |         -15.96 |           5.95 |
| VET-USD         | 2022-12-04   | 2023-03-13 |        89.04 |         4.26 |          -6.95 |           6.23 |
| CRV-USD         | 2022-12-01   | 2023-03-10 |        88.69 |        14.31 |          -2.49 |          15.59 |
| BCH-USD         | 2019-11-28   | 2020-03-06 |        88.68 |       -33.5  |         -56.37 |           0    |
| THETA-USD       | 2022-12-06   | 2023-03-15 |        88.63 |        11.19 |          -4.01 |          11.19 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 0,08 $

Dogecoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **75,00%**
- Casi negativi dopo 30 giorni: **25,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **83,66%**
- Rendimento medio dopo 30 giorni: **14,74%**
- Rendimento centrale dopo 30 giorni: **11,17%**
- Discesa media durante i 30 giorni: **-9,00%**
- Massimo rialzo medio durante i 30 giorni: **24,41%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,09 $**
- Scenario centrale a 30 giorni: **0,09 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,10 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -10,32% → **0,07 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 1,69% → **0,08 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 11,17% → **0,09 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 19,44% → **0,09 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 29,65% → **0,10 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -22,69% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -9,33% → **0,07 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -4,25% → **0,08 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -0,20% → **0,08 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **0,08 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 2,32% → **0,08 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 10,47% → **0,09 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 15,56% → **0,09 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 24,15% → **0,10 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 45,78% → **0,12 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XTZ-USD         | 2019-09-29   | 2020-01-06 |        88.53 |        64.01 |          -1.99 |          64.01 |
| KSM-USD         | 2022-12-05   | 2023-03-14 |        86.89 |        -1.2  |         -11.82 |           2.11 |
| AAVE-USD        | 2022-12-05   | 2023-03-14 |        86.15 |         2.34 |         -12.06 |           2.34 |
| ICP-USD         | 2022-12-05   | 2023-03-14 |        85.65 |        -1.17 |         -13.98 |           1.98 |
| ENJ-USD         | 2022-12-07   | 2023-03-16 |        85.62 |        13.78 |          -5.95 |          20.75 |
| LINK-USD        | 2019-08-25   | 2019-12-02 |        85.61 |       -13.76 |         -16.16 |           8.39 |
| BTC-USD         | 2022-12-05   | 2023-03-14 |        85.58 |        22.84 |          -1.5  |          22.84 |
| THETA-USD       | 2022-12-06   | 2023-03-15 |        85.49 |        11.19 |          -4.01 |          11.19 |
| HBAR-USD        | 2022-12-04   | 2023-03-13 |        85.45 |        -0.27 |          -8.15 |          13.87 |
| VET-USD         | 2022-12-04   | 2023-03-13 |        85.38 |         4.26 |          -6.95 |           6.23 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report

Generated: 2026-10-18 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-18 | BULL | 81.642 $ | True | 25.16% | 4.97% | BULL | 25.16% | 4.97% |
| DOGE-USD | 2026-10-18 | RECOVERY | 0.07915 $ | False | 9.72% | -2.50% | BULL | 25.16% | 4.97% |
| SOL-USD | 2026-10-18 | BULL | 103,44 $ | True | 32.97% | 7.62% | BULL | 25.16% | 4.97% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 60.00% | 6.96% | 19.14% | 32.19% | -8.15% | -24.07% | 13.12% | 26.51% | 34.61% | 47.50% | -1.95% | 20.58% | 60.31% |
| BTC-USD | SAME_BTC_REGIME | 8 | 75.00% | 7.37% | 10.95% | 73.18% | -9.00% | -18.14% | 11.48% | 13.90% | 73.18% | 25.00% | -19.54% | 26.62% | 157.17% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 100.00% | 21.09% | 27.52% | 31.38% | -9.17% | -13.05% | 28.19% | 35.97% | 40.64% | 50.00% | 9.08% | 23.23% | 31.72% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 8.23% | 8.23% | 8.23% | -14.02% | -14.02% | 12.63% | 12.63% | 12.63% | 0.00% | -19.22% | -19.22% | -19.22% |
| DOGE-USD | ALL_MATCHES | 40 | 75.00% | 11.17% | 19.44% | 29.65% | -4.25% | -22.69% | 15.56% | 24.15% | 45.78% | 42.50% | -7.17% | 17.92% | 65.47% |
| DOGE-USD | SAME_BTC_REGIME | 5 | 60.00% | 2.85% | 8.74% | 129.16% | -8.50% | -17.36% | 11.30% | 17.27% | 132.58% | 80.00% | 41.88% | 126.27% | 197.10% |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 60.00% | 6.24% | 13.91% | 29.41% | -8.22% | -44.08% | 12.31% | 20.06% | 31.96% | 35.00% | -8.97% | 15.09% | 52.54% |
| SOL-USD | SAME_BTC_REGIME | 14 | 71.43% | 7.37% | 9.87% | 21.90% | -8.97% | -20.02% | 12.31% | 14.48% | 26.64% | 35.71% | -9.97% | 40.11% | 99.40% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 75.00% | 9.08% | 15.94% | 26.75% | -9.17% | -15.52% | 12.31% | 20.41% | 34.42% | 50.00% | 13.29% | 35.44% | 36.60% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 3 | 66.67% | 8.23% | 9.08% | 9.59% | -14.02% | -15.73% | 11.98% | 12.31% | 12.50% | 33.33% | -8.21% | 13.29% | 26.19% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 29 | 62.07% | 9.64% | -6.95% | 28.53% | 51.72% | 3.50% | 44.59% |
| BTC-USD | HISTORICAL_BTC_BULL | 8 | 75.00% | 7.37% | -9.00% | 13.90% | 25.00% | -19.54% | 50.64% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 3 | 0.00% | -7.79% | -10.59% | 10.60% | 66.67% | 1.35% | 16.78% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 35 | 77.14% | 11.57% | -4.01% | 24.48% | 37.14% | -7.89% | 32.54% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 60.00% | 2.85% | -8.50% | 17.27% | 80.00% | 41.88% | 169.44% |
| SOL-USD | HISTORICAL_BTC_BEAR | 26 | 53.85% | 3.30% | -7.31% | 22.32% | 34.62% | -8.51% | 27.79% |
| SOL-USD | HISTORICAL_BTC_BULL | 14 | 71.43% | 7.37% | -8.97% | 14.48% | 35.71% | -9.97% | 41.83% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 29 | 62.07% | 9.64% | -7.67% | 26.65% | 51.72% | 3.50% | 42.99% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 21.09% | -9.17% | 35.97% | 50.00% | 9.08% | 51.74% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 5.95% | -15.96% | 19.58% | 33.33% | -3.38% | 82.21% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -27.42% | -31.31% | 0.00% | 0.00% | -37.46% | 0.00% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 40.00% | -7.37% | -9.50% | 12.02% | 40.00% | -12.41% | 13.61% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 37 | 75.68% | 11.19% | -4.13% | 23.82% | 37.84% | -7.89% | 32.79% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | 10.09% | -10.24% | 34.91% | 100.00% | 36.08% | 57.76% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 8.74% | -4.86% | 17.27% | 100.00% | 41.88% | 42.76% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 58.62% | 5.27% | -7.67% | 22.84% | 34.48% | -9.73% | 28.04% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 9.08% | -9.17% | 20.41% | 50.00% | 13.29% | 45.29% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | -0.40% | -18.82% | 11.54% | 50.00% | 18.71% | 62.03% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 66.67% | 6.52% | -9.50% | 11.96% | 0.00% | -26.27% | 11.96% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 1 | 2 | 8 | 8 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 0 | 5 | 5 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_BTC_REGIME | 3 | 4 | 14 | 14 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-06 | 87.56% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 209.44% | -8.28% | 209.44% | 244.33% | -8.28% | 326.83% |
| BTC-USD | LRC-USD | 2020-11-22 | 85.97% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -6.75% | -23.24% | 6.97% | -4.45% | -25.70% | 27.57% |
| BTC-USD | XLM-USD | 2025-05-30 | 85.71% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 14.78% | -1.65% | 14.78% | -21.24% | -24.08% | 14.78% |
| BTC-USD | MKR-USD | 2020-11-23 | 85.36% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| BTC-USD | ETH-USD | 2025-05-30 | 84.73% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 9.67% | -9.50% | 10.32% | -19.86% | -22.97% | 10.32% |
| BTC-USD | ADA-USD | 2025-05-30 | 84.63% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| BTC-USD | HBAR-USD | 2025-06-01 | 84.57% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -8.50% | 9.54% | -21.94% | -28.23% | 9.54% |
| BTC-USD | DOGE-USD | 2024-01-16 | 83.69% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | 8.23% | -14.02% | 12.63% | -19.22% | -19.22% | 14.94% |
| DOGE-USD | LINK-USD | 2019-08-25 | 85.61% | BULL | BULL | SAME_BTC_ONLY | BEARISH_30D | -13.76% | -16.16% | 8.39% | 34.79% | -16.89% | 39.05% |
| DOGE-USD | ZEC-USD | 2024-05-30 | 83.32% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 8.74% | -4.86% | 17.27% | 41.88% | -4.86% | 42.76% |
| DOGE-USD | MKR-USD | 2020-11-28 | 82.71% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 2.85% | -18.16% | 11.30% | 126.27% | -18.16% | 169.44% |
| DOGE-USD | RUNE-USD | 2023-07-06 | 82.53% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 209.44% | -8.28% | 209.44% | 244.33% | -8.28% | 326.83% |
| DOGE-USD | HBAR-USD | 2025-06-01 | 82.45% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -8.50% | 9.54% | -21.94% | -28.23% | 9.54% |
| SOL-USD | MKR-USD | 2020-11-23 | 89.26% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 5.95% | -15.96% | 5.95% | 119.82% | -15.96% | 119.82% |
| SOL-USD | DOGE-USD | 2024-01-16 | 88.22% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | 8.23% | -14.02% | 12.63% | -19.22% | -19.22% | 14.94% |
| SOL-USD | ZEC-USD | 2024-05-30 | 88.08% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 8.74% | -4.86% | 17.27% | 41.88% | -4.86% | 42.76% |
| SOL-USD | LINK-USD | 2019-08-25 | 88.04% | BULL | BULL | SAME_BTC_AND_ASSET | BEARISH_30D | -13.76% | -16.16% | 8.39% | 34.79% | -16.89% | 39.05% |
| SOL-USD | TRX-USD | 2025-05-30 | 87.97% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | 9.94% | 0.00% | 11.98% | -8.21% | -10.70% | 11.98% |
| SOL-USD | ETH-USD | 2025-05-30 | 87.69% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 9.67% | -9.50% | 10.32% | -19.86% | -22.97% | 10.32% |
| SOL-USD | MKR-USD | 2023-05-17 | 87.55% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 24.95% | -1.75% | 30.65% | 51.74% | -1.75% | 51.74% |
| SOL-USD | SNX-USD | 2020-11-22 | 87.53% | BULL | DISTRIBUTION | SAME_BTC_ONLY | BEARISH_30D | -14.46% | -21.67% | 9.63% | -11.74% | -33.57% | 9.63% |
| SOL-USD | ADA-USD | 2025-05-30 | 87.47% | BULL | RECOVERY | SAME_BTC_ONLY | MIXED | 6.52% | -6.80% | 13.61% | -33.27% | -36.28% | 13.61% |
| SOL-USD | HBAR-USD | 2025-06-01 | 87.20% | BULL | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -8.50% | 9.54% | -21.94% | -28.23% | 9.54% |

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

Generato: 2026-10-18 05:33 UTC

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
| BTC | 81.642 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 2 / MARKUP | MASSIMI E MINIMI DECRESCENTI | DISTRIBUZIONE POSSIBILE | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 103,44 $ | -1 | NEUTRALE / MISTO | STAGE 2 / MARKUP | MASSIMI E MINIMI DECRESCENTI | RANGE / FASE NON CHIARA | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.07915 $ | -11 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | MARKDOWN / DEBOLEZZA | MEDIO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +4 | -2 | 0 | -2 | 0 | 0 | -2 | -2 |
| SOL | +4 | -2 | -1 | -2 | 0 | 0 | 0 | -1 |
| DOGE | -3 | -2 | -1 | -2 | 0 | -1 | -2 | -11 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 80.337 $ | 82.262 $ | 87.364 $ | 62.488 $ | 2,56% | 6,84% | 26,18% |
| SOL | 98,63 $ | 105,49 $ | 124,62 $ | 74,20 $ | 4,34% | 1,71% | 35,34% |
| DOGE | 0.07841 $ | 0.07923 $ | 0.10528 $ | 0.06919 $ | 4,81% | -3,24% | 9,35% |

## Lettura dettagliata

### BTC

- Prezzo: **81.642 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,56%; distanza supporto 1,61%; distanza resistenza 0,78%

Dettaglio:

- Trend: **+4** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in salita; STAGE 2 / MARKUP
- Stage weekly: **STAGE 2 / MARKUP** — Prezzo sopra MA30 weekly con MA30 in salita.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **0** — RSI neutrale 47.0; MACD sotto signal; istogramma MACD in miglioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.13; volume ratio 0.44
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — DISTRIBUZIONE POSSIBILE. Prezzo alto nel range ma CMF negativo: possibile distribuzione.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 47.00 |
| MACD histogram | -511.13126 |
| CMF20 | -0.134 |
| Volume ratio 20 | 0.44 |
| MA20 | 83.420 $ |
| MA50 | 81.328 $ |
| MA100 | 74.025 $ |
| MA200 | 72.427 $ |
| Pendenza MA50 20g | +6,86% |
| Pendenza MA200 60g | +4,90% |
| Bollinger width | 7,42% |
| Bollinger position | 0.20 |

### SOL

- Prezzo: **103,44 $**
- Score classico: **-1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 4,34%; distanza supporto 4,78%; distanza resistenza 2,08%

Dettaglio:

- Trend: **+4** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in salita; STAGE 2 / MARKUP
- Stage weekly: **STAGE 2 / MARKUP** — Prezzo sopra MA30 weekly con MA30 in salita.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **-1** — RSI debole 37.3; MACD sotto signal; istogramma MACD in miglioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.20; volume ratio 0.49
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Doji / indecisione
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 37.33 |
| MACD histogram | -1.84964 |
| CMF20 | -0.203 |
| Volume ratio 20 | 0.49 |
| MA20 | 113,05 $ |
| MA50 | 109,35 $ |
| MA100 | 94,48 $ |
| MA200 | 87,46 $ |
| Pendenza MA50 20g | +10,87% |
| Pendenza MA200 60g | +7,48% |
| Bollinger width | 25,83% |
| Bollinger position | 0.14 |

### DOGE

- Prezzo: **0.07915 $**
- Score classico: **-11 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **MEDIO** — ATR14 4,81%; distanza supporto 0,85%; distanza resistenza 0,21%

Dettaglio:

- Trend: **-3** — prezzo sotto MA200 daily; MA50 daily in salita; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **-1** — RSI debole 34.9; MACD sotto signal; istogramma MACD in miglioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.20; volume ratio 0.52
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **-1** — Shooting star / rejection alto
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 34.94 |
| MACD histogram | -0.00136 |
| CMF20 | -0.204 |
| Volume ratio 20 | 0.52 |
| MA20 | 0.08836 $ |
| MA50 | 0.08810 $ |
| MA100 | 0.08117 $ |
| MA200 | 0.08732 $ |
| Pendenza MA50 20g | +4,68% |
| Pendenza MA200 60g | -2,66% |
| Bollinger width | 29,44% |
| Bollinger position | 0.10 |

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

Generato: 2026-10-18 05:33 UTC

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
| BTC | 81.642 $ | Eve and Adam Bottom | MATURO | rialzista | 2026-09-21 | 89.580 $ | -8,48% | n/a | Fib 23,6% NON ATTIVO (0) @ 77.995 $ | NEL RANGE | 80.337 $ |
| SOL | 103,44 $ | Triplo massimo | CANDIDATO | ribassista | n/a | 62,51 $ | n/a | 46,32% | Fib 38,2% TENUTO (+1) @ 103,32 $ | NEL RANGE | 97,45 $ |
| DOGE | 0.07915 $ | Doppio minimo | CANDIDATO | rialzista | n/a | 0.13028 $ | n/a | 33,01% | Fib 23,6% NON ATTIVO (0) @ 0.08689 $ | NEL RANGE | 0.07841 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Eve and Adam Bottom**
- Stato pattern: **MATURO** (+1)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-09-15**
- Età formazione: **33 giorni**
- Breakout pattern: **2026-09-21**
- Età breakout: **27 giorni**
- Neckline: **82.262 $**
- Target teorico: **89.580 $**
- Progresso verso target: **-8,48%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 77.995 $** — Swing UP 2026-07-01 57.748 -> 2026-10-12 84.249; livello più vicino 23.6% a 77.995; stato NON ATTIVO; confluenza: invalidazione ribassista.
- Invalidazione: **80.617 $**
- Relazione prezzo/neckline: **vicino alla neckline**
- Dettaglio: Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (27 giorni fa). Stato: MATURO. Target teorico: 89.580; progresso corrente: -8,48%. Relazione prezzo/neckline: vicino alla neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **80.337 $**
- Resistenza: **82.262 $**
- Breakout 60g: **87.364 $**
- Breakdown 60g: **62.488 $**
- RSI14: **47.05**
- ATR14: **2,56%**
- Volume ratio 20g: **0.44**
- Rendimento 30g: **+6,86%**
- Rendimento 90g: **+26,20%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Eve and Adam Bottom | MATURO | +1 | rialzista | 82.262 $ | 2026-09-21 | 27g | 89.580 $ | -8,48% | n/a | 80.617 $ | Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (27 giorni fa). Stato: MATURO. Target teorico: 89.580; progresso corrente: -8,48%. Relazione prezzo/neckline: vicino alla neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CONFERMATO RECENTE | -2 | ribassista | 82.571 $ | 2026-10-08 | 10g | 77.778 $ | 19,38% | n/a | 84.222 $ | Due massimi simili a 87.364 $ e 87.146 $. Neckline circa 82.571 $. Breakout neckline: 2026-10-08 (10 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 77.778 $; progresso: 19,38%; prezzo sotto neckline. |
| Doppio minimo | MATURO | +1 | rialzista | 82.262 $ | 2026-09-21 | 27g | 89.580 $ | -8,48% | n/a | 80.617 $ | Due minimi simili a 76.248 $ e 74.945 $. Neckline circa 82.262 $. Breakout neckline: 2026-09-21 (27 giorni fa). Stato: MATURO. Target teorico: 89.580 $; progresso: -8,48%; prezzo vicino alla neckline. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **70 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **70,69 $**
- Target teorico: **62,51 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **46,32%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 38,2% TENUTO (+1) @ 103,32 $** — Swing UP 2026-08-01 70,69 -> 2026-10-02 123,48; livello più vicino 38.2% a 103,32; stato TENUTO; confluenza: invalidazione rialzista.
- Invalidazione: **72,11 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 70 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Doji / indecisione**
- Stato prezzo: **NEL RANGE**
- Supporto: **97,45 $**
- Resistenza: **107,12 $**
- Breakout 60g: **124,62 $**
- Breakdown 60g: **74,20 $**
- RSI14: **37.46**
- ATR14: **4,33%**
- Volume ratio 20g: **0.49**
- Rendimento 30g: **+1,81%**
- Rendimento 90g: **+35,47%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,51 $ | n/a | 46,32% | 72,11 $ | Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 70 giorni. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 46,32% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 70 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 107,12 $ | 2026-09-18 | 30g | 118,01 $ | -33,76% | n/a | 104,97 $ | Due minimi simili a 97,45 $ e 96,23 $. Neckline circa 107,12 $. Breakout neckline: 2026-09-18 (30 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01 $; progresso: -33,76%; prezzo sotto neckline. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 60g | 85,65 $ | 337,94% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (60 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 337,94%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-10-08**
- Età formazione: **10 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.10528 $**
- Target teorico: **0.13028 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **33,01%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08689 $** — Swing DOWN 2026-09-22 0.10528 -> 2026-10-08 0.08122; livello più vicino 23.6% a 0.08689; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.10318 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 0.08028 tra 2026-09-02 e 2026-10-08. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Shooting star / rejection alto**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.07841 $**
- Resistenza: **0.07923 $**
- Breakout 60g: **0.10528 $**
- Breakdown 60g: **0.06919 $**
- RSI14: **35.04**
- ATR14: **4,81%**
- Volume ratio 20g: **0.52**
- Rendimento 30g: **-3,14%**
- Rendimento 90g: **+9,46%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | ATTIVO | -1 | ribassista | 0.08028 $ | 2026-10-18 | 0g | 0.06059 $ | 5,75% | n/a | 0.08189 $ | Due massimi simili a 0.09998 $ e 0.09421 $. Neckline circa 0.08028 $. Breakout neckline: 2026-10-18 (0 giorni fa). Stato: ATTIVO. Target teorico: 0.06059 $; progresso: 5,75%; prezzo sotto neckline. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.10528 $ | n/a | n/a | 0.13028 $ | n/a | 33,01% | 0.10318 $ | Due minimi simili a 0.08028 $ e 0.08122 $. Neckline circa 0.10528 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 10 giorni. |

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

Generato: 2026-10-18 05:33 UTC

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 81.752 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0060% | -0,43% | 1,56 | +0,94% | 0 $ | 0 $ |
| SOL | 103,77 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | -0,0004% | -2,39% | 6,07 | -4,86% | 0 $ | 0 $ |
| DOGE | 0.07931 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0004% | -1,56% | 1,41 | +2,62% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0093% | 180,77 mln $ | 0,60 | -8,75% |
| BTC | Bitget | OK | +0,0032% | 2,83 mld $ | 0,88 | -28,02% |
| BTC | Kucoin | OK | +0,0086% | 789,48 mln $ | 0,21 | +2,20% |
| SOL | Kraken | OK | +0,0104% | 25,91 mln $ | 0,06 | -3,26% |
| SOL | Bitget | OK | +0,0029% | 429,04 mln $ | 52,31 | -31,97% |
| SOL | Kucoin | OK | -0,0019% | 111,24 mln $ | 0,45 | -18,72% |
| DOGE | Kraken | OK | +0,0188% | 4,79 mln $ | 0,83 | -0,12% |
| DOGE | Bitget | OK | -0,0032% | 102,62 mln $ | 0,66 | +18,40% |
| DOGE | Kucoin | OK | +0,0034% | 56,55 mln $ | 0,90 | +24,92% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 10, accuratezza +30,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta. Confluenza tecnica dichiarata: invalidazione ribassista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** Eve and Adam Bottom maturo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Supporto vicino con assorbimento/acquisti: tenuta più credibile.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci tenuto con acquisti/assorbimento coerenti: conferma positiva. Confluenza tecnica dichiarata: invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 11, accuratezza +45,45%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
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
| BTC | +60,00% | +6,96% | 5 | +80,00% | RACCOLTA DATI | 0,00 | +60,00% | +6,96% |
| SOL | +60,00% | +6,24% | 5 | +100,00% | RACCOLTA DATI | 0,00 | +60,00% | +6,24% |
| DOGE | +75,00% | +11,17% | 10 | +70,00% | RACCOLTA DATI | 0,00 | +75,00% | +11,17% |

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

Generato: 2026-10-18 05:33 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **24**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-18 | BTC | 81.751,50 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,56 | -0,43% | +0,94% |
| 2026-10-18 | DOGE | 0.07931 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,41 | -1,56% | +2,62% |
| 2026-10-18 | SOL | 103,77 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 6,07 | -2,39% | -4,86% |
| 2026-10-16 | BTC | 82.351,80 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,99 | -2,45% | -0,58% |
| 2026-10-16 | DOGE | 0.08238 | V2.1.3 | OK | 1 | 0 | 3,00 | MEDIA | 1,27 | +3,38% | -0,52% |
| 2026-10-16 | SOL | 106,36 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,91 | +4,72% | +2,43% |
| 2026-10-15 | BTC | 81.453,00 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 5,82 | +5,23% | +0,79% |
| 2026-10-15 | DOGE | 0.08033 | V2.1.3 | OK | 0 | 0 | 1,25 | BASSA | 0,95 | -5,64% | -1,85% |
| 2026-10-15 | SOL | 103,29 | V2.1.3 | OK | 0 | 0 | 2,50 | BASSA | 1,14 | -5,91% | +8,22% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 10 | +40,00% | -0,44% | -1,18% | +0,59% | FEEDBACK RAPIDO |
| BTC | 3g | 10 | +40,00% | -0,44% | -2,45% | +1,64% | FEEDBACK RAPIDO |
| BTC | 7g | 10 | +30,00% | -1,89% | -3,68% | +1,86% | FEEDBACK RAPIDO |
| BTC | 14g | 9 | +33,33% | -0,96% | -4,58% | +2,58% | FEEDBACK RAPIDO |
| BTC | 30g | 5 | +80,00% | +5,55% | -5,21% | +8,55% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 5 | +100,00% | +22,07% | -4,32% | +25,38% | FEEDBACK RAPIDO |
| DOGE | 1g | 12 | +50,00% | +1,09% | -0,60% | +2,49% | FEEDBACK RAPIDO |
| DOGE | 3g | 11 | +36,36% | +1,63% | -3,44% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 7g | 11 | +45,45% | -0,13% | -4,83% | +9,23% | FEEDBACK RAPIDO |
| DOGE | 14g | 11 | +36,36% | +1,12% | -6,04% | +13,84% | FEEDBACK RAPIDO |
| DOGE | 30g | 10 | +70,00% | +9,97% | -6,58% | +29,10% | FEEDBACK RAPIDO |

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
| BTC | 81.642 $ | +0.0022% | -10.95% | 1.54 | Misto | 1/5 |
| SOL | 103,44 $ | +0.0008% | -4.34% | 1.74 | Misto | 1/5 |
| DOGE | 0.07915 $ | +0.0100% | -9.38% | 4.17 | Rischio sotto | 2/5 |

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

Generato: 2026-10-18 05:33 UTC

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                       | Stato D       | Weekly                    | Stato W       | Lettura weekly                                                                                              |   Peso |
|:--------|:----------------------------|:--------------|:--------------------------|:--------------|:------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Conferma ribassista         | CONTESTO      | Hidden bullish            | IN_FORMAZIONE | Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0. |      0 |
| SOL     | Hidden bullish              | IN_FORMAZIONE | Hidden bullish            | IN_FORMAZIONE | Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0. |      0 |
| DOGE    | Bullish regolare invalidata | INVALIDATA    | Hidden bullish invalidata | INVALIDATA    | La precedente hidden bullish non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.        |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                        | Stato         | Prezzo / RSI      | Pivot confrontati                                                 | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:----------------------------|:--------------|:------------------|:------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Conferma ribassista         | CONTESTO      | 81.619 $ / 46,96  | n/a                                                               | -3,71%              | -16,77           |      0 |
| BTC     | 1W   | Hidden bullish              | IN_FORMAZIONE | 81.619 $ / 56,64  | 2026-09-20 74.945 $ / RSI 58,69 → 2026-10-18 79.736 $ / RSI 56,64 | n/a                 | n/a              |      0 |
| SOL     | 1D   | Hidden bullish              | IN_FORMAZIONE | 103,31 $ / 37,29  | 2026-09-16 96,23 $ / RSI 51,17 → 2026-10-15 101,03 $ / RSI 40,01  | n/a                 | n/a              |      0 |
| SOL     | 1W   | Hidden bullish              | IN_FORMAZIONE | 103,31 $ / 53,02  | 2026-09-20 96,23 $ / RSI 61,01 → 2026-10-18 101,03 $ / RSI 53,02  | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Bullish regolare invalidata | INVALIDATA    | 0.07905 $ / 34,91 | n/a                                                               | -14,84%             | -18,70           |      0 |
| DOGE    | 1W   | Hidden bullish invalidata   | INVALIDATA    | 0.07905 $ / 43,43 | n/a                                                               | -12,96%             | -5,45            |      0 |

### BTC

- **1D — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.
- **1W — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.

### SOL

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.

### DOGE

- **1D — Bullish regolare invalidata / INVALIDATA**: La precedente bullish regolare non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.
- **1W — Hidden bullish invalidata / INVALIDATA**: La precedente hidden bullish non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.

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
| BTC     | 1D   | Hidden bullish   |          60 |           1 | +100,00%      | +26,95%           | RACCOLTA DATI |      0 |
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

Generato: 2026-10-18 05:33 UTC

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

| Asset   | Prezzo   |   Punteggio | Verdetto           | Trend            | Momentum        | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista                | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-------------------|:-----------------|:----------------|:------------------------------------------------------|----------------:|:---------------|:---------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 81.642 $ | 1 | NEUTRALE / MISTO | Trend rialzista | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | +1 | 0 / NON ATTIVO | Eve and Adam Bottom / MATURO | Doppio massimo / CANDIDATO | 80.337 | 84.249 |
| SOL | 103,44 $ | -4 | DEBOLE | Trend misto | Momentum debole | Struttura ribassista con massimi e minimi decrescenti | 0 | +1 / TENUTO | Doppio minimo / TARGET RAGGIUNTO | Triplo massimo / CANDIDATO | 96,23 | 123,48 |
| DOGE | 0.07915 $ | -7 | RIBASSISTA TECNICO | Trend ribassista | Momentum debole | Volatilità in espansione | 0 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 0.07841 | 0.10528 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Eve and Adam Bottom — MATURO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 1 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | INVALIDATO | CANDIDATO | ASSENTE | 0 |
| DOGE | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 47.05 | -510.199 | 83.421 | 81.328 | 72.427 | 6,34% | 4,97% | 0,92% | 25,16% |
| SOL | 37.46 | -1.84326 | 113,06 | 109,35 | 87,46 | 9,92% | 7,62% | -8,13% | 32,97% |
| DOGE | 35.04 | -0.00135 | 0.08837 | 0.08810 | 0.08732 | 4,08% | -2,50% | -9,45% | 9,72% |

## Dettaglio asset

### BTC

- Prezzo: **81.642 $**
- Punteggio tecnico: **1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 8.257e+04 -> 8.034e+04. Ultimi massimi: 8.715e+04 -> 8.425e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 80,68%. Fase non abbastanza chiara.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-10-12 84.249; livello più vicino 23.6% a 77.995; stato NON ATTIVO; confluenza: invalidazione ribassista.
- Punteggio pattern: **+1**
  - rialzista dominante: Eve and Adam Bottom (MATURO, +1); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **80.337**
- Resistenza più vicina: **84.249**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 76.248 tra 2026-09-02 e 2026-10-08. Neckline stimata: 87.364. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 87.364; target 98.479; distanza dalla neckline 7,01%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 74.945 dal 2026-09-02 al 2026-10-08. Neckline stimata: 87.364. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 87.364; target 99.783; distanza dalla neckline 7,01%; prezzo sotto neckline.
- Eve and Adam Bottom: **MATURO** (+1)
  - Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (27 giorni fa). Stato: MATURO. Target teorico: 89.580; progresso corrente: -8,48%. Relazione prezzo/neckline: vicino alla neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (27g); progresso -8,48%; prezzo vicino alla neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 84.249 tra 2026-09-03 e 2026-10-12. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 74.945; target 65.640; distanza dalla neckline 8,94%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 84.249 dal 2026-08-28 al 2026-10-12. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 74.945; target 65.640; distanza dalla neckline 8,94%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 84.249 dal 2026-09-03 al 2026-10-12. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 74.945; target 65.640; distanza dalla neckline 8,94%; prezzo sopra neckline.

### SOL

- Prezzo: **103,44 $**
- Punteggio tecnico: **-4 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend misto** (1)
- Momentum: **Momentum debole** (-2)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 97.45 -> 96.23. Ultimi massimi: 124.6 -> 123.5.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 64,82%. Fase non abbastanza chiara.
- Fibonacci automatico: **TENUTO** (+1)
  - Swing UP 2026-08-01 70,69 -> 2026-10-02 123,48; livello più vicino 38.2% a 103,32; stato TENUTO; confluenza: invalidazione rialzista.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Triplo massimo (CANDIDATO, 0).
- Supporto più vicino: **96,23**
- Resistenza più vicina: **123,48**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 96,23 tra 2026-09-02 e 2026-09-16. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (30 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: -33,76%. Relazione prezzo/neckline: sotto neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (30g); progresso -33,76%; prezzo sotto neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (60 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 307,70%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (60g); progresso 307,70%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 96,23 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (30 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: -33,76%. Relazione prezzo/neckline: sotto neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (30g); progresso -33,76%; prezzo sotto neckline.
- Doppio massimo: **INVALIDATO** (0)
  - Due massimi simili vicino a 110,04 tra 2026-08-27 e 2026-09-06. Neckline ribassista stimata: 97,45. Breakout neckline: 2026-09-15 (33 giorni fa). Stato: INVALIDATO. Target teorico: 84,86; progresso corrente: -47,58%. Relazione prezzo/neckline: sopra neckline.
  - neckline 97,45; target 84,86; breakout 2026-09-15 (33g); progresso -47,58%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 70 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 46,32%; prezzo sopra neckline.
- Adam/Eve Top: **ASSENTE** (0)

### DOGE

- Prezzo: **0.07915 $**
- Punteggio tecnico: **-7 / 12**
- Verdetto: **RIBASSISTA TECNICO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-2)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 0.09053 -> 0.08122. Ultimi massimi: 0.09421 -> 0.1053.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 29,96%. Fase non abbastanza chiara.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-09-22 0.10528 -> 2026-10-08 0.08122; livello più vicino 23.6% a 0.08689; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.07841**
- Resistenza più vicina: **0.10528**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.08028 tra 2026-09-02 e 2026-10-08. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 0.10528; target 0.13028; distanza dalla neckline 33,01%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 0.07841 dal 2026-09-02 al 2026-10-08. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 0.10528; target 0.13216; distanza dalla neckline 33,01%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.08028 dal 2026-09-02 al 2026-10-08. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 0.10528; target 0.13028; distanza dalla neckline 33,01%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.10528 tra 2026-08-22 e 2026-09-22. Neckline ribassista stimata: 0.07841. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 26 giorni.
  - neckline 0.07841; target 0.05153; distanza dalla neckline 0,95%; prezzo vicino alla neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 68 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 16,44%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07380 dal 2026-07-26 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 68 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 16,44%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-10-12 | 77.995 | 74.126 | 70.998 | 67.871 | 63.419 | 23.6% / 77.995 | NON ATTIVO | invalidazione ribassista | 0 |
| SOL | UP 2026-08-01 -> 2026-10-02 | 111,02 | 103,32 | 97,09 | 90,86 | 81,99 | 38.2% / 103,32 | TENUTO | invalidazione rialzista | +1 |
| DOGE | DOWN 2026-09-22 -> 2026-10-08 | 0.08689 | 0.09041 | 0.09325 | 0.09609 | 0.10013 | 23.6% / 0.08689 | NON ATTIVO | nessuna confluenza indipendente | 0 |

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

- **BTC**: 47/30 previsioni controllate su 100 fatte. Stato: **ATTIVA**.
- **SOL**: 47/30 previsioni controllate su 100 fatte. Stato: **ATTIVA**.
- **DOGE**: 47/30 previsioni controllate su 100 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 100 | 47 | 30/30 [██████████] | 53 | ATTIVA | 2026-10-22 / tra 4 giorni |
| SOL | 100 | 47 | 30/30 [██████████] | 53 | ATTIVA | 2026-10-22 / tra 4 giorni |
| DOGE | 100 | 47 | 30/30 [██████████] | 53 | ATTIVA | 2026-10-22 / tra 4 giorni |

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

Generato: 2026-10-18 05:34 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- Calibrazione rischio in quarantena; moduli sospesi esclusi dalla verifica prezzi correnti. Consultare lab_reduction_status.md.
- 2 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo         | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:--------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price | OK      | 81.642 $          | 81.642 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price | OK      | 0.07915 $         | 0.07915 $       | +0,0000%     |
| Scanner                 | SOL     | current_price | OK      | 103,44 $          | 103,44 $        | -0,0000%     |
| Scanner Forecast        | BTC     | current_price | OK      | 81.642 $          | 81.642 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price | OK      | 103,44 $          | 103,44 $        | -0,0000%     |
| Scanner Forecast        | DOGE    | current_price | OK      | 0.07915 $         | 0.07915 $       | +0,0000%     |
| Technical Structure     | BTC     | price         | OK      | 81.642 $          | 81.642 $        | +0,0000%     |
| Technical Structure     | SOL     | price         | OK      | 103,44 $          | 103,44 $        | -0,0000%     |
| Technical Structure     | DOGE    | price         | OK      | 0.07915 $         | 0.07915 $       | +0,0000%     |
| Classic Technical       | BTC     | price         | OK      | 81.642 $          | 81.642 $        | +0,0000%     |
| Classic Technical       | SOL     | price         | OK      | 103,44 $          | 103,44 $        | -0,0000%     |
| Classic Technical       | DOGE    | price         | OK      | 0.07915 $         | 0.07915 $       | +0,0000%     |
| Classic Visual          | BTC     | price         | OK      | 81.642 $          | 81.642 $        | +0,0000%     |
| Classic Visual          | SOL     | price         | OK      | 103,44 $          | 103,44 $        | -0,0000%     |
| Classic Visual          | DOGE    | price         | OK      | 0.07915 $         | 0.07915 $       | +0,0000%     |
| Exchange Microstructure | BTC     | price         | OK      | 81.642 $          | 81.752 $        | +0,1343%     |
| Exchange Microstructure | SOL     | price         | WARN    | 103,44 $          | 103,77 $        | +0,3142%     |
| Exchange Microstructure | DOGE    | price         | WARN    | 0.07915 $         | 0.07931 $       | +0,2021%     |

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
