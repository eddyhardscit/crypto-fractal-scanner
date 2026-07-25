# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-25 05:15 UTC

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

Segnali totali salvati: **51**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-25 | BTC | 64.087,96 | +2 | +3 | +3 | +2 | -2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-25 | DOGE | 0.06949 | -1 | +2 | +1 | +2 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-07-25 | SOL | 74,17 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-24 | BTC | 65.302,77 | 0 | +2 | +2 | +3 | -2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-24 | DOGE | 0.06902 | -5 | -1 | -1 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-24 | SOL | 75,72 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-23 | BTC | 65.399,99 | +1 | +2 | +2 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-23 | DOGE | 0.07229 | -3 | -1 | -1 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-07-23 | SOL | 77,14 | +1 | +3 | +2 | +2 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-22 | BTC | 66.234,10 | +2 | +2 | +2 | 0 | 0 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-22 | DOGE | 0.07318 | -5 | -2 | -1 | -1 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-22 | SOL | 77,82 | -3 | -1 | -1 | 0 | -1 | -1 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 17 | 16 | 15 | 14 | 12 | 10 | 7 | 3 | 0 | 0 | 0 | 0 |
| SOL | 17 | 16 | 15 | 14 | 12 | 10 | 7 | 3 | 0 | 0 | 0 | 0 |
| DOGE | 17 | 16 | 15 | 14 | 12 | 10 | 7 | 3 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-12 | 14g | 2026-07-26 | domani |
| SOL | 2026-07-12 | 14g | 2026-07-26 | domani |
| DOGE | 2026-07-12 | 14g | 2026-07-26 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 14 | 35,71% | +0,05% | +0,08% | FEEDBACK RAPIDO |
| BTC | 2g | 14 | 42,86% | +0,24% | +0,02% | FEEDBACK RAPIDO |
| BTC | 3g | 13 | 46,15% | +0,26% | -0,04% | FEEDBACK RAPIDO |
| BTC | 5g | 11 | 36,36% | +1,04% | -0,11% | FEEDBACK RAPIDO |
| BTC | 7g | 9 | 55,56% | +1,83% | +0,78% | FEEDBACK RAPIDO |
| BTC | 10g | 7 | 85,71% | +2,41% | +2,41% | FEEDBACK RAPIDO |
| BTC | 14g | 3 | 100,00% | +1,92% | +1,92% | FEEDBACK RAPIDO |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 14 | 42,86% | -0,19% | -0,69% | FEEDBACK RAPIDO |
| SOL | 2g | 14 | 21,43% | -0,41% | -1,09% | FEEDBACK RAPIDO |
| SOL | 3g | 13 | 15,38% | -0,48% | -1,40% | FEEDBACK RAPIDO |
| SOL | 5g | 11 | 36,36% | -0,35% | -1,16% | FEEDBACK RAPIDO |
| SOL | 7g | 9 | 44,44% | -0,14% | -1,18% | FEEDBACK RAPIDO |
| SOL | 10g | 6 | 16,67% | -0,43% | -1,70% | FEEDBACK RAPIDO |
| SOL | 14g | 2 | 0,00% | -2,90% | -2,90% | FEEDBACK RAPIDO |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 16 | 56,25% | -0,38% | +0,38% | FEEDBACK RAPIDO |
| DOGE | 2g | 15 | 60,00% | -0,74% | +0,74% | FEEDBACK RAPIDO |
| DOGE | 3g | 14 | 57,14% | -0,96% | +0,96% | FEEDBACK RAPIDO |
| DOGE | 5g | 12 | 66,67% | -1,03% | +1,03% | FEEDBACK RAPIDO |
| DOGE | 7g | 10 | 80,00% | -1,47% | +1,47% | FEEDBACK RAPIDO |
| DOGE | 10g | 7 | 71,43% | -2,09% | +2,09% | FEEDBACK RAPIDO |
| DOGE | 14g | 3 | 100,00% | -4,48% | +4,48% | FEEDBACK RAPIDO |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 14 | 35,71% | +0,05% | +0,08% | -0,17% | +0,76% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 16 | 37,50% | +0,01% | +0,01% | -0,21% | +0,65% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 16 | 37,50% | +0,01% | +0,01% | -0,21% | +0,65% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 12 | 33,33% | -0,07% | -0,07% | -0,30% | +0,49% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 13 | 38,46% | -0,00% | -0,56% | -0,25% | +0,63% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 14 | 42,86% | +0,24% | +0,02% | -0,31% | +1,19% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 15 | 46,67% | +0,25% | +0,25% | -0,27% | +1,23% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 15 | 46,67% | +0,25% | +0,25% | -0,27% | +1,23% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 11 | 45,45% | +0,09% | +0,09% | -0,48% | +1,14% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 12 | 41,67% | +0,45% | -0,36% | -0,10% | +1,41% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 13 | 46,15% | +0,26% | -0,04% | -1,26% | +2,16% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 14 | 64,29% | +0,42% | +0,42% | -1,13% | +2,20% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 14 | 64,29% | +0,42% | +0,42% | -1,13% | +2,20% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 10 | 70,00% | +0,52% | +0,52% | -1,11% | +2,17% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 11 | 36,36% | +1,01% | -0,21% | -0,84% | +2,54% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 11 | 36,36% | +1,04% | -0,11% | -1,89% | +3,09% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 12 | 58,33% | +1,15% | +1,15% | -1,75% | +3,22% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 12 | 58,33% | +1,15% | +1,15% | -1,75% | +3,22% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +1,32% | +1,32% | -1,90% | +3,11% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 11 | 45,45% | +1,16% | -0,83% | -1,61% | +3,33% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 9 | 55,56% | +1,83% | +0,78% | -2,09% | +3,71% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 10 | 80,00% | +1,68% | +1,68% | -1,90% | +3,81% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 10 | 80,00% | +1,68% | +1,68% | -1,90% | +3,81% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 10 | 80,00% | +1,68% | +1,68% | -1,90% | +3,81% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 9 | 44,44% | +1,91% | -0,49% | -1,75% | +3,95% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 7 | 85,71% | +2,41% | +2,41% | -2,36% | +4,35% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 7 | 85,71% | +2,41% | +2,41% | -2,36% | +4,35% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 7 | 85,71% | +2,41% | +2,41% | -2,36% | +4,35% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 7 | 85,71% | +2,41% | +2,41% | -2,36% | +4,35% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 6 | 33,33% | +2,73% | -0,29% | -2,20% | +4,64% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 3 | 100,00% | +1,92% | +1,92% | -3,05% | +5,02% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | +1,92% | +1,92% | -3,05% | +5,02% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | +1,92% | +1,92% | -3,05% | +5,02% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 3 | 100,00% | +1,92% | +1,92% | -3,05% | +5,02% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 2 | 0,00% | +1,75% | -1,75% | -2,93% | +5,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 16 | 56,25% | -0,38% | +0,38% | -0,65% | +0,36% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 16 | 56,25% | -0,38% | +0,38% | -0,65% | +0,36% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 16 | 56,25% | -0,38% | +0,38% | -0,65% | +0,36% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | -0,16% | +0,16% | -0,44% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 16 | 56,25% | -0,38% | +0,38% | -0,65% | +0,36% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 15 | 53,33% | -0,32% | +0,32% | -0,58% | +0,35% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,68% | +0,68% | +0,59% | +1,03% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 15 | 60,00% | -0,74% | +0,74% | -1,28% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 15 | 60,00% | -0,74% | +0,74% | -1,28% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 15 | 60,00% | -0,74% | +0,74% | -1,28% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | -0,52% | +0,52% | -1,09% | +0,85% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 15 | 60,00% | -0,74% | +0,74% | -1,28% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 14 | 57,14% | -0,62% | +0,62% | -1,21% | +0,75% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 14 | 57,14% | -0,96% | +0,96% | -2,13% | +1,80% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 14 | 57,14% | -0,96% | +0,96% | -2,13% | +1,80% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 14 | 57,14% | -0,96% | +0,96% | -2,13% | +1,80% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | -0,96% | +0,96% | -2,13% | +1,80% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 14 | 57,14% | -0,96% | +0,96% | -2,13% | +1,80% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 13 | 53,85% | -0,87% | +0,87% | -2,11% | +1,90% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 12 | 66,67% | -1,03% | +1,03% | -2,84% | +2,35% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 12 | 66,67% | -1,03% | +1,03% | -2,84% | +2,35% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 12 | 66,67% | -1,03% | +1,03% | -2,84% | +2,35% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 12 | 66,67% | -1,03% | +1,03% | -2,84% | +2,35% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 12 | 66,67% | -1,03% | +1,03% | -2,84% | +2,35% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 11 | 63,64% | -0,86% | +0,86% | -2,75% | +2,52% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 10 | 80,00% | -1,47% | +1,47% | -3,22% | +2,49% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 10 | 80,00% | -1,47% | +1,47% | -3,22% | +2,49% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 10 | 80,00% | -1,47% | +1,47% | -3,22% | +2,49% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 10 | 80,00% | -1,47% | +1,47% | -3,22% | +2,49% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 10 | 80,00% | -1,47% | +1,47% | -3,22% | +2,49% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 9 | 77,78% | -1,52% | +1,52% | -3,15% | +2,71% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 7 | 71,43% | -2,09% | +2,09% | -3,74% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 7 | 71,43% | -2,09% | +2,09% | -3,74% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 7 | 71,43% | -2,09% | +2,09% | -3,74% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 7 | 71,43% | -2,09% | +2,09% | -3,74% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 7 | 71,43% | -2,09% | +2,09% | -3,74% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 6 | 66,67% | -1,44% | +1,44% | -3,19% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 3 | 100,00% | -4,48% | +4,48% | -5,49% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | -4,48% | +4,48% | -5,49% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | -4,48% | +4,48% | -5,49% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 3 | 100,00% | -4,48% | +4,48% | -5,49% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 3 | 100,00% | -4,48% | +4,48% | -5,49% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 3 | 100,00% | -4,48% | +4,48% | -5,49% | +2,47% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 14 | 42,86% | -0,19% | -0,69% | -0,54% | +0,67% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 12 | 58,33% | -0,89% | -0,17% | -1,10% | -0,06% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 15 | 53,33% | -0,50% | -0,36% | -0,81% | +0,32% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 10 | 40,00% | -0,52% | -0,12% | -1,01% | +0,29% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 16 | 62,50% | -0,28% | +0,06% | -0,62% | +0,50% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 8 | 75,00% | -0,23% | +0,23% | -0,50% | +0,38% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 14 | 21,43% | -0,41% | -1,09% | -1,02% | +0,84% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 11 | 45,45% | -0,97% | -0,55% | -1,71% | +0,14% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 14 | 42,86% | -0,69% | -0,51% | -1,36% | +0,70% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 9 | 33,33% | -0,90% | -0,80% | -1,63% | +0,79% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 15 | 33,33% | -0,49% | -0,28% | -1,10% | +0,87% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 7 | 42,86% | -0,00% | +0,00% | -0,33% | +0,54% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 13 | 15,38% | -0,48% | -1,40% | -2,11% | +2,24% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 10 | 40,00% | -1,04% | -0,27% | -2,77% | +1,67% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 13 | 38,46% | -0,73% | -0,28% | -2,41% | +2,06% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 8 | 37,50% | -0,84% | -1,07% | -2,35% | +2,30% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 14 | 35,71% | -0,57% | -0,28% | -2,14% | +2,17% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 6 | 16,67% | +0,80% | -0,80% | -1,32% | +2,54% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 11 | 36,36% | -0,35% | -1,16% | -2,70% | +3,15% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 8 | 62,50% | -0,46% | -0,04% | -3,18% | +2,58% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 11 | 54,55% | -0,14% | -0,22% | -2,86% | +2,94% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -1,07% | -0,02% | -3,11% | +2,85% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 12 | 33,33% | -0,33% | -1,04% | -2,85% | +2,99% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 5 | 40,00% | +1,33% | -1,33% | -1,45% | +3,95% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 9 | 44,44% | -0,14% | -1,18% | -3,39% | +3,30% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 7 | 71,43% | -0,62% | +0,71% | -3,85% | +2,78% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 10 | 70,00% | -0,46% | +0,53% | -3,51% | +3,12% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -0,52% | -0,22% | -3,76% | +3,04% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 10 | 20,00% | -0,46% | -1,57% | -3,51% | +3,12% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 3 | 33,33% | +0,43% | -0,43% | -1,86% | +4,49% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 6 | 16,67% | -0,43% | -1,70% | -4,48% | +2,76% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 5 | 40,00% | -1,26% | -0,48% | -4,94% | +2,28% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 7 | 28,57% | -0,68% | -0,57% | -4,63% | +2,58% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 6 | 33,33% | -0,43% | -1,35% | -4,48% | +2,76% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 7 | 42,86% | -0,68% | -0,02% | -4,63% | +2,58% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 2 | 0,00% | -2,90% | -2,90% | -5,79% | +1,67% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -1,84% | +1,84% | -5,73% | +1,74% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | -2,78% | +2,78% | -5,70% | +1,62% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 2 | 0,00% | -2,90% | -2,90% | -5,79% | +1,67% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 3 | 0,00% | -2,78% | -2,78% | -5,70% | +1,62% | FEEDBACK RAPIDO |
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
