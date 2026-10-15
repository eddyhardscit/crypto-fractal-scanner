# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-15 05:34 UTC

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

Segnali totali salvati: **273**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-15 | BTC | 80.946,10 | -2 | +1 | +1 | 0 | -2 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-15 | DOGE | 0.07966 | -2 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-15 | SOL | 102,12 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-14 | BTC | 83.488,21 | 0 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-14 | DOGE | 0.08470 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-10-14 | SOL | 107,30 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-13 | BTC | 83.581,21 | +1 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-13 | DOGE | 0.08464 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-13 | SOL | 108,05 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-12 | BTC | 83.714,71 | -3 | -1 | -1 | 0 | -1 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-12 | DOGE | 0.08732 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-12 | SOL | 112,31 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 91 | 90 | 89 | 88 | 86 | 84 | 81 | 77 | 71 | 67 | 52 | 37 |
| SOL | 91 | 90 | 89 | 88 | 86 | 84 | 81 | 77 | 71 | 67 | 52 | 37 |
| DOGE | 91 | 90 | 89 | 88 | 86 | 84 | 81 | 77 | 71 | 67 | 52 | 37 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-17 | 60g | 2026-10-16 | domani |
| SOL | 2026-08-17 | 60g | 2026-10-16 | domani |
| DOGE | 2026-08-17 | 60g | 2026-10-16 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 80 | 52,50% | +0,30% | +0,29% | UTILE |
| BTC | 2g | 80 | 51,25% | +0,51% | +0,46% | UTILE |
| BTC | 3g | 79 | 46,84% | +0,64% | +0,64% | UTILE |
| BTC | 5g | 78 | 43,59% | +1,42% | +1,25% | UTILE |
| BTC | 7g | 78 | 51,28% | +2,07% | +1,93% | UTILE |
| BTC | 10g | 76 | 56,58% | +2,98% | +2,86% | UTILE |
| BTC | 14g | 72 | 62,50% | +4,67% | +4,62% | UTILE |
| BTC | 21g | 68 | 72,06% | +8,08% | +7,98% | UTILE |
| BTC | 30g | 64 | 95,31% | +12,11% | +11,44% | UTILE |
| BTC | 45g | 49 | 93,88% | +20,98% | +18,28% | PRIMA CALIBRAZIONE |
| BTC | 60g | 35 | 91,43% | +28,16% | +23,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | 82 | 46,34% | +0,13% | +0,06% | UTILE |
| SOL | 2g | 81 | 44,44% | +0,58% | +0,50% | UTILE |
| SOL | 3g | 80 | 48,75% | +1,04% | +0,93% | UTILE |
| SOL | 5g | 78 | 51,28% | +1,98% | +1,91% | UTILE |
| SOL | 7g | 76 | 56,58% | +3,02% | +3,09% | UTILE |
| SOL | 10g | 73 | 58,90% | +4,88% | +4,98% | UTILE |
| SOL | 14g | 69 | 68,12% | +7,89% | +8,41% | UTILE |
| SOL | 21g | 63 | 80,95% | +14,49% | +13,93% | UTILE |
| SOL | 30g | 60 | 83,33% | +19,64% | +16,34% | UTILE |
| SOL | 45g | 45 | 73,33% | +35,76% | +18,66% | PRIMA CALIBRAZIONE |
| SOL | 60g | 30 | 63,33% | +46,65% | +17,44% | PRIMA CALIBRAZIONE |
| DOGE | 1g | 82 | 48,78% | -0,01% | -0,03% | UTILE |
| DOGE | 2g | 81 | 44,44% | +0,22% | -0,10% | UTILE |
| DOGE | 3g | 80 | 41,25% | +0,52% | +0,16% | UTILE |
| DOGE | 5g | 79 | 46,84% | +1,13% | +0,33% | UTILE |
| DOGE | 7g | 78 | 50,00% | +1,66% | +0,52% | UTILE |
| DOGE | 10g | 75 | 41,33% | +2,40% | -0,13% | UTILE |
| DOGE | 14g | 73 | 52,05% | +4,02% | +2,20% | UTILE |
| DOGE | 21g | 67 | 58,21% | +7,75% | +1,97% | UTILE |
| DOGE | 30g | 63 | 68,25% | +10,90% | +4,91% | UTILE |
| DOGE | 45g | 48 | 45,83% | +20,69% | +4,08% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 35 | 42,86% | +26,15% | -1,20% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 80 | 52,50% | +0,30% | +0,29% | -0,28% | +0,82% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 88 | 48,86% | +0,19% | +0,25% | -0,34% | +0,70% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 88 | 48,86% | +0,19% | +0,25% | -0,34% | +0,70% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 83 | 46,99% | +0,21% | +0,04% | -0,28% | +0,73% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 35 | 42,86% | +0,53% | -0,02% | -0,31% | +1,07% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 80 | 51,25% | +0,51% | +0,46% | -0,27% | +1,20% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 87 | 51,72% | +0,48% | +0,56% | -0,26% | +1,16% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 87 | 51,72% | +0,48% | +0,56% | -0,26% | +1,16% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 82 | 46,34% | +0,47% | +0,05% | -0,17% | +1,14% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 35 | 42,86% | +0,85% | -0,11% | -0,05% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 79 | 46,84% | +0,64% | +0,64% | -1,28% | +2,43% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 86 | 50,00% | +0,80% | +0,87% | -1,32% | +2,49% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 86 | 50,00% | +0,80% | +0,87% | -1,32% | +2,49% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 81 | 39,51% | +0,82% | -0,14% | -1,25% | +2,52% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 35 | 37,14% | +1,31% | -0,55% | -1,15% | +3,03% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 78 | 43,59% | +1,42% | +1,25% | -1,91% | +3,84% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 84 | 47,62% | +1,57% | +1,60% | -1,90% | +3,94% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 84 | 47,62% | +1,57% | +1,60% | -1,90% | +3,94% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 79 | 41,77% | +1,44% | -0,71% | -1,86% | +3,88% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 34 | 35,29% | +3,06% | -2,33% | -1,68% | +5,50% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 78 | 51,28% | +2,07% | +1,93% | -2,28% | +4,92% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 82 | 57,32% | +2,29% | +2,36% | -2,25% | +5,04% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 82 | 57,32% | +2,29% | +2,36% | -2,25% | +5,04% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 77 | 42,86% | +2,25% | -1,06% | -2,22% | +5,01% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 34 | 32,35% | +4,23% | -3,81% | -2,10% | +7,38% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 76 | 56,58% | +2,98% | +2,86% | -2,57% | +6,12% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 79 | 65,82% | +3,17% | +3,31% | -2,48% | +6,29% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 79 | 65,82% | +3,17% | +3,31% | -2,48% | +6,29% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 74 | 45,95% | +3,14% | -0,45% | -2,49% | +6,33% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 33 | 36,36% | +4,54% | -4,21% | -2,21% | +8,23% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -1,47% | -1,47% | -4,23% | +1,69% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 72 | 62,50% | +4,67% | +4,62% | -2,66% | +8,35% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 76 | 60,53% | +4,65% | +4,69% | -2,68% | +8,37% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 76 | 60,53% | +4,65% | +4,69% | -2,68% | +8,37% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 70 | 57,14% | +4,83% | +1,37% | -2,65% | +8,60% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 29 | 24,14% | +5,09% | -4,15% | -1,91% | +9,57% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,11% | -0,11% | -4,30% | +2,85% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 68 | 72,06% | +8,08% | +7,98% | -2,91% | +11,95% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 71 | 76,06% | +8,03% | +8,03% | -2,89% | +11,92% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 71 | 76,06% | +8,03% | +8,03% | -2,89% | +11,92% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 64 | 56,25% | +8,48% | +1,36% | -2,86% | +12,38% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 29 | 44,83% | +8,60% | -4,88% | -2,40% | +12,46% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 64 | 95,31% | +12,11% | +11,44% | -3,00% | +16,32% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 67 | 92,54% | +12,09% | +12,09% | -2,97% | +16,41% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 67 | 92,54% | +12,09% | +12,09% | -2,97% | +16,41% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 62 | 66,13% | +12,05% | +1,30% | -2,85% | +16,53% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 26 | 61,54% | +12,81% | -2,34% | -2,66% | +17,23% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 49 | 93,88% | +20,98% | +18,28% | -2,55% | +25,79% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 52 | 100,00% | +21,33% | +21,33% | -2,55% | +26,03% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 52 | 100,00% | +21,33% | +21,33% | -2,55% | +26,03% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 47 | 53,19% | +21,37% | -2,00% | -2,34% | +26,10% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 20 | 60,00% | +15,88% | -5,83% | -2,18% | +21,66% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 35 | 91,43% | +28,16% | +23,87% | -2,74% | +33,44% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 37 | 100,00% | +27,96% | +27,96% | -2,79% | +33,29% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 37 | 100,00% | +27,96% | +27,96% | -2,79% | +33,29% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 33 | 100,00% | +28,61% | +28,61% | -2,58% | +34,15% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 32 | 37,50% | +28,34% | -7,95% | -2,53% | +33,87% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 7 | 0,00% | +32,68% | -32,68% | -1,07% | +38,39% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 82 | 48,78% | -0,01% | -0,03% | -0,80% | +1,04% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 89 | 58,43% | -0,06% | +0,46% | -0,89% | +0,93% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 89 | 58,43% | -0,06% | +0,46% | -0,89% | +0,93% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 83 | 50,60% | -0,15% | +0,20% | -1,00% | +0,84% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 50 | 40,00% | -0,06% | -0,58% | -1,00% | +0,64% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 81 | 44,44% | +0,22% | -0,10% | -0,95% | +1,57% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 88 | 57,95% | +0,03% | +0,75% | -1,08% | +1,32% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 88 | 57,95% | +0,03% | +0,75% | -1,08% | +1,32% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 82 | 53,66% | -0,27% | +0,17% | -1,39% | +1,02% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 50 | 44,00% | +0,08% | -1,04% | -1,17% | +1,03% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 80 | 41,25% | +0,52% | +0,16% | -2,55% | +3,71% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 87 | 56,32% | +0,19% | +1,09% | -2,75% | +3,38% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 87 | 56,32% | +0,19% | +1,09% | -2,75% | +3,38% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 81 | 45,68% | -0,41% | -0,06% | -3,00% | +2,74% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 49 | 34,69% | +0,31% | -1,86% | -2,85% | +3,50% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 79 | 46,84% | +1,13% | +0,33% | -3,70% | +5,98% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 85 | 54,12% | +0,82% | +1,60% | -3,91% | +5,70% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 85 | 54,12% | +0,82% | +1,60% | -3,91% | +5,70% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 79 | 50,63% | +0,05% | -0,88% | -4,30% | +4,99% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 47 | 36,17% | +1,56% | -4,28% | -3,91% | +6,43% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 78 | 50,00% | +1,66% | +0,52% | -4,37% | +7,84% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 83 | 59,04% | +1,48% | +2,03% | -4,59% | +7,59% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 83 | 59,04% | +1,48% | +2,03% | -4,59% | +7,59% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 77 | 44,16% | +0,53% | -1,32% | -5,05% | +6,65% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 45 | 28,89% | +2,80% | -6,15% | -4,47% | +8,62% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 75 | 41,33% | +2,40% | -0,13% | -5,03% | +9,93% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 80 | 56,25% | +2,00% | +1,86% | -5,24% | +9,63% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 80 | 56,25% | +2,00% | +1,86% | -5,24% | +9,63% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 74 | 43,24% | +0,74% | -2,27% | -5,78% | +8,22% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 44 | 29,55% | +3,40% | -7,10% | -5,16% | +10,81% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 73 | 52,05% | +4,02% | +2,20% | -5,81% | +13,32% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 76 | 64,47% | +3,72% | +3,35% | -5,75% | +12,99% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 76 | 64,47% | +3,72% | +3,35% | -5,75% | +12,99% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 70 | 45,71% | +1,76% | -1,78% | -6,36% | +10,51% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 43 | 39,53% | +4,51% | -5,45% | -5,57% | +13,12% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 67 | 58,21% | +7,75% | +1,97% | -5,60% | +19,02% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 70 | 58,57% | +8,09% | +4,53% | -5,59% | +19,19% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 70 | 58,57% | +8,09% | +4,53% | -5,59% | +19,19% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 64 | 54,69% | +6,13% | -2,39% | -6,26% | +16,39% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 42 | 42,86% | +5,67% | -7,44% | -5,73% | +16,02% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +4,84% | -0,04% | -5,47% | +18,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 63 | 68,25% | +10,90% | +4,91% | -5,62% | +25,54% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 66 | 69,70% | +11,19% | +7,00% | -5,59% | +25,99% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 66 | 69,70% | +11,19% | +7,00% | -5,59% | +25,99% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 60 | 58,33% | +9,77% | -2,39% | -6,33% | +23,90% | UTILE |
| DOGE | 30g | Classic technical | CALIBRABILE | 39 | 48,72% | +8,70% | -6,93% | -5,92% | +22,47% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 88,89% | +19,48% | +12,44% | -5,48% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 48 | 45,83% | +20,69% | +4,08% | -4,71% | +38,32% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 51 | 62,75% | +20,25% | +8,08% | -4,73% | +38,14% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 51 | 62,75% | +20,25% | +8,08% | -4,73% | +38,14% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 45 | 11,11% | +17,26% | -13,13% | -5,59% | +36,00% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 31 | 3,23% | +21,52% | -22,01% | -5,10% | +38,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +21,73% | +11,03% | -4,45% | +35,73% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 35 | 42,86% | +26,15% | -1,20% | -4,03% | +44,93% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 37 | 56,76% | +26,59% | +8,95% | -4,05% | +45,07% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 37 | 56,76% | +26,59% | +8,95% | -4,05% | +45,07% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +25,85% | +11,72% | -4,07% | +44,87% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 32 | 6,25% | +26,71% | -24,52% | -4,51% | +44,17% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 24 | 0,00% | +24,90% | -24,90% | -4,47% | +43,41% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +38,20% | +19,48% | -1,31% | +51,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 82 | 46,34% | +0,13% | +0,06% | -0,65% | +1,00% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 84 | 53,57% | +0,12% | +0,40% | -0,74% | +0,98% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 87 | 52,87% | +0,16% | +0,34% | -0,71% | +1,01% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 82 | 46,34% | +0,11% | -0,05% | -0,80% | +0,95% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 58 | 44,83% | +0,45% | -0,03% | -0,53% | +1,39% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 81 | 44,44% | +0,58% | +0,50% | -0,66% | +1,64% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 83 | 49,40% | +0,49% | +0,68% | -0,87% | +1,41% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 86 | 48,84% | +0,48% | +0,64% | -0,84% | +1,46% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 81 | 44,44% | +0,31% | -0,05% | -0,84% | +1,42% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 58 | 48,28% | +0,59% | +0,18% | -0,66% | +1,66% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 80 | 48,75% | +1,04% | +0,93% | -2,22% | +3,64% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 82 | 52,44% | +0,89% | +1,25% | -2,35% | +3,47% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 85 | 51,76% | +0,87% | +1,19% | -2,31% | +3,47% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 80 | 43,75% | +0,49% | -0,38% | -2,38% | +3,05% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 58 | 46,55% | +0,60% | +0,10% | -2,28% | +3,11% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 78 | 51,28% | +1,98% | +1,91% | -3,12% | +5,79% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 80 | 55,00% | +1,78% | +2,17% | -3,24% | +5,59% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 83 | 54,22% | +1,74% | +2,07% | -3,20% | +5,53% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 78 | 43,59% | +1,38% | -1,00% | -3,30% | +5,04% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 58 | 48,28% | +0,68% | +0,02% | -3,30% | +4,39% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 76 | 56,58% | +3,02% | +3,09% | -3,69% | +7,46% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 78 | 64,10% | +2,77% | +3,59% | -3,82% | +7,23% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 81 | 64,20% | +2,67% | +3,46% | -3,78% | +7,11% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 76 | 38,16% | +1,81% | -1,96% | -3,91% | +6,35% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 57 | 43,86% | +0,46% | -0,12% | -4,03% | +5,07% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 73 | 58,90% | +4,88% | +4,98% | -4,00% | +9,76% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 75 | 69,33% | +4,70% | +5,72% | -4,15% | +9,38% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 78 | 67,95% | +4,52% | +5,51% | -4,12% | +9,17% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 73 | 42,47% | +3,07% | -2,12% | -4,32% | +8,03% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 55 | 45,45% | +0,57% | -0,14% | -4,63% | +6,00% | PRIMA CALIBRAZIONE |

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
