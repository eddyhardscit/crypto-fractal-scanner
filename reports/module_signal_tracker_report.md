# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-06 05:33 UTC

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

Segnali totali salvati: **246**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-06 | BTC | 85.661,60 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-06 | DOGE | 0.09487 | -1 | -2 | -2 | 0 | +1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-06 | SOL | 120,08 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-05 | BTC | 85.487,99 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-05 | DOGE | 0.09488 | 0 | -2 | -2 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-10-05 | SOL | 120,07 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-04 | BTC | 84.850,99 | +4 | 0 | 0 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-10-04 | DOGE | 0.09275 | 0 | -2 | -2 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-10-04 | SOL | 120,74 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-03 | BTC | 84.628,98 | +1 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-03 | DOGE | 0.09320 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-03 | SOL | 119,63 | +3 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 82 | 81 | 80 | 79 | 77 | 76 | 73 | 70 | 67 | 58 | 43 | 30 |
| SOL | 82 | 81 | 80 | 79 | 77 | 76 | 73 | 70 | 67 | 58 | 43 | 30 |
| DOGE | 82 | 81 | 80 | 79 | 77 | 76 | 73 | 70 | 67 | 58 | 43 | 30 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-08 | 60g | 2026-10-07 | domani |
| SOL | 2026-08-08 | 60g | 2026-10-07 | domani |
| DOGE | 2026-08-08 | 60g | 2026-10-07 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 76 | 53,95% | +0,35% | +0,33% | UTILE |
| BTC | 2g | 75 | 53,33% | +0,65% | +0,59% | UTILE |
| BTC | 3g | 74 | 47,30% | +0,83% | +0,74% | UTILE |
| BTC | 5g | 72 | 45,83% | +1,72% | +1,54% | UTILE |
| BTC | 7g | 71 | 54,93% | +2,49% | +2,34% | UTILE |
| BTC | 10g | 69 | 62,32% | +3,47% | +3,34% | UTILE |
| BTC | 14g | 67 | 62,69% | +5,07% | +5,01% | UTILE |
| BTC | 21g | 64 | 73,44% | +8,36% | +8,26% | UTILE |
| BTC | 30g | 55 | 94,55% | +13,06% | +12,27% | PRIMA CALIBRAZIONE |
| BTC | 45g | 40 | 92,50% | +24,37% | +21,06% | PRIMA CALIBRAZIONE |
| BTC | 60g | 28 | 89,29% | +27,77% | +22,41% | FEEDBACK RAPIDO |
| SOL | 1g | 73 | 50,68% | +0,37% | +0,28% | UTILE |
| SOL | 2g | 72 | 48,61% | +1,03% | +0,93% | UTILE |
| SOL | 3g | 71 | 53,52% | +1,70% | +1,57% | UTILE |
| SOL | 5g | 69 | 57,97% | +3,02% | +2,94% | UTILE |
| SOL | 7g | 68 | 63,24% | +4,33% | +4,40% | UTILE |
| SOL | 10g | 65 | 66,15% | +6,43% | +6,54% | UTILE |
| SOL | 14g | 62 | 75,81% | +9,60% | +10,19% | UTILE |
| SOL | 21g | 60 | 83,33% | +15,11% | +14,52% | UTILE |
| SOL | 30g | 51 | 80,39% | +21,68% | +17,80% | PRIMA CALIBRAZIONE |
| SOL | 45g | 36 | 69,44% | +42,15% | +20,77% | PRIMA CALIBRAZIONE |
| SOL | 60g | 23 | 52,17% | +46,83% | +8,73% | FEEDBACK RAPIDO |
| DOGE | 1g | 75 | 45,33% | +0,19% | -0,14% | UTILE |
| DOGE | 2g | 75 | 44,00% | +0,50% | -0,20% | UTILE |
| DOGE | 3g | 75 | 38,67% | +0,82% | -0,07% | UTILE |
| DOGE | 5g | 73 | 43,84% | +1,73% | +0,03% | UTILE |
| DOGE | 7g | 72 | 48,61% | +2,48% | +0,31% | UTILE |
| DOGE | 10g | 69 | 43,48% | +3,29% | +0,26% | UTILE |
| DOGE | 14g | 66 | 57,58% | +5,55% | +3,53% | UTILE |
| DOGE | 21g | 63 | 61,90% | +8,40% | +2,93% | UTILE |
| DOGE | 30g | 54 | 74,07% | +12,81% | +5,92% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 41 | 51,22% | +24,59% | +5,09% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 28 | 28,57% | +27,07% | -7,13% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 76 | 53,95% | +0,35% | +0,33% | -0,20% | +0,87% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 79 | 49,37% | +0,29% | +0,29% | -0,22% | +0,80% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 79 | 49,37% | +0,29% | +0,29% | -0,22% | +0,80% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 74 | 44,59% | +0,31% | +0,03% | -0,15% | +0,84% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 33 | 42,42% | +0,61% | +0,02% | -0,17% | +1,14% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,49% | -0,49% | -1,07% | -0,05% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 75 | 53,33% | +0,65% | +0,59% | -0,15% | +1,34% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 78 | 51,28% | +0,63% | +0,61% | -0,10% | +1,34% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 78 | 51,28% | +0,63% | +0,61% | -0,10% | +1,34% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 73 | 45,21% | +0,63% | +0,07% | +0,00% | +1,33% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 32 | 43,75% | +1,09% | +0,02% | +0,15% | +1,79% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,28% | -0,28% | -1,06% | +0,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 74 | 47,30% | +0,83% | +0,74% | -1,17% | +2,53% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 78 | 50,00% | +1,00% | +0,85% | -1,17% | +2,66% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 78 | 50,00% | +1,00% | +0,85% | -1,17% | +2,66% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 72 | 37,50% | +1,05% | -0,12% | -1,09% | +2,70% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 31 | 38,71% | +1,82% | -0,48% | -0,87% | +3,28% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,50% | -0,50% | -1,88% | +1,29% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 72 | 45,83% | +1,72% | +1,54% | -1,74% | +4,04% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 76 | 46,05% | +1,89% | +1,69% | -1,73% | +4,22% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 76 | 46,05% | +1,89% | +1,69% | -1,73% | +4,22% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 70 | 44,29% | +1,83% | -0,59% | -1,64% | +4,20% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 29 | 41,38% | +4,06% | -2,25% | -1,22% | +6,21% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 14,29% | -1,43% | -1,43% | -2,57% | +1,68% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 71 | 54,93% | +2,49% | +2,34% | -2,06% | +5,22% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 76 | 55,26% | +2,67% | +2,47% | -2,03% | +5,36% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 76 | 55,26% | +2,67% | +2,47% | -2,03% | +5,36% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 69 | 46,38% | +2,74% | -0,95% | -1,96% | +5,40% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 29 | 37,93% | +5,44% | -4,00% | -1,49% | +8,41% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -1,74% | -1,74% | -3,24% | +1,77% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 69 | 62,32% | +3,47% | +3,34% | -2,40% | +6,43% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 73 | 64,38% | +3,58% | +3,52% | -2,37% | +6,56% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 73 | 64,38% | +3,58% | +3,52% | -2,37% | +6,56% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 66 | 51,52% | +3,73% | -0,30% | -2,31% | +6,72% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 29 | 41,38% | +5,56% | -4,39% | -1,70% | +9,12% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -1,21% | -1,21% | -3,81% | +1,86% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 67 | 62,69% | +5,07% | +5,01% | -2,59% | +8,70% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 70 | 62,86% | +5,14% | +5,14% | -2,58% | +8,78% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 70 | 62,86% | +5,14% | +5,14% | -2,58% | +8,78% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 63 | 58,73% | +5,47% | +1,62% | -2,51% | +9,15% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 28 | 25,00% | +5,37% | -4,20% | -1,80% | +9,90% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 50,00% | +0,35% | +0,35% | -4,22% | +3,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 64 | 73,44% | +8,36% | +8,26% | -2,89% | +12,18% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 67 | 77,61% | +8,30% | +8,30% | -2,87% | +12,14% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 67 | 77,61% | +8,30% | +8,30% | -2,87% | +12,14% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 62 | 58,06% | +8,84% | +1,49% | -2,74% | +12,73% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 26 | 50,00% | +8,98% | -4,54% | -2,39% | +12,74% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 55 | 94,55% | +13,06% | +12,27% | -2,84% | +17,04% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 58 | 91,38% | +12,99% | +12,99% | -2,82% | +17,10% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 58 | 91,38% | +12,99% | +12,99% | -2,82% | +17,10% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 53 | 60,38% | +13,01% | +0,44% | -2,67% | +17,31% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,37% | -2,02% | -2,62% | +17,60% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 40 | 92,50% | +24,37% | +21,06% | -2,15% | +29,01% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 43 | 100,00% | +24,55% | +24,55% | -2,17% | +29,06% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 43 | 100,00% | +24,55% | +24,55% | -2,17% | +29,06% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 38 | 42,11% | +25,02% | -3,88% | -1,87% | +29,55% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 11 | 27,27% | +24,00% | -15,47% | -0,42% | +29,95% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 28 | 89,29% | +27,77% | +22,41% | -2,90% | +32,62% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 30 | 100,00% | +27,55% | +27,55% | -2,95% | +32,49% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 30 | 100,00% | +27,55% | +27,55% | -2,95% | +32,49% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 26 | 100,00% | +28,31% | +28,31% | -2,72% | +33,45% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 25 | 32,00% | +27,95% | -10,97% | -2,65% | +33,07% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 4 | 0,00% | +33,67% | -33,67% | -1,55% | +38,08% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 75 | 45,33% | +0,19% | -0,14% | -0,59% | +1,21% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 80 | 57,50% | +0,14% | +0,46% | -0,64% | +1,12% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 80 | 57,50% | +0,14% | +0,46% | -0,64% | +1,12% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 74 | 50,00% | +0,06% | +0,12% | -0,74% | +1,03% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 44 | 38,64% | +0,01% | -0,74% | -0,85% | +0,76% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 75 | 44,00% | +0,50% | -0,20% | -0,62% | +1,89% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 79 | 56,96% | +0,39% | +0,71% | -0,71% | +1,69% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 79 | 56,96% | +0,39% | +0,71% | -0,71% | +1,69% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 73 | 53,42% | +0,08% | +0,14% | -1,02% | +1,38% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 44 | 40,91% | +0,32% | -1,41% | -0,90% | +1,29% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 75 | 38,67% | +0,82% | -0,07% | -2,24% | +3,96% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 78 | 55,13% | +0,68% | +0,98% | -2,33% | +3,68% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 78 | 55,13% | +0,68% | +0,98% | -2,33% | +3,68% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 72 | 44,44% | +0,05% | -0,02% | -2,57% | +2,99% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 44 | 29,55% | +0,62% | -2,34% | -2,62% | +3,83% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 73 | 43,84% | +1,73% | +0,03% | -3,26% | +6,41% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 76 | 51,32% | +1,63% | +1,30% | -3,29% | +6,19% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 76 | 51,32% | +1,63% | +1,30% | -3,29% | +6,19% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 70 | 51,43% | +0,83% | -0,65% | -3,68% | +5,44% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 43 | 32,56% | +2,13% | -4,81% | -3,64% | +6,91% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 72 | 48,61% | +2,48% | +0,31% | -3,83% | +8,39% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 75 | 54,67% | +2,50% | +1,38% | -3,85% | +8,22% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 75 | 54,67% | +2,50% | +1,38% | -3,85% | +8,22% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 69 | 46,38% | +1,53% | -0,98% | -4,30% | +7,22% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 43 | 27,91% | +3,41% | -6,38% | -4,15% | +8,99% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 69 | 43,48% | +3,29% | +0,26% | -4,52% | +10,49% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 72 | 51,39% | +3,21% | +1,08% | -4,51% | +10,33% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 72 | 51,39% | +3,21% | +1,08% | -4,51% | +10,33% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 66 | 48,48% | +1,91% | -1,46% | -5,05% | +8,81% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 43 | 30,23% | +3,70% | -7,04% | -4,91% | +11,04% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 66 | 57,58% | +5,55% | +3,53% | -4,92% | +14,51% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 69 | 60,87% | +5,15% | +2,64% | -4,90% | +14,10% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 69 | 60,87% | +5,15% | +2,64% | -4,90% | +14,10% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 63 | 50,79% | +3,11% | -0,83% | -5,50% | +11,45% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 41 | 41,46% | +5,35% | -5,10% | -5,18% | +13,82% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 63 | 61,90% | +8,40% | +2,93% | -5,35% | +19,20% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 66 | 59,09% | +8,73% | +4,66% | -5,36% | +19,37% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 66 | 59,09% | +8,73% | +4,66% | -5,36% | +19,37% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 60 | 58,33% | +6,70% | -1,67% | -6,05% | +16,40% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 39 | 46,15% | +6,00% | -7,03% | -5,67% | +15,73% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 66,67% | +6,54% | +0,57% | -4,75% | +18,76% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 54 | 74,07% | +12,81% | +5,92% | -5,06% | +26,10% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 57 | 73,68% | +13,05% | +8,01% | -5,06% | +26,58% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 57 | 73,68% | +13,05% | +8,01% | -5,06% | +26,58% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 51 | 62,75% | +11,60% | -2,60% | -5,86% | +24,20% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 32 | 50,00% | +10,61% | -8,31% | -5,37% | +22,37% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 88,89% | +19,48% | +12,44% | -5,48% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 41 | 51,22% | +24,59% | +5,09% | -3,61% | +41,56% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 43 | 62,79% | +24,45% | +9,74% | -3,65% | +41,49% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 43 | 62,79% | +24,45% | +9,74% | -3,65% | +41,49% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 36 | 13,89% | +22,11% | -15,88% | -4,39% | +39,93% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 28 | 3,57% | +24,28% | -23,92% | -4,09% | +41,07% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 83,33% | +29,79% | +15,53% | -2,20% | +41,23% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 28 | 28,57% | +27,07% | -7,13% | -4,78% | +43,48% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 30 | 46,67% | +27,55% | +5,79% | -4,76% | +43,75% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 30 | 46,67% | +27,55% | +5,79% | -4,76% | +43,75% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 28 | 50,00% | +26,69% | +9,03% | -4,83% | +43,41% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 29 | 0,00% | +27,27% | -27,27% | -4,87% | +43,52% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 21 | 0,00% | +25,52% | -25,52% | -5,03% | +42,31% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +42,43% | +17,48% | -1,27% | +51,44% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 73 | 50,68% | +0,37% | +0,28% | -0,36% | +1,24% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 75 | 54,67% | +0,35% | +0,44% | -0,47% | +1,21% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 78 | 53,85% | +0,38% | +0,38% | -0,44% | +1,24% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 73 | 46,58% | +0,35% | -0,03% | -0,53% | +1,19% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 55 | 47,27% | +0,55% | +0,04% | -0,45% | +1,48% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 72 | 48,61% | +1,03% | +0,93% | -0,22% | +2,11% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 74 | 48,65% | +0,91% | +0,67% | -0,46% | +1,84% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 77 | 48,05% | +0,89% | +0,63% | -0,44% | +1,88% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 72 | 43,06% | +0,72% | -0,03% | -0,42% | +1,87% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 54 | 50,00% | +0,82% | +0,37% | -0,45% | +1,90% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 71 | 53,52% | +1,70% | +1,57% | -1,73% | +4,06% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 73 | 50,68% | +1,51% | +1,20% | -1,89% | +3,86% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 76 | 50,00% | +1,47% | +1,14% | -1,86% | +3,84% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 71 | 46,48% | +1,08% | -0,18% | -1,91% | +3,39% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 53 | 50,94% | +1,08% | +0,54% | -1,86% | +3,33% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 69 | 57,97% | +3,02% | +2,94% | -2,43% | +6,46% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 71 | 52,11% | +2,76% | +1,98% | -2,59% | +6,21% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 74 | 51,35% | +2,67% | +1,87% | -2,57% | +6,12% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 69 | 47,83% | +2,34% | -0,44% | -2,64% | +5,61% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 51 | 54,90% | +1,63% | +0,89% | -2,59% | +4,86% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 68 | 63,24% | +4,33% | +4,40% | -2,86% | +8,26% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 70 | 60,00% | +4,02% | +3,07% | -3,03% | +7,99% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 73 | 60,27% | +3,85% | +2,95% | -3,01% | +7,82% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 68 | 42,65% | +2,97% | -1,23% | -3,11% | +7,02% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 50 | 50,00% | +1,59% | +0,92% | -3,11% | +5,64% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 65 | 66,15% | +6,43% | +6,54% | -3,25% | +10,66% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 68 | 66,18% | +6,06% | +5,44% | -3,44% | +10,12% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 71 | 64,79% | +5,79% | +5,22% | -3,44% | +9,86% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 65 | 47,69% | +4,40% | -1,43% | -3,60% | +8,71% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 47 | 53,19% | +1,98% | +1,15% | -3,70% | +6,60% | PRIMA CALIBRAZIONE |

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
