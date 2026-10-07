# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-07 05:33 UTC

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

Segnali totali salvati: **249**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-07 | BTC | 84.216,36 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-07 | DOGE | 0.09034 | -3 | -2 | -2 | 0 | -1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-07 | SOL | 118,68 | +1 | -2 | -2 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-06 | BTC | 85.661,60 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-06 | DOGE | 0.09487 | -1 | -2 | -2 | 0 | +1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-06 | SOL | 120,08 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-05 | BTC | 85.487,99 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-05 | DOGE | 0.09488 | 0 | -2 | -2 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-10-05 | SOL | 120,07 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-04 | BTC | 84.850,99 | +4 | 0 | 0 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-10-04 | DOGE | 0.09275 | 0 | -2 | -2 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-10-04 | SOL | 120,74 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 83 | 82 | 81 | 80 | 78 | 77 | 74 | 71 | 68 | 59 | 44 | 31 |
| SOL | 83 | 82 | 81 | 80 | 78 | 77 | 74 | 71 | 68 | 59 | 44 | 31 |
| DOGE | 83 | 82 | 81 | 80 | 78 | 77 | 74 | 71 | 68 | 59 | 44 | 31 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-09 | 60g | 2026-10-08 | domani |
| SOL | 2026-08-09 | 60g | 2026-10-08 | domani |
| DOGE | 2026-08-09 | 60g | 2026-10-08 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 77 | 53,25% | +0,32% | +0,30% | UTILE |
| BTC | 2g | 76 | 52,63% | +0,63% | +0,56% | UTILE |
| BTC | 3g | 75 | 46,67% | +0,81% | +0,72% | UTILE |
| BTC | 5g | 73 | 45,21% | +1,66% | +1,48% | UTILE |
| BTC | 7g | 72 | 55,56% | +2,47% | +2,32% | UTILE |
| BTC | 10g | 69 | 62,32% | +3,47% | +3,34% | UTILE |
| BTC | 14g | 68 | 61,76% | +4,95% | +4,90% | UTILE |
| BTC | 21g | 65 | 73,85% | +8,41% | +8,30% | UTILE |
| BTC | 30g | 56 | 94,64% | +12,92% | +12,15% | PRIMA CALIBRAZIONE |
| BTC | 45g | 41 | 92,68% | +24,03% | +20,80% | PRIMA CALIBRAZIONE |
| BTC | 60g | 29 | 89,66% | +27,83% | +22,66% | FEEDBACK RAPIDO |
| SOL | 1g | 74 | 50,00% | +0,35% | +0,26% | UTILE |
| SOL | 2g | 73 | 47,95% | +1,00% | +0,90% | UTILE |
| SOL | 3g | 72 | 52,78% | +1,65% | +1,53% | UTILE |
| SOL | 5g | 70 | 57,14% | +2,93% | +2,86% | UTILE |
| SOL | 7g | 69 | 62,32% | +4,26% | +4,33% | UTILE |
| SOL | 10g | 66 | 65,15% | +6,30% | +6,42% | UTILE |
| SOL | 14g | 63 | 74,60% | +9,44% | +10,02% | UTILE |
| SOL | 21g | 61 | 83,61% | +15,23% | +14,65% | UTILE |
| SOL | 30g | 52 | 80,77% | +21,50% | +17,70% | PRIMA CALIBRAZIONE |
| SOL | 45g | 37 | 70,27% | +41,76% | +20,95% | PRIMA CALIBRAZIONE |
| SOL | 60g | 24 | 54,17% | +47,35% | +10,83% | FEEDBACK RAPIDO |
| DOGE | 1g | 76 | 46,05% | +0,13% | -0,07% | UTILE |
| DOGE | 2g | 75 | 44,00% | +0,50% | -0,20% | UTILE |
| DOGE | 3g | 75 | 38,67% | +0,82% | -0,07% | UTILE |
| DOGE | 5g | 74 | 43,24% | +1,62% | -0,06% | UTILE |
| DOGE | 7g | 73 | 47,95% | +2,39% | +0,25% | UTILE |
| DOGE | 10g | 70 | 42,86% | +3,16% | +0,18% | UTILE |
| DOGE | 14g | 67 | 56,72% | +5,29% | +3,31% | UTILE |
| DOGE | 21g | 64 | 60,94% | +8,47% | +2,68% | UTILE |
| DOGE | 30g | 55 | 74,55% | +12,58% | +5,81% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 42 | 50,00% | +24,00% | +4,97% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 29 | 31,03% | +27,13% | -5,89% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 77 | 53,25% | +0,32% | +0,30% | -0,22% | +0,85% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 80 | 50,00% | +0,26% | +0,30% | -0,25% | +0,79% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 80 | 50,00% | +0,26% | +0,30% | -0,25% | +0,79% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 75 | 44,00% | +0,29% | +0,01% | -0,18% | +0,83% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,55% | -0,03% | -0,23% | +1,11% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,49% | -0,49% | -1,07% | -0,05% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 76 | 52,63% | +0,63% | +0,56% | -0,17% | +1,33% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 79 | 51,90% | +0,61% | +0,62% | -0,12% | +1,32% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 79 | 51,90% | +0,61% | +0,62% | -0,12% | +1,32% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 74 | 44,59% | +0,60% | +0,05% | -0,02% | +1,32% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 33 | 42,42% | +1,01% | -0,03% | +0,09% | +1,74% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,28% | -0,28% | -1,06% | +0,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 75 | 46,67% | +0,81% | +0,72% | -1,17% | +2,53% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 78 | 50,00% | +1,00% | +0,85% | -1,17% | +2,66% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 78 | 50,00% | +1,00% | +0,85% | -1,17% | +2,66% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 73 | 36,99% | +1,02% | -0,13% | -1,09% | +2,70% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 32 | 37,50% | +1,74% | -0,49% | -0,88% | +3,26% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,50% | -0,50% | -1,88% | +1,29% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 73 | 45,21% | +1,66% | +1,48% | -1,76% | +3,99% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 77 | 45,45% | +1,83% | +1,63% | -1,75% | +4,17% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 77 | 45,45% | +1,83% | +1,63% | -1,75% | +4,17% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 71 | 43,66% | +1,77% | -0,62% | -1,66% | +4,14% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 30 | 40,00% | +3,84% | -2,26% | -1,29% | +6,02% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 72 | 55,56% | +2,47% | +2,32% | -2,03% | +5,21% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 76 | 55,26% | +2,67% | +2,47% | -2,03% | +5,36% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 76 | 55,26% | +2,67% | +2,47% | -2,03% | +5,36% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 70 | 47,14% | +2,72% | -0,93% | -1,93% | +5,38% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 29 | 37,93% | +5,44% | -4,00% | -1,49% | +8,41% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -1,74% | -1,74% | -3,24% | +1,77% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 69 | 62,32% | +3,47% | +3,34% | -2,40% | +6,43% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 74 | 64,86% | +3,53% | +3,48% | -2,37% | +6,52% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 74 | 64,86% | +3,53% | +3,48% | -2,37% | +6,52% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 67 | 50,75% | +3,67% | -0,30% | -2,31% | +6,67% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 29 | 41,38% | +5,56% | -4,39% | -1,70% | +9,12% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -1,21% | -1,21% | -3,81% | +1,86% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 68 | 61,76% | +4,95% | +4,90% | -2,63% | +8,58% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 71 | 61,97% | +5,02% | +5,02% | -2,61% | +8,67% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 71 | 61,97% | +5,02% | +5,02% | -2,61% | +8,67% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 64 | 57,81% | +5,34% | +1,55% | -2,55% | +9,02% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 29 | 24,14% | +5,09% | -4,15% | -1,91% | +9,57% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,11% | -0,11% | -4,30% | +2,85% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 65 | 73,85% | +8,41% | +8,30% | -2,84% | +12,23% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 68 | 77,94% | +8,34% | +8,34% | -2,82% | +12,18% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 68 | 77,94% | +8,34% | +8,34% | -2,82% | +12,18% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 62 | 58,06% | +8,84% | +1,49% | -2,74% | +12,73% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 27 | 48,15% | +9,05% | -4,78% | -2,30% | +12,83% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 56 | 94,64% | +12,92% | +12,15% | -2,90% | +16,90% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 59 | 91,53% | +12,86% | +12,86% | -2,88% | +16,97% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 59 | 91,53% | +12,86% | +12,86% | -2,88% | +16,97% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 54 | 61,11% | +12,87% | +0,54% | -2,73% | +17,17% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,37% | -2,02% | -2,62% | +17,60% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 41 | 92,68% | +24,03% | +20,80% | -2,14% | +28,65% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 44 | 100,00% | +24,23% | +24,23% | -2,16% | +28,73% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 44 | 100,00% | +24,23% | +24,23% | -2,16% | +28,73% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 39 | 43,59% | +24,64% | -3,52% | -1,87% | +29,17% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 12 | 33,33% | +22,87% | -13,31% | -0,54% | +28,67% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +15,41% | +15,41% | -2,41% | +20,63% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 29 | 89,66% | +27,83% | +22,66% | -2,94% | +32,69% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 31 | 100,00% | +27,62% | +27,62% | -2,98% | +32,56% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 31 | 100,00% | +27,62% | +27,62% | -2,98% | +32,56% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 27 | 100,00% | +28,36% | +28,36% | -2,76% | +33,49% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 26 | 34,62% | +28,02% | -9,41% | -2,70% | +33,12% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 4 | 0,00% | +33,67% | -33,67% | -1,55% | +38,08% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 76 | 46,05% | +0,13% | -0,07% | -0,66% | +1,18% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 81 | 58,02% | +0,08% | +0,52% | -0,69% | +1,09% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 81 | 58,02% | +0,08% | +0,52% | -0,69% | +1,09% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 75 | 49,33% | -0,00% | +0,06% | -0,80% | +1,00% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 44 | 38,64% | +0,01% | -0,74% | -0,85% | +0,76% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 75 | 44,00% | +0,50% | -0,20% | -0,62% | +1,89% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 80 | 57,50% | +0,32% | +0,76% | -0,77% | +1,66% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 80 | 57,50% | +0,32% | +0,76% | -0,77% | +1,66% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 74 | 52,70% | +0,02% | +0,08% | -1,08% | +1,35% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 44 | 40,91% | +0,32% | -1,41% | -0,90% | +1,29% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 75 | 38,67% | +0,82% | -0,07% | -2,24% | +3,96% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 79 | 55,70% | +0,64% | +1,00% | -2,34% | +3,70% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 79 | 55,70% | +0,64% | +1,00% | -2,34% | +3,70% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 73 | 43,84% | +0,01% | -0,05% | -2,58% | +3,01% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 44 | 29,55% | +0,62% | -2,34% | -2,62% | +3,83% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 74 | 43,24% | +1,62% | -0,06% | -3,31% | +6,33% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 77 | 51,95% | +1,53% | +1,37% | -3,34% | +6,13% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 77 | 51,95% | +1,53% | +1,37% | -3,34% | +6,13% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 71 | 50,70% | +0,73% | -0,73% | -3,72% | +5,37% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 44 | 31,82% | +1,94% | -4,85% | -3,72% | +6,77% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 73 | 47,95% | +2,39% | +0,25% | -3,84% | +8,33% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 76 | 55,26% | +2,42% | +1,41% | -3,86% | +8,16% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 76 | 55,26% | +2,42% | +1,41% | -3,86% | +8,16% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 70 | 45,71% | +1,46% | -1,03% | -4,31% | +7,17% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 43 | 27,91% | +3,41% | -6,38% | -4,15% | +8,99% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 70 | 42,86% | +3,16% | +0,18% | -4,55% | +10,37% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 73 | 52,05% | +3,09% | +1,14% | -4,54% | +10,21% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 73 | 52,05% | +3,09% | +1,14% | -4,54% | +10,21% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 67 | 47,76% | +1,79% | -1,53% | -5,07% | +8,71% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 43 | 30,23% | +3,70% | -7,04% | -4,91% | +11,04% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 67 | 56,72% | +5,29% | +3,31% | -5,03% | +14,26% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 70 | 61,43% | +4,91% | +2,77% | -5,00% | +13,86% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 70 | 61,43% | +4,91% | +2,77% | -5,00% | +13,86% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 64 | 50,00% | +2,88% | -0,99% | -5,60% | +11,23% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 42 | 40,48% | +4,95% | -5,25% | -5,34% | +13,43% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 64 | 60,94% | +8,47% | +2,68% | -5,26% | +19,39% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 67 | 58,21% | +8,79% | +4,40% | -5,27% | +19,55% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 67 | 58,21% | +8,79% | +4,40% | -5,27% | +19,55% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 61 | 57,38% | +6,80% | -1,86% | -5,95% | +16,65% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 40 | 45,00% | +6,17% | -7,17% | -5,52% | +16,12% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 66,67% | +6,54% | +0,57% | -4,75% | +18,76% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 55 | 74,55% | +12,58% | +5,81% | -5,20% | +25,92% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 58 | 72,41% | +12,83% | +7,87% | -5,20% | +26,41% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 58 | 72,41% | +12,83% | +7,87% | -5,20% | +26,41% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 52 | 63,46% | +11,38% | -2,55% | -6,00% | +24,05% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 33 | 51,52% | +10,30% | -8,05% | -5,60% | +22,19% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 88,89% | +19,48% | +12,44% | -5,48% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 42 | 50,00% | +24,00% | +4,97% | -3,84% | +40,96% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 44 | 61,36% | +23,90% | +9,51% | -3,87% | +40,92% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 44 | 61,36% | +23,90% | +9,51% | -3,87% | +40,92% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 37 | 13,51% | +21,51% | -15,45% | -4,63% | +39,29% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 29 | 3,45% | +23,44% | -23,10% | -4,41% | +40,22% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 83,33% | +29,79% | +15,53% | -2,20% | +41,23% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 29 | 31,03% | +27,13% | -5,89% | -4,67% | +43,71% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 31 | 48,39% | +27,59% | +6,53% | -4,66% | +43,95% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 31 | 48,39% | +27,59% | +6,53% | -4,66% | +43,95% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 29 | 51,72% | +26,76% | +9,71% | -4,72% | +43,64% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 30 | 0,00% | +27,32% | -27,32% | -4,76% | +43,74% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 21 | 0,00% | +25,52% | -25,52% | -5,03% | +42,31% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +42,43% | +17,48% | -1,27% | +51,44% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 74 | 50,00% | +0,35% | +0,26% | -0,38% | +1,23% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 76 | 55,26% | +0,33% | +0,45% | -0,49% | +1,20% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 79 | 54,43% | +0,36% | +0,39% | -0,46% | +1,23% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 74 | 45,95% | +0,33% | -0,05% | -0,55% | +1,18% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 56 | 46,43% | +0,52% | +0,02% | -0,48% | +1,46% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 73 | 47,95% | +1,00% | +0,90% | -0,24% | +2,09% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 75 | 49,33% | +0,88% | +0,68% | -0,48% | +1,83% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 78 | 48,72% | +0,86% | +0,64% | -0,46% | +1,86% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 73 | 42,47% | +0,69% | -0,04% | -0,44% | +1,85% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 55 | 49,09% | +0,78% | +0,34% | -0,48% | +1,87% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 72 | 52,78% | +1,65% | +1,53% | -1,74% | +4,02% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 74 | 51,35% | +1,47% | +1,21% | -1,90% | +3,82% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 77 | 50,65% | +1,43% | +1,15% | -1,87% | +3,81% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 72 | 45,83% | +1,04% | -0,20% | -1,92% | +3,36% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 54 | 50,00% | +1,03% | +0,50% | -1,87% | +3,29% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 70 | 57,14% | +2,93% | +2,86% | -2,45% | +6,37% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 72 | 52,78% | +2,68% | +1,98% | -2,61% | +6,13% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 75 | 52,00% | +2,60% | +1,88% | -2,58% | +6,04% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 70 | 47,14% | +2,27% | -0,47% | -2,65% | +5,53% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 52 | 53,85% | +1,55% | +0,82% | -2,60% | +4,77% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 69 | 62,32% | +4,26% | +4,33% | -2,85% | +8,20% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 71 | 60,56% | +3,95% | +3,03% | -3,01% | +7,93% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 74 | 60,81% | +3,79% | +2,92% | -3,00% | +7,76% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 69 | 42,03% | +2,92% | -1,22% | -3,09% | +6,97% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 51 | 49,02% | +1,55% | +0,89% | -3,09% | +5,59% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 66 | 65,15% | +6,30% | +6,42% | -3,25% | +10,53% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 69 | 66,67% | +5,95% | +5,39% | -3,44% | +10,01% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 72 | 65,28% | +5,69% | +5,17% | -3,44% | +9,75% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 66 | 46,97% | +4,31% | -1,43% | -3,60% | +8,61% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 48 | 52,08% | +1,90% | +1,09% | -3,69% | +6,52% | PRIMA CALIBRAZIONE |

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
