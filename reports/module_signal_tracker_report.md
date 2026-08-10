# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-10 05:17 UTC

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

Segnali totali salvati: **99**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-10 | BTC | 64.966,07 | +6 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-10 | DOGE | 0.06975 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-10 | SOL | 76,57 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-09 | BTC | 64.733,97 | +7 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-09 | DOGE | 0.06994 | +4 | +4 | +3 | +3 | 0 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-09 | SOL | 75,92 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-08 | BTC | 64.965,57 | +8 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-08 | DOGE | 0.07012 | +3 | +3 | +2 | +3 | -1 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-08 | SOL | 74,51 | +3 | +4 | +3 | +3 | -2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-07 | BTC | 64.173,65 | +6 | +4 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-07 | DOGE | 0.06903 | +1 | +2 | +1 | +2 | -1 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-07 | SOL | 72,63 | +1 | +4 | +3 | +3 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 33 | 32 | 31 | 30 | 28 | 26 | 23 | 19 | 12 | 3 | 0 | 0 |
| SOL | 33 | 32 | 31 | 30 | 28 | 26 | 23 | 19 | 12 | 3 | 0 | 0 |
| DOGE | 33 | 32 | 31 | 30 | 28 | 26 | 23 | 19 | 12 | 3 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-12 | 30g | 2026-08-11 | domani |
| SOL | 2026-07-12 | 30g | 2026-08-11 | domani |
| DOGE | 2026-07-12 | 30g | 2026-08-11 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 30 | 50,00% | +0,07% | +0,03% | PRIMA CALIBRAZIONE |
| BTC | 2g | 29 | 48,28% | +0,18% | +0,02% | FEEDBACK RAPIDO |
| BTC | 3g | 28 | 42,86% | +0,12% | -0,13% | FEEDBACK RAPIDO |
| BTC | 5g | 26 | 34,62% | +0,37% | -0,12% | FEEDBACK RAPIDO |
| BTC | 7g | 24 | 45,83% | +0,53% | +0,08% | FEEDBACK RAPIDO |
| BTC | 10g | 21 | 42,86% | +0,60% | +0,16% | FEEDBACK RAPIDO |
| BTC | 14g | 17 | 52,94% | +0,16% | +0,05% | FEEDBACK RAPIDO |
| BTC | 21g | 11 | 36,36% | +0,41% | +0,02% | FEEDBACK RAPIDO |
| BTC | 30g | 3 | 100,00% | +1,85% | +1,85% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 25 | 56,00% | +0,07% | -0,18% | FEEDBACK RAPIDO |
| SOL | 2g | 24 | 45,83% | +0,03% | -0,26% | FEEDBACK RAPIDO |
| SOL | 3g | 23 | 47,83% | +0,10% | -0,29% | FEEDBACK RAPIDO |
| SOL | 5g | 21 | 47,62% | -0,39% | -0,65% | FEEDBACK RAPIDO |
| SOL | 7g | 20 | 55,00% | -0,44% | -0,18% | FEEDBACK RAPIDO |
| SOL | 10g | 17 | 35,29% | -1,25% | -0,80% | FEEDBACK RAPIDO |
| SOL | 14g | 14 | 57,14% | -3,18% | +0,21% | FEEDBACK RAPIDO |
| SOL | 21g | 11 | 63,64% | -2,96% | -0,06% | FEEDBACK RAPIDO |
| SOL | 30g | 2 | 0,00% | -3,04% | -3,04% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 30 | 40,00% | -0,05% | -0,07% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 29 | 44,83% | -0,16% | -0,16% | FEEDBACK RAPIDO |
| DOGE | 3g | 28 | 42,86% | -0,37% | +0,04% | FEEDBACK RAPIDO |
| DOGE | 5g | 26 | 53,85% | -0,73% | +0,23% | FEEDBACK RAPIDO |
| DOGE | 7g | 25 | 60,00% | -1,08% | +0,69% | FEEDBACK RAPIDO |
| DOGE | 10g | 22 | 59,09% | -1,70% | +1,12% | FEEDBACK RAPIDO |
| DOGE | 14g | 18 | 72,22% | -2,82% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 21g | 12 | 100,00% | -3,98% | +3,98% | FEEDBACK RAPIDO |
| DOGE | 30g | 3 | 100,00% | -4,95% | +4,95% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 30 | 50,00% | +0,07% | +0,03% | -0,25% | +0,61% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 32 | 53,12% | +0,05% | +0,05% | -0,27% | +0,56% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 32 | 53,12% | +0,05% | +0,05% | -0,27% | +0,56% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 28 | 53,57% | +0,02% | +0,02% | -0,31% | +0,48% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 27 | 37,04% | +0,24% | -0,34% | -0,10% | +0,75% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 4 | 0,00% | +0,76% | -0,76% | +0,03% | +1,12% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 29 | 48,28% | +0,18% | +0,02% | -0,31% | +0,85% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 31 | 51,61% | +0,14% | +0,14% | -0,32% | +0,81% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 31 | 51,61% | +0,14% | +0,14% | -0,32% | +0,81% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 27 | 51,85% | +0,06% | +0,06% | -0,42% | +0,71% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 26 | 50,00% | +0,37% | -0,25% | -0,08% | +1,03% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 4 | 25,00% | +0,86% | -0,86% | +0,50% | +1,73% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 28 | 42,86% | +0,12% | -0,13% | -1,27% | +1,74% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 30 | 56,67% | +0,20% | +0,20% | -1,24% | +1,72% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 30 | 56,67% | +0,20% | +0,20% | -1,24% | +1,72% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 26 | 57,69% | +0,20% | +0,20% | -1,25% | +1,63% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 25 | 40,00% | +0,63% | -0,21% | -0,94% | +2,07% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,18% | -1,18% | -0,41% | +2,46% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 26 | 34,62% | +0,37% | -0,12% | -2,01% | +2,35% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 28 | 46,43% | +0,35% | +0,35% | -1,97% | +2,37% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 28 | 46,43% | +0,35% | +0,35% | -1,97% | +2,37% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 24 | 50,00% | +0,50% | +0,50% | -1,95% | +2,37% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 23 | 47,83% | +0,67% | -0,40% | -1,66% | +2,72% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,14% | -1,14% | -1,16% | +2,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 24 | 45,83% | +0,53% | +0,08% | -2,32% | +2,77% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 26 | 57,69% | +0,44% | +0,44% | -2,31% | +2,76% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 26 | 57,69% | +0,44% | +0,44% | -2,31% | +2,76% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 22 | 63,64% | +0,77% | +0,77% | -2,27% | +2,83% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 21 | 33,33% | +1,09% | -0,68% | -1,95% | +3,16% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,94% | -1,94% | -1,23% | +3,13% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 21 | 42,86% | +0,60% | +0,16% | -2,79% | +3,02% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 23 | 52,17% | +0,34% | +0,34% | -2,81% | +2,99% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 23 | 52,17% | +0,34% | +0,34% | -2,81% | +2,99% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 19 | 63,16% | +0,85% | +0,85% | -2,68% | +3,12% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 18 | 38,89% | +0,75% | -0,12% | -2,43% | +3,48% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 2 | 0,00% | +1,45% | -1,45% | -2,23% | +2,64% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 17 | 52,94% | +0,16% | +0,05% | -3,18% | +3,60% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 19 | 47,37% | -0,02% | -0,02% | -3,19% | +3,50% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 19 | 47,37% | -0,02% | -0,02% | -3,19% | +3,50% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 15 | 60,00% | +0,64% | +0,64% | -2,86% | +3,80% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 15 | 53,33% | +0,23% | +0,10% | -2,77% | +3,98% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 11 | 36,36% | +0,41% | +0,02% | -2,66% | +4,94% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 12 | 58,33% | +0,52% | +0,52% | -2,66% | +4,93% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 12 | 58,33% | +0,52% | +0,52% | -2,66% | +4,93% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +0,50% | +0,50% | -2,49% | +5,16% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 11 | 9,09% | +0,49% | -0,70% | -2,60% | +4,94% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 3 | 100,00% | +1,85% | +1,85% | -3,05% | +5,02% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | +1,85% | +1,85% | -3,05% | +5,02% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | +1,85% | +1,85% | -3,05% | +5,02% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 3 | 100,00% | +1,85% | +1,85% | -3,05% | +5,02% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 2 | 0,00% | +2,09% | -2,09% | -2,93% | +5,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 30 | 40,00% | -0,05% | -0,07% | -0,51% | +0,59% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 32 | 53,12% | -0,17% | +0,21% | -0,64% | +0,45% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 32 | 53,12% | -0,17% | +0,21% | -0,64% | +0,45% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 30 | 53,33% | -0,05% | +0,10% | -0,55% | +0,59% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,12% | +0,12% | -0,60% | +0,51% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 22 | 40,91% | +0,18% | -0,18% | -0,35% | +0,74% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,92% | +1,13% | +0,84% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 29 | 44,83% | -0,16% | -0,16% | -0,78% | +0,76% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 31 | 48,39% | -0,29% | +0,02% | -0,90% | +0,60% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 31 | 48,39% | -0,29% | +0,02% | -0,90% | +0,60% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 29 | 48,28% | -0,39% | +0,11% | -0,96% | +0,55% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 30 | 60,00% | -0,30% | +0,30% | -0,91% | +0,61% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,19% | -0,19% | -0,49% | +1,28% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +4,20% | +3,33% | +3,09% | +4,54% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 28 | 42,86% | -0,37% | +0,04% | -1,92% | +1,84% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 30 | 50,00% | -0,48% | -0,06% | -2,03% | +1,66% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 30 | 50,00% | -0,48% | -0,06% | -2,03% | +1,66% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 28 | 53,57% | -0,77% | +0,19% | -1,99% | +1,50% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 29 | 48,28% | -0,50% | +0,50% | -2,05% | +1,69% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 21 | 38,10% | -0,08% | +0,08% | -1,88% | +2,28% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,43% | +1,74% | +0,13% | +5,37% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 26 | 53,85% | -0,73% | +0,23% | -2,98% | +2,09% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 28 | 50,00% | -0,83% | +0,09% | -3,03% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 28 | 50,00% | -0,83% | +0,09% | -3,03% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 26 | 50,00% | -0,85% | +0,06% | -3,06% | +1,74% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 28 | 64,29% | -0,83% | +0,83% | -3,03% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 20 | 55,00% | -0,45% | +0,45% | -2,87% | +2,58% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 25 | 60,00% | -1,08% | +0,69% | -3,49% | +2,31% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 26 | 57,69% | -1,20% | +0,45% | -3,62% | +2,13% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 26 | 57,69% | -1,20% | +0,45% | -3,62% | +2,13% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 24 | 58,33% | -1,21% | +0,39% | -3,69% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 26 | 65,38% | -1,20% | +1,20% | -3,62% | +2,13% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 20 | 55,00% | -1,01% | +1,01% | -3,42% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 22 | 59,09% | -1,70% | +1,12% | -4,35% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 23 | 56,52% | -1,80% | +0,95% | -4,45% | +2,24% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 23 | 56,52% | -1,80% | +0,95% | -4,45% | +2,24% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 21 | 57,14% | -1,89% | +0,96% | -4,54% | +2,02% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 23 | 69,57% | -1,80% | +1,80% | -4,45% | +2,24% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 19 | 63,16% | -1,37% | +1,37% | -4,08% | +2,76% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 18 | 72,22% | -2,82% | +2,29% | -5,58% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 19 | 73,68% | -2,90% | +2,04% | -5,64% | +2,37% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 19 | 73,68% | -2,90% | +2,04% | -5,64% | +2,37% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 17 | 76,47% | -3,05% | +2,09% | -5,86% | +2,12% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 19 | 78,95% | -2,90% | +2,90% | -5,64% | +2,37% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 16 | 75,00% | -2,59% | +2,59% | -5,33% | +2,92% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 12 | 100,00% | -3,98% | +3,98% | -6,47% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 12 | 100,00% | -3,98% | +3,98% | -6,47% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 12 | 100,00% | -3,98% | +3,98% | -6,47% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 12 | 100,00% | -3,98% | +3,98% | -6,47% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 12 | 100,00% | -3,98% | +3,98% | -6,47% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 11 | 100,00% | -3,84% | +3,84% | -6,32% | +2,66% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 3 | 100,00% | -4,95% | +4,95% | -7,62% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | -4,95% | +4,95% | -7,62% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | -4,95% | +4,95% | -7,62% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 3 | 100,00% | -4,95% | +4,95% | -7,62% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 3 | 100,00% | -4,95% | +4,95% | -7,62% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 3 | 100,00% | -4,95% | +4,95% | -7,62% | +2,47% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 25 | 56,00% | +0,07% | -0,18% | -0,46% | +0,73% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 28 | 64,29% | -0,26% | +0,05% | -0,74% | +0,36% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 31 | 61,29% | -0,13% | -0,06% | -0,63% | +0,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 26 | 57,69% | -0,07% | +0,08% | -0,67% | +0,53% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 31 | 48,39% | -0,06% | -0,05% | -0,57% | +0,56% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,04% | -0,04% | -0,54% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 24 | 45,83% | +0,03% | -0,26% | -0,61% | +0,92% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 27 | 51,85% | -0,26% | -0,08% | -0,96% | +0,47% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 30 | 50,00% | -0,20% | -0,11% | -0,87% | +0,70% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 25 | 48,00% | -0,17% | -0,14% | -0,87% | +0,73% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 31 | 38,71% | -0,11% | -0,26% | -0,76% | +0,78% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,02% | -0,02% | -0,52% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 23 | 47,83% | +0,10% | -0,29% | -2,03% | +2,01% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 26 | 46,15% | -0,39% | -0,09% | -2,39% | +1,63% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 29 | 44,83% | -0,32% | -0,11% | -2,27% | +1,81% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 24 | 45,83% | -0,26% | -0,34% | -2,22% | +1,84% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 30 | 43,33% | -0,26% | -0,14% | -2,15% | +1,87% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 21 | 42,86% | +0,13% | -0,13% | -1,91% | +1,82% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 21 | 47,62% | -0,39% | -0,65% | -3,03% | +2,43% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 24 | 50,00% | -0,64% | -0,35% | -3,34% | +2,08% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 27 | 48,15% | -0,49% | -0,39% | -3,19% | +2,29% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 22 | 45,45% | -0,79% | -0,46% | -3,22% | +2,20% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 28 | 50,00% | -0,56% | -0,03% | -3,18% | +2,33% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 20 | 55,00% | -0,06% | +0,06% | -2,79% | +2,42% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 20 | 55,00% | -0,44% | -0,18% | -3,64% | +2,78% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 22 | 59,09% | -1,01% | +0,03% | -4,01% | +2,36% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 25 | 60,00% | -0,90% | +0,04% | -3,86% | +2,54% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 20 | 50,00% | -0,74% | -0,63% | -3,90% | +2,47% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 26 | 42,31% | -0,85% | +0,06% | -3,84% | +2,58% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 18 | 50,00% | -0,54% | +0,54% | -3,53% | +2,71% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 17 | 35,29% | -1,25% | -0,80% | -4,54% | +2,87% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 19 | 42,11% | -1,42% | -0,28% | -5,05% | +2,37% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 22 | 40,91% | -1,25% | -0,21% | -4,83% | +2,58% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 17 | 29,41% | -0,97% | -1,30% | -4,94% | +2,50% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 23 | 65,22% | -1,35% | +1,14% | -4,83% | +2,62% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 15 | 73,33% | -1,39% | +1,39% | -4,75% | +2,78% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 14 | 57,14% | -3,18% | +0,21% | -5,68% | +2,77% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 15 | 66,67% | -2,40% | +0,10% | -6,07% | +2,35% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 18 | 72,22% | -2,52% | +0,60% | -5,71% | +2,61% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 13 | 30,77% | -2,26% | -1,99% | -5,71% | +2,52% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 19 | 57,89% | -2,60% | +1,53% | -5,78% | +2,66% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 11 | 72,73% | -2,36% | +2,36% | -6,04% | +2,90% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 11 | 63,64% | -2,96% | -0,06% | -6,79% | +3,37% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 8 | 87,50% | -3,72% | +2,53% | -7,04% | +2,92% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 11 | 90,91% | -3,45% | +2,59% | -6,78% | +3,19% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 7 | 28,57% | -3,91% | -1,48% | -6,83% | +3,09% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 12 | 58,33% | -3,10% | -0,33% | -6,80% | +3,22% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 5 | 80,00% | -1,15% | +1,15% | -6,51% | +4,11% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 2 | 0,00% | -3,04% | -3,04% | -9,26% | +1,67% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -3,39% | +3,39% | -9,20% | +1,74% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | -2,79% | +2,79% | -9,18% | +1,62% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 2 | 0,00% | -3,04% | -3,04% | -9,26% | +1,67% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 3 | 0,00% | -2,79% | -2,79% | -9,18% | +1,62% | FEEDBACK RAPIDO |
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
