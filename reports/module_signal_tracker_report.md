# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-31 05:33 UTC

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

Segnali totali salvati: **156**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-31 | BTC | 78.005,28 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-31 | DOGE | 0.08279 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-31 | SOL | 102,56 | +6 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-30 | BTC | 78.145,28 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-30 | DOGE | 0.08501 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-30 | SOL | 105,04 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-29 | BTC | 77.645,39 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-29 | DOGE | 0.08513 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-29 | SOL | 103,94 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-28 | BTC | 79.717,91 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-28 | DOGE | 0.08759 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-28 | SOL | 106,61 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 52 | 51 | 50 | 49 | 47 | 45 | 42 | 38 | 33 | 24 | 9 | 0 |
| SOL | 52 | 51 | 50 | 49 | 47 | 45 | 42 | 38 | 33 | 24 | 9 | 0 |
| DOGE | 52 | 51 | 50 | 49 | 47 | 45 | 42 | 38 | 33 | 24 | 9 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-18 | 45g | 2026-09-01 | domani |
| SOL | 2026-07-18 | 45g | 2026-09-01 | domani |
| DOGE | 2026-07-18 | 45g | 2026-09-01 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 48 | 52,08% | +0,46% | +0,44% | PRIMA CALIBRAZIONE |
| BTC | 2g | 47 | 53,19% | +0,81% | +0,71% | PRIMA CALIBRAZIONE |
| BTC | 3g | 46 | 47,83% | +1,02% | +0,86% | PRIMA CALIBRAZIONE |
| BTC | 5g | 44 | 43,18% | +2,15% | +1,86% | PRIMA CALIBRAZIONE |
| BTC | 7g | 42 | 54,76% | +3,11% | +2,85% | PRIMA CALIBRAZIONE |
| BTC | 10g | 39 | 53,85% | +4,29% | +4,06% | PRIMA CALIBRAZIONE |
| BTC | 14g | 36 | 61,11% | +5,65% | +5,55% | PRIMA CALIBRAZIONE |
| BTC | 21g | 31 | 54,84% | +7,61% | +7,40% | PRIMA CALIBRAZIONE |
| BTC | 30g | 22 | 86,36% | +10,06% | +8,11% | FEEDBACK RAPIDO |
| BTC | 45g | 9 | 77,78% | +23,21% | +13,30% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 44 | 56,82% | +0,74% | +0,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | 43 | 53,49% | +1,56% | +1,40% | PRIMA CALIBRAZIONE |
| SOL | 3g | 42 | 59,52% | +2,49% | +2,28% | PRIMA CALIBRAZIONE |
| SOL | 5g | 40 | 65,00% | +4,26% | +4,12% | PRIMA CALIBRAZIONE |
| SOL | 7g | 38 | 68,42% | +5,84% | +5,98% | PRIMA CALIBRAZIONE |
| SOL | 10g | 35 | 68,57% | +7,60% | +7,82% | PRIMA CALIBRAZIONE |
| SOL | 14g | 31 | 74,19% | +8,90% | +10,07% | PRIMA CALIBRAZIONE |
| SOL | 21g | 26 | 69,23% | +11,88% | +10,51% | FEEDBACK RAPIDO |
| SOL | 30g | 18 | 44,44% | +10,97% | -0,02% | FEEDBACK RAPIDO |
| SOL | 45g | 8 | 37,50% | +32,59% | -11,37% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 48 | 45,83% | +0,42% | +0,35% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 47 | 51,06% | +0,85% | +0,90% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 46 | 47,83% | +1,29% | +1,60% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 45 | 53,33% | +2,18% | +2,74% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 43 | 62,79% | +3,24% | +4,27% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 40 | 65,00% | +4,00% | +5,56% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 36 | 69,44% | +5,08% | +7,66% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 31 | 74,19% | +6,24% | +4,97% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 23 | 69,57% | +8,28% | +0,08% | FEEDBACK RAPIDO |
| DOGE | 45g | 9 | 0,00% | +20,03% | -20,03% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 48 | 52,08% | +0,46% | +0,44% | +0,02% | +1,04% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 51 | 54,90% | +0,43% | +0,43% | +0,00% | +0,99% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 51 | 54,90% | +0,43% | +0,43% | +0,00% | +0,99% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 46 | 39,13% | +0,58% | +0,13% | +0,13% | +1,15% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 19 | 36,84% | +0,91% | +0,35% | +0,22% | +1,49% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 47 | 53,19% | +0,81% | +0,71% | +0,23% | +1,51% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 50 | 56,00% | +0,91% | +0,91% | +0,34% | +1,61% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 50 | 56,00% | +0,91% | +0,91% | +0,34% | +1,61% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 45 | 44,44% | +1,13% | +0,21% | +0,56% | +1,83% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 18 | 38,89% | +1,33% | +0,48% | +0,78% | +2,06% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 46 | 47,83% | +1,02% | +0,86% | -0,89% | +2,69% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 49 | 57,14% | +1,35% | +1,35% | -0,87% | +2,95% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 49 | 57,14% | +1,35% | +1,35% | -0,87% | +2,95% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 44 | 36,36% | +1,73% | -0,18% | -0,66% | +3,28% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 17 | 35,29% | +2,12% | -0,14% | -0,28% | +3,57% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 44 | 43,18% | +2,15% | +1,86% | -1,42% | +4,32% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 47 | 51,06% | +2,42% | +2,42% | -1,39% | +4,66% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 47 | 51,06% | +2,42% | +2,42% | -1,39% | +4,66% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 42 | 40,48% | +2,84% | -1,19% | -1,15% | +5,13% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 15 | 40,00% | +5,49% | -2,26% | -0,45% | +7,53% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 42 | 54,76% | +3,11% | +2,85% | -1,54% | +5,69% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 45 | 62,22% | +3,45% | +3,45% | -1,53% | +6,01% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 45 | 62,22% | +3,45% | +3,45% | -1,53% | +6,01% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 40 | 40,00% | +4,17% | -2,21% | -1,25% | +6,63% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 13 | 38,46% | +8,91% | -5,26% | -0,09% | +11,67% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +2,11% | +2,11% | -0,13% | +5,37% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 39 | 53,85% | +4,29% | +4,06% | -1,87% | +6,94% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 42 | 59,52% | +4,45% | +4,45% | -1,88% | +7,20% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 42 | 59,52% | +4,45% | +4,45% | -1,88% | +7,20% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 37 | 35,14% | +5,21% | -1,98% | -1,57% | +8,01% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 10 | 20,00% | +12,17% | -8,93% | -0,05% | +14,85% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 36 | 61,11% | +5,65% | +5,55% | -2,58% | +8,89% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 38 | 60,53% | +5,27% | +5,27% | -2,61% | +8,56% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 38 | 60,53% | +5,27% | +5,27% | -2,61% | +8,56% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 34 | 67,65% | +6,18% | +6,18% | -2,40% | +9,29% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 33 | 57,58% | +6,26% | +0,33% | -2,33% | +9,61% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 8 | 25,00% | +12,28% | -12,28% | -0,83% | +16,12% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 31 | 54,84% | +7,61% | +7,40% | -2,98% | +11,27% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 33 | 63,64% | +7,09% | +7,09% | -3,02% | +10,75% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 33 | 63,64% | +7,09% | +7,09% | -3,02% | +10,75% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 29 | 68,97% | +8,25% | +8,25% | -2,82% | +11,90% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 28 | 35,71% | +8,07% | +1,14% | -2,76% | +11,80% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 4 | 0,00% | +11,68% | -11,68% | -1,55% | +14,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 22 | 86,36% | +10,06% | +8,11% | -3,09% | +13,87% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 24 | 79,17% | +9,90% | +9,90% | -3,14% | +13,82% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 24 | 79,17% | +9,90% | +9,90% | -3,14% | +13,82% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 20 | 80,00% | +10,93% | +10,93% | -2,87% | +15,17% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 19 | 31,58% | +9,16% | -6,76% | -2,79% | +13,56% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 3 | 0,00% | +24,16% | -24,16% | -1,93% | +28,09% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 9 | 77,78% | +23,21% | +13,30% | -2,48% | +26,87% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 9 | 100,00% | +23,21% | +23,21% | -2,48% | +26,87% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 9 | 100,00% | +23,21% | +23,21% | -2,48% | +26,87% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 9 | 100,00% | +23,21% | +23,21% | -2,48% | +26,87% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 8 | 37,50% | +23,55% | -6,16% | -2,38% | +27,17% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 48 | 45,83% | +0,42% | +0,35% | -0,18% | +1,47% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 50 | 60,00% | +0,28% | +0,68% | -0,33% | +1,27% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 50 | 60,00% | +0,28% | +0,68% | -0,33% | +1,27% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 44 | 52,27% | +0,17% | +0,36% | -0,46% | +1,15% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 31 | 41,94% | +0,27% | -0,51% | -0,38% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +2,48% | +2,09% | +0,94% | +3,13% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 47 | 51,06% | +0,85% | +0,90% | +0,09% | +2,18% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 49 | 55,10% | +0,64% | +1,12% | -0,09% | +1,89% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 49 | 55,10% | +0,64% | +1,12% | -0,09% | +1,89% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 43 | 58,14% | +0,16% | +0,59% | -0,54% | +1,40% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +3,38% | +3,05% | +2,44% | +5,44% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 46 | 47,83% | +1,29% | +1,60% | -1,47% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 48 | 54,17% | +1,08% | +1,63% | -1,65% | +3,80% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 48 | 54,17% | +1,08% | +1,63% | -1,65% | +3,80% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 42 | 45,24% | +0,05% | +0,45% | -1,97% | +2,63% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 31 | 32,26% | +1,30% | -2,13% | -1,89% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +3,59% | +3,29% | -0,23% | +7,51% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 45 | 53,33% | +2,18% | +2,74% | -2,35% | +6,49% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 46 | 52,17% | +2,15% | +2,70% | -2,33% | +6,26% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 46 | 52,17% | +2,15% | +2,70% | -2,33% | +6,26% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 40 | 57,50% | +0,83% | +0,50% | -2,85% | +4,95% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | +2,23% | +2,00% | -1,09% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 43 | 62,79% | +3,24% | +4,27% | -2,52% | +8,73% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 45 | 60,00% | +2,99% | +3,94% | -2,61% | +8,38% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 45 | 60,00% | +2,99% | +3,94% | -2,61% | +8,38% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 38 | 60,53% | +1,53% | +1,56% | -3,12% | +6,72% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 30 | 40,00% | +3,19% | -4,62% | -2,99% | +8,53% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | +0,39% | +0,24% | -1,74% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 40 | 65,00% | +4,00% | +5,56% | -2,55% | +10,67% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 42 | 64,29% | +3,73% | +5,23% | -2,64% | +10,21% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 42 | 64,29% | +3,73% | +5,23% | -2,64% | +10,21% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 35 | 68,57% | +1,49% | +2,58% | -3,20% | +7,51% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 27 | 48,15% | +3,79% | -3,79% | -2,82% | +10,40% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,56% | +2,95% | +0,53% | +11,40% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 36 | 69,44% | +5,08% | +7,66% | -3,66% | +12,26% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 38 | 73,68% | +4,70% | +7,17% | -3,70% | +11,67% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 38 | 73,68% | +4,70% | +7,17% | -3,70% | +11,67% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 36 | 75,00% | +5,05% | +7,48% | -3,70% | +12,07% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 33 | 66,67% | +1,58% | +1,05% | -4,09% | +8,18% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 25 | 56,00% | +2,94% | -2,94% | -3,94% | +9,85% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,47% | +2,65% | -1,31% | +16,91% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 31 | 74,19% | +6,24% | +4,97% | -4,39% | +14,84% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 33 | 84,85% | +6,48% | +10,06% | -4,40% | +15,24% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 33 | 84,85% | +6,48% | +10,06% | -4,40% | +15,24% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 31 | 87,10% | +6,98% | +10,63% | -4,44% | +15,94% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 30 | 63,33% | +5,01% | -5,01% | -4,70% | +12,46% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 22 | 68,18% | +2,23% | -2,23% | -4,78% | +9,45% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,49% | -0,95% | -1,31% | +25,23% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 23 | 69,57% | +8,28% | +0,08% | -5,42% | +18,04% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 24 | 83,33% | +8,73% | +6,83% | -5,48% | +18,84% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 24 | 83,33% | +8,73% | +6,83% | -5,48% | +18,84% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 22 | 90,91% | +6,98% | +9,99% | -5,63% | +17,16% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 24 | 50,00% | +8,73% | -8,73% | -5,48% | +18,84% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 20 | 55,00% | +7,30% | -7,30% | -5,27% | +16,83% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 9 | 0,00% | +20,03% | -20,03% | -6,87% | +36,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 9 | 0,00% | +20,03% | -20,03% | -6,87% | +36,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 9 | 0,00% | +20,03% | -20,03% | -6,87% | +36,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 9 | 0,00% | +20,03% | -20,03% | -6,87% | +36,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 9 | 0,00% | +20,03% | -20,03% | -6,87% | +36,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 8 | 0,00% | +20,65% | -20,65% | -6,72% | +36,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 44 | 56,82% | +0,74% | +0,60% | +0,09% | +1,71% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 46 | 58,70% | +0,39% | +0,38% | -0,19% | +1,33% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 49 | 57,14% | +0,44% | +0,29% | -0,15% | +1,36% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 48 | 52,08% | +0,39% | +0,36% | -0,24% | +1,28% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 32 | 53,12% | +0,65% | +0,60% | -0,11% | +1,67% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 43 | 53,49% | +1,56% | +1,40% | +0,65% | +2,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 45 | 48,89% | +1,10% | +0,56% | +0,18% | +1,94% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 48 | 47,92% | +1,05% | +0,51% | +0,16% | +1,99% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 47 | 44,68% | +0,98% | +0,33% | +0,13% | +2,12% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 31 | 54,84% | +1,19% | +1,16% | +0,33% | +2,22% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 42 | 59,52% | +2,49% | +2,28% | -1,01% | +4,67% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 44 | 50,00% | +1,88% | +1,21% | -1,38% | +4,06% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 47 | 48,94% | +1,78% | +1,11% | -1,37% | +4,02% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 46 | 50,00% | +1,61% | +0,19% | -1,45% | +3,71% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 30 | 56,67% | +1,67% | +1,49% | -1,28% | +3,75% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 40 | 65,00% | +4,26% | +4,12% | -1,55% | +7,52% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 42 | 57,14% | +3,39% | +2,10% | -1,94% | +6,65% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 45 | 55,56% | +3,21% | +1,91% | -1,95% | +6,47% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 44 | 50,00% | +3,23% | -0,40% | -2,13% | +6,35% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 28 | 64,29% | +2,62% | +2,42% | -1,88% | +5,56% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 38 | 68,42% | +5,84% | +5,98% | -1,87% | +9,52% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 40 | 62,50% | +4,82% | +3,23% | -2,29% | +8,56% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 43 | 62,79% | +4,48% | +3,01% | -2,32% | +8,24% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 42 | 40,48% | +4,44% | -1,53% | -2,51% | +8,17% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 26 | 53,85% | +2,70% | +2,78% | -2,35% | +6,28% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +3,96% | +3,96% | -2,17% | +8,29% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 35 | 68,57% | +7,60% | +7,82% | -2,33% | +11,50% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 37 | 67,57% | +6,46% | +6,26% | -2,85% | +10,12% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 40 | 65,00% | +5,96% | +5,81% | -2,89% | +9,66% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 39 | 43,59% | +5,23% | -3,39% | -3,14% | +9,13% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 23 | 56,52% | +1,58% | +1,74% | -3,19% | +5,64% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +3,45% | +3,45% | -2,62% | +8,30% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 31 | 74,19% | +8,90% | +10,07% | -3,60% | +13,98% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 34 | 85,29% | +8,52% | +9,62% | -3,78% | +12,96% | PRIMA CALIBRAZIONE |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 37 | 86,49% | +7,58% | +9,09% | -3,79% | +12,23% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 32 | 71,88% | +9,26% | +9,37% | -3,49% | +13,69% | PRIMA CALIBRAZIONE |
| SOL | 14g | Tecnico | CALIBRABILE | 36 | 30,56% | +6,07% | -6,64% | -3,97% | +10,94% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,19% | -1,19% | -4,25% | +5,07% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 26 | 69,23% | +11,88% | +10,51% | -4,89% | +17,58% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 29 | 82,76% | +12,26% | +14,18% | -4,79% | +17,23% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 32 | 84,38% | +10,85% | +13,11% | -4,91% | +15,98% | PRIMA CALIBRAZIONE |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 27 | 66,67% | +13,36% | +13,99% | -4,49% | +18,42% | FEEDBACK RAPIDO |
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
