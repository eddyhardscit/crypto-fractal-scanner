# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-23 05:32 UTC

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

Segnali totali salvati: **213**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-23 | BTC | 86.710,28 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-23 | DOGE | 0.10219 | +2 | -2 | -2 | 0 | +3 | +1 | 0 | STAI ALLA FINESTRA |
| 2026-09-23 | SOL | 118,88 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-22 | BTC | 85.107,65 | +5 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-22 | DOGE | 0.09857 | +2 | -2 | -2 | 0 | +3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-09-22 | SOL | 115,61 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-17 | BTC | 76.325,40 | +2 | +3 | +3 | 0 | 0 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-17 | DOGE | 0.08084 | -6 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-17 | SOL | 99,49 | 0 | +3 | +3 | 0 | -1 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-16 | BTC | 75.786,49 | +2 | +3 | +3 | 0 | 0 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-16 | DOGE | 0.08011 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-16 | SOL | 97,05 | +2 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 71 | 70 | 69 | 69 | 69 | 68 | 65 | 61 | 54 | 45 | 32 | 17 |
| SOL | 71 | 70 | 69 | 69 | 69 | 68 | 65 | 61 | 54 | 45 | 32 | 17 |
| DOGE | 71 | 70 | 69 | 69 | 69 | 68 | 65 | 61 | 54 | 45 | 32 | 17 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-26 | 60g | 2026-09-24 | domani |
| SOL | 2026-07-26 | 60g | 2026-09-24 | domani |
| DOGE | 2026-07-26 | 60g | 2026-09-24 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 67 | 52,24% | +0,42% | +0,40% | UTILE |
| BTC | 2g | 66 | 51,52% | +0,70% | +0,63% | UTILE |
| BTC | 3g | 66 | 46,97% | +0,90% | +0,80% | UTILE |
| BTC | 5g | 66 | 45,45% | +1,86% | +1,67% | UTILE |
| BTC | 7g | 65 | 53,85% | +2,51% | +2,35% | UTILE |
| BTC | 10g | 62 | 59,68% | +3,23% | +3,08% | UTILE |
| BTC | 14g | 58 | 56,90% | +4,63% | +4,57% | PRIMA CALIBRAZIONE |
| BTC | 21g | 51 | 66,67% | +8,53% | +8,40% | PRIMA CALIBRAZIONE |
| BTC | 30g | 42 | 92,86% | +14,93% | +13,90% | PRIMA CALIBRAZIONE |
| BTC | 45g | 30 | 90,00% | +23,48% | +19,07% | PRIMA CALIBRAZIONE |
| BTC | 60g | 15 | 86,67% | +24,03% | +18,33% | FEEDBACK RAPIDO |
| SOL | 1g | 62 | 53,23% | +0,53% | +0,43% | UTILE |
| SOL | 2g | 61 | 47,54% | +1,19% | +1,08% | UTILE |
| SOL | 3g | 61 | 54,10% | +1,92% | +1,78% | UTILE |
| SOL | 5g | 61 | 57,38% | +3,32% | +3,23% | UTILE |
| SOL | 7g | 61 | 62,30% | +4,75% | +4,83% | UTILE |
| SOL | 10g | 58 | 65,52% | +6,08% | +6,21% | PRIMA CALIBRAZIONE |
| SOL | 14g | 54 | 72,22% | +8,52% | +9,19% | PRIMA CALIBRAZIONE |
| SOL | 21g | 47 | 78,72% | +14,62% | +13,87% | PRIMA CALIBRAZIONE |
| SOL | 30g | 38 | 73,68% | +23,38% | +18,18% | PRIMA CALIBRAZIONE |
| SOL | 45g | 25 | 56,00% | +38,13% | +7,34% | FEEDBACK RAPIDO |
| SOL | 60g | 14 | 35,71% | +36,45% | -8,96% | FEEDBACK RAPIDO |
| DOGE | 1g | 66 | 45,45% | +0,45% | +0,06% | UTILE |
| DOGE | 2g | 65 | 46,15% | +0,79% | +0,03% | UTILE |
| DOGE | 3g | 65 | 40,00% | +1,14% | +0,16% | UTILE |
| DOGE | 5g | 65 | 44,62% | +2,23% | +0,32% | UTILE |
| DOGE | 7g | 64 | 51,56% | +2,81% | +0,95% | UTILE |
| DOGE | 10g | 61 | 49,18% | +2,80% | +1,80% | UTILE |
| DOGE | 14g | 57 | 66,67% | +4,47% | +6,18% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 50 | 70,00% | +7,94% | +5,69% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 43 | 81,40% | +13,42% | +8,23% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 30 | 33,33% | +22,55% | -4,09% | PRIMA CALIBRAZIONE |
| DOGE | 60g | 17 | 0,00% | +21,97% | -21,97% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 67 | 52,24% | +0,42% | +0,40% | -0,12% | +0,94% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 70 | 54,29% | +0,40% | +0,40% | -0,13% | +0,91% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 70 | 54,29% | +0,40% | +0,40% | -0,13% | +0,91% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 63 | 41,27% | +0,41% | +0,08% | -0,05% | +0,93% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 28 | 39,29% | +0,86% | +0,16% | +0,02% | +1,38% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 50,00% | +0,17% | +0,17% | -0,29% | +0,65% | FEEDBACK RAPIDO |
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
| BTC | 7g | Global confluence | BENCHMARK | 65 | 53,85% | +2,51% | +2,35% | -2,09% | +5,26% | UTILE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 68 | 58,82% | +2,77% | +2,77% | -2,06% | +5,49% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 68 | 58,82% | +2,77% | +2,77% | -2,06% | +5,49% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 62 | 43,55% | +2,98% | -1,13% | -1,96% | +5,69% | UTILE |
| BTC | 7g | Classic technical | CALIBRABILE | 27 | 40,74% | +5,59% | -3,76% | -1,42% | +8,56% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 62 | 59,68% | +3,23% | +3,08% | -2,41% | +6,18% | UTILE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 65 | 63,08% | +3,38% | +3,38% | -2,40% | +6,39% | UTILE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 65 | 63,08% | +3,38% | +3,38% | -2,40% | +6,39% | UTILE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 60 | 48,33% | +3,76% | -0,68% | -2,25% | +6,82% | UTILE |
| BTC | 10g | Classic technical | CALIBRABILE | 24 | 50,00% | +5,20% | -3,59% | -1,59% | +8,77% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 58 | 56,90% | +4,63% | +4,57% | -2,61% | +8,17% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 61 | 57,38% | +4,73% | +4,73% | -2,59% | +8,30% | UTILE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 61 | 57,38% | +4,73% | +4,73% | -2,59% | +8,30% | UTILE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 56 | 53,57% | +5,27% | +0,94% | -2,42% | +8,89% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 24 | 29,17% | +4,78% | -3,41% | -1,84% | +9,24% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 51 | 66,67% | +8,53% | +8,40% | -2,48% | +12,40% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 54 | 72,22% | +8,44% | +8,44% | -2,48% | +12,33% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 54 | 72,22% | +8,44% | +8,44% | -2,48% | +12,33% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 49 | 46,94% | +9,14% | -0,15% | -2,28% | +13,09% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 22 | 50,00% | +9,06% | -5,00% | -2,06% | +12,94% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | -0,54% | -0,54% | -2,98% | +4,64% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 42 | 92,86% | +14,93% | +13,90% | -2,15% | +19,01% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 45 | 88,89% | +14,71% | +14,71% | -2,17% | +18,96% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 45 | 88,89% | +14,71% | +14,71% | -2,17% | +18,96% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +16,14% | +16,14% | -2,21% | +20,84% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 40 | 47,50% | +14,96% | -1,69% | -1,88% | +19,47% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 13 | 38,46% | +18,78% | -9,63% | -0,70% | +23,30% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,87% | +5,87% | -2,41% | +8,88% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 30 | 90,00% | +23,48% | +19,07% | -2,95% | +28,12% | PRIMA CALIBRAZIONE |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 32 | 100,00% | +23,45% | +23,45% | -3,00% | +28,03% | PRIMA CALIBRAZIONE |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 32 | 100,00% | +23,45% | +23,45% | -3,00% | +28,03% | PRIMA CALIBRAZIONE |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 28 | 100,00% | +23,79% | +23,79% | -2,78% | +28,44% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 27 | 37,04% | +23,90% | -4,53% | -2,73% | +28,53% | FEEDBACK RAPIDO |
| BTC | 45g | Classic technical | CALIBRABILE | 4 | 0,00% | +21,70% | -21,70% | -1,55% | +30,01% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 15 | 86,67% | +24,03% | +18,33% | -3,21% | +29,19% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 17 | 100,00% | +24,08% | +24,08% | -3,26% | +29,37% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 17 | 100,00% | +24,08% | +24,08% | -3,26% | +29,37% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 13 | 100,00% | +24,53% | +24,53% | -2,88% | +30,32% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 14 | 28,57% | +24,25% | -12,34% | -2,94% | +30,04% | FEEDBACK RAPIDO |
| BTC | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 66 | 45,45% | +0,45% | +0,06% | -0,34% | +1,41% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 69 | 56,52% | +0,35% | +0,35% | -0,44% | +1,26% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 69 | 56,52% | +0,35% | +0,35% | -0,44% | +1,26% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 63 | 52,38% | +0,28% | +0,34% | -0,55% | +1,17% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 41 | 41,46% | +0,29% | -0,51% | -0,53% | +1,01% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 11 | 63,64% | +2,82% | +2,53% | +0,75% | +3,68% | FEEDBACK RAPIDO |
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
| DOGE | 7g | Global confluence | BENCHMARK | 64 | 51,56% | +2,81% | +0,95% | -3,68% | +8,71% | UTILE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 67 | 53,73% | +2,82% | +1,53% | -3,71% | +8,50% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 67 | 53,73% | +2,82% | +1,53% | -3,71% | +8,50% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 61 | 49,18% | +1,76% | -0,49% | -4,21% | +7,40% | UTILE |
| DOGE | 7g | Classic technical | CALIBRABILE | 40 | 30,00% | +3,47% | -6,14% | -4,04% | +8,97% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,37% | -0,49% | -2,97% | +7,69% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 61 | 49,18% | +2,80% | +1,80% | -4,40% | +9,92% | UTILE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 64 | 51,56% | +2,74% | +2,09% | -4,39% | +9,76% | UTILE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 64 | 51,56% | +2,74% | +2,09% | -4,39% | +9,76% | UTILE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 58 | 55,17% | +1,20% | -0,09% | -5,00% | +7,97% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 37 | 35,14% | +2,66% | -5,84% | -4,91% | +9,80% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | -0,68% | -1,01% | -4,16% | +8,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 57 | 66,67% | +4,47% | +6,18% | -4,84% | +13,00% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 60 | 68,33% | +4,07% | +4,89% | -4,81% | +12,60% | UTILE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 60 | 68,33% | +4,07% | +4,89% | -4,81% | +12,60% | UTILE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 54 | 59,26% | +1,56% | +1,24% | -5,51% | +9,34% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 34 | 50,00% | +3,40% | -3,09% | -5,30% | +11,12% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +5,41% | +1,04% | -4,48% | +13,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 50 | 70,00% | +7,94% | +5,69% | -4,39% | +18,45% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 53 | 73,58% | +8,37% | +8,30% | -4,45% | +18,70% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 53 | 73,58% | +8,37% | +8,30% | -4,45% | +18,70% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 47 | 59,57% | +5,74% | -1,88% | -5,22% | +14,83% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 31 | 48,39% | +5,15% | -7,22% | -4,78% | +14,11% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +6,66% | -0,06% | -3,62% | +19,12% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 43 | 81,40% | +13,42% | +8,23% | -4,09% | +27,04% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 45 | 91,11% | +13,78% | +12,77% | -4,11% | +27,62% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 45 | 91,11% | +13,78% | +12,77% | -4,11% | +27,62% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 38 | 94,74% | +13,46% | +15,20% | -3,59% | +28,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 38 | 50,00% | +11,94% | -7,12% | -4,89% | +24,74% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 30 | 46,67% | +11,08% | -9,11% | -4,75% | +22,89% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 85,71% | +23,10% | +14,05% | -3,96% | +33,14% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 30 | 33,33% | +22,55% | -4,09% | -4,56% | +40,41% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 32 | 50,00% | +22,50% | +2,73% | -4,56% | +40,39% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 32 | 50,00% | +22,50% | +2,73% | -4,56% | +40,39% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 30 | 53,33% | +22,12% | +4,79% | -4,61% | +40,31% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Tecnico | CALIBRABILE | 30 | 0,00% | +21,64% | -21,64% | -4,76% | +40,02% | PRIMA CALIBRAZIONE |
| DOGE | 45g | Classic technical | CALIBRABILE | 22 | 0,00% | +22,71% | -22,71% | -4,86% | +39,94% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +37,31% | +15,91% | -1,31% | +47,38% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 17 | 0,00% | +21,97% | -21,97% | -6,05% | +39,36% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 17 | 5,88% | +21,97% | -16,43% | -6,05% | +39,36% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 17 | 5,88% | +21,97% | -16,43% | -6,05% | +39,36% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 15 | 6,67% | +19,62% | -13,34% | -6,36% | +38,14% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 17 | 0,00% | +21,97% | -21,97% | -6,05% | +39,36% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 16 | 0,00% | +22,42% | -22,42% | -5,92% | +39,62% | FEEDBACK RAPIDO |
| DOGE | 60g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 62 | 53,23% | +0,53% | +0,43% | -0,19% | +1,39% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 65 | 55,38% | +0,48% | +0,47% | -0,35% | +1,33% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 68 | 54,41% | +0,51% | +0,40% | -0,32% | +1,35% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 62 | 48,39% | +0,51% | +0,06% | -0,39% | +1,32% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 44 | 50,00% | +0,83% | +0,19% | -0,23% | +1,74% | PRIMA CALIBRAZIONE |
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
| SOL | 7g | Global confluence | BENCHMARK | 61 | 62,30% | +4,75% | +4,83% | -2,84% | +8,73% | UTILE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 63 | 58,73% | +4,13% | +3,12% | -3,08% | +8,15% | UTILE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 66 | 59,09% | +3,94% | +2,99% | -3,06% | +7,95% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 60 | 40,00% | +3,00% | -1,18% | -3,19% | +7,12% | UTILE |
| SOL | 7g | Classic technical | CALIBRABILE | 42 | 47,62% | +1,36% | +1,40% | -3,24% | +5,52% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 58 | 65,52% | +6,08% | +6,21% | -3,24% | +10,49% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 60 | 61,67% | +5,42% | +4,66% | -3,53% | +9,67% | UTILE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 63 | 60,32% | +5,16% | +4,45% | -3,53% | +9,40% | UTILE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 60 | 48,33% | +4,34% | -1,26% | -3,67% | +8,74% | UTILE |
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
