# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-31 05:15 UTC

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

Segnali totali salvati: **69**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-31 | BTC | 64.349,19 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-31 | DOGE | 0.07006 | -1 | +3 | +2 | +2 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-07-31 | SOL | 74,03 | -1 | +4 | +3 | +3 | -3 | -1 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-07-30 | BTC | 63.914,36 | +2 | +4 | +3 | +2 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-30 | DOGE | 0.06964 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-07-30 | SOL | 73,45 | -1 | +3 | +2 | +3 | -2 | -1 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-07-29 | BTC | 63.913,12 | +2 | +4 | +3 | +3 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-29 | DOGE | 0.07061 | +1 | +4 | +3 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-07-29 | SOL | 73,48 | 0 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-28 | BTC | 63.381,14 | -1 | +3 | +2 | +2 | -2 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-07-28 | DOGE | 0.06994 | +1 | +4 | +3 | +2 | -3 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-07-28 | SOL | 73,27 | +1 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 23 | 22 | 21 | 20 | 18 | 16 | 13 | 9 | 2 | 0 | 0 | 0 |
| SOL | 23 | 22 | 21 | 20 | 18 | 16 | 13 | 9 | 2 | 0 | 0 | 0 |
| DOGE | 23 | 22 | 21 | 20 | 18 | 16 | 13 | 9 | 2 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-11 | 21g | 2026-08-01 | domani |
| SOL | 2026-07-11 | 21g | 2026-08-01 | domani |
| DOGE | 2026-07-11 | 21g | 2026-08-01 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 20 | 45,00% | +0,06% | -0,00% | FEEDBACK RAPIDO |
| BTC | 2g | 19 | 42,11% | +0,15% | -0,09% | FEEDBACK RAPIDO |
| BTC | 3g | 18 | 33,33% | -0,03% | -0,42% | FEEDBACK RAPIDO |
| BTC | 5g | 16 | 25,00% | +0,31% | -0,48% | FEEDBACK RAPIDO |
| BTC | 7g | 14 | 42,86% | +0,63% | -0,05% | FEEDBACK RAPIDO |
| BTC | 10g | 12 | 50,00% | +1,39% | +0,84% | FEEDBACK RAPIDO |
| BTC | 14g | 9 | 77,78% | +1,35% | +1,14% | FEEDBACK RAPIDO |
| BTC | 21g | 2 | 100,00% | +0,92% | +0,92% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 16 | 43,75% | -0,10% | -0,64% | FEEDBACK RAPIDO |
| SOL | 2g | 15 | 26,67% | -0,37% | -1,00% | FEEDBACK RAPIDO |
| SOL | 3g | 15 | 20,00% | -0,53% | -1,32% | FEEDBACK RAPIDO |
| SOL | 5g | 14 | 35,71% | -1,05% | -1,42% | FEEDBACK RAPIDO |
| SOL | 7g | 14 | 42,86% | -1,34% | -1,10% | FEEDBACK RAPIDO |
| SOL | 10g | 12 | 41,67% | -1,36% | -0,59% | FEEDBACK RAPIDO |
| SOL | 14g | 8 | 50,00% | -2,48% | -0,29% | FEEDBACK RAPIDO |
| SOL | 21g | 1 | 0,00% | -5,86% | -5,86% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 21 | 52,38% | -0,04% | -0,01% | FEEDBACK RAPIDO |
| DOGE | 2g | 20 | 45,00% | -0,29% | -0,31% | FEEDBACK RAPIDO |
| DOGE | 3g | 19 | 47,37% | -0,49% | +0,10% | FEEDBACK RAPIDO |
| DOGE | 5g | 18 | 55,56% | -0,95% | +0,44% | FEEDBACK RAPIDO |
| DOGE | 7g | 16 | 68,75% | -1,34% | +1,34% | FEEDBACK RAPIDO |
| DOGE | 10g | 13 | 69,23% | -1,98% | +1,98% | FEEDBACK RAPIDO |
| DOGE | 14g | 9 | 77,78% | -2,97% | +2,97% | FEEDBACK RAPIDO |
| DOGE | 21g | 2 | 100,00% | -4,79% | +4,79% | FEEDBACK RAPIDO |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 20 | 45,00% | +0,06% | -0,00% | -0,23% | +0,70% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 22 | 50,00% | +0,03% | +0,03% | -0,25% | +0,62% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 22 | 50,00% | +0,03% | +0,03% | -0,25% | +0,62% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 18 | 50,00% | -0,02% | -0,02% | -0,32% | +0,51% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 18 | 33,33% | +0,19% | -0,45% | -0,11% | +0,77% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 2 | 0,00% | +0,42% | -0,42% | -0,14% | +0,79% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 19 | 42,11% | +0,15% | -0,09% | -0,38% | +1,00% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 21 | 47,62% | +0,10% | +0,10% | -0,40% | +0,93% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 21 | 47,62% | +0,10% | +0,10% | -0,40% | +0,93% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 17 | 47,06% | -0,04% | -0,04% | -0,56% | +0,81% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 17 | 35,29% | +0,35% | -0,48% | -0,17% | +1,18% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 2 | 0,00% | +0,76% | -0,76% | +0,33% | +1,77% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 18 | 33,33% | -0,03% | -0,42% | -1,46% | +1,89% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 20 | 55,00% | +0,10% | +0,10% | -1,40% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 20 | 55,00% | +0,10% | +0,10% | -1,40% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 16 | 56,25% | +0,08% | +0,08% | -1,46% | +1,73% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 16 | 37,50% | +0,58% | -0,13% | -1,09% | +2,23% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 1 | 0,00% | +1,53% | -1,53% | -0,28% | +2,98% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 16 | 25,00% | +0,31% | -0,48% | -2,23% | +2,55% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 18 | 38,89% | +0,29% | +0,29% | -2,15% | +2,56% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 18 | 38,89% | +0,29% | +0,29% | -2,15% | +2,56% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 14 | 42,86% | +0,54% | +0,54% | -2,15% | +2,61% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 15 | 53,33% | +0,48% | -0,25% | -1,92% | +2,80% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 14 | 42,86% | +0,63% | -0,05% | -2,36% | +3,10% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 16 | 56,25% | +0,48% | +0,48% | -2,33% | +3,05% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 16 | 56,25% | +0,48% | +0,48% | -2,33% | +3,05% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 12 | 66,67% | +1,09% | +1,09% | -2,26% | +3,27% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 13 | 46,15% | +1,13% | -0,22% | -2,02% | +3,40% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 12 | 50,00% | +1,39% | +0,84% | -2,26% | +4,12% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 13 | 61,54% | +1,23% | +1,23% | -2,19% | +4,17% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 13 | 61,54% | +1,23% | +1,23% | -2,19% | +4,17% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 10 | 80,00% | +1,94% | +1,94% | -2,01% | +4,48% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 11 | 36,36% | +1,56% | -0,47% | -1,91% | +4,53% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 9 | 77,78% | +1,35% | +1,14% | -2,26% | +5,20% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 9 | 77,78% | +1,35% | +1,35% | -2,26% | +5,20% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 9 | 77,78% | +1,35% | +1,35% | -2,26% | +5,20% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 9 | 77,78% | +1,35% | +1,35% | -2,26% | +5,20% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 8 | 37,50% | +1,24% | -0,20% | -2,13% | +5,26% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 2 | 100,00% | +0,92% | +0,92% | -2,80% | +5,29% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | +0,92% | +0,92% | -2,80% | +5,29% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | +0,92% | +0,92% | -2,80% | +5,29% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 2 | 100,00% | +0,92% | +0,92% | -2,80% | +5,29% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 1 | 0,00% | +1,07% | -1,07% | -2,32% | +5,81% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 21 | 52,38% | -0,04% | -0,01% | -0,46% | +0,68% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 22 | 54,55% | -0,23% | +0,32% | -0,65% | +0,49% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 22 | 54,55% | -0,23% | +0,32% | -0,65% | +0,49% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 20 | 55,00% | -0,06% | +0,16% | -0,51% | +0,69% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 22 | 54,55% | -0,23% | +0,23% | -0,65% | +0,49% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 18 | 44,44% | +0,13% | -0,13% | -0,29% | +0,78% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 20 | 45,00% | -0,29% | -0,31% | -0,91% | +0,86% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 21 | 47,62% | -0,43% | +0,02% | -1,06% | +0,69% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 21 | 47,62% | -0,43% | +0,02% | -1,06% | +0,69% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 19 | 47,37% | -0,60% | +0,16% | -1,16% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 21 | 61,90% | -0,43% | +0,43% | -1,06% | +0,69% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 17 | 52,94% | +0,12% | -0,12% | -0,55% | +1,36% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 19 | 47,37% | -0,49% | +0,10% | -2,16% | +2,14% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 20 | 50,00% | -0,69% | -0,06% | -2,30% | +1,92% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 20 | 50,00% | -0,69% | -0,06% | -2,30% | +1,92% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 18 | 55,56% | -1,17% | +0,33% | -2,26% | +1,70% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 20 | 50,00% | -0,69% | +0,69% | -2,30% | +1,92% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 17 | 41,18% | -0,19% | +0,19% | -2,00% | +2,37% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 18 | 55,56% | -0,95% | +0,44% | -3,24% | +2,50% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 18 | 61,11% | -0,95% | +0,47% | -3,24% | +2,50% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 18 | 61,11% | -0,95% | +0,47% | -3,24% | +2,50% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 16 | 62,50% | -1,01% | +0,47% | -3,32% | +2,25% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 18 | 61,11% | -0,95% | +0,95% | -3,24% | +2,50% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 16 | 56,25% | -0,61% | +0,61% | -3,04% | +2,79% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 16 | 68,75% | -1,34% | +1,34% | -3,82% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 16 | 68,75% | -1,34% | +1,34% | -3,82% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 16 | 68,75% | -1,34% | +1,34% | -3,82% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 14 | 71,43% | -1,38% | +1,38% | -3,98% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 16 | 68,75% | -1,34% | +1,34% | -3,82% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 15 | 66,67% | -1,36% | +1,36% | -3,82% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,51% | +1,51% | +0,10% | +6,93% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 13 | 69,23% | -1,98% | +1,98% | -4,65% | +2,39% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 13 | 69,23% | -1,98% | +1,98% | -4,65% | +2,39% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 13 | 69,23% | -1,98% | +1,98% | -4,65% | +2,39% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 13 | 69,23% | -1,98% | +1,98% | -4,65% | +2,39% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 13 | 69,23% | -1,98% | +1,98% | -4,65% | +2,39% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 12 | 66,67% | -1,64% | +1,64% | -4,45% | +2,54% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 9 | 77,78% | -2,97% | +2,97% | -5,87% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 9 | 77,78% | -2,97% | +2,97% | -5,87% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 9 | 77,78% | -2,97% | +2,97% | -5,87% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 9 | 77,78% | -2,97% | +2,97% | -5,87% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 9 | 77,78% | -2,97% | +2,97% | -5,87% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 8 | 75,00% | -2,77% | +2,77% | -5,65% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 2 | 100,00% | -4,79% | +4,79% | -6,91% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -4,79% | +4,79% | -6,91% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | -4,79% | +4,79% | -6,91% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 2 | 100,00% | -4,79% | +4,79% | -6,91% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 2 | 100,00% | -4,79% | +4,79% | -6,91% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 2 | 100,00% | -4,79% | +4,79% | -6,91% | +2,87% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 16 | 43,75% | -0,10% | -0,64% | -0,49% | +0,79% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 18 | 61,11% | -0,60% | -0,12% | -0,92% | +0,20% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 21 | 57,14% | -0,36% | -0,26% | -0,74% | +0,43% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 16 | 50,00% | -0,33% | -0,08% | -0,85% | +0,44% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 22 | 54,55% | -0,21% | +0,04% | -0,61% | +0,55% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 14 | 57,14% | -0,14% | +0,14% | -0,53% | +0,52% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 15 | 26,67% | -0,37% | -1,00% | -0,96% | +0,85% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 17 | 47,06% | -0,81% | -0,54% | -1,48% | +0,17% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 20 | 45,00% | -0,64% | -0,51% | -1,27% | +0,56% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 15 | 40,00% | -0,75% | -0,68% | -1,41% | +0,56% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 21 | 38,10% | -0,49% | -0,05% | -1,09% | +0,68% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 13 | 46,15% | -0,24% | +0,24% | -0,67% | +0,39% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 15 | 20,00% | -0,53% | -1,32% | -2,22% | +2,03% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 16 | 37,50% | -1,15% | -0,67% | -2,89% | +1,46% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 19 | 36,84% | -0,92% | -0,61% | -2,63% | +1,76% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 14 | 35,71% | -1,05% | -1,18% | -2,67% | +1,79% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 20 | 45,00% | -0,80% | +0,20% | -2,43% | +1,85% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 12 | 41,67% | -0,26% | +0,26% | -2,21% | +1,82% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 14 | 35,71% | -1,05% | -1,42% | -3,34% | +2,55% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 14 | 42,86% | -1,42% | -0,92% | -3,73% | +2,24% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 17 | 41,18% | -1,05% | -0,88% | -3,43% | +2,53% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 12 | 33,33% | -1,82% | -1,21% | -3,59% | +2,48% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 18 | 55,56% | -1,12% | +0,21% | -3,40% | +2,59% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 10 | 70,00% | -0,56% | +0,56% | -2,81% | +2,98% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 14 | 42,86% | -1,34% | -1,10% | -4,04% | +2,75% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 12 | 58,33% | -2,04% | -0,13% | -4,50% | +2,24% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 15 | 60,00% | -1,65% | -0,08% | -4,14% | +2,58% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 10 | 40,00% | -1,70% | -1,49% | -4,36% | +2,44% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 16 | 43,75% | -1,52% | +0,24% | -4,09% | +2,64% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 8 | 62,50% | -1,50% | +1,50% | -3,66% | +2,98% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 12 | 41,67% | -1,36% | -0,59% | -4,29% | +3,14% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 9 | 44,44% | -1,61% | -0,55% | -4,66% | +2,66% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 12 | 41,67% | -1,26% | -0,36% | -4,36% | +2,97% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 8 | 25,00% | -1,27% | -1,96% | -4,62% | +2,78% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 13 | 61,54% | -1,42% | +1,05% | -4,39% | +3,02% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 5 | 80,00% | -1,68% | +1,68% | -3,43% | +4,11% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 8 | 50,00% | -2,48% | -0,29% | -4,57% | +3,12% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 7 | 71,43% | -2,21% | +0,71% | -4,83% | +2,83% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 9 | 77,78% | -2,49% | +1,32% | -4,68% | +2,94% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 6 | 16,67% | -2,51% | -1,92% | -4,69% | +2,76% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 9 | 44,44% | -2,49% | +0,23% | -4,68% | +2,94% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 2 | 100,00% | -2,40% | +2,40% | -4,20% | +4,20% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -5,29% | +5,29% | -7,04% | +1,74% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | -5,29% | +5,29% | -7,04% | +1,74% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 2 | 0,00% | -5,29% | -5,29% | -7,04% | +1,74% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |

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
