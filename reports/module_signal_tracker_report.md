# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-25 05:32 UTC

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

Segnali totali salvati: **138**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-25 | BTC | 80.778,18 | +6 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-25 | DOGE | 0.09299 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-25 | SOL | 102,40 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-24 | BTC | 76.958,14 | +6 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-24 | DOGE | 0.09174 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-24 | SOL | 93,82 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-23 | BTC | 76.280,85 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-23 | DOGE | 0.09044 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-23 | SOL | 93,05 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-22 | BTC | 77.109,54 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-22 | DOGE | 0.09028 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-22 | SOL | 93,36 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 46 | 45 | 44 | 43 | 41 | 39 | 36 | 34 | 27 | 18 | 3 | 0 |
| SOL | 46 | 45 | 44 | 43 | 41 | 39 | 36 | 34 | 27 | 18 | 3 | 0 |
| DOGE | 46 | 45 | 44 | 43 | 41 | 39 | 36 | 34 | 27 | 18 | 3 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-12 | 45g | 2026-08-26 | domani |
| SOL | 2026-07-12 | 45g | 2026-08-26 | domani |
| DOGE | 2026-07-12 | 45g | 2026-08-26 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 42 | 54,76% | +0,61% | +0,58% | PRIMA CALIBRAZIONE |
| BTC | 2g | 41 | 53,66% | +0,97% | +0,86% | PRIMA CALIBRAZIONE |
| BTC | 3g | 40 | 50,00% | +1,17% | +1,00% | PRIMA CALIBRAZIONE |
| BTC | 5g | 38 | 39,47% | +2,28% | +1,94% | PRIMA CALIBRAZIONE |
| BTC | 7g | 36 | 47,22% | +2,33% | +2,03% | PRIMA CALIBRAZIONE |
| BTC | 10g | 34 | 47,06% | +2,38% | +2,11% | PRIMA CALIBRAZIONE |
| BTC | 14g | 32 | 56,25% | +3,32% | +3,21% | PRIMA CALIBRAZIONE |
| BTC | 21g | 25 | 44,00% | +4,29% | +4,02% | FEEDBACK RAPIDO |
| BTC | 30g | 16 | 87,50% | +5,31% | +5,62% | FEEDBACK RAPIDO |
| BTC | 45g | 3 | 100,00% | +22,42% | +22,42% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 38 | 57,89% | +0,84% | +0,68% | PRIMA CALIBRAZIONE |
| SOL | 2g | 37 | 54,05% | +1,49% | +1,30% | PRIMA CALIBRAZIONE |
| SOL | 3g | 36 | 55,56% | +2,26% | +2,01% | PRIMA CALIBRAZIONE |
| SOL | 5g | 34 | 58,82% | +3,54% | +3,38% | PRIMA CALIBRAZIONE |
| SOL | 7g | 32 | 62,50% | +3,90% | +4,06% | PRIMA CALIBRAZIONE |
| SOL | 10g | 29 | 62,07% | +3,08% | +3,34% | FEEDBACK RAPIDO |
| SOL | 14g | 27 | 70,37% | +4,48% | +5,83% | FEEDBACK RAPIDO |
| SOL | 21g | 20 | 60,00% | +4,15% | +2,37% | FEEDBACK RAPIDO |
| SOL | 30g | 14 | 42,86% | +2,59% | +0,37% | FEEDBACK RAPIDO |
| SOL | 45g | 2 | 100,00% | +25,44% | +25,44% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 43 | 51,16% | +0,67% | +0,66% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 42 | 52,38% | +1,33% | +1,32% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 41 | 51,22% | +1,92% | +2,20% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 39 | 58,97% | +3,11% | +3,75% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 37 | 64,86% | +3,11% | +4,30% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 34 | 58,82% | +1,50% | +3,33% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 32 | 65,62% | +2,98% | +5,88% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 26 | 69,23% | +3,15% | +1,62% | FEEDBACK RAPIDO |
| DOGE | 30g | 18 | 72,22% | +4,53% | -1,57% | FEEDBACK RAPIDO |
| DOGE | 45g | 3 | 0,00% | +24,66% | -24,66% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 42 | 54,76% | +0,61% | +0,58% | +0,16% | +1,20% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 45 | 57,78% | +0,56% | +0,56% | +0,13% | +1,13% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 45 | 57,78% | +0,56% | +0,56% | +0,13% | +1,13% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 40 | 40,00% | +0,75% | +0,24% | +0,29% | +1,33% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 13 | 38,46% | +1,59% | +0,78% | +0,75% | +2,20% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,45% | +1,45% | +1,10% | +2,07% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 41 | 53,66% | +0,97% | +0,86% | +0,40% | +1,71% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 44 | 56,82% | +1,08% | +1,08% | +0,51% | +1,80% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 44 | 56,82% | +1,08% | +1,08% | +0,51% | +1,80% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 39 | 43,59% | +1,35% | +0,29% | +0,78% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 12 | 33,33% | +2,14% | +0,88% | +1,61% | +2,98% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +4,54% | +4,54% | +3,15% | +5,05% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 40 | 50,00% | +1,17% | +1,00% | -0,83% | +2,83% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 43 | 60,47% | +1,54% | +1,54% | -0,81% | +3,11% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 43 | 60,47% | +1,54% | +1,54% | -0,81% | +3,11% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 38 | 36,84% | +2,01% | -0,21% | -0,55% | +3,52% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 11 | 36,36% | +3,29% | -0,21% | +0,27% | +4,57% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 38 | 39,47% | +2,28% | +1,94% | -1,47% | +4,30% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 41 | 48,78% | +2,58% | +2,58% | -1,43% | +4,69% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 41 | 48,78% | +2,58% | +2,58% | -1,43% | +4,69% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 36 | 36,11% | +3,09% | -1,62% | -1,16% | +5,24% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 9 | 22,22% | +8,25% | -4,66% | -0,01% | +9,57% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 36 | 47,22% | +2,33% | +2,03% | -2,11% | +4,78% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 39 | 56,41% | +2,78% | +2,78% | -2,06% | +5,22% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 39 | 56,41% | +2,78% | +2,78% | -2,06% | +5,22% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 58,82% | +2,59% | +2,59% | -2,06% | +4,93% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 34 | 29,41% | +3,53% | -3,97% | -1,80% | +5,83% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 8 | 0,00% | +11,51% | -11,51% | -0,67% | +13,66% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 34 | 47,06% | +2,38% | +2,11% | -2,53% | +4,82% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 36 | 52,78% | +2,11% | +2,11% | -2,56% | +4,70% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 36 | 52,78% | +2,11% | +2,11% | -2,56% | +4,70% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 32 | 59,38% | +2,63% | +2,63% | -2,45% | +4,99% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 31 | 32,26% | +2,64% | -1,18% | -2,30% | +5,27% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 6 | 0,00% | +9,33% | -9,33% | -1,08% | +11,39% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 32 | 56,25% | +3,32% | +3,21% | -2,89% | +6,39% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 34 | 55,88% | +3,03% | +3,03% | -2,91% | +6,17% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 34 | 55,88% | +3,03% | +3,03% | -2,91% | +6,17% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 30 | 63,33% | +3,77% | +3,77% | -2,71% | +6,68% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 29 | 65,52% | +3,77% | +3,72% | -2,64% | +6,95% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 25 | 44,00% | +4,29% | +4,02% | -2,89% | +7,89% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 27 | 55,56% | +3,89% | +3,89% | -2,95% | +7,50% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 27 | 55,56% | +3,89% | +3,89% | -2,95% | +7,50% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 23 | 60,87% | +4,80% | +4,80% | -2,68% | +8,40% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 22 | 22,73% | +4,41% | -2,30% | -2,60% | +8,11% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 4 | 0,00% | +11,68% | -11,68% | -1,55% | +14,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 16 | 87,50% | +5,31% | +5,62% | -3,22% | +9,08% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 18 | 72,22% | +5,61% | +5,61% | -3,27% | +9,53% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 18 | 72,22% | +5,61% | +5,61% | -3,27% | +9,53% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 14 | 71,43% | +5,87% | +5,87% | -2,92% | +10,24% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 15 | 40,00% | +5,34% | -2,30% | -2,97% | +9,75% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 3 | 100,00% | +22,42% | +22,42% | -3,05% | +25,54% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | +22,42% | +22,42% | -3,05% | +25,54% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | +22,42% | +22,42% | -3,05% | +25,54% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 3 | 100,00% | +22,42% | +22,42% | -3,05% | +25,54% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 2 | 0,00% | +23,38% | -23,38% | -2,93% | +26,09% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 43 | 51,16% | +0,67% | +0,66% | +0,07% | +1,72% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 45 | 60,00% | +0,55% | +0,82% | -0,05% | +1,57% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 45 | 60,00% | +0,55% | +0,82% | -0,05% | +1,57% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 38 | 57,89% | +0,49% | +0,72% | -0,15% | +1,48% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 30 | 43,33% | +0,50% | -0,30% | -0,13% | +1,22% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +2,86% | +2,41% | +1,15% | +3,54% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 42 | 52,38% | +1,33% | +1,32% | +0,58% | +2,70% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 44 | 54,55% | +1,16% | +1,38% | +0,43% | +2,50% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 44 | 54,55% | +1,16% | +1,38% | +0,43% | +2,50% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 37 | 64,86% | +0,69% | +1,19% | +0,01% | +1,98% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 29 | 48,28% | +1,15% | -0,85% | +0,37% | +2,14% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +5,87% | +5,43% | +5,07% | +8,56% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 41 | 51,22% | +1,92% | +2,20% | -1,01% | +4,61% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 43 | 55,81% | +1,73% | +2,03% | -1,13% | +4,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 43 | 55,81% | +1,73% | +2,03% | -1,13% | +4,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 36 | 52,78% | +0,74% | +1,21% | -1,38% | +3,11% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 28 | 35,71% | +2,01% | -1,79% | -1,31% | +4,60% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +5,19% | +4,84% | +0,90% | +8,54% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 39 | 58,97% | +3,11% | +3,75% | -1,86% | +6,70% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 41 | 56,10% | +2,86% | +3,48% | -1,95% | +6,37% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 41 | 56,10% | +2,86% | +3,48% | -1,95% | +6,37% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 34 | 64,71% | +1,65% | +1,27% | -2,38% | +4,91% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 27 | 44,44% | +3,71% | -3,71% | -1,98% | +7,48% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +5,46% | +5,14% | +1,28% | +11,40% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 37 | 64,86% | +3,11% | +4,30% | -2,68% | +7,24% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 39 | 61,54% | +2,83% | +3,93% | -2,78% | +6,92% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 39 | 61,54% | +2,83% | +3,93% | -2,78% | +6,92% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 37 | 62,16% | +3,04% | +4,08% | -2,78% | +7,05% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 33 | 63,64% | +1,75% | +1,79% | -3,12% | +5,79% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 26 | 46,15% | +3,58% | -3,58% | -2,73% | +7,84% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,63% | +0,36% | -0,50% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 34 | 58,82% | +1,50% | +3,33% | -3,36% | +5,85% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 36 | 58,33% | +1,31% | +3,07% | -3,42% | +5,58% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 36 | 58,33% | +1,31% | +3,07% | -3,42% | +5,58% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 58,82% | +1,44% | +3,20% | -3,42% | +5,64% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 31 | 67,74% | -0,31% | +2,41% | -3,79% | +3,92% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 23 | 56,52% | +0,32% | -0,32% | -3,55% | +4,70% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +0,93% | +0,18% | -1,31% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 32 | 65,62% | +2,98% | +5,88% | -4,04% | +8,39% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 34 | 70,59% | +2,68% | +5,43% | -4,07% | +7,96% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 34 | 70,59% | +2,68% | +5,43% | -4,07% | +7,96% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 32 | 71,88% | +2,94% | +5,67% | -4,09% | +8,18% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 30 | 66,67% | -0,31% | +0,31% | -4,43% | +4,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 22 | 63,64% | +0,33% | -0,33% | -4,43% | +5,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,47% | +2,65% | -1,31% | +16,91% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 26 | 69,23% | +3,15% | +1,62% | -5,01% | +9,37% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 27 | 81,48% | +2,89% | +7,27% | -5,08% | +9,02% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 27 | 81,48% | +2,89% | +7,27% | -5,08% | +9,02% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 25 | 84,00% | +3,22% | +7,75% | -5,18% | +9,38% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 27 | 70,37% | +2,89% | -2,89% | -5,08% | +9,02% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 20 | 75,00% | +0,03% | -0,03% | -5,18% | +6,01% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 18 | 72,22% | +4,53% | -1,57% | -6,13% | +11,19% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 18 | 77,78% | +4,53% | +1,99% | -6,13% | +11,19% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 18 | 77,78% | +4,53% | +1,99% | -6,13% | +11,19% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 16 | 87,50% | +1,60% | +5,73% | -6,42% | +7,93% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 18 | 66,67% | +4,53% | -4,53% | -6,13% | +11,19% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 16 | 68,75% | +3,81% | -3,81% | -5,92% | +10,30% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 3 | 0,00% | +24,66% | -24,66% | -7,62% | +33,25% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 3 | 0,00% | +24,66% | -24,66% | -7,62% | +33,25% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 3 | 0,00% | +24,66% | -24,66% | -7,62% | +33,25% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 3 | 0,00% | +24,66% | -24,66% | -7,62% | +33,25% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 3 | 0,00% | +24,66% | -24,66% | -7,62% | +33,25% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 3 | 0,00% | +24,66% | -24,66% | -7,62% | +33,25% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 38 | 57,89% | +0,84% | +0,68% | +0,18% | +1,80% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 40 | 60,00% | +0,44% | +0,42% | -0,14% | +1,36% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 43 | 58,14% | +0,48% | +0,31% | -0,11% | +1,39% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 42 | 52,38% | +0,43% | +0,40% | -0,20% | +1,30% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 26 | 53,85% | +0,78% | +0,71% | -0,02% | +1,79% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,51% | +1,51% | +0,99% | +5,02% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 37 | 54,05% | +1,49% | +1,30% | +0,67% | +2,64% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 39 | 48,72% | +0,96% | +0,34% | +0,13% | +1,76% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 42 | 47,62% | +0,92% | +0,29% | +0,11% | +1,83% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 41 | 43,90% | +0,83% | +0,08% | +0,08% | +1,97% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 25 | 56,00% | +0,99% | +0,95% | +0,29% | +2,01% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,74% | +0,74% | +0,30% | +2,88% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 36 | 55,56% | +2,26% | +2,01% | -1,12% | +4,41% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 38 | 47,37% | +1,56% | +1,01% | -1,55% | +3,72% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 41 | 46,34% | +1,47% | +0,91% | -1,53% | +3,69% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 40 | 45,00% | +1,27% | -0,37% | -1,63% | +3,33% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 24 | 50,00% | +1,11% | +0,89% | -1,53% | +3,13% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,33% | +0,33% | -1,17% | +5,20% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 34 | 58,82% | +3,54% | +3,38% | -1,79% | +6,49% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 36 | 58,33% | +2,57% | +2,77% | -2,23% | +5,54% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 39 | 56,41% | +2,43% | +2,50% | -2,22% | +5,41% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 38 | 42,11% | +2,42% | -1,77% | -2,43% | +5,25% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 22 | 54,55% | +1,07% | +0,81% | -2,33% | +3,44% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 32 | 62,50% | +3,90% | +4,06% | -2,67% | +7,26% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 35 | 65,71% | +3,26% | +3,92% | -2,94% | +6,69% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 38 | 65,79% | +2,99% | +3,61% | -2,92% | +6,47% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 33 | 60,61% | +3,69% | +3,75% | -2,81% | +7,01% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 37 | 32,43% | +3,11% | -3,66% | -2,99% | +6,65% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 29 | 62,07% | +3,08% | +3,34% | -3,30% | +6,57% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 32 | 65,62% | +2,69% | +3,36% | -3,64% | +6,00% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 35 | 62,86% | +2,44% | +3,09% | -3,62% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 30 | 60,00% | +3,21% | +3,03% | -3,48% | +6,32% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 34 | 44,12% | +1,83% | -1,98% | -3,74% | +5,50% | PRIMA CALIBRAZIONE |
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
| SOL | 21g | Global confluence | BENCHMARK | 20 | 60,00% | +4,15% | +2,37% | -5,91% | +9,66% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 23 | 78,26% | +5,64% | +8,07% | -5,66% | +10,25% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 26 | 80,77% | +4,67% | +7,45% | -5,71% | +9,52% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 21 | 57,14% | +6,43% | +7,24% | -5,35% | +11,11% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 27 | 44,44% | +4,52% | -6,05% | -5,75% | +9,30% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 19 | 42,11% | +8,25% | -8,25% | -5,09% | +12,23% | FEEDBACK RAPIDO |
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
