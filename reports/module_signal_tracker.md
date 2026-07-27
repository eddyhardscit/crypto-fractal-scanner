# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-27 05:14 UTC

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

Segnali totali salvati: **57**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-27 | BTC | 65.325,99 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-27 | DOGE | 0.07289 | 0 | +3 | +2 | +2 | -3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-07-27 | SOL | 76,40 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-26 | BTC | 64.454,23 | +5 | +4 | +3 | +2 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-26 | DOGE | 0.07344 | +2 | +3 | +2 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-07-26 | SOL | 75,10 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-25 | BTC | 64.087,96 | +2 | +3 | +3 | +2 | -2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-25 | DOGE | 0.06949 | -1 | +2 | +1 | +2 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-07-25 | SOL | 74,17 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-24 | BTC | 65.302,77 | 0 | +2 | +2 | +3 | -2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-24 | DOGE | 0.06902 | -5 | -1 | -1 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-24 | SOL | 75,72 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 19 | 18 | 17 | 16 | 14 | 12 | 9 | 5 | 0 | 0 | 0 | 0 |
| SOL | 19 | 18 | 17 | 16 | 14 | 12 | 9 | 5 | 0 | 0 | 0 | 0 |
| DOGE | 19 | 18 | 17 | 16 | 14 | 12 | 9 | 5 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-14 | 14g | 2026-07-28 | domani |
| SOL | 2026-07-14 | 14g | 2026-07-28 | domani |
| DOGE | 2026-07-14 | 14g | 2026-07-28 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 16 | 43,75% | +0,16% | +0,19% | FEEDBACK RAPIDO |
| BTC | 2g | 15 | 46,67% | +0,35% | +0,15% | FEEDBACK RAPIDO |
| BTC | 3g | 14 | 42,86% | +0,14% | -0,14% | FEEDBACK RAPIDO |
| BTC | 5g | 13 | 30,77% | +0,66% | -0,32% | FEEDBACK RAPIDO |
| BTC | 7g | 11 | 54,55% | +1,62% | +0,75% | FEEDBACK RAPIDO |
| BTC | 10g | 9 | 66,67% | +2,24% | +1,51% | FEEDBACK RAPIDO |
| BTC | 14g | 5 | 100,00% | +2,17% | +2,17% | FEEDBACK RAPIDO |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 14 | 42,86% | -0,19% | -0,69% | FEEDBACK RAPIDO |
| SOL | 2g | 14 | 21,43% | -0,41% | -1,09% | FEEDBACK RAPIDO |
| SOL | 3g | 14 | 14,29% | -0,64% | -1,49% | FEEDBACK RAPIDO |
| SOL | 5g | 13 | 38,46% | -0,74% | -1,14% | FEEDBACK RAPIDO |
| SOL | 7g | 11 | 45,45% | -0,18% | -0,90% | FEEDBACK RAPIDO |
| SOL | 10g | 8 | 25,00% | -0,25% | -1,34% | FEEDBACK RAPIDO |
| SOL | 14g | 4 | 25,00% | -1,89% | -1,01% | FEEDBACK RAPIDO |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 18 | 50,00% | -0,06% | -0,02% | FEEDBACK RAPIDO |
| DOGE | 2g | 17 | 52,94% | +0,01% | -0,01% | FEEDBACK RAPIDO |
| DOGE | 3g | 16 | 50,00% | -0,39% | +0,39% | FEEDBACK RAPIDO |
| DOGE | 5g | 14 | 64,29% | -0,85% | +0,85% | FEEDBACK RAPIDO |
| DOGE | 7g | 12 | 66,67% | -0,98% | +0,98% | FEEDBACK RAPIDO |
| DOGE | 10g | 9 | 55,56% | -1,46% | +1,46% | FEEDBACK RAPIDO |
| DOGE | 14g | 5 | 60,00% | -2,33% | +2,33% | FEEDBACK RAPIDO |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 16 | 43,75% | +0,16% | +0,19% | -0,08% | +0,79% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 18 | 44,44% | +0,12% | +0,12% | -0,12% | +0,69% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 18 | 44,44% | +0,12% | +0,12% | -0,12% | +0,69% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 14 | 42,86% | +0,08% | +0,08% | -0,17% | +0,57% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 15 | 40,00% | +0,13% | -0,43% | -0,15% | +0,68% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 15 | 46,67% | +0,35% | +0,15% | -0,20% | +1,24% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 17 | 47,06% | +0,26% | +0,26% | -0,24% | +1,13% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 17 | 47,06% | +0,26% | +0,26% | -0,24% | +1,13% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 13 | 46,15% | +0,13% | +0,13% | -0,42% | +1,02% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 14 | 42,86% | +0,43% | -0,35% | -0,10% | +1,26% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 14 | 42,86% | +0,14% | -0,14% | -1,36% | +2,05% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 16 | 62,50% | +0,28% | +0,28% | -1,30% | +1,96% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 16 | 62,50% | +0,28% | +0,28% | -1,30% | +1,96% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 12 | 66,67% | +0,32% | +0,32% | -1,34% | +1,86% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 13 | 38,46% | +0,75% | -0,07% | -1,10% | +2,20% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 13 | 30,77% | +0,66% | -0,32% | -2,10% | +2,76% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 14 | 50,00% | +0,78% | +0,78% | -1,97% | +2,90% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 14 | 50,00% | +0,78% | +0,78% | -1,97% | +2,90% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +1,32% | +1,32% | -1,90% | +3,11% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 11 | 45,45% | +1,16% | -0,83% | -1,61% | +3,33% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 11 | 54,55% | +1,62% | +0,75% | -1,93% | +3,72% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 12 | 75,00% | +1,51% | +1,51% | -1,79% | +3,81% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 12 | 75,00% | +1,51% | +1,51% | -1,79% | +3,81% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 10 | 80,00% | +1,68% | +1,68% | -1,90% | +3,81% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 11 | 36,36% | +1,68% | -0,60% | -1,65% | +3,92% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 9 | 66,67% | +2,24% | +1,51% | -2,09% | +4,45% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 9 | 88,89% | +2,24% | +2,24% | -2,09% | +4,45% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 9 | 88,89% | +2,24% | +2,24% | -2,09% | +4,45% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 9 | 88,89% | +2,24% | +2,24% | -2,09% | +4,45% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 8 | 25,00% | +2,46% | -0,63% | -1,94% | +4,69% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 5 | 100,00% | +2,17% | +2,17% | -2,65% | +5,30% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 5 | 100,00% | +2,17% | +2,17% | -2,65% | +5,30% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 5 | 100,00% | +2,17% | +2,17% | -2,65% | +5,30% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 5 | 100,00% | +2,17% | +2,17% | -2,65% | +5,30% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 4 | 50,00% | +2,15% | +0,40% | -2,49% | +5,44% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 18 | 50,00% | -0,06% | -0,02% | -0,48% | +0,61% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 18 | 55,56% | -0,06% | +0,61% | -0,48% | +0,61% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 18 | 55,56% | -0,06% | +0,61% | -0,48% | +0,61% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 16 | 56,25% | +0,17% | +0,45% | -0,28% | +0,88% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 18 | 55,56% | -0,06% | +0,06% | -0,48% | +0,61% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 16 | 50,00% | +0,05% | -0,05% | -0,35% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 17 | 52,94% | +0,01% | -0,01% | -0,66% | +1,18% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 17 | 58,82% | +0,01% | +0,57% | -0,66% | +1,18% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 17 | 58,82% | +0,01% | +0,57% | -0,66% | +1,18% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 15 | 60,00% | -0,16% | +0,81% | -0,73% | +1,16% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 17 | 52,94% | +0,01% | -0,01% | -0,66% | +1,18% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 16 | 50,00% | +0,16% | -0,16% | -0,56% | +1,39% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 16 | 50,00% | -0,39% | +0,39% | -2,20% | +2,07% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 16 | 50,00% | -0,39% | +0,39% | -2,20% | +2,07% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 16 | 50,00% | -0,39% | +0,39% | -2,20% | +2,07% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | -0,96% | +0,96% | -2,13% | +1,80% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 16 | 50,00% | -0,39% | +0,39% | -2,20% | +2,07% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 15 | 46,67% | -0,28% | +0,28% | -2,18% | +2,17% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +5,61% | +5,61% | +0,26% | +6,46% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 14 | 64,29% | -0,85% | +0,85% | -3,36% | +2,14% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 14 | 64,29% | -0,85% | +0,85% | -3,36% | +2,14% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 14 | 64,29% | -0,85% | +0,85% | -3,36% | +2,14% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 14 | 64,29% | -0,85% | +0,85% | -3,36% | +2,14% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 14 | 64,29% | -0,85% | +0,85% | -3,36% | +2,14% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 13 | 61,54% | -0,69% | +0,69% | -3,32% | +2,26% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 12 | 66,67% | -0,98% | +0,98% | -3,57% | +2,46% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 12 | 66,67% | -0,98% | +0,98% | -3,57% | +2,46% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 12 | 66,67% | -0,98% | +0,98% | -3,57% | +2,46% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 12 | 66,67% | -0,98% | +0,98% | -3,57% | +2,46% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 12 | 66,67% | -0,98% | +0,98% | -3,57% | +2,46% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 11 | 63,64% | -0,98% | +0,98% | -3,54% | +2,64% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 9 | 55,56% | -1,46% | +1,46% | -4,23% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 9 | 55,56% | -1,46% | +1,46% | -4,23% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 9 | 55,56% | -1,46% | +1,46% | -4,23% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 9 | 55,56% | -1,46% | +1,46% | -4,23% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 9 | 55,56% | -1,46% | +1,46% | -4,23% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 8 | 50,00% | -0,89% | +0,89% | -3,88% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 5 | 60,00% | -2,33% | +2,33% | -5,62% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 5 | 60,00% | -2,33% | +2,33% | -5,62% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 5 | 60,00% | -2,33% | +2,33% | -5,62% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 5 | 60,00% | -2,33% | +2,33% | -5,62% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 5 | 60,00% | -2,33% | +2,33% | -5,62% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 5 | 60,00% | -2,33% | +2,33% | -5,62% | +2,99% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 14 | 42,86% | -0,19% | -0,69% | -0,54% | +0,67% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 14 | 64,29% | -0,55% | +0,06% | -0,82% | +0,18% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 17 | 58,82% | -0,26% | -0,14% | -0,61% | +0,48% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 12 | 50,00% | -0,19% | +0,15% | -0,69% | +0,51% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 18 | 55,56% | -0,09% | -0,12% | -0,45% | +0,62% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 10 | 60,00% | +0,12% | -0,12% | -0,23% | +0,63% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 14 | 21,43% | -0,41% | -1,09% | -1,02% | +0,84% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 13 | 46,15% | -0,66% | -0,30% | -1,37% | +0,31% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 16 | 43,75% | -0,47% | -0,31% | -1,13% | +0,77% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 11 | 36,36% | -0,54% | -0,45% | -1,25% | +0,87% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 17 | 35,29% | -0,30% | -0,37% | -0,92% | +0,91% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 9 | 44,44% | +0,24% | -0,24% | -0,14% | +0,70% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 14 | 14,29% | -0,64% | -1,49% | -2,30% | +2,00% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 12 | 41,67% | -1,02% | -0,37% | -2,94% | +1,40% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 15 | 40,00% | -0,75% | -0,36% | -2,59% | +1,79% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 10 | 40,00% | -0,84% | -1,03% | -2,63% | +1,85% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 16 | 37,50% | -0,61% | -0,14% | -2,35% | +1,90% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 8 | 25,00% | +0,38% | -0,38% | -1,93% | +1,91% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 13 | 38,46% | -0,74% | -1,14% | -3,18% | +2,77% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 10 | 60,00% | -0,95% | -0,25% | -3,71% | +2,21% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 13 | 53,85% | -0,57% | -0,35% | -3,32% | +2,60% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 8 | 50,00% | -1,44% | -0,52% | -3,48% | +2,57% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 14 | 42,86% | -0,70% | -0,48% | -3,28% | +2,67% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 6 | 50,00% | +0,80% | -0,80% | -2,14% | +3,43% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 11 | 45,45% | -0,18% | -0,90% | -3,39% | +3,34% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 8 | 75,00% | -0,69% | +0,78% | -3,79% | +2,87% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 11 | 72,73% | -0,53% | +0,59% | -3,50% | +3,16% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -0,52% | -0,22% | -3,76% | +3,04% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 12 | 25,00% | -0,45% | -1,25% | -3,48% | +3,19% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 5 | 40,00% | +0,11% | -0,11% | -2,46% | +4,11% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 8 | 25,00% | -0,25% | -1,34% | -4,06% | +3,12% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 7 | 42,86% | -0,83% | -0,42% | -4,33% | +2,83% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 9 | 33,33% | -0,47% | -0,51% | -4,22% | +2,94% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 6 | 33,33% | -0,43% | -1,35% | -4,48% | +2,76% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 9 | 44,44% | -0,47% | -0,07% | -4,22% | +2,94% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 2 | 50,00% | +0,27% | -0,27% | -2,80% | +4,20% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 4 | 25,00% | -1,89% | -1,01% | -4,87% | +2,44% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 4 | 75,00% | -1,36% | +1,36% | -4,84% | +2,47% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 5 | 80,00% | -2,02% | +2,02% | -5,00% | +2,26% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 4 | 25,00% | -1,89% | -1,01% | -4,87% | +2,44% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 5 | 0,00% | -2,02% | -2,04% | -5,00% | +2,26% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |

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
