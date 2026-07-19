# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-19 05:14 UTC

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

Segnali totali salvati: **33**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-19 | BTC | 64.750,69 | +3 | +1 | +1 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-19 | DOGE | 0.07243 | -6 | -3 | -2 | -2 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-19 | SOL | 76,04 | -4 | -1 | -1 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-18 | BTC | 63.883,71 | 0 | +1 | +1 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-18 | DOGE | 0.07234 | -6 | -3 | -2 | -2 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-18 | SOL | 74,93 | -3 | 0 | -1 | +1 | -2 | -1 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-07-17 | BTC | 63.638,61 | -1 | +1 | +1 | +3 | -2 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-07-17 | DOGE | 0.07218 | -6 | -3 | -2 | -3 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-17 | SOL | 75,11 | -5 | -1 | -1 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-16 | BTC | 64.033,70 | -1 | +1 | +1 | +3 | -1 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-07-16 | DOGE | 0.07304 | -6 | -3 | -2 | -3 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-16 | SOL | 76,00 | -6 | -1 | -1 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 11 | 10 | 9 | 8 | 6 | 4 | 1 | 0 | 0 | 0 | 0 | 0 |
| SOL | 11 | 10 | 9 | 8 | 6 | 4 | 1 | 0 | 0 | 0 | 0 | 0 |
| DOGE | 11 | 10 | 9 | 8 | 6 | 4 | 1 | 0 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-10 | 10g | 2026-07-20 | domani |
| SOL | 2026-07-10 | 10g | 2026-07-20 | domani |
| DOGE | 2026-07-10 | 10g | 2026-07-20 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 9 | 33,33% | -0,02% | +0,03% | FEEDBACK RAPIDO |
| BTC | 2g | 9 | 44,44% | +0,28% | -0,05% | FEEDBACK RAPIDO |
| BTC | 3g | 8 | 50,00% | +0,23% | -0,05% | FEEDBACK RAPIDO |
| BTC | 5g | 6 | 50,00% | +0,83% | +0,83% | FEEDBACK RAPIDO |
| BTC | 7g | 4 | 50,00% | +0,53% | +0,53% | FEEDBACK RAPIDO |
| BTC | 10g | 1 | 100,00% | +2,40% | +2,40% | FEEDBACK RAPIDO |
| BTC | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 9 | 44,44% | -0,25% | -0,60% | FEEDBACK RAPIDO |
| SOL | 2g | 8 | 25,00% | -0,56% | -0,76% | FEEDBACK RAPIDO |
| SOL | 3g | 7 | 14,29% | -1,12% | -1,47% | FEEDBACK RAPIDO |
| SOL | 5g | 5 | 40,00% | -1,69% | -0,82% | FEEDBACK RAPIDO |
| SOL | 7g | 3 | 33,33% | -2,28% | -1,90% | FEEDBACK RAPIDO |
| SOL | 10g | 1 | 0,00% | -2,54% | -2,54% | FEEDBACK RAPIDO |
| SOL | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 10 | 60,00% | -0,20% | +0,20% | FEEDBACK RAPIDO |
| DOGE | 2g | 9 | 55,56% | -0,28% | +0,28% | FEEDBACK RAPIDO |
| DOGE | 3g | 8 | 62,50% | -0,64% | +0,64% | FEEDBACK RAPIDO |
| DOGE | 5g | 6 | 50,00% | -0,42% | +0,42% | FEEDBACK RAPIDO |
| DOGE | 7g | 4 | 75,00% | -1,21% | +1,21% | FEEDBACK RAPIDO |
| DOGE | 10g | 1 | 100,00% | -0,58% | +0,58% | FEEDBACK RAPIDO |
| DOGE | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 9 | 33,33% | -0,02% | +0,03% | -0,18% | +0,69% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 10 | 40,00% | +0,11% | +0,11% | -0,05% | +0,77% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 10 | 40,00% | +0,11% | +0,11% | -0,05% | +0,77% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 10 | 40,00% | +0,11% | +0,11% | -0,05% | +0,77% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 9 | 33,33% | +0,10% | -0,71% | -0,08% | +0,81% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 9 | 44,44% | +0,28% | -0,05% | -0,37% | +1,42% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 9 | 44,44% | +0,28% | +0,28% | -0,37% | +1,42% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 9 | 44,44% | +0,28% | +0,28% | -0,37% | +1,42% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 9 | 44,44% | +0,28% | +0,28% | -0,37% | +1,42% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 8 | 37,50% | +0,33% | -0,47% | -0,38% | +1,48% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 8 | 50,00% | +0,23% | -0,05% | -1,50% | +2,10% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 8 | 62,50% | +0,23% | +0,23% | -1,50% | +2,10% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 8 | 62,50% | +0,23% | +0,23% | -1,50% | +2,10% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 8 | 62,50% | +0,23% | +0,23% | -1,50% | +2,10% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 7 | 42,86% | +0,51% | +0,10% | -1,43% | +2,27% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 6 | 50,00% | +0,83% | +0,83% | -2,22% | +3,06% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 6 | 50,00% | +0,83% | +0,83% | -2,22% | +3,06% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 6 | 50,00% | +0,83% | +0,83% | -2,22% | +3,06% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | +0,83% | +0,83% | -2,22% | +3,06% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 5 | 60,00% | +0,79% | -0,18% | -2,01% | +3,26% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 4 | 50,00% | +0,53% | +0,53% | -3,09% | +2,78% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 4 | 50,00% | +0,53% | +0,53% | -3,09% | +2,78% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 4 | 50,00% | +0,53% | +0,53% | -3,09% | +2,78% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 4 | 50,00% | +0,53% | +0,53% | -3,09% | +2,78% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 3 | 66,67% | +0,83% | +0,15% | -3,03% | +2,84% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 1 | 100,00% | +2,40% | +2,40% | -2,32% | +3,59% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | +2,40% | +2,40% | -2,32% | +3,59% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | +2,40% | +2,40% | -2,32% | +3,59% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 1 | 100,00% | +2,40% | +2,40% | -2,32% | +3,59% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 1 | 0,00% | +2,40% | -2,40% | -2,32% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 10 | 60,00% | -0,20% | +0,20% | -0,49% | +0,55% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 10 | 60,00% | -0,20% | +0,20% | -0,49% | +0,55% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 10 | 60,00% | -0,20% | +0,20% | -0,49% | +0,55% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | -0,20% | +0,20% | -0,49% | +0,55% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 10 | 60,00% | -0,20% | +0,20% | -0,49% | +0,55% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 9 | 55,56% | -0,09% | +0,09% | -0,35% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 9 | 55,56% | -0,28% | +0,28% | -1,02% | +1,31% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 9 | 55,56% | -0,28% | +0,28% | -1,02% | +1,31% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 9 | 55,56% | -0,28% | +0,28% | -1,02% | +1,31% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 9 | 55,56% | -0,28% | +0,28% | -1,02% | +1,31% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 9 | 55,56% | -0,28% | +0,28% | -1,02% | +1,31% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 8 | 50,00% | -0,02% | +0,02% | -0,87% | +1,74% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 8 | 62,50% | -0,64% | +0,64% | -1,99% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 8 | 62,50% | -0,64% | +0,64% | -1,99% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 8 | 62,50% | -0,64% | +0,64% | -1,99% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 8 | 62,50% | -0,64% | +0,64% | -1,99% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 8 | 62,50% | -0,64% | +0,64% | -1,99% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 7 | 57,14% | -0,42% | +0,42% | -1,93% | +2,46% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 6 | 50,00% | -0,42% | +0,42% | -2,60% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 6 | 50,00% | -0,42% | +0,42% | -2,60% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 6 | 50,00% | -0,42% | +0,42% | -2,60% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | -0,42% | +0,42% | -2,60% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 6 | 50,00% | -0,42% | +0,42% | -2,60% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 6 | 50,00% | -0,42% | +0,42% | -2,60% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 4 | 75,00% | -1,21% | +1,21% | -3,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 4 | 75,00% | -1,21% | +1,21% | -3,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 4 | 75,00% | -1,21% | +1,21% | -3,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 4 | 75,00% | -1,21% | +1,21% | -3,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 4 | 75,00% | -1,21% | +1,21% | -3,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 4 | 75,00% | -1,21% | +1,21% | -3,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 1 | 100,00% | -0,58% | +0,58% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | -0,58% | +0,58% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | -0,58% | +0,58% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 1 | 100,00% | -0,58% | +0,58% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 1 | 100,00% | -0,58% | +0,58% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 1 | 100,00% | -0,58% | +0,58% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 9 | 44,44% | -0,25% | -0,60% | -0,67% | +0,60% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 7 | 71,43% | -0,78% | +0,20% | -1,00% | +0,04% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 10 | 60,00% | -0,21% | -0,19% | -0,59% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -0,12% | +0,46% | -0,69% | +0,86% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 10 | 50,00% | -0,21% | -0,15% | -0,59% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 3 | 66,67% | +0,02% | -0,02% | -0,17% | +0,43% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 8 | 25,00% | -0,56% | -0,76% | -1,41% | +1,02% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 7 | 57,14% | -0,81% | -0,10% | -1,71% | +0,57% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 9 | 55,56% | -0,67% | -0,03% | -1,51% | +1,05% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 6 | 33,33% | -0,72% | -0,56% | -1,73% | +1,23% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 9 | 22,22% | -0,67% | -0,60% | -1,51% | +1,05% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 2 | 50,00% | -0,08% | +0,08% | -0,45% | +0,39% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 7 | 14,29% | -1,12% | -1,47% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 6 | 50,00% | -1,02% | -0,11% | -2,92% | +1,58% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 8 | 50,00% | -1,19% | +0,35% | -2,73% | +1,88% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 6 | 33,33% | -1,31% | -1,62% | -2,63% | +2,21% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 8 | 37,50% | -1,19% | -0,30% | -2,73% | +1,88% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 1 | 0,00% | +0,05% | -0,05% | -3,42% | +0,47% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 5 | 40,00% | -1,69% | -0,82% | -3,41% | +3,01% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | -1,95% | +1,95% | -3,73% | +2,42% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 6 | 83,33% | -1,44% | +1,44% | -3,60% | +2,72% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 5 | 60,00% | -1,69% | -0,22% | -3,41% | +3,01% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 6 | 16,67% | -1,44% | -1,31% | -3,60% | +2,72% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 3 | 33,33% | -2,28% | -1,90% | -4,55% | +2,16% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | -2,17% | +2,17% | -4,51% | +2,20% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | -2,55% | +2,55% | -4,55% | +2,00% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 3 | 33,33% | -2,28% | -1,90% | -4,55% | +2,16% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 4 | 0,00% | -2,55% | -2,55% | -4,55% | +2,00% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | -2,54% | +2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | -2,54% | +2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |

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
