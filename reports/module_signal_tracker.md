# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-13 05:33 UTC

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

Segnali totali salvati: **195**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-13 | BTC | 77.274,99 | +6 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-13 | DOGE | 0.08485 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-13 | SOL | 101,86 | +4 | +3 | +3 | 0 | +1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-12 | BTC | 77.204,26 | +3 | +3 | +3 | 0 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-12 | DOGE | 0.08434 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-12 | SOL | 101,54 | +4 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-11 | BTC | 77.053,66 | +5 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-11 | DOGE | 0.08388 | -6 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-11 | SOL | 99,59 | +2 | +2 | +2 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-10 | BTC | 78.479,28 | +6 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-10 | DOGE | 0.08593 | -4 | -2 | -2 | 0 | -1 | 0 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-10 | SOL | 102,04 | +5 | +2 | +2 | 0 | +2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 65 | 64 | 63 | 62 | 60 | 58 | 55 | 51 | 44 | 35 | 22 | 7 |
| SOL | 65 | 64 | 63 | 62 | 60 | 58 | 55 | 51 | 44 | 35 | 22 | 7 |
| DOGE | 65 | 64 | 63 | 62 | 60 | 58 | 55 | 51 | 44 | 35 | 22 | 7 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-16 | 60g | 2026-09-14 | domani |
| SOL | 2026-07-16 | 60g | 2026-09-14 | domani |
| DOGE | 2026-07-16 | 60g | 2026-09-14 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 61 | 50,82% | +0,35% | +0,33% | UTILE |
| BTC | 2g | 60 | 50,00% | +0,60% | +0,52% | UTILE |
| BTC | 3g | 59 | 44,07% | +0,75% | +0,63% | PRIMA CALIBRAZIONE |
| BTC | 5g | 57 | 43,86% | +1,59% | +1,37% | PRIMA CALIBRAZIONE |
| BTC | 7g | 55 | 52,73% | +2,28% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 10g | 52 | 59,62% | +3,36% | +3,18% | PRIMA CALIBRAZIONE |
| BTC | 14g | 48 | 58,33% | +5,14% | +5,07% | PRIMA CALIBRAZIONE |
| BTC | 21g | 41 | 65,85% | +9,94% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 30g | 33 | 90,91% | +14,43% | +13,13% | PRIMA CALIBRAZIONE |
| BTC | 45g | 20 | 85,00% | +22,20% | +15,59% | FEEDBACK RAPIDO |
| BTC | 60g | 7 | 100,00% | +23,11% | +23,11% | FEEDBACK RAPIDO |
| SOL | 1g | 57 | 54,39% | +0,57% | +0,46% | PRIMA CALIBRAZIONE |
| SOL | 2g | 56 | 50,00% | +1,13% | +1,01% | PRIMA CALIBRAZIONE |
| SOL | 3g | 55 | 54,55% | +1,76% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 5g | 53 | 58,49% | +3,05% | +2,95% | PRIMA CALIBRAZIONE |
| SOL | 7g | 51 | 62,75% | +4,36% | +4,46% | PRIMA CALIBRAZIONE |
| SOL | 10g | 48 | 66,67% | +6,24% | +6,40% | PRIMA CALIBRAZIONE |
| SOL | 14g | 44 | 75,00% | +9,34% | +10,17% | PRIMA CALIBRAZIONE |
| SOL | 21g | 37 | 78,38% | +16,80% | +15,84% | PRIMA CALIBRAZIONE |
| SOL | 30g | 28 | 64,29% | +20,87% | +13,81% | FEEDBACK RAPIDO |
| SOL | 45g | 16 | 37,50% | +33,69% | -9,86% | FEEDBACK RAPIDO |
| SOL | 60g | 6 | 50,00% | +33,33% | +0,21% | FEEDBACK RAPIDO |
| DOGE | 1g | 60 | 43,33% | +0,37% | +0,06% | UTILE |
| DOGE | 2g | 59 | 44,07% | +0,74% | +0,17% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 58 | 39,66% | +1,07% | +0,39% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 56 | 46,43% | +1,90% | +1,30% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 54 | 59,26% | +2,54% | +2,88% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 51 | 54,90% | +2,92% | +3,67% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 48 | 66,67% | +4,76% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 42 | 76,19% | +9,09% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 33 | 75,76% | +13,03% | +6,27% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 21 | 19,05% | +20,47% | -12,47% | FEEDBACK RAPIDO |
| DOGE | 60g | 7 | 0,00% | +19,08% | -19,08% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 61 | 50,82% | +0,35% | +0,33% | -0,09% | +0,87% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 64 | 53,12% | +0,33% | +0,33% | -0,10% | +0,84% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 64 | 53,12% | +0,33% | +0,33% | -0,10% | +0,84% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 59 | 40,68% | +0,44% | +0,09% | -0,01% | +0,95% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,81% | +0,37% | +0,13% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 60 | 50,00% | +0,60% | +0,52% | +0,03% | +1,26% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 63 | 52,38% | +0,69% | +0,69% | +0,13% | +1,35% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 63 | 52,38% | +0,69% | +0,69% | +0,13% | +1,35% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 58 | 43,10% | +0,84% | +0,13% | +0,28% | +1,49% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,18% | +0,55% | +0,59% | +1,89% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 59 | 44,07% | +0,75% | +0,63% | -1,10% | +2,48% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 62 | 51,61% | +1,03% | +1,03% | -1,07% | +2,69% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 62 | 51,61% | +1,03% | +1,03% | -1,07% | +2,69% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 57 | 35,09% | +1,29% | -0,19% | -0,92% | +2,93% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,81% | +0,20% | -0,58% | +3,31% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 57 | 43,86% | +1,59% | +1,37% | -1,66% | +3,91% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 60 | 50,00% | +1,83% | +1,83% | -1,63% | +4,20% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 60 | 50,00% | +1,83% | +1,83% | -1,63% | +4,20% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 55 | 41,82% | +2,10% | -0,98% | -1,46% | +4,51% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 24 | 50,00% | +3,70% | -1,14% | -1,03% | +5,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 55 | 52,73% | +2,28% | +2,08% | -1,90% | +5,11% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 58 | 58,62% | +2,59% | +2,59% | -1,87% | +5,39% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 58 | 58,62% | +2,59% | +2,59% | -1,87% | +5,39% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 53 | 41,51% | +3,04% | -1,77% | -1,69% | +5,80% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 24 | 45,83% | +4,87% | -2,81% | -1,33% | +8,02% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 52 | 59,62% | +3,36% | +3,18% | -2,01% | +6,40% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 55 | 63,64% | +3,53% | +3,53% | -2,01% | +6,63% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 55 | 63,64% | +3,53% | +3,53% | -2,01% | +6,63% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 50 | 46,00% | +4,00% | -1,32% | -1,79% | +7,18% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 23 | 52,17% | +5,61% | -3,56% | -1,40% | +9,17% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 48 | 58,33% | +5,14% | +5,07% | -2,16% | +8,71% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 51 | 58,82% | +5,24% | +5,24% | -2,16% | +8,83% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 51 | 58,82% | +5,24% | +5,24% | -2,16% | +8,83% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 46 | 54,35% | +5,94% | +0,68% | -1,91% | +9,61% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 19 | 36,84% | +6,37% | -3,97% | -1,30% | +10,56% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 41 | 65,85% | +9,94% | +9,78% | -2,06% | +13,84% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 44 | 72,73% | +9,73% | +9,73% | -2,08% | +13,66% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 44 | 72,73% | +9,73% | +9,73% | -2,08% | +13,66% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 39 | 41,03% | +10,77% | -0,91% | -1,78% | +14,79% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 12 | 33,33% | +14,30% | -11,49% | -0,25% | +18,32% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | -1,61% | +6,04% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 33 | 90,91% | +14,43% | +13,13% | -2,87% | +18,56% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 35 | 85,71% | +14,07% | +14,07% | -2,92% | +18,26% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 35 | 85,71% | +14,07% | +14,07% | -2,92% | +18,26% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 31 | 87,10% | +15,28% | +15,28% | -2,71% | +19,70% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 30 | 43,33% | +14,30% | -2,29% | -2,66% | +18,83% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 5 | 0,00% | +23,88% | -23,88% | -1,27% | +29,00% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 20 | 85,00% | +22,20% | +15,59% | -3,17% | +26,88% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 22 | 100,00% | +22,27% | +22,27% | -3,21% | +26,86% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 22 | 100,00% | +22,27% | +22,27% | -3,21% | +26,86% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 18 | 100,00% | +22,54% | +22,54% | -2,93% | +27,22% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 18 | 27,78% | +22,53% | -10,08% | -2,87% | +27,34% | FEEDBACK RAPIDO |
| BTC | 45g | Classic technical | CALIBRABILE | 2 | 0,00% | +21,18% | -21,18% | -2,23% | +29,25% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 7 | 100,00% | +23,11% | +23,11% | -2,47% | +29,48% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 7 | 100,00% | +23,11% | +23,11% | -2,47% | +29,48% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 7 | 100,00% | +23,11% | +23,11% | -2,47% | +29,48% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 7 | 100,00% | +23,11% | +23,11% | -2,47% | +29,48% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 6 | 50,00% | +23,08% | -1,25% | -2,34% | +29,59% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 60 | 43,33% | +0,37% | +0,06% | -0,28% | +1,33% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 63 | 57,14% | +0,27% | +0,50% | -0,40% | +1,17% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 63 | 57,14% | +0,27% | +0,50% | -0,40% | +1,17% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 57 | 50,88% | +0,18% | +0,38% | -0,51% | +1,07% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 36 | 38,89% | +0,24% | -0,49% | -0,39% | +0,95% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 59 | 44,07% | +0,74% | +0,17% | -0,05% | +1,97% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 62 | 56,45% | +0,55% | +0,84% | -0,22% | +1,70% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 62 | 56,45% | +0,55% | +0,84% | -0,22% | +1,70% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 56 | 53,57% | +0,17% | +0,53% | -0,59% | +1,30% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 35 | 40,00% | +0,47% | -1,26% | -0,28% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,90% | +2,61% | +2,02% | +4,90% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 58 | 39,66% | +1,07% | +0,39% | -1,85% | +4,08% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 61 | 55,74% | +0,88% | +1,25% | -1,98% | +3,73% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 61 | 55,74% | +0,88% | +1,25% | -1,98% | +3,73% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 55 | 45,45% | +0,07% | +0,42% | -2,26% | +2,83% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 34 | 29,41% | +0,82% | -2,31% | -2,19% | +3,95% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,49% | +2,26% | -0,95% | +6,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 56 | 46,43% | +1,90% | +1,30% | -2,73% | +6,43% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 59 | 50,85% | +1,76% | +2,02% | -2,80% | +6,16% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 59 | 50,85% | +1,76% | +2,02% | -2,80% | +6,16% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 53 | 56,60% | +0,72% | +0,48% | -3,25% | +5,15% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,67% | -4,23% | -3,21% | +6,23% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | +0,52% | +0,34% | -2,37% | +7,26% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 54 | 59,26% | +2,54% | +2,88% | -3,06% | +8,38% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 57 | 56,14% | +2,57% | +2,55% | -3,13% | +8,16% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 57 | 56,14% | +2,57% | +2,55% | -3,13% | +8,16% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 51 | 56,86% | +1,26% | +1,28% | -3,66% | +6,80% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 32 | 37,50% | +2,47% | -4,86% | -3,47% | +7,93% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,37% | -0,49% | -2,97% | +7,69% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 51 | 54,90% | +2,92% | +3,67% | -3,49% | +9,93% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 54 | 50,00% | +2,84% | +2,88% | -3,54% | +9,74% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 54 | 50,00% | +2,84% | +2,88% | -3,54% | +9,74% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 48 | 66,67% | +1,00% | +1,79% | -4,15% | +7,58% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +0,72% | +0,35% | -3,12% | +9,19% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 48 | 66,67% | +4,76% | +6,71% | -4,04% | +13,21% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 50 | 74,00% | +4,32% | +6,43% | -4,08% | +12,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 50 | 74,00% | +4,32% | +6,43% | -4,08% | +12,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 44 | 59,09% | +1,29% | +0,89% | -4,83% | +8,72% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 31 | 48,39% | +3,26% | -3,87% | -4,53% | +11,11% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +6,58% | +1,67% | -3,33% | +14,96% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 42 | 76,19% | +9,09% | +8,15% | -3,59% | +19,67% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 44 | 84,09% | +9,14% | +11,83% | -3,63% | +19,75% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 44 | 84,09% | +9,14% | +11,83% | -3,63% | +19,75% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 37 | 62,16% | +6,37% | -3,31% | -4,34% | +15,31% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 29 | 51,72% | +6,17% | -7,05% | -4,21% | +14,94% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +9,78% | +0,82% | -1,43% | +23,27% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 33 | 75,76% | +13,03% | +6,27% | -4,23% | +25,66% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 35 | 88,57% | +13,53% | +12,22% | -4,24% | +26,48% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 35 | 88,57% | +13,53% | +12,22% | -4,24% | +26,48% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 33 | 93,94% | +12,65% | +14,66% | -4,27% | +25,83% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 30 | 40,00% | +11,60% | -11,60% | -4,76% | +23,68% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 23 | 47,83% | +9,94% | -9,94% | -4,66% | +20,37% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +30,85% | +15,03% | -1,31% | +42,05% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 21 | 19,05% | +20,47% | -12,47% | -5,68% | +38,36% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 22 | 27,27% | +20,35% | -8,41% | -5,72% | +38,31% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 22 | 27,27% | +20,35% | -8,41% | -5,72% | +38,31% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 20 | 30,00% | +19,57% | -6,42% | -5,92% | +37,98% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 22 | 0,00% | +20,35% | -20,35% | -5,72% | +38,31% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 18 | 0,00% | +20,70% | -20,70% | -5,55% | +38,48% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 7 | 0,00% | +19,08% | -19,08% | -7,01% | +36,77% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 7 | 0,00% | +19,08% | -19,08% | -7,01% | +36,77% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 7 | 0,00% | +19,08% | -19,08% | -7,01% | +36,77% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 7 | 0,00% | +19,08% | -19,08% | -7,01% | +36,77% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 7 | 0,00% | +19,08% | -19,08% | -7,01% | +36,77% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 6 | 0,00% | +19,80% | -19,80% | -6,84% | +37,03% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 57 | 54,39% | +0,57% | +0,46% | -0,14% | +1,44% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 59 | 55,93% | +0,30% | +0,29% | -0,34% | +1,15% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 62 | 54,84% | +0,34% | +0,22% | -0,31% | +1,18% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 59 | 49,15% | +0,27% | +0,25% | -0,43% | +1,09% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,49% | +0,45% | -0,33% | +1,40% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 56 | 50,00% | +1,13% | +1,01% | +0,21% | +2,18% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 58 | 46,55% | +0,79% | +0,38% | -0,14% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 61 | 45,90% | +0,77% | +0,34% | -0,14% | +1,66% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 59 | 42,37% | +0,68% | +0,16% | -0,20% | +1,73% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,75% | +0,73% | -0,18% | +1,69% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 55 | 54,55% | +1,76% | +1,60% | -1,52% | +4,08% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 57 | 47,37% | +1,31% | +0,80% | -1,80% | +3,62% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 60 | 46,67% | +1,26% | +0,74% | -1,77% | +3,61% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 59 | 47,46% | +1,12% | +0,01% | -1,84% | +3,37% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 42 | 52,38% | +1,01% | +0,88% | -1,83% | +3,26% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 53 | 58,49% | +3,05% | +2,95% | -2,17% | +6,47% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 55 | 52,73% | +2,43% | +1,44% | -2,45% | +5,84% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 58 | 51,72% | +2,34% | +1,33% | -2,43% | +5,74% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 57 | 47,37% | +2,34% | -0,46% | -2,57% | +5,64% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 41 | 56,10% | +1,58% | +1,44% | -2,57% | +4,83% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 51 | 62,75% | +4,36% | +4,46% | -2,50% | +8,37% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 53 | 58,49% | +3,64% | +2,45% | -2,79% | +7,70% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 56 | 58,93% | +3,44% | +2,32% | -2,79% | +7,49% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 55 | 41,82% | +3,40% | -1,16% | -2,94% | +7,43% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 39 | 51,28% | +1,81% | +1,86% | -3,01% | +5,86% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 48 | 66,67% | +6,24% | +6,40% | -2,66% | +10,69% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 50 | 62,00% | +5,45% | +4,54% | -3,03% | +9,70% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 53 | 60,38% | +5,13% | +4,29% | -3,06% | +9,37% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 52 | 48,08% | +4,57% | -1,90% | -3,24% | +8,97% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 36 | 58,33% | +1,94% | +2,04% | -3,32% | +6,67% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 44 | 75,00% | +9,34% | +10,17% | -2,90% | +15,08% | PRIMA CALIBRAZIONE |

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
