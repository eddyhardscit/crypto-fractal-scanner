# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-10-26 06:34 UTC

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

Segnali totali salvati: **303**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-26 | BTC | 79.926,04 | -4 | -1 | -1 | 0 | -2 | 0 | 0 | STAI FUORI / SHORT SOLO DOPO ROTTURA |
| 2026-10-26 | DOGE | 0.07671 | -5 | -1 | -1 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-10-26 | SOL | 100,74 | -1 | 0 | 0 | -1 | -1 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-10-25 | BTC | 80.511,75 | 0 | +2 | +2 | 0 | -2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-25 | DOGE | 0.07699 | -5 | 0 | 0 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-10-25 | SOL | 101,78 | -2 | 0 | 0 | +2 | -1 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-10-24 | BTC | 80.612,90 | -1 | +2 | +2 | 0 | -2 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-10-24 | DOGE | 0.07824 | 0 | +3 | +3 | 0 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-10-24 | SOL | 102,15 | 0 | +1 | +1 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-10-23 | BTC | 81.657,99 | +2 | +3 | +3 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-10-23 | DOGE | 0.07979 | -1 | +3 | +3 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-10-23 | SOL | 104,39 | +3 | +3 | +3 | 0 | +1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 101 | 100 | 99 | 98 | 96 | 94 | 92 | 88 | 81 | 73 | 63 | 48 |
| SOL | 101 | 100 | 99 | 98 | 96 | 94 | 92 | 88 | 81 | 73 | 63 | 48 |
| DOGE | 101 | 100 | 99 | 98 | 96 | 94 | 92 | 88 | 81 | 73 | 63 | 48 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-08-28 | 60g | 2026-10-27 | domani |
| SOL | 2026-08-28 | 60g | 2026-10-27 | domani |
| DOGE | 2026-08-28 | 60g | 2026-10-27 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 88 | 52,27% | +0,27% | +0,25% | UTILE |
| BTC | 2g | 88 | 50,00% | +0,43% | +0,38% | UTILE |
| BTC | 3g | 87 | 44,83% | +0,54% | +0,51% | UTILE |
| BTC | 5g | 85 | 44,71% | +1,22% | +1,16% | UTILE |
| BTC | 7g | 84 | 50,00% | +1,85% | +1,78% | UTILE |
| BTC | 10g | 82 | 54,88% | +2,61% | +2,54% | UTILE |
| BTC | 14g | 79 | 58,23% | +3,94% | +4,01% | UTILE |
| BTC | 21g | 76 | 64,47% | +6,87% | +6,79% | UTILE |
| BTC | 30g | 69 | 91,30% | +11,27% | +10,65% | UTILE |
| BTC | 45g | 60 | 95,00% | +17,78% | +15,58% | UTILE |
| BTC | 60g | 45 | 91,11% | +24,33% | +21,00% | PRIMA CALIBRAZIONE |
| SOL | 1g | 90 | 46,67% | +0,14% | +0,06% | UTILE |
| SOL | 2g | 89 | 42,70% | +0,47% | +0,36% | UTILE |
| SOL | 3g | 89 | 46,07% | +0,79% | +0,65% | UTILE |
| SOL | 5g | 87 | 48,28% | +1,49% | +1,48% | UTILE |
| SOL | 7g | 85 | 54,12% | +2,35% | +2,56% | UTILE |
| SOL | 10g | 83 | 51,81% | +3,53% | +3,62% | UTILE |
| SOL | 14g | 80 | 58,75% | +5,35% | +5,81% | UTILE |
| SOL | 21g | 73 | 69,86% | +10,65% | +10,16% | UTILE |
| SOL | 30g | 65 | 78,46% | +17,43% | +14,39% | UTILE |
| SOL | 45g | 56 | 73,21% | +28,95% | +15,20% | PRIMA CALIBRAZIONE |
| SOL | 60g | 41 | 68,29% | +38,89% | +17,51% | PRIMA CALIBRAZIONE |
| DOGE | 1g | 89 | 49,44% | -0,01% | -0,03% | UTILE |
| DOGE | 2g | 88 | 44,32% | +0,12% | -0,08% | UTILE |
| DOGE | 3g | 88 | 40,91% | +0,32% | +0,08% | UTILE |
| DOGE | 5g | 87 | 47,13% | +0,79% | +0,16% | UTILE |
| DOGE | 7g | 86 | 50,00% | +1,11% | +0,47% | UTILE |
| DOGE | 10g | 84 | 44,05% | +1,29% | +0,31% | UTILE |
| DOGE | 14g | 80 | 53,75% | +2,62% | +2,44% | UTILE |
| DOGE | 21g | 75 | 53,33% | +5,20% | +0,46% | UTILE |
| DOGE | 30g | 69 | 63,77% | +8,73% | +3,26% | UTILE |
| DOGE | 45g | 59 | 49,15% | +15,31% | +3,28% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 46 | 43,48% | +19,33% | -1,00% | PRIMA CALIBRAZIONE |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 88 | 52,27% | +0,27% | +0,25% | -0,30% | +0,77% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 98 | 46,94% | +0,16% | +0,21% | -0,36% | +0,67% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 98 | 46,94% | +0,16% | +0,21% | -0,36% | +0,67% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 93 | 51,61% | +0,18% | +0,10% | -0,32% | +0,69% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,55% | -0,06% | -0,27% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 40,00% | -0,38% | -0,38% | -0,95% | +0,06% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 88 | 50,00% | +0,43% | +0,38% | -0,32% | +1,12% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 97 | 50,52% | +0,37% | +0,44% | -0,34% | +1,04% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 97 | 50,52% | +0,37% | +0,44% | -0,34% | +1,04% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 92 | 50,00% | +0,35% | +0,14% | -0,27% | +1,02% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,85% | -0,13% | -0,05% | +1,59% | PRIMA CALIBRAZIONE |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 87 | 44,83% | +0,54% | +0,51% | -1,32% | +2,32% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 96 | 48,96% | +0,63% | +0,69% | -1,39% | +2,34% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 96 | 48,96% | +0,63% | +0,69% | -1,39% | +2,34% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 91 | 41,76% | +0,63% | -0,00% | -1,33% | +2,36% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 36 | 36,11% | +1,29% | -0,55% | -1,13% | +3,01% | PRIMA CALIBRAZIONE |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 85 | 44,71% | +1,22% | +1,16% | -1,95% | +3,69% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 94 | 47,87% | +1,27% | +1,38% | -1,99% | +3,70% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 94 | 47,87% | +1,27% | +1,38% | -1,99% | +3,70% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 89 | 43,82% | +1,14% | -0,55% | -1,96% | +3,64% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 36 | 36,11% | +2,85% | -2,16% | -1,73% | +5,27% | PRIMA CALIBRAZIONE |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 84 | 50,00% | +1,85% | +1,78% | -2,32% | +4,75% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 92 | 56,52% | +1,93% | +2,09% | -2,34% | +4,72% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 92 | 56,52% | +1,93% | +2,09% | -2,34% | +4,72% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 87 | 43,68% | +1,87% | -0,93% | -2,32% | +4,66% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 36 | 33,33% | +4,03% | -3,63% | -2,13% | +7,10% | PRIMA CALIBRAZIONE |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 82 | 54,88% | +2,61% | +2,54% | -2,67% | +5,81% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 90 | 64,44% | +2,56% | +2,93% | -2,67% | +5,73% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 90 | 64,44% | +2,56% | +2,93% | -2,67% | +5,73% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 85 | 47,06% | +2,50% | -0,39% | -2,69% | +5,73% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 36 | 38,89% | +4,00% | -3,92% | -2,35% | +7,69% | PRIMA CALIBRAZIONE |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -1,34% | -1,34% | -4,20% | +1,67% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 79 | 58,23% | +3,94% | +4,01% | -2,96% | +7,74% | UTILE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 86 | 63,95% | +3,76% | +4,37% | -2,97% | +7,57% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 86 | 63,95% | +3,76% | +4,37% | -2,97% | +7,57% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 81 | 50,62% | +3,77% | +0,89% | -3,00% | +7,66% | UTILE |
| BTC | 14g | Classic technical | CALIBRABILE | 35 | 22,86% | +3,50% | -3,89% | -2,67% | +8,17% | PRIMA CALIBRAZIONE |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | -1,00% | -1,00% | -4,58% | +2,51% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 76 | 64,47% | +6,87% | +6,79% | -3,18% | +11,02% | UTILE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 79 | 75,95% | +6,87% | +7,36% | -3,15% | +11,03% | UTILE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 79 | 75,95% | +6,87% | +7,36% | -3,15% | +11,03% | UTILE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 74 | 48,65% | +6,88% | +0,73% | -3,21% | +11,14% | UTILE |
| BTC | 21g | Classic technical | CALIBRABILE | 33 | 39,39% | +6,89% | -4,95% | -2,93% | +11,17% | PRIMA CALIBRAZIONE |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | -0,41% | -0,41% | -5,42% | +4,34% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 69 | 91,30% | +11,27% | +10,65% | -3,06% | +15,67% | UTILE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 73 | 89,04% | +11,07% | +11,20% | -3,07% | +15,61% | UTILE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 73 | 89,04% | +11,07% | +11,20% | -3,07% | +15,61% | UTILE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 66 | 62,12% | +11,05% | +0,96% | -3,06% | +15,69% | UTILE |
| BTC | 30g | Classic technical | CALIBRABILE | 29 | 55,17% | +11,81% | -2,82% | -2,66% | +16,49% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +2,81% | +2,81% | -5,71% | +6,60% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 60 | 95,00% | +17,78% | +15,58% | -2,99% | +23,04% | UTILE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 63 | 100,00% | +18,22% | +18,22% | -2,97% | +23,37% | UTILE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 63 | 100,00% | +18,22% | +18,22% | -2,97% | +23,37% | UTILE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +25,41% | +25,41% | -2,21% | +30,21% | PRIMA CALIBRAZIONE |
| BTC | 45g | Tecnico | CALIBRABILE | 58 | 62,07% | +17,98% | -0,95% | -2,84% | +23,20% | PRIMA CALIBRAZIONE |
| BTC | 45g | Classic technical | CALIBRABILE | 24 | 66,67% | +13,92% | -4,17% | -2,62% | +19,88% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 100,00% | +7,72% | +7,72% | -5,13% | +13,34% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 45 | 91,11% | +24,33% | +21,00% | -2,39% | +30,16% | PRIMA CALIBRAZIONE |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 48 | 97,92% | +24,40% | +24,40% | -2,39% | +30,31% | PRIMA CALIBRAZIONE |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 48 | 97,92% | +24,40% | +24,40% | -2,39% | +30,31% | PRIMA CALIBRAZIONE |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 35 | 100,00% | +28,58% | +28,58% | -2,21% | +34,30% | PRIMA CALIBRAZIONE |
| BTC | 60g | Tecnico | CALIBRABILE | 43 | 46,51% | +24,27% | -5,37% | -2,15% | +30,39% | PRIMA CALIBRAZIONE |
| BTC | 60g | Classic technical | CALIBRABILE | 16 | 43,75% | +19,45% | -12,82% | -1,64% | +26,22% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +11,44% | +11,44% | -4,01% | +16,95% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 89 | 49,44% | -0,01% | -0,03% | -0,78% | +1,01% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 98 | 56,12% | -0,09% | +0,38% | -0,89% | +0,89% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 98 | 56,12% | -0,09% | +0,38% | -0,89% | +0,89% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 93 | 52,69% | -0,17% | +0,21% | -0,99% | +0,80% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 60 | 45,00% | -0,11% | -0,43% | -0,99% | +0,61% | UTILE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 13 | 53,85% | +1,93% | +1,69% | +0,19% | +2,94% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 88 | 44,32% | +0,12% | -0,08% | -0,98% | +1,48% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 98 | 55,10% | -0,11% | +0,54% | -1,16% | +1,17% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 98 | 55,10% | -0,11% | +0,54% | -1,16% | +1,17% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 92 | 55,43% | -0,38% | +0,30% | -1,44% | +0,89% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 59 | 47,46% | -0,11% | -0,70% | -1,23% | +0,89% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 13 | 38,46% | +1,97% | +1,77% | +0,35% | +4,40% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 88 | 40,91% | +0,32% | +0,08% | -2,62% | +3,52% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 97 | 53,61% | -0,04% | +0,76% | -2,82% | +3,17% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 97 | 53,61% | -0,04% | +0,76% | -2,82% | +3,17% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 91 | 48,35% | -0,59% | +0,18% | -3,05% | +2,59% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 58 | 39,66% | +0,02% | -1,32% | -2,88% | +3,23% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 13 | 46,15% | +1,80% | +1,64% | -1,90% | +5,55% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 87 | 47,13% | +0,79% | +0,16% | -3,80% | +5,68% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 95 | 49,47% | +0,34% | +1,05% | -4,10% | +5,32% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 95 | 49,47% | +0,34% | +1,05% | -4,10% | +5,32% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 89 | 55,06% | -0,37% | -0,37% | -4,46% | +4,66% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 56 | 44,64% | +0,76% | -3,05% | -4,15% | +5,80% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 13 | 30,77% | +1,33% | +1,20% | -3,30% | +7,79% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 86 | 50,00% | +1,11% | +0,47% | -4,63% | +7,34% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 93 | 53,76% | +0,82% | +1,31% | -4,89% | +7,00% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 93 | 53,76% | +0,82% | +1,31% | -4,89% | +7,00% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 87 | 49,43% | -0,07% | -0,63% | -5,32% | +6,12% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 54 | 38,89% | +1,53% | -4,32% | -4,91% | +7,61% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 41,67% | +0,56% | +0,47% | -3,35% | +8,92% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 84 | 44,05% | +1,29% | +0,31% | -5,62% | +8,98% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 91 | 52,75% | +0,80% | +1,47% | -5,89% | +8,58% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 91 | 52,75% | +0,80% | +1,47% | -5,89% | +8,58% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 85 | 49,41% | -0,38% | -1,26% | -6,40% | +7,28% | UTILE |
| DOGE | 10g | Classic technical | CALIBRABILE | 52 | 40,38% | +1,85% | -4,98% | -5,86% | +9,40% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 12 | 50,00% | +0,32% | +0,07% | -4,37% | +9,35% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 80 | 53,75% | +2,62% | +2,44% | -6,59% | +12,26% | UTILE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 87 | 64,37% | +1,71% | +3,60% | -6,88% | +11,53% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 87 | 64,37% | +1,71% | +3,60% | -6,88% | +11,53% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 81 | 46,91% | -0,14% | -1,80% | -7,50% | +9,28% | UTILE |
| DOGE | 14g | Classic technical | CALIBRABILE | 49 | 44,90% | +2,70% | -4,13% | -6,46% | +11,65% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 45,45% | +5,60% | +2,03% | -4,35% | +14,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 75 | 53,33% | +5,20% | +0,46% | -6,99% | +17,30% | UTILE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 80 | 63,75% | +5,01% | +6,04% | -7,24% | +17,15% | UTILE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 80 | 63,75% | +5,01% | +6,04% | -7,24% | +17,15% | UTILE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 74 | 47,30% | +3,07% | -4,30% | -7,95% | +14,56% | UTILE |
| DOGE | 21g | Classic technical | CALIBRABILE | 44 | 40,91% | +4,63% | -7,88% | -6,37% | +15,31% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +4,84% | -0,04% | -5,47% | +18,61% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 69 | 63,77% | +8,73% | +3,26% | -6,53% | +24,28% | UTILE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 72 | 70,83% | +9,09% | +7,58% | -6,47% | +24,75% | UTILE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 72 | 70,83% | +9,09% | +7,58% | -6,47% | +24,75% | UTILE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 66 | 54,55% | +7,61% | -3,45% | -7,22% | +22,73% | UTILE |
| DOGE | 30g | Classic technical | CALIBRABILE | 43 | 46,51% | +6,87% | -7,32% | -6,56% | +21,76% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 72,73% | +14,01% | +8,26% | -6,83% | +27,95% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 59 | 49,15% | +15,31% | +3,28% | -5,88% | +35,25% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 62 | 69,35% | +15,20% | +8,10% | -5,84% | +35,26% | UTILE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 62 | 69,35% | +15,20% | +8,10% | -5,84% | +35,26% | UTILE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +25,02% | +11,34% | -3,59% | +42,51% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 56 | 12,50% | +12,26% | -11,48% | -6,66% | +33,23% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 35 | 5,71% | +17,88% | -20,19% | -6,16% | +36,27% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +18,19% | +8,68% | -5,75% | +33,52% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 46 | 43,48% | +19,33% | -1,00% | -4,99% | +41,25% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 47 | 55,32% | +20,62% | +7,20% | -4,82% | +41,94% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 47 | 55,32% | +20,62% | +7,20% | -4,82% | +41,94% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +24,96% | +11,95% | -3,59% | +45,33% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Tecnico | CALIBRABILE | 41 | 7,32% | +19,57% | -21,26% | -5,85% | +39,92% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Classic technical | CALIBRABILE | 31 | 0,00% | +19,07% | -22,30% | -5,41% | +40,47% | PRIMA CALIBRAZIONE |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +19,54% | +8,85% | -4,76% | +39,64% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 90 | 46,67% | +0,14% | +0,06% | -0,64% | +0,99% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 93 | 51,61% | +0,11% | +0,36% | -0,73% | +0,95% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 96 | 51,04% | +0,14% | +0,31% | -0,70% | +0,98% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,23% | +0,35% | -0,35% | +0,83% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 91 | 47,25% | +0,09% | -0,08% | -0,80% | +0,92% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 59 | 44,07% | +0,51% | -0,09% | -0,48% | +1,43% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 89 | 42,70% | +0,47% | +0,36% | -0,71% | +1,53% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 93 | 48,39% | +0,34% | +0,51% | -0,92% | +1,28% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 96 | 47,92% | +0,34% | +0,48% | -0,90% | +1,33% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 90 | 44,44% | +0,20% | -0,02% | -0,89% | +1,31% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,60% | +0,15% | -0,64% | +1,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 89 | 46,07% | +0,79% | +0,65% | -2,27% | +3,43% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 92 | 48,91% | +0,65% | +0,97% | -2,41% | +3,25% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 95 | 48,42% | +0,64% | +0,93% | -2,37% | +3,25% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 90 | 46,67% | +0,29% | -0,27% | -2,43% | +2,87% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 59 | 45,76% | +0,61% | +0,08% | -2,23% | +3,14% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 87 | 48,28% | +1,49% | +1,48% | -3,29% | +5,42% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 90 | 52,22% | +1,30% | +1,66% | -3,42% | +5,19% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 93 | 51,61% | +1,29% | +1,58% | -3,38% | +5,15% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 88 | 46,59% | +0,94% | -0,61% | -3,47% | +4,70% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 59 | 47,46% | +0,71% | -0,02% | -3,27% | +4,40% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 85 | 54,12% | +2,35% | +2,56% | -3,96% | +6,91% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 88 | 57,95% | +2,11% | +2,83% | -4,08% | +6,67% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 91 | 58,24% | +2,04% | +2,74% | -4,04% | +6,58% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 86 | 43,02% | +1,24% | -1,51% | -4,17% | +5,87% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 59 | 42,37% | +0,39% | -0,27% | -4,06% | +5,04% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 83 | 51,81% | +3,53% | +3,62% | -4,64% | +8,72% | UTILE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 86 | 63,95% | +3,32% | +5,02% | -4,77% | +8,35% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 89 | 62,92% | +3,20% | +4,86% | -4,73% | +8,20% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 84 | 45,24% | +1,86% | -1,99% | -4,94% | +7,15% | UTILE |
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
