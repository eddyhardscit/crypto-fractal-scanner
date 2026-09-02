# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-02 05:32 UTC

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

Segnali totali salvati: **162**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-02 | BTC | 77.662,37 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-02 | DOGE | 0.08189 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-02 | SOL | 100,25 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-01 | BTC | 79.026,52 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-01 | DOGE | 0.08350 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-01 | SOL | 104,07 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-31 | BTC | 78.005,28 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-31 | DOGE | 0.08279 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-31 | SOL | 102,56 | +6 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-30 | BTC | 78.145,28 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-30 | DOGE | 0.08501 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-30 | SOL | 105,04 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 54 | 53 | 52 | 51 | 49 | 47 | 44 | 40 | 34 | 26 | 11 | 0 |
| SOL | 54 | 53 | 52 | 51 | 49 | 47 | 44 | 40 | 34 | 26 | 11 | 0 |
| DOGE | 54 | 53 | 52 | 51 | 49 | 47 | 44 | 40 | 34 | 26 | 11 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-20 | 45g | 2026-09-03 | domani |
| SOL | 2026-07-20 | 45g | 2026-09-03 | domani |
| DOGE | 2026-07-20 | 45g | 2026-09-03 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 50 | 52,00% | +0,43% | +0,41% | PRIMA CALIBRAZIONE |
| BTC | 2g | 49 | 53,06% | +0,79% | +0,69% | PRIMA CALIBRAZIONE |
| BTC | 3g | 48 | 47,92% | +1,00% | +0,85% | PRIMA CALIBRAZIONE |
| BTC | 5g | 46 | 43,48% | +2,01% | +1,73% | PRIMA CALIBRAZIONE |
| BTC | 7g | 44 | 52,27% | +2,88% | +2,63% | PRIMA CALIBRAZIONE |
| BTC | 10g | 41 | 56,10% | +4,18% | +3,96% | PRIMA CALIBRAZIONE |
| BTC | 14g | 37 | 62,16% | +6,06% | +5,96% | PRIMA CALIBRAZIONE |
| BTC | 21g | 32 | 56,25% | +8,12% | +7,91% | PRIMA CALIBRAZIONE |
| BTC | 30g | 24 | 87,50% | +11,24% | +9,45% | FEEDBACK RAPIDO |
| BTC | 45g | 10 | 80,00% | +22,88% | +13,96% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 46 | 56,52% | +0,66% | +0,53% | PRIMA CALIBRAZIONE |
| SOL | 2g | 45 | 51,11% | +1,42% | +1,27% | PRIMA CALIBRAZIONE |
| SOL | 3g | 44 | 59,09% | +2,28% | +2,08% | PRIMA CALIBRAZIONE |
| SOL | 5g | 42 | 64,29% | +3,99% | +3,86% | PRIMA CALIBRAZIONE |
| SOL | 7g | 40 | 70,00% | +5,68% | +5,81% | PRIMA CALIBRAZIONE |
| SOL | 10g | 37 | 70,27% | +7,71% | +7,92% | PRIMA CALIBRAZIONE |
| SOL | 14g | 33 | 75,76% | +10,42% | +11,52% | PRIMA CALIBRAZIONE |
| SOL | 21g | 27 | 70,37% | +12,82% | +11,51% | FEEDBACK RAPIDO |
| SOL | 30g | 20 | 50,00% | +13,83% | +3,94% | FEEDBACK RAPIDO |
| SOL | 45g | 10 | 30,00% | +33,14% | -16,16% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 49 | 46,94% | +0,38% | +0,38% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 48 | 50,00% | +0,79% | +0,84% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 48 | 45,83% | +1,12% | +1,42% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 46 | 54,35% | +2,07% | +2,75% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 45 | 60,00% | +2,74% | +3,72% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 42 | 61,90% | +3,41% | +4,89% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 38 | 71,05% | +5,79% | +8,23% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 32 | 75,00% | +6,66% | +5,42% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 25 | 68,00% | +9,07% | +0,14% | FEEDBACK RAPIDO |
| DOGE | 45g | 11 | 0,00% | +18,98% | -18,98% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 50 | 52,00% | +0,43% | +0,41% | -0,03% | +0,99% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 53 | 54,72% | +0,40% | +0,40% | -0,05% | +0,95% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 53 | 54,72% | +0,40% | +0,40% | -0,05% | +0,95% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 48 | 39,58% | +0,55% | +0,12% | +0,07% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 21 | 38,10% | +0,80% | +0,30% | +0,07% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 49 | 53,06% | +0,79% | +0,69% | +0,19% | +1,47% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 52 | 55,77% | +0,89% | +0,89% | +0,30% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 52 | 55,77% | +0,89% | +0,89% | +0,30% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 47 | 44,68% | +1,10% | +0,22% | +0,50% | +1,77% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 20 | 40,00% | +1,23% | +0,47% | +0,63% | +1,88% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 48 | 47,92% | +1,00% | +0,85% | -0,90% | +2,65% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 51 | 56,86% | +1,32% | +1,32% | -0,89% | +2,90% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 51 | 56,86% | +1,32% | +1,32% | -0,89% | +2,90% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 46 | 36,96% | +1,68% | -0,15% | -0,68% | +3,22% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 19 | 36,84% | +1,96% | -0,06% | -0,39% | +3,39% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 46 | 43,48% | +2,01% | +1,73% | -1,48% | +4,20% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 49 | 51,02% | +2,28% | +2,28% | -1,45% | +4,53% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 49 | 51,02% | +2,28% | +2,28% | -1,45% | +4,53% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 44 | 40,91% | +2,66% | -1,19% | -1,23% | +4,97% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 17 | 41,18% | +4,72% | -2,12% | -0,74% | +6,82% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 44 | 52,27% | +2,88% | +2,63% | -1,65% | +5,51% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 47 | 59,57% | +3,22% | +3,22% | -1,63% | +5,83% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 47 | 59,57% | +3,22% | +3,22% | -1,63% | +5,83% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 42 | 38,10% | +3,87% | -2,20% | -1,38% | +6,39% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 15 | 33,33% | +7,45% | -4,83% | -0,59% | +10,35% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 41 | 56,10% | +4,18% | +3,96% | -1,81% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 44 | 61,36% | +4,34% | +4,34% | -1,82% | +7,15% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 44 | 61,36% | +4,34% | +4,34% | -1,82% | +7,15% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 39 | 38,46% | +5,05% | -1,77% | -1,52% | +7,91% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 12 | 33,33% | +10,50% | -7,08% | -0,15% | +13,38% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,69% | +0,69% | -0,88% | +5,44% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 37 | 62,16% | +6,06% | +5,96% | -2,31% | +9,37% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 40 | 62,50% | +6,11% | +6,11% | -2,31% | +9,47% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 40 | 62,50% | +6,11% | +6,11% | -2,31% | +9,47% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 35 | 57,14% | +7,16% | +0,24% | -2,00% | +10,58% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 8 | 25,00% | +12,28% | -12,28% | -0,83% | +16,12% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 32 | 56,25% | +8,12% | +7,91% | -2,96% | +11,77% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 34 | 64,71% | +7,57% | +7,57% | -3,00% | +11,24% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 34 | 64,71% | +7,57% | +7,57% | -3,00% | +11,24% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 30 | 70,00% | +8,77% | +8,77% | -2,80% | +12,42% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 29 | 37,93% | +8,61% | +1,92% | -2,74% | +12,34% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 4 | 0,00% | +11,68% | -11,68% | -1,55% | +14,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 24 | 87,50% | +11,24% | +9,45% | -2,93% | +15,13% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 26 | 80,77% | +11,00% | +11,00% | -2,98% | +14,99% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 26 | 80,77% | +11,00% | +11,00% | -2,98% | +14,99% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 22 | 81,82% | +12,14% | +12,14% | -2,71% | +16,43% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 21 | 28,57% | +10,59% | -8,42% | -2,63% | +15,03% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 10 | 80,00% | +22,88% | +13,96% | -2,63% | +26,74% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 11 | 100,00% | +22,96% | +22,96% | -2,62% | +26,80% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 11 | 100,00% | +22,96% | +22,96% | -2,62% | +26,80% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 10 | 100,00% | +23,26% | +23,26% | -2,50% | +26,92% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 10 | 40,00% | +23,20% | -5,30% | -2,56% | +27,04% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 49 | 46,94% | +0,38% | +0,38% | -0,25% | +1,40% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 52 | 59,62% | +0,25% | +0,68% | -0,39% | +1,20% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 52 | 59,62% | +0,25% | +0,68% | -0,39% | +1,20% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 46 | 52,17% | +0,14% | +0,32% | -0,52% | +1,07% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 31 | 41,94% | +0,27% | -0,51% | -0,38% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +2,48% | +2,09% | +0,94% | +3,13% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 48 | 50,00% | +0,79% | +0,84% | +0,03% | +2,10% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 51 | 56,86% | +0,56% | +1,13% | -0,19% | +1,76% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 51 | 56,86% | +0,56% | +1,13% | -0,19% | +1,76% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 45 | 55,56% | +0,09% | +0,50% | -0,64% | +1,27% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +3,38% | +3,05% | +2,44% | +5,44% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 48 | 45,83% | +1,12% | +1,42% | -1,61% | +4,03% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 50 | 56,00% | +0,92% | +1,67% | -1,78% | +3,65% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 50 | 56,00% | +0,92% | +1,67% | -1,78% | +3,65% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 44 | 43,18% | -0,08% | +0,30% | -2,11% | +2,52% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 31 | 32,26% | +1,30% | -2,13% | -1,89% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +2,90% | +2,64% | -0,79% | +6,76% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 46 | 54,35% | +2,07% | +2,75% | -2,42% | +6,44% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 48 | 54,17% | +1,85% | +2,79% | -2,52% | +6,07% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 48 | 54,17% | +1,85% | +2,79% | -2,52% | +6,07% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 42 | 54,76% | +0,56% | +0,25% | -3,05% | +4,79% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | +2,23% | +2,00% | -1,09% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 45 | 60,00% | +2,74% | +3,72% | -2,85% | +8,36% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 46 | 58,70% | +2,70% | +3,63% | -2,83% | +8,13% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 46 | 58,70% | +2,70% | +3,63% | -2,83% | +8,13% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 40 | 57,50% | +1,06% | +1,09% | -3,46% | +6,40% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | +0,39% | +0,24% | -1,74% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 42 | 61,90% | +3,41% | +4,89% | -2,93% | +10,34% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 44 | 61,36% | +3,17% | +4,61% | -3,00% | +9,92% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 44 | 61,36% | +3,17% | +4,61% | -3,00% | +9,92% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 37 | 64,86% | +0,95% | +1,99% | -3,59% | +7,32% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 29 | 44,83% | +2,95% | -4,12% | -3,35% | +9,95% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +1,71% | +1,21% | -1,24% | +10,26% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 38 | 71,05% | +5,79% | +8,23% | -3,29% | +13,88% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 40 | 75,00% | +5,39% | +7,73% | -3,35% | +13,24% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 40 | 75,00% | +5,39% | +7,73% | -3,35% | +13,24% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 33 | 66,67% | +1,58% | +1,05% | -4,09% | +8,18% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 27 | 51,85% | +4,09% | -4,09% | -3,41% | +12,32% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,47% | +2,65% | -1,31% | +16,91% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 32 | 75,00% | +6,66% | +5,42% | -4,30% | +15,73% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 34 | 85,29% | +6,86% | +10,34% | -4,31% | +16,06% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 34 | 85,29% | +6,86% | +10,34% | -4,31% | +16,06% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 32 | 87,50% | +7,37% | +10,91% | -4,34% | +16,79% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 30 | 63,33% | +5,01% | -5,01% | -4,70% | +12,46% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 22 | 68,18% | +2,23% | -2,23% | -4,78% | +9,45% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,49% | -0,95% | -1,31% | +25,23% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 25 | 68,00% | +9,07% | +0,14% | -5,18% | +20,02% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 26 | 84,62% | +9,45% | +7,69% | -5,24% | +20,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 26 | 84,62% | +9,45% | +7,69% | -5,24% | +20,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 24 | 91,67% | +7,91% | +10,66% | -5,36% | +19,30% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 26 | 46,15% | +9,45% | -9,45% | -5,24% | +20,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 20 | 55,00% | +7,30% | -7,30% | -5,27% | +16,83% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 11 | 0,00% | +18,98% | -18,98% | -6,73% | +36,47% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 11 | 0,00% | +18,98% | -18,98% | -6,73% | +36,47% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 11 | 0,00% | +18,98% | -18,98% | -6,73% | +36,47% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 11 | 0,00% | +18,98% | -18,98% | -6,73% | +36,47% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 11 | 0,00% | +18,98% | -18,98% | -6,73% | +36,47% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 10 | 0,00% | +19,37% | -19,37% | -6,60% | +36,59% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 46 | 56,52% | +0,66% | +0,53% | -0,02% | +1,59% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 48 | 58,33% | +0,33% | +0,32% | -0,28% | +1,23% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 51 | 56,86% | +0,38% | +0,23% | -0,24% | +1,27% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 50 | 52,00% | +0,33% | +0,31% | -0,32% | +1,19% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 34 | 52,94% | +0,55% | +0,50% | -0,24% | +1,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 45 | 51,11% | +1,42% | +1,27% | +0,49% | +2,52% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 47 | 46,81% | +0,99% | +0,47% | +0,05% | +1,80% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 50 | 46,00% | +0,95% | +0,42% | +0,04% | +1,85% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 49 | 42,86% | +0,87% | +0,25% | +0,01% | +1,97% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 33 | 51,52% | +1,02% | +0,99% | +0,13% | +2,00% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 44 | 59,09% | +2,28% | +2,08% | -1,17% | +4,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 46 | 50,00% | +1,70% | +1,06% | -1,52% | +3,95% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 49 | 48,98% | +1,62% | +0,98% | -1,50% | +3,91% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 48 | 50,00% | +1,45% | +0,09% | -1,58% | +3,62% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 32 | 56,25% | +1,43% | +1,26% | -1,49% | +3,61% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 42 | 64,29% | +3,99% | +3,86% | -1,65% | +7,39% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 44 | 56,82% | +3,18% | +1,94% | -2,02% | +6,57% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 47 | 55,32% | +3,02% | +1,77% | -2,02% | +6,40% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 46 | 50,00% | +3,03% | -0,44% | -2,20% | +6,28% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 30 | 63,33% | +2,35% | +2,16% | -2,00% | +5,51% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 40 | 70,00% | +5,68% | +5,81% | -1,90% | +9,57% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 42 | 64,29% | +4,71% | +3,20% | -2,30% | +8,65% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 45 | 64,44% | +4,39% | +2,99% | -2,33% | +8,34% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 44 | 43,18% | +4,35% | -1,35% | -2,51% | +8,28% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 28 | 57,14% | +2,69% | +2,76% | -2,36% | +6,58% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 37 | 70,27% | +7,71% | +7,92% | -2,24% | +11,86% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 39 | 64,10% | +6,62% | +5,45% | -2,74% | +10,53% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 42 | 61,90% | +6,13% | +5,07% | -2,79% | +10,06% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 41 | 46,34% | +5,44% | -2,76% | -3,02% | +9,57% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 25 | 60,00% | +2,22% | +2,37% | -2,99% | +6,63% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +3,45% | +3,45% | -2,62% | +8,30% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 33 | 75,76% | +10,42% | +11,52% | -3,05% | +15,81% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 36 | 86,11% | +9,94% | +10,98% | -3,28% | +14,70% | PRIMA CALIBRAZIONE |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 39 | 87,18% | +8,93% | +10,37% | -3,32% | +13,87% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 34 | 73,53% | +10,71% | +10,82% | -2,97% | +15,49% | PRIMA CALIBRAZIONE |
| SOL | 14g | Tecnico | CALIBRABILE | 37 | 29,73% | +6,92% | -7,47% | -3,83% | +11,87% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,19% | -1,19% | -4,25% | +5,07% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 27 | 70,37% | +12,82% | +11,51% | -4,78% | +18,61% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 30 | 83,33% | +13,10% | +14,96% | -4,70% | +18,17% | PRIMA CALIBRAZIONE |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 33 | 84,85% | +11,66% | +13,85% | -4,82% | +16,87% | PRIMA CALIBRAZIONE |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 28 | 67,86% | +14,22% | +14,83% | -4,40% | +19,38% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 32 | 37,50% | +9,67% | -10,96% | -5,06% | +14,69% | PRIMA CALIBRAZIONE |
| SOL | 21g | Classic technical | CALIBRABILE | 21 | 38,10% | +11,18% | -11,18% | -4,64% | +15,32% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | FEEDBACK RAPIDO |

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
