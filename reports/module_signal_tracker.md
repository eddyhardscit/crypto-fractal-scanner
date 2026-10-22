# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-22 05:34 UTC

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

Segnali totali salvati: **291**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-22 | BTC | 82.752,49 | +2 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-22 | DOGE | 0.07992 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-22 | SOL | 105,09 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-21 | BTC | 82.805,01 | 0 | +1 | +1 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-21 | DOGE | 0.08166 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-21 | SOL | 105,96 | +3 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-20 | BTC | 81.867,63 | +2 | +1 | +1 | 0 | +1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-20 | DOGE | 0.07939 | -1 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-20 | SOL | 104,68 | +3 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-19 | BTC | 82.648,77 | -1 | +1 | +1 | 0 | -1 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-19 | DOGE | 0.07945 | -1 | +3 | +3 | 0 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-19 | SOL | 105,63 | -2 | +1 | +1 | 0 | -2 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 97 | 96 | 95 | 94 | 92 | 91 | 88 | 84 | 77 | 70 | 59 | 44 |
| SOL | 97 | 96 | 95 | 94 | 92 | 91 | 88 | 84 | 77 | 70 | 59 | 44 |
| DOGE | 97 | 96 | 95 | 94 | 92 | 91 | 88 | 84 | 77 | 70 | 59 | 44 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-24 | 60g | 2026-10-23 | domani |
| SOL | 2026-08-24 | 60g | 2026-10-23 | domani |
| DOGE | 2026-08-24 | 60g | 2026-10-23 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 85 | 52,94% | +0,31% | +0,29% | UTILE |
| BTC | 2g | 85 | 50,59% | +0,50% | +0,43% | UTILE |
| BTC | 3g | 84 | 46,43% | +0,62% | +0,59% | UTILE |
| BTC | 5g | 82 | 43,90% | +1,31% | +1,19% | UTILE |
| BTC | 7g | 81 | 50,62% | +1,98% | +1,82% | UTILE |
| BTC | 10g | 79 | 55,70% | +2,78% | +2,69% | UTILE |
| BTC | 14g | 78 | 57,69% | +4,05% | +4,00% | UTILE |
| BTC | 21g | 72 | 68,06% | +7,56% | +7,47% | UTILE |
| BTC | 30g | 67 | 94,03% | +11,76% | +11,11% | UTILE |
| BTC | 45g | 56 | 94,64% | +18,84% | +16,48% | PRIMA CALIBRAZIONE |
| BTC | 60g | 41 | 92,68% | +26,48% | +22,82% | PRIMA CALIBRAZIONE |
| SOL | 1g | 87 | 47,13% | +0,19% | +0,09% | UTILE |
| SOL | 2g | 86 | 44,19% | +0,57% | +0,45% | UTILE |
| SOL | 3g | 85 | 48,24% | +0,95% | +0,80% | UTILE |
| SOL | 5g | 83 | 49,40% | +1,68% | +1,62% | UTILE |
| SOL | 7g | 83 | 53,01% | +2,48% | +2,54% | UTILE |
| SOL | 10g | 80 | 53,75% | +3,77% | +3,87% | UTILE |
| SOL | 14g | 76 | 61,84% | +6,03% | +6,51% | UTILE |
| SOL | 21g | 69 | 73,91% | +12,14% | +11,63% | UTILE |
| SOL | 30g | 62 | 82,26% | +19,00% | +15,81% | UTILE |
| SOL | 45g | 52 | 75,00% | +31,17% | +16,37% | PRIMA CALIBRAZIONE |
| SOL | 60g | 37 | 70,27% | +42,66% | +18,98% | PRIMA CALIBRAZIONE |
| DOGE | 1g | 87 | 48,28% | +0,02% | -0,06% | UTILE |
| DOGE | 2g | 87 | 43,68% | +0,16% | -0,12% | UTILE |
| DOGE | 3g | 86 | 40,70% | +0,37% | +0,04% | UTILE |
| DOGE | 5g | 84 | 46,43% | +0,86% | +0,13% | UTILE |
| DOGE | 7g | 83 | 48,19% | +1,26% | +0,38% | UTILE |
| DOGE | 10g | 80 | 43,75% | +1,65% | +0,37% | UTILE |
| DOGE | 14g | 78 | 53,85% | +2,93% | +2,51% | UTILE |
| DOGE | 21g | 73 | 53,42% | +5,80% | +0,49% | UTILE |
| DOGE | 30g | 66 | 66,67% | +10,12% | +4,39% | UTILE |
| DOGE | 45g | 55 | 49,09% | +17,21% | +3,62% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 42 | 45,24% | +22,39% | -0,40% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 85 | 52,94% | +0,31% | +0,29% | -0,27% | +0,81% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 94 | 48,94% | +0,20% | +0,26% | -0,32% | +0,71% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 94 | 48,94% | +0,20% | +0,26% | -0,32% | +0,71% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 89 | 49,44% | +0,22% | +0,07% | -0,27% | +0,75% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,55% | -0,06% | -0,27% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 85 | 50,59% | +0,50% | +0,43% | -0,26% | +1,20% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 93 | 52,69% | +0,45% | +0,53% | -0,27% | +1,13% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 93 | 52,69% | +0,45% | +0,53% | -0,27% | +1,13% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 88 | 47,73% | +0,44% | +0,07% | -0,20% | +1,12% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,85% | -0,13% | -0,05% | +1,59% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 84 | 46,43% | +0,62% | +0,59% | -1,28% | +2,38% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 92 | 51,09% | +0,74% | +0,81% | -1,35% | +2,41% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 92 | 51,09% | +0,74% | +0,81% | -1,35% | +2,41% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 87 | 40,23% | +0,75% | -0,09% | -1,29% | +2,42% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 36 | 36,11% | +1,29% | -0,55% | -1,13% | +3,01% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 82 | 43,90% | +1,31% | +1,19% | -1,96% | +3,71% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 90 | 48,89% | +1,41% | +1,52% | -1,98% | +3,73% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 90 | 48,89% | +1,41% | +1,52% | -1,98% | +3,73% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 85 | 42,35% | +1,28% | -0,62% | -1,94% | +3,66% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 36 | 36,11% | +2,85% | -2,16% | -1,73% | +5,27% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 81 | 50,62% | +1,98% | +1,82% | -2,31% | +4,80% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 89 | 58,43% | +2,05% | +2,22% | -2,34% | +4,76% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 89 | 58,43% | +2,05% | +2,22% | -2,34% | +4,76% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 84 | 42,86% | +2,00% | -0,99% | -2,32% | +4,71% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 36 | 33,33% | +4,03% | -3,63% | -2,13% | +7,10% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 79 | 55,70% | +2,78% | +2,69% | -2,66% | +5,91% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 86 | 67,44% | +2,78% | +3,17% | -2,64% | +5,87% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 86 | 67,44% | +2,78% | +3,17% | -2,64% | +5,87% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 81 | 44,44% | +2,73% | -0,52% | -2,66% | +5,88% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 35 | 37,14% | +4,12% | -4,05% | -2,39% | +7,77% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -1,34% | -1,34% | -4,20% | +1,67% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 78 | 57,69% | +4,05% | +4,00% | -2,93% | +7,82% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 82 | 62,20% | +4,08% | +4,45% | -2,92% | +7,83% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 82 | 62,20% | +4,08% | +4,45% | -2,92% | +7,83% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 77 | 51,95% | +4,10% | +0,96% | -2,95% | +7,94% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 34 | 20,59% | +3,74% | -4,14% | -2,59% | +8,37% | PRIMA CALIBRAZIONE |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | -0,75% | -0,75% | -4,66% | +2,55% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 72 | 68,06% | +7,56% | +7,47% | -2,98% | +11,53% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 76 | 76,32% | +7,36% | +7,57% | -3,00% | +11,40% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 76 | 76,32% | +7,36% | +7,57% | -3,00% | +11,40% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 70 | 51,43% | +7,59% | +1,08% | -3,00% | +11,67% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 29 | 44,83% | +8,60% | -4,88% | -2,40% | +12,46% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 67 | 94,03% | +11,76% | +11,11% | -2,96% | +16,07% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 70 | 91,43% | +11,75% | +11,75% | -2,94% | +16,16% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 70 | 91,43% | +11,75% | +11,75% | -2,94% | +16,16% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 63 | 65,08% | +11,81% | +1,24% | -2,91% | +16,31% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 28 | 57,14% | +12,44% | -2,72% | -2,47% | +17,06% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 83,33% | +4,24% | +4,24% | -5,33% | +7,62% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 56 | 94,64% | +18,84% | +16,48% | -2,90% | +23,86% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 59 | 100,00% | +19,25% | +19,25% | -2,88% | +24,17% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 59 | 100,00% | +19,25% | +19,25% | -2,88% | +24,17% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 54 | 59,26% | +19,09% | -1,25% | -2,73% | +24,06% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,92% | -4,17% | -2,62% | +19,88% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +7,72% | +7,72% | -5,13% | +13,34% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 41 | 92,68% | +26,48% | +22,82% | -2,14% | +32,05% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 44 | 100,00% | +26,41% | +26,41% | -2,16% | +32,08% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 44 | 100,00% | +26,41% | +26,41% | -2,16% | +32,08% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +28,58% | +28,58% | -2,21% | +34,30% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 39 | 43,59% | +26,52% | -6,16% | -1,87% | +32,39% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 12 | 33,33% | +25,16% | -17,87% | -0,54% | +31,35% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +17,26% | +17,26% | -2,41% | +21,34% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 87 | 48,28% | +0,02% | -0,06% | -0,75% | +1,05% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 95 | 57,89% | -0,05% | +0,43% | -0,86% | +0,94% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 95 | 57,89% | -0,05% | +0,43% | -0,86% | +0,94% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 89 | 50,56% | -0,13% | +0,18% | -0,96% | +0,85% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 56 | 41,07% | -0,04% | -0,53% | -0,94% | +0,68% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 13 | 53,85% | +1,93% | +1,69% | +0,19% | +2,94% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 87 | 43,68% | +0,16% | -0,12% | -0,95% | +1,53% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 94 | 57,45% | -0,01% | +0,67% | -1,08% | +1,30% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 94 | 57,45% | -0,01% | +0,67% | -1,08% | +1,30% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 88 | 53,41% | -0,29% | +0,20% | -1,37% | +1,02% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 55 | 43,64% | +0,06% | -0,93% | -1,09% | +1,09% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 41,67% | +2,33% | +2,11% | +0,69% | +4,97% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 86 | 40,70% | +0,37% | +0,04% | -2,60% | +3,55% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 93 | 54,84% | +0,07% | +0,91% | -2,78% | +3,25% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 93 | 54,84% | +0,07% | +0,91% | -2,78% | +3,25% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 87 | 47,13% | -0,49% | +0,05% | -3,01% | +2,65% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 54 | 37,04% | +0,22% | -1,63% | -2,81% | +3,37% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 50,00% | +2,30% | +2,13% | -1,68% | +5,97% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 84 | 46,43% | +0,86% | +0,13% | -3,87% | +5,69% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 91 | 50,55% | +0,47% | +1,20% | -4,13% | +5,36% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 91 | 50,55% | +0,47% | +1,20% | -4,13% | +5,36% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 85 | 54,12% | -0,27% | -0,50% | -4,50% | +4,68% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 52 | 42,31% | +1,01% | -3,47% | -4,21% | +5,92% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 33,33% | +1,94% | +1,81% | -2,90% | +8,39% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 83 | 48,19% | +1,26% | +0,38% | -4,61% | +7,45% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 90 | 55,56% | +0,94% | +1,45% | -4,88% | +7,09% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 90 | 55,56% | +0,94% | +1,45% | -4,88% | +7,09% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 84 | 47,62% | +0,03% | -0,76% | -5,33% | +6,19% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 51 | 35,29% | +1,79% | -4,75% | -4,89% | +7,81% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +0,88% | +0,78% | -3,00% | +9,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 80 | 43,75% | +1,65% | +0,37% | -5,49% | +9,35% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 87 | 55,17% | +1,11% | +1,80% | -5,78% | +8,90% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 87 | 55,17% | +1,11% | +1,80% | -5,78% | +8,90% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 81 | 46,91% | -0,11% | -1,61% | -6,31% | +7,56% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 49 | 36,73% | +2,28% | -5,60% | -5,75% | +9,82% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 78 | 53,85% | +2,93% | +2,51% | -6,47% | +12,51% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 83 | 67,47% | +2,25% | +4,23% | -6,64% | +12,01% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 83 | 67,47% | +2,25% | +4,23% | -6,64% | +12,01% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 77 | 44,16% | +0,35% | -2,39% | -7,27% | +9,68% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 45 | 40,00% | +3,78% | -5,34% | -5,99% | +12,56% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 73 | 53,42% | +5,80% | +0,49% | -6,64% | +17,70% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 76 | 61,84% | +6,19% | +5,44% | -6,59% | +17,90% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 76 | 61,84% | +6,19% | +5,44% | -6,59% | +17,90% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 70 | 50,00% | +4,23% | -3,56% | -7,29% | +15,23% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 43 | 41,86% | +5,14% | -7,66% | -6,03% | +15,65% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +4,84% | -0,04% | -5,47% | +18,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 66 | 66,67% | +10,12% | +4,39% | -5,75% | +25,40% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 69 | 69,57% | +10,44% | +6,96% | -5,72% | +25,83% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 69 | 69,57% | +10,44% | +6,96% | -5,72% | +25,83% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 63 | 57,14% | +9,01% | -2,58% | -6,43% | +23,83% | UTILE |
| DOGE | 30g | Classic technical | CALIBRABILE | 41 | 48,78% | +8,28% | -6,60% | -5,70% | +22,87% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 72,73% | +14,01% | +8,26% | -6,83% | +27,95% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 55 | 49,09% | +17,21% | +3,62% | -5,35% | +36,33% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 58 | 67,24% | +17,00% | +7,91% | -5,34% | +36,28% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 58 | 67,24% | +17,00% | +7,91% | -5,34% | +36,28% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 52 | 9,62% | +14,04% | -12,26% | -6,16% | +34,21% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 33 | 3,03% | +19,56% | -21,33% | -5,75% | +37,18% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +18,19% | +8,68% | -5,75% | +33,52% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 42 | 45,24% | +22,39% | -0,40% | -4,04% | +43,48% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 44 | 56,82% | +22,93% | +8,10% | -4,06% | +43,66% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 44 | 56,82% | +22,93% | +8,10% | -4,06% | +43,66% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +24,96% | +11,95% | -3,59% | +45,33% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 37 | 8,11% | +23,07% | -22,17% | -4,85% | +42,31% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 29 | 0,00% | +21,38% | -22,84% | -4,58% | +42,30% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +24,97% | +12,49% | -2,74% | +43,78% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 87 | 47,13% | +0,19% | +0,09% | -0,60% | +1,05% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 90 | 53,33% | +0,15% | +0,40% | -0,71% | +1,00% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 93 | 52,69% | +0,18% | +0,35% | -0,67% | +1,03% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 88 | 46,59% | +0,14% | -0,08% | -0,76% | +0,98% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 59 | 44,07% | +0,51% | -0,09% | -0,48% | +1,43% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 86 | 44,19% | +0,57% | +0,45% | -0,64% | +1,65% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 89 | 50,56% | +0,45% | +0,63% | -0,85% | +1,41% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 92 | 50,00% | +0,45% | +0,59% | -0,82% | +1,45% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 87 | 43,68% | +0,28% | -0,04% | -0,83% | +1,41% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,60% | +0,15% | -0,64% | +1,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 85 | 48,24% | +0,95% | +0,80% | -2,22% | +3,55% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 88 | 51,14% | +0,80% | +1,13% | -2,37% | +3,35% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 91 | 50,55% | +0,79% | +1,09% | -2,33% | +3,35% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 86 | 45,35% | +0,43% | -0,33% | -2,39% | +2,95% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 59 | 45,76% | +0,61% | +0,08% | -2,23% | +3,14% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 83 | 49,40% | +1,68% | +1,62% | -3,30% | +5,51% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 86 | 53,49% | +1,48% | +1,85% | -3,43% | +5,27% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 89 | 52,81% | +1,45% | +1,76% | -3,38% | +5,22% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 84 | 45,24% | +1,11% | -0,76% | -3,48% | +4,75% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,71% | -0,02% | -3,27% | +4,40% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 83 | 53,01% | +2,48% | +2,54% | -3,96% | +6,97% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 85 | 60,00% | +2,27% | +3,02% | -4,07% | +6,77% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 88 | 60,23% | +2,19% | +2,92% | -4,02% | +6,67% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 83 | 40,96% | +1,37% | -1,66% | -4,16% | +5,95% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 59 | 42,37% | +0,39% | -0,27% | -4,06% | +5,04% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 80 | 53,75% | +3,77% | +3,87% | -4,63% | +8,93% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 82 | 67,07% | +3,64% | +5,43% | -4,75% | +8,61% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 85 | 65,88% | +3,50% | +5,25% | -4,70% | +8,44% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 80 | 42,50% | +2,12% | -2,26% | -4,91% | +7,35% | UTILE |
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
