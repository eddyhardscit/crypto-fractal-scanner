# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-14 11:04 UTC

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

Segnali totali salvati: **105**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-14 | BTC | 62.749,25 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-14 | DOGE | 0.06940 | +2 | +4 | +3 | +2 | 0 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-14 | SOL | 75,41 | +3 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-11 | BTC | 63.889,59 | +6 | +4 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-11 | DOGE | 0.06985 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-11 | SOL | 75,73 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-10 | BTC | 64.966,07 | +6 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-10 | DOGE | 0.06975 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-10 | SOL | 76,57 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-09 | BTC | 64.733,97 | +7 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-09 | DOGE | 0.06994 | +4 | +4 | +3 | +3 | 0 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-09 | SOL | 75,92 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 35 | 34 | 34 | 34 | 32 | 30 | 27 | 23 | 16 | 7 | 0 | 0 |
| SOL | 35 | 34 | 34 | 34 | 32 | 30 | 27 | 23 | 16 | 7 | 0 | 0 |
| DOGE | 35 | 34 | 34 | 34 | 32 | 30 | 27 | 23 | 16 | 7 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-16 | 30g | 2026-08-15 | domani |
| SOL | 2026-07-16 | 30g | 2026-08-15 | domani |
| DOGE | 2026-07-16 | 30g | 2026-08-15 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 32 | 46,88% | -0,01% | -0,05% | PRIMA CALIBRAZIONE |
| BTC | 2g | 32 | 43,75% | +0,02% | -0,12% | PRIMA CALIBRAZIONE |
| BTC | 3g | 32 | 37,50% | -0,14% | -0,36% | PRIMA CALIBRAZIONE |
| BTC | 5g | 30 | 30,00% | +0,05% | -0,38% | PRIMA CALIBRAZIONE |
| BTC | 7g | 28 | 42,86% | +0,25% | -0,13% | FEEDBACK RAPIDO |
| BTC | 10g | 25 | 48,00% | +0,53% | +0,17% | FEEDBACK RAPIDO |
| BTC | 14g | 21 | 42,86% | -0,03% | -0,19% | FEEDBACK RAPIDO |
| BTC | 21g | 14 | 28,57% | -0,38% | -0,68% | FEEDBACK RAPIDO |
| BTC | 30g | 7 | 85,71% | +0,76% | +0,76% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 27 | 51,85% | +0,01% | -0,22% | FEEDBACK RAPIDO |
| SOL | 2g | 27 | 44,44% | -0,01% | -0,27% | FEEDBACK RAPIDO |
| SOL | 3g | 27 | 44,44% | +0,09% | -0,24% | FEEDBACK RAPIDO |
| SOL | 5g | 25 | 52,00% | -0,02% | -0,24% | FEEDBACK RAPIDO |
| SOL | 7g | 23 | 60,87% | -0,00% | +0,23% | FEEDBACK RAPIDO |
| SOL | 10g | 20 | 45,00% | -0,52% | -0,14% | FEEDBACK RAPIDO |
| SOL | 14g | 17 | 52,94% | -2,09% | +0,05% | FEEDBACK RAPIDO |
| SOL | 21g | 14 | 57,14% | -2,85% | -0,16% | FEEDBACK RAPIDO |
| SOL | 30g | 6 | 33,33% | -1,55% | -1,41% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 32 | 40,62% | -0,05% | -0,07% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 32 | 43,75% | -0,14% | -0,15% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 32 | 40,62% | -0,35% | -0,00% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 30 | 50,00% | -0,64% | +0,19% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 28 | 60,71% | -0,96% | +0,62% | FEEDBACK RAPIDO |
| DOGE | 10g | 26 | 53,85% | -1,52% | +0,88% | FEEDBACK RAPIDO |
| DOGE | 14g | 22 | 68,18% | -2,39% | +1,87% | FEEDBACK RAPIDO |
| DOGE | 21g | 16 | 93,75% | -3,70% | +3,70% | FEEDBACK RAPIDO |
| DOGE | 30g | 7 | 100,00% | -4,49% | +4,49% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 32 | 46,88% | -0,01% | -0,05% | -0,32% | +0,55% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 34 | 50,00% | -0,02% | -0,02% | -0,33% | +0,51% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 34 | 50,00% | -0,02% | -0,02% | -0,33% | +0,51% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 30 | 50,00% | -0,06% | -0,06% | -0,38% | +0,43% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 29 | 34,48% | +0,14% | -0,40% | -0,19% | +0,67% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 4 | 0,00% | +0,76% | -0,76% | +0,03% | +1,12% | FEEDBACK RAPIDO |
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
| BTC | 5g | Global confluence | BENCHMARK | 30 | 30,00% | +0,05% | -0,38% | -2,06% | +2,18% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 32 | 40,62% | +0,05% | +0,05% | -2,02% | +2,21% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 32 | 40,62% | +0,05% | +0,05% | -2,02% | +2,21% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 28 | 42,86% | +0,14% | +0,14% | -2,01% | +2,18% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 27 | 40,74% | +0,27% | -0,64% | -1,76% | +2,48% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,14% | -1,14% | -1,16% | +2,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 28 | 42,86% | +0,25% | -0,13% | -2,25% | +2,63% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 30 | 53,33% | +0,20% | +0,20% | -2,24% | +2,63% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 30 | 53,33% | +0,20% | +0,20% | -2,24% | +2,63% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 26 | 57,69% | +0,43% | +0,43% | -2,19% | +2,67% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 25 | 36,00% | +0,69% | -0,69% | -1,92% | +2,93% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,94% | -1,94% | -1,23% | +3,13% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 25 | 48,00% | +0,53% | +0,17% | -2,53% | +3,08% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 27 | 55,56% | +0,32% | +0,32% | -2,57% | +3,05% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 27 | 55,56% | +0,32% | +0,32% | -2,57% | +3,05% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 23 | 65,22% | +0,73% | +0,73% | -2,42% | +3,17% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 22 | 31,82% | +0,65% | -0,28% | -2,20% | +3,47% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,32% | -1,32% | -1,42% | +3,31% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 21 | 42,86% | -0,03% | -0,19% | -3,07% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 23 | 43,48% | -0,16% | -0,16% | -3,08% | +3,30% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 23 | 43,48% | -0,16% | -0,16% | -3,08% | +3,30% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 19 | 52,63% | +0,33% | +0,33% | -2,80% | +3,50% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 18 | 55,56% | +0,15% | +0,12% | -2,70% | +3,76% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 2 | 50,00% | +0,00% | -0,00% | -2,23% | +2,76% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 14 | 28,57% | -0,38% | -0,68% | -3,23% | +4,06% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 16 | 43,75% | -0,47% | -0,47% | -3,28% | +3,88% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 16 | 43,75% | -0,47% | -0,47% | -3,28% | +3,88% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 12 | 50,00% | -0,16% | -0,16% | -2,88% | +4,39% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 13 | 23,08% | -0,12% | -0,06% | -2,94% | +4,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 7 | 85,71% | +0,76% | +0,76% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 7 | 85,71% | +0,76% | +0,76% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 7 | 85,71% | +0,76% | +0,76% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 7 | 85,71% | +0,76% | +0,76% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 6 | 33,33% | +0,65% | -1,20% | -2,34% | +5,40% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 32 | 40,62% | -0,05% | -0,07% | -0,52% | +0,69% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 34 | 52,94% | -0,16% | +0,19% | -0,65% | +0,56% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 34 | 52,94% | -0,16% | +0,19% | -0,65% | +0,56% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 32 | 53,12% | -0,06% | +0,08% | -0,56% | +0,68% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,12% | +0,12% | -0,60% | +0,51% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 22 | 40,91% | +0,18% | -0,18% | -0,35% | +0,74% | FEEDBACK RAPIDO |
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
| DOGE | 5g | Global confluence | BENCHMARK | 30 | 50,00% | -0,64% | +0,19% | -2,74% | +2,34% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 32 | 46,88% | -0,73% | +0,07% | -2,80% | +2,19% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 32 | 46,88% | -0,73% | +0,07% | -2,80% | +2,19% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 30 | 46,67% | -0,75% | +0,04% | -2,81% | +2,03% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 30 | 63,33% | -0,75% | +0,75% | -2,89% | +2,13% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 22 | 54,55% | -0,40% | +0,40% | -2,68% | +2,79% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 28 | 60,71% | -0,96% | +0,62% | -3,27% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 30 | 56,67% | -1,05% | +0,38% | -3,35% | +2,37% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 30 | 56,67% | -1,05% | +0,38% | -3,35% | +2,37% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 28 | 57,14% | -1,05% | +0,33% | -3,40% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 29 | 65,52% | -1,09% | +1,09% | -3,41% | +2,31% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,93% | +0,93% | -3,27% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,97% | +0,62% | -0,19% | +6,23% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 26 | 53,85% | -1,52% | +0,88% | -4,06% | +2,59% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 27 | 51,85% | -1,61% | +0,74% | -4,16% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 27 | 51,85% | -1,61% | +0,74% | -4,16% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 25 | 52,00% | -1,67% | +0,73% | -4,21% | +2,25% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 27 | 70,37% | -1,61% | +1,61% | -4,16% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 20 | 65,00% | -1,32% | +1,32% | -4,00% | +2,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 22 | 68,18% | -2,39% | +1,87% | -5,10% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 23 | 65,22% | -2,47% | +1,60% | -5,18% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 23 | 65,22% | -2,47% | +1,60% | -5,18% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 21 | 66,67% | -2,56% | +1,60% | -5,31% | +2,38% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 23 | 78,26% | -2,47% | +2,47% | -5,18% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 19 | 73,68% | -2,20% | +2,20% | -4,92% | +3,02% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 16 | 93,75% | -3,70% | +3,70% | -6,18% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 16 | 93,75% | -3,70% | +3,70% | -6,18% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 16 | 93,75% | -3,70% | +3,70% | -6,18% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 14 | 100,00% | -4,05% | +4,05% | -6,53% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 16 | 93,75% | -3,70% | +3,70% | -6,18% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 15 | 93,33% | -3,58% | +3,58% | -6,05% | +2,70% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,55% | +0,55% | -1,52% | +6,93% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 7 | 100,00% | -4,49% | +4,49% | -7,01% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 7 | 100,00% | -4,49% | +4,49% | -7,01% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 7 | 100,00% | -4,49% | +4,49% | -7,01% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 7 | 100,00% | -4,49% | +4,49% | -7,01% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 7 | 100,00% | -4,49% | +4,49% | -7,01% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 6 | 100,00% | -4,21% | +4,21% | -6,84% | +3,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 27 | 51,85% | +0,01% | -0,22% | -0,48% | +0,72% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 30 | 60,00% | -0,29% | -0,00% | -0,74% | +0,37% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 33 | 57,58% | -0,16% | -0,10% | -0,64% | +0,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 28 | 53,57% | -0,12% | +0,03% | -0,68% | +0,53% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 32 | 50,00% | -0,10% | -0,02% | -0,59% | +0,53% | PRIMA CALIBRAZIONE |
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
| SOL | 5g | Global confluence | BENCHMARK | 25 | 52,00% | -0,02% | -0,24% | -2,64% | +2,73% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 28 | 53,57% | -0,28% | -0,02% | -2,95% | +2,40% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 31 | 51,61% | -0,18% | -0,09% | -2,86% | +2,54% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 26 | 50,00% | -0,37% | -0,09% | -2,82% | +2,53% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 31 | 45,16% | -0,24% | -0,29% | -2,89% | +2,61% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 21 | 52,38% | +0,14% | -0,14% | -2,60% | +2,64% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 23 | 60,87% | -0,00% | +0,23% | -3,30% | +3,14% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 26 | 65,38% | -0,41% | +0,47% | -3,59% | +2,84% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 29 | 65,52% | -0,38% | +0,43% | -3,50% | +2,95% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 24 | 58,33% | -0,13% | -0,04% | -3,45% | +2,97% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 30 | 36,67% | -0,35% | -0,33% | -3,49% | +2,97% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 20 | 45,00% | -0,52% | -0,14% | -4,08% | +3,35% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 23 | 52,17% | -0,60% | +0,34% | -4,45% | +2,99% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 26 | 50,00% | -0,55% | +0,33% | -4,34% | +3,09% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 21 | 42,86% | -0,16% | -0,42% | -4,31% | +3,15% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 27 | 55,56% | -0,66% | +0,48% | -4,35% | +3,11% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 19 | 57,89% | -0,40% | +0,40% | -4,09% | +3,44% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 17 | 52,94% | -2,09% | +0,05% | -5,37% | +3,25% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 19 | 73,68% | -1,28% | +0,69% | -5,61% | +3,02% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 22 | 77,27% | -1,53% | +1,02% | -5,38% | +3,14% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 17 | 47,06% | -1,04% | -0,83% | -5,28% | +3,22% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 23 | 47,83% | -1,64% | +0,75% | -5,45% | +3,16% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 15 | 53,33% | -0,95% | +0,95% | -5,47% | +3,60% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 14 | 57,14% | -2,85% | -0,16% | -7,27% | +2,80% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 12 | 66,67% | -3,13% | +1,53% | -7,50% | +2,32% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 15 | 73,33% | -3,05% | +1,77% | -7,22% | +2,64% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 10 | 20,00% | -3,22% | -1,52% | -7,24% | +2,54% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 16 | 68,75% | -2,81% | +0,24% | -7,21% | +2,70% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 8 | 87,50% | -1,29% | +1,29% | -7,09% | +3,06% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 6 | 33,33% | -1,55% | -1,41% | -8,00% | +2,76% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 5 | 80,00% | -2,33% | +1,22% | -8,45% | +2,28% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 7 | 71,43% | -1,65% | +0,86% | -8,15% | +2,58% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | -1,55% | -0,85% | -8,00% | +2,76% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 7 | 28,57% | -1,65% | -1,02% | -8,15% | +2,58% | FEEDBACK RAPIDO |
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
