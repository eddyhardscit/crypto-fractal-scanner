# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-04 05:32 UTC

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

Segnali totali salvati: **168**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-04 | BTC | 80.963,98 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-04 | DOGE | 0.08695 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-04 | SOL | 103,67 | +6 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-03 | BTC | 77.295,19 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-03 | DOGE | 0.08235 | -1 | -2 | -2 | 0 | +1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-03 | SOL | 100,15 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-02 | BTC | 77.662,37 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-02 | DOGE | 0.08189 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-02 | SOL | 100,25 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-01 | BTC | 79.026,52 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-01 | DOGE | 0.08350 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-01 | SOL | 104,07 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 56 | 55 | 54 | 53 | 51 | 49 | 46 | 42 | 35 | 28 | 13 | 0 |
| SOL | 56 | 55 | 54 | 53 | 51 | 49 | 46 | 42 | 35 | 28 | 13 | 0 |
| DOGE | 56 | 55 | 54 | 53 | 51 | 49 | 46 | 42 | 35 | 28 | 13 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-22 | 45g | 2026-09-05 | domani |
| SOL | 2026-07-22 | 45g | 2026-09-05 | domani |
| DOGE | 2026-07-22 | 45g | 2026-09-05 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 52 | 51,92% | +0,50% | +0,48% | PRIMA CALIBRAZIONE |
| BTC | 2g | 51 | 52,94% | +0,80% | +0,71% | PRIMA CALIBRAZIONE |
| BTC | 3g | 50 | 48,00% | +0,99% | +0,85% | PRIMA CALIBRAZIONE |
| BTC | 5g | 48 | 43,75% | +1,99% | +1,73% | PRIMA CALIBRAZIONE |
| BTC | 7g | 46 | 52,17% | +2,75% | +2,51% | PRIMA CALIBRAZIONE |
| BTC | 10g | 43 | 58,14% | +4,01% | +3,79% | PRIMA CALIBRAZIONE |
| BTC | 14g | 39 | 64,10% | +6,23% | +6,14% | PRIMA CALIBRAZIONE |
| BTC | 21g | 33 | 57,58% | +8,75% | +8,55% | PRIMA CALIBRAZIONE |
| BTC | 30g | 26 | 88,46% | +12,19% | +10,54% | FEEDBACK RAPIDO |
| BTC | 45g | 12 | 83,33% | +22,74% | +15,31% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 48 | 56,25% | +0,71% | +0,58% | PRIMA CALIBRAZIONE |
| SOL | 2g | 47 | 51,06% | +1,35% | +1,20% | PRIMA CALIBRAZIONE |
| SOL | 3g | 46 | 56,52% | +2,12% | +1,93% | PRIMA CALIBRAZIONE |
| SOL | 5g | 44 | 61,36% | +3,70% | +3,57% | PRIMA CALIBRAZIONE |
| SOL | 7g | 42 | 66,67% | +5,33% | +5,45% | PRIMA CALIBRAZIONE |
| SOL | 10g | 39 | 71,79% | +7,52% | +7,72% | PRIMA CALIBRAZIONE |
| SOL | 14g | 35 | 77,14% | +10,78% | +11,82% | PRIMA CALIBRAZIONE |
| SOL | 21g | 28 | 71,43% | +13,70% | +12,43% | FEEDBACK RAPIDO |
| SOL | 30g | 21 | 52,38% | +15,09% | +5,68% | FEEDBACK RAPIDO |
| SOL | 45g | 12 | 33,33% | +32,98% | -13,41% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 51 | 45,10% | +0,48% | +0,24% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 50 | 50,00% | +0,86% | +0,71% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 49 | 44,90% | +1,19% | +1,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 48 | 54,17% | +1,96% | +2,61% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 46 | 60,87% | +2,58% | +3,74% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 44 | 59,09% | +2,87% | +4,29% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 40 | 72,50% | +5,89% | +8,21% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 33 | 75,76% | +7,22% | +6,02% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 26 | 69,23% | +9,39% | +0,81% | FEEDBACK RAPIDO |
| DOGE | 45g | 13 | 0,00% | +18,68% | -18,68% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 52 | 51,92% | +0,50% | +0,48% | +0,04% | +1,06% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 55 | 54,55% | +0,47% | +0,47% | +0,02% | +1,01% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 55 | 54,55% | +0,47% | +0,47% | +0,02% | +1,01% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 50 | 40,00% | +0,61% | +0,20% | +0,14% | +1,16% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 23 | 39,13% | +0,92% | +0,46% | +0,22% | +1,45% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 51 | 52,94% | +0,80% | +0,71% | +0,21% | +1,47% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 54 | 55,56% | +0,90% | +0,90% | +0,32% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 54 | 55,56% | +0,90% | +0,90% | +0,32% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 49 | 44,90% | +1,09% | +0,25% | +0,51% | +1,76% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 22 | 40,91% | +1,21% | +0,52% | +0,63% | +1,86% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 50 | 48,00% | +0,99% | +0,85% | -0,98% | +2,64% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 53 | 56,60% | +1,30% | +1,30% | -0,96% | +2,88% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 53 | 56,60% | +1,30% | +1,30% | -0,96% | +2,88% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 48 | 37,50% | +1,65% | -0,11% | -0,77% | +3,18% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,85% | +0,02% | -0,61% | +3,28% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 48 | 43,75% | +1,99% | +1,73% | -1,51% | +4,15% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 51 | 50,98% | +2,25% | +2,25% | -1,48% | +4,48% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 51 | 50,98% | +2,25% | +2,25% | -1,48% | +4,48% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 46 | 41,30% | +2,62% | -1,07% | -1,26% | +4,89% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 19 | 42,11% | +4,39% | -1,73% | -0,88% | +6,44% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 46 | 52,17% | +2,75% | +2,51% | -1,73% | +5,39% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 49 | 59,18% | +3,09% | +3,09% | -1,71% | +5,71% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 49 | 59,18% | +3,09% | +3,09% | -1,71% | +5,71% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 44 | 38,64% | +3,69% | -2,10% | -1,48% | +6,23% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 17 | 35,29% | +6,57% | -4,27% | -0,94% | +9,46% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 43 | 58,14% | +4,01% | +3,79% | -1,87% | +6,72% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 46 | 63,04% | +4,17% | +4,17% | -1,88% | +6,98% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 46 | 63,04% | +4,17% | +4,17% | -1,88% | +6,98% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 41 | 41,46% | +4,82% | -1,67% | -1,60% | +7,68% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 14 | 42,86% | +9,05% | -6,02% | -0,58% | +11,93% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 39 | 64,10% | +6,23% | +6,14% | -2,05% | +9,54% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 42 | 64,29% | +6,27% | +6,27% | -2,06% | +9,62% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 42 | 64,29% | +6,27% | +6,27% | -2,06% | +9,62% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 37 | 59,46% | +7,29% | +0,74% | -1,74% | +10,69% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 10 | 40,00% | +11,72% | -7,93% | -0,10% | +15,43% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 33 | 57,58% | +8,75% | +8,55% | -2,87% | +12,32% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 35 | 65,71% | +8,19% | +8,19% | -2,92% | +11,76% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 35 | 65,71% | +8,19% | +8,19% | -2,92% | +11,76% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 31 | 70,97% | +9,42% | +9,42% | -2,71% | +12,97% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 30 | 36,67% | +9,29% | +0,89% | -2,66% | +12,92% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 5 | 0,00% | +15,15% | -15,15% | -1,27% | +17,36% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 26 | 88,46% | +12,19% | +10,54% | -2,89% | +16,05% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 28 | 82,14% | +11,90% | +11,90% | -2,94% | +15,85% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 28 | 82,14% | +11,90% | +11,90% | -2,94% | +15,85% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 24 | 83,33% | +13,09% | +13,09% | -2,68% | +17,31% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 23 | 30,43% | +11,72% | -7,90% | -2,61% | +16,07% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 12 | 83,33% | +22,74% | +15,31% | -2,86% | +26,54% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 13 | 100,00% | +22,82% | +22,82% | -2,84% | +26,60% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 13 | 100,00% | +22,82% | +22,82% | -2,84% | +26,60% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 10 | 100,00% | +23,26% | +23,26% | -2,50% | +26,92% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 11 | 36,36% | +22,95% | -6,68% | -2,60% | +27,01% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 51 | 45,10% | +0,48% | +0,24% | -0,15% | +1,51% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 54 | 57,41% | +0,36% | +0,54% | -0,29% | +1,31% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 54 | 57,41% | +0,36% | +0,54% | -0,29% | +1,31% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 48 | 54,17% | +0,26% | +0,44% | -0,41% | +1,20% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 31 | 41,94% | +0,27% | -0,51% | -0,38% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +2,48% | +2,09% | +0,94% | +3,13% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 50 | 50,00% | +0,86% | +0,71% | +0,09% | +2,15% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 53 | 56,60% | +0,63% | +1,00% | -0,12% | +1,83% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 53 | 56,60% | +0,63% | +1,00% | -0,12% | +1,83% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 47 | 55,32% | +0,19% | +0,58% | -0,54% | +1,36% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +3,38% | +3,05% | +2,44% | +5,44% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 49 | 44,90% | +1,19% | +1,30% | -1,66% | +4,05% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 52 | 55,77% | +0,96% | +1,54% | -1,83% | +3,64% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 52 | 55,77% | +0,96% | +1,54% | -1,83% | +3,64% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 46 | 43,48% | +0,00% | +0,37% | -2,15% | +2,55% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 31 | 32,26% | +1,30% | -2,13% | -1,89% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +2,90% | +2,64% | -0,79% | +6,76% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 48 | 54,17% | +1,96% | +2,61% | -2,54% | +6,28% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 50 | 54,00% | +1,76% | +2,70% | -2,63% | +5,92% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 50 | 54,00% | +1,76% | +2,70% | -2,63% | +5,92% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 44 | 54,55% | +0,51% | +0,22% | -3,15% | +4,68% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | +1,54% | +1,34% | -1,56% | +8,05% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 46 | 60,87% | +2,58% | +3,74% | -2,92% | +8,27% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 48 | 60,42% | +2,48% | +3,59% | -3,01% | +7,90% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 48 | 60,42% | +2,48% | +3,59% | -3,01% | +7,90% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 42 | 54,76% | +0,88% | +0,91% | -3,64% | +6,22% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | +0,39% | +0,24% | -1,74% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 44 | 59,09% | +2,87% | +4,29% | -3,37% | +9,83% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 46 | 58,70% | +2,67% | +4,05% | -3,42% | +9,45% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 46 | 58,70% | +2,67% | +4,05% | -3,42% | +9,45% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 39 | 61,54% | +0,48% | +1,45% | -4,06% | +6,89% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,00% | -0,43% | -2,75% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 40 | 72,50% | +5,89% | +8,21% | -3,00% | +14,57% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 42 | 76,19% | +5,51% | +7,74% | -3,07% | +13,93% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 42 | 76,19% | +5,51% | +7,74% | -3,07% | +13,93% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 35 | 68,57% | +1,94% | +1,44% | -3,72% | +9,28% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 27 | 51,85% | +4,09% | -4,09% | -3,41% | +12,32% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +12,07% | +4,21% | +0,53% | +20,35% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 33 | 75,76% | +7,22% | +6,02% | -4,17% | +16,58% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 35 | 85,71% | +7,39% | +10,77% | -4,19% | +16,86% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 35 | 85,71% | +7,39% | +10,77% | -4,19% | +16,86% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 33 | 87,88% | +7,91% | +11,35% | -4,22% | +17,61% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 30 | 63,33% | +5,01% | -5,01% | -4,70% | +12,46% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 23 | 65,22% | +3,23% | -3,23% | -4,58% | +10,96% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,49% | -0,95% | -1,31% | +25,23% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 26 | 69,23% | +9,39% | +0,81% | -5,08% | +20,88% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 28 | 85,71% | +10,27% | +8,63% | -5,04% | +22,25% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 28 | 85,71% | +10,27% | +8,63% | -5,04% | +22,25% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 26 | 92,31% | +8,91% | +11,45% | -5,14% | +21,10% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 28 | 42,86% | +10,27% | -10,27% | -5,04% | +22,25% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 20 | 55,00% | +7,30% | -7,30% | -5,27% | +16,83% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 13 | 0,00% | +18,68% | -18,68% | -6,62% | +36,75% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 13 | 0,00% | +18,68% | -18,68% | -6,62% | +36,75% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 13 | 0,00% | +18,68% | -18,68% | -6,62% | +36,75% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 13 | 0,00% | +18,68% | -18,68% | -6,62% | +36,75% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 13 | 0,00% | +18,68% | -18,68% | -6,62% | +36,75% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 12 | 0,00% | +18,98% | -18,98% | -6,50% | +36,87% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 48 | 56,25% | +0,71% | +0,58% | +0,03% | +1,63% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 50 | 58,00% | +0,39% | +0,37% | -0,22% | +1,28% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 53 | 56,60% | +0,43% | +0,29% | -0,18% | +1,31% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 52 | 51,92% | +0,39% | +0,36% | -0,26% | +1,24% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 36 | 52,78% | +0,61% | +0,57% | -0,16% | +1,57% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 47 | 51,06% | +1,35% | +1,20% | +0,44% | +2,44% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 49 | 46,94% | +0,94% | +0,45% | +0,02% | +1,75% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 52 | 46,15% | +0,90% | +0,40% | +0,01% | +1,80% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 51 | 43,14% | +0,83% | +0,23% | -0,02% | +1,92% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 35 | 51,43% | +0,95% | +0,93% | +0,09% | +1,92% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 46 | 56,52% | +2,12% | +1,93% | -1,34% | +4,37% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 48 | 47,92% | +1,57% | +0,96% | -1,67% | +3,82% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 51 | 47,06% | +1,50% | +0,88% | -1,64% | +3,80% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 50 | 48,00% | +1,34% | +0,03% | -1,73% | +3,51% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 34 | 52,94% | +1,26% | +1,10% | -1,70% | +3,45% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 44 | 61,36% | +3,70% | +3,57% | -1,86% | +7,12% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 46 | 54,35% | +2,93% | +1,75% | -2,21% | +6,35% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 49 | 53,06% | +2,79% | +1,60% | -2,20% | +6,20% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 48 | 47,92% | +2,80% | -0,52% | -2,36% | +6,09% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 32 | 59,38% | +2,05% | +1,87% | -2,26% | +5,26% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 42 | 66,67% | +5,33% | +5,45% | -2,07% | +9,34% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 44 | 61,36% | +4,42% | +2,98% | -2,44% | +8,48% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 47 | 61,70% | +4,13% | +2,79% | -2,46% | +8,19% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 46 | 41,30% | +4,09% | -1,36% | -2,64% | +8,13% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 30 | 53,33% | +2,40% | +2,46% | -2,57% | +6,46% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 39 | 71,79% | +7,52% | +7,72% | -2,27% | +11,88% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 41 | 65,85% | +6,49% | +5,38% | -2,74% | +10,62% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 44 | 63,64% | +6,03% | +5,02% | -2,79% | +10,16% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 43 | 48,84% | +5,37% | -2,45% | -3,01% | +9,70% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 27 | 62,96% | +2,36% | +2,49% | -2,97% | +7,06% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +2,90% | +2,90% | -3,71% | +8,09% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 35 | 77,14% | +10,78% | +11,82% | -2,74% | +16,41% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 37 | 83,78% | +10,09% | +10,26% | -3,14% | +14,92% | PRIMA CALIBRAZIONE |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 40 | 85,00% | +9,10% | +9,72% | -3,19% | +14,09% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 34 | 73,53% | +10,71% | +10,82% | -2,97% | +15,49% | PRIMA CALIBRAZIONE |
| SOL | 14g | Tecnico | CALIBRABILE | 39 | 33,33% | +7,43% | -6,23% | -3,51% | +12,61% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 23 | 43,48% | +2,55% | +0,38% | -3,66% | +6,91% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +10,82% | +10,82% | -3,34% | +16,86% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 28 | 71,43% | +13,70% | +12,43% | -4,67% | +19,58% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 31 | 83,87% | +13,88% | +15,68% | -4,60% | +19,06% | PRIMA CALIBRAZIONE |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 34 | 85,29% | +12,41% | +14,54% | -4,73% | +17,73% | PRIMA CALIBRAZIONE |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 29 | 68,97% | +15,02% | +15,61% | -4,31% | +20,29% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 33 | 36,36% | +10,52% | -11,76% | -4,96% | +15,64% | PRIMA CALIBRAZIONE |
| SOL | 21g | Classic technical | CALIBRABILE | 21 | 38,10% | +11,18% | -11,18% | -4,64% | +15,32% | FEEDBACK RAPIDO |

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
