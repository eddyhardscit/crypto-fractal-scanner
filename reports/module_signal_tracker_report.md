# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-10 05:33 UTC

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

Segnali totali salvati: **258**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-10 | BTC | 82.650,00 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-10 | DOGE | 0.08645 | -1 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-10 | SOL | 110,05 | +6 | +3 | +3 | 0 | +1 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-09 | BTC | 82.441,21 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-09 | DOGE | 0.08534 | 0 | +2 | +2 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-09 | SOL | 110,52 | +1 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-08 | BTC | 82.929,12 | +2 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-08 | DOGE | 0.08776 | -3 | -1 | -1 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-08 | SOL | 115,60 | +1 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-07 | BTC | 84.216,36 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-07 | DOGE | 0.09034 | -3 | -2 | -2 | 0 | -1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-07 | SOL | 118,68 | +1 | -2 | -2 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 86 | 85 | 84 | 83 | 81 | 79 | 77 | 73 | 69 | 62 | 47 | 34 |
| SOL | 86 | 85 | 84 | 83 | 81 | 79 | 77 | 73 | 69 | 62 | 47 | 34 |
| DOGE | 86 | 85 | 84 | 83 | 81 | 79 | 77 | 73 | 69 | 62 | 47 | 34 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-27 | 45g | 2026-10-11 | domani |
| SOL | 2026-08-27 | 45g | 2026-10-11 | domani |
| DOGE | 2026-08-27 | 45g | 2026-10-11 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 78 | 52,56% | +0,31% | +0,29% | UTILE |
| BTC | 2g | 78 | 51,28% | +0,56% | +0,50% | UTILE |
| BTC | 3g | 77 | 45,45% | +0,70% | +0,61% | UTILE |
| BTC | 5g | 76 | 43,42% | +1,48% | +1,32% | UTILE |
| BTC | 7g | 74 | 54,05% | +2,31% | +2,16% | UTILE |
| BTC | 10g | 72 | 59,72% | +3,30% | +3,18% | UTILE |
| BTC | 14g | 69 | 60,87% | +4,85% | +4,80% | UTILE |
| BTC | 21g | 66 | 74,24% | +8,41% | +8,31% | UTILE |
| BTC | 30g | 59 | 94,92% | +12,52% | +11,79% | PRIMA CALIBRAZIONE |
| BTC | 45g | 44 | 93,18% | +22,71% | +19,71% | PRIMA CALIBRAZIONE |
| BTC | 60g | 32 | 90,62% | +27,86% | +23,17% | PRIMA CALIBRAZIONE |
| SOL | 1g | 77 | 48,05% | +0,24% | +0,16% | UTILE |
| SOL | 2g | 76 | 46,05% | +0,75% | +0,66% | UTILE |
| SOL | 3g | 75 | 50,67% | +1,33% | +1,21% | UTILE |
| SOL | 5g | 73 | 54,79% | +2,54% | +2,46% | UTILE |
| SOL | 7g | 71 | 60,56% | +3,89% | +3,97% | UTILE |
| SOL | 10g | 69 | 62,32% | +5,79% | +5,90% | UTILE |
| SOL | 14g | 65 | 72,31% | +8,88% | +9,44% | UTILE |
| SOL | 21g | 61 | 83,61% | +15,23% | +14,65% | UTILE |
| SOL | 30g | 55 | 81,82% | +20,80% | +17,20% | PRIMA CALIBRAZIONE |
| SOL | 45g | 40 | 72,50% | +39,74% | +20,50% | PRIMA CALIBRAZIONE |
| SOL | 60g | 27 | 59,26% | +47,35% | +14,89% | FEEDBACK RAPIDO |
| DOGE | 1g | 78 | 47,44% | +0,05% | +0,00% | UTILE |
| DOGE | 2g | 78 | 46,15% | +0,30% | -0,01% | UTILE |
| DOGE | 3g | 77 | 40,26% | +0,61% | +0,11% | UTILE |
| DOGE | 5g | 75 | 44,00% | +1,52% | +0,02% | UTILE |
| DOGE | 7g | 75 | 48,00% | +2,08% | +0,19% | UTILE |
| DOGE | 10g | 73 | 41,10% | +2,72% | -0,13% | UTILE |
| DOGE | 14g | 69 | 55,07% | +4,78% | +2,85% | UTILE |
| DOGE | 21g | 65 | 60,00% | +8,47% | +2,51% | UTILE |
| DOGE | 30g | 58 | 70,69% | +11,80% | +5,37% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 45 | 46,67% | +22,11% | +4,35% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 32 | 37,50% | +26,82% | -3,10% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 78 | 52,56% | +0,31% | +0,29% | -0,24% | +0,83% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 83 | 50,60% | +0,23% | +0,32% | -0,28% | +0,74% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 83 | 50,60% | +0,23% | +0,32% | -0,28% | +0,74% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 78 | 43,59% | +0,25% | -0,01% | -0,22% | +0,78% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,55% | -0,03% | -0,23% | +1,11% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,49% | -0,49% | -1,07% | -0,05% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 78 | 51,28% | +0,56% | +0,50% | -0,22% | +1,25% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 82 | 53,66% | +0,52% | +0,66% | -0,21% | +1,21% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 82 | 53,66% | +0,52% | +0,66% | -0,21% | +1,21% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 77 | 42,86% | +0,51% | -0,03% | -0,12% | +1,20% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,89% | -0,12% | -0,02% | +1,61% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,28% | -0,28% | -1,06% | +0,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 77 | 45,45% | +0,70% | +0,61% | -1,25% | +2,48% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 81 | 51,85% | +0,85% | +0,93% | -1,29% | +2,57% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 81 | 51,85% | +0,85% | +0,93% | -1,29% | +2,57% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 76 | 35,53% | +0,87% | -0,24% | -1,21% | +2,60% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,44% | -0,66% | -1,08% | +3,10% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,50% | -0,50% | -1,88% | +1,29% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 76 | 43,42% | +1,48% | +1,32% | -1,85% | +3,92% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 79 | 46,84% | +1,72% | +1,66% | -1,81% | +4,12% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 79 | 46,84% | +1,72% | +1,66% | -1,81% | +4,12% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 74 | 41,89% | +1,59% | -0,70% | -1,76% | +4,07% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 33 | 36,36% | +3,24% | -2,30% | -1,55% | +5,67% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 74 | 54,05% | +2,31% | +2,16% | -2,12% | +5,11% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 78 | 55,13% | +2,51% | +2,38% | -2,11% | +5,27% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 78 | 55,13% | +2,51% | +2,38% | -2,11% | +5,27% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 72 | 45,83% | +2,54% | -1,00% | -2,03% | +5,28% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 31 | 35,48% | +4,86% | -3,97% | -1,74% | +7,97% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 72 | 59,72% | +3,30% | +3,18% | -2,39% | +6,36% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 76 | 65,79% | +3,42% | +3,40% | -2,34% | +6,48% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 76 | 65,79% | +3,42% | +3,40% | -2,34% | +6,48% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 70 | 48,57% | +3,48% | -0,32% | -2,30% | +6,59% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 29 | 41,38% | +5,56% | -4,39% | -1,70% | +9,12% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -1,21% | -1,21% | -3,81% | +1,86% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 69 | 60,87% | +4,85% | +4,80% | -2,63% | +8,51% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 73 | 61,64% | +4,84% | +4,88% | -2,63% | +8,53% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 73 | 61,64% | +4,84% | +4,88% | -2,63% | +8,53% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 66 | 56,06% | +5,13% | +1,46% | -2,58% | +8,86% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 29 | 24,14% | +5,09% | -4,15% | -1,91% | +9,57% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,11% | -0,11% | -4,30% | +2,85% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 66 | 74,24% | +8,41% | +8,31% | -2,80% | +12,27% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 69 | 78,26% | +8,34% | +8,34% | -2,78% | +12,22% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 69 | 78,26% | +8,34% | +8,34% | -2,78% | +12,22% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 62 | 58,06% | +8,84% | +1,49% | -2,74% | +12,73% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 28 | 46,43% | +9,04% | -4,92% | -2,22% | +12,89% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 59 | 94,92% | +12,52% | +11,79% | -3,00% | +16,60% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 62 | 91,94% | +12,48% | +12,48% | -2,97% | +16,68% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 62 | 91,94% | +12,48% | +12,48% | -2,97% | +16,68% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 57 | 63,16% | +12,46% | +0,77% | -2,84% | +16,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,37% | -2,02% | -2,62% | +17,60% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 44 | 93,18% | +22,71% | +19,71% | -2,34% | +27,43% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 47 | 100,00% | +22,99% | +22,99% | -2,34% | +27,58% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 47 | 100,00% | +22,99% | +22,99% | -2,34% | +27,58% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 42 | 47,62% | +23,22% | -2,93% | -2,09% | +27,85% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 15 | 46,67% | +19,25% | -9,70% | -1,43% | +25,07% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 32 | 90,62% | +27,86% | +23,17% | -2,96% | +32,94% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 34 | 100,00% | +27,66% | +27,66% | -3,00% | +32,81% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 34 | 100,00% | +27,66% | +27,66% | -3,00% | +32,81% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 30 | 100,00% | +28,33% | +28,33% | -2,80% | +33,68% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 29 | 41,38% | +28,03% | -5,53% | -2,74% | +33,36% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 4 | 0,00% | +33,67% | -33,67% | -1,55% | +38,08% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 78 | 47,44% | +0,05% | +0,00% | -0,74% | +1,10% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 84 | 59,52% | +0,03% | +0,58% | -0,76% | +1,02% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 84 | 59,52% | +0,03% | +0,58% | -0,76% | +1,02% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 78 | 50,00% | -0,06% | +0,11% | -0,87% | +0,93% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 46 | 39,13% | -0,02% | -0,68% | -0,90% | +0,69% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 78 | 46,15% | +0,30% | -0,01% | -0,83% | +1,66% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 83 | 59,04% | +0,14% | +0,90% | -0,96% | +1,45% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 83 | 59,04% | +0,14% | +0,90% | -0,96% | +1,45% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 77 | 53,25% | -0,17% | +0,07% | -1,28% | +1,14% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 45 | 42,22% | +0,28% | -1,35% | -0,94% | +1,23% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 77 | 40,26% | +0,61% | +0,11% | -2,46% | +3,83% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 82 | 57,32% | +0,35% | +1,23% | -2,62% | +3,56% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 82 | 57,32% | +0,35% | +1,23% | -2,62% | +3,56% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 76 | 43,42% | -0,28% | -0,22% | -2,87% | +2,89% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 44 | 29,55% | +0,62% | -2,34% | -2,62% | +3,83% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 75 | 44,00% | +1,52% | +0,02% | -3,35% | +6,31% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 80 | 53,75% | +1,19% | +1,60% | -3,60% | +6,03% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 80 | 53,75% | +1,19% | +1,60% | -3,60% | +6,03% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 74 | 48,65% | +0,40% | -1,01% | -3,98% | +5,30% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 44 | 31,82% | +1,94% | -4,85% | -3,72% | +6,77% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 75 | 48,00% | +2,08% | +0,19% | -4,08% | +8,18% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 78 | 56,41% | +2,12% | +1,62% | -4,09% | +8,02% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 78 | 56,41% | +2,12% | +1,62% | -4,09% | +8,02% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 72 | 44,44% | +1,16% | -1,26% | -4,55% | +7,05% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 44 | 27,27% | +3,07% | -6,50% | -4,35% | +8,81% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 73 | 41,10% | +2,72% | -0,13% | -4,77% | +10,13% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 76 | 53,95% | +2,68% | +1,39% | -4,75% | +9,99% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 76 | 53,95% | +2,68% | +1,39% | -4,75% | +9,99% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 70 | 45,71% | +1,40% | -1,77% | -5,28% | +8,53% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 43 | 30,23% | +3,70% | -7,04% | -4,91% | +11,04% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 69 | 55,07% | +4,78% | +2,85% | -5,35% | +13,87% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 72 | 62,50% | +4,43% | +3,04% | -5,30% | +13,50% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 72 | 62,50% | +4,43% | +3,04% | -5,30% | +13,50% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 66 | 48,48% | +2,41% | -1,34% | -5,91% | +10,92% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 43 | 39,53% | +4,51% | -5,45% | -5,57% | +13,12% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 65 | 60,00% | +8,47% | +2,51% | -5,17% | +19,56% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 68 | 57,35% | +8,79% | +4,21% | -5,19% | +19,71% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 68 | 57,35% | +8,79% | +4,21% | -5,19% | +19,71% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 62 | 56,45% | +6,83% | -1,96% | -5,84% | +16,87% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 41 | 43,90% | +6,23% | -7,20% | -5,36% | +16,47% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 70,00% | +6,74% | +1,36% | -4,20% | +19,90% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 58 | 70,69% | +11,80% | +5,37% | -5,53% | +25,55% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 61 | 72,13% | +12,08% | +7,61% | -5,51% | +26,04% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 61 | 72,13% | +12,08% | +7,61% | -5,51% | +26,04% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 55 | 60,00% | +10,63% | -2,57% | -6,30% | +23,76% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 34 | 50,00% | +9,92% | -7,89% | -5,82% | +22,04% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 88,89% | +19,48% | +12,44% | -5,48% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 45 | 46,67% | +22,11% | +4,35% | -4,47% | +39,32% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 46 | 58,70% | +22,58% | +8,83% | -4,36% | +39,75% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 46 | 58,70% | +22,58% | +8,83% | -4,36% | +39,75% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 40 | 12,50% | +19,57% | -14,62% | -5,28% | +37,58% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 31 | 3,23% | +21,52% | -22,01% | -5,10% | +38,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +24,92% | +12,69% | -3,96% | +37,45% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 32 | 37,50% | +26,82% | -3,10% | -4,35% | +44,37% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 34 | 52,94% | +27,26% | +8,06% | -4,36% | +44,55% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 34 | 52,94% | +27,26% | +8,06% | -4,36% | +44,55% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | +26,49% | +11,04% | -4,40% | +44,30% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 30 | 0,00% | +27,32% | -27,32% | -4,76% | +43,74% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 22 | 0,00% | +25,52% | -25,52% | -4,86% | +42,69% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +38,20% | +19,48% | -1,31% | +51,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 77 | 48,05% | +0,24% | +0,16% | -0,50% | +1,10% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 79 | 55,70% | +0,22% | +0,51% | -0,61% | +1,08% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 82 | 54,88% | +0,26% | +0,45% | -0,57% | +1,10% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 77 | 45,45% | +0,22% | -0,13% | -0,67% | +1,05% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 57 | 45,61% | +0,47% | -0,02% | -0,53% | +1,41% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 76 | 46,05% | +0,75% | +0,66% | -0,48% | +1,82% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 78 | 51,28% | +0,65% | +0,85% | -0,70% | +1,57% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 81 | 50,62% | +0,64% | +0,81% | -0,68% | +1,62% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 76 | 40,79% | +0,46% | -0,25% | -0,67% | +1,59% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 57 | 47,37% | +0,57% | +0,14% | -0,69% | +1,64% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 75 | 50,67% | +1,33% | +1,21% | -2,00% | +3,86% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 77 | 53,25% | +1,17% | +1,41% | -2,15% | +3,68% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 80 | 52,50% | +1,14% | +1,34% | -2,11% | +3,67% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 75 | 44,00% | +0,75% | -0,44% | -2,17% | +3,23% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 57 | 47,37% | +0,64% | +0,14% | -2,20% | +3,12% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 73 | 54,79% | +2,54% | +2,46% | -2,70% | +6,17% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 75 | 54,67% | +2,30% | +2,17% | -2,85% | +5,94% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 78 | 53,85% | +2,24% | +2,06% | -2,82% | +5,86% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 73 | 45,21% | +1,90% | -0,73% | -2,89% | +5,37% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 55 | 50,91% | +1,10% | +0,41% | -2,93% | +4,60% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 71 | 60,56% | +3,89% | +3,97% | -3,08% | +8,00% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 73 | 61,64% | +3,61% | +3,19% | -3,24% | +7,74% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 76 | 61,84% | +3,46% | +3,07% | -3,21% | +7,59% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 71 | 40,85% | +2,60% | -1,43% | -3,32% | +6,80% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 53 | 47,17% | +1,16% | +0,53% | -3,40% | +5,43% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 69 | 62,32% | +5,79% | +5,90% | -3,43% | +10,26% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 71 | 67,61% | +5,58% | +5,43% | -3,60% | +9,85% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 74 | 66,22% | +5,35% | +5,22% | -3,60% | +9,61% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 69 | 44,93% | +3,88% | -1,61% | -3,77% | +8,42% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 51 | 49,02% | +1,47% | +0,70% | -3,91% | +6,38% | PRIMA CALIBRAZIONE |

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
