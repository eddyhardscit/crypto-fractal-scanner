# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-18 05:14 UTC

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

Segnali totali salvati: **30**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-18 | BTC | 63.883,71 | 0 | +1 | +1 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-18 | DOGE | 0.07234 | -6 | -3 | -2 | -2 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-18 | SOL | 74,93 | -3 | 0 | -1 | +1 | -2 | -1 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-07-17 | BTC | 63.638,61 | -1 | +1 | +1 | +3 | -2 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-07-17 | DOGE | 0.07218 | -6 | -3 | -2 | -3 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-17 | SOL | 75,11 | -5 | -1 | -1 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-16 | BTC | 64.033,70 | -1 | +1 | +1 | +3 | -1 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-07-16 | DOGE | 0.07304 | -6 | -3 | -2 | -3 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-16 | SOL | 76,00 | -6 | -1 | -1 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-15 | BTC | 64.529,99 | +5 | +3 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-15 | DOGE | 0.07394 | -5 | -4 | -3 | -3 | -1 | 0 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-15 | SOL | 77,56 | +2 | +2 | +1 | +2 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 10 | 9 | 8 | 7 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| SOL | 10 | 9 | 8 | 7 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOGE | 10 | 9 | 8 | 7 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-09 | 10g | 2026-07-19 | domani |
| SOL | 2026-07-09 | 10g | 2026-07-19 | domani |
| DOGE | 2026-07-09 | 10g | 2026-07-19 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 9 | 33,33% | -0,02% | +0,03% | FEEDBACK RAPIDO |
| BTC | 2g | 8 | 50,00% | +0,10% | +0,16% | FEEDBACK RAPIDO |
| BTC | 3g | 7 | 57,14% | +0,11% | +0,11% | FEEDBACK RAPIDO |
| BTC | 5g | 5 | 40,00% | +0,29% | +0,29% | FEEDBACK RAPIDO |
| BTC | 7g | 3 | 33,33% | +0,22% | +0,22% | FEEDBACK RAPIDO |
| BTC | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 8 | 50,00% | -0,47% | -0,49% | FEEDBACK RAPIDO |
| SOL | 2g | 7 | 28,57% | -0,82% | -0,69% | FEEDBACK RAPIDO |
| SOL | 3g | 6 | 16,67% | -1,31% | -1,70% | FEEDBACK RAPIDO |
| SOL | 5g | 4 | 50,00% | -2,49% | -0,65% | FEEDBACK RAPIDO |
| SOL | 7g | 2 | 0,00% | -3,14% | -3,14% | FEEDBACK RAPIDO |
| SOL | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 9 | 66,67% | -0,24% | +0,24% | FEEDBACK RAPIDO |
| DOGE | 2g | 8 | 62,50% | -0,36% | +0,36% | FEEDBACK RAPIDO |
| DOGE | 3g | 7 | 57,14% | -0,61% | +0,61% | FEEDBACK RAPIDO |
| DOGE | 5g | 5 | 60,00% | -0,61% | +0,61% | FEEDBACK RAPIDO |
| DOGE | 7g | 3 | 66,67% | -1,43% | +1,43% | FEEDBACK RAPIDO |
| DOGE | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 9 | 33,33% | -0,02% | +0,03% | -0,18% | +0,69% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 9 | 33,33% | -0,02% | -0,02% | -0,18% | +0,69% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 9 | 33,33% | -0,02% | -0,02% | -0,18% | +0,69% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 9 | 33,33% | -0,02% | -0,02% | -0,18% | +0,69% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 8 | 37,50% | -0,06% | -0,63% | -0,23% | +0,72% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 8 | 50,00% | +0,10% | +0,16% | -0,61% | +1,35% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 8 | 37,50% | +0,10% | +0,10% | -0,61% | +1,35% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 8 | 37,50% | +0,10% | +0,10% | -0,61% | +1,35% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 8 | 37,50% | +0,10% | +0,10% | -0,61% | +1,35% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 7 | 42,86% | +0,12% | -0,28% | -0,64% | +1,42% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 7 | 57,14% | +0,11% | +0,11% | -1,37% | +2,22% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 7 | 57,14% | +0,11% | +0,11% | -1,37% | +2,22% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 7 | 57,14% | +0,11% | +0,11% | -1,37% | +2,22% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | +0,11% | +0,11% | -1,37% | +2,22% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 6 | 50,00% | +0,41% | +0,30% | -1,26% | +2,43% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 5 | 40,00% | +0,29% | +0,29% | -2,65% | +2,73% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 5 | 40,00% | +0,29% | +0,29% | -2,65% | +2,73% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 5 | 40,00% | +0,29% | +0,29% | -2,65% | +2,73% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 5 | 40,00% | +0,29% | +0,29% | -2,65% | +2,73% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 4 | 75,00% | +0,10% | +0,65% | -2,49% | +2,89% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 3 | 33,33% | +0,22% | +0,22% | -3,05% | +2,82% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 3 | 33,33% | +0,22% | +0,22% | -3,05% | +2,82% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 3 | 33,33% | +0,22% | +0,22% | -3,05% | +2,82% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 3 | 33,33% | +0,22% | +0,22% | -3,05% | +2,82% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 2 | 50,00% | +0,51% | -0,51% | -2,93% | +2,94% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 9 | 66,67% | -0,24% | +0,24% | -0,53% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 9 | 66,67% | -0,24% | +0,24% | -0,53% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 9 | 66,67% | -0,24% | +0,24% | -0,53% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 9 | 66,67% | -0,24% | +0,24% | -0,53% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 9 | 66,67% | -0,24% | +0,24% | -0,53% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 8 | 62,50% | -0,12% | +0,12% | -0,38% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 8 | 62,50% | -0,36% | +0,36% | -1,16% | +1,38% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 8 | 62,50% | -0,36% | +0,36% | -1,16% | +1,38% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 8 | 62,50% | -0,36% | +0,36% | -1,16% | +1,38% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 8 | 62,50% | -0,36% | +0,36% | -1,16% | +1,38% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 8 | 62,50% | -0,36% | +0,36% | -1,16% | +1,38% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 7 | 57,14% | -0,07% | +0,07% | -1,01% | +1,88% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 7 | 57,14% | -0,61% | +0,61% | -1,89% | +2,57% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 7 | 57,14% | -0,61% | +0,61% | -1,89% | +2,57% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 7 | 57,14% | -0,61% | +0,61% | -1,89% | +2,57% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -0,61% | +0,61% | -1,89% | +2,57% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 7 | 57,14% | -0,61% | +0,61% | -1,89% | +2,57% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 6 | 50,00% | -0,35% | +0,35% | -1,80% | +2,92% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 5 | 60,00% | -0,61% | +0,61% | -2,85% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 5 | 60,00% | -0,61% | +0,61% | -2,85% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 5 | 60,00% | -0,61% | +0,61% | -2,85% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 5 | 60,00% | -0,61% | +0,61% | -2,85% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 5 | 60,00% | -0,61% | +0,61% | -2,85% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 5 | 60,00% | -0,61% | +0,61% | -2,85% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 3 | 66,67% | -1,43% | +1,43% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 3 | 66,67% | -1,43% | +1,43% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 3 | 66,67% | -1,43% | +1,43% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 3 | 66,67% | -1,43% | +1,43% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 3 | 66,67% | -1,43% | +1,43% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 3 | 66,67% | -1,43% | +1,43% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 8 | 50,00% | -0,47% | -0,49% | -0,84% | +0,44% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 7 | 71,43% | -0,78% | +0,20% | -1,00% | +0,04% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 9 | 66,67% | -0,40% | -0,05% | -0,73% | +0,44% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | -0,39% | +0,29% | -0,92% | +0,68% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 9 | 55,56% | -0,40% | -0,00% | -0,73% | +0,44% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 2 | 100,00% | -0,71% | +0,71% | -0,59% | -0,30% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 7 | 28,57% | -0,82% | -0,69% | -1,67% | +0,93% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 6 | 66,67% | -1,15% | +0,09% | -2,07% | +0,39% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 8 | 62,50% | -0,91% | +0,12% | -1,75% | +0,97% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 6 | 33,33% | -0,72% | -0,56% | -1,73% | +1,23% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 8 | 25,00% | -0,91% | -0,52% | -1,75% | +0,97% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 1 | 100,00% | -1,41% | +1,41% | -1,33% | -0,87% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 6 | 16,67% | -1,31% | -1,70% | -2,63% | +2,21% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 5 | 60,00% | -1,23% | -0,13% | -2,82% | +1,80% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 7 | 57,14% | -1,37% | +0,40% | -2,63% | +2,08% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 6 | 33,33% | -1,31% | -1,62% | -2,63% | +2,21% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 7 | 42,86% | -1,37% | -0,33% | -2,63% | +2,08% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 4 | 50,00% | -2,49% | -0,65% | -3,76% | +2,44% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | -1,95% | +1,95% | -3,73% | +2,42% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 5 | 100,00% | -2,03% | +2,03% | -3,92% | +2,22% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 4 | 50,00% | -2,49% | -0,65% | -3,76% | +2,44% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 5 | 20,00% | -2,03% | -1,27% | -3,92% | +2,22% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 2 | 0,00% | -3,14% | -3,14% | -4,81% | +1,67% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -2,96% | +2,96% | -4,75% | +1,74% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | -3,20% | +3,20% | -4,73% | +1,62% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 2 | 0,00% | -3,14% | -3,14% | -4,81% | +1,67% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 3 | 0,00% | -3,20% | -3,20% | -4,73% | +1,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |

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
