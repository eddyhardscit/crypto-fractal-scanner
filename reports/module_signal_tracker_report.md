# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-05 05:33 UTC

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

Segnali totali salvati: **243**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-05 | BTC | 85.487,99 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-05 | DOGE | 0.09488 | 0 | -2 | -2 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-10-05 | SOL | 120,07 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-04 | BTC | 84.850,99 | +4 | 0 | 0 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-10-04 | DOGE | 0.09275 | 0 | -2 | -2 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-10-04 | SOL | 120,74 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-03 | BTC | 84.628,98 | +1 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-03 | DOGE | 0.09320 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-03 | SOL | 119,63 | +3 | -1 | -1 | 0 | +2 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-02 | BTC | 86.570,73 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-10-02 | DOGE | 0.09654 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-10-02 | SOL | 121,92 | +1 | -2 | -2 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 81 | 80 | 79 | 78 | 77 | 75 | 72 | 69 | 66 | 57 | 42 | 29 |
| SOL | 81 | 80 | 79 | 78 | 77 | 75 | 72 | 69 | 66 | 57 | 42 | 29 |
| DOGE | 81 | 80 | 79 | 78 | 77 | 75 | 72 | 69 | 66 | 57 | 42 | 29 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-07 | 60g | 2026-10-06 | domani |
| SOL | 2026-08-07 | 60g | 2026-10-06 | domani |
| DOGE | 2026-08-07 | 60g | 2026-10-06 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 75 | 53,33% | +0,35% | +0,33% | UTILE |
| BTC | 2g | 74 | 52,70% | +0,65% | +0,59% | UTILE |
| BTC | 3g | 73 | 46,58% | +0,83% | +0,73% | UTILE |
| BTC | 5g | 72 | 45,83% | +1,72% | +1,54% | UTILE |
| BTC | 7g | 70 | 54,29% | +2,48% | +2,33% | UTILE |
| BTC | 10g | 69 | 62,32% | +3,47% | +3,34% | UTILE |
| BTC | 14g | 66 | 62,12% | +5,13% | +5,08% | UTILE |
| BTC | 21g | 63 | 73,02% | +8,33% | +8,22% | UTILE |
| BTC | 30g | 54 | 94,44% | +13,16% | +12,37% | PRIMA CALIBRAZIONE |
| BTC | 45g | 39 | 92,31% | +24,71% | +21,31% | PRIMA CALIBRAZIONE |
| BTC | 60g | 27 | 88,89% | +27,56% | +22,00% | FEEDBACK RAPIDO |
| SOL | 1g | 72 | 50,00% | +0,37% | +0,28% | UTILE |
| SOL | 2g | 71 | 49,30% | +1,05% | +0,95% | UTILE |
| SOL | 3g | 70 | 52,86% | +1,72% | +1,59% | UTILE |
| SOL | 5g | 69 | 57,97% | +3,02% | +2,94% | UTILE |
| SOL | 7g | 67 | 62,69% | +4,36% | +4,44% | UTILE |
| SOL | 10g | 64 | 67,19% | +6,53% | +6,65% | UTILE |
| SOL | 14g | 61 | 75,41% | +9,69% | +10,29% | UTILE |
| SOL | 21g | 59 | 83,05% | +15,05% | +14,44% | PRIMA CALIBRAZIONE |
| SOL | 30g | 50 | 80,00% | +21,85% | +17,89% | PRIMA CALIBRAZIONE |
| SOL | 45g | 35 | 68,57% | +42,54% | +20,55% | PRIMA CALIBRAZIONE |
| SOL | 60g | 22 | 50,00% | +45,99% | +6,15% | FEEDBACK RAPIDO |
| DOGE | 1g | 75 | 45,33% | +0,19% | -0,14% | UTILE |
| DOGE | 2g | 75 | 44,00% | +0,50% | -0,20% | UTILE |
| DOGE | 3g | 74 | 39,19% | +0,81% | -0,05% | UTILE |
| DOGE | 5g | 73 | 43,84% | +1,73% | +0,03% | UTILE |
| DOGE | 7g | 71 | 47,89% | +2,49% | +0,29% | UTILE |
| DOGE | 10g | 68 | 44,12% | +3,37% | +0,30% | UTILE |
| DOGE | 14g | 65 | 58,46% | +5,69% | +3,65% | UTILE |
| DOGE | 21g | 62 | 62,90% | +8,31% | +3,21% | UTILE |
| DOGE | 30g | 53 | 73,58% | +12,97% | +5,95% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 40 | 50,00% | +25,08% | +5,09% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 27 | 25,93% | +26,68% | -8,78% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 75 | 53,33% | +0,35% | +0,33% | -0,20% | +0,87% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 78 | 50,00% | +0,29% | +0,29% | -0,22% | +0,80% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 78 | 50,00% | +0,29% | +0,29% | -0,22% | +0,80% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 73 | 43,84% | +0,31% | +0,03% | -0,15% | +0,84% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 32 | 40,62% | +0,63% | +0,02% | -0,17% | +1,16% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,49% | -0,49% | -1,07% | -0,05% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 74 | 52,70% | +0,65% | +0,59% | -0,16% | +1,34% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 78 | 51,28% | +0,63% | +0,61% | -0,10% | +1,34% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 78 | 51,28% | +0,63% | +0,61% | -0,10% | +1,34% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 72 | 44,44% | +0,63% | +0,05% | -0,00% | +1,33% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 31 | 41,94% | +1,09% | -0,01% | +0,14% | +1,80% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,28% | -0,28% | -1,06% | +0,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 73 | 46,58% | +0,83% | +0,73% | -1,19% | +2,53% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 77 | 50,65% | +0,99% | +0,88% | -1,19% | +2,67% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 77 | 50,65% | +0,99% | +0,88% | -1,19% | +2,67% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 71 | 36,62% | +1,05% | -0,14% | -1,10% | +2,71% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 30 | 36,67% | +1,84% | -0,54% | -0,91% | +3,31% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,50% | -0,50% | -1,88% | +1,29% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 72 | 45,83% | +1,72% | +1,54% | -1,74% | +4,04% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 76 | 46,05% | +1,89% | +1,69% | -1,73% | +4,22% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 76 | 46,05% | +1,89% | +1,69% | -1,73% | +4,22% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 70 | 44,29% | +1,83% | -0,59% | -1,64% | +4,20% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 29 | 41,38% | +4,06% | -2,25% | -1,22% | +6,21% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 14,29% | -1,43% | -1,43% | -2,57% | +1,68% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 70 | 54,29% | +2,48% | +2,33% | -2,08% | +5,23% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 75 | 56,00% | +2,67% | +2,55% | -2,05% | +5,37% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 75 | 56,00% | +2,67% | +2,55% | -2,05% | +5,37% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 68 | 45,59% | +2,74% | -1,01% | -1,98% | +5,40% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 29 | 37,93% | +5,44% | -4,00% | -1,49% | +8,41% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 28,57% | -1,74% | -1,74% | -3,24% | +1,77% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 69 | 62,32% | +3,47% | +3,34% | -2,40% | +6,43% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 72 | 65,28% | +3,60% | +3,60% | -2,38% | +6,60% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 72 | 65,28% | +3,60% | +3,60% | -2,38% | +6,60% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 65 | 50,77% | +3,75% | -0,34% | -2,32% | +6,76% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 29 | 41,38% | +5,56% | -4,39% | -1,70% | +9,12% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -1,21% | -1,21% | -3,81% | +1,86% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 66 | 62,12% | +5,13% | +5,08% | -2,59% | +8,79% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 69 | 62,32% | +5,20% | +5,20% | -2,57% | +8,87% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 69 | 62,32% | +5,20% | +5,20% | -2,57% | +8,87% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 62 | 58,06% | +5,55% | +1,64% | -2,50% | +9,26% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 28 | 25,00% | +5,37% | -4,20% | -1,80% | +9,90% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 63 | 73,02% | +8,33% | +8,22% | -2,88% | +12,17% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 66 | 77,27% | +8,26% | +8,26% | -2,86% | +12,13% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 66 | 77,27% | +8,26% | +8,26% | -2,86% | +12,13% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 61 | 57,38% | +8,81% | +1,34% | -2,73% | +12,72% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 25 | 52,00% | +8,91% | -4,29% | -2,36% | +12,73% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 54 | 94,44% | +13,16% | +12,37% | -2,78% | +17,18% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 57 | 91,23% | +13,09% | +13,09% | -2,76% | +17,23% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 57 | 91,23% | +13,09% | +13,09% | -2,76% | +17,23% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 52 | 59,62% | +13,12% | +0,31% | -2,60% | +17,47% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,37% | -2,02% | -2,62% | +17,60% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 100,00% | +5,25% | +5,25% | -4,87% | +8,45% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 39 | 92,31% | +24,71% | +21,31% | -2,13% | +29,41% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 42 | 100,00% | +24,87% | +24,87% | -2,16% | +29,44% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 42 | 100,00% | +24,87% | +24,87% | -2,16% | +29,44% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 37 | 40,54% | +25,39% | -4,29% | -1,84% | +29,99% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 10 | 20,00% | +25,29% | -18,12% | -0,19% | +31,62% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 27 | 88,89% | +27,56% | +22,00% | -2,92% | +32,49% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 29 | 100,00% | +27,35% | +27,35% | -2,97% | +32,37% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 29 | 100,00% | +27,35% | +27,35% | -2,97% | +32,37% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 25 | 100,00% | +28,10% | +28,10% | -2,72% | +33,35% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 24 | 29,17% | +27,72% | -12,83% | -2,65% | +32,94% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 4 | 0,00% | +33,67% | -33,67% | -1,55% | +38,08% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 75 | 45,33% | +0,19% | -0,14% | -0,59% | +1,21% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 79 | 56,96% | +0,14% | +0,47% | -0,64% | +1,12% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 79 | 56,96% | +0,14% | +0,47% | -0,64% | +1,12% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 73 | 50,68% | +0,06% | +0,12% | -0,74% | +1,03% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 44 | 38,64% | +0,01% | -0,74% | -0,85% | +0,76% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 75 | 44,00% | +0,50% | -0,20% | -0,62% | +1,89% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 78 | 57,69% | +0,36% | +0,74% | -0,74% | +1,68% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 78 | 57,69% | +0,36% | +0,74% | -0,74% | +1,68% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 72 | 52,78% | +0,05% | +0,11% | -1,06% | +1,36% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 44 | 40,91% | +0,32% | -1,41% | -0,90% | +1,29% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 74 | 39,19% | +0,81% | -0,05% | -2,26% | +3,95% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 77 | 55,84% | +0,67% | +1,02% | -2,35% | +3,67% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 77 | 55,84% | +0,67% | +1,02% | -2,35% | +3,67% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 71 | 43,66% | +0,02% | -0,04% | -2,60% | +2,97% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 44 | 29,55% | +0,62% | -2,34% | -2,62% | +3,83% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 73 | 43,84% | +1,73% | +0,03% | -3,26% | +6,41% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 76 | 51,32% | +1,63% | +1,30% | -3,29% | +6,19% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 76 | 51,32% | +1,63% | +1,30% | -3,29% | +6,19% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 70 | 51,43% | +0,83% | -0,65% | -3,68% | +5,44% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 43 | 32,56% | +2,13% | -4,81% | -3,64% | +6,91% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 71 | 47,89% | +2,49% | +0,29% | -3,84% | +8,44% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 74 | 55,41% | +2,51% | +1,42% | -3,86% | +8,26% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 74 | 55,41% | +2,51% | +1,42% | -3,86% | +8,26% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 68 | 45,59% | +1,53% | -1,03% | -4,33% | +7,26% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 43 | 27,91% | +3,41% | -6,38% | -4,15% | +8,99% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 68 | 44,12% | +3,37% | +0,30% | -4,48% | +10,62% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 71 | 50,70% | +3,29% | +1,06% | -4,48% | +10,45% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 71 | 50,70% | +3,29% | +1,06% | -4,48% | +10,45% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 65 | 49,23% | +1,97% | -1,44% | -5,02% | +8,92% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 43 | 30,23% | +3,70% | -7,04% | -4,91% | +11,04% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 65 | 58,46% | +5,69% | +3,65% | -4,87% | +14,65% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 68 | 60,29% | +5,28% | +2,62% | -4,85% | +14,22% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 68 | 60,29% | +5,28% | +2,62% | -4,85% | +14,22% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 62 | 51,61% | +3,22% | -0,78% | -5,45% | +11,54% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 41 | 41,46% | +5,35% | -5,10% | -5,18% | +13,82% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 50,00% | +6,54% | +2,61% | -3,97% | +15,08% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 62 | 62,90% | +8,31% | +3,21% | -5,36% | +19,07% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 65 | 60,00% | +8,64% | +4,95% | -5,36% | +19,25% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 65 | 60,00% | +8,64% | +4,95% | -5,36% | +19,25% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 59 | 59,32% | +6,57% | -1,45% | -6,06% | +16,22% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 38 | 47,37% | +5,77% | -6,83% | -5,68% | +15,43% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 66,67% | +6,54% | +0,57% | -4,75% | +18,76% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 53 | 73,58% | +12,97% | +5,95% | -4,89% | +26,29% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 56 | 75,00% | +13,21% | +8,24% | -4,90% | +26,78% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 56 | 75,00% | +13,21% | +8,24% | -4,90% | +26,78% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 50 | 62,00% | +11,74% | -2,74% | -5,70% | +24,36% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 31 | 48,39% | +10,82% | -8,72% | -5,10% | +22,58% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 87,50% | +21,36% | +13,45% | -4,45% | +31,96% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 40 | 50,00% | +25,08% | +5,09% | -3,37% | +42,18% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 42 | 61,90% | +24,92% | +9,85% | -3,43% | +42,08% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 42 | 61,90% | +24,92% | +9,85% | -3,43% | +42,08% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 35 | 11,43% | +22,59% | -16,48% | -4,14% | +40,59% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 27 | 0,00% | +24,99% | -24,99% | -3,76% | +41,98% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +34,73% | +17,62% | -0,01% | +46,16% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 27 | 25,93% | +26,68% | -8,78% | -4,95% | +43,14% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 29 | 44,83% | +27,21% | +4,70% | -4,92% | +43,45% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 29 | 44,83% | +27,21% | +4,70% | -4,92% | +43,45% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 27 | 48,15% | +26,29% | +7,98% | -5,01% | +43,07% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 28 | 0,00% | +26,91% | -26,91% | -5,04% | +43,20% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 20 | 0,00% | +24,92% | -24,92% | -5,27% | +41,80% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 72 | 50,00% | +0,37% | +0,28% | -0,36% | +1,25% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 74 | 55,41% | +0,36% | +0,44% | -0,47% | +1,22% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 77 | 54,55% | +0,38% | +0,38% | -0,44% | +1,24% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 72 | 45,83% | +0,35% | -0,03% | -0,53% | +1,19% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 54 | 46,30% | +0,56% | +0,05% | -0,45% | +1,49% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 71 | 49,30% | +1,05% | +0,95% | -0,21% | +2,13% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 73 | 47,95% | +0,93% | +0,68% | -0,46% | +1,87% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 76 | 47,37% | +0,91% | +0,64% | -0,44% | +1,90% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 71 | 43,66% | +0,74% | -0,02% | -0,41% | +1,89% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 53 | 50,94% | +0,84% | +0,39% | -0,45% | +1,93% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 70 | 52,86% | +1,72% | +1,59% | -1,75% | +4,09% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 72 | 51,39% | +1,53% | +1,23% | -1,92% | +3,89% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 75 | 50,67% | +1,48% | +1,16% | -1,89% | +3,87% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 70 | 45,71% | +1,09% | -0,18% | -1,93% | +3,41% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 52 | 50,00% | +1,09% | +0,54% | -1,89% | +3,35% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 69 | 57,97% | +3,02% | +2,94% | -2,43% | +6,46% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 71 | 52,11% | +2,76% | +1,98% | -2,59% | +6,21% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 74 | 51,35% | +2,67% | +1,87% | -2,57% | +6,12% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 69 | 47,83% | +2,34% | -0,44% | -2,64% | +5,61% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 51 | 54,90% | +1,63% | +0,89% | -2,59% | +4,86% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 67 | 62,69% | +4,36% | +4,44% | -2,90% | +8,31% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 69 | 60,87% | +4,05% | +3,15% | -3,06% | +8,03% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 72 | 61,11% | +3,87% | +3,02% | -3,05% | +7,86% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 67 | 41,79% | +2,99% | -1,28% | -3,14% | +7,05% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 49 | 48,98% | +1,58% | +0,90% | -3,16% | +5,65% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 64 | 67,19% | +6,53% | +6,65% | -3,25% | +10,77% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 67 | 65,67% | +6,15% | +5,52% | -3,44% | +10,22% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 70 | 64,29% | +5,88% | +5,29% | -3,44% | +9,95% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 64 | 48,44% | +4,47% | -1,45% | -3,61% | +8,79% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 46 | 54,35% | +2,02% | +1,18% | -3,71% | +6,67% | PRIMA CALIBRAZIONE |

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
