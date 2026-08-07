# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-07 05:17 UTC

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

Segnali totali salvati: **90**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-07 | BTC | 64.173,65 | +6 | +4 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-07 | DOGE | 0.06903 | +1 | +2 | +1 | +2 | -1 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-07 | SOL | 72,63 | +1 | +4 | +3 | +3 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-06 | BTC | 64.856,39 | +6 | +4 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-06 | DOGE | 0.06999 | +2 | +2 | +1 | +2 | 0 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-06 | SOL | 74,14 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-05 | BTC | 64.252,74 | +2 | +4 | +3 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-05 | DOGE | 0.06992 | 0 | +2 | +1 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-05 | SOL | 73,88 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-04 | BTC | 63.800,01 | +5 | +4 | +3 | +3 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-04 | DOGE | 0.07017 | +1 | +2 | +1 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-04 | SOL | 73,68 | 0 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 30 | 29 | 28 | 27 | 25 | 23 | 20 | 16 | 9 | 0 | 0 | 0 |
| SOL | 30 | 29 | 28 | 27 | 25 | 23 | 20 | 16 | 9 | 0 | 0 | 0 |
| DOGE | 30 | 29 | 28 | 27 | 25 | 23 | 20 | 16 | 9 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-09 | 30g | 2026-08-08 | domani |
| SOL | 2026-07-09 | 30g | 2026-08-08 | domani |
| DOGE | 2026-07-09 | 30g | 2026-08-08 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 27 | 48,15% | +0,03% | -0,01% | FEEDBACK RAPIDO |
| BTC | 2g | 26 | 42,31% | +0,16% | -0,02% | FEEDBACK RAPIDO |
| BTC | 3g | 25 | 40,00% | +0,05% | -0,23% | FEEDBACK RAPIDO |
| BTC | 5g | 23 | 26,09% | +0,15% | -0,40% | FEEDBACK RAPIDO |
| BTC | 7g | 21 | 38,10% | +0,19% | -0,32% | FEEDBACK RAPIDO |
| BTC | 10g | 18 | 33,33% | +0,48% | -0,03% | FEEDBACK RAPIDO |
| BTC | 14g | 14 | 50,00% | +0,10% | -0,03% | FEEDBACK RAPIDO |
| BTC | 21g | 9 | 33,33% | +0,37% | -0,10% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 22 | 50,00% | -0,17% | -0,45% | FEEDBACK RAPIDO |
| SOL | 2g | 21 | 38,10% | -0,34% | -0,67% | FEEDBACK RAPIDO |
| SOL | 3g | 20 | 40,00% | -0,32% | -0,76% | FEEDBACK RAPIDO |
| SOL | 5g | 19 | 42,11% | -0,74% | -1,03% | FEEDBACK RAPIDO |
| SOL | 7g | 17 | 47,06% | -1,12% | -0,82% | FEEDBACK RAPIDO |
| SOL | 10g | 15 | 40,00% | -1,87% | -0,45% | FEEDBACK RAPIDO |
| SOL | 14g | 14 | 57,14% | -3,18% | +0,21% | FEEDBACK RAPIDO |
| SOL | 21g | 8 | 62,50% | -4,07% | -0,09% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 27 | 40,74% | -0,09% | -0,11% | FEEDBACK RAPIDO |
| DOGE | 2g | 26 | 42,31% | -0,21% | -0,22% | FEEDBACK RAPIDO |
| DOGE | 3g | 26 | 42,31% | -0,43% | +0,00% | FEEDBACK RAPIDO |
| DOGE | 5g | 24 | 58,33% | -0,80% | +0,28% | FEEDBACK RAPIDO |
| DOGE | 7g | 22 | 63,64% | -1,21% | +0,79% | FEEDBACK RAPIDO |
| DOGE | 10g | 19 | 57,89% | -1,93% | +1,29% | FEEDBACK RAPIDO |
| DOGE | 14g | 16 | 81,25% | -2,93% | +2,93% | FEEDBACK RAPIDO |
| DOGE | 21g | 9 | 100,00% | -4,26% | +4,26% | FEEDBACK RAPIDO |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 27 | 48,15% | +0,03% | -0,01% | -0,31% | +0,60% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 29 | 51,72% | +0,01% | +0,01% | -0,32% | +0,55% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 29 | 51,72% | +0,01% | +0,01% | -0,32% | +0,55% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 25 | 52,00% | -0,02% | -0,02% | -0,38% | +0,46% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 24 | 33,33% | +0,22% | -0,44% | -0,14% | +0,76% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 4 | 0,00% | +0,76% | -0,76% | +0,03% | +1,12% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 26 | 42,31% | +0,16% | -0,02% | -0,36% | +0,88% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 28 | 46,43% | +0,12% | +0,12% | -0,38% | +0,83% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 28 | 46,43% | +0,12% | +0,12% | -0,38% | +0,83% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 24 | 45,83% | +0,02% | +0,02% | -0,49% | +0,73% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 23 | 43,48% | +0,37% | -0,33% | -0,11% | +1,09% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 4 | 25,00% | +0,86% | -0,86% | +0,50% | +1,73% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 25 | 40,00% | +0,05% | -0,23% | -1,40% | +1,81% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 27 | 55,56% | +0,14% | +0,14% | -1,36% | +1,78% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 27 | 55,56% | +0,14% | +0,14% | -1,36% | +1,78% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 23 | 56,52% | +0,13% | +0,13% | -1,40% | +1,69% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 22 | 40,91% | +0,62% | -0,24% | -1,05% | +2,19% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,18% | -1,18% | -0,41% | +2,46% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 23 | 26,09% | +0,15% | -0,40% | -2,30% | +2,32% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 25 | 40,00% | +0,15% | +0,15% | -2,24% | +2,34% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 25 | 40,00% | +0,15% | +0,15% | -2,24% | +2,34% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 21 | 42,86% | +0,28% | +0,28% | -2,26% | +2,34% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 20 | 50,00% | +0,46% | -0,30% | -1,94% | +2,74% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 3 | 33,33% | +0,35% | -0,35% | -1,83% | +2,72% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 21 | 38,10% | +0,19% | -0,32% | -2,55% | +2,68% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 23 | 52,17% | +0,12% | +0,12% | -2,51% | +2,67% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 23 | 52,17% | +0,12% | +0,12% | -2,51% | +2,67% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 19 | 57,89% | +0,43% | +0,43% | -2,50% | +2,74% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 18 | 38,89% | +0,79% | -0,31% | -2,15% | +3,11% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 2 | 0,00% | +0,60% | -0,60% | -2,23% | +2,64% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 18 | 33,33% | +0,48% | -0,03% | -2,78% | +3,20% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 20 | 45,00% | +0,20% | +0,20% | -2,80% | +3,14% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 20 | 45,00% | +0,20% | +0,20% | -2,80% | +3,14% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 16 | 56,25% | +0,76% | +0,76% | -2,64% | +3,33% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 16 | 43,75% | +0,67% | +0,05% | -2,40% | +3,64% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 1 | 0,00% | +1,25% | -1,25% | -1,82% | +3,07% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 14 | 50,00% | +0,10% | -0,03% | -3,06% | +4,06% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 16 | 43,75% | -0,10% | -0,10% | -3,09% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 16 | 43,75% | -0,10% | -0,10% | -3,09% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 12 | 58,33% | +0,69% | +0,69% | -2,65% | +4,39% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 13 | 53,85% | +0,13% | +0,18% | -2,70% | +4,27% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 9 | 33,33% | +0,37% | -0,10% | -2,48% | +5,20% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 9 | 55,56% | +0,37% | +0,37% | -2,48% | +5,20% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 9 | 55,56% | +0,37% | +0,37% | -2,48% | +5,20% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 9 | 55,56% | +0,37% | +0,37% | -2,48% | +5,20% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 8 | 12,50% | +0,32% | -0,60% | -2,38% | +5,26% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 27 | 40,74% | -0,09% | -0,11% | -0,54% | +0,57% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 29 | 55,17% | -0,22% | +0,19% | -0,69% | +0,42% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 29 | 55,17% | -0,22% | +0,19% | -0,69% | +0,42% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 27 | 55,56% | -0,10% | +0,07% | -0,58% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 28 | 50,00% | -0,18% | +0,18% | -0,66% | +0,47% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 20 | 40,00% | +0,13% | -0,13% | -0,37% | +0,71% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 26 | 42,31% | -0,21% | -0,22% | -0,84% | +0,76% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 28 | 46,43% | -0,35% | -0,02% | -0,97% | +0,59% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 28 | 46,43% | -0,35% | -0,02% | -0,97% | +0,59% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 26 | 46,15% | -0,48% | +0,08% | -1,04% | +0,53% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 28 | 60,71% | -0,35% | +0,35% | -0,97% | +0,59% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 20 | 50,00% | +0,13% | -0,13% | -0,57% | +1,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 26 | 42,31% | -0,43% | +0,00% | -2,02% | +1,82% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 27 | 48,15% | -0,58% | -0,12% | -2,12% | +1,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 27 | 48,15% | -0,58% | -0,12% | -2,12% | +1,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 25 | 52,00% | -0,92% | +0,16% | -2,08% | +1,49% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 27 | 51,85% | -0,58% | +0,58% | -2,12% | +1,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 20 | 40,00% | -0,14% | +0,14% | -1,99% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 24 | 58,33% | -0,80% | +0,28% | -3,03% | +2,21% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 25 | 52,00% | -0,92% | +0,10% | -3,12% | +2,03% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 25 | 52,00% | -0,92% | +0,10% | -3,12% | +2,03% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 23 | 52,17% | -0,96% | +0,07% | -3,16% | +1,82% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 25 | 64,00% | -0,92% | +0,92% | -3,12% | +2,03% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 20 | 55,00% | -0,45% | +0,45% | -2,87% | +2,58% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 22 | 63,64% | -1,21% | +0,79% | -3,64% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 23 | 60,87% | -1,34% | +0,52% | -3,77% | +2,21% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 23 | 60,87% | -1,34% | +0,52% | -3,77% | +2,21% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 21 | 61,90% | -1,36% | +0,47% | -3,88% | +2,00% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 23 | 65,22% | -1,34% | +1,34% | -3,77% | +2,21% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 19 | 57,89% | -1,06% | +1,06% | -3,47% | +2,74% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 19 | 57,89% | -1,93% | +1,29% | -4,56% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 20 | 60,00% | -2,04% | +1,13% | -4,67% | +2,32% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 20 | 60,00% | -2,04% | +1,13% | -4,67% | +2,32% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 18 | 61,11% | -2,17% | +1,16% | -4,80% | +2,08% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 20 | 70,00% | -2,04% | +2,04% | -4,67% | +2,32% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 17 | 64,71% | -1,53% | +1,53% | -4,24% | +2,85% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 16 | 81,25% | -2,93% | +2,93% | -5,67% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 16 | 81,25% | -2,93% | +2,93% | -5,67% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 16 | 81,25% | -2,93% | +2,93% | -5,67% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 14 | 85,71% | -3,12% | +3,12% | -5,95% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 16 | 81,25% | -2,93% | +2,93% | -5,67% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 15 | 80,00% | -2,82% | +2,82% | -5,54% | +2,70% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,01% | +0,01% | -1,52% | +6,93% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 9 | 100,00% | -4,26% | +4,26% | -6,68% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 9 | 100,00% | -4,26% | +4,26% | -6,68% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 9 | 100,00% | -4,26% | +4,26% | -6,68% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 9 | 100,00% | -4,26% | +4,26% | -6,68% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 9 | 100,00% | -4,26% | +4,26% | -6,68% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 8 | 100,00% | -4,11% | +4,11% | -6,51% | +2,82% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 22 | 50,00% | -0,17% | -0,45% | -0,67% | +0,54% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 25 | 60,00% | -0,51% | -0,16% | -0,96% | +0,14% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 28 | 57,14% | -0,34% | -0,26% | -0,82% | +0,33% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 23 | 52,17% | -0,31% | -0,14% | -0,91% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 29 | 51,72% | -0,22% | +0,10% | -0,71% | +0,42% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 20 | 50,00% | -0,09% | +0,09% | -0,63% | +0,46% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 21 | 38,10% | -0,34% | -0,67% | -0,97% | +0,63% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 24 | 45,83% | -0,61% | -0,42% | -1,32% | +0,16% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 27 | 44,44% | -0,51% | -0,41% | -1,18% | +0,45% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 22 | 40,91% | -0,55% | -0,51% | -1,25% | +0,42% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 28 | 42,86% | -0,40% | -0,00% | -1,05% | +0,55% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 20 | 50,00% | -0,20% | +0,20% | -0,76% | +0,30% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 20 | 40,00% | -0,32% | -0,76% | -2,18% | +1,82% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 23 | 39,13% | -0,82% | -0,48% | -2,57% | +1,41% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 26 | 38,46% | -0,69% | -0,46% | -2,41% | +1,64% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 21 | 38,10% | -0,72% | -0,80% | -2,39% | +1,63% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 27 | 48,15% | -0,61% | +0,16% | -2,27% | +1,71% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 19 | 47,37% | -0,19% | +0,19% | -2,07% | +1,63% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 19 | 42,11% | -0,74% | -1,03% | -3,19% | +2,33% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 21 | 42,86% | -1,16% | -0,82% | -3,58% | +1,90% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 24 | 41,67% | -0,92% | -0,81% | -3,39% | +2,15% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 19 | 36,84% | -1,38% | -1,00% | -3,47% | +2,02% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 25 | 56,00% | -0,98% | +0,32% | -3,36% | +2,21% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 17 | 64,71% | -0,59% | +0,59% | -3,00% | +2,26% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 17 | 47,06% | -1,12% | -0,82% | -4,02% | +2,60% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 19 | 52,63% | -1,71% | -0,50% | -4,41% | +2,13% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 22 | 54,55% | -1,49% | -0,42% | -4,18% | +2,37% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 17 | 41,18% | -1,47% | -1,35% | -4,32% | +2,23% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 23 | 47,83% | -1,40% | +0,52% | -4,14% | +2,42% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 15 | 60,00% | -1,34% | +1,34% | -3,93% | +2,49% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 15 | 40,00% | -1,87% | -0,45% | -4,59% | +2,76% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 16 | 31,25% | -2,20% | -0,85% | -5,25% | +2,21% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 19 | 31,58% | -1,88% | -0,68% | -4,96% | +2,48% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 14 | 14,29% | -1,77% | -2,16% | -5,14% | +2,35% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 20 | 75,00% | -1,96% | +1,72% | -4,95% | +2,54% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 12 | 91,67% | -2,42% | +2,42% | -4,93% | +2,67% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 14 | 57,14% | -3,18% | +0,21% | -5,68% | +2,77% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 12 | 58,33% | -3,15% | -0,02% | -6,09% | +2,27% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 15 | 66,67% | -3,14% | +0,60% | -5,65% | +2,60% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 10 | 10,00% | -3,12% | -2,77% | -5,62% | +2,47% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 16 | 68,75% | -3,19% | +1,93% | -5,73% | +2,66% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 8 | 100,00% | -3,47% | +3,47% | -6,05% | +2,98% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 8 | 62,50% | -4,07% | -0,09% | -6,88% | +3,12% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 7 | 85,71% | -4,23% | +2,87% | -7,04% | +2,83% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 9 | 88,89% | -4,14% | +3,08% | -6,87% | +2,94% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 6 | 33,33% | -4,46% | -1,63% | -7,03% | +2,76% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 9 | 55,56% | -4,14% | -0,44% | -6,87% | +2,94% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 2 | 100,00% | -2,87% | +2,87% | -6,43% | +4,20% | FEEDBACK RAPIDO |
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
