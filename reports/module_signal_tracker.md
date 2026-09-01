# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-01 05:33 UTC

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

Segnali totali salvati: **159**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-01 | BTC | 79.026,52 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-01 | DOGE | 0.08350 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-01 | SOL | 104,07 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-31 | BTC | 78.005,28 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-31 | DOGE | 0.08279 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-31 | SOL | 102,56 | +6 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-30 | BTC | 78.145,28 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-30 | DOGE | 0.08501 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-30 | SOL | 105,04 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-29 | BTC | 77.645,39 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-29 | DOGE | 0.08513 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-29 | SOL | 103,94 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 53 | 52 | 51 | 50 | 48 | 46 | 43 | 39 | 34 | 25 | 10 | 0 |
| SOL | 53 | 52 | 51 | 50 | 48 | 46 | 43 | 39 | 34 | 25 | 10 | 0 |
| DOGE | 53 | 52 | 51 | 50 | 48 | 46 | 43 | 39 | 34 | 25 | 10 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-19 | 45g | 2026-09-02 | domani |
| SOL | 2026-07-19 | 45g | 2026-09-02 | domani |
| DOGE | 2026-07-19 | 45g | 2026-09-02 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 49 | 53,06% | +0,48% | +0,45% | PRIMA CALIBRAZIONE |
| BTC | 2g | 48 | 54,17% | +0,82% | +0,72% | PRIMA CALIBRAZIONE |
| BTC | 3g | 47 | 48,94% | +1,03% | +0,88% | PRIMA CALIBRAZIONE |
| BTC | 5g | 45 | 44,44% | +2,11% | +1,83% | PRIMA CALIBRAZIONE |
| BTC | 7g | 43 | 53,49% | +2,99% | +2,73% | PRIMA CALIBRAZIONE |
| BTC | 10g | 40 | 55,00% | +4,24% | +4,02% | PRIMA CALIBRAZIONE |
| BTC | 14g | 36 | 61,11% | +5,65% | +5,55% | PRIMA CALIBRAZIONE |
| BTC | 21g | 32 | 56,25% | +8,12% | +7,91% | PRIMA CALIBRAZIONE |
| BTC | 30g | 23 | 86,96% | +10,70% | +8,83% | FEEDBACK RAPIDO |
| BTC | 45g | 9 | 77,78% | +23,21% | +13,30% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 45 | 57,78% | +0,76% | +0,62% | PRIMA CALIBRAZIONE |
| SOL | 2g | 44 | 52,27% | +1,51% | +1,35% | PRIMA CALIBRAZIONE |
| SOL | 3g | 43 | 60,47% | +2,44% | +2,23% | PRIMA CALIBRAZIONE |
| SOL | 5g | 41 | 65,85% | +4,23% | +4,10% | PRIMA CALIBRAZIONE |
| SOL | 7g | 39 | 69,23% | +5,74% | +5,87% | PRIMA CALIBRAZIONE |
| SOL | 10g | 36 | 69,44% | +7,71% | +7,92% | PRIMA CALIBRAZIONE |
| SOL | 14g | 32 | 75,00% | +9,79% | +10,93% | PRIMA CALIBRAZIONE |
| SOL | 21g | 27 | 70,37% | +12,82% | +11,51% | FEEDBACK RAPIDO |
| SOL | 30g | 19 | 47,37% | +12,59% | +2,18% | FEEDBACK RAPIDO |
| SOL | 45g | 9 | 33,33% | +33,29% | -14,42% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 48 | 45,83% | +0,42% | +0,35% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 48 | 50,00% | +0,79% | +0,84% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 47 | 46,81% | +1,23% | +1,53% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 46 | 54,35% | +2,07% | +2,75% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 44 | 61,36% | +2,93% | +3,94% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 41 | 63,41% | +3,72% | +5,24% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 37 | 70,27% | +5,48% | +7,99% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 32 | 75,00% | +6,66% | +5,42% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 24 | 70,83% | +8,73% | +0,87% | FEEDBACK RAPIDO |
| DOGE | 45g | 10 | 0,00% | +19,57% | -19,57% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 49 | 53,06% | +0,48% | +0,45% | +0,02% | +1,05% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 52 | 55,77% | +0,45% | +0,45% | +0,01% | +1,00% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 52 | 55,77% | +0,45% | +0,45% | +0,01% | +1,00% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 47 | 40,43% | +0,60% | +0,16% | +0,13% | +1,15% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 20 | 40,00% | +0,93% | +0,40% | +0,22% | +1,48% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 48 | 54,17% | +0,82% | +0,72% | +0,23% | +1,51% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 51 | 56,86% | +0,92% | +0,92% | +0,34% | +1,60% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 51 | 56,86% | +0,92% | +0,92% | +0,34% | +1,60% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 46 | 45,65% | +1,13% | +0,23% | +0,55% | +1,81% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 19 | 42,11% | +1,32% | +0,52% | +0,74% | +2,00% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 47 | 48,94% | +1,03% | +0,88% | -0,89% | +2,68% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 50 | 58,00% | +1,36% | +1,36% | -0,87% | +2,93% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 50 | 58,00% | +1,36% | +1,36% | -0,87% | +2,93% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 45 | 37,78% | +1,73% | -0,14% | -0,66% | +3,26% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 18 | 38,89% | +2,10% | -0,03% | -0,31% | +3,50% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 45 | 44,44% | +2,11% | +1,83% | -1,44% | +4,30% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 48 | 52,08% | +2,38% | +2,38% | -1,41% | +4,64% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 48 | 52,08% | +2,38% | +2,38% | -1,41% | +4,64% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 43 | 41,86% | +2,78% | -1,15% | -1,17% | +5,09% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 16 | 43,75% | +5,17% | -2,09% | -0,56% | +7,27% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 43 | 53,49% | +2,99% | +2,73% | -1,62% | +5,57% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 46 | 60,87% | +3,33% | +3,33% | -1,61% | +5,90% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 46 | 60,87% | +3,33% | +3,33% | -1,61% | +5,90% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 41 | 39,02% | +4,01% | -2,21% | -1,34% | +6,48% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 14 | 35,71% | +8,12% | -5,04% | -0,42% | +10,89% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 40 | 55,00% | +4,24% | +4,02% | -1,87% | +6,90% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 43 | 60,47% | +4,40% | +4,40% | -1,88% | +7,16% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 43 | 60,47% | +4,40% | +4,40% | -1,88% | +7,16% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 38 | 36,84% | +5,13% | -1,86% | -1,58% | +7,94% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 11 | 27,27% | +11,29% | -7,89% | -0,22% | +14,00% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 36 | 61,11% | +5,65% | +5,55% | -2,58% | +8,89% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 39 | 61,54% | +5,73% | +5,73% | -2,55% | +9,03% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 39 | 61,54% | +5,73% | +5,73% | -2,55% | +9,03% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 34 | 67,65% | +6,18% | +6,18% | -2,40% | +9,29% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 34 | 55,88% | +6,76% | -0,37% | -2,27% | +10,11% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 8 | 25,00% | +12,28% | -12,28% | -0,83% | +16,12% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 32 | 56,25% | +8,12% | +7,91% | -2,96% | +11,77% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 34 | 64,71% | +7,57% | +7,57% | -3,00% | +11,24% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 34 | 64,71% | +7,57% | +7,57% | -3,00% | +11,24% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 30 | 70,00% | +8,77% | +8,77% | -2,80% | +12,42% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 29 | 37,93% | +8,61% | +1,92% | -2,74% | +12,34% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 4 | 0,00% | +11,68% | -11,68% | -1,55% | +14,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 23 | 86,96% | +10,70% | +8,83% | -3,04% | +14,50% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 25 | 80,00% | +10,49% | +10,49% | -3,09% | +14,40% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 25 | 80,00% | +10,49% | +10,49% | -3,09% | +14,40% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 21 | 80,95% | +11,59% | +11,59% | -2,82% | +15,80% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 20 | 30,00% | +9,93% | -7,66% | -2,74% | +14,29% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 3 | 0,00% | +24,16% | -24,16% | -1,93% | +28,09% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 9 | 77,78% | +23,21% | +13,30% | -2,48% | +26,87% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 10 | 100,00% | +23,26% | +23,26% | -2,50% | +26,92% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 10 | 100,00% | +23,26% | +23,26% | -2,50% | +26,92% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 10 | 100,00% | +23,26% | +23,26% | -2,50% | +26,92% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 9 | 33,33% | +23,57% | -8,11% | -2,41% | +27,19% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 48 | 45,83% | +0,42% | +0,35% | -0,18% | +1,47% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 51 | 58,82% | +0,29% | +0,65% | -0,32% | +1,26% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 51 | 58,82% | +0,29% | +0,65% | -0,32% | +1,26% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 45 | 53,33% | +0,18% | +0,37% | -0,45% | +1,14% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 31 | 41,94% | +0,27% | -0,51% | -0,38% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +2,48% | +2,09% | +0,94% | +3,13% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 48 | 50,00% | +0,79% | +0,84% | +0,03% | +2,10% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 50 | 56,00% | +0,60% | +1,13% | -0,14% | +1,82% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 50 | 56,00% | +0,60% | +1,13% | -0,14% | +1,82% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 44 | 56,82% | +0,12% | +0,54% | -0,59% | +1,32% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +3,38% | +3,05% | +2,44% | +5,44% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 47 | 46,81% | +1,23% | +1,53% | -1,53% | +4,14% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 49 | 55,10% | +1,02% | +1,63% | -1,71% | +3,76% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 49 | 55,10% | +1,02% | +1,63% | -1,71% | +3,76% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 43 | 44,19% | +0,00% | +0,40% | -2,03% | +2,61% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 31 | 32,26% | +1,30% | -2,13% | -1,89% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +2,90% | +2,64% | -0,79% | +6,76% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 46 | 54,35% | +2,07% | +2,75% | -2,42% | +6,44% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 47 | 53,19% | +2,03% | +2,71% | -2,40% | +6,22% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 47 | 53,19% | +2,03% | +2,71% | -2,40% | +6,22% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 41 | 56,10% | +0,73% | +0,41% | -2,93% | +4,94% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | +2,23% | +2,00% | -1,09% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 44 | 61,36% | +2,93% | +3,94% | -2,75% | +8,46% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 46 | 58,70% | +2,70% | +3,63% | -2,83% | +8,13% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 46 | 58,70% | +2,70% | +3,63% | -2,83% | +8,13% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 39 | 58,97% | +1,23% | +1,26% | -3,36% | +6,47% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | +0,39% | +0,24% | -1,74% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 41 | 63,41% | +3,72% | +5,24% | -2,73% | +10,52% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 43 | 62,79% | +3,46% | +4,94% | -2,81% | +10,07% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 43 | 62,79% | +3,46% | +4,94% | -2,81% | +10,07% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 36 | 66,67% | +1,24% | +2,30% | -3,39% | +7,43% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 28 | 46,43% | +3,39% | -3,92% | -3,08% | +10,19% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +1,71% | +1,21% | -1,24% | +10,26% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 37 | 70,27% | +5,48% | +7,99% | -3,55% | +13,10% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 39 | 74,36% | +5,09% | +7,49% | -3,60% | +12,48% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 39 | 74,36% | +5,09% | +7,49% | -3,60% | +12,48% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 37 | 75,68% | +5,45% | +7,81% | -3,60% | +12,91% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 33 | 66,67% | +1,58% | +1,05% | -4,09% | +8,18% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 26 | 53,85% | +3,59% | -3,59% | -3,78% | +11,14% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,47% | +2,65% | -1,31% | +16,91% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 32 | 75,00% | +6,66% | +5,42% | -4,30% | +15,73% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 34 | 85,29% | +6,86% | +10,34% | -4,31% | +16,06% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 34 | 85,29% | +6,86% | +10,34% | -4,31% | +16,06% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 32 | 87,50% | +7,37% | +10,91% | -4,34% | +16,79% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 30 | 63,33% | +5,01% | -5,01% | -4,70% | +12,46% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 22 | 68,18% | +2,23% | -2,23% | -4,78% | +9,45% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,49% | -0,95% | -1,31% | +25,23% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 24 | 70,83% | +8,73% | +0,87% | -5,30% | +19,06% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 25 | 84,00% | +9,14% | +7,31% | -5,36% | +19,78% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 25 | 84,00% | +9,14% | +7,31% | -5,36% | +19,78% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 23 | 91,30% | +7,50% | +10,38% | -5,50% | +18,26% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 25 | 48,00% | +9,14% | -9,14% | -5,36% | +19,78% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 20 | 55,00% | +7,30% | -7,30% | -5,27% | +16,83% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 10 | 0,00% | +19,57% | -19,57% | -6,79% | +36,31% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 10 | 0,00% | +19,57% | -19,57% | -6,79% | +36,31% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 10 | 0,00% | +19,57% | -19,57% | -6,79% | +36,31% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 10 | 0,00% | +19,57% | -19,57% | -6,79% | +36,31% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 10 | 0,00% | +19,57% | -19,57% | -6,79% | +36,31% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 9 | 0,00% | +20,07% | -20,07% | -6,65% | +36,43% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 45 | 57,78% | +0,76% | +0,62% | +0,09% | +1,70% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 47 | 59,57% | +0,42% | +0,40% | -0,18% | +1,33% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 50 | 58,00% | +0,46% | +0,31% | -0,14% | +1,36% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 49 | 53,06% | +0,41% | +0,39% | -0,23% | +1,28% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 33 | 54,55% | +0,68% | +0,62% | -0,09% | +1,66% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 44 | 52,27% | +1,51% | +1,35% | +0,59% | +2,62% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 46 | 47,83% | +1,06% | +0,53% | +0,13% | +1,88% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 49 | 46,94% | +1,01% | +0,48% | +0,12% | +1,93% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 48 | 43,75% | +0,94% | +0,30% | +0,08% | +2,05% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 32 | 53,12% | +1,12% | +1,09% | +0,25% | +2,12% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 43 | 60,47% | +2,44% | +2,23% | -1,05% | +4,64% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 45 | 51,11% | +1,84% | +1,19% | -1,42% | +4,04% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 48 | 50,00% | +1,75% | +1,09% | -1,41% | +4,00% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 47 | 51,06% | +1,58% | +0,18% | -1,49% | +3,70% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 31 | 58,06% | +1,62% | +1,44% | -1,34% | +3,73% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 41 | 65,85% | +4,23% | +4,10% | -1,51% | +7,55% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 43 | 58,14% | +3,39% | +2,12% | -1,90% | +6,70% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 46 | 56,52% | +3,21% | +1,94% | -1,91% | +6,52% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 45 | 51,11% | +3,23% | -0,31% | -2,08% | +6,41% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 29 | 65,52% | +2,64% | +2,44% | -1,82% | +5,68% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 39 | 69,23% | +5,74% | +5,87% | -2,00% | +9,47% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 41 | 63,41% | +4,74% | +3,19% | -2,40% | +8,54% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 44 | 63,64% | +4,41% | +2,98% | -2,42% | +8,22% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 43 | 41,86% | +4,37% | -1,46% | -2,62% | +8,15% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 27 | 55,56% | +2,66% | +2,73% | -2,52% | +6,32% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +3,37% | +3,37% | -3,38% | +8,08% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 36 | 69,44% | +7,71% | +7,92% | -2,31% | +11,68% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 38 | 65,79% | +6,59% | +5,79% | -2,82% | +10,33% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 41 | 63,41% | +6,09% | +5,39% | -2,86% | +9,86% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 40 | 45,00% | +5,38% | -3,02% | -3,10% | +9,35% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 24 | 58,33% | +1,99% | +2,14% | -3,13% | +6,15% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +3,45% | +3,45% | -2,62% | +8,30% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 32 | 75,00% | +9,79% | +10,93% | -3,44% | +14,96% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 35 | 85,71% | +9,35% | +10,42% | -3,64% | +13,89% | PRIMA CALIBRAZIONE |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 38 | 86,84% | +8,37% | +9,84% | -3,66% | +13,10% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 33 | 72,73% | +10,12% | +10,22% | -3,35% | +14,65% | PRIMA CALIBRAZIONE |
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
