# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-16 05:35 UTC

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

Segnali totali salvati: **111**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-16 | BTC | 63.005,56 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-16 | DOGE | 0.06966 | +4 | +4 | +3 | +2 | +1 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-16 | SOL | 75,33 | +1 | +3 | +3 | +3 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-15 | BTC | 63.058,07 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-15 | DOGE | 0.07017 | +4 | +4 | +3 | +2 | +1 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-15 | SOL | 75,40 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-14 | BTC | 62.749,25 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-14 | DOGE | 0.06940 | +2 | +4 | +3 | +2 | 0 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-14 | SOL | 75,41 | +3 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-11 | BTC | 63.889,59 | +6 | +4 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-11 | DOGE | 0.06985 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-11 | SOL | 75,73 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 37 | 36 | 35 | 34 | 34 | 32 | 29 | 25 | 18 | 9 | 0 | 0 |
| SOL | 37 | 36 | 35 | 34 | 34 | 32 | 29 | 25 | 18 | 9 | 0 | 0 |
| DOGE | 37 | 36 | 35 | 34 | 34 | 32 | 29 | 25 | 18 | 9 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-18 | 30g | 2026-08-17 | domani |
| SOL | 2026-07-18 | 30g | 2026-08-17 | domani |
| DOGE | 2026-07-18 | 30g | 2026-08-17 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 34 | 47,06% | +0,00% | -0,03% | PRIMA CALIBRAZIONE |
| BTC | 2g | 33 | 45,45% | +0,04% | -0,11% | PRIMA CALIBRAZIONE |
| BTC | 3g | 32 | 37,50% | -0,14% | -0,36% | PRIMA CALIBRAZIONE |
| BTC | 5g | 32 | 28,12% | -0,09% | -0,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | 30 | 40,00% | +0,05% | -0,31% | PRIMA CALIBRAZIONE |
| BTC | 10g | 27 | 44,44% | +0,32% | -0,02% | FEEDBACK RAPIDO |
| BTC | 14g | 23 | 39,13% | -0,05% | -0,20% | FEEDBACK RAPIDO |
| BTC | 21g | 16 | 25,00% | -0,57% | -0,84% | FEEDBACK RAPIDO |
| BTC | 30g | 9 | 88,89% | +0,31% | +0,87% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 29 | 48,28% | +0,01% | -0,21% | FEEDBACK RAPIDO |
| SOL | 2g | 28 | 42,86% | -0,01% | -0,27% | FEEDBACK RAPIDO |
| SOL | 3g | 27 | 44,44% | +0,09% | -0,24% | FEEDBACK RAPIDO |
| SOL | 5g | 27 | 48,15% | -0,10% | -0,30% | FEEDBACK RAPIDO |
| SOL | 7g | 25 | 60,00% | +0,02% | +0,22% | FEEDBACK RAPIDO |
| SOL | 10g | 22 | 50,00% | -0,31% | +0,04% | FEEDBACK RAPIDO |
| SOL | 14g | 19 | 57,89% | -1,57% | +0,34% | FEEDBACK RAPIDO |
| SOL | 21g | 14 | 57,14% | -2,85% | -0,16% | FEEDBACK RAPIDO |
| SOL | 30g | 8 | 37,50% | -1,22% | -0,99% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 34 | 41,18% | -0,04% | -0,05% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 33 | 45,45% | -0,13% | -0,13% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 32 | 40,62% | -0,35% | -0,00% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 32 | 50,00% | -0,59% | +0,19% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 30 | 60,00% | -0,91% | +0,57% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 27 | 51,85% | -1,48% | +0,83% | FEEDBACK RAPIDO |
| DOGE | 14g | 24 | 62,50% | -2,22% | +1,68% | FEEDBACK RAPIDO |
| DOGE | 21g | 18 | 83,33% | -3,52% | +2,95% | FEEDBACK RAPIDO |
| DOGE | 30g | 9 | 100,00% | -4,31% | +4,31% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 34 | 47,06% | +0,00% | -0,03% | -0,30% | +0,54% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 36 | 50,00% | -0,01% | -0,01% | -0,31% | +0,50% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 36 | 50,00% | -0,01% | -0,01% | -0,31% | +0,50% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 32 | 50,00% | -0,04% | -0,04% | -0,35% | +0,42% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 31 | 35,48% | +0,14% | -0,39% | -0,17% | +0,65% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 6 | 16,67% | +0,58% | -0,58% | +0,04% | +0,84% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 33 | 45,45% | +0,04% | -0,11% | -0,43% | +0,73% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 35 | 48,57% | +0,01% | +0,01% | -0,44% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 35 | 48,57% | +0,01% | +0,01% | -0,44% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 31 | 48,39% | -0,08% | -0,08% | -0,54% | +0,61% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 30 | 43,33% | +0,19% | -0,38% | -0,25% | +0,88% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 5 | 20,00% | +0,77% | -0,77% | +0,47% | +1,49% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 32 | 37,50% | -0,14% | -0,36% | -1,40% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 34 | 50,00% | -0,06% | -0,06% | -1,37% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 34 | 50,00% | -0,06% | -0,06% | -1,37% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 30 | 50,00% | -0,09% | -0,09% | -1,39% | +1,46% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 29 | 34,48% | +0,27% | -0,46% | -1,13% | +1,83% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,18% | -1,18% | -0,41% | +2,46% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 32 | 28,12% | -0,09% | -0,49% | -2,11% | +2,04% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 34 | 38,24% | -0,08% | -0,08% | -2,07% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 34 | 38,24% | -0,08% | -0,08% | -2,07% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 30 | 40,00% | -0,01% | -0,01% | -2,06% | +2,03% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 29 | 37,93% | +0,10% | -0,74% | -1,83% | +2,30% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,14% | -1,14% | -1,16% | +2,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 30 | 40,00% | +0,05% | -0,31% | -2,32% | +2,50% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 32 | 50,00% | +0,01% | +0,01% | -2,31% | +2,51% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 32 | 50,00% | +0,01% | +0,01% | -2,31% | +2,51% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 28 | 53,57% | +0,20% | +0,20% | -2,28% | +2,53% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 27 | 33,33% | +0,43% | -0,85% | -2,03% | +2,78% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,94% | -1,94% | -1,23% | +3,13% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 27 | 44,44% | +0,32% | -0,02% | -2,57% | +2,95% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 29 | 51,72% | +0,13% | +0,13% | -2,60% | +2,93% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 29 | 51,72% | +0,13% | +0,13% | -2,60% | +2,93% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 25 | 60,00% | +0,48% | +0,48% | -2,46% | +3,02% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 24 | 33,33% | +0,40% | -0,30% | -2,27% | +3,29% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,32% | -1,32% | -1,42% | +3,31% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 23 | 39,13% | -0,05% | -0,20% | -2,94% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 25 | 40,00% | -0,17% | -0,17% | -2,96% | +3,31% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 25 | 40,00% | -0,17% | -0,17% | -2,96% | +3,31% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 21 | 47,62% | +0,27% | +0,27% | -2,69% | +3,49% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 20 | 60,00% | +0,10% | +0,14% | -2,59% | +3,73% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 3 | 66,67% | +0,00% | -0,00% | -1,93% | +3,08% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 16 | 25,00% | -0,57% | -0,84% | -3,22% | +3,82% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 18 | 38,89% | -0,63% | -0,63% | -3,27% | +3,69% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 18 | 38,89% | -0,63% | -0,63% | -3,27% | +3,69% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 14 | 42,86% | -0,42% | -0,42% | -2,92% | +4,07% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 15 | 26,67% | -0,36% | -0,09% | -2,97% | +3,98% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 9 | 88,89% | +0,31% | +0,87% | -2,48% | +5,20% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 9 | 66,67% | +0,31% | +0,31% | -2,48% | +5,20% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 9 | 66,67% | +0,31% | +0,31% | -2,48% | +5,20% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 9 | 66,67% | +0,31% | +0,31% | -2,48% | +5,20% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 8 | 50,00% | +0,18% | -0,58% | -2,38% | +5,26% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 34 | 41,18% | -0,04% | -0,05% | -0,50% | +0,68% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 36 | 52,78% | -0,15% | +0,19% | -0,62% | +0,55% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 36 | 52,78% | -0,15% | +0,19% | -0,62% | +0,55% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 52,94% | -0,04% | +0,09% | -0,53% | +0,67% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 31 | 48,39% | -0,14% | +0,10% | -0,61% | +0,48% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 23 | 39,13% | +0,22% | -0,22% | -0,30% | +0,77% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,92% | +1,13% | +0,84% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 33 | 45,45% | -0,13% | -0,13% | -0,77% | +0,95% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 35 | 48,57% | -0,24% | +0,03% | -0,88% | +0,80% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 35 | 48,57% | -0,24% | +0,03% | -0,88% | +0,80% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 33 | 48,48% | -0,34% | +0,10% | -0,92% | +0,76% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 30 | 60,00% | -0,30% | +0,30% | -0,91% | +0,61% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 23 | 47,83% | +0,18% | -0,18% | -0,46% | +1,21% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +3,12% | +2,46% | +2,21% | +3,52% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 32 | 40,62% | -0,35% | -0,00% | -1,84% | +2,02% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | -0,46% | -0,09% | -1,94% | +1,85% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,46% | -0,09% | -1,94% | +1,85% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 32 | 50,00% | -0,71% | +0,13% | -1,90% | +1,72% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,49% | +0,49% | -2,02% | +1,67% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 22 | 40,91% | -0,10% | +0,10% | -1,86% | +2,37% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,70% | +1,18% | -0,25% | +5,07% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 32 | 50,00% | -0,59% | +0,19% | -2,65% | +2,44% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | -0,68% | +0,08% | -2,71% | +2,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,68% | +0,08% | -2,71% | +2,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 32 | 46,88% | -0,69% | +0,05% | -2,71% | +2,16% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 30 | 63,33% | -0,75% | +0,75% | -2,89% | +2,13% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 22 | 54,55% | -0,40% | +0,40% | -2,68% | +2,79% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 30 | 60,00% | -0,91% | +0,57% | -3,16% | +2,57% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 32 | 56,25% | -0,99% | +0,34% | -3,24% | +2,47% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 32 | 56,25% | -0,99% | +0,34% | -3,24% | +2,47% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 30 | 56,67% | -0,99% | +0,30% | -3,28% | +2,34% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 30 | 63,33% | -1,05% | +1,05% | -3,36% | +2,36% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 22 | 54,55% | -0,91% | +0,91% | -3,18% | +2,88% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,63% | +0,36% | -0,50% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 27 | 51,85% | -1,48% | +0,83% | -3,97% | +2,65% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 29 | 51,72% | -1,50% | +0,68% | -4,01% | +2,54% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 29 | 51,72% | -1,50% | +0,68% | -4,01% | +2,54% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 27 | 51,85% | -1,55% | +0,67% | -4,04% | +2,39% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 28 | 67,86% | -1,54% | +1,54% | -4,09% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 20 | 65,00% | -1,32% | +1,32% | -4,00% | +2,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 24 | 62,50% | -2,22% | +1,68% | -4,89% | +2,86% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 25 | 64,00% | -2,30% | +1,45% | -4,97% | +2,67% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 25 | 64,00% | -2,30% | +1,45% | -4,97% | +2,67% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 23 | 65,22% | -2,36% | +1,44% | -5,07% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 25 | 76,00% | -2,30% | +2,30% | -4,97% | +2,67% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 20 | 70,00% | -2,09% | +2,09% | -4,80% | +3,07% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 18 | 83,33% | -3,52% | +2,95% | -6,03% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 18 | 88,89% | -3,52% | +3,06% | -6,03% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 18 | 88,89% | -3,52% | +3,06% | -6,03% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 16 | 93,75% | -3,80% | +3,28% | -6,31% | +2,38% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 18 | 88,89% | -3,52% | +3,52% | -6,03% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 16 | 87,50% | -3,30% | +3,30% | -5,81% | +2,92% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 9 | 100,00% | -4,31% | +4,31% | -6,87% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 9 | 100,00% | -4,31% | +4,31% | -6,87% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 9 | 100,00% | -4,31% | +4,31% | -6,87% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 9 | 100,00% | -4,31% | +4,31% | -6,87% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 9 | 100,00% | -4,31% | +4,31% | -6,87% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 8 | 100,00% | -4,09% | +4,09% | -6,72% | +2,82% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 29 | 48,28% | +0,01% | -0,21% | -0,46% | +0,69% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 32 | 56,25% | -0,28% | -0,01% | -0,71% | +0,37% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 35 | 54,29% | -0,16% | -0,10% | -0,62% | +0,49% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 30 | 50,00% | -0,11% | +0,02% | -0,65% | +0,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 34 | 52,94% | -0,09% | -0,01% | -0,57% | +0,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,04% | -0,04% | -0,54% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 28 | 42,86% | -0,01% | -0,27% | -0,66% | +0,89% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 31 | 48,39% | -0,26% | -0,11% | -0,96% | +0,50% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,21% | -0,13% | -0,88% | +0,70% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 29 | 44,83% | -0,19% | -0,16% | -0,88% | +0,72% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 33 | 42,42% | -0,15% | -0,20% | -0,80% | +0,76% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,02% | -0,02% | -0,52% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 27 | 44,44% | +0,09% | -0,24% | -1,86% | +2,00% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 30 | 43,33% | -0,33% | -0,07% | -2,19% | +1,67% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 33 | 42,42% | -0,27% | -0,10% | -2,10% | +1,83% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 28 | 42,86% | -0,22% | -0,29% | -2,02% | +1,85% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 32 | 43,75% | -0,20% | -0,17% | -2,04% | +1,90% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 21 | 42,86% | +0,13% | -0,13% | -1,91% | +1,82% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 27 | 48,15% | -0,10% | -0,30% | -2,59% | +2,61% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 30 | 50,00% | -0,33% | -0,09% | -2,88% | +2,31% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 33 | 48,48% | -0,23% | -0,15% | -2,80% | +2,46% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 28 | 46,43% | -0,42% | -0,16% | -2,75% | +2,42% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 32 | 46,88% | -0,28% | -0,24% | -2,88% | +2,55% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 21 | 52,38% | +0,14% | -0,14% | -2,60% | +2,64% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 25 | 60,00% | +0,02% | +0,22% | -3,10% | +3,11% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 28 | 64,29% | -0,37% | +0,45% | -3,38% | +2,84% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 31 | 64,52% | -0,34% | +0,42% | -3,32% | +2,94% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 26 | 57,69% | -0,10% | -0,02% | -3,24% | +2,96% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 31 | 35,48% | -0,30% | -0,36% | -3,37% | +3,01% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 22 | 50,00% | -0,31% | +0,04% | -3,91% | +3,49% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 25 | 56,00% | -0,40% | +0,46% | -4,27% | +3,14% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 28 | 53,57% | -0,38% | +0,43% | -4,18% | +3,22% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 23 | 47,83% | +0,01% | -0,23% | -4,12% | +3,30% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 29 | 51,72% | -0,49% | +0,32% | -4,20% | +3,23% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 20 | 55,00% | -0,28% | +0,28% | -3,99% | +3,52% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 19 | 57,89% | -1,57% | +0,34% | -5,00% | +3,53% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 21 | 76,19% | -0,88% | +0,90% | -5,26% | +3,30% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 24 | 79,17% | -1,16% | +1,17% | -5,09% | +3,37% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 19 | 52,63% | -0,63% | -0,45% | -4,92% | +3,51% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 25 | 44,00% | -1,28% | +0,46% | -5,16% | +3,38% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 17 | 47,06% | -0,50% | +0,50% | -5,04% | +3,87% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 14 | 57,14% | -2,85% | -0,16% | -7,27% | +2,80% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 14 | 71,43% | -2,54% | +1,45% | -7,19% | +2,56% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 17 | 76,47% | -2,58% | +1,68% | -6,99% | +2,80% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 12 | 33,33% | -2,52% | -1,10% | -6,92% | +2,78% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 18 | 61,11% | -2,39% | +0,10% | -6,99% | +2,84% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 10 | 70,00% | -0,84% | +0,84% | -6,72% | +3,25% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 8 | 37,50% | -1,22% | -0,99% | -7,61% | +3,12% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 7 | 71,43% | -1,73% | +0,94% | -7,87% | +2,83% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 9 | 66,67% | -1,34% | +0,72% | -7,77% | +2,94% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | -1,55% | -0,85% | -8,00% | +2,76% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 9 | 33,33% | -1,34% | -0,74% | -7,77% | +2,94% | FEEDBACK RAPIDO |
| SOL | 30g | Classic technical | CALIBRABILE | 2 | 50,00% | -0,25% | +0,25% | -6,43% | +4,20% | FEEDBACK RAPIDO |
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
