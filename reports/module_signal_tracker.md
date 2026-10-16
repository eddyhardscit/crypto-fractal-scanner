# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-16 05:34 UTC

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

Segnali totali salvati: **276**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-16 | BTC | 82.086,63 | +2 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-16 | DOGE | 0.08216 | -1 | +3 | +3 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-16 | SOL | 105,81 | 0 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-15 | BTC | 80.946,10 | -2 | +1 | +1 | 0 | -2 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-15 | DOGE | 0.07966 | -2 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-15 | SOL | 102,12 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-14 | BTC | 83.488,21 | 0 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-14 | DOGE | 0.08470 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-10-14 | SOL | 107,30 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-13 | BTC | 83.581,21 | +1 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-13 | DOGE | 0.08464 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-13 | SOL | 108,05 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 92 | 91 | 90 | 89 | 87 | 85 | 82 | 78 | 72 | 68 | 53 | 38 |
| SOL | 92 | 91 | 90 | 89 | 87 | 85 | 82 | 78 | 72 | 68 | 53 | 38 |
| DOGE | 92 | 91 | 90 | 89 | 87 | 85 | 82 | 78 | 72 | 68 | 53 | 38 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-18 | 60g | 2026-10-17 | domani |
| SOL | 2026-08-18 | 60g | 2026-10-17 | domani |
| DOGE | 2026-08-18 | 60g | 2026-10-17 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 81 | 51,85% | +0,31% | +0,27% | UTILE |
| BTC | 2g | 80 | 51,25% | +0,51% | +0,46% | UTILE |
| BTC | 3g | 80 | 46,25% | +0,61% | +0,61% | UTILE |
| BTC | 5g | 78 | 43,59% | +1,42% | +1,25% | UTILE |
| BTC | 7g | 78 | 51,28% | +2,07% | +1,93% | UTILE |
| BTC | 10g | 77 | 55,84% | +2,89% | +2,77% | UTILE |
| BTC | 14g | 73 | 61,64% | +4,53% | +4,49% | UTILE |
| BTC | 21g | 69 | 71,01% | +7,93% | +7,83% | UTILE |
| BTC | 30g | 65 | 95,38% | +12,05% | +11,39% | UTILE |
| BTC | 45g | 50 | 94,00% | +20,64% | +18,00% | PRIMA CALIBRAZIONE |
| BTC | 60g | 36 | 91,67% | +28,20% | +24,03% | PRIMA CALIBRAZIONE |
| SOL | 1g | 83 | 46,99% | +0,18% | +0,10% | UTILE |
| SOL | 2g | 82 | 43,90% | +0,56% | +0,47% | UTILE |
| SOL | 3g | 81 | 48,15% | +1,00% | +0,89% | UTILE |
| SOL | 5g | 79 | 50,63% | +1,91% | +1,84% | UTILE |
| SOL | 7g | 77 | 55,84% | +2,92% | +2,99% | UTILE |
| SOL | 10g | 74 | 58,11% | +4,65% | +4,75% | UTILE |
| SOL | 14g | 70 | 67,14% | +7,59% | +8,11% | UTILE |
| SOL | 21g | 64 | 79,69% | +14,06% | +13,50% | UTILE |
| SOL | 30g | 61 | 83,61% | +19,46% | +16,22% | UTILE |
| SOL | 45g | 46 | 73,91% | +35,02% | +18,29% | PRIMA CALIBRAZIONE |
| SOL | 60g | 31 | 64,52% | +46,45% | +18,17% | PRIMA CALIBRAZIONE |
| DOGE | 1g | 83 | 48,19% | +0,03% | -0,06% | UTILE |
| DOGE | 2g | 82 | 43,90% | +0,18% | -0,14% | UTILE |
| DOGE | 3g | 81 | 40,74% | +0,48% | +0,12% | UTILE |
| DOGE | 5g | 80 | 46,25% | +1,07% | +0,28% | UTILE |
| DOGE | 7g | 78 | 50,00% | +1,66% | +0,52% | UTILE |
| DOGE | 10g | 76 | 42,11% | +2,19% | +0,04% | UTILE |
| DOGE | 14g | 74 | 51,35% | +3,76% | +1,97% | UTILE |
| DOGE | 21g | 68 | 57,35% | +7,39% | +1,69% | UTILE |
| DOGE | 30g | 64 | 67,19% | +10,77% | +4,79% | UTILE |
| DOGE | 45g | 49 | 46,94% | +20,24% | +4,03% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 36 | 44,44% | +25,90% | -0,69% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 81 | 51,85% | +0,31% | +0,27% | -0,27% | +0,83% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 89 | 49,44% | +0,21% | +0,26% | -0,32% | +0,71% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 89 | 49,44% | +0,21% | +0,26% | -0,32% | +0,71% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 84 | 46,43% | +0,23% | +0,03% | -0,27% | +0,75% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,55% | -0,06% | -0,27% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 80 | 51,25% | +0,51% | +0,46% | -0,27% | +1,20% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 88 | 51,14% | +0,45% | +0,54% | -0,28% | +1,13% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 88 | 51,14% | +0,45% | +0,54% | -0,28% | +1,13% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 83 | 46,99% | +0,44% | +0,07% | -0,20% | +1,11% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 35 | 42,86% | +0,85% | -0,11% | -0,05% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 80 | 46,25% | +0,61% | +0,61% | -1,30% | +2,41% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 87 | 49,43% | +0,77% | +0,84% | -1,33% | +2,47% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 87 | 49,43% | +0,77% | +0,84% | -1,33% | +2,47% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 82 | 40,24% | +0,78% | -0,12% | -1,26% | +2,49% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 35 | 37,14% | +1,31% | -0,55% | -1,15% | +3,03% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 78 | 43,59% | +1,42% | +1,25% | -1,91% | +3,84% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 85 | 48,24% | +1,54% | +1,60% | -1,91% | +3,91% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 85 | 48,24% | +1,54% | +1,60% | -1,91% | +3,91% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 80 | 41,25% | +1,41% | -0,71% | -1,86% | +3,85% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 34 | 35,29% | +3,06% | -2,33% | -1,68% | +5,50% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 78 | 51,28% | +2,07% | +1,93% | -2,28% | +4,92% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 83 | 57,83% | +2,26% | +2,33% | -2,24% | +5,01% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 83 | 57,83% | +2,26% | +2,33% | -2,24% | +5,01% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 78 | 42,31% | +2,21% | -1,05% | -2,22% | +4,97% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 34 | 32,35% | +4,23% | -3,81% | -2,10% | +7,38% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 77 | 55,84% | +2,89% | +2,77% | -2,62% | +6,04% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 80 | 66,25% | +3,08% | +3,32% | -2,53% | +6,21% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 80 | 66,25% | +3,08% | +3,32% | -2,53% | +6,21% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 75 | 45,33% | +3,04% | -0,50% | -2,54% | +6,24% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 34 | 35,29% | +4,28% | -4,21% | -2,33% | +7,98% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -1,47% | -1,47% | -4,23% | +1,69% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 73 | 61,64% | +4,53% | +4,49% | -2,73% | +8,24% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 77 | 59,74% | +4,52% | +4,56% | -2,74% | +8,26% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 77 | 59,74% | +4,52% | +4,56% | -2,74% | +8,26% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 71 | 56,34% | +4,69% | +1,28% | -2,71% | +8,49% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 30 | 23,33% | +4,74% | -4,19% | -2,08% | +9,27% | PRIMA CALIBRAZIONE |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,75% | -0,75% | -4,66% | +2,55% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 69 | 71,01% | +7,93% | +7,83% | -2,93% | +11,83% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 72 | 75,00% | +7,88% | +7,88% | -2,91% | +11,80% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 72 | 75,00% | +7,88% | +7,88% | -2,91% | +11,80% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 65 | 55,38% | +8,31% | +1,30% | -2,88% | +12,24% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 29 | 44,83% | +8,60% | -4,88% | -2,40% | +12,46% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 65 | 95,38% | +12,05% | +11,39% | -2,95% | +16,30% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 68 | 92,65% | +12,04% | +12,04% | -2,93% | +16,39% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 68 | 92,65% | +12,04% | +12,04% | -2,93% | +16,39% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 62 | 66,13% | +12,05% | +1,30% | -2,85% | +16,53% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 27 | 59,26% | +12,64% | -2,56% | -2,56% | +17,16% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 50 | 94,00% | +20,64% | +18,00% | -2,60% | +25,49% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 53 | 100,00% | +21,00% | +21,00% | -2,60% | +25,74% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 53 | 100,00% | +21,00% | +21,00% | -2,60% | +25,74% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 48 | 54,17% | +21,00% | -1,88% | -2,40% | +25,78% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 21 | 61,90% | +15,31% | -5,37% | -2,33% | +21,13% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 36 | 91,67% | +28,20% | +24,03% | -2,64% | +33,56% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 38 | 100,00% | +28,00% | +28,00% | -2,69% | +33,41% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 38 | 100,00% | +28,00% | +28,00% | -2,69% | +33,41% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 34 | 100,00% | +28,63% | +28,63% | -2,48% | +34,25% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 33 | 36,36% | +28,37% | -8,60% | -2,43% | +33,98% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 8 | 0,00% | +32,27% | -32,27% | -0,83% | +38,31% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 83 | 48,19% | +0,03% | -0,06% | -0,77% | +1,07% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 90 | 58,89% | -0,03% | +0,49% | -0,86% | +0,96% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 90 | 58,89% | -0,03% | +0,49% | -0,86% | +0,96% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 84 | 50,00% | -0,11% | +0,16% | -0,97% | +0,87% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 51 | 39,22% | +0,00% | -0,63% | -0,95% | +0,69% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 82 | 43,90% | +0,18% | -0,14% | -0,99% | +1,51% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 89 | 57,30% | -0,00% | +0,71% | -1,12% | +1,27% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 89 | 57,30% | -0,00% | +0,71% | -1,12% | +1,27% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 83 | 54,22% | -0,30% | +0,20% | -1,43% | +0,97% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 50 | 44,00% | +0,08% | -1,04% | -1,17% | +1,03% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 81 | 40,74% | +0,48% | +0,12% | -2,58% | +3,68% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 88 | 55,68% | +0,16% | +1,04% | -2,77% | +3,35% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 88 | 55,68% | +0,16% | +1,04% | -2,77% | +3,35% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 82 | 46,34% | -0,44% | -0,03% | -3,01% | +2,72% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 50 | 36,00% | +0,25% | -1,76% | -2,88% | +3,45% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 80 | 46,25% | +1,07% | +0,28% | -3,72% | +5,94% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 86 | 53,49% | +0,76% | +1,54% | -3,93% | +5,67% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 86 | 53,49% | +0,76% | +1,54% | -3,93% | +5,67% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 80 | 51,25% | -0,00% | -0,82% | -4,32% | +4,97% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 48 | 37,50% | +1,45% | -4,11% | -3,95% | +6,36% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 78 | 50,00% | +1,66% | +0,52% | -4,37% | +7,84% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 84 | 58,33% | +1,42% | +1,96% | -4,60% | +7,54% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 84 | 58,33% | +1,42% | +1,96% | -4,60% | +7,54% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 78 | 44,87% | +0,48% | -1,26% | -5,06% | +6,60% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 46 | 30,43% | +2,66% | -5,94% | -4,50% | +8,50% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 76 | 42,11% | +2,19% | +0,04% | -5,17% | +9,79% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 81 | 56,79% | +1,81% | +2,00% | -5,37% | +9,50% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 81 | 56,79% | +1,81% | +2,00% | -5,37% | +9,50% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 75 | 42,67% | +0,55% | -2,41% | -5,91% | +8,10% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 44 | 29,55% | +3,40% | -7,10% | -5,16% | +10,81% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 74 | 51,35% | +3,76% | +1,97% | -5,95% | +13,15% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 77 | 64,94% | +3,48% | +3,50% | -5,89% | +12,83% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 77 | 64,94% | +3,48% | +3,50% | -5,89% | +12,83% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 71 | 45,07% | +1,52% | -1,97% | -6,51% | +10,38% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 44 | 38,64% | +4,07% | -5,67% | -5,83% | +12,84% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 68 | 57,35% | +7,39% | +1,69% | -5,79% | +18,75% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 71 | 59,15% | +7,74% | +4,71% | -5,77% | +18,92% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 71 | 59,15% | +7,74% | +4,71% | -5,77% | +18,92% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 65 | 53,85% | +5,77% | -2,62% | -6,45% | +16,14% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 43 | 41,86% | +5,14% | -7,66% | -6,03% | +15,65% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +4,84% | -0,04% | -5,47% | +18,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 64 | 67,19% | +10,77% | +4,79% | -5,52% | +25,63% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 67 | 68,66% | +11,06% | +6,86% | -5,50% | +26,07% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 67 | 68,66% | +11,06% | +6,86% | -5,50% | +26,07% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 61 | 57,38% | +9,66% | -2,39% | -6,22% | +24,02% | UTILE |
| DOGE | 30g | Classic technical | CALIBRABILE | 40 | 47,50% | +8,55% | -6,82% | -5,76% | +22,69% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 88,89% | +19,48% | +12,44% | -5,48% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 49 | 46,94% | +20,24% | +4,03% | -4,73% | +38,07% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 52 | 63,46% | +19,83% | +7,96% | -4,75% | +37,91% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 52 | 63,46% | +19,83% | +7,96% | -4,75% | +37,91% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 46 | 10,87% | +16,85% | -12,88% | -5,60% | +35,79% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 31 | 3,23% | +21,52% | -22,01% | -5,10% | +38,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +21,73% | +11,03% | -4,45% | +35,73% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 36 | 44,44% | +25,90% | -0,69% | -3,93% | +45,08% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 38 | 57,89% | +26,35% | +9,17% | -3,96% | +45,21% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 38 | 57,89% | +26,35% | +9,17% | -3,96% | +45,21% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 36 | 61,11% | +25,61% | +11,88% | -3,98% | +45,02% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 33 | 6,06% | +26,42% | -24,30% | -4,39% | +44,35% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 25 | 0,00% | +24,60% | -24,60% | -4,32% | +43,69% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +38,20% | +19,48% | -1,31% | +51,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 83 | 46,99% | +0,18% | +0,10% | -0,61% | +1,04% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 85 | 54,12% | +0,17% | +0,43% | -0,71% | +1,02% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 88 | 53,41% | +0,20% | +0,38% | -0,67% | +1,04% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 83 | 45,78% | +0,16% | -0,09% | -0,76% | +0,99% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 59 | 44,07% | +0,51% | -0,09% | -0,48% | +1,43% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 82 | 43,90% | +0,56% | +0,47% | -0,69% | +1,60% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 84 | 48,81% | +0,47% | +0,65% | -0,89% | +1,38% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 87 | 48,28% | +0,46% | +0,62% | -0,86% | +1,43% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 82 | 45,12% | +0,29% | -0,04% | -0,86% | +1,39% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 58 | 48,28% | +0,59% | +0,18% | -0,66% | +1,66% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 81 | 48,15% | +1,00% | +0,89% | -2,24% | +3,60% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 83 | 51,81% | +0,86% | +1,21% | -2,37% | +3,43% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 86 | 51,16% | +0,84% | +1,16% | -2,33% | +3,43% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 81 | 44,44% | +0,46% | -0,35% | -2,40% | +3,01% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 58 | 46,55% | +0,60% | +0,10% | -2,28% | +3,11% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 79 | 50,63% | +1,91% | +1,84% | -3,16% | +5,76% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 81 | 54,32% | +1,71% | +2,10% | -3,28% | +5,56% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 84 | 53,57% | +1,68% | +2,00% | -3,24% | +5,50% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 79 | 44,30% | +1,32% | -0,95% | -3,34% | +5,02% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 58 | 48,28% | +0,68% | +0,02% | -3,30% | +4,39% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 77 | 55,84% | +2,92% | +2,99% | -3,74% | +7,40% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 79 | 63,29% | +2,69% | +3,49% | -3,86% | +7,17% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 82 | 63,41% | +2,58% | +3,36% | -3,82% | +7,05% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 77 | 38,96% | +1,73% | -1,88% | -3,95% | +6,29% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 57 | 43,86% | +0,46% | -0,12% | -4,03% | +5,07% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 74 | 58,11% | +4,65% | +4,75% | -4,14% | +9,64% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 76 | 69,74% | +4,49% | +5,80% | -4,28% | +9,27% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 79 | 68,35% | +4,31% | +5,59% | -4,25% | +9,07% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 74 | 41,89% | +2,87% | -2,25% | -4,45% | +7,93% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 56 | 44,64% | +0,35% | -0,35% | -4,81% | +5,91% | PRIMA CALIBRAZIONE |

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
