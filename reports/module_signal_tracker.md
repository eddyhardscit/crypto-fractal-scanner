# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-05 08:22 UTC

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

Segnali totali salvati: **171**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-05 | BTC | 79.660,00 | +5 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-05 | DOGE | 0.08560 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-05 | SOL | 102,27 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-04 | BTC | 80.963,98 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-04 | DOGE | 0.08695 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-04 | SOL | 103,67 | +6 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-03 | BTC | 77.295,19 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-03 | DOGE | 0.08235 | -1 | -2 | -2 | 0 | +1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-03 | SOL | 100,15 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-02 | BTC | 77.662,37 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-02 | DOGE | 0.08189 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-02 | SOL | 100,25 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 57 | 56 | 55 | 54 | 52 | 50 | 47 | 43 | 36 | 29 | 14 | 0 |
| SOL | 57 | 56 | 55 | 54 | 52 | 50 | 47 | 43 | 36 | 29 | 14 | 0 |
| DOGE | 57 | 56 | 55 | 54 | 52 | 50 | 47 | 43 | 36 | 29 | 14 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-23 | 45g | 2026-09-06 | domani |
| SOL | 2026-07-23 | 45g | 2026-09-06 | domani |
| DOGE | 2026-07-23 | 45g | 2026-09-06 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 53 | 50,94% | +0,46% | +0,44% | PRIMA CALIBRAZIONE |
| BTC | 2g | 52 | 53,85% | +0,84% | +0,75% | PRIMA CALIBRAZIONE |
| BTC | 3g | 51 | 49,02% | +1,02% | +0,88% | PRIMA CALIBRAZIONE |
| BTC | 5g | 49 | 44,90% | +1,99% | +1,74% | PRIMA CALIBRAZIONE |
| BTC | 7g | 47 | 53,19% | +2,75% | +2,52% | PRIMA CALIBRAZIONE |
| BTC | 10g | 44 | 59,09% | +3,93% | +3,72% | PRIMA CALIBRAZIONE |
| BTC | 14g | 40 | 65,00% | +6,16% | +6,07% | PRIMA CALIBRAZIONE |
| BTC | 21g | 34 | 58,82% | +9,27% | +9,07% | PRIMA CALIBRAZIONE |
| BTC | 30g | 27 | 88,89% | +12,59% | +10,99% | FEEDBACK RAPIDO |
| BTC | 45g | 13 | 84,62% | +22,55% | +15,69% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 49 | 55,10% | +0,66% | +0,54% | PRIMA CALIBRAZIONE |
| SOL | 2g | 48 | 52,08% | +1,37% | +1,22% | PRIMA CALIBRAZIONE |
| SOL | 3g | 47 | 57,45% | +2,12% | +1,93% | PRIMA CALIBRAZIONE |
| SOL | 5g | 45 | 60,00% | +3,61% | +3,49% | PRIMA CALIBRAZIONE |
| SOL | 7g | 43 | 65,12% | +5,17% | +5,29% | PRIMA CALIBRAZIONE |
| SOL | 10g | 40 | 72,50% | +7,47% | +7,66% | PRIMA CALIBRAZIONE |
| SOL | 14g | 36 | 77,78% | +10,75% | +11,76% | PRIMA CALIBRAZIONE |
| SOL | 21g | 29 | 72,41% | +14,46% | +13,23% | FEEDBACK RAPIDO |
| SOL | 30g | 22 | 54,55% | +16,13% | +7,14% | FEEDBACK RAPIDO |
| SOL | 45g | 13 | 30,77% | +32,86% | -14,79% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 52 | 46,15% | +0,44% | +0,27% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 51 | 49,02% | +0,92% | +0,62% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 50 | 44,00% | +1,25% | +1,19% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 48 | 54,17% | +1,96% | +2,61% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 47 | 61,70% | +2,54% | +3,67% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 45 | 57,78% | +2,78% | +4,16% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 41 | 70,73% | +5,62% | +7,89% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 34 | 76,47% | +7,66% | +6,49% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 27 | 70,37% | +9,87% | +1,60% | FEEDBACK RAPIDO |
| DOGE | 45g | 14 | 0,00% | +18,56% | -18,56% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 53 | 50,94% | +0,46% | +0,44% | +0,00% | +1,01% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 56 | 53,57% | +0,43% | +0,43% | -0,01% | +0,97% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 56 | 53,57% | +0,43% | +0,43% | -0,01% | +0,97% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 51 | 39,22% | +0,57% | +0,16% | +0,10% | +1,10% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,81% | +0,37% | +0,13% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | -0,20% | -0,20% | -0,66% | +0,18% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 52 | 53,85% | +0,84% | +0,75% | +0,24% | +1,55% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 55 | 56,36% | +0,94% | +0,94% | +0,34% | +1,63% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 55 | 56,36% | +0,94% | +0,94% | +0,34% | +1,63% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 50 | 46,00% | +1,13% | +0,31% | +0,53% | +1,83% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 23 | 43,48% | +1,29% | +0,63% | +0,68% | +2,02% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 51 | 49,02% | +1,02% | +0,88% | -0,98% | +2,70% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 54 | 57,41% | +1,33% | +1,33% | -0,96% | +2,93% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 54 | 57,41% | +1,33% | +1,33% | -0,96% | +2,93% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 49 | 38,78% | +1,66% | -0,06% | -0,77% | +3,23% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 22 | 40,91% | +1,88% | +0,13% | -0,63% | +3,40% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 49 | 44,90% | +1,99% | +1,74% | -1,52% | +4,18% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 52 | 51,92% | +2,25% | +2,25% | -1,49% | +4,50% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 52 | 51,92% | +2,25% | +2,25% | -1,49% | +4,50% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 47 | 42,55% | +2,60% | -1,00% | -1,28% | +4,90% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 20 | 45,00% | +4,27% | -1,53% | -0,94% | +6,39% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 47 | 53,19% | +2,75% | +2,52% | -1,73% | +5,40% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 50 | 60,00% | +3,08% | +3,08% | -1,72% | +5,71% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 50 | 60,00% | +3,08% | +3,08% | -1,72% | +5,71% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 45 | 40,00% | +3,67% | -2,00% | -1,48% | +6,22% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 18 | 38,89% | +6,35% | -3,89% | -0,99% | +9,27% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 44 | 59,09% | +3,93% | +3,72% | -1,91% | +6,66% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 47 | 63,83% | +4,10% | +4,10% | -1,92% | +6,92% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 47 | 63,83% | +4,10% | +4,10% | -1,92% | +6,92% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 42 | 42,86% | +4,72% | -1,61% | -1,65% | +7,60% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 15 | 46,67% | +8,49% | -5,57% | -0,79% | +11,40% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 40 | 65,00% | +6,16% | +6,07% | -2,05% | +9,47% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 43 | 65,12% | +6,20% | +6,20% | -2,06% | +9,55% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 43 | 65,12% | +6,20% | +6,20% | -2,06% | +9,55% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 38 | 60,53% | +7,18% | +0,80% | -1,74% | +10,59% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 11 | 45,45% | +10,96% | -6,91% | -0,26% | +14,63% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 34 | 58,82% | +9,27% | +9,07% | -2,81% | +12,85% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 36 | 66,67% | +8,69% | +8,69% | -2,85% | +12,28% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 36 | 66,67% | +8,69% | +8,69% | -2,85% | +12,28% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 32 | 71,88% | +9,95% | +9,95% | -2,65% | +13,52% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 31 | 35,48% | +9,84% | +0,01% | -2,59% | +13,48% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 6 | 0,00% | +17,01% | -17,01% | -1,17% | +19,54% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 27 | 88,89% | +12,59% | +10,99% | -2,92% | +16,45% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 29 | 82,76% | +12,27% | +12,27% | -2,97% | +16,23% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 29 | 82,76% | +12,27% | +12,27% | -2,97% | +16,23% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 25 | 84,00% | +13,48% | +13,48% | -2,72% | +17,70% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 24 | 33,33% | +12,18% | -6,62% | -2,65% | +16,52% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 13 | 84,62% | +22,55% | +15,69% | -3,10% | +26,36% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 14 | 100,00% | +22,63% | +22,63% | -3,07% | +26,43% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 14 | 100,00% | +22,63% | +22,63% | -3,07% | +26,43% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 10 | 100,00% | +23,26% | +23,26% | -2,50% | +26,92% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 11 | 36,36% | +22,95% | -6,68% | -2,60% | +27,01% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 52 | 46,15% | +0,44% | +0,27% | -0,20% | +1,46% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 55 | 58,18% | +0,32% | +0,56% | -0,33% | +1,26% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 55 | 58,18% | +0,32% | +0,56% | -0,33% | +1,26% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 49 | 53,06% | +0,22% | +0,40% | -0,45% | +1,15% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 31 | 41,94% | +0,27% | -0,51% | -0,38% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +2,48% | +2,09% | +0,94% | +3,13% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 51 | 49,02% | +0,92% | +0,62% | +0,13% | +2,25% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 54 | 55,56% | +0,69% | +0,91% | -0,08% | +1,92% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 54 | 55,56% | +0,69% | +0,91% | -0,08% | +1,92% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 48 | 56,25% | +0,27% | +0,65% | -0,49% | +1,48% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +3,38% | +3,05% | +2,44% | +5,44% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 50 | 44,00% | +1,25% | +1,19% | -1,64% | +4,17% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 53 | 54,72% | +1,02% | +1,43% | -1,81% | +3,75% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 53 | 54,72% | +1,02% | +1,43% | -1,81% | +3,75% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 47 | 44,68% | +0,10% | +0,46% | -2,12% | +2,70% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 31 | 32,26% | +1,30% | -2,13% | -1,89% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +2,90% | +2,64% | -0,79% | +6,76% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 48 | 54,17% | +1,96% | +2,61% | -2,54% | +6,28% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 51 | 52,94% | +1,79% | +2,58% | -2,64% | +5,97% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 51 | 52,94% | +1,79% | +2,58% | -2,64% | +5,97% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 45 | 55,56% | +0,57% | +0,29% | -3,15% | +4,77% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | +1,54% | +1,34% | -1,56% | +8,05% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 47 | 61,70% | +2,54% | +3,67% | -2,98% | +8,21% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 49 | 59,18% | +2,44% | +3,51% | -3,07% | +7,85% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 49 | 59,18% | +2,44% | +3,51% | -3,07% | +7,85% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 43 | 55,81% | +0,88% | +0,90% | -3,69% | +6,20% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +0,41% | +0,28% | -2,23% | +8,54% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 45 | 57,78% | +2,78% | +4,16% | -3,46% | +9,70% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 46 | 58,70% | +2,67% | +4,05% | -3,42% | +9,45% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 46 | 58,70% | +2,67% | +4,05% | -3,42% | +9,45% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 40 | 60,00% | +0,43% | +1,38% | -4,15% | +6,82% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,00% | -0,43% | -2,75% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 41 | 70,73% | +5,62% | +7,89% | -3,20% | +14,33% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 43 | 74,42% | +5,26% | +7,44% | -3,26% | +13,71% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 43 | 74,42% | +5,26% | +7,44% | -3,26% | +13,71% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 36 | 66,67% | +1,74% | +1,26% | -3,92% | +9,15% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 28 | 50,00% | +3,76% | -4,13% | -3,68% | +12,04% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +9,19% | +2,65% | -1,41% | +17,72% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 34 | 76,47% | +7,66% | +6,49% | -4,09% | +17,35% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 36 | 86,11% | +7,79% | +11,08% | -4,11% | +17,58% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 36 | 86,11% | +7,79% | +11,08% | -4,11% | +17,58% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 34 | 88,24% | +8,33% | +11,66% | -4,13% | +18,34% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 31 | 64,52% | +5,56% | -4,14% | -4,59% | +13,43% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 23 | 65,22% | +3,23% | -3,23% | -4,58% | +10,96% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,49% | -0,95% | -1,31% | +25,23% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 27 | 70,37% | +9,87% | +1,60% | -4,95% | +21,70% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 29 | 86,21% | +10,68% | +9,11% | -4,92% | +22,96% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 29 | 86,21% | +10,68% | +9,11% | -4,92% | +22,96% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 27 | 92,59% | +9,40% | +11,85% | -5,01% | +21,91% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 28 | 42,86% | +10,27% | -10,27% | -5,04% | +22,25% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 20 | 55,00% | +7,30% | -7,30% | -5,27% | +16,83% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 14 | 0,00% | +18,56% | -18,56% | -6,65% | +36,74% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 14 | 0,00% | +18,56% | -18,56% | -6,65% | +36,74% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 14 | 0,00% | +18,56% | -18,56% | -6,65% | +36,74% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 14 | 0,00% | +18,56% | -18,56% | -6,65% | +36,74% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 14 | 0,00% | +18,56% | -18,56% | -6,65% | +36,74% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 13 | 0,00% | +18,83% | -18,83% | -6,54% | +36,85% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 49 | 55,10% | +0,66% | +0,54% | -0,01% | +1,57% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 51 | 56,86% | +0,35% | +0,34% | -0,25% | +1,23% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 54 | 55,56% | +0,39% | +0,26% | -0,22% | +1,27% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 53 | 50,94% | +0,35% | +0,33% | -0,29% | +1,19% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 37 | 51,35% | +0,56% | +0,51% | -0,20% | +1,49% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 48 | 52,08% | +1,37% | +1,22% | +0,44% | +2,48% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 50 | 48,00% | +0,96% | +0,48% | +0,03% | +1,80% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 53 | 47,17% | +0,93% | +0,43% | +0,02% | +1,85% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 52 | 44,23% | +0,86% | +0,27% | -0,01% | +1,97% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 36 | 52,78% | +0,99% | +0,96% | +0,10% | +1,99% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 47 | 57,45% | +2,12% | +1,93% | -1,33% | +4,39% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 49 | 48,98% | +1,58% | +0,98% | -1,65% | +3,85% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 52 | 48,08% | +1,51% | +0,91% | -1,63% | +3,83% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 51 | 49,02% | +1,35% | +0,07% | -1,71% | +3,55% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 35 | 54,29% | +1,28% | +1,13% | -1,68% | +3,50% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 45 | 60,00% | +3,61% | +3,49% | -1,93% | +7,03% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 47 | 53,19% | +2,86% | +1,70% | -2,27% | +6,27% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 50 | 52,00% | +2,73% | +1,56% | -2,25% | +6,13% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 49 | 46,94% | +2,73% | -0,52% | -2,42% | +6,02% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 33 | 57,58% | +1,98% | +1,81% | -2,35% | +5,19% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 43 | 65,12% | +5,17% | +5,29% | -2,17% | +9,20% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 45 | 60,00% | +4,28% | +2,87% | -2,53% | +8,37% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 48 | 60,42% | +4,01% | +2,70% | -2,54% | +8,09% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 47 | 40,43% | +3,97% | -1,37% | -2,72% | +8,02% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 31 | 51,61% | +2,27% | +2,33% | -2,69% | +6,36% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 40 | 72,50% | +7,47% | +7,66% | -2,20% | +11,92% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 42 | 66,67% | +6,47% | +5,38% | -2,66% | +10,69% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 45 | 64,44% | +6,02% | +5,03% | -2,71% | +10,24% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 44 | 50,00% | +5,38% | -2,27% | -2,93% | +9,78% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 28 | 64,29% | +2,47% | +2,59% | -2,85% | +7,29% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 36 | 77,78% | +10,75% | +11,76% | -2,71% | +16,45% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 38 | 81,58% | +10,08% | +9,74% | -3,10% | +15,00% | PRIMA CALIBRAZIONE |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 41 | 82,93% | +9,11% | +9,25% | -3,16% | +14,19% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 34 | 73,53% | +10,71% | +10,82% | -2,97% | +15,49% | PRIMA CALIBRAZIONE |
| SOL | 14g | Tecnico | CALIBRABILE | 40 | 35,00% | +7,48% | -5,83% | -3,46% | +12,74% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 24 | 45,83% | +2,84% | +0,76% | -3,58% | +7,36% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +10,82% | +10,82% | -3,34% | +16,86% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 29 | 72,41% | +14,46% | +13,23% | -4,56% | +20,49% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 32 | 84,38% | +14,56% | +16,31% | -4,50% | +19,90% | PRIMA CALIBRAZIONE |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 35 | 85,71% | +13,08% | +15,15% | -4,64% | +18,53% | PRIMA CALIBRAZIONE |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 30 | 70,00% | +15,71% | +16,28% | -4,22% | +21,15% | PRIMA CALIBRAZIONE |
| SOL | 21g | Tecnico | CALIBRABILE | 34 | 35,29% | +11,26% | -12,47% | -4,86% | +16,53% | PRIMA CALIBRAZIONE |
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
