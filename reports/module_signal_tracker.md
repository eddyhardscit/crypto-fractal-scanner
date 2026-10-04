# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-04 14:40 UTC

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

Segnali totali salvati: **240**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-04 | BTC | 84.850,99 | +4 | 0 | 0 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-10-04 | DOGE | 0.09275 | 0 | -2 | -2 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-10-04 | SOL | 120,74 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-03 | BTC | 84.628,98 | +1 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-03 | DOGE | 0.09320 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-03 | SOL | 119,63 | +3 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-02 | BTC | 86.570,73 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-10-02 | DOGE | 0.09654 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-10-02 | SOL | 121,92 | +1 | -2 | -2 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-30 | BTC | 83.418,75 | +3 | 0 | 0 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-30 | DOGE | 0.09397 | +3 | -1 | -1 | 0 | +3 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-30 | SOL | 119,28 | +1 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 80 | 79 | 78 | 77 | 76 | 74 | 71 | 69 | 65 | 56 | 41 | 28 |
| SOL | 80 | 79 | 78 | 77 | 76 | 74 | 71 | 69 | 65 | 56 | 41 | 28 |
| DOGE | 80 | 79 | 78 | 77 | 76 | 74 | 71 | 69 | 65 | 56 | 41 | 28 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-06 | 60g | 2026-10-05 | domani |
| SOL | 2026-08-06 | 60g | 2026-10-05 | domani |
| DOGE | 2026-08-06 | 60g | 2026-10-05 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 74 | 52,70% | +0,34% | +0,33% | UTILE |
| BTC | 2g | 73 | 52,05% | +0,65% | +0,58% | UTILE |
| BTC | 3g | 72 | 47,22% | +0,86% | +0,76% | UTILE |
| BTC | 5g | 71 | 45,07% | +1,71% | +1,53% | UTILE |
| BTC | 7g | 69 | 53,62% | +2,47% | +2,32% | UTILE |
| BTC | 10g | 68 | 61,76% | +3,50% | +3,37% | UTILE |
| BTC | 14g | 66 | 62,12% | +5,13% | +5,08% | UTILE |
| BTC | 21g | 62 | 72,58% | +8,30% | +8,19% | UTILE |
| BTC | 30g | 53 | 94,34% | +13,27% | +12,46% | PRIMA CALIBRAZIONE |
| BTC | 45g | 38 | 92,11% | +24,99% | +21,51% | PRIMA CALIBRAZIONE |
| BTC | 60g | 26 | 88,46% | +27,39% | +21,62% | FEEDBACK RAPIDO |
| SOL | 1g | 71 | 50,70% | +0,38% | +0,30% | UTILE |
| SOL | 2g | 70 | 48,57% | +1,06% | +0,96% | UTILE |
| SOL | 3g | 69 | 53,62% | +1,76% | +1,64% | UTILE |
| SOL | 5g | 68 | 57,35% | +3,05% | +2,97% | UTILE |
| SOL | 7g | 66 | 62,12% | +4,41% | +4,49% | UTILE |
| SOL | 10g | 63 | 68,25% | +6,66% | +6,78% | UTILE |
| SOL | 14g | 61 | 75,41% | +9,69% | +10,29% | UTILE |
| SOL | 21g | 58 | 82,76% | +14,98% | +14,37% | PRIMA CALIBRAZIONE |
| SOL | 30g | 49 | 79,59% | +21,94% | +17,90% | PRIMA CALIBRAZIONE |
| SOL | 45g | 34 | 67,65% | +42,79% | +20,15% | PRIMA CALIBRAZIONE |
| SOL | 60g | 21 | 47,62% | +45,23% | +3,50% | FEEDBACK RAPIDO |
| DOGE | 1g | 75 | 45,33% | +0,19% | -0,14% | UTILE |
| DOGE | 2g | 74 | 44,59% | +0,49% | -0,18% | UTILE |
| DOGE | 3g | 73 | 39,73% | +0,84% | -0,03% | UTILE |
| DOGE | 5g | 72 | 43,06% | +1,75% | +0,02% | UTILE |
| DOGE | 7g | 70 | 47,14% | +2,50% | +0,26% | UTILE |
| DOGE | 10g | 67 | 44,78% | +3,49% | +0,37% | UTILE |
| DOGE | 14g | 65 | 58,46% | +5,69% | +3,65% | UTILE |
| DOGE | 21g | 61 | 63,93% | +8,23% | +3,47% | UTILE |
| DOGE | 30g | 52 | 75,00% | +13,01% | +6,27% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 39 | 48,72% | +25,34% | +4,84% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 26 | 23,08% | +26,34% | -10,48% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 74 | 52,70% | +0,34% | +0,33% | -0,21% | +0,85% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 78 | 50,00% | +0,29% | +0,29% | -0,22% | +0,80% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 78 | 50,00% | +0,29% | +0,29% | -0,22% | +0,80% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 72 | 43,06% | +0,31% | +0,02% | -0,17% | +0,82% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 31 | 38,71% | +0,62% | -0,01% | -0,20% | +1,12% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,49% | -0,49% | -1,07% | -0,05% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 73 | 52,05% | +0,65% | +0,58% | -0,17% | +1,32% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 77 | 51,95% | +0,63% | +0,63% | -0,11% | +1,32% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 77 | 51,95% | +0,63% | +0,63% | -0,11% | +1,32% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 71 | 43,66% | +0,62% | +0,04% | -0,02% | +1,31% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 30 | 40,00% | +1,10% | -0,05% | +0,11% | +1,77% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,28% | -0,28% | -1,06% | +0,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 72 | 47,22% | +0,86% | +0,76% | -1,17% | +2,56% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 76 | 51,32% | +1,02% | +0,91% | -1,17% | +2,70% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 76 | 51,32% | +1,02% | +0,91% | -1,17% | +2,70% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 70 | 37,14% | +1,08% | -0,13% | -1,08% | +2,74% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 29 | 37,93% | +1,95% | -0,51% | -0,85% | +3,41% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 71 | 45,07% | +1,71% | +1,53% | -1,76% | +4,03% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 76 | 46,05% | +1,89% | +1,69% | -1,73% | +4,22% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 76 | 46,05% | +1,89% | +1,69% | -1,73% | +4,22% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 69 | 43,48% | +1,82% | -0,63% | -1,66% | +4,19% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 29 | 41,38% | +4,06% | -2,25% | -1,22% | +6,21% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 14,29% | -1,43% | -1,43% | -2,57% | +1,68% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 69 | 53,62% | +2,47% | +2,32% | -2,11% | +5,23% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 74 | 56,76% | +2,66% | +2,62% | -2,07% | +5,37% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 74 | 56,76% | +2,66% | +2,62% | -2,07% | +5,37% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 67 | 44,78% | +2,73% | -1,07% | -2,01% | +5,41% | UTILE |
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
| BTC | 21g | Global confluence | BENCHMARK | 62 | 72,58% | +8,30% | +8,19% | -2,88% | +12,16% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 65 | 76,92% | +8,23% | +8,23% | -2,86% | +12,12% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 65 | 76,92% | +8,23% | +8,23% | -2,86% | +12,12% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 60 | 56,67% | +8,78% | +1,19% | -2,72% | +12,72% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 24 | 54,17% | +8,85% | -4,04% | -2,32% | +12,73% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 53 | 94,34% | +13,27% | +12,46% | -2,72% | +17,32% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 56 | 91,07% | +13,19% | +13,19% | -2,71% | +17,37% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 56 | 91,07% | +13,19% | +13,19% | -2,71% | +17,37% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 51 | 58,82% | +13,24% | +0,18% | -2,53% | +17,62% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,37% | -2,02% | -2,62% | +17,60% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 100,00% | +5,25% | +5,25% | -4,87% | +8,45% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 38 | 92,11% | +24,99% | +21,51% | -2,18% | +29,75% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 41 | 100,00% | +25,14% | +25,14% | -2,20% | +29,76% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 41 | 100,00% | +25,14% | +25,14% | -2,20% | +29,76% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 36 | 38,89% | +25,71% | -4,79% | -1,89% | +30,37% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 9 | 11,11% | +26,56% | -21,68% | -0,19% | +33,31% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 26 | 88,46% | +27,39% | +21,62% | -2,89% | +32,41% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 28 | 100,00% | +27,19% | +27,19% | -2,94% | +32,28% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 28 | 100,00% | +27,19% | +27,19% | -2,94% | +32,28% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 24 | 100,00% | +27,95% | +27,95% | -2,68% | +33,29% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 23 | 26,09% | +27,54% | -14,77% | -2,61% | +32,86% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 4 | 0,00% | +33,67% | -33,67% | -1,55% | +38,08% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 75 | 45,33% | +0,19% | -0,14% | -0,59% | +1,21% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 78 | 57,69% | +0,12% | +0,50% | -0,67% | +1,08% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 78 | 57,69% | +0,12% | +0,50% | -0,67% | +1,08% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 72 | 50,00% | +0,03% | +0,09% | -0,78% | +0,99% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 44 | 38,64% | +0,01% | -0,74% | -0,85% | +0,76% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 74 | 44,59% | +0,49% | -0,18% | -0,65% | +1,86% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 77 | 58,44% | +0,35% | +0,78% | -0,77% | +1,65% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 77 | 58,44% | +0,35% | +0,78% | -0,77% | +1,65% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 71 | 52,11% | +0,03% | +0,09% | -1,10% | +1,33% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 44 | 40,91% | +0,32% | -1,41% | -0,90% | +1,29% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 73 | 39,73% | +0,84% | -0,03% | -2,23% | +4,00% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 76 | 55,26% | +0,70% | +1,01% | -2,33% | +3,72% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 76 | 55,26% | +0,70% | +1,01% | -2,33% | +3,72% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 70 | 44,29% | +0,05% | -0,02% | -2,58% | +3,01% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 43 | 30,23% | +0,67% | -2,36% | -2,59% | +3,92% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 72 | 43,06% | +1,75% | +0,02% | -3,25% | +6,44% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 75 | 52,00% | +1,64% | +1,33% | -3,29% | +6,23% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 75 | 52,00% | +1,64% | +1,33% | -3,29% | +6,23% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 69 | 50,72% | +0,83% | -0,67% | -3,68% | +5,46% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 43 | 32,56% | +2,13% | -4,81% | -3,64% | +6,91% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 70 | 47,14% | +2,50% | +0,26% | -3,86% | +8,49% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 73 | 56,16% | +2,52% | +1,47% | -3,88% | +8,31% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 73 | 56,16% | +2,52% | +1,47% | -3,88% | +8,31% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 67 | 44,78% | +1,52% | -1,07% | -4,35% | +7,29% | UTILE |
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
| DOGE | 21g | Global confluence | BENCHMARK | 61 | 63,93% | +8,23% | +3,47% | -5,33% | +18,97% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 64 | 60,94% | +8,57% | +5,23% | -5,34% | +19,16% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 64 | 60,94% | +8,57% | +5,23% | -5,34% | +19,16% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 58 | 60,34% | +6,46% | -1,26% | -6,05% | +16,07% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 37 | 48,65% | +5,58% | -6,66% | -5,65% | +15,17% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 66,67% | +6,54% | +0,57% | -4,75% | +18,76% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 52 | 75,00% | +13,01% | +6,27% | -4,82% | +26,35% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 55 | 76,36% | +13,25% | +8,58% | -4,84% | +26,85% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 55 | 76,36% | +13,25% | +8,58% | -4,84% | +26,85% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 49 | 61,22% | +11,76% | -3,02% | -5,65% | +24,39% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 31 | 48,39% | +10,82% | -8,72% | -5,10% | +22,58% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 87,50% | +21,36% | +13,45% | -4,45% | +31,96% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 39 | 48,72% | +25,34% | +4,84% | -3,33% | +42,56% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 41 | 60,98% | +25,16% | +9,73% | -3,38% | +42,44% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 41 | 60,98% | +25,16% | +9,73% | -3,38% | +42,44% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 34 | 8,82% | +22,82% | -17,40% | -4,11% | +40,98% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 27 | 0,00% | +24,99% | -24,99% | -3,76% | +41,98% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +34,73% | +17,62% | -0,01% | +46,16% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 26 | 23,08% | +26,34% | -10,48% | -5,08% | +42,86% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 28 | 42,86% | +26,91% | +3,60% | -5,04% | +43,20% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 28 | 42,86% | +26,91% | +3,60% | -5,04% | +43,20% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 26 | 46,15% | +25,93% | +6,92% | -5,14% | +42,79% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 28 | 0,00% | +26,91% | -26,91% | -5,04% | +43,20% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 20 | 0,00% | +24,92% | -24,92% | -5,27% | +41,80% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 71 | 50,70% | +0,38% | +0,30% | -0,36% | +1,25% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 73 | 54,79% | +0,37% | +0,44% | -0,47% | +1,22% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 76 | 53,95% | +0,40% | +0,38% | -0,44% | +1,25% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 71 | 46,48% | +0,36% | -0,03% | -0,53% | +1,20% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 53 | 47,17% | +0,59% | +0,06% | -0,45% | +1,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 70 | 48,57% | +1,06% | +0,96% | -0,22% | +2,14% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 72 | 48,61% | +0,94% | +0,69% | -0,47% | +1,87% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 75 | 48,00% | +0,91% | +0,65% | -0,45% | +1,90% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 70 | 42,86% | +0,74% | -0,03% | -0,43% | +1,89% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 52 | 50,00% | +0,85% | +0,39% | -0,46% | +1,93% | PRIMA CALIBRAZIONE |
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
| SOL | 5g | Global confluence | BENCHMARK | 68 | 57,35% | +3,05% | +2,97% | -2,44% | +6,50% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 70 | 52,86% | +2,79% | +2,01% | -2,60% | +6,25% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 73 | 52,05% | +2,70% | +1,90% | -2,58% | +6,15% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 68 | 47,06% | +2,36% | -0,46% | -2,64% | +5,64% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 50 | 54,00% | +1,65% | +0,89% | -2,60% | +4,89% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 66 | 62,12% | +4,41% | +4,49% | -2,91% | +8,38% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 69 | 60,87% | +4,05% | +3,15% | -3,06% | +8,03% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 72 | 61,11% | +3,87% | +3,02% | -3,05% | +7,86% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 66 | 40,91% | +3,01% | -1,32% | -3,16% | +7,09% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 48 | 47,92% | +1,59% | +0,89% | -3,19% | +5,68% | PRIMA CALIBRAZIONE |
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
