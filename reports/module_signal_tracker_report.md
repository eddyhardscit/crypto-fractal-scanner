# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-20 05:32 UTC

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

Segnali totali salvati: **123**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-20 | BTC | 69.558,29 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-20 | DOGE | 0.07454 | +4 | +3 | +3 | 0 | +2 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-20 | SOL | 84,90 | +3 | 0 | 0 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-19 | BTC | 64.293,48 | +5 | +3 | +2 | +2 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-19 | DOGE | 0.06997 | +3 | +4 | +3 | +2 | 0 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-19 | SOL | 76,87 | +2 | +3 | +2 | +2 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-18 | BTC | 64.145,05 | 0 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-18 | DOGE | 0.06969 | +3 | +4 | +3 | +2 | 0 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-18 | SOL | 75,65 | +1 | +3 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-17 | BTC | 63.428,86 | +1 | +4 | +3 | +1 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-17 | DOGE | 0.07007 | +2 | +4 | +3 | +2 | -1 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-17 | SOL | 75,40 | +1 | +3 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 41 | 40 | 39 | 38 | 36 | 34 | 33 | 29 | 22 | 13 | 0 | 0 |
| SOL | 41 | 40 | 39 | 38 | 36 | 34 | 33 | 29 | 22 | 13 | 0 | 0 |
| DOGE | 41 | 40 | 39 | 38 | 36 | 34 | 33 | 29 | 22 | 13 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-22 | 30g | 2026-08-21 | domani |
| SOL | 2026-07-22 | 30g | 2026-08-21 | domani |
| DOGE | 2026-07-22 | 30g | 2026-08-21 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 37 | 51,35% | +0,27% | +0,24% | PRIMA CALIBRAZIONE |
| BTC | 2g | 36 | 50,00% | +0,14% | +0,01% | PRIMA CALIBRAZIONE |
| BTC | 3g | 36 | 44,44% | +0,28% | +0,08% | PRIMA CALIBRAZIONE |
| BTC | 5g | 34 | 32,35% | +0,29% | -0,08% | PRIMA CALIBRAZIONE |
| BTC | 7g | 32 | 40,62% | -0,02% | -0,35% | PRIMA CALIBRAZIONE |
| BTC | 10g | 31 | 41,94% | +0,40% | +0,11% | PRIMA CALIBRAZIONE |
| BTC | 14g | 27 | 48,15% | +0,29% | +0,16% | FEEDBACK RAPIDO |
| BTC | 21g | 20 | 30,00% | -0,07% | -0,40% | FEEDBACK RAPIDO |
| BTC | 30g | 12 | 83,33% | +0,69% | +1,11% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 33 | 54,55% | +0,38% | +0,19% | PRIMA CALIBRAZIONE |
| SOL | 2g | 32 | 46,88% | +0,44% | +0,22% | PRIMA CALIBRAZIONE |
| SOL | 3g | 31 | 48,39% | +0,56% | +0,28% | PRIMA CALIBRAZIONE |
| SOL | 5g | 29 | 51,72% | +0,41% | +0,22% | FEEDBACK RAPIDO |
| SOL | 7g | 27 | 55,56% | -0,05% | +0,15% | FEEDBACK RAPIDO |
| SOL | 10g | 26 | 57,69% | +0,41% | +0,71% | FEEDBACK RAPIDO |
| SOL | 14g | 22 | 63,64% | -0,36% | +1,29% | FEEDBACK RAPIDO |
| SOL | 21g | 16 | 56,25% | -1,32% | -0,91% | FEEDBACK RAPIDO |
| SOL | 30g | 12 | 41,67% | +0,00% | -0,05% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 38 | 44,74% | +0,15% | +0,14% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 37 | 45,95% | +0,07% | +0,06% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 36 | 44,44% | -0,12% | +0,20% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 34 | 52,94% | -0,35% | +0,39% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 32 | 59,38% | -0,84% | +0,54% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 31 | 54,84% | -1,03% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 27 | 59,26% | -1,74% | +1,70% | FEEDBACK RAPIDO |
| DOGE | 21g | 21 | 76,19% | -2,74% | +2,80% | FEEDBACK RAPIDO |
| DOGE | 30g | 13 | 92,31% | -3,53% | +3,53% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 37 | 51,35% | +0,27% | +0,24% | -0,07% | +0,79% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 40 | 55,00% | +0,25% | +0,25% | -0,08% | +0,75% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 40 | 55,00% | +0,25% | +0,25% | -0,08% | +0,75% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 35 | 34,29% | +0,42% | -0,17% | +0,07% | +0,91% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 8 | 12,50% | +0,66% | -0,66% | +0,09% | +0,94% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 36 | 50,00% | +0,14% | +0,01% | -0,33% | +0,81% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 39 | 53,85% | +0,32% | +0,32% | -0,15% | +0,99% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 39 | 53,85% | +0,32% | +0,32% | -0,15% | +0,99% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 52,94% | +0,04% | +0,04% | -0,42% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 34 | 38,24% | +0,52% | -0,69% | +0,07% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 8 | 12,50% | +0,95% | -0,95% | +0,58% | +1,56% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 36 | 44,44% | +0,28% | +0,08% | -1,25% | +1,85% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 38 | 55,26% | +0,33% | +0,33% | -1,23% | +1,82% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 38 | 55,26% | +0,33% | +0,33% | -1,23% | +1,82% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,35% | +0,35% | -1,24% | +1,77% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 33 | 30,30% | +0,68% | -0,84% | -1,00% | +2,10% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 8 | 12,50% | +2,41% | -2,41% | -0,24% | +3,25% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 34 | 32,35% | +0,29% | -0,08% | -2,01% | +2,32% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 36 | 41,67% | +0,28% | +0,28% | -1,98% | +2,34% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 36 | 41,67% | +0,28% | +0,28% | -1,98% | +2,34% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 32 | 43,75% | +0,39% | +0,39% | -1,96% | +2,34% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 31 | 35,48% | +0,50% | -1,11% | -1,74% | +2,60% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 6 | 16,67% | +2,89% | -2,89% | -0,91% | +4,25% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 32 | 40,62% | -0,02% | -0,35% | -2,37% | +2,35% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 34 | 50,00% | -0,05% | -0,05% | -2,35% | +2,37% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 34 | 50,00% | -0,05% | -0,05% | -2,35% | +2,37% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 30 | 53,33% | +0,12% | +0,12% | -2,33% | +2,37% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 29 | 34,48% | +0,33% | -0,86% | -2,10% | +2,59% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,94% | -1,94% | -1,23% | +3,13% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 31 | 41,94% | +0,40% | +0,11% | -2,68% | +2,92% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 33 | 48,48% | +0,24% | +0,24% | -2,70% | +2,91% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 33 | 48,48% | +0,24% | +0,24% | -2,70% | +2,91% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 29 | 55,17% | +0,55% | +0,55% | -2,60% | +2,98% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 28 | 32,14% | +0,48% | -0,12% | -2,43% | +3,21% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,32% | -1,32% | -1,42% | +3,31% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 27 | 48,15% | +0,29% | +0,16% | -2,83% | +3,47% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 29 | 48,28% | +0,16% | +0,16% | -2,86% | +3,41% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 29 | 48,28% | +0,16% | +0,16% | -2,86% | +3,41% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 25 | 56,00% | +0,58% | +0,58% | -2,61% | +3,58% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 24 | 58,33% | +0,46% | +0,40% | -2,53% | +3,78% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 20 | 30,00% | -0,07% | -0,40% | -3,17% | +3,80% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 22 | 45,45% | -0,16% | -0,16% | -3,21% | +3,70% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 22 | 45,45% | -0,16% | -0,16% | -3,21% | +3,70% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 18 | 50,00% | +0,11% | +0,11% | -2,93% | +3,99% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 18 | 22,22% | +0,29% | -0,67% | -2,87% | +4,14% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 2 | 0,00% | +0,90% | -0,90% | -2,23% | +2,76% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 12 | 83,33% | +0,69% | +1,11% | -2,86% | +5,08% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 13 | 61,54% | +0,58% | +0,58% | -2,84% | +5,05% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 13 | 61,54% | +0,58% | +0,58% | -2,84% | +5,05% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +0,21% | +0,21% | -2,50% | +5,16% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 11 | 45,45% | -0,01% | -0,46% | -2,60% | +4,94% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 38 | 44,74% | +0,15% | +0,14% | -0,29% | +0,88% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 40 | 55,00% | +0,04% | +0,35% | -0,41% | +0,76% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 40 | 55,00% | +0,04% | +0,35% | -0,41% | +0,76% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 33 | 51,52% | -0,13% | +0,13% | -0,60% | +0,48% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 27 | 37,04% | +0,44% | -0,44% | -0,04% | +1,04% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,92% | +1,13% | +0,84% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 37 | 45,95% | +0,07% | +0,06% | -0,53% | +1,12% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 39 | 48,72% | -0,05% | +0,19% | -0,65% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 39 | 48,72% | -0,05% | +0,19% | -0,65% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 37 | 48,65% | -0,12% | +0,27% | -0,67% | +0,95% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 33 | 60,61% | -0,28% | +0,28% | -0,87% | +0,59% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 26 | 46,15% | +0,42% | -0,42% | -0,16% | +1,46% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +3,12% | +2,46% | +2,21% | +3,52% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 36 | 44,44% | -0,12% | +0,20% | -1,69% | +2,11% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 38 | 50,00% | -0,22% | +0,11% | -1,79% | +1,95% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 38 | 50,00% | -0,22% | +0,11% | -1,79% | +1,95% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 36 | 52,78% | -0,43% | +0,32% | -1,74% | +1,84% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 33 | 48,48% | -0,26% | +0,25% | -1,90% | +1,81% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 25 | 36,00% | +0,22% | -0,22% | -1,67% | +2,52% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,70% | +1,18% | -0,25% | +5,07% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 34 | 52,94% | -0,35% | +0,39% | -2,53% | +2,59% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 36 | 50,00% | -0,44% | +0,27% | -2,60% | +2,44% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 36 | 50,00% | -0,44% | +0,27% | -2,60% | +2,44% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | -0,44% | +0,25% | -2,60% | +2,32% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 31 | 64,52% | -0,52% | +0,92% | -2,84% | +2,32% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 23 | 52,17% | -0,35% | +0,35% | -2,57% | +2,73% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 32 | 59,38% | -0,84% | +0,54% | -3,04% | +2,67% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 34 | 55,88% | -0,93% | +0,33% | -3,12% | +2,57% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 34 | 55,88% | -0,93% | +0,33% | -3,12% | +2,57% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | -0,92% | +0,28% | -3,15% | +2,45% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 30 | 63,33% | -1,05% | +1,05% | -3,36% | +2,36% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 22 | 54,55% | -0,91% | +0,91% | -3,18% | +2,88% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,63% | +0,36% | -0,50% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 31 | 54,84% | -1,03% | +0,97% | -3,60% | +3,03% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 33 | 54,55% | -1,08% | +0,84% | -3,65% | +2,91% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 33 | 54,55% | -1,08% | +0,84% | -3,65% | +2,91% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 31 | 54,84% | -1,10% | +0,83% | -3,66% | +2,80% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 30 | 66,67% | -1,40% | +1,40% | -3,88% | +2,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 22 | 59,09% | -1,13% | +1,13% | -3,71% | +2,91% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +0,93% | +0,18% | -1,31% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 27 | 59,26% | -1,74% | +1,70% | -4,58% | +3,16% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 29 | 65,52% | -1,77% | +1,46% | -4,58% | +3,01% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 29 | 65,52% | -1,77% | +1,46% | -4,58% | +3,01% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 27 | 66,67% | -1,78% | +1,45% | -4,64% | +2,90% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 28 | 71,43% | -2,07% | +2,07% | -4,68% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 20 | 70,00% | -2,09% | +2,09% | -4,80% | +3,07% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 21 | 76,19% | -2,74% | +2,80% | -5,59% | +3,02% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 22 | 77,27% | -2,79% | +2,59% | -5,65% | +2,88% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 22 | 77,27% | -2,79% | +2,59% | -5,65% | +2,88% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 20 | 80,00% | -2,95% | +2,72% | -5,84% | +2,71% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 22 | 86,36% | -2,79% | +2,79% | -5,65% | +2,88% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 18 | 83,33% | -2,56% | +2,56% | -5,46% | +3,32% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 13 | 92,31% | -3,53% | +3,53% | -6,62% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 13 | 92,31% | -3,53% | +3,53% | -6,62% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 13 | 92,31% | -3,53% | +3,53% | -6,62% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 13 | 92,31% | -3,53% | +3,53% | -6,62% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 13 | 92,31% | -3,53% | +3,53% | -6,62% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 12 | 91,67% | -3,31% | +3,31% | -6,50% | +2,79% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 33 | 54,55% | +0,38% | +0,19% | -0,12% | +1,04% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 36 | 61,11% | +0,10% | +0,34% | -0,37% | +0,72% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 39 | 58,97% | +0,18% | +0,23% | -0,31% | +0,81% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 37 | 48,65% | -0,03% | -0,07% | -0,52% | +0,55% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,04% | -0,04% | -0,54% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 32 | 46,88% | +0,44% | +0,22% | -0,22% | +1,29% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 35 | 51,43% | +0,19% | +0,32% | -0,52% | +0,91% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 38 | 50,00% | +0,20% | +0,27% | -0,48% | +1,06% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 33 | 48,48% | +0,28% | +0,31% | -0,43% | +1,13% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 37 | 37,84% | +0,26% | -0,57% | -0,40% | +1,12% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,02% | -0,02% | -0,52% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 31 | 48,39% | +0,56% | +0,28% | -1,76% | +2,29% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | +0,15% | +0,38% | -2,06% | +1,97% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 37 | 45,95% | +0,16% | +0,32% | -1,99% | +2,09% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 32 | 46,88% | +0,28% | +0,22% | -1,91% | +2,15% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 36 | 41,67% | +0,23% | -0,57% | -1,94% | +2,16% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 21 | 42,86% | +0,13% | -0,13% | -1,91% | +1,82% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 29 | 51,72% | +0,41% | +0,22% | -2,52% | +2,97% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 32 | 53,12% | +0,15% | +0,37% | -2,80% | +2,66% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 35 | 51,43% | +0,20% | +0,28% | -2,73% | +2,77% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 30 | 50,00% | +0,09% | +0,34% | -2,68% | +2,79% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 34 | 44,12% | +0,17% | -0,65% | -2,80% | +2,86% | PRIMA CALIBRAZIONE |
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
| SOL | 10g | Global confluence | BENCHMARK | 26 | 57,69% | +0,41% | +0,71% | -3,48% | +3,89% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 29 | 62,07% | +0,25% | +1,00% | -3,84% | +3,54% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 32 | 59,38% | +0,21% | +0,93% | -3,80% | +3,58% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 27 | 55,56% | +0,66% | +0,46% | -3,68% | +3,71% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 32 | 46,88% | +0,07% | -0,22% | -3,88% | +3,64% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,08% | +0,08% | -3,74% | +3,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 22 | 63,64% | -0,36% | +1,29% | -4,56% | +4,28% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 25 | 80,00% | +0,24% | +1,74% | -4,70% | +4,06% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 28 | 82,14% | -0,12% | +1,89% | -4,61% | +4,04% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 23 | 60,87% | +0,55% | +0,70% | -4,37% | +4,30% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 29 | 37,93% | -0,25% | -0,45% | -4,69% | +4,03% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 20 | 40,00% | +0,08% | -0,08% | -4,53% | +4,13% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 16 | 56,25% | -1,32% | -0,91% | -6,82% | +3,85% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 18 | 72,22% | -0,75% | +2,36% | -6,62% | +3,65% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 21 | 76,19% | -1,03% | +2,41% | -6,54% | +3,68% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 16 | 43,75% | -0,50% | +0,56% | -6,34% | +3,94% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 22 | 54,55% | -0,95% | -0,92% | -6,56% | +3,68% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 14 | 57,14% | +0,98% | -0,98% | -6,13% | +4,45% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 12 | 41,67% | +0,00% | -0,05% | -7,52% | +3,88% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 9 | 77,78% | -0,46% | +1,74% | -7,97% | +3,64% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 12 | 66,67% | -0,28% | +1,25% | -7,68% | +3,71% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 8 | 62,50% | -0,01% | +0,51% | -7,91% | +3,88% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 13 | 30,77% | -0,18% | -1,26% | -7,63% | +3,70% | FEEDBACK RAPIDO |
| SOL | 30g | Classic technical | CALIBRABILE | 5 | 40,00% | +0,15% | -0,15% | -6,51% | +4,11% | FEEDBACK RAPIDO |
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
