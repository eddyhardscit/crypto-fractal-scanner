# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-13 05:33 UTC

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

Segnali totali salvati: **267**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-13 | BTC | 83.581,21 | +1 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-13 | DOGE | 0.08464 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-13 | SOL | 108,05 | +2 | +3 | +3 | 0 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-12 | BTC | 83.714,71 | -3 | -1 | -1 | 0 | -1 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-12 | DOGE | 0.08732 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-12 | SOL | 112,31 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-11 | BTC | 83.006,99 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-11 | DOGE | 0.08535 | +1 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-11 | SOL | 109,56 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-10 | BTC | 82.650,00 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-10 | DOGE | 0.08645 | -1 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-10 | SOL | 110,05 | +6 | +3 | +3 | 0 | +1 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 89 | 88 | 87 | 86 | 84 | 82 | 79 | 76 | 70 | 65 | 50 | 35 |
| SOL | 89 | 88 | 87 | 86 | 84 | 82 | 79 | 76 | 70 | 65 | 50 | 35 |
| DOGE | 89 | 88 | 87 | 86 | 84 | 82 | 79 | 76 | 70 | 65 | 50 | 35 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-15 | 60g | 2026-10-14 | domani |
| SOL | 2026-08-15 | 60g | 2026-10-14 | domani |
| DOGE | 2026-08-15 | 60g | 2026-10-14 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 79 | 53,16% | +0,30% | +0,29% | UTILE |
| BTC | 2g | 78 | 51,28% | +0,56% | +0,50% | UTILE |
| BTC | 3g | 78 | 46,15% | +0,69% | +0,60% | UTILE |
| BTC | 5g | 78 | 43,59% | +1,42% | +1,25% | UTILE |
| BTC | 7g | 77 | 51,95% | +2,13% | +1,99% | UTILE |
| BTC | 10g | 74 | 58,11% | +3,15% | +3,03% | UTILE |
| BTC | 14g | 71 | 61,97% | +4,73% | +4,68% | UTILE |
| BTC | 21g | 67 | 73,13% | +8,26% | +8,16% | UTILE |
| BTC | 30g | 62 | 95,16% | +12,31% | +11,61% | UTILE |
| BTC | 45g | 47 | 93,62% | +21,65% | +18,84% | PRIMA CALIBRAZIONE |
| BTC | 60g | 33 | 90,91% | +28,02% | +23,47% | PRIMA CALIBRAZIONE |
| SOL | 1g | 80 | 47,50% | +0,21% | +0,13% | UTILE |
| SOL | 2g | 79 | 45,57% | +0,72% | +0,63% | UTILE |
| SOL | 3g | 78 | 50,00% | +1,21% | +1,10% | UTILE |
| SOL | 5g | 76 | 52,63% | +2,17% | +2,09% | UTILE |
| SOL | 7g | 74 | 58,11% | +3,39% | +3,46% | UTILE |
| SOL | 10g | 71 | 60,56% | +5,38% | +5,49% | UTILE |
| SOL | 14g | 68 | 69,12% | +8,15% | +8,69% | UTILE |
| SOL | 21g | 62 | 82,26% | +14,88% | +14,31% | UTILE |
| SOL | 30g | 58 | 82,76% | +20,18% | +16,77% | PRIMA CALIBRAZIONE |
| SOL | 45g | 43 | 74,42% | +37,39% | +19,49% | PRIMA CALIBRAZIONE |
| SOL | 60g | 28 | 60,71% | +47,20% | +15,90% | FEEDBACK RAPIDO |
| DOGE | 1g | 80 | 48,75% | +0,06% | +0,05% | UTILE |
| DOGE | 2g | 80 | 45,00% | +0,29% | -0,03% | UTILE |
| DOGE | 3g | 79 | 41,77% | +0,53% | +0,17% | UTILE |
| DOGE | 5g | 78 | 46,15% | +1,25% | +0,24% | UTILE |
| DOGE | 7g | 76 | 48,68% | +1,91% | +0,33% | UTILE |
| DOGE | 10g | 75 | 41,33% | +2,40% | -0,13% | UTILE |
| DOGE | 14g | 72 | 52,78% | +4,21% | +2,36% | UTILE |
| DOGE | 21g | 66 | 59,09% | +8,13% | +2,26% | UTILE |
| DOGE | 30g | 61 | 68,85% | +11,30% | +5,02% | UTILE |
| DOGE | 45g | 47 | 46,81% | +21,14% | +4,17% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 33 | 39,39% | +26,67% | -2,34% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 79 | 53,16% | +0,30% | +0,29% | -0,28% | +0,82% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 86 | 50,00% | +0,23% | +0,29% | -0,30% | +0,74% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 86 | 50,00% | +0,23% | +0,29% | -0,30% | +0,74% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 81 | 45,68% | +0,26% | +0,01% | -0,24% | +0,77% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 35 | 42,86% | +0,53% | -0,02% | -0,31% | +1,07% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 78 | 51,28% | +0,56% | +0,50% | -0,22% | +1,25% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 85 | 51,76% | +0,53% | +0,61% | -0,21% | +1,21% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 85 | 51,76% | +0,53% | +0,61% | -0,21% | +1,21% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 80 | 45,00% | +0,52% | +0,00% | -0,12% | +1,20% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,89% | -0,12% | -0,02% | +1,61% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 78 | 46,15% | +0,69% | +0,60% | -1,25% | +2,46% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 84 | 50,00% | +0,85% | +0,86% | -1,28% | +2,53% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 84 | 50,00% | +0,85% | +0,86% | -1,28% | +2,53% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 79 | 37,97% | +0,87% | -0,20% | -1,21% | +2,56% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,44% | -0,66% | -1,08% | +3,10% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -0,50% | -0,50% | -1,88% | +1,29% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 78 | 43,59% | +1,42% | +1,25% | -1,91% | +3,84% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 82 | 47,56% | +1,62% | +1,63% | -1,90% | +3,98% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 82 | 47,56% | +1,62% | +1,63% | -1,90% | +3,98% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 77 | 41,56% | +1,49% | -0,71% | -1,86% | +3,92% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 34 | 35,29% | +3,06% | -2,33% | -1,68% | +5,50% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 77 | 51,95% | +2,13% | +1,99% | -2,27% | +4,96% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 80 | 56,25% | +2,39% | +2,38% | -2,21% | +5,15% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 80 | 56,25% | +2,39% | +2,38% | -2,21% | +5,15% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 75 | 44,00% | +2,35% | -1,05% | -2,18% | +5,12% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 34 | 32,35% | +4,23% | -3,81% | -2,10% | +7,38% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 74 | 58,11% | +3,15% | +3,03% | -2,49% | +6,23% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 78 | 65,38% | +3,28% | +3,29% | -2,44% | +6,35% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 78 | 65,38% | +3,28% | +3,29% | -2,44% | +6,35% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 72 | 47,22% | +3,32% | -0,37% | -2,40% | +6,45% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 31 | 38,71% | +5,05% | -4,25% | -1,98% | +8,63% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -1,47% | -1,47% | -4,23% | +1,69% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 71 | 61,97% | +4,73% | +4,68% | -2,65% | +8,40% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 76 | 60,53% | +4,65% | +4,69% | -2,68% | +8,37% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 76 | 60,53% | +4,65% | +4,69% | -2,68% | +8,37% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 69 | 56,52% | +4,90% | +1,39% | -2,63% | +8,66% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 29 | 24,14% | +5,09% | -4,15% | -1,91% | +9,57% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | -0,11% | -0,11% | -4,30% | +2,85% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 67 | 73,13% | +8,26% | +8,16% | -2,84% | +12,12% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 70 | 77,14% | +8,20% | +8,20% | -2,82% | +12,08% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 70 | 77,14% | +8,20% | +8,20% | -2,82% | +12,08% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 63 | 57,14% | +8,67% | +1,44% | -2,78% | +12,56% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 28 | 46,43% | +9,04% | -4,92% | -2,22% | +12,89% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +1,01% | +1,01% | -4,69% | +5,62% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 62 | 95,16% | +12,31% | +11,61% | -2,99% | +16,44% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 65 | 92,31% | +12,28% | +12,28% | -2,97% | +16,52% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 65 | 92,31% | +12,28% | +12,28% | -2,97% | +16,52% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 60 | 65,00% | +12,24% | +1,14% | -2,84% | +16,66% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,37% | -2,02% | -2,62% | +17,60% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 47 | 93,62% | +21,65% | +18,84% | -2,49% | +26,39% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 50 | 100,00% | +21,97% | +21,97% | -2,49% | +26,59% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 50 | 100,00% | +21,97% | +21,97% | -2,49% | +26,59% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 45 | 51,11% | +22,08% | -2,32% | -2,27% | +26,73% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 18 | 55,56% | +17,05% | -7,07% | -1,98% | +22,74% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 33 | 90,91% | +28,02% | +23,47% | -2,87% | +33,13% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 35 | 100,00% | +27,82% | +27,82% | -2,92% | +32,99% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 35 | 100,00% | +27,82% | +27,82% | -2,92% | +32,99% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 31 | 100,00% | +28,49% | +28,49% | -2,71% | +33,86% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 30 | 40,00% | +28,20% | -6,45% | -2,66% | +33,55% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 5 | 0,00% | +33,58% | -33,58% | -1,27% | +38,31% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 80 | 48,75% | +0,06% | +0,05% | -0,73% | +1,10% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 87 | 58,62% | +0,00% | +0,54% | -0,83% | +0,99% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 87 | 58,62% | +0,00% | +0,54% | -0,83% | +0,99% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 81 | 50,62% | -0,08% | +0,13% | -0,94% | +0,90% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 49 | 40,82% | -0,06% | -0,59% | -1,02% | +0,65% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 80 | 45,00% | +0,29% | -0,03% | -0,88% | +1,63% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 86 | 59,30% | +0,13% | +0,88% | -0,99% | +1,42% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 86 | 59,30% | +0,13% | +0,88% | -0,99% | +1,42% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 80 | 52,50% | -0,16% | +0,06% | -1,30% | +1,12% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 48 | 41,67% | +0,26% | -1,27% | -1,01% | +1,19% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +2,89% | +2,65% | +1,08% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 79 | 41,77% | +0,53% | +0,17% | -2,54% | +3,72% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 85 | 57,65% | +0,31% | +1,23% | -2,66% | +3,46% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 85 | 57,65% | +0,31% | +1,23% | -2,66% | +3,46% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 79 | 44,30% | -0,30% | -0,18% | -2,91% | +2,81% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 47 | 31,91% | +0,53% | -2,14% | -2,69% | +3,64% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +2,81% | +2,62% | -1,35% | +6,66% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 78 | 46,15% | +1,25% | +0,24% | -3,64% | +6,04% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 83 | 55,42% | +0,94% | +1,75% | -3,86% | +5,78% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 83 | 55,42% | +0,94% | +1,75% | -3,86% | +5,78% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 77 | 49,35% | +0,16% | -1,01% | -4,25% | +5,06% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 45 | 33,33% | +1,82% | -4,66% | -3,81% | +6,61% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 36,36% | +2,17% | +2,02% | -2,50% | +9,16% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 76 | 48,68% | +1,91% | +0,33% | -4,22% | +8,05% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 81 | 58,02% | +1,71% | +1,89% | -4,46% | +7,78% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 81 | 58,02% | +1,71% | +1,89% | -4,46% | +7,78% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 75 | 42,67% | +0,75% | -1,56% | -4,92% | +6,83% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 44 | 27,27% | +3,07% | -6,50% | -4,35% | +8,81% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 75 | 41,33% | +2,40% | -0,13% | -5,03% | +9,93% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 78 | 55,13% | +2,37% | +1,59% | -5,01% | +9,80% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 78 | 55,13% | +2,37% | +1,59% | -5,01% | +9,80% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 72 | 44,44% | +1,10% | -1,99% | -5,54% | +8,37% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 44 | 29,55% | +3,40% | -7,10% | -5,16% | +10,81% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 72 | 52,78% | +4,21% | +2,36% | -5,70% | +13,45% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 75 | 64,00% | +3,90% | +3,27% | -5,64% | +13,11% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 75 | 64,00% | +3,90% | +3,27% | -5,64% | +13,11% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 69 | 46,38% | +1,92% | -1,67% | -6,26% | +10,61% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 43 | 39,53% | +4,51% | -5,45% | -5,57% | +13,12% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 66 | 59,09% | +8,13% | +2,26% | -5,37% | +19,35% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 69 | 57,97% | +8,46% | +4,35% | -5,37% | +19,50% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 69 | 57,97% | +8,46% | +4,35% | -5,37% | +19,50% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 63 | 55,56% | +6,50% | -2,16% | -6,03% | +16,69% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 41 | 43,90% | +6,23% | -7,20% | -5,36% | +16,47% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +4,84% | -0,04% | -5,47% | +18,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 61 | 68,85% | +11,30% | +5,02% | -5,61% | +25,52% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 64 | 70,31% | +11,59% | +7,17% | -5,58% | +25,98% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 64 | 70,31% | +11,59% | +7,17% | -5,58% | +25,98% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 58 | 58,62% | +10,16% | -2,52% | -6,34% | +23,82% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 37 | 48,65% | +9,25% | -7,39% | -5,92% | +22,26% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 88,89% | +19,48% | +12,44% | -5,48% | +30,17% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 47 | 46,81% | +21,14% | +4,17% | -4,64% | +38,63% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 49 | 61,22% | +21,16% | +8,33% | -4,65% | +38,66% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 49 | 61,22% | +21,16% | +8,33% | -4,65% | +38,66% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 43 | 11,63% | +18,16% | -13,64% | -5,55% | +36,49% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 31 | 3,23% | +21,52% | -22,01% | -5,10% | +38,53% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +21,73% | +11,03% | -4,45% | +35,73% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 33 | 39,39% | +26,67% | -2,34% | -4,23% | +44,59% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 35 | 54,29% | +27,11% | +8,46% | -4,24% | +44,76% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 35 | 54,29% | +27,11% | +8,46% | -4,24% | +44,76% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 33 | 57,58% | +26,35% | +11,37% | -4,27% | +44,53% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 30 | 0,00% | +27,32% | -27,32% | -4,76% | +43,74% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 23 | 0,00% | +25,36% | -25,36% | -4,66% | +43,08% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +38,20% | +19,48% | -1,31% | +51,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 80 | 47,50% | +0,21% | +0,13% | -0,59% | +1,06% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 82 | 54,88% | +0,20% | +0,47% | -0,68% | +1,04% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 85 | 54,12% | +0,23% | +0,42% | -0,65% | +1,06% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 80 | 45,00% | +0,19% | -0,12% | -0,74% | +1,01% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 58 | 44,83% | +0,45% | -0,03% | -0,53% | +1,39% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 79 | 45,57% | +0,72% | +0,63% | -0,54% | +1,77% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 81 | 50,62% | +0,62% | +0,82% | -0,76% | +1,53% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 84 | 50,00% | +0,61% | +0,78% | -0,73% | +1,58% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 79 | 43,04% | +0,44% | -0,18% | -0,73% | +1,54% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 58 | 48,28% | +0,59% | +0,18% | -0,66% | +1,66% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 78 | 50,00% | +1,21% | +1,10% | -2,11% | +3,73% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 80 | 53,75% | +1,06% | +1,42% | -2,25% | +3,56% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 83 | 53,01% | +1,03% | +1,36% | -2,21% | +3,55% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 78 | 42,31% | +0,65% | -0,54% | -2,27% | +3,12% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 58 | 46,55% | +0,60% | +0,10% | -2,28% | +3,11% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 76 | 52,63% | +2,17% | +2,09% | -3,04% | +5,88% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 78 | 56,41% | +1,95% | +2,36% | -3,17% | +5,67% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 81 | 55,56% | +1,90% | +2,24% | -3,13% | +5,60% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 76 | 43,42% | +1,55% | -0,97% | -3,23% | +5,11% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 57 | 49,12% | +0,81% | +0,14% | -3,23% | +4,42% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 74 | 58,11% | +3,39% | +3,46% | -3,48% | +7,72% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 76 | 63,16% | +3,13% | +3,40% | -3,62% | +7,47% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 79 | 63,29% | +3,00% | +3,28% | -3,58% | +7,34% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 74 | 39,19% | +2,14% | -1,72% | -3,71% | +6,57% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 56 | 44,64% | +0,64% | +0,04% | -3,90% | +5,19% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 71 | 60,56% | +5,38% | +5,49% | -3,72% | +10,00% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 73 | 68,49% | +5,19% | +5,52% | -3,88% | +9,61% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 76 | 67,11% | +4,98% | +5,31% | -3,86% | +9,38% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 71 | 43,66% | +3,53% | -1,81% | -4,05% | +8,22% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 53 | 47,17% | +1,08% | +0,35% | -4,28% | +6,18% | PRIMA CALIBRAZIONE |

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
