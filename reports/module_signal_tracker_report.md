# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-09 05:17 UTC

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

Segnali totali salvati: **96**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-09 | BTC | 64.733,97 | +7 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-09 | DOGE | 0.06994 | +4 | +4 | +3 | +3 | 0 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-09 | SOL | 75,92 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-08 | BTC | 64.965,57 | +8 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-08 | DOGE | 0.07012 | +3 | +3 | +2 | +3 | -1 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-08 | SOL | 74,51 | +3 | +4 | +3 | +3 | -2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-07 | BTC | 64.173,65 | +6 | +4 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-07 | DOGE | 0.06903 | +1 | +2 | +1 | +2 | -1 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-07 | SOL | 72,63 | +1 | +4 | +3 | +3 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-06 | BTC | 64.856,39 | +6 | +4 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-06 | DOGE | 0.06999 | +2 | +2 | +1 | +2 | 0 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-06 | SOL | 74,14 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 32 | 31 | 30 | 29 | 27 | 25 | 22 | 18 | 11 | 2 | 0 | 0 |
| SOL | 32 | 31 | 30 | 29 | 27 | 25 | 22 | 18 | 11 | 2 | 0 | 0 |
| DOGE | 32 | 31 | 30 | 29 | 27 | 25 | 22 | 18 | 11 | 2 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-11 | 30g | 2026-08-10 | domani |
| SOL | 2026-07-11 | 30g | 2026-08-10 | domani |
| DOGE | 2026-07-11 | 30g | 2026-08-10 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 29 | 48,28% | +0,06% | +0,02% | FEEDBACK RAPIDO |
| BTC | 2g | 28 | 46,43% | +0,19% | +0,02% | FEEDBACK RAPIDO |
| BTC | 3g | 27 | 40,74% | +0,08% | -0,18% | FEEDBACK RAPIDO |
| BTC | 5g | 25 | 32,00% | +0,34% | -0,17% | FEEDBACK RAPIDO |
| BTC | 7g | 23 | 43,48% | +0,40% | -0,07% | FEEDBACK RAPIDO |
| BTC | 10g | 20 | 40,00% | +0,58% | +0,12% | FEEDBACK RAPIDO |
| BTC | 14g | 16 | 56,25% | +0,20% | +0,08% | FEEDBACK RAPIDO |
| BTC | 21g | 10 | 30,00% | +0,33% | -0,10% | FEEDBACK RAPIDO |
| BTC | 30g | 2 | 100,00% | +2,05% | +2,05% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 24 | 54,17% | +0,03% | -0,23% | FEEDBACK RAPIDO |
| SOL | 2g | 23 | 43,48% | -0,09% | -0,39% | FEEDBACK RAPIDO |
| SOL | 3g | 22 | 45,45% | -0,14% | -0,54% | FEEDBACK RAPIDO |
| SOL | 5g | 20 | 45,00% | -0,59% | -0,87% | FEEDBACK RAPIDO |
| SOL | 7g | 19 | 52,63% | -0,73% | -0,45% | FEEDBACK RAPIDO |
| SOL | 10g | 16 | 37,50% | -1,54% | -0,63% | FEEDBACK RAPIDO |
| SOL | 14g | 14 | 57,14% | -3,18% | +0,21% | FEEDBACK RAPIDO |
| SOL | 21g | 10 | 70,00% | -3,32% | +0,00% | FEEDBACK RAPIDO |
| SOL | 30g | 1 | 0,00% | -4,50% | -4,50% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 29 | 41,38% | -0,04% | -0,06% | FEEDBACK RAPIDO |
| DOGE | 2g | 28 | 46,43% | -0,14% | -0,15% | FEEDBACK RAPIDO |
| DOGE | 3g | 27 | 40,74% | -0,42% | -0,00% | FEEDBACK RAPIDO |
| DOGE | 5g | 26 | 53,85% | -0,73% | +0,23% | FEEDBACK RAPIDO |
| DOGE | 7g | 24 | 58,33% | -1,12% | +0,71% | FEEDBACK RAPIDO |
| DOGE | 10g | 21 | 57,14% | -1,76% | +1,16% | FEEDBACK RAPIDO |
| DOGE | 14g | 18 | 72,22% | -2,82% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 21g | 11 | 100,00% | -4,08% | +4,08% | FEEDBACK RAPIDO |
| DOGE | 30g | 2 | 100,00% | -4,54% | +4,54% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 29 | 48,28% | +0,06% | +0,02% | -0,27% | +0,60% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 31 | 51,61% | +0,04% | +0,04% | -0,28% | +0,56% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 31 | 51,61% | +0,04% | +0,04% | -0,28% | +0,56% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 27 | 51,85% | +0,01% | +0,01% | -0,33% | +0,47% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 26 | 34,62% | +0,23% | -0,37% | -0,11% | +0,75% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 4 | 0,00% | +0,76% | -0,76% | +0,03% | +1,12% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 28 | 46,43% | +0,19% | +0,02% | -0,31% | +0,87% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 30 | 50,00% | +0,15% | +0,15% | -0,33% | +0,83% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 30 | 50,00% | +0,15% | +0,15% | -0,33% | +0,83% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 26 | 50,00% | +0,06% | +0,06% | -0,42% | +0,73% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 25 | 48,00% | +0,39% | -0,26% | -0,07% | +1,06% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 4 | 25,00% | +0,86% | -0,86% | +0,50% | +1,73% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 27 | 40,74% | +0,08% | -0,18% | -1,35% | +1,75% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 29 | 55,17% | +0,16% | +0,16% | -1,32% | +1,72% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 29 | 55,17% | +0,16% | +0,16% | -1,32% | +1,72% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 25 | 56,00% | +0,16% | +0,16% | -1,34% | +1,63% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 24 | 37,50% | +0,61% | -0,27% | -1,02% | +2,09% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,18% | -1,18% | -0,41% | +2,46% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 25 | 32,00% | +0,34% | -0,17% | -2,08% | +2,37% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 27 | 44,44% | +0,32% | +0,32% | -2,04% | +2,39% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 27 | 44,44% | +0,32% | +0,32% | -2,04% | +2,39% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 23 | 47,83% | +0,48% | +0,48% | -2,02% | +2,39% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 22 | 50,00% | +0,65% | -0,36% | -1,72% | +2,77% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,14% | -1,14% | -1,16% | +2,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 23 | 43,48% | +0,40% | -0,07% | -2,46% | +2,71% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 25 | 56,00% | +0,32% | +0,32% | -2,43% | +2,71% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 25 | 56,00% | +0,32% | +0,32% | -2,43% | +2,71% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 21 | 61,90% | +0,64% | +0,64% | -2,41% | +2,77% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 20 | 35,00% | +0,96% | -0,54% | -2,09% | +3,11% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 3 | 0,00% | +1,41% | -1,41% | -1,92% | +2,79% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 20 | 40,00% | +0,58% | +0,12% | -2,76% | +3,10% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 22 | 50,00% | +0,31% | +0,31% | -2,78% | +3,06% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 22 | 50,00% | +0,31% | +0,31% | -2,78% | +3,06% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 18 | 61,11% | +0,84% | +0,84% | -2,64% | +3,21% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 18 | 38,89% | +0,75% | -0,12% | -2,43% | +3,48% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 2 | 0,00% | +1,45% | -1,45% | -2,23% | +2,64% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 16 | 56,25% | +0,20% | +0,08% | -3,08% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 18 | 50,00% | +0,01% | +0,01% | -3,10% | +3,69% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 18 | 50,00% | +0,01% | +0,01% | -3,10% | +3,69% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 14 | 64,29% | +0,72% | +0,72% | -2,72% | +4,07% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 15 | 53,33% | +0,23% | +0,10% | -2,77% | +3,98% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 10 | 30,00% | +0,33% | -0,10% | -2,62% | +5,02% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 11 | 54,55% | +0,45% | +0,45% | -2,62% | +4,99% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 11 | 54,55% | +0,45% | +0,45% | -2,62% | +4,99% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +0,50% | +0,50% | -2,49% | +5,16% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 10 | 10,00% | +0,42% | -0,65% | -2,56% | +5,01% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 2 | 100,00% | +2,05% | +2,05% | -2,80% | +5,29% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | +2,05% | +2,05% | -2,80% | +5,29% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | +2,05% | +2,05% | -2,80% | +5,29% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 2 | 100,00% | +2,05% | +2,05% | -2,80% | +5,29% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 1 | 0,00% | +2,74% | -2,74% | -2,32% | +5,81% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 29 | 41,38% | -0,04% | -0,06% | -0,49% | +0,61% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 31 | 54,84% | -0,16% | +0,22% | -0,63% | +0,47% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 31 | 54,84% | -0,16% | +0,22% | -0,63% | +0,47% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 29 | 55,17% | -0,04% | +0,11% | -0,53% | +0,60% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,12% | +0,12% | -0,60% | +0,51% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 21 | 38,10% | +0,20% | -0,20% | -0,32% | +0,77% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,65% | +1,60% | +1,48% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 28 | 46,43% | -0,14% | -0,15% | -0,76% | +0,79% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 30 | 50,00% | -0,28% | +0,03% | -0,89% | +0,63% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 30 | 50,00% | -0,28% | +0,03% | -0,89% | +0,63% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 28 | 50,00% | -0,39% | +0,13% | -0,94% | +0,58% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 29 | 58,62% | -0,30% | +0,30% | -0,90% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,19% | -0,19% | -0,49% | +1,28% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +4,20% | +3,33% | +3,09% | +4,54% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 27 | 40,74% | -0,42% | -0,00% | -2,00% | +1,78% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 29 | 48,28% | -0,53% | -0,10% | -2,11% | +1,60% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 29 | 48,28% | -0,53% | -0,10% | -2,11% | +1,60% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 27 | 51,85% | -0,84% | +0,16% | -2,07% | +1,42% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 28 | 50,00% | -0,55% | +0,55% | -2,13% | +1,63% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 20 | 40,00% | -0,14% | +0,14% | -1,99% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 26 | 53,85% | -0,73% | +0,23% | -2,98% | +2,09% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 27 | 51,85% | -0,85% | +0,10% | -3,06% | +1,93% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 27 | 51,85% | -0,85% | +0,10% | -3,06% | +1,93% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 25 | 52,00% | -0,88% | +0,07% | -3,10% | +1,73% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 27 | 62,96% | -0,85% | +0,85% | -3,06% | +1,93% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 20 | 55,00% | -0,45% | +0,45% | -2,87% | +2,58% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 24 | 58,33% | -1,12% | +0,71% | -3,55% | +2,31% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 25 | 60,00% | -1,24% | +0,47% | -3,68% | +2,13% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 25 | 60,00% | -1,24% | +0,47% | -3,68% | +2,13% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 23 | 60,87% | -1,26% | +0,42% | -3,76% | +1,92% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 25 | 64,00% | -1,24% | +1,24% | -3,68% | +2,13% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 20 | 55,00% | -1,01% | +1,01% | -3,42% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 21 | 57,14% | -1,76% | +1,16% | -4,42% | +2,46% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 22 | 59,09% | -1,86% | +1,01% | -4,52% | +2,25% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 22 | 59,09% | -1,86% | +1,01% | -4,52% | +2,25% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 20 | 60,00% | -1,96% | +1,03% | -4,62% | +2,02% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 22 | 68,18% | -1,86% | +1,86% | -4,52% | +2,25% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 18 | 61,11% | -1,42% | +1,42% | -4,14% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 18 | 72,22% | -2,82% | +2,29% | -5,58% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 18 | 77,78% | -2,82% | +2,39% | -5,58% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 18 | 77,78% | -2,82% | +2,39% | -5,58% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 16 | 81,25% | -2,97% | +2,49% | -5,80% | +2,38% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 18 | 77,78% | -2,82% | +2,82% | -5,58% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 16 | 75,00% | -2,59% | +2,59% | -5,33% | +2,92% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 11 | 100,00% | -4,08% | +4,08% | -6,57% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 11 | 100,00% | -4,08% | +4,08% | -6,57% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 11 | 100,00% | -4,08% | +4,08% | -6,57% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 11 | 100,00% | -4,08% | +4,08% | -6,57% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 11 | 100,00% | -4,08% | +4,08% | -6,57% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 10 | 100,00% | -3,94% | +3,94% | -6,42% | +2,65% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 2 | 100,00% | -4,54% | +4,54% | -7,34% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -4,54% | +4,54% | -7,34% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | -4,54% | +4,54% | -7,34% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 2 | 100,00% | -4,54% | +4,54% | -7,34% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 2 | 100,00% | -4,54% | +4,54% | -7,34% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 2 | 100,00% | -4,54% | +4,54% | -7,34% | +2,87% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 24 | 54,17% | +0,03% | -0,23% | -0,49% | +0,71% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 27 | 62,96% | -0,30% | +0,02% | -0,78% | +0,33% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 30 | 60,00% | -0,16% | -0,09% | -0,67% | +0,48% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 25 | 56,00% | -0,11% | +0,05% | -0,72% | +0,49% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 31 | 48,39% | -0,06% | -0,05% | -0,57% | +0,56% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,04% | -0,04% | -0,54% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 23 | 43,48% | -0,09% | -0,39% | -0,74% | +0,82% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 26 | 50,00% | -0,37% | -0,19% | -1,08% | +0,37% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 29 | 48,28% | -0,30% | -0,21% | -0,97% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 24 | 45,83% | -0,30% | -0,26% | -1,00% | +0,63% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 30 | 40,00% | -0,21% | -0,17% | -0,86% | +0,70% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,02% | -0,02% | -0,52% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 22 | 45,45% | -0,14% | -0,54% | -2,18% | +1,83% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 25 | 44,00% | -0,62% | -0,31% | -2,54% | +1,46% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 28 | 42,86% | -0,52% | -0,31% | -2,39% | +1,66% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 23 | 43,48% | -0,51% | -0,59% | -2,37% | +1,66% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 29 | 44,83% | -0,45% | +0,04% | -2,27% | +1,73% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 20 | 45,00% | -0,13% | +0,13% | -2,07% | +1,62% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 20 | 45,00% | -0,59% | -0,87% | -3,08% | +2,35% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 23 | 47,83% | -0,83% | -0,52% | -3,39% | +2,00% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 26 | 46,15% | -0,65% | -0,54% | -3,23% | +2,22% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 21 | 42,86% | -1,00% | -0,65% | -3,27% | +2,11% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 27 | 51,85% | -0,72% | +0,11% | -3,21% | +2,27% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 19 | 57,89% | -0,25% | +0,25% | -2,83% | +2,34% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 19 | 52,63% | -0,73% | -0,45% | -3,79% | +2,64% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 21 | 57,14% | -1,30% | -0,20% | -4,17% | +2,21% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 24 | 58,33% | -1,15% | -0,17% | -3,98% | +2,42% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 19 | 47,37% | -1,04% | -0,93% | -4,06% | +2,31% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 25 | 44,00% | -1,08% | +0,27% | -3,96% | +2,47% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 17 | 52,94% | -0,87% | +0,87% | -3,69% | +2,55% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 16 | 37,50% | -1,54% | -0,63% | -4,54% | +2,81% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 18 | 38,89% | -1,69% | -0,49% | -5,08% | +2,29% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 21 | 38,10% | -1,48% | -0,39% | -4,85% | +2,52% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 16 | 25,00% | -1,25% | -1,59% | -4,97% | +2,41% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 22 | 68,18% | -1,56% | +1,34% | -4,85% | +2,57% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 14 | 78,57% | -1,74% | +1,74% | -4,76% | +2,70% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 14 | 57,14% | -3,18% | +0,21% | -5,68% | +2,77% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 14 | 64,29% | -2,59% | +0,09% | -5,97% | +2,47% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 17 | 70,59% | -2,68% | +0,62% | -5,61% | +2,72% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 12 | 25,00% | -2,47% | -2,18% | -5,56% | +2,67% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 18 | 61,11% | -2,75% | +1,63% | -5,68% | +2,77% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 10 | 80,00% | -2,62% | +2,62% | -5,90% | +3,12% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 10 | 70,00% | -3,32% | +0,00% | -6,77% | +3,35% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 8 | 87,50% | -3,72% | +2,53% | -7,04% | +2,92% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 11 | 90,91% | -3,45% | +2,59% | -6,78% | +3,19% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 7 | 28,57% | -3,91% | -1,48% | -6,83% | +3,09% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 11 | 63,64% | -3,45% | -0,29% | -6,78% | +3,19% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 4 | 100,00% | -1,62% | +1,62% | -6,39% | +4,25% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -3,39% | +3,39% | -9,20% | +1,74% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | -3,39% | +3,39% | -9,20% | +1,74% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 2 | 0,00% | -3,39% | -3,39% | -9,20% | +1,74% | FEEDBACK RAPIDO |
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
