# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-30 05:33 UTC

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

Segnali totali salvati: **231**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-30 | BTC | 83.418,75 | +3 | 0 | 0 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-30 | DOGE | 0.09397 | +3 | -1 | -1 | 0 | +3 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-30 | SOL | 119,28 | +1 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-29 | BTC | 83.140,92 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-29 | DOGE | 0.09319 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-29 | SOL | 117,59 | +1 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-28 | BTC | 82.981,23 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-28 | DOGE | 0.09299 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-28 | SOL | 118,67 | +4 | 0 | 0 | 0 | +2 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-27 | BTC | 84.404,98 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-27 | DOGE | 0.09592 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-27 | SOL | 120,66 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 77 | 76 | 75 | 74 | 72 | 71 | 69 | 68 | 61 | 52 | 37 | 24 |
| SOL | 77 | 76 | 75 | 74 | 72 | 71 | 69 | 68 | 61 | 52 | 37 | 24 |
| DOGE | 77 | 76 | 75 | 74 | 72 | 71 | 69 | 68 | 61 | 52 | 37 | 24 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-02 | 60g | 2026-10-01 | domani |
| SOL | 2026-08-02 | 60g | 2026-10-01 | domani |
| DOGE | 2026-08-02 | 60g | 2026-10-01 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 71 | 52,11% | +0,36% | +0,34% | UTILE |
| BTC | 2g | 70 | 51,43% | +0,62% | +0,55% | UTILE |
| BTC | 3g | 69 | 44,93% | +0,78% | +0,68% | UTILE |
| BTC | 5g | 69 | 43,48% | +1,70% | +1,51% | UTILE |
| BTC | 7g | 68 | 52,94% | +2,47% | +2,31% | UTILE |
| BTC | 10g | 66 | 62,12% | +3,62% | +3,48% | UTILE |
| BTC | 14g | 65 | 61,54% | +5,04% | +4,99% | UTILE |
| BTC | 21g | 58 | 70,69% | +8,18% | +8,06% | PRIMA CALIBRAZIONE |
| BTC | 30g | 49 | 93,88% | +13,68% | +12,80% | PRIMA CALIBRAZIONE |
| BTC | 45g | 35 | 91,43% | +24,64% | +20,86% | PRIMA CALIBRAZIONE |
| BTC | 60g | 22 | 86,36% | +26,17% | +19,35% | FEEDBACK RAPIDO |
| SOL | 1g | 68 | 51,47% | +0,43% | +0,33% | UTILE |
| SOL | 2g | 67 | 47,76% | +1,08% | +0,97% | UTILE |
| SOL | 3g | 66 | 53,03% | +1,79% | +1,65% | UTILE |
| SOL | 5g | 64 | 56,25% | +3,20% | +3,11% | UTILE |
| SOL | 7g | 63 | 63,49% | +4,63% | +4,71% | UTILE |
| SOL | 10g | 61 | 67,21% | +6,78% | +6,90% | UTILE |
| SOL | 14g | 61 | 75,41% | +9,69% | +10,29% | UTILE |
| SOL | 21g | 54 | 81,48% | +14,71% | +14,05% | PRIMA CALIBRAZIONE |
| SOL | 30g | 45 | 77,78% | +22,30% | +17,91% | PRIMA CALIBRAZIONE |
| SOL | 45g | 30 | 63,33% | +41,29% | +15,64% | PRIMA CALIBRAZIONE |
| SOL | 60g | 18 | 38,89% | +42,11% | -6,58% | FEEDBACK RAPIDO |
| DOGE | 1g | 72 | 44,44% | +0,25% | -0,11% | UTILE |
| DOGE | 2g | 71 | 43,66% | +0,51% | -0,19% | UTILE |
| DOGE | 3g | 70 | 38,57% | +0,82% | -0,09% | UTILE |
| DOGE | 5g | 68 | 42,65% | +1,89% | +0,06% | UTILE |
| DOGE | 7g | 67 | 49,25% | +2,76% | +0,43% | UTILE |
| DOGE | 10g | 65 | 46,15% | +3,76% | +0,55% | UTILE |
| DOGE | 14g | 64 | 59,38% | +5,52% | +3,96% | UTILE |
| DOGE | 21g | 57 | 68,42% | +8,02% | +4,50% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 48 | 81,25% | +13,04% | +7,85% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 35 | 42,86% | +24,50% | +1,66% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 23 | 17,39% | +25,19% | -13,11% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 71 | 52,11% | +0,36% | +0,34% | -0,18% | +0,88% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 76 | 51,32% | +0,32% | +0,33% | -0,20% | +0,84% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 76 | 51,32% | +0,32% | +0,33% | -0,20% | +0,84% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 69 | 42,03% | +0,33% | +0,03% | -0,14% | +0,85% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 29 | 37,93% | +0,73% | +0,06% | -0,13% | +1,26% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,24% | -0,24% | -0,87% | +0,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 70 | 51,43% | +0,62% | +0,55% | -0,14% | +1,30% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 75 | 53,33% | +0,64% | +0,70% | -0,09% | +1,34% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 75 | 53,33% | +0,64% | +0,70% | -0,09% | +1,34% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 68 | 42,65% | +0,59% | -0,01% | +0,02% | +1,29% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 29 | 41,38% | +1,20% | +0,02% | +0,19% | +1,90% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,04% | -0,04% | -0,90% | +1,02% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 69 | 44,93% | +0,78% | +0,68% | -1,21% | +2,52% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 74 | 52,70% | +0,96% | +1,02% | -1,20% | +2,66% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 74 | 52,70% | +0,96% | +1,02% | -1,20% | +2,66% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 67 | 34,33% | +1,01% | -0,25% | -1,12% | +2,71% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 29 | 37,93% | +1,95% | -0,51% | -0,85% | +3,41% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 69 | 43,48% | +1,70% | +1,51% | -1,80% | +4,03% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 72 | 48,61% | +1,89% | +1,89% | -1,77% | +4,27% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 72 | 48,61% | +1,89% | +1,89% | -1,77% | +4,27% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 65 | 40,00% | +1,81% | -0,79% | -1,69% | +4,25% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 29 | 41,38% | +4,06% | -2,25% | -1,22% | +6,21% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 14,29% | -1,43% | -1,43% | -2,57% | +1,68% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 68 | 52,94% | +2,47% | +2,31% | -2,11% | +5,25% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 71 | 57,75% | +2,71% | +2,71% | -2,08% | +5,48% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 71 | 57,75% | +2,71% | +2,71% | -2,08% | +5,48% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 64 | 42,19% | +2,79% | -1,19% | -2,02% | +5,53% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 29 | 37,93% | +5,44% | -4,00% | -1,49% | +8,41% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -1,74% | -1,74% | -3,24% | +1,77% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 66 | 62,12% | +3,62% | +3,48% | -2,36% | +6,64% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 69 | 65,22% | +3,74% | +3,74% | -2,35% | +6,82% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 69 | 65,22% | +3,74% | +3,74% | -2,35% | +6,82% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 62 | 50,00% | +3,92% | -0,37% | -2,28% | +7,01% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 28 | 42,86% | +5,84% | -4,46% | -1,59% | +9,49% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 65 | 61,54% | +5,04% | +4,99% | -2,63% | +8,70% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 68 | 61,76% | +5,11% | +5,11% | -2,61% | +8,79% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 68 | 61,76% | +5,11% | +5,11% | -2,61% | +8,79% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 62 | 58,06% | +5,55% | +1,64% | -2,50% | +9,26% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 27 | 25,93% | +5,15% | -3,94% | -1,87% | +9,73% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 58 | 70,69% | +8,18% | +8,06% | -2,85% | +12,13% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 61 | 75,41% | +8,11% | +8,11% | -2,83% | +12,08% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 61 | 75,41% | +8,11% | +8,11% | -2,83% | +12,08% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 56 | 53,57% | +8,70% | +0,56% | -2,68% | +12,72% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 24 | 54,17% | +8,85% | -4,04% | -2,32% | +12,73% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 49 | 93,88% | +13,68% | +12,80% | -2,55% | +17,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 52 | 90,38% | +13,57% | +13,57% | -2,55% | +17,86% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 52 | 90,38% | +13,57% | +13,57% | -2,55% | +17,86% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 47 | 55,32% | +13,66% | -0,51% | -2,34% | +18,18% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 20 | 60,00% | +14,38% | -4,09% | -2,18% | +18,93% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +5,40% | +5,40% | -4,01% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 35 | 91,43% | +24,64% | +20,86% | -2,74% | +29,47% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 37 | 100,00% | +24,55% | +24,55% | -2,79% | +29,32% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 37 | 100,00% | +24,55% | +24,55% | -2,79% | +29,32% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 33 | 100,00% | +24,97% | +24,97% | -2,58% | +29,81% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 32 | 37,50% | +25,10% | -4,92% | -2,53% | +29,94% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 7 | 0,00% | +26,18% | -26,18% | -1,07% | +33,78% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 22 | 86,36% | +26,17% | +19,35% | -3,09% | +31,48% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 24 | 100,00% | +26,03% | +26,03% | -3,14% | +31,42% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 24 | 100,00% | +26,03% | +26,03% | -3,14% | +31,42% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 20 | 100,00% | +26,71% | +26,71% | -2,87% | +32,45% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 19 | 26,32% | +26,16% | -14,13% | -2,79% | +31,89% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 3 | 0,00% | +32,24% | -32,24% | -1,93% | +37,69% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 72 | 44,44% | +0,25% | -0,11% | -0,55% | +1,28% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 75 | 57,33% | +0,17% | +0,48% | -0,64% | +1,14% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 75 | 57,33% | +0,17% | +0,48% | -0,64% | +1,14% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 69 | 50,72% | +0,09% | +0,15% | -0,75% | +1,05% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 43 | 39,53% | +0,09% | -0,68% | -0,78% | +0,85% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 71 | 43,66% | +0,51% | -0,19% | -0,61% | +1,87% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 74 | 59,46% | +0,36% | +0,81% | -0,73% | +1,65% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 74 | 59,46% | +0,36% | +0,81% | -0,73% | +1,65% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 68 | 51,47% | +0,03% | +0,09% | -1,08% | +1,31% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 43 | 41,86% | +0,42% | -1,35% | -0,82% | +1,40% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 70 | 38,57% | +0,82% | -0,09% | -2,29% | +4,00% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 73 | 56,16% | +0,67% | +1,11% | -2,39% | +3,71% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 73 | 56,16% | +0,67% | +1,11% | -2,39% | +3,71% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 67 | 43,28% | -0,01% | -0,08% | -2,66% | +2,97% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 43 | 30,23% | +0,67% | -2,36% | -2,59% | +3,92% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 68 | 42,65% | +1,89% | +0,06% | -3,24% | +6,63% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 71 | 52,11% | +1,77% | +1,37% | -3,28% | +6,39% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 71 | 52,11% | +1,77% | +1,37% | -3,28% | +6,39% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 65 | 50,77% | +0,92% | -0,67% | -3,69% | +5,59% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 43 | 32,56% | +2,13% | -4,81% | -3,64% | +6,91% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 67 | 49,25% | +2,76% | +0,43% | -3,76% | +8,81% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 70 | 54,29% | +2,77% | +1,39% | -3,78% | +8,61% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 70 | 54,29% | +2,77% | +1,39% | -3,78% | +8,61% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 64 | 46,88% | +1,75% | -0,96% | -4,27% | +7,58% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 42 | 28,57% | +3,56% | -6,47% | -4,07% | +9,20% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 65 | 46,15% | +3,76% | +0,55% | -4,30% | +11,06% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 68 | 48,53% | +3,66% | +0,88% | -4,30% | +10,86% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 68 | 48,53% | +3,66% | +0,88% | -4,30% | +10,86% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 62 | 51,61% | +2,31% | -1,27% | -4,85% | +9,30% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 41 | 31,71% | +4,20% | -7,07% | -4,70% | +11,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 60,00% | +1,26% | +0,96% | -3,68% | +10,47% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 64 | 59,38% | +5,52% | +3,96% | -4,96% | +14,40% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 67 | 61,19% | +5,11% | +2,91% | -4,93% | +13,98% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 67 | 61,19% | +5,11% | +2,91% | -4,93% | +13,98% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 61 | 52,46% | +3,00% | -0,52% | -5,55% | +11,23% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 40 | 42,50% | +5,07% | -4,81% | -5,32% | +13,41% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +5,41% | +1,04% | -4,48% | +13,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 57 | 68,42% | +8,02% | +4,50% | -5,18% | +18,60% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 60 | 65,00% | +8,40% | +6,33% | -5,20% | +18,82% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 60 | 65,00% | +8,40% | +6,33% | -5,20% | +18,82% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 54 | 64,81% | +6,11% | -0,52% | -5,95% | +15,46% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 34 | 52,94% | +5,05% | -6,23% | -5,53% | +14,31% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 66,67% | +6,54% | +0,57% | -4,75% | +18,76% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 48 | 81,25% | +13,04% | +7,85% | -4,71% | +26,39% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 51 | 82,35% | +13,29% | +10,25% | -4,73% | +26,92% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 51 | 82,35% | +13,29% | +10,25% | -4,73% | +26,92% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 45 | 57,78% | +11,68% | -4,42% | -5,59% | +24,26% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 31 | 48,39% | +10,82% | -8,72% | -5,10% | +22,58% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 87,50% | +21,36% | +13,45% | -4,45% | +31,96% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 35 | 42,86% | +24,50% | +1,66% | -4,03% | +41,91% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 37 | 56,76% | +24,35% | +7,24% | -4,05% | +41,81% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 37 | 56,76% | +24,35% | +7,24% | -4,05% | +41,81% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +24,12% | +9,27% | -4,07% | +41,82% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 32 | 6,25% | +22,40% | -18,17% | -4,51% | +40,68% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 24 | 0,00% | +23,68% | -23,68% | -4,47% | +40,90% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +37,31% | +15,91% | -1,31% | +47,38% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 23 | 17,39% | +25,19% | -13,11% | -5,42% | +41,90% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 24 | 33,33% | +25,64% | -1,56% | -5,48% | +42,01% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 24 | 33,33% | +25,64% | -1,56% | -5,48% | +42,01% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 22 | 36,36% | +24,37% | +1,90% | -5,63% | +41,41% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 24 | 0,00% | +25,64% | -25,64% | -5,48% | +42,01% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 20 | 0,00% | +24,92% | -24,92% | -5,27% | +41,80% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 68 | 51,47% | +0,43% | +0,33% | -0,30% | +1,32% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 70 | 54,29% | +0,41% | +0,44% | -0,42% | +1,29% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 73 | 53,42% | +0,44% | +0,37% | -0,39% | +1,31% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 68 | 47,06% | +0,40% | -0,00% | -0,49% | +1,26% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 50 | 48,00% | +0,65% | +0,09% | -0,38% | +1,61% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 67 | 47,76% | +1,08% | +0,97% | -0,16% | +2,14% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 69 | 49,28% | +0,95% | +0,75% | -0,42% | +1,85% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 72 | 48,61% | +0,92% | +0,70% | -0,41% | +1,89% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 67 | 41,79% | +0,75% | -0,06% | -0,38% | +1,87% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 49 | 48,98% | +0,86% | +0,37% | -0,40% | +1,91% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 66 | 53,03% | +1,79% | +1,65% | -1,75% | +4,21% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 69 | 52,17% | +1,56% | +1,31% | -1,92% | +3,99% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 72 | 51,39% | +1,51% | +1,25% | -1,89% | +3,96% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 66 | 45,45% | +1,12% | -0,23% | -1,94% | +3,50% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 48 | 50,00% | +1,14% | +0,54% | -1,90% | +3,47% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 64 | 56,25% | +3,20% | +3,11% | -2,45% | +6,69% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 67 | 53,73% | +2,88% | +2,13% | -2,61% | +6,37% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 70 | 52,86% | +2,79% | +2,01% | -2,58% | +6,26% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 64 | 45,31% | +2,46% | -0,53% | -2,67% | +5,77% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 46 | 52,17% | +1,73% | +0,91% | -2,63% | +5,01% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 63 | 63,49% | +4,63% | +4,71% | -2,87% | +8,65% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 66 | 60,61% | +4,24% | +3,28% | -3,03% | +8,28% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 69 | 60,87% | +4,05% | +3,14% | -3,02% | +8,09% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 63 | 41,27% | +3,17% | -1,37% | -3,14% | +7,30% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 45 | 48,89% | +1,71% | +0,97% | -3,16% | +5,88% | PRIMA CALIBRAZIONE |
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
