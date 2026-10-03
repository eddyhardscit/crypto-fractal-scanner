# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-03 05:33 UTC

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

Segnali totali salvati: **237**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-03 | BTC | 84.628,98 | +1 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-03 | DOGE | 0.09320 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-03 | SOL | 119,63 | +3 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-02 | BTC | 86.570,73 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-10-02 | DOGE | 0.09654 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-10-02 | SOL | 121,92 | +1 | -2 | -2 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-30 | BTC | 83.418,75 | +3 | 0 | 0 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-30 | DOGE | 0.09397 | +3 | -1 | -1 | 0 | +3 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-30 | SOL | 119,28 | +1 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-29 | BTC | 83.140,92 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-29 | DOGE | 0.09319 | +2 | -1 | -1 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-29 | SOL | 117,59 | +1 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79 | 78 | 77 | 77 | 75 | 73 | 71 | 69 | 64 | 55 | 40 | 27 |
| SOL | 79 | 78 | 77 | 77 | 75 | 73 | 71 | 69 | 64 | 55 | 40 | 27 |
| DOGE | 79 | 78 | 77 | 77 | 75 | 73 | 71 | 69 | 64 | 55 | 40 | 27 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-05 | 60g | 2026-10-04 | domani |
| SOL | 2026-08-05 | 60g | 2026-10-04 | domani |
| DOGE | 2026-08-05 | 60g | 2026-10-04 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 73 | 52,05% | +0,34% | +0,33% | UTILE |
| BTC | 2g | 72 | 52,78% | +0,68% | +0,62% | UTILE |
| BTC | 3g | 72 | 47,22% | +0,86% | +0,76% | UTILE |
| BTC | 5g | 70 | 44,29% | +1,70% | +1,52% | UTILE |
| BTC | 7g | 69 | 53,62% | +2,47% | +2,32% | UTILE |
| BTC | 10g | 68 | 61,76% | +3,50% | +3,37% | UTILE |
| BTC | 14g | 66 | 62,12% | +5,13% | +5,08% | UTILE |
| BTC | 21g | 61 | 72,13% | +8,27% | +8,16% | UTILE |
| BTC | 30g | 52 | 94,23% | +13,44% | +12,61% | PRIMA CALIBRAZIONE |
| BTC | 45g | 37 | 91,89% | +25,08% | +21,50% | PRIMA CALIBRAZIONE |
| BTC | 60g | 25 | 88,00% | +27,21% | +21,20% | FEEDBACK RAPIDO |
| SOL | 1g | 70 | 50,00% | +0,38% | +0,29% | UTILE |
| SOL | 2g | 69 | 49,28% | +1,09% | +0,98% | UTILE |
| SOL | 3g | 69 | 53,62% | +1,76% | +1,64% | UTILE |
| SOL | 5g | 67 | 56,72% | +3,06% | +2,97% | UTILE |
| SOL | 7g | 65 | 61,54% | +4,47% | +4,55% | UTILE |
| SOL | 10g | 63 | 68,25% | +6,66% | +6,78% | UTILE |
| SOL | 14g | 61 | 75,41% | +9,69% | +10,29% | UTILE |
| SOL | 21g | 57 | 82,46% | +14,92% | +14,29% | PRIMA CALIBRAZIONE |
| SOL | 30g | 48 | 79,17% | +22,05% | +17,93% | PRIMA CALIBRAZIONE |
| SOL | 45g | 33 | 66,67% | +42,81% | +19,48% | PRIMA CALIBRAZIONE |
| SOL | 60g | 20 | 45,00% | +44,32% | +0,50% | FEEDBACK RAPIDO |
| DOGE | 1g | 74 | 44,59% | +0,20% | -0,15% | UTILE |
| DOGE | 2g | 73 | 45,21% | +0,55% | -0,13% | UTILE |
| DOGE | 3g | 73 | 39,73% | +0,84% | -0,03% | UTILE |
| DOGE | 5g | 71 | 43,66% | +1,78% | +0,02% | UTILE |
| DOGE | 7g | 69 | 47,83% | +2,58% | +0,32% | UTILE |
| DOGE | 10g | 67 | 44,78% | +3,49% | +0,37% | UTILE |
| DOGE | 14g | 65 | 58,46% | +5,69% | +3,65% | UTILE |
| DOGE | 21g | 60 | 65,00% | +8,21% | +3,69% | UTILE |
| DOGE | 30g | 51 | 76,47% | +13,13% | +6,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 38 | 47,37% | +25,36% | +4,32% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 26 | 23,08% | +26,34% | -10,48% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 73 | 52,05% | +0,34% | +0,33% | -0,22% | +0,85% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 77 | 50,65% | +0,29% | +0,30% | -0,23% | +0,81% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 77 | 50,65% | +0,29% | +0,30% | -0,23% | +0,81% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 71 | 42,25% | +0,31% | +0,02% | -0,17% | +0,83% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 30 | 36,67% | +0,64% | -0,01% | -0,21% | +1,14% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,49% | -0,49% | -1,07% | -0,05% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 72 | 52,78% | +0,68% | +0,62% | -0,14% | +1,37% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 76 | 52,63% | +0,66% | +0,66% | -0,09% | +1,36% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 76 | 52,63% | +0,66% | +0,66% | -0,09% | +1,36% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 70 | 44,29% | +0,66% | +0,07% | +0,01% | +1,36% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 29 | 41,38% | +1,20% | +0,02% | +0,19% | +1,90% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,04% | -0,04% | -0,90% | +1,02% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 72 | 47,22% | +0,86% | +0,76% | -1,17% | +2,56% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 76 | 51,32% | +1,02% | +0,91% | -1,17% | +2,70% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 76 | 51,32% | +1,02% | +0,91% | -1,17% | +2,70% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 70 | 37,14% | +1,08% | -0,13% | -1,08% | +2,74% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 29 | 37,93% | +1,95% | -0,51% | -0,85% | +3,41% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 70 | 44,29% | +1,70% | +1,52% | -1,78% | +4,02% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 75 | 46,67% | +1,89% | +1,74% | -1,75% | +4,21% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 75 | 46,67% | +1,89% | +1,74% | -1,75% | +4,21% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 68 | 42,65% | +1,82% | -0,67% | -1,68% | +4,18% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 29 | 41,38% | +4,06% | -2,25% | -1,22% | +6,21% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 14,29% | -1,43% | -1,43% | -2,57% | +1,68% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 69 | 53,62% | +2,47% | +2,32% | -2,11% | +5,23% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 73 | 57,53% | +2,69% | +2,67% | -2,07% | +5,40% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 73 | 57,53% | +2,69% | +2,67% | -2,07% | +5,40% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 66 | 43,94% | +2,77% | -1,10% | -2,01% | +5,44% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 29 | 37,93% | +5,44% | -4,00% | -1,49% | +8,41% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -1,74% | -1,74% | -3,24% | +1,77% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 68 | 61,76% | +3,50% | +3,37% | -2,41% | +6,47% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 71 | 64,79% | +3,63% | +3,63% | -2,39% | +6,64% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 71 | 64,79% | +3,63% | +3,63% | -2,39% | +6,64% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 64 | 50,00% | +3,78% | -0,37% | -2,33% | +6,81% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 29 | 41,38% | +5,56% | -4,39% | -1,70% | +9,12% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -1,21% | -1,21% | -3,81% | +1,86% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 66 | 62,12% | +5,13% | +5,08% | -2,59% | +8,79% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 69 | 62,32% | +5,20% | +5,20% | -2,57% | +8,87% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 69 | 62,32% | +5,20% | +5,20% | -2,57% | +8,87% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 62 | 58,06% | +5,55% | +1,64% | -2,50% | +9,26% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 28 | 25,00% | +5,37% | -4,20% | -1,80% | +9,90% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 61 | 72,13% | +8,27% | +8,16% | -2,87% | +12,15% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 64 | 76,56% | +8,20% | +8,20% | -2,85% | +12,10% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 64 | 76,56% | +8,20% | +8,20% | -2,85% | +12,10% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 59 | 55,93% | +8,77% | +1,05% | -2,72% | +12,72% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 24 | 54,17% | +8,85% | -4,04% | -2,32% | +12,73% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 52 | 94,23% | +13,44% | +12,61% | -2,63% | +17,50% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 55 | 90,91% | +13,34% | +13,34% | -2,62% | +17,54% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 55 | 90,91% | +13,34% | +13,34% | -2,62% | +17,54% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 50 | 58,00% | +13,41% | +0,08% | -2,43% | +17,81% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 23 | 65,22% | +13,74% | -2,32% | -2,41% | +18,02% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +5,40% | +5,40% | -4,01% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 37 | 91,89% | +25,08% | +21,50% | -2,38% | +29,87% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 40 | 100,00% | +25,22% | +25,22% | -2,38% | +29,86% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 40 | 100,00% | +25,22% | +25,22% | -2,38% | +29,86% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 35 | 37,14% | +25,82% | -5,56% | -2,09% | +30,51% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 8 | 0,00% | +27,13% | -27,13% | -0,83% | +34,28% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 25 | 88,00% | +27,21% | +21,20% | -2,89% | +32,26% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 27 | 100,00% | +27,01% | +27,01% | -2,95% | +32,15% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 27 | 100,00% | +27,01% | +27,01% | -2,95% | +32,15% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 23 | 100,00% | +27,77% | +27,77% | -2,68% | +33,17% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 22 | 27,27% | +27,34% | -13,98% | -2,60% | +32,72% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 4 | 0,00% | +33,67% | -33,67% | -1,55% | +38,08% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 74 | 44,59% | +0,20% | -0,15% | -0,59% | +1,23% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 77 | 57,14% | +0,12% | +0,50% | -0,67% | +1,10% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 77 | 57,14% | +0,12% | +0,50% | -0,67% | +1,10% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 71 | 50,70% | +0,04% | +0,10% | -0,79% | +1,01% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 44 | 38,64% | +0,01% | -0,74% | -0,85% | +0,76% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 73 | 45,21% | +0,55% | -0,13% | -0,61% | +1,94% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 76 | 57,89% | +0,40% | +0,74% | -0,73% | +1,72% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 76 | 57,89% | +0,40% | +0,74% | -0,73% | +1,72% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 70 | 52,86% | +0,09% | +0,15% | -1,06% | +1,40% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 43 | 41,86% | +0,42% | -1,35% | -0,82% | +1,40% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 73 | 39,73% | +0,84% | -0,03% | -2,23% | +4,00% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 76 | 55,26% | +0,70% | +1,01% | -2,33% | +3,72% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 76 | 55,26% | +0,70% | +1,01% | -2,33% | +3,72% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 70 | 44,29% | +0,05% | -0,02% | -2,58% | +3,01% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 43 | 30,23% | +0,67% | -2,36% | -2,59% | +3,92% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 71 | 43,66% | +1,78% | +0,02% | -3,26% | +6,46% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 74 | 51,35% | +1,67% | +1,34% | -3,29% | +6,25% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 74 | 51,35% | +1,67% | +1,34% | -3,29% | +6,25% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 68 | 51,47% | +0,85% | -0,68% | -3,69% | +5,47% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 43 | 32,56% | +2,13% | -4,81% | -3,64% | +6,91% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 69 | 47,83% | +2,58% | +0,32% | -3,83% | +8,58% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 72 | 55,56% | +2,60% | +1,45% | -3,86% | +8,40% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 72 | 55,56% | +2,60% | +1,45% | -3,86% | +8,40% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 66 | 45,45% | +1,60% | -1,04% | -4,33% | +7,37% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 43 | 27,91% | +3,41% | -6,38% | -4,15% | +8,99% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 67 | 44,78% | +3,49% | +0,37% | -4,42% | +10,78% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 70 | 50,00% | +3,40% | +1,01% | -4,42% | +10,59% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 70 | 50,00% | +3,40% | +1,01% | -4,42% | +10,59% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 64 | 50,00% | +2,07% | -1,40% | -4,96% | +9,06% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 42 | 30,95% | +3,89% | -7,11% | -4,83% | +11,29% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 65 | 58,46% | +5,69% | +3,65% | -4,87% | +14,65% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 68 | 60,29% | +5,28% | +2,62% | -4,85% | +14,22% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 68 | 60,29% | +5,28% | +2,62% | -4,85% | +14,22% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 62 | 51,61% | +3,22% | -0,78% | -5,45% | +11,54% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 41 | 41,46% | +5,35% | -5,10% | -5,18% | +13,82% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 50,00% | +6,54% | +2,61% | -3,97% | +15,08% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 60 | 65,00% | +8,21% | +3,69% | -5,30% | +18,89% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 63 | 61,90% | +8,56% | +5,46% | -5,30% | +19,08% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 63 | 61,90% | +8,56% | +5,46% | -5,30% | +19,08% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 57 | 61,40% | +6,41% | -1,12% | -6,03% | +15,93% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 36 | 50,00% | +5,48% | -6,59% | -5,60% | +14,92% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 66,67% | +6,54% | +0,57% | -4,75% | +18,76% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 51 | 76,47% | +13,13% | +6,53% | -4,73% | +26,46% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 54 | 77,78% | +13,37% | +8,86% | -4,74% | +26,95% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 54 | 77,78% | +13,37% | +8,86% | -4,74% | +26,95% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 48 | 60,42% | +11,87% | -3,22% | -5,56% | +24,46% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 31 | 48,39% | +10,82% | -8,72% | -5,10% | +22,58% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 87,50% | +21,36% | +13,45% | -4,45% | +31,96% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 38 | 47,37% | +25,36% | +4,32% | -3,55% | +42,59% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 40 | 60,00% | +25,18% | +9,36% | -3,60% | +42,47% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 40 | 60,00% | +25,18% | +9,36% | -3,60% | +42,47% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 33 | 6,06% | +22,77% | -18,67% | -4,39% | +40,97% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 27 | 0,00% | +24,99% | -24,99% | -3,76% | +41,98% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +37,31% | +15,91% | -1,31% | +47,38% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 26 | 23,08% | +26,34% | -10,48% | -5,08% | +42,86% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 27 | 40,74% | +26,70% | +2,52% | -5,14% | +42,92% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 27 | 40,74% | +26,70% | +2,52% | -5,14% | +42,92% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 25 | 44,00% | +25,66% | +5,89% | -5,25% | +42,48% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 27 | 0,00% | +26,70% | -26,70% | -5,14% | +42,92% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 20 | 0,00% | +24,92% | -24,92% | -5,27% | +41,80% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 70 | 50,00% | +0,38% | +0,29% | -0,36% | +1,26% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 72 | 55,56% | +0,36% | +0,46% | -0,48% | +1,22% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 75 | 54,67% | +0,39% | +0,40% | -0,45% | +1,25% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 70 | 45,71% | +0,36% | -0,04% | -0,54% | +1,20% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 52 | 46,15% | +0,58% | +0,04% | -0,46% | +1,51% | PRIMA CALIBRAZIONE |
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
| SOL | 3g | Global confluence | BENCHMARK | 69 | 53,62% | +1,76% | +1,64% | -1,74% | +4,15% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 71 | 50,70% | +1,57% | +1,22% | -1,90% | +3,95% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 74 | 50,00% | +1,52% | +1,16% | -1,88% | +3,92% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 69 | 46,38% | +1,13% | -0,16% | -1,92% | +3,47% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 51 | 50,98% | +1,15% | +0,58% | -1,87% | +3,43% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 67 | 56,72% | +3,06% | +2,97% | -2,47% | +6,52% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 69 | 53,62% | +2,79% | +2,08% | -2,63% | +6,26% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 72 | 52,78% | +2,70% | +1,97% | -2,60% | +6,17% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 67 | 46,27% | +2,36% | -0,50% | -2,67% | +5,65% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 49 | 53,06% | +1,63% | +0,85% | -2,64% | +4,89% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 65 | 61,54% | +4,47% | +4,55% | -2,90% | +8,47% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 68 | 61,76% | +4,10% | +3,19% | -3,06% | +8,12% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 71 | 61,97% | +3,93% | +3,06% | -3,04% | +7,94% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 65 | 40,00% | +3,06% | -1,34% | -3,16% | +7,17% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 47 | 46,81% | +1,62% | +0,91% | -3,19% | +5,75% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 63 | 68,25% | +6,66% | +6,78% | -3,23% | +10,91% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 66 | 65,15% | +6,27% | +5,58% | -3,42% | +10,34% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 69 | 63,77% | +5,99% | +5,34% | -3,42% | +10,06% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 63 | 49,21% | +4,57% | -1,44% | -3,60% | +8,90% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 45 | 55,56% | +2,11% | +1,24% | -3,69% | +6,77% | PRIMA CALIBRAZIONE |

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
