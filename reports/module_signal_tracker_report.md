# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-10 05:33 UTC

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

Segnali totali salvati: **186**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-10 | BTC | 78.479,28 | +6 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-10 | DOGE | 0.08593 | -4 | -2 | -2 | 0 | -1 | 0 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-10 | SOL | 102,04 | +5 | +2 | +2 | 0 | +2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-09 | BTC | 78.978,35 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-09 | DOGE | 0.09017 | +3 | -1 | -1 | 0 | +3 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-09 | SOL | 104,26 | +5 | +2 | +2 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-08 | BTC | 78.724,26 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-08 | DOGE | 0.09002 | +3 | -2 | -2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-08 | SOL | 103,26 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-07 | BTC | 79.828,11 | +7 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-07 | DOGE | 0.09027 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | STAI ALLA FINESTRA |
| 2026-09-07 | SOL | 105,55 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62 | 61 | 60 | 59 | 57 | 55 | 52 | 48 | 41 | 34 | 19 | 4 |
| SOL | 62 | 61 | 60 | 59 | 57 | 55 | 52 | 48 | 41 | 34 | 19 | 4 |
| DOGE | 62 | 61 | 60 | 59 | 57 | 55 | 52 | 48 | 41 | 34 | 19 | 4 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-13 | 60g | 2026-09-11 | domani |
| SOL | 2026-07-13 | 60g | 2026-09-11 | domani |
| DOGE | 2026-07-13 | 60g | 2026-09-11 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 58 | 50,00% | +0,39% | +0,37% | PRIMA CALIBRAZIONE |
| BTC | 2g | 57 | 50,88% | +0,70% | +0,62% | PRIMA CALIBRAZIONE |
| BTC | 3g | 56 | 46,43% | +0,89% | +0,77% | PRIMA CALIBRAZIONE |
| BTC | 5g | 54 | 46,30% | +1,84% | +1,61% | PRIMA CALIBRAZIONE |
| BTC | 7g | 52 | 55,77% | +2,62% | +2,42% | PRIMA CALIBRAZIONE |
| BTC | 10g | 49 | 63,27% | +3,63% | +3,44% | PRIMA CALIBRAZIONE |
| BTC | 14g | 45 | 62,22% | +5,60% | +5,52% | PRIMA CALIBRAZIONE |
| BTC | 21g | 38 | 63,16% | +10,62% | +10,44% | PRIMA CALIBRAZIONE |
| BTC | 30g | 32 | 90,62% | +14,16% | +12,82% | PRIMA CALIBRAZIONE |
| BTC | 45g | 17 | 88,24% | +22,40% | +17,15% | FEEDBACK RAPIDO |
| BTC | 60g | 4 | 100,00% | +23,95% | +23,95% | FEEDBACK RAPIDO |
| SOL | 1g | 54 | 53,70% | +0,60% | +0,48% | PRIMA CALIBRAZIONE |
| SOL | 2g | 53 | 50,94% | +1,25% | +1,12% | PRIMA CALIBRAZIONE |
| SOL | 3g | 52 | 57,69% | +1,98% | +1,81% | PRIMA CALIBRAZIONE |
| SOL | 5g | 50 | 62,00% | +3,46% | +3,35% | PRIMA CALIBRAZIONE |
| SOL | 7g | 48 | 66,67% | +4,81% | +4,92% | PRIMA CALIBRAZIONE |
| SOL | 10g | 45 | 66,67% | +6,69% | +6,86% | PRIMA CALIBRAZIONE |
| SOL | 14g | 41 | 80,49% | +10,31% | +11,20% | PRIMA CALIBRAZIONE |
| SOL | 21g | 34 | 76,47% | +17,42% | +16,38% | PRIMA CALIBRAZIONE |
| SOL | 30g | 27 | 62,96% | +20,35% | +13,02% | FEEDBACK RAPIDO |
| SOL | 45g | 14 | 35,71% | +33,18% | -11,07% | FEEDBACK RAPIDO |
| SOL | 60g | 3 | 66,67% | +34,24% | +11,96% | FEEDBACK RAPIDO |
| DOGE | 1g | 57 | 43,86% | +0,41% | +0,04% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 56 | 44,64% | +0,91% | +0,29% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 55 | 40,00% | +1,39% | +0,63% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 53 | 49,06% | +2,39% | +1,75% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 51 | 58,82% | +2,91% | +3,08% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 48 | 58,33% | +2,96% | +4,04% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 46 | 69,57% | +4,99% | +7,03% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 39 | 79,49% | +10,08% | +9,06% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 32 | 75,00% | +12,74% | +5,77% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 18 | 5,56% | +20,48% | -17,95% | FEEDBACK RAPIDO |
| DOGE | 60g | 4 | 0,00% | +21,40% | -21,40% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 58 | 50,00% | +0,39% | +0,37% | -0,06% | +0,94% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 61 | 52,46% | +0,37% | +0,37% | -0,07% | +0,90% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 61 | 52,46% | +0,37% | +0,37% | -0,07% | +0,90% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 56 | 39,29% | +0,49% | +0,12% | +0,03% | +1,02% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,81% | +0,37% | +0,13% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 57 | 50,88% | +0,70% | +0,62% | +0,12% | +1,38% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 60 | 53,33% | +0,79% | +0,79% | +0,22% | +1,47% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 60 | 53,33% | +0,79% | +0,79% | +0,22% | +1,47% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 55 | 43,64% | +0,96% | +0,21% | +0,38% | +1,64% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,18% | +0,55% | +0,59% | +1,89% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 56 | 46,43% | +0,89% | +0,77% | -1,00% | +2,57% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 59 | 54,24% | +1,18% | +1,18% | -0,98% | +2,79% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 59 | 54,24% | +1,18% | +1,18% | -0,98% | +2,79% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 54 | 37,04% | +1,47% | -0,09% | -0,81% | +3,05% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,81% | +0,20% | -0,58% | +3,31% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 54 | 46,30% | +1,84% | +1,61% | -1,54% | +4,09% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 57 | 52,63% | +2,08% | +2,08% | -1,51% | +4,39% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 57 | 52,63% | +2,08% | +2,08% | -1,51% | +4,39% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 52 | 44,23% | +2,39% | -0,87% | -1,32% | +4,74% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 24 | 50,00% | +3,70% | -1,14% | -1,03% | +5,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 25,00% | -0,34% | -0,34% | -1,71% | +2,56% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 52 | 55,77% | +2,62% | +2,42% | -1,73% | +5,39% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 55 | 61,82% | +2,93% | +2,93% | -1,72% | +5,67% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 55 | 61,82% | +2,93% | +2,93% | -1,72% | +5,67% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 50 | 44,00% | +3,45% | -1,65% | -1,51% | +6,12% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 23 | 47,83% | +5,29% | -2,72% | -1,15% | +8,39% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 49 | 63,27% | +3,63% | +3,44% | -2,00% | +6,48% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 52 | 67,31% | +3,79% | +3,79% | -2,00% | +6,72% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 52 | 67,31% | +3,79% | +3,79% | -2,00% | +6,72% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 47 | 48,94% | +4,32% | -1,34% | -1,77% | +7,31% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 20 | 60,00% | +6,61% | -3,94% | -1,28% | +9,78% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 45 | 62,22% | +5,60% | +5,52% | -2,11% | +8,97% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 48 | 62,50% | +5,67% | +5,67% | -2,12% | +9,08% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 48 | 62,50% | +5,67% | +5,67% | -2,12% | +9,08% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 43 | 58,14% | +6,48% | +0,84% | -1,85% | +9,94% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 16 | 43,75% | +7,88% | -4,40% | -1,01% | +11,63% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 38 | 63,16% | +10,62% | +10,44% | -2,18% | +14,30% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 41 | 70,73% | +10,34% | +10,34% | -2,20% | +14,07% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 41 | 70,73% | +10,34% | +10,34% | -2,20% | +14,07% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 36 | 36,11% | +11,56% | -1,09% | -1,89% | +15,35% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 9 | 11,11% | +18,62% | -15,77% | -0,19% | +21,75% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 32 | 90,62% | +14,16% | +12,82% | -2,96% | +18,17% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 34 | 85,29% | +13,80% | +13,80% | -3,00% | +17,88% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 34 | 85,29% | +13,80% | +13,80% | -3,00% | +17,88% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 30 | 86,67% | +15,02% | +15,02% | -2,80% | +19,32% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 29 | 44,83% | +13,99% | -1,57% | -2,74% | +18,41% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 17 | 88,24% | +22,40% | +17,15% | -3,31% | +26,49% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 19 | 100,00% | +22,46% | +22,46% | -3,35% | +26,51% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 19 | 100,00% | +22,46% | +22,46% | -3,35% | +26,51% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 15 | 100,00% | +22,83% | +22,83% | -3,04% | +26,85% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 15 | 33,33% | +22,81% | -7,88% | -2,97% | +26,99% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 4 | 100,00% | +23,95% | +23,95% | -3,09% | +29,06% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | +23,95% | +23,95% | -3,09% | +29,06% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | +23,95% | +23,95% | -3,09% | +29,06% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 4 | 100,00% | +23,95% | +23,95% | -3,09% | +29,06% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 3 | 33,33% | +24,18% | -8,86% | -3,03% | +29,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 57 | 43,86% | +0,41% | +0,04% | -0,25% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 60 | 58,33% | +0,31% | +0,50% | -0,37% | +1,24% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 60 | 58,33% | +0,31% | +0,50% | -0,37% | +1,24% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 54 | 51,85% | +0,21% | +0,37% | -0,48% | +1,13% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,22% | -0,49% | -0,44% | +0,96% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 56 | 44,64% | +0,91% | +0,29% | +0,12% | +2,20% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 59 | 55,93% | +0,71% | +0,76% | -0,08% | +1,91% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 59 | 55,93% | +0,71% | +0,76% | -0,08% | +1,91% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 53 | 54,72% | +0,33% | +0,67% | -0,45% | +1,51% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,45% | -1,26% | -0,31% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,90% | +2,61% | +2,02% | +4,90% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 55 | 40,00% | +1,39% | +0,63% | -1,59% | +4,32% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 58 | 53,45% | +1,17% | +1,07% | -1,75% | +3,93% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 58 | 53,45% | +1,17% | +1,07% | -1,75% | +3,93% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 52 | 46,15% | +0,35% | +0,68% | -2,02% | +3,00% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 33 | 30,30% | +1,05% | -2,17% | -2,02% | +4,02% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,49% | +2,26% | -0,95% | +6,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 53 | 49,06% | +2,39% | +1,75% | -2,41% | +6,72% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 56 | 48,21% | +2,21% | +1,77% | -2,51% | +6,42% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 56 | 48,21% | +2,21% | +1,77% | -2,51% | +6,42% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 50 | 60,00% | +1,17% | +0,91% | -2,95% | +5,39% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | +1,54% | +1,34% | -1,56% | +8,05% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 51 | 58,82% | +2,91% | +3,08% | -2,91% | +8,55% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 54 | 53,70% | +2,92% | +2,47% | -2,99% | +8,30% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 54 | 53,70% | +2,92% | +2,47% | -2,99% | +8,30% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 48 | 60,42% | +1,58% | +1,61% | -3,54% | +6,88% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +0,41% | +0,28% | -2,23% | +8,54% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 48 | 58,33% | +2,96% | +4,04% | -3,63% | +9,67% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 51 | 52,94% | +2,88% | +3,18% | -3,67% | +9,48% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 51 | 52,94% | +2,88% | +3,18% | -3,67% | +9,48% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 45 | 64,44% | +0,92% | +1,77% | -4,34% | +7,15% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +0,72% | +0,35% | -3,12% | +9,19% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 46 | 69,57% | +4,99% | +7,03% | -3,97% | +13,31% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 47 | 72,34% | +4,71% | +6,72% | -3,92% | +12,89% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 47 | 72,34% | +4,71% | +6,72% | -3,92% | +12,89% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 41 | 63,41% | +1,51% | +1,09% | -4,70% | +8,65% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 31 | 48,39% | +3,26% | -3,87% | -4,53% | +11,11% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +7,65% | +2,04% | -2,99% | +15,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 39 | 79,49% | +10,08% | +9,06% | -3,22% | +20,42% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 41 | 87,80% | +10,08% | +12,96% | -3,28% | +20,47% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 41 | 87,80% | +10,08% | +12,96% | -3,28% | +20,47% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 34 | 64,71% | +7,26% | -3,28% | -3,99% | +15,79% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 27 | 55,56% | +7,10% | -7,10% | -3,69% | +15,72% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +13,05% | +2,29% | +0,50% | +27,01% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 32 | 75,00% | +12,74% | +5,77% | -4,35% | +25,08% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 34 | 88,24% | +13,27% | +11,92% | -4,36% | +25,97% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 34 | 88,24% | +13,27% | +11,92% | -4,36% | +25,97% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 32 | 93,75% | +12,35% | +14,42% | -4,40% | +25,26% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 30 | 40,00% | +11,60% | -11,60% | -4,76% | +23,68% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 22 | 50,00% | +9,38% | -9,38% | -4,86% | +19,29% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +30,85% | +15,03% | -1,31% | +42,05% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 18 | 5,56% | +20,48% | -17,95% | -6,13% | +37,64% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 19 | 15,79% | +20,35% | -12,96% | -6,16% | +37,61% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 19 | 15,79% | +20,35% | -12,96% | -6,16% | +37,61% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 17 | 17,65% | +19,42% | -11,16% | -6,44% | +37,15% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 19 | 0,00% | +20,35% | -20,35% | -6,16% | +37,61% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 16 | 0,00% | +20,67% | -20,67% | -5,92% | +37,88% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 4 | 0,00% | +21,40% | -21,40% | -7,38% | +36,23% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 4 | 0,00% | +21,40% | -21,40% | -7,38% | +36,23% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 4 | 0,00% | +21,40% | -21,40% | -7,38% | +36,23% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 4 | 0,00% | +21,40% | -21,40% | -7,38% | +36,23% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 4 | 0,00% | +21,40% | -21,40% | -7,38% | +36,23% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 4 | 0,00% | +21,40% | -21,40% | -7,38% | +36,23% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 54 | 53,70% | +0,60% | +0,48% | -0,12% | +1,49% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 56 | 55,36% | +0,32% | +0,31% | -0,34% | +1,18% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 59 | 54,24% | +0,36% | +0,23% | -0,30% | +1,22% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 58 | 50,00% | +0,32% | +0,30% | -0,38% | +1,15% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,49% | +0,45% | -0,33% | +1,40% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 53 | 50,94% | +1,25% | +1,12% | +0,29% | +2,32% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 55 | 47,27% | +0,88% | +0,44% | -0,08% | +1,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 58 | 46,55% | +0,86% | +0,40% | -0,08% | +1,76% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 57 | 43,86% | +0,79% | +0,25% | -0,11% | +1,86% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 41 | 51,22% | +0,88% | +0,85% | -0,05% | +1,84% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 52 | 57,69% | +1,98% | +1,81% | -1,36% | +4,25% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 54 | 50,00% | +1,50% | +0,96% | -1,65% | +3,76% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 57 | 49,12% | +1,44% | +0,89% | -1,63% | +3,74% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 56 | 50,00% | +1,30% | +0,13% | -1,70% | +3,49% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 40 | 55,00% | +1,21% | +1,08% | -1,67% | +3,42% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 50 | 62,00% | +3,46% | +3,35% | -1,94% | +6,81% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 52 | 55,77% | +2,79% | +1,74% | -2,25% | +6,13% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 55 | 54,55% | +2,68% | +1,61% | -2,23% | +6,01% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 54 | 50,00% | +2,68% | -0,27% | -2,38% | +5,91% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 38 | 60,53% | +2,00% | +1,85% | -2,31% | +5,14% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 48 | 66,67% | +4,81% | +4,92% | -2,34% | +8,71% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 50 | 62,00% | +4,03% | +2,76% | -2,65% | +7,98% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 53 | 62,26% | +3,80% | +2,61% | -2,66% | +7,75% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 52 | 44,23% | +3,76% | -1,07% | -2,82% | +7,68% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 36 | 55,56% | +2,20% | +2,25% | -2,84% | +6,10% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 45 | 66,67% | +6,69% | +6,86% | -2,63% | +11,03% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 47 | 61,70% | +5,83% | +4,85% | -3,03% | +9,96% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 50 | 60,00% | +5,46% | +4,57% | -3,05% | +9,60% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 49 | 46,94% | +4,87% | -1,99% | -3,25% | +9,18% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 33 | 57,58% | +2,16% | +2,27% | -3,34% | +6,77% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 41 | 80,49% | +10,31% | +11,20% | -2,57% | +16,04% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 43 | 81,40% | +9,74% | +8,79% | -2,93% | +14,78% | PRIMA CALIBRAZIONE |

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
