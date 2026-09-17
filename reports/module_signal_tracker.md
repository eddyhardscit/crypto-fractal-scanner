# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-17 05:33 UTC

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

Segnali totali salvati: **207**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-17 | BTC | 76.325,40 | +2 | +3 | +3 | 0 | 0 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-17 | DOGE | 0.08084 | -6 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-17 | SOL | 99,49 | 0 | +3 | +3 | 0 | -1 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-16 | BTC | 75.786,49 | +2 | +3 | +3 | 0 | 0 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-09-16 | DOGE | 0.08011 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-16 | SOL | 97,05 | +2 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-15 | BTC | 77.430,91 | +4 | +3 | +3 | 0 | +1 | -1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-15 | DOGE | 0.08280 | -4 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-15 | SOL | 100,84 | +2 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-14 | BTC | 77.497,87 | +3 | +3 | +3 | 0 | +1 | -1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-14 | DOGE | 0.08404 | -4 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-14 | SOL | 101,01 | +3 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 69 | 68 | 67 | 66 | 64 | 62 | 59 | 55 | 48 | 39 | 26 | 11 |
| SOL | 69 | 68 | 67 | 66 | 64 | 62 | 59 | 55 | 48 | 39 | 26 | 11 |
| DOGE | 69 | 68 | 67 | 66 | 64 | 62 | 59 | 55 | 48 | 39 | 26 | 11 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-20 | 60g | 2026-09-18 | domani |
| SOL | 2026-07-20 | 60g | 2026-09-18 | domani |
| DOGE | 2026-07-20 | 60g | 2026-09-18 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 65 | 50,77% | +0,31% | +0,29% | UTILE |
| BTC | 2g | 64 | 50,00% | +0,52% | +0,44% | UTILE |
| BTC | 3g | 63 | 44,44% | +0,66% | +0,55% | UTILE |
| BTC | 5g | 61 | 40,98% | +1,39% | +1,18% | UTILE |
| BTC | 7g | 59 | 49,15% | +1,93% | +1,75% | PRIMA CALIBRAZIONE |
| BTC | 10g | 56 | 55,36% | +2,82% | +2,66% | PRIMA CALIBRAZIONE |
| BTC | 14g | 52 | 53,85% | +4,63% | +4,56% | PRIMA CALIBRAZIONE |
| BTC | 21g | 45 | 62,22% | +8,82% | +8,67% | PRIMA CALIBRAZIONE |
| BTC | 30g | 36 | 91,67% | +15,05% | +13,85% | PRIMA CALIBRAZIONE |
| BTC | 45g | 24 | 87,50% | +22,02% | +16,51% | FEEDBACK RAPIDO |
| BTC | 60g | 10 | 80,00% | +22,23% | +13,69% | FEEDBACK RAPIDO |
| SOL | 1g | 61 | 52,46% | +0,49% | +0,39% | UTILE |
| SOL | 2g | 60 | 46,67% | +0,95% | +0,83% | UTILE |
| SOL | 3g | 59 | 52,54% | +1,55% | +1,40% | PRIMA CALIBRAZIONE |
| SOL | 5g | 57 | 54,39% | +2,68% | +2,59% | PRIMA CALIBRAZIONE |
| SOL | 7g | 55 | 58,18% | +3,75% | +3,85% | PRIMA CALIBRAZIONE |
| SOL | 10g | 52 | 61,54% | +5,41% | +5,56% | PRIMA CALIBRAZIONE |
| SOL | 14g | 48 | 68,75% | +8,39% | +9,14% | PRIMA CALIBRAZIONE |
| SOL | 21g | 41 | 75,61% | +15,28% | +14,42% | PRIMA CALIBRAZIONE |
| SOL | 30g | 32 | 68,75% | +22,26% | +16,09% | PRIMA CALIBRAZIONE |
| SOL | 45g | 20 | 45,00% | +34,10% | -4,38% | FEEDBACK RAPIDO |
| SOL | 60g | 10 | 30,00% | +32,75% | -12,62% | FEEDBACK RAPIDO |
| DOGE | 1g | 64 | 45,31% | +0,28% | +0,13% | UTILE |
| DOGE | 2g | 63 | 47,62% | +0,54% | +0,31% | UTILE |
| DOGE | 3g | 62 | 41,94% | +0,82% | +0,54% | UTILE |
| DOGE | 5g | 60 | 48,33% | +1,46% | +1,31% | UTILE |
| DOGE | 7g | 58 | 56,90% | +1,81% | +2,34% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 55 | 54,55% | +2,18% | +3,12% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 51 | 68,63% | +4,39% | +6,41% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 46 | 71,74% | +7,58% | +6,99% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 37 | 78,38% | +13,49% | +7,46% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 25 | 20,00% | +19,91% | -12,06% | FEEDBACK RAPIDO |
| DOGE | 60g | 11 | 0,00% | +16,88% | -16,88% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 65 | 50,77% | +0,31% | +0,29% | -0,14% | +0,83% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 68 | 52,94% | +0,29% | +0,29% | -0,15% | +0,80% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 68 | 52,94% | +0,29% | +0,29% | -0,15% | +0,80% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 62 | 40,32% | +0,39% | +0,05% | -0,07% | +0,90% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 27 | 40,74% | +0,67% | +0,39% | +0,03% | +1,19% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 64 | 50,00% | +0,52% | +0,44% | -0,05% | +1,16% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 67 | 52,24% | +0,61% | +0,61% | +0,04% | +1,25% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 67 | 52,24% | +0,61% | +0,61% | +0,04% | +1,25% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 62 | 43,55% | +0,74% | +0,07% | +0,18% | +1,38% | UTILE |
| BTC | 2g | Classic technical | CALIBRABILE | 26 | 46,15% | +0,95% | +0,65% | +0,37% | +1,63% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 63 | 44,44% | +0,66% | +0,55% | -1,14% | +2,42% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 66 | 51,52% | +0,93% | +0,93% | -1,12% | +2,62% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 66 | 51,52% | +0,93% | +0,93% | -1,12% | +2,62% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 61 | 36,07% | +1,16% | -0,22% | -0,99% | +2,84% | UTILE |
| BTC | 3g | Classic technical | CALIBRABILE | 25 | 44,00% | +1,67% | +0,25% | -0,69% | +3,22% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 61 | 40,98% | +1,39% | +1,18% | -1,74% | +3,80% | UTILE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 64 | 46,88% | +1,63% | +1,63% | -1,70% | +4,08% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 64 | 46,88% | +1,63% | +1,63% | -1,70% | +4,08% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 59 | 38,98% | +1,86% | -1,01% | -1,56% | +4,36% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 24 | 50,00% | +3,70% | -1,14% | -1,03% | +5,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 59 | 49,15% | +1,93% | +1,75% | -2,05% | +4,84% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 62 | 54,84% | +2,24% | +2,24% | -2,02% | +5,11% | UTILE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 62 | 54,84% | +2,24% | +2,24% | -2,02% | +5,11% | UTILE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 57 | 38,60% | +2,63% | -1,84% | -1,87% | +5,47% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 24 | 45,83% | +4,87% | -2,81% | -1,33% | +8,02% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 56 | 55,36% | +2,82% | +2,66% | -2,26% | +5,97% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 59 | 59,32% | +3,01% | +3,01% | -2,25% | +6,21% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 59 | 59,32% | +3,01% | +3,01% | -2,25% | +6,21% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 54 | 42,59% | +3,40% | -1,53% | -2,07% | +6,67% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 24 | 50,00% | +5,20% | -3,59% | -1,59% | +8,77% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 52 | 53,85% | +4,63% | +4,56% | -2,23% | +8,44% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 55 | 54,55% | +4,74% | +4,74% | -2,22% | +8,57% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 55 | 54,55% | +4,74% | +4,74% | -2,22% | +8,57% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 50 | 50,00% | +5,34% | +0,50% | -2,00% | +9,26% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 23 | 30,43% | +4,99% | -3,56% | -1,60% | +9,63% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 45 | 62,22% | +8,82% | +8,67% | -2,23% | +13,00% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 48 | 68,75% | +8,70% | +8,70% | -2,25% | +12,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 48 | 68,75% | +8,70% | +8,70% | -2,25% | +12,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 43 | 39,53% | +9,52% | -1,07% | -1,99% | +13,82% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 16 | 31,25% | +10,06% | -9,28% | -1,20% | +14,82% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | -0,54% | -0,54% | -2,98% | +4,64% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 36 | 91,67% | +15,05% | +13,85% | -2,64% | +19,54% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 39 | 87,18% | +14,79% | +14,79% | -2,63% | +19,43% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 39 | 87,18% | +14,79% | +14,79% | -2,63% | +19,43% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 34 | 88,24% | +15,85% | +15,85% | -2,48% | +20,63% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 34 | 38,24% | +15,09% | -4,50% | -2,36% | +20,11% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 8 | 0,00% | +23,09% | -23,09% | -0,83% | +29,47% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 24 | 87,50% | +22,02% | +16,51% | -2,93% | +27,36% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 26 | 100,00% | +22,09% | +22,09% | -2,98% | +27,31% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 26 | 100,00% | +22,09% | +22,09% | -2,98% | +27,31% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 22 | 100,00% | +22,28% | +22,28% | -2,71% | +27,69% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 21 | 23,81% | +22,36% | -11,69% | -2,63% | +27,78% | FEEDBACK RAPIDO |
| BTC | 45g | Classic technical | CALIBRABILE | 4 | 0,00% | +21,70% | -21,70% | -1,55% | +30,01% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 10 | 80,00% | +22,23% | +13,69% | -2,63% | +29,11% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 11 | 100,00% | +21,91% | +21,91% | -2,62% | +29,08% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 11 | 100,00% | +21,91% | +21,91% | -2,62% | +29,08% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 10 | 100,00% | +22,31% | +22,31% | -2,50% | +29,28% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 10 | 40,00% | +21,77% | -5,10% | -2,56% | +29,11% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 64 | 45,31% | +0,28% | +0,13% | -0,39% | +1,21% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 67 | 58,21% | +0,18% | +0,54% | -0,49% | +1,07% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 67 | 58,21% | +0,18% | +0,54% | -0,49% | +1,07% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 61 | 52,46% | +0,09% | +0,43% | -0,61% | +0,96% | UTILE |
| DOGE | 1g | Classic technical | CALIBRABILE | 40 | 42,50% | +0,10% | -0,32% | -0,56% | +0,80% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 63 | 47,62% | +0,54% | +0,31% | -0,25% | +1,73% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 66 | 59,09% | +0,37% | +0,94% | -0,41% | +1,49% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 66 | 59,09% | +0,37% | +0,94% | -0,41% | +1,49% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 60 | 56,67% | -0,00% | +0,65% | -0,77% | +1,09% | UTILE |
| DOGE | 2g | Classic technical | CALIBRABILE | 39 | 46,15% | +0,17% | -0,88% | -0,59% | +1,08% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,90% | +2,61% | +2,02% | +4,90% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 62 | 41,94% | +0,82% | +0,54% | -2,00% | +3,88% | UTILE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 65 | 56,92% | +0,65% | +1,34% | -2,12% | +3,56% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 65 | 56,92% | +0,65% | +1,34% | -2,12% | +3,56% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 59 | 47,46% | -0,12% | +0,58% | -2,40% | +2,70% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 38 | 34,21% | +0,44% | -1,77% | -2,40% | +3,63% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,49% | +2,26% | -0,95% | +6,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 60 | 48,33% | +1,46% | +1,31% | -2,96% | +6,07% | UTILE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 63 | 53,97% | +1,35% | +2,19% | -3,02% | +5,83% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 63 | 53,97% | +1,35% | +2,19% | -3,02% | +5,83% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 57 | 57,89% | +0,34% | +0,54% | -3,46% | +4,86% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 36 | 38,89% | +1,34% | -3,75% | -3,35% | +6,00% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | +0,52% | +0,34% | -2,37% | +7,26% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 58 | 56,90% | +1,81% | +2,34% | -3,49% | +7,85% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 61 | 59,02% | +1,87% | +2,91% | -3,54% | +7,66% | UTILE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 61 | 59,02% | +1,87% | +2,91% | -3,54% | +7,66% | UTILE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 55 | 54,55% | +0,59% | +0,82% | -4,07% | +6,35% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,88% | -5,01% | -3,79% | +7,55% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,37% | -0,49% | -2,97% | +7,69% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 55 | 54,55% | +2,18% | +3,12% | -3,86% | +9,54% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 58 | 53,45% | +2,15% | +3,18% | -3,89% | +9,38% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 58 | 53,45% | +2,15% | +3,18% | -3,89% | +9,38% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 52 | 61,54% | +0,36% | +1,10% | -4,50% | +7,35% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 33 | 39,39% | +1,41% | -4,80% | -4,47% | +8,76% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | -0,68% | -1,01% | -4,16% | +8,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 51 | 68,63% | +4,39% | +6,41% | -4,02% | +13,26% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 54 | 74,07% | +3,94% | +6,01% | -4,03% | +12,80% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 54 | 74,07% | +3,94% | +6,01% | -4,03% | +12,80% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 48 | 56,25% | +1,11% | +0,75% | -4,71% | +9,16% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 31 | 48,39% | +3,26% | -3,87% | -4,53% | +11,11% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +6,58% | +1,67% | -3,33% | +14,96% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 46 | 71,74% | +7,58% | +6,99% | -4,21% | +18,44% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 47 | 80,85% | +8,01% | +10,79% | -4,13% | +18,78% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 47 | 80,85% | +8,01% | +10,79% | -4,13% | +18,78% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 41 | 56,10% | +4,94% | -3,80% | -4,96% | +14,35% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 31 | 48,39% | +5,15% | -7,22% | -4,78% | +14,11% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +7,18% | -0,50% | -3,01% | +20,33% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 37 | 78,38% | +13,49% | +7,46% | -3,82% | +27,54% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 39 | 89,74% | +13,91% | +12,74% | -3,86% | +28,18% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 39 | 89,74% | +13,91% | +12,74% | -3,86% | +28,18% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 37 | 94,59% | +13,15% | +14,93% | -3,86% | +27,69% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 33 | 42,42% | +12,15% | -9,80% | -4,39% | +25,43% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 26 | 42,31% | +10,69% | -10,69% | -4,15% | +23,01% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +30,85% | +15,03% | -1,31% | +42,05% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 25 | 20,00% | +19,91% | -12,06% | -5,18% | +39,06% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 26 | 38,46% | +19,84% | -4,50% | -5,24% | +38,99% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 26 | 38,46% | +19,84% | -4,50% | -5,24% | +38,99% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 24 | 41,67% | +19,14% | -2,52% | -5,36% | +38,77% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 26 | 0,00% | +19,84% | -19,84% | -5,24% | +38,99% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 20 | 0,00% | +20,53% | -20,53% | -5,27% | +38,90% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 11 | 0,00% | +16,88% | -16,88% | -6,73% | +37,18% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 11 | 0,00% | +16,88% | -16,88% | -6,73% | +37,18% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 11 | 0,00% | +16,88% | -16,88% | -6,73% | +37,18% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 11 | 0,00% | +16,88% | -16,88% | -6,73% | +37,18% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 11 | 0,00% | +16,88% | -16,88% | -6,73% | +37,18% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 10 | 0,00% | +17,09% | -17,09% | -6,60% | +37,38% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 61 | 52,46% | +0,49% | +0,39% | -0,23% | +1,35% | UTILE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 63 | 53,97% | +0,25% | +0,23% | -0,42% | +1,08% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 66 | 53,03% | +0,28% | +0,17% | -0,38% | +1,12% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 60 | 48,33% | +0,26% | +0,23% | -0,46% | +1,06% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,49% | +0,45% | -0,33% | +1,40% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 60 | 46,67% | +0,95% | +0,83% | +0,02% | +1,96% | UTILE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 62 | 43,55% | +0,63% | +0,24% | -0,30% | +1,43% | UTILE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 65 | 43,08% | +0,62% | +0,21% | -0,29% | +1,49% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 60 | 41,67% | +0,65% | +0,14% | -0,22% | +1,72% | UTILE |
| SOL | 2g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,75% | +0,73% | -0,18% | +1,69% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 59 | 52,54% | +1,55% | +1,40% | -1,64% | +3,94% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 61 | 45,90% | +1,14% | +0,65% | -1,89% | +3,53% | UTILE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 64 | 45,31% | +1,10% | +0,61% | -1,85% | +3,52% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 60 | 46,67% | +1,03% | -0,07% | -1,90% | +3,36% | UTILE |
| SOL | 3g | Classic technical | CALIBRABILE | 42 | 52,38% | +1,01% | +0,88% | -1,83% | +3,26% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 57 | 54,39% | +2,68% | +2,59% | -2,32% | +6,24% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 59 | 49,15% | +2,12% | +1,20% | -2,57% | +5,66% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 62 | 48,39% | +2,05% | +1,10% | -2,54% | +5,58% | UTILE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 59 | 45,76% | +2,19% | -0,51% | -2,63% | +5,53% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 42 | 54,76% | +1,47% | +1,33% | -2,64% | +4,74% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 55 | 58,18% | +3,75% | +3,85% | -2,76% | +7,89% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 57 | 54,39% | +3,11% | +1,99% | -3,02% | +7,27% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 60 | 55,00% | +2,95% | +1,90% | -3,00% | +7,10% | UTILE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 59 | 38,98% | +2,89% | -1,36% | -3,15% | +7,04% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 42 | 47,62% | +1,36% | +1,40% | -3,24% | +5,52% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 52 | 61,54% | +5,41% | +5,56% | -2,96% | +10,04% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 54 | 57,41% | +4,71% | +3,86% | -3,29% | +9,15% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 57 | 56,14% | +4,45% | +3,67% | -3,30% | +8,87% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 56 | 44,64% | +3,92% | -2,09% | -3,48% | +8,49% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 40 | 52,50% | +1,30% | +1,39% | -3,64% | +6,22% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 48 | 68,75% | +8,39% | +9,14% | -3,05% | +14,26% | PRIMA CALIBRAZIONE |

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
