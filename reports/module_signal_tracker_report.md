# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-26 05:32 UTC

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

Segnali totali salvati: **219**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-26 | BTC | 83.890,58 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-26 | DOGE | 0.09735 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-26 | SOL | 120,35 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-25 | BTC | 84.066,00 | +3 | +1 | +1 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-25 | DOGE | 0.09907 | +4 | -1 | -1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-25 | SOL | 122,07 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-23 | BTC | 86.710,28 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-23 | DOGE | 0.10219 | +2 | -2 | -2 | 0 | +3 | +1 | 0 | STAI ALLA FINESTRA |
| 2026-09-23 | SOL | 118,88 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-22 | BTC | 85.107,65 | +5 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-22 | DOGE | 0.09857 | +2 | -2 | -2 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-22 | SOL | 115,61 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 73 | 72 | 71 | 71 | 69 | 69 | 68 | 64 | 57 | 48 | 34 | 20 |
| SOL | 73 | 72 | 71 | 71 | 69 | 69 | 68 | 64 | 57 | 48 | 34 | 20 |
| DOGE | 73 | 72 | 71 | 71 | 69 | 69 | 68 | 64 | 57 | 48 | 34 | 20 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-29 | 60g | 2026-09-27 | domani |
| SOL | 2026-07-29 | 60g | 2026-09-27 | domani |
| DOGE | 2026-07-29 | 60g | 2026-09-27 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 69 | 50,72% | +0,36% | +0,35% | UTILE |
| BTC | 2g | 68 | 50,00% | +0,62% | +0,55% | UTILE |
| BTC | 3g | 68 | 45,59% | +0,81% | +0,71% | UTILE |
| BTC | 5g | 66 | 45,45% | +1,86% | +1,67% | UTILE |
| BTC | 7g | 66 | 54,55% | +2,63% | +2,47% | UTILE |
| BTC | 10g | 65 | 61,54% | +3,51% | +3,37% | UTILE |
| BTC | 14g | 61 | 59,02% | +4,82% | +4,76% | UTILE |
| BTC | 21g | 54 | 68,52% | +8,40% | +8,28% | PRIMA CALIBRAZIONE |
| BTC | 30g | 45 | 93,33% | +14,32% | +13,36% | PRIMA CALIBRAZIONE |
| BTC | 45g | 32 | 90,62% | +23,93% | +19,80% | PRIMA CALIBRAZIONE |
| BTC | 60g | 18 | 83,33% | +25,13% | +16,79% | FEEDBACK RAPIDO |
| SOL | 1g | 64 | 51,56% | +0,47% | +0,37% | UTILE |
| SOL | 2g | 63 | 49,21% | +1,22% | +1,11% | UTILE |
| SOL | 3g | 63 | 55,56% | +1,97% | +1,83% | UTILE |
| SOL | 5g | 61 | 57,38% | +3,32% | +3,23% | UTILE |
| SOL | 7g | 61 | 62,30% | +4,75% | +4,83% | UTILE |
| SOL | 10g | 61 | 67,21% | +6,78% | +6,90% | UTILE |
| SOL | 14g | 57 | 73,68% | +9,05% | +9,69% | PRIMA CALIBRAZIONE |
| SOL | 21g | 50 | 80,00% | +14,79% | +14,08% | PRIMA CALIBRAZIONE |
| SOL | 30g | 41 | 75,61% | +23,12% | +18,30% | PRIMA CALIBRAZIONE |
| SOL | 45g | 27 | 59,26% | +39,52% | +11,02% | FEEDBACK RAPIDO |
| SOL | 60g | 15 | 40,00% | +38,30% | -4,08% | FEEDBACK RAPIDO |
| DOGE | 1g | 68 | 44,12% | +0,31% | -0,06% | UTILE |
| DOGE | 2g | 67 | 44,78% | +0,68% | -0,06% | UTILE |
| DOGE | 3g | 67 | 40,30% | +1,04% | +0,09% | UTILE |
| DOGE | 5g | 65 | 44,62% | +2,23% | +0,32% | UTILE |
| DOGE | 7g | 65 | 50,77% | +3,05% | +0,65% | UTILE |
| DOGE | 10g | 64 | 46,88% | +3,53% | +0,85% | UTILE |
| DOGE | 14g | 60 | 63,33% | +5,00% | +5,12% | UTILE |
| DOGE | 21g | 53 | 66,04% | +8,32% | +4,53% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 46 | 80,43% | +13,19% | +7,78% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 32 | 37,50% | +23,62% | -1,37% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 19 | 10,53% | +23,31% | -15,99% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 69 | 50,72% | +0,36% | +0,35% | -0,19% | +0,89% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 72 | 52,78% | +0,35% | +0,35% | -0,19% | +0,86% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 72 | 52,78% | +0,35% | +0,35% | -0,19% | +0,86% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 65 | 40,00% | +0,35% | +0,04% | -0,12% | +0,87% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 29 | 37,93% | +0,73% | +0,06% | -0,13% | +1,26% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,24% | -0,24% | -0,87% | +0,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 68 | 50,00% | +0,62% | +0,55% | -0,15% | +1,32% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 71 | 52,11% | +0,70% | +0,70% | -0,06% | +1,40% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 71 | 52,11% | +0,70% | +0,70% | -0,06% | +1,40% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 64 | 42,19% | +0,66% | +0,01% | +0,06% | +1,35% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 29 | 41,38% | +1,20% | +0,02% | +0,19% | +1,90% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,04% | -0,04% | -0,90% | +1,02% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 68 | 45,59% | +0,81% | +0,71% | -1,21% | +2,55% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 71 | 52,11% | +1,05% | +1,05% | -1,18% | +2,73% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 71 | 52,11% | +1,05% | +1,05% | -1,18% | +2,73% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 64 | 35,94% | +1,11% | -0,21% | -1,10% | +2,79% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 29 | 37,93% | +1,95% | -0,51% | -0,85% | +3,41% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 66 | 45,45% | +1,86% | +1,67% | -1,75% | +4,19% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 69 | 50,72% | +2,06% | +2,06% | -1,72% | +4,43% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 69 | 50,72% | +2,06% | +2,06% | -1,72% | +4,43% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 62 | 41,94% | +2,00% | -0,73% | -1,64% | +4,42% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 28 | 42,86% | +4,36% | -2,17% | -1,11% | +6,49% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 66 | 54,55% | +2,63% | +2,47% | -2,06% | +5,40% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 69 | 59,42% | +2,88% | +2,88% | -2,04% | +5,62% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 69 | 59,42% | +2,88% | +2,88% | -2,04% | +5,62% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 62 | 43,55% | +2,98% | -1,13% | -1,96% | +5,69% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 28 | 39,29% | +5,77% | -4,00% | -1,37% | +8,77% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 65 | 61,54% | +3,51% | +3,37% | -2,40% | +6,52% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 68 | 64,71% | +3,64% | +3,64% | -2,38% | +6,71% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 68 | 64,71% | +3,64% | +3,64% | -2,38% | +6,71% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 62 | 50,00% | +3,92% | -0,37% | -2,28% | +7,01% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 27 | 44,44% | +5,67% | -4,24% | -1,64% | +9,30% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 61 | 59,02% | +4,82% | +4,76% | -2,65% | +8,39% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 64 | 59,38% | +4,91% | +4,91% | -2,63% | +8,50% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 64 | 59,38% | +4,91% | +4,91% | -2,63% | +8,50% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 59 | 55,93% | +5,43% | +1,32% | -2,47% | +9,08% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 24 | 29,17% | +4,78% | -3,41% | -1,84% | +9,24% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 54 | 68,52% | +8,40% | +8,28% | -2,65% | +12,28% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 57 | 73,68% | +8,32% | +8,32% | -2,64% | +12,22% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 57 | 73,68% | +8,32% | +8,32% | -2,64% | +12,22% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 52 | 50,00% | +8,97% | +0,21% | -2,46% | +12,93% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 24 | 54,17% | +8,85% | -4,04% | -2,32% | +12,73% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +0,55% | +0,55% | -4,09% | +5,46% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 45 | 93,33% | +14,32% | +13,36% | -2,39% | +18,40% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 48 | 89,58% | +14,15% | +14,15% | -2,39% | +18,39% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 48 | 89,58% | +14,15% | +14,15% | -2,39% | +18,39% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 43 | 51,16% | +14,32% | -1,17% | -2,15% | +18,81% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 16 | 50,00% | +16,35% | -6,74% | -1,64% | +20,79% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +5,40% | +5,40% | -4,01% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 32 | 90,62% | +23,93% | +19,80% | -2,96% | +28,59% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 34 | 100,00% | +23,88% | +23,88% | -3,00% | +28,48% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 34 | 100,00% | +23,88% | +23,88% | -3,00% | +28,48% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 30 | 100,00% | +24,25% | +24,25% | -2,80% | +28,91% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 29 | 41,38% | +24,37% | -2,10% | -2,74% | +29,02% | FEEDBACK RAPIDO |
| BTC | 45g | Classic technical | CALIBRABILE | 4 | 0,00% | +21,70% | -21,70% | -1,55% | +30,01% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 18 | 83,33% | +25,13% | +16,79% | -3,23% | +30,27% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 20 | 100,00% | +25,07% | +25,07% | -3,27% | +30,32% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 20 | 100,00% | +25,07% | +25,07% | -3,27% | +30,32% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 16 | 100,00% | +25,68% | +25,68% | -2,97% | +31,33% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 16 | 31,25% | +25,17% | -10,89% | -2,90% | +30,87% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 1 | 0,00% | +32,36% | -32,36% | -1,82% | +37,84% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 68 | 44,12% | +0,31% | -0,06% | -0,50% | +1,29% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 71 | 57,75% | +0,23% | +0,45% | -0,60% | +1,15% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 71 | 57,75% | +0,23% | +0,45% | -0,60% | +1,15% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 65 | 50,77% | +0,14% | +0,21% | -0,71% | +1,06% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 43 | 39,53% | +0,09% | -0,68% | -0,78% | +0,85% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 67 | 44,78% | +0,68% | -0,06% | -0,48% | +2,02% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 70 | 58,57% | +0,52% | +0,72% | -0,61% | +1,78% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 70 | 58,57% | +0,52% | +0,72% | -0,61% | +1,78% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 64 | 53,12% | +0,18% | +0,25% | -0,97% | +1,43% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 42 | 42,86% | +0,50% | -1,31% | -0,76% | +1,49% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 67 | 40,30% | +1,04% | +0,09% | -2,17% | +4,13% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 70 | 54,29% | +0,88% | +0,98% | -2,27% | +3,82% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 70 | 54,29% | +0,88% | +0,98% | -2,27% | +3,82% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 64 | 45,31% | +0,18% | +0,11% | -2,54% | +3,05% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 42 | 30,95% | +0,84% | -2,27% | -2,52% | +4,00% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 65 | 44,62% | +2,23% | +0,32% | -3,01% | +6,88% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 68 | 50,00% | +2,10% | +1,18% | -3,07% | +6,62% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 68 | 50,00% | +2,10% | +1,18% | -3,07% | +6,62% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 62 | 53,23% | +1,24% | -0,43% | -3,48% | +5,81% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 41 | 34,15% | +2,58% | -4,70% | -3,39% | +7,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 40,00% | +2,66% | +2,50% | -2,06% | +9,50% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 65 | 50,77% | +3,05% | +0,65% | -3,61% | +9,04% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 68 | 52,94% | +3,05% | +1,23% | -3,64% | +8,82% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 68 | 52,94% | +3,05% | +1,23% | -3,64% | +8,82% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 62 | 48,39% | +2,03% | -0,78% | -4,13% | +7,77% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 41 | 29,27% | +3,84% | -6,44% | -3,92% | +9,49% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 50,00% | +1,51% | +1,40% | -2,60% | +9,95% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 64 | 46,88% | +3,53% | +0,85% | -4,37% | +10,76% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 67 | 49,25% | +3,44% | +1,17% | -4,37% | +10,57% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 67 | 49,25% | +3,44% | +1,17% | -4,37% | +10,57% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 61 | 52,46% | +2,05% | -0,99% | -4,94% | +8,96% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 40 | 32,50% | +3,84% | -6,78% | -4,83% | +11,16% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | -0,68% | -1,01% | -4,16% | +8,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 60 | 63,33% | +5,00% | +5,12% | -4,97% | +13,56% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 63 | 65,08% | +4,59% | +3,95% | -4,94% | +13,15% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 63 | 65,08% | +4,59% | +3,95% | -4,94% | +13,15% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 57 | 56,14% | +2,27% | +0,38% | -5,61% | +10,13% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 36 | 47,22% | +4,14% | -3,85% | -5,38% | +11,90% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +5,41% | +1,04% | -4,48% | +13,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 53 | 66,04% | +8,32% | +4,53% | -4,58% | +18,76% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 56 | 69,64% | +8,71% | +7,07% | -4,62% | +18,98% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 56 | 69,64% | +8,71% | +7,07% | -4,62% | +18,98% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 50 | 62,00% | +6,28% | -0,89% | -5,37% | +15,37% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 31 | 48,39% | +5,15% | -7,22% | -4,78% | +14,11% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +6,66% | -0,06% | -3,62% | +19,12% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 46 | 80,43% | +13,19% | +7,78% | -4,57% | +26,51% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 47 | 89,36% | +13,53% | +12,01% | -4,46% | +27,19% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 47 | 89,36% | +13,53% | +12,01% | -4,46% | +27,19% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 41 | 53,66% | +11,80% | -5,87% | -5,37% | +24,31% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 31 | 48,39% | +10,82% | -8,72% | -5,10% | +22,58% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 85,71% | +23,10% | +14,05% | -3,96% | +33,14% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 32 | 37,50% | +23,62% | -1,37% | -4,35% | +41,06% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 34 | 52,94% | +23,50% | +4,89% | -4,36% | +41,00% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 34 | 52,94% | +23,50% | +4,89% | -4,36% | +41,00% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | +23,21% | +6,96% | -4,40% | +40,96% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 30 | 0,00% | +21,64% | -21,64% | -4,76% | +40,02% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 22 | 0,00% | +22,71% | -22,71% | -4,86% | +39,94% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +37,31% | +15,91% | -1,31% | +47,38% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 19 | 10,53% | +23,31% | -15,99% | -5,95% | +40,16% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 20 | 20,00% | +23,95% | -8,69% | -5,99% | +40,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 20 | 20,00% | +23,95% | -8,69% | -5,99% | +40,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 18 | 22,22% | +22,21% | -5,26% | -6,24% | +39,47% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 20 | 0,00% | +23,95% | -23,95% | -5,99% | +40,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 17 | 0,00% | +23,40% | -23,40% | -5,74% | +40,26% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 64 | 51,56% | +0,47% | +0,37% | -0,28% | +1,33% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 67 | 55,22% | +0,43% | +0,46% | -0,43% | +1,27% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 70 | 54,29% | +0,45% | +0,39% | -0,40% | +1,30% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 64 | 46,88% | +0,44% | +0,01% | -0,48% | +1,26% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 46 | 47,83% | +0,73% | +0,12% | -0,36% | +1,65% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 63 | 49,21% | +1,22% | +1,11% | -0,07% | +2,25% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 66 | 46,97% | +1,07% | +0,70% | -0,35% | +1,93% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 69 | 46,38% | +1,04% | +0,66% | -0,34% | +1,97% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 63 | 42,86% | +0,87% | +0,01% | -0,30% | +1,98% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 45 | 51,11% | +1,04% | +0,51% | -0,30% | +2,06% | PRIMA CALIBRAZIONE |
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
| SOL | 5g | Global confluence | BENCHMARK | 61 | 57,38% | +3,32% | +3,23% | -2,38% | +6,83% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 64 | 53,12% | +2,98% | +2,13% | -2,56% | +6,48% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 67 | 52,24% | +2,88% | +2,01% | -2,53% | +6,37% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 61 | 45,90% | +2,55% | -0,59% | -2,61% | +5,87% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 43 | 53,49% | +1,81% | +0,92% | -2,55% | +5,09% | PRIMA CALIBRAZIONE |
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
| SOL | 10g | Famiglia statistica | CALIBRABILE | 63 | 63,49% | +6,13% | +5,41% | -3,49% | +10,26% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 66 | 62,12% | +5,85% | +5,17% | -3,49% | +9,97% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 60 | 48,33% | +4,34% | -1,26% | -3,67% | +8,74% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 42 | 54,76% | +1,60% | +1,69% | -3,81% | +6,40% | PRIMA CALIBRAZIONE |

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
