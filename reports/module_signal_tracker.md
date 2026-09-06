# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-06 05:33 UTC

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

Segnali totali salvati: **174**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-06 | BTC | 79.879,48 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-06 | DOGE | 0.09088 | +3 | -2 | -2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-06 | SOL | 105,95 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-05 | BTC | 79.660,00 | +5 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-05 | DOGE | 0.08560 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-05 | SOL | 102,27 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-04 | BTC | 80.963,98 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-04 | DOGE | 0.08695 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-04 | SOL | 103,67 | +6 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-03 | BTC | 77.295,19 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-03 | DOGE | 0.08235 | -1 | -2 | -2 | 0 | +1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-03 | SOL | 100,15 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 58 | 57 | 56 | 55 | 53 | 51 | 48 | 44 | 37 | 30 | 15 | 0 |
| SOL | 58 | 57 | 56 | 55 | 53 | 51 | 48 | 44 | 37 | 30 | 15 | 0 |
| DOGE | 58 | 57 | 56 | 55 | 53 | 51 | 48 | 44 | 37 | 30 | 15 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-09 | 60g | 2026-09-07 | domani |
| SOL | 2026-07-09 | 60g | 2026-09-07 | domani |
| DOGE | 2026-07-09 | 60g | 2026-09-07 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 54 | 51,85% | +0,46% | +0,43% | PRIMA CALIBRAZIONE |
| BTC | 2g | 53 | 52,83% | +0,80% | +0,71% | PRIMA CALIBRAZIONE |
| BTC | 3g | 52 | 50,00% | +1,07% | +0,93% | PRIMA CALIBRAZIONE |
| BTC | 5g | 50 | 46,00% | +1,98% | +1,72% | PRIMA CALIBRAZIONE |
| BTC | 7g | 48 | 54,17% | +2,73% | +2,51% | PRIMA CALIBRAZIONE |
| BTC | 10g | 45 | 60,00% | +3,88% | +3,68% | PRIMA CALIBRAZIONE |
| BTC | 14g | 41 | 65,85% | +6,12% | +6,04% | PRIMA CALIBRAZIONE |
| BTC | 21g | 35 | 60,00% | +9,77% | +9,58% | PRIMA CALIBRAZIONE |
| BTC | 30g | 28 | 89,29% | +13,01% | +11,47% | FEEDBACK RAPIDO |
| BTC | 45g | 14 | 85,71% | +22,52% | +16,15% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 50 | 56,00% | +0,72% | +0,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | 49 | 53,06% | +1,39% | +1,24% | PRIMA CALIBRAZIONE |
| SOL | 3g | 48 | 58,33% | +2,19% | +2,01% | PRIMA CALIBRAZIONE |
| SOL | 5g | 46 | 60,87% | +3,57% | +3,45% | PRIMA CALIBRAZIONE |
| SOL | 7g | 44 | 65,91% | +5,07% | +5,19% | PRIMA CALIBRAZIONE |
| SOL | 10g | 41 | 73,17% | +7,41% | +7,60% | PRIMA CALIBRAZIONE |
| SOL | 14g | 37 | 78,38% | +10,83% | +11,81% | PRIMA CALIBRAZIONE |
| SOL | 21g | 30 | 73,33% | +15,33% | +14,15% | PRIMA CALIBRAZIONE |
| SOL | 30g | 23 | 56,52% | +17,42% | +8,83% | FEEDBACK RAPIDO |
| SOL | 45g | 14 | 35,71% | +33,18% | -11,07% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 53 | 45,28% | +0,55% | +0,15% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 52 | 48,08% | +0,99% | +0,52% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 51 | 43,14% | +1,43% | +0,96% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 49 | 53,06% | +2,10% | +2,38% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 48 | 62,50% | +2,63% | +3,74% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 46 | 56,52% | +2,84% | +3,96% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 42 | 71,43% | +5,50% | +7,71% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 35 | 77,14% | +8,31% | +7,18% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 28 | 71,43% | +10,64% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 45g | 15 | 0,00% | +19,04% | -19,04% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 54 | 51,85% | +0,46% | +0,43% | +0,00% | +1,00% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 57 | 54,39% | +0,43% | +0,43% | -0,01% | +0,96% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 57 | 54,39% | +0,43% | +0,43% | -0,01% | +0,96% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 52 | 40,38% | +0,56% | +0,17% | +0,10% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,81% | +0,37% | +0,13% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | -0,20% | -0,20% | -0,66% | +0,18% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 53 | 52,83% | +0,80% | +0,71% | +0,21% | +1,50% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 56 | 55,36% | +0,89% | +0,89% | +0,31% | +1,59% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 56 | 55,36% | +0,89% | +0,89% | +0,31% | +1,59% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 51 | 45,10% | +1,09% | +0,27% | +0,50% | +1,78% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,18% | +0,55% | +0,59% | +1,89% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,27% | +1,27% | +0,55% | +1,72% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 52 | 50,00% | +1,07% | +0,93% | -0,93% | +2,75% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 55 | 58,18% | +1,36% | +1,36% | -0,91% | +2,98% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 55 | 58,18% | +1,36% | +1,36% | -0,91% | +2,98% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 50 | 40,00% | +1,70% | +0,01% | -0,72% | +3,28% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 23 | 43,48% | +1,94% | +0,27% | -0,53% | +3,49% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 50 | 46,00% | +1,98% | +1,72% | -1,56% | +4,18% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 53 | 52,83% | +2,23% | +2,23% | -1,53% | +4,49% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 53 | 52,83% | +2,23% | +2,23% | -1,53% | +4,49% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 48 | 43,75% | +2,57% | -0,95% | -1,33% | +4,88% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 21 | 47,62% | +4,12% | -1,41% | -1,07% | +6,28% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 48 | 54,17% | +2,73% | +2,51% | -1,75% | +5,40% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 51 | 60,78% | +3,06% | +3,06% | -1,73% | +5,70% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 51 | 60,78% | +3,06% | +3,06% | -1,73% | +5,70% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 46 | 41,30% | +3,64% | -1,91% | -1,50% | +6,20% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 19 | 42,11% | +6,13% | -3,56% | -1,07% | +9,06% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 45 | 60,00% | +3,88% | +3,68% | -1,94% | +6,62% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 48 | 64,58% | +4,04% | +4,04% | -1,94% | +6,87% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 48 | 64,58% | +4,04% | +4,04% | -1,94% | +6,87% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 43 | 44,19% | +4,65% | -1,53% | -1,68% | +7,53% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 16 | 50,00% | +8,06% | -5,13% | -0,93% | +10,98% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 41 | 65,85% | +6,12% | +6,04% | -2,00% | +9,43% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 44 | 65,91% | +6,17% | +6,17% | -2,01% | +9,51% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 44 | 65,91% | +6,17% | +6,17% | -2,01% | +9,51% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 39 | 61,54% | +7,12% | +0,90% | -1,70% | +10,52% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 12 | 50,00% | +10,44% | -5,94% | -0,24% | +14,07% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +1,23% | +1,23% | -1,55% | +6,04% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 35 | 60,00% | +9,77% | +9,58% | -2,74% | +13,36% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 37 | 67,57% | +9,18% | +9,18% | -2,79% | +12,78% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 37 | 67,57% | +9,18% | +9,18% | -2,79% | +12,78% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 33 | 72,73% | +10,46% | +10,46% | -2,58% | +14,04% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 32 | 34,38% | +10,37% | -0,83% | -2,53% | +14,02% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 7 | 0,00% | +18,41% | -18,41% | -1,07% | +21,11% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 28 | 89,29% | +13,01% | +11,47% | -2,90% | +16,87% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 30 | 83,33% | +12,68% | +12,68% | -2,95% | +16,63% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 30 | 83,33% | +12,68% | +12,68% | -2,95% | +16,63% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 26 | 84,62% | +13,91% | +13,91% | -2,72% | +18,10% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 25 | 36,00% | +12,68% | -5,38% | -2,65% | +16,99% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 14 | 85,71% | +22,52% | +16,15% | -3,23% | +26,32% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 15 | 100,00% | +22,60% | +22,60% | -3,18% | +26,39% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 15 | 100,00% | +22,60% | +22,60% | -3,18% | +26,39% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 11 | 100,00% | +23,16% | +23,16% | -2,71% | +26,81% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 12 | 33,33% | +22,88% | -7,97% | -2,79% | +26,91% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 53 | 45,28% | +0,55% | +0,15% | -0,10% | +1,56% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 56 | 57,14% | +0,43% | +0,44% | -0,24% | +1,37% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 56 | 57,14% | +0,43% | +0,44% | -0,24% | +1,37% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 50 | 54,00% | +0,34% | +0,51% | -0,35% | +1,27% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 31 | 41,94% | +0,27% | -0,51% | -0,38% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +2,48% | +2,09% | +0,94% | +3,13% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 52 | 48,08% | +0,99% | +0,52% | +0,19% | +2,31% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 55 | 54,55% | +0,76% | +0,81% | -0,02% | +1,99% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 55 | 54,55% | +0,76% | +0,81% | -0,02% | +1,99% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 49 | 57,14% | +0,36% | +0,73% | -0,42% | +1,56% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +3,38% | +3,05% | +2,44% | +5,44% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 51 | 43,14% | +1,43% | +0,96% | -1,57% | +4,30% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 54 | 53,70% | +1,20% | +1,21% | -1,74% | +3,89% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 54 | 53,70% | +1,20% | +1,21% | -1,74% | +3,89% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 48 | 45,83% | +0,31% | +0,66% | -2,03% | +2,88% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 31 | 32,26% | +1,30% | -2,13% | -1,89% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +2,90% | +2,64% | -0,79% | +6,76% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 49 | 53,06% | +2,10% | +2,38% | -2,57% | +6,35% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 52 | 51,92% | +1,93% | +2,36% | -2,66% | +6,04% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 52 | 51,92% | +1,93% | +2,36% | -2,66% | +6,04% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 46 | 56,52% | +0,75% | +0,47% | -3,16% | +4,87% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | +1,54% | +1,34% | -1,56% | +8,05% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 48 | 62,50% | +2,63% | +3,74% | -3,04% | +8,20% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 50 | 58,00% | +2,53% | +3,30% | -3,12% | +7,85% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 50 | 58,00% | +2,53% | +3,30% | -3,12% | +7,85% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 44 | 56,82% | +1,01% | +1,04% | -3,73% | +6,23% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +0,41% | +0,28% | -2,23% | +8,54% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 46 | 56,52% | +2,84% | +3,96% | -3,54% | +9,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 47 | 57,45% | +2,73% | +3,84% | -3,50% | +9,38% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 47 | 57,45% | +2,73% | +3,84% | -3,50% | +9,38% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 41 | 60,98% | +0,55% | +1,48% | -4,21% | +6,80% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,00% | -0,43% | -2,75% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 42 | 71,43% | +5,50% | +7,71% | -3,39% | +14,06% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 44 | 75,00% | +5,15% | +7,28% | -3,44% | +13,47% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 44 | 75,00% | +5,15% | +7,28% | -3,44% | +13,47% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 37 | 67,57% | +1,71% | +1,23% | -4,12% | +9,00% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 29 | 51,72% | +3,65% | -3,97% | -3,94% | +11,74% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +9,19% | +2,65% | -1,41% | +17,72% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 35 | 77,14% | +8,31% | +7,18% | -3,98% | +18,09% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 37 | 86,49% | +8,41% | +11,61% | -4,01% | +18,28% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 37 | 86,49% | +8,41% | +11,61% | -4,01% | +18,28% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 88,57% | +8,96% | +12,20% | -4,02% | +19,06% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 32 | 65,62% | +6,34% | -3,06% | -4,46% | +14,37% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 24 | 62,50% | +4,37% | -4,37% | -4,40% | +12,31% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,49% | -0,95% | -1,31% | +25,23% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 28 | 71,43% | +10,64% | +2,68% | -4,78% | +22,52% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 30 | 86,67% | +11,38% | +9,86% | -4,76% | +23,69% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 30 | 86,67% | +11,38% | +9,86% | -4,76% | +23,69% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 28 | 92,86% | +10,20% | +12,56% | -4,83% | +22,72% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 29 | 41,38% | +11,00% | -11,00% | -4,87% | +23,03% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 21 | 52,38% | +8,46% | -8,46% | -5,03% | +18,17% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +31,57% | +10,47% | -1,27% | +41,74% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 15 | 0,00% | +19,04% | -19,04% | -6,61% | +36,84% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 15 | 0,00% | +19,04% | -19,04% | -6,61% | +36,84% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 15 | 0,00% | +19,04% | -19,04% | -6,61% | +36,84% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 14 | 0,00% | +18,56% | -18,56% | -6,65% | +36,74% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 15 | 0,00% | +19,04% | -19,04% | -6,61% | +36,84% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 14 | 0,00% | +19,32% | -19,32% | -6,50% | +36,96% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 50 | 56,00% | +0,72% | +0,60% | +0,01% | +1,63% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 52 | 57,69% | +0,41% | +0,40% | -0,23% | +1,30% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 55 | 56,36% | +0,45% | +0,32% | -0,20% | +1,33% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 54 | 51,85% | +0,41% | +0,39% | -0,27% | +1,25% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 38 | 52,63% | +0,64% | +0,59% | -0,18% | +1,57% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 49 | 53,06% | +1,39% | +1,24% | +0,42% | +2,49% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 51 | 49,02% | +0,99% | +0,51% | +0,02% | +1,82% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 54 | 48,15% | +0,95% | +0,47% | +0,01% | +1,87% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 53 | 45,28% | +0,88% | +0,30% | -0,02% | +1,99% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 37 | 54,05% | +1,02% | +0,99% | +0,08% | +2,01% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 48 | 58,33% | +2,19% | +2,01% | -1,29% | +4,44% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 50 | 50,00% | +1,67% | +1,08% | -1,61% | +3,91% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 53 | 49,06% | +1,59% | +1,00% | -1,59% | +3,88% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 52 | 50,00% | +1,44% | +0,18% | -1,67% | +3,61% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 36 | 55,56% | +1,41% | +1,26% | -1,62% | +3,59% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 46 | 60,87% | +3,57% | +3,45% | -2,03% | +6,93% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 48 | 54,17% | +2,84% | +1,71% | -2,35% | +6,20% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 51 | 52,94% | +2,71% | +1,56% | -2,33% | +6,06% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 50 | 48,00% | +2,71% | -0,47% | -2,50% | +5,95% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 34 | 58,82% | +1,98% | +1,81% | -2,47% | +5,11% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 44 | 65,91% | +5,07% | +5,19% | -2,28% | +9,03% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 46 | 60,87% | +4,21% | +2,83% | -2,63% | +8,22% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 49 | 61,22% | +3,95% | +2,66% | -2,64% | +7,96% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 48 | 41,67% | +3,90% | -1,32% | -2,81% | +7,89% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 32 | 53,12% | +2,22% | +2,28% | -2,83% | +6,21% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 41 | 73,17% | +7,41% | +7,60% | -2,22% | +11,85% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 43 | 67,44% | +6,44% | +5,37% | -2,68% | +10,65% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 46 | 65,22% | +6,00% | +5,04% | -2,73% | +10,21% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 45 | 51,11% | +5,37% | -2,10% | -2,94% | +9,77% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 29 | 65,52% | +2,56% | +2,68% | -2,87% | +7,35% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 37 | 78,38% | +10,83% | +11,81% | -2,62% | +16,50% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 39 | 79,49% | +10,17% | +9,13% | -3,01% | +15,08% | PRIMA CALIBRAZIONE |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 42 | 80,95% | +9,23% | +8,70% | -3,07% | +14,28% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 34 | 73,53% | +10,71% | +10,82% | -2,97% | +15,49% | PRIMA CALIBRAZIONE |
| SOL | 14g | Tecnico | CALIBRABILE | 41 | 36,59% | +7,64% | -5,35% | -3,37% | +12,87% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 25 | 48,00% | +3,28% | +1,28% | -3,42% | +7,80% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +10,82% | +10,82% | -3,34% | +16,86% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 30 | 73,33% | +15,33% | +14,15% | -4,45% | +21,34% | PRIMA CALIBRAZIONE |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 33 | 84,85% | +15,35% | +17,05% | -4,40% | +20,70% | PRIMA CALIBRAZIONE |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 36 | 86,11% | +13,84% | +15,85% | -4,55% | +19,30% | PRIMA CALIBRAZIONE |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 31 | 70,97% | +16,52% | +17,06% | -4,12% | +21,95% | PRIMA CALIBRAZIONE |
| SOL | 21g | Tecnico | CALIBRABILE | 35 | 34,29% | +12,10% | -13,27% | -4,75% | +17,37% | PRIMA CALIBRAZIONE |
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
