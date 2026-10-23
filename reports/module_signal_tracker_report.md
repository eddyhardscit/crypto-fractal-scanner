# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-23 05:34 UTC

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

Segnali totali salvati: **294**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-23 | BTC | 81.657,99 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-23 | DOGE | 0.07979 | -1 | +3 | +3 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-23 | SOL | 104,39 | +3 | +3 | +3 | 0 | +1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-22 | BTC | 82.752,49 | +2 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-22 | DOGE | 0.07992 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-22 | SOL | 105,09 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-21 | BTC | 82.805,01 | 0 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-21 | DOGE | 0.08166 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-21 | SOL | 105,96 | +3 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-20 | BTC | 81.867,63 | +2 | +1 | +1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-20 | DOGE | 0.07939 | -1 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-20 | SOL | 104,68 | +3 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 98 | 97 | 96 | 95 | 93 | 92 | 89 | 85 | 78 | 71 | 60 | 45 |
| SOL | 98 | 97 | 96 | 95 | 93 | 92 | 89 | 85 | 78 | 71 | 60 | 45 |
| DOGE | 98 | 97 | 96 | 95 | 93 | 92 | 89 | 85 | 78 | 71 | 60 | 45 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-25 | 60g | 2026-10-24 | domani |
| SOL | 2026-08-25 | 60g | 2026-10-24 | domani |
| DOGE | 2026-08-25 | 60g | 2026-10-24 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 86 | 52,33% | +0,29% | +0,27% | UTILE |
| BTC | 2g | 85 | 50,59% | +0,50% | +0,43% | UTILE |
| BTC | 3g | 85 | 45,88% | +0,61% | +0,58% | UTILE |
| BTC | 5g | 83 | 44,58% | +1,30% | +1,18% | UTILE |
| BTC | 7g | 82 | 50,00% | +1,95% | +1,79% | UTILE |
| BTC | 10g | 80 | 55,00% | +2,72% | +2,63% | UTILE |
| BTC | 14g | 78 | 57,69% | +4,05% | +4,00% | UTILE |
| BTC | 21g | 73 | 67,12% | +7,38% | +7,29% | UTILE |
| BTC | 30g | 68 | 92,65% | +11,50% | +10,87% | UTILE |
| BTC | 45g | 57 | 94,74% | +18,57% | +16,25% | PRIMA CALIBRAZIONE |
| BTC | 60g | 42 | 92,86% | +26,00% | +22,42% | PRIMA CALIBRAZIONE |
| SOL | 1g | 88 | 46,59% | +0,18% | +0,08% | UTILE |
| SOL | 2g | 87 | 43,68% | +0,55% | +0,43% | UTILE |
| SOL | 3g | 86 | 47,67% | +0,94% | +0,79% | UTILE |
| SOL | 5g | 84 | 48,81% | +1,67% | +1,59% | UTILE |
| SOL | 7g | 83 | 53,01% | +2,48% | +2,54% | UTILE |
| SOL | 10g | 81 | 53,09% | +3,68% | +3,78% | UTILE |
| SOL | 14g | 77 | 61,04% | +5,88% | +6,35% | UTILE |
| SOL | 21g | 70 | 72,86% | +11,76% | +11,26% | UTILE |
| SOL | 30g | 63 | 80,95% | +18,51% | +15,37% | UTILE |
| SOL | 45g | 53 | 75,47% | +30,61% | +16,08% | PRIMA CALIBRAZIONE |
| SOL | 60g | 38 | 71,05% | +41,84% | +18,77% | PRIMA CALIBRAZIONE |
| DOGE | 1g | 87 | 48,28% | +0,02% | -0,06% | UTILE |
| DOGE | 2g | 87 | 43,68% | +0,16% | -0,12% | UTILE |
| DOGE | 3g | 87 | 40,23% | +0,37% | +0,03% | UTILE |
| DOGE | 5g | 85 | 45,88% | +0,86% | +0,11% | UTILE |
| DOGE | 7g | 84 | 48,81% | +1,21% | +0,41% | UTILE |
| DOGE | 10g | 81 | 43,21% | +1,56% | +0,30% | UTILE |
| DOGE | 14g | 78 | 53,85% | +2,93% | +2,51% | UTILE |
| DOGE | 21g | 74 | 52,70% | +5,49% | +0,25% | UTILE |
| DOGE | 30g | 67 | 65,67% | +9,64% | +4,00% | UTILE |
| DOGE | 45g | 56 | 48,21% | +16,70% | +3,35% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 43 | 44,19% | +21,57% | -0,70% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 86 | 52,33% | +0,29% | +0,27% | -0,29% | +0,79% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 95 | 48,42% | +0,19% | +0,24% | -0,34% | +0,70% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 95 | 48,42% | +0,19% | +0,24% | -0,34% | +0,70% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 90 | 50,00% | +0,21% | +0,08% | -0,29% | +0,73% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,55% | -0,06% | -0,27% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 85 | 50,59% | +0,50% | +0,43% | -0,26% | +1,20% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 94 | 52,13% | +0,43% | +0,51% | -0,29% | +1,11% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 94 | 52,13% | +0,43% | +0,51% | -0,29% | +1,11% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 89 | 48,31% | +0,42% | +0,09% | -0,22% | +1,09% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,85% | -0,13% | -0,05% | +1,59% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 85 | 45,88% | +0,61% | +0,58% | -1,28% | +2,39% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 93 | 50,54% | +0,73% | +0,79% | -1,34% | +2,42% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 93 | 50,54% | +0,73% | +0,79% | -1,34% | +2,42% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 88 | 39,77% | +0,74% | -0,09% | -1,28% | +2,43% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 36 | 36,11% | +1,29% | -0,55% | -1,13% | +3,01% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 83 | 44,58% | +1,30% | +1,18% | -1,94% | +3,71% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 91 | 49,45% | +1,40% | +1,51% | -1,96% | +3,74% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 91 | 49,45% | +1,40% | +1,51% | -1,96% | +3,74% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 86 | 43,02% | +1,26% | -0,62% | -1,93% | +3,67% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 36 | 36,11% | +2,85% | -2,16% | -1,73% | +5,27% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 82 | 50,00% | +1,95% | +1,79% | -2,31% | +4,78% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 90 | 57,78% | +2,03% | +2,19% | -2,33% | +4,75% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 90 | 57,78% | +2,03% | +2,19% | -2,33% | +4,75% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 85 | 43,53% | +1,97% | -0,97% | -2,31% | +4,69% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 36 | 33,33% | +4,03% | -3,63% | -2,13% | +7,10% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 80 | 55,00% | +2,72% | +2,63% | -2,68% | +5,86% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 87 | 66,67% | +2,73% | +3,11% | -2,66% | +5,82% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 87 | 66,67% | +2,73% | +3,11% | -2,66% | +5,82% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 82 | 45,12% | +2,67% | -0,49% | -2,68% | +5,82% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 35 | 37,14% | +4,12% | -4,05% | -2,39% | +7,77% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -1,34% | -1,34% | -4,20% | +1,67% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 78 | 57,69% | +4,05% | +4,00% | -2,93% | +7,82% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 83 | 62,65% | +4,02% | +4,40% | -2,93% | +7,77% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 83 | 62,65% | +4,02% | +4,40% | -2,93% | +7,77% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 78 | 51,28% | +4,04% | +0,93% | -2,95% | +7,87% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 34 | 20,59% | +3,74% | -4,14% | -2,59% | +8,37% | PRIMA CALIBRAZIONE |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,75% | -0,75% | -4,66% | +2,55% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 73 | 67,12% | +7,38% | +7,29% | -3,05% | +11,38% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 77 | 75,32% | +7,20% | +7,40% | -3,06% | +11,26% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 77 | 75,32% | +7,20% | +7,40% | -3,06% | +11,26% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 71 | 50,70% | +7,40% | +0,99% | -3,07% | +11,52% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 30 | 43,33% | +8,12% | -4,90% | -2,58% | +12,06% | PRIMA CALIBRAZIONE |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | -0,41% | -0,41% | -5,42% | +4,34% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 68 | 92,65% | +11,50% | +10,87% | -3,03% | +15,84% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 71 | 90,14% | +11,51% | +11,51% | -3,01% | +15,94% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 71 | 90,14% | +11,51% | +11,51% | -3,01% | +15,94% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 64 | 64,06% | +11,54% | +1,13% | -2,99% | +16,06% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 29 | 55,17% | +11,81% | -2,82% | -2,66% | +16,49% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +2,81% | +2,81% | -5,71% | +6,60% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 57 | 94,74% | +18,57% | +16,25% | -2,93% | +23,64% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 60 | 100,00% | +18,99% | +18,99% | -2,91% | +23,95% | UTILE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 60 | 100,00% | +18,99% | +18,99% | -2,91% | +23,95% | UTILE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 55 | 60,00% | +18,81% | -1,16% | -2,77% | +23,82% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,92% | -4,17% | -2,62% | +19,88% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +7,72% | +7,72% | -5,13% | +13,34% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 42 | 92,86% | +26,00% | +22,42% | -2,15% | +31,61% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 45 | 100,00% | +25,96% | +25,96% | -2,17% | +31,67% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 45 | 100,00% | +25,96% | +25,96% | -2,17% | +31,67% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +28,58% | +28,58% | -2,21% | +34,30% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 40 | 45,00% | +26,01% | -5,86% | -1,88% | +31,92% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 13 | 38,46% | +23,69% | -16,03% | -0,70% | +29,98% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +17,26% | +17,26% | -2,41% | +21,34% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 87 | 48,28% | +0,02% | -0,06% | -0,75% | +1,05% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 96 | 57,29% | -0,05% | +0,43% | -0,87% | +0,92% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 96 | 57,29% | -0,05% | +0,43% | -0,87% | +0,92% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 90 | 51,11% | -0,13% | +0,18% | -0,97% | +0,84% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 57 | 42,11% | -0,05% | -0,52% | -0,95% | +0,67% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 13 | 53,85% | +1,93% | +1,69% | +0,19% | +2,94% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 87 | 43,68% | +0,16% | -0,12% | -0,95% | +1,53% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 95 | 56,84% | -0,03% | +0,64% | -1,11% | +1,26% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 95 | 56,84% | -0,03% | +0,64% | -1,11% | +1,26% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 89 | 53,93% | -0,31% | +0,22% | -1,39% | +0,98% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 56 | 44,64% | +0,01% | -0,87% | -1,14% | +1,03% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 13 | 38,46% | +1,97% | +1,77% | +0,35% | +4,40% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 87 | 40,23% | +0,37% | +0,03% | -2,58% | +3,57% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 94 | 55,32% | +0,08% | +0,91% | -2,76% | +3,27% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 94 | 55,32% | +0,08% | +0,91% | -2,76% | +3,27% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 88 | 46,59% | -0,48% | +0,05% | -2,99% | +2,68% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 55 | 36,36% | +0,23% | -1,61% | -2,77% | +3,40% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 50,00% | +2,30% | +2,13% | -1,68% | +5,97% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 85 | 45,88% | +0,86% | +0,11% | -3,83% | +5,69% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 92 | 51,09% | +0,47% | +1,20% | -4,09% | +5,37% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 92 | 51,09% | +0,47% | +1,20% | -4,09% | +5,37% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 86 | 53,49% | -0,26% | -0,50% | -4,46% | +4,69% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 53 | 41,51% | +1,01% | -3,42% | -4,14% | +5,92% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 33,33% | +1,94% | +1,81% | -2,90% | +8,39% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 84 | 48,81% | +1,21% | +0,41% | -4,64% | +7,39% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 91 | 54,95% | +0,90% | +1,40% | -4,91% | +7,03% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 91 | 54,95% | +0,90% | +1,40% | -4,91% | +7,03% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 85 | 48,24% | -0,00% | -0,72% | -5,35% | +6,14% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 52 | 36,54% | +1,70% | -4,60% | -4,94% | +7,69% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 41,67% | +0,56% | +0,47% | -3,35% | +8,92% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 81 | 43,21% | +1,56% | +0,30% | -5,54% | +9,24% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 88 | 54,55% | +1,03% | +1,72% | -5,82% | +8,81% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 88 | 54,55% | +1,03% | +1,72% | -5,82% | +8,81% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 82 | 47,56% | -0,18% | -1,53% | -6,35% | +7,48% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 50 | 38,00% | +2,12% | -5,38% | -5,84% | +9,64% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 78 | 53,85% | +2,93% | +2,51% | -6,47% | +12,51% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 84 | 66,67% | +2,14% | +4,10% | -6,69% | +11,91% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 84 | 66,67% | +2,14% | +4,10% | -6,69% | +11,91% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 78 | 44,87% | +0,26% | -2,27% | -7,31% | +9,60% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 46 | 41,30% | +3,56% | -5,08% | -6,09% | +12,35% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 74 | 52,70% | +5,49% | +0,25% | -6,84% | +17,47% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 77 | 62,34% | +5,88% | +5,59% | -6,78% | +17,68% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 77 | 62,34% | +5,88% | +5,59% | -6,78% | +17,68% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 71 | 49,30% | +3,93% | -3,75% | -7,49% | +15,03% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 44 | 40,91% | +4,63% | -7,88% | -6,37% | +15,31% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +4,84% | -0,04% | -5,47% | +18,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 67 | 65,67% | +9,64% | +4,00% | -6,04% | +24,98% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 70 | 70,00% | +9,98% | +7,18% | -6,00% | +25,43% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 70 | 70,00% | +9,98% | +7,18% | -6,00% | +25,43% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 64 | 56,25% | +8,53% | -2,88% | -6,73% | +23,41% | UTILE |
| DOGE | 30g | Classic technical | CALIBRABILE | 42 | 47,62% | +7,56% | -6,97% | -6,17% | +22,27% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 72,73% | +14,01% | +8,26% | -6,83% | +27,95% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 56 | 48,21% | +16,70% | +3,35% | -5,53% | +35,99% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 59 | 67,80% | +16,52% | +7,97% | -5,50% | +35,96% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 59 | 67,80% | +16,52% | +7,97% | -5,50% | +35,96% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 53 | 9,43% | +13,56% | -12,24% | -6,33% | +33,89% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 34 | 2,94% | +18,65% | -21,04% | -6,03% | +36,58% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +18,19% | +8,68% | -5,75% | +33,52% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 43 | 44,19% | +21,57% | -0,70% | -4,34% | +42,81% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 45 | 55,56% | +22,13% | +7,63% | -4,34% | +43,02% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 45 | 55,56% | +22,13% | +7,63% | -4,34% | +43,02% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +24,96% | +11,95% | -3,59% | +45,33% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 38 | 7,89% | +22,12% | -21,93% | -5,17% | +41,58% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 30 | 0,00% | +20,24% | -22,52% | -4,99% | +41,38% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +19,54% | +8,85% | -4,76% | +39,64% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 88 | 46,59% | +0,18% | +0,08% | -0,61% | +1,03% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 91 | 52,75% | +0,14% | +0,39% | -0,72% | +0,99% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 94 | 52,13% | +0,17% | +0,34% | -0,68% | +1,01% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 89 | 47,19% | +0,13% | -0,07% | -0,77% | +0,96% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 59 | 44,07% | +0,51% | -0,09% | -0,48% | +1,43% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 87 | 43,68% | +0,55% | +0,43% | -0,66% | +1,61% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 90 | 50,00% | +0,43% | +0,60% | -0,87% | +1,38% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 93 | 49,46% | +0,43% | +0,57% | -0,84% | +1,42% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 88 | 44,32% | +0,26% | -0,03% | -0,84% | +1,38% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,60% | +0,15% | -0,64% | +1,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 86 | 47,67% | +0,94% | +0,79% | -2,21% | +3,55% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 89 | 50,56% | +0,79% | +1,12% | -2,35% | +3,36% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 92 | 50,00% | +0,77% | +1,07% | -2,31% | +3,36% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 87 | 45,98% | +0,42% | -0,32% | -2,38% | +2,97% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 59 | 45,76% | +0,61% | +0,08% | -2,23% | +3,14% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 84 | 48,81% | +1,67% | +1,59% | -3,26% | +5,51% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 87 | 54,02% | +1,48% | +1,84% | -3,39% | +5,27% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 90 | 53,33% | +1,45% | +1,75% | -3,34% | +5,23% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 85 | 44,71% | +1,11% | -0,76% | -3,44% | +4,76% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,71% | -0,02% | -3,27% | +4,40% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 83 | 53,01% | +2,48% | +2,54% | -3,96% | +6,97% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 86 | 59,30% | +2,23% | +2,96% | -4,08% | +6,73% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 89 | 59,55% | +2,15% | +2,87% | -4,04% | +6,63% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 84 | 41,67% | +1,34% | -1,62% | -4,17% | +5,91% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 59 | 42,37% | +0,39% | -0,27% | -4,06% | +5,04% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 81 | 53,09% | +3,68% | +3,78% | -4,66% | +8,83% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 83 | 66,27% | +3,55% | +5,32% | -4,77% | +8,52% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 86 | 65,12% | +3,42% | +5,15% | -4,73% | +8,36% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 81 | 43,21% | +2,06% | -2,19% | -4,94% | +7,27% | UTILE |
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
