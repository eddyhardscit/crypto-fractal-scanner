# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-09-03 05:32 UTC

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

Segnali totali salvati: **165**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-03 | BTC | 77.295,19 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-03 | DOGE | 0.08235 | -1 | -2 | -2 | 0 | +1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-03 | SOL | 100,15 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-02 | BTC | 77.662,37 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-02 | DOGE | 0.08189 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-02 | SOL | 100,25 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-01 | BTC | 79.026,52 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-01 | DOGE | 0.08350 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-01 | SOL | 104,07 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-31 | BTC | 78.005,28 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-31 | DOGE | 0.08279 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-31 | SOL | 102,56 | +6 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 55 | 54 | 53 | 52 | 50 | 48 | 45 | 41 | 34 | 27 | 12 | 0 |
| SOL | 55 | 54 | 53 | 52 | 50 | 48 | 45 | 41 | 34 | 27 | 12 | 0 |
| DOGE | 55 | 54 | 53 | 52 | 50 | 48 | 45 | 41 | 34 | 27 | 12 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-21 | 45g | 2026-09-04 | domani |
| SOL | 2026-07-21 | 45g | 2026-09-04 | domani |
| DOGE | 2026-07-21 | 45g | 2026-09-04 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 51 | 50,98% | +0,42% | +0,39% | PRIMA CALIBRAZIONE |
| BTC | 2g | 50 | 52,00% | +0,73% | +0,64% | PRIMA CALIBRAZIONE |
| BTC | 3g | 49 | 46,94% | +0,96% | +0,82% | PRIMA CALIBRAZIONE |
| BTC | 5g | 47 | 42,55% | +1,96% | +1,69% | PRIMA CALIBRAZIONE |
| BTC | 7g | 45 | 51,11% | +2,77% | +2,53% | PRIMA CALIBRAZIONE |
| BTC | 10g | 42 | 57,14% | +4,10% | +3,88% | PRIMA CALIBRAZIONE |
| BTC | 14g | 38 | 63,16% | +6,19% | +6,10% | PRIMA CALIBRAZIONE |
| BTC | 21g | 32 | 56,25% | +8,12% | +7,91% | PRIMA CALIBRAZIONE |
| BTC | 30g | 25 | 88,00% | +11,64% | +9,92% | FEEDBACK RAPIDO |
| BTC | 45g | 11 | 81,82% | +22,66% | +14,55% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 47 | 55,32% | +0,65% | +0,51% | PRIMA CALIBRAZIONE |
| SOL | 2g | 46 | 50,00% | +1,31% | +1,16% | PRIMA CALIBRAZIONE |
| SOL | 3g | 45 | 57,78% | +2,18% | +1,98% | PRIMA CALIBRAZIONE |
| SOL | 5g | 43 | 62,79% | +3,81% | +3,68% | PRIMA CALIBRAZIONE |
| SOL | 7g | 41 | 68,29% | +5,52% | +5,65% | PRIMA CALIBRAZIONE |
| SOL | 10g | 38 | 71,05% | +7,68% | +7,89% | PRIMA CALIBRAZIONE |
| SOL | 14g | 34 | 76,47% | +10,64% | +11,71% | PRIMA CALIBRAZIONE |
| SOL | 21g | 27 | 70,37% | +12,82% | +11,51% | FEEDBACK RAPIDO |
| SOL | 30g | 20 | 50,00% | +13,83% | +3,94% | FEEDBACK RAPIDO |
| SOL | 45g | 11 | 27,27% | +33,02% | -17,58% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 50 | 46,00% | +0,38% | +0,36% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 49 | 51,02% | +0,75% | +0,85% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 48 | 45,83% | +1,12% | +1,42% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 47 | 53,19% | +1,95% | +2,62% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 46 | 60,87% | +2,58% | +3,74% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 43 | 60,47% | +3,09% | +4,54% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 39 | 71,79% | +5,91% | +8,29% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 32 | 75,00% | +6,66% | +5,42% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 26 | 69,23% | +9,39% | +0,81% | FEEDBACK RAPIDO |
| DOGE | 45g | 12 | 0,00% | +18,62% | -18,62% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 51 | 50,98% | +0,42% | +0,39% | -0,05% | +0,98% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 54 | 53,70% | +0,39% | +0,39% | -0,06% | +0,93% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 54 | 53,70% | +0,39% | +0,39% | -0,06% | +0,93% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 49 | 38,78% | +0,53% | +0,11% | +0,05% | +1,07% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 22 | 36,36% | +0,74% | +0,27% | +0,03% | +1,28% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 50 | 52,00% | +0,73% | +0,64% | +0,14% | +1,41% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 53 | 54,72% | +0,83% | +0,83% | +0,25% | +1,50% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 53 | 54,72% | +0,83% | +0,83% | +0,25% | +1,50% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 48 | 43,75% | +1,03% | +0,17% | +0,44% | +1,70% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,07% | +0,34% | +0,48% | +1,72% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 49 | 46,94% | +0,96% | +0,82% | -0,93% | +2,63% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 52 | 55,77% | +1,28% | +1,28% | -0,91% | +2,87% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 52 | 55,77% | +1,28% | +1,28% | -0,91% | +2,87% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 47 | 36,17% | +1,63% | -0,17% | -0,71% | +3,18% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 20 | 35,00% | +1,82% | -0,11% | -0,47% | +3,30% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 47 | 42,55% | +1,96% | +1,69% | -1,49% | +4,15% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 50 | 50,00% | +2,22% | +2,22% | -1,46% | +4,49% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 50 | 50,00% | +2,22% | +2,22% | -1,46% | +4,49% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 45 | 40,00% | +2,59% | -1,17% | -1,24% | +4,90% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 18 | 38,89% | +4,43% | -2,02% | -0,79% | +6,56% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 45 | 51,11% | +2,77% | +2,53% | -1,67% | +5,46% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 48 | 58,33% | +3,12% | +3,12% | -1,66% | +5,78% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 48 | 58,33% | +3,12% | +3,12% | -1,66% | +5,78% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 43 | 37,21% | +3,74% | -2,19% | -1,41% | +6,33% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 16 | 31,25% | +6,88% | -4,63% | -0,73% | +9,92% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 42 | 57,14% | +4,10% | +3,88% | -1,79% | +6,87% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 45 | 62,22% | +4,26% | +4,26% | -1,80% | +7,12% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 45 | 62,22% | +4,26% | +4,26% | -1,80% | +7,12% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 40 | 40,00% | +4,93% | -1,71% | -1,50% | +7,86% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 13 | 38,46% | +9,73% | -6,50% | -0,20% | +12,79% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,69% | +0,69% | -0,88% | +5,44% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 38 | 63,16% | +6,19% | +6,10% | -2,12% | +9,57% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 41 | 63,41% | +6,23% | +6,23% | -2,13% | +9,65% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 41 | 63,41% | +6,23% | +6,23% | -2,13% | +9,65% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 36 | 58,33% | +7,27% | +0,54% | -1,80% | +10,76% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 9 | 33,33% | +12,16% | -9,68% | -0,19% | +16,21% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 32 | 56,25% | +8,12% | +7,91% | -2,96% | +11,77% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 34 | 64,71% | +7,57% | +7,57% | -3,00% | +11,24% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 34 | 64,71% | +7,57% | +7,57% | -3,00% | +11,24% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 30 | 70,00% | +8,77% | +8,77% | -2,80% | +12,42% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 29 | 37,93% | +8,61% | +1,92% | -2,74% | +12,34% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 4 | 0,00% | +11,68% | -11,68% | -1,55% | +14,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 25 | 88,00% | +11,64% | +9,92% | -2,89% | +15,63% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 27 | 81,48% | +11,37% | +11,37% | -2,95% | +15,45% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 27 | 81,48% | +11,37% | +11,37% | -2,95% | +15,45% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 23 | 82,61% | +12,53% | +12,53% | -2,68% | +16,91% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 22 | 31,82% | +11,07% | -7,08% | -2,60% | +15,59% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 11 | 81,82% | +22,66% | +14,55% | -2,66% | +26,74% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 12 | 100,00% | +22,75% | +22,75% | -2,66% | +26,79% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 12 | 100,00% | +22,75% | +22,75% | -2,66% | +26,79% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 10 | 100,00% | +23,26% | +23,26% | -2,50% | +26,92% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 11 | 36,36% | +22,95% | -6,68% | -2,60% | +27,01% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 50 | 46,00% | +0,38% | +0,36% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 53 | 58,49% | +0,26% | +0,65% | -0,39% | +1,21% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 53 | 58,49% | +0,26% | +0,65% | -0,39% | +1,21% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 47 | 53,19% | +0,15% | +0,33% | -0,53% | +1,08% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 31 | 41,94% | +0,27% | -0,51% | -0,38% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +2,48% | +2,09% | +0,94% | +3,13% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 49 | 51,02% | +0,75% | +0,85% | -0,03% | +2,05% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 52 | 57,69% | +0,53% | +1,14% | -0,24% | +1,72% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 52 | 57,69% | +0,53% | +1,14% | -0,24% | +1,72% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 46 | 54,35% | +0,06% | +0,46% | -0,68% | +1,23% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +3,38% | +3,05% | +2,44% | +5,44% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 48 | 45,83% | +1,12% | +1,42% | -1,61% | +4,03% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 51 | 56,86% | +0,89% | +1,65% | -1,79% | +3,61% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 51 | 56,86% | +0,89% | +1,65% | -1,79% | +3,61% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 45 | 42,22% | -0,09% | +0,28% | -2,11% | +2,49% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 31 | 32,26% | +1,30% | -2,13% | -1,89% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +2,90% | +2,64% | -0,79% | +6,76% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 47 | 53,19% | +1,95% | +2,62% | -2,48% | +6,34% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 49 | 55,10% | +1,75% | +2,80% | -2,57% | +5,97% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 49 | 55,10% | +1,75% | +2,80% | -2,57% | +5,97% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 43 | 53,49% | +0,47% | +0,17% | -3,09% | +4,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | +1,54% | +1,34% | -1,56% | +8,05% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 46 | 60,87% | +2,58% | +3,74% | -2,92% | +8,27% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 47 | 59,57% | +2,55% | +3,65% | -2,90% | +8,06% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 47 | 59,57% | +2,55% | +3,65% | -2,90% | +8,06% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 41 | 56,10% | +0,92% | +0,95% | -3,53% | +6,36% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | +0,39% | +0,24% | -1,74% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 43 | 60,47% | +3,09% | +4,54% | -3,13% | +10,13% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 45 | 60,00% | +2,87% | +4,28% | -3,19% | +9,73% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 45 | 60,00% | +2,87% | +4,28% | -3,19% | +9,73% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 38 | 63,16% | +0,66% | +1,66% | -3,81% | +7,16% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 30 | 43,33% | +2,51% | -4,32% | -3,63% | +9,66% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +0,00% | -0,43% | -2,75% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 39 | 71,79% | +5,91% | +8,29% | -3,01% | +14,40% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 41 | 75,61% | +5,51% | +7,80% | -3,08% | +13,75% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 41 | 75,61% | +5,51% | +7,80% | -3,08% | +13,75% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 34 | 67,65% | +1,84% | +1,33% | -3,74% | +8,94% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 27 | 51,85% | +4,09% | -4,09% | -3,41% | +12,32% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +12,07% | +4,21% | +0,53% | +20,35% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 32 | 75,00% | +6,66% | +5,42% | -4,30% | +15,73% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 34 | 85,29% | +6,86% | +10,34% | -4,31% | +16,06% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 34 | 85,29% | +6,86% | +10,34% | -4,31% | +16,06% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 32 | 87,50% | +7,37% | +10,91% | -4,34% | +16,79% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 30 | 63,33% | +5,01% | -5,01% | -4,70% | +12,46% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 22 | 68,18% | +2,23% | -2,23% | -4,78% | +9,45% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,49% | -0,95% | -1,31% | +25,23% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 26 | 69,23% | +9,39% | +0,81% | -5,08% | +20,88% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 27 | 85,19% | +9,75% | +8,05% | -5,14% | +21,49% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 27 | 85,19% | +9,75% | +8,05% | -5,14% | +21,49% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 25 | 92,00% | +8,29% | +10,93% | -5,25% | +20,22% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 27 | 44,44% | +9,75% | -9,75% | -5,14% | +21,49% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 20 | 55,00% | +7,30% | -7,30% | -5,27% | +16,83% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 12 | 0,00% | +18,62% | -18,62% | -6,62% | +36,70% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 12 | 0,00% | +18,62% | -18,62% | -6,62% | +36,70% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 12 | 0,00% | +18,62% | -18,62% | -6,62% | +36,70% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 12 | 0,00% | +18,62% | -18,62% | -6,62% | +36,70% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 12 | 0,00% | +18,62% | -18,62% | -6,62% | +36,70% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 11 | 0,00% | +18,94% | -18,94% | -6,48% | +36,83% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 47 | 55,32% | +0,65% | +0,51% | -0,04% | +1,58% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 49 | 57,14% | +0,32% | +0,31% | -0,29% | +1,22% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 52 | 55,77% | +0,37% | +0,23% | -0,25% | +1,26% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 51 | 50,98% | +0,32% | +0,30% | -0,33% | +1,18% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 35 | 51,43% | +0,53% | +0,48% | -0,26% | +1,49% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 46 | 50,00% | +1,31% | +1,16% | +0,39% | +2,40% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 48 | 45,83% | +0,89% | +0,38% | -0,05% | +1,70% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 51 | 45,10% | +0,86% | +0,34% | -0,05% | +1,76% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 50 | 42,00% | +0,78% | +0,17% | -0,08% | +1,88% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 34 | 50,00% | +0,88% | +0,85% | -0,00% | +1,85% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 45 | 57,78% | +2,18% | +1,98% | -1,23% | +4,47% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 47 | 48,94% | +1,62% | +0,99% | -1,57% | +3,90% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 50 | 48,00% | +1,54% | +0,91% | -1,55% | +3,87% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 49 | 48,98% | +1,38% | +0,04% | -1,63% | +3,58% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 33 | 54,55% | +1,31% | +1,15% | -1,56% | +3,55% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 43 | 62,79% | +3,81% | +3,68% | -1,74% | +7,29% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 45 | 55,56% | +3,02% | +1,81% | -2,10% | +6,49% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 48 | 54,17% | +2,88% | +1,66% | -2,09% | +6,33% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 47 | 48,94% | +2,88% | -0,51% | -2,26% | +6,22% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 31 | 61,29% | +2,16% | +1,98% | -2,10% | +5,44% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 41 | 68,29% | +5,52% | +5,65% | -1,91% | +9,55% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 43 | 62,79% | +4,58% | +3,11% | -2,30% | +8,66% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 46 | 63,04% | +4,28% | +2,91% | -2,33% | +8,35% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 45 | 42,22% | +4,24% | -1,33% | -2,51% | +8,29% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 29 | 55,17% | +2,58% | +2,64% | -2,36% | +6,66% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 38 | 71,05% | +7,68% | +7,89% | -2,14% | +12,00% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 40 | 65,00% | +6,62% | +5,48% | -2,63% | +10,70% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 43 | 62,79% | +6,15% | +5,11% | -2,69% | +10,23% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 42 | 47,62% | +5,47% | -2,53% | -2,91% | +9,75% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 26 | 61,54% | +2,40% | +2,53% | -2,82% | +7,04% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +3,45% | +3,45% | -2,62% | +8,30% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 34 | 76,47% | +10,64% | +11,71% | -2,87% | +16,22% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 36 | 86,11% | +9,94% | +10,98% | -3,28% | +14,70% | PRIMA CALIBRAZIONE |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 39 | 87,18% | +8,93% | +10,37% | -3,32% | +13,87% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 34 | 73,53% | +10,71% | +10,82% | -2,97% | +15,49% | PRIMA CALIBRAZIONE |
| SOL | 14g | Tecnico | CALIBRABILE | 38 | 31,58% | +7,21% | -6,80% | -3,65% | +12,34% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 22 | 40,91% | +1,95% | -0,32% | -3,91% | +6,19% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 27 | 70,37% | +12,82% | +11,51% | -4,78% | +18,61% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 30 | 83,33% | +13,10% | +14,96% | -4,70% | +18,17% | PRIMA CALIBRAZIONE |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 33 | 84,85% | +11,66% | +13,85% | -4,82% | +16,87% | PRIMA CALIBRAZIONE |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 28 | 67,86% | +14,22% | +14,83% | -4,40% | +19,38% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 32 | 37,50% | +9,67% | -10,96% | -5,06% | +14,69% | PRIMA CALIBRAZIONE |
| SOL | 21g | Classic technical | CALIBRABILE | 21 | 38,10% | +11,18% | -11,18% | -4,64% | +15,32% | FEEDBACK RAPIDO |

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
