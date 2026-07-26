# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-26 05:14 UTC

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

Segnali totali salvati: **54**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-26 | BTC | 64.454,23 | +5 | +4 | +3 | +2 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-26 | DOGE | 0.07344 | +2 | +3 | +2 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-07-26 | SOL | 75,10 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-25 | BTC | 64.087,96 | +2 | +3 | +3 | +2 | -2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-25 | DOGE | 0.06949 | -1 | +2 | +1 | +2 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-07-25 | SOL | 74,17 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-24 | BTC | 65.302,77 | 0 | +2 | +2 | +3 | -2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-24 | DOGE | 0.06902 | -5 | -1 | -1 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-24 | SOL | 75,72 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-23 | BTC | 65.399,99 | +1 | +2 | +2 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-23 | DOGE | 0.07229 | -3 | -1 | -1 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-07-23 | SOL | 77,14 | +1 | +3 | +2 | +2 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 18 | 17 | 16 | 15 | 13 | 11 | 8 | 4 | 0 | 0 | 0 | 0 |
| SOL | 18 | 17 | 16 | 15 | 13 | 11 | 8 | 4 | 0 | 0 | 0 | 0 |
| DOGE | 18 | 17 | 16 | 15 | 13 | 11 | 8 | 4 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-13 | 14g | 2026-07-27 | domani |
| SOL | 2026-07-13 | 14g | 2026-07-27 | domani |
| DOGE | 2026-07-13 | 14g | 2026-07-27 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 15 | 40,00% | +0,08% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | 14 | 42,86% | +0,24% | +0,02% | FEEDBACK RAPIDO |
| BTC | 3g | 14 | 42,86% | +0,14% | -0,14% | FEEDBACK RAPIDO |
| BTC | 5g | 12 | 33,33% | +0,83% | -0,23% | FEEDBACK RAPIDO |
| BTC | 7g | 10 | 50,00% | +1,60% | +0,65% | FEEDBACK RAPIDO |
| BTC | 10g | 8 | 75,00% | +2,19% | +2,03% | FEEDBACK RAPIDO |
| BTC | 14g | 4 | 100,00% | +1,69% | +1,69% | FEEDBACK RAPIDO |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 14 | 42,86% | -0,19% | -0,69% | FEEDBACK RAPIDO |
| SOL | 2g | 14 | 21,43% | -0,41% | -1,09% | FEEDBACK RAPIDO |
| SOL | 3g | 14 | 14,29% | -0,64% | -1,49% | FEEDBACK RAPIDO |
| SOL | 5g | 12 | 33,33% | -0,65% | -1,39% | FEEDBACK RAPIDO |
| SOL | 7g | 10 | 50,00% | -0,25% | -0,93% | FEEDBACK RAPIDO |
| SOL | 10g | 7 | 28,57% | -0,53% | -1,29% | FEEDBACK RAPIDO |
| SOL | 14g | 3 | 33,33% | -2,53% | -1,33% | FEEDBACK RAPIDO |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 17 | 52,94% | -0,02% | +0,02% | FEEDBACK RAPIDO |
| DOGE | 2g | 16 | 56,25% | -0,30% | +0,30% | FEEDBACK RAPIDO |
| DOGE | 3g | 15 | 53,33% | -0,79% | +0,79% | FEEDBACK RAPIDO |
| DOGE | 5g | 13 | 61,54% | -0,88% | +0,88% | FEEDBACK RAPIDO |
| DOGE | 7g | 11 | 72,73% | -1,21% | +1,21% | FEEDBACK RAPIDO |
| DOGE | 10g | 8 | 62,50% | -1,76% | +1,76% | FEEDBACK RAPIDO |
| DOGE | 14g | 4 | 75,00% | -3,15% | +3,15% | FEEDBACK RAPIDO |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 15 | 40,00% | +0,08% | +0,11% | -0,14% | +0,76% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 17 | 41,18% | +0,04% | +0,04% | -0,18% | +0,65% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 17 | 41,18% | +0,04% | +0,04% | -0,18% | +0,65% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 13 | 38,46% | -0,02% | -0,02% | -0,25% | +0,51% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 14 | 35,71% | +0,04% | -0,56% | -0,21% | +0,63% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 14 | 42,86% | +0,24% | +0,02% | -0,31% | +1,19% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 16 | 43,75% | +0,16% | +0,16% | -0,34% | +1,07% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 16 | 43,75% | +0,16% | +0,16% | -0,34% | +1,07% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 12 | 41,67% | -0,02% | -0,02% | -0,56% | +0,95% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 13 | 46,15% | +0,31% | -0,23% | -0,21% | +1,21% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 14 | 42,86% | +0,14% | -0,14% | -1,36% | +2,05% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 15 | 60,00% | +0,30% | +0,30% | -1,23% | +2,09% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 15 | 60,00% | +0,30% | +0,30% | -1,23% | +2,09% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 11 | 63,64% | +0,34% | +0,34% | -1,25% | +2,02% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 12 | 41,67% | +0,81% | -0,07% | -0,99% | +2,38% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 12 | 33,33% | +0,83% | -0,23% | -1,96% | +2,98% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 13 | 53,85% | +0,95% | +0,95% | -1,83% | +3,12% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 13 | 53,85% | +0,95% | +0,95% | -1,83% | +3,12% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +1,32% | +1,32% | -1,90% | +3,11% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 11 | 45,45% | +1,16% | -0,83% | -1,61% | +3,33% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 10 | 50,00% | +1,60% | +0,65% | -2,04% | +3,67% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 11 | 72,73% | +1,49% | +1,49% | -1,88% | +3,77% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 11 | 72,73% | +1,49% | +1,49% | -1,88% | +3,77% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 10 | 80,00% | +1,68% | +1,68% | -1,90% | +3,81% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 10 | 40,00% | +1,67% | -0,49% | -1,74% | +3,89% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 8 | 75,00% | +2,19% | +2,03% | -2,36% | +4,37% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 8 | 87,50% | +2,19% | +2,19% | -2,36% | +4,37% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 8 | 87,50% | +2,19% | +2,19% | -2,36% | +4,37% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 8 | 87,50% | +2,19% | +2,19% | -2,36% | +4,37% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 7 | 28,57% | +2,43% | -0,34% | -2,23% | +4,62% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 4 | 100,00% | +1,69% | +1,69% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | +1,69% | +1,69% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | +1,69% | +1,69% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 4 | 100,00% | +1,69% | +1,69% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 3 | 33,33% | +1,50% | -0,83% | -3,03% | +5,05% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 17 | 52,94% | -0,02% | +0,02% | -0,43% | +0,66% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 17 | 58,82% | -0,02% | +0,69% | -0,43% | +0,66% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 17 | 58,82% | -0,02% | +0,69% | -0,43% | +0,66% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 15 | 60,00% | +0,23% | +0,53% | -0,21% | +0,95% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 17 | 52,94% | -0,02% | +0,02% | -0,43% | +0,66% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 16 | 50,00% | +0,05% | -0,05% | -0,35% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 16 | 56,25% | -0,30% | +0,30% | -0,97% | +0,91% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 16 | 56,25% | -0,30% | +0,30% | -0,97% | +0,91% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 16 | 56,25% | -0,30% | +0,30% | -0,97% | +0,91% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | -0,52% | +0,52% | -1,09% | +0,85% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 16 | 56,25% | -0,30% | +0,30% | -0,97% | +0,91% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 15 | 53,33% | -0,16% | +0,16% | -0,88% | +1,11% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +6,40% | +6,40% | +3,75% | +6,18% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 15 | 53,33% | -0,79% | +0,79% | -2,36% | +1,77% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 15 | 53,33% | -0,79% | +0,79% | -2,36% | +1,77% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 15 | 53,33% | -0,79% | +0,79% | -2,36% | +1,77% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | -0,96% | +0,96% | -2,13% | +1,80% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 15 | 53,33% | -0,79% | +0,79% | -2,36% | +1,77% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 14 | 50,00% | -0,70% | +0,70% | -2,36% | +1,87% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 13 | 61,54% | -0,88% | +0,88% | -3,10% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 13 | 61,54% | -0,88% | +0,88% | -3,10% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 13 | 61,54% | -0,88% | +0,88% | -3,10% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 13 | 61,54% | -0,88% | +0,88% | -3,10% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 13 | 61,54% | -0,88% | +0,88% | -3,10% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 12 | 58,33% | -0,71% | +0,71% | -3,04% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 11 | 72,73% | -1,21% | +1,21% | -3,45% | +2,43% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 11 | 72,73% | -1,21% | +1,21% | -3,45% | +2,43% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 11 | 72,73% | -1,21% | +1,21% | -3,45% | +2,43% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 11 | 72,73% | -1,21% | +1,21% | -3,45% | +2,43% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 11 | 72,73% | -1,21% | +1,21% | -3,45% | +2,43% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 10 | 70,00% | -1,23% | +1,23% | -3,40% | +2,63% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 8 | 62,50% | -1,76% | +1,76% | -4,08% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 8 | 62,50% | -1,76% | +1,76% | -4,08% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 8 | 62,50% | -1,76% | +1,76% | -4,08% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 8 | 62,50% | -1,76% | +1,76% | -4,08% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 8 | 62,50% | -1,76% | +1,76% | -4,08% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 7 | 57,14% | -1,15% | +1,15% | -3,67% | +2,89% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 4 | 75,00% | -3,15% | +3,15% | -5,68% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 4 | 75,00% | -3,15% | +3,15% | -5,68% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 4 | 75,00% | -3,15% | +3,15% | -5,68% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 4 | 75,00% | -3,15% | +3,15% | -5,68% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 4 | 75,00% | -3,15% | +3,15% | -5,68% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 4 | 75,00% | -3,15% | +3,15% | -5,68% | +2,68% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 14 | 42,86% | -0,19% | -0,69% | -0,54% | +0,67% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 13 | 61,54% | -0,73% | -0,06% | -0,99% | +0,04% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 16 | 56,25% | -0,39% | -0,26% | -0,73% | +0,38% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 11 | 45,45% | -0,36% | +0,01% | -0,89% | +0,37% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 17 | 58,82% | -0,19% | -0,02% | -0,56% | +0,54% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 9 | 66,67% | -0,06% | +0,06% | -0,41% | +0,48% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 14 | 21,43% | -0,41% | -1,09% | -1,02% | +0,84% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 12 | 41,67% | -0,96% | -0,57% | -1,71% | +0,06% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 15 | 40,00% | -0,70% | -0,53% | -1,38% | +0,60% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 10 | 30,00% | -0,89% | -0,80% | -1,64% | +0,63% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 16 | 37,50% | -0,51% | -0,21% | -1,14% | +0,77% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 8 | 50,00% | -0,11% | +0,11% | -0,50% | +0,37% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 14 | 14,29% | -0,64% | -1,49% | -2,30% | +2,00% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 11 | 36,36% | -1,19% | -0,49% | -2,95% | +1,42% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 14 | 35,71% | -0,87% | -0,45% | -2,58% | +1,84% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 9 | 33,33% | -1,04% | -1,24% | -2,62% | +1,92% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 15 | 40,00% | -0,71% | -0,08% | -2,32% | +1,95% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 7 | 28,57% | +0,30% | -0,30% | -1,81% | +2,01% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 12 | 33,33% | -0,65% | -1,39% | -2,98% | +2,94% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 9 | 55,56% | -0,86% | -0,48% | -3,50% | +2,36% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 12 | 50,00% | -0,46% | -0,53% | -3,13% | +2,75% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 8 | 50,00% | -1,44% | -0,52% | -3,48% | +2,57% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 13 | 38,46% | -0,62% | -0,65% | -3,10% | +2,81% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 5 | 40,00% | +1,33% | -1,33% | -1,45% | +3,95% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 10 | 50,00% | -0,25% | -0,93% | -3,39% | +3,32% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 8 | 75,00% | -0,69% | +0,78% | -3,79% | +2,87% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 11 | 72,73% | -0,53% | +0,59% | -3,50% | +3,16% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -0,52% | -0,22% | -3,76% | +3,04% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 11 | 27,27% | -0,53% | -1,32% | -3,50% | +3,16% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,02% | -0,02% | -2,24% | +4,25% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 7 | 28,57% | -0,53% | -1,29% | -4,33% | +2,87% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 6 | 50,00% | -1,25% | -0,21% | -4,69% | +2,50% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 8 | 37,50% | -0,74% | -0,35% | -4,48% | +2,71% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 6 | 33,33% | -0,43% | -1,35% | -4,48% | +2,76% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 8 | 50,00% | -0,74% | +0,13% | -4,48% | +2,71% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 1 | 100,00% | -1,18% | +1,18% | -3,42% | +3,59% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 3 | 33,33% | -2,53% | -1,33% | -5,20% | +2,16% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | -1,83% | +1,83% | -5,16% | +2,20% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | -2,54% | +2,54% | -5,28% | +2,00% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 3 | 33,33% | -2,53% | -1,33% | -5,20% | +2,16% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 4 | 0,00% | -2,54% | -2,54% | -5,28% | +2,00% | FEEDBACK RAPIDO |
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
