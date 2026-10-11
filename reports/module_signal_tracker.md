# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-11 05:33 UTC

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

Segnali totali salvati: **261**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-11 | BTC | 83.006,99 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-11 | DOGE | 0.08535 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-11 | SOL | 109,56 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-10 | BTC | 82.650,00 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-10 | DOGE | 0.08645 | -1 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-10 | SOL | 110,05 | +6 | +3 | +3 | 0 | +1 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-09 | BTC | 82.441,21 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-09 | DOGE | 0.08534 | 0 | +2 | +2 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-09 | SOL | 110,52 | +1 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-08 | BTC | 82.929,12 | +2 | -1 | -1 | 0 | +2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-08 | DOGE | 0.08776 | -3 | -1 | -1 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-08 | SOL | 115,60 | +1 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 87 | 86 | 85 | 84 | 82 | 80 | 77 | 74 | 69 | 63 | 48 | 34 |
| SOL | 87 | 86 | 85 | 84 | 82 | 80 | 77 | 74 | 69 | 63 | 48 | 34 |
| DOGE | 87 | 86 | 85 | 84 | 82 | 80 | 77 | 74 | 69 | 63 | 48 | 34 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-28 | 45g | 2026-10-12 | domani |
| SOL | 2026-08-28 | 45g | 2026-10-12 | domani |
| DOGE | 2026-08-28 | 45g | 2026-10-12 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 78 | 52,56% | +0,31% | +0,29% | UTILE |
| BTC | 2g | 78 | 51,28% | +0,56% | +0,50% | UTILE |
| BTC | 3g | 78 | 46,15% | +0,69% | +0,60% | UTILE |
| BTC | 5g | 77 | 42,86% | +1,42% | +1,26% | UTILE |
| BTC | 7g | 75 | 53,33% | +2,25% | +2,10% | UTILE |
| BTC | 10g | 72 | 59,72% | +3,30% | +3,18% | UTILE |
| BTC | 14g | 69 | 60,87% | +4,85% | +4,80% | UTILE |
| BTC | 21g | 66 | 74,24% | +8,41% | +8,31% | UTILE |
| BTC | 30g | 60 | 95,00% | +12,44% | +11,72% | UTILE |
| BTC | 45g | 45 | 93,33% | +22,33% | +19,39% | PRIMA CALIBRAZIONE |
| BTC | 60g | 32 | 90,62% | +27,86% | +23,17% | PRIMA CALIBRAZIONE |
| SOL | 1g | 78 | 47,44% | +0,23% | +0,15% | UTILE |
| SOL | 2g | 77 | 45,45% | +0,73% | +0,64% | UTILE |
| SOL | 3g | 76 | 50,00% | +1,25% | +1,13% | UTILE |
| SOL | 5g | 74 | 54,05% | +2,39% | +2,31% | UTILE |
| SOL | 7g | 72 | 59,72% | +3,71% | +3,78% | UTILE |
| SOL | 10g | 69 | 62,32% | +5,79% | +5,90% | UTILE |
| SOL | 14g | 66 | 71,21% | +8,60% | +9,15% | UTILE |
| SOL | 21g | 61 | 83,61% | +15,23% | +14,65% | UTILE |
| SOL | 30g | 56 | 82,14% | +20,61% | +17,08% | PRIMA CALIBRAZIONE |
| SOL | 45g | 41 | 73,17% | +38,98% | +20,21% | PRIMA CALIBRAZIONE |
| SOL | 60g | 27 | 59,26% | +47,35% | +14,89% | FEEDBACK RAPIDO |
| DOGE | 1g | 79 | 48,10% | +0,03% | +0,02% | UTILE |
| DOGE | 2g | 78 | 46,15% | +0,30% | -0,01% | UTILE |
| DOGE | 3g | 78 | 41,03% | +0,57% | +0,15% | UTILE |
| DOGE | 5g | 76 | 44,74% | +1,37% | +0,15% | UTILE |
| DOGE | 7g | 75 | 48,00% | +2,08% | +0,19% | UTILE |
| DOGE | 10g | 73 | 41,10% | +2,72% | -0,13% | UTILE |
| DOGE | 14g | 70 | 54,29% | +4,55% | +2,65% | UTILE |
| DOGE | 21g | 65 | 60,00% | +8,47% | +2,51% | UTILE |
| DOGE | 30g | 59 | 69,49% | +11,63% | +5,25% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 46 | 47,83% | +21,61% | +4,28% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 32 | 37,50% | +26,82% | -3,10% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 78 | 52,56% | +0,31% | +0,29% | -0,24% | +0,83% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 84 | 50,00% | +0,23% | +0,31% | -0,28% | +0,74% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 84 | 50,00% | +0,23% | +0,31% | -0,28% | +0,74% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 79 | 44,30% | +0,25% | -0,01% | -0,22% | +0,78% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,55% | -0,03% | -0,23% | +1,11% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,49% | -0,49% | -1,07% | -0,05% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 78 | 51,28% | +0,56% | +0,50% | -0,22% | +1,25% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 83 | 53,01% | +0,52% | +0,65% | -0,20% | +1,21% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 83 | 53,01% | +0,52% | +0,65% | -0,20% | +1,21% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 78 | 43,59% | +0,51% | -0,02% | -0,11% | +1,19% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,89% | -0,12% | -0,02% | +1,61% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,28% | -0,28% | -1,06% | +0,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 78 | 46,15% | +0,69% | +0,60% | -1,25% | +2,46% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 82 | 51,22% | +0,84% | +0,92% | -1,29% | +2,55% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 82 | 51,22% | +0,84% | +0,92% | -1,29% | +2,55% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 77 | 36,36% | +0,86% | -0,23% | -1,22% | +2,57% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,44% | -0,66% | -1,08% | +3,10% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,50% | -0,50% | -1,88% | +1,29% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 77 | 42,86% | +1,42% | +1,26% | -1,91% | +3,87% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 80 | 47,50% | +1,66% | +1,68% | -1,87% | +4,07% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 80 | 47,50% | +1,66% | +1,68% | -1,87% | +4,07% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 75 | 41,33% | +1,52% | -0,74% | -1,82% | +4,01% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 34 | 35,29% | +3,06% | -2,33% | -1,68% | +5,50% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 75 | 53,33% | +2,25% | +2,10% | -2,17% | +5,08% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 78 | 55,13% | +2,51% | +2,38% | -2,11% | +5,27% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 78 | 55,13% | +2,51% | +2,38% | -2,11% | +5,27% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 73 | 45,21% | +2,48% | -1,01% | -2,08% | +5,24% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 32 | 34,38% | +4,64% | -3,91% | -1,85% | +7,80% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 72 | 59,72% | +3,30% | +3,18% | -2,39% | +6,36% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 76 | 65,79% | +3,42% | +3,40% | -2,34% | +6,48% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 76 | 65,79% | +3,42% | +3,40% | -2,34% | +6,48% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 70 | 48,57% | +3,48% | -0,32% | -2,30% | +6,59% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 29 | 41,38% | +5,56% | -4,39% | -1,70% | +9,12% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -1,21% | -1,21% | -3,81% | +1,86% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 69 | 60,87% | +4,85% | +4,80% | -2,63% | +8,51% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 74 | 62,16% | +4,75% | +4,84% | -2,66% | +8,46% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 74 | 62,16% | +4,75% | +4,84% | -2,66% | +8,46% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 67 | 55,22% | +5,03% | +1,41% | -2,61% | +8,78% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 29 | 24,14% | +5,09% | -4,15% | -1,91% | +9,57% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,11% | -0,11% | -4,30% | +2,85% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 66 | 74,24% | +8,41% | +8,31% | -2,80% | +12,27% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 69 | 78,26% | +8,34% | +8,34% | -2,78% | +12,22% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 69 | 78,26% | +8,34% | +8,34% | -2,78% | +12,22% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 62 | 58,06% | +8,84% | +1,49% | -2,74% | +12,73% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 28 | 46,43% | +9,04% | -4,92% | -2,22% | +12,89% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 60 | 95,00% | +12,44% | +11,72% | -2,99% | +16,55% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 63 | 92,06% | +12,40% | +12,40% | -2,97% | +16,63% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 63 | 92,06% | +12,40% | +12,40% | -2,97% | +16,63% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 58 | 63,79% | +12,38% | +0,89% | -2,84% | +16,78% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,37% | -2,02% | -2,62% | +17,60% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 45 | 93,33% | +22,33% | +19,39% | -2,39% | +27,07% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 48 | 100,00% | +22,62% | +22,62% | -2,39% | +27,24% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 48 | 100,00% | +22,62% | +22,62% | -2,39% | +27,24% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 43 | 48,84% | +22,81% | -2,73% | -2,15% | +27,46% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 16 | 50,00% | +18,39% | -8,74% | -1,64% | +24,20% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 32 | 90,62% | +27,86% | +23,17% | -2,96% | +32,94% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 34 | 100,00% | +27,66% | +27,66% | -3,00% | +32,81% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 34 | 100,00% | +27,66% | +27,66% | -3,00% | +32,81% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 30 | 100,00% | +28,33% | +28,33% | -2,80% | +33,68% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 29 | 41,38% | +28,03% | -5,53% | -2,74% | +33,36% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 4 | 0,00% | +33,67% | -33,67% | -1,55% | +38,08% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 79 | 48,10% | +0,03% | +0,02% | -0,75% | +1,08% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 85 | 58,82% | +0,01% | +0,56% | -0,78% | +1,01% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 85 | 58,82% | +0,01% | +0,56% | -0,78% | +1,01% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 79 | 50,63% | -0,07% | +0,12% | -0,88% | +0,92% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 47 | 40,43% | -0,05% | -0,63% | -0,92% | +0,67% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 78 | 46,15% | +0,30% | -0,01% | -0,83% | +1,66% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 84 | 59,52% | +0,14% | +0,89% | -0,95% | +1,44% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 84 | 59,52% | +0,14% | +0,89% | -0,95% | +1,44% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 78 | 52,56% | -0,17% | +0,07% | -1,27% | +1,13% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 46 | 41,30% | +0,27% | -1,32% | -0,93% | +1,22% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 78 | 41,03% | +0,57% | +0,15% | -2,49% | +3,75% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 83 | 57,83% | +0,31% | +1,25% | -2,64% | +3,49% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 83 | 57,83% | +0,31% | +1,25% | -2,64% | +3,49% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 77 | 44,16% | -0,31% | -0,19% | -2,89% | +2,83% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 45 | 31,11% | +0,54% | -2,23% | -2,66% | +3,71% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 76 | 44,74% | +1,37% | +0,15% | -3,50% | +6,21% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 81 | 54,32% | +1,05% | +1,71% | -3,73% | +5,94% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 81 | 54,32% | +1,05% | +1,71% | -3,73% | +5,94% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 75 | 48,00% | +0,26% | -1,13% | -4,12% | +5,21% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 44 | 31,82% | +1,94% | -4,85% | -3,72% | +6,77% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 75 | 48,00% | +2,08% | +0,19% | -4,08% | +8,18% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 79 | 56,96% | +1,99% | +1,70% | -4,20% | +7,98% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 79 | 56,96% | +1,99% | +1,70% | -4,20% | +7,98% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 73 | 43,84% | +1,03% | -1,35% | -4,66% | +7,02% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 44 | 27,27% | +3,07% | -6,50% | -4,35% | +8,81% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 73 | 41,10% | +2,72% | -0,13% | -4,77% | +10,13% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 76 | 53,95% | +2,68% | +1,39% | -4,75% | +9,99% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 76 | 53,95% | +2,68% | +1,39% | -4,75% | +9,99% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 70 | 45,71% | +1,40% | -1,77% | -5,28% | +8,53% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 43 | 30,23% | +3,70% | -7,04% | -4,91% | +11,04% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 70 | 54,29% | +4,55% | +2,65% | -5,49% | +13,70% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 73 | 63,01% | +4,21% | +3,15% | -5,44% | +13,34% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 73 | 63,01% | +4,21% | +3,15% | -5,44% | +13,34% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 67 | 47,76% | +2,21% | -1,49% | -6,06% | +10,78% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 43 | 39,53% | +4,51% | -5,45% | -5,57% | +13,12% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 65 | 60,00% | +8,47% | +2,51% | -5,17% | +19,56% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 68 | 57,35% | +8,79% | +4,21% | -5,19% | +19,71% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 68 | 57,35% | +8,79% | +4,21% | -5,19% | +19,71% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 62 | 56,45% | +6,83% | -1,96% | -5,84% | +16,87% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 41 | 43,90% | +6,23% | -7,20% | -5,36% | +16,47% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 70,00% | +6,74% | +1,36% | -4,20% | +19,90% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 59 | 69,49% | +11,63% | +5,25% | -5,55% | +25,55% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 62 | 70,97% | +11,91% | +7,46% | -5,52% | +26,03% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 62 | 70,97% | +11,91% | +7,46% | -5,52% | +26,03% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 56 | 58,93% | +10,47% | -2,55% | -6,31% | +23,79% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 35 | 48,57% | +9,69% | -7,71% | -5,84% | +22,14% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 88,89% | +19,48% | +12,44% | -5,48% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 46 | 47,83% | +21,61% | +4,28% | -4,57% | +38,95% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 47 | 59,57% | +22,08% | +8,66% | -4,46% | +39,37% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 47 | 59,57% | +22,08% | +8,66% | -4,46% | +39,37% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 41 | 12,20% | +19,07% | -14,29% | -5,37% | +37,20% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 31 | 3,23% | +21,52% | -22,01% | -5,10% | +38,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +24,92% | +12,69% | -3,96% | +37,45% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 32 | 37,50% | +26,82% | -3,10% | -4,35% | +44,37% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 34 | 52,94% | +27,26% | +8,06% | -4,36% | +44,55% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 34 | 52,94% | +27,26% | +8,06% | -4,36% | +44,55% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | +26,49% | +11,04% | -4,40% | +44,30% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 30 | 0,00% | +27,32% | -27,32% | -4,76% | +43,74% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 22 | 0,00% | +25,52% | -25,52% | -4,86% | +42,69% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +38,20% | +19,48% | -1,31% | +51,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 78 | 47,44% | +0,23% | +0,15% | -0,51% | +1,09% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 80 | 55,00% | +0,22% | +0,50% | -0,61% | +1,06% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 83 | 54,22% | +0,25% | +0,44% | -0,58% | +1,09% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 78 | 44,87% | +0,21% | -0,14% | -0,67% | +1,04% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 58 | 44,83% | +0,45% | -0,03% | -0,53% | +1,39% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 77 | 45,45% | +0,73% | +0,64% | -0,49% | +1,79% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 79 | 50,63% | +0,63% | +0,83% | -0,71% | +1,55% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 82 | 50,00% | +0,62% | +0,79% | -0,68% | +1,59% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 77 | 41,56% | +0,45% | -0,23% | -0,68% | +1,56% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 57 | 47,37% | +0,57% | +0,14% | -0,69% | +1,64% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 76 | 50,00% | +1,25% | +1,13% | -2,05% | +3,77% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 78 | 53,85% | +1,09% | +1,46% | -2,20% | +3,59% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 81 | 53,09% | +1,06% | +1,39% | -2,16% | +3,58% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 76 | 43,42% | +0,67% | -0,51% | -2,22% | +3,14% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 57 | 47,37% | +0,64% | +0,14% | -2,20% | +3,12% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 74 | 54,05% | +2,39% | +2,31% | -2,83% | +6,09% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 76 | 55,26% | +2,16% | +2,26% | -2,97% | +5,87% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 79 | 54,43% | +2,10% | +2,15% | -2,93% | +5,80% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 74 | 44,59% | +1,75% | -0,84% | -3,02% | +5,30% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 56 | 50,00% | +0,92% | +0,24% | -3,09% | +4,53% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 72 | 59,72% | +3,71% | +3,78% | -3,21% | +7,90% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 74 | 62,16% | +3,43% | +3,27% | -3,36% | +7,65% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 77 | 62,34% | +3,30% | +3,15% | -3,33% | +7,50% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 72 | 40,28% | +2,43% | -1,54% | -3,44% | +6,72% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 54 | 46,30% | +0,97% | +0,35% | -3,56% | +5,35% | PRIMA CALIBRAZIONE |
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
