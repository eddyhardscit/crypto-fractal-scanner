# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-12 05:32 UTC

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

Segnali totali salvati: **192**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-12 | BTC | 77.204,26 | +3 | +3 | +3 | 0 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-12 | DOGE | 0.08434 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-12 | SOL | 101,54 | +4 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-11 | BTC | 77.053,66 | +5 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-11 | DOGE | 0.08388 | -6 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-11 | SOL | 99,59 | +2 | +2 | +2 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-10 | BTC | 78.479,28 | +6 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-10 | DOGE | 0.08593 | -4 | -2 | -2 | 0 | -1 | 0 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-10 | SOL | 102,04 | +5 | +2 | +2 | 0 | +2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-09 | BTC | 78.978,35 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-09 | DOGE | 0.09017 | +3 | -1 | -1 | 0 | +3 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-09 | SOL | 104,26 | +5 | +2 | +2 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 64 | 63 | 62 | 61 | 59 | 57 | 54 | 50 | 43 | 34 | 21 | 6 |
| SOL | 64 | 63 | 62 | 61 | 59 | 57 | 54 | 50 | 43 | 34 | 21 | 6 |
| DOGE | 64 | 63 | 62 | 61 | 59 | 57 | 54 | 50 | 43 | 34 | 21 | 6 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-15 | 60g | 2026-09-13 | domani |
| SOL | 2026-07-15 | 60g | 2026-09-13 | domani |
| DOGE | 2026-07-15 | 60g | 2026-09-13 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 60 | 50,00% | +0,35% | +0,33% | UTILE |
| BTC | 2g | 59 | 49,15% | +0,61% | +0,53% | PRIMA CALIBRAZIONE |
| BTC | 3g | 58 | 44,83% | +0,79% | +0,67% | PRIMA CALIBRAZIONE |
| BTC | 5g | 56 | 44,64% | +1,66% | +1,43% | PRIMA CALIBRAZIONE |
| BTC | 7g | 54 | 53,70% | +2,38% | +2,18% | PRIMA CALIBRAZIONE |
| BTC | 10g | 51 | 60,78% | +3,42% | +3,25% | PRIMA CALIBRAZIONE |
| BTC | 14g | 47 | 59,57% | +5,28% | +5,20% | PRIMA CALIBRAZIONE |
| BTC | 21g | 40 | 65,00% | +10,15% | +9,99% | PRIMA CALIBRAZIONE |
| BTC | 30g | 32 | 90,62% | +14,16% | +12,82% | PRIMA CALIBRAZIONE |
| BTC | 45g | 19 | 84,21% | +22,27% | +15,31% | FEEDBACK RAPIDO |
| BTC | 60g | 6 | 100,00% | +23,67% | +23,67% | FEEDBACK RAPIDO |
| SOL | 1g | 56 | 53,57% | +0,57% | +0,46% | PRIMA CALIBRAZIONE |
| SOL | 2g | 55 | 49,09% | +1,11% | +0,99% | PRIMA CALIBRAZIONE |
| SOL | 3g | 54 | 55,56% | +1,80% | +1,63% | PRIMA CALIBRAZIONE |
| SOL | 5g | 52 | 59,62% | +3,14% | +3,03% | PRIMA CALIBRAZIONE |
| SOL | 7g | 50 | 64,00% | +4,53% | +4,63% | PRIMA CALIBRAZIONE |
| SOL | 10g | 47 | 65,96% | +6,34% | +6,50% | PRIMA CALIBRAZIONE |
| SOL | 14g | 43 | 76,74% | +9,63% | +10,47% | PRIMA CALIBRAZIONE |
| SOL | 21g | 36 | 77,78% | +17,01% | +16,02% | PRIMA CALIBRAZIONE |
| SOL | 30g | 27 | 62,96% | +20,35% | +13,02% | FEEDBACK RAPIDO |
| SOL | 45g | 15 | 40,00% | +33,36% | -7,93% | FEEDBACK RAPIDO |
| SOL | 60g | 5 | 40,00% | +33,73% | -6,01% | FEEDBACK RAPIDO |
| DOGE | 1g | 59 | 44,07% | +0,37% | +0,07% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 58 | 44,83% | +0,73% | +0,19% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 57 | 38,60% | +1,11% | +0,37% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 55 | 47,27% | +2,04% | +1,43% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 53 | 60,38% | +2,71% | +3,06% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 50 | 56,00% | +2,91% | +3,81% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 47 | 68,09% | +4,87% | +6,86% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 41 | 78,05% | +9,46% | +8,50% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 32 | 75,00% | +12,74% | +5,77% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 20 | 15,00% | +20,40% | -14,19% | FEEDBACK RAPIDO |
| DOGE | 60g | 6 | 0,00% | +19,80% | -19,80% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 60 | 50,00% | +0,35% | +0,33% | -0,09% | +0,89% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 63 | 52,38% | +0,33% | +0,33% | -0,10% | +0,85% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 63 | 52,38% | +0,33% | +0,33% | -0,10% | +0,85% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 58 | 39,66% | +0,45% | +0,09% | -0,01% | +0,96% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,81% | +0,37% | +0,13% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 59 | 49,15% | +0,61% | +0,53% | +0,03% | +1,27% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 62 | 51,61% | +0,70% | +0,70% | +0,13% | +1,36% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 62 | 51,61% | +0,70% | +0,70% | +0,13% | +1,36% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 57 | 42,11% | +0,85% | +0,13% | +0,28% | +1,51% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,18% | +0,55% | +0,59% | +1,89% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 58 | 44,83% | +0,79% | +0,67% | -1,06% | +2,49% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 61 | 52,46% | +1,07% | +1,07% | -1,04% | +2,71% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 61 | 52,46% | +1,07% | +1,07% | -1,04% | +2,71% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 56 | 35,71% | +1,34% | -0,16% | -0,89% | +2,95% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,81% | +0,20% | -0,58% | +3,31% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 56 | 44,64% | +1,66% | +1,43% | -1,63% | +3,95% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 59 | 50,85% | +1,90% | +1,90% | -1,60% | +4,25% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 59 | 50,85% | +1,90% | +1,90% | -1,60% | +4,25% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 54 | 42,59% | +2,17% | -0,96% | -1,43% | +4,57% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 24 | 50,00% | +3,70% | -1,14% | -1,03% | +5,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 54 | 53,70% | +2,38% | +2,18% | -1,85% | +5,20% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 57 | 59,65% | +2,69% | +2,69% | -1,82% | +5,48% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 57 | 59,65% | +2,69% | +2,69% | -1,82% | +5,48% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 52 | 42,31% | +3,17% | -1,74% | -1,63% | +5,90% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 24 | 45,83% | +4,87% | -2,81% | -1,33% | +8,02% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | -0,70% | -0,70% | -2,63% | +2,73% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 51 | 60,78% | +3,42% | +3,25% | -2,02% | +6,42% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 54 | 64,81% | +3,60% | +3,60% | -2,02% | +6,66% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 54 | 64,81% | +3,60% | +3,60% | -2,02% | +6,66% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 49 | 46,94% | +4,08% | -1,34% | -1,80% | +7,21% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 22 | 54,55% | +5,87% | -3,72% | -1,40% | +9,34% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 47 | 59,57% | +5,28% | +5,20% | -2,15% | +8,79% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 50 | 60,00% | +5,36% | +5,36% | -2,16% | +8,90% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 50 | 60,00% | +5,36% | +5,36% | -2,16% | +8,90% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 45 | 55,56% | +6,10% | +0,72% | -1,90% | +9,70% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 18 | 38,89% | +6,79% | -4,13% | -1,24% | +10,85% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 40 | 65,00% | +10,15% | +9,99% | -2,10% | +13,99% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 43 | 72,09% | +9,92% | +9,92% | -2,13% | +13,79% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 43 | 72,09% | +9,92% | +9,92% | -2,13% | +13,79% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 38 | 39,47% | +11,02% | -0,96% | -1,82% | +14,97% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 11 | 27,27% | +15,48% | -12,65% | -0,26% | +19,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 32 | 90,62% | +14,16% | +12,82% | -2,96% | +18,17% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 34 | 85,29% | +13,80% | +13,80% | -3,00% | +17,88% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 34 | 85,29% | +13,80% | +13,80% | -3,00% | +17,88% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 30 | 86,67% | +15,02% | +15,02% | -2,80% | +19,32% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 29 | 44,83% | +13,99% | -1,57% | -2,74% | +18,41% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 19 | 84,21% | +22,27% | +15,31% | -3,20% | +26,78% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 21 | 100,00% | +22,34% | +22,34% | -3,24% | +26,77% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 21 | 100,00% | +22,34% | +22,34% | -3,24% | +26,77% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 17 | 100,00% | +22,64% | +22,64% | -2,95% | +27,14% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 17 | 29,41% | +22,62% | -9,44% | -2,88% | +27,25% | FEEDBACK RAPIDO |
| BTC | 45g | Classic technical | CALIBRABILE | 2 | 0,00% | +21,18% | -21,18% | -2,23% | +29,25% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 6 | 100,00% | +23,67% | +23,67% | -2,29% | +29,81% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 6 | 100,00% | +23,67% | +23,67% | -2,29% | +29,81% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 6 | 100,00% | +23,67% | +23,67% | -2,29% | +29,81% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 6 | 100,00% | +23,67% | +23,67% | -2,29% | +29,81% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 5 | 40,00% | +23,75% | -5,45% | -2,09% | +30,01% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 59 | 44,07% | +0,37% | +0,07% | -0,29% | +1,34% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 62 | 58,06% | +0,27% | +0,51% | -0,41% | +1,18% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 62 | 58,06% | +0,27% | +0,51% | -0,41% | +1,18% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 56 | 51,79% | +0,17% | +0,39% | -0,52% | +1,07% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 35 | 40,00% | +0,23% | -0,49% | -0,42% | +0,95% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 58 | 44,83% | +0,73% | +0,19% | -0,06% | +1,98% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 61 | 57,38% | +0,54% | +0,88% | -0,24% | +1,71% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 61 | 57,38% | +0,54% | +0,88% | -0,24% | +1,71% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 55 | 54,55% | +0,15% | +0,56% | -0,61% | +1,30% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,45% | -1,26% | -0,31% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,90% | +2,61% | +2,02% | +4,90% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 57 | 38,60% | +1,11% | +0,37% | -1,82% | +4,12% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 60 | 55,00% | +0,91% | +1,25% | -1,96% | +3,75% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 60 | 55,00% | +0,91% | +1,25% | -1,96% | +3,75% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 54 | 44,44% | +0,09% | +0,41% | -2,24% | +2,84% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 34 | 29,41% | +0,82% | -2,31% | -2,19% | +3,95% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,49% | +2,26% | -0,95% | +6,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 55 | 47,27% | +2,04% | +1,43% | -2,63% | +6,52% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 58 | 50,00% | +1,89% | +1,95% | -2,71% | +6,24% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 58 | 50,00% | +1,89% | +1,95% | -2,71% | +6,24% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 52 | 57,69% | +0,85% | +0,60% | -3,16% | +5,22% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 33 | 36,36% | +1,89% | -4,18% | -3,06% | +6,37% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | +0,52% | +0,34% | -2,37% | +7,26% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 53 | 60,38% | +2,71% | +3,06% | -2,95% | +8,52% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 56 | 55,36% | +2,73% | +2,48% | -3,02% | +8,29% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 56 | 55,36% | +2,73% | +2,48% | -3,02% | +8,29% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 50 | 58,00% | +1,42% | +1,44% | -3,55% | +6,92% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +0,41% | +0,28% | -2,23% | +8,54% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 50 | 56,00% | +2,91% | +3,81% | -3,57% | +9,84% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 53 | 50,94% | +2,84% | +2,99% | -3,61% | +9,65% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 53 | 50,94% | +2,84% | +2,99% | -3,61% | +9,65% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 47 | 65,96% | +0,95% | +1,76% | -4,26% | +7,44% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +0,72% | +0,35% | -3,12% | +9,19% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 47 | 68,09% | +4,87% | +6,86% | -4,01% | +13,26% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 49 | 73,47% | +4,42% | +6,55% | -4,05% | +12,74% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 49 | 73,47% | +4,42% | +6,55% | -4,05% | +12,74% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 43 | 60,47% | +1,32% | +0,91% | -4,81% | +8,67% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 31 | 48,39% | +3,26% | -3,87% | -4,53% | +11,11% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +6,58% | +1,67% | -3,33% | +14,96% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 41 | 78,05% | +9,46% | +8,50% | -3,40% | +20,05% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 43 | 86,05% | +9,49% | +12,24% | -3,45% | +20,12% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 43 | 86,05% | +9,49% | +12,24% | -3,45% | +20,12% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 36 | 63,89% | +6,72% | -3,23% | -4,15% | +15,62% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 28 | 53,57% | +6,61% | -7,08% | -3,96% | +15,32% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +9,78% | +0,82% | -1,43% | +23,27% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 32 | 75,00% | +12,74% | +5,77% | -4,35% | +25,08% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 34 | 88,24% | +13,27% | +11,92% | -4,36% | +25,97% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 34 | 88,24% | +13,27% | +11,92% | -4,36% | +25,97% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 32 | 93,75% | +12,35% | +14,42% | -4,40% | +25,26% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 30 | 40,00% | +11,60% | -11,60% | -4,76% | +23,68% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 22 | 50,00% | +9,38% | -9,38% | -4,86% | +19,29% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +30,85% | +15,03% | -1,31% | +42,05% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 20 | 15,00% | +20,40% | -14,19% | -5,84% | +38,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 21 | 23,81% | +20,28% | -9,85% | -5,88% | +38,06% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 21 | 23,81% | +20,28% | -9,85% | -5,88% | +38,06% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 19 | 26,32% | +19,45% | -7,91% | -6,11% | +37,69% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 21 | 0,00% | +20,28% | -20,28% | -5,88% | +38,06% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 17 | 0,00% | +20,63% | -20,63% | -5,74% | +38,18% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 6 | 0,00% | +19,80% | -19,80% | -6,84% | +37,03% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 6 | 0,00% | +19,80% | -19,80% | -6,84% | +37,03% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 6 | 0,00% | +19,80% | -19,80% | -6,84% | +37,03% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 6 | 0,00% | +19,80% | -19,80% | -6,84% | +37,03% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 6 | 0,00% | +19,80% | -19,80% | -6,84% | +37,03% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 6 | 0,00% | +19,80% | -19,80% | -6,84% | +37,03% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 56 | 53,57% | +0,57% | +0,46% | -0,14% | +1,45% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 58 | 55,17% | +0,30% | +0,29% | -0,35% | +1,16% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 61 | 54,10% | +0,34% | +0,22% | -0,32% | +1,19% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 59 | 49,15% | +0,27% | +0,25% | -0,43% | +1,09% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,49% | +0,45% | -0,33% | +1,40% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 55 | 49,09% | +1,11% | +0,99% | +0,18% | +2,17% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 57 | 45,61% | +0,77% | +0,34% | -0,18% | +1,58% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 60 | 45,00% | +0,74% | +0,31% | -0,17% | +1,64% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 59 | 42,37% | +0,68% | +0,16% | -0,20% | +1,73% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,75% | +0,73% | -0,18% | +1,69% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 54 | 55,56% | +1,80% | +1,63% | -1,49% | +4,09% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 56 | 48,21% | +1,34% | +0,81% | -1,77% | +3,63% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 59 | 47,46% | +1,29% | +0,76% | -1,74% | +3,62% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 58 | 48,28% | +1,15% | +0,02% | -1,81% | +3,37% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 42 | 52,38% | +1,01% | +0,88% | -1,83% | +3,26% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 52 | 59,62% | +3,14% | +3,03% | -2,13% | +6,55% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 54 | 53,70% | +2,50% | +1,50% | -2,41% | +5,91% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 57 | 52,63% | +2,41% | +1,38% | -2,39% | +5,81% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 56 | 48,21% | +2,41% | -0,44% | -2,54% | +5,70% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 40 | 57,50% | +1,65% | +1,51% | -2,53% | +4,89% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 50 | 64,00% | +4,53% | +4,63% | -2,41% | +8,52% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 52 | 59,62% | +3,79% | +2,57% | -2,71% | +7,83% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 55 | 60,00% | +3,58% | +2,43% | -2,71% | +7,61% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 54 | 42,59% | +3,53% | -1,11% | -2,87% | +7,55% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 38 | 52,63% | +1,96% | +2,01% | -2,91% | +5,99% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 47 | 65,96% | +6,34% | +6,50% | -2,68% | +10,77% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 49 | 61,22% | +5,53% | +4,59% | -3,06% | +9,76% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 52 | 59,62% | +5,20% | +4,34% | -3,08% | +9,42% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 51 | 47,06% | +4,62% | -1,97% | -3,28% | +9,01% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 35 | 57,14% | +1,95% | +2,05% | -3,37% | +6,66% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 43 | 76,74% | +9,63% | +10,47% | -2,80% | +15,39% | PRIMA CALIBRAZIONE |

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
