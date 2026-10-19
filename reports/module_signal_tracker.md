# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-19 05:34 UTC

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

Segnali totali salvati: **282**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-19 | BTC | 82.648,77 | -1 | +1 | +1 | 0 | -1 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-19 | DOGE | 0.07945 | -1 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-19 | SOL | 105,63 | -2 | +1 | +1 | 0 | -2 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-10-18 | BTC | 81.614,92 | +3 | +2 | +2 | 0 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-10-18 | DOGE | 0.07904 | -2 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-18 | SOL | 103,34 | -1 | +2 | +2 | 0 | -2 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-10-16 | BTC | 82.086,63 | +2 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-16 | DOGE | 0.08216 | -1 | +3 | +3 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-16 | SOL | 105,81 | 0 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-15 | BTC | 80.946,10 | -2 | +1 | +1 | 0 | -2 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-15 | DOGE | 0.07966 | -2 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-15 | SOL | 102,12 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 94 | 93 | 92 | 92 | 90 | 88 | 85 | 81 | 75 | 69 | 56 | 41 |
| SOL | 94 | 93 | 92 | 92 | 90 | 88 | 85 | 81 | 75 | 69 | 56 | 41 |
| DOGE | 94 | 93 | 92 | 92 | 90 | 88 | 85 | 81 | 75 | 69 | 56 | 41 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-21 | 60g | 2026-10-20 | domani |
| SOL | 2026-08-21 | 60g | 2026-10-20 | domani |
| DOGE | 2026-08-21 | 60g | 2026-10-20 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 83 | 51,81% | +0,31% | +0,27% | UTILE |
| BTC | 2g | 82 | 50,00% | +0,50% | +0,43% | UTILE |
| BTC | 3g | 82 | 46,34% | +0,62% | +0,59% | UTILE |
| BTC | 5g | 80 | 43,75% | +1,32% | +1,22% | UTILE |
| BTC | 7g | 79 | 51,90% | +2,03% | +1,92% | UTILE |
| BTC | 10g | 78 | 55,13% | +2,83% | +2,71% | UTILE |
| BTC | 14g | 76 | 59,21% | +4,21% | +4,17% | UTILE |
| BTC | 21g | 70 | 70,00% | +7,81% | +7,72% | UTILE |
| BTC | 30g | 66 | 95,45% | +11,98% | +11,32% | UTILE |
| BTC | 45g | 53 | 94,34% | +19,71% | +17,22% | PRIMA CALIBRAZIONE |
| BTC | 60g | 38 | 92,11% | +27,92% | +23,97% | PRIMA CALIBRAZIONE |
| SOL | 1g | 84 | 46,43% | +0,20% | +0,07% | UTILE |
| SOL | 2g | 83 | 44,58% | +0,57% | +0,48% | UTILE |
| SOL | 3g | 83 | 48,19% | +0,95% | +0,84% | UTILE |
| SOL | 5g | 82 | 48,78% | +1,67% | +1,61% | UTILE |
| SOL | 7g | 80 | 53,75% | +2,59% | +2,66% | UTILE |
| SOL | 10g | 77 | 55,84% | +4,11% | +4,21% | UTILE |
| SOL | 14g | 73 | 64,38% | +6,73% | +7,22% | UTILE |
| SOL | 21g | 67 | 76,12% | +12,84% | +12,31% | UTILE |
| SOL | 30g | 61 | 83,61% | +19,46% | +16,22% | UTILE |
| SOL | 45g | 49 | 75,51% | +33,04% | +17,34% | PRIMA CALIBRAZIONE |
| SOL | 60g | 34 | 67,65% | +45,16% | +19,38% | PRIMA CALIBRAZIONE |
| DOGE | 1g | 85 | 48,24% | -0,01% | -0,02% | UTILE |
| DOGE | 2g | 84 | 45,24% | +0,12% | -0,08% | UTILE |
| DOGE | 3g | 84 | 41,67% | +0,33% | +0,09% | UTILE |
| DOGE | 5g | 82 | 45,12% | +0,89% | +0,12% | UTILE |
| DOGE | 7g | 80 | 50,00% | +1,42% | +0,52% | UTILE |
| DOGE | 10g | 78 | 43,59% | +1,85% | +0,33% | UTILE |
| DOGE | 14g | 75 | 52,00% | +3,51% | +2,14% | UTILE |
| DOGE | 21g | 71 | 54,93% | +6,36% | +0,90% | UTILE |
| DOGE | 30g | 65 | 67,69% | +10,57% | +4,75% | UTILE |
| DOGE | 45g | 52 | 50,00% | +18,76% | +4,11% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 39 | 48,72% | +24,76% | +0,21% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 83 | 51,81% | +0,31% | +0,27% | -0,27% | +0,82% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 91 | 49,45% | +0,21% | +0,26% | -0,32% | +0,71% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 91 | 49,45% | +0,21% | +0,26% | -0,32% | +0,71% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 86 | 47,67% | +0,23% | +0,05% | -0,27% | +0,74% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,55% | -0,06% | -0,27% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 82 | 50,00% | +0,50% | +0,43% | -0,28% | +1,19% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 90 | 51,11% | +0,45% | +0,53% | -0,29% | +1,13% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 90 | 51,11% | +0,45% | +0,53% | -0,29% | +1,13% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 85 | 47,06% | +0,43% | +0,06% | -0,21% | +1,11% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,85% | -0,13% | -0,05% | +1,59% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 82 | 46,34% | +0,62% | +0,59% | -1,29% | +2,39% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 90 | 50,00% | +0,74% | +0,81% | -1,36% | +2,42% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 90 | 50,00% | +0,74% | +0,81% | -1,36% | +2,42% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 85 | 40,00% | +0,75% | -0,11% | -1,29% | +2,43% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 36 | 36,11% | +1,29% | -0,55% | -1,13% | +3,01% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 80 | 43,75% | +1,32% | +1,22% | -1,98% | +3,75% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 88 | 47,73% | +1,42% | +1,53% | -2,00% | +3,78% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 88 | 47,73% | +1,42% | +1,53% | -2,00% | +3,78% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 83 | 43,37% | +1,28% | -0,61% | -1,96% | +3,71% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 35 | 37,14% | +2,90% | -2,19% | -1,77% | +5,36% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 79 | 51,90% | +2,03% | +1,92% | -2,31% | +4,86% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 86 | 59,30% | +2,13% | +2,30% | -2,31% | +4,88% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 86 | 59,30% | +2,13% | +2,30% | -2,31% | +4,88% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 81 | 41,98% | +2,08% | -1,04% | -2,29% | +4,83% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 35 | 34,29% | +4,08% | -3,67% | -2,18% | +7,18% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 78 | 55,13% | +2,83% | +2,71% | -2,63% | +5,98% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 83 | 66,27% | +2,91% | +3,25% | -2,59% | +6,03% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 83 | 66,27% | +2,91% | +3,25% | -2,59% | +6,03% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 78 | 44,87% | +2,87% | -0,54% | -2,60% | +6,05% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 34 | 35,29% | +4,28% | -4,21% | -2,33% | +7,98% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -1,47% | -1,47% | -4,23% | +1,69% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 76 | 59,21% | +4,21% | +4,17% | -2,86% | +8,00% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 79 | 60,76% | +4,32% | +4,53% | -2,83% | +8,11% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 79 | 60,76% | +4,32% | +4,53% | -2,83% | +8,11% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 74 | 54,05% | +4,36% | +1,08% | -2,85% | +8,24% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 33 | 21,21% | +3,99% | -4,13% | -2,45% | +8,63% | PRIMA CALIBRAZIONE |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,75% | -0,75% | -4,66% | +2,55% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 70 | 70,00% | +7,81% | +7,72% | -2,94% | +11,73% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 75 | 76,00% | +7,48% | +7,65% | -2,99% | +11,49% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 75 | 76,00% | +7,48% | +7,65% | -2,99% | +11,49% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 68 | 52,94% | +7,85% | +1,15% | -2,97% | +11,88% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 29 | 44,83% | +8,60% | -4,88% | -2,40% | +12,46% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 66 | 95,45% | +11,98% | +11,32% | -2,91% | +16,28% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 69 | 92,75% | +11,96% | +11,96% | -2,89% | +16,36% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 69 | 92,75% | +11,96% | +11,96% | -2,89% | +16,36% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 62 | 66,13% | +12,05% | +1,30% | -2,85% | +16,53% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 28 | 57,14% | +12,44% | -2,72% | -2,47% | +17,06% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 53 | 94,34% | +19,71% | +17,22% | -2,72% | +24,68% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 56 | 100,00% | +20,10% | +20,10% | -2,71% | +24,95% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 56 | 100,00% | +20,10% | +20,10% | -2,71% | +24,95% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 51 | 56,86% | +20,02% | -1,52% | -2,53% | +24,92% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,92% | -4,17% | -2,62% | +19,88% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 100,00% | +8,74% | +8,74% | -4,87% | +14,33% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 38 | 92,11% | +27,92% | +23,97% | -2,18% | +33,41% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 41 | 100,00% | +27,73% | +27,73% | -2,20% | +33,35% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 41 | 100,00% | +27,73% | +27,73% | -2,20% | +33,35% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +28,58% | +28,58% | -2,21% | +34,30% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 36 | 38,89% | +28,04% | -7,37% | -1,89% | +33,87% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 9 | 11,11% | +30,78% | -26,59% | -0,19% | +36,90% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 85 | 48,24% | -0,01% | -0,02% | -0,79% | +1,03% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 92 | 58,70% | -0,06% | +0,44% | -0,88% | +0,92% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 92 | 58,70% | -0,06% | +0,44% | -0,88% | +0,92% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 86 | 50,00% | -0,15% | +0,19% | -0,99% | +0,83% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 53 | 39,62% | -0,06% | -0,55% | -0,98% | +0,64% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 58,33% | +2,27% | +2,00% | +0,38% | +3,14% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 84 | 45,24% | +0,12% | -0,08% | -1,02% | +1,49% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 91 | 56,04% | -0,05% | +0,65% | -1,14% | +1,26% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 91 | 56,04% | -0,05% | +0,65% | -1,14% | +1,26% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 85 | 55,29% | -0,35% | +0,25% | -1,45% | +0,96% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 52 | 46,15% | -0,01% | -0,91% | -1,21% | +1,01% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 41,67% | +2,33% | +2,11% | +0,69% | +4,97% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 84 | 41,67% | +0,33% | +0,09% | -2,65% | +3,55% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 91 | 53,85% | +0,03% | +0,89% | -2,82% | +3,24% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 91 | 53,85% | +0,03% | +0,89% | -2,82% | +3,24% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 85 | 48,24% | -0,55% | +0,10% | -3,07% | +2,62% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 52 | 38,46% | +0,16% | -1,62% | -2,89% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 50,00% | +2,30% | +2,13% | -1,68% | +5,97% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 82 | 45,12% | +0,89% | +0,12% | -3,82% | +5,78% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 89 | 51,69% | +0,49% | +1,24% | -4,09% | +5,44% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 89 | 51,69% | +0,49% | +1,24% | -4,09% | +5,44% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 83 | 53,01% | -0,27% | -0,52% | -4,47% | +4,75% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 50 | 40,00% | +1,07% | -3,63% | -4,14% | +6,08% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 80 | 50,00% | +1,42% | +0,52% | -4,48% | +7,70% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 87 | 56,32% | +1,08% | +1,61% | -4,77% | +7,31% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 87 | 56,32% | +1,08% | +1,61% | -4,77% | +7,31% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 81 | 46,91% | +0,15% | -0,90% | -5,23% | +6,39% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 49 | 34,69% | +1,98% | -5,06% | -4,80% | +8,03% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 78 | 43,59% | +1,85% | +0,33% | -5,34% | +9,53% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 84 | 57,14% | +1,40% | +2,12% | -5,56% | +9,19% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 84 | 57,14% | +1,40% | +2,12% | -5,56% | +9,19% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 78 | 44,87% | +0,15% | -1,95% | -6,10% | +7,82% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 46 | 32,61% | +2,88% | -6,43% | -5,36% | +10,41% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 75 | 52,00% | +3,51% | +2,14% | -6,09% | +13,04% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 80 | 66,25% | +2,77% | +3,95% | -6,29% | +12,48% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 80 | 66,25% | +2,77% | +3,95% | -6,29% | +12,48% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 74 | 43,24% | +0,84% | -2,51% | -6,91% | +10,10% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 44 | 38,64% | +4,07% | -5,67% | -5,83% | +12,84% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 71 | 54,93% | +6,36% | +0,90% | -6,31% | +18,07% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 74 | 60,81% | +6,73% | +5,21% | -6,27% | +18,27% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 74 | 60,81% | +6,73% | +5,21% | -6,27% | +18,27% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 68 | 51,47% | +4,77% | -3,25% | -6,96% | +15,56% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 43 | 41,86% | +5,14% | -7,66% | -6,03% | +15,65% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +4,84% | -0,04% | -5,47% | +18,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 65 | 67,69% | +10,57% | +4,75% | -5,49% | +25,70% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 68 | 69,12% | +10,87% | +6,79% | -5,47% | +26,13% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 68 | 69,12% | +10,87% | +6,79% | -5,47% | +26,13% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 62 | 58,06% | +9,46% | -2,31% | -6,17% | +24,12% | UTILE |
| DOGE | 30g | Classic technical | CALIBRABILE | 41 | 48,78% | +8,28% | -6,60% | -5,70% | +22,87% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 80,00% | +17,31% | +10,98% | -5,24% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 52 | 50,00% | +18,76% | +4,11% | -4,84% | +37,36% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 55 | 65,45% | +18,46% | +7,82% | -4,85% | +37,25% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 55 | 65,45% | +18,46% | +7,82% | -4,85% | +37,25% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 49 | 10,20% | +15,49% | -12,42% | -5,66% | +35,18% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 31 | 3,23% | +21,52% | -22,01% | -5,10% | +38,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +21,73% | +11,03% | -4,45% | +35,73% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 39 | 48,72% | +24,76% | +0,21% | -3,35% | +45,27% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 41 | 60,98% | +25,22% | +9,30% | -3,40% | +45,38% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 41 | 60,98% | +25,22% | +9,30% | -3,40% | +45,38% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +24,96% | +11,95% | -3,59% | +45,33% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 34 | 8,82% | +25,84% | -23,39% | -4,14% | +44,26% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 27 | 0,00% | +23,75% | -23,75% | -3,76% | +44,21% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +31,87% | +16,90% | -0,17% | +49,22% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 84 | 46,43% | +0,20% | +0,07% | -0,60% | +1,05% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 87 | 54,02% | +0,16% | +0,42% | -0,71% | +1,00% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 90 | 53,33% | +0,19% | +0,37% | -0,68% | +1,03% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 85 | 45,88% | +0,15% | -0,09% | -0,77% | +0,98% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 59 | 44,07% | +0,51% | -0,09% | -0,48% | +1,43% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 83 | 44,58% | +0,57% | +0,48% | -0,67% | +1,64% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 86 | 48,84% | +0,44% | +0,62% | -0,89% | +1,39% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 89 | 48,31% | +0,44% | +0,59% | -0,86% | +1,44% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 84 | 45,24% | +0,27% | -0,02% | -0,87% | +1,40% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,60% | +0,15% | -0,64% | +1,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 83 | 48,19% | +0,95% | +0,84% | -2,25% | +3,56% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 86 | 51,16% | +0,80% | +1,14% | -2,40% | +3,37% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 89 | 50,56% | +0,78% | +1,09% | -2,36% | +3,37% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 84 | 45,24% | +0,41% | -0,31% | -2,43% | +2,96% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 59 | 45,76% | +0,61% | +0,08% | -2,23% | +3,14% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 82 | 48,78% | +1,67% | +1,61% | -3,32% | +5,51% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 84 | 52,38% | +1,48% | +1,86% | -3,43% | +5,32% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 87 | 51,72% | +1,46% | +1,77% | -3,38% | +5,28% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 82 | 46,34% | +1,10% | -0,74% | -3,49% | +4,80% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 58 | 48,28% | +0,68% | +0,02% | -3,30% | +4,39% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 80 | 53,75% | +2,59% | +2,66% | -3,92% | +7,16% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 82 | 60,98% | +2,37% | +3,14% | -4,04% | +6,95% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 85 | 61,18% | +2,28% | +3,04% | -3,99% | +6,84% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 80 | 40,00% | +1,44% | -1,74% | -4,13% | +6,10% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 58 | 43,10% | +0,35% | -0,23% | -4,10% | +5,03% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 77 | 55,84% | +4,11% | +4,21% | -4,45% | +9,24% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 79 | 69,62% | +3,96% | +5,82% | -4,58% | +8,90% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 82 | 68,29% | +3,81% | +5,62% | -4,54% | +8,72% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 77 | 41,56% | +2,40% | -2,41% | -4,75% | +7,60% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 57 | 43,86% | +0,11% | -0,57% | -4,99% | +5,77% | PRIMA CALIBRAZIONE |

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
