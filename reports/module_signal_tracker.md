# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-09 05:33 UTC

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

Segnali totali salvati: **183**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-09 | BTC | 78.978,35 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-09 | DOGE | 0.09017 | +3 | -1 | -1 | 0 | +3 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-09 | SOL | 104,26 | +5 | +2 | +2 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-08 | BTC | 78.724,26 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-08 | DOGE | 0.09002 | +3 | -2 | -2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-08 | SOL | 103,26 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-07 | BTC | 79.828,11 | +7 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-07 | DOGE | 0.09027 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | STAI ALLA FINESTRA |
| 2026-09-07 | SOL | 105,55 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-06 | BTC | 79.879,48 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-06 | DOGE | 0.09088 | +3 | -2 | -2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-06 | SOL | 105,95 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 61 | 60 | 59 | 58 | 56 | 54 | 51 | 47 | 40 | 33 | 18 | 3 |
| SOL | 61 | 60 | 59 | 58 | 56 | 54 | 51 | 47 | 40 | 33 | 18 | 3 |
| DOGE | 61 | 60 | 59 | 58 | 56 | 54 | 51 | 47 | 40 | 33 | 18 | 3 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-12 | 60g | 2026-09-10 | domani |
| SOL | 2026-07-12 | 60g | 2026-09-10 | domani |
| DOGE | 2026-07-12 | 60g | 2026-09-10 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 57 | 50,88% | +0,41% | +0,39% | PRIMA CALIBRAZIONE |
| BTC | 2g | 56 | 51,79% | +0,72% | +0,63% | PRIMA CALIBRAZIONE |
| BTC | 3g | 55 | 47,27% | +0,94% | +0,81% | PRIMA CALIBRAZIONE |
| BTC | 5g | 53 | 47,17% | +1,91% | +1,67% | PRIMA CALIBRAZIONE |
| BTC | 7g | 51 | 54,90% | +2,65% | +2,43% | PRIMA CALIBRAZIONE |
| BTC | 10g | 48 | 62,50% | +3,69% | +3,50% | PRIMA CALIBRAZIONE |
| BTC | 14g | 44 | 63,64% | +5,73% | +5,65% | PRIMA CALIBRAZIONE |
| BTC | 21g | 37 | 62,16% | +10,56% | +10,38% | PRIMA CALIBRAZIONE |
| BTC | 30g | 31 | 90,32% | +13,88% | +12,49% | PRIMA CALIBRAZIONE |
| BTC | 45g | 16 | 87,50% | +22,54% | +16,97% | FEEDBACK RAPIDO |
| BTC | 60g | 3 | 100,00% | +24,28% | +24,28% | FEEDBACK RAPIDO |
| SOL | 1g | 53 | 54,72% | +0,65% | +0,53% | PRIMA CALIBRAZIONE |
| SOL | 2g | 52 | 51,92% | +1,30% | +1,16% | PRIMA CALIBRAZIONE |
| SOL | 3g | 51 | 58,82% | +2,09% | +1,91% | PRIMA CALIBRAZIONE |
| SOL | 5g | 49 | 63,27% | +3,53% | +3,42% | PRIMA CALIBRAZIONE |
| SOL | 7g | 47 | 65,96% | +4,87% | +4,99% | PRIMA CALIBRAZIONE |
| SOL | 10g | 44 | 68,18% | +6,85% | +7,02% | PRIMA CALIBRAZIONE |
| SOL | 14g | 40 | 80,00% | +10,54% | +11,45% | PRIMA CALIBRAZIONE |
| SOL | 21g | 33 | 75,76% | +17,34% | +16,26% | PRIMA CALIBRAZIONE |
| SOL | 30g | 26 | 61,54% | +19,79% | +12,19% | FEEDBACK RAPIDO |
| SOL | 45g | 14 | 35,71% | +33,18% | -11,07% | FEEDBACK RAPIDO |
| SOL | 60g | 2 | 100,00% | +34,65% | +34,65% | FEEDBACK RAPIDO |
| DOGE | 1g | 56 | 44,64% | +0,51% | +0,12% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 55 | 45,45% | +1,01% | +0,38% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 54 | 40,74% | +1,50% | +0,73% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 52 | 50,00% | +2,43% | +1,80% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 50 | 60,00% | +2,88% | +3,23% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 48 | 58,33% | +2,96% | +4,04% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 45 | 68,89% | +5,11% | +7,18% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 38 | 78,95% | +9,94% | +8,90% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 31 | 74,19% | +12,41% | +5,21% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 18 | 5,56% | +20,48% | -17,95% | FEEDBACK RAPIDO |
| DOGE | 60g | 3 | 0,00% | +22,53% | -22,53% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 57 | 50,88% | +0,41% | +0,39% | -0,03% | +0,97% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 60 | 53,33% | +0,39% | +0,39% | -0,05% | +0,93% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 60 | 53,33% | +0,39% | +0,39% | -0,05% | +0,93% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 55 | 40,00% | +0,51% | +0,14% | +0,06% | +1,05% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,81% | +0,37% | +0,13% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 56 | 51,79% | +0,72% | +0,63% | +0,14% | +1,41% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 59 | 54,24% | +0,81% | +0,81% | +0,24% | +1,50% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 59 | 54,24% | +0,81% | +0,81% | +0,24% | +1,50% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 54 | 44,44% | +0,98% | +0,22% | +0,41% | +1,67% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,18% | +0,55% | +0,59% | +1,89% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 55 | 47,27% | +0,94% | +0,81% | -0,96% | +2,62% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 58 | 55,17% | +1,23% | +1,23% | -0,95% | +2,84% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 58 | 55,17% | +1,23% | +1,23% | -0,95% | +2,84% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 53 | 37,74% | +1,53% | -0,06% | -0,77% | +3,11% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,81% | +0,20% | -0,58% | +3,31% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 53 | 47,17% | +1,91% | +1,67% | -1,52% | +4,15% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 56 | 53,57% | +2,15% | +2,15% | -1,49% | +4,44% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 56 | 53,57% | +2,15% | +2,15% | -1,49% | +4,44% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 51 | 45,10% | +2,46% | -0,86% | -1,30% | +4,81% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 24 | 50,00% | +3,70% | -1,14% | -1,03% | +5,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 25,00% | -0,34% | -0,34% | -1,71% | +2,56% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 51 | 54,90% | +2,65% | +2,43% | -1,78% | +5,39% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 54 | 61,11% | +2,96% | +2,96% | -1,76% | +5,67% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 54 | 61,11% | +2,96% | +2,96% | -1,76% | +5,67% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 49 | 42,86% | +3,49% | -1,72% | -1,55% | +6,14% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 22 | 45,45% | +5,46% | -2,91% | -1,23% | +8,53% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 48 | 62,50% | +3,69% | +3,50% | -2,00% | +6,50% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 51 | 66,67% | +3,86% | +3,86% | -2,00% | +6,75% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 51 | 66,67% | +3,86% | +3,86% | -2,00% | +6,75% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 46 | 47,83% | +4,40% | -1,38% | -1,76% | +7,35% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 19 | 57,89% | +6,93% | -4,18% | -1,23% | +10,01% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 44 | 63,64% | +5,73% | +5,65% | -2,09% | +9,07% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 47 | 63,83% | +5,79% | +5,79% | -2,10% | +9,18% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 47 | 63,83% | +5,79% | +5,79% | -2,10% | +9,18% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 42 | 59,52% | +6,63% | +0,86% | -1,82% | +10,07% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 15 | 46,67% | +8,42% | -4,69% | -0,87% | +12,10% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 37 | 62,16% | +10,56% | +10,38% | -2,38% | +14,19% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 40 | 70,00% | +10,28% | +10,28% | -2,38% | +13,97% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 40 | 70,00% | +10,28% | +10,28% | -2,38% | +13,97% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 35 | 34,29% | +11,52% | -1,49% | -2,08% | +15,27% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 8 | 0,00% | +19,34% | -19,34% | -0,83% | +22,19% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 31 | 90,32% | +13,88% | +12,49% | -2,98% | +17,83% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 33 | 84,85% | +13,53% | +13,53% | -3,02% | +17,55% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 33 | 84,85% | +13,53% | +13,53% | -3,02% | +17,55% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 29 | 86,21% | +14,75% | +14,75% | -2,82% | +19,00% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 28 | 42,86% | +13,68% | -2,44% | -2,76% | +18,04% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 16 | 87,50% | +22,54% | +16,97% | -3,22% | +26,53% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 18 | 100,00% | +22,59% | +22,59% | -3,27% | +26,54% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 18 | 100,00% | +22,59% | +22,59% | -3,27% | +26,54% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 14 | 100,00% | +23,03% | +23,03% | -2,92% | +26,92% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 15 | 33,33% | +22,81% | -7,88% | -2,97% | +26,99% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 3 | 100,00% | +24,28% | +24,28% | -3,05% | +29,12% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | +24,28% | +24,28% | -3,05% | +29,12% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | +24,28% | +24,28% | -3,05% | +29,12% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 3 | 100,00% | +24,28% | +24,28% | -3,05% | +29,12% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 2 | 0,00% | +24,78% | -24,78% | -2,93% | +29,27% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 56 | 44,64% | +0,51% | +0,12% | -0,15% | +1,52% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 59 | 57,63% | +0,39% | +0,43% | -0,28% | +1,34% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 59 | 57,63% | +0,39% | +0,43% | -0,28% | +1,34% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 53 | 52,83% | +0,31% | +0,47% | -0,39% | +1,24% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,22% | -0,49% | -0,44% | +0,96% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 55 | 45,45% | +1,01% | +0,38% | +0,21% | +2,32% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 58 | 55,17% | +0,80% | +0,69% | +0,01% | +2,01% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 58 | 55,17% | +0,80% | +0,69% | +0,01% | +2,01% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 52 | 55,77% | +0,42% | +0,78% | -0,35% | +1,62% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 33 | 42,42% | +0,60% | -1,16% | -0,16% | +1,59% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,90% | +2,61% | +2,02% | +4,90% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 54 | 40,74% | +1,50% | +0,73% | -1,52% | +4,37% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 57 | 52,63% | +1,28% | +1,00% | -1,68% | +3,98% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 57 | 52,63% | +1,28% | +1,00% | -1,68% | +3,98% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 51 | 47,06% | +0,46% | +0,78% | -1,95% | +3,04% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 32 | 31,25% | +1,23% | -2,09% | -1,90% | +4,10% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,49% | +2,26% | -0,95% | +6,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 52 | 50,00% | +2,43% | +1,80% | -2,45% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 55 | 49,09% | +2,25% | +1,81% | -2,55% | +6,40% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 55 | 49,09% | +2,25% | +1,81% | -2,55% | +6,40% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 49 | 59,18% | +1,18% | +0,92% | -3,00% | +5,35% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | +1,54% | +1,34% | -1,56% | +8,05% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 50 | 60,00% | +2,88% | +3,23% | -3,01% | +8,43% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 53 | 54,72% | +2,90% | +2,60% | -3,09% | +8,19% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 53 | 54,72% | +2,90% | +2,60% | -3,09% | +8,19% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 47 | 59,57% | +1,52% | +1,55% | -3,65% | +6,72% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +0,41% | +0,28% | -2,23% | +8,54% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 48 | 58,33% | +2,96% | +4,04% | -3,63% | +9,67% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 50 | 54,00% | +2,86% | +3,32% | -3,68% | +9,40% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 50 | 54,00% | +2,86% | +3,32% | -3,68% | +9,40% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 44 | 63,64% | +0,85% | +1,72% | -4,37% | +7,00% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +0,72% | +0,35% | -3,12% | +9,19% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 45 | 68,89% | +5,11% | +7,18% | -3,91% | +13,41% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 46 | 71,74% | +4,82% | +6,86% | -3,86% | +12,97% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 46 | 71,74% | +4,82% | +6,86% | -3,86% | +12,97% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 40 | 65,00% | +1,56% | +1,12% | -4,65% | +8,64% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 31 | 48,39% | +3,26% | -3,87% | -4,53% | +11,11% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +7,65% | +2,04% | -2,99% | +15,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 38 | 78,95% | +9,94% | +8,90% | -3,51% | +20,06% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 40 | 87,50% | +9,95% | +12,91% | -3,56% | +20,13% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 40 | 87,50% | +9,95% | +12,91% | -3,56% | +20,13% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 33 | 63,64% | +7,02% | -3,84% | -4,34% | +15,23% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 27 | 55,56% | +7,10% | -7,10% | -3,69% | +15,72% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,49% | -0,95% | -1,31% | +25,23% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 31 | 74,19% | +12,41% | +5,21% | -4,45% | +24,50% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 33 | 87,88% | +12,97% | +11,59% | -4,45% | +25,44% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 33 | 87,88% | +12,97% | +11,59% | -4,45% | +25,44% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 31 | 93,55% | +12,01% | +14,14% | -4,50% | +24,68% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 30 | 40,00% | +11,60% | -11,60% | -4,76% | +23,68% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 22 | 50,00% | +9,38% | -9,38% | -4,86% | +19,29% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +30,85% | +15,03% | -1,31% | +42,05% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 18 | 5,56% | +20,48% | -17,95% | -6,13% | +37,64% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 18 | 11,11% | +20,48% | -14,67% | -6,13% | +37,64% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 18 | 11,11% | +20,48% | -14,67% | -6,13% | +37,64% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 16 | 12,50% | +19,51% | -12,97% | -6,42% | +37,15% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 18 | 0,00% | +20,48% | -20,48% | -6,13% | +37,64% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 16 | 0,00% | +20,67% | -20,67% | -5,92% | +37,88% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 3 | 0,00% | +22,53% | -22,53% | -7,62% | +35,88% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 3 | 0,00% | +22,53% | -22,53% | -7,62% | +35,88% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 3 | 0,00% | +22,53% | -22,53% | -7,62% | +35,88% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 3 | 0,00% | +22,53% | -22,53% | -7,62% | +35,88% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 3 | 0,00% | +22,53% | -22,53% | -7,62% | +35,88% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 3 | 0,00% | +22,53% | -22,53% | -7,62% | +35,88% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 53 | 54,72% | +0,65% | +0,53% | -0,06% | +1,56% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 55 | 56,36% | +0,36% | +0,35% | -0,28% | +1,24% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 58 | 55,17% | +0,40% | +0,28% | -0,25% | +1,27% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 57 | 50,88% | +0,36% | +0,34% | -0,32% | +1,20% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 41 | 51,22% | +0,55% | +0,51% | -0,25% | +1,48% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 52 | 51,92% | +1,30% | +1,16% | +0,35% | +2,39% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 54 | 48,15% | +0,92% | +0,48% | -0,03% | +1,76% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 57 | 47,37% | +0,89% | +0,43% | -0,03% | +1,81% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 56 | 44,64% | +0,83% | +0,28% | -0,06% | +1,92% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 40 | 52,50% | +0,93% | +0,90% | +0,01% | +1,91% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 51 | 58,82% | +2,09% | +1,91% | -1,30% | +4,35% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 53 | 50,94% | +1,59% | +1,04% | -1,60% | +3,85% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 56 | 50,00% | +1,53% | +0,97% | -1,58% | +3,82% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 55 | 50,91% | +1,38% | +0,19% | -1,65% | +3,57% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 39 | 56,41% | +1,33% | +1,19% | -1,60% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 49 | 63,27% | +3,53% | +3,42% | -1,95% | +6,85% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 51 | 56,86% | +2,85% | +1,78% | -2,26% | +6,16% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 54 | 55,56% | +2,73% | +1,64% | -2,24% | +6,04% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 53 | 50,94% | +2,73% | -0,28% | -2,40% | +5,93% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 37 | 62,16% | +2,06% | +1,90% | -2,33% | +5,15% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 47 | 65,96% | +4,87% | +4,99% | -2,40% | +8,75% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 49 | 61,22% | +4,08% | +2,78% | -2,72% | +8,00% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 52 | 61,54% | +3,84% | +2,63% | -2,72% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 51 | 43,14% | +3,79% | -1,12% | -2,89% | +7,70% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 35 | 54,29% | +2,21% | +2,26% | -2,93% | +6,07% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 44 | 68,18% | +6,85% | +7,02% | -2,57% | +11,18% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 46 | 63,04% | +5,96% | +4,97% | -2,98% | +10,08% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 49 | 61,22% | +5,59% | +4,68% | -3,01% | +9,70% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 48 | 47,92% | +4,98% | -2,02% | -3,21% | +9,28% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 32 | 59,38% | +2,24% | +2,35% | -3,29% | +6,84% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 40 | 80,00% | +10,54% | +11,45% | -2,55% | +16,22% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 42 | 80,95% | +9,94% | +8,98% | -2,92% | +14,91% | PRIMA CALIBRAZIONE |

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
