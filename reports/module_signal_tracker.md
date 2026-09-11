# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-11 05:33 UTC

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

Segnali totali salvati: **189**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-11 | BTC | 77.053,66 | +5 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-11 | DOGE | 0.08388 | -6 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-11 | SOL | 99,59 | +2 | +2 | +2 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-10 | BTC | 78.479,28 | +6 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-10 | DOGE | 0.08593 | -4 | -2 | -2 | 0 | -1 | 0 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-10 | SOL | 102,04 | +5 | +2 | +2 | 0 | +2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-09 | BTC | 78.978,35 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-09 | DOGE | 0.09017 | +3 | -1 | -1 | 0 | +3 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-09 | SOL | 104,26 | +5 | +2 | +2 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-08 | BTC | 78.724,26 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-08 | DOGE | 0.09002 | +3 | -2 | -2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-08 | SOL | 103,26 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63 | 62 | 61 | 60 | 58 | 56 | 53 | 49 | 42 | 34 | 20 | 5 |
| SOL | 63 | 62 | 61 | 60 | 58 | 56 | 53 | 49 | 42 | 34 | 20 | 5 |
| DOGE | 63 | 62 | 61 | 60 | 58 | 56 | 53 | 49 | 42 | 34 | 20 | 5 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-14 | 60g | 2026-09-12 | domani |
| SOL | 2026-07-14 | 60g | 2026-09-12 | domani |
| DOGE | 2026-07-14 | 60g | 2026-09-12 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 59 | 49,15% | +0,36% | +0,34% | PRIMA CALIBRAZIONE |
| BTC | 2g | 58 | 50,00% | +0,65% | +0,56% | PRIMA CALIBRAZIONE |
| BTC | 3g | 57 | 45,61% | +0,84% | +0,72% | PRIMA CALIBRAZIONE |
| BTC | 5g | 55 | 45,45% | +1,75% | +1,51% | PRIMA CALIBRAZIONE |
| BTC | 7g | 53 | 54,72% | +2,48% | +2,28% | PRIMA CALIBRAZIONE |
| BTC | 10g | 50 | 62,00% | +3,51% | +3,32% | PRIMA CALIBRAZIONE |
| BTC | 14g | 46 | 60,87% | +5,40% | +5,33% | PRIMA CALIBRAZIONE |
| BTC | 21g | 39 | 64,10% | +10,41% | +10,24% | PRIMA CALIBRAZIONE |
| BTC | 30g | 32 | 90,62% | +14,16% | +12,82% | PRIMA CALIBRAZIONE |
| BTC | 45g | 18 | 83,33% | +22,36% | +15,00% | FEEDBACK RAPIDO |
| BTC | 60g | 5 | 100,00% | +23,72% | +23,72% | FEEDBACK RAPIDO |
| SOL | 1g | 55 | 52,73% | +0,55% | +0,43% | PRIMA CALIBRAZIONE |
| SOL | 2g | 54 | 50,00% | +1,14% | +1,01% | PRIMA CALIBRAZIONE |
| SOL | 3g | 53 | 56,60% | +1,88% | +1,71% | PRIMA CALIBRAZIONE |
| SOL | 5g | 51 | 60,78% | +3,27% | +3,16% | PRIMA CALIBRAZIONE |
| SOL | 7g | 49 | 65,31% | +4,63% | +4,74% | PRIMA CALIBRAZIONE |
| SOL | 10g | 46 | 65,22% | +6,45% | +6,61% | PRIMA CALIBRAZIONE |
| SOL | 14g | 42 | 78,57% | +9,91% | +10,78% | PRIMA CALIBRAZIONE |
| SOL | 21g | 35 | 77,14% | +17,24% | +16,23% | PRIMA CALIBRAZIONE |
| SOL | 30g | 27 | 62,96% | +20,35% | +13,02% | FEEDBACK RAPIDO |
| SOL | 45g | 15 | 40,00% | +33,36% | -7,93% | FEEDBACK RAPIDO |
| SOL | 60g | 4 | 50,00% | +33,28% | +1,37% | FEEDBACK RAPIDO |
| DOGE | 1g | 58 | 44,83% | +0,37% | +0,08% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 57 | 43,86% | +0,78% | +0,16% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 56 | 39,29% | +1,24% | +0,49% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 54 | 48,15% | +2,20% | +1,58% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 52 | 59,62% | +2,79% | +3,09% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 49 | 57,14% | +2,91% | +3,94% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 46 | 69,57% | +4,99% | +7,03% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 40 | 80,00% | +9,86% | +8,87% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 32 | 75,00% | +12,74% | +5,77% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 19 | 10,53% | +20,45% | -15,96% | FEEDBACK RAPIDO |
| DOGE | 60g | 5 | 0,00% | +20,35% | -20,35% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 59 | 49,15% | +0,36% | +0,34% | -0,10% | +0,89% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 62 | 51,61% | +0,34% | +0,34% | -0,11% | +0,86% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 62 | 51,61% | +0,34% | +0,34% | -0,11% | +0,86% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 57 | 38,60% | +0,45% | +0,09% | -0,01% | +0,97% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,81% | +0,37% | +0,13% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 58 | 50,00% | +0,65% | +0,56% | +0,06% | +1,32% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 61 | 52,46% | +0,74% | +0,74% | +0,16% | +1,41% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 61 | 52,46% | +0,74% | +0,74% | +0,16% | +1,41% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 56 | 42,86% | +0,90% | +0,16% | +0,32% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,18% | +0,55% | +0,59% | +1,89% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 57 | 45,61% | +0,84% | +0,72% | -1,03% | +2,55% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 60 | 53,33% | +1,12% | +1,12% | -1,01% | +2,76% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 60 | 53,33% | +1,12% | +1,12% | -1,01% | +2,76% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 55 | 36,36% | +1,41% | -0,13% | -0,85% | +3,01% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,81% | +0,20% | -0,58% | +3,31% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 55 | 45,45% | +1,75% | +1,51% | -1,58% | +4,03% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 58 | 51,72% | +1,99% | +1,99% | -1,55% | +4,32% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 58 | 51,72% | +1,99% | +1,99% | -1,55% | +4,32% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 53 | 43,40% | +2,28% | -0,92% | -1,38% | +4,66% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 24 | 50,00% | +3,70% | -1,14% | -1,03% | +5,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 53 | 54,72% | +2,48% | +2,28% | -1,81% | +5,27% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 56 | 60,71% | +2,79% | +2,79% | -1,78% | +5,56% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 56 | 60,71% | +2,79% | +2,79% | -1,78% | +5,56% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 51 | 43,14% | +3,29% | -1,71% | -1,59% | +5,99% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 24 | 45,83% | +4,87% | -2,81% | -1,33% | +8,02% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | -0,70% | -0,70% | -2,63% | +2,73% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 50 | 62,00% | +3,51% | +3,32% | -2,03% | +6,43% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 53 | 66,04% | +3,68% | +3,68% | -2,03% | +6,67% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 53 | 66,04% | +3,68% | +3,68% | -2,03% | +6,67% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 48 | 47,92% | +4,18% | -1,36% | -1,81% | +7,24% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 21 | 57,14% | +6,18% | -3,87% | -1,39% | +9,51% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 46 | 60,87% | +5,40% | +5,33% | -2,16% | +8,85% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 49 | 61,22% | +5,49% | +5,49% | -2,16% | +8,96% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 49 | 61,22% | +5,49% | +5,49% | -2,16% | +8,96% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 44 | 56,82% | +6,25% | +0,75% | -1,90% | +9,79% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 17 | 41,18% | +7,22% | -4,34% | -1,20% | +11,14% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 39 | 64,10% | +10,41% | +10,24% | -2,11% | +14,18% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 42 | 71,43% | +10,16% | +10,16% | -2,13% | +13,96% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 42 | 71,43% | +10,16% | +10,16% | -2,13% | +13,96% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 37 | 37,84% | +11,32% | -0,99% | -1,82% | +15,19% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 10 | 20,00% | +17,02% | -13,93% | -0,10% | +20,53% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 32 | 90,62% | +14,16% | +12,82% | -2,96% | +18,17% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 34 | 85,29% | +13,80% | +13,80% | -3,00% | +17,88% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 34 | 85,29% | +13,80% | +13,80% | -3,00% | +17,88% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 30 | 86,67% | +15,02% | +15,02% | -2,80% | +19,32% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 29 | 44,83% | +13,99% | -1,57% | -2,74% | +18,41% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 18 | 83,33% | +22,36% | +15,00% | -3,23% | +26,68% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 20 | 100,00% | +22,42% | +22,42% | -3,27% | +26,67% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 20 | 100,00% | +22,42% | +22,42% | -3,27% | +26,67% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 16 | 100,00% | +22,75% | +22,75% | -2,97% | +27,04% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 16 | 31,25% | +22,74% | -8,73% | -2,90% | +27,16% | FEEDBACK RAPIDO |
| BTC | 45g | Classic technical | CALIBRABILE | 1 | 0,00% | +21,57% | -21,57% | -1,82% | +29,79% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 5 | 100,00% | +23,72% | +23,72% | -2,65% | +29,47% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 5 | 100,00% | +23,72% | +23,72% | -2,65% | +29,47% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 5 | 100,00% | +23,72% | +23,72% | -2,65% | +29,47% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 5 | 100,00% | +23,72% | +23,72% | -2,65% | +29,47% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 4 | 50,00% | +23,83% | -0,95% | -2,49% | +29,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 58 | 44,83% | +0,37% | +0,08% | -0,30% | +1,35% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 61 | 59,02% | +0,26% | +0,53% | -0,42% | +1,18% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 61 | 59,02% | +0,26% | +0,53% | -0,42% | +1,18% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 55 | 52,73% | +0,17% | +0,41% | -0,54% | +1,07% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,22% | -0,49% | -0,44% | +0,96% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 57 | 43,86% | +0,78% | +0,16% | -0,03% | +2,05% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 60 | 56,67% | +0,58% | +0,86% | -0,21% | +1,76% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 60 | 56,67% | +0,58% | +0,86% | -0,21% | +1,76% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 54 | 53,70% | +0,19% | +0,53% | -0,59% | +1,35% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,45% | -1,26% | -0,31% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,90% | +2,61% | +2,02% | +4,90% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 56 | 39,29% | +1,24% | +0,49% | -1,70% | +4,27% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 59 | 54,24% | +1,04% | +1,16% | -1,85% | +3,89% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 59 | 54,24% | +1,04% | +1,16% | -1,85% | +3,89% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 53 | 45,28% | +0,22% | +0,54% | -2,13% | +2,98% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 34 | 29,41% | +0,82% | -2,31% | -2,19% | +3,95% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,49% | +2,26% | -0,95% | +6,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 54 | 48,15% | +2,20% | +1,58% | -2,53% | +6,61% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 57 | 49,12% | +2,04% | +1,87% | -2,62% | +6,32% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 57 | 49,12% | +2,04% | +1,87% | -2,62% | +6,32% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 51 | 58,82% | +0,99% | +0,74% | -3,06% | +5,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 32 | 37,50% | +2,16% | -4,10% | -2,90% | +6,52% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | +0,52% | +0,34% | -2,37% | +7,26% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 52 | 59,62% | +2,79% | +3,09% | -2,94% | +8,55% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 55 | 54,55% | +2,81% | +2,49% | -3,02% | +8,30% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 55 | 54,55% | +2,81% | +2,49% | -3,02% | +8,30% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 49 | 59,18% | +1,48% | +1,50% | -3,56% | +6,91% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +0,41% | +0,28% | -2,23% | +8,54% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 49 | 57,14% | +2,91% | +3,94% | -3,63% | +9,74% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 52 | 51,92% | +2,83% | +3,11% | -3,67% | +9,55% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 52 | 51,92% | +2,83% | +3,11% | -3,67% | +9,55% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 46 | 65,22% | +0,91% | +1,74% | -4,33% | +7,27% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +0,72% | +0,35% | -3,12% | +9,19% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 46 | 69,57% | +4,99% | +7,03% | -3,97% | +13,31% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 48 | 72,92% | +4,53% | +6,67% | -4,01% | +12,78% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 48 | 72,92% | +4,53% | +6,67% | -4,01% | +12,78% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 42 | 61,90% | +1,37% | +0,96% | -4,79% | +8,62% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 31 | 48,39% | +3,26% | -3,87% | -4,53% | +11,11% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +7,65% | +2,04% | -2,99% | +15,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 40 | 80,00% | +9,86% | +8,87% | -3,21% | +20,44% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 42 | 88,10% | +9,88% | +12,69% | -3,27% | +20,49% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 42 | 88,10% | +9,88% | +12,69% | -3,27% | +20,49% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 35 | 65,71% | +7,10% | -3,14% | -3,95% | +15,94% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 27 | 55,56% | +7,10% | -7,10% | -3,69% | +15,72% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +13,05% | +2,29% | +0,50% | +27,01% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 32 | 75,00% | +12,74% | +5,77% | -4,35% | +25,08% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 34 | 88,24% | +13,27% | +11,92% | -4,36% | +25,97% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 34 | 88,24% | +13,27% | +11,92% | -4,36% | +25,97% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 32 | 93,75% | +12,35% | +14,42% | -4,40% | +25,26% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 30 | 40,00% | +11,60% | -11,60% | -4,76% | +23,68% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 22 | 50,00% | +9,38% | -9,38% | -4,86% | +19,29% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +30,85% | +15,03% | -1,31% | +42,05% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 19 | 10,53% | +20,45% | -15,96% | -5,95% | +37,92% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 20 | 20,00% | +20,33% | -11,31% | -5,99% | +37,88% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 20 | 20,00% | +20,33% | -11,31% | -5,99% | +37,88% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 18 | 22,22% | +19,45% | -9,43% | -6,24% | +37,47% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 20 | 0,00% | +20,33% | -20,33% | -5,99% | +37,88% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 17 | 0,00% | +20,63% | -20,63% | -5,74% | +38,18% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 5 | 0,00% | +20,35% | -20,35% | -7,07% | +36,68% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 5 | 0,00% | +20,35% | -20,35% | -7,07% | +36,68% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 5 | 0,00% | +20,35% | -20,35% | -7,07% | +36,68% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 5 | 0,00% | +20,35% | -20,35% | -7,07% | +36,68% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 5 | 0,00% | +20,35% | -20,35% | -7,07% | +36,68% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 5 | 0,00% | +20,35% | -20,35% | -7,07% | +36,68% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 55 | 52,73% | +0,55% | +0,43% | -0,18% | +1,42% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 57 | 54,39% | +0,27% | +0,26% | -0,39% | +1,13% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 60 | 53,33% | +0,31% | +0,19% | -0,35% | +1,16% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 59 | 49,15% | +0,27% | +0,25% | -0,43% | +1,09% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,49% | +0,45% | -0,33% | +1,40% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 54 | 50,00% | +1,14% | +1,01% | +0,19% | +2,20% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 56 | 46,43% | +0,79% | +0,36% | -0,17% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 59 | 45,76% | +0,77% | +0,32% | -0,17% | +1,66% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 58 | 43,10% | +0,70% | +0,17% | -0,20% | +1,76% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,75% | +0,73% | -0,18% | +1,69% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 53 | 56,60% | +1,88% | +1,71% | -1,42% | +4,20% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 55 | 49,09% | +1,41% | +0,88% | -1,71% | +3,72% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 58 | 48,28% | +1,35% | +0,81% | -1,68% | +3,71% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 57 | 49,12% | +1,21% | +0,06% | -1,75% | +3,45% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 41 | 53,66% | +1,10% | +0,96% | -1,74% | +3,38% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 51 | 60,78% | +3,27% | +3,16% | -2,04% | +6,69% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 53 | 54,72% | +2,62% | +1,60% | -2,33% | +6,03% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 56 | 53,57% | +2,52% | +1,47% | -2,32% | +5,92% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 55 | 49,09% | +2,52% | -0,38% | -2,47% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 39 | 58,97% | +1,79% | +1,65% | -2,43% | +5,03% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 49 | 65,31% | +4,63% | +4,74% | -2,39% | +8,60% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 51 | 60,78% | +3,88% | +2,63% | -2,70% | +7,89% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 54 | 61,11% | +3,66% | +2,49% | -2,70% | +7,67% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 53 | 43,40% | +3,61% | -1,12% | -2,86% | +7,60% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 37 | 54,05% | +2,03% | +2,08% | -2,89% | +6,02% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 46 | 65,22% | +6,45% | +6,61% | -2,71% | +10,85% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 48 | 60,42% | +5,61% | +4,66% | -3,09% | +9,82% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 51 | 58,82% | +5,27% | +4,40% | -3,11% | +9,47% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 50 | 46,00% | +4,69% | -2,04% | -3,31% | +9,05% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 34 | 55,88% | +1,97% | +2,07% | -3,43% | +6,65% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 42 | 78,57% | +9,91% | +10,78% | -2,71% | +15,67% | PRIMA CALIBRAZIONE |

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
