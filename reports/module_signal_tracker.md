# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-22 05:32 UTC

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

Segnali totali salvati: **129**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-22 | BTC | 77.109,54 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-22 | DOGE | 0.09028 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-22 | SOL | 93,36 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-21 | BTC | 75.089,33 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-21 | DOGE | 0.08259 | +2 | +1 | +1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-21 | SOL | 89,61 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-20 | BTC | 69.558,29 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-20 | DOGE | 0.07454 | +4 | +3 | +3 | 0 | +2 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-20 | SOL | 84,90 | +3 | 0 | 0 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-19 | BTC | 64.293,48 | +5 | +3 | +2 | +2 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-19 | DOGE | 0.06997 | +3 | +4 | +3 | +2 | 0 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-19 | SOL | 76,87 | +2 | +3 | +2 | +2 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 43 | 42 | 41 | 40 | 38 | 36 | 34 | 31 | 24 | 15 | 0 | 0 |
| SOL | 43 | 42 | 41 | 40 | 38 | 36 | 34 | 31 | 24 | 15 | 0 | 0 |
| DOGE | 43 | 42 | 41 | 40 | 38 | 36 | 34 | 31 | 24 | 15 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-09 | 45g | 2026-08-23 | domani |
| SOL | 2026-07-09 | 45g | 2026-08-23 | domani |
| DOGE | 2026-07-09 | 45g | 2026-08-23 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 39 | 53,85% | +0,53% | +0,50% | PRIMA CALIBRAZIONE |
| BTC | 2g | 38 | 52,63% | +0,86% | +0,73% | PRIMA CALIBRAZIONE |
| BTC | 3g | 37 | 45,95% | +0,81% | +0,62% | PRIMA CALIBRAZIONE |
| BTC | 5g | 36 | 36,11% | +1,41% | +1,05% | PRIMA CALIBRAZIONE |
| BTC | 7g | 34 | 44,12% | +1,22% | +0,90% | PRIMA CALIBRAZIONE |
| BTC | 10g | 32 | 43,75% | +0,94% | +0,65% | PRIMA CALIBRAZIONE |
| BTC | 14g | 29 | 51,72% | +1,50% | +1,38% | FEEDBACK RAPIDO |
| BTC | 21g | 22 | 36,36% | +1,71% | +1,41% | FEEDBACK RAPIDO |
| BTC | 30g | 14 | 85,71% | +2,82% | +3,18% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 35 | 57,14% | +0,64% | +0,46% | PRIMA CALIBRAZIONE |
| SOL | 2g | 34 | 50,00% | +1,20% | +0,99% | PRIMA CALIBRAZIONE |
| SOL | 3g | 33 | 51,52% | +1,74% | +1,47% | PRIMA CALIBRAZIONE |
| SOL | 5g | 31 | 54,84% | +1,77% | +1,59% | PRIMA CALIBRAZIONE |
| SOL | 7g | 29 | 58,62% | +1,43% | +1,61% | FEEDBACK RAPIDO |
| SOL | 10g | 27 | 59,26% | +1,08% | +1,36% | FEEDBACK RAPIDO |
| SOL | 14g | 24 | 66,67% | +1,70% | +3,21% | FEEDBACK RAPIDO |
| SOL | 21g | 18 | 55,56% | +1,54% | -0,44% | FEEDBACK RAPIDO |
| SOL | 30g | 14 | 42,86% | +2,59% | +0,37% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 40 | 47,50% | +0,65% | +0,63% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 39 | 48,72% | +1,07% | +1,07% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 38 | 47,37% | +1,14% | +1,44% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 36 | 55,56% | +0,99% | +1,68% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 34 | 61,76% | +0,61% | +1,91% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 32 | 56,25% | -0,43% | +1,51% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 29 | 62,07% | +0,05% | +3,25% | FEEDBACK RAPIDO |
| DOGE | 21g | 23 | 69,57% | -0,47% | +0,53% | FEEDBACK RAPIDO |
| DOGE | 30g | 15 | 80,00% | -0,54% | +0,54% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 39 | 53,85% | +0,53% | +0,50% | +0,13% | +1,10% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 42 | 57,14% | +0,49% | +0,49% | +0,10% | +1,03% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 42 | 57,14% | +0,49% | +0,49% | +0,10% | +1,03% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 37 | 37,84% | +0,68% | +0,13% | +0,27% | +1,23% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 10 | 30,00% | +1,59% | +0,54% | +0,82% | +2,11% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 38 | 52,63% | +0,86% | +0,73% | +0,32% | +1,58% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 41 | 56,10% | +0,98% | +0,98% | +0,45% | +1,69% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 41 | 56,10% | +0,98% | +0,98% | +0,45% | +1,69% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 36 | 41,67% | +1,26% | +0,11% | +0,74% | +1,97% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 9 | 22,22% | +2,05% | +0,36% | +1,71% | +2,86% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 37 | 45,95% | +0,81% | +0,62% | -1,03% | +2,40% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 40 | 57,50% | +1,24% | +1,24% | -1,00% | +2,74% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 40 | 57,50% | +1,24% | +1,24% | -1,00% | +2,74% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 35 | 31,43% | +1,70% | -0,71% | -0,74% | +3,13% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 8 | 12,50% | +2,41% | -2,41% | -0,24% | +3,25% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 36 | 36,11% | +1,41% | +1,05% | -1,88% | +3,42% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 38 | 44,74% | +1,34% | +1,34% | -1,86% | +3,38% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 38 | 44,74% | +1,34% | +1,34% | -1,86% | +3,38% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 47,06% | +1,56% | +1,56% | -1,83% | +3,50% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 33 | 33,33% | +1,71% | -2,28% | -1,62% | +3,78% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 8 | 12,50% | +7,26% | -7,26% | -0,63% | +8,70% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 34 | 44,12% | +1,22% | +0,90% | -2,25% | +3,55% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 36 | 52,78% | +1,12% | +1,12% | -2,24% | +3,50% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 36 | 52,78% | +1,12% | +1,12% | -2,24% | +3,50% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | +1,43% | +1,43% | -2,21% | +3,64% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 31 | 32,26% | +1,66% | -2,15% | -1,99% | +3,88% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 6 | 0,00% | +8,28% | -8,28% | -0,96% | +9,64% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 32 | 43,75% | +0,94% | +0,65% | -2,66% | +3,40% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 34 | 50,00% | +0,75% | +0,75% | -2,68% | +3,36% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 34 | 50,00% | +0,75% | +0,75% | -2,68% | +3,36% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 30 | 56,67% | +1,12% | +1,12% | -2,58% | +3,49% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 29 | 34,48% | +1,07% | +0,49% | -2,43% | +3,73% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,32% | -1,32% | -1,42% | +3,31% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 29 | 51,72% | +1,50% | +1,38% | -2,86% | +4,58% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 31 | 51,61% | +1,30% | +1,30% | -2,88% | +4,45% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 31 | 51,61% | +1,30% | +1,30% | -2,88% | +4,45% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 27 | 59,26% | +1,86% | +1,86% | -2,66% | +4,76% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 26 | 61,54% | +1,80% | +1,74% | -2,58% | +4,99% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 22 | 36,36% | +1,71% | +1,41% | -3,09% | +5,38% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 24 | 50,00% | +1,47% | +1,47% | -3,14% | +5,15% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 24 | 50,00% | +1,47% | +1,47% | -3,14% | +5,15% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 20 | 55,00% | +2,04% | +2,04% | -2,87% | +5,71% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 19 | 21,05% | +1,45% | -1,81% | -2,79% | +5,23% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 3 | 0,00% | +8,03% | -8,03% | -1,93% | +10,14% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 14 | 85,71% | +2,82% | +3,18% | -3,23% | +6,82% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 15 | 66,67% | +2,59% | +2,59% | -3,18% | +6,68% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 15 | 66,67% | +2,59% | +2,59% | -3,18% | +6,68% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 11 | 63,64% | +1,81% | +1,81% | -2,71% | +6,55% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 12 | 41,67% | +1,49% | -1,91% | -2,79% | +6,23% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 40 | 47,50% | +0,65% | +0,63% | +0,15% | +1,63% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 42 | 57,14% | +0,52% | +0,81% | +0,01% | +1,47% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 42 | 57,14% | +0,52% | +0,81% | +0,01% | +1,47% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 35 | 54,29% | +0,45% | +0,69% | -0,08% | +1,36% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 27 | 37,04% | +0,44% | -0,44% | -0,04% | +1,04% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,69% | +3,06% | +2,25% | +3,87% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 39 | 48,72% | +1,07% | +1,07% | +0,41% | +2,39% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 41 | 51,22% | +0,91% | +1,14% | +0,26% | +2,19% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 41 | 51,22% | +0,91% | +1,14% | +0,26% | +2,19% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 34 | 61,76% | +0,35% | +0,89% | -0,23% | +1,57% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 27 | 44,44% | +1,08% | -1,08% | +0,40% | +2,07% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +6,72% | +6,19% | +5,95% | +9,58% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 38 | 47,37% | +1,14% | +1,44% | -1,43% | +3,61% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 40 | 52,50% | +0,98% | +1,29% | -1,54% | +3,39% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 40 | 52,50% | +0,98% | +1,29% | -1,54% | +3,39% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 33 | 48,48% | -0,26% | +0,25% | -1,90% | +1,81% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 27 | 33,33% | +1,97% | -1,97% | -1,30% | +4,60% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,70% | +1,18% | -0,25% | +5,07% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 36 | 55,56% | +0,99% | +1,68% | -2,42% | +4,14% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 38 | 52,63% | +0,83% | +1,50% | -2,49% | +3,92% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 38 | 52,63% | +0,83% | +1,50% | -2,49% | +3,92% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 36 | 52,78% | +0,90% | +1,56% | -2,48% | +3,88% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 33 | 63,64% | +0,95% | +0,56% | -2,69% | +4,03% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 25 | 48,00% | +1,57% | -1,57% | -2,40% | +4,96% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 34 | 61,76% | +0,61% | +1,91% | -2,90% | +4,31% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 36 | 58,33% | +0,45% | +1,64% | -2,99% | +4,13% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 36 | 58,33% | +0,45% | +1,64% | -2,99% | +4,13% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 58,82% | +0,54% | +1,67% | -3,00% | +4,11% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 31 | 64,52% | -0,09% | +1,94% | -3,29% | +3,65% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 23 | 52,17% | -0,04% | +0,04% | -3,05% | +3,58% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,63% | +0,36% | -0,50% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 32 | 56,25% | -0,43% | +1,51% | -3,53% | +3,51% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 34 | 55,88% | -0,51% | +1,35% | -3,58% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 34 | 55,88% | -0,51% | +1,35% | -3,58% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | -0,49% | +1,38% | -3,59% | +3,29% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 30 | 66,67% | -1,40% | +1,40% | -3,88% | +2,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 22 | 59,09% | -1,13% | +1,13% | -3,71% | +2,91% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +0,93% | +0,18% | -1,31% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 29 | 62,07% | +0,05% | +3,25% | -4,33% | +5,08% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 31 | 67,74% | -0,09% | +2,93% | -4,34% | +4,82% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 31 | 67,74% | -0,09% | +2,93% | -4,34% | +4,82% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 29 | 68,97% | +0,01% | +3,02% | -4,38% | +4,84% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 30 | 66,67% | -0,31% | +0,31% | -4,43% | +4,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 21 | 66,67% | -1,05% | +1,05% | -4,58% | +3,86% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +6,85% | -6,24% | -1,27% | +10,97% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 23 | 69,57% | -0,47% | +0,53% | -5,34% | +5,38% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 24 | 79,17% | -0,61% | +4,32% | -5,40% | +5,15% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 24 | 79,17% | -0,61% | +4,32% | -5,40% | +5,15% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 22 | 81,82% | -0,56% | +4,59% | -5,55% | +5,21% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 24 | 79,17% | -0,61% | +0,61% | -5,40% | +5,15% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 20 | 75,00% | +0,03% | -0,03% | -5,18% | +6,01% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 15 | 80,00% | -0,54% | +0,54% | -6,61% | +5,66% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 15 | 80,00% | -0,54% | +0,54% | -6,61% | +5,66% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 15 | 80,00% | -0,54% | +0,54% | -6,61% | +5,66% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 14 | 85,71% | -2,36% | +2,36% | -6,65% | +3,35% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 15 | 80,00% | -0,54% | +0,54% | -6,61% | +5,66% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 14 | 78,57% | -0,15% | +0,15% | -6,50% | +6,03% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 35 | 57,14% | +0,64% | +0,46% | +0,06% | +1,53% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 37 | 59,46% | +0,21% | +0,22% | -0,28% | +1,06% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 40 | 57,50% | +0,28% | +0,12% | -0,23% | +1,12% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 39 | 51,28% | +0,22% | +0,19% | -0,34% | +1,02% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 23 | 52,17% | +0,46% | +0,39% | -0,22% | +1,38% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,51% | +1,51% | +0,99% | +5,02% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 34 | 50,00% | +1,20% | +0,99% | +0,46% | +2,29% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 36 | 52,78% | +0,64% | +0,77% | -0,12% | +1,36% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 39 | 51,28% | +0,62% | +0,69% | -0,11% | +1,47% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 38 | 39,47% | +0,51% | -0,29% | -0,16% | +1,61% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 22 | 50,00% | +0,47% | +0,43% | -0,09% | +1,38% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 33 | 51,52% | +1,74% | +1,47% | -1,33% | +3,70% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 36 | 50,00% | +1,25% | +1,46% | -1,65% | +3,28% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 39 | 48,72% | +1,18% | +1,33% | -1,61% | +3,29% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 37 | 40,54% | +0,73% | -1,05% | -1,85% | +2,61% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 21 | 42,86% | +0,13% | -0,13% | -1,91% | +1,82% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 31 | 54,84% | +1,77% | +1,59% | -2,41% | +4,53% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 34 | 55,88% | +1,40% | +1,60% | -2,68% | +4,10% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 37 | 54,05% | +1,34% | +1,42% | -2,62% | +4,08% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 32 | 53,12% | +1,42% | +1,65% | -2,56% | +4,31% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 36 | 41,67% | +1,34% | -1,80% | -2,69% | +4,21% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 21 | 52,38% | +0,14% | -0,14% | -2,60% | +2,64% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 29 | 58,62% | +1,43% | +1,61% | -2,94% | +4,63% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 32 | 62,50% | +0,96% | +1,68% | -3,21% | +4,24% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 35 | 62,86% | +0,87% | +1,54% | -3,17% | +4,21% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 30 | 56,67% | +1,28% | +1,35% | -3,08% | +4,44% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 34 | 35,29% | +0,94% | -1,54% | -3,25% | +4,35% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 27 | 59,26% | +1,08% | +1,36% | -3,43% | +4,44% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 30 | 63,33% | +0,86% | +1,58% | -3,78% | +4,05% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 33 | 60,61% | +0,76% | +1,45% | -3,75% | +4,04% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 28 | 57,14% | +1,29% | +1,09% | -3,62% | +4,25% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 32 | 46,88% | +0,07% | -0,22% | -3,88% | +3,64% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,08% | +0,08% | -3,74% | +3,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 24 | 66,67% | +1,70% | +3,21% | -4,14% | +6,43% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 27 | 81,48% | +2,03% | +3,41% | -4,32% | +5,99% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 30 | 83,33% | +1,51% | +3,38% | -4,28% | +5,78% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 25 | 64,00% | +2,45% | +2,59% | -3,99% | +6,37% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 31 | 35,48% | +1,33% | -1,99% | -4,36% | +5,71% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,19% | -1,19% | -4,25% | +5,07% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 18 | 55,56% | +1,54% | -0,44% | -6,41% | +6,79% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 20 | 75,00% | +1,76% | +4,56% | -6,27% | +6,31% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 23 | 78,26% | +1,18% | +4,32% | -6,25% | +5,99% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 18 | 50,00% | +2,26% | +3,20% | -5,99% | +6,87% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 24 | 50,00% | +1,16% | -2,87% | -6,28% | +5,89% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 16 | 50,00% | +3,90% | -3,90% | -5,75% | +7,67% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 14 | 42,86% | +2,59% | +0,37% | -7,69% | +6,71% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 11 | 72,73% | +2,91% | +1,96% | -8,12% | +7,29% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 14 | 64,29% | +2,34% | +1,49% | -7,84% | +6,56% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 9 | 66,67% | +2,32% | +2,79% | -7,96% | +6,98% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 15 | 26,67% | +2,26% | -3,51% | -7,78% | +6,36% | FEEDBACK RAPIDO |
| SOL | 30g | Classic technical | CALIBRABILE | 7 | 28,57% | +5,28% | -5,28% | -7,15% | +9,70% | FEEDBACK RAPIDO |
| SOL | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | FEEDBACK RAPIDO |
| SOL | 30g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | FEEDBACK RAPIDO |

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
