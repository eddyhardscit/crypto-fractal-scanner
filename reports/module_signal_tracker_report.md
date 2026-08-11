# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-11 05:23 UTC

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

Segnali totali salvati: **102**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-11 | BTC | 63.889,59 | +6 | +4 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-11 | DOGE | 0.06985 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-11 | SOL | 75,73 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-10 | BTC | 64.966,07 | +6 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-10 | DOGE | 0.06975 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-10 | SOL | 76,57 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-09 | BTC | 64.733,97 | +7 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-09 | DOGE | 0.06994 | +4 | +4 | +3 | +3 | 0 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-09 | SOL | 75,92 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-08 | BTC | 64.965,57 | +8 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-08 | DOGE | 0.07012 | +3 | +3 | +2 | +3 | -1 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-08 | SOL | 74,51 | +3 | +4 | +3 | +3 | -2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 34 | 33 | 32 | 31 | 29 | 27 | 24 | 20 | 13 | 4 | 0 | 0 |
| SOL | 34 | 33 | 32 | 31 | 29 | 27 | 24 | 20 | 13 | 4 | 0 | 0 |
| DOGE | 34 | 33 | 32 | 31 | 29 | 27 | 24 | 20 | 13 | 4 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-13 | 30g | 2026-08-12 | domani |
| SOL | 2026-07-13 | 30g | 2026-08-12 | domani |
| DOGE | 2026-07-13 | 30g | 2026-08-12 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 31 | 48,39% | +0,02% | -0,02% | PRIMA CALIBRAZIONE |
| BTC | 2g | 30 | 46,67% | +0,13% | -0,03% | PRIMA CALIBRAZIONE |
| BTC | 3g | 29 | 41,38% | +0,06% | -0,18% | FEEDBACK RAPIDO |
| BTC | 5g | 27 | 33,33% | +0,30% | -0,17% | FEEDBACK RAPIDO |
| BTC | 7g | 25 | 48,00% | +0,51% | +0,08% | FEEDBACK RAPIDO |
| BTC | 10g | 22 | 45,45% | +0,63% | +0,21% | FEEDBACK RAPIDO |
| BTC | 14g | 18 | 50,00% | +0,19% | +0,00% | FEEDBACK RAPIDO |
| BTC | 21g | 12 | 33,33% | +0,17% | -0,18% | FEEDBACK RAPIDO |
| BTC | 30g | 4 | 100,00% | +1,41% | +1,41% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 26 | 53,85% | +0,02% | -0,22% | FEEDBACK RAPIDO |
| SOL | 2g | 25 | 44,00% | +0,02% | -0,26% | FEEDBACK RAPIDO |
| SOL | 3g | 24 | 50,00% | +0,16% | -0,21% | FEEDBACK RAPIDO |
| SOL | 5g | 22 | 50,00% | -0,28% | -0,52% | FEEDBACK RAPIDO |
| SOL | 7g | 20 | 55,00% | -0,44% | -0,18% | FEEDBACK RAPIDO |
| SOL | 10g | 18 | 38,89% | -0,98% | -0,56% | FEEDBACK RAPIDO |
| SOL | 14g | 15 | 60,00% | -2,74% | +0,42% | FEEDBACK RAPIDO |
| SOL | 21g | 12 | 58,33% | -2,97% | -0,32% | FEEDBACK RAPIDO |
| SOL | 30g | 3 | 33,33% | -2,35% | -1,70% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 31 | 41,94% | -0,04% | -0,06% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 30 | 43,33% | -0,16% | -0,16% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 29 | 41,38% | -0,37% | +0,02% | FEEDBACK RAPIDO |
| DOGE | 5g | 27 | 51,85% | -0,71% | +0,22% | FEEDBACK RAPIDO |
| DOGE | 7g | 26 | 57,69% | -1,06% | +0,64% | FEEDBACK RAPIDO |
| DOGE | 10g | 23 | 60,87% | -1,64% | +1,09% | FEEDBACK RAPIDO |
| DOGE | 14g | 19 | 68,42% | -2,68% | +2,16% | FEEDBACK RAPIDO |
| DOGE | 21g | 13 | 100,00% | -3,98% | +3,98% | FEEDBACK RAPIDO |
| DOGE | 30g | 4 | 100,00% | -4,73% | +4,73% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 31 | 48,39% | +0,02% | -0,02% | -0,30% | +0,54% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 33 | 51,52% | +0,00% | +0,00% | -0,31% | +0,50% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 33 | 51,52% | +0,00% | +0,00% | -0,31% | +0,50% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 29 | 51,72% | -0,04% | -0,04% | -0,36% | +0,42% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 28 | 35,71% | +0,17% | -0,39% | -0,16% | +0,67% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 4 | 0,00% | +0,76% | -0,76% | +0,03% | +1,12% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 30 | 46,67% | +0,13% | -0,03% | -0,34% | +0,79% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 32 | 50,00% | +0,10% | +0,10% | -0,36% | +0,75% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 32 | 50,00% | +0,10% | +0,10% | -0,36% | +0,75% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 28 | 50,00% | +0,01% | +0,01% | -0,45% | +0,65% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 27 | 48,15% | +0,31% | -0,29% | -0,13% | +0,96% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 4 | 25,00% | +0,86% | -0,86% | +0,50% | +1,73% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 29 | 41,38% | +0,06% | -0,18% | -1,28% | +1,70% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 31 | 54,84% | +0,14% | +0,14% | -1,26% | +1,68% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 31 | 54,84% | +0,14% | +0,14% | -1,26% | +1,68% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 27 | 55,56% | +0,13% | +0,13% | -1,27% | +1,59% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 26 | 38,46% | +0,54% | -0,27% | -0,97% | +2,01% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,18% | -1,18% | -0,41% | +2,46% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 27 | 33,33% | +0,30% | -0,17% | -1,99% | +2,29% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 29 | 44,83% | +0,29% | +0,29% | -1,96% | +2,31% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 29 | 44,83% | +0,29% | +0,29% | -1,96% | +2,31% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 25 | 48,00% | +0,42% | +0,42% | -1,93% | +2,30% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 24 | 45,83% | +0,58% | -0,44% | -1,65% | +2,64% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,14% | -1,14% | -1,16% | +2,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 25 | 48,00% | +0,51% | +0,08% | -2,23% | +2,76% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 27 | 59,26% | +0,43% | +0,43% | -2,22% | +2,75% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 27 | 59,26% | +0,43% | +0,43% | -2,22% | +2,75% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 23 | 65,22% | +0,74% | +0,74% | -2,17% | +2,82% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 22 | 36,36% | +1,04% | -0,64% | -1,86% | +3,13% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,94% | -1,94% | -1,23% | +3,13% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 22 | 45,45% | +0,63% | +0,21% | -2,72% | +3,05% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 24 | 54,17% | +0,38% | +0,38% | -2,74% | +3,02% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 24 | 54,17% | +0,38% | +0,38% | -2,74% | +3,02% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 20 | 65,00% | +0,87% | +0,87% | -2,61% | +3,15% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 19 | 36,84% | +0,78% | -0,18% | -2,37% | +3,50% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 3 | 0,00% | +1,40% | -1,40% | -1,93% | +3,00% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 18 | 50,00% | +0,19% | +0,00% | -3,10% | +3,58% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 20 | 50,00% | +0,02% | +0,02% | -3,12% | +3,48% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 20 | 50,00% | +0,02% | +0,02% | -3,12% | +3,48% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 16 | 62,50% | +0,65% | +0,65% | -2,79% | +3,76% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 16 | 50,00% | +0,27% | +0,04% | -2,71% | +3,94% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 1 | 0,00% | +0,80% | -0,80% | -1,82% | +3,19% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 12 | 33,33% | +0,17% | -0,18% | -2,86% | +4,69% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 13 | 53,85% | +0,29% | +0,29% | -2,84% | +4,69% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 13 | 53,85% | +0,29% | +0,29% | -2,84% | +4,69% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +0,50% | +0,50% | -2,49% | +5,16% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 11 | 9,09% | +0,49% | -0,70% | -2,60% | +4,94% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 4 | 100,00% | +1,41% | +1,41% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | +1,41% | +1,41% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | +1,41% | +1,41% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 4 | 100,00% | +1,41% | +1,41% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 3 | 33,33% | +1,43% | -1,36% | -3,03% | +5,05% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 31 | 41,94% | -0,04% | -0,06% | -0,50% | +0,60% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 33 | 54,55% | -0,16% | +0,21% | -0,63% | +0,46% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 33 | 54,55% | -0,16% | +0,21% | -0,63% | +0,46% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 31 | 54,84% | -0,05% | +0,10% | -0,54% | +0,59% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,12% | +0,12% | -0,60% | +0,51% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 22 | 40,91% | +0,18% | -0,18% | -0,35% | +0,74% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,92% | +1,13% | +0,84% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 30 | 43,33% | -0,16% | -0,16% | -0,77% | +0,75% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 32 | 46,88% | -0,28% | +0,01% | -0,89% | +0,60% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 32 | 46,88% | -0,28% | +0,01% | -0,89% | +0,60% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 30 | 46,67% | -0,39% | +0,10% | -0,94% | +0,55% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 30 | 60,00% | -0,30% | +0,30% | -0,91% | +0,61% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 22 | 50,00% | +0,17% | -0,17% | -0,49% | +1,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +3,12% | +2,46% | +2,21% | +3,52% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 29 | 41,38% | -0,37% | +0,02% | -1,90% | +1,81% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 31 | 48,39% | -0,48% | -0,07% | -2,00% | +1,64% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 31 | 48,39% | -0,48% | -0,07% | -2,00% | +1,64% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 29 | 51,72% | -0,76% | +0,17% | -1,96% | +1,48% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,49% | +0,49% | -2,02% | +1,67% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 21 | 38,10% | -0,08% | +0,08% | -1,88% | +2,28% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,43% | +1,74% | +0,13% | +5,37% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 27 | 51,85% | -0,71% | +0,22% | -2,93% | +2,09% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 29 | 48,28% | -0,81% | +0,08% | -2,98% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 29 | 48,28% | -0,81% | +0,08% | -2,98% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 27 | 48,15% | -0,83% | +0,05% | -3,01% | +1,75% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 28 | 64,29% | -0,83% | +0,83% | -3,03% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 20 | 55,00% | -0,45% | +0,45% | -2,87% | +2,58% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 26 | 57,69% | -1,06% | +0,64% | -3,46% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 27 | 55,56% | -1,17% | +0,41% | -3,58% | +2,12% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 27 | 55,56% | -1,17% | +0,41% | -3,58% | +2,12% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 25 | 56,00% | -1,18% | +0,36% | -3,65% | +1,93% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 27 | 66,67% | -1,17% | +1,17% | -3,58% | +2,12% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 20 | 55,00% | -1,01% | +1,01% | -3,42% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 23 | 60,87% | -1,64% | +1,09% | -4,27% | +2,41% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 24 | 54,17% | -1,74% | +0,90% | -4,37% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 24 | 54,17% | -1,74% | +0,90% | -4,37% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 22 | 54,55% | -1,82% | +0,90% | -4,45% | +2,01% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 24 | 70,83% | -1,74% | +1,74% | -4,37% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 20 | 65,00% | -1,32% | +1,32% | -4,00% | +2,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 19 | 68,42% | -2,68% | +2,16% | -5,43% | +2,59% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 20 | 70,00% | -2,76% | +1,93% | -5,50% | +2,36% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 20 | 70,00% | -2,76% | +1,93% | -5,50% | +2,36% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 18 | 72,22% | -2,89% | +1,97% | -5,69% | +2,12% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 20 | 80,00% | -2,76% | +2,76% | -5,50% | +2,36% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 17 | 76,47% | -2,45% | +2,45% | -5,18% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 13 | 100,00% | -3,98% | +3,98% | -6,48% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 13 | 100,00% | -3,98% | +3,98% | -6,48% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 13 | 100,00% | -3,98% | +3,98% | -6,48% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 13 | 100,00% | -3,98% | +3,98% | -6,48% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 13 | 100,00% | -3,98% | +3,98% | -6,48% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 12 | 100,00% | -3,86% | +3,86% | -6,35% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 4 | 100,00% | -4,73% | +4,73% | -7,38% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | -4,73% | +4,73% | -7,38% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | -4,73% | +4,73% | -7,38% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 4 | 100,00% | -4,73% | +4,73% | -7,38% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 4 | 100,00% | -4,73% | +4,73% | -7,38% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 4 | 100,00% | -4,73% | +4,73% | -7,38% | +2,68% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 26 | 53,85% | +0,02% | -0,22% | -0,48% | +0,68% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 29 | 62,07% | -0,29% | +0,01% | -0,75% | +0,33% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 32 | 59,38% | -0,16% | -0,10% | -0,65% | +0,47% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 27 | 55,56% | -0,11% | +0,04% | -0,69% | +0,49% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 32 | 50,00% | -0,10% | -0,02% | -0,59% | +0,53% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,04% | -0,04% | -0,54% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 25 | 44,00% | +0,02% | -0,26% | -0,60% | +0,90% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 28 | 50,00% | -0,26% | -0,09% | -0,93% | +0,47% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 31 | 48,39% | -0,20% | -0,12% | -0,85% | +0,69% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 26 | 46,15% | -0,18% | -0,14% | -0,85% | +0,71% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 31 | 38,71% | -0,11% | -0,26% | -0,76% | +0,78% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,02% | -0,02% | -0,52% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 24 | 50,00% | +0,16% | -0,21% | -1,88% | +2,10% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 27 | 48,15% | -0,31% | -0,03% | -2,24% | +1,72% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 30 | 46,67% | -0,25% | -0,06% | -2,14% | +1,89% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 25 | 48,00% | -0,19% | -0,26% | -2,07% | +1,93% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 31 | 41,94% | -0,19% | -0,19% | -2,03% | +1,94% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 21 | 42,86% | +0,13% | -0,13% | -1,91% | +1,82% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 22 | 50,00% | -0,28% | -0,52% | -3,00% | +2,53% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 25 | 52,00% | -0,53% | -0,25% | -3,29% | +2,19% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 28 | 50,00% | -0,40% | -0,30% | -3,16% | +2,37% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 23 | 47,83% | -0,66% | -0,35% | -3,18% | +2,31% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 29 | 48,28% | -0,47% | -0,10% | -3,14% | +2,41% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 20 | 55,00% | -0,06% | +0,06% | -2,79% | +2,42% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 20 | 55,00% | -0,44% | -0,18% | -3,64% | +2,78% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 23 | 60,87% | -0,85% | +0,15% | -3,92% | +2,49% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 26 | 61,54% | -0,76% | +0,15% | -3,78% | +2,65% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 21 | 52,38% | -0,57% | -0,47% | -3,80% | +2,60% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 27 | 40,74% | -0,71% | -0,04% | -3,76% | +2,69% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 19 | 47,37% | -0,37% | +0,37% | -3,44% | +2,85% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 18 | 38,89% | -0,98% | -0,56% | -4,38% | +3,05% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 20 | 45,00% | -1,17% | -0,09% | -4,89% | +2,56% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 23 | 43,48% | -1,04% | -0,05% | -4,70% | +2,74% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 18 | 33,33% | -0,72% | -1,03% | -4,76% | +2,70% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 24 | 62,50% | -1,14% | +0,94% | -4,70% | +2,77% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 16 | 68,75% | -1,08% | +1,08% | -4,56% | +2,99% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 15 | 60,00% | -2,74% | +0,42% | -5,54% | +2,99% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 16 | 68,75% | -2,04% | +0,30% | -5,91% | +2,57% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 19 | 73,68% | -2,21% | +0,74% | -5,59% | +2,79% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 14 | 35,71% | -1,86% | -1,61% | -5,55% | +2,76% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 20 | 55,00% | -2,30% | +1,28% | -5,66% | +2,82% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 12 | 66,67% | -1,88% | +1,88% | -5,83% | +3,15% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 12 | 58,33% | -2,97% | -0,32% | -7,03% | +3,14% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 9 | 77,78% | -3,66% | +1,90% | -7,32% | +2,66% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 12 | 83,33% | -3,43% | +2,11% | -7,01% | +2,97% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 8 | 25,00% | -3,82% | -1,69% | -7,18% | +2,78% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 13 | 61,54% | -3,11% | -0,06% | -7,01% | +3,02% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 5 | 80,00% | -1,15% | +1,15% | -6,51% | +4,11% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 3 | 33,33% | -2,35% | -1,70% | -8,70% | +2,16% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | -2,59% | +2,59% | -8,66% | +2,20% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | -2,34% | +2,34% | -8,78% | +2,00% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 3 | 33,33% | -2,35% | -1,70% | -8,70% | +2,16% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 4 | 0,00% | -2,34% | -2,34% | -8,78% | +2,00% | FEEDBACK RAPIDO |
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
