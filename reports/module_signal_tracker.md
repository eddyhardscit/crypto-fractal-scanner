# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-18 05:32 UTC

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

Segnali totali salvati: **117**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-18 | BTC | 64.145,05 | 0 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-18 | DOGE | 0.06969 | +3 | +4 | +3 | +2 | 0 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-18 | SOL | 75,65 | +1 | +3 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-17 | BTC | 63.428,86 | +1 | +4 | +3 | +1 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-17 | DOGE | 0.07007 | +2 | +4 | +3 | +2 | -1 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-17 | SOL | 75,40 | +1 | +3 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-16 | BTC | 63.005,56 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-16 | DOGE | 0.06966 | +4 | +4 | +3 | +2 | +1 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-16 | SOL | 75,33 | +1 | +3 | +3 | +3 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-15 | BTC | 63.058,07 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-15 | DOGE | 0.07017 | +4 | +4 | +3 | +2 | +1 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-15 | SOL | 75,40 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 39 | 38 | 37 | 36 | 34 | 34 | 31 | 27 | 20 | 11 | 0 | 0 |
| SOL | 39 | 38 | 37 | 36 | 34 | 34 | 31 | 27 | 20 | 11 | 0 | 0 |
| DOGE | 39 | 38 | 37 | 36 | 34 | 34 | 31 | 27 | 20 | 11 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-20 | 30g | 2026-08-19 | domani |
| SOL | 2026-07-20 | 30g | 2026-08-19 | domani |
| DOGE | 2026-07-20 | 30g | 2026-08-19 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 36 | 50,00% | +0,05% | +0,02% | PRIMA CALIBRAZIONE |
| BTC | 2g | 35 | 48,57% | +0,10% | -0,03% | PRIMA CALIBRAZIONE |
| BTC | 3g | 34 | 41,18% | -0,05% | -0,26% | PRIMA CALIBRAZIONE |
| BTC | 5g | 32 | 28,12% | -0,09% | -0,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | 32 | 40,62% | -0,02% | -0,35% | PRIMA CALIBRAZIONE |
| BTC | 10g | 29 | 41,38% | +0,21% | -0,10% | FEEDBACK RAPIDO |
| BTC | 14g | 25 | 44,00% | +0,02% | -0,12% | FEEDBACK RAPIDO |
| BTC | 21g | 18 | 22,22% | -0,60% | -0,97% | FEEDBACK RAPIDO |
| BTC | 30g | 10 | 80,00% | +0,18% | +0,69% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 31 | 51,61% | +0,02% | -0,18% | PRIMA CALIBRAZIONE |
| SOL | 2g | 30 | 43,33% | +0,00% | -0,23% | PRIMA CALIBRAZIONE |
| SOL | 3g | 29 | 44,83% | +0,10% | -0,21% | FEEDBACK RAPIDO |
| SOL | 5g | 27 | 48,15% | -0,10% | -0,30% | FEEDBACK RAPIDO |
| SOL | 7g | 27 | 55,56% | -0,05% | +0,15% | FEEDBACK RAPIDO |
| SOL | 10g | 24 | 54,17% | -0,06% | +0,26% | FEEDBACK RAPIDO |
| SOL | 14g | 20 | 60,00% | -1,32% | +0,49% | FEEDBACK RAPIDO |
| SOL | 21g | 15 | 60,00% | -2,44% | +0,07% | FEEDBACK RAPIDO |
| SOL | 30g | 10 | 40,00% | -0,97% | -0,80% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 36 | 41,67% | -0,03% | -0,05% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 35 | 45,71% | -0,12% | -0,13% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 34 | 41,18% | -0,33% | +0,01% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 32 | 50,00% | -0,59% | +0,19% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 32 | 59,38% | -0,84% | +0,54% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 29 | 51,72% | -1,34% | +0,80% | FEEDBACK RAPIDO |
| DOGE | 14g | 26 | 57,69% | -2,06% | +1,51% | FEEDBACK RAPIDO |
| DOGE | 21g | 19 | 78,95% | -3,35% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 30g | 11 | 100,00% | -4,16% | +4,16% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 36 | 50,00% | +0,05% | +0,02% | -0,27% | +0,58% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 38 | 52,63% | +0,04% | +0,04% | -0,28% | +0,54% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 38 | 52,63% | +0,04% | +0,04% | -0,28% | +0,54% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 52,94% | +0,01% | +0,01% | -0,32% | +0,47% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 33 | 33,33% | +0,19% | -0,42% | -0,15% | +0,69% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 8 | 12,50% | +0,66% | -0,66% | +0,09% | +0,94% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 35 | 48,57% | +0,10% | -0,03% | -0,38% | +0,78% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 37 | 51,35% | +0,07% | +0,07% | -0,39% | +0,75% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 37 | 51,35% | +0,07% | +0,07% | -0,39% | +0,75% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 33 | 51,52% | -0,00% | -0,00% | -0,48% | +0,66% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 32 | 40,62% | +0,25% | -0,43% | -0,20% | +0,92% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 7 | 14,29% | +0,89% | -0,89% | +0,49% | +1,50% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 34 | 41,18% | -0,05% | -0,26% | -1,34% | +1,58% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 36 | 52,78% | +0,02% | +0,02% | -1,31% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 36 | 52,78% | +0,02% | +0,02% | -1,31% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 32 | 53,12% | +0,00% | +0,00% | -1,33% | +1,48% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 31 | 32,26% | +0,34% | -0,52% | -1,08% | +1,83% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 6 | 16,67% | +1,26% | -1,26% | -0,39% | +2,22% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 32 | 28,12% | -0,09% | -0,49% | -2,11% | +2,04% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 34 | 38,24% | -0,08% | -0,08% | -2,07% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 34 | 38,24% | -0,08% | -0,08% | -2,07% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 30 | 40,00% | -0,01% | -0,01% | -2,06% | +2,03% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 29 | 37,93% | +0,10% | -0,74% | -1,83% | +2,30% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,14% | -1,14% | -1,16% | +2,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 32 | 40,62% | -0,02% | -0,35% | -2,37% | +2,35% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 34 | 50,00% | -0,05% | -0,05% | -2,35% | +2,37% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 34 | 50,00% | -0,05% | -0,05% | -2,35% | +2,37% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 30 | 53,33% | +0,12% | +0,12% | -2,33% | +2,37% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 29 | 34,48% | +0,33% | -0,86% | -2,10% | +2,59% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,94% | -1,94% | -1,23% | +3,13% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 29 | 41,38% | +0,21% | -0,10% | -2,61% | +2,84% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 31 | 48,39% | +0,05% | +0,05% | -2,64% | +2,83% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 31 | 48,39% | +0,05% | +0,05% | -2,64% | +2,83% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 27 | 55,56% | +0,36% | +0,36% | -2,52% | +2,89% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 26 | 30,77% | +0,28% | -0,37% | -2,34% | +3,14% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,32% | -1,32% | -1,42% | +3,31% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 25 | 44,00% | +0,02% | -0,12% | -2,80% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 27 | 44,44% | -0,10% | -0,10% | -2,83% | +3,32% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 27 | 44,44% | -0,10% | -0,10% | -2,83% | +3,32% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 23 | 52,17% | +0,32% | +0,32% | -2,56% | +3,48% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 22 | 59,09% | +0,17% | +0,10% | -2,46% | +3,69% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 18 | 22,22% | -0,60% | -0,97% | -3,23% | +3,58% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 20 | 40,00% | -0,65% | -0,65% | -3,27% | +3,49% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 20 | 40,00% | -0,65% | -0,65% | -3,27% | +3,49% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 16 | 43,75% | -0,47% | -0,47% | -2,96% | +3,77% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 16 | 25,00% | -0,26% | -0,16% | -2,90% | +3,94% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 1 | 0,00% | +1,21% | -1,21% | -1,82% | +3,19% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 10 | 80,00% | +0,18% | +0,69% | -2,63% | +5,02% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 11 | 54,55% | +0,10% | +0,10% | -2,62% | +4,99% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 11 | 54,55% | +0,10% | +0,10% | -2,62% | +4,99% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +0,21% | +0,21% | -2,50% | +5,16% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 10 | 50,00% | -0,02% | -0,49% | -2,56% | +5,01% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 36 | 41,67% | -0,03% | -0,05% | -0,50% | +0,67% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 38 | 52,63% | -0,14% | +0,18% | -0,61% | +0,55% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 38 | 52,63% | -0,14% | +0,18% | -0,61% | +0,55% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 36 | 52,78% | -0,04% | +0,08% | -0,53% | +0,67% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 33 | 51,52% | -0,13% | +0,13% | -0,60% | +0,48% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 25 | 40,00% | +0,20% | -0,20% | -0,31% | +0,75% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,92% | +1,13% | +0,84% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 35 | 45,71% | -0,12% | -0,13% | -0,75% | +0,92% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 37 | 48,65% | -0,23% | +0,02% | -0,86% | +0,78% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 37 | 48,65% | -0,23% | +0,02% | -0,86% | +0,78% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | -0,32% | +0,09% | -0,90% | +0,75% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 32 | 59,38% | -0,29% | +0,28% | -0,89% | +0,60% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 24 | 45,83% | +0,18% | -0,18% | -0,45% | +1,20% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +3,12% | +2,46% | +2,21% | +3,52% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 34 | 41,18% | -0,33% | +0,01% | -1,77% | +1,95% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 36 | 47,22% | -0,42% | -0,07% | -1,86% | +1,80% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 36 | 47,22% | -0,42% | -0,07% | -1,86% | +1,80% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | -0,66% | +0,13% | -1,82% | +1,67% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 31 | 48,39% | -0,50% | +0,45% | -1,99% | +1,63% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 23 | 39,13% | -0,05% | +0,05% | -1,78% | +2,33% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,70% | +1,18% | -0,25% | +5,07% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 32 | 50,00% | -0,59% | +0,19% | -2,65% | +2,44% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | -0,68% | +0,08% | -2,71% | +2,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,68% | +0,08% | -2,71% | +2,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 32 | 46,88% | -0,69% | +0,05% | -2,71% | +2,16% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 30 | 63,33% | -0,75% | +0,75% | -2,89% | +2,13% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 22 | 54,55% | -0,40% | +0,40% | -2,68% | +2,79% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 32 | 59,38% | -0,84% | +0,54% | -3,04% | +2,67% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 34 | 55,88% | -0,93% | +0,33% | -3,12% | +2,57% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 34 | 55,88% | -0,93% | +0,33% | -3,12% | +2,57% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | -0,92% | +0,28% | -3,15% | +2,45% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 30 | 63,33% | -1,05% | +1,05% | -3,36% | +2,36% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 22 | 54,55% | -0,91% | +0,91% | -3,18% | +2,88% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,63% | +0,36% | -0,50% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 29 | 51,72% | -1,34% | +0,80% | -3,76% | +2,79% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 31 | 51,61% | -1,37% | +0,67% | -3,80% | +2,68% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 31 | 51,61% | -1,37% | +0,67% | -3,80% | +2,68% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 29 | 51,72% | -1,41% | +0,65% | -3,82% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 30 | 66,67% | -1,40% | +1,40% | -3,88% | +2,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 21 | 61,90% | -1,18% | +1,18% | -3,82% | +2,85% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,23% | +0,22% | -1,27% | +6,23% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 26 | 57,69% | -2,06% | +1,51% | -4,70% | +2,96% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 27 | 62,96% | -2,14% | +1,33% | -4,77% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 27 | 62,96% | -2,14% | +1,33% | -4,77% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 25 | 64,00% | -2,19% | +1,31% | -4,86% | +2,63% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 27 | 74,07% | -2,14% | +2,14% | -4,77% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 20 | 70,00% | -2,09% | +2,09% | -4,80% | +3,07% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 19 | 78,95% | -3,35% | +2,77% | -5,86% | +2,70% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 20 | 80,00% | -3,38% | +2,54% | -5,90% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 20 | 80,00% | -3,38% | +2,54% | -5,90% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 18 | 83,33% | -3,61% | +2,68% | -6,14% | +2,34% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 20 | 90,00% | -3,38% | +3,38% | -5,90% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 17 | 88,24% | -3,12% | +3,12% | -5,64% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 11 | 100,00% | -4,16% | +4,16% | -6,73% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 11 | 100,00% | -4,16% | +4,16% | -6,73% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 11 | 100,00% | -4,16% | +4,16% | -6,73% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 11 | 100,00% | -4,16% | +4,16% | -6,73% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 11 | 100,00% | -4,16% | +4,16% | -6,73% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 10 | 100,00% | -3,96% | +3,96% | -6,60% | +2,65% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 31 | 51,61% | +0,02% | -0,18% | -0,48% | +0,68% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 34 | 58,82% | -0,25% | +0,01% | -0,71% | +0,37% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 37 | 56,76% | -0,14% | -0,08% | -0,62% | +0,49% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 32 | 53,12% | -0,09% | +0,04% | -0,66% | +0,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 36 | 50,00% | -0,08% | -0,02% | -0,58% | +0,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,04% | -0,04% | -0,54% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 30 | 43,33% | +0,00% | -0,23% | -0,67% | +0,86% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 33 | 48,48% | -0,23% | -0,09% | -0,94% | +0,50% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 36 | 47,22% | -0,18% | -0,11% | -0,87% | +0,69% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 31 | 45,16% | -0,16% | -0,13% | -0,87% | +0,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 35 | 40,00% | -0,13% | -0,20% | -0,79% | +0,75% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,02% | -0,02% | -0,52% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 29 | 44,83% | +0,10% | -0,21% | -1,83% | +1,90% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 32 | 43,75% | -0,30% | -0,06% | -2,14% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 35 | 42,86% | -0,25% | -0,08% | -2,06% | +1,75% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 30 | 43,33% | -0,19% | -0,26% | -1,98% | +1,77% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 34 | 44,12% | -0,18% | -0,17% | -2,01% | +1,82% | PRIMA CALIBRAZIONE |
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
| SOL | 7g | Global confluence | BENCHMARK | 27 | 55,56% | -0,05% | +0,15% | -3,04% | +2,97% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 30 | 60,00% | -0,40% | +0,37% | -3,32% | +2,72% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 33 | 60,61% | -0,37% | +0,35% | -3,26% | +2,83% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 28 | 53,57% | -0,15% | -0,08% | -3,18% | +2,83% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 32 | 37,50% | -0,34% | -0,30% | -3,35% | +2,93% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 24 | 54,17% | -0,06% | +0,26% | -3,55% | +3,66% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 27 | 59,26% | -0,18% | +0,63% | -3,92% | +3,31% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 30 | 56,67% | -0,18% | +0,58% | -3,88% | +3,37% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 25 | 52,00% | +0,23% | +0,01% | -3,76% | +3,48% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 31 | 48,39% | -0,28% | +0,13% | -3,90% | +3,38% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,08% | +0,08% | -3,74% | +3,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 20 | 60,00% | -1,32% | +0,49% | -4,80% | +3,68% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 23 | 78,26% | -0,54% | +1,09% | -4,92% | +3,52% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 26 | 80,77% | -0,84% | +1,32% | -4,80% | +3,56% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 21 | 57,14% | -0,28% | -0,12% | -4,58% | +3,73% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 27 | 40,74% | -0,96% | +0,21% | -4,88% | +3,57% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 19 | 42,11% | -0,13% | +0,13% | -4,66% | +4,08% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 15 | 60,00% | -2,44% | +0,07% | -7,02% | +3,01% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 16 | 68,75% | -2,10% | +1,39% | -6,97% | +2,71% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 19 | 73,68% | -2,20% | +1,60% | -6,83% | +2,90% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 14 | 35,71% | -2,02% | -0,80% | -6,71% | +2,92% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 20 | 60,00% | -2,06% | -0,00% | -6,84% | +2,94% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 12 | 66,67% | -0,54% | +0,54% | -6,52% | +3,34% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 10 | 40,00% | -0,97% | -0,80% | -7,36% | +3,35% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 8 | 75,00% | -1,58% | +0,89% | -7,77% | +2,92% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 11 | 63,64% | -1,09% | +0,58% | -7,51% | +3,19% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -1,24% | -0,64% | -7,67% | +3,09% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 11 | 36,36% | -1,09% | -0,61% | -7,51% | +3,19% | FEEDBACK RAPIDO |
| SOL | 30g | Classic technical | CALIBRABILE | 4 | 50,00% | -0,10% | +0,10% | -6,39% | +4,25% | FEEDBACK RAPIDO |
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
