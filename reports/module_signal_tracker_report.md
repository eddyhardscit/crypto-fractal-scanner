# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-15 05:33 UTC

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

Segnali totali salvati: **201**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-15 | BTC | 77.430,91 | +4 | +3 | +3 | 0 | +1 | -1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-15 | DOGE | 0.08280 | -4 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-15 | SOL | 100,84 | +2 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-14 | BTC | 77.497,87 | +3 | +3 | +3 | 0 | +1 | -1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-14 | DOGE | 0.08404 | -4 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-14 | SOL | 101,01 | +3 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-13 | BTC | 77.274,99 | +6 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-13 | DOGE | 0.08485 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-13 | SOL | 101,86 | +4 | +3 | +3 | 0 | +1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-12 | BTC | 77.204,26 | +3 | +3 | +3 | 0 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-12 | DOGE | 0.08434 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-12 | SOL | 101,54 | +4 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 67 | 66 | 65 | 64 | 62 | 60 | 57 | 53 | 46 | 37 | 24 | 9 |
| SOL | 67 | 66 | 65 | 64 | 62 | 60 | 57 | 53 | 46 | 37 | 24 | 9 |
| DOGE | 67 | 66 | 65 | 64 | 62 | 60 | 57 | 53 | 46 | 37 | 24 | 9 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-18 | 60g | 2026-09-16 | domani |
| SOL | 2026-07-18 | 60g | 2026-09-16 | domani |
| DOGE | 2026-07-18 | 60g | 2026-09-16 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 63 | 50,79% | +0,34% | +0,32% | UTILE |
| BTC | 2g | 62 | 51,61% | +0,59% | +0,52% | UTILE |
| BTC | 3g | 61 | 45,90% | +0,74% | +0,62% | UTILE |
| BTC | 5g | 59 | 42,37% | +1,49% | +1,27% | PRIMA CALIBRAZIONE |
| BTC | 7g | 57 | 50,88% | +2,12% | +1,93% | PRIMA CALIBRAZIONE |
| BTC | 10g | 54 | 57,41% | +3,10% | +2,93% | PRIMA CALIBRAZIONE |
| BTC | 14g | 50 | 56,00% | +4,88% | +4,82% | PRIMA CALIBRAZIONE |
| BTC | 21g | 43 | 65,12% | +9,40% | +9,24% | PRIMA CALIBRAZIONE |
| BTC | 30g | 35 | 91,43% | +14,92% | +13,69% | PRIMA CALIBRAZIONE |
| BTC | 45g | 22 | 86,36% | +22,15% | +16,13% | FEEDBACK RAPIDO |
| BTC | 60g | 9 | 77,78% | +22,72% | +13,23% | FEEDBACK RAPIDO |
| SOL | 1g | 59 | 52,54% | +0,53% | +0,42% | PRIMA CALIBRAZIONE |
| SOL | 2g | 58 | 48,28% | +1,07% | +0,95% | PRIMA CALIBRAZIONE |
| SOL | 3g | 57 | 54,39% | +1,71% | +1,56% | PRIMA CALIBRAZIONE |
| SOL | 5g | 55 | 56,36% | +2,86% | +2,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | 53 | 60,38% | +4,07% | +4,17% | PRIMA CALIBRAZIONE |
| SOL | 10g | 50 | 64,00% | +5,91% | +6,07% | PRIMA CALIBRAZIONE |
| SOL | 14g | 46 | 71,74% | +8,83% | +9,62% | PRIMA CALIBRAZIONE |
| SOL | 21g | 39 | 76,92% | +16,10% | +15,19% | PRIMA CALIBRAZIONE |
| SOL | 30g | 30 | 66,67% | +21,74% | +15,15% | PRIMA CALIBRAZIONE |
| SOL | 45g | 18 | 38,89% | +34,08% | -8,68% | FEEDBACK RAPIDO |
| SOL | 60g | 8 | 37,50% | +33,39% | -8,23% | FEEDBACK RAPIDO |
| DOGE | 1g | 62 | 45,16% | +0,32% | +0,10% | UTILE |
| DOGE | 2g | 61 | 45,90% | +0,67% | +0,21% | UTILE |
| DOGE | 3g | 60 | 40,00% | +1,00% | +0,40% | UTILE |
| DOGE | 5g | 58 | 46,55% | +1,66% | +1,20% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 56 | 57,14% | +2,18% | +2,51% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 53 | 56,60% | +2,68% | +3,66% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 49 | 67,35% | +4,65% | +6,59% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 44 | 72,73% | +8,24% | +7,34% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 35 | 77,14% | +13,39% | +7,02% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 23 | 17,39% | +20,35% | -13,04% | FEEDBACK RAPIDO |
| DOGE | 60g | 9 | 0,00% | +18,15% | -18,15% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 63 | 50,79% | +0,34% | +0,32% | -0,11% | +0,87% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 66 | 53,03% | +0,32% | +0,32% | -0,12% | +0,84% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 66 | 53,03% | +0,32% | +0,32% | -0,12% | +0,84% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 61 | 40,98% | +0,43% | +0,09% | -0,03% | +0,94% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 25 | 40,00% | +0,78% | +0,36% | +0,12% | +1,31% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 62 | 51,61% | +0,59% | +0,52% | +0,02% | +1,25% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 65 | 53,85% | +0,68% | +0,68% | +0,11% | +1,34% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 65 | 53,85% | +0,68% | +0,68% | +0,11% | +1,34% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 60 | 45,00% | +0,83% | +0,14% | +0,26% | +1,48% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,18% | +0,55% | +0,59% | +1,89% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 61 | 45,90% | +0,74% | +0,62% | -1,09% | +2,43% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 64 | 53,12% | +1,01% | +1,01% | -1,07% | +2,64% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 64 | 53,12% | +1,01% | +1,01% | -1,07% | +2,64% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 59 | 37,29% | +1,26% | -0,17% | -0,92% | +2,87% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,81% | +0,20% | -0,58% | +3,31% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 59 | 42,37% | +1,49% | +1,27% | -1,71% | +3,82% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 62 | 48,39% | +1,72% | +1,72% | -1,68% | +4,11% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 62 | 48,39% | +1,72% | +1,72% | -1,68% | +4,11% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 57 | 40,35% | +1,97% | -1,00% | -1,52% | +4,40% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 24 | 50,00% | +3,70% | -1,14% | -1,03% | +5,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 57 | 50,88% | +2,12% | +1,93% | -1,97% | +4,96% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 60 | 56,67% | +2,42% | +2,42% | -1,94% | +5,24% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 60 | 56,67% | +2,42% | +2,42% | -1,94% | +5,24% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 55 | 40,00% | +2,85% | -1,79% | -1,77% | +5,61% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 24 | 45,83% | +4,87% | -2,81% | -1,33% | +8,02% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 54 | 57,41% | +3,10% | +2,93% | -2,13% | +6,18% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 57 | 61,40% | +3,28% | +3,28% | -2,12% | +6,41% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 57 | 61,40% | +3,28% | +3,28% | -2,12% | +6,41% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 52 | 44,23% | +3,71% | -1,40% | -1,92% | +6,91% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 24 | 50,00% | +5,20% | -3,59% | -1,59% | +8,77% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | -0,67% | -0,67% | -3,33% | +2,78% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 50 | 56,00% | +4,88% | +4,82% | -2,20% | +8,55% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 53 | 56,60% | +4,99% | +4,99% | -2,20% | +8,68% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 53 | 56,60% | +4,99% | +4,99% | -2,20% | +8,68% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 48 | 52,08% | +5,64% | +0,59% | -1,96% | +9,41% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 21 | 33,33% | +5,64% | -3,72% | -1,46% | +10,00% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 43 | 65,12% | +9,40% | +9,24% | -2,12% | +13,40% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 46 | 71,74% | +9,23% | +9,23% | -2,14% | +13,25% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 46 | 71,74% | +9,23% | +9,23% | -2,14% | +13,25% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 41 | 41,46% | +10,16% | -0,95% | -1,86% | +14,28% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 14 | 35,71% | +12,01% | -10,09% | -0,70% | +16,33% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | -0,54% | -0,54% | -2,98% | +4,64% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 35 | 91,43% | +14,92% | +13,69% | -2,74% | +19,25% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 37 | 86,49% | +14,55% | +14,55% | -2,79% | +18,92% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 37 | 86,49% | +14,55% | +14,55% | -2,79% | +18,92% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 33 | 87,88% | +15,74% | +15,74% | -2,58% | +20,36% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 32 | 40,62% | +14,84% | -3,58% | -2,53% | +19,56% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 7 | 0,00% | +23,60% | -23,60% | -1,07% | +29,43% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 22 | 86,36% | +22,15% | +16,13% | -3,09% | +27,09% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 24 | 100,00% | +22,22% | +22,22% | -3,14% | +27,05% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 24 | 100,00% | +22,22% | +22,22% | -3,14% | +27,05% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 20 | 100,00% | +22,45% | +22,45% | -2,87% | +27,42% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 19 | 26,32% | +22,54% | -10,75% | -2,79% | +27,50% | FEEDBACK RAPIDO |
| BTC | 45g | Classic technical | CALIBRABILE | 3 | 0,00% | +21,72% | -21,72% | -1,93% | +29,65% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 9 | 77,78% | +22,72% | +13,23% | -2,48% | +29,34% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 9 | 100,00% | +22,72% | +22,72% | -2,48% | +29,34% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 9 | 100,00% | +22,72% | +22,72% | -2,48% | +29,34% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 9 | 100,00% | +22,72% | +22,72% | -2,48% | +29,34% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 8 | 37,50% | +22,65% | -6,28% | -2,38% | +29,41% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 62 | 45,16% | +0,32% | +0,10% | -0,35% | +1,28% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 65 | 58,46% | +0,23% | +0,52% | -0,45% | +1,12% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 65 | 58,46% | +0,23% | +0,52% | -0,45% | +1,12% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 59 | 52,54% | +0,13% | +0,40% | -0,57% | +1,01% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 38 | 42,11% | +0,16% | -0,40% | -0,49% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 61 | 45,90% | +0,67% | +0,21% | -0,13% | +1,89% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 64 | 57,81% | +0,49% | +0,86% | -0,29% | +1,63% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 64 | 57,81% | +0,49% | +0,86% | -0,29% | +1,63% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 58 | 55,17% | +0,12% | +0,56% | -0,65% | +1,23% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 37 | 43,24% | +0,37% | -1,12% | -0,40% | +1,30% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,90% | +2,61% | +2,02% | +4,90% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 60 | 40,00% | +1,00% | +0,40% | -1,86% | +3,99% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 63 | 55,56% | +0,82% | +1,24% | -1,99% | +3,65% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 63 | 55,56% | +0,82% | +1,24% | -1,99% | +3,65% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 57 | 45,61% | +0,04% | +0,44% | -2,26% | +2,77% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 36 | 30,56% | +0,73% | -2,13% | -2,19% | +3,80% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,49% | +2,26% | -0,95% | +6,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 58 | 46,55% | +1,66% | +1,20% | -2,86% | +6,20% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 61 | 52,46% | +1,53% | +2,12% | -2,93% | +5,95% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 61 | 52,46% | +1,53% | +2,12% | -2,93% | +5,95% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 55 | 56,36% | +0,51% | +0,40% | -3,37% | +4,96% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,67% | -4,23% | -3,21% | +6,23% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | +0,52% | +0,34% | -2,37% | +7,26% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 56 | 57,14% | +2,18% | +2,51% | -3,26% | +8,13% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 59 | 57,63% | +2,23% | +2,72% | -3,32% | +7,93% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 59 | 57,63% | +2,23% | +2,72% | -3,32% | +7,93% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 53 | 54,72% | +0,93% | +0,95% | -3,85% | +6,60% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,88% | -5,01% | -3,79% | +7,55% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,37% | -0,49% | -2,97% | +7,69% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 53 | 56,60% | +2,68% | +3,66% | -3,54% | +9,85% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 56 | 51,79% | +2,62% | +2,90% | -3,58% | +9,67% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 56 | 51,79% | +2,62% | +2,90% | -3,58% | +9,67% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 50 | 64,00% | +0,82% | +1,59% | -4,18% | +7,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +0,72% | +0,35% | -3,12% | +9,19% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 49 | 67,35% | +4,65% | +6,59% | -4,04% | +13,20% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 52 | 73,08% | +4,17% | +6,17% | -4,05% | +12,73% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 52 | 73,08% | +4,17% | +6,17% | -4,05% | +12,73% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 46 | 58,70% | +1,24% | +0,87% | -4,77% | +8,92% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 31 | 48,39% | +3,26% | -3,87% | -4,53% | +11,11% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +6,58% | +1,67% | -3,33% | +14,96% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 44 | 72,73% | +8,24% | +7,34% | -4,02% | +18,87% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 46 | 80,43% | +8,32% | +10,89% | -4,04% | +18,98% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 46 | 80,43% | +8,32% | +10,89% | -4,04% | +18,98% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 39 | 58,97% | +5,55% | -3,64% | -4,79% | +14,63% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 31 | 48,39% | +5,15% | -7,22% | -4,78% | +14,11% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +7,18% | -0,50% | -3,01% | +20,33% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 35 | 77,14% | +13,39% | +7,02% | -4,03% | +26,65% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 37 | 89,19% | +13,84% | +12,60% | -4,05% | +27,38% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 37 | 89,19% | +13,84% | +12,60% | -4,05% | +27,38% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 35 | 94,29% | +13,03% | +14,92% | -4,07% | +26,81% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 32 | 43,75% | +12,08% | -9,66% | -4,51% | +24,89% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 24 | 45,83% | +10,31% | -10,31% | -4,47% | +21,33% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +30,85% | +15,03% | -1,31% | +42,05% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 23 | 17,39% | +20,35% | -13,04% | -5,42% | +38,74% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 24 | 33,33% | +20,25% | -6,12% | -5,48% | +38,67% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 24 | 33,33% | +20,25% | -6,12% | -5,48% | +38,67% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 22 | 36,36% | +19,52% | -4,11% | -5,63% | +38,41% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 24 | 0,00% | +20,25% | -20,25% | -5,48% | +38,67% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 20 | 0,00% | +20,53% | -20,53% | -5,27% | +38,90% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 9 | 0,00% | +18,15% | -18,15% | -6,87% | +36,98% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 9 | 0,00% | +18,15% | -18,15% | -6,87% | +36,98% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 9 | 0,00% | +18,15% | -18,15% | -6,87% | +36,98% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 9 | 0,00% | +18,15% | -18,15% | -6,87% | +36,98% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 9 | 0,00% | +18,15% | -18,15% | -6,87% | +36,98% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 8 | 0,00% | +18,57% | -18,57% | -6,72% | +37,20% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 59 | 52,54% | +0,53% | +0,42% | -0,18% | +1,41% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 61 | 54,10% | +0,27% | +0,26% | -0,38% | +1,13% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 64 | 53,12% | +0,31% | +0,20% | -0,35% | +1,16% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 60 | 48,33% | +0,26% | +0,23% | -0,46% | +1,06% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,49% | +0,45% | -0,33% | +1,40% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 58 | 48,28% | +1,07% | +0,95% | +0,14% | +2,11% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 60 | 45,00% | +0,74% | +0,34% | -0,19% | +1,55% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 63 | 44,44% | +0,72% | +0,31% | -0,19% | +1,61% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 60 | 41,67% | +0,65% | +0,14% | -0,22% | +1,72% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,75% | +0,73% | -0,18% | +1,69% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 57 | 54,39% | +1,71% | +1,56% | -1,52% | +4,00% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 59 | 47,46% | +1,28% | +0,78% | -1,78% | +3,57% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 62 | 46,77% | +1,23% | +0,73% | -1,75% | +3,56% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 59 | 47,46% | +1,12% | +0,01% | -1,84% | +3,37% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 42 | 52,38% | +1,01% | +0,88% | -1,83% | +3,26% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 55 | 56,36% | +2,86% | +2,76% | -2,25% | +6,32% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 57 | 50,88% | +2,27% | +1,32% | -2,52% | +5,72% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 60 | 50,00% | +2,19% | +1,22% | -2,49% | +5,63% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 59 | 45,76% | +2,19% | -0,51% | -2,63% | +5,53% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 42 | 54,76% | +1,47% | +1,33% | -2,64% | +4,74% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 53 | 60,38% | +4,07% | +4,17% | -2,61% | +8,10% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 55 | 56,36% | +3,39% | +2,24% | -2,89% | +7,45% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 58 | 56,90% | +3,21% | +2,13% | -2,88% | +7,27% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 57 | 40,35% | +3,16% | -1,24% | -3,04% | +7,20% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 41 | 48,78% | +1,56% | +1,61% | -3,14% | +5,62% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 50 | 64,00% | +5,91% | +6,07% | -2,72% | +10,42% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 52 | 59,62% | +5,16% | +4,29% | -3,08% | +9,48% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 55 | 58,18% | +4,87% | +4,06% | -3,10% | +9,18% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 54 | 46,30% | +4,32% | -1,90% | -3,28% | +8,79% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 38 | 55,26% | +1,74% | +1,83% | -3,37% | +6,53% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 46 | 71,74% | +8,83% | +9,62% | -3,02% | +14,59% | PRIMA CALIBRAZIONE |

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
