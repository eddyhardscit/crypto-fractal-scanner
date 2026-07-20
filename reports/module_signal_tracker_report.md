# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-20 05:14 UTC

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

Segnali totali salvati: **36**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-20 | BTC | 64.190,23 | +2 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-20 | DOGE | 0.07180 | -7 | -3 | -2 | -2 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-20 | SOL | 76,01 | -4 | 0 | 0 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-19 | BTC | 64.750,69 | +3 | +1 | +1 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-19 | DOGE | 0.07243 | -6 | -3 | -2 | -2 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-19 | SOL | 76,04 | -4 | -1 | -1 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-18 | BTC | 63.883,71 | 0 | +1 | +1 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-18 | DOGE | 0.07234 | -6 | -3 | -2 | -2 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-18 | SOL | 74,93 | -3 | 0 | -1 | +1 | -2 | -1 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-07-17 | BTC | 63.638,61 | -1 | +1 | +1 | +3 | -2 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-07-17 | DOGE | 0.07218 | -6 | -3 | -2 | -3 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-17 | SOL | 75,11 | -5 | -1 | -1 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 12 | 11 | 10 | 9 | 7 | 5 | 2 | 0 | 0 | 0 | 0 | 0 |
| SOL | 12 | 11 | 10 | 9 | 7 | 5 | 2 | 0 | 0 | 0 | 0 | 0 |
| DOGE | 12 | 11 | 10 | 9 | 7 | 5 | 2 | 0 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-11 | 10g | 2026-07-21 | domani |
| SOL | 2026-07-11 | 10g | 2026-07-21 | domani |
| DOGE | 2026-07-11 | 10g | 2026-07-21 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 10 | 30,00% | -0,11% | -0,06% | FEEDBACK RAPIDO |
| BTC | 2g | 9 | 44,44% | +0,28% | -0,05% | FEEDBACK RAPIDO |
| BTC | 3g | 9 | 44,44% | +0,30% | -0,14% | FEEDBACK RAPIDO |
| BTC | 5g | 7 | 42,86% | +0,64% | +0,64% | FEEDBACK RAPIDO |
| BTC | 7g | 5 | 60,00% | +0,88% | +0,88% | FEEDBACK RAPIDO |
| BTC | 10g | 2 | 100,00% | +1,45% | +1,45% | FEEDBACK RAPIDO |
| BTC | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 10 | 50,00% | -0,23% | -0,53% | FEEDBACK RAPIDO |
| SOL | 2g | 9 | 22,22% | -0,34% | -0,83% | FEEDBACK RAPIDO |
| SOL | 3g | 8 | 12,50% | -0,83% | -1,43% | FEEDBACK RAPIDO |
| SOL | 5g | 6 | 33,33% | -1,74% | -1,01% | FEEDBACK RAPIDO |
| SOL | 7g | 4 | 50,00% | -1,83% | -1,31% | FEEDBACK RAPIDO |
| SOL | 10g | 1 | 0,00% | -2,54% | -2,54% | FEEDBACK RAPIDO |
| SOL | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 11 | 63,64% | -0,26% | +0,26% | FEEDBACK RAPIDO |
| DOGE | 2g | 10 | 60,00% | -0,33% | +0,33% | FEEDBACK RAPIDO |
| DOGE | 3g | 9 | 66,67% | -0,62% | +0,62% | FEEDBACK RAPIDO |
| DOGE | 5g | 7 | 57,14% | -0,77% | +0,77% | FEEDBACK RAPIDO |
| DOGE | 7g | 5 | 80,00% | -1,08% | +1,08% | FEEDBACK RAPIDO |
| DOGE | 10g | 2 | 100,00% | -1,70% | +1,70% | FEEDBACK RAPIDO |
| DOGE | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 10 | 30,00% | -0,11% | -0,06% | -0,26% | +0,65% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 11 | 36,36% | +0,03% | +0,03% | -0,14% | +0,74% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 11 | 36,36% | +0,03% | +0,03% | -0,14% | +0,74% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 10 | 40,00% | +0,11% | +0,11% | -0,05% | +0,77% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 10 | 30,00% | +0,00% | -0,73% | -0,17% | +0,77% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 9 | 44,44% | +0,28% | -0,05% | -0,37% | +1,42% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 10 | 50,00% | +0,30% | +0,30% | -0,30% | +1,45% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 10 | 50,00% | +0,30% | +0,30% | -0,30% | +1,45% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 10 | 50,00% | +0,30% | +0,30% | -0,30% | +1,45% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 9 | 33,33% | +0,34% | -0,47% | -0,30% | +1,51% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 9 | 44,44% | +0,30% | -0,14% | -1,30% | +2,10% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 9 | 66,67% | +0,30% | +0,30% | -1,30% | +2,10% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 9 | 66,67% | +0,30% | +0,30% | -1,30% | +2,10% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 9 | 66,67% | +0,30% | +0,30% | -1,30% | +2,10% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 8 | 37,50% | +0,56% | -0,02% | -1,21% | +2,25% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 7 | 42,86% | +0,64% | +0,64% | -2,36% | +2,73% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 7 | 42,86% | +0,64% | +0,64% | -2,36% | +2,73% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 7 | 42,86% | +0,64% | +0,64% | -2,36% | +2,73% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 7 | 42,86% | +0,64% | +0,64% | -2,36% | +2,73% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 6 | 50,00% | +0,57% | -0,24% | -2,20% | +2,84% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 5 | 60,00% | +0,88% | +0,88% | -2,65% | +3,10% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 5 | 60,00% | +0,88% | +0,88% | -2,65% | +3,10% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 5 | 60,00% | +0,88% | +0,88% | -2,65% | +3,10% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 5 | 60,00% | +0,88% | +0,88% | -2,65% | +3,10% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 4 | 75,00% | +1,19% | +0,68% | -2,49% | +3,23% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 2 | 100,00% | +1,45% | +1,45% | -2,80% | +3,08% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | +1,45% | +1,45% | -2,80% | +3,08% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | +1,45% | +1,45% | -2,80% | +3,08% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 2 | 100,00% | +1,45% | +1,45% | -2,80% | +3,08% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 1 | 0,00% | +2,40% | -2,40% | -2,32% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 11 | 63,64% | -0,26% | +0,26% | -0,51% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 11 | 63,64% | -0,26% | +0,26% | -0,51% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 11 | 63,64% | -0,26% | +0,26% | -0,51% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 11 | 63,64% | -0,26% | +0,26% | -0,51% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 11 | 63,64% | -0,26% | +0,26% | -0,51% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 10 | 60,00% | -0,17% | +0,17% | -0,39% | +0,57% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 10 | 60,00% | -0,33% | +0,33% | -0,98% | +1,26% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 10 | 60,00% | -0,33% | +0,33% | -0,98% | +1,26% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 10 | 60,00% | -0,33% | +0,33% | -0,98% | +1,26% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | -0,33% | +0,33% | -0,98% | +1,26% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 10 | 60,00% | -0,33% | +0,33% | -0,98% | +1,26% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 9 | 55,56% | -0,10% | +0,10% | -0,84% | +1,63% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 9 | 66,67% | -0,62% | +0,62% | -1,81% | +2,09% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 9 | 66,67% | -0,62% | +0,62% | -1,81% | +2,09% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 9 | 66,67% | -0,62% | +0,62% | -1,81% | +2,09% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 9 | 66,67% | -0,62% | +0,62% | -1,81% | +2,09% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 9 | 66,67% | -0,62% | +0,62% | -1,81% | +2,09% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 8 | 62,50% | -0,43% | +0,43% | -1,74% | +2,28% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 7 | 57,14% | -0,77% | +0,77% | -2,79% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 7 | 57,14% | -0,77% | +0,77% | -2,79% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 7 | 57,14% | -0,77% | +0,77% | -2,79% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -0,77% | +0,77% | -2,79% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 7 | 57,14% | -0,77% | +0,77% | -2,79% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 6 | 50,00% | -0,42% | +0,42% | -2,60% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 5 | 80,00% | -1,08% | +1,08% | -2,94% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 5 | 80,00% | -1,08% | +1,08% | -2,94% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 5 | 80,00% | -1,08% | +1,08% | -2,94% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 5 | 80,00% | -1,08% | +1,08% | -2,94% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 5 | 80,00% | -1,08% | +1,08% | -2,94% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 5 | 80,00% | -1,08% | +1,08% | -2,94% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 2 | 100,00% | -1,70% | +1,70% | -3,25% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -1,70% | +1,70% | -3,25% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | -1,70% | +1,70% | -3,25% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 2 | 100,00% | -1,70% | +1,70% | -3,25% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 2 | 100,00% | -1,70% | +1,70% | -3,25% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 2 | 100,00% | -1,70% | +1,70% | -3,25% | +2,87% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 10 | 50,00% | -0,23% | -0,53% | -0,60% | +0,67% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 8 | 75,00% | -0,68% | +0,18% | -0,88% | +0,20% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 11 | 63,64% | -0,20% | -0,17% | -0,54% | +0,66% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -0,12% | +0,46% | -0,69% | +0,86% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 11 | 54,55% | -0,20% | -0,13% | -0,54% | +0,66% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 4 | 75,00% | +0,01% | -0,01% | -0,13% | +0,66% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 9 | 22,22% | -0,34% | -0,83% | -1,09% | +1,22% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 7 | 57,14% | -0,81% | -0,10% | -1,71% | +0,57% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 10 | 50,00% | -0,46% | -0,17% | -1,21% | +1,23% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 7 | 42,86% | -0,41% | -0,28% | -1,27% | +1,46% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 10 | 20,00% | -0,46% | -0,68% | -1,21% | +1,23% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 3 | 33,33% | +0,42% | -0,42% | +0,19% | +1,21% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 8 | 12,50% | -0,83% | -1,43% | -2,49% | +2,04% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 7 | 42,86% | -0,70% | -0,27% | -2,61% | +1,72% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 9 | 44,44% | -0,93% | +0,17% | -2,51% | +1,96% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 6 | 33,33% | -1,31% | -1,62% | -2,63% | +2,21% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 9 | 33,33% | -0,93% | -0,40% | -2,51% | +1,96% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 2 | 0,00% | +0,63% | -0,63% | -2,09% | +1,54% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 6 | 33,33% | -1,74% | -1,01% | -3,74% | +2,48% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 5 | 80,00% | -1,96% | +1,16% | -4,05% | +1,91% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 7 | 71,43% | -1,52% | +0,95% | -3,86% | +2,31% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | -1,74% | -0,52% | -3,74% | +2,48% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 7 | 28,57% | -1,52% | -0,83% | -3,86% | +2,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 4 | 50,00% | -1,83% | -1,31% | -4,38% | +2,44% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | -1,74% | +1,74% | -4,35% | +2,47% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 5 | 100,00% | -2,13% | +2,13% | -4,42% | +2,26% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 4 | 50,00% | -1,83% | -1,31% | -4,38% | +2,44% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 5 | 20,00% | -2,13% | -1,94% | -4,42% | +2,26% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -2,36% | +2,36% | -5,73% | +1,74% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | -2,36% | +2,36% | -5,73% | +1,74% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 2 | 0,00% | -2,36% | -2,36% | -5,73% | +1,74% | FEEDBACK RAPIDO |
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
