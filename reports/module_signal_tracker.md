# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-22 05:14 UTC

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

Segnali totali salvati: **42**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-22 | BTC | 66.234,10 | +2 | +2 | +2 | 0 | 0 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-22 | DOGE | 0.07318 | -5 | -2 | -1 | -1 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-22 | SOL | 77,82 | -3 | -1 | -1 | 0 | -1 | -1 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-07-21 | BTC | 65.476,52 | +3 | +2 | +2 | 0 | 0 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-21 | DOGE | 0.07281 | -6 | -3 | -2 | -2 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-21 | SOL | 78,22 | +1 | +2 | +1 | +2 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-20 | BTC | 64.190,23 | +2 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-20 | DOGE | 0.07180 | -7 | -3 | -2 | -2 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-20 | SOL | 76,01 | -4 | 0 | 0 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-19 | BTC | 64.750,69 | +3 | +1 | +1 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-19 | DOGE | 0.07243 | -6 | -3 | -2 | -2 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-19 | SOL | 76,04 | -4 | -1 | -1 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 14 | 13 | 12 | 11 | 9 | 7 | 4 | 0 | 0 | 0 | 0 | 0 |
| SOL | 14 | 13 | 12 | 11 | 9 | 7 | 4 | 0 | 0 | 0 | 0 | 0 |
| DOGE | 14 | 13 | 12 | 11 | 9 | 7 | 4 | 0 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-09 | 14g | 2026-07-23 | domani |
| SOL | 2026-07-09 | 14g | 2026-07-23 | domani |
| DOGE | 2026-07-09 | 14g | 2026-07-23 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 12 | 41,67% | +0,17% | +0,21% | FEEDBACK RAPIDO |
| BTC | 2g | 11 | 54,55% | +0,62% | +0,35% | FEEDBACK RAPIDO |
| BTC | 3g | 10 | 50,00% | +0,50% | +0,11% | FEEDBACK RAPIDO |
| BTC | 5g | 9 | 33,33% | +1,20% | -0,21% | FEEDBACK RAPIDO |
| BTC | 7g | 7 | 71,43% | +1,68% | +1,68% | FEEDBACK RAPIDO |
| BTC | 10g | 4 | 100,00% | +2,23% | +2,23% | FEEDBACK RAPIDO |
| BTC | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 12 | 41,67% | +0,01% | -0,73% | FEEDBACK RAPIDO |
| SOL | 2g | 11 | 18,18% | +0,20% | -1,16% | FEEDBACK RAPIDO |
| SOL | 3g | 10 | 10,00% | +0,01% | -1,82% | FEEDBACK RAPIDO |
| SOL | 5g | 8 | 25,00% | -0,49% | -1,58% | FEEDBACK RAPIDO |
| SOL | 7g | 6 | 50,00% | -0,43% | -1,55% | FEEDBACK RAPIDO |
| SOL | 10g | 3 | 33,33% | -0,08% | -1,25% | FEEDBACK RAPIDO |
| SOL | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 13 | 53,85% | -0,08% | +0,08% | FEEDBACK RAPIDO |
| DOGE | 2g | 12 | 50,00% | -0,07% | +0,07% | FEEDBACK RAPIDO |
| DOGE | 3g | 11 | 54,55% | -0,36% | +0,36% | FEEDBACK RAPIDO |
| DOGE | 5g | 9 | 55,56% | -0,48% | +0,48% | FEEDBACK RAPIDO |
| DOGE | 7g | 7 | 71,43% | -0,77% | +0,77% | FEEDBACK RAPIDO |
| DOGE | 10g | 4 | 75,00% | -1,13% | +1,13% | FEEDBACK RAPIDO |
| DOGE | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 12 | 41,67% | +0,17% | +0,21% | -0,01% | +0,89% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 13 | 46,15% | +0,26% | +0,26% | +0,08% | +0,94% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 13 | 46,15% | +0,26% | +0,26% | +0,08% | +0,94% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 10 | 40,00% | +0,11% | +0,11% | -0,05% | +0,77% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 11 | 27,27% | +0,18% | -0,84% | -0,02% | +0,90% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 11 | 54,55% | +0,62% | +0,35% | +0,02% | +1,64% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 12 | 58,33% | +0,61% | +0,61% | +0,05% | +1,64% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 12 | 58,33% | +0,61% | +0,61% | +0,05% | +1,64% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 10 | 50,00% | +0,30% | +0,30% | -0,30% | +1,45% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 11 | 36,36% | +0,67% | -0,57% | +0,09% | +1,71% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 10 | 50,00% | +0,50% | +0,11% | -1,33% | +2,19% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 11 | 72,73% | +0,68% | +0,68% | -1,15% | +2,24% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 11 | 72,73% | +0,68% | +0,68% | -1,15% | +2,24% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 10 | 70,00% | +0,52% | +0,52% | -1,11% | +2,17% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 10 | 40,00% | +0,92% | -0,04% | -1,07% | +2,38% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 9 | 33,33% | +1,20% | -0,21% | -2,09% | +2,93% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 9 | 55,56% | +1,20% | +1,20% | -2,09% | +2,93% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 9 | 55,56% | +1,20% | +1,20% | -2,09% | +2,93% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 9 | 55,56% | +1,20% | +1,20% | -2,09% | +2,93% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 8 | 37,50% | +1,22% | -0,97% | -1,94% | +3,04% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 7 | 71,43% | +1,68% | +1,68% | -2,36% | +3,39% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 7 | 71,43% | +1,68% | +1,68% | -2,36% | +3,39% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 7 | 71,43% | +1,68% | +1,68% | -2,36% | +3,39% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 7 | 71,43% | +1,68% | +1,68% | -2,36% | +3,39% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 6 | 66,67% | +2,01% | +0,11% | -2,20% | +3,53% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 4 | 100,00% | +2,23% | +2,23% | -3,09% | +3,29% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | +2,23% | +2,23% | -3,09% | +3,29% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | +2,23% | +2,23% | -3,09% | +3,29% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 4 | 100,00% | +2,23% | +2,23% | -3,09% | +3,29% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 3 | 33,33% | +2,81% | -0,28% | -3,03% | +3,53% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 13 | 53,85% | -0,08% | +0,08% | -0,37% | +0,68% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 13 | 53,85% | -0,08% | +0,08% | -0,37% | +0,68% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 13 | 53,85% | -0,08% | +0,08% | -0,37% | +0,68% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 13 | 53,85% | -0,08% | +0,08% | -0,37% | +0,68% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 13 | 53,85% | -0,08% | +0,08% | -0,37% | +0,68% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 12 | 50,00% | +0,02% | -0,02% | -0,26% | +0,70% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 12 | 50,00% | -0,07% | +0,07% | -0,70% | +1,32% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 12 | 50,00% | -0,07% | +0,07% | -0,70% | +1,32% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 12 | 50,00% | -0,07% | +0,07% | -0,70% | +1,32% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 12 | 50,00% | -0,07% | +0,07% | -0,70% | +1,32% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 12 | 50,00% | -0,07% | +0,07% | -0,70% | +1,32% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 11 | 45,45% | +0,14% | -0,14% | -0,56% | +1,63% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 11 | 54,55% | -0,36% | +0,36% | -1,69% | +1,93% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 11 | 54,55% | -0,36% | +0,36% | -1,69% | +1,93% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 11 | 54,55% | -0,36% | +0,36% | -1,69% | +1,93% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 11 | 54,55% | -0,36% | +0,36% | -1,69% | +1,93% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 11 | 54,55% | -0,36% | +0,36% | -1,69% | +1,93% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 10 | 50,00% | -0,18% | +0,18% | -1,61% | +2,07% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 9 | 55,56% | -0,48% | +0,48% | -2,61% | +2,41% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 9 | 55,56% | -0,48% | +0,48% | -2,61% | +2,41% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 9 | 55,56% | -0,48% | +0,48% | -2,61% | +2,41% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 9 | 55,56% | -0,48% | +0,48% | -2,61% | +2,41% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 9 | 55,56% | -0,48% | +0,48% | -2,61% | +2,41% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 8 | 50,00% | -0,18% | +0,18% | -2,45% | +2,64% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 7 | 71,43% | -0,77% | +0,77% | -2,85% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 7 | 71,43% | -0,77% | +0,77% | -2,85% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 7 | 71,43% | -0,77% | +0,77% | -2,85% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 7 | 71,43% | -0,77% | +0,77% | -2,85% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 7 | 71,43% | -0,77% | +0,77% | -2,85% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 6 | 66,67% | -0,72% | +0,72% | -2,68% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 4 | 75,00% | -1,13% | +1,13% | -3,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 4 | 75,00% | -1,13% | +1,13% | -3,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 4 | 75,00% | -1,13% | +1,13% | -3,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 4 | 75,00% | -1,13% | +1,13% | -3,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 4 | 75,00% | -1,13% | +1,13% | -3,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 4 | 75,00% | -1,13% | +1,13% | -3,29% | +2,68% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 12 | 41,67% | +0,01% | -0,73% | -0,36% | +0,85% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 9 | 66,67% | -0,66% | +0,10% | -0,83% | +0,22% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 12 | 58,33% | -0,22% | -0,20% | -0,53% | +0,63% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 8 | 50,00% | -0,17% | +0,34% | -0,66% | +0,79% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 13 | 53,85% | +0,02% | -0,30% | -0,32% | +0,82% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 5 | 60,00% | +0,59% | -0,59% | +0,34% | +1,15% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 11 | 18,18% | +0,20% | -1,16% | -0,47% | +1,57% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 8 | 50,00% | -0,35% | -0,44% | -1,23% | +0,88% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 11 | 45,45% | -0,16% | -0,42% | -0,91% | +1,40% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 7 | 42,86% | -0,41% | -0,28% | -1,27% | +1,46% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 12 | 16,67% | +0,05% | -1,01% | -0,63% | +1,55% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 5 | 20,00% | +1,30% | -1,30% | +1,03% | +1,98% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 10 | 10,00% | +0,01% | -1,82% | -1,99% | +2,41% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 8 | 37,50% | -0,32% | -0,53% | -2,37% | +1,91% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 11 | 36,36% | -0,15% | -0,47% | -2,05% | +2,31% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 7 | 42,86% | -0,50% | -0,76% | -2,15% | +2,54% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 11 | 27,27% | -0,15% | -0,94% | -2,05% | +2,31% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 4 | 0,00% | +2,00% | -2,00% | -1,04% | +2,71% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 8 | 25,00% | -0,49% | -1,58% | -3,33% | +2,80% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 7 | 57,14% | -0,47% | -0,10% | -3,49% | +2,44% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 9 | 55,56% | -0,46% | +0,01% | -3,46% | +2,64% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | -1,74% | -0,52% | -3,74% | +2,48% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 9 | 22,22% | -0,46% | -1,37% | -3,46% | +2,64% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 2 | 0,00% | +3,26% | -3,26% | -2,09% | +3,78% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 6 | 50,00% | -0,43% | -1,55% | -4,16% | +2,70% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 5 | 100,00% | -1,33% | +1,46% | -4,55% | +2,21% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 7 | 85,71% | -0,85% | +0,94% | -4,21% | +2,53% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 6 | 66,67% | -0,43% | -0,08% | -4,16% | +2,70% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 7 | 14,29% | -0,85% | -2,06% | -4,21% | +2,53% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 3 | 33,33% | -0,08% | -1,25% | -5,20% | +2,16% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 3 | 66,67% | -0,99% | +0,99% | -5,16% | +2,20% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 4 | 50,00% | -0,61% | +0,61% | -5,28% | +2,00% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 3 | 33,33% | -0,08% | -1,25% | -5,20% | +2,16% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 4 | 50,00% | -0,61% | -0,61% | -5,28% | +2,00% | FEEDBACK RAPIDO |
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
