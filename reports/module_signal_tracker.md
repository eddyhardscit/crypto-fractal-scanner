# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-15 05:34 UTC

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

Segnali totali salvati: **108**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-15 | BTC | 63.058,07 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-15 | DOGE | 0.07017 | +4 | +4 | +3 | +2 | +1 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-15 | SOL | 75,40 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-14 | BTC | 62.749,25 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-14 | DOGE | 0.06940 | +2 | +4 | +3 | +2 | 0 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-14 | SOL | 75,41 | +3 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-11 | BTC | 63.889,59 | +6 | +4 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-11 | DOGE | 0.06985 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-11 | SOL | 75,73 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-10 | BTC | 64.966,07 | +6 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-10 | DOGE | 0.06975 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-10 | SOL | 76,57 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 36 | 35 | 34 | 34 | 33 | 31 | 28 | 24 | 17 | 8 | 0 | 0 |
| SOL | 36 | 35 | 34 | 34 | 33 | 31 | 28 | 24 | 17 | 8 | 0 | 0 |
| DOGE | 36 | 35 | 34 | 34 | 33 | 31 | 28 | 24 | 17 | 8 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-17 | 30g | 2026-08-16 | domani |
| SOL | 2026-07-17 | 30g | 2026-08-16 | domani |
| DOGE | 2026-07-17 | 30g | 2026-08-16 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 33 | 48,48% | +0,01% | -0,03% | PRIMA CALIBRAZIONE |
| BTC | 2g | 32 | 43,75% | +0,02% | -0,12% | PRIMA CALIBRAZIONE |
| BTC | 3g | 32 | 37,50% | -0,14% | -0,36% | PRIMA CALIBRAZIONE |
| BTC | 5g | 31 | 29,03% | -0,05% | -0,46% | PRIMA CALIBRAZIONE |
| BTC | 7g | 29 | 41,38% | +0,14% | -0,23% | FEEDBACK RAPIDO |
| BTC | 10g | 26 | 46,15% | +0,44% | +0,09% | FEEDBACK RAPIDO |
| BTC | 14g | 22 | 40,91% | -0,03% | -0,19% | FEEDBACK RAPIDO |
| BTC | 21g | 15 | 26,67% | -0,46% | -0,74% | FEEDBACK RAPIDO |
| BTC | 30g | 8 | 87,50% | +0,47% | +0,85% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 28 | 50,00% | +0,01% | -0,21% | FEEDBACK RAPIDO |
| SOL | 2g | 27 | 44,44% | -0,01% | -0,27% | FEEDBACK RAPIDO |
| SOL | 3g | 27 | 44,44% | +0,09% | -0,24% | FEEDBACK RAPIDO |
| SOL | 5g | 26 | 50,00% | -0,08% | -0,29% | FEEDBACK RAPIDO |
| SOL | 7g | 24 | 62,50% | +0,05% | +0,27% | FEEDBACK RAPIDO |
| SOL | 10g | 21 | 47,62% | -0,40% | -0,03% | FEEDBACK RAPIDO |
| SOL | 14g | 18 | 55,56% | -1,80% | +0,22% | FEEDBACK RAPIDO |
| SOL | 21g | 14 | 57,14% | -2,85% | -0,16% | FEEDBACK RAPIDO |
| SOL | 30g | 7 | 42,86% | -1,44% | -1,09% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 33 | 42,42% | -0,02% | -0,03% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 32 | 43,75% | -0,14% | -0,15% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 32 | 40,62% | -0,35% | -0,00% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 31 | 51,61% | -0,60% | +0,21% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 29 | 62,07% | -0,92% | +0,60% | FEEDBACK RAPIDO |
| DOGE | 10g | 26 | 53,85% | -1,52% | +0,88% | FEEDBACK RAPIDO |
| DOGE | 14g | 23 | 65,22% | -2,28% | +1,79% | FEEDBACK RAPIDO |
| DOGE | 21g | 17 | 88,24% | -3,42% | +3,42% | FEEDBACK RAPIDO |
| DOGE | 30g | 8 | 100,00% | -4,42% | +4,42% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 33 | 48,48% | +0,01% | -0,03% | -0,30% | +0,55% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 35 | 51,43% | -0,01% | -0,01% | -0,31% | +0,51% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 35 | 51,43% | -0,01% | -0,01% | -0,31% | +0,51% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 31 | 51,61% | -0,04% | -0,04% | -0,36% | +0,43% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 30 | 33,33% | +0,15% | -0,41% | -0,17% | +0,67% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 5 | 0,00% | +0,71% | -0,71% | +0,08% | +1,00% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 32 | 43,75% | +0,02% | -0,12% | -0,46% | +0,74% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | -0,00% | -0,00% | -0,47% | +0,71% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,00% | -0,00% | -0,47% | +0,71% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 30 | 46,67% | -0,09% | -0,09% | -0,57% | +0,61% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 29 | 44,83% | +0,18% | -0,38% | -0,27% | +0,89% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 4 | 25,00% | +0,86% | -0,86% | +0,50% | +1,73% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 32 | 37,50% | -0,14% | -0,36% | -1,40% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 34 | 50,00% | -0,06% | -0,06% | -1,37% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 34 | 50,00% | -0,06% | -0,06% | -1,37% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 30 | 50,00% | -0,09% | -0,09% | -1,39% | +1,46% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 29 | 34,48% | +0,27% | -0,46% | -1,13% | +1,83% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,18% | -1,18% | -0,41% | +2,46% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 31 | 29,03% | -0,05% | -0,46% | -2,10% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 33 | 39,39% | -0,04% | -0,04% | -2,06% | +2,11% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 33 | 39,39% | -0,04% | -0,04% | -2,06% | +2,11% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 29 | 41,38% | +0,03% | +0,03% | -2,05% | +2,08% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 28 | 39,29% | +0,15% | -0,72% | -1,82% | +2,36% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,14% | -1,14% | -1,16% | +2,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 29 | 41,38% | +0,14% | -0,23% | -2,28% | +2,56% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 31 | 51,61% | +0,10% | +0,10% | -2,27% | +2,56% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 31 | 51,61% | +0,10% | +0,10% | -2,27% | +2,56% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 27 | 55,56% | +0,31% | +0,31% | -2,23% | +2,59% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 26 | 34,62% | +0,55% | -0,78% | -1,98% | +2,85% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,94% | -1,94% | -1,23% | +3,13% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 26 | 46,15% | +0,44% | +0,09% | -2,52% | +3,03% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 28 | 53,57% | +0,24% | +0,24% | -2,56% | +3,01% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 28 | 53,57% | +0,24% | +0,24% | -2,56% | +3,01% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 24 | 62,50% | +0,62% | +0,62% | -2,41% | +3,11% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 23 | 34,78% | +0,54% | -0,19% | -2,21% | +3,40% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,32% | -1,32% | -1,42% | +3,31% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 22 | 40,91% | -0,03% | -0,19% | -2,99% | +3,38% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 24 | 41,67% | -0,15% | -0,15% | -3,01% | +3,32% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 24 | 41,67% | -0,15% | -0,15% | -3,01% | +3,32% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 20 | 50,00% | +0,31% | +0,31% | -2,73% | +3,51% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 19 | 57,89% | +0,14% | +0,12% | -2,63% | +3,75% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 3 | 66,67% | +0,00% | -0,00% | -1,93% | +3,08% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 15 | 26,67% | -0,46% | -0,74% | -3,20% | +3,96% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 17 | 41,18% | -0,53% | -0,53% | -3,26% | +3,80% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 17 | 41,18% | -0,53% | -0,53% | -3,26% | +3,80% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 13 | 46,15% | -0,27% | -0,27% | -2,88% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 14 | 28,57% | -0,22% | +0,06% | -2,93% | +4,14% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 8 | 87,50% | +0,47% | +0,85% | -2,52% | +5,21% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 8 | 75,00% | +0,47% | +0,47% | -2,52% | +5,21% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 8 | 75,00% | +0,47% | +0,47% | -2,52% | +5,21% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 8 | 75,00% | +0,47% | +0,47% | -2,52% | +5,21% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 7 | 42,86% | +0,34% | -0,81% | -2,41% | +5,27% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 33 | 42,42% | -0,02% | -0,03% | -0,48% | +0,72% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 35 | 54,29% | -0,13% | +0,22% | -0,61% | +0,58% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 35 | 54,29% | -0,13% | +0,22% | -0,61% | +0,58% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 33 | 54,55% | -0,02% | +0,11% | -0,52% | +0,71% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,12% | +0,12% | -0,60% | +0,51% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 23 | 39,13% | +0,22% | -0,22% | -0,30% | +0,77% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,92% | +1,13% | +0,84% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 32 | 43,75% | -0,14% | -0,15% | -0,79% | +0,96% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | -0,26% | +0,01% | -0,91% | +0,80% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,26% | +0,01% | -0,91% | +0,80% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 32 | 46,88% | -0,36% | +0,09% | -0,96% | +0,77% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 30 | 60,00% | -0,30% | +0,30% | -0,91% | +0,61% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 22 | 50,00% | +0,17% | -0,17% | -0,49% | +1,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +3,12% | +2,46% | +2,21% | +3,52% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 32 | 40,62% | -0,35% | -0,00% | -1,84% | +2,02% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | -0,46% | -0,09% | -1,94% | +1,85% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,46% | -0,09% | -1,94% | +1,85% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 32 | 50,00% | -0,71% | +0,13% | -1,90% | +1,72% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,49% | +0,49% | -2,02% | +1,67% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 22 | 40,91% | -0,10% | +0,10% | -1,86% | +2,37% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,70% | +1,18% | -0,25% | +5,07% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 31 | 51,61% | -0,60% | +0,21% | -2,69% | +2,41% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 33 | 48,48% | -0,69% | +0,09% | -2,75% | +2,26% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 33 | 48,48% | -0,69% | +0,09% | -2,75% | +2,26% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 31 | 48,39% | -0,70% | +0,06% | -2,76% | +2,11% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 30 | 63,33% | -0,75% | +0,75% | -2,89% | +2,13% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 22 | 54,55% | -0,40% | +0,40% | -2,68% | +2,79% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 29 | 62,07% | -0,92% | +0,60% | -3,22% | +2,52% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 31 | 58,06% | -1,01% | +0,37% | -3,30% | +2,42% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 31 | 58,06% | -1,01% | +0,37% | -3,30% | +2,42% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 29 | 58,62% | -1,01% | +0,32% | -3,34% | +2,28% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 30 | 63,33% | -1,05% | +1,05% | -3,36% | +2,36% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,93% | +0,93% | -3,27% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,97% | +0,62% | -0,19% | +6,23% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 26 | 53,85% | -1,52% | +0,88% | -4,06% | +2,59% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 28 | 53,57% | -1,54% | +0,72% | -4,09% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 28 | 53,57% | -1,54% | +0,72% | -4,09% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 26 | 53,85% | -1,59% | +0,71% | -4,14% | +2,32% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 28 | 67,86% | -1,54% | +1,54% | -4,09% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 20 | 65,00% | -1,32% | +1,32% | -4,00% | +2,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 23 | 65,22% | -2,28% | +1,79% | -4,99% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 24 | 66,67% | -2,37% | +1,54% | -5,06% | +2,62% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 24 | 66,67% | -2,37% | +1,54% | -5,06% | +2,62% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 22 | 68,18% | -2,44% | +1,53% | -5,18% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 24 | 75,00% | -2,37% | +2,37% | -5,06% | +2,62% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 20 | 70,00% | -2,09% | +2,09% | -4,80% | +3,07% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 17 | 88,24% | -3,42% | +3,42% | -5,95% | +2,78% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 17 | 94,12% | -3,42% | +3,54% | -5,95% | +2,78% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 17 | 94,12% | -3,42% | +3,54% | -5,95% | +2,78% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 15 | 100,00% | -3,71% | +3,84% | -6,24% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 17 | 88,24% | -3,42% | +3,42% | -5,95% | +2,78% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 16 | 87,50% | -3,30% | +3,30% | -5,81% | +2,92% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 8 | 100,00% | -4,42% | +4,42% | -7,00% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 8 | 100,00% | -4,42% | +4,42% | -7,00% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 8 | 100,00% | -4,42% | +4,42% | -7,00% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 8 | 100,00% | -4,42% | +4,42% | -7,00% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 8 | 100,00% | -4,42% | +4,42% | -7,00% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 7 | 100,00% | -4,17% | +4,17% | -6,85% | +2,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 28 | 50,00% | +0,01% | -0,21% | -0,47% | +0,70% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 31 | 58,06% | -0,28% | -0,00% | -0,72% | +0,37% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 34 | 55,88% | -0,16% | -0,10% | -0,63% | +0,50% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 29 | 51,72% | -0,11% | +0,03% | -0,67% | +0,52% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 33 | 51,52% | -0,09% | -0,02% | -0,58% | +0,52% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,04% | -0,04% | -0,54% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 27 | 44,44% | -0,01% | -0,27% | -0,68% | +0,91% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 30 | 50,00% | -0,27% | -0,11% | -0,98% | +0,51% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 33 | 48,48% | -0,21% | -0,13% | -0,90% | +0,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 28 | 46,43% | -0,19% | -0,16% | -0,91% | +0,74% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 32 | 40,62% | -0,15% | -0,20% | -0,81% | +0,78% | PRIMA CALIBRAZIONE |
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
| SOL | 5g | Global confluence | BENCHMARK | 26 | 50,00% | -0,08% | -0,29% | -2,64% | +2,65% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 29 | 51,72% | -0,32% | -0,08% | -2,93% | +2,34% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 32 | 50,00% | -0,22% | -0,14% | -2,84% | +2,48% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 27 | 48,15% | -0,42% | -0,15% | -2,81% | +2,45% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 32 | 46,88% | -0,28% | -0,24% | -2,88% | +2,55% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 21 | 52,38% | +0,14% | -0,14% | -2,60% | +2,64% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 24 | 62,50% | +0,05% | +0,27% | -3,15% | +3,18% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 27 | 66,67% | -0,35% | +0,50% | -3,45% | +2,89% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 30 | 66,67% | -0,33% | +0,46% | -3,37% | +2,99% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 25 | 60,00% | -0,08% | +0,01% | -3,31% | +3,02% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 31 | 35,48% | -0,30% | -0,36% | -3,37% | +3,01% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 21 | 47,62% | -0,40% | -0,03% | -3,99% | +3,43% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 24 | 54,17% | -0,49% | +0,41% | -4,36% | +3,07% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 27 | 51,85% | -0,46% | +0,39% | -4,25% | +3,17% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 22 | 45,45% | -0,06% | -0,31% | -4,21% | +3,24% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 28 | 53,57% | -0,56% | +0,39% | -4,27% | +3,18% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 20 | 55,00% | -0,28% | +0,28% | -3,99% | +3,52% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 18 | 55,56% | -1,80% | +0,22% | -5,17% | +3,41% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 20 | 75,00% | -1,06% | +0,82% | -5,42% | +3,17% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 23 | 78,26% | -1,32% | +1,11% | -5,22% | +3,27% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 18 | 50,00% | -0,81% | -0,62% | -5,08% | +3,39% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 24 | 45,83% | -1,44% | +0,59% | -5,29% | +3,28% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 16 | 50,00% | -0,70% | +0,70% | -5,23% | +3,76% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 14 | 57,14% | -2,85% | -0,16% | -7,27% | +2,80% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 13 | 69,23% | -2,76% | +1,54% | -7,29% | +2,50% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 16 | 75,00% | -2,76% | +1,77% | -7,06% | +2,77% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 11 | 27,27% | -2,77% | -1,23% | -7,01% | +2,73% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 17 | 64,71% | -2,55% | +0,13% | -7,06% | +2,81% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 9 | 77,78% | -0,96% | +0,96% | -6,82% | +3,24% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 7 | 42,86% | -1,44% | -1,09% | -7,86% | +2,87% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 6 | 83,33% | -2,07% | +1,15% | -8,21% | +2,50% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 8 | 75,00% | -1,54% | +0,85% | -8,00% | +2,71% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | -1,55% | -0,85% | -8,00% | +2,76% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 8 | 37,50% | -1,54% | -0,79% | -8,00% | +2,71% | FEEDBACK RAPIDO |
| SOL | 30g | Classic technical | CALIBRABILE | 1 | 100,00% | -0,79% | +0,79% | -6,98% | +3,59% | FEEDBACK RAPIDO |
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
