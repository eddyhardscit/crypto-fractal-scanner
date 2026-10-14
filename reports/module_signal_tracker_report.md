# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-14 05:33 UTC

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

Segnali totali salvati: **270**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-14 | BTC | 83.488,21 | 0 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-14 | DOGE | 0.08470 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-10-14 | SOL | 107,30 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-13 | BTC | 83.581,21 | +1 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-13 | DOGE | 0.08464 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-13 | SOL | 108,05 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-12 | BTC | 83.714,71 | -3 | -1 | -1 | 0 | -1 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-12 | DOGE | 0.08732 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-12 | SOL | 112,31 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-11 | BTC | 83.006,99 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-11 | DOGE | 0.08535 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-11 | SOL | 109,56 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 90 | 89 | 88 | 87 | 85 | 83 | 80 | 77 | 71 | 66 | 51 | 36 |
| SOL | 90 | 89 | 88 | 87 | 85 | 83 | 80 | 77 | 71 | 66 | 51 | 36 |
| DOGE | 90 | 89 | 88 | 87 | 85 | 83 | 80 | 77 | 71 | 66 | 51 | 36 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-16 | 60g | 2026-10-15 | domani |
| SOL | 2026-08-16 | 60g | 2026-10-15 | domani |
| DOGE | 2026-08-16 | 60g | 2026-10-15 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 80 | 52,50% | +0,30% | +0,29% | UTILE |
| BTC | 2g | 79 | 51,90% | +0,55% | +0,50% | UTILE |
| BTC | 3g | 78 | 46,15% | +0,69% | +0,60% | UTILE |
| BTC | 5g | 78 | 43,59% | +1,42% | +1,25% | UTILE |
| BTC | 7g | 77 | 51,95% | +2,13% | +1,99% | UTILE |
| BTC | 10g | 75 | 57,33% | +3,09% | +2,97% | UTILE |
| BTC | 14g | 72 | 62,50% | +4,67% | +4,62% | UTILE |
| BTC | 21g | 68 | 72,06% | +8,08% | +7,98% | UTILE |
| BTC | 30g | 63 | 95,24% | +12,23% | +11,55% | UTILE |
| BTC | 45g | 48 | 93,75% | +21,34% | +18,59% | PRIMA CALIBRAZIONE |
| BTC | 60g | 34 | 91,18% | +28,15% | +23,74% | PRIMA CALIBRAZIONE |
| SOL | 1g | 81 | 46,91% | +0,19% | +0,12% | UTILE |
| SOL | 2g | 80 | 45,00% | +0,66% | +0,57% | UTILE |
| SOL | 3g | 79 | 49,37% | +1,17% | +1,06% | UTILE |
| SOL | 5g | 77 | 51,95% | +2,10% | +2,03% | UTILE |
| SOL | 7g | 75 | 57,33% | +3,21% | +3,28% | UTILE |
| SOL | 10g | 72 | 59,72% | +5,15% | +5,26% | UTILE |
| SOL | 14g | 69 | 68,12% | +7,89% | +8,41% | UTILE |
| SOL | 21g | 63 | 80,95% | +14,49% | +13,93% | UTILE |
| SOL | 30g | 59 | 83,05% | +19,95% | +16,60% | PRIMA CALIBRAZIONE |
| SOL | 45g | 44 | 75,00% | +36,59% | +19,09% | PRIMA CALIBRAZIONE |
| SOL | 60g | 29 | 62,07% | +47,03% | +16,81% | FEEDBACK RAPIDO |
| DOGE | 1g | 81 | 49,38% | +0,06% | +0,05% | UTILE |
| DOGE | 2g | 80 | 45,00% | +0,29% | -0,03% | UTILE |
| DOGE | 3g | 80 | 41,25% | +0,52% | +0,16% | UTILE |
| DOGE | 5g | 78 | 46,15% | +1,25% | +0,24% | UTILE |
| DOGE | 7g | 77 | 49,35% | +1,80% | +0,40% | UTILE |
| DOGE | 10g | 75 | 41,33% | +2,40% | -0,13% | UTILE |
| DOGE | 14g | 73 | 52,05% | +4,02% | +2,20% | UTILE |
| DOGE | 21g | 67 | 58,21% | +7,75% | +1,97% | UTILE |
| DOGE | 30g | 62 | 67,74% | +11,14% | +4,93% | UTILE |
| DOGE | 45g | 48 | 45,83% | +20,69% | +4,08% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 34 | 41,18% | +26,50% | -1,66% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 80 | 52,50% | +0,30% | +0,29% | -0,28% | +0,82% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 87 | 49,43% | +0,23% | +0,29% | -0,30% | +0,73% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 87 | 49,43% | +0,23% | +0,29% | -0,30% | +0,73% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 82 | 46,34% | +0,25% | +0,01% | -0,25% | +0,77% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 35 | 42,86% | +0,53% | -0,02% | -0,31% | +1,07% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 79 | 51,90% | +0,55% | +0,50% | -0,23% | +1,24% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 86 | 52,33% | +0,52% | +0,61% | -0,22% | +1,20% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 86 | 52,33% | +0,52% | +0,61% | -0,22% | +1,20% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 81 | 45,68% | +0,51% | +0,01% | -0,13% | +1,18% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 35 | 42,86% | +0,85% | -0,11% | -0,05% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 78 | 46,15% | +0,69% | +0,60% | -1,25% | +2,46% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 85 | 49,41% | +0,85% | +0,84% | -1,29% | +2,52% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 85 | 49,41% | +0,85% | +0,84% | -1,29% | +2,52% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 80 | 38,75% | +0,87% | -0,19% | -1,22% | +2,54% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,44% | -0,66% | -1,08% | +3,10% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 78 | 43,59% | +1,42% | +1,25% | -1,91% | +3,84% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 83 | 46,99% | +1,62% | +1,60% | -1,89% | +3,96% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 83 | 46,99% | +1,62% | +1,60% | -1,89% | +3,96% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 78 | 42,31% | +1,48% | -0,69% | -1,85% | +3,90% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 34 | 35,29% | +3,06% | -2,33% | -1,68% | +5,50% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 77 | 51,95% | +2,13% | +1,99% | -2,27% | +4,96% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 81 | 56,79% | +2,35% | +2,36% | -2,24% | +5,09% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 81 | 56,79% | +2,35% | +2,36% | -2,24% | +5,09% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 76 | 43,42% | +2,31% | -1,05% | -2,22% | +5,05% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 34 | 32,35% | +4,23% | -3,81% | -2,10% | +7,38% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 75 | 57,33% | +3,09% | +2,97% | -2,52% | +6,18% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 78 | 65,38% | +3,28% | +3,29% | -2,44% | +6,35% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 78 | 65,38% | +3,28% | +3,29% | -2,44% | +6,35% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 73 | 46,58% | +3,26% | -0,39% | -2,44% | +6,39% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 32 | 37,50% | +4,84% | -4,17% | -2,09% | +8,44% | PRIMA CALIBRAZIONE |
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
| BTC | 30g | Global confluence | BENCHMARK | 63 | 95,24% | +12,23% | +11,55% | -3,00% | +16,38% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 66 | 92,42% | +12,21% | +12,21% | -2,97% | +16,46% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 66 | 92,42% | +12,21% | +12,21% | -2,97% | +16,46% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 61 | 65,57% | +12,17% | +1,25% | -2,85% | +16,59% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 25 | 64,00% | +13,14% | -2,25% | -2,64% | +17,41% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 48 | 93,75% | +21,34% | +18,59% | -2,52% | +26,08% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 51 | 100,00% | +21,67% | +21,67% | -2,52% | +26,30% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 51 | 100,00% | +21,67% | +21,67% | -2,52% | +26,30% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 46 | 52,17% | +21,75% | -2,13% | -2,31% | +26,41% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 19 | 57,89% | +16,51% | -6,34% | -2,09% | +22,16% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 34 | 91,18% | +28,15% | +23,74% | -2,81% | +33,29% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 36 | 100,00% | +27,95% | +27,95% | -2,85% | +33,15% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 36 | 100,00% | +27,95% | +27,95% | -2,85% | +33,15% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 32 | 100,00% | +28,61% | +28,61% | -2,65% | +34,01% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 31 | 38,71% | +28,33% | -7,29% | -2,59% | +33,71% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 6 | 0,00% | +33,38% | -33,38% | -1,17% | +38,35% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 81 | 49,38% | +0,06% | +0,05% | -0,73% | +1,10% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 88 | 59,09% | +0,00% | +0,53% | -0,83% | +0,98% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 88 | 59,09% | +0,00% | +0,53% | -0,83% | +0,98% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 82 | 50,00% | -0,08% | +0,13% | -0,94% | +0,89% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 50 | 40,00% | -0,06% | -0,58% | -1,00% | +0,64% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 80 | 45,00% | +0,29% | -0,03% | -0,88% | +1,63% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 87 | 58,62% | +0,10% | +0,83% | -1,02% | +1,37% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 87 | 58,62% | +0,10% | +0,83% | -1,02% | +1,37% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 81 | 53,09% | -0,20% | +0,10% | -1,33% | +1,07% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 49 | 42,86% | +0,20% | -1,18% | -1,06% | +1,11% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 80 | 41,25% | +0,52% | +0,16% | -2,55% | +3,71% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 86 | 56,98% | +0,30% | +1,20% | -2,67% | +3,45% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 86 | 56,98% | +0,30% | +1,20% | -2,67% | +3,45% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 80 | 45,00% | -0,30% | -0,17% | -2,92% | +2,81% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 48 | 33,33% | +0,50% | -2,08% | -2,72% | +3,62% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 78 | 46,15% | +1,25% | +0,24% | -3,64% | +6,04% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 84 | 54,76% | +0,92% | +1,72% | -3,86% | +5,75% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 84 | 54,76% | +0,92% | +1,72% | -3,86% | +5,75% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 78 | 50,00% | +0,15% | -0,99% | -4,25% | +5,04% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 46 | 34,78% | +1,76% | -4,54% | -3,81% | +6,54% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 77 | 49,35% | +1,80% | +0,40% | -4,30% | +7,94% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 82 | 58,54% | +1,61% | +1,94% | -4,53% | +7,68% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 82 | 58,54% | +1,61% | +1,94% | -4,53% | +7,68% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 76 | 43,42% | +0,66% | -1,46% | -4,99% | +6,73% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 44 | 27,27% | +3,07% | -6,50% | -4,35% | +8,81% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 75 | 41,33% | +2,40% | -0,13% | -5,03% | +9,93% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 79 | 55,70% | +2,23% | +1,68% | -5,10% | +9,73% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 79 | 55,70% | +2,23% | +1,68% | -5,10% | +9,73% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 73 | 43,84% | +0,97% | -2,08% | -5,64% | +8,31% | UTILE |
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
| DOGE | 30g | Global confluence | BENCHMARK | 62 | 67,74% | +11,14% | +4,93% | -5,62% | +25,51% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 65 | 69,23% | +11,42% | +7,05% | -5,60% | +25,97% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 65 | 69,23% | +11,42% | +7,05% | -5,60% | +25,97% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 59 | 57,63% | +10,00% | -2,49% | -6,35% | +23,84% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 38 | 47,37% | +9,03% | -7,21% | -5,94% | +22,34% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 88,89% | +19,48% | +12,44% | -5,48% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 48 | 45,83% | +20,69% | +4,08% | -4,71% | +38,32% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 50 | 62,00% | +20,73% | +8,17% | -4,72% | +38,36% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 50 | 62,00% | +20,73% | +8,17% | -4,72% | +38,36% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 44 | 11,36% | +17,74% | -13,34% | -5,60% | +36,20% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 31 | 3,23% | +21,52% | -22,01% | -5,10% | +38,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +21,73% | +11,03% | -4,45% | +35,73% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 34 | 41,18% | +26,50% | -1,66% | -4,14% | +44,75% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 36 | 55,56% | +26,93% | +8,80% | -4,16% | +44,90% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 36 | 55,56% | +26,93% | +8,80% | -4,16% | +44,90% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 34 | 58,82% | +26,19% | +11,65% | -4,18% | +44,69% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 31 | 3,23% | +27,11% | -25,77% | -4,65% | +43,94% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 23 | 0,00% | +25,36% | -25,36% | -4,66% | +43,08% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +38,20% | +19,48% | -1,31% | +51,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 81 | 46,91% | +0,19% | +0,12% | -0,59% | +1,05% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 83 | 54,22% | +0,18% | +0,46% | -0,69% | +1,02% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 86 | 53,49% | +0,22% | +0,40% | -0,65% | +1,05% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 81 | 45,68% | +0,18% | -0,11% | -0,75% | +1,00% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 58 | 44,83% | +0,45% | -0,03% | -0,53% | +1,39% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 80 | 45,00% | +0,66% | +0,57% | -0,60% | +1,70% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 82 | 50,00% | +0,56% | +0,75% | -0,81% | +1,47% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 85 | 49,41% | +0,55% | +0,71% | -0,78% | +1,51% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 80 | 43,75% | +0,38% | -0,12% | -0,78% | +1,48% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 58 | 48,28% | +0,59% | +0,18% | -0,66% | +1,66% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 79 | 49,37% | +1,17% | +1,06% | -2,13% | +3,72% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 81 | 53,09% | +1,02% | +1,38% | -2,26% | +3,55% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 84 | 52,38% | +0,99% | +1,32% | -2,23% | +3,55% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 79 | 43,04% | +0,61% | -0,50% | -2,29% | +3,12% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 58 | 46,55% | +0,60% | +0,10% | -2,28% | +3,11% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 77 | 51,95% | +2,10% | +2,03% | -3,06% | +5,83% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 79 | 55,70% | +1,89% | +2,29% | -3,19% | +5,62% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 82 | 54,88% | +1,85% | +2,18% | -3,15% | +5,56% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 77 | 44,16% | +1,49% | -0,92% | -3,24% | +5,07% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 57 | 49,12% | +0,81% | +0,14% | -3,23% | +4,42% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 75 | 57,33% | +3,21% | +3,28% | -3,58% | +7,59% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 77 | 63,64% | +2,96% | +3,48% | -3,71% | +7,36% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 80 | 63,75% | +2,85% | +3,36% | -3,68% | +7,23% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 75 | 38,67% | +1,99% | -1,83% | -3,80% | +6,46% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 57 | 43,86% | +0,46% | -0,12% | -4,03% | +5,07% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 72 | 59,72% | +5,15% | +5,26% | -3,85% | +9,88% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 74 | 68,92% | +4,97% | +5,59% | -4,00% | +9,49% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 77 | 67,53% | +4,77% | +5,38% | -3,98% | +9,27% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 72 | 43,06% | +3,32% | -1,94% | -4,17% | +8,12% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 54 | 46,30% | +0,86% | +0,13% | -4,44% | +6,09% | PRIMA CALIBRAZIONE |

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
