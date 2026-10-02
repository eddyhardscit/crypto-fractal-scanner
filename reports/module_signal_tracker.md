# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-02 14:08 UTC

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

Segnali totali salvati: **234**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-02 | BTC | 86.570,73 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-10-02 | DOGE | 0.09654 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-10-02 | SOL | 121,92 | +1 | -2 | -2 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-30 | BTC | 83.418,75 | +3 | 0 | 0 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-30 | DOGE | 0.09397 | +3 | -1 | -1 | 0 | +3 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-30 | SOL | 119,28 | +1 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-29 | BTC | 83.140,92 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-29 | DOGE | 0.09319 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-29 | SOL | 117,59 | +1 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-28 | BTC | 82.981,23 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-28 | DOGE | 0.09299 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-28 | SOL | 118,67 | +4 | 0 | 0 | 0 | +2 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 78 | 77 | 77 | 76 | 74 | 72 | 70 | 69 | 63 | 54 | 39 | 26 |
| SOL | 78 | 77 | 77 | 76 | 74 | 72 | 70 | 69 | 63 | 54 | 39 | 26 |
| DOGE | 78 | 77 | 77 | 76 | 74 | 72 | 70 | 69 | 63 | 54 | 39 | 26 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-04 | 60g | 2026-10-03 | domani |
| SOL | 2026-08-04 | 60g | 2026-10-03 | domani |
| DOGE | 2026-08-04 | 60g | 2026-10-03 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 72 | 52,78% | +0,38% | +0,36% | UTILE |
| BTC | 2g | 72 | 52,78% | +0,68% | +0,62% | UTILE |
| BTC | 3g | 71 | 46,48% | +0,85% | +0,75% | UTILE |
| BTC | 5g | 69 | 43,48% | +1,70% | +1,51% | UTILE |
| BTC | 7g | 69 | 53,62% | +2,47% | +2,32% | UTILE |
| BTC | 10g | 67 | 62,69% | +3,59% | +3,45% | UTILE |
| BTC | 14g | 66 | 62,12% | +5,13% | +5,08% | UTILE |
| BTC | 21g | 60 | 71,67% | +8,25% | +8,14% | UTILE |
| BTC | 30g | 51 | 94,12% | +13,52% | +12,67% | PRIMA CALIBRAZIONE |
| BTC | 45g | 36 | 91,67% | +24,89% | +21,22% | PRIMA CALIBRAZIONE |
| BTC | 60g | 24 | 87,50% | +26,98% | +20,73% | FEEDBACK RAPIDO |
| SOL | 1g | 69 | 50,72% | +0,41% | +0,32% | UTILE |
| SOL | 2g | 69 | 49,28% | +1,09% | +0,98% | UTILE |
| SOL | 3g | 68 | 52,94% | +1,79% | +1,66% | UTILE |
| SOL | 5g | 66 | 56,06% | +3,09% | +3,01% | UTILE |
| SOL | 7g | 64 | 62,50% | +4,55% | +4,64% | UTILE |
| SOL | 10g | 62 | 67,74% | +6,76% | +6,88% | UTILE |
| SOL | 14g | 61 | 75,41% | +9,69% | +10,29% | UTILE |
| SOL | 21g | 56 | 82,14% | +14,87% | +14,23% | PRIMA CALIBRAZIONE |
| SOL | 30g | 47 | 78,72% | +22,11% | +17,90% | PRIMA CALIBRAZIONE |
| SOL | 45g | 32 | 65,62% | +42,41% | +18,35% | PRIMA CALIBRAZIONE |
| SOL | 60g | 20 | 45,00% | +44,32% | +0,50% | FEEDBACK RAPIDO |
| DOGE | 1g | 73 | 45,21% | +0,25% | -0,10% | UTILE |
| DOGE | 2g | 73 | 45,21% | +0,55% | -0,13% | UTILE |
| DOGE | 3g | 72 | 40,28% | +0,86% | -0,02% | UTILE |
| DOGE | 5g | 70 | 42,86% | +1,80% | +0,02% | UTILE |
| DOGE | 7g | 68 | 48,53% | +2,68% | +0,38% | UTILE |
| DOGE | 10g | 66 | 45,45% | +3,67% | +0,51% | UTILE |
| DOGE | 14g | 65 | 58,46% | +5,69% | +3,65% | UTILE |
| DOGE | 21g | 59 | 66,10% | +8,17% | +3,93% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 50 | 78,00% | +13,13% | +6,92% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 37 | 45,95% | +25,15% | +3,54% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 25 | 20,00% | +26,08% | -12,21% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 72 | 52,78% | +0,38% | +0,36% | -0,19% | +0,90% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 76 | 51,32% | +0,32% | +0,33% | -0,20% | +0,84% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 76 | 51,32% | +0,32% | +0,33% | -0,20% | +0,84% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 70 | 42,86% | +0,34% | +0,05% | -0,14% | +0,87% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 29 | 37,93% | +0,73% | +0,06% | -0,13% | +1,26% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,24% | -0,24% | -0,87% | +0,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 72 | 52,78% | +0,68% | +0,62% | -0,14% | +1,37% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 76 | 52,63% | +0,66% | +0,66% | -0,09% | +1,36% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 76 | 52,63% | +0,66% | +0,66% | -0,09% | +1,36% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 70 | 44,29% | +0,66% | +0,07% | +0,01% | +1,36% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 29 | 41,38% | +1,20% | +0,02% | +0,19% | +1,90% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,04% | -0,04% | -0,90% | +1,02% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 71 | 46,48% | +0,85% | +0,75% | -1,18% | +2,56% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 76 | 51,32% | +1,02% | +0,91% | -1,17% | +2,70% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 76 | 51,32% | +1,02% | +0,91% | -1,17% | +2,70% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 69 | 36,23% | +1,07% | -0,15% | -1,09% | +2,75% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 29 | 37,93% | +1,95% | -0,51% | -0,85% | +3,41% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 69 | 43,48% | +1,70% | +1,51% | -1,80% | +4,03% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 74 | 47,30% | +1,89% | +1,79% | -1,77% | +4,23% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 74 | 47,30% | +1,89% | +1,79% | -1,77% | +4,23% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 67 | 41,79% | +1,82% | -0,71% | -1,70% | +4,20% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 29 | 41,38% | +4,06% | -2,25% | -1,22% | +6,21% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 14,29% | -1,43% | -1,43% | -2,57% | +1,68% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 69 | 53,62% | +2,47% | +2,32% | -2,11% | +5,23% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 72 | 58,33% | +2,72% | +2,72% | -2,08% | +5,45% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 72 | 58,33% | +2,72% | +2,72% | -2,08% | +5,45% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 65 | 43,08% | +2,80% | -1,13% | -2,01% | +5,50% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 29 | 37,93% | +5,44% | -4,00% | -1,49% | +8,41% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -1,74% | -1,74% | -3,24% | +1,77% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 67 | 62,69% | +3,59% | +3,45% | -2,37% | +6,58% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 70 | 65,71% | +3,71% | +3,71% | -2,36% | +6,76% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 70 | 65,71% | +3,71% | +3,71% | -2,36% | +6,76% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 63 | 50,79% | +3,88% | -0,34% | -2,29% | +6,94% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 28 | 42,86% | +5,84% | -4,46% | -1,59% | +9,49% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 50,00% | -1,01% | -1,01% | -3,64% | +2,39% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 66 | 62,12% | +5,13% | +5,08% | -2,59% | +8,79% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 69 | 62,32% | +5,20% | +5,20% | -2,57% | +8,87% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 69 | 62,32% | +5,20% | +5,20% | -2,57% | +8,87% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 62 | 58,06% | +5,55% | +1,64% | -2,50% | +9,26% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 28 | 25,00% | +5,37% | -4,20% | -1,80% | +9,90% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 60 | 71,67% | +8,25% | +8,14% | -2,87% | +12,13% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 63 | 76,19% | +8,18% | +8,18% | -2,85% | +12,09% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 63 | 76,19% | +8,18% | +8,18% | -2,85% | +12,09% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 58 | 55,17% | +8,75% | +0,90% | -2,71% | +12,71% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 24 | 54,17% | +8,85% | -4,04% | -2,32% | +12,73% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 51 | 94,12% | +13,52% | +12,67% | -2,62% | +17,59% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 54 | 90,74% | +13,41% | +13,41% | -2,61% | +17,62% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 54 | 90,74% | +13,41% | +13,41% | -2,61% | +17,62% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 49 | 57,14% | +13,49% | -0,11% | -2,42% | +17,91% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 22 | 63,64% | +13,93% | -2,86% | -2,38% | +18,25% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +5,40% | +5,40% | -4,01% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 36 | 91,67% | +24,89% | +21,22% | -2,64% | +29,70% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 39 | 100,00% | +25,05% | +25,05% | -2,63% | +29,71% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 39 | 100,00% | +25,05% | +25,05% | -2,63% | +29,71% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 34 | 100,00% | +25,23% | +25,23% | -2,48% | +30,05% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 34 | 35,29% | +25,65% | -6,65% | -2,36% | +30,35% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 8 | 0,00% | +27,13% | -27,13% | -0,83% | +34,28% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 24 | 87,50% | +26,98% | +20,73% | -2,93% | +32,07% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 26 | 100,00% | +26,79% | +26,79% | -2,98% | +31,96% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 26 | 100,00% | +26,79% | +26,79% | -2,98% | +31,96% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 22 | 100,00% | +27,55% | +27,55% | -2,71% | +33,00% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 21 | 23,81% | +27,08% | -16,20% | -2,63% | +32,52% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 4 | 0,00% | +33,67% | -33,67% | -1,55% | +38,08% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 73 | 45,21% | +0,25% | -0,10% | -0,55% | +1,29% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 76 | 56,58% | +0,17% | +0,46% | -0,63% | +1,15% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 76 | 56,58% | +0,17% | +0,46% | -0,63% | +1,15% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 70 | 51,43% | +0,09% | +0,15% | -0,74% | +1,07% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 43 | 39,53% | +0,09% | -0,68% | -0,78% | +0,85% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 73 | 45,21% | +0,55% | -0,13% | -0,61% | +1,94% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 76 | 57,89% | +0,40% | +0,74% | -0,73% | +1,72% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 76 | 57,89% | +0,40% | +0,74% | -0,73% | +1,72% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 70 | 52,86% | +0,09% | +0,15% | -1,06% | +1,40% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 43 | 41,86% | +0,42% | -1,35% | -0,82% | +1,40% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 72 | 40,28% | +0,86% | -0,02% | -2,25% | +4,03% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 75 | 54,67% | +0,72% | +1,01% | -2,34% | +3,74% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 75 | 54,67% | +0,72% | +1,01% | -2,34% | +3,74% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 69 | 44,93% | +0,06% | -0,01% | -2,60% | +3,02% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 43 | 30,23% | +0,67% | -2,36% | -2,59% | +3,92% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 70 | 42,86% | +1,80% | +0,02% | -3,29% | +6,49% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 73 | 52,05% | +1,69% | +1,37% | -3,32% | +6,26% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 73 | 52,05% | +1,69% | +1,37% | -3,32% | +6,26% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 67 | 50,75% | +0,86% | -0,69% | -3,73% | +5,48% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 43 | 32,56% | +2,13% | -4,81% | -3,64% | +6,91% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 68 | 48,53% | +2,68% | +0,38% | -3,81% | +8,69% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 71 | 54,93% | +2,70% | +1,41% | -3,83% | +8,50% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 71 | 54,93% | +2,70% | +1,41% | -3,83% | +8,50% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 65 | 46,15% | +1,69% | -0,99% | -4,31% | +7,47% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 43 | 27,91% | +3,41% | -6,38% | -4,15% | +8,99% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 66 | 45,45% | +3,67% | +0,51% | -4,34% | +10,98% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 69 | 49,28% | +3,58% | +0,90% | -4,33% | +10,79% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 69 | 49,28% | +3,58% | +0,90% | -4,33% | +10,79% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 63 | 50,79% | +2,24% | -1,28% | -4,88% | +9,24% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 41 | 31,71% | +4,20% | -7,07% | -4,70% | +11,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 65 | 58,46% | +5,69% | +3,65% | -4,87% | +14,65% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 68 | 60,29% | +5,28% | +2,62% | -4,85% | +14,22% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 68 | 60,29% | +5,28% | +2,62% | -4,85% | +14,22% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 62 | 51,61% | +3,22% | -0,78% | -5,45% | +11,54% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 41 | 41,46% | +5,35% | -5,10% | -5,18% | +13,82% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 50,00% | +6,54% | +2,61% | -3,97% | +15,08% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 59 | 66,10% | +8,17% | +3,93% | -5,27% | +18,79% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 62 | 62,90% | +8,53% | +5,72% | -5,28% | +18,98% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 62 | 62,90% | +8,53% | +5,72% | -5,28% | +18,98% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 56 | 62,50% | +6,34% | -0,95% | -6,01% | +15,77% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 35 | 51,43% | +5,33% | -6,48% | -5,56% | +14,63% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 66,67% | +6,54% | +0,57% | -4,75% | +18,76% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 50 | 78,00% | +13,13% | +6,92% | -4,73% | +26,43% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 53 | 79,25% | +13,37% | +9,28% | -4,74% | +26,94% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 53 | 79,25% | +13,37% | +9,28% | -4,74% | +26,94% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 47 | 59,57% | +11,84% | -3,57% | -5,58% | +24,39% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 31 | 48,39% | +10,82% | -8,72% | -5,10% | +22,58% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 87,50% | +21,36% | +13,45% | -4,45% | +31,96% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 37 | 45,95% | +25,15% | +3,54% | -3,82% | +42,38% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 39 | 58,97% | +24,97% | +8,75% | -3,86% | +42,26% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 39 | 58,97% | +24,97% | +8,75% | -3,86% | +42,26% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 37 | 62,16% | +24,80% | +10,75% | -3,86% | +42,30% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 33 | 6,06% | +22,77% | -18,67% | -4,39% | +40,97% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 26 | 0,00% | +24,68% | -24,68% | -4,15% | +41,65% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +37,31% | +15,91% | -1,31% | +47,38% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 25 | 20,00% | +26,08% | -12,21% | -5,18% | +42,58% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 26 | 38,46% | +26,46% | +1,36% | -5,24% | +42,65% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 26 | 38,46% | +26,46% | +1,36% | -5,24% | +42,65% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 24 | 41,67% | +25,37% | +4,77% | -5,36% | +42,16% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 26 | 0,00% | +26,46% | -26,46% | -5,24% | +42,65% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 20 | 0,00% | +24,92% | -24,92% | -5,27% | +41,80% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 69 | 50,72% | +0,41% | +0,32% | -0,33% | +1,30% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 71 | 54,93% | +0,39% | +0,44% | -0,45% | +1,27% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 74 | 54,05% | +0,42% | +0,38% | -0,41% | +1,29% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 69 | 46,38% | +0,39% | -0,01% | -0,51% | +1,24% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 51 | 47,06% | +0,63% | +0,08% | -0,42% | +1,58% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 69 | 49,28% | +1,09% | +0,98% | -0,19% | +2,18% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 71 | 47,89% | +0,96% | +0,69% | -0,45% | +1,91% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 74 | 47,30% | +0,94% | +0,64% | -0,43% | +1,94% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 69 | 43,48% | +0,77% | -0,01% | -0,40% | +1,93% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 51 | 50,98% | +0,89% | +0,41% | -0,44% | +1,98% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 68 | 52,94% | +1,79% | +1,66% | -1,73% | +4,21% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 70 | 51,43% | +1,59% | +1,24% | -1,90% | +4,00% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 73 | 50,68% | +1,54% | +1,18% | -1,87% | +3,97% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 68 | 45,59% | +1,14% | -0,17% | -1,92% | +3,51% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 50 | 50,00% | +1,16% | +0,59% | -1,87% | +3,49% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 66 | 56,06% | +3,09% | +3,01% | -2,48% | +6,57% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 69 | 53,62% | +2,79% | +2,08% | -2,63% | +6,26% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 72 | 52,78% | +2,70% | +1,97% | -2,60% | +6,17% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 66 | 45,45% | +2,38% | -0,52% | -2,69% | +5,69% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 48 | 52,08% | +1,65% | +0,86% | -2,66% | +4,92% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 64 | 62,50% | +4,55% | +4,64% | -2,90% | +8,55% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 67 | 61,19% | +4,17% | +3,23% | -3,05% | +8,18% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 70 | 61,43% | +3,99% | +3,10% | -3,04% | +8,00% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 64 | 40,62% | +3,12% | -1,35% | -3,16% | +7,22% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 46 | 47,83% | +1,67% | +0,94% | -3,19% | +5,80% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 62 | 67,74% | +6,76% | +6,88% | -3,20% | +11,01% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 65 | 64,62% | +6,36% | +5,65% | -3,40% | +10,43% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 68 | 63,24% | +6,07% | +5,41% | -3,40% | +10,14% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 62 | 48,39% | +4,63% | -1,48% | -3,57% | +8,96% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 44 | 54,55% | +2,14% | +1,25% | -3,66% | +6,82% | PRIMA CALIBRAZIONE |

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
