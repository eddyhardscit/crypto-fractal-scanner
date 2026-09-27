# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-27 05:32 UTC

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

Segnali totali salvati: **222**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-27 | BTC | 84.404,98 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-27 | DOGE | 0.09592 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-27 | SOL | 120,66 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-26 | BTC | 83.890,58 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-26 | DOGE | 0.09735 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-26 | SOL | 120,35 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-25 | BTC | 84.066,00 | +3 | +1 | +1 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-25 | DOGE | 0.09907 | +4 | -1 | -1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-25 | SOL | 122,07 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-23 | BTC | 86.710,28 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-23 | DOGE | 0.10219 | +2 | -2 | -2 | 0 | +3 | +1 | 0 | STAI ALLA FINESTRA |
| 2026-09-23 | SOL | 118,88 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 74 | 73 | 72 | 71 | 70 | 69 | 69 | 65 | 58 | 49 | 34 | 21 |
| SOL | 74 | 73 | 72 | 71 | 70 | 69 | 69 | 65 | 58 | 49 | 34 | 21 |
| DOGE | 74 | 73 | 72 | 71 | 70 | 69 | 69 | 65 | 58 | 49 | 34 | 21 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-30 | 60g | 2026-09-28 | domani |
| SOL | 2026-07-30 | 60g | 2026-09-28 | domani |
| DOGE | 2026-07-30 | 60g | 2026-09-28 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 69 | 50,72% | +0,36% | +0,35% | UTILE |
| BTC | 2g | 69 | 50,72% | +0,62% | +0,55% | UTILE |
| BTC | 3g | 68 | 45,59% | +0,81% | +0,71% | UTILE |
| BTC | 5g | 67 | 44,78% | +1,82% | +1,63% | UTILE |
| BTC | 7g | 66 | 54,55% | +2,63% | +2,47% | UTILE |
| BTC | 10g | 66 | 62,12% | +3,62% | +3,48% | UTILE |
| BTC | 14g | 62 | 59,68% | +4,89% | +4,83% | UTILE |
| BTC | 21g | 55 | 69,09% | +8,35% | +8,23% | PRIMA CALIBRAZIONE |
| BTC | 30g | 46 | 93,48% | +14,14% | +13,20% | PRIMA CALIBRAZIONE |
| BTC | 45g | 32 | 90,62% | +23,93% | +19,80% | PRIMA CALIBRAZIONE |
| BTC | 60g | 19 | 84,21% | +25,50% | +17,59% | FEEDBACK RAPIDO |
| SOL | 1g | 65 | 52,31% | +0,46% | +0,37% | UTILE |
| SOL | 2g | 64 | 48,44% | +1,18% | +1,07% | UTILE |
| SOL | 3g | 63 | 55,56% | +1,97% | +1,83% | UTILE |
| SOL | 5g | 62 | 58,06% | +3,34% | +3,25% | UTILE |
| SOL | 7g | 61 | 62,30% | +4,75% | +4,83% | UTILE |
| SOL | 10g | 61 | 67,21% | +6,78% | +6,90% | UTILE |
| SOL | 14g | 58 | 74,14% | +9,21% | +9,84% | PRIMA CALIBRAZIONE |
| SOL | 21g | 51 | 80,39% | +14,77% | +14,07% | PRIMA CALIBRAZIONE |
| SOL | 30g | 42 | 76,19% | +22,89% | +18,18% | PRIMA CALIBRAZIONE |
| SOL | 45g | 27 | 59,26% | +39,52% | +11,02% | FEEDBACK RAPIDO |
| SOL | 60g | 15 | 40,00% | +38,30% | -4,08% | FEEDBACK RAPIDO |
| DOGE | 1g | 69 | 43,48% | +0,29% | -0,08% | UTILE |
| DOGE | 2g | 68 | 44,12% | +0,62% | -0,10% | UTILE |
| DOGE | 3g | 67 | 40,30% | +1,04% | +0,09% | UTILE |
| DOGE | 5g | 66 | 43,94% | +2,16% | +0,27% | UTILE |
| DOGE | 7g | 65 | 50,77% | +3,05% | +0,65% | UTILE |
| DOGE | 10g | 65 | 46,15% | +3,76% | +0,55% | UTILE |
| DOGE | 14g | 61 | 62,30% | +5,13% | +4,82% | UTILE |
| DOGE | 21g | 54 | 66,67% | +8,27% | +4,55% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 46 | 80,43% | +13,19% | +7,78% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 32 | 37,50% | +23,62% | -1,37% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 20 | 15,00% | +23,94% | -13,40% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 69 | 50,72% | +0,36% | +0,35% | -0,19% | +0,89% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 73 | 52,05% | +0,35% | +0,33% | -0,18% | +0,85% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 73 | 52,05% | +0,35% | +0,33% | -0,18% | +0,85% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 66 | 40,91% | +0,36% | +0,05% | -0,11% | +0,86% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 29 | 37,93% | +0,73% | +0,06% | -0,13% | +1,26% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,24% | -0,24% | -0,87% | +0,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 69 | 50,72% | +0,62% | +0,55% | -0,14% | +1,31% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 72 | 52,78% | +0,70% | +0,70% | -0,05% | +1,39% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 72 | 52,78% | +0,70% | +0,70% | -0,05% | +1,39% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 65 | 43,08% | +0,65% | +0,02% | +0,06% | +1,34% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 29 | 41,38% | +1,20% | +0,02% | +0,19% | +1,90% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,04% | -0,04% | -0,90% | +1,02% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 68 | 45,59% | +0,81% | +0,71% | -1,21% | +2,55% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 71 | 52,11% | +1,05% | +1,05% | -1,18% | +2,73% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 71 | 52,11% | +1,05% | +1,05% | -1,18% | +2,73% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 64 | 35,94% | +1,11% | -0,21% | -1,10% | +2,79% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 29 | 37,93% | +1,95% | -0,51% | -0,85% | +3,41% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 67 | 44,78% | +1,82% | +1,63% | -1,76% | +4,16% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 70 | 50,00% | +2,02% | +2,02% | -1,73% | +4,40% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 70 | 50,00% | +2,02% | +2,02% | -1,73% | +4,40% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 63 | 41,27% | +1,95% | -0,74% | -1,65% | +4,39% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 28 | 42,86% | +4,36% | -2,17% | -1,11% | +6,49% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 16,67% | -0,95% | -0,95% | -2,27% | +2,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 66 | 54,55% | +2,63% | +2,47% | -2,06% | +5,40% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 69 | 59,42% | +2,88% | +2,88% | -2,04% | +5,62% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 69 | 59,42% | +2,88% | +2,88% | -2,04% | +5,62% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 62 | 43,55% | +2,98% | -1,13% | -1,96% | +5,69% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 28 | 39,29% | +5,77% | -4,00% | -1,37% | +8,77% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 66 | 62,12% | +3,62% | +3,48% | -2,36% | +6,64% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 69 | 65,22% | +3,74% | +3,74% | -2,35% | +6,82% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 69 | 65,22% | +3,74% | +3,74% | -2,35% | +6,82% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 62 | 50,00% | +3,92% | -0,37% | -2,28% | +7,01% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 28 | 42,86% | +5,84% | -4,46% | -1,59% | +9,49% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 62 | 59,68% | +4,89% | +4,83% | -2,65% | +8,47% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 65 | 60,00% | +4,97% | +4,97% | -2,63% | +8,57% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 65 | 60,00% | +4,97% | +4,97% | -2,63% | +8,57% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 60 | 56,67% | +5,49% | +1,45% | -2,48% | +9,14% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 24 | 29,17% | +4,78% | -3,41% | -1,84% | +9,24% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 55 | 69,09% | +8,35% | +8,23% | -2,71% | +12,22% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 58 | 74,14% | +8,27% | +8,27% | -2,70% | +12,17% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 58 | 74,14% | +8,27% | +8,27% | -2,70% | +12,17% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 53 | 50,94% | +8,90% | +0,31% | -2,53% | +12,86% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 24 | 54,17% | +8,85% | -4,04% | -2,32% | +12,73% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 46 | 93,48% | +14,14% | +13,20% | -2,47% | +18,21% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 49 | 89,80% | +13,99% | +13,99% | -2,47% | +18,21% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 49 | 89,80% | +13,99% | +13,99% | -2,47% | +18,21% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 44 | 52,27% | +14,13% | -1,01% | -2,24% | +18,60% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 17 | 52,94% | +15,73% | -5,99% | -1,89% | +20,13% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +5,40% | +5,40% | -4,01% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 32 | 90,62% | +23,93% | +19,80% | -2,96% | +28,59% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 34 | 100,00% | +23,88% | +23,88% | -3,00% | +28,48% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 34 | 100,00% | +23,88% | +23,88% | -3,00% | +28,48% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 30 | 100,00% | +24,25% | +24,25% | -2,80% | +28,91% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 29 | 41,38% | +24,37% | -2,10% | -2,74% | +29,02% | FEEDBACK RAPIDO |
| BTC | 45g | Classic technical | CALIBRABILE | 4 | 0,00% | +21,70% | -21,70% | -1,55% | +30,01% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 19 | 84,21% | +25,50% | +17,59% | -3,20% | +30,61% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 21 | 100,00% | +25,40% | +25,40% | -3,24% | +30,62% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 21 | 100,00% | +25,40% | +25,40% | -3,24% | +30,62% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 17 | 100,00% | +26,05% | +26,05% | -2,95% | +31,65% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 17 | 29,41% | +25,58% | -12,13% | -2,88% | +31,21% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 2 | 0,00% | +32,21% | -32,21% | -2,23% | +37,27% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 69 | 43,48% | +0,29% | -0,08% | -0,52% | +1,27% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 72 | 58,33% | +0,20% | +0,47% | -0,61% | +1,13% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 72 | 58,33% | +0,20% | +0,47% | -0,61% | +1,13% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 66 | 50,00% | +0,12% | +0,18% | -0,73% | +1,03% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 43 | 39,53% | +0,09% | -0,68% | -0,78% | +0,85% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 68 | 44,12% | +0,62% | -0,10% | -0,52% | +1,95% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 71 | 59,15% | +0,46% | +0,76% | -0,65% | +1,72% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 71 | 59,15% | +0,46% | +0,76% | -0,65% | +1,72% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 65 | 52,31% | +0,13% | +0,19% | -1,01% | +1,37% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 43 | 41,86% | +0,42% | -1,35% | -0,82% | +1,40% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 67 | 40,30% | +1,04% | +0,09% | -2,17% | +4,13% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 70 | 54,29% | +0,88% | +0,98% | -2,27% | +3,82% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 70 | 54,29% | +0,88% | +0,98% | -2,27% | +3,82% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 64 | 45,31% | +0,18% | +0,11% | -2,54% | +3,05% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 42 | 30,95% | +0,84% | -2,27% | -2,52% | +4,00% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 66 | 43,94% | +2,16% | +0,27% | -3,07% | +6,86% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 69 | 50,72% | +2,03% | +1,20% | -3,12% | +6,61% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 69 | 50,72% | +2,03% | +1,20% | -3,12% | +6,61% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 63 | 52,38% | +1,18% | -0,47% | -3,53% | +5,81% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 41 | 34,15% | +2,58% | -4,70% | -3,39% | +7,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 65 | 50,77% | +3,05% | +0,65% | -3,61% | +9,04% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 68 | 52,94% | +3,05% | +1,23% | -3,64% | +8,82% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 68 | 52,94% | +3,05% | +1,23% | -3,64% | +8,82% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 62 | 48,39% | +2,03% | -0,78% | -4,13% | +7,77% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 41 | 29,27% | +3,84% | -6,44% | -3,92% | +9,49% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 50,00% | +1,51% | +1,40% | -2,60% | +9,95% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 65 | 46,15% | +3,76% | +0,55% | -4,30% | +11,06% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 68 | 48,53% | +3,66% | +0,88% | -4,30% | +10,86% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 68 | 48,53% | +3,66% | +0,88% | -4,30% | +10,86% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 62 | 51,61% | +2,31% | -1,27% | -4,85% | +9,30% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 41 | 31,71% | +4,20% | -7,07% | -4,70% | +11,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 60,00% | +1,26% | +0,96% | -3,68% | +10,47% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 61 | 62,30% | +5,13% | +4,82% | -5,01% | +13,74% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 64 | 64,06% | +4,72% | +3,68% | -4,98% | +13,33% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 64 | 64,06% | +4,72% | +3,68% | -4,98% | +13,33% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 58 | 55,17% | +2,45% | +0,15% | -5,64% | +10,37% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 37 | 45,95% | +4,39% | -4,10% | -5,44% | +12,23% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +5,41% | +1,04% | -4,48% | +13,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 54 | 66,67% | +8,27% | +4,55% | -4,75% | +18,71% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 57 | 68,42% | +8,65% | +6,85% | -4,78% | +18,92% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 57 | 68,42% | +8,65% | +6,85% | -4,78% | +18,92% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 51 | 62,75% | +6,26% | -0,76% | -5,53% | +15,38% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 32 | 50,00% | +5,16% | -6,82% | -5,06% | +14,16% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 66,67% | +6,54% | +0,57% | -4,75% | +18,76% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 46 | 80,43% | +13,19% | +7,78% | -4,57% | +26,51% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 48 | 87,50% | +13,45% | +11,56% | -4,59% | +27,05% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 48 | 87,50% | +13,45% | +11,56% | -4,59% | +27,05% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 42 | 54,76% | +11,75% | -5,50% | -5,49% | +24,21% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 31 | 48,39% | +10,82% | -8,72% | -5,10% | +22,58% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 85,71% | +23,10% | +14,05% | -3,96% | +33,14% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 32 | 37,50% | +23,62% | -1,37% | -4,35% | +41,06% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 34 | 52,94% | +23,50% | +4,89% | -4,36% | +41,00% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 34 | 52,94% | +23,50% | +4,89% | -4,36% | +41,00% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | +23,21% | +6,96% | -4,40% | +40,96% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 30 | 0,00% | +21,64% | -21,64% | -4,76% | +40,02% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 22 | 0,00% | +22,71% | -22,71% | -4,86% | +39,94% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +37,31% | +15,91% | -1,31% | +47,38% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 20 | 15,00% | +23,94% | -13,40% | -5,84% | +40,60% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 21 | 23,81% | +24,51% | -6,57% | -5,88% | +40,79% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 21 | 23,81% | +24,51% | -6,57% | -5,88% | +40,79% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 19 | 26,32% | +22,93% | -3,09% | -6,11% | +39,97% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 21 | 0,00% | +24,51% | -24,51% | -5,88% | +40,79% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 17 | 0,00% | +23,40% | -23,40% | -5,74% | +40,26% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 65 | 52,31% | +0,46% | +0,37% | -0,28% | +1,32% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 68 | 54,41% | +0,42% | +0,45% | -0,43% | +1,27% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 71 | 53,52% | +0,45% | +0,38% | -0,40% | +1,30% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 65 | 47,69% | +0,44% | +0,01% | -0,48% | +1,26% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 47 | 48,94% | +0,72% | +0,12% | -0,36% | +1,63% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 64 | 48,44% | +1,18% | +1,07% | -0,10% | +2,21% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 67 | 47,76% | +1,04% | +0,71% | -0,37% | +1,90% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 70 | 47,14% | +1,01% | +0,67% | -0,35% | +1,94% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 64 | 42,19% | +0,83% | -0,01% | -0,32% | +1,94% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 46 | 50,00% | +0,99% | +0,47% | -0,33% | +2,00% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 63 | 55,56% | +1,97% | +1,83% | -1,70% | +4,32% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 66 | 50,00% | +1,73% | +1,28% | -1,88% | +4,08% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 69 | 49,28% | +1,66% | +1,21% | -1,85% | +4,05% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 63 | 47,62% | +1,27% | -0,14% | -1,90% | +3,57% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 45 | 53,33% | +1,35% | +0,71% | -1,84% | +3,57% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 62 | 58,06% | +3,34% | +3,25% | -2,38% | +6,82% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 65 | 53,85% | +3,01% | +2,17% | -2,55% | +6,48% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 68 | 52,94% | +2,90% | +2,04% | -2,53% | +6,37% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 62 | 46,77% | +2,58% | -0,51% | -2,61% | +5,87% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 44 | 54,55% | +1,87% | +1,00% | -2,54% | +5,12% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 61 | 62,30% | +4,75% | +4,83% | -2,84% | +8,73% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 64 | 59,38% | +4,34% | +3,35% | -3,01% | +8,34% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 67 | 59,70% | +4,14% | +3,20% | -3,00% | +8,14% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 61 | 39,34% | +3,24% | -1,45% | -3,12% | +7,34% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 43 | 46,51% | +1,74% | +0,96% | -3,13% | +5,86% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 61 | 67,21% | +6,78% | +6,90% | -3,21% | +11,06% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 64 | 64,06% | +6,37% | +5,66% | -3,41% | +10,47% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 67 | 62,69% | +6,08% | +5,41% | -3,41% | +10,17% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 61 | 47,54% | +4,62% | -1,59% | -3,59% | +8,98% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 43 | 53,49% | +2,06% | +1,15% | -3,69% | +6,79% | PRIMA CALIBRAZIONE |

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
