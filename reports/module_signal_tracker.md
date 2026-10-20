# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-20 05:34 UTC

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

Segnali totali salvati: **285**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-20 | BTC | 81.867,63 | +2 | +1 | +1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-20 | DOGE | 0.07939 | -1 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-20 | SOL | 104,68 | +3 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-19 | BTC | 82.648,77 | -1 | +1 | +1 | 0 | -1 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-19 | DOGE | 0.07945 | -1 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-19 | SOL | 105,63 | -2 | +1 | +1 | 0 | -2 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-10-18 | BTC | 81.614,92 | +3 | +2 | +2 | 0 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-10-18 | DOGE | 0.07904 | -2 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-18 | SOL | 103,34 | -1 | +2 | +2 | 0 | -2 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-10-16 | BTC | 82.086,63 | +2 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-16 | DOGE | 0.08216 | -1 | +3 | +3 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-16 | SOL | 105,81 | 0 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 95 | 94 | 93 | 92 | 91 | 89 | 86 | 82 | 76 | 69 | 57 | 42 |
| SOL | 95 | 94 | 93 | 92 | 91 | 89 | 86 | 82 | 76 | 69 | 57 | 42 |
| DOGE | 95 | 94 | 93 | 92 | 91 | 89 | 86 | 82 | 76 | 69 | 57 | 42 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-22 | 60g | 2026-10-21 | domani |
| SOL | 2026-08-22 | 60g | 2026-10-21 | domani |
| DOGE | 2026-08-22 | 60g | 2026-10-21 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 84 | 52,38% | +0,30% | +0,28% | UTILE |
| BTC | 2g | 83 | 50,60% | +0,50% | +0,43% | UTILE |
| BTC | 3g | 82 | 46,34% | +0,62% | +0,59% | UTILE |
| BTC | 5g | 81 | 43,21% | +1,32% | +1,19% | UTILE |
| BTC | 7g | 80 | 51,25% | +1,98% | +1,87% | UTILE |
| BTC | 10g | 78 | 55,13% | +2,83% | +2,71% | UTILE |
| BTC | 14g | 77 | 58,44% | +4,10% | +4,06% | UTILE |
| BTC | 21g | 71 | 69,01% | +7,68% | +7,59% | UTILE |
| BTC | 30g | 66 | 95,45% | +11,98% | +11,32% | UTILE |
| BTC | 45g | 54 | 94,44% | +19,40% | +16,95% | PRIMA CALIBRAZIONE |
| BTC | 60g | 39 | 92,31% | +27,43% | +23,58% | PRIMA CALIBRAZIONE |
| SOL | 1g | 85 | 47,06% | +0,19% | +0,08% | UTILE |
| SOL | 2g | 84 | 44,05% | +0,57% | +0,46% | UTILE |
| SOL | 3g | 83 | 48,19% | +0,95% | +0,84% | UTILE |
| SOL | 5g | 83 | 49,40% | +1,68% | +1,62% | UTILE |
| SOL | 7g | 81 | 53,09% | +2,52% | +2,59% | UTILE |
| SOL | 10g | 78 | 55,13% | +3,99% | +4,09% | UTILE |
| SOL | 14g | 74 | 63,51% | +6,46% | +6,95% | UTILE |
| SOL | 21g | 68 | 75,00% | +12,49% | +11,96% | UTILE |
| SOL | 30g | 61 | 83,61% | +19,46% | +16,22% | UTILE |
| SOL | 45g | 50 | 76,00% | +32,43% | +17,04% | PRIMA CALIBRAZIONE |
| SOL | 60g | 35 | 68,57% | +44,35% | +19,31% | PRIMA CALIBRAZIONE |
| DOGE | 1g | 86 | 48,84% | -0,01% | -0,02% | UTILE |
| DOGE | 2g | 85 | 44,71% | +0,12% | -0,08% | UTILE |
| DOGE | 3g | 84 | 41,67% | +0,33% | +0,09% | UTILE |
| DOGE | 5g | 83 | 45,78% | +0,88% | +0,12% | UTILE |
| DOGE | 7g | 81 | 49,38% | +1,33% | +0,44% | UTILE |
| DOGE | 10g | 79 | 44,30% | +1,72% | +0,43% | UTILE |
| DOGE | 14g | 76 | 52,63% | +3,25% | +2,33% | UTILE |
| DOGE | 21g | 72 | 54,17% | +6,07% | +0,68% | UTILE |
| DOGE | 30g | 65 | 67,69% | +10,57% | +4,75% | UTILE |
| DOGE | 45g | 53 | 50,94% | +18,27% | +4,17% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 40 | 47,50% | +24,04% | +0,11% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 84 | 52,38% | +0,30% | +0,28% | -0,29% | +0,80% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 92 | 48,91% | +0,20% | +0,25% | -0,34% | +0,69% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 92 | 48,91% | +0,20% | +0,25% | -0,34% | +0,69% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 87 | 48,28% | +0,21% | +0,06% | -0,29% | +0,73% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,55% | -0,06% | -0,27% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 83 | 50,60% | +0,50% | +0,43% | -0,28% | +1,19% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 91 | 51,65% | +0,44% | +0,53% | -0,29% | +1,12% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 91 | 51,65% | +0,44% | +0,53% | -0,29% | +1,12% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 86 | 47,67% | +0,43% | +0,06% | -0,21% | +1,10% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,85% | -0,13% | -0,05% | +1,59% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 82 | 46,34% | +0,62% | +0,59% | -1,29% | +2,39% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 90 | 50,00% | +0,74% | +0,81% | -1,36% | +2,42% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 90 | 50,00% | +0,74% | +0,81% | -1,36% | +2,42% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 85 | 40,00% | +0,75% | -0,11% | -1,29% | +2,43% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 36 | 36,11% | +1,29% | -0,55% | -1,13% | +3,01% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 81 | 43,21% | +1,32% | +1,19% | -1,96% | +3,74% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 89 | 48,31% | +1,42% | +1,53% | -1,98% | +3,76% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 89 | 48,31% | +1,42% | +1,53% | -1,98% | +3,76% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 84 | 42,86% | +1,28% | -0,62% | -1,94% | +3,69% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 36 | 36,11% | +2,85% | -2,16% | -1,73% | +5,27% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 80 | 51,25% | +1,98% | +1,87% | -2,34% | +4,81% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 87 | 58,62% | +2,09% | +2,25% | -2,33% | +4,83% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 87 | 58,62% | +2,09% | +2,25% | -2,33% | +4,83% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 82 | 42,68% | +2,03% | -1,00% | -2,31% | +4,78% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 35 | 34,29% | +4,08% | -3,67% | -2,18% | +7,18% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 78 | 55,13% | +2,83% | +2,71% | -2,63% | +5,98% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 84 | 66,67% | +2,87% | +3,23% | -2,60% | +5,98% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 84 | 66,67% | +2,87% | +3,23% | -2,60% | +5,98% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 79 | 44,30% | +2,82% | -0,54% | -2,61% | +6,00% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 34 | 35,29% | +4,28% | -4,21% | -2,33% | +7,98% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -1,47% | -1,47% | -4,23% | +1,69% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 77 | 58,44% | +4,10% | +4,06% | -2,91% | +7,90% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 80 | 61,25% | +4,21% | +4,53% | -2,88% | +8,01% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 80 | 61,25% | +4,21% | +4,53% | -2,88% | +8,01% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 75 | 53,33% | +4,24% | +1,01% | -2,90% | +8,12% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 34 | 20,59% | +3,74% | -4,14% | -2,59% | +8,37% | PRIMA CALIBRAZIONE |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,75% | -0,75% | -4,66% | +2,55% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 71 | 69,01% | +7,68% | +7,59% | -2,96% | +11,63% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 76 | 76,32% | +7,36% | +7,57% | -3,00% | +11,40% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 76 | 76,32% | +7,36% | +7,57% | -3,00% | +11,40% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 69 | 52,17% | +7,71% | +1,11% | -2,98% | +11,78% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 29 | 44,83% | +8,60% | -4,88% | -2,40% | +12,46% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 66 | 95,45% | +11,98% | +11,32% | -2,91% | +16,28% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 69 | 92,75% | +11,96% | +11,96% | -2,89% | +16,36% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 69 | 92,75% | +11,96% | +11,96% | -2,89% | +16,36% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 62 | 66,13% | +12,05% | +1,30% | -2,85% | +16,53% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 28 | 57,14% | +12,44% | -2,72% | -2,47% | +17,06% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 54 | 94,44% | +19,40% | +16,95% | -2,78% | +24,40% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 57 | 100,00% | +19,80% | +19,80% | -2,76% | +24,69% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 57 | 100,00% | +19,80% | +19,80% | -2,76% | +24,69% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 52 | 57,69% | +19,68% | -1,43% | -2,60% | +24,62% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,92% | -4,17% | -2,62% | +19,88% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 100,00% | +8,74% | +8,74% | -4,87% | +14,33% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 39 | 92,31% | +27,43% | +23,58% | -2,13% | +32,98% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 42 | 100,00% | +27,29% | +27,29% | -2,16% | +32,94% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 42 | 100,00% | +27,29% | +27,29% | -2,16% | +32,94% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +28,58% | +28,58% | -2,21% | +34,30% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 37 | 40,54% | +27,52% | -6,93% | -1,84% | +33,39% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 10 | 20,00% | +28,60% | -23,03% | -0,19% | +34,84% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 86 | 48,84% | -0,01% | -0,02% | -0,79% | +1,02% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 93 | 58,06% | -0,06% | +0,44% | -0,88% | +0,91% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 93 | 58,06% | -0,06% | +0,44% | -0,88% | +0,91% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 87 | 50,57% | -0,15% | +0,19% | -0,99% | +0,83% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 54 | 40,74% | -0,06% | -0,53% | -0,98% | +0,63% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 58,33% | +2,27% | +2,00% | +0,38% | +3,14% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 85 | 44,71% | +0,12% | -0,08% | -1,01% | +1,48% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 92 | 56,52% | -0,05% | +0,64% | -1,14% | +1,25% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 92 | 56,52% | -0,05% | +0,64% | -1,14% | +1,25% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 86 | 54,65% | -0,34% | +0,24% | -1,44% | +0,96% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 53 | 45,28% | -0,01% | -0,90% | -1,19% | +1,00% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 41,67% | +2,33% | +2,11% | +0,69% | +4,97% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 84 | 41,67% | +0,33% | +0,09% | -2,65% | +3,55% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 91 | 53,85% | +0,03% | +0,89% | -2,82% | +3,24% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 91 | 53,85% | +0,03% | +0,89% | -2,82% | +3,24% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 85 | 48,24% | -0,55% | +0,10% | -3,07% | +2,62% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 52 | 38,46% | +0,16% | -1,62% | -2,89% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 50,00% | +2,30% | +2,13% | -1,68% | +5,97% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 83 | 45,78% | +0,88% | +0,12% | -3,83% | +5,76% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 90 | 51,11% | +0,48% | +1,22% | -4,09% | +5,42% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 90 | 51,11% | +0,48% | +1,22% | -4,09% | +5,42% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 84 | 53,57% | -0,27% | -0,51% | -4,47% | +4,74% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 51 | 41,18% | +1,04% | -3,55% | -4,15% | +6,04% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 81 | 49,38% | +1,33% | +0,44% | -4,55% | +7,62% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 88 | 55,68% | +1,00% | +1,52% | -4,83% | +7,23% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 88 | 55,68% | +1,00% | +1,52% | -4,83% | +7,23% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 82 | 47,56% | +0,07% | -0,82% | -5,28% | +6,32% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 50 | 36,00% | +1,82% | -4,84% | -4,90% | +7,89% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 79 | 44,30% | +1,72% | +0,43% | -5,42% | +9,43% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 85 | 56,47% | +1,28% | +2,00% | -5,64% | +9,10% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 85 | 56,47% | +1,28% | +2,00% | -5,64% | +9,10% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 79 | 45,57% | +0,04% | -1,82% | -6,17% | +7,74% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 47 | 34,04% | +2,65% | -6,12% | -5,50% | +10,22% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 76 | 52,63% | +3,25% | +2,33% | -6,27% | +12,85% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 81 | 66,67% | +2,53% | +4,10% | -6,45% | +12,32% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 81 | 66,67% | +2,53% | +4,10% | -6,45% | +12,32% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 75 | 42,67% | +0,61% | -2,70% | -7,08% | +9,95% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 44 | 38,64% | +4,07% | -5,67% | -5,83% | +12,84% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 72 | 54,17% | +6,07% | +0,68% | -6,47% | +17,89% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 75 | 61,33% | +6,45% | +5,34% | -6,43% | +18,09% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 75 | 61,33% | +6,45% | +5,34% | -6,43% | +18,09% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 69 | 50,72% | +4,49% | -3,42% | -7,13% | +15,40% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 43 | 41,86% | +5,14% | -7,66% | -6,03% | +15,65% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +4,84% | -0,04% | -5,47% | +18,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 65 | 67,69% | +10,57% | +4,75% | -5,49% | +25,70% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 68 | 69,12% | +10,87% | +6,79% | -5,47% | +26,13% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 68 | 69,12% | +10,87% | +6,79% | -5,47% | +26,13% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 62 | 58,06% | +9,46% | -2,31% | -6,17% | +24,12% | UTILE |
| DOGE | 30g | Classic technical | CALIBRABILE | 41 | 48,78% | +8,28% | -6,60% | -5,70% | +22,87% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 80,00% | +17,31% | +10,98% | -5,24% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 53 | 50,94% | +18,27% | +4,17% | -4,95% | +37,09% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 56 | 66,07% | +18,00% | +7,81% | -4,96% | +37,00% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 56 | 66,07% | +18,00% | +7,81% | -4,96% | +37,00% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 50 | 10,00% | +15,04% | -12,31% | -5,77% | +34,93% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 31 | 3,23% | +21,52% | -22,01% | -5,10% | +38,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +21,73% | +11,03% | -4,45% | +35,73% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 40 | 47,50% | +24,04% | +0,11% | -3,46% | +44,83% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 42 | 59,52% | +24,53% | +8,99% | -3,51% | +44,96% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 42 | 59,52% | +24,53% | +8,99% | -3,51% | +44,96% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +24,96% | +11,95% | -3,59% | +45,33% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 35 | 8,57% | +24,99% | -22,83% | -4,24% | +43,78% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 27 | 0,00% | +23,75% | -23,75% | -3,76% | +44,21% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +31,87% | +16,90% | -0,17% | +49,22% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 85 | 47,06% | +0,19% | +0,08% | -0,61% | +1,03% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 88 | 53,41% | +0,15% | +0,41% | -0,72% | +0,99% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 91 | 52,75% | +0,18% | +0,36% | -0,69% | +1,02% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 86 | 46,51% | +0,14% | -0,07% | -0,78% | +0,96% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 59 | 44,07% | +0,51% | -0,09% | -0,48% | +1,43% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 84 | 44,05% | +0,57% | +0,46% | -0,66% | +1,64% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 87 | 49,43% | +0,45% | +0,63% | -0,87% | +1,40% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 90 | 48,89% | +0,45% | +0,60% | -0,85% | +1,44% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 85 | 44,71% | +0,28% | -0,04% | -0,85% | +1,40% | UTILE |
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
| SOL | 5g | Global confluence | BENCHMARK | 83 | 49,40% | +1,68% | +1,62% | -3,30% | +5,51% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 85 | 52,94% | +1,50% | +1,87% | -3,41% | +5,32% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 88 | 52,27% | +1,47% | +1,78% | -3,36% | +5,27% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 83 | 45,78% | +1,12% | -0,76% | -3,46% | +4,80% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,71% | -0,02% | -3,27% | +4,40% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 81 | 53,09% | +2,52% | +2,59% | -3,96% | +7,07% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 83 | 60,24% | +2,31% | +3,07% | -4,07% | +6,87% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 86 | 60,47% | +2,22% | +2,96% | -4,03% | +6,76% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 81 | 40,74% | +1,39% | -1,68% | -4,17% | +6,02% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 58 | 43,10% | +0,35% | -0,23% | -4,10% | +5,03% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 78 | 55,13% | +3,99% | +4,09% | -4,50% | +9,16% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 80 | 68,75% | +3,85% | +5,69% | -4,63% | +8,82% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 83 | 67,47% | +3,71% | +5,49% | -4,59% | +8,65% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 78 | 41,03% | +2,30% | -2,44% | -4,80% | +7,54% | UTILE |
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
