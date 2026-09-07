# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-07 05:32 UTC

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

Segnali totali salvati: **177**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-07 | BTC | 79.828,11 | +7 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-07 | DOGE | 0.09027 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | STAI ALLA FINESTRA |
| 2026-09-07 | SOL | 105,55 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-06 | BTC | 79.879,48 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-06 | DOGE | 0.09088 | +3 | -2 | -2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-06 | SOL | 105,95 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-05 | BTC | 79.660,00 | +5 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-05 | DOGE | 0.08560 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-05 | SOL | 102,27 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-04 | BTC | 80.963,98 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-04 | DOGE | 0.08695 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-04 | SOL | 103,67 | +6 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59 | 58 | 57 | 56 | 54 | 52 | 49 | 45 | 38 | 31 | 16 | 1 |
| SOL | 59 | 58 | 57 | 56 | 54 | 52 | 49 | 45 | 38 | 31 | 16 | 1 |
| DOGE | 59 | 58 | 57 | 56 | 54 | 52 | 49 | 45 | 38 | 31 | 16 | 1 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-10 | 60g | 2026-09-08 | domani |
| SOL | 2026-07-10 | 60g | 2026-09-08 | domani |
| DOGE | 2026-07-10 | 60g | 2026-09-08 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 55 | 50,91% | +0,45% | +0,43% | PRIMA CALIBRAZIONE |
| BTC | 2g | 54 | 53,70% | +0,79% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 3g | 53 | 49,06% | +1,02% | +0,89% | PRIMA CALIBRAZIONE |
| BTC | 5g | 51 | 47,06% | +1,99% | +1,74% | PRIMA CALIBRAZIONE |
| BTC | 7g | 49 | 55,10% | +2,73% | +2,51% | PRIMA CALIBRAZIONE |
| BTC | 10g | 46 | 60,87% | +3,80% | +3,60% | PRIMA CALIBRAZIONE |
| BTC | 14g | 42 | 66,67% | +6,07% | +5,98% | PRIMA CALIBRAZIONE |
| BTC | 21g | 36 | 61,11% | +10,21% | +10,03% | PRIMA CALIBRAZIONE |
| BTC | 30g | 29 | 89,66% | +13,35% | +11,87% | FEEDBACK RAPIDO |
| BTC | 45g | 14 | 85,71% | +22,52% | +16,15% | FEEDBACK RAPIDO |
| BTC | 60g | 1 | 100,00% | +26,24% | +26,24% | FEEDBACK RAPIDO |
| SOL | 1g | 51 | 54,90% | +0,70% | +0,58% | PRIMA CALIBRAZIONE |
| SOL | 2g | 50 | 54,00% | +1,42% | +1,28% | PRIMA CALIBRAZIONE |
| SOL | 3g | 49 | 59,18% | +2,19% | +2,01% | PRIMA CALIBRAZIONE |
| SOL | 5g | 47 | 61,70% | +3,60% | +3,49% | PRIMA CALIBRAZIONE |
| SOL | 7g | 45 | 66,67% | +5,02% | +5,14% | PRIMA CALIBRAZIONE |
| SOL | 10g | 42 | 71,43% | +7,21% | +7,39% | PRIMA CALIBRAZIONE |
| SOL | 14g | 38 | 78,95% | +10,88% | +11,83% | PRIMA CALIBRAZIONE |
| SOL | 21g | 31 | 74,19% | +16,13% | +14,98% | PRIMA CALIBRAZIONE |
| SOL | 30g | 24 | 58,33% | +18,43% | +10,19% | FEEDBACK RAPIDO |
| SOL | 45g | 14 | 35,71% | +33,18% | -11,07% | FEEDBACK RAPIDO |
| SOL | 60g | 1 | 100,00% | +35,29% | +35,29% | FEEDBACK RAPIDO |
| DOGE | 1g | 54 | 44,44% | +0,53% | +0,13% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 53 | 47,17% | +1,07% | +0,41% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 52 | 42,31% | +1,48% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 50 | 52,00% | +2,26% | +2,13% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 48 | 62,50% | +2,63% | +3,74% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 46 | 56,52% | +2,84% | +3,96% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 43 | 69,77% | +5,33% | +7,49% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 36 | 77,78% | +8,88% | +7,78% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 29 | 72,41% | +11,27% | +3,57% | FEEDBACK RAPIDO |
| DOGE | 45g | 16 | 0,00% | +19,77% | -19,77% | FEEDBACK RAPIDO |
| DOGE | 60g | 1 | 0,00% | +23,91% | -23,91% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 55 | 50,91% | +0,45% | +0,43% | -0,00% | +1,00% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 58 | 53,45% | +0,42% | +0,42% | -0,02% | +0,95% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 58 | 53,45% | +0,42% | +0,42% | -0,02% | +0,95% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 53 | 39,62% | +0,55% | +0,16% | +0,09% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,81% | +0,37% | +0,13% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 54 | 53,70% | +0,79% | +0,70% | +0,20% | +1,49% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 57 | 56,14% | +0,88% | +0,88% | +0,30% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 57 | 56,14% | +0,88% | +0,88% | +0,30% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 52 | 46,15% | +1,07% | +0,27% | +0,48% | +1,76% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,18% | +0,55% | +0,59% | +1,89% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,27% | +1,27% | +0,55% | +1,72% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 53 | 49,06% | +1,02% | +0,89% | -0,94% | +2,69% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 56 | 57,14% | +1,31% | +1,31% | -0,93% | +2,91% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 56 | 57,14% | +1,31% | +1,31% | -0,93% | +2,91% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 51 | 39,22% | +1,64% | -0,02% | -0,74% | +3,20% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,81% | +0,20% | -0,58% | +3,31% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,72% | +0,72% | -0,94% | +2,21% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 51 | 47,06% | +1,99% | +1,74% | -1,55% | +4,21% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 54 | 53,70% | +2,24% | +2,24% | -1,52% | +4,52% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 54 | 53,70% | +2,24% | +2,24% | -1,52% | +4,52% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 49 | 44,90% | +2,58% | -0,88% | -1,32% | +4,90% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 22 | 50,00% | +4,06% | -1,22% | -1,06% | +6,26% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 49 | 55,10% | +2,73% | +2,51% | -1,76% | +5,40% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 52 | 61,54% | +3,05% | +3,05% | -1,74% | +5,70% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 52 | 61,54% | +3,05% | +3,05% | -1,74% | +5,70% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 47 | 42,55% | +3,61% | -1,82% | -1,52% | +6,19% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 20 | 45,00% | +5,94% | -3,27% | -1,13% | +8,88% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 46 | 60,87% | +3,80% | +3,60% | -1,99% | +6,54% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 49 | 65,31% | +3,96% | +3,96% | -1,99% | +6,79% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 49 | 65,31% | +3,96% | +3,96% | -1,99% | +6,79% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 44 | 45,45% | +4,55% | -1,50% | -1,74% | +7,43% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 17 | 52,94% | +7,60% | -4,82% | -1,13% | +10,52% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 42 | 66,67% | +6,07% | +5,98% | -1,97% | +9,37% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 45 | 66,67% | +6,11% | +6,11% | -1,99% | +9,45% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 45 | 66,67% | +6,11% | +6,11% | -1,99% | +9,45% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 40 | 62,50% | +7,03% | +0,98% | -1,68% | +10,43% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 13 | 53,85% | +9,92% | -5,20% | -0,30% | +13,51% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +1,23% | +1,23% | -1,55% | +6,04% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 36 | 61,11% | +10,21% | +10,03% | -2,64% | +13,81% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 38 | 68,42% | +9,62% | +9,62% | -2,69% | +13,22% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 38 | 68,42% | +9,62% | +9,62% | -2,69% | +13,22% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 34 | 73,53% | +10,91% | +10,91% | -2,48% | +14,50% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 33 | 33,33% | +10,84% | -1,59% | -2,43% | +14,49% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 8 | 0,00% | +19,34% | -19,34% | -0,83% | +22,19% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 29 | 89,66% | +13,35% | +11,87% | -2,94% | +17,21% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 31 | 83,87% | +13,01% | +13,01% | -2,98% | +16,95% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 31 | 83,87% | +13,01% | +13,01% | -2,98% | +16,95% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 27 | 85,19% | +14,24% | +14,24% | -2,76% | +18,42% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 26 | 38,46% | +13,07% | -4,29% | -2,70% | +17,36% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 14 | 85,71% | +22,52% | +16,15% | -3,23% | +26,32% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 16 | 100,00% | +22,58% | +22,58% | -3,28% | +26,36% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 16 | 100,00% | +22,58% | +22,58% | -3,28% | +26,36% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 12 | 100,00% | +23,08% | +23,08% | -2,88% | +26,74% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 13 | 30,77% | +22,83% | -9,06% | -2,94% | +26,83% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 1 | 100,00% | +26,24% | +26,24% | -2,32% | +30,09% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | +26,24% | +26,24% | -2,32% | +30,09% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | +26,24% | +26,24% | -2,32% | +30,09% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 1 | 100,00% | +26,24% | +26,24% | -2,32% | +30,09% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 1 | 0,00% | +26,24% | -26,24% | -2,32% | +30,09% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 54 | 44,44% | +0,53% | +0,13% | -0,13% | +1,54% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 57 | 57,89% | +0,41% | +0,44% | -0,27% | +1,35% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 57 | 57,89% | +0,41% | +0,44% | -0,27% | +1,35% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 51 | 52,94% | +0,32% | +0,49% | -0,38% | +1,25% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 32 | 40,62% | +0,24% | -0,51% | -0,42% | +0,95% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 53 | 47,17% | +1,07% | +0,41% | +0,26% | +2,39% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 56 | 53,57% | +0,85% | +0,70% | +0,05% | +2,07% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 56 | 53,57% | +0,85% | +0,70% | +0,05% | +2,07% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 50 | 58,00% | +0,46% | +0,83% | -0,32% | +1,66% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +3,38% | +3,05% | +2,44% | +5,44% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 52 | 42,31% | +1,48% | +0,87% | -1,59% | +4,38% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 55 | 52,73% | +1,25% | +1,12% | -1,76% | +3,97% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 55 | 52,73% | +1,25% | +1,12% | -1,76% | +3,97% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 49 | 46,94% | +0,38% | +0,73% | -2,05% | +2,99% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 31 | 32,26% | +1,30% | -2,13% | -1,89% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +2,90% | +2,64% | -0,79% | +6,76% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 50 | 52,00% | +2,26% | +2,13% | -2,53% | +6,52% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 53 | 50,94% | +2,08% | +2,12% | -2,63% | +6,21% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 53 | 50,94% | +2,08% | +2,12% | -2,63% | +6,21% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 47 | 57,45% | +0,95% | +0,68% | -3,11% | +5,09% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | +1,54% | +1,34% | -1,56% | +8,05% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 48 | 62,50% | +2,63% | +3,74% | -3,04% | +8,20% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 51 | 56,86% | +2,66% | +3,06% | -3,12% | +7,96% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 51 | 56,86% | +2,66% | +3,06% | -3,12% | +7,96% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 45 | 57,78% | +1,19% | +1,22% | -3,72% | +6,40% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +0,41% | +0,28% | -2,23% | +8,54% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 46 | 56,52% | +2,84% | +3,96% | -3,54% | +9,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 48 | 56,25% | +2,73% | +3,70% | -3,60% | +9,34% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 48 | 56,25% | +2,73% | +3,70% | -3,60% | +9,34% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 42 | 61,90% | +0,61% | +1,52% | -4,31% | +6,82% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,00% | -0,43% | -2,75% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 43 | 69,77% | +5,33% | +7,49% | -3,60% | +13,80% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 45 | 73,33% | +5,00% | +7,08% | -3,64% | +13,23% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 45 | 73,33% | +5,00% | +7,08% | -3,64% | +13,23% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 38 | 65,79% | +1,62% | +1,16% | -4,34% | +8,83% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 30 | 50,00% | +3,47% | -3,89% | -4,22% | +11,44% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +7,65% | +2,04% | -2,99% | +15,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 36 | 77,78% | +8,88% | +7,78% | -3,89% | +18,78% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 38 | 86,84% | +8,94% | +12,06% | -3,92% | +18,92% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 38 | 86,84% | +8,94% | +12,06% | -3,92% | +18,92% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 36 | 88,89% | +9,51% | +12,66% | -3,93% | +19,72% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 33 | 63,64% | +7,02% | -3,84% | -4,34% | +15,23% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 25 | 60,00% | +5,34% | -5,34% | -4,25% | +13,53% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,49% | -0,95% | -1,31% | +25,23% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 29 | 72,41% | +11,27% | +3,57% | -4,67% | +23,21% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 31 | 87,10% | +11,94% | +10,47% | -4,66% | +24,30% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 31 | 87,10% | +11,94% | +10,47% | -4,66% | +24,30% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 29 | 93,10% | +10,84% | +13,12% | -4,72% | +23,41% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 30 | 40,00% | +11,60% | -11,60% | -4,76% | +23,68% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 21 | 52,38% | +8,46% | -8,46% | -5,03% | +18,17% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +31,57% | +10,47% | -1,27% | +41,74% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 16 | 0,00% | +19,77% | -19,77% | -6,29% | +37,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 16 | 0,00% | +19,77% | -19,77% | -6,29% | +37,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 16 | 0,00% | +19,77% | -19,77% | -6,29% | +37,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 14 | 0,00% | +18,56% | -18,56% | -6,65% | +36,74% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 16 | 0,00% | +19,77% | -19,77% | -6,29% | +37,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 15 | 0,00% | +20,08% | -20,08% | -6,17% | +37,48% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +30,79% | +30,79% | -1,52% | +44,86% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 1 | 0,00% | +23,91% | -23,91% | -6,69% | +37,24% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 1 | 0,00% | +23,91% | -23,91% | -6,69% | +37,24% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 1 | 0,00% | +23,91% | -23,91% | -6,69% | +37,24% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | +23,91% | -23,91% | -6,69% | +37,24% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 1 | 0,00% | +23,91% | -23,91% | -6,69% | +37,24% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 1 | 0,00% | +23,91% | -23,91% | -6,69% | +37,24% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 51 | 54,90% | +0,70% | +0,58% | -0,01% | +1,62% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 53 | 56,60% | +0,40% | +0,39% | -0,24% | +1,29% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 56 | 55,36% | +0,44% | +0,31% | -0,21% | +1,32% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 55 | 50,91% | +0,40% | +0,37% | -0,28% | +1,24% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 39 | 51,28% | +0,61% | +0,57% | -0,20% | +1,55% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 50 | 54,00% | +1,42% | +1,28% | +0,47% | +2,53% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 52 | 50,00% | +1,03% | +0,57% | +0,07% | +1,87% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 55 | 49,09% | +0,99% | +0,52% | +0,06% | +1,92% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 54 | 46,30% | +0,93% | +0,36% | +0,03% | +2,03% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 38 | 55,26% | +1,08% | +1,05% | +0,15% | +2,08% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 49 | 59,18% | +2,19% | +2,01% | -1,31% | +4,41% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 51 | 50,98% | +1,67% | +1,09% | -1,62% | +3,89% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 54 | 50,00% | +1,59% | +1,01% | -1,60% | +3,86% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 53 | 50,94% | +1,45% | +0,21% | -1,67% | +3,59% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 37 | 56,76% | +1,42% | +1,27% | -1,63% | +3,57% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 47 | 61,70% | +3,60% | +3,49% | -2,00% | +6,92% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 49 | 55,10% | +2,89% | +1,78% | -2,32% | +6,20% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 52 | 53,85% | +2,76% | +1,63% | -2,30% | +6,07% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 51 | 49,02% | +2,77% | -0,36% | -2,46% | +5,96% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 35 | 60,00% | +2,07% | +1,91% | -2,42% | +5,15% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 45 | 66,67% | +5,02% | +5,14% | -2,34% | +8,92% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 47 | 61,70% | +4,18% | +2,83% | -2,68% | +8,13% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 50 | 62,00% | +3,92% | +2,67% | -2,68% | +7,88% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 49 | 42,86% | +3,88% | -1,24% | -2,86% | +7,81% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 33 | 54,55% | +2,25% | +2,30% | -2,89% | +6,15% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 42 | 71,43% | +7,21% | +7,39% | -2,38% | +11,59% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 44 | 65,91% | +6,27% | +5,23% | -2,81% | +10,42% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 47 | 63,83% | +5,85% | +4,91% | -2,85% | +10,01% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 46 | 50,00% | +5,23% | -2,08% | -3,06% | +9,57% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 30 | 63,33% | +2,44% | +2,56% | -3,06% | +7,12% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 38 | 78,95% | +10,88% | +11,83% | -2,52% | +16,52% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 40 | 80,00% | +10,23% | +9,21% | -2,90% | +15,14% | PRIMA CALIBRAZIONE |

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
