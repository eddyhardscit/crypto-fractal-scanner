# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-06 05:16 UTC

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

Segnali totali salvati: **87**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-06 | BTC | 64.856,39 | +6 | +4 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-06 | DOGE | 0.06999 | +2 | +2 | +1 | +2 | 0 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-06 | SOL | 74,14 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-05 | BTC | 64.252,74 | +2 | +4 | +3 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-05 | DOGE | 0.06992 | 0 | +2 | +1 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-05 | SOL | 73,88 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-04 | BTC | 63.800,01 | +5 | +4 | +3 | +3 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-04 | DOGE | 0.07017 | +1 | +2 | +1 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-04 | SOL | 73,68 | 0 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-03 | BTC | 62.745,61 | +2 | +4 | +3 | +3 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-03 | DOGE | 0.06985 | -2 | +2 | +1 | +2 | -3 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-08-03 | SOL | 72,93 | +1 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 29 | 28 | 27 | 26 | 24 | 22 | 19 | 15 | 8 | 0 | 0 | 0 |
| SOL | 29 | 28 | 27 | 26 | 24 | 22 | 19 | 15 | 8 | 0 | 0 | 0 |
| DOGE | 29 | 28 | 27 | 26 | 24 | 22 | 19 | 15 | 8 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-17 | 21g | 2026-08-07 | domani |
| SOL | 2026-07-17 | 21g | 2026-08-07 | domani |
| DOGE | 2026-07-17 | 21g | 2026-08-07 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 26 | 50,00% | +0,08% | +0,03% | FEEDBACK RAPIDO |
| BTC | 2g | 25 | 44,00% | +0,17% | -0,02% | FEEDBACK RAPIDO |
| BTC | 3g | 24 | 37,50% | +0,03% | -0,27% | FEEDBACK RAPIDO |
| BTC | 5g | 22 | 22,73% | +0,10% | -0,47% | FEEDBACK RAPIDO |
| BTC | 7g | 20 | 40,00% | +0,21% | -0,33% | FEEDBACK RAPIDO |
| BTC | 10g | 17 | 35,29% | +0,43% | +0,05% | FEEDBACK RAPIDO |
| BTC | 14g | 14 | 50,00% | +0,10% | -0,03% | FEEDBACK RAPIDO |
| BTC | 21g | 8 | 37,50% | +0,31% | -0,01% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 21 | 52,38% | -0,08% | -0,38% | FEEDBACK RAPIDO |
| SOL | 2g | 20 | 40,00% | -0,27% | -0,62% | FEEDBACK RAPIDO |
| SOL | 3g | 20 | 40,00% | -0,32% | -0,76% | FEEDBACK RAPIDO |
| SOL | 5g | 18 | 44,44% | -0,72% | -1,02% | FEEDBACK RAPIDO |
| SOL | 7g | 16 | 43,75% | -1,08% | -0,99% | FEEDBACK RAPIDO |
| SOL | 10g | 14 | 42,86% | -1,94% | -0,42% | FEEDBACK RAPIDO |
| SOL | 14g | 14 | 57,14% | -3,18% | +0,21% | FEEDBACK RAPIDO |
| SOL | 21g | 7 | 57,14% | -4,18% | -0,57% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 26 | 42,31% | -0,04% | -0,06% | FEEDBACK RAPIDO |
| DOGE | 2g | 26 | 42,31% | -0,21% | -0,22% | FEEDBACK RAPIDO |
| DOGE | 3g | 25 | 44,00% | -0,39% | +0,07% | FEEDBACK RAPIDO |
| DOGE | 5g | 23 | 60,87% | -0,76% | +0,36% | FEEDBACK RAPIDO |
| DOGE | 7g | 21 | 61,90% | -1,20% | +0,76% | FEEDBACK RAPIDO |
| DOGE | 10g | 18 | 61,11% | -1,97% | +1,44% | FEEDBACK RAPIDO |
| DOGE | 14g | 15 | 86,67% | -3,12% | +3,12% | FEEDBACK RAPIDO |
| DOGE | 21g | 8 | 100,00% | -4,25% | +4,25% | FEEDBACK RAPIDO |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 26 | 50,00% | +0,08% | +0,03% | -0,28% | +0,65% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 28 | 53,57% | +0,05% | +0,05% | -0,29% | +0,60% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 28 | 53,57% | +0,05% | +0,05% | -0,29% | +0,60% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 24 | 54,17% | +0,02% | +0,02% | -0,35% | +0,51% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 23 | 34,78% | +0,27% | -0,41% | -0,10% | +0,82% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 4 | 0,00% | +0,76% | -0,76% | +0,03% | +1,12% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 25 | 44,00% | +0,17% | -0,02% | -0,37% | +0,90% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 27 | 48,15% | +0,13% | +0,13% | -0,38% | +0,86% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 27 | 48,15% | +0,13% | +0,13% | -0,38% | +0,86% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 23 | 47,83% | +0,03% | +0,03% | -0,50% | +0,75% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 22 | 40,91% | +0,40% | -0,35% | -0,11% | +1,13% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 4 | 25,00% | +0,86% | -0,86% | +0,50% | +1,73% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 24 | 37,50% | +0,03% | -0,27% | -1,46% | +1,81% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 26 | 53,85% | +0,12% | +0,12% | -1,42% | +1,78% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 26 | 53,85% | +0,12% | +0,12% | -1,42% | +1,78% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 22 | 54,55% | +0,11% | +0,11% | -1,46% | +1,69% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 21 | 38,10% | +0,62% | -0,28% | -1,10% | +2,21% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,18% | -1,18% | -0,41% | +2,46% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 22 | 22,73% | +0,10% | -0,47% | -2,32% | +2,31% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 24 | 37,50% | +0,10% | +0,10% | -2,25% | +2,34% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 24 | 37,50% | +0,10% | +0,10% | -2,25% | +2,34% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 20 | 40,00% | +0,24% | +0,24% | -2,28% | +2,33% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 19 | 52,63% | +0,42% | -0,25% | -1,94% | +2,76% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 3 | 33,33% | +0,35% | -0,35% | -1,83% | +2,72% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 20 | 40,00% | +0,21% | -0,33% | -2,51% | +2,76% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 22 | 54,55% | +0,14% | +0,14% | -2,47% | +2,75% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 22 | 54,55% | +0,14% | +0,14% | -2,47% | +2,75% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 18 | 61,11% | +0,47% | +0,47% | -2,46% | +2,84% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 18 | 38,89% | +0,79% | -0,31% | -2,15% | +3,11% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 2 | 0,00% | +0,60% | -0,60% | -2,23% | +2,64% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 17 | 35,29% | +0,43% | +0,05% | -2,83% | +3,20% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 19 | 42,11% | +0,14% | +0,14% | -2,85% | +3,14% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 19 | 42,11% | +0,14% | +0,14% | -2,85% | +3,14% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 15 | 53,33% | +0,73% | +0,73% | -2,70% | +3,35% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 15 | 46,67% | +0,63% | +0,13% | -2,44% | +3,68% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 14 | 50,00% | +0,10% | -0,03% | -3,06% | +4,06% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 15 | 46,67% | +0,01% | +0,01% | -2,98% | +4,11% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 15 | 46,67% | +0,01% | +0,01% | -2,98% | +4,11% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 11 | 63,64% | +0,91% | +0,91% | -2,46% | +4,74% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 12 | 50,00% | +0,29% | +0,05% | -2,53% | +4,58% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 8 | 37,50% | +0,31% | -0,01% | -2,52% | +5,21% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 8 | 50,00% | +0,31% | +0,31% | -2,52% | +5,21% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 8 | 50,00% | +0,31% | +0,31% | -2,52% | +5,21% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 8 | 50,00% | +0,31% | +0,31% | -2,52% | +5,21% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 7 | 14,29% | +0,24% | -0,56% | -2,41% | +5,27% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 26 | 42,31% | -0,04% | -0,06% | -0,51% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 28 | 57,14% | -0,18% | +0,25% | -0,66% | +0,47% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 28 | 57,14% | -0,18% | +0,25% | -0,66% | +0,47% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 26 | 57,69% | -0,05% | +0,12% | -0,55% | +0,62% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 28 | 50,00% | -0,18% | +0,18% | -0,66% | +0,47% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 20 | 40,00% | +0,13% | -0,13% | -0,37% | +0,71% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 26 | 42,31% | -0,21% | -0,22% | -0,84% | +0,76% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 27 | 48,15% | -0,32% | +0,03% | -0,96% | +0,64% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 27 | 48,15% | -0,32% | +0,03% | -0,96% | +0,64% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 25 | 48,00% | -0,45% | +0,13% | -1,02% | +0,58% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 27 | 59,26% | -0,32% | +0,32% | -0,96% | +0,64% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 20 | 50,00% | +0,13% | -0,13% | -0,57% | +1,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 25 | 44,00% | -0,39% | +0,07% | -2,02% | +1,88% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 26 | 50,00% | -0,54% | -0,06% | -2,13% | +1,72% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 26 | 50,00% | -0,54% | -0,06% | -2,13% | +1,72% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 24 | 54,17% | -0,89% | +0,24% | -2,09% | +1,54% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 26 | 50,00% | -0,54% | +0,54% | -2,13% | +1,72% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 20 | 40,00% | -0,14% | +0,14% | -1,99% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 23 | 60,87% | -0,76% | +0,36% | -3,08% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 24 | 54,17% | -0,89% | +0,18% | -3,17% | +2,09% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 24 | 54,17% | -0,89% | +0,18% | -3,17% | +2,09% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 22 | 54,55% | -0,93% | +0,15% | -3,22% | +1,87% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 24 | 62,50% | -0,89% | +0,89% | -3,17% | +2,09% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 20 | 55,00% | -0,45% | +0,45% | -2,87% | +2,58% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 21 | 61,90% | -1,20% | +0,76% | -3,67% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 22 | 63,64% | -1,33% | +0,62% | -3,81% | +2,24% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 22 | 63,64% | -1,33% | +0,62% | -3,81% | +2,24% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 20 | 65,00% | -1,36% | +0,57% | -3,92% | +2,02% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 22 | 63,64% | -1,33% | +1,33% | -3,81% | +2,24% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 18 | 55,56% | -1,04% | +1,04% | -3,50% | +2,80% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 18 | 61,11% | -1,97% | +1,44% | -4,66% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 19 | 63,16% | -2,08% | +1,26% | -4,77% | +2,35% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 19 | 63,16% | -2,08% | +1,26% | -4,77% | +2,35% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 17 | 64,71% | -2,22% | +1,30% | -4,91% | +2,10% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 19 | 68,42% | -2,08% | +2,08% | -4,77% | +2,35% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 16 | 62,50% | -1,54% | +1,54% | -4,33% | +2,91% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 15 | 86,67% | -3,12% | +3,12% | -5,95% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 15 | 86,67% | -3,12% | +3,12% | -5,95% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 15 | 86,67% | -3,12% | +3,12% | -5,95% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 14 | 85,71% | -3,12% | +3,12% | -5,95% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 15 | 86,67% | -3,12% | +3,12% | -5,95% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 14 | 85,71% | -3,03% | +3,03% | -5,83% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 8 | 100,00% | -4,25% | +4,25% | -6,79% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 8 | 100,00% | -4,25% | +4,25% | -6,79% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 8 | 100,00% | -4,25% | +4,25% | -6,79% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 8 | 100,00% | -4,25% | +4,25% | -6,79% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 8 | 100,00% | -4,25% | +4,25% | -6,79% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 7 | 100,00% | -4,08% | +4,08% | -6,60% | +2,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 21 | 52,38% | -0,08% | -0,38% | -0,60% | +0,65% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 24 | 62,50% | -0,44% | -0,08% | -0,91% | +0,22% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 27 | 59,26% | -0,27% | -0,20% | -0,77% | +0,41% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 22 | 54,55% | -0,23% | -0,05% | -0,85% | +0,41% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 28 | 50,00% | -0,16% | +0,03% | -0,66% | +0,50% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 20 | 50,00% | -0,09% | +0,09% | -0,63% | +0,46% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 20 | 40,00% | -0,27% | -0,62% | -0,93% | +0,73% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 23 | 47,83% | -0,57% | -0,37% | -1,30% | +0,23% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 26 | 46,15% | -0,46% | -0,36% | -1,15% | +0,52% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 21 | 42,86% | -0,50% | -0,45% | -1,22% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 27 | 40,74% | -0,36% | -0,07% | -1,02% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 19 | 47,37% | -0,12% | +0,12% | -0,70% | +0,39% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 20 | 40,00% | -0,32% | -0,76% | -2,18% | +1,82% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 22 | 40,91% | -0,79% | -0,44% | -2,61% | +1,41% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 25 | 40,00% | -0,66% | -0,42% | -2,44% | +1,65% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 20 | 40,00% | -0,68% | -0,77% | -2,43% | +1,64% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 26 | 46,15% | -0,57% | +0,12% | -2,30% | +1,72% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 18 | 44,44% | -0,12% | +0,12% | -2,09% | +1,65% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 18 | 44,44% | -0,72% | -1,02% | -3,26% | +2,36% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 20 | 45,00% | -1,16% | -0,81% | -3,66% | +1,91% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 23 | 43,48% | -0,92% | -0,79% | -3,45% | +2,17% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 18 | 38,89% | -1,40% | -0,99% | -3,56% | +2,04% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 24 | 54,17% | -0,98% | +0,29% | -3,42% | +2,23% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 16 | 62,50% | -0,56% | +0,56% | -3,06% | +2,30% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 16 | 43,75% | -1,08% | -0,99% | -3,98% | +2,71% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 18 | 55,56% | -1,70% | -0,43% | -4,40% | +2,20% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 21 | 57,14% | -1,47% | -0,35% | -4,16% | +2,44% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 16 | 43,75% | -1,44% | -1,31% | -4,30% | +2,31% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 22 | 45,45% | -1,38% | +0,46% | -4,12% | +2,49% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 14 | 57,14% | -1,30% | +1,30% | -3,89% | +2,61% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 14 | 42,86% | -1,94% | -0,42% | -4,67% | +2,77% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 15 | 33,33% | -2,29% | -0,84% | -5,36% | +2,19% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 18 | 33,33% | -1,94% | -0,67% | -5,04% | +2,48% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 13 | 15,38% | -1,84% | -2,26% | -5,27% | +2,34% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 19 | 73,68% | -2,01% | +1,76% | -5,03% | +2,54% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 11 | 90,91% | -2,56% | +2,56% | -5,06% | +2,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 14 | 57,14% | -3,18% | +0,21% | -5,68% | +2,77% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 11 | 63,64% | -3,06% | +0,34% | -6,04% | +2,28% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 14 | 71,43% | -3,07% | +0,93% | -5,58% | +2,63% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 9 | 11,11% | -3,01% | -2,62% | -5,50% | +2,50% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 15 | 66,67% | -3,14% | +1,78% | -5,67% | +2,69% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 7 | 100,00% | -3,38% | +3,38% | -5,97% | +3,10% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 7 | 57,14% | -4,18% | -0,57% | -7,02% | +2,87% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 6 | 83,33% | -4,38% | +2,80% | -7,23% | +2,50% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 8 | 87,50% | -4,24% | +3,06% | -7,00% | +2,71% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 6 | 33,33% | -4,46% | -1,63% | -7,03% | +2,76% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 8 | 50,00% | -4,24% | -0,90% | -7,00% | +2,71% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 1 | 100,00% | -2,45% | +2,45% | -6,98% | +3,59% | FEEDBACK RAPIDO |
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
