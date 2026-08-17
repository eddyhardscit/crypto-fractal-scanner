# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-17 05:32 UTC

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

Segnali totali salvati: **114**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-17 | BTC | 63.428,86 | +1 | +4 | +3 | +1 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-17 | DOGE | 0.07007 | +2 | +4 | +3 | +2 | -1 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-17 | SOL | 75,40 | +1 | +3 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-16 | BTC | 63.005,56 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-16 | DOGE | 0.06966 | +4 | +4 | +3 | +2 | +1 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-16 | SOL | 75,33 | +1 | +3 | +3 | +3 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-15 | BTC | 63.058,07 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-15 | DOGE | 0.07017 | +4 | +4 | +3 | +2 | +1 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-15 | SOL | 75,40 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-14 | BTC | 62.749,25 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-14 | DOGE | 0.06940 | +2 | +4 | +3 | +2 | 0 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-14 | SOL | 75,41 | +3 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 38 | 37 | 36 | 35 | 34 | 33 | 30 | 26 | 19 | 10 | 0 | 0 |
| SOL | 38 | 37 | 36 | 35 | 34 | 33 | 30 | 26 | 19 | 10 | 0 | 0 |
| DOGE | 38 | 37 | 36 | 35 | 34 | 33 | 30 | 26 | 19 | 10 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-19 | 30g | 2026-08-18 | domani |
| SOL | 2026-07-19 | 30g | 2026-08-18 | domani |
| DOGE | 2026-07-19 | 30g | 2026-08-18 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 35 | 48,57% | +0,02% | -0,01% | PRIMA CALIBRAZIONE |
| BTC | 2g | 34 | 47,06% | +0,05% | -0,09% | PRIMA CALIBRAZIONE |
| BTC | 3g | 33 | 39,39% | -0,10% | -0,32% | PRIMA CALIBRAZIONE |
| BTC | 5g | 32 | 28,12% | -0,09% | -0,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | 31 | 38,71% | -0,03% | -0,38% | PRIMA CALIBRAZIONE |
| BTC | 10g | 28 | 42,86% | +0,26% | -0,06% | FEEDBACK RAPIDO |
| BTC | 14g | 24 | 41,67% | -0,01% | -0,15% | FEEDBACK RAPIDO |
| BTC | 21g | 17 | 23,53% | -0,71% | -0,96% | FEEDBACK RAPIDO |
| BTC | 30g | 9 | 88,89% | +0,31% | +0,87% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 30 | 50,00% | +0,01% | -0,20% | PRIMA CALIBRAZIONE |
| SOL | 2g | 29 | 41,38% | -0,01% | -0,26% | FEEDBACK RAPIDO |
| SOL | 3g | 28 | 42,86% | +0,09% | -0,23% | FEEDBACK RAPIDO |
| SOL | 5g | 27 | 48,15% | -0,10% | -0,30% | FEEDBACK RAPIDO |
| SOL | 7g | 26 | 57,69% | -0,04% | +0,16% | FEEDBACK RAPIDO |
| SOL | 10g | 23 | 52,17% | -0,13% | +0,21% | FEEDBACK RAPIDO |
| SOL | 14g | 20 | 60,00% | -1,32% | +0,49% | FEEDBACK RAPIDO |
| SOL | 21g | 14 | 57,14% | -2,85% | -0,16% | FEEDBACK RAPIDO |
| SOL | 30g | 9 | 33,33% | -1,02% | -0,95% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 35 | 42,86% | -0,02% | -0,04% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 34 | 44,12% | -0,13% | -0,13% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 33 | 42,42% | -0,31% | +0,03% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 32 | 50,00% | -0,59% | +0,19% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 31 | 61,29% | -0,86% | +0,57% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 28 | 53,57% | -1,37% | +0,85% | FEEDBACK RAPIDO |
| DOGE | 14g | 25 | 60,00% | -2,12% | +1,60% | FEEDBACK RAPIDO |
| DOGE | 21g | 18 | 83,33% | -3,52% | +2,95% | FEEDBACK RAPIDO |
| DOGE | 30g | 10 | 100,00% | -4,20% | +4,20% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 35 | 48,57% | +0,02% | -0,01% | -0,30% | +0,54% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 37 | 51,35% | +0,01% | +0,01% | -0,31% | +0,51% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 37 | 51,35% | +0,01% | +0,01% | -0,31% | +0,51% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 33 | 51,52% | -0,02% | -0,02% | -0,36% | +0,43% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 32 | 34,38% | +0,16% | -0,40% | -0,18% | +0,66% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 7 | 14,29% | +0,59% | -0,59% | -0,03% | +0,84% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 34 | 47,06% | +0,05% | -0,09% | -0,44% | +0,73% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 36 | 50,00% | +0,03% | +0,03% | -0,45% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 36 | 50,00% | +0,03% | +0,03% | -0,45% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 32 | 50,00% | -0,06% | -0,06% | -0,54% | +0,61% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 31 | 41,94% | +0,20% | -0,39% | -0,26% | +0,87% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 6 | 16,67% | +0,74% | -0,74% | +0,30% | +1,36% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 33 | 39,39% | -0,10% | -0,32% | -1,36% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 35 | 51,43% | -0,03% | -0,03% | -1,33% | +1,55% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 35 | 51,43% | -0,03% | -0,03% | -1,33% | +1,55% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 31 | 51,61% | -0,05% | -0,05% | -1,35% | +1,46% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 30 | 33,33% | +0,30% | -0,48% | -1,09% | +1,81% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 5 | 20,00% | +1,16% | -1,16% | -0,33% | +2,21% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 32 | 28,12% | -0,09% | -0,49% | -2,11% | +2,04% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 34 | 38,24% | -0,08% | -0,08% | -2,07% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 34 | 38,24% | -0,08% | -0,08% | -2,07% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 30 | 40,00% | -0,01% | -0,01% | -2,06% | +2,03% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 29 | 37,93% | +0,10% | -0,74% | -1,83% | +2,30% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,14% | -1,14% | -1,16% | +2,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 31 | 38,71% | -0,03% | -0,38% | -2,37% | +2,40% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 33 | 48,48% | -0,06% | -0,06% | -2,36% | +2,41% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 33 | 48,48% | -0,06% | -0,06% | -2,36% | +2,41% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 29 | 51,72% | +0,11% | +0,11% | -2,33% | +2,42% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 28 | 32,14% | +0,33% | -0,90% | -2,10% | +2,65% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,94% | -1,94% | -1,23% | +3,13% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 28 | 42,86% | +0,26% | -0,06% | -2,57% | +2,92% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 30 | 50,00% | +0,09% | +0,09% | -2,60% | +2,90% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 30 | 50,00% | +0,09% | +0,09% | -2,60% | +2,90% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 26 | 57,69% | +0,42% | +0,42% | -2,47% | +2,98% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 25 | 32,00% | +0,34% | -0,33% | -2,28% | +3,24% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,32% | -1,32% | -1,42% | +3,31% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 24 | 41,67% | -0,01% | -0,15% | -2,83% | +3,41% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 26 | 42,31% | -0,12% | -0,12% | -2,86% | +3,35% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 26 | 42,31% | -0,12% | -0,12% | -2,86% | +3,35% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 22 | 50,00% | +0,31% | +0,31% | -2,58% | +3,53% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 21 | 57,14% | +0,15% | +0,08% | -2,48% | +3,75% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 17 | 23,53% | -0,71% | -0,96% | -3,31% | +3,61% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 19 | 36,84% | -0,75% | -0,75% | -3,35% | +3,50% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 19 | 36,84% | -0,75% | -0,75% | -3,35% | +3,50% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 15 | 40,00% | -0,58% | -0,58% | -3,04% | +3,81% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 15 | 26,67% | -0,36% | -0,09% | -2,97% | +3,98% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 9 | 88,89% | +0,31% | +0,87% | -2,48% | +5,20% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 10 | 60,00% | +0,21% | +0,21% | -2,50% | +5,16% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 10 | 60,00% | +0,21% | +0,21% | -2,50% | +5,16% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +0,21% | +0,21% | -2,50% | +5,16% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 9 | 55,56% | +0,08% | -0,44% | -2,41% | +5,20% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 35 | 42,86% | -0,02% | -0,04% | -0,49% | +0,68% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 37 | 54,05% | -0,13% | +0,20% | -0,61% | +0,56% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 37 | 54,05% | -0,13% | +0,20% | -0,61% | +0,56% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | -0,02% | +0,10% | -0,52% | +0,68% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 32 | 50,00% | -0,12% | +0,11% | -0,60% | +0,48% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,23% | -0,23% | -0,30% | +0,77% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,92% | +1,13% | +0,84% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 34 | 44,12% | -0,13% | -0,13% | -0,77% | +0,92% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 36 | 47,22% | -0,24% | +0,02% | -0,88% | +0,77% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 36 | 47,22% | -0,24% | +0,02% | -0,88% | +0,77% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 47,06% | -0,33% | +0,10% | -0,93% | +0,74% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 31 | 58,06% | -0,30% | +0,29% | -0,91% | +0,59% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 23 | 47,83% | +0,18% | -0,18% | -0,46% | +1,21% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +3,12% | +2,46% | +2,21% | +3,52% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 33 | 42,42% | -0,31% | +0,03% | -1,78% | +2,01% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 35 | 48,57% | -0,42% | -0,06% | -1,88% | +1,84% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 35 | 48,57% | -0,42% | -0,06% | -1,88% | +1,84% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 33 | 51,52% | -0,66% | +0,16% | -1,84% | +1,72% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,49% | +0,49% | -2,02% | +1,67% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 23 | 39,13% | -0,05% | +0,05% | -1,78% | +2,33% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,70% | +1,18% | -0,25% | +5,07% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 32 | 50,00% | -0,59% | +0,19% | -2,65% | +2,44% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | -0,68% | +0,08% | -2,71% | +2,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,68% | +0,08% | -2,71% | +2,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 32 | 46,88% | -0,69% | +0,05% | -2,71% | +2,16% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 30 | 63,33% | -0,75% | +0,75% | -2,89% | +2,13% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 22 | 54,55% | -0,40% | +0,40% | -2,68% | +2,79% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 31 | 61,29% | -0,86% | +0,57% | -3,09% | +2,63% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 33 | 57,58% | -0,95% | +0,35% | -3,18% | +2,54% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 33 | 57,58% | -0,95% | +0,35% | -3,18% | +2,54% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 31 | 58,06% | -0,94% | +0,30% | -3,21% | +2,41% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 30 | 63,33% | -1,05% | +1,05% | -3,36% | +2,36% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 22 | 54,55% | -0,91% | +0,91% | -3,18% | +2,88% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,63% | +0,36% | -0,50% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 28 | 53,57% | -1,37% | +0,85% | -3,83% | +2,75% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 30 | 53,33% | -1,40% | +0,71% | -3,88% | +2,64% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 30 | 53,33% | -1,40% | +0,71% | -3,88% | +2,64% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 28 | 53,57% | -1,44% | +0,70% | -3,90% | +2,50% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 29 | 65,52% | -1,43% | +1,43% | -3,95% | +2,59% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 21 | 61,90% | -1,18% | +1,18% | -3,82% | +2,85% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,23% | +0,22% | -1,27% | +6,23% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 25 | 60,00% | -2,12% | +1,60% | -4,78% | +2,92% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 26 | 65,38% | -2,20% | +1,40% | -4,86% | +2,73% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 26 | 65,38% | -2,20% | +1,40% | -4,86% | +2,73% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 24 | 66,67% | -2,25% | +1,39% | -4,95% | +2,58% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 26 | 73,08% | -2,20% | +2,20% | -4,86% | +2,73% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 20 | 70,00% | -2,09% | +2,09% | -4,80% | +3,07% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 18 | 83,33% | -3,52% | +2,95% | -6,03% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 19 | 84,21% | -3,54% | +2,69% | -6,07% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 19 | 84,21% | -3,54% | +2,69% | -6,07% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 17 | 88,24% | -3,81% | +2,86% | -6,34% | +2,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 19 | 89,47% | -3,54% | +3,54% | -6,07% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 16 | 87,50% | -3,30% | +3,30% | -5,81% | +2,92% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 10 | 100,00% | -4,20% | +4,20% | -6,79% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 10 | 100,00% | -4,20% | +4,20% | -6,79% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 10 | 100,00% | -4,20% | +4,20% | -6,79% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 10 | 100,00% | -4,20% | +4,20% | -6,79% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 10 | 100,00% | -4,20% | +4,20% | -6,79% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 9 | 100,00% | -3,98% | +3,98% | -6,65% | +2,73% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 30 | 50,00% | +0,01% | -0,20% | -0,49% | +0,67% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 33 | 57,58% | -0,26% | -0,00% | -0,72% | +0,36% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 36 | 55,56% | -0,15% | -0,09% | -0,63% | +0,49% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 31 | 51,61% | -0,10% | +0,03% | -0,67% | +0,50% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 35 | 51,43% | -0,09% | -0,01% | -0,59% | +0,50% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,04% | -0,04% | -0,54% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 29 | 41,38% | -0,01% | -0,26% | -0,68% | +0,86% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 32 | 46,88% | -0,25% | -0,11% | -0,97% | +0,49% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 35 | 45,71% | -0,20% | -0,13% | -0,89% | +0,68% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 30 | 43,33% | -0,18% | -0,15% | -0,89% | +0,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 34 | 41,18% | -0,15% | -0,19% | -0,81% | +0,74% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,02% | -0,02% | -0,52% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 28 | 42,86% | +0,09% | -0,23% | -1,84% | +1,94% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 31 | 41,94% | -0,32% | -0,07% | -2,16% | +1,63% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 34 | 41,18% | -0,26% | -0,09% | -2,07% | +1,78% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 29 | 41,38% | -0,21% | -0,28% | -2,00% | +1,80% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 33 | 45,45% | -0,20% | -0,16% | -2,02% | +1,85% | PRIMA CALIBRAZIONE |
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
| SOL | 7g | Global confluence | BENCHMARK | 26 | 57,69% | -0,04% | +0,16% | -3,08% | +3,02% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 29 | 62,07% | -0,41% | +0,39% | -3,36% | +2,76% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 32 | 62,50% | -0,38% | +0,36% | -3,30% | +2,87% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 27 | 55,56% | -0,16% | -0,08% | -3,23% | +2,87% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 32 | 37,50% | -0,34% | -0,30% | -3,35% | +2,93% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 23 | 52,17% | -0,13% | +0,21% | -3,69% | +3,64% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 26 | 57,69% | -0,24% | +0,59% | -4,06% | +3,28% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 29 | 55,17% | -0,24% | +0,55% | -3,99% | +3,35% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 24 | 50,00% | +0,17% | -0,06% | -3,90% | +3,45% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,34% | +0,18% | -4,02% | +3,35% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,08% | +0,08% | -3,74% | +3,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 20 | 60,00% | -1,32% | +0,49% | -4,80% | +3,68% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 22 | 77,27% | -0,69% | +1,01% | -5,06% | +3,44% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 25 | 80,00% | -0,98% | +1,26% | -4,92% | +3,49% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 20 | 55,00% | -0,43% | -0,25% | -4,72% | +3,65% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 26 | 42,31% | -1,10% | +0,32% | -5,00% | +3,50% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 18 | 44,44% | -0,29% | +0,29% | -4,81% | +4,01% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 14 | 57,14% | -2,85% | -0,16% | -7,27% | +2,80% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 15 | 66,67% | -2,46% | +1,27% | -7,21% | +2,50% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 18 | 72,22% | -2,51% | +1,51% | -7,02% | +2,73% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 13 | 30,77% | -2,42% | -1,12% | -6,96% | +2,69% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 19 | 63,16% | -2,34% | +0,17% | -7,02% | +2,78% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 11 | 72,73% | -0,88% | +0,88% | -6,79% | +3,10% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 9 | 33,33% | -1,02% | -0,95% | -7,39% | +3,33% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 7 | 71,43% | -1,73% | +0,94% | -7,87% | +2,83% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 10 | 60,00% | -1,14% | +0,59% | -7,56% | +3,15% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -1,24% | -0,64% | -7,67% | +3,09% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 10 | 30,00% | -1,14% | -0,73% | -7,56% | +3,15% | FEEDBACK RAPIDO |
| SOL | 30g | Classic technical | CALIBRABILE | 3 | 33,33% | +0,04% | -0,04% | -6,17% | +4,49% | FEEDBACK RAPIDO |
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
