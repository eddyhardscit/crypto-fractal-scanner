# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-22 05:32 UTC

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

Segnali totali salvati: **210**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-22 | BTC | 85.107,65 | +5 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-22 | DOGE | 0.09857 | +2 | -2 | -2 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-22 | SOL | 115,61 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-17 | BTC | 76.325,40 | +2 | +3 | +3 | 0 | 0 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-17 | DOGE | 0.08084 | -6 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-17 | SOL | 99,49 | 0 | +3 | +3 | 0 | -1 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-16 | BTC | 75.786,49 | +2 | +3 | +3 | 0 | 0 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-16 | DOGE | 0.08011 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-16 | SOL | 97,05 | +2 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-15 | BTC | 77.430,91 | +4 | +3 | +3 | 0 | +1 | -1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-15 | DOGE | 0.08280 | -4 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-15 | SOL | 100,84 | +2 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 70 | 69 | 69 | 69 | 69 | 67 | 64 | 60 | 53 | 44 | 31 | 16 |
| SOL | 70 | 69 | 69 | 69 | 69 | 67 | 64 | 60 | 53 | 44 | 31 | 16 |
| DOGE | 70 | 69 | 69 | 69 | 69 | 67 | 64 | 60 | 53 | 44 | 31 | 16 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-25 | 60g | 2026-09-23 | domani |
| SOL | 2026-07-25 | 60g | 2026-09-23 | domani |
| DOGE | 2026-07-25 | 60g | 2026-09-23 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 66 | 51,52% | +0,40% | +0,38% | UTILE |
| BTC | 2g | 66 | 51,52% | +0,70% | +0,63% | UTILE |
| BTC | 3g | 66 | 46,97% | +0,90% | +0,80% | UTILE |
| BTC | 5g | 66 | 45,45% | +1,86% | +1,67% | UTILE |
| BTC | 7g | 64 | 53,12% | +2,33% | +2,16% | UTILE |
| BTC | 10g | 61 | 59,02% | +3,08% | +2,93% | UTILE |
| BTC | 14g | 57 | 56,14% | +4,54% | +4,48% | PRIMA CALIBRAZIONE |
| BTC | 21g | 50 | 66,00% | +8,47% | +8,34% | PRIMA CALIBRAZIONE |
| BTC | 30g | 41 | 92,68% | +14,98% | +13,93% | PRIMA CALIBRAZIONE |
| BTC | 45g | 29 | 89,66% | +23,12% | +18,56% | FEEDBACK RAPIDO |
| BTC | 60g | 14 | 85,71% | +23,22% | +17,12% | FEEDBACK RAPIDO |
| SOL | 1g | 61 | 52,46% | +0,49% | +0,39% | UTILE |
| SOL | 2g | 61 | 47,54% | +1,19% | +1,08% | UTILE |
| SOL | 3g | 61 | 54,10% | +1,92% | +1,78% | UTILE |
| SOL | 5g | 61 | 57,38% | +3,32% | +3,23% | UTILE |
| SOL | 7g | 60 | 61,67% | +4,45% | +4,54% | UTILE |
| SOL | 10g | 57 | 64,91% | +5,89% | +6,03% | PRIMA CALIBRAZIONE |
| SOL | 14g | 53 | 71,70% | +8,42% | +9,10% | PRIMA CALIBRAZIONE |
| SOL | 21g | 46 | 78,26% | +14,54% | +13,76% | PRIMA CALIBRAZIONE |
| SOL | 30g | 37 | 72,97% | +23,29% | +17,95% | PRIMA CALIBRAZIONE |
| SOL | 45g | 24 | 54,17% | +37,36% | +5,29% | FEEDBACK RAPIDO |
| SOL | 60g | 14 | 35,71% | +36,45% | -8,96% | FEEDBACK RAPIDO |
| DOGE | 1g | 65 | 44,62% | +0,40% | +0,00% | UTILE |
| DOGE | 2g | 65 | 46,15% | +0,79% | +0,03% | UTILE |
| DOGE | 3g | 65 | 40,00% | +1,14% | +0,16% | UTILE |
| DOGE | 5g | 65 | 44,62% | +2,23% | +0,32% | UTILE |
| DOGE | 7g | 63 | 52,38% | +2,42% | +1,40% | UTILE |
| DOGE | 10g | 60 | 50,00% | +2,50% | +2,17% | UTILE |
| DOGE | 14g | 56 | 66,07% | +4,31% | +6,05% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 49 | 71,43% | +7,60% | +6,31% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 42 | 80,95% | +13,46% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 29 | 31,03% | +21,74% | -5,83% | FEEDBACK RAPIDO |
| DOGE | 60g | 16 | 0,00% | +20,40% | -20,40% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 66 | 51,52% | +0,40% | +0,38% | -0,14% | +0,92% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 69 | 53,62% | +0,38% | +0,38% | -0,15% | +0,89% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 69 | 53,62% | +0,38% | +0,38% | -0,15% | +0,89% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 62 | 40,32% | +0,39% | +0,05% | -0,07% | +0,90% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 28 | 39,29% | +0,86% | +0,16% | +0,02% | +1,38% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 66 | 51,52% | +0,70% | +0,63% | -0,05% | +1,35% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 69 | 53,62% | +0,78% | +0,78% | +0,04% | +1,43% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 69 | 53,62% | +0,78% | +0,78% | +0,04% | +1,43% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 62 | 43,55% | +0,74% | +0,07% | +0,18% | +1,38% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 28 | 42,86% | +1,35% | +0,13% | +0,35% | +2,03% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 66 | 46,97% | +0,90% | +0,80% | -1,14% | +2,62% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 69 | 53,62% | +1,15% | +1,15% | -1,12% | +2,80% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 69 | 53,62% | +1,15% | +1,15% | -1,12% | +2,80% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 62 | 37,10% | +1,22% | -0,14% | -1,02% | +2,87% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 28 | 39,29% | +2,14% | -0,42% | -0,72% | +3,60% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 66 | 45,45% | +1,86% | +1,67% | -1,75% | +4,19% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 69 | 50,72% | +2,06% | +2,06% | -1,72% | +4,43% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 69 | 50,72% | +2,06% | +2,06% | -1,72% | +4,43% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 62 | 41,94% | +2,00% | -0,73% | -1,64% | +4,42% | UTILE |
| BTC | 5g | Classic technical | CALIBRABILE | 28 | 42,86% | +4,36% | -2,17% | -1,11% | +6,49% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 64 | 53,12% | +2,33% | +2,16% | -2,13% | +5,10% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 67 | 58,21% | +2,59% | +2,59% | -2,10% | +5,35% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 67 | 58,21% | +2,59% | +2,59% | -2,10% | +5,35% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 62 | 43,55% | +2,98% | -1,13% | -1,96% | +5,69% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 26 | 42,31% | +5,25% | -3,35% | -1,48% | +8,31% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 61 | 59,02% | +3,08% | +2,93% | -2,40% | +6,07% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 64 | 62,50% | +3,24% | +3,24% | -2,39% | +6,28% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 64 | 62,50% | +3,24% | +3,24% | -2,39% | +6,28% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 59 | 47,46% | +3,61% | -0,89% | -2,23% | +6,71% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 24 | 50,00% | +5,20% | -3,59% | -1,59% | +8,77% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 57 | 56,14% | +4,54% | +4,48% | -2,56% | +8,13% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 60 | 56,67% | +4,65% | +4,65% | -2,55% | +8,26% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 60 | 56,67% | +4,65% | +4,65% | -2,55% | +8,26% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 55 | 52,73% | +5,19% | +0,78% | -2,37% | +8,86% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 24 | 29,17% | +4,78% | -3,41% | -1,84% | +9,24% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 50 | 66,00% | +8,47% | +8,34% | -2,46% | +12,40% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 53 | 71,70% | +8,38% | +8,38% | -2,46% | +12,33% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 53 | 71,70% | +8,38% | +8,38% | -2,46% | +12,33% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 48 | 45,83% | +9,09% | -0,40% | -2,25% | +13,11% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 21 | 47,62% | +8,94% | -5,79% | -1,99% | +12,96% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | -0,54% | -0,54% | -2,98% | +4,64% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 41 | 92,68% | +14,98% | +13,93% | -2,14% | +19,14% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 44 | 88,64% | +14,76% | +14,76% | -2,16% | +19,08% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 44 | 88,64% | +14,76% | +14,76% | -2,16% | +19,08% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 39 | 46,15% | +15,02% | -2,06% | -1,87% | +19,63% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 12 | 33,33% | +19,29% | -11,49% | -0,54% | +24,11% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,87% | +5,87% | -2,41% | +8,88% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 29 | 89,66% | +23,12% | +18,56% | -2,94% | +27,89% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 31 | 100,00% | +23,11% | +23,11% | -2,98% | +27,81% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 31 | 100,00% | +23,11% | +23,11% | -2,98% | +27,81% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 27 | 100,00% | +23,41% | +23,41% | -2,76% | +28,19% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 26 | 34,62% | +23,52% | -6,01% | -2,70% | +28,28% | FEEDBACK RAPIDO |
| BTC | 45g | Classic technical | CALIBRABILE | 4 | 0,00% | +21,70% | -21,70% | -1,55% | +30,01% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 14 | 85,71% | +23,22% | +17,12% | -3,23% | +28,68% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 16 | 100,00% | +23,38% | +23,38% | -3,28% | +28,93% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 16 | 100,00% | +23,38% | +23,38% | -3,28% | +28,93% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 12 | 100,00% | +23,63% | +23,63% | -2,88% | +29,82% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 13 | 30,77% | +23,40% | -10,57% | -2,94% | +29,56% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 65 | 44,62% | +0,40% | +0,00% | -0,37% | +1,34% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 68 | 57,35% | +0,30% | +0,41% | -0,48% | +1,19% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 68 | 57,35% | +0,30% | +0,41% | -0,48% | +1,19% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 62 | 51,61% | +0,22% | +0,29% | -0,59% | +1,10% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 41 | 41,46% | +0,29% | -0,51% | -0,53% | +1,01% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 60,00% | +2,73% | +2,42% | +0,65% | +3,48% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 65 | 46,15% | +0,79% | +0,03% | -0,23% | +2,03% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 68 | 57,35% | +0,62% | +0,66% | -0,38% | +1,78% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 68 | 57,35% | +0,62% | +0,66% | -0,38% | +1,78% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 62 | 54,84% | +0,28% | +0,35% | -0,72% | +1,43% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 41 | 43,90% | +0,59% | -1,27% | -0,53% | +1,59% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 50,00% | +3,46% | +3,20% | +1,88% | +5,67% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 65 | 40,00% | +1,14% | +0,16% | -1,97% | +4,21% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 68 | 54,41% | +0,96% | +0,95% | -2,09% | +3,89% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 68 | 54,41% | +0,96% | +0,95% | -2,09% | +3,89% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 62 | 45,16% | +0,26% | +0,18% | -2,35% | +3,10% | UTILE |
| DOGE | 3g | Classic technical | CALIBRABILE | 41 | 31,71% | +0,97% | -2,21% | -2,33% | +4,17% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 50,00% | +3,04% | +2,83% | -0,79% | +6,76% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 65 | 44,62% | +2,23% | +0,32% | -3,01% | +6,88% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 68 | 50,00% | +2,10% | +1,18% | -3,07% | +6,62% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 68 | 50,00% | +2,10% | +1,18% | -3,07% | +6,62% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 62 | 53,23% | +1,24% | -0,43% | -3,48% | +5,81% | UTILE |
| DOGE | 5g | Classic technical | CALIBRABILE | 41 | 34,15% | +2,58% | -4,70% | -3,39% | +7,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 10 | 40,00% | +2,66% | +2,50% | -2,06% | +9,50% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 63 | 52,38% | +2,42% | +1,40% | -3,74% | +8,37% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 66 | 54,55% | +2,45% | +1,97% | -3,77% | +8,18% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 66 | 54,55% | +2,45% | +1,97% | -3,77% | +8,18% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 60 | 50,00% | +1,33% | -0,04% | -4,29% | +7,03% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 39 | 30,77% | +2,86% | -5,59% | -4,15% | +8,43% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,37% | -0,49% | -2,97% | +7,69% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 60 | 50,00% | +2,50% | +2,17% | -4,35% | +9,70% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 63 | 52,38% | +2,46% | +2,45% | -4,34% | +9,55% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 63 | 52,38% | +2,46% | +2,45% | -4,34% | +9,55% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 57 | 56,14% | +0,86% | +0,27% | -4,95% | +7,71% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 36 | 36,11% | +2,16% | -5,43% | -4,83% | +9,44% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | -0,68% | -1,01% | -4,16% | +8,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 56 | 66,07% | +4,31% | +6,05% | -4,70% | +12,96% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 59 | 69,49% | +3,91% | +5,20% | -4,68% | +12,55% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 59 | 69,49% | +3,91% | +5,20% | -4,68% | +12,55% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 53 | 58,49% | +1,34% | +1,01% | -5,36% | +9,23% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 34 | 50,00% | +3,40% | -3,09% | -5,30% | +11,12% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +5,41% | +1,04% | -4,48% | +13,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 49 | 71,43% | +7,60% | +6,31% | -4,39% | +18,27% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 52 | 75,00% | +8,06% | +8,93% | -4,46% | +18,53% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 52 | 75,00% | +8,06% | +8,93% | -4,46% | +18,53% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 46 | 58,70% | +5,33% | -2,46% | -5,24% | +14,56% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 31 | 48,39% | +5,15% | -7,22% | -4,78% | +14,11% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +6,66% | -0,06% | -3,62% | +19,12% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 42 | 80,95% | +13,46% | +8,15% | -3,84% | +27,36% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 44 | 90,91% | +13,84% | +12,80% | -3,87% | +27,94% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 44 | 90,91% | +13,84% | +12,80% | -3,87% | +27,94% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 37 | 48,65% | +11,96% | -7,62% | -4,63% | +25,04% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 29 | 44,83% | +11,07% | -9,81% | -4,41% | +23,21% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 83,33% | +25,05% | +14,50% | -2,20% | +36,41% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 29 | 31,03% | +21,74% | -5,83% | -4,67% | +40,11% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 31 | 48,39% | +21,74% | +1,33% | -4,66% | +40,11% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 31 | 48,39% | +21,74% | +1,33% | -4,66% | +40,11% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 29 | 51,72% | +21,29% | +3,37% | -4,72% | +40,01% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 30 | 0,00% | +21,64% | -21,64% | -4,76% | +40,02% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 21 | 0,00% | +21,59% | -21,59% | -5,03% | +39,52% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +34,37% | +5,85% | -1,27% | +46,88% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 16 | 0,00% | +20,40% | -20,40% | -6,29% | +38,70% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 16 | 0,00% | +20,40% | -20,40% | -6,29% | +38,70% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 16 | 0,00% | +20,40% | -20,40% | -6,29% | +38,70% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 14 | 0,00% | +17,66% | -17,66% | -6,65% | +37,30% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 16 | 0,00% | +20,40% | -20,40% | -6,29% | +38,70% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 15 | 0,00% | +20,77% | -20,77% | -6,17% | +38,93% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +42,81% | +42,81% | -1,52% | +51,95% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 61 | 52,46% | +0,49% | +0,39% | -0,23% | +1,35% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 64 | 54,69% | +0,45% | +0,44% | -0,39% | +1,30% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 67 | 53,73% | +0,48% | +0,37% | -0,35% | +1,32% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 61 | 47,54% | +0,47% | +0,01% | -0,43% | +1,28% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 43 | 48,84% | +0,79% | +0,13% | -0,29% | +1,70% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 61 | 47,54% | +1,19% | +1,08% | +0,05% | +2,22% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 64 | 45,31% | +1,04% | +0,67% | -0,24% | +1,89% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 67 | 44,78% | +1,01% | +0,62% | -0,24% | +1,93% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 61 | 40,98% | +0,83% | -0,05% | -0,19% | +1,93% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 43 | 48,84% | +1,00% | +0,44% | -0,14% | +2,00% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 61 | 54,10% | +1,92% | +1,78% | -1,63% | +4,32% | UTILE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 64 | 48,44% | +1,67% | +1,21% | -1,82% | +4,07% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 67 | 47,76% | +1,61% | +1,15% | -1,80% | +4,04% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 61 | 45,90% | +1,20% | -0,26% | -1,84% | +3,54% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 43 | 51,16% | +1,26% | +0,59% | -1,75% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 61 | 57,38% | +3,32% | +3,23% | -2,38% | +6,83% | UTILE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 64 | 53,12% | +2,98% | +2,13% | -2,56% | +6,48% | UTILE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 67 | 52,24% | +2,88% | +2,01% | -2,53% | +6,37% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 61 | 45,90% | +2,55% | -0,59% | -2,61% | +5,87% | UTILE |
| SOL | 5g | Classic technical | CALIBRABILE | 43 | 53,49% | +1,81% | +0,92% | -2,55% | +5,09% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 60 | 61,67% | +4,45% | +4,54% | -2,92% | +8,48% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 62 | 58,06% | +3,83% | +2,81% | -3,15% | +7,90% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 65 | 58,46% | +3,65% | +2,69% | -3,13% | +7,71% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 60 | 40,00% | +3,00% | -1,18% | -3,19% | +7,12% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 42 | 47,62% | +1,36% | +1,40% | -3,24% | +5,52% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 57 | 64,91% | +5,89% | +6,03% | -3,20% | +10,36% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 59 | 61,02% | +5,23% | +4,46% | -3,50% | +9,54% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 62 | 59,68% | +4,97% | +4,25% | -3,50% | +9,27% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 59 | 47,46% | +4,13% | -1,57% | -3,64% | +8,59% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 42 | 54,76% | +1,60% | +1,69% | -3,81% | +6,40% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |

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
