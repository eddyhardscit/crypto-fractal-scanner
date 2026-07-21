# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-21 05:14 UTC

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

Segnali totali salvati: **39**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-21 | BTC | 65.476,52 | +3 | +2 | +2 | 0 | 0 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-21 | DOGE | 0.07281 | -6 | -3 | -2 | -2 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-21 | SOL | 78,22 | +1 | +2 | +1 | +2 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-20 | BTC | 64.190,23 | +2 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-20 | DOGE | 0.07180 | -7 | -3 | -2 | -2 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-20 | SOL | 76,01 | -4 | 0 | 0 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-19 | BTC | 64.750,69 | +3 | +1 | +1 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-19 | DOGE | 0.07243 | -6 | -3 | -2 | -2 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-19 | SOL | 76,04 | -4 | -1 | -1 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-18 | BTC | 63.883,71 | 0 | +1 | +1 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-18 | DOGE | 0.07234 | -6 | -3 | -2 | -2 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-18 | SOL | 74,93 | -3 | 0 | -1 | +1 | -2 | -1 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 13 | 12 | 11 | 10 | 8 | 6 | 3 | 0 | 0 | 0 | 0 | 0 |
| SOL | 13 | 12 | 11 | 10 | 8 | 6 | 3 | 0 | 0 | 0 | 0 | 0 |
| DOGE | 13 | 12 | 11 | 10 | 8 | 6 | 3 | 0 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-12 | 10g | 2026-07-22 | domani |
| SOL | 2026-07-12 | 10g | 2026-07-22 | domani |
| DOGE | 2026-07-12 | 10g | 2026-07-22 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 11 | 36,36% | +0,08% | +0,13% | FEEDBACK RAPIDO |
| BTC | 2g | 10 | 50,00% | +0,37% | +0,06% | FEEDBACK RAPIDO |
| BTC | 3g | 9 | 44,44% | +0,30% | -0,14% | FEEDBACK RAPIDO |
| BTC | 5g | 8 | 37,50% | +0,84% | +0,27% | FEEDBACK RAPIDO |
| BTC | 7g | 6 | 66,67% | +1,52% | +1,52% | FEEDBACK RAPIDO |
| BTC | 10g | 3 | 100,00% | +1,72% | +1,72% | FEEDBACK RAPIDO |
| BTC | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 11 | 45,45% | +0,06% | -0,75% | FEEDBACK RAPIDO |
| SOL | 2g | 10 | 20,00% | -0,02% | -1,04% | FEEDBACK RAPIDO |
| SOL | 3g | 9 | 11,11% | -0,25% | -1,76% | FEEDBACK RAPIDO |
| SOL | 5g | 7 | 28,57% | -1,08% | -1,29% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | 40,00% | -0,59% | -1,92% | FEEDBACK RAPIDO |
| SOL | 10g | 2 | 50,00% | -1,00% | -1,00% | FEEDBACK RAPIDO |
| SOL | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 12 | 58,33% | -0,12% | +0,12% | FEEDBACK RAPIDO |
| DOGE | 2g | 11 | 54,55% | -0,25% | +0,25% | FEEDBACK RAPIDO |
| DOGE | 3g | 10 | 60,00% | -0,50% | +0,50% | FEEDBACK RAPIDO |
| DOGE | 5g | 8 | 62,50% | -0,71% | +0,71% | FEEDBACK RAPIDO |
| DOGE | 7g | 6 | 66,67% | -0,72% | +0,72% | FEEDBACK RAPIDO |
| DOGE | 10g | 3 | 100,00% | -1,67% | +1,67% | FEEDBACK RAPIDO |
| DOGE | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 11 | 36,36% | +0,08% | +0,13% | -0,10% | +0,80% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 12 | 41,67% | +0,19% | +0,19% | -0,00% | +0,86% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 12 | 41,67% | +0,19% | +0,19% | -0,00% | +0,86% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 10 | 40,00% | +0,11% | +0,11% | -0,05% | +0,77% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 11 | 27,27% | +0,18% | -0,84% | -0,02% | +0,90% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 10 | 50,00% | +0,37% | +0,06% | -0,28% | +1,41% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 11 | 54,55% | +0,38% | +0,38% | -0,22% | +1,44% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 11 | 54,55% | +0,38% | +0,38% | -0,22% | +1,44% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 10 | 50,00% | +0,30% | +0,30% | -0,30% | +1,45% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 10 | 40,00% | +0,42% | -0,31% | -0,21% | +1,49% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 9 | 44,44% | +0,30% | -0,14% | -1,30% | +2,10% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 10 | 70,00% | +0,52% | +0,52% | -1,11% | +2,17% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 10 | 70,00% | +0,52% | +0,52% | -1,11% | +2,17% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 10 | 70,00% | +0,52% | +0,52% | -1,11% | +2,17% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 9 | 33,33% | +0,77% | -0,30% | -1,01% | +2,31% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 8 | 37,50% | +0,84% | +0,27% | -2,36% | +2,70% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 8 | 50,00% | +0,84% | +0,84% | -2,36% | +2,70% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 8 | 50,00% | +0,84% | +0,84% | -2,36% | +2,70% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 8 | 50,00% | +0,84% | +0,84% | -2,36% | +2,70% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 7 | 42,86% | +0,81% | -0,53% | -2,23% | +2,79% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 6 | 66,67% | +1,52% | +1,52% | -2,22% | +3,40% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 6 | 66,67% | +1,52% | +1,52% | -2,22% | +3,40% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 6 | 66,67% | +1,52% | +1,52% | -2,22% | +3,40% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 6 | 66,67% | +1,52% | +1,52% | -2,22% | +3,40% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 5 | 60,00% | +1,89% | -0,39% | -2,01% | +3,57% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 3 | 100,00% | +1,72% | +1,72% | -3,05% | +2,89% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | +1,72% | +1,72% | -3,05% | +2,89% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | +1,72% | +1,72% | -3,05% | +2,89% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 3 | 100,00% | +1,72% | +1,72% | -3,05% | +2,89% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 2 | 0,00% | +2,32% | -2,32% | -2,93% | +3,04% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 12 | 58,33% | -0,12% | +0,12% | -0,45% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 12 | 58,33% | -0,12% | +0,12% | -0,45% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 12 | 58,33% | -0,12% | +0,12% | -0,45% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 12 | 58,33% | -0,12% | +0,12% | -0,45% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 12 | 58,33% | -0,12% | +0,12% | -0,45% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 11 | 54,55% | -0,02% | +0,02% | -0,33% | +0,64% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 11 | 54,55% | -0,25% | +0,25% | -0,95% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 11 | 54,55% | -0,25% | +0,25% | -0,95% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 11 | 54,55% | -0,25% | +0,25% | -0,95% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 11 | 54,55% | -0,25% | +0,25% | -0,95% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 11 | 54,55% | -0,25% | +0,25% | -0,95% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 10 | 50,00% | -0,04% | +0,04% | -0,82% | +1,52% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 10 | 60,00% | -0,50% | +0,50% | -1,70% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 10 | 60,00% | -0,50% | +0,50% | -1,70% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 10 | 60,00% | -0,50% | +0,50% | -1,70% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | -0,50% | +0,50% | -1,70% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 10 | 60,00% | -0,50% | +0,50% | -1,70% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 9 | 55,56% | -0,31% | +0,31% | -1,62% | +2,10% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 8 | 62,50% | -0,71% | +0,71% | -2,77% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 8 | 62,50% | -0,71% | +0,71% | -2,77% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 8 | 62,50% | -0,71% | +0,71% | -2,77% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 8 | 62,50% | -0,71% | +0,71% | -2,77% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 8 | 62,50% | -0,71% | +0,71% | -2,77% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 7 | 57,14% | -0,40% | +0,40% | -2,62% | +2,71% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 6 | 66,67% | -0,72% | +0,72% | -2,68% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 6 | 66,67% | -0,72% | +0,72% | -2,68% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 6 | 66,67% | -0,72% | +0,72% | -2,68% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 6 | 66,67% | -0,72% | +0,72% | -2,68% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 6 | 66,67% | -0,72% | +0,72% | -2,68% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 6 | 66,67% | -0,72% | +0,72% | -2,68% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 3 | 100,00% | -1,67% | +1,67% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | -1,67% | +1,67% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | -1,67% | +1,67% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 3 | 100,00% | -1,67% | +1,67% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 3 | 100,00% | -1,67% | +1,67% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 3 | 100,00% | -1,67% | +1,67% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 11 | 45,45% | +0,06% | -0,75% | -0,35% | +0,89% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 8 | 75,00% | -0,68% | +0,18% | -0,88% | +0,20% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 11 | 63,64% | -0,20% | -0,17% | -0,54% | +0,66% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -0,12% | +0,46% | -0,69% | +0,86% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 12 | 50,00% | +0,06% | -0,36% | -0,31% | +0,86% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 5 | 60,00% | +0,59% | -0,59% | +0,34% | +1,15% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 10 | 20,00% | -0,02% | -1,04% | -0,76% | +1,40% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 8 | 50,00% | -0,35% | -0,44% | -1,23% | +0,88% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 11 | 45,45% | -0,16% | -0,42% | -0,91% | +1,40% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 7 | 42,86% | -0,41% | -0,28% | -1,27% | +1,46% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 11 | 18,18% | -0,16% | -0,88% | -0,91% | +1,40% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,03% | -1,03% | +0,68% | +1,67% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 9 | 11,11% | -0,25% | -1,76% | -2,14% | +2,32% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 7 | 42,86% | -0,70% | -0,27% | -2,61% | +1,72% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 10 | 40,00% | -0,40% | -0,28% | -2,19% | +2,22% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 7 | 42,86% | -0,50% | -0,76% | -2,15% | +2,54% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 10 | 30,00% | -0,40% | -0,80% | -2,19% | +2,22% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 3 | 0,00% | +1,88% | -1,88% | -1,17% | +2,55% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 7 | 28,57% | -1,08% | -1,29% | -3,69% | +2,57% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 6 | 66,67% | -1,15% | +0,48% | -3,95% | +2,11% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 8 | 62,50% | -0,97% | +0,47% | -3,80% | +2,41% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | -1,74% | -0,52% | -3,74% | +2,48% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 8 | 25,00% | -0,97% | -1,10% | -3,80% | +2,41% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 1 | 0,00% | +2,92% | -2,92% | -3,42% | +3,10% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 5 | 40,00% | -0,59% | -1,92% | -3,91% | +3,01% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | -1,74% | +1,74% | -4,35% | +2,47% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 6 | 83,33% | -1,04% | +1,04% | -4,02% | +2,76% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 5 | 60,00% | -0,59% | -0,17% | -3,91% | +3,01% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 6 | 16,67% | -1,04% | -2,35% | -4,02% | +2,76% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 2 | 50,00% | -1,00% | -1,00% | -5,79% | +1,67% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -2,36% | +2,36% | -5,73% | +1,74% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 3 | 66,67% | -1,39% | +1,39% | -5,70% | +1,62% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 2 | 50,00% | -1,00% | -1,00% | -5,79% | +1,67% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 3 | 33,33% | -1,39% | -1,39% | -5,70% | +1,62% | FEEDBACK RAPIDO |
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
