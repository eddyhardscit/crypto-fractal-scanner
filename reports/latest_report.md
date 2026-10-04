<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-10-04 05:32 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +4 | BULLISH | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | +1 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | 0 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+4**, spot = **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+1**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **0**, spot = **STAI ALLA FINESTRA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+4**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**
- Long leva: **LONG PRUDENTE**
- Short leva: **NO SHORT**
- Rischio: **MEDIO**
- Conferme: Prima resistenza sopra 87.364; conferma del doppio minimo sopra 82.262.
- Invalidazioni: Sotto 82.571 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+1**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **HOLD LEGGERO / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 124,62; milestone analogiche 126,78 / 135,23, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 114,70 / 96,23 / 62,19.

### DOGE

- Global Confluence: **0**
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
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 1; EMA200 circa 111,42 $; upside verso EMA200 -7,72%. Non autorizza leva e non aggiunge punti automatici.
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

Generato: 2026-10-04 05:33 UTC

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

Segnali totali salvati: **240**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-04 | BTC | 84.850,99 | +4 | 0 | 0 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-10-04 | DOGE | 0.09275 | 0 | -2 | -2 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-10-04 | SOL | 120,74 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-03 | BTC | 84.628,98 | +1 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-03 | DOGE | 0.09320 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-03 | SOL | 119,63 | +3 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-02 | BTC | 86.570,73 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-10-02 | DOGE | 0.09654 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-10-02 | SOL | 121,92 | +1 | -2 | -2 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-30 | BTC | 83.418,75 | +3 | 0 | 0 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-30 | DOGE | 0.09397 | +3 | -1 | -1 | 0 | +3 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-30 | SOL | 119,28 | +1 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 80 | 79 | 78 | 77 | 76 | 74 | 71 | 69 | 65 | 56 | 41 | 28 |
| SOL | 80 | 79 | 78 | 77 | 76 | 74 | 71 | 69 | 65 | 56 | 41 | 28 |
| DOGE | 80 | 79 | 78 | 77 | 76 | 74 | 71 | 69 | 65 | 56 | 41 | 28 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-06 | 60g | 2026-10-05 | domani |
| SOL | 2026-08-06 | 60g | 2026-10-05 | domani |
| DOGE | 2026-08-06 | 60g | 2026-10-05 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 74 | 52,70% | +0,34% | +0,33% | UTILE |
| BTC | 2g | 73 | 52,05% | +0,65% | +0,58% | UTILE |
| BTC | 3g | 72 | 47,22% | +0,86% | +0,76% | UTILE |
| BTC | 5g | 71 | 45,07% | +1,71% | +1,53% | UTILE |
| BTC | 7g | 69 | 53,62% | +2,47% | +2,32% | UTILE |
| BTC | 10g | 68 | 61,76% | +3,50% | +3,37% | UTILE |
| BTC | 14g | 66 | 62,12% | +5,13% | +5,08% | UTILE |
| BTC | 21g | 62 | 72,58% | +8,30% | +8,19% | UTILE |
| BTC | 30g | 53 | 94,34% | +13,27% | +12,46% | PRIMA CALIBRAZIONE |
| BTC | 45g | 38 | 92,11% | +24,99% | +21,51% | PRIMA CALIBRAZIONE |
| BTC | 60g | 26 | 88,46% | +27,39% | +21,62% | FEEDBACK RAPIDO |
| SOL | 1g | 71 | 50,70% | +0,38% | +0,30% | UTILE |
| SOL | 2g | 70 | 48,57% | +1,06% | +0,96% | UTILE |
| SOL | 3g | 69 | 53,62% | +1,76% | +1,64% | UTILE |
| SOL | 5g | 68 | 57,35% | +3,05% | +2,97% | UTILE |
| SOL | 7g | 66 | 62,12% | +4,41% | +4,49% | UTILE |
| SOL | 10g | 63 | 68,25% | +6,66% | +6,78% | UTILE |
| SOL | 14g | 61 | 75,41% | +9,69% | +10,29% | UTILE |
| SOL | 21g | 58 | 82,76% | +14,98% | +14,37% | PRIMA CALIBRAZIONE |
| SOL | 30g | 49 | 79,59% | +21,94% | +17,90% | PRIMA CALIBRAZIONE |
| SOL | 45g | 34 | 67,65% | +42,79% | +20,15% | PRIMA CALIBRAZIONE |
| SOL | 60g | 21 | 47,62% | +45,23% | +3,50% | FEEDBACK RAPIDO |
| DOGE | 1g | 75 | 45,33% | +0,19% | -0,14% | UTILE |
| DOGE | 2g | 74 | 44,59% | +0,49% | -0,18% | UTILE |
| DOGE | 3g | 73 | 39,73% | +0,84% | -0,03% | UTILE |
| DOGE | 5g | 72 | 43,06% | +1,75% | +0,02% | UTILE |
| DOGE | 7g | 70 | 47,14% | +2,50% | +0,26% | UTILE |
| DOGE | 10g | 67 | 44,78% | +3,49% | +0,37% | UTILE |
| DOGE | 14g | 65 | 58,46% | +5,69% | +3,65% | UTILE |
| DOGE | 21g | 61 | 63,93% | +8,23% | +3,47% | UTILE |
| DOGE | 30g | 52 | 75,00% | +13,01% | +6,27% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 39 | 48,72% | +25,34% | +4,84% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 26 | 23,08% | +26,34% | -10,48% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 74 | 52,70% | +0,34% | +0,33% | -0,21% | +0,85% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 78 | 50,00% | +0,29% | +0,29% | -0,22% | +0,80% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 78 | 50,00% | +0,29% | +0,29% | -0,22% | +0,80% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 72 | 43,06% | +0,31% | +0,02% | -0,17% | +0,82% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 31 | 38,71% | +0,62% | -0,01% | -0,20% | +1,12% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,49% | -0,49% | -1,07% | -0,05% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 73 | 52,05% | +0,65% | +0,58% | -0,17% | +1,32% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 77 | 51,95% | +0,63% | +0,63% | -0,11% | +1,32% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 77 | 51,95% | +0,63% | +0,63% | -0,11% | +1,32% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 71 | 43,66% | +0,62% | +0,04% | -0,02% | +1,31% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 30 | 40,00% | +1,10% | -0,05% | +0,11% | +1,77% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,28% | -0,28% | -1,06% | +0,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 72 | 47,22% | +0,86% | +0,76% | -1,17% | +2,56% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 76 | 51,32% | +1,02% | +0,91% | -1,17% | +2,70% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 76 | 51,32% | +1,02% | +0,91% | -1,17% | +2,70% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 70 | 37,14% | +1,08% | -0,13% | -1,08% | +2,74% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 29 | 37,93% | +1,95% | -0,51% | -0,85% | +3,41% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 71 | 45,07% | +1,71% | +1,53% | -1,76% | +4,03% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 76 | 46,05% | +1,89% | +1,69% | -1,73% | +4,22% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 76 | 46,05% | +1,89% | +1,69% | -1,73% | +4,22% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 69 | 43,48% | +1,82% | -0,63% | -1,66% | +4,19% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 29 | 41,38% | +4,06% | -2,25% | -1,22% | +6,21% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 14,29% | -1,43% | -1,43% | -2,57% | +1,68% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 69 | 53,62% | +2,47% | +2,32% | -2,11% | +5,23% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 74 | 56,76% | +2,66% | +2,62% | -2,07% | +5,37% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 74 | 56,76% | +2,66% | +2,62% | -2,07% | +5,37% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 67 | 44,78% | +2,73% | -1,07% | -2,01% | +5,41% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 29 | 37,93% | +5,44% | -4,00% | -1,49% | +8,41% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -1,74% | -1,74% | -3,24% | +1,77% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 68 | 61,76% | +3,50% | +3,37% | -2,41% | +6,47% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 71 | 64,79% | +3,63% | +3,63% | -2,39% | +6,64% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 71 | 64,79% | +3,63% | +3,63% | -2,39% | +6,64% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 64 | 50,00% | +3,78% | -0,37% | -2,33% | +6,81% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 29 | 41,38% | +5,56% | -4,39% | -1,70% | +9,12% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -1,21% | -1,21% | -3,81% | +1,86% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 66 | 62,12% | +5,13% | +5,08% | -2,59% | +8,79% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 69 | 62,32% | +5,20% | +5,20% | -2,57% | +8,87% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 69 | 62,32% | +5,20% | +5,20% | -2,57% | +8,87% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 62 | 58,06% | +5,55% | +1,64% | -2,50% | +9,26% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 28 | 25,00% | +5,37% | -4,20% | -1,80% | +9,90% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 62 | 72,58% | +8,30% | +8,19% | -2,88% | +12,16% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 65 | 76,92% | +8,23% | +8,23% | -2,86% | +12,12% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 65 | 76,92% | +8,23% | +8,23% | -2,86% | +12,12% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 60 | 56,67% | +8,78% | +1,19% | -2,72% | +12,72% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 24 | 54,17% | +8,85% | -4,04% | -2,32% | +12,73% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 53 | 94,34% | +13,27% | +12,46% | -2,72% | +17,32% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 56 | 91,07% | +13,19% | +13,19% | -2,71% | +17,37% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 56 | 91,07% | +13,19% | +13,19% | -2,71% | +17,37% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 51 | 58,82% | +13,24% | +0,18% | -2,53% | +17,62% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,37% | -2,02% | -2,62% | +17,60% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 100,00% | +5,25% | +5,25% | -4,87% | +8,45% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 38 | 92,11% | +24,99% | +21,51% | -2,18% | +29,75% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 41 | 100,00% | +25,14% | +25,14% | -2,20% | +29,76% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 41 | 100,00% | +25,14% | +25,14% | -2,20% | +29,76% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 36 | 38,89% | +25,71% | -4,79% | -1,89% | +30,37% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 9 | 11,11% | +26,56% | -21,68% | -0,19% | +33,31% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 26 | 88,46% | +27,39% | +21,62% | -2,89% | +32,41% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 28 | 100,00% | +27,19% | +27,19% | -2,94% | +32,28% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 28 | 100,00% | +27,19% | +27,19% | -2,94% | +32,28% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 24 | 100,00% | +27,95% | +27,95% | -2,68% | +33,29% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 23 | 26,09% | +27,54% | -14,77% | -2,61% | +32,86% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 4 | 0,00% | +33,67% | -33,67% | -1,55% | +38,08% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 75 | 45,33% | +0,19% | -0,14% | -0,59% | +1,21% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 78 | 57,69% | +0,12% | +0,50% | -0,67% | +1,08% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 78 | 57,69% | +0,12% | +0,50% | -0,67% | +1,08% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 72 | 50,00% | +0,03% | +0,09% | -0,78% | +0,99% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 44 | 38,64% | +0,01% | -0,74% | -0,85% | +0,76% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 74 | 44,59% | +0,49% | -0,18% | -0,65% | +1,86% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 77 | 58,44% | +0,35% | +0,78% | -0,77% | +1,65% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 77 | 58,44% | +0,35% | +0,78% | -0,77% | +1,65% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 71 | 52,11% | +0,03% | +0,09% | -1,10% | +1,33% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 44 | 40,91% | +0,32% | -1,41% | -0,90% | +1,29% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 73 | 39,73% | +0,84% | -0,03% | -2,23% | +4,00% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 76 | 55,26% | +0,70% | +1,01% | -2,33% | +3,72% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 76 | 55,26% | +0,70% | +1,01% | -2,33% | +3,72% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 70 | 44,29% | +0,05% | -0,02% | -2,58% | +3,01% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 43 | 30,23% | +0,67% | -2,36% | -2,59% | +3,92% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 72 | 43,06% | +1,75% | +0,02% | -3,25% | +6,44% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 75 | 52,00% | +1,64% | +1,33% | -3,29% | +6,23% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 75 | 52,00% | +1,64% | +1,33% | -3,29% | +6,23% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 69 | 50,72% | +0,83% | -0,67% | -3,68% | +5,46% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 43 | 32,56% | +2,13% | -4,81% | -3,64% | +6,91% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 70 | 47,14% | +2,50% | +0,26% | -3,86% | +8,49% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 73 | 56,16% | +2,52% | +1,47% | -3,88% | +8,31% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 73 | 56,16% | +2,52% | +1,47% | -3,88% | +8,31% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 67 | 44,78% | +1,52% | -1,07% | -4,35% | +7,29% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 43 | 27,91% | +3,41% | -6,38% | -4,15% | +8,99% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 67 | 44,78% | +3,49% | +0,37% | -4,42% | +10,78% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 70 | 50,00% | +3,40% | +1,01% | -4,42% | +10,59% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 70 | 50,00% | +3,40% | +1,01% | -4,42% | +10,59% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 64 | 50,00% | +2,07% | -1,40% | -4,96% | +9,06% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 42 | 30,95% | +3,89% | -7,11% | -4,83% | +11,29% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 65 | 58,46% | +5,69% | +3,65% | -4,87% | +14,65% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 68 | 60,29% | +5,28% | +2,62% | -4,85% | +14,22% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 68 | 60,29% | +5,28% | +2,62% | -4,85% | +14,22% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 62 | 51,61% | +3,22% | -0,78% | -5,45% | +11,54% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 41 | 41,46% | +5,35% | -5,10% | -5,18% | +13,82% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 50,00% | +6,54% | +2,61% | -3,97% | +15,08% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 61 | 63,93% | +8,23% | +3,47% | -5,33% | +18,97% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 64 | 60,94% | +8,57% | +5,23% | -5,34% | +19,16% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 64 | 60,94% | +8,57% | +5,23% | -5,34% | +19,16% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 58 | 60,34% | +6,46% | -1,26% | -6,05% | +16,07% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 37 | 48,65% | +5,58% | -6,66% | -5,65% | +15,17% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 66,67% | +6,54% | +0,57% | -4,75% | +18,76% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 52 | 75,00% | +13,01% | +6,27% | -4,82% | +26,35% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 55 | 76,36% | +13,25% | +8,58% | -4,84% | +26,85% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 55 | 76,36% | +13,25% | +8,58% | -4,84% | +26,85% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 49 | 61,22% | +11,76% | -3,02% | -5,65% | +24,39% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 31 | 48,39% | +10,82% | -8,72% | -5,10% | +22,58% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 87,50% | +21,36% | +13,45% | -4,45% | +31,96% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 39 | 48,72% | +25,34% | +4,84% | -3,33% | +42,56% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 41 | 60,98% | +25,16% | +9,73% | -3,38% | +42,44% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 41 | 60,98% | +25,16% | +9,73% | -3,38% | +42,44% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 34 | 8,82% | +22,82% | -17,40% | -4,11% | +40,98% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 27 | 0,00% | +24,99% | -24,99% | -3,76% | +41,98% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +34,73% | +17,62% | -0,01% | +46,16% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 26 | 23,08% | +26,34% | -10,48% | -5,08% | +42,86% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 28 | 42,86% | +26,91% | +3,60% | -5,04% | +43,20% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 28 | 42,86% | +26,91% | +3,60% | -5,04% | +43,20% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 26 | 46,15% | +25,93% | +6,92% | -5,14% | +42,79% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 28 | 0,00% | +26,91% | -26,91% | -5,04% | +43,20% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 20 | 0,00% | +24,92% | -24,92% | -5,27% | +41,80% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 71 | 50,70% | +0,38% | +0,30% | -0,36% | +1,25% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 73 | 54,79% | +0,37% | +0,44% | -0,47% | +1,22% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 76 | 53,95% | +0,40% | +0,38% | -0,44% | +1,25% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 71 | 46,48% | +0,36% | -0,03% | -0,53% | +1,20% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 53 | 47,17% | +0,59% | +0,06% | -0,45% | +1,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 70 | 48,57% | +1,06% | +0,96% | -0,22% | +2,14% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 72 | 48,61% | +0,94% | +0,69% | -0,47% | +1,87% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 75 | 48,00% | +0,91% | +0,65% | -0,45% | +1,90% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 70 | 42,86% | +0,74% | -0,03% | -0,43% | +1,89% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 52 | 50,00% | +0,85% | +0,39% | -0,46% | +1,93% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 69 | 53,62% | +1,76% | +1,64% | -1,74% | +4,15% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 71 | 50,70% | +1,57% | +1,22% | -1,90% | +3,95% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 74 | 50,00% | +1,52% | +1,16% | -1,88% | +3,92% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 69 | 46,38% | +1,13% | -0,16% | -1,92% | +3,47% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 51 | 50,98% | +1,15% | +0,58% | -1,87% | +3,43% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 68 | 57,35% | +3,05% | +2,97% | -2,44% | +6,50% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 70 | 52,86% | +2,79% | +2,01% | -2,60% | +6,25% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 73 | 52,05% | +2,70% | +1,90% | -2,58% | +6,15% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 68 | 47,06% | +2,36% | -0,46% | -2,64% | +5,64% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 50 | 54,00% | +1,65% | +0,89% | -2,60% | +4,89% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 66 | 62,12% | +4,41% | +4,49% | -2,91% | +8,38% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 69 | 60,87% | +4,05% | +3,15% | -3,06% | +8,03% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 72 | 61,11% | +3,87% | +3,02% | -3,05% | +7,86% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 66 | 40,91% | +3,01% | -1,32% | -3,16% | +7,09% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 48 | 47,92% | +1,59% | +0,89% | -3,19% | +5,68% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 63 | 68,25% | +6,66% | +6,78% | -3,23% | +10,91% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 66 | 65,15% | +6,27% | +5,58% | -3,42% | +10,34% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 69 | 63,77% | +5,99% | +5,34% | -3,42% | +10,06% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 63 | 49,21% | +4,57% | -1,44% | -3,60% | +8,90% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 45 | 55,56% | +2,11% | +1,24% | -3,69% | +6,77% | PRIMA CALIBRAZIONE |

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

Generato: 2026-10-04 05:33 UTC

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
| BTC | 80 | UTILE | 78 | 22 | 16 | 0 | Famiglia statistica | 1g | 50,00% | +0,29% | campione utile, valutare con prudenza |
| SOL | 80 | UTILE | 73 | 29 | 16 | 0 | Famiglia statistica | 1g | 54,79% | +0,44% | campione utile, valutare con prudenza |
| DOGE | 80 | UTILE | 78 | 29 | 15 | 0 | Famiglia statistica | 1g | 57,69% | +0,50% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 31 | 38,71% | -0,01% | +0,62% | -0,20% | +1,12% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 78 | 50,00% | +0,29% | +0,29% | -0,22% | +0,80% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 8 | 37,50% | -0,49% | -0,49% | -1,07% | -0,05% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 72 | 43,06% | +0,02% | +0,31% | -0,17% | +0,82% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 30 | 40,00% | -0,05% | +1,10% | +0,11% | +1,77% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 77 | 51,95% | +0,63% | +0,63% | -0,11% | +1,32% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 8 | 25,00% | -0,28% | -0,28% | -1,06% | +0,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 71 | 43,66% | +0,04% | +0,62% | -0,02% | +1,31% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 29 | 37,93% | -0,51% | +1,95% | -0,85% | +3,41% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 76 | 51,32% | +0,91% | +1,02% | -1,17% | +2,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 70 | 37,14% | -0,13% | +1,08% | -1,08% | +2,74% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 29 | 41,38% | -2,25% | +4,06% | -1,22% | +6,21% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 76 | 46,05% | +1,69% | +1,89% | -1,73% | +4,22% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 7 | 14,29% | -1,43% | -1,43% | -2,57% | +1,68% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 69 | 43,48% | -0,63% | +1,82% | -1,66% | +4,19% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 29 | 37,93% | -4,00% | +5,44% | -1,49% | +8,41% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 74 | 56,76% | +2,62% | +2,66% | -2,07% | +5,37% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 7 | 28,57% | -1,74% | -1,74% | -3,24% | +1,77% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 67 | 44,78% | -1,07% | +2,73% | -2,01% | +5,41% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 29 | 41,38% | -4,39% | +5,56% | -1,70% | +9,12% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 71 | 64,79% | +3,63% | +3,63% | -2,39% | +6,64% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | -1,21% | -1,21% | -3,81% | +1,86% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 64 | 50,00% | -0,37% | +3,78% | -2,33% | +6,81% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 28 | 25,00% | -4,20% | +5,37% | -1,80% | +9,90% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 69 | 62,32% | +5,20% | +5,20% | -2,57% | +8,87% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 62 | 58,06% | +1,64% | +5,55% | -2,50% | +9,26% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 24 | 54,17% | -4,04% | +8,85% | -2,32% | +12,73% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 65 | 76,92% | +8,23% | +8,23% | -2,86% | +12,12% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 60 | 56,67% | +1,19% | +8,78% | -2,72% | +12,72% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 24 | 66,67% | -2,02% | +13,37% | -2,62% | +17,60% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 56 | 91,07% | +13,19% | +13,19% | -2,71% | +17,37% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 4 | 100,00% | +5,25% | +5,25% | -4,87% | +8,45% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 51 | 58,82% | +0,18% | +13,24% | -2,53% | +17,62% | PESO OK | 0,0 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 9 | 11,11% | -21,68% | +26,56% | -0,19% | +33,31% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 41 | 100,00% | +25,14% | +25,14% | -2,20% | +29,76% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 36 | 38,89% | -4,79% | +25,71% | -1,89% | +30,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 4 | 0,00% | -33,67% | +33,67% | -1,55% | +38,08% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 28 | 100,00% | +27,19% | +27,19% | -2,94% | +32,28% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 23 | 26,09% | -14,77% | +27,54% | -2,61% | +32,86% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 44 | 38,64% | -0,74% | +0,01% | -0,85% | +0,76% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 78 | 57,69% | +0,50% | +0,12% | -0,67% | +1,08% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 11 | 63,64% | +2,53% | +2,82% | +0,75% | +3,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 72 | 50,00% | +0,09% | +0,03% | -0,78% | +0,99% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 44 | 40,91% | -1,41% | +0,32% | -0,90% | +1,29% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 77 | 58,44% | +0,78% | +0,35% | -0,77% | +1,65% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 11 | 45,45% | +2,65% | +2,89% | +1,08% | +5,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 71 | 52,11% | +0,09% | +0,03% | -1,10% | +1,33% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 43 | 30,23% | -2,36% | +0,67% | -2,59% | +3,92% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 76 | 55,26% | +1,01% | +0,70% | -2,33% | +3,72% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 11 | 54,55% | +2,62% | +2,81% | -1,35% | +6,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 70 | 44,29% | -0,02% | +0,05% | -2,58% | +3,01% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 43 | 32,56% | -4,81% | +2,13% | -3,64% | +6,91% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 75 | 52,00% | +1,33% | +1,64% | -3,29% | +6,23% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 11 | 36,36% | +2,02% | +2,17% | -2,50% | +9,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 69 | 50,72% | -0,67% | +0,83% | -3,68% | +5,46% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 43 | 27,91% | -6,38% | +3,41% | -4,15% | +8,99% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 73 | 56,16% | +1,47% | +2,52% | -3,88% | +8,31% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 11 | 45,45% | +0,78% | +0,88% | -3,00% | +9,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 67 | 44,78% | -1,07% | +1,52% | -4,35% | +7,29% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 42 | 30,95% | -7,11% | +3,89% | -4,83% | +11,29% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 70 | 50,00% | +1,01% | +3,40% | -4,42% | +10,59% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 64 | 50,00% | -1,40% | +2,07% | -4,96% | +9,06% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 41 | 41,46% | -5,10% | +5,35% | -5,18% | +13,82% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 68 | 60,29% | +2,62% | +5,28% | -4,85% | +14,22% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 10 | 50,00% | +2,61% | +6,54% | -3,97% | +15,08% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 62 | 51,61% | -0,78% | +3,22% | -5,45% | +11,54% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 37 | 48,65% | -6,66% | +5,58% | -5,65% | +15,17% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 64 | 60,94% | +5,23% | +8,57% | -5,34% | +19,16% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 9 | 66,67% | +0,57% | +6,54% | -4,75% | +18,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 58 | 60,34% | -1,26% | +6,46% | -6,05% | +16,07% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 31 | 48,39% | -8,72% | +10,82% | -5,10% | +22,58% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 55 | 76,36% | +8,58% | +13,25% | -4,84% | +26,85% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 8 | 87,50% | +13,45% | +21,36% | -4,45% | +31,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 49 | 61,22% | -3,02% | +11,76% | -5,65% | +24,39% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 27 | 0,00% | -24,99% | +24,99% | -3,76% | +41,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 41 | 60,98% | +9,73% | +25,16% | -3,38% | +42,44% | PESO OK | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 5 | 80,00% | +17,62% | +34,73% | -0,01% | +46,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 34 | 8,82% | -17,40% | +22,82% | -4,11% | +40,98% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 20 | 0,00% | -24,92% | +24,92% | -5,27% | +41,80% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 28 | 42,86% | +3,60% | +26,91% | -5,04% | +43,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 28 | 0,00% | -26,91% | +26,91% | -5,04% | +43,20% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 53 | 47,17% | +0,06% | +0,59% | -0,45% | +1,51% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 73 | 54,79% | +0,44% | +0,37% | -0,47% | +1,22% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 71 | 46,48% | -0,03% | +0,36% | -0,53% | +1,20% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 52 | 50,00% | +0,39% | +0,85% | -0,46% | +1,93% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 72 | 48,61% | +0,69% | +0,94% | -0,47% | +1,87% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 70 | 42,86% | -0,03% | +0,74% | -0,43% | +1,89% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 51 | 50,98% | +0,58% | +1,15% | -1,87% | +3,43% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 71 | 50,70% | +1,22% | +1,57% | -1,90% | +3,95% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 69 | 46,38% | -0,16% | +1,13% | -1,92% | +3,47% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 50 | 54,00% | +0,89% | +1,65% | -2,60% | +4,89% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 70 | 52,86% | +2,01% | +2,79% | -2,60% | +6,25% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 68 | 47,06% | -0,46% | +2,36% | -2,64% | +5,64% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 48 | 47,92% | +0,89% | +1,59% | -3,19% | +5,68% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 69 | 60,87% | +3,15% | +4,05% | -3,06% | +8,03% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 66 | 40,91% | -1,32% | +3,01% | -3,16% | +7,09% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 45 | 55,56% | +1,24% | +2,11% | -3,69% | +6,77% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 66 | 65,15% | +5,58% | +6,27% | -3,42% | +10,34% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 63 | 49,21% | -1,44% | +4,57% | -3,60% | +8,90% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 43 | 51,16% | +1,68% | +3,73% | -4,16% | +8,54% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 64 | 76,56% | +8,84% | +9,47% | -3,73% | +14,30% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 61 | 44,26% | -2,39% | +6,96% | -3,98% | +12,10% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 42 | 64,29% | -0,31% | +10,88% | -4,69% | +15,79% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 60 | 83,33% | +14,87% | +14,92% | -4,29% | +20,36% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 60 | 55,00% | -4,74% | +12,61% | -4,60% | +18,09% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Classic technical | 37 | 48,65% | -6,52% | +23,60% | -4,30% | +28,74% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 51 | 88,24% | +21,16% | +24,19% | -4,03% | +30,37% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 53 | 37,74% | -10,11% | +21,68% | -4,43% | +27,55% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 22 | 4,55% | -35,13% | +38,96% | -4,29% | +48,44% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 36 | 77,78% | +29,37% | +42,52% | -3,91% | +50,22% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,56% | +44,56% | -5,94% | +49,24% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 38 | 13,16% | -33,24% | +40,64% | -4,48% | +48,49% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 20 | 0,00% | -53,15% | +53,15% | -4,94% | +59,57% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 24 | 66,67% | +26,88% | +49,61% | -5,75% | +56,37% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +41,93% | +41,93% | -9,62% | +45,82% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 28 | 14,29% | -38,09% | +47,78% | -5,91% | +54,93% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 75 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 78 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 90 | 38,89% | -0,18% |
| BTC | BREVE | Famiglia statistica | 231 | 51,08% | +0,61% |
| BTC | BREVE | Microstruttura exchange | 23 | 30,43% | -0,39% |
| BTC | BREVE | Tecnico | 213 | 41,31% | -0,02% |
| BTC | SETTIMANALE | Classic technical | 87 | 40,23% | -3,54% |
| BTC | SETTIMANALE | Famiglia statistica | 221 | 55,66% | +2,63% |
| BTC | SETTIMANALE | Microstruttura exchange | 21 | 28,57% | -1,46% |
| BTC | SETTIMANALE | Tecnico | 200 | 46,00% | -0,70% |
| BTC | SWING | Classic technical | 52 | 38,46% | -4,13% |
| BTC | SWING | Famiglia statistica | 134 | 69,40% | +6,67% |
| BTC | SWING | Microstruttura exchange | 10 | 60,00% | +0,93% |
| BTC | SWING | Tecnico | 122 | 57,38% | +1,42% |
| BTC | MEDIO | Classic technical | 37 | 45,95% | -10,23% |
| BTC | MEDIO | Famiglia statistica | 125 | 96,00% | +20,24% |
| BTC | MEDIO | Microstruttura exchange | 6 | 100,00% | +11,24% |
| BTC | MEDIO | Tecnico | 110 | 45,45% | -4,57% |
| DOGE | BREVE | Classic technical | 131 | 36,64% | -1,50% |
| DOGE | BREVE | Famiglia statistica | 231 | 57,14% | +0,76% |
| DOGE | BREVE | Microstruttura exchange | 33 | 54,55% | +2,60% |
| DOGE | BREVE | Tecnico | 213 | 48,83% | +0,05% |
| DOGE | SETTIMANALE | Classic technical | 128 | 30,47% | -6,09% |
| DOGE | SETTIMANALE | Famiglia statistica | 218 | 52,75% | +1,28% |
| DOGE | SETTIMANALE | Microstruttura exchange | 33 | 45,45% | +1,16% |
| DOGE | SETTIMANALE | Tecnico | 200 | 48,50% | -1,04% |
| DOGE | SWING | Classic technical | 78 | 44,87% | -5,84% |
| DOGE | SWING | Famiglia statistica | 132 | 60,61% | +3,89% |
| DOGE | SWING | Microstruttura exchange | 19 | 57,89% | +1,64% |
| DOGE | SWING | Tecnico | 120 | 55,83% | -1,01% |
| DOGE | MEDIO | Classic technical | 78 | 19,23% | -18,51% |
| DOGE | MEDIO | Famiglia statistica | 124 | 63,71% | +7,84% |
| DOGE | MEDIO | Microstruttura exchange | 15 | 86,67% | +19,04% |
| DOGE | MEDIO | Tecnico | 111 | 29,73% | -13,45% |
| SOL | BREVE | Classic technical | 156 | 49,36% | +0,34% |
| SOL | BREVE | Famiglia statistica | 216 | 51,39% | +0,78% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 210 | 45,24% | -0,07% |
| SOL | SETTIMANALE | Classic technical | 143 | 52,45% | +1,00% |
| SOL | SETTIMANALE | Famiglia statistica | 205 | 59,51% | +3,54% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 197 | 45,69% | -1,06% |
| SOL | SWING | Classic technical | 85 | 57,65% | +0,70% |
| SOL | SWING | Famiglia statistica | 124 | 79,84% | +11,76% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 121 | 49,59% | -3,56% |
| SOL | MEDIO | Classic technical | 79 | 24,05% | -26,29% |
| SOL | MEDIO | Famiglia statistica | 111 | 80,18% | +25,06% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 8 | 100,00% | +29,97% |
| SOL | MEDIO | Tecnico | 119 | 24,37% | -24,08% |

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
| BTC     |         80 |              56 |          24 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         80 |              56 |          24 | OSSERVAZIONE 30+ | 1,79%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         80 |              56 |          24 | OSSERVAZIONE 30+ | 16,07%           | 5,36%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                         |
|:--------|:---------------|:---------------|:------------------------------------------------------------------|
| BTC     | MEDIO          | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo |
| SOL     | ALTO           | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo |
| DOGE    | ALTO           | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-10-04 05:32 UTC

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
| BTC | +4 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | Prima resistenza sopra 87.364; conferma del doppio minimo sopra 82.262. | Sotto 82.571 il quadro tecnico peggiora. |
| SOL | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 124,62; milestone analogiche 126,78 / 135,23, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 114,70 / 96,23 / 62,19. |
| DOGE | 0 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.10528 migliora; sopra 0.07997 viene invalidato il pattern ribassista dominante. | Sotto 0.07841 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 0 | 0 | 0 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +4 |
| SOL | -2 | 0 | -2 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | +1 |
| DOGE | -2 | 0 | -2 | 0 | +2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

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

- Famiglia statistica: **0** — Scanner grezzo 0, Market Regime grezzo 0, match regime 1. Scanner neutro e regime non abbastanza forte o non abbastanza popolato. Punteggio contato nel Global: 0.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **0** — Casi positivi 50,00%, return centrale 30g -0,55%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 1, positivi 30g 100,00%, return p50 +29,09%.
- Scanner path: **0** — Controlli disponibili 78. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 9/12, verdetto rialzista tecnico, trend rialzista, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score +2 (rialzista Doppio minimo / CONFERMATO RECENTE; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 6/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — BTC: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: Prima resistenza sopra 87.364; conferma del doppio minimo sopra 82.262.

Invalidazioni: Sotto 82.571 il quadro tecnico peggiora.

### SOL

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**

SOL è ancora in zona mista. Il frattale resta soltanto uno scenario contestuale: non è confermato dal prezzo e vale 0 punti operativi finché il gap non rientra. Meglio evitare leva e ragionare solo a tranche piccole.

Dettaglio moduli:

- Famiglia statistica: **-2** — Scanner grezzo -2, Market Regime grezzo 0, match regime 2. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-2** — Casi positivi 35,00%, return centrale 30g -6,56%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 2, positivi 30g 100,00%, return p50 +17,11%.
- Scanner path: **0** — Controlli disponibili 78. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 7/12, verdetto rialzista tecnico, trend rialzista, struttura volatilità in espansione, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Triplo massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 8/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto STRUTTURA ANALOGA, PREZZO NON ADERENTE, somiglianza strutturale +71,85%, aderenza live +68,52%, errore live +15,74%, gap corrente +8,78%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE NON CONFERMATO DAL PREZZO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 76, ma percorso ancorato non aderente: gap +8,78%, errore live +15,74%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 1, bias CONTESTO DA OSSERVARE, EMA200 111,42 $, upside EMA200 -7,72%, gap EMA50/EMA200 -4,62%, hit EMA200 12w +100,00%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **-1** — SOL: cambiamento medio in peggioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 107,12; nuova conferma tecnica sopra 124,62; milestone analogiche 126,78 / 135,23, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 114,70 / 96,23 / 62,19.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **0**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **-2** — Scanner grezzo -2, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-2** — Casi positivi 35,00%, return centrale 30g -5,00%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 78. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+2** — Score tecnico 6/12, verdetto costruttivo ma non confermato, trend rialzista, struttura volatilità in espansione, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score +2 (rialzista Doppio minimo / CONFERMATO RECENTE; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 1/12, verdetto NEUTRALE / MISTO, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff RANGE / FASE NON CHIARA, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow -2.00, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE NEGATIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in miglioramento rispetto a ieri.

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

Generato: 2026-10-04 05:32 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 84.851 $ | prezzo corrente |
| Power Law centrale | 126.295 $ | deviazione -32,82% |
| Banda p10-p90 | 78.576 $ / 318.922 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 17,45% | posizione storica nel corridoio |
| Esponente β | 5,7891 | R² log-log 91,94% |
| Stabilità β | BASSA | range 1,3160 cambiando finestra |
| Ultimo halving | 2024-04-19 | 898 giorni fa |
| Fase ciclo | 61,47% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-10-04 (4400 osservazioni)
- Formula stimata: prezzo ≈ exp(-38.9400) × giorni^5.7891
- Prezzo centrale oggi: **126.295 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 17,45%
- Scarto dal centro: **-32,82%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,7891 | 91,94% |
| 2015 | 5,8694 | 91,48% |
| 2016 | 5,5518 | 87,76% |
| 2017 | 4,8271 | 83,02% |
| 2018 | 4,5535 | 78,59% |

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
| 2012-11-28 → 2016-07-09 | 2015-02-17 | +7,11% | -4,30% | +6,12% | +70,90% |
| 2016-07-09 → 2020-05-11 | 2018-11-18 | -34,28% | -35,45% | +30,59% | +47,76% |
| 2020-05-11 → 2024-04-19 | 2022-10-12 | -11,08% | -8,93% | +54,79% | +39,67% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 5 | 1 | 11.27443743363461 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -4 | -1 | 1.2036191155411213 | 0 |

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

Generato: 2026-10-04 05:32 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00142320 | +5 | +1 | 0 | SOVRAPERFORMA BTC | MEDIA | +11,27% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000109 | -4 | -1 | 0 | SOTTOPERFORMA BTC | BASSA | +1,20% | RIALZISTA | SALE SOLO IN USD: BTC resta più forte |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** SOVRAPERFORMA BTC (+5)
- **Candidato futuro:** +1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** CONFERMA FORTE: sale in USD e batte BTC
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g -1,03%; 30g +11,27%; 90g +11,19%; 180g +22,27%
- **Daily:** RSI 61.35; MA50 0.00131684; MA200 0.00119734
- **Weekly:** MA30 0.00120467; RSI 63.13
- **Livelli:** supporto 0.00127800; resistenza 0.00146600; breakout 60g 0.00146600; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00133900; target 0.00140150
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00135815
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; struttura con massimi/minimi crescenti; RSI relativo forte; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-4)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** SALE SOLO IN USD: BTC resta più forte
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g -4,65%; 30g +1,20%; 90g -10,64%; 180g -16,92%
- **Daily:** RSI 46.02; MA50 0.00000111; MA200 0.00000123
- **Weekly:** MA30 0.00000123; RSI 40.90
- **Livelli:** supporto 0.00000105; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000099
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; MACD relativo negativo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 211 | 52,61% | +1,96% | -1,04% |
| SOL | 30g | 207 | 47,83% | +4,57% | +0,63% |
| SOL | 90g | 202 | 52,97% | +9,80% | +3,12% |
| DOGE | 7g | 296 | 55,41% | +1,80% | -1,66% |
| DOGE | 30g | 295 | 52,88% | +1,96% | -3,48% |
| DOGE | 90g | 289 | 54,33% | +6,90% | -9,23% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 46 | 56,52% | +0,29% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 44 | 52,27% | +0,70% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 41 | 46,34% | +0,71% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 35 | 45,71% | +0,59% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 32 | 53,12% | -0,41% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 55 | 67,27% | -0,00% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 54 | 57,41% | +0,01% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 54 | 53,70% | -0,56% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 54 | 50,00% | -0,66% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 45 | 51,11% | -0,65% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **4 ottobre 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 120,74 $ | 2026-10-04T05:30:21Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 120,74 $ | 2026-10-04T05:31:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 1m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | 0,00000 $ | 0,00% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=120.73999786376953
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-10-04T05:30:21Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=120.73999786376953
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-10-04T05:31:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-10-04T05:32:11Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=110.217924
ANCHOR_AGE_HOURS=0.03061609
CURRENT_VS_ANCHOR_GAP_USD=0.0
CURRENT_VS_ANCHOR_GAP_PCT=0.0
```

## Verdetto: STRUTTURA ANALOGA, PREZZO NON ADERENTE

- **Fase attuale:** FRATTALE NON CONFERMATO DAL PREZZO
- **Somiglianza totale:** +71,85%
- **Somiglianza strutturale:** +71,85%
- **Aderenza prezzo live:** +68,52%
- **Errore medio live:** +15,74%
- **Gap prezzo corrente:** +8,78%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA / NON OPERATIVO
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** La geometria ricorda BTC 2022, ma SOL è troppo distante dal percorso scalato per usarlo come conferma operativa.
- **SOL è al giorno:** 120 dal bottom usato.
- **Giorno BTC equivalente:** 2023-03-21
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Laterale / movimento non forte.** Zona bassa **116,30 $** intorno al **10 ottobre 2026**; zona alta **122,04 $** intorno al **14 ottobre 2026**; fine step circa **120,71 $** entro il **18 ottobre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=STRUTTURA ANALOGA, PREZZO NON ADERENTE
PRICE_ADHERENCE_FAILED=YES
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=YES
PRICE_ADHERENCE_LAST_GAP_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=15.73944025225595
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=8.783466268312656
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 4 ottobre 2026 | 94 | +68,52% | +15,74% | +8,78% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 4 ottobre 2026 | 121 | +72,86% | +13,57% | +8,78% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: STRUTTURA ANALOGA, PREZZO NON ADERENTE.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: STRUTTURA ANALOGA, PREZZO NON ADERENTE. |
| Aderenza live | +68,52% | Errore medio live +15,74%. |
| Gap corrente | +8,78% | Prezzo non aderente: superata almeno una soglia canonica (15% medio / 18% ultimo). |
| Prima conferma prezzo | 126,78 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 135,23 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 114,70 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 534,59 $ |
| Massimo percorso base | 534,59 $ (21 aprile 2029) |

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
| Prima conferma | 126,78 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 135,23 $ | Scenario più credibile. |
| Invalidazione soft | 114,70 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 11 ottobre 2026 | -3,22% | 116,85 $ | 116,30 $ | 121,42 $ |
| 14 giorni | 18 ottobre 2026 | -0,03% | 120,71 $ | 116,30 $ | 122,04 $ |
| 30 giorni | 3 novembre 2026 | +0,25% | 121,04 $ | 116,30 $ | 130,64 $ |
| 60 giorni | 3 dicembre 2026 | -3,71% | 116,26 $ | 114,78 $ | 130,64 $ |
| 90 giorni | 2 gennaio 2027 | -4,70% | 115,06 $ | 107,67 $ | 130,64 $ |
| 120 giorni | 1 febbraio 2027 | +6,17% | 128,19 $ | 107,67 $ | 134,88 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 4 ottobre 2026 -> 18 ottobre 2026 | -0,03% | 116,30 $ (10 ottobre 2026) | 122,04 $ (14 ottobre 2026) | 120,71 $ | Laterale / movimento non forte. |
| Step 2 - primo mese | 19 ottobre 2026 -> 3 novembre 2026 | +0,25% | 119,67 $ (21 ottobre 2026) | 130,64 $ (28 ottobre 2026) | 121,04 $ | Spike poco sostenuto. |
| Step 3 - secondo mese | 4 novembre 2026 -> 3 dicembre 2026 | -3,71% | 114,78 $ (26 novembre 2026) | 126,56 $ (18 novembre 2026) | 116,26 $ | Prima spike, poi scarico. |
| Step 4 - terzo mese | 4 dicembre 2026 -> 2 gennaio 2027 | -4,70% | 107,67 $ (28 dicembre 2026) | 120,35 $ (11 dicembre 2026) | 115,06 $ | Laterale / movimento non forte. |

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
| Prezzo SOL | 120,74 $ |  |
| Weekly RSI | 64,52 / linea grezza 51,53 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 50,54 / linea grezza 55,13 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 534,59 $ | Avanzamento +22,59% |
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
| Score on-chain | 0 |
| Bias | NEUTRALE / MISTA |
| Azione coerente | NESSUNA CONFERMA FORTE / LEGGERE INSIEME AL FRATTALE |
| Prezzo SOL | 120,74 $ |
| TVL Solana | 6,68 mld $ |
| TVL 7g | +0,94% |
| DEX volume 24h | 2,13 mld $ |
| Fees 24h | 12,97 mln $ |
| Stablecoin su Solana | 16,82 mld $ |
| Stake ratio | 69,59% |
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
| Prezzo SOL | 120,74 $ |
| EMA200 weekly target | 111,42 $ |
| Upside verso EMA200 | -7,72% |
| Distanza prezzo da EMA200 | +8,37% |
| Gap EMA50/EMA200 | -4,62% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 64,52 |
| Età SOL | 6,5 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +100,00% |
| Max gain mediano 12w | +21,63% |
| Drawdown mediano 12w | -22,91% |

Lettura semplice:

**SOLO OSSERVAZIONE**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-10-04 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-10-04 05:30:22 UTC**

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
| BTC | NESSUN CAMBIAMENTO FORTE | miglioramento | NEUTRALE / INCERTO | +50.00% | +2.50 punti |
| SOL | CAMBIAMENTO MEDIO | peggioramento | NEUTRALE / INCERTO | +35.00% | -5.00 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | miglioramento | NEUTRALE / INCERTO | +35.00% | 0.00 punti |

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
| BTC | 80.602 $ | 93.329 $ | +41,38% | +15,79% | rimbalzo debole | 93.329 $ | 80.602 $ | +44,83% | -13,64% | scarico possibile |
| SOL | 114,70 $ | 132,81 $ | +25,00% | +15,79% | rimbalzo poco frequente | 132,81 $ | 114,70 $ | +47,83% | -13,64% | scarico possibile |
| DOGE | 0,08814 $ | 0,10206 $ | +33,33% | +15,79% | rimbalzo poco frequente | 0,10206 $ | 0,08814 $ | +50,00% | -13,64% | attenzione a prendere profitto |

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

- **BTC: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +41,38% (12/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 13 poi sono scaricati a -5,00%. Percentuale: +44,83% (13/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.**
- **SOL: su 40 casi simili, 32 prima sono scesi a -5,00%. Tra quei 32, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +25,00% (8/32). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 11 poi sono scaricati a -5,00%. Percentuale: +47,83% (11/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.**
- **DOGE: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +33,33% (11/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 12 poi sono scaricati a -5,00%. Percentuale: +50,00% (12/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-10-04 05:31:53 UTC

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-10-04 | 2026-10-04T05:30:21Z | 2026-10-04 05:30:22 |
| SOL | 2026-10-04 | 2026-10-04T05:30:21Z | 2026-10-04 05:30:22 |
| DOGE | 2026-10-04 | 2026-10-04T05:30:21Z | 2026-10-04 05:30:22 |

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
| BTC | 2026-10-04 | 84.844 $ | INCERTO | 50,00% | 71.667,53 $ | 78.166,76 $ | 84.378,44 $ | 103.324,22 $ | 118.063,28 $ |
| SOL | 2026-10-04 | 120,74 $ | DISCESA | 35,00% | 100,89 $ | 106,56 $ | 112,82 $ | 136,05 $ | 164,55 $ |
| DOGE | 2026-10-04 | 0.09278 $ | DISCESA | 35,00% | 0.07393 $ | 0.08067 $ | 0.08814 $ | 0.11299 $ | 0.13665 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | AVAILABLE | SAME_BTC_REGIME | 1 | 1 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 84.378,44 $ | 83.443,41 $ | 118.063,28 $ | 108.624,57 $ |
| SOL | AVAILABLE | SAME_ASSET_REGIME | 2 | 6 | 12 | 6 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 112,82 $ | 123,47 $ | 164,55 $ | 182,04 $ |
| DOGE | AVAILABLE | SAME_BTC_REGIME | 0 | 1 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.08814 $ | 0.08997 $ | 0.13665 $ | 0.11762 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-09-04**; verificato fino al **2026-10-04**; stato **COMPLETO 30/30g**.
- Reale **84.845,39 $**; p50 previsto **91.365,78 $**; scarto **-7,14%**.
- Errore medio assoluto **3,31%**; massimo **9,24%**; DENTRO p10-p90; DENTRO p25-p75.

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

**Campione corrente:** 8 episodi qualificati su 40 · 8 asset distinti.

**SMALL SAMPLE / DIAGNOSTIC ONLY:** le frequenze empiriche non sono probabilità calibrate.

![SOL conditional successor corrente](scanner_forecast_SOL_conditional_successor_current.png)

###### Confronto diretto a 30 giorni

| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Cono standard | 2026-10-04 | 40 | 2026-11-03 | 100.89 $ | 106.56 $ | 112.82 $ | 136.05 $ | 164.55 $ |
| Conditional corrente | 2026-10-04 | 8 | 2026-11-03 | 92.91 $ | 106.16 $ | 126.99 $ | 155.50 $ | 243.36 $ |

###### Struttura successiva dei casi correnti

| Classe | Episodi | Frequenza empirica |
| --- | ---: | ---: |
| DIRECT_CONTINUATION | 4 | 50.00% |
| SHALLOW_PULLBACK_THEN_CONTINUATION | 0 | 0.00% |
| DEEP_PULLBACK_THEN_RECOVERY | 1 | 12.50% |
| FAILURE | 3 | 37.50% |
| UNRESOLVED | 0 | 0.00% |

###### Episodi qualificati oggi

| Asset | Match window | -5% hit | +10% anchor | Classe 60d |
| --- | --- | --- | --- | --- |
| RUNE-USD | 2023-06-21 → 2023-09-28 | 2023-10-06 | 2023-10-23 | DIRECT_CONTINUATION |
| BTC-USD | 2022-11-21 → 2023-02-28 | 2023-03-08 | 2023-03-17 | DIRECT_CONTINUATION |
| KSM-USD | 2023-09-06 → 2023-12-14 | 2023-12-15 | 2023-12-21 | DIRECT_CONTINUATION |
| EOS-USD | 2023-09-08 → 2023-12-16 | 2023-12-19 | 2023-12-27 | FAILURE |
| KAVA-USD | 2023-09-08 → 2023-12-16 | 2023-12-18 | 2023-12-26 | FAILURE |
| XTZ-USD | 2023-09-08 → 2023-12-16 | 2023-12-18 | 2023-12-25 | FAILURE |
| ETC-USD | 2023-09-08 → 2023-12-16 | 2023-12-19 | 2024-01-10 | DIRECT_CONTINUATION |
| AVAX-USD | 2021-06-21 → 2021-09-28 | 2021-10-10 | 2021-10-25 | DEEP_PULLBACK_THEN_RECOVERY |

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

- Ultimo close disponibile: **2026-10-04** · SOL **120.74 $**.
- Giorno del vintage: **16/30**.
- P50 condizionato previsto per quel giorno: **123.57 $**.
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

- Cono congelato il **2026-09-04**; verificato fino al **2026-10-04**; stato **COMPLETO 30/30g**.
- Reale **120,74 $**; p50 previsto **118,15 $**; scarto **2,19%**.
- Errore medio assoluto **4,22%**; massimo **15,54%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_ASSET_REGIME**; fallback: **1_SAME_ASSET_FALLBACK**; motivo: **FALLBACK_TO_SAME_ASSET_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted SOL](scanner_forecast_SOL_regime_adjusted.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-09-04**; verificato fino al **2026-10-04**; stato **COMPLETO 30/30g**.
- Reale **0.09275 $**; p50 previsto **0.07929 $**; scarto **16,98%**.
- Errore medio assoluto **9,30%**; massimo **20,13%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted DOGE](scanner_forecast_DOGE_regime_adjusted.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 78 | 93,59% | 69,23% | 1,97% | 0,42% |
| BTC | 3g | 74 | 93,24% | 75,68% | 3,36% | 0,69% |
| BTC | 7g | 67 | 92,54% | 68,66% | 4,88% | 1,75% |
| BTC | 14g | 54 | 98,15% | 72,22% | 5,57% | 2,13% |
| BTC | 30g | 27 | 100,00% | 92,59% | 8,20% | 2,71% |
| SOL | 1g | 78 | 83,33% | 64,10% | 2,68% | 0,88% |
| SOL | 3g | 74 | 91,89% | 74,32% | 3,92% | 1,76% |
| SOL | 7g | 67 | 91,04% | 73,13% | 5,48% | 3,75% |
| SOL | 14g | 54 | 87,04% | 75,93% | 8,04% | 7,16% |
| SOL | 30g | 27 | 92,59% | 55,56% | 14,43% | 13,95% |
| DOGE | 1g | 78 | 88,46% | 61,54% | 3,05% | 0,52% |
| DOGE | 3g | 74 | 91,89% | 63,51% | 4,68% | 1,45% |
| DOGE | 7g | 67 | 76,12% | 74,63% | 8,50% | 5,88% |
| DOGE | 14g | 54 | 83,33% | 46,30% | 11,35% | 9,79% |
| DOGE | 30g | 27 | 92,59% | 33,33% | 17,78% | 17,78% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |

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

Generato: 2026-10-04 05:32 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +50,00%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +65,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +65,00%       | Nessun lato sopra soglia estrema |                  40 |

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
- Casi positivi / salita storica: **50,00%**
- Casi negativi / discesa storica: **50,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **84.844,13 $**
- Return normale fra 30 giorni: **84.378,44 $** (-0,55%)
- Drawdown normale durante il mese: **75.456,78 $** (-11,06%)
- Drawdown brutto da rispettare: **71.779,36 $** (-15,40%)
- Max gain normale durante il mese: **99.836,03 $** (17,67%)
- Max gain buono / take profit ottimistico: **117.893,94 $** (38,95%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **35,00%**
- Casi negativi / discesa storica: **65,00%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **120,74 $**
- Return normale fra 30 giorni: **112,82 $** (-6,56%)
- Drawdown normale durante il mese: **104,72 $** (-13,27%)
- Drawdown brutto da rispettare: **95,27 $** (-21,09%)
- Max gain normale durante il mese: **138,59 $** (14,78%)
- Max gain buono / take profit ottimistico: **155,73 $** (28,98%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **35,00%**
- Casi negativi / discesa storica: **65,00%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **0,09 $**
- Return normale fra 30 giorni: **0,09 $** (-5,00%)
- Drawdown normale durante il mese: **0,08 $** (-15,10%)
- Drawdown brutto da rispettare: **0,07 $** (-22,10%)
- Max gain normale durante il mese: **0,11 $** (16,49%)
- Max gain buono / take profit ottimistico: **0,12 $** (32,51%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è prudente/debole. Lo scanner vede più rischio di discesa che salita pulita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 84.844,13 $

**Direzione più probabile a 30 giorni:** **INCERTO**
- Probabilità storica di salita: **50,00%**
- Probabilità storica di discesa: **50,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è incerta, con segnale molto debole / quasi pari. Nei casi storici simili non c'è stato un vantaggio chiaro né per salita né per discesa.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **71.667,53 $** (-15,53%)
- Se va male: **78.166,76 $** (-7,87%)
- Scenario normale: **84.378,44 $** (-0,55%)
- Se va bene: **103.324,22 $** (21,78%)
- Se va molto bene: **118.063,28 $** (39,15%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **75.456,78 $** (-11,06%)
- Discesa brutta: **71.779,36 $** (-15,40%)
- Discesa molto brutta: **65.623,13 $** (-22,65%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **99.836,03 $** (17,67%)
- Rialzo buono: **117.893,94 $** (38,95%)
- Rialzo molto forte: **140.425,01 $** (65,51%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **75.456,78 $** e uno spike normale intorno a **99.836,03 $**.

La chiusura a 30 giorni è incerta: salita 50,00%, discesa 50,00%. Non c'è un vantaggio netto.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 120,74 $

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

- Se va molto male: **100,89 $** (-16,44%)
- Se va male: **106,56 $** (-11,74%)
- Scenario normale: **112,82 $** (-6,56%)
- Se va bene: **136,05 $** (12,68%)
- Se va molto bene: **164,55 $** (36,28%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **104,72 $** (-13,27%)
- Discesa brutta: **95,27 $** (-21,09%)
- Discesa molto brutta: **90,39 $** (-25,14%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **138,59 $** (14,78%)
- Rialzo buono: **155,73 $** (28,98%)
- Rialzo molto forte: **199,84 $** (65,51%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **104,72 $** e uno spike normale intorno a **138,59 $**.

La chiusura a 30 giorni era più spesso negativa: salita 35,00%, discesa 65,00%. Quindi la lettura principale è prudente/debole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 0,09 $

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

- Se va molto male: **0,07 $** (-20,32%)
- Se va male: **0,08 $** (-13,06%)
- Scenario normale: **0,09 $** (-5,00%)
- Se va bene: **0,11 $** (21,78%)
- Se va molto bene: **0,14 $** (47,29%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,08 $** (-15,10%)
- Discesa brutta: **0,07 $** (-22,10%)
- Discesa molto brutta: **0,07 $** (-26,37%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,11 $** (16,49%)
- Rialzo buono: **0,12 $** (32,51%)
- Rialzo molto forte: **0,18 $** (96,52%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,08 $** e uno spike normale intorno a **0,11 $**.

La chiusura a 30 giorni era più spesso negativa: salita 35,00%, discesa 65,00%. Quindi la lettura principale è prudente/debole.

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

- Previsioni già controllate: **34**
- Direzione corretta: **88,89%**
- Errore medio dello scenario centrale: **6,84%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **2,94%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **34**
- Direzione corretta: **89,29%**
- Errore medio dello scenario centrale: **15,81%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **29,41%**
- Prezzo finale dentro lo scenario 10%-90%: **94,12%**

### Solana

- Previsioni già controllate: **34**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **11,86%**
- Zona rischio toccata: **5,88%**
- Zona rialzo media toccata: **32,35%**
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

- Previsioni controllate: **34**
- Previsioni usate per la calibrazione recente: **34**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **88,89%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **INCERTO**
- Direzione calibrata oggi: **INCERTO**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **-0,55%** → **84.378,44 $**
- Correzione imparata dagli errori: **1,80%**
- Calibrato: **1,25%** → **85.901,91 $**
- Lettura: Lo scanner è stato abbastanza centrato sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-11,06%** → **75.456,78 $**
- Correzione imparata dagli errori: **5,20%**
- Calibrato: **-5,87%** → **79.867,74 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **17,67%** → **99.836,03 $**
- Correzione imparata dagli errori: **-3,28%**
- Calibrato: **14,39%** → **97.054,49 $**
- Lettura: Lo scanner ha sovrastimato gli spike: nella realtà il prezzo è salito meno del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Solana

- Previsioni controllate: **34**
- Previsioni usate per la calibrazione recente: **34**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **100,00%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **DISCESA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **-6,56%** → **112,82 $**
- Correzione imparata dagli errori: **8,76%**
- Calibrato: **2,20%** → **123,40 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-13,27%** → **104,72 $**
- Correzione imparata dagli errori: **3,49%**
- Calibrato: **-9,78%** → **108,93 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **14,78%** → **138,59 $**
- Correzione imparata dagli errori: **2,71%**
- Calibrato: **17,49%** → **141,86 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Dogecoin

- Previsioni controllate: **34**
- Previsioni usate per la calibrazione recente: **34**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **89,29%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **DISCESA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **-5,00%** → **0,09 $**
- Correzione imparata dagli errori: **15,81%**
- Calibrato: **10,81%** → **0,10 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-15,10%** → **0,08 $**
- Correzione imparata dagli errori: **14,50%**
- Calibrato: **-0,60%** → **0,09 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **16,49%** → **0,11 $**
- Correzione imparata dagli errori: **2,70%**
- Calibrato: **19,19%** → **0,11 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 84.844,13 $

Bitcoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **50,00%**
- Casi negativi dopo 30 giorni: **50,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **87,05%**
- Rendimento medio dopo 30 giorni: **9,40%**
- Rendimento centrale dopo 30 giorni: **-0,55%**
- Discesa media durante i 30 giorni: **-11,70%**
- Massimo rialzo medio durante i 30 giorni: **29,62%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **92.822,86 $**
- Scenario centrale a 30 giorni: **84.378,44 $**
- Zona di rischio media: **74.913,22 $**
- Zona di rialzo media: **109.975,27 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -15,53% → **71.667,53 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -7,87% → **78.166,76 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -0,55% → **84.378,44 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 21,78% → **103.324,22 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 39,15% → **118.063,28 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -22,65% → **65.623,13 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -15,40% → **71.779,36 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -11,06% → **75.456,78 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,78% → **80.791,15 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -1,03% → **83.973,53 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **84.844,13 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 4,00% → **88.240,36 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 17,67% → **99.836,03 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 38,95% → **117.893,94 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 65,51% → **140.425,01 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| BTC-USD         | 2022-11-21   | 2023-02-28 |        91.99 |        21.11 |         -12.79 |          22.47 |
| RUNE-USD        | 2023-06-16   | 2023-09-23 |        90.38 |        25.2  |         -11.23 |          25.2  |
| INJ-USD         | 2023-08-31   | 2023-12-08 |        89.01 |        89.93 |          -3.56 |         124.52 |
| EGLD-USD        | 2023-09-08   | 2023-12-16 |        88.84 |       -12.39 |         -15.18 |          20    |
| XTZ-USD         | 2023-09-08   | 2023-12-16 |        88.72 |        23.8  |          -8.09 |          23.8  |
| QTUM-USD        | 2023-09-03   | 2023-12-11 |        88.72 |         1.33 |          -4.79 |          19.28 |
| ETH-USD         | 2022-11-17   | 2023-02-24 |        88.71 |        10.4  |         -11.14 |          12.93 |
| THETA-USD       | 2023-09-07   | 2023-12-15 |        88.44 |        -2.94 |          -2.94 |          35.89 |
| AAVE-USD        | 2022-11-20   | 2023-02-27 |        87.99 |        -9.26 |         -16.04 |           3.18 |
| ATOM-USD        | 2023-09-08   | 2023-12-16 |        87.93 |       -15.48 |         -21.95 |           0    |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 120,74 $

Solana è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **35,00%**
- Casi negativi dopo 30 giorni: **65,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **87,16%**
- Rendimento medio dopo 30 giorni: **2,88%**
- Rendimento centrale dopo 30 giorni: **-6,56%**
- Discesa media durante i 30 giorni: **-13,62%**
- Massimo rialzo medio durante i 30 giorni: **23,00%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **124,22 $**
- Scenario centrale a 30 giorni: **112,82 $**
- Zona di rischio media: **104,29 $**
- Zona di rialzo media: **148,51 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -16,44% → **100,89 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -11,74% → **106,56 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -6,56% → **112,82 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 12,68% → **136,05 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 36,28% → **164,55 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -25,14% → **90,39 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -21,09% → **95,27 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -13,27% → **104,72 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -6,96% → **112,33 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **120,74 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **120,74 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 3,58% → **125,06 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 14,78% → **138,59 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 28,98% → **155,73 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 65,51% → **199,84 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| RUNE-USD        | 2023-06-21   | 2023-09-28 |        90.49 |        29.46 |         -20.98 |          29.46 |
| CRV-USD         | 2022-11-21   | 2023-02-28 |        89.89 |        -7.24 |         -15.46 |           4.32 |
| ATOM-USD        | 2023-09-13   | 2023-12-21 |        89.1  |       -13.76 |         -17.48 |           4.95 |
| EGLD-USD        | 2023-09-08   | 2023-12-16 |        88.85 |       -12.39 |         -15.18 |          20    |
| HBAR-USD        | 2022-11-19   | 2023-02-26 |        88.67 |       -20.31 |         -23.17 |           0    |
| MKR-USD         | 2018-12-24   | 2019-04-02 |        88.63 |       -29.36 |         -36.47 |           0    |
| BTC-USD         | 2022-11-21   | 2023-02-28 |        88.19 |        21.11 |         -12.79 |          22.47 |
| THETA-USD       | 2022-11-21   | 2023-02-28 |        88.16 |        -9.46 |         -21.44 |           6.02 |
| ENJ-USD         | 2022-11-22   | 2023-03-01 |        88.1  |       -15.05 |         -26.18 |           0    |
| AAVE-USD        | 2022-11-20   | 2023-02-27 |        88.05 |        -9.26 |         -16.04 |           3.18 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 0,09 $

Dogecoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **35,00%**
- Casi negativi dopo 30 giorni: **65,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **84,03%**
- Rendimento medio dopo 30 giorni: **10,15%**
- Rendimento centrale dopo 30 giorni: **-5,00%**
- Discesa media durante i 30 giorni: **-15,25%**
- Massimo rialzo medio durante i 30 giorni: **32,18%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,10 $**
- Scenario centrale a 30 giorni: **0,09 $**
- Zona di rischio media: **0,08 $**
- Zona di rialzo media: **0,12 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -20,32% → **0,07 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -13,06% → **0,08 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -5,00% → **0,09 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 21,78% → **0,11 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 47,29% → **0,14 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -26,37% → **0,07 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -22,10% → **0,07 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -15,10% → **0,08 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -5,45% → **0,09 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -2,71% → **0,09 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,09 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 1,38% → **0,09 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 16,49% → **0,11 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 32,51% → **0,12 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 96,52% → **0,18 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XTZ-USD         | 2019-09-14   | 2019-12-22 |        87.13 |         4.58 |         -15.44 |           8.21 |
| NEAR-USD        | 2023-09-08   | 2023-12-16 |        86.94 |        38.69 |          -4.73 |          80.83 |
| EGLD-USD        | 2023-09-08   | 2023-12-16 |        86.21 |       -12.39 |         -15.18 |          20    |
| AAVE-USD        | 2022-11-20   | 2023-02-27 |        85.85 |        -9.26 |         -16.04 |           3.18 |
| BTC-USD         | 2022-11-21   | 2023-02-28 |        85.61 |        21.11 |         -12.79 |          22.47 |
| ALGO-USD        | 2026-02-08   | 2026-05-18 |        85.53 |        -9.06 |         -20.22 |          16.94 |
| ENJ-USD         | 2022-11-22   | 2023-03-01 |        85.42 |       -15.05 |         -26.18 |           0    |
| EOS-USD         | 2023-09-08   | 2023-12-16 |        85.36 |        -3.03 |         -12.83 |          12.39 |
| HBAR-USD        | 2023-09-10   | 2023-12-18 |        85    |        -0.62 |          -5.39 |          22.01 |
| SOL-USD         | 2022-11-20   | 2023-02-27 |        84.93 |        -6.97 |         -23.73 |           0    |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report

Generated: 2026-10-04 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-04 | RECOVERY | 84.844 $ | True | 32.58% | 1.09% | RECOVERY | 32.58% | 1.09% |
| DOGE-USD | 2026-10-04 | RECOVERY | 0.09278 $ | True | 21.15% | -5.82% | RECOVERY | 32.58% | 1.09% |
| SOL-USD | 2026-10-04 | RECOVERY | 120,74 $ | True | 47.40% | 1.34% | RECOVERY | 32.58% | 1.09% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 50.00% | -0.55% | 21.78% | 39.15% | -11.06% | -22.65% | 17.67% | 38.95% | 65.51% | 52.50% | 0.46% | 32.29% | 86.69% |
| BTC-USD | SAME_BTC_REGIME | 13 | 46.15% | -1.65% | 9.65% | 28.03% | -8.66% | -14.72% | 20.00% | 31.38% | 41.49% | 38.46% | -3.46% | 0.84% | 26.50% |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 29.09% | 29.09% | 29.09% | -7.20% | -7.20% | 42.37% | 42.37% | 42.37% | 100.00% | 29.72% | 29.72% | 29.72% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 29.09% | 29.09% | 29.09% | -7.20% | -7.20% | 42.37% | 42.37% | 42.37% | 100.00% | 29.72% | 29.72% | 29.72% |
| DOGE-USD | ALL_MATCHES | 40 | 35.00% | -5.00% | 21.78% | 47.29% | -15.10% | -26.37% | 16.49% | 32.51% | 96.52% | 47.50% | -2.00% | 29.77% | 101.64% |
| DOGE-USD | SAME_BTC_REGIME | 9 | 33.33% | -3.03% | 6.09% | 26.78% | -9.25% | -16.54% | 20.00% | 30.24% | 41.27% | 44.44% | -2.99% | 8.08% | 18.92% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 0.00% | -0.62% | -0.62% | -0.62% | -5.39% | -5.39% | 22.01% | 22.01% | 22.01% | 100.00% | 7.74% | 7.74% | 7.74% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 35.00% | -6.56% | 12.68% | 36.28% | -13.27% | -25.14% | 14.78% | 28.98% | 65.51% | 45.00% | -1.53% | 34.72% | 86.86% |
| SOL-USD | SAME_BTC_REGIME | 12 | 33.33% | -3.36% | 9.80% | 28.56% | -9.74% | -15.04% | 22.55% | 29.46% | 41.27% | 33.33% | -2.49% | 3.47% | 28.11% |
| SOL-USD | SAME_ASSET_REGIME | 6 | 50.00% | 2.26% | 23.10% | 50.77% | -6.30% | -30.34% | 25.41% | 38.98% | 66.76% | 50.00% | 3.01% | 24.22% | 57.41% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 17.11% | 23.10% | 26.69% | -3.60% | -6.48% | 35.59% | 38.98% | 41.02% | 50.00% | 13.99% | 21.85% | 26.57% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 21 | 52.38% | 0.23% | -11.14% | 41.87% | 57.14% | 2.97% | 43.24% |
| BTC-USD | HISTORICAL_BTC_BULL | 4 | 50.00% | -0.51% | -13.48% | 84.24% | 75.00% | 89.21% | 288.36% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 50.00% | -12.65% | -31.59% | 18.90% | 50.00% | 100.93% | 205.53% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 13 | 46.15% | -1.65% | -8.66% | 31.38% | 38.46% | -3.46% | 31.38% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 25 | 28.00% | -7.24% | -17.65% | 26.28% | 40.00% | -6.05% | 35.89% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 80.00% | 29.46% | -15.44% | 110.64% | 80.00% | 146.24% | 232.96% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -8.72% | -8.72% | 52.83% | 100.00% | 14.96% | 52.83% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 9 | 33.33% | -3.03% | -9.25% | 30.24% | 44.44% | -2.99% | 30.24% |
| SOL-USD | HISTORICAL_BTC_BEAR | 19 | 31.58% | -7.24% | -15.46% | 29.18% | 47.37% | -1.33% | 54.54% |
| SOL-USD | HISTORICAL_BTC_BULL | 9 | 44.44% | -10.38% | -15.44% | 22.56% | 55.56% | 32.95% | 146.24% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 12 | 33.33% | -3.36% | -9.74% | 29.46% | 33.33% | -2.49% | 29.46% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 35 | 48.57% | -1.32% | -11.14% | 33.64% | 48.57% | -1.33% | 39.92% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | 81.51% | -7.14% | 145.42% | 50.00% | 198.24% | 358.24% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 32.89% | -14.30% | 93.49% | 100.00% | 57.96% | 106.96% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 29.09% | -7.20% | 42.37% | 100.00% | 29.72% | 42.37% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 34 | 32.35% | -7.11% | -15.45% | 28.66% | 41.18% | -3.11% | 34.84% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 47.00% | 0.00% | 150.35% | 66.67% | 14.96% | 292.23% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 32.89% | -14.30% | 93.49% | 100.00% | 57.96% | 106.96% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -0.62% | -5.39% | 22.01% | 100.00% | 7.74% | 22.01% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 30.00% | -7.35% | -13.76% | 24.60% | 40.00% | -4.49% | 42.92% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | -5.93% | -13.21% | 44.53% | 75.00% | 43.60% | 113.91% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | 2.26% | -6.30% | 38.98% | 50.00% | 3.01% | 38.98% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | SAME_BTC_REGIME | 1 | 1 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | SAME_BTC_REGIME | 0 | 1 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| SOL-USD | SAME_ASSET_REGIME | 2 | 6 | 12 | 6 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING DOGE-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | EGLD-USD | 2023-09-08 | 88.84% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -12.39% | -15.18% | 20.00% | 0.08% | -19.94% | 20.00% |
| BTC-USD | XTZ-USD | 2023-09-08 | 88.72% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 23.80% | -8.09% | 23.80% | 13.64% | -8.09% | 23.80% |
| BTC-USD | QTUM-USD | 2023-09-03 | 88.72% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 1.33% | -4.79% | 19.28% | -3.46% | -10.06% | 19.28% |
| BTC-USD | ATOM-USD | 2023-09-08 | 87.93% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.48% | -21.95% | 0.00% | -15.03% | -25.65% | 0.00% |
| BTC-USD | EOS-USD | 2023-09-08 | 87.87% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -12.83% | 12.39% | -5.97% | -15.90% | 12.39% |
| BTC-USD | MANA-USD | 2023-09-03 | 87.71% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -5.13% | -12.85% | 14.59% | -4.63% | -13.25% | 14.59% |
| BTC-USD | ETC-USD | 2023-09-08 | 87.12% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BULLISH_30D | 29.09% | -7.20% | 42.37% | 29.72% | -7.20% | 42.37% |
| BTC-USD | XRP-USD | 2023-09-08 | 86.40% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.08% | -10.99% | 4.28% | -13.14% | -18.82% | 4.28% |
| BTC-USD | KAVA-USD | 2023-09-08 | 86.16% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.45% | -9.25% | 16.06% | -9.35% | -17.51% | 16.06% |
| BTC-USD | NEAR-USD | 2023-09-08 | 85.59% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 38.69% | -4.73% | 80.83% | 40.02% | -4.73% | 80.83% |
| DOGE-USD | NEAR-USD | 2023-09-08 | 86.94% | RECOVERY | BEAR | SAME_BTC_ONLY | HIGH_SPIKE_60D | 38.69% | -4.73% | 80.83% | 40.02% | -4.73% | 80.83% |
| DOGE-USD | EGLD-USD | 2023-09-08 | 86.21% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -12.39% | -15.18% | 20.00% | 0.08% | -19.94% | 20.00% |
| DOGE-USD | EOS-USD | 2023-09-08 | 85.36% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -3.03% | -12.83% | 12.39% | -5.97% | -15.90% | 12.39% |
| DOGE-USD | XTZ-USD | 2023-09-08 | 84.68% | RECOVERY | BEAR | SAME_BTC_ONLY | BULLISH_30D | 23.80% | -8.09% | 23.80% | 13.64% | -8.09% | 23.80% |
| DOGE-USD | KAVA-USD | 2023-09-08 | 84.65% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -7.45% | -9.25% | 16.06% | -9.35% | -17.51% | 16.06% |
| DOGE-USD | DOT-USD | 2023-09-08 | 84.39% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | 6.09% | -5.23% | 30.24% | 8.08% | -10.63% | 30.24% |
| DOGE-USD | LRC-USD | 2023-09-08 | 83.88% | RECOVERY | BEAR | SAME_BTC_ONLY | MIXED | -1.65% | -8.66% | 31.38% | -3.24% | -12.90% | 31.38% |
| DOGE-USD | ATOM-USD | 2023-09-08 | 82.80% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -15.48% | -21.95% | 0.00% | -15.03% | -25.65% | 0.00% |
| DOGE-USD | MANA-USD | 2023-09-08 | 82.42% | RECOVERY | BEAR | SAME_BTC_ONLY | BEARISH_30D | -10.01% | -15.01% | 11.74% | -2.99% | -15.41% | 11.74% |
| SOL-USD | MKR-USD | 2018-12-24 | 88.63% | BEAR | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -29.36% | -36.47% | 0.00% | -7.04% | -36.47% | 0.00% |
| SOL-USD | HBAR-USD | 2023-09-10 | 87.83% | BEAR | RECOVERY | SAME_ASSET_ONLY | MIXED | -0.62% | -5.39% | 22.01% | 7.74% | -13.94% | 22.01% |
| SOL-USD | WAVES-USD | 2023-09-08 | 87.35% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | MIXED | 5.14% | 0.00% | 28.82% | -1.73% | -11.91% | 28.82% |
| SOL-USD | ZEC-USD | 2024-05-20 | 86.84% | BULL | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -15.14% | -24.21% | 0.00% | -2.90% | -27.89% | 6.57% |
| SOL-USD | OP-USD | 2023-09-09 | 86.76% | BEAR | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 72.45% | 0.00% | 91.14% | 85.11% | 0.00% | 91.14% |
| SOL-USD | ETC-USD | 2023-09-08 | 86.21% | RECOVERY | RECOVERY | SAME_BTC_AND_ASSET | BULLISH_30D | 29.09% | -7.20% | 42.37% | 29.72% | -7.20% | 42.37% |

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

Generato: 2026-10-04 05:32 UTC

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
| BTC | 84.844 $ | +6 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | BASSO | SPOT OK / LONG SOLO PRUDENTE SU CONFERMA |
| SOL | 120,74 $ | +8 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | BASSO | TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME |
| DOGE | 0.09278 $ | +1 | NEUTRALE / MISTO | STAGE 3 / DISTRIBUZIONE O PAUSA | VOLATILITÀ IN ESPANSIONE | RANGE / FASE NON CHIARA | MEDIO | STAI ALLA FINESTRA |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | +2 | 0 | 0 | 0 | 0 | +2 | +6 |
| SOL | +3 | +2 | -1 | +2 | 0 | 0 | +2 | +8 |
| DOGE | +1 | 0 | -1 | +1 | 0 | 0 | 0 | +1 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 82.571 $ | 87.364 $ | 87.364 $ | 62.227 $ | 2,65% | 4,40% | 33,52% |
| SOL | 116,53 $ | 124,62 $ | 124,62 $ | 70,69 $ | 4,01% | 16,12% | 48,29% |
| DOGE | 0.08189 $ | 0.09421 $ | 0.10528 $ | 0.06797 $ | 6,14% | 5,66% | 19,32% |

## Lettura dettagliata

### BTC

- Prezzo: **84.844 $**
- Score classico: **+6 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **SPOT OK / LONG SOLO PRUDENTE SU CONFERMA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,65%; distanza supporto 2,76%; distanza resistenza 2,96%

Dettaglio:

- Trend: **+2** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **0** — RSI sano 64.0; RSI in miglioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **0** — OBV sotto media; CMF positivo 0.09; volume ratio 0.38
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 63.99 |
| MACD histogram | -148.30089 |
| CMF20 | 0.093 |
| Volume ratio 20 | 0.38 |
| MA20 | 82.446 $ |
| MA50 | 78.560 $ |
| MA100 | 71.006 $ |
| MA200 | 71.426 $ |
| Pendenza MA50 20g | +10,40% |
| Pendenza MA200 60g | +0,87% |
| Bollinger width | 15,87% |
| Bollinger position | 0.68 |

### SOL

- Prezzo: **120,74 $**
- Score classico: **+8 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME**
- Volatilità tecnica locale: **BASSO** — ATR14 4,01%; distanza supporto 3,62%; distanza resistenza 3,21%

Dettaglio:

- Trend: **+3** — prezzo sopra MA200 daily; medie daily allineate rialziste; MA50 daily in salita; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-1** — RSI sano 65.0; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.21; volume ratio 0.35
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 65.05 |
| MACD histogram | -0.34380 |
| CMF20 | 0.210 |
| Volume ratio 20 | 0.35 |
| MA20 | 114,14 $ |
| MA50 | 103,79 $ |
| MA100 | 89,84 $ |
| MA200 | 85,80 $ |
| Pendenza MA50 20g | +18,05% |
| Pendenza MA200 60g | +0,92% |
| Bollinger width | 26,56% |
| Bollinger position | 0.71 |

### DOGE

- Prezzo: **0.09278 $**
- Score classico: **+1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **STAI ALLA FINESTRA**
- Volatilità tecnica locale: **MEDIO** — ATR14 6,14%; distanza supporto 13,26%; distanza resistenza 1,57%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **-1** — RSI sano 53.5; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **+1** — OBV sopra media; CMF neutrale 0.02; volume ratio 0.34
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 53.47 |
| MACD histogram | -0.00047 |
| CMF20 | 0.018 |
| Volume ratio 20 | 0.34 |
| MA20 | 0.09161 $ |
| MA50 | 0.08699 $ |
| MA100 | 0.07956 $ |
| MA200 | 0.08777 $ |
| Pendenza MA50 20g | +10,92% |
| Pendenza MA200 60g | -6,16% |
| Bollinger width | 27,26% |
| Bollinger position | 0.55 |

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

Generato: 2026-10-04 05:32 UTC

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
| BTC | 84.844 $ | Doppio minimo | CONFERMATO RECENTE | rialzista | 2026-09-21 | 89.580 $ | 35,28% | n/a | Fib 23,6% NON ATTIVO (0) @ 80.374 $ | NEL RANGE | 82.571 $ |
| SOL | 120,74 $ | Triplo massimo | CANDIDATO | ribassista | n/a | 62,51 $ | n/a | 70,79% | Fib 23,6% NON ATTIVO (0) @ 111,89 $ | NEL RANGE | 97,45 $ |
| DOGE | 0.09278 $ | Doppio minimo | CONFERMATO RECENTE | rialzista | 2026-09-21 | 0.11001 $ | -9,04% | n/a | Fib 38,2% TENUTO (+1) @ 0.09103 $ | NEL RANGE | 0.09274 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CONFERMATO RECENTE** (+2)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-09-15**
- Età formazione: **19 giorni**
- Breakout pattern: **2026-09-21**
- Età breakout: **13 giorni**
- Neckline: **82.262 $**
- Target teorico: **89.580 $**
- Progresso verso target: **35,28%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 80.374 $** — Swing UP 2026-07-01 57.748 -> 2026-09-21 87.364; livello più vicino 23.6% a 80.374; stato NON ATTIVO; confluenza: invalidazione rialzista.
- Invalidazione: **80.617 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due minimi simili vicino a 74.945 tra 2026-09-02 e 2026-09-15. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (13 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 89.580; progresso corrente: 35,28%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **82.571 $**
- Resistenza: **87.364 $**
- Breakout 60g: **87.364 $**
- Breakdown 60g: **62.227 $**
- RSI14: **63.97**
- ATR14: **2,65%**
- Volume ratio 20g: **0.38**
- Rendimento 30g: **+4,40%**
- Rendimento 90g: **+33,51%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CONFERMATO RECENTE | +2 | rialzista | 82.262 $ | 2026-09-21 | 13g | 89.580 $ | 35,28% | n/a | 80.617 $ | Due minimi simili a 76.248 $ e 74.945 $. Neckline circa 82.262 $. Breakout neckline: 2026-09-21 (13 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 89.580 $; progresso: 35,28%; prezzo sopra neckline. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 36,35% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 56 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **56 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **70,69 $**
- Target teorico: **62,51 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **70,79%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 111,89 $** — Swing UP 2026-08-01 70,69 -> 2026-09-27 124,62; livello più vicino 23.6% a 111,89; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **72,11 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 56 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **97,45 $**
- Resistenza: **124,62 $**
- Breakout 60g: **124,62 $**
- Breakdown 60g: **70,69 $**
- RSI14: **65.05**
- ATR14: **4,01%**
- Volume ratio 20g: **0.35**
- Rendimento 30g: **+16,12%**
- Rendimento 90g: **+48,29%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,51 $ | n/a | 70,79% | 72,11 $ | Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 56 giorni. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 70,79% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 56 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 107,12 $ | 2026-09-18 | 16g | 118,01 $ | 125,09% | n/a | 104,97 $ | Due minimi simili a 97,45 $ e 96,23 $. Neckline circa 107,12 $. Breakout neckline: 2026-09-18 (16 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01 $; progresso: 125,09%; prezzo sopra neckline. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 46g | 85,65 $ | 569,31% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (46 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 569,31%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CONFERMATO RECENTE** (+2)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-09-16**
- Età formazione: **18 giorni**
- Breakout pattern: **2026-09-21**
- Età breakout: **13 giorni**
- Neckline: **0.09421 $**
- Target teorico: **0.11001 $**
- Progresso verso target: **-9,04%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 38,2% TENUTO (+1) @ 0.09103 $** — Swing UP 2026-08-01 0.06797 -> 2026-09-22 0.10528; livello più vicino 38.2% a 0.09103; stato TENUTO; confluenza: neckline rialzista, invalidazione rialzista.
- Invalidazione: **0.09232 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 0.07841 tra 2026-09-02 e 2026-09-16. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (13 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 0.11001; progresso corrente: -9,04%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Doji / indecisione**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.09274 $**
- Resistenza: **0.09421 $**
- Breakout 60g: **0.10528 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **53.52**
- ATR14: **6,14%**
- Volume ratio 20g: **0.34**
- Rendimento 30g: **+5,69%**
- Rendimento 90g: **+19,36%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CONFERMATO RECENTE | +2 | rialzista | 0.09421 $ | 2026-09-21 | 13g | 0.11001 $ | -9,04% | n/a | 0.09232 $ | Due minimi simili a 0.08028 $ e 0.07841 $. Neckline circa 0.09421 $. Breakout neckline: 2026-09-21 (13 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 0.11001 $; progresso: -9,04%; prezzo sotto neckline. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.07841 $ | n/a | n/a | 0.05153 $ | n/a | 18,33% | 0.07997 $ | Due massimi simili a 0.09998 $ e 0.10528 $. Neckline circa 0.07841 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 12 giorni. |

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

Generato: 2026-10-04 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-10-04**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-21**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **120,74 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+71,85%**
- Aderenza live principale: **+68,52%**
- Errore medio live principale: **15,74%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **120**
- Osservazioni inclusive dal bottom: **121**
- Osservazioni da inizio programma/scanner: **94**
- Errore assoluto medio dal bottom: **13,57%**
- Errore assoluto medio da inizio programma: **15,74%**
- Gap firmato medio ultimi 7 giorni: **+12,81%**
- Errore assoluto medio ultimi 7 giorni: **12,81%**
- Gap ultimo giorno: **+8,78%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+8,78%**
- Gap firmato medio 7g: **+12,81%**
- Errore assoluto medio 7g: **12,81%**
- Variazione recente gap: **-2,68%**
- Stato gap: **SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 111 | 2026-09-25 | 2023-03-12 | 122,01 $ | 87,31 $ | +39,74% | da inizio programma |
| 112 | 2026-09-26 | 2023-03-13 | 121,43 $ | 95,32 $ | +27,39% | da inizio programma |
| 113 | 2026-09-27 | 2023-03-14 | 122,06 $ | 97,48 $ | +25,21% | da inizio programma |
| 114 | 2026-09-28 | 2023-03-15 | 118,84 $ | 96,02 $ | +23,76% | da inizio programma |
| 115 | 2026-09-29 | 2023-03-16 | 119,06 $ | 98,69 $ | +20,64% | da inizio programma |
| 116 | 2026-09-30 | 2023-03-17 | 117,99 $ | 108,03 $ | +9,22% | da inizio programma |
| 117 | 2026-10-01 | 2023-03-18 | 118,40 $ | 106,22 $ | +11,46% | da inizio programma |
| 118 | 2026-10-02 | 2023-03-19 | 118,62 $ | 110,45 $ | +7,39% | da inizio programma |
| 119 | 2026-10-03 | 2023-03-20 | 118,62 $ | 109,38 $ | +8,44% | da inizio programma |
| 120 | 2026-10-04 | 2023-03-21 | 120,74 $ | 110,99 $ | +8,78% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-11 | 107,42 $ | 116,85 $ | 116,30 $ / 121,42 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-18 | 110,96 $ | 120,71 $ | 116,30 $ / 122,04 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-25 | 119,10 $ | 129,56 $ | 116,30 $ / 129,56 $ | no | n/a | n/a | n/a |
| 28g | 2026-11-01 | 119,74 $ | 130,26 $ | 116,30 $ / 130,64 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-08 | 111,51 $ | 121,30 $ | 116,30 $ / 130,64 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-15 | 112,98 $ | 122,90 $ | 116,30 $ / 130,64 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-22 | 108,95 $ | 118,52 $ | 116,30 $ / 130,64 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-29 | 106,50 $ | 115,86 $ | 114,78 $ / 130,64 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-06 | 107,25 $ | 116,67 $ | 114,65 $ / 130,64 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-13 | 109,13 $ | 118,71 $ | 112,85 $ / 130,64 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-20 | 107,30 $ | 116,72 $ | 110,39 $ / 130,64 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-27 | 102,10 $ | 111,07 $ | 110,39 $ / 130,64 $ | no | n/a | n/a | n/a |
| 91g | 2027-01-03 | 111,59 $ | 121,39 $ | 107,67 $ / 130,64 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-10 | 120,89 $ | 131,51 $ | 107,67 $ / 131,54 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-17 | 121,24 $ | 131,89 $ | 107,67 $ / 133,51 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-24 | 120,62 $ | 131,22 $ | 107,67 $ / 133,51 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-31 | 117,61 $ | 127,94 $ | 107,67 $ / 134,88 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-07 | 115,13 $ | 125,25 $ | 107,67 $ / 134,88 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 76 | 38,16% | 11,97% | 14,61% |
| 14g | 70 | 24,29% | 17,07% | 15,11% |
| 21g | 66 | 25,76% | 21,85% | 16,17% |
| 28g | 59 | 22,03% | 23,18% | 16,35% |
| 35g | 52 | 34,62% | 24,64% | 16,20% |
| 42g | 45 | 44,44% | 23,02% | 15,05% |
| 49g | 38 | 52,63% | 24,22% | 17,62% |
| 56g | 33 | 48,48% | 21,62% | 18,34% |
| 63g | 26 | 42,31% | 14,81% | 21,18% |
| 70g | 19 | 57,89% | 9,95% | 25,71% |
| 77g | 12 | 41,67% | 10,01% | 18,20% |
| 84g | 5 | 100,00% | 6,51% | 8,21% |
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

Generato: 2026-10-04 05:32 UTC

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 84.802 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0055% | +1,95% | 2,05 | -4,74% | 0 $ | 0 $ |
| SOL | 120,76 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | -0,0007% | -0,23% | 1,06 | +13,86% | 0 $ | 0 $ |
| DOGE | 0.09279 $ | 3 | 0 | 0 | LEGGERMENTE NEGATIVA / NON PESATA | BASSA | 100% | +0,0096% | +0,52% | 0,79 | -9,98% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0008% | 170,40 mln $ | 1,90 | +8,87% |
| BTC | Bitget | OK | +0,0100% | 2,82 mld $ | 0,69 | -51,85% |
| BTC | Kucoin | OK | +0,0067% | 1,00 mld $ | 2,97 | -5,45% |
| SOL | Kraken | OK | +0,0259% | 33,43 mln $ | 1,48 | +6,62% |
| SOL | Bitget | OK | -0,0004% | 478,25 mln $ | 69,57 | -83,11% |
| SOL | Kucoin | OK | +0,0027% | 136,93 mln $ | 1,26 | -15,89% |
| DOGE | Kraken | OK | -0,0045% | 5,21 mln $ | 1,18 | -7,55% |
| DOGE | Bitget | OK | +0,0100% | 123,15 mln $ | 1,27 | -67,42% |
| DOGE | Kucoin | OK | +0,0100% | 58,43 mln $ | 1,85 | +11,21% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+1,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 8, accuratezza +37,50%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
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
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta.
- **RSI:** RSI alto ma sostenuto da acquisti e leva non estrema: momentum ancora credibile.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **-2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 11, accuratezza +45,45%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 2, divergenze 0.
- Flusso taker/order book: **-2,00**.
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
| BTC | +50,00% | -0,55% | 4 | +75,00% | RACCOLTA DATI | 0,00 | +50,00% | -0,55% |
| SOL | +35,00% | -6,56% | 5 | +100,00% | RACCOLTA DATI | 0,00 | +35,00% | -6,56% |
| DOGE | +35,00% | -5,00% | 8 | +75,00% | RACCOLTA DATI | 0,00 | +35,00% | -5,00% |

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

Generato: 2026-10-04 05:32 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **9**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-04 | BTC | 84.802,20 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 2,05 | +1,95% | -4,74% |
| 2026-10-04 | DOGE | 0.09279 | V2.1.3 | OK | 0 | 0 | -2,00 | BASSA | 0,79 | +0,52% | -9,98% |
| 2026-10-04 | SOL | 120,76 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,06 | -0,23% | +13,86% |
| 2026-10-03 | BTC | 84.535,00 | V2.1.3 | OK | 0 | 0 | -1,25 | BASSA | 0,77 | +4,45% | -6,45% |
| 2026-10-03 | DOGE | 0.09296 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,25 | -0,56% | +0,80% |
| 2026-10-03 | SOL | 119,07 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,36 | -2,40% | +7,35% |
| 2026-10-02 | BTC | 86.562,08 | V2.1.3 | OK | 1 | 0 | 3,25 | ALTA | 2,47 | +2,46% | +2,36% |
| 2026-10-02 | DOGE | 0.09653 | V2.1.3 | OK | 0 | 0 | 1,75 | MEDIA | 1,68 | +5,66% | -11,25% |
| 2026-10-02 | SOL | 121,84 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 2,91 | +0,44% | +6,60% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 9 | +33,33% | -0,58% | -1,37% | +0,50% | FEEDBACK RAPIDO |
| BTC | 3g | 8 | +37,50% | -0,46% | -2,47% | +1,78% | FEEDBACK RAPIDO |
| BTC | 7g | 8 | +37,50% | -1,56% | -3,39% | +2,06% | FEEDBACK RAPIDO |
| BTC | 14g | 5 | +40,00% | +0,20% | -4,71% | +3,32% | FEEDBACK RAPIDO |
| BTC | 30g | 4 | +75,00% | +5,12% | -4,99% | +8,32% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 5 | +100,00% | +22,07% | -4,32% | +25,38% | FEEDBACK RAPIDO |
| DOGE | 1g | 11 | +54,55% | +1,55% | -0,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 3g | 11 | +36,36% | +1,63% | -3,44% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 7g | 11 | +45,45% | -0,13% | -4,83% | +9,23% | FEEDBACK RAPIDO |
| DOGE | 14g | 10 | +40,00% | +1,75% | -5,70% | +14,70% | FEEDBACK RAPIDO |
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

**SOL** — SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**DOGE** — DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 84.844 $ | +0.0037% | n/d | 0.90 | Misto | 1/5 |
| SOL | 120,74 $ | +0.0100% | n/d | 1.97 | Rischio sotto | 2/5 |
| DOGE | 0.09278 $ | +0.0021% | n/d | 3.33 | Misto | 1/5 |

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

Generato: 2026-10-04 05:32 UTC

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                                                | Stato D   | Weekly             | Stato W    | Lettura weekly                                                                                                              |   Peso |
|:--------|:-----------------------------------------------------|:----------|:-------------------|:-----------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Misto / nessuna divergenza                           | CONTESTO  | Conferma rialzista | CONTESTO   | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| SOL     | Misto / nessuna divergenza                           | CONTESTO  | Conferma rialzista | CONTESTO   | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| DOGE    | Momentum in indebolimento, divergenza non confermata | CONTESTO  | Hidden bearish     | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                                                 | Stato      | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:-----------------------------------------------------|:-----------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Misto / nessuna divergenza                           | CONTESTO   | 84.851 $ / 63,99  | n/a                                                                 | +4,45%              | -0,32            |      0 |
| BTC     | 1W   | Conferma rialzista                                   | CONTESTO   | 84.851 $ / 61,88  | n/a                                                                 | +9,13%              | 5,24             |      0 |
| SOL     | 1D   | Misto / nessuna divergenza                           | CONTESTO   | 120,74 $ / 65,05  | n/a                                                                 | +8,76%              | 1,21             |      0 |
| SOL     | 1W   | Conferma rialzista                                   | CONTESTO   | 120,74 $ / 64,52  | n/a                                                                 | +26,51%             | 9,99             |      0 |
| DOGE    | 1D   | Momentum in indebolimento, divergenza non confermata | CONTESTO   | 0.09275 $ / 53,47 | n/a                                                                 | +5,73%              | -3,80            |      0 |
| DOGE    | 1W   | Hidden bearish                                       | CONFERMATA | 0.09275 $ / 50,29 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 49,72 | n/a                 | n/a              |      0 |

### BTC

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### SOL

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### DOGE

- **1D — Momentum in indebolimento, divergenza non confermata / CONTESTO**: Momentum in indebolimento, divergenza non confermata. Non esiste una divergenza confermata sugli ultimi pivot.
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
| DOGE    | 1W   | Hidden bearish   |          30 |           1 | 0,00%         | -13,35%           | RACCOLTA DATI |      0 |
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

Generato: 2026-10-04 05:32 UTC

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

| Asset   | Prezzo   |   Punteggio | Verdetto                      | Trend           | Momentum        | Struttura                                          |   Pattern score | Fibonacci      | Pattern rialzista                  | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:------------------------------|:----------------|:----------------|:---------------------------------------------------|----------------:|:---------------|:-----------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 84.844 $ | 9 | RIALZISTA TECNICO | Trend rialzista | Momentum misto | Struttura rialzista con massimi e minimi crescenti | +2 | 0 / NON ATTIVO | Doppio minimo / CONFERMATO RECENTE | Doppio massimo / CANDIDATO | 82.571 | 87.364 |
| SOL | 120,74 $ | 7 | RIALZISTA TECNICO | Trend rialzista | Momentum misto | Volatilità in espansione | 0 | 0 / NON ATTIVO | Doppio minimo / TARGET RAGGIUNTO | Triplo massimo / CANDIDATO | 96,23 | 124,62 |
| DOGE | 0.09278 $ | 6 | COSTRUTTIVO MA NON CONFERMATO | Trend rialzista | Momentum debole | Volatilità in espansione | +2 | +1 / TENUTO | Doppio minimo / CONFERMATO RECENTE | Doppio massimo / CANDIDATO | 0.07841 | 0.10528 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo      | Triplo minimo    | Adam/Eve Bottom                          | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-------------------|:-----------------|:-----------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CONFERMATO RECENTE | TARGET RAGGIUNTO | Eve and Adam Bottom — CONFERMATO RECENTE | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 2 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | INVALIDATO | CANDIDATO | ASSENTE | 0 |
| DOGE | CONFERMATO RECENTE | TARGET RAGGIUNTO | Adam and Eve Bottom — CONFERMATO RECENTE | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 2 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 63.97 | -148.739 | 82.446 | 78.560 | 71.426 | 10,00% | 1,09% | 6,49% | 32,58% |
| SOL | 65.05 | -0.3438 | 114,14 | 103,79 | 85,80 | 17,36% | 1,34% | 18,43% | 47,40% |
| DOGE | 53.52 | -0.00047 | 0.09161 | 0.08699 | 0.08777 | 10,63% | -5,82% | 9,39% | 21,15% |

## Dettaglio asset

### BTC

- Prezzo: **84.844 $**
- Punteggio tecnico: **9 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum misto** (0)
- Volume: **Volume neutrale** (0)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 7.494e+04 -> 8.257e+04. Ultimi massimi: 8.226e+04 -> 8.736e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-09-21 87.364; livello più vicino 23.6% a 80.374; stato NON ATTIVO; confluenza: invalidazione rialzista.
- Punteggio pattern: **+2**
  - rialzista dominante: Doppio minimo (CONFERMATO RECENTE, +2); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **82.571**
- Resistenza più vicina: **87.364**

Pattern classici e ciclo di vita:

- Doppio minimo: **CONFERMATO RECENTE** (+2)
  - Due minimi simili vicino a 74.945 tra 2026-09-02 e 2026-09-15. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (13 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 89.580; progresso corrente: 35,28%. Relazione prezzo/neckline: sopra neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (13g); progresso 35,28%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 58.076 dal 2026-06-25 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (46 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 75.744; progresso corrente: 203,01%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 75.744; breakout 2026-08-19 (46g); progresso 203,01%; prezzo sopra neckline.
- Eve and Adam Bottom: **CONFERMATO RECENTE** (+2)
  - Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (13 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 89.580; progresso corrente: 35,28%. Relazione prezzo/neckline: sopra neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (13g); progresso 35,28%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 87.364 tra 2026-09-03 e 2026-09-21. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 74.945; target 62.525; distanza dalla neckline 13,21%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 56 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 46,92%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 87.364 dal 2026-09-03 al 2026-09-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 74.945; target 62.525; distanza dalla neckline 13,21%; prezzo sopra neckline.

### SOL

- Prezzo: **120,74 $**
- Punteggio tecnico: **7 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum misto** (0)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 97.45 -> 96.23. Ultimi massimi: 107.1 -> 124.6.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing UP 2026-08-01 70,69 -> 2026-09-27 124,62; livello più vicino 23.6% a 111,89; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Triplo massimo (CANDIDATO, 0).
- Supporto più vicino: **96,23**
- Resistenza più vicina: **124,62**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 96,23 tra 2026-09-02 e 2026-09-16. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (16 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: 125,09%. Relazione prezzo/neckline: sopra neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (16g); progresso 125,09%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (46 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 523,10%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (46g); progresso 523,10%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 96,23 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (16 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: 125,09%. Relazione prezzo/neckline: sopra neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (16g); progresso 125,09%; prezzo sopra neckline.
- Doppio massimo: **INVALIDATO** (0)
  - Due massimi simili vicino a 110,04 tra 2026-08-27 e 2026-09-06. Neckline ribassista stimata: 97,45. Breakout neckline: 2026-09-15 (19 giorni fa). Stato: INVALIDATO. Target teorico: 84,86; progresso corrente: -185,01%. Relazione prezzo/neckline: sopra neckline.
  - neckline 97,45; target 84,86; breakout 2026-09-15 (19g); progresso -185,01%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 56 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 70,79%; prezzo sopra neckline.
- Adam/Eve Top: **ASSENTE** (0)

### DOGE

- Prezzo: **0.09278 $**
- Punteggio tecnico: **6 / 12**
- Verdetto: **COSTRUTTIVO MA NON CONFERMATO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum debole** (-3)
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
  - Due minimi simili vicino a 0.07841 tra 2026-09-02 e 2026-09-16. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (13 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 0.11001; progresso corrente: -9,04%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.09421; target 0.11001; breakout 2026-09-21 (13g); progresso -9,04%; prezzo sotto neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06835 dal 2026-07-13 al 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (46 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07926; progresso corrente: 347,86%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07926; breakout 2026-08-19 (46g); progresso 347,86%; prezzo sopra neckline.
- Adam and Eve Bottom: **CONFERMATO RECENTE** (+2)
  - Pattern Adam and Eve Bottom vicino a 0.07841 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (13 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 0.11001; progresso corrente: -9,04%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.09421; target 0.11001; breakout 2026-09-21 (13g); progresso -9,04%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.10528 tra 2026-08-22 e 2026-09-22. Neckline ribassista stimata: 0.07841. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 0.07841; target 0.05153; distanza dalla neckline 18,33%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 54 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 36,50%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07380 dal 2026-07-26 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 54 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 36,50%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                       | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                                  |   Score |
|:--------|:----------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-09-21 | 80.374 | 76.050 | 72.556 | 69.061 | 64.086 | 23.6% / 80.374 | NON ATTIVO | invalidazione rialzista | 0 |
| SOL | UP 2026-08-01 -> 2026-09-27 | 111,89 | 104,02 | 97,66 | 91,29 | 82,23 | 23.6% / 111,89 | NON ATTIVO | nessuna confluenza indipendente | 0 |
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

- **BTC**: 34/30 previsioni controllate su 87 fatte. Stato: **ATTIVA**.
- **SOL**: 34/30 previsioni controllate su 87 fatte. Stato: **ATTIVA**.
- **DOGE**: 34/30 previsioni controllate su 87 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 87 | 34 | 30/30 [██████████] | 53 | ATTIVA | 2026-10-05 / tra 1 giorno |
| SOL | 87 | 34 | 30/30 [██████████] | 53 | ATTIVA | 2026-10-05 / tra 1 giorno |
| DOGE | 87 | 34 | 30/30 [██████████] | 53 | ATTIVA | 2026-10-05 / tra 1 giorno |

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

Generato: 2026-10-04 05:33 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 84.844 $          | 84.844 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.09278 $         | 0.09278 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 120,74 $          | 120,74 $        | -0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 84.844 $          | 84.844 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 120,74 $          | 120,74 $        | -0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.09278 $         | 0.09278 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 84.844 $          | 84.844 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 120,74 $          | 120,74 $        | -0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.09278 $         | 0.09278 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 84.844 $          | 84.844 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 120,74 $          | 120,74 $        | -0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.09278 $         | 0.09278 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 84.844 $          | 84.844 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 120,74 $          | 120,74 $        | -0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.09278 $         | 0.09278 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 84.844 $          | 84.802 $        | -0,0494%     |
| Exchange Microstructure | SOL     | price             | OK      | 120,74 $          | 120,76 $        | +0,0191%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.09278 $         | 0.09279 $       | +0,0108%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 120,74 $          | 120,74 $        | -0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 120,74 $          | 120,74 $        | -0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 120,74 $          | 120,74 $        | -0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 120,74 $          | 120,74 $        | -0,0000%     |

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
