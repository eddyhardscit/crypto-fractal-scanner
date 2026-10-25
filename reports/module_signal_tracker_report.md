# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-25 06:34 UTC

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

Segnali totali salvati: **300**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-25 | BTC | 80.511,75 | 0 | +2 | +2 | 0 | -2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-25 | DOGE | 0.07699 | -5 | 0 | 0 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-10-25 | SOL | 101,78 | -2 | 0 | 0 | +2 | -1 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-10-24 | BTC | 80.612,90 | -1 | +2 | +2 | 0 | -2 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-24 | DOGE | 0.07824 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-24 | SOL | 102,15 | 0 | +1 | +1 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-23 | BTC | 81.657,99 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-23 | DOGE | 0.07979 | -1 | +3 | +3 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-23 | SOL | 104,39 | +3 | +3 | +3 | 0 | +1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-10-22 | BTC | 82.752,49 | +2 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-22 | DOGE | 0.07992 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-22 | SOL | 105,09 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 100 | 99 | 98 | 97 | 95 | 93 | 91 | 87 | 80 | 72 | 62 | 47 |
| SOL | 100 | 99 | 98 | 97 | 95 | 93 | 91 | 87 | 80 | 72 | 62 | 47 |
| DOGE | 100 | 99 | 98 | 97 | 95 | 93 | 91 | 87 | 80 | 72 | 62 | 47 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-27 | 60g | 2026-10-26 | domani |
| SOL | 2026-08-27 | 60g | 2026-10-26 | domani |
| DOGE | 2026-08-27 | 60g | 2026-10-26 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 88 | 52,27% | +0,27% | +0,25% | UTILE |
| BTC | 2g | 87 | 49,43% | +0,44% | +0,37% | UTILE |
| BTC | 3g | 86 | 45,35% | +0,57% | +0,54% | UTILE |
| BTC | 5g | 85 | 44,71% | +1,22% | +1,16% | UTILE |
| BTC | 7g | 83 | 49,40% | +1,91% | +1,76% | UTILE |
| BTC | 10g | 81 | 55,56% | +2,67% | +2,60% | UTILE |
| BTC | 14g | 78 | 57,69% | +4,05% | +4,00% | UTILE |
| BTC | 21g | 75 | 65,33% | +7,05% | +6,96% | UTILE |
| BTC | 30g | 69 | 91,30% | +11,27% | +10,65% | UTILE |
| BTC | 45g | 59 | 94,92% | +18,02% | +15,78% | PRIMA CALIBRAZIONE |
| BTC | 60g | 44 | 90,91% | +24,85% | +21,44% | PRIMA CALIBRAZIONE |
| SOL | 1g | 89 | 46,07% | +0,15% | +0,05% | UTILE |
| SOL | 2g | 89 | 42,70% | +0,47% | +0,36% | UTILE |
| SOL | 3g | 88 | 46,59% | +0,84% | +0,69% | UTILE |
| SOL | 5g | 86 | 48,84% | +1,57% | +1,55% | UTILE |
| SOL | 7g | 84 | 53,57% | +2,43% | +2,53% | UTILE |
| SOL | 10g | 83 | 51,81% | +3,53% | +3,62% | UTILE |
| SOL | 14g | 79 | 59,49% | +5,55% | +6,01% | UTILE |
| SOL | 21g | 72 | 70,83% | +11,02% | +10,52% | UTILE |
| SOL | 30g | 64 | 79,69% | +17,96% | +14,87% | UTILE |
| SOL | 45g | 55 | 72,73% | +29,45% | +15,46% | PRIMA CALIBRAZIONE |
| SOL | 60g | 40 | 70,00% | +39,86% | +17,95% | PRIMA CALIBRAZIONE |
| DOGE | 1g | 88 | 48,86% | -0,00% | -0,03% | UTILE |
| DOGE | 2g | 88 | 44,32% | +0,12% | -0,08% | UTILE |
| DOGE | 3g | 87 | 40,23% | +0,37% | +0,03% | UTILE |
| DOGE | 5g | 87 | 47,13% | +0,79% | +0,16% | UTILE |
| DOGE | 7g | 85 | 49,41% | +1,16% | +0,43% | UTILE |
| DOGE | 10g | 83 | 43,37% | +1,39% | +0,24% | UTILE |
| DOGE | 14g | 80 | 53,75% | +2,62% | +2,44% | UTILE |
| DOGE | 21g | 75 | 53,33% | +5,20% | +0,46% | UTILE |
| DOGE | 30g | 68 | 64,71% | +9,17% | +3,62% | UTILE |
| DOGE | 45g | 58 | 48,28% | +15,72% | +3,19% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 45 | 42,22% | +20,01% | -1,27% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 88 | 52,27% | +0,27% | +0,25% | -0,30% | +0,77% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 97 | 47,42% | +0,17% | +0,22% | -0,35% | +0,68% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 97 | 47,42% | +0,17% | +0,22% | -0,35% | +0,68% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 92 | 51,09% | +0,19% | +0,10% | -0,31% | +0,71% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,55% | -0,06% | -0,27% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 87 | 49,43% | +0,44% | +0,37% | -0,31% | +1,14% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 96 | 51,04% | +0,38% | +0,46% | -0,33% | +1,06% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 96 | 51,04% | +0,38% | +0,46% | -0,33% | +1,06% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 91 | 49,45% | +0,36% | +0,13% | -0,26% | +1,04% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,85% | -0,13% | -0,05% | +1,59% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 86 | 45,35% | +0,57% | +0,54% | -1,30% | +2,35% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 95 | 49,47% | +0,66% | +0,72% | -1,37% | +2,38% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 95 | 49,47% | +0,66% | +0,72% | -1,37% | +2,38% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 90 | 41,11% | +0,66% | -0,03% | -1,32% | +2,39% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 36 | 36,11% | +1,29% | -0,55% | -1,13% | +3,01% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 85 | 44,71% | +1,22% | +1,16% | -1,95% | +3,69% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 93 | 48,39% | +1,32% | +1,43% | -1,97% | +3,72% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 93 | 48,39% | +1,32% | +1,43% | -1,97% | +3,72% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 88 | 43,18% | +1,19% | -0,59% | -1,93% | +3,66% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 36 | 36,11% | +2,85% | -2,16% | -1,73% | +5,27% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 83 | 49,40% | +1,91% | +1,76% | -2,30% | +4,77% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 91 | 57,14% | +1,99% | +2,15% | -2,32% | +4,74% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 91 | 57,14% | +1,99% | +2,15% | -2,32% | +4,74% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 86 | 43,02% | +1,93% | -0,98% | -2,30% | +4,69% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 36 | 33,33% | +4,03% | -3,63% | -2,13% | +7,10% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 81 | 55,56% | +2,67% | +2,60% | -2,66% | +5,84% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 89 | 65,17% | +2,62% | +2,99% | -2,66% | +5,76% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 89 | 65,17% | +2,62% | +2,99% | -2,66% | +5,76% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 84 | 46,43% | +2,56% | -0,43% | -2,68% | +5,76% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 36 | 38,89% | +4,00% | -3,92% | -2,35% | +7,69% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -1,34% | -1,34% | -4,20% | +1,67% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 78 | 57,69% | +4,05% | +4,00% | -2,93% | +7,82% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 85 | 63,53% | +3,86% | +4,36% | -2,94% | +7,65% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 85 | 63,53% | +3,86% | +4,36% | -2,94% | +7,65% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 80 | 50,00% | +3,87% | +0,84% | -2,97% | +7,73% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 34 | 20,59% | +3,74% | -4,14% | -2,59% | +8,37% | PRIMA CALIBRAZIONE |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -1,00% | -1,00% | -4,58% | +2,51% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 75 | 65,33% | +7,05% | +6,96% | -3,12% | +11,15% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 78 | 75,64% | +7,04% | +7,37% | -3,10% | +11,15% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 78 | 75,64% | +7,04% | +7,37% | -3,10% | +11,15% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 73 | 49,32% | +7,07% | +0,83% | -3,15% | +11,27% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 32 | 40,62% | +7,31% | -4,91% | -2,79% | +11,47% | PRIMA CALIBRAZIONE |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | -0,41% | -0,41% | -5,42% | +4,34% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 69 | 91,30% | +11,27% | +10,65% | -3,06% | +15,67% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 72 | 88,89% | +11,29% | +11,29% | -3,04% | +15,77% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 72 | 88,89% | +11,29% | +11,29% | -3,04% | +15,77% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 65 | 63,08% | +11,29% | +1,04% | -3,02% | +15,87% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 29 | 55,17% | +11,81% | -2,82% | -2,66% | +16,49% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +2,81% | +2,81% | -5,71% | +6,60% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 59 | 94,92% | +18,02% | +15,78% | -3,00% | +23,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 62 | 100,00% | +18,46% | +18,46% | -2,97% | +23,53% | UTILE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 62 | 100,00% | +18,46% | +18,46% | -2,97% | +23,53% | UTILE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 57 | 61,40% | +18,23% | -1,03% | -2,84% | +23,37% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,92% | -4,17% | -2,62% | +19,88% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +7,72% | +7,72% | -5,13% | +13,34% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 44 | 90,91% | +24,85% | +21,44% | -2,34% | +30,59% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 47 | 97,87% | +24,88% | +24,88% | -2,34% | +30,71% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 47 | 97,87% | +24,88% | +24,88% | -2,34% | +30,71% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +28,58% | +28,58% | -2,21% | +34,30% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 42 | 45,24% | +24,81% | -5,54% | -2,09% | +30,84% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 15 | 40,00% | +20,64% | -13,78% | -1,43% | +27,22% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +11,44% | +11,44% | -4,01% | +16,95% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 88 | 48,86% | -0,00% | -0,03% | -0,77% | +1,02% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 98 | 56,12% | -0,09% | +0,38% | -0,89% | +0,89% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 98 | 56,12% | -0,09% | +0,38% | -0,89% | +0,89% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 92 | 52,17% | -0,17% | +0,21% | -0,99% | +0,80% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 59 | 44,07% | -0,10% | -0,44% | -0,98% | +0,62% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 13 | 53,85% | +1,93% | +1,69% | +0,19% | +2,94% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 88 | 44,32% | +0,12% | -0,08% | -0,98% | +1,48% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 97 | 55,67% | -0,09% | +0,57% | -1,14% | +1,20% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 97 | 55,67% | -0,09% | +0,57% | -1,14% | +1,20% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 91 | 54,95% | -0,37% | +0,28% | -1,43% | +0,92% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 58 | 46,55% | -0,08% | -0,75% | -1,20% | +0,93% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 13 | 38,46% | +1,97% | +1,77% | +0,35% | +4,40% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 87 | 40,23% | +0,37% | +0,03% | -2,58% | +3,57% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 96 | 54,17% | -0,01% | +0,81% | -2,79% | +3,22% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 96 | 54,17% | -0,01% | +0,81% | -2,79% | +3,22% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 90 | 47,78% | -0,56% | +0,13% | -3,01% | +2,63% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 57 | 38,60% | +0,08% | -1,41% | -2,82% | +3,31% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 13 | 46,15% | +1,80% | +1,64% | -1,90% | +5,55% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 87 | 47,13% | +0,79% | +0,16% | -3,80% | +5,68% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 94 | 50,00% | +0,41% | +1,13% | -4,06% | +5,37% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 94 | 50,00% | +0,41% | +1,13% | -4,06% | +5,37% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 88 | 54,55% | -0,31% | -0,44% | -4,41% | +4,71% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 55 | 43,64% | +0,89% | -3,22% | -4,08% | +5,90% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 33,33% | +1,94% | +1,81% | -2,90% | +8,39% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 85 | 49,41% | +1,16% | +0,43% | -4,62% | +7,37% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 92 | 54,35% | +0,86% | +1,36% | -4,88% | +7,02% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 92 | 54,35% | +0,86% | +1,36% | -4,88% | +7,02% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 86 | 48,84% | -0,03% | -0,68% | -5,32% | +6,13% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 53 | 37,74% | +1,62% | -4,47% | -4,89% | +7,66% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 41,67% | +0,56% | +0,47% | -3,35% | +8,92% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 83 | 43,37% | +1,39% | +0,24% | -5,58% | +9,07% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 90 | 53,33% | +0,88% | +1,56% | -5,85% | +8,66% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 90 | 53,33% | +0,88% | +1,56% | -5,85% | +8,66% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 84 | 48,81% | -0,31% | -1,36% | -6,37% | +7,35% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 51 | 39,22% | +2,01% | -5,21% | -5,81% | +9,55% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 54,55% | +0,96% | +0,68% | -3,98% | +10,03% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 80 | 53,75% | +2,62% | +2,44% | -6,59% | +12,26% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 86 | 65,12% | +1,87% | +3,78% | -6,80% | +11,68% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 86 | 65,12% | +1,87% | +3,78% | -6,80% | +11,68% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 80 | 46,25% | +0,01% | -1,97% | -7,41% | +9,42% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 48 | 43,75% | +3,01% | -4,47% | -6,31% | +11,94% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 75 | 53,33% | +5,20% | +0,46% | -6,99% | +17,30% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 79 | 63,29% | +5,32% | +5,87% | -7,07% | +17,35% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 79 | 63,29% | +5,32% | +5,87% | -7,07% | +17,35% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 73 | 47,95% | +3,37% | -4,10% | -7,78% | +14,74% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 44 | 40,91% | +4,63% | -7,88% | -6,37% | +15,31% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +4,84% | -0,04% | -5,47% | +18,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 68 | 64,71% | +9,17% | +3,62% | -6,29% | +24,62% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 71 | 70,42% | +9,52% | +7,39% | -6,24% | +25,07% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 71 | 70,42% | +9,52% | +7,39% | -6,24% | +25,07% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 65 | 55,38% | +8,06% | -3,18% | -6,98% | +23,06% | UTILE |
| DOGE | 30g | Classic technical | CALIBRABILE | 43 | 46,51% | +6,87% | -7,32% | -6,56% | +21,76% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 72,73% | +14,01% | +8,26% | -6,83% | +27,95% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 58 | 48,28% | +15,72% | +3,19% | -5,80% | +35,42% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 61 | 68,85% | +15,59% | +8,09% | -5,76% | +35,42% | UTILE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 61 | 68,85% | +15,59% | +8,09% | -5,76% | +35,42% | UTILE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 55 | 10,91% | +12,64% | -11,85% | -6,58% | +33,37% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 34 | 2,94% | +18,65% | -21,04% | -6,03% | +36,58% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +18,19% | +8,68% | -5,75% | +33,52% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 45 | 42,22% | +20,01% | -1,27% | -4,81% | +41,68% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 46 | 54,35% | +21,31% | +7,12% | -4,64% | +42,37% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 46 | 54,35% | +21,31% | +7,12% | -4,64% | +42,37% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +24,96% | +11,95% | -3,59% | +45,33% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 40 | 7,50% | +20,34% | -21,51% | -5,67% | +40,37% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 31 | 0,00% | +19,07% | -22,30% | -5,41% | +40,47% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +19,54% | +8,85% | -4,76% | +39,64% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 89 | 46,07% | +0,15% | +0,05% | -0,63% | +1,00% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 93 | 51,61% | +0,11% | +0,36% | -0,73% | +0,95% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 96 | 51,04% | +0,14% | +0,31% | -0,70% | +0,98% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 90 | 46,67% | +0,11% | -0,09% | -0,79% | +0,93% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 59 | 44,07% | +0,51% | -0,09% | -0,48% | +1,43% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 89 | 42,70% | +0,47% | +0,36% | -0,71% | +1,53% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 92 | 48,91% | +0,36% | +0,53% | -0,91% | +1,30% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 95 | 48,42% | +0,36% | +0,50% | -0,88% | +1,35% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 90 | 44,44% | +0,20% | -0,02% | -0,89% | +1,31% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,60% | +0,15% | -0,64% | +1,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 88 | 46,59% | +0,84% | +0,69% | -2,24% | +3,49% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 91 | 49,45% | +0,70% | +1,02% | -2,38% | +3,30% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 94 | 48,94% | +0,69% | +0,98% | -2,34% | +3,30% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 89 | 47,19% | +0,33% | -0,24% | -2,40% | +2,92% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 59 | 45,76% | +0,61% | +0,08% | -2,23% | +3,14% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 86 | 48,84% | +1,57% | +1,55% | -3,25% | +5,46% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 89 | 52,81% | +1,37% | +1,73% | -3,38% | +5,24% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 92 | 52,17% | +1,35% | +1,65% | -3,34% | +5,19% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 87 | 45,98% | +1,01% | -0,67% | -3,43% | +4,74% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,71% | -0,02% | -3,27% | +4,40% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 84 | 53,57% | +2,43% | +2,53% | -3,93% | +6,95% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 87 | 58,62% | +2,19% | +2,91% | -4,05% | +6,71% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 90 | 58,89% | +2,11% | +2,82% | -4,01% | +6,62% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 85 | 42,35% | +1,31% | -1,58% | -4,14% | +5,91% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 59 | 42,37% | +0,39% | -0,27% | -4,06% | +5,04% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 83 | 51,81% | +3,53% | +3,62% | -4,64% | +8,72% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 85 | 64,71% | +3,41% | +5,14% | -4,75% | +8,42% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 88 | 63,64% | +3,29% | +4,97% | -4,71% | +8,26% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 83 | 44,58% | +1,94% | -2,07% | -4,92% | +7,20% | UTILE |
| SOL | 10g | Classic technical | CALIBRABILE | 59 | 44,07% | +0,02% | -0,63% | -4,99% | +5,74% | PRIMA CALIBRAZIONE |

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
