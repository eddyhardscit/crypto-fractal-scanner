# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-14 05:33 UTC

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

Segnali totali salvati: **198**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-14 | BTC | 77.497,87 | +3 | +3 | +3 | 0 | +1 | -1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-14 | DOGE | 0.08404 | -4 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-14 | SOL | 101,01 | +3 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-13 | BTC | 77.274,99 | +6 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-13 | DOGE | 0.08485 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-13 | SOL | 101,86 | +4 | +3 | +3 | 0 | +1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-12 | BTC | 77.204,26 | +3 | +3 | +3 | 0 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-12 | DOGE | 0.08434 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-12 | SOL | 101,54 | +4 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-11 | BTC | 77.053,66 | +5 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-11 | DOGE | 0.08388 | -6 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-11 | SOL | 99,59 | +2 | +2 | +2 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 66 | 65 | 64 | 63 | 61 | 59 | 56 | 52 | 45 | 36 | 23 | 8 |
| SOL | 66 | 65 | 64 | 63 | 61 | 59 | 56 | 52 | 45 | 36 | 23 | 8 |
| DOGE | 66 | 65 | 64 | 63 | 61 | 59 | 56 | 52 | 45 | 36 | 23 | 8 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-17 | 60g | 2026-09-15 | domani |
| SOL | 2026-07-17 | 60g | 2026-09-15 | domani |
| DOGE | 2026-07-17 | 60g | 2026-09-15 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 62 | 51,61% | +0,35% | +0,33% | UTILE |
| BTC | 2g | 61 | 50,82% | +0,60% | +0,52% | UTILE |
| BTC | 3g | 60 | 45,00% | +0,74% | +0,63% | UTILE |
| BTC | 5g | 58 | 43,10% | +1,53% | +1,32% | PRIMA CALIBRAZIONE |
| BTC | 7g | 56 | 51,79% | +2,18% | +1,99% | PRIMA CALIBRAZIONE |
| BTC | 10g | 53 | 58,49% | +3,21% | +3,04% | PRIMA CALIBRAZIONE |
| BTC | 14g | 49 | 57,14% | +5,03% | +4,96% | PRIMA CALIBRAZIONE |
| BTC | 21g | 42 | 66,67% | +9,72% | +9,56% | PRIMA CALIBRAZIONE |
| BTC | 30g | 34 | 91,18% | +14,68% | +13,42% | PRIMA CALIBRAZIONE |
| BTC | 45g | 21 | 85,71% | +22,12% | +15,82% | FEEDBACK RAPIDO |
| BTC | 60g | 8 | 87,50% | +22,85% | +17,59% | FEEDBACK RAPIDO |
| SOL | 1g | 58 | 53,45% | +0,54% | +0,43% | PRIMA CALIBRAZIONE |
| SOL | 2g | 57 | 49,12% | +1,11% | +0,98% | PRIMA CALIBRAZIONE |
| SOL | 3g | 56 | 55,36% | +1,75% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 5g | 54 | 57,41% | +2,94% | +2,84% | PRIMA CALIBRAZIONE |
| SOL | 7g | 52 | 61,54% | +4,20% | +4,30% | PRIMA CALIBRAZIONE |
| SOL | 10g | 49 | 65,31% | +6,06% | +6,22% | PRIMA CALIBRAZIONE |
| SOL | 14g | 45 | 73,33% | +9,10% | +9,91% | PRIMA CALIBRAZIONE |
| SOL | 21g | 38 | 78,95% | +16,56% | +15,63% | PRIMA CALIBRAZIONE |
| SOL | 30g | 29 | 65,52% | +21,32% | +14,50% | FEEDBACK RAPIDO |
| SOL | 45g | 17 | 35,29% | +33,86% | -11,42% | FEEDBACK RAPIDO |
| SOL | 60g | 7 | 42,86% | +33,27% | -4,52% | FEEDBACK RAPIDO |
| DOGE | 1g | 61 | 44,26% | +0,35% | +0,07% | UTILE |
| DOGE | 2g | 60 | 45,00% | +0,72% | +0,17% | UTILE |
| DOGE | 3g | 59 | 38,98% | +1,05% | +0,38% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 57 | 45,61% | +1,75% | +1,16% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 55 | 58,18% | +2,36% | +2,71% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 52 | 55,77% | +2,80% | +3,67% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 48 | 66,67% | +4,76% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 43 | 74,42% | +8,68% | +7,76% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 34 | 76,47% | +13,23% | +6,67% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 22 | 18,18% | +20,45% | -12,81% | FEEDBACK RAPIDO |
| DOGE | 60g | 8 | 0,00% | +18,58% | -18,58% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 62 | 51,61% | +0,35% | +0,33% | -0,11% | +0,87% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 65 | 53,85% | +0,33% | +0,33% | -0,12% | +0,84% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 65 | 53,85% | +0,33% | +0,33% | -0,12% | +0,84% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 60 | 41,67% | +0,44% | +0,09% | -0,03% | +0,94% | UTILE |
| BTC | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,81% | +0,37% | +0,13% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 61 | 50,82% | +0,60% | +0,52% | +0,02% | +1,25% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 64 | 53,12% | +0,69% | +0,69% | +0,12% | +1,34% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 64 | 53,12% | +0,69% | +0,69% | +0,12% | +1,34% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 59 | 44,07% | +0,84% | +0,14% | +0,26% | +1,48% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,18% | +0,55% | +0,59% | +1,89% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 60 | 45,00% | +0,74% | +0,63% | -1,09% | +2,45% | UTILE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 63 | 52,38% | +1,02% | +1,02% | -1,07% | +2,66% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 63 | 52,38% | +1,02% | +1,02% | -1,07% | +2,66% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 58 | 36,21% | +1,28% | -0,17% | -0,92% | +2,89% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,81% | +0,20% | -0,58% | +3,31% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 58 | 43,10% | +1,53% | +1,32% | -1,69% | +3,86% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 61 | 49,18% | +1,77% | +1,77% | -1,66% | +4,15% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 61 | 49,18% | +1,77% | +1,77% | -1,66% | +4,15% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 56 | 41,07% | +2,03% | -0,99% | -1,50% | +4,45% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 24 | 50,00% | +3,70% | -1,14% | -1,03% | +5,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 56 | 51,79% | +2,18% | +1,99% | -1,94% | +5,02% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 59 | 57,63% | +2,49% | +2,49% | -1,92% | +5,30% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 59 | 57,63% | +2,49% | +2,49% | -1,92% | +5,30% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 54 | 40,74% | +2,93% | -1,79% | -1,74% | +5,69% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 24 | 45,83% | +4,87% | -2,81% | -1,33% | +8,02% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 53 | 58,49% | +3,21% | +3,04% | -2,08% | +6,27% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 56 | 62,50% | +3,39% | +3,39% | -2,08% | +6,51% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 56 | 62,50% | +3,39% | +3,39% | -2,08% | +6,51% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 51 | 45,10% | +3,84% | -1,38% | -1,88% | +7,03% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 24 | 50,00% | +5,20% | -3,59% | -1,59% | +8,77% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | -0,67% | -0,67% | -3,33% | +2,78% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 49 | 57,14% | +5,03% | +4,96% | -2,17% | +8,65% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 52 | 57,69% | +5,12% | +5,12% | -2,17% | +8,76% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 52 | 57,69% | +5,12% | +5,12% | -2,17% | +8,76% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 47 | 53,19% | +5,80% | +0,65% | -1,92% | +9,52% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 20 | 35,00% | +6,02% | -3,81% | -1,36% | +10,30% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 42 | 66,67% | +9,72% | +9,56% | -2,03% | +13,67% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 45 | 73,33% | +9,53% | +9,53% | -2,06% | +13,51% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 45 | 73,33% | +9,53% | +9,53% | -2,06% | +13,51% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 40 | 42,50% | +10,52% | -0,87% | -1,76% | +14,59% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 13 | 38,46% | +13,25% | -10,55% | -0,31% | +17,44% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | -1,61% | +6,04% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 34 | 91,18% | +14,68% | +13,42% | -2,81% | +18,91% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 36 | 86,11% | +14,32% | +14,32% | -2,85% | +18,60% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 36 | 86,11% | +14,32% | +14,32% | -2,85% | +18,60% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 32 | 87,50% | +15,52% | +15,52% | -2,65% | +20,04% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 31 | 41,94% | +14,58% | -2,96% | -2,59% | +19,21% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 6 | 0,00% | +23,72% | -23,72% | -1,17% | +29,25% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 21 | 85,71% | +22,12% | +15,82% | -3,18% | +26,92% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 23 | 100,00% | +22,19% | +22,19% | -3,22% | +26,90% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 23 | 100,00% | +22,19% | +22,19% | -3,22% | +26,90% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 19 | 100,00% | +22,43% | +22,43% | -2,95% | +27,26% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 18 | 27,78% | +22,53% | -10,08% | -2,87% | +27,34% | FEEDBACK RAPIDO |
| BTC | 45g | Classic technical | CALIBRABILE | 2 | 0,00% | +21,18% | -21,18% | -2,23% | +29,25% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 8 | 87,50% | +22,85% | +17,59% | -2,52% | +29,35% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 8 | 100,00% | +22,85% | +22,85% | -2,52% | +29,35% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 8 | 100,00% | +22,85% | +22,85% | -2,52% | +29,35% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 8 | 100,00% | +22,85% | +22,85% | -2,52% | +29,35% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 7 | 42,86% | +22,79% | -4,08% | -2,41% | +29,43% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 61 | 44,26% | +0,35% | +0,07% | -0,33% | +1,30% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 64 | 57,81% | +0,25% | +0,50% | -0,44% | +1,14% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 64 | 57,81% | +0,25% | +0,50% | -0,44% | +1,14% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 58 | 51,72% | +0,16% | +0,39% | -0,55% | +1,03% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 37 | 40,54% | +0,21% | -0,45% | -0,47% | +0,90% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 60 | 45,00% | +0,72% | +0,17% | -0,09% | +1,94% | UTILE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 63 | 57,14% | +0,54% | +0,84% | -0,26% | +1,67% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 63 | 57,14% | +0,54% | +0,84% | -0,26% | +1,67% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 57 | 54,39% | +0,16% | +0,52% | -0,62% | +1,27% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 36 | 41,67% | +0,44% | -1,21% | -0,34% | +1,37% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,90% | +2,61% | +2,02% | +4,90% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 59 | 38,98% | +1,05% | +0,38% | -1,85% | +4,04% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 62 | 54,84% | +0,87% | +1,23% | -1,98% | +3,70% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 62 | 54,84% | +0,87% | +1,23% | -1,98% | +3,70% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 56 | 44,64% | +0,07% | +0,41% | -2,26% | +2,81% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 35 | 28,57% | +0,80% | -2,25% | -2,18% | +3,88% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,49% | +2,26% | -0,95% | +6,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 57 | 45,61% | +1,75% | +1,16% | -2,83% | +6,27% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 60 | 51,67% | +1,62% | +2,10% | -2,90% | +6,01% | UTILE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 60 | 51,67% | +1,62% | +2,10% | -2,90% | +6,01% | UTILE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 54 | 55,56% | +0,58% | +0,34% | -3,36% | +5,01% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,67% | -4,23% | -3,21% | +6,23% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | +0,52% | +0,34% | -2,37% | +7,26% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 55 | 58,18% | +2,36% | +2,71% | -3,16% | +8,25% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 58 | 56,90% | +2,40% | +2,62% | -3,23% | +8,04% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 58 | 56,90% | +2,40% | +2,62% | -3,23% | +8,04% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 52 | 55,77% | +1,10% | +1,13% | -3,76% | +6,70% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 33 | 36,36% | +2,18% | -4,92% | -3,64% | +7,73% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,37% | -0,49% | -2,97% | +7,69% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 52 | 55,77% | +2,80% | +3,67% | -3,53% | +9,90% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 55 | 50,91% | +2,73% | +2,89% | -3,57% | +9,72% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 55 | 50,91% | +2,73% | +2,89% | -3,57% | +9,72% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 49 | 65,31% | +0,91% | +1,69% | -4,18% | +7,60% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +0,72% | +0,35% | -3,12% | +9,19% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 48 | 66,67% | +4,76% | +6,71% | -4,04% | +13,21% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 51 | 72,55% | +4,27% | +6,27% | -4,06% | +12,72% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 51 | 72,55% | +4,27% | +6,27% | -4,06% | +12,72% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 45 | 60,00% | +1,29% | +0,90% | -4,79% | +8,83% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 31 | 48,39% | +3,26% | -3,87% | -4,53% | +11,11% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +6,58% | +1,67% | -3,33% | +14,96% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 43 | 74,42% | +8,68% | +7,76% | -3,79% | +19,28% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 45 | 82,22% | +8,75% | +11,38% | -3,82% | +19,37% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 45 | 82,22% | +8,75% | +11,38% | -3,82% | +19,37% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 38 | 60,53% | +5,98% | -3,45% | -4,56% | +14,98% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 30 | 50,00% | +5,68% | -7,09% | -4,48% | +14,53% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +7,18% | -0,50% | -3,01% | +20,33% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 34 | 76,47% | +13,23% | +6,67% | -4,14% | +26,15% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 36 | 88,89% | +13,70% | +12,43% | -4,16% | +26,93% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 36 | 88,89% | +13,70% | +12,43% | -4,16% | +26,93% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 34 | 94,12% | +12,86% | +14,81% | -4,18% | +26,32% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 31 | 41,94% | +11,86% | -10,58% | -4,65% | +24,29% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 23 | 47,83% | +9,94% | -9,94% | -4,66% | +20,37% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +30,85% | +15,03% | -1,31% | +42,05% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 22 | 18,18% | +20,45% | -12,81% | -5,55% | +38,56% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 23 | 30,43% | +20,34% | -7,17% | -5,61% | +38,50% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 23 | 30,43% | +20,34% | -7,17% | -5,61% | +38,50% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 21 | 33,33% | +19,58% | -5,17% | -5,78% | +38,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 23 | 0,00% | +20,34% | -20,34% | -5,61% | +38,50% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 19 | 0,00% | +20,66% | -20,66% | -5,42% | +38,70% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 8 | 0,00% | +18,58% | -18,58% | -7,00% | +36,78% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 8 | 0,00% | +18,58% | -18,58% | -7,00% | +36,78% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 8 | 0,00% | +18,58% | -18,58% | -7,00% | +36,78% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 8 | 0,00% | +18,58% | -18,58% | -7,00% | +36,78% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 8 | 0,00% | +18,58% | -18,58% | -7,00% | +36,78% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 7 | 0,00% | +19,13% | -19,13% | -6,85% | +37,01% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 58 | 53,45% | +0,54% | +0,43% | -0,18% | +1,40% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 60 | 55,00% | +0,28% | +0,27% | -0,38% | +1,12% | UTILE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 63 | 53,97% | +0,32% | +0,20% | -0,35% | +1,15% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 60 | 48,33% | +0,26% | +0,23% | -0,46% | +1,06% | UTILE |
| SOL | 1g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,49% | +0,45% | -0,33% | +1,40% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 57 | 49,12% | +1,11% | +0,98% | +0,16% | +2,13% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 59 | 45,76% | +0,77% | +0,36% | -0,18% | +1,57% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 62 | 45,16% | +0,75% | +0,33% | -0,17% | +1,62% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 59 | 42,37% | +0,68% | +0,16% | -0,20% | +1,73% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,75% | +0,73% | -0,18% | +1,69% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 56 | 55,36% | +1,75% | +1,60% | -1,51% | +4,05% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 58 | 48,28% | +1,32% | +0,81% | -1,77% | +3,61% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 61 | 47,54% | +1,27% | +0,75% | -1,75% | +3,60% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 59 | 47,46% | +1,12% | +0,01% | -1,84% | +3,37% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 42 | 52,38% | +1,01% | +0,88% | -1,83% | +3,26% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 54 | 57,41% | +2,94% | +2,84% | -2,23% | +6,37% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 56 | 51,79% | +2,33% | +1,36% | -2,50% | +5,76% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 59 | 50,85% | +2,25% | +1,26% | -2,48% | +5,67% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 58 | 46,55% | +2,24% | -0,50% | -2,62% | +5,57% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 42 | 54,76% | +1,47% | +1,33% | -2,64% | +4,74% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 52 | 61,54% | +4,20% | +4,30% | -2,58% | +8,21% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 54 | 57,41% | +3,50% | +2,32% | -2,86% | +7,55% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 57 | 57,89% | +3,31% | +2,21% | -2,85% | +7,36% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 56 | 41,07% | +3,26% | -1,22% | -3,01% | +7,29% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 40 | 50,00% | +1,66% | +1,71% | -3,10% | +5,71% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 49 | 65,31% | +6,06% | +6,22% | -2,71% | +10,54% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 51 | 60,78% | +5,29% | +4,40% | -3,07% | +9,57% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 54 | 59,26% | +4,99% | +4,16% | -3,09% | +9,26% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 53 | 47,17% | +4,43% | -1,91% | -3,27% | +8,86% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 37 | 56,76% | +1,82% | +1,92% | -3,36% | +6,58% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 45 | 73,33% | +9,10% | +9,91% | -2,94% | +14,84% | PRIMA CALIBRAZIONE |

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
