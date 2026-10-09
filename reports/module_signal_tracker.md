# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-09 05:33 UTC

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

Segnali totali salvati: **255**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-09 | BTC | 82.441,21 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-09 | DOGE | 0.08534 | 0 | +2 | +2 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-09 | SOL | 110,52 | +1 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-08 | BTC | 82.929,12 | +2 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-08 | DOGE | 0.08776 | -3 | -1 | -1 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-08 | SOL | 115,60 | +1 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-07 | BTC | 84.216,36 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-07 | DOGE | 0.09034 | -3 | -2 | -2 | 0 | -1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-07 | SOL | 118,68 | +1 | -2 | -2 | 0 | +2 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-06 | BTC | 85.661,60 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-06 | DOGE | 0.09487 | -1 | -2 | -2 | 0 | +1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-06 | SOL | 120,08 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 85 | 84 | 83 | 82 | 80 | 78 | 76 | 72 | 69 | 61 | 46 | 33 |
| SOL | 85 | 84 | 83 | 82 | 80 | 78 | 76 | 72 | 69 | 61 | 46 | 33 |
| DOGE | 85 | 84 | 83 | 82 | 80 | 78 | 76 | 72 | 69 | 61 | 46 | 33 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-11 | 60g | 2026-10-10 | domani |
| SOL | 2026-08-11 | 60g | 2026-10-10 | domani |
| DOGE | 2026-08-11 | 60g | 2026-10-10 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 78 | 52,56% | +0,31% | +0,29% | UTILE |
| BTC | 2g | 77 | 51,95% | +0,58% | +0,52% | UTILE |
| BTC | 3g | 77 | 45,45% | +0,70% | +0,61% | UTILE |
| BTC | 5g | 75 | 44,00% | +1,55% | +1,38% | UTILE |
| BTC | 7g | 73 | 54,79% | +2,37% | +2,22% | UTILE |
| BTC | 10g | 71 | 60,56% | +3,36% | +3,23% | UTILE |
| BTC | 14g | 69 | 60,87% | +4,85% | +4,80% | UTILE |
| BTC | 21g | 66 | 74,24% | +8,41% | +8,31% | UTILE |
| BTC | 30g | 58 | 94,83% | +12,64% | +11,90% | PRIMA CALIBRAZIONE |
| BTC | 45g | 43 | 93,02% | +23,14% | +20,06% | PRIMA CALIBRAZIONE |
| BTC | 60g | 31 | 90,32% | +27,81% | +22,97% | PRIMA CALIBRAZIONE |
| SOL | 1g | 76 | 48,68% | +0,24% | +0,16% | UTILE |
| SOL | 2g | 75 | 46,67% | +0,83% | +0,73% | UTILE |
| SOL | 3g | 74 | 51,35% | +1,45% | +1,33% | UTILE |
| SOL | 5g | 72 | 55,56% | +2,69% | +2,61% | UTILE |
| SOL | 7g | 70 | 61,43% | +4,06% | +4,14% | UTILE |
| SOL | 10g | 68 | 63,24% | +5,99% | +6,10% | UTILE |
| SOL | 14g | 64 | 73,44% | +9,15% | +9,72% | UTILE |
| SOL | 21g | 61 | 83,61% | +15,23% | +14,65% | UTILE |
| SOL | 30g | 54 | 81,48% | +21,04% | +17,38% | PRIMA CALIBRAZIONE |
| SOL | 45g | 39 | 71,79% | +40,41% | +20,68% | PRIMA CALIBRAZIONE |
| SOL | 60g | 26 | 57,69% | +47,42% | +13,72% | FEEDBACK RAPIDO |
| DOGE | 1g | 78 | 47,44% | +0,05% | +0,00% | UTILE |
| DOGE | 2g | 77 | 45,45% | +0,32% | -0,03% | UTILE |
| DOGE | 3g | 76 | 39,47% | +0,68% | +0,06% | UTILE |
| DOGE | 5g | 75 | 44,00% | +1,52% | +0,02% | UTILE |
| DOGE | 7g | 74 | 47,30% | +2,20% | +0,09% | UTILE |
| DOGE | 10g | 72 | 41,67% | +2,87% | -0,02% | UTILE |
| DOGE | 14g | 68 | 55,88% | +5,01% | +3,05% | UTILE |
| DOGE | 21g | 65 | 60,00% | +8,47% | +2,51% | UTILE |
| DOGE | 30g | 57 | 71,93% | +12,00% | +5,47% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 44 | 47,73% | +22,62% | +4,46% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 31 | 35,48% | +26,92% | -3,96% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 78 | 52,56% | +0,31% | +0,29% | -0,24% | +0,83% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 82 | 51,22% | +0,23% | +0,32% | -0,28% | +0,75% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 82 | 51,22% | +0,23% | +0,32% | -0,28% | +0,75% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 77 | 42,86% | +0,25% | -0,02% | -0,22% | +0,79% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,55% | -0,03% | -0,23% | +1,11% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,49% | -0,49% | -1,07% | -0,05% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 77 | 51,95% | +0,58% | +0,52% | -0,22% | +1,28% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 81 | 53,09% | +0,53% | +0,67% | -0,21% | +1,23% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 81 | 53,09% | +0,53% | +0,67% | -0,21% | +1,23% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 76 | 43,42% | +0,52% | -0,03% | -0,11% | +1,22% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,89% | -0,12% | -0,02% | +1,61% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,28% | -0,28% | -1,06% | +0,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 77 | 45,45% | +0,70% | +0,61% | -1,25% | +2,48% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 80 | 51,25% | +0,89% | +0,92% | -1,25% | +2,61% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 80 | 51,25% | +0,89% | +0,92% | -1,25% | +2,61% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 75 | 36,00% | +0,91% | -0,22% | -1,17% | +2,65% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,44% | -0,66% | -1,08% | +3,10% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,50% | -0,50% | -1,88% | +1,29% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 75 | 44,00% | +1,55% | +1,38% | -1,80% | +3,95% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 78 | 46,15% | +1,79% | +1,64% | -1,76% | +4,15% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 78 | 46,15% | +1,79% | +1,64% | -1,76% | +4,15% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 73 | 42,47% | +1,65% | -0,67% | -1,70% | +4,10% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 32 | 37,50% | +3,45% | -2,27% | -1,41% | +5,81% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 73 | 54,79% | +2,37% | +2,22% | -2,08% | +5,14% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 77 | 54,55% | +2,57% | +2,38% | -2,08% | +5,30% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 77 | 54,55% | +2,57% | +2,38% | -2,08% | +5,30% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 71 | 46,48% | +2,61% | -0,98% | -1,99% | +5,31% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 30 | 36,67% | +5,10% | -4,02% | -1,63% | +8,15% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 71 | 60,56% | +3,36% | +3,23% | -2,37% | +6,38% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 76 | 65,79% | +3,42% | +3,40% | -2,34% | +6,48% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 76 | 65,79% | +3,42% | +3,40% | -2,34% | +6,48% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 69 | 49,28% | +3,55% | -0,31% | -2,28% | +6,62% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 29 | 41,38% | +5,56% | -4,39% | -1,70% | +9,12% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -1,21% | -1,21% | -3,81% | +1,86% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 69 | 60,87% | +4,85% | +4,80% | -2,63% | +8,51% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 72 | 61,11% | +4,93% | +4,93% | -2,61% | +8,60% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 72 | 61,11% | +4,93% | +4,93% | -2,61% | +8,60% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 65 | 56,92% | +5,23% | +1,50% | -2,55% | +8,94% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 29 | 24,14% | +5,09% | -4,15% | -1,91% | +9,57% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,11% | -0,11% | -4,30% | +2,85% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 66 | 74,24% | +8,41% | +8,31% | -2,80% | +12,27% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 69 | 78,26% | +8,34% | +8,34% | -2,78% | +12,22% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 69 | 78,26% | +8,34% | +8,34% | -2,78% | +12,22% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 62 | 58,06% | +8,84% | +1,49% | -2,74% | +12,73% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 28 | 46,43% | +9,04% | -4,92% | -2,22% | +12,89% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 58 | 94,83% | +12,64% | +11,90% | -2,97% | +16,69% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 61 | 91,80% | +12,60% | +12,60% | -2,94% | +16,77% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 61 | 91,80% | +12,60% | +12,60% | -2,94% | +16,77% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 56 | 62,50% | +12,59% | +0,69% | -2,81% | +16,94% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,37% | -2,02% | -2,62% | +17,60% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 43 | 93,02% | +23,14% | +20,06% | -2,27% | +27,82% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 46 | 100,00% | +23,39% | +23,39% | -2,28% | +27,96% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 46 | 100,00% | +23,39% | +23,39% | -2,28% | +27,96% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 41 | 46,34% | +23,68% | -3,11% | -2,01% | +28,27% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 14 | 42,86% | +20,30% | -10,71% | -1,16% | +26,12% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 31 | 90,32% | +27,81% | +22,97% | -2,98% | +32,82% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 33 | 100,00% | +27,61% | +27,61% | -3,02% | +32,69% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 33 | 100,00% | +27,61% | +27,61% | -3,02% | +32,69% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 29 | 100,00% | +28,30% | +28,30% | -2,82% | +33,58% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 28 | 39,29% | +27,98% | -6,77% | -2,76% | +33,23% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 4 | 0,00% | +33,67% | -33,67% | -1,55% | +38,08% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 78 | 47,44% | +0,05% | +0,00% | -0,74% | +1,10% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 83 | 59,04% | +0,01% | +0,57% | -0,77% | +1,02% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 83 | 59,04% | +0,01% | +0,57% | -0,77% | +1,02% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 77 | 50,65% | -0,08% | +0,13% | -0,88% | +0,93% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 45 | 40,00% | -0,05% | -0,66% | -0,92% | +0,68% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 77 | 45,45% | +0,32% | -0,03% | -0,80% | +1,70% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 82 | 58,54% | +0,16% | +0,90% | -0,93% | +1,48% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 82 | 58,54% | +0,16% | +0,90% | -0,93% | +1,48% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 76 | 52,63% | -0,15% | +0,05% | -1,26% | +1,17% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 44 | 40,91% | +0,32% | -1,41% | -0,90% | +1,29% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 76 | 39,47% | +0,68% | +0,06% | -2,36% | +3,89% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 81 | 56,79% | +0,41% | +1,20% | -2,53% | +3,61% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 81 | 56,79% | +0,41% | +1,20% | -2,53% | +3,61% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 75 | 42,67% | -0,22% | -0,28% | -2,78% | +2,94% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 44 | 29,55% | +0,62% | -2,34% | -2,62% | +3,83% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 75 | 44,00% | +1,52% | +0,02% | -3,35% | +6,31% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 79 | 53,16% | +1,31% | +1,51% | -3,46% | +6,09% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 79 | 53,16% | +1,31% | +1,51% | -3,46% | +6,09% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 73 | 49,32% | +0,52% | -0,90% | -3,84% | +5,35% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 44 | 31,82% | +1,94% | -4,85% | -3,72% | +6,77% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 74 | 47,30% | +2,20% | +0,09% | -3,96% | +8,23% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 77 | 55,84% | +2,24% | +1,55% | -3,98% | +8,07% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 77 | 55,84% | +2,24% | +1,55% | -3,98% | +8,07% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 71 | 45,07% | +1,27% | -1,17% | -4,43% | +7,09% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 44 | 27,27% | +3,07% | -6,50% | -4,35% | +8,81% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 72 | 41,67% | +2,87% | -0,02% | -4,65% | +10,22% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 75 | 53,33% | +2,82% | +1,30% | -4,63% | +10,07% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 75 | 53,33% | +2,82% | +1,30% | -4,63% | +10,07% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 69 | 46,38% | +1,53% | -1,68% | -5,16% | +8,60% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 43 | 30,23% | +3,70% | -7,04% | -4,91% | +11,04% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 68 | 55,88% | +5,01% | +3,05% | -5,18% | +14,05% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 71 | 61,97% | +4,65% | +2,92% | -5,15% | +13,67% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 71 | 61,97% | +4,65% | +2,92% | -5,15% | +13,67% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 65 | 49,23% | +2,62% | -1,19% | -5,75% | +11,06% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 43 | 39,53% | +4,51% | -5,45% | -5,57% | +13,12% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 65 | 60,00% | +8,47% | +2,51% | -5,17% | +19,56% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 68 | 57,35% | +8,79% | +4,21% | -5,19% | +19,71% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 68 | 57,35% | +8,79% | +4,21% | -5,19% | +19,71% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 62 | 56,45% | +6,83% | -1,96% | -5,84% | +16,87% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 41 | 43,90% | +6,23% | -7,20% | -5,36% | +16,47% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 70,00% | +6,74% | +1,36% | -4,20% | +19,90% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 57 | 71,93% | +12,00% | +5,47% | -5,48% | +25,61% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 60 | 73,33% | +12,27% | +7,74% | -5,45% | +26,09% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 60 | 73,33% | +12,27% | +7,74% | -5,45% | +26,09% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 54 | 61,11% | +10,81% | -2,60% | -6,26% | +23,78% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 34 | 50,00% | +9,92% | -7,89% | -5,82% | +22,04% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 88,89% | +19,48% | +12,44% | -5,48% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 44 | 47,73% | +22,62% | +4,46% | -4,35% | +39,73% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 46 | 58,70% | +22,58% | +8,83% | -4,36% | +39,75% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 46 | 58,70% | +22,58% | +8,83% | -4,36% | +39,75% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 39 | 12,82% | +20,08% | -14,98% | -5,17% | +37,99% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 31 | 3,23% | +21,52% | -22,01% | -5,10% | +38,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +24,92% | +12,69% | -3,96% | +37,45% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 31 | 35,48% | +26,92% | -3,96% | -4,45% | +44,16% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 33 | 51,52% | +27,37% | +7,59% | -4,45% | +44,36% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 33 | 51,52% | +27,37% | +7,59% | -4,45% | +44,36% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 31 | 54,84% | +26,58% | +10,63% | -4,50% | +44,10% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 30 | 0,00% | +27,32% | -27,32% | -4,76% | +43,74% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 22 | 0,00% | +25,52% | -25,52% | -4,86% | +42,69% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +38,20% | +19,48% | -1,31% | +51,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 76 | 48,68% | +0,24% | +0,16% | -0,49% | +1,12% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 78 | 56,41% | +0,23% | +0,53% | -0,60% | +1,10% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 81 | 55,56% | +0,26% | +0,46% | -0,56% | +1,12% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 76 | 44,74% | +0,22% | -0,14% | -0,66% | +1,07% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 57 | 45,61% | +0,47% | -0,02% | -0,53% | +1,41% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 75 | 46,67% | +0,83% | +0,73% | -0,41% | +1,91% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 77 | 50,65% | +0,72% | +0,80% | -0,63% | +1,66% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 80 | 50,00% | +0,71% | +0,76% | -0,61% | +1,70% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 75 | 41,33% | +0,53% | -0,18% | -0,60% | +1,67% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 57 | 47,37% | +0,57% | +0,14% | -0,69% | +1,64% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 74 | 51,35% | +1,45% | +1,33% | -1,88% | +3,94% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 76 | 52,63% | +1,28% | +1,33% | -2,03% | +3,75% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 79 | 51,90% | +1,24% | +1,27% | -2,00% | +3,74% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 74 | 44,59% | +0,85% | -0,35% | -2,05% | +3,30% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 56 | 48,21% | +0,78% | +0,27% | -2,05% | +3,21% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 72 | 55,56% | +2,69% | +2,61% | -2,58% | +6,24% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 74 | 54,05% | +2,45% | +2,09% | -2,73% | +6,00% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 77 | 53,25% | +2,38% | +1,98% | -2,70% | +5,92% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 72 | 45,83% | +2,04% | -0,62% | -2,77% | +5,42% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 54 | 51,85% | +1,28% | +0,57% | -2,77% | +4,65% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 70 | 61,43% | +4,06% | +4,14% | -2,96% | +8,08% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 72 | 61,11% | +3,77% | +3,12% | -3,12% | +7,82% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 75 | 61,33% | +3,61% | +3,00% | -3,10% | +7,66% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 70 | 41,43% | +2,75% | -1,34% | -3,20% | +6,87% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 52 | 48,08% | +1,34% | +0,70% | -3,24% | +5,49% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 68 | 63,24% | +5,99% | +6,10% | -3,32% | +10,36% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 70 | 67,14% | +5,77% | +5,39% | -3,49% | +9,94% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 73 | 65,75% | +5,53% | +5,18% | -3,49% | +9,69% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 68 | 45,59% | +4,06% | -1,52% | -3,66% | +8,49% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 50 | 50,00% | +1,65% | +0,87% | -3,77% | +6,44% | PRIMA CALIBRAZIONE |

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
