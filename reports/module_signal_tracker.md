# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-29 05:15 UTC

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

Segnali totali salvati: **63**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-29 | BTC | 63.913,12 | +2 | +4 | +3 | +3 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-29 | DOGE | 0.07061 | +1 | +4 | +3 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-07-29 | SOL | 73,48 | 0 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-28 | BTC | 63.381,14 | -1 | +3 | +2 | +2 | -2 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-07-28 | DOGE | 0.06994 | +1 | +4 | +3 | +2 | -3 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-07-28 | SOL | 73,27 | +1 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-27 | BTC | 65.325,99 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-27 | DOGE | 0.07289 | 0 | +3 | +2 | +2 | -3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-07-27 | SOL | 76,40 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-26 | BTC | 64.454,23 | +5 | +4 | +3 | +2 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-26 | DOGE | 0.07344 | +2 | +3 | +2 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-07-26 | SOL | 75,10 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 21 | 20 | 19 | 18 | 16 | 14 | 11 | 7 | 0 | 0 | 0 | 0 |
| SOL | 21 | 20 | 19 | 18 | 16 | 14 | 11 | 7 | 0 | 0 | 0 | 0 |
| DOGE | 21 | 20 | 19 | 18 | 16 | 14 | 11 | 7 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-09 | 21g | 2026-07-30 | domani |
| SOL | 2026-07-09 | 21g | 2026-07-30 | domani |
| DOGE | 2026-07-09 | 21g | 2026-07-30 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 18 | 38,89% | +0,03% | -0,04% | FEEDBACK RAPIDO |
| BTC | 2g | 17 | 41,18% | +0,08% | -0,09% | FEEDBACK RAPIDO |
| BTC | 3g | 16 | 37,50% | +0,00% | -0,25% | FEEDBACK RAPIDO |
| BTC | 5g | 14 | 28,57% | +0,39% | -0,51% | FEEDBACK RAPIDO |
| BTC | 7g | 13 | 46,15% | +0,85% | +0,12% | FEEDBACK RAPIDO |
| BTC | 10g | 10 | 60,00% | +1,89% | +1,23% | FEEDBACK RAPIDO |
| BTC | 14g | 7 | 85,71% | +1,60% | +1,60% | FEEDBACK RAPIDO |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 15 | 46,67% | -0,16% | -0,63% | FEEDBACK RAPIDO |
| SOL | 2g | 14 | 21,43% | -0,41% | -1,09% | FEEDBACK RAPIDO |
| SOL | 3g | 14 | 14,29% | -0,64% | -1,49% | FEEDBACK RAPIDO |
| SOL | 5g | 14 | 35,71% | -1,05% | -1,42% | FEEDBACK RAPIDO |
| SOL | 7g | 13 | 46,15% | -1,07% | -0,82% | FEEDBACK RAPIDO |
| SOL | 10g | 10 | 40,00% | -0,76% | -0,51% | FEEDBACK RAPIDO |
| SOL | 14g | 6 | 33,33% | -2,51% | -1,18% | FEEDBACK RAPIDO |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 19 | 52,63% | -0,01% | +0,03% | FEEDBACK RAPIDO |
| DOGE | 2g | 18 | 50,00% | -0,26% | -0,27% | FEEDBACK RAPIDO |
| DOGE | 3g | 18 | 44,44% | -0,53% | +0,10% | FEEDBACK RAPIDO |
| DOGE | 5g | 16 | 62,50% | -0,80% | +0,80% | FEEDBACK RAPIDO |
| DOGE | 7g | 14 | 71,43% | -1,38% | +1,38% | FEEDBACK RAPIDO |
| DOGE | 10g | 11 | 63,64% | -1,72% | +1,72% | FEEDBACK RAPIDO |
| DOGE | 14g | 7 | 71,43% | -2,73% | +2,73% | FEEDBACK RAPIDO |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 18 | 38,89% | +0,03% | -0,04% | -0,25% | +0,63% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 20 | 45,00% | -0,00% | -0,00% | -0,27% | +0,55% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 20 | 45,00% | -0,00% | -0,00% | -0,27% | +0,55% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 16 | 43,75% | -0,07% | -0,07% | -0,35% | +0,41% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 16 | 37,50% | +0,17% | -0,46% | -0,12% | +0,70% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 1 | 0,00% | +0,84% | -0,84% | +0,30% | +1,01% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 17 | 41,18% | +0,08% | -0,09% | -0,46% | +0,91% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 19 | 42,11% | +0,03% | +0,03% | -0,47% | +0,84% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 19 | 42,11% | +0,03% | +0,03% | -0,47% | +0,84% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 15 | 40,00% | -0,15% | -0,15% | -0,68% | +0,68% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 15 | 40,00% | +0,29% | -0,44% | -0,24% | +1,10% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 16 | 37,50% | +0,00% | -0,25% | -1,37% | +2,05% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 18 | 55,56% | +0,14% | +0,14% | -1,32% | +1,97% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 18 | 55,56% | +0,14% | +0,14% | -1,32% | +1,97% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | +0,13% | +0,13% | -1,36% | +1,88% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 15 | 40,00% | +0,52% | -0,04% | -1,15% | +2,18% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 14 | 28,57% | +0,39% | -0,51% | -2,21% | +2,60% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 16 | 43,75% | +0,36% | +0,36% | -2,11% | +2,61% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 16 | 43,75% | +0,36% | +0,36% | -2,11% | +2,61% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 12 | 50,00% | +0,66% | +0,66% | -2,11% | +2,68% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 13 | 53,85% | +0,58% | -0,30% | -1,84% | +2,90% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 13 | 46,15% | +0,85% | +0,12% | -2,23% | +3,30% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 14 | 64,29% | +0,81% | +0,81% | -2,08% | +3,40% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 14 | 64,29% | +0,81% | +0,81% | -2,08% | +3,40% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 10 | 80,00% | +1,68% | +1,68% | -1,90% | +3,81% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 11 | 36,36% | +1,68% | -0,60% | -1,65% | +3,92% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 10 | 60,00% | +1,89% | +1,23% | -2,07% | +4,34% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 11 | 72,73% | +1,64% | +1,64% | -2,00% | +4,38% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 11 | 72,73% | +1,64% | +1,64% | -2,00% | +4,38% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 10 | 80,00% | +1,94% | +1,94% | -2,01% | +4,48% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 10 | 30,00% | +1,76% | -0,56% | -1,87% | +4,56% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 7 | 85,71% | +1,60% | +1,60% | -2,36% | +5,31% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 7 | 85,71% | +1,60% | +1,60% | -2,36% | +5,31% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 7 | 85,71% | +1,60% | +1,60% | -2,36% | +5,31% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 7 | 85,71% | +1,60% | +1,60% | -2,36% | +5,31% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 6 | 33,33% | +1,49% | -0,12% | -2,20% | +5,40% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 19 | 52,63% | -0,01% | +0,03% | -0,45% | +0,66% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 20 | 55,00% | -0,21% | +0,39% | -0,66% | +0,46% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 20 | 55,00% | -0,21% | +0,39% | -0,66% | +0,46% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 18 | 55,56% | -0,02% | +0,22% | -0,50% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 20 | 55,00% | -0,21% | +0,21% | -0,66% | +0,46% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 17 | 47,06% | +0,11% | -0,11% | -0,33% | +0,72% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 18 | 50,00% | -0,26% | -0,27% | -0,92% | +0,88% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 19 | 52,63% | -0,41% | +0,09% | -1,08% | +0,70% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 19 | 52,63% | -0,41% | +0,09% | -1,08% | +0,70% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 17 | 52,94% | -0,60% | +0,25% | -1,20% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 19 | 57,89% | -0,41% | +0,41% | -1,08% | +0,70% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 16 | 50,00% | +0,16% | -0,16% | -0,56% | +1,39% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 18 | 44,44% | -0,53% | +0,10% | -2,22% | +2,17% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 18 | 50,00% | -0,53% | +0,17% | -2,22% | +2,17% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 18 | 50,00% | -0,53% | +0,17% | -2,22% | +2,17% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 16 | 56,25% | -1,04% | +0,64% | -2,17% | +1,95% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 18 | 50,00% | -0,53% | +0,53% | -2,22% | +2,17% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 16 | 43,75% | -0,22% | +0,22% | -2,05% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 16 | 62,50% | -0,80% | +0,80% | -3,27% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 16 | 62,50% | -0,80% | +0,80% | -3,27% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 16 | 62,50% | -0,80% | +0,80% | -3,27% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 14 | 64,29% | -0,85% | +0,85% | -3,36% | +2,14% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 16 | 62,50% | -0,80% | +0,80% | -3,27% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 15 | 60,00% | -0,66% | +0,66% | -3,23% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,30% | +2,30% | +0,26% | +6,93% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 14 | 71,43% | -1,38% | +1,38% | -3,98% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 14 | 71,43% | -1,38% | +1,38% | -3,98% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 14 | 71,43% | -1,38% | +1,38% | -3,98% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 14 | 71,43% | -1,38% | +1,38% | -3,98% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 14 | 71,43% | -1,38% | +1,38% | -3,98% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 13 | 69,23% | -1,40% | +1,40% | -3,99% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 11 | 63,64% | -1,72% | +1,72% | -4,49% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 11 | 63,64% | -1,72% | +1,72% | -4,49% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 11 | 63,64% | -1,72% | +1,72% | -4,49% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 11 | 63,64% | -1,72% | +1,72% | -4,49% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 11 | 63,64% | -1,72% | +1,72% | -4,49% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 10 | 60,00% | -1,29% | +1,29% | -4,23% | +2,64% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 7 | 71,43% | -2,73% | +2,73% | -5,85% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 7 | 71,43% | -2,73% | +2,73% | -5,85% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 7 | 71,43% | -2,73% | +2,73% | -5,85% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 7 | 71,43% | -2,73% | +2,73% | -5,85% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 7 | 71,43% | -2,73% | +2,73% | -5,85% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 6 | 66,67% | -2,43% | +2,43% | -5,56% | +3,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 15 | 46,67% | -0,16% | -0,63% | -0,54% | +0,69% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 16 | 62,50% | -0,72% | -0,18% | -1,03% | +0,04% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 19 | 57,89% | -0,44% | -0,33% | -0,81% | +0,33% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 14 | 50,00% | -0,43% | -0,14% | -0,95% | +0,30% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 20 | 55,00% | -0,27% | +0,09% | -0,66% | +0,46% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 12 | 58,33% | -0,22% | +0,22% | -0,61% | +0,37% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 14 | 21,43% | -0,41% | -1,09% | -1,02% | +0,84% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 15 | 40,00% | -0,99% | -0,68% | -1,69% | -0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 18 | 38,89% | -0,76% | -0,62% | -1,41% | +0,44% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 13 | 30,77% | -0,94% | -0,86% | -1,63% | +0,40% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 19 | 42,11% | -0,60% | -0,00% | -1,21% | +0,59% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 11 | 54,55% | -0,37% | +0,37% | -0,80% | +0,17% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 14 | 14,29% | -0,64% | -1,49% | -2,30% | +2,00% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 14 | 35,71% | -1,11% | -0,56% | -2,85% | +1,68% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 17 | 35,29% | -0,86% | -0,52% | -2,56% | +1,98% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 12 | 33,33% | -0,98% | -1,14% | -2,58% | +2,10% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 18 | 44,44% | -0,73% | +0,07% | -2,34% | +2,07% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 10 | 40,00% | -0,03% | +0,03% | -2,00% | +2,20% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 14 | 35,71% | -1,05% | -1,42% | -3,34% | +2,55% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 12 | 50,00% | -1,46% | -0,87% | -3,85% | +2,00% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 15 | 46,67% | -1,03% | -0,84% | -3,49% | +2,38% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 10 | 40,00% | -1,95% | -1,21% | -3,70% | +2,25% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 16 | 50,00% | -1,11% | +0,08% | -3,44% | +2,45% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 8 | 62,50% | -0,40% | +0,40% | -2,75% | +2,81% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 13 | 46,15% | -1,07% | -0,82% | -3,87% | +2,94% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 10 | 70,00% | -1,75% | +0,55% | -4,34% | +2,44% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 13 | 69,23% | -1,37% | +0,45% | -3,96% | +2,78% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 8 | 50,00% | -1,24% | -0,98% | -4,13% | +2,74% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 14 | 35,71% | -1,23% | -0,22% | -3,92% | +2,84% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 6 | 50,00% | -0,83% | +0,83% | -3,11% | +3,56% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 10 | 40,00% | -0,76% | -0,51% | -3,93% | +3,35% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 8 | 50,00% | -1,14% | +0,05% | -4,31% | +2,92% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 11 | 45,45% | -0,89% | +0,09% | -4,07% | +3,19% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 7 | 28,57% | -0,68% | -1,47% | -4,21% | +3,09% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 11 | 54,55% | -0,89% | +0,45% | -4,07% | +3,19% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 4 | 75,00% | -1,26% | +1,26% | -3,10% | +4,25% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 6 | 33,33% | -2,51% | -1,18% | -4,69% | +2,76% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 5 | 60,00% | -2,14% | +0,04% | -5,08% | +2,28% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 7 | 71,43% | -2,51% | +1,01% | -4,81% | +2,58% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 6 | 16,67% | -2,51% | -1,92% | -4,69% | +2,76% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 7 | 28,57% | -2,51% | -0,39% | -4,81% | +2,58% | FEEDBACK RAPIDO |
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
