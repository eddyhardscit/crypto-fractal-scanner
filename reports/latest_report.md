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

Generato: 2026-10-25 06:34 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 0 | NEUTRALE / COSTRUTTIVO | HOLD / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | -2 | LEGGERMENTE BEARISH | TAKE PROFIT SU SPIKE / NON INSEGUIRE | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | -5 | BEARISH | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **0**, spot = **HOLD / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **-2**, spot = **TAKE PROFIT SU SPIKE / NON INSEGUIRE**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **-5**, spot = **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

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
- Conferme: Prima resistenza sopra 84.249; conferma del eve and adam bottom sopra 82.262.
- Invalidazioni: Sotto 79.736 il quadro tecnico peggiora.

### SOL

- Global Confluence: **-2**
- Confluenza: **DEBOLE / FRAGILE**
- Bias Global: **Fragile**
- Direzione decisionale: **LEGGERMENTE BEARISH**
- Azione spot dal Global: **TAKE PROFIT SU SPIKE / NON INSEGUIRE**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: conferma del doppio minimo sopra 124,62; nuova conferma tecnica sopra 123,48.
- Invalidazioni: Allarmi sotto 100,51.

### DOGE

- Global Confluence: **-5**
- Confluenza: **NEGATIVA**
- Bias Global: **Ribassista**
- Direzione decisionale: **BEARISH**
- Azione spot dal Global: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**
- Long leva: **NO LONG A LEVA**
- Short leva: **SHORT SOLO DOPO SPIKE**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.10528 migliora; sopra 0.07997 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.07623 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 3; EMA200 circa 111,26 $; upside verso EMA200 +9,28%. Non autorizza leva e non aggiunge punti automatici.
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

Generato: 2026-10-25 06:34 UTC

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

Segnali totali salvati: **300**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-25 | BTC | 80.511,75 | 0 | +2 | +2 | 0 | -2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-25 | DOGE | 0.07699 | -5 | 0 | 0 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-10-25 | SOL | 101,78 | -2 | 0 | 0 | +2 | -1 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-10-24 | BTC | 80.612,90 | -1 | +2 | +2 | 0 | -2 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-24 | DOGE | 0.07824 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-24 | SOL | 102,15 | 0 | +1 | +1 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-23 | BTC | 81.657,99 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-23 | DOGE | 0.07979 | -1 | +3 | +3 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-23 | SOL | 104,39 | +3 | +3 | +3 | 0 | +1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-22 | BTC | 82.752,49 | +2 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-22 | DOGE | 0.07992 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-22 | SOL | 105,09 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 100 | 99 | 98 | 97 | 95 | 93 | 91 | 87 | 80 | 72 | 62 | 47 |
| SOL | 100 | 99 | 98 | 97 | 95 | 93 | 91 | 87 | 80 | 72 | 62 | 47 |
| DOGE | 100 | 99 | 98 | 97 | 95 | 93 | 91 | 87 | 80 | 72 | 62 | 47 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-27 | 60g | 2026-10-26 | domani |
| SOL | 2026-08-27 | 60g | 2026-10-26 | domani |
| DOGE | 2026-08-27 | 60g | 2026-10-26 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 88 | 52,27% | +0,27% | +0,25% | UTILE |
| BTC | 2g | 87 | 49,43% | +0,44% | +0,37% | UTILE |
| BTC | 3g | 86 | 45,35% | +0,57% | +0,54% | UTILE |
| BTC | 5g | 85 | 44,71% | +1,22% | +1,16% | UTILE |
| BTC | 7g | 83 | 49,40% | +1,91% | +1,76% | UTILE |
| BTC | 10g | 81 | 55,56% | +2,67% | +2,60% | UTILE |
| BTC | 14g | 78 | 57,69% | +4,05% | +4,00% | UTILE |
| BTC | 21g | 75 | 65,33% | +7,05% | +6,96% | UTILE |
| BTC | 30g | 69 | 91,30% | +11,27% | +10,65% | UTILE |
| BTC | 45g | 59 | 94,92% | +18,02% | +15,78% | PRIMA CALIBRAZIONE |
| BTC | 60g | 44 | 90,91% | +24,85% | +21,44% | PRIMA CALIBRAZIONE |
| SOL | 1g | 89 | 46,07% | +0,15% | +0,05% | UTILE |
| SOL | 2g | 89 | 42,70% | +0,47% | +0,36% | UTILE |
| SOL | 3g | 88 | 46,59% | +0,84% | +0,69% | UTILE |
| SOL | 5g | 86 | 48,84% | +1,57% | +1,55% | UTILE |
| SOL | 7g | 84 | 53,57% | +2,43% | +2,53% | UTILE |
| SOL | 10g | 83 | 51,81% | +3,53% | +3,62% | UTILE |
| SOL | 14g | 79 | 59,49% | +5,55% | +6,01% | UTILE |
| SOL | 21g | 72 | 70,83% | +11,02% | +10,52% | UTILE |
| SOL | 30g | 64 | 79,69% | +17,96% | +14,87% | UTILE |
| SOL | 45g | 55 | 72,73% | +29,45% | +15,46% | PRIMA CALIBRAZIONE |
| SOL | 60g | 40 | 70,00% | +39,86% | +17,95% | PRIMA CALIBRAZIONE |
| DOGE | 1g | 88 | 48,86% | -0,00% | -0,03% | UTILE |
| DOGE | 2g | 88 | 44,32% | +0,12% | -0,08% | UTILE |
| DOGE | 3g | 87 | 40,23% | +0,37% | +0,03% | UTILE |
| DOGE | 5g | 87 | 47,13% | +0,79% | +0,16% | UTILE |
| DOGE | 7g | 85 | 49,41% | +1,16% | +0,43% | UTILE |
| DOGE | 10g | 83 | 43,37% | +1,39% | +0,24% | UTILE |
| DOGE | 14g | 80 | 53,75% | +2,62% | +2,44% | UTILE |
| DOGE | 21g | 75 | 53,33% | +5,20% | +0,46% | UTILE |
| DOGE | 30g | 68 | 64,71% | +9,17% | +3,62% | UTILE |
| DOGE | 45g | 58 | 48,28% | +15,72% | +3,19% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 45 | 42,22% | +20,01% | -1,27% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 88 | 52,27% | +0,27% | +0,25% | -0,30% | +0,77% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 97 | 47,42% | +0,17% | +0,22% | -0,35% | +0,68% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 97 | 47,42% | +0,17% | +0,22% | -0,35% | +0,68% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 92 | 51,09% | +0,19% | +0,10% | -0,31% | +0,71% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,55% | -0,06% | -0,27% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 87 | 49,43% | +0,44% | +0,37% | -0,31% | +1,14% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 96 | 51,04% | +0,38% | +0,46% | -0,33% | +1,06% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 96 | 51,04% | +0,38% | +0,46% | -0,33% | +1,06% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 91 | 49,45% | +0,36% | +0,13% | -0,26% | +1,04% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,85% | -0,13% | -0,05% | +1,59% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 86 | 45,35% | +0,57% | +0,54% | -1,30% | +2,35% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 95 | 49,47% | +0,66% | +0,72% | -1,37% | +2,38% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 95 | 49,47% | +0,66% | +0,72% | -1,37% | +2,38% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 90 | 41,11% | +0,66% | -0,03% | -1,32% | +2,39% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 36 | 36,11% | +1,29% | -0,55% | -1,13% | +3,01% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 85 | 44,71% | +1,22% | +1,16% | -1,95% | +3,69% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 93 | 48,39% | +1,32% | +1,43% | -1,97% | +3,72% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 93 | 48,39% | +1,32% | +1,43% | -1,97% | +3,72% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 88 | 43,18% | +1,19% | -0,59% | -1,93% | +3,66% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 36 | 36,11% | +2,85% | -2,16% | -1,73% | +5,27% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 83 | 49,40% | +1,91% | +1,76% | -2,30% | +4,77% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 91 | 57,14% | +1,99% | +2,15% | -2,32% | +4,74% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 91 | 57,14% | +1,99% | +2,15% | -2,32% | +4,74% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 86 | 43,02% | +1,93% | -0,98% | -2,30% | +4,69% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 36 | 33,33% | +4,03% | -3,63% | -2,13% | +7,10% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 81 | 55,56% | +2,67% | +2,60% | -2,66% | +5,84% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 89 | 65,17% | +2,62% | +2,99% | -2,66% | +5,76% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 89 | 65,17% | +2,62% | +2,99% | -2,66% | +5,76% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 84 | 46,43% | +2,56% | -0,43% | -2,68% | +5,76% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 36 | 38,89% | +4,00% | -3,92% | -2,35% | +7,69% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -1,34% | -1,34% | -4,20% | +1,67% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 78 | 57,69% | +4,05% | +4,00% | -2,93% | +7,82% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 85 | 63,53% | +3,86% | +4,36% | -2,94% | +7,65% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 85 | 63,53% | +3,86% | +4,36% | -2,94% | +7,65% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 80 | 50,00% | +3,87% | +0,84% | -2,97% | +7,73% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 34 | 20,59% | +3,74% | -4,14% | -2,59% | +8,37% | PRIMA CALIBRAZIONE |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -1,00% | -1,00% | -4,58% | +2,51% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 75 | 65,33% | +7,05% | +6,96% | -3,12% | +11,15% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 78 | 75,64% | +7,04% | +7,37% | -3,10% | +11,15% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 78 | 75,64% | +7,04% | +7,37% | -3,10% | +11,15% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 73 | 49,32% | +7,07% | +0,83% | -3,15% | +11,27% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 32 | 40,62% | +7,31% | -4,91% | -2,79% | +11,47% | PRIMA CALIBRAZIONE |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | -0,41% | -0,41% | -5,42% | +4,34% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 69 | 91,30% | +11,27% | +10,65% | -3,06% | +15,67% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 72 | 88,89% | +11,29% | +11,29% | -3,04% | +15,77% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 72 | 88,89% | +11,29% | +11,29% | -3,04% | +15,77% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 65 | 63,08% | +11,29% | +1,04% | -3,02% | +15,87% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 29 | 55,17% | +11,81% | -2,82% | -2,66% | +16,49% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +2,81% | +2,81% | -5,71% | +6,60% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 59 | 94,92% | +18,02% | +15,78% | -3,00% | +23,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 62 | 100,00% | +18,46% | +18,46% | -2,97% | +23,53% | UTILE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 62 | 100,00% | +18,46% | +18,46% | -2,97% | +23,53% | UTILE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 57 | 61,40% | +18,23% | -1,03% | -2,84% | +23,37% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,92% | -4,17% | -2,62% | +19,88% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +7,72% | +7,72% | -5,13% | +13,34% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 44 | 90,91% | +24,85% | +21,44% | -2,34% | +30,59% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 47 | 97,87% | +24,88% | +24,88% | -2,34% | +30,71% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 47 | 97,87% | +24,88% | +24,88% | -2,34% | +30,71% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +28,58% | +28,58% | -2,21% | +34,30% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 42 | 45,24% | +24,81% | -5,54% | -2,09% | +30,84% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 15 | 40,00% | +20,64% | -13,78% | -1,43% | +27,22% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +11,44% | +11,44% | -4,01% | +16,95% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 88 | 48,86% | -0,00% | -0,03% | -0,77% | +1,02% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 98 | 56,12% | -0,09% | +0,38% | -0,89% | +0,89% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 98 | 56,12% | -0,09% | +0,38% | -0,89% | +0,89% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 92 | 52,17% | -0,17% | +0,21% | -0,99% | +0,80% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 59 | 44,07% | -0,10% | -0,44% | -0,98% | +0,62% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 13 | 53,85% | +1,93% | +1,69% | +0,19% | +2,94% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 88 | 44,32% | +0,12% | -0,08% | -0,98% | +1,48% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 97 | 55,67% | -0,09% | +0,57% | -1,14% | +1,20% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 97 | 55,67% | -0,09% | +0,57% | -1,14% | +1,20% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 91 | 54,95% | -0,37% | +0,28% | -1,43% | +0,92% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 58 | 46,55% | -0,08% | -0,75% | -1,20% | +0,93% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 13 | 38,46% | +1,97% | +1,77% | +0,35% | +4,40% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 87 | 40,23% | +0,37% | +0,03% | -2,58% | +3,57% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 96 | 54,17% | -0,01% | +0,81% | -2,79% | +3,22% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 96 | 54,17% | -0,01% | +0,81% | -2,79% | +3,22% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 90 | 47,78% | -0,56% | +0,13% | -3,01% | +2,63% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 57 | 38,60% | +0,08% | -1,41% | -2,82% | +3,31% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 13 | 46,15% | +1,80% | +1,64% | -1,90% | +5,55% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 87 | 47,13% | +0,79% | +0,16% | -3,80% | +5,68% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 94 | 50,00% | +0,41% | +1,13% | -4,06% | +5,37% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 94 | 50,00% | +0,41% | +1,13% | -4,06% | +5,37% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 88 | 54,55% | -0,31% | -0,44% | -4,41% | +4,71% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 55 | 43,64% | +0,89% | -3,22% | -4,08% | +5,90% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 33,33% | +1,94% | +1,81% | -2,90% | +8,39% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 85 | 49,41% | +1,16% | +0,43% | -4,62% | +7,37% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 92 | 54,35% | +0,86% | +1,36% | -4,88% | +7,02% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 92 | 54,35% | +0,86% | +1,36% | -4,88% | +7,02% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 86 | 48,84% | -0,03% | -0,68% | -5,32% | +6,13% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 53 | 37,74% | +1,62% | -4,47% | -4,89% | +7,66% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 41,67% | +0,56% | +0,47% | -3,35% | +8,92% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 83 | 43,37% | +1,39% | +0,24% | -5,58% | +9,07% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 90 | 53,33% | +0,88% | +1,56% | -5,85% | +8,66% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 90 | 53,33% | +0,88% | +1,56% | -5,85% | +8,66% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 84 | 48,81% | -0,31% | -1,36% | -6,37% | +7,35% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 51 | 39,22% | +2,01% | -5,21% | -5,81% | +9,55% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 80 | 53,75% | +2,62% | +2,44% | -6,59% | +12,26% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 86 | 65,12% | +1,87% | +3,78% | -6,80% | +11,68% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 86 | 65,12% | +1,87% | +3,78% | -6,80% | +11,68% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 80 | 46,25% | +0,01% | -1,97% | -7,41% | +9,42% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 48 | 43,75% | +3,01% | -4,47% | -6,31% | +11,94% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 75 | 53,33% | +5,20% | +0,46% | -6,99% | +17,30% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 79 | 63,29% | +5,32% | +5,87% | -7,07% | +17,35% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 79 | 63,29% | +5,32% | +5,87% | -7,07% | +17,35% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 73 | 47,95% | +3,37% | -4,10% | -7,78% | +14,74% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 44 | 40,91% | +4,63% | -7,88% | -6,37% | +15,31% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +4,84% | -0,04% | -5,47% | +18,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 68 | 64,71% | +9,17% | +3,62% | -6,29% | +24,62% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 71 | 70,42% | +9,52% | +7,39% | -6,24% | +25,07% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 71 | 70,42% | +9,52% | +7,39% | -6,24% | +25,07% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 65 | 55,38% | +8,06% | -3,18% | -6,98% | +23,06% | UTILE |
| DOGE | 30g | Classic technical | CALIBRABILE | 43 | 46,51% | +6,87% | -7,32% | -6,56% | +21,76% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 72,73% | +14,01% | +8,26% | -6,83% | +27,95% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 58 | 48,28% | +15,72% | +3,19% | -5,80% | +35,42% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 61 | 68,85% | +15,59% | +8,09% | -5,76% | +35,42% | UTILE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 61 | 68,85% | +15,59% | +8,09% | -5,76% | +35,42% | UTILE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 55 | 10,91% | +12,64% | -11,85% | -6,58% | +33,37% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 34 | 2,94% | +18,65% | -21,04% | -6,03% | +36,58% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +18,19% | +8,68% | -5,75% | +33,52% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 45 | 42,22% | +20,01% | -1,27% | -4,81% | +41,68% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 46 | 54,35% | +21,31% | +7,12% | -4,64% | +42,37% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 46 | 54,35% | +21,31% | +7,12% | -4,64% | +42,37% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +24,96% | +11,95% | -3,59% | +45,33% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 40 | 7,50% | +20,34% | -21,51% | -5,67% | +40,37% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 31 | 0,00% | +19,07% | -22,30% | -5,41% | +40,47% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +19,54% | +8,85% | -4,76% | +39,64% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 89 | 46,07% | +0,15% | +0,05% | -0,63% | +1,00% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 93 | 51,61% | +0,11% | +0,36% | -0,73% | +0,95% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 96 | 51,04% | +0,14% | +0,31% | -0,70% | +0,98% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 90 | 46,67% | +0,11% | -0,09% | -0,79% | +0,93% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 59 | 44,07% | +0,51% | -0,09% | -0,48% | +1,43% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 89 | 42,70% | +0,47% | +0,36% | -0,71% | +1,53% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 92 | 48,91% | +0,36% | +0,53% | -0,91% | +1,30% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 95 | 48,42% | +0,36% | +0,50% | -0,88% | +1,35% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 90 | 44,44% | +0,20% | -0,02% | -0,89% | +1,31% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,60% | +0,15% | -0,64% | +1,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 88 | 46,59% | +0,84% | +0,69% | -2,24% | +3,49% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 91 | 49,45% | +0,70% | +1,02% | -2,38% | +3,30% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 94 | 48,94% | +0,69% | +0,98% | -2,34% | +3,30% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 89 | 47,19% | +0,33% | -0,24% | -2,40% | +2,92% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 59 | 45,76% | +0,61% | +0,08% | -2,23% | +3,14% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 86 | 48,84% | +1,57% | +1,55% | -3,25% | +5,46% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 89 | 52,81% | +1,37% | +1,73% | -3,38% | +5,24% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 92 | 52,17% | +1,35% | +1,65% | -3,34% | +5,19% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 87 | 45,98% | +1,01% | -0,67% | -3,43% | +4,74% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,71% | -0,02% | -3,27% | +4,40% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 84 | 53,57% | +2,43% | +2,53% | -3,93% | +6,95% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 87 | 58,62% | +2,19% | +2,91% | -4,05% | +6,71% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 90 | 58,89% | +2,11% | +2,82% | -4,01% | +6,62% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 85 | 42,35% | +1,31% | -1,58% | -4,14% | +5,91% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 59 | 42,37% | +0,39% | -0,27% | -4,06% | +5,04% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 83 | 51,81% | +3,53% | +3,62% | -4,64% | +8,72% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 85 | 64,71% | +3,41% | +5,14% | -4,75% | +8,42% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 88 | 63,64% | +3,29% | +4,97% | -4,71% | +8,26% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 83 | 44,58% | +1,94% | -2,07% | -4,92% | +7,20% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 59 | 44,07% | +0,02% | -0,63% | -4,99% | +5,74% | PRIMA CALIBRAZIONE |

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

Generato: 2026-10-25 06:34 UTC

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
| BTC | 100 | UTILE | 97 | 30 | 19 | 0 | Famiglia statistica | 1g | 47,42% | +0,22% | campione utile, valutare con prudenza |
| SOL | 100 | UTILE | 93 | 32 | 18 | 0 | Famiglia statistica | 1g | 51,61% | +0,36% | campione utile, valutare con prudenza |
| DOGE | 100 | UTILE | 98 | 33 | 19 | 0 | Famiglia statistica | 1g | 56,12% | +0,38% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 36 | 41,67% | -0,06% | +0,55% | -0,27% | +1,09% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 97 | 47,42% | +0,22% | +0,17% | -0,35% | +0,68% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 92 | 51,09% | +0,10% | +0,19% | -0,31% | +0,71% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 36 | 41,67% | -0,13% | +0,85% | -0,05% | +1,59% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 96 | 51,04% | +0,46% | +0,38% | -0,33% | +1,06% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 91 | 49,45% | +0,13% | +0,36% | -0,26% | +1,04% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 36 | 36,11% | -0,55% | +1,29% | -1,13% | +3,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Famiglia statistica | 95 | 49,47% | +0,72% | +0,66% | -1,37% | +2,38% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 90 | 41,11% | -0,03% | +0,66% | -1,32% | +2,39% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 36 | 36,11% | -2,16% | +2,85% | -1,73% | +5,27% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 93 | 48,39% | +1,43% | +1,32% | -1,97% | +3,72% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 88 | 43,18% | -0,59% | +1,19% | -1,93% | +3,66% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 36 | 33,33% | -3,63% | +4,03% | -2,13% | +7,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 91 | 57,14% | +2,15% | +1,99% | -2,32% | +4,74% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 86 | 43,02% | -0,98% | +1,93% | -2,30% | +4,69% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 36 | 38,89% | -3,92% | +4,00% | -2,35% | +7,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 89 | 65,17% | +2,99% | +2,62% | -2,66% | +5,76% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 9 | 33,33% | -1,34% | -1,34% | -4,20% | +1,67% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 84 | 46,43% | -0,43% | +2,56% | -2,68% | +5,76% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 34 | 20,59% | -4,14% | +3,74% | -2,59% | +8,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Famiglia statistica | 85 | 63,53% | +4,36% | +3,86% | -2,94% | +7,65% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 9 | 33,33% | -1,00% | -1,00% | -4,58% | +2,51% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 80 | 50,00% | +0,84% | +3,87% | -2,97% | +7,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 32 | 40,62% | -4,91% | +7,31% | -2,79% | +11,47% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 21g | SWING | Famiglia statistica | 78 | 75,64% | +7,37% | +7,04% | -3,10% | +11,15% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 8 | 50,00% | -0,41% | -0,41% | -5,42% | +4,34% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 73 | 49,32% | +0,83% | +7,07% | -3,15% | +11,27% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 29 | 55,17% | -2,82% | +11,81% | -2,66% | +16,49% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 72 | 88,89% | +11,29% | +11,29% | -3,04% | +15,77% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Microstruttura exchange | 7 | 71,43% | +2,81% | +2,81% | -5,71% | +6,60% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 65 | 63,08% | +1,04% | +11,29% | -3,02% | +15,87% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Classic technical | 24 | 66,67% | -4,17% | +13,92% | -2,62% | +19,88% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 62 | 100,00% | +18,46% | +18,46% | -2,97% | +23,53% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +7,72% | +7,72% | -5,13% | +13,34% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 57 | 61,40% | -1,03% | +18,23% | -2,84% | +23,37% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 15 | 40,00% | -13,78% | +20,64% | -1,43% | +27,22% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 47 | 97,87% | +24,88% | +24,88% | -2,34% | +30,71% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 60g | MEDIO | Microstruttura exchange | 3 | 66,67% | +11,44% | +11,44% | -4,01% | +16,95% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 42 | 45,24% | -5,54% | +24,81% | -2,09% | +30,84% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Classic technical | 59 | 44,07% | -0,44% | -0,10% | -0,98% | +0,62% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 98 | 56,12% | +0,38% | -0,09% | -0,89% | +0,89% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 13 | 53,85% | +1,69% | +1,93% | +0,19% | +2,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 92 | 52,17% | +0,21% | -0,17% | -0,99% | +0,80% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 58 | 46,55% | -0,75% | -0,08% | -1,20% | +0,93% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 97 | 55,67% | +0,57% | -0,09% | -1,14% | +1,20% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 13 | 38,46% | +1,77% | +1,97% | +0,35% | +4,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 91 | 54,95% | +0,28% | -0,37% | -1,43% | +0,92% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 57 | 38,60% | -1,41% | +0,08% | -2,82% | +3,31% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 96 | 54,17% | +0,81% | -0,01% | -2,79% | +3,22% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 13 | 46,15% | +1,64% | +1,80% | -1,90% | +5,55% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 90 | 47,78% | +0,13% | -0,56% | -3,01% | +2,63% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 55 | 43,64% | -3,22% | +0,89% | -4,08% | +5,90% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 94 | 50,00% | +1,13% | +0,41% | -4,06% | +5,37% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 12 | 33,33% | +1,81% | +1,94% | -2,90% | +8,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 88 | 54,55% | -0,44% | -0,31% | -4,41% | +4,71% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 53 | 37,74% | -4,47% | +1,62% | -4,89% | +7,66% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 92 | 54,35% | +1,36% | +0,86% | -4,88% | +7,02% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 12 | 41,67% | +0,47% | +0,56% | -3,35% | +8,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 86 | 48,84% | -0,68% | -0,03% | -5,32% | +6,13% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 51 | 39,22% | -5,21% | +2,01% | -5,81% | +9,55% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 90 | 53,33% | +1,56% | +0,88% | -5,85% | +8,66% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 84 | 48,81% | -1,36% | -0,31% | -6,37% | +7,35% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 48 | 43,75% | -4,47% | +3,01% | -6,31% | +11,94% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 86 | 65,12% | +3,78% | +1,87% | -6,80% | +11,68% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 11 | 45,45% | +2,03% | +5,60% | -4,35% | +14,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 80 | 46,25% | -1,97% | +0,01% | -7,41% | +9,42% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 44 | 40,91% | -7,88% | +4,63% | -6,37% | +15,31% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 79 | 63,29% | +5,87% | +5,32% | -7,07% | +17,35% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 11 | 63,64% | -0,04% | +4,84% | -5,47% | +18,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 73 | 47,95% | -4,10% | +3,37% | -7,78% | +14,74% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Classic technical | 43 | 46,51% | -7,32% | +6,87% | -6,56% | +21,76% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 71 | 70,42% | +7,39% | +9,52% | -6,24% | +25,07% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 11 | 72,73% | +8,26% | +14,01% | -6,83% | +27,95% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 65 | 55,38% | -3,18% | +8,06% | -6,98% | +23,06% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 45g | MEDIO | Classic technical | 34 | 2,94% | -21,04% | +18,65% | -6,03% | +36,58% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Famiglia statistica | 61 | 68,85% | +8,09% | +15,59% | -5,76% | +35,42% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 9 | 55,56% | +8,68% | +18,19% | -5,75% | +33,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 55 | 10,91% | -11,85% | +12,64% | -6,58% | +33,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 31 | 0,00% | -22,30% | +19,07% | -5,41% | +40,47% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Famiglia statistica | 46 | 54,35% | +7,12% | +21,31% | -4,64% | +42,37% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 7 | 57,14% | +8,85% | +19,54% | -4,76% | +39,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 40 | 7,50% | -21,51% | +20,34% | -5,67% | +40,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 1g | BREVE | Classic technical | 59 | 44,07% | -0,09% | +0,51% | -0,48% | +1,43% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 93 | 51,61% | +0,36% | +0,11% | -0,73% | +0,95% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 90 | 46,67% | -0,09% | +0,11% | -0,79% | +0,93% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 59 | 47,46% | +0,15% | +0,60% | -0,64% | +1,71% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 92 | 48,91% | +0,53% | +0,36% | -0,91% | +1,30% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 90 | 44,44% | -0,02% | +0,20% | -0,89% | +1,31% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 59 | 45,76% | +0,08% | +0,61% | -2,23% | +3,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 91 | 49,45% | +1,02% | +0,70% | -2,38% | +3,30% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 89 | 47,19% | -0,24% | +0,33% | -2,40% | +2,92% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 59 | 47,46% | -0,02% | +0,71% | -3,27% | +4,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 89 | 52,81% | +1,73% | +1,37% | -3,38% | +5,24% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 87 | 45,98% | -0,67% | +1,01% | -3,43% | +4,74% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 59 | 42,37% | -0,27% | +0,39% | -4,06% | +5,04% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 87 | 58,62% | +2,91% | +2,19% | -4,05% | +6,71% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 85 | 42,35% | -1,58% | +1,31% | -4,14% | +5,91% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 59 | 44,07% | -0,63% | +0,02% | -4,99% | +5,74% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 85 | 64,71% | +5,14% | +3,41% | -4,75% | +8,42% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 83 | 44,58% | -2,07% | +1,94% | -4,92% | +7,20% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 58 | 39,66% | -1,01% | +0,50% | -6,22% | +7,02% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 81 | 76,54% | +8,40% | +5,67% | -5,43% | +11,79% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 79 | 37,97% | -3,46% | +3,44% | -5,76% | +9,89% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 54 | 50,00% | -3,06% | +6,24% | -6,70% | +13,42% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 74 | 83,78% | +14,34% | +11,44% | -5,61% | +18,31% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 72 | 45,83% | -6,06% | +8,84% | -6,12% | +15,93% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Classic technical | 46 | 50,00% | -4,82% | +19,57% | -5,26% | +26,11% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 67 | 88,06% | +17,77% | +19,58% | -4,72% | +27,68% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 64 | 42,19% | -7,85% | +18,60% | -5,14% | +25,66% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 45g | MEDIO | Classic technical | 42 | 42,86% | -14,46% | +24,35% | -4,70% | +36,72% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 45g | MEDIO | Famiglia statistica | 57 | 73,68% | +18,28% | +29,75% | -4,38% | +40,46% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +28,91% | +28,91% | -3,55% | +37,55% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 59 | 37,29% | -18,61% | +28,97% | -4,73% | +39,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 28 | 21,43% | -37,31% | +43,29% | -3,57% | +53,55% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 42 | 71,43% | +28,07% | +43,12% | -3,49% | +55,45% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 5 | 80,00% | +23,15% | +23,15% | -3,55% | +39,85% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 44 | 22,73% | -32,09% | +42,06% | -4,00% | +53,86% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 89 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 98 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 108 | 39,81% | -0,25% |
| BTC | BREVE | Famiglia statistica | 288 | 49,31% | +0,46% |
| BTC | BREVE | Microstruttura exchange | 27 | 37,04% | -0,30% |
| BTC | BREVE | Tecnico | 273 | 47,25% | +0,07% |
| BTC | SETTIMANALE | Classic technical | 108 | 36,11% | -3,24% |
| BTC | SETTIMANALE | Famiglia statistica | 273 | 56,78% | +2,18% |
| BTC | SETTIMANALE | Microstruttura exchange | 27 | 22,22% | -1,65% |
| BTC | SETTIMANALE | Tecnico | 258 | 44,19% | -0,67% |
| BTC | SWING | Classic technical | 66 | 30,30% | -4,51% |
| BTC | SWING | Famiglia statistica | 163 | 69,33% | +5,80% |
| BTC | SWING | Microstruttura exchange | 17 | 41,18% | -0,72% |
| BTC | SWING | Tecnico | 153 | 49,67% | +0,83% |
| BTC | MEDIO | Classic technical | 68 | 55,88% | -5,72% |
| BTC | MEDIO | Famiglia statistica | 181 | 95,03% | +17,27% |
| BTC | MEDIO | Microstruttura exchange | 15 | 80,00% | +6,17% |
| BTC | MEDIO | Tecnico | 164 | 57,93% | -1,36% |
| DOGE | BREVE | Classic technical | 174 | 43,10% | -0,86% |
| DOGE | BREVE | Famiglia statistica | 291 | 55,33% | +0,58% |
| DOGE | BREVE | Microstruttura exchange | 39 | 46,15% | +1,70% |
| DOGE | BREVE | Tecnico | 273 | 51,65% | +0,21% |
| DOGE | SETTIMANALE | Classic technical | 159 | 40,25% | -4,27% |
| DOGE | SETTIMANALE | Famiglia statistica | 276 | 52,54% | +1,34% |
| DOGE | SETTIMANALE | Microstruttura exchange | 35 | 42,86% | +1,00% |
| DOGE | SETTIMANALE | Tecnico | 258 | 50,78% | -0,82% |
| DOGE | SWING | Classic technical | 92 | 42,39% | -6,10% |
| DOGE | SWING | Famiglia statistica | 165 | 64,24% | +4,78% |
| DOGE | SWING | Microstruttura exchange | 22 | 54,55% | +0,99% |
| DOGE | SWING | Tecnico | 153 | 47,06% | -2,99% |
| DOGE | MEDIO | Classic technical | 108 | 19,44% | -15,94% |
| DOGE | MEDIO | Famiglia statistica | 178 | 65,73% | +7,56% |
| DOGE | MEDIO | Microstruttura exchange | 27 | 62,96% | +8,55% |
| DOGE | MEDIO | Tecnico | 160 | 28,12% | -10,74% |
| SOL | BREVE | Classic technical | 177 | 45,76% | +0,05% |
| SOL | BREVE | Famiglia statistica | 276 | 50,00% | +0,63% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 269 | 46,10% | -0,12% |
| SOL | SETTIMANALE | Classic technical | 177 | 44,63% | -0,31% |
| SOL | SETTIMANALE | Famiglia statistica | 261 | 58,62% | +3,23% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 255 | 44,31% | -1,43% |
| SOL | SWING | Classic technical | 112 | 44,64% | -2,00% |
| SOL | SWING | Famiglia statistica | 155 | 80,00% | +11,24% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 151 | 41,72% | -4,70% |
| SOL | MEDIO | Classic technical | 116 | 40,52% | -16,16% |
| SOL | MEDIO | Famiglia statistica | 166 | 78,92% | +20,55% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 15 | 93,33% | +24,60% |
| SOL | MEDIO | Tecnico | 167 | 35,33% | -18,04% |

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

Generato: 2026-10-25 06:33 UTC

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
| BTC | 0 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD / ATTESA CONFERME | Prima resistenza sopra 84.249; conferma del eve and adam bottom sopra 82.262. | Sotto 79.736 il quadro tecnico peggiora. |
| SOL | -2 | DEBOLE / FRAGILE | Fragile | BASSA / RACCOLTA DATI | TAKE PROFIT SU SPIKE / NON INSEGUIRE | conferma del doppio minimo sopra 124,62; nuova conferma tecnica sopra 123,48. | Allarmi sotto 100,51. |
| DOGE | -5 | NEGATIVA | Ribassista | MEDIA | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | Sopra 0.10528 migliora; sopra 0.07997 viene invalidato il pattern ribassista dominante. | Sotto 0.07623 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | 0 | +2 | 0 | -2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| SOL | 0 | +2 | 0 | 0 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | -2 |
| DOGE | 0 | 0 | 0 | 0 | -3 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | -5 |

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

- Famiglia statistica: **+2** — Scanner grezzo +2, Market Regime grezzo 0, match regime 1. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+2** — Casi positivi 62,50%, return centrale 30g +2,88%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 1, positivi 30g 100,00%, return p50 +6,46%.
- Scanner path: **0** — Controlli disponibili 98. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -5/12, verdetto debole, trend misto, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff possibile distribuzione, pattern score +1 (rialzista Eve and Adam Bottom / MATURO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -3/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 2 / MARKUP, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff DISTRIBUZIONE POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Fractal path: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- RSI top-cycle: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.50; exchange 3/3, copertura 100%, consenso bull 2, bear 0, divergenze 0, campioni 4h 9 su 4.00h; candidato +1, peso Global +0 (LOCKED / RACCOLTA 7G). Bias POSITIVA / CANDIDATA, ANCORA NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +1 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — BTC: nessun cambiamento forte in misto rispetto a ieri.

Conferme: Prima resistenza sopra 84.249; conferma del eve and adam bottom sopra 82.262.

Invalidazioni: Sotto 79.736 il quadro tecnico peggiora.

### SOL

- Confluenza: **DEBOLE / FRAGILE**
- Bias: **Fragile**
- Punteggio finale: **-2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **TAKE PROFIT SU SPIKE / NON INSEGUIRE**

SOL è fragile nel breve. Il frattale da solo non basta: se non recupera le conferme e il gap non rientra, il rischio è di inseguire uno spike scaricato.

Dettaglio moduli:

- Famiglia statistica: **0** — Scanner grezzo 0, Market Regime grezzo +2, match regime 5. Scanner neutro e regime non abbastanza forte o non abbastanza popolato. Punteggio contato nel Global: 0.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **0** — Casi positivi 50,00%, return centrale 30g +0,30%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 5, positivi 30g 60,00%, return p50 +6,46%.
- Scanner path: **0** — Controlli disponibili 98. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-1** — Score tecnico -2/12, verdetto neutrale / misto, trend misto, struttura compressione / triangolo, divergenza rialzista nascosta rsi, Wyckoff range / fase non chiara, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Triplo massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 2 / MARKUP, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff RANGE / FASE NON CHIARA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Fractal path: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- RSI top-cycle: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 3, bias SQUEEZE SETUP MODERATO, EMA200 111,26 $, upside EMA200 +9,28%, gap EMA50/EMA200 -4,53%, hit EMA200 12w +76,67%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Leva alta, direzione mista, forza 3/5.
- Daily change: **-1** — SOL: cambiamento medio in peggioramento rispetto a ieri.

Conferme: conferma del doppio minimo sopra 124,62; nuova conferma tecnica sopra 123,48.

Invalidazioni: Allarmi sotto 100,51.

### DOGE

- Confluenza: **NEGATIVA**
- Bias: **Ribassista**
- Punteggio finale: **-5**
- Affidabilità: **MEDIA**
- Azione coerente: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**

DOGE resta l'asset più debole. Anche senza contare due volte Scanner e Market Regime, la confluenza generale resta chiaramente negativa rispetto a BTC e SOL.

Dettaglio moduli:

- Famiglia statistica: **0** — Scanner grezzo 0, Market Regime grezzo 0, match regime 1. Scanner neutro e regime non abbastanza forte o non abbastanza popolato. Punteggio contato nel Global: 0.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **0** — Casi positivi 50,00%, return centrale 30g +1,43%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 1, positivi 30g 0,00%, return p50 -46,00%.
- Scanner path: **0** — Controlli disponibili 98. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-3** — Score tecnico -8/12, verdetto ribassista tecnico, trend ribassista, struttura volatilità in espansione, divergenza nessuna, Wyckoff range / fase non chiara, pattern score -1 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / ATTIVO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -11/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Fractal path: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- RSI top-cycle: **0** — SOSPESO dal 2026-10-13; archivio escluso dai segnali.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow -0.25, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 0, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — DOGE: cambiamento forte in peggioramento rispetto a ieri.

Conferme: Sopra 0.10528 migliora; sopra 0.07997 viene invalidato il pattern ribassista dominante.

Invalidazioni: Sotto 0.07623 il rischio ribassista aumenta.


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

Generato: 2026-10-25 06:33 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 80.511 $ | prezzo corrente |
| Power Law centrale | 127.263 $ | deviazione -36,74% |
| Banda p10-p90 | 79.702 $ / 322.393 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 10,90% | posizione storica nel corridoio |
| Esponente β | 5,7770 | R² log-log 91,95% |
| Stabilità β | BASSA | range 1,3152 cambiando finestra |
| Ultimo halving | 2024-04-19 | 919 giorni fa |
| Fase ciclo | 62,90% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-10-25 (4421 osservazioni)
- Formula stimata: prezzo ≈ exp(-38.8425) × giorni^5.7770
- Prezzo centrale oggi: **127.263 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 10,90%
- Scarto dal centro: **-36,74%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,7770 | 91,95% |
| 2015 | 5,8559 | 91,49% |
| 2016 | 5,5370 | 87,79% |
| 2017 | 4,8149 | 83,11% |
| 2018 | 4,5407 | 78,73% |

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
| 2012-11-28 → 2016-07-09 | 2015-03-08 | -7,72% | -17,76% | -16,06% | +51,02% |
| 2016-07-09 → 2020-05-11 | 2018-12-08 | +15,80% | +12,23% | +125,02% | +117,61% |
| 2020-05-11 → 2024-04-19 | 2022-11-02 | -15,23% | +14,78% | +39,35% | +73,31% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | 0 | 0 | -8.93294989298099 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -7 | -1 | -15.72957992215358 | 0 |

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

Generato: 2026-10-25 06:33 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00126310 | 0 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | -8,93% | MISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000096 | -7 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -15,73% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (0)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g -0,46%; 30g -8,93%; 90g +7,77%; 180g +15,25%
- **Daily:** RSI 33.22; MA50 0.00133892; MA200 0.00120513
- **Weekly:** MA30 0.00120707; RSI 49.13
- **Livelli:** supporto 0.00124400; resistenza 0.00129400; breakout 60g 0.00146600; breakdown 60g 0.00118000
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00133900; target 0.00140150
- **Fibonacci:** VICINO — 50.0% a 0.00124300
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in salita; struttura con massimi/minimi decrescenti; RSI relativo debole; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-7)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g -1,78%; 30g -15,73%; 90g -14,75%; 180g -25,25%
- **Daily:** RSI 30.41; MA50 0.00000107; MA200 0.00000119
- **Weekly:** MA30 0.00000120; RSI 33.84
- **Livelli:** supporto 0.00000092; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000093
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000105
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; RSI relativo debole; MACD relativo negativo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 212 | 52,36% | +1,92% | -1,06% |
| SOL | 30g | 210 | 47,62% | +4,51% | +0,58% |
| SOL | 90g | 203 | 52,71% | +9,70% | +3,16% |
| DOGE | 7g | 298 | 55,70% | +1,81% | -1,68% |
| DOGE | 30g | 296 | 53,04% | +1,98% | -3,49% |
| DOGE | 90g | 292 | 54,79% | +6,92% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 52 | 48,08% | -0,01% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 52 | 44,23% | +0,06% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 52 | 36,54% | -0,67% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 52 | 34,62% | -1,85% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 39 | 51,28% | -0,98% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 73 | 65,75% | +0,23% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 71 | 64,79% | +0,51% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 67 | 62,69% | +0,46% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 61 | 55,74% | +0,45% | LOCKED / RACCOLTA LIVE | 0 |
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
| Prezzo SOL | 101,76 $ |
| EMA200 weekly target | 111,26 $ |
| Upside verso EMA200 | +9,28% |
| Distanza prezzo da EMA200 | -8,49% |
| Gap EMA50/EMA200 | -4,53% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 52,10 |
| Età SOL | 6,5 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +76,67% |
| Max gain mediano 12w | +36,63% |
| Drawdown mediano 12w | -30,75% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-10-25 06:33 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-10-25 06:30:22 UTC**

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
| BTC | NESSUN CAMBIAMENTO FORTE | misto | RIALZISTA | +62.50% | 0.00 punti |
| SOL | CAMBIAMENTO MEDIO | peggioramento | NEUTRALE / INCERTO | +50.00% | -7.50 punti |
| DOGE | CAMBIAMENTO FORTE | peggioramento | NEUTRALE / INCERTO | +50.00% | -17.50 punti |

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
| BTC | 76.495 $ | 88.573 $ | +40,00% | +15,79% | rimbalzo debole | 88.573 $ | 76.495 $ | +12,00% | -13,64% | spike storicamente più resistente |
| SOL | 96,67 $ | 111,94 $ | +46,88% | +15,79% | rimbalzo debole | 111,94 $ | 96,67 $ | +12,50% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07312 $ | 0,08467 $ | +50,00% | +15,79% | rimbalzo possibile | 0,08467 $ | 0,07312 $ | +11,54% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 10 poi sono rimbalzati fino a +10,00%. Percentuale: +40,00% (10/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 3 poi sono scaricati a -5,00%. Percentuale: +12,00% (3/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 32 prima sono scesi a -5,00%. Tra quei 32, 15 poi sono rimbalzati fino a +10,00%. Percentuale: +46,88% (15/32). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **SOL: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 3 poi sono scaricati a -5,00%. Percentuale: +12,50% (3/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 15 poi sono rimbalzati fino a +10,00%. Percentuale: +50,00% (15/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **DOGE: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 3 poi sono scaricati a -5,00%. Percentuale: +11,54% (3/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-10-25 06:32:56 UTC

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-10-25 | 2026-10-25T06:30:21Z | 2026-10-25 06:30:22 |
| SOL | 2026-10-25 | 2026-10-25T06:30:21Z | 2026-10-25 06:30:22 |
| DOGE | 2026-10-25 | 2026-10-25T06:30:21Z | 2026-10-25 06:30:22 |

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
| BTC | 2026-10-25 | 80.521 $ | SALITA | 62,50% | 63.031,64 $ | 70.765,39 $ | 82.842,95 $ | 99.462,21 $ | 109.496,20 $ |
| SOL | 2026-10-25 | 101,76 $ | INCERTO | 50,00% | 87,17 $ | 96,98 $ | 102,07 $ | 113,95 $ | 129,24 $ |
| DOGE | 2026-10-25 | 0.07697 $ | INCERTO | 50,00% | 0.06792 $ | 0.07395 $ | 0.07807 $ | 0.09508 $ | 0.11184 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted              | selected_regime_group     |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:--------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | AVAILABLE | SAME_BTC_REGIME | 1 | 2 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 82.842,95 $ | 69.636,10 $ | 109.496,20 $ | 134.290,19 $ |
| SOL | AVAILABLE | SAME_BTC_AND_ASSET_REGIME | 5 | 5 | 13 | 5 | 5 | 0_FULL_REGIME | FULL_REGIME_THRESHOLD_MET | 102,07 $ | 108,34 $ | 129,24 $ | 117,85 $ |
| DOGE | INSUFFICIENT_REGIME_MATCHES | NONE | 1 | 3 | 4 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 0.07807 $ | n/a | 0.11184 $ | n/a |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-09-25**; verificato fino al **2026-10-25**; stato **COMPLETO 30/30g**.
- Reale **80.522,71 $**; p50 previsto **87.565,11 $**; scarto **-8,04%**.
- Errore medio assoluto **7,01%**; massimo **14,30%**; DENTRO p10-p90; DENTRO p25-p75.

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
| Cono standard | 2026-10-25 | 40 | 2026-11-24 | 87.17 $ | 96.98 $ | 102.07 $ | 113.95 $ | 129.24 $ |
| Conditional corrente | 2026-10-25 | 15 | 2026-11-24 | 76.02 $ | 81.59 $ | 89.87 $ | 113.99 $ | 139.53 $ |

###### Struttura successiva dei casi correnti

| Classe | Episodi | Frequenza empirica |
| --- | ---: | ---: |
| DIRECT_CONTINUATION | 2 | 13.33% |
| SHALLOW_PULLBACK_THEN_CONTINUATION | 2 | 13.33% |
| DEEP_PULLBACK_THEN_RECOVERY | 1 | 6.67% |
| FAILURE | 10 | 66.67% |
| UNRESOLVED | 0 | 0.00% |

###### Episodi qualificati oggi

| Asset | Match window | -5% hit | +10% anchor | Classe 60d |
| --- | --- | --- | --- | --- |
| MKR-USD | 2020-12-03 → 2021-03-12 | 2021-03-15 | 2021-04-02 | FAILURE |
| ENJ-USD | 2022-12-12 → 2023-03-21 | 2023-03-22 | 2023-04-07 | FAILURE |
| ZEC-USD | 2024-06-09 → 2024-09-16 | 2024-10-01 | 2024-10-10 | DIRECT_CONTINUATION |
| LRC-USD | 2020-12-02 → 2021-03-11 | 2021-03-12 | 2021-03-17 | FAILURE |
| CRV-USD | 2022-12-11 → 2023-03-20 | 2023-03-24 | 2023-04-13 | FAILURE |
| MKR-USD | 2019-01-13 → 2019-04-22 | 2019-04-24 | 2019-05-15 | FAILURE |
| HBAR-USD | 2022-12-09 → 2023-03-18 | 2023-03-27 | 2023-03-29 | FAILURE |
| VET-USD | 2022-12-14 → 2023-03-23 | 2023-03-27 | 2023-04-16 | FAILURE |
| ICP-USD | 2022-12-10 → 2023-03-19 | 2023-03-20 | 2023-04-16 | DIRECT_CONTINUATION |
| FIL-USD | 2022-12-11 → 2023-03-20 | 2023-03-25 | 2023-04-15 | FAILURE |
| BAT-USD | 2022-12-12 → 2023-03-21 | 2023-03-22 | 2023-04-01 | FAILURE |
| DOGE-USD | 2024-01-21 → 2024-04-29 | 2024-04-30 | 2024-05-04 | FAILURE |
| ZIL-USD | 2022-12-09 → 2023-03-18 | 2023-03-25 | 2023-04-01 | SHALLOW_PULLBACK_THEN_CONTINUATION |
| AVAX-USD | 2023-10-09 → 2024-01-16 | 2024-01-18 | 2024-02-10 | DEEP_PULLBACK_THEN_RECOVERY |
| ETH-USD | 2020-12-02 → 2021-03-11 | 2021-03-22 | 2021-04-02 | SHALLOW_PULLBACK_THEN_CONTINUATION |

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

- Cono congelato il **2026-09-25**; verificato fino al **2026-10-25**; stato **COMPLETO 30/30g**.
- Reale **101,81 $**; p50 previsto **116,73 $**; scarto **-12,78%**.
- Errore medio assoluto **7,26%**; massimo **15,68%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_AND_ASSET_REGIME**; fallback: **0_FULL_REGIME**; motivo: **FULL_REGIME_THRESHOLD_MET**.

![Scanner forecast regime-adjusted SOL](scanner_forecast_SOL_regime_adjusted.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-09-25**; verificato fino al **2026-10-25**; stato **COMPLETO 30/30g**.
- Reale **0.07697 $**; p50 previsto **0.09324 $**; scarto **-17,45%**.
- Errore medio assoluto **5,90%**; massimo **17,45%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 98 | 94,90% | 73,47% | 1,82% | 0,17% |
| BTC | 3g | 94 | 94,68% | 78,72% | 2,95% | 0,42% |
| BTC | 7g | 86 | 94,19% | 73,26% | 4,67% | 0,74% |
| BTC | 14g | 73 | 98,63% | 79,45% | 5,70% | -0,01% |
| BTC | 30g | 44 | 100,00% | 68,18% | 12,12% | -5,43% |
| SOL | 1g | 98 | 86,73% | 65,31% | 2,59% | 0,36% |
| SOL | 3g | 94 | 92,55% | 72,34% | 3,81% | 0,91% |
| SOL | 7g | 86 | 93,02% | 72,09% | 5,89% | 1,48% |
| SOL | 14g | 73 | 90,41% | 69,86% | 8,44% | 2,87% |
| SOL | 30g | 44 | 95,45% | 72,73% | 14,70% | 2,77% |
| DOGE | 1g | 98 | 89,80% | 62,24% | 2,95% | 0,04% |
| DOGE | 3g | 94 | 92,55% | 60,64% | 4,66% | 0,46% |
| DOGE | 7g | 86 | 77,91% | 68,60% | 8,51% | 2,91% |
| DOGE | 14g | 73 | 83,56% | 49,32% | 10,48% | 5,32% |
| DOGE | 30g | 44 | 95,45% | 43,18% | 16,01% | 13,70% |

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
- Prezzo attuale: **80.521,30 $**
- Return normale fra 30 giorni: **82.842,95 $** (2,88%)
- Drawdown normale durante il mese: **74.120,54 $** (-7,95%)
- Drawdown brutto da rispettare: **66.893,44 $** (-16,92%)
- Max gain normale durante il mese: **92.034,67 $** (14,30%)
- Max gain buono / take profit ottimistico: **101.521,58 $** (26,08%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **50,00%**
- Casi negativi / discesa storica: **50,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **101,76 $**
- Return normale fra 30 giorni: **102,07 $** (0,30%)
- Drawdown normale durante il mese: **90,77 $** (-10,80%)
- Drawdown brutto da rispettare: **84,63 $** (-16,83%)
- Max gain normale durante il mese: **115,06 $** (13,07%)
- Max gain buono / take profit ottimistico: **121,37 $** (19,27%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **50,00%**
- Casi negativi / discesa storica: **50,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **0,08 $**
- Return normale fra 30 giorni: **0,08 $** (1,43%)
- Drawdown normale durante il mese: **0,07 $** (-9,03%)
- Drawdown brutto da rispettare: **0,07 $** (-12,16%)
- Max gain normale durante il mese: **0,09 $** (13,40%)
- Max gain buono / take profit ottimistico: **0,10 $** (26,22%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è misto. Alcuni asset possono avere lettura diversa, quindi è meglio valutare asset per asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 80.521,30 $

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

- Se va molto male: **63.031,64 $** (-21,72%)
- Se va male: **70.765,39 $** (-12,12%)
- Scenario normale: **82.842,95 $** (2,88%)
- Se va bene: **99.462,21 $** (23,52%)
- Se va molto bene: **109.496,20 $** (35,98%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **74.120,54 $** (-7,95%)
- Discesa brutta: **66.893,44 $** (-16,92%)
- Discesa molto brutta: **60.544,24 $** (-24,81%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **92.034,67 $** (14,30%)
- Rialzo buono: **101.521,58 $** (26,08%)
- Rialzo molto forte: **129.542,04 $** (60,88%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **74.120,54 $** e uno spike normale intorno a **92.034,67 $**.

La chiusura a 30 giorni era più spesso positiva: salita 62,50%, discesa 37,50%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 101,76 $

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

- Se va molto male: **87,17 $** (-14,33%)
- Se va male: **96,98 $** (-4,69%)
- Scenario normale: **102,07 $** (0,30%)
- Se va bene: **113,95 $** (11,98%)
- Se va molto bene: **129,24 $** (27,01%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **90,77 $** (-10,80%)
- Discesa brutta: **84,63 $** (-16,83%)
- Discesa molto brutta: **72,46 $** (-28,79%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **115,06 $** (13,07%)
- Rialzo buono: **121,37 $** (19,27%)
- Rialzo molto forte: **133,04 $** (30,74%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **90,77 $** e uno spike normale intorno a **115,06 $**.

La chiusura a 30 giorni è incerta: salita 50,00%, discesa 50,00%. Non c'è un vantaggio netto.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 0,08 $

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

- Se va molto male: **0,07 $** (-11,76%)
- Se va male: **0,07 $** (-3,92%)
- Scenario normale: **0,08 $** (1,43%)
- Se va bene: **0,10 $** (23,52%)
- Se va molto bene: **0,11 $** (45,30%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,07 $** (-9,03%)
- Discesa brutta: **0,07 $** (-12,16%)
- Discesa molto brutta: **0,06 $** (-21,41%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,09 $** (13,40%)
- Rialzo buono: **0,10 $** (26,22%)
- Rialzo molto forte: **0,12 $** (50,88%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,07 $** e uno spike normale intorno a **0,09 $**.

La chiusura a 30 giorni è incerta: salita 50,00%, discesa 50,00%. Non c'è un vantaggio netto.

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

- Previsioni già controllate: **51**
- Direzione corretta: **86,05%**
- Errore medio dello scenario centrale: **10,68%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **1,96%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **51**
- Direzione corretta: **75,00%**
- Errore medio dello scenario centrale: **14,95%**
- Zona rischio toccata: **1,96%**
- Zona rialzo media toccata: **27,45%**
- Prezzo finale dentro lo scenario 10%-90%: **96,08%**

### Solana

- Previsioni già controllate: **51**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **12,95%**
- Zona rischio toccata: **3,92%**
- Zona rialzo media toccata: **21,57%**
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

- Previsioni controllate: **51**
- Previsioni usate per la calibrazione recente: **51**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **86,05%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **SALITA**
- Direzione calibrata oggi: **DISCESA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **2,88%** → **82.842,95 $**
- Correzione imparata dagli errori: **-4,92%**
- Calibrato: **-2,04%** → **78.882,55 $**
- Lettura: Lo scanner è stato troppo ottimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-7,95%** → **74.120,54 $**
- Correzione imparata dagli errori: **4,34%**
- Calibrato: **-3,61%** → **77.615,97 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **14,30%** → **92.034,67 $**
- Correzione imparata dagli errori: **-9,85%**
- Calibrato: **4,45%** → **84.104,59 $**
- Lettura: Lo scanner ha sovrastimato gli spike: nella realtà il prezzo è salito meno del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Solana

- Previsioni controllate: **51**
- Previsioni usate per la calibrazione recente: **51**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **100,00%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **INCERTO**
- Direzione calibrata oggi: **INCERTO**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **0,30%** → **102,07 $**
- Correzione imparata dagli errori: **0,86%**
- Calibrato: **1,16%** → **102,94 $**
- Lettura: Lo scanner è stato abbastanza centrato sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-10,80%** → **90,77 $**
- Correzione imparata dagli errori: **3,43%**
- Calibrato: **-7,37%** → **94,26 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **13,07%** → **115,06 $**
- Correzione imparata dagli errori: **-3,12%**
- Calibrato: **9,95%** → **111,88 $**
- Lettura: Lo scanner ha sovrastimato gli spike: nella realtà il prezzo è salito meno del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Dogecoin

- Previsioni controllate: **51**
- Previsioni usate per la calibrazione recente: **51**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **75,00%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **INCERTO**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **1,43%** → **0,08 $**
- Correzione imparata dagli errori: **12,96%**
- Calibrato: **14,39%** → **0,09 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-9,03%** → **0,07 $**
- Correzione imparata dagli errori: **13,09%**
- Calibrato: **4,06%** → **0,08 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **13,40%** → **0,09 $**
- Correzione imparata dagli errori: **2,54%**
- Calibrato: **15,94%** → **0,09 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 80.521,30 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **62,50%**
- Casi negativi dopo 30 giorni: **37,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,46%**
- Rendimento medio dopo 30 giorni: **15,13%**
- Rendimento centrale dopo 30 giorni: **2,88%**
- Discesa media durante i 30 giorni: **-10,74%**
- Massimo rialzo medio durante i 30 giorni: **27,24%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **92.706,93 $**
- Scenario centrale a 30 giorni: **82.842,95 $**
- Zona di rischio media: **71.874,77 $**
- Zona di rialzo media: **102.456,44 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -21,72% → **63.031,64 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -12,12% → **70.765,39 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 2,88% → **82.842,95 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 23,52% → **99.462,21 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 35,98% → **109.496,20 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -24,81% → **60.544,24 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -16,92% → **66.893,44 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -7,95% → **74.120,54 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -2,55% → **78.468,59 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,22% → **80.345,68 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 2,56% → **82.584,53 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 4,84% → **84.417,83 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 14,30% → **92.034,67 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 26,08% → **101.521,58 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 60,88% → **129.542,04 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| RUNE-USD        | 2023-07-11   | 2023-10-18 |        90.64 |       308.03 |          -3.16 |         308.03 |
| XTZ-USD         | 2019-10-04   | 2020-01-11 |        89.42 |       101.06 |          -1.98 |         102.61 |
| ADA-USD         | 2025-06-09   | 2025-09-16 |        88.38 |       -26.77 |         -28.22 |           5.07 |
| LRC-USD         | 2020-12-02   | 2021-03-11 |        88.19 |        -1.03 |         -19.36 |          12.38 |
| CRV-USD         | 2022-12-11   | 2023-03-20 |        87.44 |        -0.51 |          -7.61 |          14.87 |
| AVAX-USD        | 2021-07-11   | 2021-10-18 |        87.3  |        94.33 |           0    |          94.33 |
| BTC-USD         | 2020-03-27   | 2020-07-04 |        87.14 |        23.15 |          -0.64 |          28.77 |
| MKR-USD         | 2019-01-13   | 2019-04-22 |        87.13 |         8.61 |         -17.54 |          18.4  |
| QTUM-USD        | 2023-09-23   | 2023-12-31 |        86.93 |       -22.07 |         -24.6  |           0    |
| ETH-USD         | 2025-06-09   | 2025-09-16 |        86.93 |       -13.52 |         -16.72 |           4.09 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 101,76 $

Solana è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **50,00%**
- Casi negativi dopo 30 giorni: **50,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **87,95%**
- Rendimento medio dopo 30 giorni: **13,27%**
- Rendimento centrale dopo 30 giorni: **0,30%**
- Discesa media durante i 30 giorni: **-13,43%**
- Massimo rialzo medio durante i 30 giorni: **23,93%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **115,27 $**
- Scenario centrale a 30 giorni: **102,07 $**
- Zona di rischio media: **88,09 $**
- Zona di rialzo media: **126,11 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -14,33% → **87,17 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -4,69% → **96,98 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 0,30% → **102,07 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 11,98% → **113,95 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 27,01% → **129,24 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -28,79% → **72,46 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -16,83% → **84,63 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -10,80% → **90,77 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -6,62% → **95,02 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -2,41% → **99,31 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,20% → **101,97 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 4,84% → **106,68 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 13,07% → **115,06 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 19,27% → **121,37 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 30,74% → **133,04 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XTZ-USD         | 2019-10-04   | 2020-01-11 |        93.12 |       101.06 |          -1.98 |         102.61 |
| AVAX-USD        | 2021-07-11   | 2021-10-18 |        90.3  |        94.33 |           0    |          94.33 |
| MKR-USD         | 2020-12-03   | 2021-03-12 |        90.16 |         6.46 |         -14.63 |          16.1  |
| ENJ-USD         | 2022-12-12   | 2023-03-21 |        90    |        -2.47 |         -10.27 |          15.21 |
| ZEC-USD         | 2024-06-09   | 2024-09-16 |        89.96 |        26.95 |         -11.92 |          28.52 |
| LRC-USD         | 2020-12-02   | 2021-03-11 |        89.75 |        -1.03 |         -19.36 |          12.38 |
| CRV-USD         | 2022-12-11   | 2023-03-20 |        89.71 |        -0.51 |          -7.61 |          14.87 |
| MKR-USD         | 2019-01-13   | 2019-04-22 |        89.59 |         8.61 |         -17.54 |          18.4  |
| THETA-USD       | 2022-12-11   | 2023-03-20 |        89.26 |         8.36 |          -4.11 |          20.8  |
| RUNE-USD        | 2023-07-11   | 2023-10-18 |        89.17 |       308.03 |          -3.16 |         308.03 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 0,08 $

Dogecoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **50,00%**
- Casi negativi dopo 30 giorni: **50,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **82,77%**
- Rendimento medio dopo 30 giorni: **17,17%**
- Rendimento centrale dopo 30 giorni: **1,43%**
- Discesa media durante i 30 giorni: **-11,46%**
- Massimo rialzo medio durante i 30 giorni: **27,98%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,09 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,10 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -11,76% → **0,07 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -3,92% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 1,43% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 23,52% → **0,10 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 45,30% → **0,11 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -21,41% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -12,16% → **0,07 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -9,03% → **0,07 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,82% → **0,07 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,61% → **0,08 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,08 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 4,89% → **0,08 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 13,40% → **0,09 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 26,22% → **0,10 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 50,88% → **0,12 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XTZ-USD         | 2019-10-04   | 2020-01-11 |        90.55 |       101.06 |          -1.98 |         102.61 |
| LINK-USD        | 2019-09-04   | 2019-12-12 |        88.66 |         7.75 |         -17.83 |           7.75 |
| ZEC-USD         | 2024-06-09   | 2024-09-16 |        86.32 |        26.95 |         -11.92 |          28.52 |
| ENJ-USD         | 2022-12-12   | 2023-03-21 |        84.92 |        -2.47 |         -10.27 |          15.21 |
| BAT-USD         | 2022-12-12   | 2023-03-21 |        84.51 |        -0.01 |          -7.13 |          16.37 |
| WAVES-USD       | 2022-12-12   | 2023-03-21 |        84.38 |       -11.67 |         -11.67 |           0.66 |
| THETA-USD       | 2022-12-11   | 2023-03-20 |        84.35 |         8.36 |          -4.11 |          20.8  |
| ENJ-USD         | 2020-03-22   | 2020-06-29 |        83.99 |         2.9  |          -1.99 |          20.85 |
| AAVE-USD        | 2022-12-10   | 2023-03-19 |        83.94 |         2.87 |         -12.35 |           4.73 |
| CRV-USD         | 2022-12-11   | 2023-03-20 |        83.91 |        -0.51 |          -7.61 |          14.87 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report

Generated: 2026-10-25 06:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-10-25 | BULL | 80.521 $ | True | 26.36% | 5.38% | BULL | 26.36% | 5.38% |
| DOGE-USD | 2026-10-25 | RECOVERY | 0.07697 $ | False | 9.43% | -2.52% | BULL | 26.36% | 5.38% |
| SOL-USD | 2026-10-25 | BULL | 101,76 $ | True | 37.25% | 8.48% | BULL | 26.36% | 5.38% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 62.50% | 2.88% | 23.52% | 35.98% | -7.95% | -24.81% | 14.30% | 26.08% | 60.88% | 47.50% | -2.82% | 27.07% | 93.14% |
| BTC-USD | SAME_BTC_REGIME | 9 | 33.33% | -13.52% | 0.29% | 66.78% | -19.36% | -29.36% | 5.07% | 12.38% | 74.49% | 22.22% | -29.91% | -8.26% | 171.11% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 100.00% | 16.24% | 21.13% | 24.06% | -9.57% | -13.62% | 22.25% | 25.33% | 27.18% | 100.00% | 86.46% | 118.94% | 138.43% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 6.46% | 6.46% | 6.46% | -14.63% | -14.63% | 16.10% | 16.10% | 16.10% | 100.00% | 151.43% | 151.43% | 151.43% |
| DOGE-USD | ALL_MATCHES | 40 | 50.00% | 1.43% | 23.52% | 45.30% | -9.03% | -21.41% | 13.40% | 26.22% | 50.88% | 35.00% | -9.13% | 26.16% | 62.68% |
| DOGE-USD | SAME_BTC_REGIME | 4 | 50.00% | 3.36% | 82.82% | 217.95% | -18.60% | -38.00% | 10.06% | 86.29% | 219.34% | 50.00% | 26.36% | 108.20% | 193.18% |
| DOGE-USD | SAME_ASSET_REGIME | 3 | 33.33% | -7.64% | 9.94% | 20.48% | -19.66% | -40.73% | 1.05% | 15.61% | 24.34% | 33.33% | -4.06% | 15.59% | 27.38% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -46.00% | -46.00% | -46.00% | -46.00% | -46.00% | 1.05% | 1.05% | 1.05% | 0.00% | -38.82% | -38.82% | -38.82% |
| SOL-USD | ALL_MATCHES | 40 | 50.00% | 0.30% | 11.98% | 27.01% | -10.80% | -28.79% | 13.07% | 19.27% | 30.74% | 40.00% | -10.96% | 27.59% | 93.14% |
| SOL-USD | SAME_BTC_REGIME | 13 | 38.46% | -2.78% | 14.08% | 24.41% | -15.53% | -27.92% | 10.16% | 17.36% | 33.00% | 38.46% | -14.43% | 38.06% | 144.43% |
| SOL-USD | SAME_ASSET_REGIME | 5 | 60.00% | 6.46% | 14.08% | 15.81% | -12.75% | -15.17% | 16.10% | 17.36% | 19.68% | 60.00% | 38.06% | 116.42% | 137.43% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 5 | 60.00% | 6.46% | 14.08% | 15.81% | -12.75% | -15.17% | 16.10% | 17.36% | 19.68% | 60.00% | 38.06% | 116.42% | 137.43% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 29 | 68.97% | 6.46% | -5.05% | 25.31% | 51.72% | 8.14% | 47.84% |
| BTC-USD | HISTORICAL_BTC_BULL | 9 | 33.33% | -13.52% | -19.36% | 12.38% | 22.22% | -29.91% | 34.03% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 100.00% | 29.69% | -6.08% | 63.93% | 100.00% | 27.41% | 86.54% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 34 | 50.00% | 1.43% | -8.26% | 24.76% | 32.35% | -12.35% | 33.09% |
| DOGE-USD | HISTORICAL_BTC_BULL | 4 | 50.00% | 3.36% | -18.60% | 86.29% | 50.00% | 26.36% | 135.74% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 26.95% | -11.92% | 28.52% | 100.00% | 32.52% | 58.24% |
| DOGE-USD | HISTORICAL_BTC_MIXED | 1 | 0.00% | -7.64% | -19.66% | 0.00% | 0.00% | -4.06% | 1.58% |
| SOL-USD | HISTORICAL_BTC_BEAR | 26 | 53.85% | 1.16% | -8.14% | 18.72% | 38.46% | -10.96% | 34.49% |
| SOL-USD | HISTORICAL_BTC_BULL | 13 | 38.46% | -2.78% | -15.53% | 17.36% | 38.46% | -14.43% | 41.33% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 26.95% | -11.92% | 28.52% | 100.00% | 32.52% | 58.24% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 32 | 68.75% | 4.68% | -5.79% | 26.11% | 50.00% | 3.10% | 50.48% |
| BTC-USD | HISTORICAL_ASSET_BULL | 2 | 100.00% | 16.24% | -9.57% | 25.33% | 100.00% | 86.46% | 144.32% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.03% | -19.36% | 12.38% | 0.00% | -8.26% | 34.03% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 20.00% | -15.62% | -21.04% | 5.77% | 20.00% | -29.69% | 5.77% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 35 | 51.43% | 2.87% | -8.29% | 26.99% | 34.29% | -11.93% | 36.75% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 1 | 100.00% | 7.75% | -17.83% | 7.75% | 100.00% | 60.99% | 64.10% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.03% | -19.36% | 12.38% | 0.00% | -8.26% | 34.03% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -7.64% | -19.66% | 15.61% | 33.33% | -4.06% | 21.73% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 53.33% | 1.16% | -9.28% | 20.29% | 40.00% | -10.96% | 38.08% |
| SOL-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 6.46% | -12.75% | 17.36% | 60.00% | 38.06% | 116.42% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -1.90% | -21.69% | 10.86% | 0.00% | -12.65% | 27.10% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -13.52% | -16.72% | 17.52% | 33.33% | -29.69% | 23.38% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group     |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            |
|:---------|:--------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|
| BTC-USD | SAME_BTC_REGIME | 1 | 2 | 9 | 9 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME |
| DOGE-USD | NONE | 1 | 3 | 4 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 5 | 5 | 13 | 5 | 5 | 0_FULL_REGIME | FULL_REGIME_THRESHOLD_MET |

- WARNING BTC-USD: SAME_BTC_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | RUNE-USD | 2023-07-11 | 90.64% | BULL | BEAR | SAME_BTC_ONLY | EXPLOSIVE_60D | 308.03% | -3.16% | 308.03% | 249.83% | -3.16% | 350.68% |
| BTC-USD | ADA-USD | 2025-06-09 | 88.38% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -26.77% | -28.22% | 5.07% | -42.84% | -43.41% | 5.07% |
| BTC-USD | LRC-USD | 2020-12-02 | 88.19% | BULL | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -1.03% | -19.36% | 12.38% | -8.26% | -21.94% | 34.03% |
| BTC-USD | ETH-USD | 2025-06-09 | 86.93% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -13.52% | -16.72% | 4.09% | -29.69% | -31.08% | 4.09% |
| BTC-USD | ONE-USD | 2023-08-04 | 86.86% | BULL | BEAR | SAME_BTC_ONLY | MIXED | 0.29% | -0.68% | 1.26% | -43.98% | -45.15% | 1.26% |
| BTC-USD | MKR-USD | 2020-12-03 | 86.86% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 6.46% | -14.63% | 16.10% | 151.43% | -14.63% | 181.05% |
| BTC-USD | LINK-USD | 2025-06-09 | 85.39% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -25.92% | -26.73% | 4.88% | -39.90% | -41.26% | 4.88% |
| BTC-USD | HBAR-USD | 2025-06-06 | 84.55% | BULL | BEAR | SAME_BTC_ONLY | BEARISH_30D | -21.68% | -33.92% | 0.00% | -29.91% | -34.48% | 0.00% |
| BTC-USD | ALGO-USD | 2025-06-08 | 83.41% | BULL | RECOVERY | SAME_BTC_ONLY | BEARISH_30D | -15.62% | -24.43% | 5.77% | -30.93% | -33.70% | 5.77% |
| SOL-USD | MKR-USD | 2020-12-03 | 90.16% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 6.46% | -14.63% | 16.10% | 151.43% | -14.63% | 181.05% |
| SOL-USD | LINK-USD | 2019-08-30 | 87.87% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -6.00% | -15.53% | 10.16% | 38.06% | -15.53% | 41.33% |
| SOL-USD | DOGE-USD | 2024-01-21 | 87.20% | BULL | BULL | SAME_BTC_AND_ASSET | BULLISH_30D | 14.08% | -9.31% | 21.23% | -14.43% | -17.04% | 21.23% |
| SOL-USD | TRX-USD | 2025-06-04 | 86.92% | BULL | BULL | SAME_BTC_AND_ASSET | MIXED | -9.18% | -9.18% | 1.79% | -14.47% | -18.83% | 1.79% |
| SOL-USD | ETH-USD | 2020-12-02 | 85.96% | BULL | BULL | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 16.96% | -12.75% | 17.36% | 116.42% | -12.75% | 116.42% |

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

Generato: 2026-10-25 06:33 UTC

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
| BTC | 80.521 $ | -3 | DEBOLE / NON CONFERMATO | STAGE 2 / MARKUP | VOLATILITÀ IN ESPANSIONE | DISTRIBUZIONE POSSIBILE | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 101,76 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 2 / MARKUP | MASSIMI E MINIMI DECRESCENTI | RANGE / FASE NON CHIARA | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.07697 $ | -11 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | MARKDOWN / DEBOLEZZA | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +4 | 0 | -3 | -2 | 0 | 0 | -2 | -3 |
| SOL | +4 | -2 | -2 | -2 | 0 | 0 | 0 | -2 |
| DOGE | -4 | -2 | -1 | -2 | 0 | 0 | -2 | -11 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 80.337 $ | 81.347 $ | 87.364 $ | 73.011 $ | 2,54% | -4,57% | 23,24% |
| SOL | 100,51 $ | 105,49 $ | 124,62 $ | 87,60 $ | 4,09% | -12,97% | 32,93% |
| DOGE | 0.07623 $ | 0.07923 $ | 0.10528 $ | 0.07623 $ | 4,31% | -19,56% | 5,08% |

## Lettura dettagliata

### BTC

- Prezzo: **80.521 $**
- Score classico: **-3 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,54%; distanza supporto 0,23%; distanza resistenza 1,02%

Dettaglio:

- Trend: **+4** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in salita; STAGE 2 / MARKUP
- Stage weekly: **STAGE 2 / MARKUP** — Prezzo sopra MA30 weekly con MA30 in salita.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **-3** — RSI neutrale 43.3; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.12; volume ratio 0.73
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — DISTRIBUZIONE POSSIBILE. Prezzo alto nel range ma CMF negativo: possibile distribuzione.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 43.31 |
| MACD histogram | -304.96307 |
| CMF20 | -0.124 |
| Volume ratio 20 | 0.73 |
| MA20 | 82.531 $ |
| MA50 | 81.795 $ |
| MA100 | 75.286 $ |
| MA200 | 72.899 $ |
| Pendenza MA50 20g | +3,50% |
| Pendenza MA200 60g | +5,46% |
| Bollinger width | 6,99% |
| Bollinger position | 0.14 |

### SOL

- Prezzo: **101,76 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 4,09%; distanza supporto 1,32%; distanza resistenza 3,59%

Dettaglio:

- Trend: **+4** — prezzo sopra MA200 daily; breve termine sotto MA20/MA50; MA50 daily in salita; MA200 daily in salita; STAGE 2 / MARKUP
- Stage weekly: **STAGE 2 / MARKUP** — Prezzo sopra MA30 weekly con MA30 in salita.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **-2** — RSI debole 36.9; RSI in peggioramento; MACD sotto signal; istogramma MACD in miglioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.15; volume ratio 0.83
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 36.86 |
| MACD histogram | -0.65100 |
| CMF20 | -0.145 |
| Volume ratio 20 | 0.83 |
| MA20 | 107,86 $ |
| MA50 | 109,62 $ |
| MA100 | 96,41 $ |
| MA200 | 88,27 $ |
| Pendenza MA50 20g | +4,70% |
| Pendenza MA200 60g | +8,57% |
| Bollinger width | 21,92% |
| Bollinger position | 0.23 |

### DOGE

- Prezzo: **0.07697 $**
- Score classico: **-11 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 4,31%; distanza supporto 1,04%; distanza resistenza 2,87%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; breve termine sotto MA20/MA50; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **-1** — RSI debole 33.9; MACD sotto signal; istogramma MACD in miglioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.13; volume ratio 0.81
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 33.87 |
| MACD histogram | -0.00048 |
| CMF20 | -0.129 |
| Volume ratio 20 | 0.81 |
| MA20 | 0.08331 $ |
| MA50 | 0.08752 $ |
| MA100 | 0.08162 $ |
| MA200 | 0.08688 $ |
| Pendenza MA50 20g | -0,00% |
| Pendenza MA200 60g | -2,57% |
| Bollinger width | 25,55% |
| Bollinger position | 0.18 |

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

Generato: 2026-10-25 06:33 UTC

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
| BTC | 80.521 $ | Eve and Adam Bottom | MATURO | rialzista | 2026-09-21 | 89.580 $ | -23,79% | n/a | Fib 23,6% NON ATTIVO (0) @ 77.995 $ | NEL RANGE | 80.337 $ |
| SOL | 101,76 $ | Doppio minimo | CANDIDATO | rialzista | n/a | 151,78 $ | n/a | 22,46% | Fib 23,6% REJECTION (0) @ 106,20 $ | NEL RANGE | 100,51 $ |
| DOGE | 0.07697 $ | Doppio massimo | ATTIVO | ribassista | 2026-10-25 | 0.05153 $ | 5,34% | n/a | Fib 23,6% REJECTION (0) @ 0.08308 $ | NEL RANGE | 0.07623 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Eve and Adam Bottom**
- Stato pattern: **MATURO** (+1)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-09-15**
- Età formazione: **40 giorni**
- Breakout pattern: **2026-09-21**
- Età breakout: **34 giorni**
- Neckline: **82.262 $**
- Target teorico: **89.580 $**
- Progresso verso target: **-23,79%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 77.995 $** — Swing UP 2026-07-01 57.748 -> 2026-10-12 84.249; livello più vicino 23.6% a 77.995; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **80.617 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (34 giorni fa). Stato: MATURO. Target teorico: 89.580; progresso corrente: -23,79%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **80.337 $**
- Resistenza: **81.347 $**
- Breakout 60g: **87.364 $**
- Breakdown 60g: **73.011 $**
- RSI14: **43.31**
- ATR14: **2,54%**
- Volume ratio 20g: **0.73**
- Rendimento 30g: **-4,57%**
- Rendimento 90g: **+23,23%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Eve and Adam Bottom | MATURO | +1 | rialzista | 82.262 $ | 2026-09-21 | 34g | 89.580 $ | -23,79% | n/a | 80.617 $ | Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (34 giorni fa). Stato: MATURO. Target teorico: 89.580; progresso corrente: -23,79%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | MATURO | -1 | ribassista | 82.571 $ | 2026-10-08 | 17g | 77.778 $ | 42,76% | n/a | 84.222 $ | Due massimi simili a 87.364 $ e 87.146 $. Neckline circa 82.571 $. Breakout neckline: 2026-10-08 (17 giorni fa). Stato: MATURO. Target teorico: 77.778 $; progresso: 42,76%; prezzo sotto neckline. |
| Doppio minimo | MATURO | +1 | rialzista | 82.262 $ | 2026-09-21 | 34g | 89.580 $ | -23,79% | n/a | 80.617 $ | Due minimi simili a 76.248 $ e 74.945 $. Neckline circa 82.262 $. Breakout neckline: 2026-09-21 (34 giorni fa). Stato: MATURO. Target teorico: 89.580 $; progresso: -23,79%; prezzo sotto neckline. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-10-18**
- Età formazione: **7 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **124,62 $**
- Target teorico: **151,78 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **22,46%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% REJECTION (0) @ 106,20 $** — Swing DOWN 2026-09-27 124,62 -> 2026-10-18 100,51; livello più vicino 23.6% a 106,20; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Invalidazione: **122,13 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 97,45 tra 2026-09-02 e 2026-10-18. Neckline stimata: 124,62. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **100,51 $**
- Resistenza: **107,12 $**
- Breakout 60g: **124,62 $**
- Breakdown 60g: **87,60 $**
- RSI14: **36.75**
- ATR14: **4,10%**
- Volume ratio 20g: **0.83**
- Rendimento 30g: **-13,03%**
- Rendimento 90g: **+32,84%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CANDIDATO | 0 | rialzista | 124,62 $ | n/a | n/a | 151,78 $ | n/a | 22,46% | 122,13 $ | Due minimi simili a 97,45 $ e 100,51 $. Neckline circa 124,62 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 7 giorni. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 43,94% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 77 giorni. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 67g | 85,65 $ | 315,47% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (67 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 315,47%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **ATTIVO** (-1)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-08-22 -> 2026-09-22**
- Età formazione: **33 giorni**
- Breakout pattern: **2026-10-25**
- Età breakout: **0 giorni**
- Neckline: **0.07841 $**
- Target teorico: **0.05153 $**
- Progresso verso target: **5,34%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% REJECTION (0) @ 0.08308 $** — Swing DOWN 2026-09-22 0.10528 -> 2026-10-18 0.07623; livello più vicino 23.6% a 0.08308; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.07997 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due massimi simili vicino a 0.10528 tra 2026-08-22 e 2026-09-22. Neckline ribassista stimata: 0.07841. Breakout neckline: 2026-10-25 (0 giorni fa). Stato: ATTIVO. Target teorico: 0.05153; progresso corrente: 5,34%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.07623 $**
- Resistenza: **0.07923 $**
- Breakout 60g: **0.10528 $**
- Breakdown 60g: **0.07623 $**
- RSI14: **33.80**
- ATR14: **4,31%**
- Volume ratio 20g: **0.81**
- Rendimento 30g: **-19,61%**
- Rendimento 90g: **+5,01%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | ATTIVO | -1 | ribassista | 0.07841 $ | 2026-10-25 | 0g | 0.05153 $ | 5,34% | n/a | 0.07997 $ | Due massimi simili vicino a 0.10528 tra 2026-08-22 e 2026-09-22. Neckline ribassista stimata: 0.07841. Breakout neckline: 2026-10-25 (0 giorni fa). Stato: ATTIVO. Target teorico: 0.05153; progresso corrente: 5,34%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CONFERMATO RECENTE | -2 | ribassista | 0.08028 $ | 2026-10-17 | 8g | 0.06059 $ | 16,82% | n/a | 0.08189 $ | Due massimi simili a 0.09998 $ e 0.09421 $. Neckline circa 0.08028 $. Breakout neckline: 2026-10-17 (8 giorni fa). Stato: CONFERMATO RECENTE. Target teorico: 0.06059 $; progresso: 16,82%; prezzo sotto neckline. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.10528 $ | n/a | n/a | 0.13434 $ | n/a | 36,78% | 0.10318 $ | Due minimi simili a 0.07841 $ e 0.07623 $. Neckline circa 0.10528 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 7 giorni. |

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

Generato: 2026-10-25 06:33 UTC

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 80.554 $ | 3 | +1 | 0 | POSITIVA / CANDIDATA, ANCORA NON PESATA | MEDIA | 100% | +0,0068% | +0,80% | 2,78 | -3,82% | 0 $ | 0 $ |
| SOL | 101,76 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0017% | +0,19% | 1,87 | +1,05% | 0 $ | 0 $ |
| DOGE | 0.07694 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0013% | -2,69% | 0,72 | -3,48% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0054% | 216,20 mln $ | 0,71 | -2,57% |
| BTC | Bitget | OK | +0,0054% | 2,90 mld $ | 2,62 | +15,08% |
| BTC | Kucoin | OK | +0,0027% | 772,95 mln $ | 1,70 | +6,97% |
| SOL | Kraken | OK | -0,0025% | 21,40 mln $ | 0,34 | +1,60% |
| SOL | Bitget | OK | -0,0015% | 423,24 mln $ | 0,93 | +0,35% |
| SOL | Kucoin | OK | +0,0014% | 120,52 mln $ | 2,14 | +5,35% |
| DOGE | Kraken | OK | -0,0048% | 4,17 mln $ | 0,67 | -12,62% |
| DOGE | Bitget | OK | -0,0033% | 97,33 mln $ | 0,44 | +2,84% |
| DOGE | Kucoin | OK | +0,0086% | 53,96 mln $ | 0,52 | -32,45% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,50**; candidato: **+1**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 10, accuratezza +30,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 2, bear 0, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Markdown non pienamente confermato: compare assorbimento compratore.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** Eve and Adam Bottom maturo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Supporto vicino con assorbimento/acquisti: tenuta più credibile.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci rejection; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Supporto vicino con assorbimento/acquisti: tenuta più credibile.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **-0,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 12, accuratezza +41,67%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 0.
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
| BTC | +62,50% | +2,88% | 8 | +50,00% | RACCOLTA DATI | 0,00 | +62,50% | +2,88% |
| SOL | +50,00% | +0,30% | 5 | +100,00% | RACCOLTA DATI | 0,00 | +50,00% | +0,30% |
| DOGE | +50,00% | +1,43% | 11 | +63,64% | RACCOLTA DATI | 0,00 | +50,00% | +1,43% |

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

Generato: 2026-10-25 06:33 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-25 | BTC | 80.554,50 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 2,78 | +0,80% | -3,82% |
| 2026-10-25 | DOGE | 0.07694 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,72 | -2,69% | -3,48% |
| 2026-10-25 | SOL | 101,76 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,87 | +0,19% | +1,05% |
| 2026-10-24 | BTC | 80.803,09 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,89 | -1,46% | +5,56% |
| 2026-10-24 | DOGE | 0.07859 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,19 | -3,56% | +2,38% |
| 2026-10-24 | SOL | 102,45 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,05 | -1,66% | -5,17% |
| 2026-10-23 | BTC | 81.699,50 | V2.1.3 | OK | 0 | 0 | 0,38 | MEDIA | 3,22 | +2,20% | -0,97% |
| 2026-10-23 | DOGE | 0.07955 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,14 | +0,85% | -3,30% |
| 2026-10-23 | SOL | 104,14 | V2.1.3 | OK | 0 | 0 | 0,38 | MEDIA | 1,86 | +2,40% | +1,99% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 10 | +40,00% | -0,44% | -1,18% | +0,59% | FEEDBACK RAPIDO |
| BTC | 3g | 10 | +40,00% | -0,44% | -2,45% | +1,64% | FEEDBACK RAPIDO |
| BTC | 7g | 10 | +30,00% | -1,89% | -3,68% | +1,86% | FEEDBACK RAPIDO |
| BTC | 14g | 10 | +30,00% | -1,16% | -4,52% | +2,54% | FEEDBACK RAPIDO |
| BTC | 30g | 8 | +50,00% | +1,78% | -5,80% | +6,08% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 5 | +100,00% | +22,07% | -4,32% | +25,38% | FEEDBACK RAPIDO |
| DOGE | 1g | 13 | +46,15% | +0,84% | -0,72% | +2,33% | FEEDBACK RAPIDO |
| DOGE | 3g | 13 | +30,77% | +0,78% | -3,69% | +5,57% | FEEDBACK RAPIDO |
| DOGE | 7g | 12 | +41,67% | -0,39% | -5,05% | +8,59% | FEEDBACK RAPIDO |
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

**DOGE** — DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 80.521 $ | +0.0086% | -4.35% | 1.25 | Misto | 1/5 |
| SOL | 101,76 $ | -0.0049% | +9.79% | 1.61 | Leva alta, direzione mista | 3/5 |
| DOGE | 0.07697 $ | -0.0064% | -0.02% | 3.32 | Misto | 1/5 |

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

Generato: 2026-10-25 06:33 UTC

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily               | Stato D       | Weekly                     | Stato W       | Lettura weekly                                                                                              |   Peso |
|:--------|:--------------------|:--------------|:---------------------------|:--------------|:------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish      | IN_FORMAZIONE | Misto / nessuna divergenza | CONTESTO      | Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.                        |      0 |
| SOL     | Hidden bullish      | IN_FORMAZIONE | Hidden bullish             | IN_FORMAZIONE | Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0. |      0 |
| DOGE    | Conferma ribassista | CONTESTO      | Conferma ribassista        | CONTESTO      | Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.   |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                       | Stato         | Prezzo / RSI      | Pivot confrontati                                                 | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:---------------------------|:--------------|:------------------|:------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish             | IN_FORMAZIONE | 80.519 $ / 43,30  | 2026-10-15 79.736 $ / RSI 48,70 → 2026-10-23 80.422 $ / RSI 45,21 | n/a                 | n/a              |      0 |
| BTC     | 1W   | Misto / nessuna divergenza | CONTESTO      | 80.519 $ / 55,14  | n/a                                                               | +4,79%              | 0,52             |      0 |
| SOL     | 1D   | Hidden bullish             | IN_FORMAZIONE | 101,80 $ / 36,82  | 2026-10-18 100,51 $ / RSI 38,93 → 2026-10-25 101,68 $ / RSI 36,82 | n/a                 | n/a              |      0 |
| SOL     | 1W   | Hidden bullish             | IN_FORMAZIONE | 101,80 $ / 52,09  | 2026-09-20 96,23 $ / RSI 61,01 → 2026-10-18 100,51 $ / RSI 53,42  | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Conferma ribassista        | CONTESTO      | 0.07702 $ / 33,87 | n/a                                                               | -10,14%             | -8,09            |      0 |
| DOGE    | 1W   | Conferma ribassista        | CONTESTO      | 0.07702 $ / 42,48 | n/a                                                               | -6,55%              | -2,37            |      0 |

### BTC

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.

### SOL

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.

### DOGE

- **1D — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.
- **1W — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **10**.
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

Generato: 2026-10-25 06:33 UTC

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

| Asset   | Prezzo   |   Punteggio | Verdetto           | Trend            | Momentum        | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista            | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-------------------|:-----------------|:----------------|:------------------------------------------------------|----------------:|:---------------|:-----------------------------|:---------------------------|:-----------|:-------------|
| BTC | 80.521 $ | -5 | DEBOLE | Trend misto | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | +1 | 0 / NON ATTIVO | Eve and Adam Bottom / MATURO | Doppio massimo / CANDIDATO | 79.736 | 84.249 |
| SOL | 101,76 $ | -2 | NEUTRALE / MISTO | Trend misto | Momentum debole | Compressione / triangolo | 0 | 0 / REJECTION | Doppio minimo / CANDIDATO | Triplo massimo / CANDIDATO | 100,51 | 123,48 |
| DOGE | 0.07697 $ | -8 | RIBASSISTA TECNICO | Trend ribassista | Momentum debole | Volatilità in espansione | -1 | 0 / REJECTION | Doppio minimo / CANDIDATO | Doppio massimo / ATTIVO | 0.07623 | 0.10528 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom                 | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Eve and Adam Bottom — MATURO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 1 |
| SOL | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | INVALIDATO | CANDIDATO | ASSENTE | 0 |
| DOGE | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | ATTIVO | CANDIDATO | Adam and Eve Top — CANDIDATO | -1 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 43.31 | -305.053 | 82.531 | 81.795 | 72.899 | 2,90% | 5,38% | -4,18% | 26,36% |
| SOL | 36.75 | -0.65546 | 107,86 | 109,62 | 88,27 | 3,79% | 8,48% | -16,60% | 37,25% |
| DOGE | 33.8 | -0.00048 | 0.08330 | 0.08752 | 0.08688 | -0,59% | -2,52% | -22,21% | 9,43% |

## Dettaglio asset

### BTC

- Prezzo: **80.521 $**
- Punteggio tecnico: **-5 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend misto** (1)
- Momentum: **Momentum misto** (-1)
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
  - Due minimi simili vicino a 76.248 tra 2026-09-02 e 2026-10-15. Neckline stimata: 87.364. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 87.364; target 98.479; distanza dalla neckline 8,50%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 76.248 dal 2026-09-02 al 2026-10-15. Neckline stimata: 87.364. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 87.364; target 98.479; distanza dalla neckline 8,50%; prezzo sotto neckline.
- Eve and Adam Bottom: **MATURO** (+1)
  - Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (34 giorni fa). Stato: MATURO. Target teorico: 89.580; progresso corrente: -23,79%. Relazione prezzo/neckline: sotto neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (34g); progresso -23,79%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 84.249 tra 2026-09-03 e 2026-10-12. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 74.945; target 65.640; distanza dalla neckline 7,44%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 84.249 dal 2026-08-28 al 2026-10-12. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 74.945; target 65.640; distanza dalla neckline 7,44%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 84.249 dal 2026-09-03 al 2026-10-12. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 74.945. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 74.945; target 65.640; distanza dalla neckline 7,44%; prezzo sopra neckline.

### SOL

- Prezzo: **101,76 $**
- Punteggio tecnico: **-2 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (1)
- Momentum: **Momentum debole** (-2)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 96.23 -> 100.5. Ultimi massimi: 124.6 -> 123.5.
- Divergenza: **Divergenza rialzista nascosta RSI** (1)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 58,27%. Fase non abbastanza chiara.
- Fibonacci automatico: **REJECTION** (0)
  - Swing DOWN 2026-09-27 124,62 -> 2026-10-18 100,51; livello più vicino 23.6% a 106,20; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Triplo massimo (CANDIDATO, 0).
- Supporto più vicino: **100,51**
- Resistenza più vicina: **123,48**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 97,45 tra 2026-09-02 e 2026-10-18. Neckline stimata: 124,62. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 124,62; target 151,78; distanza dalla neckline 22,46%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 96,23 dal 2026-09-02 al 2026-10-18. Neckline stimata: 124,62. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 124,62; target 153,01; distanza dalla neckline 22,46%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 97,45 dal 2026-09-02 al 2026-10-18. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 124,62. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 124,62; target 151,78; distanza dalla neckline 22,46%; prezzo sotto neckline.
- Doppio massimo: **INVALIDATO** (0)
  - Due massimi simili vicino a 110,04 tra 2026-08-27 e 2026-09-06. Neckline ribassista stimata: 97,45. Breakout neckline: 2026-09-15 (40 giorni fa). Stato: INVALIDATO. Target teorico: 84,86; progresso corrente: -34,23%. Relazione prezzo/neckline: sopra neckline.
  - neckline 97,45; target 84,86; breakout 2026-09-15 (40g); progresso -34,23%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 77 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 43,94%; prezzo sopra neckline.
- Adam/Eve Top: **ASSENTE** (0)

### DOGE

- Prezzo: **0.07697 $**
- Punteggio tecnico: **-8 / 12**
- Verdetto: **RIBASSISTA TECNICO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-2)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 0.08122 -> 0.07623. Ultimi massimi: 0.09421 -> 0.1053.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 24,12%. Fase non abbastanza chiara.
- Fibonacci automatico: **REJECTION** (0)
  - Swing DOWN 2026-09-22 0.10528 -> 2026-10-18 0.07623; livello più vicino 23.6% a 0.08308; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **-1**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (ATTIVO, -1).
- Supporto più vicino: **0.07623**
- Resistenza più vicina: **0.10528**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.08028 tra 2026-09-02 e 2026-10-08. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 17 giorni.
  - neckline 0.10528; target 0.13028; distanza dalla neckline 36,78%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 0.07841 dal 2026-09-02 al 2026-10-08. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 17 giorni.
  - neckline 0.10528; target 0.13216; distanza dalla neckline 36,78%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.08028 dal 2026-09-02 al 2026-10-08. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.10528. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 17 giorni.
  - neckline 0.10528; target 0.13028; distanza dalla neckline 36,78%; prezzo sotto neckline.
- Doppio massimo: **ATTIVO** (-1)
  - Due massimi simili vicino a 0.10528 tra 2026-08-22 e 2026-09-22. Neckline ribassista stimata: 0.07841. Breakout neckline: 2026-10-25 (0 giorni fa). Stato: ATTIVO. Target teorico: 0.05153; progresso corrente: 5,34%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07841; target 0.05153; breakout 2026-10-25 (0g); progresso 5,34%; prezzo sotto neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 75 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 13,24%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07380 dal 2026-07-26 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 75 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 13,24%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-10-12 | 77.995 | 74.126 | 70.998 | 67.871 | 63.419 | 23.6% / 77.995 | NON ATTIVO | nessuna confluenza indipendente | 0 |
| SOL | DOWN 2026-09-27 -> 2026-10-18 | 106,20 | 109,72 | 112,56 | 115,41 | 119,46 | 23.6% / 106,20 | REJECTION | nessuna confluenza indipendente | 0 |
| DOGE | DOWN 2026-09-22 -> 2026-10-18 | 0.08308 | 0.08733 | 0.09075 | 0.09418 | 0.09906 | 23.6% / 0.08308 | REJECTION | nessuna confluenza indipendente | 0 |

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

- **BTC**: 51/30 previsioni controllate su 107 fatte. Stato: **ATTIVA**.
- **SOL**: 51/30 previsioni controllate su 107 fatte. Stato: **ATTIVA**.
- **DOGE**: 51/30 previsioni controllate su 107 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 107 | 51 | 30/30 [██████████] | 56 | ATTIVA | 2026-10-26 / tra 1 giorno |
| SOL | 107 | 51 | 30/30 [██████████] | 56 | ATTIVA | 2026-10-26 / tra 1 giorno |
| DOGE | 107 | 51 | 30/30 [██████████] | 56 | ATTIVA | 2026-10-26 / tra 1 giorno |

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

Generato: 2026-10-25 06:34 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- Calibrazione rischio in quarantena; moduli sospesi esclusi dalla verifica prezzi correnti. Consultare lab_reduction_status.md.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo         | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:--------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price | OK      | 80.521 $          | 80.521 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price | OK      | 0.07697 $         | 0.07697 $       | -0,0000%     |
| Scanner                 | SOL     | current_price | OK      | 101,76 $          | 101,76 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price | OK      | 80.521 $          | 80.521 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price | OK      | 101,76 $          | 101,76 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price | OK      | 0.07697 $         | 0.07697 $       | -0,0000%     |
| Technical Structure     | BTC     | price         | OK      | 80.521 $          | 80.521 $        | +0,0000%     |
| Technical Structure     | SOL     | price         | OK      | 101,76 $          | 101,76 $        | +0,0000%     |
| Technical Structure     | DOGE    | price         | OK      | 0.07697 $         | 0.07697 $       | -0,0000%     |
| Classic Technical       | BTC     | price         | OK      | 80.521 $          | 80.521 $        | +0,0000%     |
| Classic Technical       | SOL     | price         | OK      | 101,76 $          | 101,76 $        | +0,0000%     |
| Classic Technical       | DOGE    | price         | OK      | 0.07697 $         | 0.07697 $       | -0,0000%     |
| Classic Visual          | BTC     | price         | OK      | 80.521 $          | 80.521 $        | +0,0000%     |
| Classic Visual          | SOL     | price         | OK      | 101,76 $          | 101,76 $        | +0,0000%     |
| Classic Visual          | DOGE    | price         | OK      | 0.07697 $         | 0.07697 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price         | OK      | 80.521 $          | 80.554 $        | +0,0412%     |
| Exchange Microstructure | SOL     | price         | OK      | 101,76 $          | 101,76 $        | -0,0030%     |
| Exchange Microstructure | DOGE    | price         | OK      | 0.07697 $         | 0.07694 $       | -0,0390%     |

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
