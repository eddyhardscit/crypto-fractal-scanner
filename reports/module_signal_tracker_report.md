# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-26 05:32 UTC

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

Segnali totali salvati: **141**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-26 | BTC | 79.104,96 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-26 | DOGE | 0.08675 | +1 | 0 | 0 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-26 | SOL | 96,96 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-25 | BTC | 80.778,18 | +6 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-25 | DOGE | 0.09299 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-25 | SOL | 102,40 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-24 | BTC | 76.958,14 | +6 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-24 | DOGE | 0.09174 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-24 | SOL | 93,82 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-23 | BTC | 76.280,85 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-23 | DOGE | 0.09044 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-23 | SOL | 93,05 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 47 | 46 | 45 | 44 | 42 | 40 | 37 | 34 | 28 | 19 | 4 | 0 |
| SOL | 47 | 46 | 45 | 44 | 42 | 40 | 37 | 34 | 28 | 19 | 4 | 0 |
| DOGE | 47 | 46 | 45 | 44 | 42 | 40 | 37 | 34 | 28 | 19 | 4 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-13 | 45g | 2026-08-27 | domani |
| SOL | 2026-07-13 | 45g | 2026-08-27 | domani |
| DOGE | 2026-07-13 | 45g | 2026-08-27 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 43 | 53,49% | +0,55% | +0,52% | PRIMA CALIBRAZIONE |
| BTC | 2g | 42 | 54,76% | +1,02% | +0,90% | PRIMA CALIBRAZIONE |
| BTC | 3g | 41 | 51,22% | +1,23% | +1,06% | PRIMA CALIBRAZIONE |
| BTC | 5g | 39 | 41,03% | +2,35% | +2,03% | PRIMA CALIBRAZIONE |
| BTC | 7g | 37 | 48,65% | +2,89% | +2,60% | PRIMA CALIBRAZIONE |
| BTC | 10g | 35 | 48,57% | +3,04% | +2,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | 32 | 56,25% | +3,32% | +3,21% | PRIMA CALIBRAZIONE |
| BTC | 21g | 26 | 46,15% | +5,01% | +4,76% | FEEDBACK RAPIDO |
| BTC | 30g | 17 | 88,24% | +6,24% | +6,53% | FEEDBACK RAPIDO |
| BTC | 45g | 4 | 100,00% | +22,81% | +22,81% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 39 | 56,41% | +0,69% | +0,53% | PRIMA CALIBRAZIONE |
| SOL | 2g | 38 | 55,26% | +1,54% | +1,35% | PRIMA CALIBRAZIONE |
| SOL | 3g | 37 | 56,76% | +2,31% | +2,07% | PRIMA CALIBRAZIONE |
| SOL | 5g | 35 | 60,00% | +3,67% | +3,52% | PRIMA CALIBRAZIONE |
| SOL | 7g | 33 | 63,64% | +4,57% | +4,73% | PRIMA CALIBRAZIONE |
| SOL | 10g | 30 | 63,33% | +3,93% | +4,19% | PRIMA CALIBRAZIONE |
| SOL | 14g | 27 | 70,37% | +4,48% | +5,83% | FEEDBACK RAPIDO |
| SOL | 21g | 21 | 61,90% | +5,44% | +3,75% | FEEDBACK RAPIDO |
| SOL | 30g | 14 | 42,86% | +2,59% | +0,37% | FEEDBACK RAPIDO |
| SOL | 45g | 3 | 66,67% | +25,89% | +8,04% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 44 | 50,00% | +0,50% | +0,49% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 43 | 51,16% | +1,17% | +1,16% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 42 | 50,00% | +1,78% | +2,05% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 40 | 60,00% | +3,15% | +3,78% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 38 | 65,79% | +3,66% | +4,82% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 35 | 60,00% | +2,15% | +3,93% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 32 | 65,62% | +2,98% | +5,88% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 26 | 69,23% | +3,15% | +1,62% | FEEDBACK RAPIDO |
| DOGE | 30g | 18 | 72,22% | +4,53% | -1,57% | FEEDBACK RAPIDO |
| DOGE | 45g | 4 | 0,00% | +23,27% | -23,27% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 43 | 53,49% | +0,55% | +0,52% | +0,08% | +1,13% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 46 | 56,52% | +0,50% | +0,50% | +0,06% | +1,06% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 46 | 56,52% | +0,50% | +0,50% | +0,06% | +1,06% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 41 | 39,02% | +0,68% | +0,18% | +0,21% | +1,25% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 14 | 35,71% | +1,33% | +0,58% | +0,48% | +1,91% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 42 | 54,76% | +1,02% | +0,90% | +0,43% | +1,74% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 45 | 57,78% | +1,12% | +1,12% | +0,54% | +1,83% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 45 | 57,78% | +1,12% | +1,12% | +0,54% | +1,83% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 40 | 45,00% | +1,39% | +0,35% | +0,81% | +2,10% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 13 | 38,46% | +2,19% | +1,03% | +1,63% | +2,98% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +4,54% | +4,54% | +3,15% | +5,05% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 41 | 51,22% | +1,23% | +1,06% | -0,79% | +2,88% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 44 | 61,36% | +1,59% | +1,59% | -0,78% | +3,15% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 44 | 61,36% | +1,59% | +1,59% | -0,78% | +3,15% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 39 | 38,46% | +2,05% | -0,11% | -0,53% | +3,56% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 12 | 41,67% | +3,32% | +0,11% | +0,29% | +4,59% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +2,79% | +2,79% | +0,99% | +4,54% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 39 | 41,03% | +2,35% | +2,03% | -1,41% | +4,35% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 42 | 50,00% | +2,64% | +2,64% | -1,38% | +4,74% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 42 | 50,00% | +2,64% | +2,64% | -1,38% | +4,74% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 37 | 37,84% | +3,15% | -1,43% | -1,10% | +5,27% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 10 | 30,00% | +7,96% | -3,66% | +0,06% | +9,26% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 37 | 48,65% | +2,89% | +2,60% | -1,87% | +5,31% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 40 | 57,50% | +3,29% | +3,29% | -1,83% | +5,70% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 40 | 57,50% | +3,29% | +3,29% | -1,83% | +5,70% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 35 | 31,43% | +4,08% | -3,20% | -1,55% | +6,36% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 8 | 0,00% | +11,51% | -11,51% | -0,67% | +13,66% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 35 | 48,57% | +3,04% | +2,78% | -2,47% | +5,46% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 37 | 54,05% | +2,75% | +2,75% | -2,50% | +5,30% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 37 | 54,05% | +2,75% | +2,75% | -2,50% | +5,30% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 33 | 60,61% | +3,33% | +3,33% | -2,39% | +5,66% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 32 | 31,25% | +3,36% | -1,94% | -2,24% | +5,94% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 7 | 0,00% | +11,65% | -11,65% | -1,00% | +13,61% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 32 | 56,25% | +3,32% | +3,21% | -2,89% | +6,39% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 34 | 55,88% | +3,03% | +3,03% | -2,91% | +6,17% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 34 | 55,88% | +3,03% | +3,03% | -2,91% | +6,17% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 30 | 63,33% | +3,77% | +3,77% | -2,71% | +6,68% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 29 | 65,52% | +3,77% | +3,72% | -2,64% | +6,95% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 26 | 46,15% | +5,01% | +4,76% | -2,89% | +8,53% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 28 | 57,14% | +4,57% | +4,57% | -2,94% | +8,11% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 28 | 57,14% | +4,57% | +4,57% | -2,94% | +8,11% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 24 | 62,50% | +5,57% | +5,57% | -2,68% | +9,07% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 23 | 21,74% | +5,23% | -3,21% | -2,61% | +8,82% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 4 | 0,00% | +11,68% | -11,68% | -1,55% | +14,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 17 | 88,24% | +6,24% | +6,53% | -3,31% | +9,86% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 19 | 73,68% | +6,43% | +6,43% | -3,35% | +10,21% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 19 | 73,68% | +6,43% | +6,43% | -3,35% | +10,21% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 15 | 73,33% | +6,89% | +6,89% | -3,04% | +11,05% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 15 | 40,00% | +5,34% | -2,30% | -2,97% | +9,75% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 4 | 100,00% | +22,81% | +22,81% | -3,09% | +25,48% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | +22,81% | +22,81% | -3,09% | +25,48% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | +22,81% | +22,81% | -3,09% | +25,48% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 4 | 100,00% | +22,81% | +22,81% | -3,09% | +25,48% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 3 | 33,33% | +23,57% | -7,60% | -3,03% | +25,83% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 44 | 50,00% | +0,50% | +0,49% | -0,11% | +1,53% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 46 | 58,70% | +0,39% | +0,66% | -0,22% | +1,39% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 46 | 58,70% | +0,39% | +0,66% | -0,22% | +1,39% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 39 | 56,41% | +0,31% | +0,53% | -0,35% | +1,28% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 31 | 41,94% | +0,27% | -0,51% | -0,38% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +2,86% | +2,41% | +1,15% | +3,54% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 43 | 51,16% | +1,17% | +1,16% | +0,41% | +2,51% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 45 | 53,33% | +1,02% | +1,23% | +0,27% | +2,33% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 45 | 53,33% | +1,02% | +1,23% | +0,27% | +2,33% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 38 | 63,16% | +0,53% | +1,02% | -0,17% | +1,79% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 30 | 46,67% | +0,94% | -1,00% | +0,14% | +1,89% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +4,25% | +3,88% | +3,39% | +6,58% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 42 | 50,00% | +1,78% | +2,05% | -1,11% | +4,58% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 44 | 54,55% | +1,60% | +1,89% | -1,22% | +4,34% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 44 | 54,55% | +1,60% | +1,89% | -1,22% | +4,34% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 37 | 51,35% | +0,61% | +1,07% | -1,49% | +3,11% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 29 | 34,48% | +1,80% | -1,87% | -1,45% | +4,56% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +5,19% | +4,84% | +0,90% | +8,54% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 40 | 60,00% | +3,15% | +3,78% | -1,72% | +7,06% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 42 | 57,14% | +2,91% | +3,52% | -1,82% | +6,72% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 42 | 57,14% | +2,91% | +3,52% | -1,82% | +6,72% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 35 | 65,71% | +1,74% | +1,38% | -2,21% | +5,38% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 27 | 44,44% | +3,71% | -3,71% | -1,98% | +7,48% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +5,46% | +5,14% | +1,28% | +11,40% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 38 | 65,79% | +3,66% | +4,82% | -2,44% | +8,18% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 40 | 62,50% | +3,36% | +4,43% | -2,55% | +7,82% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 40 | 62,50% | +3,36% | +4,43% | -2,55% | +7,82% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 33 | 63,64% | +1,75% | +1,79% | -3,12% | +5,79% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 27 | 44,44% | +4,34% | -4,34% | -2,39% | +9,14% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,63% | +0,36% | -0,50% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 35 | 60,00% | +2,15% | +3,93% | -3,27% | +6,93% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 37 | 59,46% | +1,94% | +3,65% | -3,34% | +6,61% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 37 | 59,46% | +1,94% | +3,65% | -3,34% | +6,61% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +2,10% | +3,81% | -3,33% | +6,72% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 32 | 68,75% | +0,47% | +3,10% | -3,68% | +5,15% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 24 | 54,17% | +1,33% | -1,33% | -3,42% | +6,32% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +0,93% | +0,18% | -1,31% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 32 | 65,62% | +2,98% | +5,88% | -4,04% | +8,39% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 34 | 70,59% | +2,68% | +5,43% | -4,07% | +7,96% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 34 | 70,59% | +2,68% | +5,43% | -4,07% | +7,96% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 32 | 71,88% | +2,94% | +5,67% | -4,09% | +8,18% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 30 | 66,67% | -0,31% | +0,31% | -4,43% | +4,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 22 | 63,64% | +0,33% | -0,33% | -4,43% | +5,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,47% | +2,65% | -1,31% | +16,91% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 26 | 69,23% | +3,15% | +1,62% | -5,01% | +9,37% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 28 | 82,14% | +3,64% | +7,87% | -4,97% | +10,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 28 | 82,14% | +3,64% | +7,87% | -4,97% | +10,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 26 | 84,62% | +4,02% | +8,38% | -5,07% | +10,67% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 28 | 67,86% | +3,64% | -3,64% | -4,97% | +10,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 20 | 75,00% | +0,03% | -0,03% | -5,18% | +6,01% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 18 | 72,22% | +4,53% | -1,57% | -6,13% | +11,19% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 19 | 78,95% | +5,29% | +2,88% | -6,16% | +12,56% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 19 | 78,95% | +5,29% | +2,88% | -6,16% | +12,56% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 17 | 88,24% | +2,62% | +6,51% | -6,44% | +9,65% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 19 | 63,16% | +5,29% | -5,29% | -6,16% | +12,56% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 16 | 68,75% | +3,81% | -3,81% | -5,92% | +10,30% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 4 | 0,00% | +23,27% | -23,27% | -7,38% | +34,26% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 4 | 0,00% | +23,27% | -23,27% | -7,38% | +34,26% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 4 | 0,00% | +23,27% | -23,27% | -7,38% | +34,26% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 4 | 0,00% | +23,27% | -23,27% | -7,38% | +34,26% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 4 | 0,00% | +23,27% | -23,27% | -7,38% | +34,26% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 4 | 0,00% | +23,27% | -23,27% | -7,38% | +34,26% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 39 | 56,41% | +0,69% | +0,53% | +0,02% | +1,63% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 41 | 58,54% | +0,30% | +0,28% | -0,29% | +1,21% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 44 | 56,82% | +0,35% | +0,19% | -0,24% | +1,25% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 43 | 51,16% | +0,30% | +0,27% | -0,34% | +1,15% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 27 | 51,85% | +0,55% | +0,49% | -0,24% | +1,55% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | -0,20% | -0,20% | -0,75% | +2,55% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 38 | 55,26% | +1,54% | +1,35% | +0,72% | +2,67% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 40 | 50,00% | +1,02% | +0,42% | +0,19% | +1,81% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 43 | 48,84% | +0,97% | +0,36% | +0,17% | +1,88% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 42 | 45,24% | +0,89% | +0,16% | +0,14% | +2,02% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 26 | 57,69% | +1,08% | +1,05% | +0,38% | +2,08% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,74% | +0,74% | +0,30% | +2,88% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 37 | 56,76% | +2,31% | +2,07% | -1,08% | +4,45% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 39 | 46,15% | +1,63% | +0,87% | -1,51% | +3,78% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 42 | 45,24% | +1,54% | +0,79% | -1,49% | +3,75% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 41 | 46,34% | +1,34% | -0,26% | -1,58% | +3,40% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 25 | 52,00% | +1,24% | +1,02% | -1,46% | +3,24% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,33% | +0,33% | -1,17% | +5,20% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 35 | 60,00% | +3,67% | +3,52% | -1,68% | +6,69% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 37 | 56,76% | +2,72% | +2,47% | -2,12% | +5,75% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 40 | 55,00% | +2,57% | +2,23% | -2,11% | +5,61% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 39 | 43,59% | +2,57% | -1,51% | -2,32% | +5,46% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 23 | 56,52% | +1,38% | +1,13% | -2,15% | +3,88% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +1,18% | +1,18% | -1,95% | +5,20% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 33 | 63,64% | +4,57% | +4,73% | -2,31% | +8,02% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 36 | 66,67% | +3,90% | +4,53% | -2,60% | +7,40% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 39 | 66,67% | +3,59% | +4,19% | -2,61% | +7,13% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 37 | 32,43% | +3,11% | -3,66% | -2,99% | +6,65% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 30 | 63,33% | +3,93% | +4,19% | -3,23% | +7,52% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 33 | 66,67% | +3,47% | +4,13% | -3,57% | +6,88% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 36 | 63,89% | +3,17% | +3,80% | -3,56% | +6,63% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 31 | 61,29% | +4,03% | +3,86% | -3,41% | +7,24% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 35 | 42,86% | +2,60% | -2,74% | -3,67% | +6,35% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,08% | +0,08% | -3,74% | +3,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 27 | 70,37% | +4,48% | +5,83% | -3,95% | +9,24% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 30 | 83,33% | +4,50% | +5,75% | -4,13% | +8,56% | PRIMA CALIBRAZIONE |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 33 | 84,85% | +3,81% | +5,51% | -4,11% | +8,14% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 28 | 67,86% | +5,06% | +5,18% | -3,82% | +9,08% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 32 | 34,38% | +2,00% | -2,63% | -4,32% | +6,56% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,19% | -1,19% | -4,25% | +5,07% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 21 | 61,90% | +5,44% | +3,75% | -5,73% | +10,99% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 24 | 79,17% | +6,70% | +9,03% | -5,51% | +11,40% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 27 | 81,48% | +5,65% | +8,33% | -5,57% | +10,57% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 22 | 59,09% | +7,56% | +8,33% | -5,21% | +12,32% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 28 | 42,86% | +5,48% | -6,95% | -5,62% | +10,32% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 20 | 40,00% | +9,40% | -9,40% | -4,94% | +13,51% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |

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
