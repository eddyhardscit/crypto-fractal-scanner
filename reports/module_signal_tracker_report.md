# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-23 05:32 UTC

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

Segnali totali salvati: **132**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-23 | BTC | 76.280,85 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-23 | DOGE | 0.09044 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-23 | SOL | 93,05 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-22 | BTC | 77.109,54 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-22 | DOGE | 0.09028 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-22 | SOL | 93,36 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-21 | BTC | 75.089,33 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-21 | DOGE | 0.08259 | +2 | +1 | +1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-21 | SOL | 89,61 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-20 | BTC | 69.558,29 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-20 | DOGE | 0.07454 | +4 | +3 | +3 | 0 | +2 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-20 | SOL | 84,90 | +3 | 0 | 0 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 44 | 43 | 42 | 41 | 39 | 37 | 34 | 32 | 25 | 16 | 1 | 0 |
| SOL | 44 | 43 | 42 | 41 | 39 | 37 | 34 | 32 | 25 | 16 | 1 | 0 |
| DOGE | 44 | 43 | 42 | 41 | 39 | 37 | 34 | 32 | 25 | 16 | 1 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-10 | 45g | 2026-08-24 | domani |
| SOL | 2026-07-10 | 45g | 2026-08-24 | domani |
| DOGE | 2026-07-10 | 45g | 2026-08-24 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 40 | 52,50% | +0,49% | +0,46% | PRIMA CALIBRAZIONE |
| BTC | 2g | 39 | 53,85% | +0,88% | +0,76% | PRIMA CALIBRAZIONE |
| BTC | 3g | 38 | 47,37% | +1,04% | +0,86% | PRIMA CALIBRAZIONE |
| BTC | 5g | 36 | 36,11% | +1,41% | +1,05% | PRIMA CALIBRAZIONE |
| BTC | 7g | 35 | 45,71% | +1,79% | +1,48% | PRIMA CALIBRAZIONE |
| BTC | 10g | 32 | 43,75% | +0,94% | +0,65% | PRIMA CALIBRAZIONE |
| BTC | 14g | 30 | 53,33% | +2,04% | +1,93% | PRIMA CALIBRAZIONE |
| BTC | 21g | 23 | 39,13% | +2,52% | +2,23% | FEEDBACK RAPIDO |
| BTC | 30g | 14 | 85,71% | +2,82% | +3,18% | FEEDBACK RAPIDO |
| BTC | 45g | 1 | 100,00% | +20,63% | +20,63% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 36 | 55,56% | +0,61% | +0,44% | PRIMA CALIBRAZIONE |
| SOL | 2g | 35 | 51,43% | +1,27% | +1,07% | PRIMA CALIBRAZIONE |
| SOL | 3g | 34 | 52,94% | +1,97% | +1,71% | PRIMA CALIBRAZIONE |
| SOL | 5g | 32 | 56,25% | +2,43% | +2,26% | PRIMA CALIBRAZIONE |
| SOL | 7g | 30 | 60,00% | +2,16% | +2,34% | PRIMA CALIBRAZIONE |
| SOL | 10g | 27 | 59,26% | +1,08% | +1,36% | FEEDBACK RAPIDO |
| SOL | 14g | 25 | 68,00% | +2,53% | +3,99% | FEEDBACK RAPIDO |
| SOL | 21g | 19 | 57,89% | +2,86% | +0,99% | FEEDBACK RAPIDO |
| SOL | 30g | 14 | 42,86% | +2,59% | +0,37% | FEEDBACK RAPIDO |
| SOL | 45g | 1 | 100,00% | +19,26% | +19,26% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 41 | 48,78% | +0,63% | +0,62% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 40 | 50,00% | +1,28% | +1,28% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 39 | 48,72% | +1,66% | +1,95% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 37 | 56,76% | +1,76% | +2,44% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 35 | 62,86% | +1,44% | +2,71% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 32 | 56,25% | -0,43% | +1,51% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 30 | 63,33% | +1,02% | +4,12% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 24 | 70,83% | +0,75% | +1,71% | FEEDBACK RAPIDO |
| DOGE | 30g | 16 | 75,00% | +1,43% | -1,43% | FEEDBACK RAPIDO |
| DOGE | 45g | 1 | 0,00% | +24,15% | -24,15% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 40 | 52,50% | +0,49% | +0,46% | +0,09% | +1,08% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 43 | 55,81% | +0,45% | +0,45% | +0,06% | +1,02% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 43 | 55,81% | +0,45% | +0,45% | +0,06% | +1,02% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 38 | 36,84% | +0,64% | +0,10% | +0,22% | +1,21% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 11 | 27,27% | +1,35% | +0,39% | +0,60% | +1,95% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 39 | 53,85% | +0,88% | +0,76% | +0,34% | +1,61% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 42 | 57,14% | +0,99% | +0,99% | +0,47% | +1,72% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 42 | 57,14% | +0,99% | +0,99% | +0,47% | +1,72% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 37 | 43,24% | +1,27% | +0,15% | +0,74% | +2,00% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 10 | 30,00% | +2,00% | +0,48% | +1,65% | +2,88% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 38 | 47,37% | +1,04% | +0,86% | -0,87% | +2,72% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 41 | 58,54% | +1,44% | +1,44% | -0,85% | +3,02% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 41 | 58,54% | +1,44% | +1,44% | -0,85% | +3,02% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 36 | 33,33% | +1,92% | -0,42% | -0,58% | +3,44% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 9 | 22,22% | +3,21% | -1,06% | +0,33% | +4,47% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 36 | 36,11% | +1,41% | +1,05% | -1,88% | +3,42% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 39 | 46,15% | +1,79% | +1,79% | -1,82% | +3,91% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 39 | 46,15% | +1,79% | +1,79% | -1,82% | +3,91% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 47,06% | +1,56% | +1,56% | -1,83% | +3,50% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 34 | 32,35% | +2,22% | -2,77% | -1,58% | +4,37% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 8 | 12,50% | +7,26% | -7,26% | -0,63% | +8,70% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 35 | 45,71% | +1,79% | +1,48% | -2,20% | +4,19% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 37 | 54,05% | +1,66% | +1,66% | -2,20% | +4,11% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 37 | 54,05% | +1,66% | +1,66% | -2,20% | +4,11% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 33 | 57,58% | +2,02% | +2,02% | -2,15% | +4,32% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 32 | 31,25% | +2,27% | -2,75% | -1,94% | +4,58% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 7 | 0,00% | +10,11% | -10,11% | -0,89% | +11,99% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 32 | 43,75% | +0,94% | +0,65% | -2,66% | +3,40% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 34 | 50,00% | +0,75% | +0,75% | -2,68% | +3,36% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 34 | 50,00% | +0,75% | +0,75% | -2,68% | +3,36% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 30 | 56,67% | +1,12% | +1,12% | -2,58% | +3,49% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 29 | 34,48% | +1,07% | +0,49% | -2,43% | +3,73% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,32% | -1,32% | -1,42% | +3,31% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 30 | 53,33% | +2,04% | +1,93% | -2,88% | +5,18% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 32 | 53,12% | +1,82% | +1,82% | -2,90% | +5,02% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 32 | 53,12% | +1,82% | +1,82% | -2,90% | +5,02% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 28 | 60,71% | +2,43% | +2,43% | -2,69% | +5,40% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 27 | 62,96% | +2,39% | +2,33% | -2,61% | +5,64% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 23 | 39,13% | +2,52% | +2,23% | -3,04% | +6,25% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 25 | 52,00% | +2,23% | +2,23% | -3,09% | +5,96% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 25 | 52,00% | +2,23% | +2,23% | -3,09% | +5,96% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 21 | 57,14% | +2,92% | +2,92% | -2,82% | +6,64% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 20 | 20,00% | +2,39% | -2,73% | -2,74% | +6,24% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 3 | 0,00% | +8,03% | -8,03% | -1,93% | +10,14% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 14 | 85,71% | +2,82% | +3,18% | -3,23% | +6,82% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 16 | 68,75% | +3,48% | +3,48% | -3,28% | +7,62% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 16 | 68,75% | +3,48% | +3,48% | -3,28% | +7,62% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 12 | 66,67% | +3,06% | +3,06% | -2,88% | +7,81% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 13 | 38,46% | +2,66% | -3,06% | -2,94% | +7,42% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 1 | 100,00% | +20,63% | +20,63% | -2,32% | +25,66% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | +20,63% | +20,63% | -2,32% | +25,66% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | +20,63% | +20,63% | -2,32% | +25,66% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 1 | 100,00% | +20,63% | +20,63% | -2,32% | +25,66% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 1 | 0,00% | +20,63% | -20,63% | -2,32% | +25,66% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 41 | 48,78% | +0,63% | +0,62% | +0,11% | +1,69% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 43 | 58,14% | +0,51% | +0,79% | -0,01% | +1,54% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 43 | 58,14% | +0,51% | +0,79% | -0,01% | +1,54% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 36 | 55,56% | +0,44% | +0,68% | -0,11% | +1,44% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 28 | 39,29% | +0,43% | -0,42% | -0,08% | +1,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +3,11% | +2,58% | +1,68% | +3,93% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 40 | 50,00% | +1,28% | +1,28% | +0,60% | +2,68% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 42 | 52,38% | +1,11% | +1,34% | +0,45% | +2,47% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 42 | 52,38% | +1,11% | +1,34% | +0,45% | +2,47% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 35 | 62,86% | +0,61% | +1,14% | +0,01% | +1,92% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 27 | 44,44% | +1,08% | -1,08% | +0,40% | +2,07% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +6,72% | +6,19% | +5,95% | +9,58% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 39 | 48,72% | +1,66% | +1,95% | -1,19% | +4,19% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 41 | 53,66% | +1,47% | +1,78% | -1,31% | +3,95% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 41 | 53,66% | +1,47% | +1,78% | -1,31% | +3,95% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 34 | 50,00% | +0,37% | +0,87% | -1,61% | +2,54% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 27 | 33,33% | +1,97% | -1,97% | -1,30% | +4,60% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +5,63% | +5,21% | +1,37% | +9,34% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 37 | 56,76% | +1,76% | +2,44% | -2,35% | +4,98% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 39 | 53,85% | +1,57% | +2,23% | -2,42% | +4,72% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 39 | 53,85% | +1,57% | +2,23% | -2,42% | +4,72% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 37 | 54,05% | +1,68% | +2,32% | -2,41% | +4,73% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 33 | 63,64% | +0,95% | +0,56% | -2,69% | +4,03% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 26 | 46,15% | +2,66% | -2,66% | -2,30% | +6,12% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 35 | 62,86% | +1,44% | +2,71% | -2,82% | +5,20% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 37 | 59,46% | +1,24% | +2,40% | -2,91% | +4,97% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 37 | 59,46% | +1,24% | +2,40% | -2,91% | +4,97% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +1,37% | +2,47% | -2,93% | +5,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 32 | 65,62% | +0,84% | +2,81% | -3,19% | +4,64% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 24 | 50,00% | +1,20% | -1,20% | -2,94% | +4,90% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,63% | +0,36% | -0,50% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 32 | 56,25% | -0,43% | +1,51% | -3,53% | +3,51% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 34 | 55,88% | -0,51% | +1,35% | -3,58% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 34 | 55,88% | -0,51% | +1,35% | -3,58% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | -0,49% | +1,38% | -3,59% | +3,29% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 30 | 66,67% | -1,40% | +1,40% | -3,88% | +2,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 22 | 59,09% | -1,13% | +1,13% | -3,71% | +2,91% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +0,93% | +0,18% | -1,31% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 30 | 63,33% | +1,02% | +4,12% | -4,23% | +6,07% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 32 | 68,75% | +0,82% | +3,75% | -4,25% | +5,76% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 32 | 68,75% | +0,82% | +3,75% | -4,25% | +5,76% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 30 | 70,00% | +0,98% | +3,90% | -4,28% | +5,84% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 30 | 66,67% | -0,31% | +0,31% | -4,43% | +4,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 22 | 63,64% | +0,33% | -0,33% | -4,43% | +5,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,47% | +2,65% | -1,31% | +16,91% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 24 | 70,83% | +0,75% | +1,71% | -5,23% | +6,58% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 25 | 80,00% | +0,56% | +5,30% | -5,29% | +6,32% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 25 | 80,00% | +0,56% | +5,30% | -5,29% | +6,32% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 23 | 82,61% | +0,72% | +5,65% | -5,43% | +6,47% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 25 | 76,00% | +0,56% | -0,56% | -5,29% | +6,32% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 20 | 75,00% | +0,03% | -0,03% | -5,18% | +6,01% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 16 | 75,00% | +1,43% | -1,43% | -6,29% | +7,59% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 16 | 75,00% | +1,43% | -1,43% | -6,29% | +7,59% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 16 | 75,00% | +1,43% | -1,43% | -6,29% | +7,59% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 14 | 85,71% | -2,36% | +2,36% | -6,65% | +3,35% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 16 | 75,00% | +1,43% | -1,43% | -6,29% | +7,59% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 15 | 73,33% | +1,93% | -1,93% | -6,17% | +8,06% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +31,03% | +31,03% | -1,52% | +36,52% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 1 | 0,00% | +24,15% | -24,15% | -6,69% | +29,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 1 | 0,00% | +24,15% | -24,15% | -6,69% | +29,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 1 | 0,00% | +24,15% | -24,15% | -6,69% | +29,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | +24,15% | -24,15% | -6,69% | +29,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 1 | 0,00% | +24,15% | -24,15% | -6,69% | +29,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 1 | 0,00% | +24,15% | -24,15% | -6,69% | +29,34% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 36 | 55,56% | +0,61% | +0,44% | +0,02% | +1,58% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 38 | 60,53% | +0,20% | +0,22% | -0,31% | +1,13% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 41 | 58,54% | +0,26% | +0,13% | -0,26% | +1,18% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 40 | 50,00% | +0,21% | +0,17% | -0,36% | +1,08% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 24 | 50,00% | +0,43% | +0,36% | -0,27% | +1,46% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,51% | +1,51% | +0,99% | +5,02% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 35 | 51,43% | +1,27% | +1,07% | +0,53% | +2,45% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 37 | 51,35% | +0,73% | +0,65% | -0,04% | +1,53% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 40 | 50,00% | +0,70% | +0,57% | -0,04% | +1,62% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 39 | 41,03% | +0,60% | -0,19% | -0,08% | +1,77% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 23 | 52,17% | +0,62% | +0,58% | +0,03% | +1,66% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,74% | +0,74% | +0,30% | +2,88% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 34 | 52,94% | +1,97% | +1,71% | -1,20% | +3,99% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 36 | 50,00% | +1,25% | +1,46% | -1,65% | +3,28% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 39 | 48,72% | +1,18% | +1,33% | -1,61% | +3,29% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 38 | 42,11% | +0,96% | -0,77% | -1,72% | +2,90% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 22 | 45,45% | +0,56% | +0,31% | -1,68% | +2,36% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 32 | 56,25% | +2,43% | +2,26% | -2,29% | +5,25% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 35 | 57,14% | +2,01% | +2,22% | -2,57% | +4,77% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 38 | 55,26% | +1,91% | +1,99% | -2,52% | +4,70% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 33 | 54,55% | +2,08% | +2,30% | -2,44% | +5,01% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 37 | 40,54% | +1,93% | -2,38% | -2,58% | +4,84% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 21 | 52,38% | +0,14% | -0,14% | -2,60% | +2,64% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 30 | 60,00% | +2,16% | +2,34% | -2,89% | +5,41% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 33 | 63,64% | +1,65% | +2,34% | -3,15% | +4,97% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 36 | 63,89% | +1,50% | +2,15% | -3,11% | +4,88% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 31 | 58,06% | +1,99% | +2,06% | -3,02% | +5,21% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 35 | 34,29% | +1,58% | -2,16% | -3,19% | +5,03% | PRIMA CALIBRAZIONE |
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
| SOL | 14g | Global confluence | BENCHMARK | 25 | 68,00% | +2,53% | +3,99% | -4,07% | +7,26% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 28 | 82,14% | +2,76% | +4,10% | -4,24% | +6,75% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 31 | 83,87% | +2,19% | +4,00% | -4,21% | +6,47% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 26 | 65,38% | +3,22% | +3,36% | -3,92% | +7,17% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 31 | 35,48% | +1,33% | -1,99% | -4,36% | +5,71% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,19% | -1,19% | -4,25% | +5,07% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 19 | 57,89% | +2,86% | +0,99% | -6,18% | +8,09% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 21 | 76,19% | +2,95% | +5,61% | -6,06% | +7,50% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 24 | 79,17% | +2,24% | +5,26% | -6,07% | +7,06% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 19 | 52,63% | +3,55% | +4,44% | -5,78% | +8,16% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 25 | 48,00% | +2,18% | -3,83% | -6,10% | +6,92% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 17 | 47,06% | +5,25% | -5,25% | -5,53% | +9,07% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
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
