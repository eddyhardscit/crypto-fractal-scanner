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

Generato: 2026-10-22 05:34 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | NEUTRALE / COSTRUTTIVO | HOLD / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | +2 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | 0 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+2**, spot = **HOLD / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **+2**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **0**, spot = **STAI ALLA FINESTRA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+2**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MEDIO / ALTO**
- Conferme: Prima resistenza sopra 84.249; conferma del eve and adam bottom sopra 82.262.
- Invalidazioni: Sotto 79.736 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+2**
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
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 3; EMA200 circa 111,29 $; upside verso EMA200 +5,97%. Non autorizza leva e non aggiunge punti automatici.
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

Generato: 2026-10-22 05:34 UTC

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

Segnali totali salvati: **291**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-22 | BTC | 82.752,49 | +2 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-22 | DOGE | 0.07992 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-22 | SOL | 105,09 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-21 | BTC | 82.805,01 | 0 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-21 | DOGE | 0.08166 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-21 | SOL | 105,96 | +3 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-20 | BTC | 81.867,63 | +2 | +1 | +1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-20 | DOGE | 0.07939 | -1 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-20 | SOL | 104,68 | +3 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-19 | BTC | 82.648,77 | -1 | +1 | +1 | 0 | -1 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-19 | DOGE | 0.07945 | -1 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-19 | SOL | 105,63 | -2 | +1 | +1 | 0 | -2 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 97 | 96 | 95 | 94 | 92 | 91 | 88 | 84 | 77 | 70 | 59 | 44 |
| SOL | 97 | 96 | 95 | 94 | 92 | 91 | 88 | 84 | 77 | 70 | 59 | 44 |
| DOGE | 97 | 96 | 95 | 94 | 92 | 91 | 88 | 84 | 77 | 70 | 59 | 44 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-24 | 60g | 2026-10-23 | domani |
| SOL | 2026-08-24 | 60g | 2026-10-23 | domani |
| DOGE | 2026-08-24 | 60g | 2026-10-23 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 85 | 52,94% | +0,31% | +0,29% | UTILE |
| BTC | 2g | 85 | 50,59% | +0,50% | +0,43% | UTILE |
| BTC | 3g | 84 | 46,43% | +0,62% | +0,59% | UTILE |
| BTC | 5g | 82 | 43,90% | +1,31% | +1,19% | UTILE |
| BTC | 7g | 81 | 50,62% | +1,98% | +1,82% | UTILE |
| BTC | 10g | 79 | 55,70% | +2,78% | +2,69% | UTILE |
| BTC | 14g | 78 | 57,69% | +4,05% | +4,00% | UTILE |
| BTC | 21g | 72 | 68,06% | +7,56% | +7,47% | UTILE |
| BTC | 30g | 67 | 94,03% | +11,76% | +11,11% | UTILE |
| BTC | 45g | 56 | 94,64% | +18,84% | +16,48% | PRIMA CALIBRAZIONE |
| BTC | 60g | 41 | 92,68% | +26,48% | +22,82% | PRIMA CALIBRAZIONE |
| SOL | 1g | 87 | 47,13% | +0,19% | +0,09% | UTILE |
| SOL | 2g | 86 | 44,19% | +0,57% | +0,45% | UTILE |
| SOL | 3g | 85 | 48,24% | +0,95% | +0,80% | UTILE |
| SOL | 5g | 83 | 49,40% | +1,68% | +1,62% | UTILE |
| SOL | 7g | 83 | 53,01% | +2,48% | +2,54% | UTILE |
| SOL | 10g | 80 | 53,75% | +3,77% | +3,87% | UTILE |
| SOL | 14g | 76 | 61,84% | +6,03% | +6,51% | UTILE |
| SOL | 21g | 69 | 73,91% | +12,14% | +11,63% | UTILE |
| SOL | 30g | 62 | 82,26% | +19,00% | +15,81% | UTILE |
| SOL | 45g | 52 | 75,00% | +31,17% | +16,37% | PRIMA CALIBRAZIONE |
| SOL | 60g | 37 | 70,27% | +42,66% | +18,98% | PRIMA CALIBRAZIONE |
| DOGE | 1g | 87 | 48,28% | +0,02% | -0,06% | UTILE |
| DOGE | 2g | 87 | 43,68% | +0,16% | -0,12% | UTILE |
| DOGE | 3g | 86 | 40,70% | +0,37% | +0,04% | UTILE |
| DOGE | 5g | 84 | 46,43% | +0,86% | +0,13% | UTILE |
| DOGE | 7g | 83 | 48,19% | +1,26% | +0,38% | UTILE |
| DOGE | 10g | 80 | 43,75% | +1,65% | +0,37% | UTILE |
| DOGE | 14g | 78 | 53,85% | +2,93% | +2,51% | UTILE |
| DOGE | 21g | 73 | 53,42% | +5,80% | +0,49% | UTILE |
| DOGE | 30g | 66 | 66,67% | +10,12% | +4,39% | UTILE |
| DOGE | 45g | 55 | 49,09% | +17,21% | +3,62% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 42 | 45,24% | +22,39% | -0,40% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 85 | 52,94% | +0,31% | +0,29% | -0,27% | +0,81% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 94 | 48,94% | +0,20% | +0,26% | -0,32% | +0,71% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 94 | 48,94% | +0,20% | +0,26% | -0,32% | +0,71% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 89 | 49,44% | +0,22% | +0,07% | -0,27% | +0,75% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,55% | -0,06% | -0,27% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 85 | 50,59% | +0,50% | +0,43% | -0,26% | +1,20% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 93 | 52,69% | +0,45% | +0,53% | -0,27% | +1,13% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 93 | 52,69% | +0,45% | +0,53% | -0,27% | +1,13% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 88 | 47,73% | +0,44% | +0,07% | -0,20% | +1,12% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,85% | -0,13% | -0,05% | +1,59% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 84 | 46,43% | +0,62% | +0,59% | -1,28% | +2,38% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 92 | 51,09% | +0,74% | +0,81% | -1,35% | +2,41% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 92 | 51,09% | +0,74% | +0,81% | -1,35% | +2,41% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 87 | 40,23% | +0,75% | -0,09% | -1,29% | +2,42% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 36 | 36,11% | +1,29% | -0,55% | -1,13% | +3,01% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 82 | 43,90% | +1,31% | +1,19% | -1,96% | +3,71% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 90 | 48,89% | +1,41% | +1,52% | -1,98% | +3,73% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 90 | 48,89% | +1,41% | +1,52% | -1,98% | +3,73% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 85 | 42,35% | +1,28% | -0,62% | -1,94% | +3,66% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 36 | 36,11% | +2,85% | -2,16% | -1,73% | +5,27% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 81 | 50,62% | +1,98% | +1,82% | -2,31% | +4,80% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 89 | 58,43% | +2,05% | +2,22% | -2,34% | +4,76% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 89 | 58,43% | +2,05% | +2,22% | -2,34% | +4,76% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 84 | 42,86% | +2,00% | -0,99% | -2,32% | +4,71% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 36 | 33,33% | +4,03% | -3,63% | -2,13% | +7,10% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 79 | 55,70% | +2,78% | +2,69% | -2,66% | +5,91% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 86 | 67,44% | +2,78% | +3,17% | -2,64% | +5,87% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 86 | 67,44% | +2,78% | +3,17% | -2,64% | +5,87% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 81 | 44,44% | +2,73% | -0,52% | -2,66% | +5,88% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 35 | 37,14% | +4,12% | -4,05% | -2,39% | +7,77% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -1,34% | -1,34% | -4,20% | +1,67% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 78 | 57,69% | +4,05% | +4,00% | -2,93% | +7,82% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 82 | 62,20% | +4,08% | +4,45% | -2,92% | +7,83% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 82 | 62,20% | +4,08% | +4,45% | -2,92% | +7,83% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 77 | 51,95% | +4,10% | +0,96% | -2,95% | +7,94% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 34 | 20,59% | +3,74% | -4,14% | -2,59% | +8,37% | PRIMA CALIBRAZIONE |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,75% | -0,75% | -4,66% | +2,55% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 72 | 68,06% | +7,56% | +7,47% | -2,98% | +11,53% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 76 | 76,32% | +7,36% | +7,57% | -3,00% | +11,40% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 76 | 76,32% | +7,36% | +7,57% | -3,00% | +11,40% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 70 | 51,43% | +7,59% | +1,08% | -3,00% | +11,67% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 29 | 44,83% | +8,60% | -4,88% | -2,40% | +12,46% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 67 | 94,03% | +11,76% | +11,11% | -2,96% | +16,07% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 70 | 91,43% | +11,75% | +11,75% | -2,94% | +16,16% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 70 | 91,43% | +11,75% | +11,75% | -2,94% | +16,16% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 63 | 65,08% | +11,81% | +1,24% | -2,91% | +16,31% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 28 | 57,14% | +12,44% | -2,72% | -2,47% | +17,06% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 83,33% | +4,24% | +4,24% | -5,33% | +7,62% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 56 | 94,64% | +18,84% | +16,48% | -2,90% | +23,86% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 59 | 100,00% | +19,25% | +19,25% | -2,88% | +24,17% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 59 | 100,00% | +19,25% | +19,25% | -2,88% | +24,17% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 54 | 59,26% | +19,09% | -1,25% | -2,73% | +24,06% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,92% | -4,17% | -2,62% | +19,88% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +7,72% | +7,72% | -5,13% | +13,34% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 41 | 92,68% | +26,48% | +22,82% | -2,14% | +32,05% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 44 | 100,00% | +26,41% | +26,41% | -2,16% | +32,08% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 44 | 100,00% | +26,41% | +26,41% | -2,16% | +32,08% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +28,58% | +28,58% | -2,21% | +34,30% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 39 | 43,59% | +26,52% | -6,16% | -1,87% | +32,39% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 12 | 33,33% | +25,16% | -17,87% | -0,54% | +31,35% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +17,26% | +17,26% | -2,41% | +21,34% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 87 | 48,28% | +0,02% | -0,06% | -0,75% | +1,05% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 95 | 57,89% | -0,05% | +0,43% | -0,86% | +0,94% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 95 | 57,89% | -0,05% | +0,43% | -0,86% | +0,94% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 89 | 50,56% | -0,13% | +0,18% | -0,96% | +0,85% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 56 | 41,07% | -0,04% | -0,53% | -0,94% | +0,68% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 13 | 53,85% | +1,93% | +1,69% | +0,19% | +2,94% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 87 | 43,68% | +0,16% | -0,12% | -0,95% | +1,53% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 94 | 57,45% | -0,01% | +0,67% | -1,08% | +1,30% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 94 | 57,45% | -0,01% | +0,67% | -1,08% | +1,30% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 88 | 53,41% | -0,29% | +0,20% | -1,37% | +1,02% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 55 | 43,64% | +0,06% | -0,93% | -1,09% | +1,09% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 41,67% | +2,33% | +2,11% | +0,69% | +4,97% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 86 | 40,70% | +0,37% | +0,04% | -2,60% | +3,55% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 93 | 54,84% | +0,07% | +0,91% | -2,78% | +3,25% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 93 | 54,84% | +0,07% | +0,91% | -2,78% | +3,25% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 87 | 47,13% | -0,49% | +0,05% | -3,01% | +2,65% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 54 | 37,04% | +0,22% | -1,63% | -2,81% | +3,37% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 50,00% | +2,30% | +2,13% | -1,68% | +5,97% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 84 | 46,43% | +0,86% | +0,13% | -3,87% | +5,69% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 91 | 50,55% | +0,47% | +1,20% | -4,13% | +5,36% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 91 | 50,55% | +0,47% | +1,20% | -4,13% | +5,36% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 85 | 54,12% | -0,27% | -0,50% | -4,50% | +4,68% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 52 | 42,31% | +1,01% | -3,47% | -4,21% | +5,92% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 33,33% | +1,94% | +1,81% | -2,90% | +8,39% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 83 | 48,19% | +1,26% | +0,38% | -4,61% | +7,45% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 90 | 55,56% | +0,94% | +1,45% | -4,88% | +7,09% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 90 | 55,56% | +0,94% | +1,45% | -4,88% | +7,09% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 84 | 47,62% | +0,03% | -0,76% | -5,33% | +6,19% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 51 | 35,29% | +1,79% | -4,75% | -4,89% | +7,81% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 80 | 43,75% | +1,65% | +0,37% | -5,49% | +9,35% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 87 | 55,17% | +1,11% | +1,80% | -5,78% | +8,90% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 87 | 55,17% | +1,11% | +1,80% | -5,78% | +8,90% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 81 | 46,91% | -0,11% | -1,61% | -6,31% | +7,56% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 49 | 36,73% | +2,28% | -5,60% | -5,75% | +9,82% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 78 | 53,85% | +2,93% | +2,51% | -6,47% | +12,51% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 83 | 67,47% | +2,25% | +4,23% | -6,64% | +12,01% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 83 | 67,47% | +2,25% | +4,23% | -6,64% | +12,01% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 77 | 44,16% | +0,35% | -2,39% | -7,27% | +9,68% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 45 | 40,00% | +3,78% | -5,34% | -5,99% | +12,56% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 73 | 53,42% | +5,80% | +0,49% | -6,64% | +17,70% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 76 | 61,84% | +6,19% | +5,44% | -6,59% | +17,90% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 76 | 61,84% | +6,19% | +5,44% | -6,59% | +17,90% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 70 | 50,00% | +4,23% | -3,56% | -7,29% | +15,23% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 43 | 41,86% | +5,14% | -7,66% | -6,03% | +15,65% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +4,84% | -0,04% | -5,47% | +18,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 66 | 66,67% | +10,12% | +4,39% | -5,75% | +25,40% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 69 | 69,57% | +10,44% | +6,96% | -5,72% | +25,83% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 69 | 69,57% | +10,44% | +6,96% | -5,72% | +25,83% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 63 | 57,14% | +9,01% | -2,58% | -6,43% | +23,83% | UTILE |
| DOGE | 30g | Classic technical | CALIBRABILE | 41 | 48,78% | +8,28% | -6,60% | -5,70% | +22,87% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 72,73% | +14,01% | +8,26% | -6,83% | +27,95% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 55 | 49,09% | +17,21% | +3,62% | -5,35% | +36,33% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 58 | 67,24% | +17,00% | +7,91% | -5,34% | +36,28% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 58 | 67,24% | +17,00% | +7,91% | -5,34% | +36,28% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 52 | 9,62% | +14,04% | -12,26% | -6,16% | +34,21% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 33 | 3,03% | +19,56% | -21,33% | -5,75% | +37,18% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +18,19% | +8,68% | -5,75% | +33,52% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 42 | 45,24% | +22,39% | -0,40% | -4,04% | +43,48% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 44 | 56,82% | +22,93% | +8,10% | -4,06% | +43,66% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 44 | 56,82% | +22,93% | +8,10% | -4,06% | +43,66% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +24,96% | +11,95% | -3,59% | +45,33% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 37 | 8,11% | +23,07% | -22,17% | -4,85% | +42,31% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 29 | 0,00% | +21,38% | -22,84% | -4,58% | +42,30% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +24,97% | +12,49% | -2,74% | +43,78% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 87 | 47,13% | +0,19% | +0,09% | -0,60% | +1,05% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 90 | 53,33% | +0,15% | +0,40% | -0,71% | +1,00% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 93 | 52,69% | +0,18% | +0,35% | -0,67% | +1,03% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 88 | 46,59% | +0,14% | -0,08% | -0,76% | +0,98% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 59 | 44,07% | +0,51% | -0,09% | -0,48% | +1,43% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 86 | 44,19% | +0,57% | +0,45% | -0,64% | +1,65% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 89 | 50,56% | +0,45% | +0,63% | -0,85% | +1,41% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 92 | 50,00% | +0,45% | +0,59% | -0,82% | +1,45% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 87 | 43,68% | +0,28% | -0,04% | -0,83% | +1,41% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,60% | +0,15% | -0,64% | +1,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 85 | 48,24% | +0,95% | +0,80% | -2,22% | +3,55% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 88 | 51,14% | +0,80% | +1,13% | -2,37% | +3,35% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 91 | 50,55% | +0,79% | +1,09% | -2,33% | +3,35% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 86 | 45,35% | +0,43% | -0,33% | -2,39% | +2,95% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 59 | 45,76% | +0,61% | +0,08% | -2,23% | +3,14% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 83 | 49,40% | +1,68% | +1,62% | -3,30% | +5,51% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 86 | 53,49% | +1,48% | +1,85% | -3,43% | +5,27% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 89 | 52,81% | +1,45% | +1,76% | -3,38% | +5,22% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 84 | 45,24% | +1,11% | -0,76% | -3,48% | +4,75% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,71% | -0,02% | -3,27% | +4,40% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 83 | 53,01% | +2,48% | +2,54% | -3,96% | +6,97% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 85 | 60,00% | +2,27% | +3,02% | -4,07% | +6,77% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 88 | 60,23% | +2,19% | +2,92% | -4,02% | +6,67% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 83 | 40,96% | +1,37% | -1,66% | -4,16% | +5,95% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 59 | 42,37% | +0,39% | -0,27% | -4,06% | +5,04% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 80 | 53,75% | +3,77% | +3,87% | -4,63% | +8,93% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 82 | 67,07% | +3,64% | +5,43% | -4,75% | +8,61% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 85 | 65,88% | +3,50% | +5,25% | -4,70% | +8,44% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 80 | 42,50% | +2,12% | -2,26% | -4,91% | +7,35% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 58 | 43,10% | +0,03% | -0,65% | -5,05% | +5,72% | PRIMA CALIBRAZIONE |

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

Generato: 2026-10-22 05:34 UTC

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
| BTC | 97 | UTILE | 94 | 29 | 18 | 0 | Famiglia statistica | 1g | 48,94% | +0,26% | campione utile, valutare con prudenza |
| SOL | 97 | UTILE | 90 | 32 | 18 | 0 | Famiglia statistica | 1g | 53,33% | +0,40% | campione utile, valutare con prudenza |
| DOGE | 97 | UTILE | 95 | 32 | 18 | 0 | Famiglia statistica | 1g | 57,89% | +0,43% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 36 | 41,67% | -0,06% | +0,55% | -0,27% | +1,09% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 94 | 48,94% | +0,26% | +0,20% | -0,32% | +0,71% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 89 | 49,44% | +0,07% | +0,22% | -0,27% | +0,75% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 36 | 41,67% | -0,13% | +0,85% | -0,05% | +1,59% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 93 | 52,69% | +0,53% | +0,45% | -0,27% | +1,13% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 88 | 47,73% | +0,07% | +0,44% | -0,20% | +1,12% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 36 | 36,11% | -0,55% | +1,29% | -1,13% | +3,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Famiglia statistica | 92 | 51,09% | +0,81% | +0,74% | -1,35% | +2,41% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 87 | 40,23% | -0,09% | +0,75% | -1,29% | +2,42% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 36 | 36,11% | -2,16% | +2,85% | -1,73% | +5,27% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 90 | 48,89% | +1,52% | +1,41% | -1,98% | +3,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 85 | 42,35% | -0,62% | +1,28% | -1,94% | +3,66% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 36 | 33,33% | -3,63% | +4,03% | -2,13% | +7,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 89 | 58,43% | +2,22% | +2,05% | -2,34% | +4,76% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 84 | 42,86% | -0,99% | +2,00% | -2,32% | +4,71% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 35 | 37,14% | -4,05% | +4,12% | -2,39% | +7,77% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 86 | 67,44% | +3,17% | +2,78% | -2,64% | +5,87% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 9 | 33,33% | -1,34% | -1,34% | -4,20% | +1,67% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 81 | 44,44% | -0,52% | +2,73% | -2,66% | +5,88% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 34 | 20,59% | -4,14% | +3,74% | -2,59% | +8,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Famiglia statistica | 82 | 62,20% | +4,45% | +4,08% | -2,92% | +7,83% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 8 | 37,50% | -0,75% | -0,75% | -4,66% | +2,55% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 77 | 51,95% | +0,96% | +4,10% | -2,95% | +7,94% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 29 | 44,83% | -4,88% | +8,60% | -2,40% | +12,46% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 76 | 76,32% | +7,57% | +7,36% | -3,00% | +11,40% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 70 | 51,43% | +1,08% | +7,59% | -3,00% | +11,67% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 28 | 57,14% | -2,72% | +12,44% | -2,47% | +17,06% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 70 | 91,43% | +11,75% | +11,75% | -2,94% | +16,16% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Microstruttura exchange | 6 | 83,33% | +4,24% | +4,24% | -5,33% | +7,62% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 63 | 65,08% | +1,24% | +11,81% | -2,91% | +16,31% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Classic technical | 24 | 66,67% | -4,17% | +13,92% | -2,62% | +19,88% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 59 | 100,00% | +19,25% | +19,25% | -2,88% | +24,17% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +7,72% | +7,72% | -5,13% | +13,34% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 54 | 59,26% | -1,25% | +19,09% | -2,73% | +24,06% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 12 | 33,33% | -17,87% | +25,16% | -0,54% | +31,35% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 44 | 100,00% | +26,41% | +26,41% | -2,16% | +32,08% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +17,26% | +17,26% | -2,41% | +21,34% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 39 | 43,59% | -6,16% | +26,52% | -1,87% | +32,39% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Classic technical | 56 | 41,07% | -0,53% | -0,04% | -0,94% | +0,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 95 | 57,89% | +0,43% | -0,05% | -0,86% | +0,94% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 13 | 53,85% | +1,69% | +1,93% | +0,19% | +2,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 89 | 50,56% | +0,18% | -0,13% | -0,96% | +0,85% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 55 | 43,64% | -0,93% | +0,06% | -1,09% | +1,09% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 94 | 57,45% | +0,67% | -0,01% | -1,08% | +1,30% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 12 | 41,67% | +2,11% | +2,33% | +0,69% | +4,97% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 88 | 53,41% | +0,20% | -0,29% | -1,37% | +1,02% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 54 | 37,04% | -1,63% | +0,22% | -2,81% | +3,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 93 | 54,84% | +0,91% | +0,07% | -2,78% | +3,25% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 12 | 50,00% | +2,13% | +2,30% | -1,68% | +5,97% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 87 | 47,13% | +0,05% | -0,49% | -3,01% | +2,65% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 52 | 42,31% | -3,47% | +1,01% | -4,21% | +5,92% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 91 | 50,55% | +1,20% | +0,47% | -4,13% | +5,36% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 12 | 33,33% | +1,81% | +1,94% | -2,90% | +8,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 85 | 54,12% | -0,50% | -0,27% | -4,50% | +4,68% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 51 | 35,29% | -4,75% | +1,79% | -4,89% | +7,81% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 90 | 55,56% | +1,45% | +0,94% | -4,88% | +7,09% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 11 | 45,45% | +0,78% | +0,88% | -3,00% | +9,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 84 | 47,62% | -0,76% | +0,03% | -5,33% | +6,19% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 49 | 36,73% | -5,60% | +2,28% | -5,75% | +9,82% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 87 | 55,17% | +1,80% | +1,11% | -5,78% | +8,90% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 81 | 46,91% | -1,61% | -0,11% | -6,31% | +7,56% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 45 | 40,00% | -5,34% | +3,78% | -5,99% | +12,56% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 83 | 67,47% | +4,23% | +2,25% | -6,64% | +12,01% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 11 | 45,45% | +2,03% | +5,60% | -4,35% | +14,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 77 | 44,16% | -2,39% | +0,35% | -7,27% | +9,68% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 43 | 41,86% | -7,66% | +5,14% | -6,03% | +15,65% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 76 | 61,84% | +5,44% | +6,19% | -6,59% | +17,90% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 11 | 63,64% | -0,04% | +4,84% | -5,47% | +18,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 70 | 50,00% | -3,56% | +4,23% | -7,29% | +15,23% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Classic technical | 41 | 48,78% | -6,60% | +8,28% | -5,70% | +22,87% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 69 | 69,57% | +6,96% | +10,44% | -5,72% | +25,83% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 11 | 72,73% | +8,26% | +14,01% | -6,83% | +27,95% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 63 | 57,14% | -2,58% | +9,01% | -6,43% | +23,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 45g | MEDIO | Classic technical | 33 | 3,03% | -21,33% | +19,56% | -5,75% | +37,18% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Famiglia statistica | 58 | 67,24% | +7,91% | +17,00% | -5,34% | +36,28% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 9 | 55,56% | +8,68% | +18,19% | -5,75% | +33,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 52 | 9,62% | -12,26% | +14,04% | -6,16% | +34,21% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 29 | 0,00% | -22,84% | +21,38% | -4,58% | +42,30% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 44 | 56,82% | +8,10% | +22,93% | -4,06% | +43,66% | PESO OK | 0,0 | MEDIA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 6 | 66,67% | +12,49% | +24,97% | -2,74% | +43,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 37 | 8,11% | -22,17% | +23,07% | -4,85% | +42,31% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 1g | BREVE | Classic technical | 59 | 44,07% | -0,09% | +0,51% | -0,48% | +1,43% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 90 | 53,33% | +0,40% | +0,15% | -0,71% | +1,00% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 88 | 46,59% | -0,08% | +0,14% | -0,76% | +0,98% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 59 | 47,46% | +0,15% | +0,60% | -0,64% | +1,71% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 89 | 50,56% | +0,63% | +0,45% | -0,85% | +1,41% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 87 | 43,68% | -0,04% | +0,28% | -0,83% | +1,41% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 59 | 45,76% | +0,08% | +0,61% | -2,23% | +3,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 88 | 51,14% | +1,13% | +0,80% | -2,37% | +3,35% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 86 | 45,35% | -0,33% | +0,43% | -2,39% | +2,95% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 59 | 47,46% | -0,02% | +0,71% | -3,27% | +4,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 86 | 53,49% | +1,85% | +1,48% | -3,43% | +5,27% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 84 | 45,24% | -0,76% | +1,11% | -3,48% | +4,75% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 59 | 42,37% | -0,27% | +0,39% | -4,06% | +5,04% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 85 | 60,00% | +3,02% | +2,27% | -4,07% | +6,77% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 83 | 40,96% | -1,66% | +1,37% | -4,16% | +5,95% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 58 | 43,10% | -0,65% | +0,03% | -5,05% | +5,72% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 82 | 67,07% | +5,43% | +3,64% | -4,75% | +8,61% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 80 | 42,50% | -2,26% | +2,12% | -4,91% | +7,35% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 57 | 40,35% | -0,90% | +0,64% | -6,17% | +7,09% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 78 | 79,49% | +8,98% | +6,14% | -5,31% | +12,13% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 76 | 36,84% | -3,67% | +3,84% | -5,64% | +10,17% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 51 | 52,94% | -2,36% | +7,49% | -6,11% | +14,15% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 71 | 83,10% | +14,32% | +12,56% | -5,14% | +19,03% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 69 | 47,83% | -5,68% | +9,87% | -5,66% | +16,58% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Classic technical | 44 | 52,27% | -4,39% | +21,12% | -4,75% | +27,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 65 | 89,23% | +18,25% | +20,63% | -4,36% | +28,42% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 62 | 43,55% | -7,64% | +19,66% | -4,78% | +26,37% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 45g | MEDIO | Classic technical | 40 | 42,50% | -15,16% | +25,59% | -4,57% | +37,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 45g | MEDIO | Famiglia statistica | 54 | 75,93% | +19,32% | +31,43% | -4,25% | +41,56% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +28,91% | +28,91% | -3,55% | +37,55% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 56 | 37,50% | -19,58% | +30,54% | -4,62% | +40,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 25 | 16,00% | -42,43% | +47,84% | -3,75% | +56,65% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 39 | 71,79% | +29,82% | +46,02% | -3,60% | +57,58% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 3 | 100,00% | +37,00% | +37,00% | -3,34% | +49,68% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 41 | 19,51% | -34,83% | +44,74% | -4,14% | +55,78% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 87 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 95 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 108 | 39,81% | -0,25% |
| BTC | BREVE | Famiglia statistica | 279 | 50,90% | +0,53% |
| BTC | BREVE | Microstruttura exchange | 27 | 37,04% | -0,30% |
| BTC | BREVE | Tecnico | 264 | 45,83% | +0,02% |
| BTC | SETTIMANALE | Classic technical | 107 | 35,51% | -3,27% |
| BTC | SETTIMANALE | Famiglia statistica | 265 | 58,11% | +2,29% |
| BTC | SETTIMANALE | Microstruttura exchange | 27 | 22,22% | -1,65% |
| BTC | SETTIMANALE | Tecnico | 250 | 43,20% | -0,71% |
| BTC | SWING | Classic technical | 63 | 31,75% | -4,48% |
| BTC | SWING | Famiglia statistica | 158 | 68,99% | +5,95% |
| BTC | SWING | Microstruttura exchange | 15 | 46,67% | -0,24% |
| BTC | SWING | Tecnico | 147 | 51,70% | +1,02% |
| BTC | MEDIO | Classic technical | 64 | 56,25% | -6,10% |
| BTC | MEDIO | Famiglia statistica | 173 | 96,53% | +18,04% |
| BTC | MEDIO | Microstruttura exchange | 13 | 92,31% | +7,58% |
| BTC | MEDIO | Tecnico | 156 | 57,69% | -1,47% |
| DOGE | BREVE | Classic technical | 165 | 40,61% | -1,02% |
| DOGE | BREVE | Famiglia statistica | 282 | 56,74% | +0,67% |
| DOGE | BREVE | Microstruttura exchange | 37 | 48,65% | +1,97% |
| DOGE | BREVE | Tecnico | 264 | 50,38% | +0,14% |
| DOGE | SETTIMANALE | Classic technical | 152 | 38,16% | -4,59% |
| DOGE | SETTIMANALE | Famiglia statistica | 268 | 53,73% | +1,48% |
| DOGE | SETTIMANALE | Microstruttura exchange | 34 | 44,12% | +1,11% |
| DOGE | SETTIMANALE | Tecnico | 250 | 49,60% | -0,95% |
| DOGE | SWING | Classic technical | 88 | 40,91% | -6,48% |
| DOGE | SWING | Famiglia statistica | 159 | 64,78% | +4,81% |
| DOGE | SWING | Microstruttura exchange | 22 | 54,55% | +0,99% |
| DOGE | SWING | Tecnico | 147 | 46,94% | -2,94% |
| DOGE | MEDIO | Classic technical | 103 | 20,39% | -15,89% |
| DOGE | MEDIO | Famiglia statistica | 171 | 65,50% | +7,58% |
| DOGE | MEDIO | Microstruttura exchange | 26 | 65,38% | +9,38% |
| DOGE | MEDIO | Tecnico | 152 | 28,95% | -10,66% |
| SOL | BREVE | Classic technical | 177 | 45,76% | +0,05% |
| SOL | BREVE | Famiglia statistica | 267 | 51,69% | +0,72% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 261 | 45,21% | -0,15% |
| SOL | SETTIMANALE | Classic technical | 176 | 44,32% | -0,31% |
| SOL | SETTIMANALE | Famiglia statistica | 253 | 60,08% | +3,40% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 247 | 42,91% | -1,54% |
| SOL | SWING | Classic technical | 108 | 46,30% | -1,59% |
| SOL | SWING | Famiglia statistica | 149 | 81,21% | +11,52% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 145 | 42,07% | -4,63% |
| SOL | MEDIO | Classic technical | 109 | 40,37% | -17,07% |
| SOL | MEDIO | Famiglia statistica | 158 | 80,38% | +21,47% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 13 | 100,00% | +28,02% |
| SOL | MEDIO | Tecnico | 159 | 35,22% | -18,86% |

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

Generato: 2026-10-22 05:34 UTC

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
| BTC | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD / ATTESA CONFERME | Prima resistenza sopra 84.249; conferma del eve and adam bottom sopra 82.262. | Sotto 79.736 il quadro tecnico peggiora. |
| SOL | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | conferma del doppio minimo sopra 107,12; nuova conferma tecnica sopra 123,48. | Allarmi sotto 96,23. |
| DOGE | 0 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.10528 migliora; sopra 0.07997 viene invalidato il pattern ribassista dominante. | Sotto 0.07841 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | 0 | +2 | 0 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +2 |
| SOL | +3 | 0 | +3 | 0 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +2 |
| DOGE | +3 | 0 | +3 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD / ATTESA CONFERME**

BTC è in fase mista. Non è abbastanza debole da autorizzare short semplici, ma non ha ancora una conferma piena.

Dettaglio moduli:

- Famiglia statistica: **+2** — Scanner grezzo +2, Market Regime grezzo 0, match regime 2. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+2** — Casi positivi 62,50%, return centrale 30g +5,13%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 2, positivi 30g 100,00%, return p50 +20,73%.
- Scanner path: **0** — Controlli disponibili 95. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-1** — Score tecnico -1/12, verdetto neutrale / misto, trend rialzista, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff possibile distribuzione, pattern score +1 (rialzista Eve and Adam Bottom / MATURO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 0/12, verdetto NEUTRALE / MISTO, stage STAGE 2 / MARKUP, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff DISTRIBUZIONE POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Fractal path: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- RSI top-cycle: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.50; exchange 3/3, copertura 100%, consenso bull 0, bear 2, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — BTC: cambiamento forte in miglioramento rispetto a ieri.

Conferme: Prima resistenza sopra 84.249; conferma del eve and adam bottom sopra 82.262.

Invalidazioni: Sotto 79.736 il quadro tecnico peggiora.

### SOL

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**

SOL è ancora in zona mista. Il frattale resta soltanto uno scenario contestuale: non è confermato dal prezzo e vale 0 punti operativi finché il gap non rientra. Meglio evitare leva e ragionare solo a tranche piccole.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 4. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 72,50%, return centrale 30g +6,00%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 4, positivi 30g 50,00%, return p50 +4,04%.
- Scanner path: **0** — Controlli disponibili 95. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-1** — Score tecnico -1/12, verdetto neutrale / misto, trend misto, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff possibile distribuzione, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Triplo massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 3/12, verdetto ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO, stage STAGE 2 / MARKUP, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff RANGE / FASE NON CHIARA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Fractal path: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- RSI top-cycle: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 3, bias SQUEEZE SETUP MODERATO, EMA200 111,29 $, upside EMA200 +5,97%, gap EMA50/EMA200 -4,45%, hit EMA200 12w +76,67%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow -0.25, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 0, bear 0, divergenze 2, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Leva alta, direzione mista, forza 3/5.
- Daily change: **0** — SOL: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: conferma del doppio minimo sopra 107,12; nuova conferma tecnica sopra 123,48.

Invalidazioni: Allarmi sotto 96,23.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **0**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 80,00%, return centrale 30g +9,60%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 95. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -5/12, verdetto debole, trend ribassista, struttura volatilità in espansione, divergenza nessuna, Wyckoff range / fase non chiara, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -10/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Fractal path: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- RSI top-cycle: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +2.00, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Leva alta, direzione mista, forza 3/5.
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

Generato: 2026-10-22 05:34 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 82.752 $ | prezzo corrente |
| Power Law centrale | 127.049 $ | deviazione -34,87% |
| Banda p10-p90 | 79.522 $ / 321.824 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 14,12% | posizione storica nel corridoio |
| Esponente β | 5,7788 | R² log-log 91,95% |
| Stabilità β | BASSA | range 1,3152 cambiando finestra |
| Ultimo halving | 2024-04-19 | 916 giorni fa |
| Fase ciclo | 62,70% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-10-22 (4418 osservazioni)
- Formula stimata: prezzo ≈ exp(-38.8569) × giorni^5.7788
- Prezzo centrale oggi: **127.049 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 14,12%
- Scarto dal centro: **-34,87%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,7788 | 91,95% |
| 2015 | 5,8579 | 91,49% |
| 2016 | 5,5392 | 87,78% |
| 2017 | 4,8168 | 83,10% |
| 2018 | 4,5427 | 78,71% |

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
| 2012-11-28 → 2016-07-09 | 2015-03-05 | -8,14% | -18,21% | -17,40% | +48,79% |
| 2016-07-09 → 2020-05-11 | 2018-12-05 | +2,76% | +3,79% | +118,67% | +98,41% |
| 2020-05-11 → 2024-04-19 | 2022-10-30 | -20,31% | +11,61% | +42,18% | +67,20% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | 2 | 0 | -7.272060321988993 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -7 | -1 | -16.047136858930955 | 0 |

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

Generato: 2026-10-22 05:34 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00127130 | +2 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | -7,27% | MISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000097 | -7 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -16,05% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

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
- **Rendimenti relativi:** 7g -0,37%; 30g -7,27%; 90g +9,03%; 180g +14,22%
- **Daily:** RSI 34.75; MA50 0.00133999; MA200 0.00120382
- **Weekly:** MA30 0.00120734; RSI 49.77
- **Livelli:** supporto 0.00117400; resistenza 0.00129400; breakout 60g 0.00146600; breakdown 60g 0.00117400
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00133900; target 0.00140150
- **Fibonacci:** VICINO — 38.2% a 0.00129143
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in salita; struttura con massimi/minimi crescenti; RSI relativo debole; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-7)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g -3,58%; 30g -16,05%; 90g -9,14%; 180g -24,03%
- **Daily:** RSI 32.08; MA50 0.00000108; MA200 0.00000120
- **Weekly:** MA30 0.00000120; RSI 34.29
- **Livelli:** supporto 0.00000093; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000093
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000106
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; RSI relativo debole; MACD relativo negativo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 212 | 52,36% | +1,92% | -1,06% |
| SOL | 30g | 210 | 47,62% | +4,51% | +0,58% |
| SOL | 90g | 202 | 52,97% | +9,80% | +3,12% |
| DOGE | 7g | 297 | 55,56% | +1,81% | -1,68% |
| DOGE | 30g | 296 | 53,04% | +1,98% | -3,49% |
| DOGE | 90g | 292 | 54,79% | +6,93% | -9,18% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 52 | 48,08% | -0,01% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 52 | 44,23% | +0,06% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 52 | 36,54% | -0,67% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 51 | 35,29% | -1,79% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 36 | 55,56% | -0,39% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 70 | 67,14% | +0,20% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 68 | 64,71% | +0,49% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 65 | 61,54% | +0,42% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 58 | 53,45% | +0,11% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 54 | 57,41% | +0,39% | LOCKED / RACCOLTA LIVE | 0 |

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
| Confronto precedente | 2026-10-19 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 105,19 $ |
| EMA200 weekly target | 111,29 $ |
| Upside verso EMA200 | +5,97% |
| Distanza prezzo da EMA200 | -5,63% |
| Gap EMA50/EMA200 | -4,45% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 53,95 |
| Età SOL | 6,5 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +76,67% |
| Max gain mediano 12w | +24,46% |
| Drawdown mediano 12w | -37,49% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-10-22 05:33 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-10-22 05:30:22 UTC**

Questo report confronta il grafico attuale di Bitcoin, Solana e Dogecoin con tanti grafici storici di altre crypto.

Non è una previsione certa. È uno scanner statistico: guarda situazioni simili già successe e mostra cosa accadde dopo nei 30 giorni successivi.

<!-- COMPACT_SECTION_START:daily_change -->
<details open>
<summary><strong>🗓️ Cambiamenti rispetto a ieri</strong></summary>

<!-- DAILY_CHANGE_START -->

---

# Mini report cambiamenti da ieri

Report separato completo: [daily_change_report.md](daily_change_report.md)

- BTC: cambiamento importante in miglioramento rispetto a ieri.
- SOL: nessun cambiamento forte rispetto a ieri.
- DOGE: nessun cambiamento forte rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +62.50% | +5.00 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | peggioramento | RIALZISTA | +72.50% | +2.50 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | peggioramento | RIALZISTA | +80.00% | -2.50 punti |

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
| BTC | 78.695 $ | 91.121 $ | +37,93% | +15,79% | rimbalzo debole | 91.121 $ | 78.695 $ | +15,38% | -13,64% | spike storicamente più resistente |
| SOL | 99,93 $ | 115,71 $ | +44,44% | +15,79% | rimbalzo debole | 115,71 $ | 99,93 $ | +7,69% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07608 $ | 0,08809 $ | +50,00% | +15,79% | rimbalzo possibile | 0,08809 $ | 0,07608 $ | +6,90% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +37,93% (11/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 4 poi sono scaricati a -5,00%. Percentuale: +15,38% (4/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 27 prima sono scesi a -5,00%. Tra quei 27, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +44,44% (12/27). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **SOL: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 2 poi sono scaricati a -5,00%. Percentuale: +7,69% (2/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 24 prima sono scesi a -5,00%. Tra quei 24, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +50,00% (12/24). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **DOGE: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 2 poi sono scaricati a -5,00%. Percentuale: +6,90% (2/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-10-22 05:33:01 UTC

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-10-22 | 2026-10-22T05:30:21Z | 2026-10-22 05:30:22 |
| SOL | 2026-10-22 | 2026-10-22T05:30:21Z | 2026-10-22 05:30:22 |
| DOGE | 2026-10-22 | 2026-10-22T05:30:21Z | 2026-10-22 05:30:22 |

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
| BTC | 2026-10-22 | 82.837 $ | SALITA | 62,50% | 65.933,25 $ | 70.518,59 $ | 87.089,03 $ | 101.203,12 $ | 105.859,81 $ |
| SOL | 2026-10-22 | 105,19 $ | SALITA | 72,50% | 81,50 $ | 104,27 $ | 111,50 $ | 122,11 $ | 135,91 $ |
| DOGE | 2026-10-22 | 0.08008 $ | SALITA | 80,00% | 0.07039 $ | 0.08084 $ | 0.08777 $ | 0.09783 $ | 0.11196 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | AVAILABLE | SAME_BTC_REGIME | 2 | 2 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 87.089,03 $ | 83.566,29 $ | 105.859,81 $ | 105.522,01 $ |
| SOL | AVAILABLE | SAME_BTC_REGIME | 4 | 4 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 111,50 $ | 106,12 $ | 135,91 $ | 148,42 $ |
| DOGE | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 1 | 3 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 0.08777 $ | n/a | 0.11196 $ | n/a |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-09-22**; verificato fino al **2026-10-22**; stato **COMPLETO 30/30g**.
- Reale **82.749,18 $**; p50 previsto **96.162,99 $**; scarto **-13,95%**.
- Errore medio assoluto **9,90%**; massimo **19,64%**; DENTRO p10-p90; DENTRO p25-p75.

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

**Campione corrente:** 12 episodi qualificati su 40 · 11 asset distinti.

![SOL conditional successor corrente](scanner_forecast_SOL_conditional_successor_current.png)

###### Confronto diretto a 30 giorni

| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Cono standard | 2026-10-22 | 40 | 2026-11-21 | 81.50 $ | 104.27 $ | 111.50 $ | 122.11 $ | 135.91 $ |
| Conditional corrente | 2026-10-22 | 12 | 2026-11-21 | 76.59 $ | 88.27 $ | 98.37 $ | 116.31 $ | 201.21 $ |

###### Struttura successiva dei casi correnti

| Classe | Episodi | Frequenza empirica |
| --- | ---: | ---: |
| DIRECT_CONTINUATION | 4 | 33.33% |
| SHALLOW_PULLBACK_THEN_CONTINUATION | 0 | 0.00% |
| DEEP_PULLBACK_THEN_RECOVERY | 0 | 0.00% |
| FAILURE | 8 | 66.67% |
| UNRESOLVED | 0 | 0.00% |

###### Episodi qualificati oggi

| Asset | Match window | -5% hit | +10% anchor | Classe 60d |
| --- | --- | --- | --- | --- |
| MKR-USD | 2020-11-28 → 2021-03-07 | 2021-03-14 | 2021-04-02 | FAILURE |
| ZEC-USD | 2024-06-04 → 2024-09-11 | 2024-09-30 | 2024-10-10 | DIRECT_CONTINUATION |
| MKR-USD | 2019-01-13 → 2019-04-22 | 2019-04-24 | 2019-05-15 | FAILURE |
| ENJ-USD | 2022-12-07 → 2023-03-16 | 2023-03-27 | 2023-04-07 | FAILURE |
| DOGE-USD | 2024-01-21 → 2024-04-29 | 2024-04-30 | 2024-05-04 | FAILURE |
| TRX-USD | 2021-06-30 → 2021-10-07 | 2021-10-27 | 2021-11-02 | DIRECT_CONTINUATION |
| HBAR-USD | 2022-12-09 → 2023-03-18 | 2023-03-27 | 2023-03-29 | FAILURE |
| DASH-USD | 2019-12-03 → 2020-03-11 | 2020-03-12 | 2020-04-09 | FAILURE |
| ICP-USD | 2022-12-10 → 2023-03-19 | 2023-03-20 | 2023-04-16 | DIRECT_CONTINUATION |
| RUNE-USD | 2023-07-06 → 2023-10-13 | 2023-10-17 | 2023-10-22 | DIRECT_CONTINUATION |
| 1INCH-USD | 2022-12-09 → 2023-03-18 | 2023-03-27 | 2023-04-16 | FAILURE |
| FIL-USD | 2022-12-11 → 2023-03-20 | 2023-03-25 | 2023-04-15 | FAILURE |

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

- Ultimo close disponibile: **2026-10-18** · SOL **104.02 $**.
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

- Cono congelato il **2026-09-22**; verificato fino al **2026-10-22**; stato **COMPLETO 30/30g**.
- Reale **105,06 $**; p50 previsto **121,93 $**; scarto **-13,84%**.
- Errore medio assoluto **5,39%**; massimo **15,74%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted SOL](scanner_forecast_SOL_regime_adjusted.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-09-22**; verificato fino al **2026-10-22**; stato **COMPLETO 30/30g**.
- Reale **0.07986 $**; p50 previsto **0.09029 $**; scarto **-11,55%**.
- Errore medio assoluto **6,57%**; massimo **14,02%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 95 | 94,74% | 72,63% | 1,81% | 0,25% |
| BTC | 3g | 91 | 94,51% | 80,22% | 2,95% | 0,53% |
| BTC | 7g | 84 | 94,05% | 73,81% | 4,66% | 0,88% |
| BTC | 14g | 70 | 98,57% | 78,57% | 5,81% | 0,13% |
| BTC | 30g | 41 | 100,00% | 68,29% | 12,09% | -4,91% |
| SOL | 1g | 95 | 86,32% | 64,21% | 2,60% | 0,45% |
| SOL | 3g | 91 | 92,31% | 73,63% | 3,76% | 1,11% |
| SOL | 7g | 84 | 92,86% | 72,62% | 5,85% | 1,70% |
| SOL | 14g | 70 | 90,00% | 72,86% | 8,38% | 3,41% |
| SOL | 30g | 41 | 95,12% | 70,73% | 14,88% | 3,87% |
| DOGE | 1g | 95 | 89,47% | 61,05% | 2,97% | 0,11% |
| DOGE | 3g | 91 | 92,31% | 62,64% | 4,60% | 0,69% |
| DOGE | 7g | 84 | 77,38% | 70,24% | 8,45% | 3,24% |
| DOGE | 14g | 70 | 87,14% | 51,43% | 10,43% | 6,04% |
| DOGE | 30g | 41 | 95,12% | 41,46% | 16,20% | 15,68% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |

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
- Casi positivi / salita storica: **62,50%**
- Casi negativi / discesa storica: **37,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **82.837,29 $**
- Return normale fra 30 giorni: **87.089,03 $** (5,13%)
- Drawdown normale durante il mese: **74.680,60 $** (-9,85%)
- Drawdown brutto da rispettare: **67.745,15 $** (-18,22%)
- Max gain normale durante il mese: **93.395,68 $** (12,75%)
- Max gain buono / take profit ottimistico: **101.471,36 $** (22,49%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **72,50%**
- Casi negativi / discesa storica: **27,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **105,19 $**
- Return normale fra 30 giorni: **111,50 $** (6,00%)
- Drawdown normale durante il mese: **95,94 $** (-8,79%)
- Drawdown brutto da rispettare: **84,91 $** (-19,28%)
- Max gain normale durante il mese: **118,60 $** (12,75%)
- Max gain buono / take profit ottimistico: **128,51 $** (22,17%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **80,00%**
- Casi negativi / discesa storica: **20,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,08 $**
- Return normale fra 30 giorni: **0,09 $** (9,60%)
- Drawdown normale durante il mese: **0,08 $** (-6,21%)
- Drawdown brutto da rispettare: **0,07 $** (-13,15%)
- Max gain normale durante il mese: **0,09 $** (16,09%)
- Max gain buono / take profit ottimistico: **0,10 $** (23,31%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 82.837,29 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **62,50%**
- Probabilità storica di discesa: **37,50%**
- Quanto è netto il segnale: **medio**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale medio. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **65.933,25 $** (-20,41%)
- Se va male: **70.518,59 $** (-14,87%)
- Scenario normale: **87.089,03 $** (5,13%)
- Se va bene: **101.203,12 $** (22,17%)
- Se va molto bene: **105.859,81 $** (27,79%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **74.680,60 $** (-9,85%)
- Discesa brutta: **67.745,15 $** (-18,22%)
- Discesa molto brutta: **61.611,28 $** (-25,62%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **93.395,68 $** (12,75%)
- Rialzo buono: **101.471,36 $** (22,49%)
- Rialzo molto forte: **107.887,13 $** (30,24%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **74.680,60 $** e uno spike normale intorno a **93.395,68 $**.

La chiusura a 30 giorni era più spesso positiva: salita 62,50%, discesa 37,50%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 105,19 $

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

- Se va molto male: **81,50 $** (-22,52%)
- Se va male: **104,27 $** (-0,88%)
- Scenario normale: **111,50 $** (6,00%)
- Se va bene: **122,11 $** (16,08%)
- Se va molto bene: **135,91 $** (29,21%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **95,94 $** (-8,79%)
- Discesa brutta: **84,91 $** (-19,28%)
- Discesa molto brutta: **68,99 $** (-34,41%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **118,60 $** (12,75%)
- Rialzo buono: **128,51 $** (22,17%)
- Rialzo molto forte: **154,08 $** (46,48%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **95,94 $** e uno spike normale intorno a **118,60 $**.

La chiusura a 30 giorni era più spesso positiva: salita 72,50%, discesa 27,50%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 0,08 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **80,00%**
- Probabilità storica di discesa: **20,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,07 $** (-12,10%)
- Se va male: **0,08 $** (0,95%)
- Scenario normale: **0,09 $** (9,60%)
- Se va bene: **0,10 $** (22,17%)
- Se va molto bene: **0,11 $** (39,81%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,08 $** (-6,21%)
- Discesa brutta: **0,07 $** (-13,15%)
- Discesa molto brutta: **0,06 $** (-26,43%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,09 $** (16,09%)
- Rialzo buono: **0,10 $** (23,31%)
- Rialzo molto forte: **0,13 $** (59,30%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,08 $** e uno spike normale intorno a **0,09 $**.

La chiusura a 30 giorni era più spesso positiva: salita 80,00%, discesa 20,00%. Quindi la lettura principale è favorevole.

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

- Previsioni già controllate: **48**
- Direzione corretta: **90,24%**
- Errore medio dello scenario centrale: **10,56%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **2,08%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **48**
- Direzione corretta: **73,81%**
- Errore medio dello scenario centrale: **15,04%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **29,17%**
- Prezzo finale dentro lo scenario 10%-90%: **95,83%**

### Solana

- Previsioni già controllate: **48**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **12,99%**
- Zona rischio toccata: **4,17%**
- Zona rialzo media toccata: **22,92%**
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

- Previsioni controllate: **48**
- Previsioni usate per la calibrazione recente: **48**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **90,24%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **INCERTO**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **5,13%** → **87.089,03 $**
- Correzione imparata dagli errori: **-4,44%**
- Calibrato: **0,69%** → **83.408,98 $**
- Lettura: Lo scanner è stato troppo ottimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-9,85%** → **74.680,60 $**
- Correzione imparata dagli errori: **4,56%**
- Calibrato: **-5,29%** → **78.457,53 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **12,75%** → **93.395,68 $**
- Correzione imparata dagli errori: **-9,11%**
- Calibrato: **3,64%** → **85.852,38 $**
- Lettura: Lo scanner ha sovrastimato gli spike: nella realtà il prezzo è salito meno del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Solana

- Previsioni controllate: **48**
- Previsioni usate per la calibrazione recente: **48**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **100,00%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **6,00%** → **111,50 $**
- Correzione imparata dagli errori: **1,68%**
- Calibrato: **7,69%** → **113,28 $**
- Lettura: Lo scanner è stato abbastanza centrato sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-8,79%** → **95,94 $**
- Correzione imparata dagli errori: **3,51%**
- Calibrato: **-5,28%** → **99,63 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **12,75%** → **118,60 $**
- Correzione imparata dagli errori: **-2,48%**
- Calibrato: **10,27%** → **115,99 $**
- Lettura: Lo scanner ha sovrastimato gli spike: nella realtà il prezzo è salito meno del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Dogecoin

- Previsioni controllate: **48**
- Previsioni usate per la calibrazione recente: **48**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **73,81%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **9,60%** → **0,09 $**
- Correzione imparata dagli errori: **14,61%**
- Calibrato: **24,21%** → **0,10 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-6,21%** → **0,08 $**
- Correzione imparata dagli errori: **13,73%**
- Calibrato: **7,52%** → **0,09 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **16,09%** → **0,09 $**
- Correzione imparata dagli errori: **3,20%**
- Calibrato: **19,30%** → **0,10 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 82.837,29 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **62,50%**
- Casi negativi dopo 30 giorni: **37,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,56%**
- Rendimento medio dopo 30 giorni: **11,91%**
- Rendimento centrale dopo 30 giorni: **5,13%**
- Discesa media durante i 30 giorni: **-11,96%**
- Massimo rialzo medio durante i 30 giorni: **22,46%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **92.707,29 $**
- Scenario centrale a 30 giorni: **87.089,03 $**
- Zona di rischio media: **72.933,95 $**
- Zona di rialzo media: **101.440,08 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -20,41% → **65.933,25 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -14,87% → **70.518,59 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 5,13% → **87.089,03 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 22,17% → **101.203,12 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 27,79% → **105.859,81 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -25,62% → **61.611,28 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -18,22% → **67.745,15 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -9,85% → **74.680,60 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -3,30% → **80.104,67 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,20% → **82.670,15 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 2,45% → **84.866,74 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 3,71% → **85.909,22 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 12,75% → **93.395,68 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 22,49% → **101.471,36 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 30,24% → **107.887,13 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| RUNE-USD        | 2023-07-06   | 2023-10-13 |        89.13 |       209.44 |          -8.28 |         209.44 |
| QTUM-USD        | 2023-09-18   | 2023-12-26 |        88.4  |       -16.6  |         -16.6  |          10.61 |
| BTC-USD         | 2022-12-09   | 2023-03-18 |        88.32 |         9.19 |           0    |          13.05 |
| ADA-USD         | 2025-06-04   | 2025-09-11 |        88.25 |       -29.3  |         -29.3  |           3.99 |
| AVAX-USD        | 2021-07-11   | 2021-10-18 |        88.05 |        94.33 |           0    |          94.33 |
| LRC-USD         | 2020-11-27   | 2021-03-06 |        87.86 |         0.88 |         -22.65 |           7.79 |
| ETH-USD         | 2025-06-04   | 2025-09-11 |        87.17 |       -15.93 |         -15.93 |           5.69 |
| ETH-USD         | 2022-12-07   | 2023-03-16 |        86.97 |        24.76 |           0    |          25.31 |
| MKR-USD         | 2020-11-28   | 2021-03-07 |        86.89 |         2.85 |         -18.16 |          11.3  |
| BTC-USD         | 2020-03-24   | 2020-07-01 |        86.66 |        22.7  |          -1.67 |          22.7  |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 105,19 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **72,50%**
- Casi negativi dopo 30 giorni: **27,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **88,19%**
- Rendimento medio dopo 30 giorni: **12,53%**
- Rendimento centrale dopo 30 giorni: **6,00%**
- Discesa media durante i 30 giorni: **-13,67%**
- Massimo rialzo medio durante i 30 giorni: **22,82%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **118,37 $**
- Scenario centrale a 30 giorni: **111,50 $**
- Zona di rischio media: **90,81 $**
- Zona di rialzo media: **129,19 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -22,52% → **81,50 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -0,88% → **104,27 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 6,00% → **111,50 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 16,08% → **122,11 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 29,21% → **135,91 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -34,41% → **68,99 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -19,28% → **84,91 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -8,79% → **95,94 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,02% → **100,97 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,20% → **104,98 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 2,10% → **107,40 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 6,15% → **111,66 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 12,75% → **118,60 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 22,17% → **128,51 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 46,48% → **154,08 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| AVAX-USD        | 2021-07-11   | 2021-10-18 |        91.67 |        94.33 |           0    |          94.33 |
| MKR-USD         | 2020-11-28   | 2021-03-07 |        90.75 |         2.85 |         -18.16 |          11.3  |
| ZEC-USD         | 2024-06-04   | 2024-09-11 |        90.55 |        22.09 |         -13.47 |          22.09 |
| ETH-USD         | 2025-06-04   | 2025-09-11 |        89.74 |       -15.93 |         -15.93 |           5.69 |
| MKR-USD         | 2019-01-13   | 2019-04-22 |        89.73 |         8.61 |         -17.54 |          18.4  |
| XTZ-USD         | 2019-09-29   | 2020-01-06 |        89.49 |        64.01 |          -1.99 |          64.01 |
| MKR-USD         | 2023-05-22   | 2023-08-29 |        89.48 |        44.53 |          -0.31 |          44.53 |
| VET-USD         | 2022-12-09   | 2023-03-18 |        89.42 |        10.59 |          -4.34 |          13.84 |
| CRV-USD         | 2022-12-06   | 2023-03-15 |        89.32 |        22.43 |          -0.22 |          22.43 |
| ETH-USD         | 2021-06-25   | 2021-10-02 |        89.29 |        27.51 |          -0.34 |          30.16 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 0,08 $

Dogecoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **80,00%**
- Casi negativi dopo 30 giorni: **20,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **83,50%**
- Rendimento medio dopo 30 giorni: **12,41%**
- Rendimento centrale dopo 30 giorni: **9,60%**
- Discesa media durante i 30 giorni: **-10,26%**
- Massimo rialzo medio durante i 30 giorni: **21,50%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,09 $**
- Scenario centrale a 30 giorni: **0,09 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,10 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -12,10% → **0,07 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 0,95% → **0,08 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 9,60% → **0,09 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 22,17% → **0,10 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 39,81% → **0,11 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -26,43% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -13,15% → **0,07 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -6,21% → **0,08 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -2,06% → **0,08 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **0,08 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 3,61% → **0,08 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 7,88% → **0,09 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 16,09% → **0,09 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 23,31% → **0,10 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 59,30% → **0,13 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| LINK-USD        | 2019-08-30   | 2019-12-07 |        88.02 |        -6    |         -15.53 |          10.16 |
| KSM-USD         | 2022-12-10   | 2023-03-19 |        87.78 |         1.71 |         -13.05 |           2.71 |
| ZEC-USD         | 2024-06-04   | 2024-09-11 |        86.81 |        22.09 |         -13.47 |          22.09 |
| LINK-USD        | 2021-06-25   | 2021-10-02 |        85.53 |        17.14 |          -8.62 |          20.62 |
| ICP-USD         | 2022-12-10   | 2023-03-19 |        85.41 |        25.46 |         -12.22 |          25.46 |
| XTZ-USD         | 2019-09-29   | 2020-01-06 |        85.38 |        64.01 |          -1.99 |          64.01 |
| VET-USD         | 2022-12-09   | 2023-03-18 |        85.32 |        10.59 |          -4.34 |          13.84 |
| MKR-USD         | 2019-01-13   | 2019-04-22 |        85.26 |         8.61 |         -17.54 |          18.4  |
| FIL-USD         | 2021-06-29   | 2021-10-06 |        84.98 |       -11.45 |         -23.07 |          10.39 |
| ETH-USD         | 2021-06-25   | 2021-10-02 |        84.61 |        27.51 |          -0.34 |          30.16 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report

Generated: 2026-10-22 05:33 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-22 | BULL | 82.837 $ | True | 29.23% | 5.40% | BULL | 29.23% | 5.40% |
| DOGE-USD | 2026-10-22 | RECOVERY | 0.08008 $ | False | 15.19% | -2.40% | BULL | 29.23% | 5.40% |
| SOL-USD | 2026-10-22 | BULL | 105,19 $ | True | 42.38% | 8.39% | BULL | 29.23% | 5.40% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 62.50% | 5.13% | 22.17% | 27.79% | -9.85% | -25.62% | 12.75% | 22.49% | 30.24% | 47.50% | -0.92% | 27.16% | 93.14% |
| BTC-USD | SAME_BTC_REGIME | 11 | 54.55% | 0.88% | 18.08% | 27.38% | -18.16% | -29.65% | 7.79% | 21.66% | 29.52% | 36.36% | -14.43% | 83.24% | 126.27% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 100.00% | 20.73% | 24.06% | 26.05% | -6.51% | -8.75% | 25.38% | 27.45% | 28.69% | 50.00% | 49.23% | 81.06% | 100.16% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 2 | 100.00% | 20.73% | 24.06% | 26.05% | -6.51% | -8.75% | 25.38% | 27.45% | 28.69% | 50.00% | 49.23% | 81.06% | 100.16% |
| DOGE-USD | ALL_MATCHES | 40 | 80.00% | 9.60% | 22.17% | 39.81% | -6.21% | -26.43% | 16.09% | 23.31% | 59.30% | 35.00% | -8.73% | 15.39% | 39.61% |
| DOGE-USD | SAME_BTC_REGIME | 3 | 66.67% | 0.88% | 11.48% | 17.84% | -15.53% | -21.23% | 10.16% | 16.12% | 19.70% | 66.67% | 38.06% | 45.82% | 50.48% |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 100.00% | 27.51% | 27.51% | 27.51% | -0.34% | -0.34% | 30.16% | 30.16% | 30.16% | 100.00% | 35.24% | 35.24% | 35.24% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 72.50% | 6.00% | 16.08% | 29.21% | -8.79% | -34.41% | 12.75% | 22.17% | 46.48% | 42.50% | -8.17% | 23.36% | 101.39% |
| SOL-USD | SAME_BTC_REGIME | 13 | 53.85% | 0.88% | 22.09% | 41.10% | -15.53% | -28.25% | 10.16% | 22.09% | 41.53% | 46.15% | -1.57% | 53.59% | 123.59% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 50.00% | 4.04% | 17.41% | 23.39% | -9.24% | -13.66% | 15.70% | 23.30% | 27.03% | 50.00% | 11.81% | 56.77% | 90.44% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 4 | 50.00% | 4.04% | 17.41% | 23.39% | -9.24% | -13.66% | 15.70% | 23.30% | 27.03% | 50.00% | 11.81% | 56.77% | 90.44% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 28 | 67.86% | 10.17% | -7.57% | 23.07% | 53.57% | 1.84% | 32.14% |
| BTC-USD | HISTORICAL_BTC_BULL | 11 | 54.55% | 0.88% | -18.16% | 21.66% | 36.36% | -14.43% | 84.17% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -10.38% | -10.38% | 19.13% | 0.00% | -8.02% | 19.13% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 35 | 85.71% | 11.25% | -5.95% | 25.22% | 34.29% | -9.63% | 28.35% |
| DOGE-USD | HISTORICAL_BTC_BULL | 3 | 66.67% | 0.88% | -15.53% | 16.12% | 66.67% | 38.06% | 48.39% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -17.62% | -27.03% | 5.77% | 0.00% | -28.43% | 5.77% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -26.36% | -26.36% | 4.66% | 0.00% | -30.78% | 4.66% |
| SOL-USD | HISTORICAL_BTC_BEAR | 27 | 81.48% | 6.89% | -5.95% | 21.61% | 40.74% | -8.51% | 26.91% |
| SOL-USD | HISTORICAL_BTC_BULL | 13 | 53.85% | 0.88% | -15.53% | 22.09% | 46.15% | -1.57% | 55.45% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 31 | 64.52% | 7.41% | -8.40% | 22.56% | 51.61% | 1.61% | 32.36% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 20.73% | -6.51% | 27.45% | 50.00% | 49.23% | 89.98% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 11.48% | -18.06% | 18.51% | 50.00% | 26.01% | 48.73% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 20.00% | -15.93% | -15.93% | 19.13% | 20.00% | -4.65% | 19.13% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 36 | 80.56% | 9.60% | -6.11% | 23.31% | 30.56% | -10.96% | 26.66% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 1 | 0.00% | -6.00% | -15.53% | 10.16% | 100.00% | 38.06% | 41.33% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 11.48% | -18.06% | 18.51% | 50.00% | 26.01% | 48.73% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 27.51% | -0.34% | 30.16% | 100.00% | 35.24% | 41.88% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 31 | 77.42% | 6.46% | -6.37% | 21.61% | 41.94% | -8.51% | 28.42% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 4.04% | -9.24% | 23.30% | 50.00% | 11.81% | 59.22% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 0.88% | -22.65% | 14.94% | 33.33% | -1.57% | 42.00% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | 5.79% | -8.14% | 24.05% | 50.00% | 7.62% | 32.83% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 2 | 2 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | NONE | 0 | 1 | 3 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | SAME_BTC_REGIME | 4 | 4 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.
- WARNING SOL-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-06 | 89.13% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 209.44% | -8.28% | 209.44% | 244.33% | -8.28% | 326.83% |
| BTC-USD | ADA-USD | 2025-06-04 | 88.25% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.30% | -29.30% | 3.99% | -33.69% | -41.68% | 3.99% |
| BTC-USD | LRC-USD | 2020-11-27 | 87.86% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 0.88% | -22.65% | 7.79% | -1.57% | -25.13% | 28.55% |
| BTC-USD | ETH-USD | 2025-06-04 | 87.17% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -15.93% | -15.93% | 5.69% | -20.01% | -26.20% | 5.69% |
| BTC-USD | MKR-USD | 2020-11-28 | 86.89% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 2.85% | -18.16% | 11.30% | 126.27% | -18.16% | 169.44% |
| BTC-USD | XLM-USD | 2025-06-04 | 85.52% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -18.36% | -19.58% | 3.25% | -24.08% | -31.94% | 3.25% |
| BTC-USD | LINK-USD | 2025-06-04 | 85.42% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.65% | -29.65% | 2.74% | -33.20% | -39.85% | 2.74% |
| BTC-USD | DOGE-USD | 2024-01-21 | 84.42% | BULL | BULL | SAME_BTC_AND_ASSET | BULLISH_30D | 14.08% | -9.31% | 21.23% | -14.43% | -17.04% | 21.23% |
| BTC-USD | HBAR-USD | 2025-06-06 | 84.42% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -21.68% | -33.92% | 0.00% | -29.91% | -34.48% | 0.00% |
| BTC-USD | ZEC-USD | 2024-06-04 | 84.23% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 22.09% | -13.47% | 22.09% | 53.59% | -13.47% | 55.45% |
| SOL-USD | MKR-USD | 2020-11-28 | 90.75% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 2.85% | -18.16% | 11.30% | 126.27% | -18.16% | 169.44% |
| SOL-USD | ZEC-USD | 2024-06-04 | 90.55% | BULL | DISTRIBUTION | SAME_BTC_ONLY | EXPLOSIVE_60D | 22.09% | -13.47% | 22.09% | 53.59% | -13.47% | 55.45% |
| SOL-USD | ETH-USD | 2025-06-04 | 89.74% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -15.93% | -15.93% | 5.69% | -20.01% | -26.20% | 5.69% |
| SOL-USD | MKR-USD | 2023-05-22 | 89.48% | BULL | BEAR | SAME_BTC_ONLY | BULLISH_30D | 44.53% | -0.31% | 44.53% | 37.69% | -0.31% | 49.44% |
| SOL-USD | ADA-USD | 2025-06-04 | 89.25% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.30% | -29.30% | 3.99% | -33.69% | -41.68% | 3.99% |
| SOL-USD | DOGE-USD | 2024-01-21 | 88.83% | BULL | BULL | SAME_BTC_AND_ASSET | BULLISH_30D | 14.08% | -9.31% | 21.23% | -14.43% | -17.04% | 21.23% |
| SOL-USD | LINK-USD | 2025-06-04 | 88.78% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -29.65% | -29.65% | 2.74% | -33.20% | -39.85% | 2.74% |
| SOL-USD | LRC-USD | 2020-11-27 | 88.76% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 0.88% | -22.65% | 7.79% | -1.57% | -25.13% | 28.55% |
| SOL-USD | TRX-USD | 2025-06-04 | 88.61% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -9.18% | -9.18% | 1.79% | -14.47% | -18.83% | 1.79% |
| SOL-USD | SNX-USD | 2020-11-27 | 87.21% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -2.78% | -24.03% | 6.30% | -17.04% | -35.57% | 6.30% |

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

Generato: 2026-10-22 05:33 UTC

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
| BTC | 82.837 $ | 0 | NEUTRALE / MISTO | STAGE 2 / MARKUP | MASSIMI E MINIMI DECRESCENTI | DISTRIBUZIONE POSSIBILE | BASSO | HOLD / ASPETTA ROTTURA RESISTENZA |
| SOL | 105,19 $ | +3 | ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO | STAGE 2 / MARKUP | MASSIMI E MINIMI DECRESCENTI | RANGE / FASE NON CHIARA | BASSO | HOLD LEGGERO / ATTESA CONFERME |
| DOGE | 0.08008 $ | -10 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | MARKDOWN / DEBOLEZZA | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +4 | -2 | +2 | -2 | 0 | 0 | -2 | 0 |
| SOL | +4 | -2 | +1 | 0 | 0 | 0 | 0 | +3 |
| DOGE | -4 | -2 | 0 | -2 | 0 | 0 | -2 | -10 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 82.571 $ | 84.249 $ | 87.364 $ | 63.980 $ | 2,42% | -4,47% | 27,20% |
| SOL | 100,51 $ | 105,49 $ | 124,62 $ | 75,19 $ | 4,37% | -11,56% | 38,44% |
| DOGE | 0.07841 $ | 0.08494 $ | 0.10528 $ | 0.06961 $ | 4,35% | -19,80% | 15,57% |

## Lettura dettagliata

### BTC

- Prezzo: **82.837 $**
- Score classico: **0 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **HOLD / ASPETTA ROTTURA RESISTENZA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,42%; distanza supporto 0,20%; distanza resistenza 1,83%

Dettaglio:

- Trend: **+4** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in salita; STAGE 2 / MARKUP
- Stage weekly: **STAGE 2 / MARKUP** — Prezzo sopra MA30 weekly con MA30 in salita.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+2** — RSI sano 51.7; RSI in miglioramento; MACD sotto signal; istogramma MACD in miglioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.15; volume ratio 1.31
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — DISTRIBUZIONE POSSIBILE. Prezzo alto nel range ma CMF negativo: possibile distribuzione.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 51.71 |
| MACD histogram | -208.29820 |
| CMF20 | -0.148 |
| Volume ratio 20 | 1.31 |
| MA20 | 83.108 $ |
| MA50 | 81.677 $ |
| MA100 | 74.779 $ |
| MA200 | 72.727 $ |
| Pendenza MA50 20g | +5,12% |
| Pendenza MA200 60g | +5,43% |
| Bollinger width | 7,49% |
| Bollinger position | 0.44 |

### SOL

- Prezzo: **105,19 $**
- Score classico: **+3 / 12**
- Verdetto: **ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**
- Volatilità tecnica locale: **BASSO** — ATR14 4,37%; distanza supporto 4,49%; distanza resistenza 0,45%

Dettaglio:

- Trend: **+4** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in salita; STAGE 2 / MARKUP
- Stage weekly: **STAGE 2 / MARKUP** — Prezzo sopra MA30 weekly con MA30 in salita.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+1** — RSI neutrale 42.0; RSI in miglioramento; MACD sotto signal; istogramma MACD in miglioramento
- Volume: **0** — OBV sopra media; CMF negativo -0.13; volume ratio 1.00
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 41.99 |
| MACD histogram | -0.81346 |
| CMF20 | -0.128 |
| Volume ratio 20 | 1.00 |
| MA20 | 110,36 $ |
| MA50 | 109,55 $ |
| MA100 | 95,62 $ |
| MA200 | 87,96 $ |
| Pendenza MA50 20g | +7,36% |
| Pendenza MA200 60g | +8,41% |
| Bollinger width | 25,24% |
| Bollinger position | 0.30 |

### DOGE

- Prezzo: **0.08008 $**
- Score classico: **-10 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 4,35%; distanza supporto 1,91%; distanza resistenza 6,31%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; breve termine sotto MA20/MA50; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **0** — RSI neutrale 38.6; MACD sotto signal; istogramma MACD in miglioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.10; volume ratio 0.82
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 38.59 |
| MACD histogram | -0.00062 |
| CMF20 | -0.098 |
| Volume ratio 20 | 0.82 |
| MA20 | 0.08558 $ |
| MA50 | 0.08788 $ |
| MA100 | 0.08146 $ |
| MA200 | 0.08709 $ |
| Pendenza MA50 20g | +2,09% |
| Pendenza MA200 60g | -2,46% |
| Bollinger width | 28,69% |
| Bollinger position | 0.25 |

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

Generato: 2026-10-22 05:33 UTC

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
| BTC | 82.837 $ | Eve and Adam Bottom | MATURO | rialzista | 2026-09-21 | 89.580 $ | 7,86% | n/a | Fib 23,6% NON ATTIVO (0) @ 77.995 $ | NEL RANGE | 82.571 $ |
| SOL | 105,19 $ | Triplo massimo | CANDIDATO | ribassista | n/a | 62,51 $ | n/a | 48,80% | Fib 38,2% TENUTO (+1) @ 103,32 $ | NEL RANGE | 97,45 $ |
| DOGE | 0.08008 $ | Doppio minimo | CANDIDATO | rialzista | n/a | 0.13028 $ | n/a | 31,47% | Fib 23,6% NON ATTIVO (0) @ 0.08689 $ | NEL RANGE | 0.07841 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Eve and Adam Bottom**
- Stato pattern: **MATURO** (+1)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-09-15**
- Età formazione: **37 giorni**
- Breakout pattern: **2026-09-21**
- Età breakout: **31 giorni**
- Neckline: **82.262 $**
- Target teorico: **89.580 $**
- Progresso verso target: **7,86%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 77.995 $** — Swing UP 2026-07-01 57.748 -> 2026-10-12 84.249; livello più vicino 23.6% a 77.995; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **80.617 $**
- Relazione prezzo/neckline: **vicino alla neckline**
- Dettaglio: Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (31 giorni fa). Stato: MATURO. Target teorico: 89.580; progresso corrente: 7,86%. Relazione prezzo/neckline: vicino alla neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **82.571 $**
- Resistenza: **84.249 $**
- Breakout 60g: **87.364 $**
- Breakdown 60g: **63.980 $**
- RSI14: **52.16**
- ATR14: **2,42%**
- Volume ratio 20g: **1.31**
- Rendimento 30g: **-4,35%**
- Rendimento 90g: **+27,35%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Eve and Adam Bottom | MATURO | +1 | rialzista | 82.262 $ | 2026-09-21 | 31g | 89.580 $ | 7,86% | n/a | 80.617 $ | Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (31 giorni fa). Stato: MATURO. Target teorico: 89.580; progresso corrente: 7,86%. Relazione prezzo/neckline: vicino alla neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CONFERMATO RECENTE | -2 | ribassista | 82.571 $ | 2026-10-08 | 14g | 77.778 $ | -5,56% | n/a | 84.222 $ | Due massimi simili a 87.364 $ e 87.146 $. Neckline circa 82.571 $. Breakout neckline: 2026-10-08 (14 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 77.778 $; progresso: -5,56%; prezzo vicino alla neckline. |
| Doppio minimo | MATURO | +1 | rialzista | 82.262 $ | 2026-09-21 | 31g | 89.580 $ | 7,86% | n/a | 80.617 $ | Due minimi simili a 76.248 $ e 74.945 $. Neckline circa 82.262 $. Breakout neckline: 2026-09-21 (31 giorni fa). Stato: MATURO. Target teorico: 89.580 $; progresso: 7,86%; prezzo vicino alla neckline. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **74 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **70,69 $**
- Target teorico: **62,51 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **48,80%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 38,2% TENUTO (+1) @ 103,32 $** — Swing UP 2026-08-01 70,69 -> 2026-10-02 123,48; livello più vicino 38.2% a 103,32; stato TENUTO; confluenza: invalidazione rialzista.
- Invalidazione: **72,11 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 74 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **97,45 $**
- Resistenza: **107,12 $**
- Breakout 60g: **124,62 $**
- Breakdown 60g: **75,19 $**
- RSI14: **42.28**
- ATR14: **4,36%**
- Volume ratio 20g: **1.00**
- Rendimento 30g: **-11,42%**
- Rendimento 90g: **+38,66%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,51 $ | n/a | 48,80% | 72,11 $ | Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 74 giorni. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 48,80% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 74 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 107,12 $ | 2026-09-18 | 34g | 118,01 $ | -17,69% | n/a | 104,97 $ | Due minimi simili a 97,45 $ e 96,23 $. Neckline circa 107,12 $. Breakout neckline: 2026-09-18 (34 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01 $; progresso: -17,69%; prezzo sotto neckline. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 64g | 85,65 $ | 361,34% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (64 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 361,34%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-10-08**
- Età formazione: **14 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.10528 $**
- Target teorico: **0.13028 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **31,47%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08689 $** — Swing DOWN 2026-09-22 0.10528 -> 2026-10-08 0.08122; livello più vicino 23.6% a 0.08689; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.10318 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 0.08028 tra 2026-09-02 e 2026-10-08. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.07841 $**
- Resistenza: **0.09169 $**
- Breakout 60g: **0.10528 $**
- Breakdown 60g: **0.06961 $**
- RSI14: **38.87**
- ATR14: **4,34%**
- Volume ratio 20g: **0.82**
- Rendimento 30g: **-19,62%**
- Rendimento 90g: **+15,83%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CONFERMATO RECENTE | -2 | ribassista | 0.08028 $ | 2026-10-17 | 5g | 0.06059 $ | 1,03% | n/a | 0.08189 $ | Due massimi simili a 0.09998 $ e 0.09421 $. Neckline circa 0.08028 $. Breakout neckline: 2026-10-17 (5 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 0.06059 $; progresso: 1,03%; prezzo vicino alla neckline. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.10528 $ | n/a | n/a | 0.13028 $ | n/a | 31,47% | 0.10318 $ | Due minimi simili a 0.08028 $ e 0.08122 $. Neckline circa 0.10528 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 14 giorni. |

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

Generato: 2026-10-22 05:34 UTC

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 82.821 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0030% | +2,22% | 1,74 | +1,79% | 0 $ | 0 $ |
| SOL | 105,40 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0029% | -1,78% | 0,90 | -5,33% | 0 $ | 0 $ |
| DOGE | 0.08008 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0079% | -1,38% | 1,44 | +11,60% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0218% | 196,28 mln $ | 5,18 | +6,06% |
| BTC | Bitget | OK | +0,0100% | 2,90 mld $ | 0,11 | -26,31% |
| BTC | Kucoin | OK | +0,0086% | 734,49 mln $ | 0,75 | +0,95% |
| SOL | Kraken | OK | -0,0086% | 23,97 mln $ | 2,63 | -2,25% |
| SOL | Bitget | OK | +0,0002% | 429,99 mln $ | 0,50 | -18,99% |
| SOL | Kucoin | OK | -0,0055% | 110,12 mln $ | 0,95 | +5,03% |
| DOGE | Kraken | OK | +0,0062% | 4,56 mln $ | 1,05 | +13,46% |
| DOGE | Bitget | OK | +0,0054% | 102,48 mln $ | 0,73 | +31,34% |
| DOGE | Kucoin | OK | +0,0100% | 57,48 mln $ | 1,43 | -5,61% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,50**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 10, accuratezza +30,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Markdown non pienamente confermato: compare assorbimento compratore.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** Eve and Adam Bottom maturo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Resistenza vicina con acquisti aggressivi: breakout più credibile, ma serve chiusura sopra il livello.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **-0,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 0, divergenze 2.
- Flusso taker/order book: **-0,25**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff debole ma senza conferma exchange netta.
- **Fibonacci:** Fibonacci tenuto; nessuna conferma exchange netta. Confluenza tecnica dichiarata: invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 11, accuratezza +45,45%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 1.
- Flusso taker/order book: **+2,00**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +62,50% | +5,13% | 6 | +66,67% | RACCOLTA DATI | 0,00 | +62,50% | +5,13% |
| SOL | +72,50% | +6,00% | 5 | +100,00% | RACCOLTA DATI | 0,00 | +72,50% | +6,00% |
| DOGE | +80,00% | +9,60% | 11 | +63,64% | RACCOLTA DATI | 0,00 | +80,00% | +9,60% |

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

Generato: 2026-10-22 05:33 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-22 | BTC | 82.821,00 | V2.1.3 | OK | 0 | 0 | 2,50 | MEDIA | 1,74 | +2,22% | +1,79% |
| 2026-10-22 | DOGE | 0.08008 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,44 | -1,38% | +11,60% |
| 2026-10-22 | SOL | 105,40 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,90 | -1,78% | -5,33% |
| 2026-10-21 | BTC | 82.880,00 | V2.1.3 | OK | 0 | 0 | 2,50 | MEDIA | 3,60 | +1,09% | +5,13% |
| 2026-10-21 | DOGE | 0.08169 | V2.1.3 | OK | 1 | 0 | 3,00 | MEDIA | 1,16 | +4,02% | +4,30% |
| 2026-10-21 | SOL | 106,07 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,42 | +2,72% | -2,45% |
| 2026-10-20 | BTC | 81.980,50 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,64 | -0,92% | +0,20% |
| 2026-10-20 | DOGE | 0.07954 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,87 | +0,09% | +5,57% |
| 2026-10-20 | SOL | 105,03 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,86 | -0,84% | -1,61% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 10 | +40,00% | -0,44% | -1,18% | +0,59% | FEEDBACK RAPIDO |
| BTC | 3g | 10 | +40,00% | -0,44% | -2,45% | +1,64% | FEEDBACK RAPIDO |
| BTC | 7g | 10 | +30,00% | -1,89% | -3,68% | +1,86% | FEEDBACK RAPIDO |
| BTC | 14g | 9 | +33,33% | -0,96% | -4,58% | +2,58% | FEEDBACK RAPIDO |
| BTC | 30g | 6 | +66,67% | +4,10% | -5,46% | +7,48% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 5 | +100,00% | +22,07% | -4,32% | +25,38% | FEEDBACK RAPIDO |
| DOGE | 1g | 13 | +46,15% | +0,84% | -0,72% | +2,33% | FEEDBACK RAPIDO |
| DOGE | 3g | 12 | +33,33% | +1,19% | -3,61% | +5,84% | FEEDBACK RAPIDO |
| DOGE | 7g | 11 | +45,45% | -0,13% | -4,83% | +9,23% | FEEDBACK RAPIDO |
| DOGE | 14g | 11 | +36,36% | +1,12% | -6,04% | +13,84% | FEEDBACK RAPIDO |
| DOGE | 30g | 11 | +63,64% | +7,24% | -8,14% | +26,94% | FEEDBACK RAPIDO |

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

**SOL** — SOL: c'è molta leva nel mercato, ma la direzione non è pulita. Può arrivare un movimento violento, ma non è chiaro se sopra o sotto. Meglio non forzare. Aspetta conferma dal frattale o dal prezzo.

**DOGE** — DOGE: c'è molta leva nel mercato, ma la direzione non è pulita. Può arrivare un movimento violento, ma non è chiaro se sopra o sotto. Meglio non forzare. Aspetta conferma dal frattale o dal prezzo.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 82.837 $ | +0.0092% | +0.54% | 0.93 | Misto | 1/5 |
| SOL | 105,19 $ | +0.0012% | +14.68% | 1.61 | Leva alta, direzione mista | 3/5 |
| DOGE | 0.08008 $ | +0.0076% | +15.82% | 2.54 | Leva alta, direzione mista | 3/5 |

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

Generato: 2026-10-22 05:33 UTC

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                     | Stato D       | Weekly                     | Stato W       | Lettura weekly                                                                                              |   Peso |
|:--------|:--------------------------|:--------------|:---------------------------|:--------------|:------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bearish invalidata | INVALIDATA    | Conferma rialzista         | CONTESTO      | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                         |      0 |
| SOL     | Hidden bullish            | IN_FORMAZIONE | Hidden bullish             | IN_FORMAZIONE | Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0. |      0 |
| DOGE    | Conferma ribassista       | CONTESTO      | Misto / nessuna divergenza | CONTESTO      | Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.                        |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                       | Stato         | Prezzo / RSI      | Pivot confrontati                                                | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:---------------------------|:--------------|:------------------|:-----------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bearish invalidata  | INVALIDATA    | 82.757 $ / 51,80  | n/a                                                              | -0,62%              | -1,03            |      0 |
| BTC     | 1W   | Conferma rialzista         | CONTESTO      | 82.757 $ / 57,90  | n/a                                                              | +7,70%              | 3,28             |      0 |
| SOL     | 1D   | Hidden bullish             | IN_FORMAZIONE | 105,09 $ / 42,11  | 2026-09-16 96,23 $ / RSI 51,17 → 2026-10-18 100,51 $ / RSI 38,93 | n/a                 | n/a              |      0 |
| SOL     | 1W   | Hidden bullish             | IN_FORMAZIONE | 105,09 $ / 53,99  | 2026-09-20 96,23 $ / RSI 61,01 → 2026-10-18 100,51 $ / RSI 53,42 | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Conferma ribassista        | CONTESTO      | 0.07992 $ / 38,62 | n/a                                                              | -10,18%             | -6,89            |      0 |
| DOGE    | 1W   | Misto / nessuna divergenza | CONTESTO      | 0.07992 $ / 43,91 | n/a                                                              | -3,03%              | -0,93            |      0 |

### BTC

- **1D — Hidden bearish invalidata / INVALIDATA**: La precedente hidden bearish non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

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

Generato: 2026-10-22 05:33 UTC

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

| Asset   | Prezzo   |   Punteggio | Verdetto         | Trend            | Momentum       | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista                | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-----------------|:-----------------|:---------------|:------------------------------------------------------|----------------:|:---------------|:---------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 82.837 $ | -1 | NEUTRALE / MISTO | Trend rialzista | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | +1 | 0 / NON ATTIVO | Eve and Adam Bottom / MATURO | Doppio massimo / CANDIDATO | 79.736 | 84.249 |
| SOL | 105,19 $ | -1 | NEUTRALE / MISTO | Trend misto | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | 0 | +1 / TENUTO | Doppio minimo / TARGET RAGGIUNTO | Triplo massimo / CANDIDATO | 96,23 | 123,48 |
| DOGE | 0.08008 $ | -5 | DEBOLE | Trend ribassista | Momentum misto | Volatilità in espansione | 0 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 0.07841 | 0.10528 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Eve and Adam Bottom — MATURO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 1 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | INVALIDATO | CANDIDATO | ASSENTE | 0 |
| DOGE | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 52.16 | -201.782 | 83.113 | 81.679 | 72.728 | 4,55% | 5,40% | -3,87% | 29,23% |
| SOL | 42.28 | -0.80261 | 110,36 | 109,55 | 87,96 | 6,48% | 8,39% | -11,24% | 42,38% |
| DOGE | 38.87 | -0.00061 | 0.08559 | 0.08788 | 0.08709 | 1,55% | -2,40% | -20,21% | 15,19% |

## Dettaglio asset

### BTC

- Prezzo: **82.837 $**
- Punteggio tecnico: **-1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 8.034e+04 -> 7.974e+04. Ultimi massimi: 8.715e+04 -> 8.425e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Possibile distribuzione** (-2)
  - Dettaglio Wyckoff: Prezzo sopra MA200 ma momentum debole vicino alla parte alta del range.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-10-12 84.249; livello più vicino 23.6% a 77.995; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **+1**
  - rialzista dominante: Eve and Adam Bottom (MATURO, +1); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **79.736**
- Resistenza più vicina: **84.249**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 76.248 tra 2026-09-02 e 2026-10-15. Neckline stimata: 87.364. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 87.364; target 98.479; distanza dalla neckline 5,46%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 76.248 dal 2026-09-02 al 2026-10-15. Neckline stimata: 87.364. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 87.364; target 98.479; distanza dalla neckline 5,46%; prezzo sotto neckline.
- Eve and Adam Bottom: **MATURO** (+1)
  - Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (31 giorni fa). Stato: MATURO. Target teorico: 89.580; progresso corrente: 7,86%. Relazione prezzo/neckline: vicino alla neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (31g); progresso 7,86%; prezzo vicino alla neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 84.249 tra 2026-09-03 e 2026-10-12. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 74.945; target 65.640; distanza dalla neckline 10,53%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 84.249 dal 2026-08-28 al 2026-10-12. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 74.945; target 65.640; distanza dalla neckline 10,53%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 84.249 dal 2026-09-03 al 2026-10-12. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 74.945; target 65.640; distanza dalla neckline 10,53%; prezzo sopra neckline.

### SOL

- Prezzo: **105,19 $**
- Punteggio tecnico: **-1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (1)
- Momentum: **Momentum misto** (1)
- Volume: **Volume neutrale** (0)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 97.45 -> 96.23. Ultimi massimi: 124.6 -> 123.5.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Possibile distribuzione** (-2)
  - Dettaglio Wyckoff: Prezzo sopra MA200 ma momentum debole vicino alla parte alta del range.
- Fibonacci automatico: **TENUTO** (+1)
  - Swing UP 2026-08-01 70,69 -> 2026-10-02 123,48; livello più vicino 38.2% a 103,32; stato TENUTO; confluenza: invalidazione rialzista.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Triplo massimo (CANDIDATO, 0).
- Supporto più vicino: **96,23**
- Resistenza più vicina: **123,48**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 96,23 tra 2026-09-02 e 2026-09-16. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (34 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: -17,69%. Relazione prezzo/neckline: sotto neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (34g); progresso -17,69%; prezzo sotto neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (64 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 329,49%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (64g); progresso 329,49%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 96,23 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (34 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: -17,69%. Relazione prezzo/neckline: sotto neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (34g); progresso -17,69%; prezzo sotto neckline.
- Doppio massimo: **INVALIDATO** (0)
  - Due massimi simili vicino a 110,04 tra 2026-08-27 e 2026-09-06. Neckline ribassista stimata: 97,45. Breakout neckline: 2026-09-15 (37 giorni fa). Stato: INVALIDATO. Target teorico: 84,86; progresso corrente: -61,48%. Relazione prezzo/neckline: sopra neckline.
  - neckline 97,45; target 84,86; breakout 2026-09-15 (37g); progresso -61,48%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 74 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 48,80%; prezzo sopra neckline.
- Adam/Eve Top: **ASSENTE** (0)

### DOGE

- Prezzo: **0.08008 $**
- Punteggio tecnico: **-5 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (0)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 0.09053 -> 0.08122. Ultimi massimi: 0.09421 -> 0.1053.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 32,45%. Fase non abbastanza chiara.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-09-22 0.10528 -> 2026-10-08 0.08122; livello più vicino 23.6% a 0.08689; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.07841**
- Resistenza più vicina: **0.10528**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.08028 tra 2026-09-02 e 2026-10-08. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni.
  - neckline 0.10528; target 0.13028; distanza dalla neckline 31,47%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 0.07841 dal 2026-09-02 al 2026-10-08. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni.
  - neckline 0.10528; target 0.13216; distanza dalla neckline 31,47%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.08028 dal 2026-09-02 al 2026-10-08. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni.
  - neckline 0.10528; target 0.13028; distanza dalla neckline 31,47%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.10528 tra 2026-08-22 e 2026-09-22. Neckline ribassista stimata: 0.07841. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 30 giorni.
  - neckline 0.07841; target 0.05153; distanza dalla neckline 2,14%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 72 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 17,81%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07380 dal 2026-07-26 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 72 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 17,81%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-10-12 | 77.995 | 74.126 | 70.998 | 67.871 | 63.419 | 23.6% / 77.995 | NON ATTIVO | nessuna confluenza indipendente | 0 |
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

- **BTC**: 48/30 previsioni controllate su 104 fatte. Stato: **ATTIVA**.
- **SOL**: 48/30 previsioni controllate su 104 fatte. Stato: **ATTIVA**.
- **DOGE**: 48/30 previsioni controllate su 104 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 104 | 48 | 30/30 [██████████] | 56 | ATTIVA | 2026-10-23 / tra 1 giorno |
| SOL | 104 | 48 | 30/30 [██████████] | 56 | ATTIVA | 2026-10-23 / tra 1 giorno |
| DOGE | 104 | 48 | 30/30 [██████████] | 56 | ATTIVA | 2026-10-23 / tra 1 giorno |

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

Generato: 2026-10-22 05:34 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- Calibrazione rischio in quarantena; moduli sospesi esclusi dalla verifica prezzi correnti. Consultare lab_reduction_status.md.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo         | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:--------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price | OK      | 82.837 $          | 82.837 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price | OK      | 0.08008 $         | 0.08008 $       | -0,0000%     |
| Scanner                 | SOL     | current_price | OK      | 105,19 $          | 105,19 $        | -0,0000%     |
| Scanner Forecast        | BTC     | current_price | OK      | 82.837 $          | 82.837 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price | OK      | 105,19 $          | 105,19 $        | -0,0000%     |
| Scanner Forecast        | DOGE    | current_price | OK      | 0.08008 $         | 0.08008 $       | -0,0000%     |
| Technical Structure     | BTC     | price         | OK      | 82.837 $          | 82.837 $        | +0,0000%     |
| Technical Structure     | SOL     | price         | OK      | 105,19 $          | 105,19 $        | -0,0000%     |
| Technical Structure     | DOGE    | price         | OK      | 0.08008 $         | 0.08008 $       | -0,0000%     |
| Classic Technical       | BTC     | price         | OK      | 82.837 $          | 82.837 $        | +0,0000%     |
| Classic Technical       | SOL     | price         | OK      | 105,19 $          | 105,19 $        | -0,0000%     |
| Classic Technical       | DOGE    | price         | OK      | 0.08008 $         | 0.08008 $       | -0,0000%     |
| Classic Visual          | BTC     | price         | OK      | 82.837 $          | 82.837 $        | +0,0000%     |
| Classic Visual          | SOL     | price         | OK      | 105,19 $          | 105,19 $        | -0,0000%     |
| Classic Visual          | DOGE    | price         | OK      | 0.08008 $         | 0.08008 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price         | OK      | 82.837 $          | 82.821 $        | -0,0197%     |
| Exchange Microstructure | SOL     | price         | OK      | 105,19 $          | 105,40 $        | +0,1977%     |
| Exchange Microstructure | DOGE    | price         | OK      | 0.08008 $         | 0.08008 $       | -0,0000%     |

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
