# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-12 05:33 UTC

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

Segnali totali salvati: **264**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-12 | BTC | 83.714,71 | -3 | -1 | -1 | 0 | -1 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-12 | DOGE | 0.08732 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-12 | SOL | 112,31 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-11 | BTC | 83.006,99 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-11 | DOGE | 0.08535 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-11 | SOL | 109,56 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-10 | BTC | 82.650,00 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-10 | DOGE | 0.08645 | -1 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-10 | SOL | 110,05 | +6 | +3 | +3 | 0 | +1 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-09 | BTC | 82.441,21 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-09 | DOGE | 0.08534 | 0 | +2 | +2 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-09 | SOL | 110,52 | +1 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 88 | 87 | 86 | 85 | 83 | 81 | 78 | 75 | 69 | 64 | 49 | 34 |
| SOL | 88 | 87 | 86 | 85 | 83 | 81 | 78 | 75 | 69 | 64 | 49 | 34 |
| DOGE | 88 | 87 | 86 | 85 | 83 | 81 | 78 | 75 | 69 | 64 | 49 | 34 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-14 | 60g | 2026-10-13 | domani |
| SOL | 2026-08-14 | 60g | 2026-10-13 | domani |
| DOGE | 2026-08-14 | 60g | 2026-10-13 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 78 | 52,56% | +0,31% | +0,29% | UTILE |
| BTC | 2g | 78 | 51,28% | +0,56% | +0,50% | UTILE |
| BTC | 3g | 78 | 46,15% | +0,69% | +0,60% | UTILE |
| BTC | 5g | 77 | 42,86% | +1,42% | +1,26% | UTILE |
| BTC | 7g | 76 | 52,63% | +2,19% | +2,05% | UTILE |
| BTC | 10g | 73 | 58,90% | +3,21% | +3,09% | UTILE |
| BTC | 14g | 70 | 61,43% | +4,79% | +4,74% | UTILE |
| BTC | 21g | 66 | 74,24% | +8,41% | +8,31% | UTILE |
| BTC | 30g | 61 | 95,08% | +12,37% | +11,67% | UTILE |
| BTC | 45g | 46 | 93,48% | +21,96% | +19,08% | PRIMA CALIBRAZIONE |
| BTC | 60g | 32 | 90,62% | +27,86% | +23,17% | PRIMA CALIBRAZIONE |
| SOL | 1g | 79 | 48,10% | +0,26% | +0,18% | UTILE |
| SOL | 2g | 78 | 46,15% | +0,75% | +0,66% | UTILE |
| SOL | 3g | 77 | 50,65% | +1,25% | +1,14% | UTILE |
| SOL | 5g | 75 | 53,33% | +2,28% | +2,21% | UTILE |
| SOL | 7g | 73 | 58,90% | +3,57% | +3,64% | UTILE |
| SOL | 10g | 70 | 61,43% | +5,60% | +5,71% | UTILE |
| SOL | 14g | 67 | 70,15% | +8,39% | +8,94% | UTILE |
| SOL | 21g | 61 | 83,61% | +15,23% | +14,65% | UTILE |
| SOL | 30g | 57 | 82,46% | +20,43% | +16,96% | PRIMA CALIBRAZIONE |
| SOL | 45g | 42 | 73,81% | +38,18% | +19,86% | PRIMA CALIBRAZIONE |
| SOL | 60g | 27 | 59,26% | +47,35% | +14,89% | FEEDBACK RAPIDO |
| DOGE | 1g | 80 | 48,75% | +0,06% | +0,05% | UTILE |
| DOGE | 2g | 79 | 45,57% | +0,31% | -0,02% | UTILE |
| DOGE | 3g | 78 | 41,03% | +0,57% | +0,15% | UTILE |
| DOGE | 5g | 77 | 45,45% | +1,31% | +0,19% | UTILE |
| DOGE | 7g | 75 | 48,00% | +2,08% | +0,19% | UTILE |
| DOGE | 10g | 74 | 40,54% | +2,56% | -0,26% | UTILE |
| DOGE | 14g | 71 | 53,52% | +4,40% | +2,53% | UTILE |
| DOGE | 21g | 65 | 60,00% | +8,47% | +2,51% | UTILE |
| DOGE | 30g | 60 | 68,33% | +11,50% | +5,10% | UTILE |
| DOGE | 45g | 46 | 47,83% | +21,61% | +4,28% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 32 | 37,50% | +26,82% | -3,10% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 78 | 52,56% | +0,31% | +0,29% | -0,24% | +0,83% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 85 | 49,41% | +0,24% | +0,29% | -0,27% | +0,75% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 85 | 49,41% | +0,24% | +0,29% | -0,27% | +0,75% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 80 | 45,00% | +0,26% | +0,00% | -0,21% | +0,78% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,55% | -0,03% | -0,23% | +1,11% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 78 | 51,28% | +0,56% | +0,50% | -0,22% | +1,25% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 84 | 52,38% | +0,53% | +0,62% | -0,19% | +1,21% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 84 | 52,38% | +0,53% | +0,62% | -0,19% | +1,21% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 79 | 44,30% | +0,52% | -0,00% | -0,10% | +1,20% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,89% | -0,12% | -0,02% | +1,61% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,28% | -0,28% | -1,06% | +0,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 78 | 46,15% | +0,69% | +0,60% | -1,25% | +2,46% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 83 | 50,60% | +0,85% | +0,89% | -1,28% | +2,54% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 83 | 50,60% | +0,85% | +0,89% | -1,28% | +2,54% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 78 | 37,18% | +0,87% | -0,21% | -1,20% | +2,57% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,44% | -0,66% | -1,08% | +3,10% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,50% | -0,50% | -1,88% | +1,29% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 77 | 42,86% | +1,42% | +1,26% | -1,91% | +3,87% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 81 | 48,15% | +1,63% | +1,66% | -1,90% | +4,01% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 81 | 48,15% | +1,63% | +1,66% | -1,90% | +4,01% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 76 | 40,79% | +1,49% | -0,73% | -1,86% | +3,96% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 34 | 35,29% | +3,06% | -2,33% | -1,68% | +5,50% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 76 | 52,63% | +2,19% | +2,05% | -2,22% | +5,03% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 79 | 55,70% | +2,45% | +2,38% | -2,16% | +5,22% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 79 | 55,70% | +2,45% | +2,38% | -2,16% | +5,22% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 74 | 44,59% | +2,42% | -1,03% | -2,13% | +5,19% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 33 | 33,33% | +4,44% | -3,85% | -1,98% | +7,61% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 73 | 58,90% | +3,21% | +3,09% | -2,45% | +6,28% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 77 | 64,94% | +3,34% | +3,31% | -2,40% | +6,40% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 77 | 64,94% | +3,34% | +3,31% | -2,40% | +6,40% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 71 | 47,89% | +3,39% | -0,36% | -2,37% | +6,50% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 30 | 40,00% | +5,26% | -4,35% | -1,88% | +8,83% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -1,47% | -1,47% | -4,23% | +1,69% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 70 | 61,43% | +4,79% | +4,74% | -2,64% | +8,46% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 75 | 61,33% | +4,70% | +4,76% | -2,67% | +8,41% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 75 | 61,33% | +4,70% | +4,76% | -2,67% | +8,41% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 68 | 55,88% | +4,97% | +1,40% | -2,62% | +8,72% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 29 | 24,14% | +5,09% | -4,15% | -1,91% | +9,57% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,11% | -0,11% | -4,30% | +2,85% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 66 | 74,24% | +8,41% | +8,31% | -2,80% | +12,27% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 69 | 78,26% | +8,34% | +8,34% | -2,78% | +12,22% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 69 | 78,26% | +8,34% | +8,34% | -2,78% | +12,22% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 62 | 58,06% | +8,84% | +1,49% | -2,74% | +12,73% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 28 | 46,43% | +9,04% | -4,92% | -2,22% | +12,89% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 61 | 95,08% | +12,37% | +11,67% | -2,99% | +16,49% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 64 | 92,19% | +12,34% | +12,34% | -2,97% | +16,57% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 64 | 92,19% | +12,34% | +12,34% | -2,97% | +16,57% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 59 | 64,41% | +12,31% | +1,02% | -2,84% | +16,72% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,37% | -2,02% | -2,62% | +17,60% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 46 | 93,48% | +21,96% | +19,08% | -2,47% | +26,69% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 49 | 100,00% | +22,26% | +22,26% | -2,47% | +26,88% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 49 | 100,00% | +22,26% | +22,26% | -2,47% | +26,88% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 44 | 50,00% | +22,41% | -2,55% | -2,24% | +27,05% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 17 | 52,94% | +17,60% | -7,93% | -1,89% | +23,34% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 32 | 90,62% | +27,86% | +23,17% | -2,96% | +32,94% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 34 | 100,00% | +27,66% | +27,66% | -3,00% | +32,81% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 34 | 100,00% | +27,66% | +27,66% | -3,00% | +32,81% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 30 | 100,00% | +28,33% | +28,33% | -2,80% | +33,68% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 29 | 41,38% | +28,03% | -5,53% | -2,74% | +33,36% | FEEDBACK RAPIDO |
| BTC | 60g | Classic technical | CALIBRABILE | 4 | 0,00% | +33,67% | -33,67% | -1,55% | +38,08% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 80 | 48,75% | +0,06% | +0,05% | -0,73% | +1,10% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 86 | 59,30% | +0,04% | +0,58% | -0,75% | +1,03% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 86 | 59,30% | +0,04% | +0,58% | -0,75% | +1,03% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 80 | 50,00% | -0,04% | +0,09% | -0,86% | +0,94% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 48 | 39,58% | +0,00% | -0,67% | -0,88% | +0,72% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 79 | 45,57% | +0,31% | -0,02% | -0,82% | +1,66% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 85 | 60,00% | +0,15% | +0,90% | -0,94% | +1,44% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 85 | 60,00% | +0,15% | +0,90% | -0,94% | +1,44% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 79 | 51,90% | -0,15% | +0,05% | -1,25% | +1,14% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 47 | 40,43% | +0,29% | -1,31% | -0,91% | +1,23% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 78 | 41,03% | +0,57% | +0,15% | -2,49% | +3,75% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 84 | 58,33% | +0,34% | +1,27% | -2,61% | +3,48% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 84 | 58,33% | +0,34% | +1,27% | -2,61% | +3,48% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 78 | 43,59% | -0,27% | -0,21% | -2,86% | +2,83% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 46 | 30,43% | +0,58% | -2,23% | -2,61% | +3,69% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 77 | 45,45% | +1,31% | +0,19% | -3,58% | +6,12% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 82 | 54,88% | +0,99% | +1,72% | -3,81% | +5,86% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 82 | 54,88% | +0,99% | +1,72% | -3,81% | +5,86% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 76 | 48,68% | +0,21% | -1,07% | -4,20% | +5,13% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 44 | 31,82% | +1,94% | -4,85% | -3,72% | +6,77% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 75 | 48,00% | +2,08% | +0,19% | -4,08% | +8,18% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 80 | 57,50% | +1,87% | +1,78% | -4,33% | +7,90% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 80 | 57,50% | +1,87% | +1,78% | -4,33% | +7,90% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 74 | 43,24% | +0,91% | -1,44% | -4,79% | +6,94% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 44 | 27,27% | +3,07% | -6,50% | -4,35% | +8,81% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 74 | 40,54% | +2,56% | -0,26% | -4,92% | +10,00% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 77 | 54,55% | +2,52% | +1,49% | -4,90% | +9,87% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 77 | 54,55% | +2,52% | +1,49% | -4,90% | +9,87% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 71 | 45,07% | +1,24% | -1,88% | -5,43% | +8,42% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 44 | 29,55% | +3,40% | -7,10% | -5,16% | +10,81% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 71 | 53,52% | +4,40% | +2,53% | -5,59% | +13,57% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 74 | 63,51% | +4,08% | +3,19% | -5,54% | +13,23% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 74 | 63,51% | +4,08% | +3,19% | -5,54% | +13,23% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 68 | 47,06% | +2,09% | -1,56% | -6,15% | +10,70% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 43 | 39,53% | +4,51% | -5,45% | -5,57% | +13,12% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 65 | 60,00% | +8,47% | +2,51% | -5,17% | +19,56% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 68 | 57,35% | +8,79% | +4,21% | -5,19% | +19,71% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 68 | 57,35% | +8,79% | +4,21% | -5,19% | +19,71% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 62 | 56,45% | +6,83% | -1,96% | -5,84% | +16,87% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 41 | 43,90% | +6,23% | -7,20% | -5,36% | +16,47% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 70,00% | +6,74% | +1,36% | -4,20% | +19,90% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 60 | 68,33% | +11,50% | +5,10% | -5,57% | +25,54% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 63 | 69,84% | +11,78% | +7,28% | -5,55% | +26,01% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 63 | 69,84% | +11,78% | +7,28% | -5,55% | +26,01% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 57 | 57,89% | +10,35% | -2,57% | -6,32% | +23,81% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 36 | 47,22% | +9,51% | -7,60% | -5,87% | +22,21% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 88,89% | +19,48% | +12,44% | -5,48% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 46 | 47,83% | +21,61% | +4,28% | -4,57% | +38,95% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 48 | 60,42% | +21,62% | +8,49% | -4,59% | +38,97% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 48 | 60,42% | +21,62% | +8,49% | -4,59% | +38,97% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 42 | 11,90% | +18,61% | -13,95% | -5,49% | +36,80% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 31 | 3,23% | +21,52% | -22,01% | -5,10% | +38,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +24,92% | +12,69% | -3,96% | +37,45% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 32 | 37,50% | +26,82% | -3,10% | -4,35% | +44,37% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 34 | 52,94% | +27,26% | +8,06% | -4,36% | +44,55% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 34 | 52,94% | +27,26% | +8,06% | -4,36% | +44,55% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | +26,49% | +11,04% | -4,40% | +44,30% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 30 | 0,00% | +27,32% | -27,32% | -4,76% | +43,74% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 22 | 0,00% | +25,52% | -25,52% | -4,86% | +42,69% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +38,20% | +19,48% | -1,31% | +51,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 79 | 48,10% | +0,26% | +0,18% | -0,49% | +1,12% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 81 | 55,56% | +0,24% | +0,53% | -0,59% | +1,09% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 84 | 54,76% | +0,27% | +0,47% | -0,55% | +1,12% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 79 | 44,30% | +0,24% | -0,17% | -0,65% | +1,06% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 58 | 44,83% | +0,45% | -0,03% | -0,53% | +1,39% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 78 | 46,15% | +0,75% | +0,66% | -0,47% | +1,80% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 80 | 51,25% | +0,65% | +0,84% | -0,69% | +1,56% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 83 | 50,60% | +0,64% | +0,80% | -0,67% | +1,61% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 78 | 42,31% | +0,47% | -0,20% | -0,66% | +1,58% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 58 | 48,28% | +0,59% | +0,18% | -0,66% | +1,66% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 77 | 50,65% | +1,25% | +1,14% | -2,05% | +3,75% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 79 | 54,43% | +1,09% | +1,46% | -2,19% | +3,57% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 82 | 53,66% | +1,06% | +1,40% | -2,15% | +3,57% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 77 | 42,86% | +0,68% | -0,52% | -2,21% | +3,13% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 57 | 47,37% | +0,64% | +0,14% | -2,20% | +3,12% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 75 | 53,33% | +2,28% | +2,21% | -2,93% | +5,99% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 77 | 55,84% | +2,06% | +2,30% | -3,07% | +5,77% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 80 | 55,00% | +2,01% | +2,19% | -3,03% | +5,70% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 75 | 44,00% | +1,66% | -0,90% | -3,12% | +5,21% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 57 | 49,12% | +0,81% | +0,14% | -3,23% | +4,42% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 73 | 58,90% | +3,57% | +3,64% | -3,33% | +7,81% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 75 | 62,67% | +3,30% | +3,31% | -3,47% | +7,57% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 78 | 62,82% | +3,17% | +3,19% | -3,44% | +7,43% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 73 | 39,73% | +2,31% | -1,61% | -3,56% | +6,65% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 55 | 45,45% | +0,83% | +0,23% | -3,71% | +5,27% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 70 | 61,43% | +5,60% | +5,71% | -3,57% | +10,11% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 72 | 68,06% | +5,40% | +5,46% | -3,74% | +9,71% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 75 | 66,67% | +5,17% | +5,25% | -3,72% | +9,48% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 70 | 44,29% | +3,72% | -1,70% | -3,90% | +8,31% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 52 | 48,08% | +1,29% | +0,54% | -4,09% | +6,26% | PRIMA CALIBRAZIONE |

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
