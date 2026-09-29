# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-29 05:33 UTC

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

Segnali totali salvati: **228**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-29 | BTC | 83.140,92 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-29 | DOGE | 0.09319 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-29 | SOL | 117,59 | +1 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-28 | BTC | 82.981,23 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-28 | DOGE | 0.09299 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-28 | SOL | 118,67 | +4 | 0 | 0 | 0 | +2 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-27 | BTC | 84.404,98 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-27 | DOGE | 0.09592 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-27 | SOL | 120,66 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-26 | BTC | 83.890,58 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-26 | DOGE | 0.09735 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-26 | SOL | 120,35 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 76 | 75 | 74 | 73 | 71 | 70 | 69 | 67 | 60 | 51 | 36 | 23 |
| SOL | 76 | 75 | 74 | 73 | 71 | 70 | 69 | 67 | 60 | 51 | 36 | 23 |
| DOGE | 76 | 75 | 74 | 73 | 71 | 70 | 69 | 67 | 60 | 51 | 36 | 23 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-01 | 60g | 2026-09-30 | domani |
| SOL | 2026-08-01 | 60g | 2026-09-30 | domani |
| DOGE | 2026-08-01 | 60g | 2026-09-30 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 70 | 51,43% | +0,36% | +0,34% | UTILE |
| BTC | 2g | 69 | 50,72% | +0,62% | +0,55% | UTILE |
| BTC | 3g | 69 | 44,93% | +0,78% | +0,68% | UTILE |
| BTC | 5g | 68 | 44,12% | +1,73% | +1,55% | UTILE |
| BTC | 7g | 67 | 53,73% | +2,56% | +2,40% | UTILE |
| BTC | 10g | 66 | 62,12% | +3,62% | +3,48% | UTILE |
| BTC | 14g | 64 | 60,94% | +4,96% | +4,91% | UTILE |
| BTC | 21g | 57 | 70,18% | +8,22% | +8,11% | PRIMA CALIBRAZIONE |
| BTC | 30g | 48 | 93,75% | +13,82% | +12,93% | PRIMA CALIBRAZIONE |
| BTC | 45g | 34 | 91,18% | +24,41% | +20,52% | PRIMA CALIBRAZIONE |
| BTC | 60g | 21 | 85,71% | +25,88% | +18,73% | FEEDBACK RAPIDO |
| SOL | 1g | 67 | 50,75% | +0,41% | +0,32% | UTILE |
| SOL | 2g | 66 | 46,97% | +1,08% | +0,98% | UTILE |
| SOL | 3g | 65 | 53,85% | +1,83% | +1,70% | UTILE |
| SOL | 5g | 63 | 57,14% | +3,28% | +3,20% | UTILE |
| SOL | 7g | 62 | 62,90% | +4,70% | +4,78% | UTILE |
| SOL | 10g | 61 | 67,21% | +6,78% | +6,90% | UTILE |
| SOL | 14g | 60 | 75,00% | +9,47% | +10,08% | UTILE |
| SOL | 21g | 53 | 81,13% | +14,71% | +14,04% | PRIMA CALIBRAZIONE |
| SOL | 30g | 44 | 77,27% | +22,44% | +17,95% | PRIMA CALIBRAZIONE |
| SOL | 45g | 29 | 62,07% | +40,71% | +14,16% | FEEDBACK RAPIDO |
| SOL | 60g | 17 | 35,29% | +40,88% | -10,68% | FEEDBACK RAPIDO |
| DOGE | 1g | 71 | 43,66% | +0,24% | -0,12% | UTILE |
| DOGE | 2g | 70 | 42,86% | +0,50% | -0,20% | UTILE |
| DOGE | 3g | 69 | 39,13% | +0,86% | -0,06% | UTILE |
| DOGE | 5g | 67 | 43,28% | +1,99% | +0,13% | UTILE |
| DOGE | 7g | 66 | 50,00% | +2,92% | +0,56% | UTILE |
| DOGE | 10g | 65 | 46,15% | +3,76% | +0,55% | UTILE |
| DOGE | 14g | 63 | 60,32% | +5,33% | +4,30% | UTILE |
| DOGE | 21g | 56 | 67,86% | +8,09% | +4,51% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 48 | 81,25% | +13,04% | +7,85% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 34 | 41,18% | +24,19% | +0,68% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 22 | 18,18% | +24,79% | -12,16% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 70 | 51,43% | +0,36% | +0,34% | -0,19% | +0,88% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 75 | 52,00% | +0,32% | +0,34% | -0,20% | +0,85% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 75 | 52,00% | +0,32% | +0,34% | -0,20% | +0,85% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 68 | 41,18% | +0,32% | +0,02% | -0,14% | +0,86% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 29 | 37,93% | +0,73% | +0,06% | -0,13% | +1,26% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,24% | -0,24% | -0,87% | +0,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 69 | 50,72% | +0,62% | +0,55% | -0,14% | +1,31% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 74 | 54,05% | +0,65% | +0,72% | -0,09% | +1,35% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 74 | 54,05% | +0,65% | +0,72% | -0,09% | +1,35% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 67 | 41,79% | +0,59% | -0,02% | +0,02% | +1,30% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 29 | 41,38% | +1,20% | +0,02% | +0,19% | +1,90% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,04% | -0,04% | -0,90% | +1,02% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 69 | 44,93% | +0,78% | +0,68% | -1,21% | +2,52% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 73 | 52,05% | +0,99% | +1,02% | -1,18% | +2,69% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 73 | 52,05% | +0,99% | +1,02% | -1,18% | +2,69% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 66 | 34,85% | +1,04% | -0,23% | -1,10% | +2,74% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 29 | 37,93% | +1,95% | -0,51% | -0,85% | +3,41% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 68 | 44,12% | +1,73% | +1,55% | -1,80% | +4,08% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 71 | 49,30% | +1,93% | +1,93% | -1,77% | +4,31% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 71 | 49,30% | +1,93% | +1,93% | -1,77% | +4,31% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 64 | 40,62% | +1,85% | -0,79% | -1,69% | +4,29% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 29 | 41,38% | +4,06% | -2,25% | -1,22% | +6,21% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 14,29% | -1,43% | -1,43% | -2,57% | +1,68% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 67 | 53,73% | +2,56% | +2,40% | -2,07% | +5,36% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 70 | 58,57% | +2,80% | +2,80% | -2,05% | +5,58% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 70 | 58,57% | +2,80% | +2,80% | -2,05% | +5,58% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 63 | 42,86% | +2,90% | -1,15% | -1,97% | +5,64% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 28 | 39,29% | +5,77% | -4,00% | -1,37% | +8,77% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 33,33% | -1,39% | -1,39% | -2,98% | +2,35% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 66 | 62,12% | +3,62% | +3,48% | -2,36% | +6,64% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 69 | 65,22% | +3,74% | +3,74% | -2,35% | +6,82% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 69 | 65,22% | +3,74% | +3,74% | -2,35% | +6,82% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 62 | 50,00% | +3,92% | -0,37% | -2,28% | +7,01% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 28 | 42,86% | +5,84% | -4,46% | -1,59% | +9,49% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 64 | 60,94% | +4,96% | +4,91% | -2,67% | +8,60% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 67 | 61,19% | +5,04% | +5,04% | -2,65% | +8,69% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 67 | 61,19% | +5,04% | +5,04% | -2,65% | +8,69% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 62 | 58,06% | +5,55% | +1,64% | -2,50% | +9,26% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 26 | 26,92% | +4,97% | -3,71% | -1,95% | +9,52% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 57 | 70,18% | +8,22% | +8,11% | -2,81% | +12,15% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 60 | 75,00% | +8,16% | +8,16% | -2,79% | +12,10% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 60 | 75,00% | +8,16% | +8,16% | -2,79% | +12,10% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 55 | 52,73% | +8,75% | +0,47% | -2,64% | +12,76% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 24 | 54,17% | +8,85% | -4,04% | -2,32% | +12,73% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 48 | 93,75% | +13,82% | +12,93% | -2,52% | +17,96% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 51 | 90,20% | +13,70% | +13,70% | -2,52% | +17,97% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 51 | 90,20% | +13,70% | +13,70% | -2,52% | +17,97% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 46 | 54,35% | +13,81% | -0,68% | -2,31% | +18,32% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 19 | 57,89% | +14,77% | -4,67% | -2,09% | +19,29% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +5,40% | +5,40% | -4,01% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 34 | 91,18% | +24,41% | +20,52% | -2,81% | +29,20% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 36 | 100,00% | +24,33% | +24,33% | -2,85% | +29,06% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 36 | 100,00% | +24,33% | +24,33% | -2,85% | +29,06% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 32 | 100,00% | +24,74% | +24,74% | -2,65% | +29,54% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 31 | 38,71% | +24,87% | -4,03% | -2,59% | +29,66% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 6 | 0,00% | +25,15% | -25,15% | -1,17% | +32,97% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 21 | 85,71% | +25,88% | +18,73% | -3,18% | +31,15% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 23 | 100,00% | +25,76% | +25,76% | -3,22% | +31,11% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 23 | 100,00% | +25,76% | +25,76% | -3,22% | +31,11% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 19 | 100,00% | +26,42% | +26,42% | -2,95% | +32,13% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 18 | 27,78% | +25,82% | -13,12% | -2,87% | +31,52% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 2 | 0,00% | +32,21% | -32,21% | -2,23% | +37,27% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 71 | 43,66% | +0,24% | -0,12% | -0,56% | +1,28% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 74 | 58,11% | +0,16% | +0,49% | -0,65% | +1,14% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 74 | 58,11% | +0,16% | +0,49% | -0,65% | +1,14% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 68 | 50,00% | +0,07% | +0,14% | -0,76% | +1,05% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 43 | 39,53% | +0,09% | -0,68% | -0,78% | +0,85% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 70 | 42,86% | +0,50% | -0,20% | -0,62% | +1,88% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 73 | 60,27% | +0,35% | +0,84% | -0,75% | +1,65% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 73 | 60,27% | +0,35% | +0,84% | -0,75% | +1,65% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 67 | 50,75% | +0,01% | +0,08% | -1,10% | +1,31% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 43 | 41,86% | +0,42% | -1,35% | -0,82% | +1,40% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 69 | 39,13% | +0,86% | -0,06% | -2,26% | +4,03% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 72 | 55,56% | +0,71% | +1,10% | -2,36% | +3,74% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 72 | 55,56% | +0,71% | +1,10% | -2,36% | +3,74% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 66 | 43,94% | +0,02% | -0,05% | -2,63% | +2,98% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 43 | 30,23% | +0,67% | -2,36% | -2,59% | +3,92% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 67 | 43,28% | +1,99% | +0,13% | -3,18% | +6,72% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 70 | 51,43% | +1,87% | +1,32% | -3,22% | +6,48% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 70 | 51,43% | +1,87% | +1,32% | -3,22% | +6,48% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 64 | 51,56% | +1,02% | -0,60% | -3,64% | +5,68% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 42 | 33,33% | +2,31% | -4,80% | -3,56% | +7,06% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 66 | 50,00% | +2,92% | +0,56% | -3,66% | +8,99% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 69 | 53,62% | +2,93% | +1,29% | -3,69% | +8,77% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 69 | 53,62% | +2,93% | +1,29% | -3,69% | +8,77% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 63 | 47,62% | +1,91% | -0,85% | -4,17% | +7,74% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 41 | 29,27% | +3,84% | -6,44% | -3,92% | +9,49% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 65 | 46,15% | +3,76% | +0,55% | -4,30% | +11,06% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 68 | 48,53% | +3,66% | +0,88% | -4,30% | +10,86% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 68 | 48,53% | +3,66% | +0,88% | -4,30% | +10,86% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 62 | 51,61% | +2,31% | -1,27% | -4,85% | +9,30% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 41 | 31,71% | +4,20% | -7,07% | -4,70% | +11,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 60,00% | +1,26% | +0,96% | -3,68% | +10,47% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 63 | 60,32% | +5,33% | +4,30% | -5,05% | +14,13% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 66 | 62,12% | +4,93% | +3,22% | -5,01% | +13,72% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 66 | 62,12% | +4,93% | +3,22% | -5,01% | +13,72% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 60 | 53,33% | +2,76% | -0,24% | -5,66% | +10,90% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 39 | 43,59% | +4,76% | -4,49% | -5,47% | +12,94% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +5,41% | +1,04% | -4,48% | +13,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 56 | 67,86% | +8,09% | +4,51% | -5,04% | +18,64% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 59 | 66,10% | +8,47% | +6,51% | -5,06% | +18,85% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 59 | 66,10% | +8,47% | +6,51% | -5,06% | +18,85% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 53 | 64,15% | +6,15% | -0,61% | -5,81% | +15,44% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 34 | 52,94% | +5,05% | -6,23% | -5,53% | +14,31% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 66,67% | +6,54% | +0,57% | -4,75% | +18,76% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 48 | 81,25% | +13,04% | +7,85% | -4,71% | +26,39% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 50 | 84,00% | +13,29% | +10,72% | -4,72% | +26,92% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 50 | 84,00% | +13,29% | +10,72% | -4,72% | +26,92% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 44 | 56,82% | +11,64% | -4,82% | -5,60% | +24,19% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 31 | 48,39% | +10,82% | -8,72% | -5,10% | +22,58% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 87,50% | +21,36% | +13,45% | -4,45% | +31,96% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 34 | 41,18% | +24,19% | +0,68% | -4,14% | +41,64% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 36 | 55,56% | +24,05% | +6,48% | -4,16% | +41,55% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 36 | 55,56% | +24,05% | +6,48% | -4,16% | +41,55% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 34 | 58,82% | +23,81% | +8,52% | -4,18% | +41,55% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 31 | 3,23% | +22,00% | -19,88% | -4,65% | +40,34% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 23 | 0,00% | +23,20% | -23,20% | -4,66% | +40,46% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +37,31% | +15,91% | -1,31% | +47,38% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 22 | 18,18% | +24,79% | -12,16% | -5,55% | +41,52% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 23 | 30,43% | +25,27% | -3,11% | -5,61% | +41,65% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 23 | 30,43% | +25,27% | -3,11% | -5,61% | +41,65% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 21 | 33,33% | +23,91% | +0,37% | -5,78% | +41,00% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 23 | 0,00% | +25,27% | -25,27% | -5,61% | +41,65% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 19 | 0,00% | +24,44% | -24,44% | -5,42% | +41,36% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 67 | 50,75% | +0,41% | +0,32% | -0,32% | +1,31% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 69 | 55,07% | +0,39% | +0,46% | -0,44% | +1,28% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 72 | 54,17% | +0,42% | +0,40% | -0,41% | +1,30% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 67 | 46,27% | +0,39% | -0,02% | -0,51% | +1,25% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 49 | 46,94% | +0,64% | +0,07% | -0,41% | +1,61% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 66 | 46,97% | +1,08% | +0,98% | -0,16% | +2,15% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 69 | 49,28% | +0,95% | +0,75% | -0,42% | +1,85% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 72 | 48,61% | +0,92% | +0,70% | -0,41% | +1,89% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 66 | 40,91% | +0,75% | -0,07% | -0,38% | +1,89% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 48 | 47,92% | +0,87% | +0,37% | -0,41% | +1,93% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 65 | 53,85% | +1,83% | +1,70% | -1,73% | +4,25% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 68 | 51,47% | +1,60% | +1,32% | -1,91% | +4,02% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 71 | 50,70% | +1,55% | +1,25% | -1,88% | +3,99% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 65 | 46,15% | +1,16% | -0,22% | -1,93% | +3,52% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 47 | 51,06% | +1,19% | +0,57% | -1,88% | +3,50% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 63 | 57,14% | +3,28% | +3,20% | -2,43% | +6,76% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 66 | 53,03% | +2,96% | +2,13% | -2,59% | +6,43% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 69 | 52,17% | +2,86% | +2,01% | -2,57% | +6,32% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 63 | 46,03% | +2,54% | -0,50% | -2,65% | +5,83% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 45 | 53,33% | +1,82% | +0,98% | -2,60% | +5,07% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 62 | 62,90% | +4,70% | +4,78% | -2,84% | +8,71% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 65 | 60,00% | +4,30% | +3,32% | -3,00% | +8,33% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 68 | 60,29% | +4,11% | +3,18% | -2,99% | +8,13% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 62 | 40,32% | +3,21% | -1,40% | -3,11% | +7,34% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 44 | 47,73% | +1,74% | +0,98% | -3,11% | +5,91% | PRIMA CALIBRAZIONE |
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
