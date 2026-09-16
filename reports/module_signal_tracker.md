# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-16 05:32 UTC

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

Segnali totali salvati: **204**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-16 | BTC | 75.786,49 | +2 | +3 | +3 | 0 | 0 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-16 | DOGE | 0.08011 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-16 | SOL | 97,05 | +2 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-15 | BTC | 77.430,91 | +4 | +3 | +3 | 0 | +1 | -1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-15 | DOGE | 0.08280 | -4 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-15 | SOL | 100,84 | +2 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-14 | BTC | 77.497,87 | +3 | +3 | +3 | 0 | +1 | -1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-14 | DOGE | 0.08404 | -4 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-14 | SOL | 101,01 | +3 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-13 | BTC | 77.274,99 | +6 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-13 | DOGE | 0.08485 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-13 | SOL | 101,86 | +4 | +3 | +3 | 0 | +1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 68 | 67 | 66 | 65 | 63 | 61 | 58 | 54 | 47 | 38 | 25 | 10 |
| SOL | 68 | 67 | 66 | 65 | 63 | 61 | 58 | 54 | 47 | 38 | 25 | 10 |
| DOGE | 68 | 67 | 66 | 65 | 63 | 61 | 58 | 54 | 47 | 38 | 25 | 10 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-19 | 60g | 2026-09-17 | domani |
| SOL | 2026-07-19 | 60g | 2026-09-17 | domani |
| DOGE | 2026-07-19 | 60g | 2026-09-17 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 64 | 50,00% | +0,30% | +0,28% | UTILE |
| BTC | 2g | 63 | 50,79% | +0,55% | +0,47% | UTILE |
| BTC | 3g | 62 | 45,16% | +0,69% | +0,58% | UTILE |
| BTC | 5g | 60 | 41,67% | +1,43% | +1,22% | UTILE |
| BTC | 7g | 58 | 50,00% | +2,01% | +1,82% | PRIMA CALIBRAZIONE |
| BTC | 10g | 55 | 56,36% | +2,95% | +2,79% | PRIMA CALIBRAZIONE |
| BTC | 14g | 51 | 54,90% | +4,74% | +4,67% | PRIMA CALIBRAZIONE |
| BTC | 21g | 44 | 63,64% | +9,09% | +8,94% | PRIMA CALIBRAZIONE |
| BTC | 30g | 36 | 91,67% | +15,05% | +13,85% | PRIMA CALIBRAZIONE |
| BTC | 45g | 23 | 86,96% | +22,04% | +16,28% | FEEDBACK RAPIDO |
| BTC | 60g | 9 | 77,78% | +22,72% | +13,23% | FEEDBACK RAPIDO |
| SOL | 1g | 60 | 51,67% | +0,46% | +0,35% | UTILE |
| SOL | 2g | 59 | 47,46% | +0,98% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 3g | 58 | 53,45% | +1,60% | +1,45% | PRIMA CALIBRAZIONE |
| SOL | 5g | 56 | 55,36% | +2,77% | +2,67% | PRIMA CALIBRAZIONE |
| SOL | 7g | 54 | 59,26% | +3,87% | +3,97% | PRIMA CALIBRAZIONE |
| SOL | 10g | 51 | 62,75% | +5,63% | +5,78% | PRIMA CALIBRAZIONE |
| SOL | 14g | 47 | 70,21% | +8,58% | +9,35% | PRIMA CALIBRAZIONE |
| SOL | 21g | 40 | 77,50% | +15,70% | +14,81% | PRIMA CALIBRAZIONE |
| SOL | 30g | 31 | 67,74% | +21,97% | +15,59% | PRIMA CALIBRAZIONE |
| SOL | 45g | 19 | 42,11% | +33,98% | -6,53% | FEEDBACK RAPIDO |
| SOL | 60g | 9 | 33,33% | +32,96% | -10,60% | FEEDBACK RAPIDO |
| DOGE | 1g | 63 | 46,03% | +0,27% | +0,15% | UTILE |
| DOGE | 2g | 62 | 46,77% | +0,58% | +0,28% | UTILE |
| DOGE | 3g | 61 | 40,98% | +0,90% | +0,49% | UTILE |
| DOGE | 5g | 59 | 47,46% | +1,55% | +1,26% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 57 | 56,14% | +1,95% | +2,27% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 54 | 55,56% | +2,41% | +3,37% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 50 | 68,00% | +4,51% | +6,50% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 45 | 71,11% | +7,88% | +7,00% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 36 | 77,78% | +13,42% | +7,22% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 24 | 20,83% | +20,09% | -11,91% | FEEDBACK RAPIDO |
| DOGE | 60g | 10 | 0,00% | +17,41% | -17,41% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 64 | 50,00% | +0,30% | +0,28% | -0,15% | +0,83% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 67 | 52,24% | +0,29% | +0,29% | -0,15% | +0,80% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 67 | 52,24% | +0,29% | +0,29% | -0,15% | +0,80% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 62 | 40,32% | +0,39% | +0,05% | -0,07% | +0,90% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 26 | 42,31% | +0,67% | +0,43% | +0,02% | +1,19% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 63 | 50,79% | +0,55% | +0,47% | -0,02% | +1,20% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 66 | 53,03% | +0,64% | +0,64% | +0,07% | +1,29% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 66 | 53,03% | +0,64% | +0,64% | +0,07% | +1,29% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 61 | 44,26% | +0,78% | +0,10% | +0,21% | +1,42% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 25 | 44,00% | +1,05% | +0,61% | +0,46% | +1,73% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 62 | 45,16% | +0,69% | +0,58% | -1,11% | +2,44% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 65 | 52,31% | +0,96% | +0,96% | -1,09% | +2,65% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 65 | 52,31% | +0,96% | +0,96% | -1,09% | +2,65% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 60 | 36,67% | +1,21% | -0,20% | -0,95% | +2,87% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,81% | +0,20% | -0,58% | +3,31% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 60 | 41,67% | +1,43% | +1,22% | -1,72% | +3,81% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 63 | 47,62% | +1,67% | +1,67% | -1,69% | +4,09% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 63 | 47,62% | +1,67% | +1,67% | -1,69% | +4,09% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 58 | 39,66% | +1,91% | -1,01% | -1,53% | +4,38% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 24 | 50,00% | +3,70% | -1,14% | -1,03% | +5,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 58 | 50,00% | +2,01% | +1,82% | -2,01% | +4,89% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 61 | 55,74% | +2,32% | +2,32% | -1,98% | +5,17% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 61 | 55,74% | +2,32% | +2,32% | -1,98% | +5,17% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 56 | 39,29% | +2,73% | -1,83% | -1,82% | +5,53% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 24 | 45,83% | +4,87% | -2,81% | -1,33% | +8,02% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 55 | 56,36% | +2,95% | +2,79% | -2,19% | +6,08% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 58 | 60,34% | +3,14% | +3,14% | -2,18% | +6,31% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 58 | 60,34% | +3,14% | +3,14% | -2,18% | +6,31% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 53 | 43,40% | +3,54% | -1,47% | -1,99% | +6,79% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 24 | 50,00% | +5,20% | -3,59% | -1,59% | +8,77% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 51 | 54,90% | +4,74% | +4,67% | -2,21% | +8,50% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 54 | 55,56% | +4,85% | +4,85% | -2,21% | +8,63% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 54 | 55,56% | +4,85% | +4,85% | -2,21% | +8,63% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 49 | 51,02% | +5,48% | +0,53% | -1,98% | +9,34% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 22 | 31,82% | +5,27% | -3,66% | -1,53% | +9,82% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 44 | 63,64% | +9,09% | +8,94% | -2,18% | +13,19% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 47 | 70,21% | +8,94% | +8,94% | -2,19% | +13,06% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 47 | 70,21% | +8,94% | +8,94% | -2,19% | +13,06% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 42 | 40,48% | +9,82% | -1,02% | -1,92% | +14,03% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 15 | 33,33% | +10,93% | -9,70% | -0,96% | +15,50% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | -0,54% | -0,54% | -2,98% | +4,64% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 36 | 91,67% | +15,05% | +13,85% | -2,64% | +19,54% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 38 | 86,84% | +14,68% | +14,68% | -2,69% | +19,20% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 38 | 86,84% | +14,68% | +14,68% | -2,69% | +19,20% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 34 | 88,24% | +15,85% | +15,85% | -2,48% | +20,63% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 33 | 39,39% | +14,98% | -4,06% | -2,43% | +19,87% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 8 | 0,00% | +23,09% | -23,09% | -0,83% | +29,47% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 23 | 86,96% | +22,04% | +16,28% | -3,04% | +27,20% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 25 | 100,00% | +22,11% | +22,11% | -3,09% | +27,16% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 25 | 100,00% | +22,11% | +22,11% | -3,09% | +27,16% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 21 | 100,00% | +22,31% | +22,31% | -2,82% | +27,53% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 20 | 25,00% | +22,39% | -11,19% | -2,74% | +27,61% | FEEDBACK RAPIDO |
| BTC | 45g | Classic technical | CALIBRABILE | 3 | 0,00% | +21,72% | -21,72% | -1,93% | +29,65% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 9 | 77,78% | +22,72% | +13,23% | -2,48% | +29,34% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 10 | 100,00% | +22,31% | +22,31% | -2,50% | +29,28% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 10 | 100,00% | +22,31% | +22,31% | -2,50% | +29,28% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 10 | 100,00% | +22,31% | +22,31% | -2,50% | +29,28% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 9 | 33,33% | +22,20% | -7,65% | -2,41% | +29,34% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 63 | 46,03% | +0,27% | +0,15% | -0,40% | +1,21% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 66 | 59,09% | +0,17% | +0,56% | -0,51% | +1,06% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 66 | 59,09% | +0,17% | +0,56% | -0,51% | +1,06% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 60 | 53,33% | +0,08% | +0,45% | -0,62% | +0,95% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 39 | 43,59% | +0,08% | -0,31% | -0,58% | +0,78% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 62 | 46,77% | +0,58% | +0,28% | -0,21% | +1,79% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 65 | 58,46% | +0,41% | +0,92% | -0,37% | +1,54% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 65 | 58,46% | +0,41% | +0,92% | -0,37% | +1,54% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 59 | 55,93% | +0,04% | +0,63% | -0,73% | +1,14% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 38 | 44,74% | +0,23% | -0,96% | -0,53% | +1,16% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,90% | +2,61% | +2,02% | +4,90% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 61 | 40,98% | +0,90% | +0,49% | -1,93% | +3,95% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 64 | 56,25% | +0,72% | +1,31% | -2,06% | +3,61% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 64 | 56,25% | +0,72% | +1,31% | -2,06% | +3,61% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 58 | 46,55% | -0,06% | +0,52% | -2,33% | +2,75% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 37 | 32,43% | +0,56% | -1,92% | -2,31% | +3,73% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,49% | +2,26% | -0,95% | +6,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 59 | 47,46% | +1,55% | +1,26% | -2,90% | +6,14% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 62 | 53,23% | +1,43% | +2,16% | -2,96% | +5,89% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 62 | 53,23% | +1,43% | +2,16% | -2,96% | +5,89% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 56 | 57,14% | +0,42% | +0,48% | -3,41% | +4,91% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 35 | 37,14% | +1,49% | -3,98% | -3,27% | +6,12% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | +0,52% | +0,34% | -2,37% | +7,26% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 57 | 56,14% | +1,95% | +2,27% | -3,41% | +7,95% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 60 | 58,33% | +2,00% | +2,86% | -3,46% | +7,75% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 60 | 58,33% | +2,00% | +2,86% | -3,46% | +7,75% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 54 | 53,70% | +0,71% | +0,73% | -4,00% | +6,43% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,88% | -5,01% | -3,79% | +7,55% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,37% | -0,49% | -2,97% | +7,69% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 54 | 55,56% | +2,41% | +3,37% | -3,70% | +9,69% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 57 | 52,63% | +2,37% | +3,05% | -3,74% | +9,52% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 57 | 52,63% | +2,37% | +3,05% | -3,74% | +9,52% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 51 | 62,75% | +0,57% | +1,32% | -4,34% | +7,46% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 32 | 40,62% | +1,78% | -4,62% | -4,22% | +8,99% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | -0,68% | -1,01% | -4,16% | +8,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 50 | 68,00% | +4,51% | +6,50% | -4,02% | +13,24% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 53 | 73,58% | +4,05% | +6,09% | -4,03% | +12,77% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 53 | 73,58% | +4,05% | +6,09% | -4,03% | +12,77% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 47 | 57,45% | +1,17% | +0,80% | -4,73% | +9,05% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 31 | 48,39% | +3,26% | -3,87% | -4,53% | +11,11% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +6,58% | +1,67% | -3,33% | +14,96% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 45 | 71,11% | +7,88% | +7,00% | -4,11% | +18,64% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 46 | 80,43% | +8,32% | +10,89% | -4,04% | +18,98% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 46 | 80,43% | +8,32% | +10,89% | -4,04% | +18,98% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 40 | 57,50% | +5,22% | -3,74% | -4,88% | +14,48% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 31 | 48,39% | +5,15% | -7,22% | -4,78% | +14,11% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +7,18% | -0,50% | -3,01% | +20,33% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 36 | 77,78% | +13,42% | +7,22% | -3,93% | +27,09% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 38 | 89,47% | +13,85% | +12,65% | -3,96% | +27,78% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 38 | 89,47% | +13,85% | +12,65% | -3,96% | +27,78% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 36 | 94,44% | +13,07% | +14,91% | -3,98% | +27,25% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 33 | 42,42% | +12,15% | -9,80% | -4,39% | +25,43% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 25 | 44,00% | +10,47% | -10,47% | -4,32% | +22,19% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +30,85% | +15,03% | -1,31% | +42,05% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 24 | 20,83% | +20,09% | -11,91% | -5,30% | +38,89% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 25 | 36,00% | +20,00% | -5,31% | -5,36% | +38,82% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 25 | 36,00% | +20,00% | -5,31% | -5,36% | +38,82% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 23 | 39,13% | +19,28% | -3,31% | -5,50% | +38,58% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 25 | 0,00% | +20,00% | -20,00% | -5,36% | +38,82% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 20 | 0,00% | +20,53% | -20,53% | -5,27% | +38,90% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 10 | 0,00% | +17,41% | -17,41% | -6,79% | +37,10% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 10 | 0,00% | +17,41% | -17,41% | -6,79% | +37,10% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 10 | 0,00% | +17,41% | -17,41% | -6,79% | +37,10% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 10 | 0,00% | +17,41% | -17,41% | -6,79% | +37,10% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 10 | 0,00% | +17,41% | -17,41% | -6,79% | +37,10% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 9 | 0,00% | +17,70% | -17,70% | -6,65% | +37,31% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 60 | 51,67% | +0,46% | +0,35% | -0,25% | +1,33% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 62 | 53,23% | +0,21% | +0,20% | -0,45% | +1,05% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 65 | 52,31% | +0,25% | +0,14% | -0,41% | +1,09% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 60 | 48,33% | +0,26% | +0,23% | -0,46% | +1,06% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,49% | +0,45% | -0,33% | +1,40% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 59 | 47,46% | +0,98% | +0,87% | +0,06% | +2,01% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 61 | 44,26% | +0,66% | +0,27% | -0,27% | +1,47% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 64 | 43,75% | +0,65% | +0,24% | -0,26% | +1,53% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 60 | 41,67% | +0,65% | +0,14% | -0,22% | +1,72% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,75% | +0,73% | -0,18% | +1,69% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 58 | 53,45% | +1,60% | +1,45% | -1,58% | +3,98% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 60 | 46,67% | +1,18% | +0,69% | -1,84% | +3,56% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 63 | 46,03% | +1,14% | +0,64% | -1,81% | +3,55% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 60 | 46,67% | +1,03% | -0,07% | -1,90% | +3,36% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 42 | 52,38% | +1,01% | +0,88% | -1,83% | +3,26% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 56 | 55,36% | +2,77% | +2,67% | -2,27% | +6,30% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 58 | 50,00% | +2,19% | +1,25% | -2,53% | +5,71% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 61 | 49,18% | +2,12% | +1,16% | -2,50% | +5,62% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 59 | 45,76% | +2,19% | -0,51% | -2,63% | +5,53% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 42 | 54,76% | +1,47% | +1,33% | -2,64% | +4,74% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 54 | 59,26% | +3,87% | +3,97% | -2,70% | +7,97% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 56 | 55,36% | +3,21% | +2,07% | -2,97% | +7,34% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 59 | 55,93% | +3,04% | +1,97% | -2,96% | +7,17% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 58 | 39,66% | +2,99% | -1,34% | -3,11% | +7,10% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 42 | 47,62% | +1,36% | +1,40% | -3,24% | +5,52% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 51 | 62,75% | +5,63% | +5,78% | -2,85% | +10,23% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 53 | 58,49% | +4,91% | +4,05% | -3,19% | +9,32% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 56 | 57,14% | +4,63% | +3,84% | -3,20% | +9,03% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 55 | 45,45% | +4,09% | -2,02% | -3,38% | +8,64% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 39 | 53,85% | +1,48% | +1,57% | -3,51% | +6,38% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 47 | 70,21% | +8,58% | +9,35% | -3,04% | +14,42% | PRIMA CALIBRAZIONE |

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
