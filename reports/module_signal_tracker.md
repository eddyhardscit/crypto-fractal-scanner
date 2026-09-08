# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-08 05:33 UTC

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

Segnali totali salvati: **180**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-08 | BTC | 78.724,26 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-08 | DOGE | 0.09002 | +3 | -2 | -2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-08 | SOL | 103,26 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-07 | BTC | 79.828,11 | +7 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-07 | DOGE | 0.09027 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | STAI ALLA FINESTRA |
| 2026-09-07 | SOL | 105,55 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-06 | BTC | 79.879,48 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-06 | DOGE | 0.09088 | +3 | -2 | -2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-06 | SOL | 105,95 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-05 | BTC | 79.660,00 | +5 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-05 | DOGE | 0.08560 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-05 | SOL | 102,27 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60 | 59 | 58 | 57 | 55 | 53 | 50 | 46 | 39 | 32 | 17 | 2 |
| SOL | 60 | 59 | 58 | 57 | 55 | 53 | 50 | 46 | 39 | 32 | 17 | 2 |
| DOGE | 60 | 59 | 58 | 57 | 55 | 53 | 50 | 46 | 39 | 32 | 17 | 2 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-11 | 60g | 2026-09-09 | domani |
| SOL | 2026-07-11 | 60g | 2026-09-09 | domani |
| DOGE | 2026-07-11 | 60g | 2026-09-09 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 56 | 50,00% | +0,41% | +0,39% | PRIMA CALIBRAZIONE |
| BTC | 2g | 55 | 52,73% | +0,75% | +0,66% | PRIMA CALIBRAZIONE |
| BTC | 3g | 54 | 48,15% | +0,98% | +0,85% | PRIMA CALIBRAZIONE |
| BTC | 5g | 52 | 48,08% | +1,99% | +1,75% | PRIMA CALIBRAZIONE |
| BTC | 7g | 50 | 54,00% | +2,66% | +2,45% | PRIMA CALIBRAZIONE |
| BTC | 10g | 47 | 61,70% | +3,75% | +3,55% | PRIMA CALIBRAZIONE |
| BTC | 14g | 43 | 65,12% | +5,87% | +5,79% | PRIMA CALIBRAZIONE |
| BTC | 21g | 36 | 61,11% | +10,21% | +10,03% | PRIMA CALIBRAZIONE |
| BTC | 30g | 30 | 90,00% | +13,63% | +12,19% | PRIMA CALIBRAZIONE |
| BTC | 45g | 15 | 86,67% | +22,54% | +16,60% | FEEDBACK RAPIDO |
| BTC | 60g | 2 | 100,00% | +24,75% | +24,75% | FEEDBACK RAPIDO |
| SOL | 1g | 52 | 53,85% | +0,65% | +0,53% | PRIMA CALIBRAZIONE |
| SOL | 2g | 51 | 52,94% | +1,35% | +1,21% | PRIMA CALIBRAZIONE |
| SOL | 3g | 50 | 60,00% | +2,16% | +1,98% | PRIMA CALIBRAZIONE |
| SOL | 5g | 48 | 62,50% | +3,59% | +3,48% | PRIMA CALIBRAZIONE |
| SOL | 7g | 46 | 65,22% | +4,89% | +5,01% | PRIMA CALIBRAZIONE |
| SOL | 10g | 43 | 69,77% | +7,03% | +7,21% | PRIMA CALIBRAZIONE |
| SOL | 14g | 39 | 79,49% | +10,62% | +11,55% | PRIMA CALIBRAZIONE |
| SOL | 21g | 32 | 75,00% | +16,77% | +15,65% | PRIMA CALIBRAZIONE |
| SOL | 30g | 25 | 60,00% | +19,14% | +11,23% | FEEDBACK RAPIDO |
| SOL | 45g | 14 | 35,71% | +33,18% | -11,07% | FEEDBACK RAPIDO |
| SOL | 60g | 1 | 100,00% | +35,29% | +35,29% | FEEDBACK RAPIDO |
| DOGE | 1g | 55 | 43,64% | +0,51% | +0,12% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 54 | 46,30% | +1,03% | +0,39% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 53 | 41,51% | +1,55% | +0,76% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 51 | 50,98% | +2,40% | +1,90% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 49 | 61,22% | +2,74% | +3,51% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 47 | 57,45% | +2,90% | +3,99% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 44 | 68,18% | +5,14% | +7,25% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 37 | 78,38% | +9,43% | +8,36% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 30 | 73,33% | +11,85% | +4,41% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 17 | 0,00% | +20,35% | -20,35% | FEEDBACK RAPIDO |
| DOGE | 60g | 2 | 0,00% | +22,88% | -22,88% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 56 | 50,00% | +0,41% | +0,39% | -0,03% | +0,97% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 59 | 52,54% | +0,39% | +0,39% | -0,04% | +0,93% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 59 | 52,54% | +0,39% | +0,39% | -0,04% | +0,93% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 54 | 38,89% | +0,51% | +0,13% | +0,06% | +1,06% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,81% | +0,37% | +0,13% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 55 | 52,73% | +0,75% | +0,66% | +0,17% | +1,45% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 58 | 55,17% | +0,84% | +0,84% | +0,27% | +1,54% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 58 | 55,17% | +0,84% | +0,84% | +0,27% | +1,54% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 53 | 45,28% | +1,02% | +0,24% | +0,45% | +1,72% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,18% | +0,55% | +0,59% | +1,89% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 54 | 48,15% | +0,98% | +0,85% | -0,95% | +2,66% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 57 | 56,14% | +1,27% | +1,27% | -0,93% | +2,88% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 57 | 56,14% | +1,27% | +1,27% | -0,93% | +2,88% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 52 | 38,46% | +1,58% | -0,04% | -0,75% | +3,16% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,81% | +0,20% | -0,58% | +3,31% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,72% | +0,72% | -0,94% | +2,21% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 52 | 48,08% | +1,99% | +1,75% | -1,49% | +4,24% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 55 | 54,55% | +2,23% | +2,23% | -1,46% | +4,53% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 55 | 54,55% | +2,23% | +2,23% | -1,46% | +4,53% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 50 | 46,00% | +2,56% | -0,82% | -1,26% | +4,91% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 23 | 52,17% | +3,97% | -1,09% | -0,94% | +6,22% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 50 | 54,00% | +2,66% | +2,45% | -1,79% | +5,37% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 53 | 60,38% | +2,98% | +2,98% | -1,77% | +5,67% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 53 | 60,38% | +2,98% | +2,98% | -1,77% | +5,67% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 48 | 41,67% | +3,53% | -1,79% | -1,56% | +6,14% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | +5,64% | -3,13% | -1,24% | +8,65% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 47 | 61,70% | +3,75% | +3,55% | -1,99% | +6,53% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 50 | 66,00% | +3,91% | +3,91% | -1,99% | +6,78% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 50 | 66,00% | +3,91% | +3,91% | -1,99% | +6,78% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 45 | 46,67% | +4,48% | -1,43% | -1,75% | +7,39% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 18 | 55,56% | +7,25% | -4,47% | -1,17% | +10,27% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 43 | 65,12% | +5,87% | +5,79% | -2,06% | +9,19% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 46 | 65,22% | +5,92% | +5,92% | -2,07% | +9,29% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 46 | 65,22% | +5,92% | +5,92% | -2,07% | +9,29% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 41 | 60,98% | +6,80% | +0,89% | -1,77% | +10,22% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 14 | 50,00% | +9,03% | -5,01% | -0,68% | +12,68% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 36 | 61,11% | +10,21% | +10,03% | -2,64% | +13,81% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 39 | 69,23% | +9,96% | +9,96% | -2,63% | +13,61% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 39 | 69,23% | +9,96% | +9,96% | -2,63% | +13,61% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 34 | 73,53% | +10,91% | +10,91% | -2,48% | +14,50% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 34 | 32,35% | +11,19% | -2,21% | -2,36% | +14,89% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 8 | 0,00% | +19,34% | -19,34% | -0,83% | +22,19% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 30 | 90,00% | +13,63% | +12,19% | -2,95% | +17,54% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 32 | 84,38% | +13,28% | +13,28% | -3,00% | +17,27% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 32 | 84,38% | +13,28% | +13,28% | -3,00% | +17,27% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 28 | 85,71% | +14,50% | +14,50% | -2,78% | +18,72% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 27 | 40,74% | +13,39% | -3,33% | -2,73% | +17,72% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 15 | 86,67% | +22,54% | +16,60% | -3,21% | +26,45% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 17 | 100,00% | +22,59% | +22,59% | -3,26% | +26,48% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 17 | 100,00% | +22,59% | +22,59% | -3,26% | +26,48% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 13 | 100,00% | +23,06% | +23,06% | -2,88% | +26,87% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 14 | 28,57% | +22,83% | -10,05% | -2,94% | +26,94% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 2 | 100,00% | +24,75% | +24,75% | -2,80% | +29,45% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | +24,75% | +24,75% | -2,80% | +29,45% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | +24,75% | +24,75% | -2,80% | +29,45% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 2 | 100,00% | +24,75% | +24,75% | -2,80% | +29,45% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 1 | 0,00% | +26,24% | -26,24% | -2,32% | +30,09% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 55 | 43,64% | +0,51% | +0,12% | -0,14% | +1,53% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 58 | 58,62% | +0,39% | +0,44% | -0,28% | +1,35% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 58 | 58,62% | +0,39% | +0,44% | -0,28% | +1,35% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 52 | 51,92% | +0,31% | +0,47% | -0,38% | +1,25% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 33 | 39,39% | +0,22% | -0,51% | -0,43% | +0,96% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 54 | 46,30% | +1,03% | +0,39% | +0,23% | +2,35% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 57 | 54,39% | +0,82% | +0,70% | +0,03% | +2,04% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 57 | 54,39% | +0,82% | +0,70% | +0,03% | +2,04% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 51 | 56,86% | +0,43% | +0,79% | -0,34% | +1,64% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 32 | 43,75% | +0,62% | -1,20% | -0,14% | +1,62% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,90% | +2,61% | +2,02% | +4,90% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 53 | 41,51% | +1,55% | +0,76% | -1,50% | +4,44% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 56 | 51,79% | +1,32% | +1,00% | -1,67% | +4,03% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 56 | 51,79% | +1,32% | +1,00% | -1,67% | +4,03% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 50 | 48,00% | +0,48% | +0,82% | -1,94% | +3,08% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 31 | 32,26% | +1,30% | -2,13% | -1,89% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +2,90% | +2,64% | -0,79% | +6,76% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 51 | 50,98% | +2,40% | +1,90% | -2,44% | +6,68% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 54 | 50,00% | +2,22% | +1,91% | -2,54% | +6,37% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 54 | 50,00% | +2,22% | +1,91% | -2,54% | +6,37% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 48 | 58,33% | +1,13% | +0,86% | -3,00% | +5,28% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | +1,54% | +1,34% | -1,56% | +8,05% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 49 | 61,22% | +2,74% | +3,51% | -3,05% | +8,30% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 52 | 55,77% | +2,76% | +2,85% | -3,13% | +8,06% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 52 | 55,77% | +2,76% | +2,85% | -3,13% | +8,06% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 46 | 58,70% | +1,34% | +1,36% | -3,72% | +6,54% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +0,41% | +0,28% | -2,23% | +8,54% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 47 | 57,45% | +2,90% | +3,99% | -3,58% | +9,65% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 49 | 55,10% | +2,80% | +3,51% | -3,64% | +9,37% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 49 | 55,10% | +2,80% | +3,51% | -3,64% | +9,37% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 43 | 62,79% | +0,73% | +1,62% | -4,35% | +6,91% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +0,72% | +0,35% | -3,12% | +9,19% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 44 | 68,18% | +5,14% | +7,25% | -3,83% | +13,51% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 46 | 71,74% | +4,82% | +6,86% | -3,86% | +12,97% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 46 | 71,74% | +4,82% | +6,86% | -3,86% | +12,97% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 39 | 64,10% | +1,50% | +1,05% | -4,58% | +8,64% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 31 | 48,39% | +3,26% | -3,87% | -4,53% | +11,11% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +7,65% | +2,04% | -2,99% | +15,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 37 | 78,38% | +9,43% | +8,36% | -3,77% | +19,44% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 39 | 87,18% | +9,46% | +12,50% | -3,81% | +19,55% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 39 | 87,18% | +9,46% | +12,50% | -3,81% | +19,55% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 37 | 89,19% | +10,04% | +13,11% | -3,82% | +20,36% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 33 | 63,64% | +7,02% | -3,84% | -4,34% | +15,23% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 26 | 57,69% | +6,26% | -6,26% | -4,08% | +14,68% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,49% | -0,95% | -1,31% | +25,23% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 30 | 73,33% | +11,85% | +4,41% | -4,56% | +23,87% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 32 | 87,50% | +12,46% | +11,04% | -4,56% | +24,89% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 32 | 87,50% | +12,46% | +11,04% | -4,56% | +24,89% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 30 | 93,33% | +11,43% | +13,64% | -4,61% | +24,06% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 30 | 40,00% | +11,60% | -11,60% | -4,76% | +23,68% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 22 | 50,00% | +9,38% | -9,38% | -4,86% | +19,29% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +30,85% | +15,03% | -1,31% | +42,05% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 17 | 0,00% | +20,35% | -20,35% | -6,05% | +37,73% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 17 | 5,88% | +20,35% | -16,87% | -6,05% | +37,73% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 17 | 5,88% | +20,35% | -16,87% | -6,05% | +37,73% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 15 | 6,67% | +19,29% | -15,36% | -6,36% | +37,21% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 17 | 0,00% | +20,35% | -20,35% | -6,05% | +37,73% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 16 | 0,00% | +20,67% | -20,67% | -5,92% | +37,88% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 2 | 0,00% | +22,88% | -22,88% | -7,34% | +36,28% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 2 | 0,00% | +22,88% | -22,88% | -7,34% | +36,28% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 2 | 0,00% | +22,88% | -22,88% | -7,34% | +36,28% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 2 | 0,00% | +22,88% | -22,88% | -7,34% | +36,28% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 2 | 0,00% | +22,88% | -22,88% | -7,34% | +36,28% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 2 | 0,00% | +22,88% | -22,88% | -7,34% | +36,28% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 52 | 53,85% | +0,65% | +0,53% | -0,06% | +1,56% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 54 | 55,56% | +0,35% | +0,34% | -0,28% | +1,24% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 57 | 54,39% | +0,39% | +0,26% | -0,25% | +1,27% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 56 | 50,00% | +0,35% | +0,33% | -0,32% | +1,20% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 40 | 50,00% | +0,54% | +0,50% | -0,25% | +1,49% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 51 | 52,94% | +1,35% | +1,21% | +0,40% | +2,45% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 53 | 49,06% | +0,96% | +0,51% | +0,01% | +1,81% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 56 | 48,21% | +0,93% | +0,46% | +0,01% | +1,86% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 55 | 45,45% | +0,86% | +0,31% | -0,02% | +1,97% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 39 | 53,85% | +0,98% | +0,96% | +0,07% | +1,99% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 50 | 60,00% | +2,16% | +1,98% | -1,27% | +4,42% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 52 | 51,92% | +1,66% | +1,09% | -1,58% | +3,91% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 55 | 50,91% | +1,58% | +1,01% | -1,56% | +3,88% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 54 | 51,85% | +1,44% | +0,22% | -1,63% | +3,62% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 38 | 57,89% | +1,41% | +1,26% | -1,57% | +3,61% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 48 | 62,50% | +3,59% | +3,48% | -1,95% | +6,92% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 50 | 56,00% | +2,89% | +1,80% | -2,27% | +6,22% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 53 | 54,72% | +2,77% | +1,66% | -2,25% | +6,09% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 52 | 50,00% | +2,77% | -0,29% | -2,41% | +5,98% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 36 | 61,11% | +2,10% | +1,94% | -2,34% | +5,20% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 46 | 65,22% | +4,89% | +5,01% | -2,43% | +8,79% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 48 | 60,42% | +4,08% | +2,76% | -2,76% | +8,02% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 51 | 60,78% | +3,83% | +2,60% | -2,75% | +7,78% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 50 | 42,00% | +3,79% | -1,23% | -2,93% | +7,72% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 34 | 52,94% | +2,16% | +2,21% | -3,00% | +6,05% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 43 | 69,77% | +7,03% | +7,21% | -2,47% | +11,39% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 45 | 64,44% | +6,11% | +5,10% | -2,89% | +10,26% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 48 | 62,50% | +5,72% | +4,79% | -2,92% | +9,87% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 47 | 48,94% | +5,11% | -2,05% | -3,13% | +9,43% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 31 | 61,29% | +2,34% | +2,45% | -3,16% | +7,00% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 39 | 79,49% | +10,62% | +11,55% | -2,63% | +16,29% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 41 | 80,49% | +10,00% | +9,01% | -3,00% | +14,95% | PRIMA CALIBRAZIONE |

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
