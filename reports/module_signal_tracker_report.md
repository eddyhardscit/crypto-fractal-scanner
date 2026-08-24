# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-24 05:32 UTC

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

Segnali totali salvati: **135**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-24 | BTC | 76.958,14 | +6 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-24 | DOGE | 0.09174 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-24 | SOL | 93,82 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-23 | BTC | 76.280,85 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-23 | DOGE | 0.09044 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-23 | SOL | 93,05 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-22 | BTC | 77.109,54 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-22 | DOGE | 0.09028 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-22 | SOL | 93,36 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-21 | BTC | 75.089,33 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-21 | DOGE | 0.08259 | +2 | +1 | +1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-21 | SOL | 89,61 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 45 | 44 | 43 | 42 | 40 | 38 | 35 | 33 | 26 | 17 | 2 | 0 |
| SOL | 45 | 44 | 43 | 42 | 40 | 38 | 35 | 33 | 26 | 17 | 2 | 0 |
| DOGE | 45 | 44 | 43 | 42 | 40 | 38 | 35 | 33 | 26 | 17 | 2 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-11 | 45g | 2026-08-25 | domani |
| SOL | 2026-07-11 | 45g | 2026-08-25 | domani |
| DOGE | 2026-07-11 | 45g | 2026-08-25 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 41 | 53,66% | +0,50% | +0,47% | PRIMA CALIBRAZIONE |
| BTC | 2g | 40 | 52,50% | +0,85% | +0,73% | PRIMA CALIBRAZIONE |
| BTC | 3g | 39 | 48,72% | +1,08% | +0,90% | PRIMA CALIBRAZIONE |
| BTC | 5g | 37 | 37,84% | +1,90% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 7g | 36 | 47,22% | +2,33% | +2,03% | PRIMA CALIBRAZIONE |
| BTC | 10g | 33 | 45,45% | +1,60% | +1,32% | PRIMA CALIBRAZIONE |
| BTC | 14g | 31 | 54,84% | +2,57% | +2,46% | PRIMA CALIBRAZIONE |
| BTC | 21g | 24 | 41,67% | +3,36% | +3,08% | FEEDBACK RAPIDO |
| BTC | 30g | 15 | 86,67% | +3,97% | +4,31% | FEEDBACK RAPIDO |
| BTC | 45g | 2 | 100,00% | +20,57% | +20,57% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 37 | 56,76% | +0,62% | +0,45% | PRIMA CALIBRAZIONE |
| SOL | 2g | 36 | 52,78% | +1,25% | +1,06% | PRIMA CALIBRAZIONE |
| SOL | 3g | 35 | 54,29% | +2,05% | +1,79% | PRIMA CALIBRAZIONE |
| SOL | 5g | 33 | 57,58% | +3,02% | +2,86% | PRIMA CALIBRAZIONE |
| SOL | 7g | 31 | 61,29% | +2,88% | +3,05% | PRIMA CALIBRAZIONE |
| SOL | 10g | 28 | 60,71% | +1,91% | +2,18% | FEEDBACK RAPIDO |
| SOL | 14g | 26 | 69,23% | +3,30% | +4,70% | FEEDBACK RAPIDO |
| SOL | 21g | 20 | 60,00% | +4,15% | +2,37% | FEEDBACK RAPIDO |
| SOL | 30g | 14 | 42,86% | +2,59% | +0,37% | FEEDBACK RAPIDO |
| SOL | 45g | 1 | 100,00% | +19,26% | +19,26% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 42 | 50,00% | +0,65% | +0,64% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 41 | 51,22% | +1,29% | +1,28% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 40 | 50,00% | +1,89% | +2,18% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 38 | 57,89% | +2,54% | +3,20% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 36 | 63,89% | +2,26% | +3,49% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 33 | 57,58% | +0,56% | +2,44% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 31 | 64,52% | +2,00% | +5,00% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 25 | 68,00% | +1,97% | +0,39% | FEEDBACK RAPIDO |
| DOGE | 30g | 17 | 70,59% | +3,23% | -3,23% | FEEDBACK RAPIDO |
| DOGE | 45g | 2 | 0,00% | +24,16% | -24,16% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 41 | 53,66% | +0,50% | +0,47% | +0,10% | +1,10% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 44 | 56,82% | +0,46% | +0,46% | +0,08% | +1,04% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 44 | 56,82% | +0,46% | +0,46% | +0,08% | +1,04% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 39 | 38,46% | +0,64% | +0,12% | +0,24% | +1,23% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 12 | 33,33% | +1,31% | +0,43% | +0,62% | +1,94% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,45% | +1,45% | +1,10% | +2,07% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 40 | 52,50% | +0,85% | +0,73% | +0,32% | +1,59% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 43 | 55,81% | +0,97% | +0,97% | +0,45% | +1,70% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 43 | 55,81% | +0,97% | +0,97% | +0,45% | +1,70% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 38 | 42,11% | +1,23% | +0,14% | +0,72% | +1,97% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 11 | 27,27% | +1,80% | +0,42% | +1,46% | +2,69% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 39 | 48,72% | +1,08% | +0,90% | -0,80% | +2,77% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 42 | 59,52% | +1,47% | +1,47% | -0,78% | +3,07% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 42 | 59,52% | +1,47% | +1,47% | -0,78% | +3,07% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 37 | 35,14% | +1,93% | -0,34% | -0,52% | +3,48% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 10 | 30,00% | +3,14% | -0,71% | +0,49% | +4,52% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 37 | 37,84% | +1,90% | +1,56% | -1,64% | +3,97% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 40 | 47,50% | +2,24% | +2,24% | -1,59% | +4,40% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 40 | 47,50% | +2,24% | +2,24% | -1,59% | +4,40% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 35 | 34,29% | +2,71% | -2,12% | -1,33% | +4,92% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 8 | 12,50% | +7,26% | -7,26% | -0,63% | +8,70% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 36 | 47,22% | +2,33% | +2,03% | -2,11% | +4,78% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 38 | 55,26% | +2,18% | +2,18% | -2,11% | +4,66% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 38 | 55,26% | +2,18% | +2,18% | -2,11% | +4,66% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 58,82% | +2,59% | +2,59% | -2,06% | +4,93% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 33 | 30,30% | +2,85% | -3,31% | -1,86% | +5,21% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 8 | 0,00% | +11,51% | -11,51% | -0,67% | +13,66% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 33 | 45,45% | +1,60% | +1,32% | -2,59% | +4,11% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 35 | 51,43% | +1,37% | +1,37% | -2,61% | +4,02% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 35 | 51,43% | +1,37% | +1,37% | -2,61% | +4,02% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 31 | 58,06% | +1,81% | +1,81% | -2,51% | +4,24% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 30 | 33,33% | +1,79% | -0,28% | -2,35% | +4,49% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 5 | 0,00% | +5,58% | -5,58% | -1,17% | +7,97% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 31 | 54,84% | +2,57% | +2,46% | -2,91% | +5,73% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 33 | 54,55% | +2,32% | +2,32% | -2,93% | +5,55% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 33 | 54,55% | +2,32% | +2,32% | -2,93% | +5,55% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 29 | 62,07% | +2,99% | +2,99% | -2,72% | +5,98% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 28 | 64,29% | +2,97% | +2,91% | -2,65% | +6,24% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 24 | 41,67% | +3,36% | +3,08% | -2,93% | +7,10% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 26 | 53,85% | +3,01% | +3,01% | -2,98% | +6,76% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 26 | 53,85% | +3,01% | +3,01% | -2,98% | +6,76% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 22 | 59,09% | +3,81% | +3,81% | -2,71% | +7,55% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 21 | 19,05% | +3,36% | -3,68% | -2,63% | +7,21% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 4 | 0,00% | +11,68% | -11,68% | -1,55% | +14,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 15 | 86,67% | +3,97% | +4,31% | -3,21% | +7,97% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 17 | 70,59% | +4,45% | +4,45% | -3,26% | +8,58% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 17 | 70,59% | +4,45% | +4,45% | -3,26% | +8,58% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 13 | 69,23% | +4,37% | +4,37% | -2,88% | +9,05% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 14 | 35,71% | +3,91% | -4,27% | -2,94% | +8,61% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 2 | 100,00% | +20,57% | +20,57% | -2,80% | +25,05% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | +20,57% | +20,57% | -2,80% | +25,05% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | +20,57% | +20,57% | -2,80% | +25,05% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 2 | 100,00% | +20,57% | +20,57% | -2,80% | +25,05% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 1 | 0,00% | +20,63% | -20,63% | -2,32% | +25,66% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 42 | 50,00% | +0,65% | +0,64% | +0,12% | +1,73% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 44 | 59,09% | +0,53% | +0,81% | -0,00% | +1,58% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 44 | 59,09% | +0,53% | +0,81% | -0,00% | +1,58% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 37 | 56,76% | +0,47% | +0,70% | -0,10% | +1,49% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 29 | 41,38% | +0,47% | -0,36% | -0,07% | +1,22% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +3,11% | +2,58% | +1,68% | +3,93% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 41 | 51,22% | +1,29% | +1,28% | +0,60% | +2,70% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 43 | 53,49% | +1,13% | +1,35% | +0,45% | +2,50% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 43 | 53,49% | +1,13% | +1,35% | +0,45% | +2,50% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 36 | 63,89% | +0,64% | +1,15% | +0,02% | +1,96% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 28 | 46,43% | +1,10% | -0,98% | +0,41% | +2,12% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +5,87% | +5,43% | +5,07% | +8,56% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 40 | 50,00% | +1,89% | +2,18% | -1,00% | +4,61% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 42 | 54,76% | +1,70% | +2,00% | -1,12% | +4,35% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 42 | 54,76% | +1,70% | +2,00% | -1,12% | +4,35% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 35 | 51,43% | +0,68% | +1,16% | -1,38% | +3,07% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 27 | 33,33% | +1,97% | -1,97% | -1,30% | +4,60% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +5,63% | +5,21% | +1,37% | +9,34% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 38 | 57,89% | +2,54% | +3,20% | -2,12% | +5,98% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 40 | 55,00% | +2,31% | +2,95% | -2,20% | +5,67% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 40 | 55,00% | +2,31% | +2,95% | -2,20% | +5,67% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 33 | 63,64% | +0,95% | +0,56% | -2,69% | +4,03% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 27 | 44,44% | +3,71% | -3,71% | -1,98% | +7,48% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 36 | 63,89% | +2,26% | +3,49% | -2,76% | +6,24% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 38 | 60,53% | +2,02% | +3,15% | -2,85% | +5,96% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 38 | 60,53% | +2,02% | +3,15% | -2,85% | +5,96% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 36 | 61,11% | +2,19% | +3,26% | -2,86% | +6,04% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 33 | 63,64% | +1,75% | +1,79% | -3,12% | +5,79% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 25 | 48,00% | +2,39% | -2,39% | -2,84% | +6,41% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,63% | +0,36% | -0,50% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 33 | 57,58% | +0,56% | +2,44% | -3,42% | +4,74% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 35 | 57,14% | +0,42% | +2,23% | -3,48% | +4,53% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 35 | 57,14% | +0,42% | +2,23% | -3,48% | +4,53% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 33 | 57,58% | +0,50% | +2,31% | -3,48% | +4,53% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 30 | 66,67% | -1,40% | +1,40% | -3,88% | +2,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 23 | 56,52% | +0,32% | -0,32% | -3,55% | +4,70% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +0,93% | +0,18% | -1,31% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 31 | 64,52% | +2,00% | +5,00% | -4,13% | +7,27% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 33 | 69,70% | +1,75% | +4,59% | -4,15% | +6,89% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 33 | 69,70% | +1,75% | +4,59% | -4,15% | +6,89% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 31 | 70,97% | +1,97% | +4,79% | -4,18% | +7,05% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 30 | 66,67% | -0,31% | +0,31% | -4,43% | +4,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 22 | 63,64% | +0,33% | -0,33% | -4,43% | +5,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,47% | +2,65% | -1,31% | +16,91% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 25 | 68,00% | +1,97% | +0,39% | -5,11% | +8,04% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 26 | 80,77% | +1,75% | +6,30% | -5,17% | +7,73% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 26 | 80,77% | +1,75% | +6,30% | -5,17% | +7,73% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 24 | 83,33% | +2,00% | +6,72% | -5,29% | +8,00% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 26 | 73,08% | +1,75% | -1,75% | -5,17% | +7,73% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 20 | 75,00% | +0,03% | -0,03% | -5,18% | +6,01% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 17 | 70,59% | +3,23% | -3,23% | -6,05% | +9,72% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 17 | 76,47% | +3,23% | +0,54% | -6,05% | +9,72% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 17 | 76,47% | +3,23% | +0,54% | -6,05% | +9,72% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 15 | 86,67% | -0,07% | +4,34% | -6,36% | +6,05% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 17 | 70,59% | +3,23% | -3,23% | -6,05% | +9,72% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 16 | 68,75% | +3,81% | -3,81% | -5,92% | +10,30% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 2 | 0,00% | +24,16% | -24,16% | -7,34% | +32,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 2 | 0,00% | +24,16% | -24,16% | -7,34% | +32,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 2 | 0,00% | +24,16% | -24,16% | -7,34% | +32,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 2 | 0,00% | +24,16% | -24,16% | -7,34% | +32,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 2 | 0,00% | +24,16% | -24,16% | -7,34% | +32,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 2 | 0,00% | +24,16% | -24,16% | -7,34% | +32,34% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 37 | 56,76% | +0,62% | +0,45% | +0,04% | +1,61% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 39 | 58,97% | +0,21% | +0,20% | -0,28% | +1,16% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 42 | 57,14% | +0,28% | +0,10% | -0,23% | +1,21% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 41 | 51,22% | +0,22% | +0,19% | -0,33% | +1,11% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 25 | 52,00% | +0,44% | +0,37% | -0,23% | +1,51% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,51% | +1,51% | +0,99% | +5,02% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 36 | 52,78% | +1,25% | +1,06% | +0,52% | +2,44% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 38 | 50,00% | +0,72% | +0,62% | -0,03% | +1,55% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 41 | 48,78% | +0,69% | +0,55% | -0,03% | +1,64% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 40 | 42,50% | +0,60% | -0,17% | -0,07% | +1,78% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 24 | 54,17% | +0,62% | +0,58% | +0,05% | +1,68% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,74% | +0,74% | +0,30% | +2,88% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 35 | 54,29% | +2,05% | +1,79% | -1,11% | +4,27% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 37 | 48,65% | +1,34% | +1,30% | -1,55% | +3,56% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 40 | 47,50% | +1,26% | +1,18% | -1,53% | +3,55% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 39 | 43,59% | +1,06% | -0,63% | -1,63% | +3,17% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 23 | 47,83% | +0,74% | +0,50% | -1,52% | +2,85% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,33% | +0,33% | -1,17% | +5,20% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 33 | 57,58% | +3,02% | +2,86% | -1,94% | +6,07% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 36 | 58,33% | +2,57% | +2,77% | -2,23% | +5,54% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 39 | 56,41% | +2,43% | +2,50% | -2,22% | +5,41% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 37 | 40,54% | +1,93% | -2,38% | -2,58% | +4,84% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 21 | 52,38% | +0,14% | -0,14% | -2,60% | +2,64% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 31 | 61,29% | +2,88% | +3,05% | -2,80% | +6,36% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 34 | 64,71% | +2,32% | +2,99% | -3,07% | +5,85% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 37 | 64,86% | +2,12% | +2,76% | -3,04% | +5,69% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 32 | 59,38% | +2,70% | +2,76% | -2,93% | +6,14% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 36 | 33,33% | +2,22% | -2,78% | -3,11% | +5,86% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 28 | 60,71% | +1,91% | +2,18% | -3,36% | +5,53% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 31 | 64,52% | +1,62% | +2,31% | -3,71% | +5,05% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 34 | 61,76% | +1,46% | +2,13% | -3,68% | +4,95% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 29 | 58,62% | +2,09% | +1,90% | -3,55% | +5,31% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 33 | 45,45% | +0,80% | -0,95% | -3,81% | +4,59% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,08% | +0,08% | -3,74% | +3,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 26 | 69,23% | +3,30% | +4,70% | -4,03% | +8,25% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 29 | 82,76% | +3,44% | +4,73% | -4,20% | +7,65% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 32 | 84,38% | +2,83% | +4,58% | -4,18% | +7,30% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 27 | 66,67% | +3,94% | +4,07% | -3,89% | +8,12% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 32 | 34,38% | +2,00% | -2,63% | -4,32% | +6,56% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,19% | -1,19% | -4,25% | +5,07% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 20 | 60,00% | +4,15% | +2,37% | -5,91% | +9,66% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 22 | 77,27% | +4,12% | +6,66% | -5,83% | +8,96% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 25 | 80,00% | +3,30% | +6,19% | -5,86% | +8,35% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 20 | 55,00% | +4,80% | +5,65% | -5,53% | +9,73% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 26 | 46,15% | +3,20% | -4,78% | -5,90% | +8,17% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 18 | 44,44% | +6,55% | -6,55% | -5,27% | +10,76% | FEEDBACK RAPIDO |
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
