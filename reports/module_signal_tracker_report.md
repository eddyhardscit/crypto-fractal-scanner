# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-21 05:34 UTC

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

Segnali totali salvati: **288**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-21 | BTC | 82.805,01 | 0 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-21 | DOGE | 0.08166 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-21 | SOL | 105,96 | +3 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-20 | BTC | 81.867,63 | +2 | +1 | +1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-20 | DOGE | 0.07939 | -1 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-20 | SOL | 104,68 | +3 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-19 | BTC | 82.648,77 | -1 | +1 | +1 | 0 | -1 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-19 | DOGE | 0.07945 | -1 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-19 | SOL | 105,63 | -2 | +1 | +1 | 0 | -2 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-10-18 | BTC | 81.614,92 | +3 | +2 | +2 | 0 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-10-18 | DOGE | 0.07904 | -2 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-18 | SOL | 103,34 | -1 | +2 | +2 | 0 | -2 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 96 | 95 | 94 | 93 | 92 | 90 | 87 | 83 | 77 | 69 | 58 | 43 |
| SOL | 96 | 95 | 94 | 93 | 92 | 90 | 87 | 83 | 77 | 69 | 58 | 43 |
| DOGE | 96 | 95 | 94 | 93 | 92 | 90 | 87 | 83 | 77 | 69 | 58 | 43 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-23 | 60g | 2026-10-22 | domani |
| SOL | 2026-08-23 | 60g | 2026-10-22 | domani |
| DOGE | 2026-08-23 | 60g | 2026-10-22 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 85 | 52,94% | +0,31% | +0,29% | UTILE |
| BTC | 2g | 84 | 50,00% | +0,49% | +0,42% | UTILE |
| BTC | 3g | 83 | 46,99% | +0,63% | +0,60% | UTILE |
| BTC | 5g | 82 | 43,90% | +1,31% | +1,19% | UTILE |
| BTC | 7g | 80 | 51,25% | +1,98% | +1,87% | UTILE |
| BTC | 10g | 78 | 55,13% | +2,83% | +2,71% | UTILE |
| BTC | 14g | 77 | 58,44% | +4,10% | +4,06% | UTILE |
| BTC | 21g | 72 | 68,06% | +7,56% | +7,47% | UTILE |
| BTC | 30g | 66 | 95,45% | +11,98% | +11,32% | UTILE |
| BTC | 45g | 55 | 94,55% | +19,11% | +16,71% | PRIMA CALIBRAZIONE |
| BTC | 60g | 40 | 92,50% | +26,93% | +23,18% | PRIMA CALIBRAZIONE |
| SOL | 1g | 86 | 47,67% | +0,20% | +0,10% | UTILE |
| SOL | 2g | 85 | 43,53% | +0,57% | +0,45% | UTILE |
| SOL | 3g | 84 | 47,62% | +0,97% | +0,80% | UTILE |
| SOL | 5g | 83 | 49,40% | +1,68% | +1,62% | UTILE |
| SOL | 7g | 82 | 52,44% | +2,48% | +2,54% | UTILE |
| SOL | 10g | 79 | 54,43% | +3,90% | +4,00% | UTILE |
| SOL | 14g | 75 | 62,67% | +6,23% | +6,72% | UTILE |
| SOL | 21g | 69 | 73,91% | +12,14% | +11,63% | UTILE |
| SOL | 30g | 61 | 83,61% | +19,46% | +16,22% | UTILE |
| SOL | 45g | 51 | 76,47% | +31,79% | +16,70% | PRIMA CALIBRAZIONE |
| SOL | 60g | 36 | 69,44% | +43,49% | +19,14% | PRIMA CALIBRAZIONE |
| DOGE | 1g | 87 | 48,28% | +0,02% | -0,06% | UTILE |
| DOGE | 2g | 86 | 44,19% | +0,15% | -0,12% | UTILE |
| DOGE | 3g | 85 | 41,18% | +0,37% | +0,05% | UTILE |
| DOGE | 5g | 84 | 46,43% | +0,86% | +0,13% | UTILE |
| DOGE | 7g | 82 | 48,78% | +1,27% | +0,39% | UTILE |
| DOGE | 10g | 80 | 43,75% | +1,65% | +0,37% | UTILE |
| DOGE | 14g | 77 | 53,25% | +3,08% | +2,42% | UTILE |
| DOGE | 21g | 73 | 53,42% | +5,80% | +0,49% | UTILE |
| DOGE | 30g | 65 | 67,69% | +10,57% | +4,75% | UTILE |
| DOGE | 45g | 54 | 50,00% | +17,74% | +3,90% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 41 | 46,34% | +23,22% | -0,13% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 85 | 52,94% | +0,31% | +0,29% | -0,27% | +0,81% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 93 | 49,46% | +0,21% | +0,26% | -0,32% | +0,70% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 93 | 49,46% | +0,21% | +0,26% | -0,32% | +0,70% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 88 | 48,86% | +0,23% | +0,07% | -0,27% | +0,73% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,55% | -0,06% | -0,27% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 84 | 50,00% | +0,49% | +0,42% | -0,28% | +1,18% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 92 | 52,17% | +0,44% | +0,52% | -0,29% | +1,11% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 92 | 52,17% | +0,44% | +0,52% | -0,29% | +1,11% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 87 | 47,13% | +0,43% | +0,06% | -0,21% | +1,10% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,85% | -0,13% | -0,05% | +1,59% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 83 | 46,99% | +0,63% | +0,60% | -1,28% | +2,38% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 91 | 50,55% | +0,75% | +0,81% | -1,34% | +2,41% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 91 | 50,55% | +0,75% | +0,81% | -1,34% | +2,41% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 86 | 40,70% | +0,76% | -0,09% | -1,28% | +2,43% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 36 | 36,11% | +1,29% | -0,55% | -1,13% | +3,01% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 82 | 43,90% | +1,31% | +1,19% | -1,96% | +3,71% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 90 | 48,89% | +1,41% | +1,52% | -1,98% | +3,73% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 90 | 48,89% | +1,41% | +1,52% | -1,98% | +3,73% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 85 | 42,35% | +1,28% | -0,62% | -1,94% | +3,66% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 36 | 36,11% | +2,85% | -2,16% | -1,73% | +5,27% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 80 | 51,25% | +1,98% | +1,87% | -2,34% | +4,81% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 88 | 57,95% | +2,05% | +2,22% | -2,36% | +4,77% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 88 | 57,95% | +2,05% | +2,22% | -2,36% | +4,77% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 83 | 43,37% | +2,00% | -0,98% | -2,34% | +4,72% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 35 | 34,29% | +4,08% | -3,67% | -2,18% | +7,18% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 78 | 55,13% | +2,83% | +2,71% | -2,63% | +5,98% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 85 | 67,06% | +2,83% | +3,19% | -2,61% | +5,93% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 85 | 67,06% | +2,83% | +3,19% | -2,61% | +5,93% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 80 | 43,75% | +2,78% | -0,54% | -2,63% | +5,94% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 34 | 35,29% | +4,28% | -4,21% | -2,33% | +7,98% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -1,34% | -1,34% | -4,20% | +1,67% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 77 | 58,44% | +4,10% | +4,06% | -2,91% | +7,90% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 81 | 61,73% | +4,13% | +4,50% | -2,91% | +7,91% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 81 | 61,73% | +4,13% | +4,50% | -2,91% | +7,91% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 76 | 52,63% | +4,16% | +0,97% | -2,94% | +8,02% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 34 | 20,59% | +3,74% | -4,14% | -2,59% | +8,37% | PRIMA CALIBRAZIONE |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,75% | -0,75% | -4,66% | +2,55% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 72 | 68,06% | +7,56% | +7,47% | -2,98% | +11,53% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 76 | 76,32% | +7,36% | +7,57% | -3,00% | +11,40% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 76 | 76,32% | +7,36% | +7,57% | -3,00% | +11,40% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 70 | 51,43% | +7,59% | +1,08% | -3,00% | +11,67% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 29 | 44,83% | +8,60% | -4,88% | -2,40% | +12,46% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 66 | 95,45% | +11,98% | +11,32% | -2,91% | +16,28% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 69 | 92,75% | +11,96% | +11,96% | -2,89% | +16,36% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 69 | 92,75% | +11,96% | +11,96% | -2,89% | +16,36% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 62 | 66,13% | +12,05% | +1,30% | -2,85% | +16,53% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 28 | 57,14% | +12,44% | -2,72% | -2,47% | +17,06% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 55 | 94,55% | +19,11% | +16,71% | -2,84% | +24,13% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 58 | 100,00% | +19,52% | +19,52% | -2,82% | +24,42% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 58 | 100,00% | +19,52% | +19,52% | -2,82% | +24,42% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 53 | 58,49% | +19,38% | -1,34% | -2,67% | +24,33% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,92% | -4,17% | -2,62% | +19,88% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +7,72% | +7,72% | -5,13% | +13,34% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 40 | 92,50% | +26,93% | +23,18% | -2,15% | +32,48% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 43 | 100,00% | +26,82% | +26,82% | -2,17% | +32,49% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 43 | 100,00% | +26,82% | +26,82% | -2,17% | +32,49% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +28,58% | +28,58% | -2,21% | +34,30% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 38 | 42,11% | +26,99% | -6,55% | -1,87% | +32,86% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 11 | 27,27% | +26,67% | -20,27% | -0,42% | +32,88% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 87 | 48,28% | +0,02% | -0,06% | -0,75% | +1,05% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 94 | 58,51% | -0,03% | +0,46% | -0,85% | +0,94% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 94 | 58,51% | -0,03% | +0,46% | -0,85% | +0,94% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 88 | 50,00% | -0,11% | +0,16% | -0,95% | +0,86% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 55 | 40,00% | -0,01% | -0,58% | -0,92% | +0,69% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 58,33% | +2,27% | +2,00% | +0,38% | +3,14% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 86 | 44,19% | +0,15% | -0,12% | -0,97% | +1,51% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 93 | 56,99% | -0,02% | +0,67% | -1,10% | +1,28% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 93 | 56,99% | -0,02% | +0,67% | -1,10% | +1,28% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 87 | 54,02% | -0,30% | +0,21% | -1,39% | +0,99% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 54 | 44,44% | +0,05% | -0,94% | -1,12% | +1,05% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 41,67% | +2,33% | +2,11% | +0,69% | +4,97% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 85 | 41,18% | +0,37% | +0,05% | -2,62% | +3,55% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 92 | 54,35% | +0,07% | +0,92% | -2,80% | +3,25% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 92 | 54,35% | +0,07% | +0,92% | -2,80% | +3,25% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 86 | 47,67% | -0,50% | +0,06% | -3,03% | +2,64% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 53 | 37,74% | +0,22% | -1,65% | -2,84% | +3,37% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 50,00% | +2,30% | +2,13% | -1,68% | +5,97% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 84 | 46,43% | +0,86% | +0,13% | -3,87% | +5,69% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 91 | 50,55% | +0,47% | +1,20% | -4,13% | +5,36% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 91 | 50,55% | +0,47% | +1,20% | -4,13% | +5,36% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 85 | 54,12% | -0,27% | -0,50% | -4,50% | +4,68% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 52 | 42,31% | +1,01% | -3,47% | -4,21% | +5,92% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 33,33% | +1,94% | +1,81% | -2,90% | +8,39% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 82 | 48,78% | +1,27% | +0,39% | -4,61% | +7,50% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 89 | 55,06% | +0,95% | +1,46% | -4,89% | +7,12% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 89 | 55,06% | +0,95% | +1,46% | -4,89% | +7,12% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 83 | 48,19% | +0,03% | -0,76% | -5,34% | +6,22% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 50 | 36,00% | +1,82% | -4,84% | -4,90% | +7,89% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 80 | 43,75% | +1,65% | +0,37% | -5,49% | +9,35% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 86 | 55,81% | +1,22% | +1,92% | -5,70% | +9,03% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 86 | 55,81% | +1,22% | +1,92% | -5,70% | +9,03% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 80 | 46,25% | -0,01% | -1,74% | -6,23% | +7,68% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 48 | 35,42% | +2,50% | -5,90% | -5,61% | +10,07% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 77 | 53,25% | +3,08% | +2,42% | -6,39% | +12,67% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 82 | 67,07% | +2,38% | +4,17% | -6,56% | +12,16% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 82 | 67,07% | +2,38% | +4,17% | -6,56% | +12,16% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 76 | 43,42% | +0,47% | -2,54% | -7,19% | +9,81% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 44 | 38,64% | +4,07% | -5,67% | -5,83% | +12,84% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 73 | 53,42% | +5,80% | +0,49% | -6,64% | +17,70% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 76 | 61,84% | +6,19% | +5,44% | -6,59% | +17,90% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 76 | 61,84% | +6,19% | +5,44% | -6,59% | +17,90% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 70 | 50,00% | +4,23% | -3,56% | -7,29% | +15,23% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 43 | 41,86% | +5,14% | -7,66% | -6,03% | +15,65% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +4,84% | -0,04% | -5,47% | +18,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 65 | 67,69% | +10,57% | +4,75% | -5,49% | +25,70% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 68 | 69,12% | +10,87% | +6,79% | -5,47% | +26,13% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 68 | 69,12% | +10,87% | +6,79% | -5,47% | +26,13% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 62 | 58,06% | +9,46% | -2,31% | -6,17% | +24,12% | UTILE |
| DOGE | 30g | Classic technical | CALIBRABILE | 41 | 48,78% | +8,28% | -6,60% | -5,70% | +22,87% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 80,00% | +17,31% | +10,98% | -5,24% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 54 | 50,00% | +17,74% | +3,90% | -5,16% | +36,70% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 57 | 66,67% | +17,50% | +7,85% | -5,16% | +36,63% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 57 | 66,67% | +17,50% | +7,85% | -5,16% | +36,63% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 51 | 9,80% | +14,54% | -12,27% | -5,97% | +34,56% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 32 | 3,12% | +20,53% | -21,64% | -5,44% | +37,82% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +18,19% | +8,68% | -5,75% | +33,52% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 41 | 46,34% | +23,22% | -0,13% | -3,75% | +44,14% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 43 | 58,14% | +23,74% | +8,56% | -3,79% | +44,30% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 43 | 58,14% | +23,74% | +8,56% | -3,79% | +44,30% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +24,96% | +11,95% | -3,59% | +45,33% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 36 | 8,33% | +24,03% | -22,46% | -4,55% | +43,03% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 28 | 0,00% | +22,56% | -23,24% | -4,18% | +43,23% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +24,97% | +12,49% | -2,74% | +43,78% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 86 | 47,67% | +0,20% | +0,10% | -0,59% | +1,05% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 89 | 53,93% | +0,16% | +0,42% | -0,70% | +1,00% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 92 | 53,26% | +0,19% | +0,37% | -0,67% | +1,03% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 87 | 45,98% | +0,15% | -0,09% | -0,76% | +0,97% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 59 | 44,07% | +0,51% | -0,09% | -0,48% | +1,43% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 85 | 43,53% | +0,57% | +0,45% | -0,65% | +1,64% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 88 | 50,00% | +0,45% | +0,63% | -0,86% | +1,39% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 91 | 49,45% | +0,45% | +0,60% | -0,84% | +1,44% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 86 | 44,19% | +0,28% | -0,04% | -0,84% | +1,40% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,60% | +0,15% | -0,64% | +1,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 84 | 47,62% | +0,97% | +0,80% | -2,22% | +3,56% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 87 | 51,72% | +0,82% | +1,15% | -2,37% | +3,37% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 90 | 51,11% | +0,80% | +1,10% | -2,33% | +3,37% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 85 | 44,71% | +0,44% | -0,34% | -2,40% | +2,96% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 59 | 45,76% | +0,61% | +0,08% | -2,23% | +3,14% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 83 | 49,40% | +1,68% | +1,62% | -3,30% | +5,51% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 86 | 53,49% | +1,48% | +1,85% | -3,43% | +5,27% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 89 | 52,81% | +1,45% | +1,76% | -3,38% | +5,22% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 84 | 45,24% | +1,11% | -0,76% | -3,48% | +4,75% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,71% | -0,02% | -3,27% | +4,40% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 82 | 52,44% | +2,48% | +2,54% | -3,99% | +6,98% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 84 | 59,52% | +2,26% | +3,02% | -4,10% | +6,78% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 87 | 59,77% | +2,18% | +2,92% | -4,05% | +6,68% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 82 | 41,46% | +1,35% | -1,64% | -4,19% | +5,95% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 58 | 43,10% | +0,35% | -0,23% | -4,10% | +5,03% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 79 | 54,43% | +3,90% | +4,00% | -4,55% | +9,09% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 81 | 67,90% | +3,76% | +5,58% | -4,67% | +8,76% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 84 | 66,67% | +3,62% | +5,39% | -4,63% | +8,58% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 79 | 41,77% | +2,23% | -2,37% | -4,84% | +7,48% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 58 | 43,10% | +0,03% | -0,65% | -5,05% | +5,72% | PRIMA CALIBRAZIONE |

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
