# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-18 05:33 UTC

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

Segnali totali salvati: **279**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-18 | BTC | 81.614,92 | +3 | +2 | +2 | 0 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-10-18 | DOGE | 0.07904 | -2 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-18 | SOL | 103,34 | -1 | +2 | +2 | 0 | -2 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-10-16 | BTC | 82.086,63 | +2 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-16 | DOGE | 0.08216 | -1 | +3 | +3 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-16 | SOL | 105,81 | 0 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-15 | BTC | 80.946,10 | -2 | +1 | +1 | 0 | -2 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-15 | DOGE | 0.07966 | -2 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-15 | SOL | 102,12 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-14 | BTC | 83.488,21 | 0 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-14 | DOGE | 0.08470 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-10-14 | SOL | 107,30 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 93 | 92 | 92 | 91 | 89 | 87 | 84 | 80 | 74 | 69 | 55 | 40 |
| SOL | 93 | 92 | 92 | 91 | 89 | 87 | 84 | 80 | 74 | 69 | 55 | 40 |
| DOGE | 93 | 92 | 92 | 91 | 89 | 87 | 84 | 80 | 74 | 69 | 55 | 40 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-20 | 60g | 2026-10-19 | domani |
| SOL | 2026-08-20 | 60g | 2026-10-19 | domani |
| DOGE | 2026-08-20 | 60g | 2026-10-19 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 82 | 51,22% | +0,30% | +0,26% | UTILE |
| BTC | 2g | 82 | 50,00% | +0,50% | +0,43% | UTILE |
| BTC | 3g | 81 | 45,68% | +0,62% | +0,59% | UTILE |
| BTC | 5g | 80 | 43,75% | +1,32% | +1,22% | UTILE |
| BTC | 7g | 78 | 51,28% | +2,07% | +1,93% | UTILE |
| BTC | 10g | 78 | 55,13% | +2,83% | +2,71% | UTILE |
| BTC | 14g | 75 | 60,00% | +4,31% | +4,27% | UTILE |
| BTC | 21g | 69 | 71,01% | +7,93% | +7,83% | UTILE |
| BTC | 30g | 66 | 95,45% | +11,98% | +11,32% | UTILE |
| BTC | 45g | 52 | 94,23% | +20,05% | +17,51% | PRIMA CALIBRAZIONE |
| BTC | 60g | 37 | 91,89% | +28,16% | +24,10% | PRIMA CALIBRAZIONE |
| SOL | 1g | 83 | 46,99% | +0,18% | +0,10% | UTILE |
| SOL | 2g | 83 | 44,58% | +0,57% | +0,48% | UTILE |
| SOL | 3g | 83 | 48,19% | +0,95% | +0,84% | UTILE |
| SOL | 5g | 81 | 49,38% | +1,71% | +1,65% | UTILE |
| SOL | 7g | 79 | 54,43% | +2,70% | +2,77% | UTILE |
| SOL | 10g | 76 | 56,58% | +4,22% | +4,32% | UTILE |
| SOL | 14g | 72 | 65,28% | +6,99% | +7,49% | UTILE |
| SOL | 21g | 66 | 77,27% | +13,20% | +12,66% | UTILE |
| SOL | 30g | 61 | 83,61% | +19,46% | +16,22% | UTILE |
| SOL | 45g | 48 | 75,00% | +33,69% | +17,66% | PRIMA CALIBRAZIONE |
| SOL | 60g | 33 | 66,67% | +45,78% | +19,23% | PRIMA CALIBRAZIONE |
| DOGE | 1g | 84 | 48,81% | -0,02% | -0,02% | UTILE |
| DOGE | 2g | 84 | 45,24% | +0,12% | -0,08% | UTILE |
| DOGE | 3g | 83 | 40,96% | +0,37% | +0,05% | UTILE |
| DOGE | 5g | 81 | 45,68% | +0,98% | +0,20% | UTILE |
| DOGE | 7g | 80 | 50,00% | +1,42% | +0,52% | UTILE |
| DOGE | 10g | 78 | 43,59% | +1,85% | +0,33% | UTILE |
| DOGE | 14g | 75 | 52,00% | +3,51% | +2,14% | UTILE |
| DOGE | 21g | 70 | 55,71% | +6,66% | +1,12% | UTILE |
| DOGE | 30g | 65 | 67,69% | +10,57% | +4,75% | UTILE |
| DOGE | 45g | 51 | 49,02% | +19,30% | +4,02% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 38 | 47,37% | +25,24% | +0,04% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 82 | 51,22% | +0,30% | +0,26% | -0,27% | +0,81% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 90 | 48,89% | +0,20% | +0,25% | -0,33% | +0,70% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 90 | 48,89% | +0,20% | +0,25% | -0,33% | +0,70% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 85 | 47,06% | +0,22% | +0,03% | -0,28% | +0,73% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,55% | -0,06% | -0,27% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 82 | 50,00% | +0,50% | +0,43% | -0,28% | +1,19% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 90 | 51,11% | +0,45% | +0,53% | -0,29% | +1,13% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 90 | 51,11% | +0,45% | +0,53% | -0,29% | +1,13% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 85 | 47,06% | +0,43% | +0,06% | -0,21% | +1,11% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,85% | -0,13% | -0,05% | +1,59% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 81 | 45,68% | +0,62% | +0,59% | -1,29% | +2,41% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 89 | 49,44% | +0,74% | +0,81% | -1,35% | +2,43% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 89 | 49,44% | +0,74% | +0,81% | -1,35% | +2,43% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 84 | 40,48% | +0,75% | -0,10% | -1,29% | +2,45% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 36 | 36,11% | +1,29% | -0,55% | -1,13% | +3,01% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 80 | 43,75% | +1,32% | +1,22% | -1,98% | +3,75% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 87 | 48,28% | +1,45% | +1,56% | -1,97% | +3,83% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 87 | 48,28% | +1,45% | +1,56% | -1,97% | +3,83% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 82 | 42,68% | +1,31% | -0,63% | -1,93% | +3,77% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 35 | 37,14% | +2,90% | -2,19% | -1,77% | +5,36% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 78 | 51,28% | +2,07% | +1,93% | -2,28% | +4,92% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 85 | 58,82% | +2,17% | +2,31% | -2,28% | +4,93% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 85 | 58,82% | +2,17% | +2,31% | -2,28% | +4,93% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 80 | 41,25% | +2,12% | -1,06% | -2,26% | +4,89% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 34 | 32,35% | +4,23% | -3,81% | -2,10% | +7,38% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 78 | 55,13% | +2,83% | +2,71% | -2,63% | +5,98% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 82 | 67,07% | +2,95% | +3,30% | -2,58% | +6,08% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 82 | 67,07% | +2,95% | +3,30% | -2,58% | +6,08% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 77 | 44,16% | +2,90% | -0,55% | -2,59% | +6,10% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 34 | 35,29% | +4,28% | -4,21% | -2,33% | +7,98% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -1,47% | -1,47% | -4,23% | +1,69% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 75 | 60,00% | +4,31% | +4,27% | -2,81% | +8,09% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 78 | 60,26% | +4,41% | +4,55% | -2,78% | +8,19% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 78 | 60,26% | +4,41% | +4,55% | -2,78% | +8,19% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 73 | 54,79% | +4,46% | +1,14% | -2,80% | +8,33% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 32 | 21,88% | +4,22% | -4,16% | -2,32% | +8,86% | PRIMA CALIBRAZIONE |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,75% | -0,75% | -4,66% | +2,55% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 69 | 71,01% | +7,93% | +7,83% | -2,93% | +11,83% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 74 | 75,68% | +7,59% | +7,75% | -2,97% | +11,58% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 74 | 75,68% | +7,59% | +7,75% | -2,97% | +11,58% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 67 | 53,73% | +7,97% | +1,17% | -2,95% | +11,98% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 29 | 44,83% | +8,60% | -4,88% | -2,40% | +12,46% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 66 | 95,45% | +11,98% | +11,32% | -2,91% | +16,28% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 69 | 92,75% | +11,96% | +11,96% | -2,89% | +16,36% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 69 | 92,75% | +11,96% | +11,96% | -2,89% | +16,36% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 62 | 66,13% | +12,05% | +1,30% | -2,85% | +16,53% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 28 | 57,14% | +12,44% | -2,72% | -2,47% | +17,06% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 52 | 94,23% | +20,05% | +17,51% | -2,63% | +25,00% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 55 | 100,00% | +20,43% | +20,43% | -2,62% | +25,26% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 55 | 100,00% | +20,43% | +20,43% | -2,62% | +25,26% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 50 | 56,00% | +20,37% | -1,59% | -2,43% | +25,26% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 23 | 65,22% | +14,44% | -4,44% | -2,41% | +20,40% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 37 | 91,89% | +28,16% | +24,10% | -2,38% | +33,63% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 40 | 100,00% | +27,95% | +27,95% | -2,38% | +33,54% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 40 | 100,00% | +27,95% | +27,95% | -2,38% | +33,54% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +28,58% | +28,58% | -2,21% | +34,30% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 35 | 37,14% | +28,30% | -8,12% | -2,09% | +34,10% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 8 | 0,00% | +32,27% | -32,27% | -0,83% | +38,31% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 84 | 48,81% | -0,02% | -0,02% | -0,80% | +1,02% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 91 | 58,24% | -0,07% | +0,44% | -0,89% | +0,92% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 91 | 58,24% | -0,07% | +0,44% | -0,89% | +0,92% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 85 | 50,59% | -0,15% | +0,20% | -1,00% | +0,83% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 52 | 40,38% | -0,07% | -0,55% | -1,01% | +0,63% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 58,33% | +2,27% | +2,00% | +0,38% | +3,14% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 84 | 45,24% | +0,12% | -0,08% | -1,02% | +1,49% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 91 | 56,04% | -0,05% | +0,65% | -1,14% | +1,26% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 91 | 56,04% | -0,05% | +0,65% | -1,14% | +1,26% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 85 | 55,29% | -0,35% | +0,25% | -1,45% | +0,96% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 52 | 46,15% | -0,01% | -0,91% | -1,21% | +1,01% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 41,67% | +2,33% | +2,11% | +0,69% | +4,97% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 83 | 40,96% | +0,37% | +0,05% | -2,61% | +3,61% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 90 | 54,44% | +0,07% | +0,94% | -2,80% | +3,30% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 90 | 54,44% | +0,07% | +0,94% | -2,80% | +3,30% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 84 | 47,62% | -0,52% | +0,06% | -3,04% | +2,67% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 51 | 37,25% | +0,23% | -1,71% | -2,84% | +3,45% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 81 | 45,68% | +0,98% | +0,20% | -3,77% | +5,88% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 88 | 52,27% | +0,56% | +1,32% | -4,05% | +5,53% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 88 | 52,27% | +0,56% | +1,32% | -4,05% | +5,53% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 82 | 52,44% | -0,20% | -0,60% | -4,43% | +4,83% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 50 | 40,00% | +1,07% | -3,63% | -4,14% | +6,08% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 80 | 50,00% | +1,42% | +0,52% | -4,48% | +7,70% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 86 | 56,98% | +1,20% | +1,73% | -4,70% | +7,42% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 86 | 56,98% | +1,20% | +1,73% | -4,70% | +7,42% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 80 | 46,25% | +0,27% | -1,03% | -5,15% | +6,50% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 48 | 33,33% | +2,21% | -5,36% | -4,67% | +8,24% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 78 | 43,59% | +1,85% | +0,33% | -5,34% | +9,53% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 83 | 57,83% | +1,50% | +2,23% | -5,52% | +9,26% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 83 | 57,83% | +1,50% | +2,23% | -5,52% | +9,26% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 77 | 44,16% | +0,24% | -2,06% | -6,07% | +7,88% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 45 | 31,11% | +3,10% | -6,72% | -5,29% | +10,57% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 75 | 52,00% | +3,51% | +2,14% | -6,09% | +13,04% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 79 | 65,82% | +3,01% | +3,79% | -6,14% | +12,62% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 79 | 65,82% | +3,01% | +3,79% | -6,14% | +12,62% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 73 | 43,84% | +1,07% | -2,33% | -6,76% | +10,22% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 44 | 38,64% | +4,07% | -5,67% | -5,83% | +12,84% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 70 | 55,71% | +6,66% | +1,12% | -6,16% | +18,26% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 73 | 60,27% | +7,02% | +5,08% | -6,13% | +18,45% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 73 | 60,27% | +7,02% | +5,08% | -6,13% | +18,45% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 67 | 52,24% | +5,06% | -3,08% | -6,82% | +15,71% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 43 | 41,86% | +5,14% | -7,66% | -6,03% | +15,65% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +4,84% | -0,04% | -5,47% | +18,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 65 | 67,69% | +10,57% | +4,75% | -5,49% | +25,70% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 68 | 69,12% | +10,87% | +6,79% | -5,47% | +26,13% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 68 | 69,12% | +10,87% | +6,79% | -5,47% | +26,13% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 62 | 58,06% | +9,46% | -2,31% | -6,17% | +24,12% | UTILE |
| DOGE | 30g | Classic technical | CALIBRABILE | 41 | 48,78% | +8,28% | -6,60% | -5,70% | +22,87% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 80,00% | +17,31% | +10,98% | -5,24% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 51 | 49,02% | +19,30% | +4,02% | -4,73% | +37,68% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 54 | 64,81% | +18,96% | +7,80% | -4,75% | +37,55% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 54 | 64,81% | +18,96% | +7,80% | -4,75% | +37,55% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 48 | 10,42% | +15,99% | -12,50% | -5,56% | +35,47% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 31 | 3,23% | +21,52% | -22,01% | -5,10% | +38,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +21,73% | +11,03% | -4,45% | +35,73% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 38 | 47,37% | +25,24% | +0,04% | -3,55% | +45,38% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 40 | 60,00% | +25,69% | +9,37% | -3,60% | +45,49% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 40 | 60,00% | +25,69% | +9,37% | -3,60% | +45,49% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +24,96% | +11,95% | -3,59% | +45,33% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 33 | 6,06% | +26,42% | -24,30% | -4,39% | +44,35% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 27 | 0,00% | +23,75% | -23,75% | -3,76% | +44,21% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +38,20% | +19,48% | -1,31% | +51,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 83 | 46,99% | +0,18% | +0,10% | -0,61% | +1,04% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 86 | 53,49% | +0,14% | +0,40% | -0,73% | +0,99% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 89 | 52,81% | +0,17% | +0,35% | -0,69% | +1,02% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 84 | 46,43% | +0,13% | -0,06% | -0,79% | +0,96% | UTILE |
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
| SOL | 3g | Famiglia statistica | CALIBRABILE | 85 | 51,76% | +0,81% | +1,15% | -2,38% | +3,41% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 88 | 51,14% | +0,79% | +1,10% | -2,34% | +3,41% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 83 | 44,58% | +0,42% | -0,31% | -2,41% | +2,99% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 59 | 45,76% | +0,61% | +0,08% | -2,23% | +3,14% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 81 | 49,38% | +1,71% | +1,65% | -3,29% | +5,58% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 83 | 53,01% | +1,52% | +1,90% | -3,40% | +5,39% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 86 | 52,33% | +1,49% | +1,81% | -3,35% | +5,34% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 81 | 45,68% | +1,13% | -0,77% | -3,46% | +4,86% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 58 | 48,28% | +0,68% | +0,02% | -3,30% | +4,39% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 79 | 54,43% | +2,70% | +2,77% | -3,85% | +7,29% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 81 | 61,73% | +2,47% | +3,26% | -3,96% | +7,07% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 84 | 61,90% | +2,38% | +3,14% | -3,92% | +6,96% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 79 | 39,24% | +1,54% | -1,83% | -4,06% | +6,21% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 58 | 43,10% | +0,35% | -0,23% | -4,10% | +5,03% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 76 | 56,58% | +4,22% | +4,32% | -4,40% | +9,33% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 78 | 70,51% | +4,07% | +5,95% | -4,53% | +8,98% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 81 | 69,14% | +3,91% | +5,74% | -4,49% | +8,80% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 76 | 40,79% | +2,49% | -2,50% | -4,70% | +7,67% | UTILE |
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
