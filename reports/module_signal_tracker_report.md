# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-30 05:33 UTC

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

Segnali totali salvati: **153**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-30 | BTC | 78.145,28 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-30 | DOGE | 0.08501 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-30 | SOL | 105,04 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-29 | BTC | 77.645,39 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-29 | DOGE | 0.08513 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-29 | SOL | 103,94 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-28 | BTC | 79.717,91 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-28 | DOGE | 0.08759 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-28 | SOL | 106,61 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-27 | BTC | 78.624,75 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-27 | DOGE | 0.08623 | -1 | -1 | -1 | 0 | +1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-08-27 | SOL | 100,81 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 51 | 50 | 49 | 48 | 46 | 44 | 41 | 37 | 32 | 23 | 8 | 0 |
| SOL | 51 | 50 | 49 | 48 | 46 | 44 | 41 | 37 | 32 | 23 | 8 | 0 |
| DOGE | 51 | 50 | 49 | 48 | 46 | 44 | 41 | 37 | 32 | 23 | 8 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-17 | 45g | 2026-08-31 | domani |
| SOL | 2026-07-17 | 45g | 2026-08-31 | domani |
| DOGE | 2026-07-17 | 45g | 2026-08-31 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 47 | 53,19% | +0,47% | +0,45% | PRIMA CALIBRAZIONE |
| BTC | 2g | 46 | 52,17% | +0,82% | +0,71% | PRIMA CALIBRAZIONE |
| BTC | 3g | 45 | 48,89% | +1,09% | +0,93% | PRIMA CALIBRAZIONE |
| BTC | 5g | 43 | 44,19% | +2,23% | +1,94% | PRIMA CALIBRAZIONE |
| BTC | 7g | 41 | 53,66% | +3,15% | +2,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | 38 | 52,63% | +4,30% | +4,06% | PRIMA CALIBRAZIONE |
| BTC | 14g | 35 | 60,00% | +5,15% | +5,05% | PRIMA CALIBRAZIONE |
| BTC | 21g | 30 | 53,33% | +7,20% | +6,98% | PRIMA CALIBRAZIONE |
| BTC | 30g | 21 | 85,71% | +9,41% | +7,36% | FEEDBACK RAPIDO |
| BTC | 45g | 8 | 87,50% | +23,29% | +17,78% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 43 | 58,14% | +0,81% | +0,67% | PRIMA CALIBRAZIONE |
| SOL | 2g | 42 | 54,76% | +1,63% | +1,46% | PRIMA CALIBRAZIONE |
| SOL | 3g | 41 | 60,98% | +2,65% | +2,43% | PRIMA CALIBRAZIONE |
| SOL | 5g | 39 | 64,10% | +4,22% | +4,08% | PRIMA CALIBRAZIONE |
| SOL | 7g | 37 | 67,57% | +5,75% | +5,89% | PRIMA CALIBRAZIONE |
| SOL | 10g | 34 | 67,65% | +7,40% | +7,63% | PRIMA CALIBRAZIONE |
| SOL | 14g | 30 | 73,33% | +7,99% | +9,20% | PRIMA CALIBRAZIONE |
| SOL | 21g | 25 | 68,00% | +11,00% | +9,57% | FEEDBACK RAPIDO |
| SOL | 30g | 17 | 41,18% | +9,25% | -2,39% | FEEDBACK RAPIDO |
| SOL | 45g | 7 | 42,86% | +32,02% | -7,77% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 47 | 46,81% | +0,49% | +0,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 46 | 52,17% | +0,93% | +0,98% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 46 | 47,83% | +1,29% | +1,60% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 44 | 54,55% | +2,34% | +2,91% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 42 | 64,29% | +3,55% | +4,60% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 39 | 64,10% | +4,10% | +5,69% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 35 | 68,57% | +4,71% | +7,37% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 30 | 73,33% | +5,83% | +4,51% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 22 | 72,73% | +7,84% | +0,91% | FEEDBACK RAPIDO |
| DOGE | 45g | 8 | 0,00% | +20,70% | -20,70% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 47 | 53,19% | +0,47% | +0,45% | +0,04% | +1,06% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 50 | 56,00% | +0,44% | +0,44% | +0,02% | +1,01% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 50 | 56,00% | +0,44% | +0,44% | +0,02% | +1,01% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 45 | 40,00% | +0,60% | +0,14% | +0,15% | +1,17% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 18 | 38,89% | +0,97% | +0,38% | +0,28% | +1,57% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 46 | 52,17% | +0,82% | +0,71% | +0,24% | +1,54% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 49 | 55,10% | +0,92% | +0,92% | +0,36% | +1,63% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 49 | 55,10% | +0,92% | +0,92% | +0,36% | +1,63% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 44 | 43,18% | +1,15% | +0,21% | +0,58% | +1,86% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 17 | 35,29% | +1,38% | +0,48% | +0,84% | +2,14% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 45 | 48,89% | +1,09% | +0,93% | -0,84% | +2,80% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 48 | 58,33% | +1,43% | +1,43% | -0,83% | +3,05% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 48 | 58,33% | +1,43% | +1,43% | -0,83% | +3,05% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 43 | 37,21% | +1,82% | -0,14% | -0,60% | +3,41% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 16 | 37,50% | +2,39% | -0,01% | -0,12% | +3,93% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 43 | 44,19% | +2,23% | +1,94% | -1,39% | +4,35% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 46 | 52,17% | +2,50% | +2,50% | -1,36% | +4,70% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 46 | 52,17% | +2,50% | +2,50% | -1,36% | +4,70% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 41 | 41,46% | +2,94% | -1,19% | -1,11% | +5,19% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 14 | 42,86% | +5,98% | -2,32% | -0,28% | +7,86% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 41 | 53,66% | +3,15% | +2,89% | -1,58% | +5,69% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 44 | 61,36% | +3,50% | +3,50% | -1,57% | +6,02% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 44 | 61,36% | +3,50% | +3,50% | -1,57% | +6,02% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 39 | 38,46% | +4,24% | -2,30% | -1,28% | +6,65% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 12 | 33,33% | +9,54% | -5,81% | -0,09% | +12,17% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +2,11% | +2,11% | -0,13% | +5,37% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 38 | 52,63% | +4,30% | +4,06% | -1,94% | +6,90% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 41 | 58,54% | +4,46% | +4,46% | -1,94% | +7,17% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 41 | 58,54% | +4,46% | +4,46% | -1,94% | +7,17% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 36 | 33,33% | +5,24% | -2,14% | -1,63% | +8,00% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 9 | 11,11% | +13,10% | -10,35% | -0,13% | +15,57% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 35 | 60,00% | +5,15% | +5,05% | -2,68% | +8,34% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 37 | 59,46% | +4,79% | +4,79% | -2,71% | +8,03% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 37 | 59,46% | +4,79% | +4,79% | -2,71% | +8,03% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 33 | 66,67% | +5,67% | +5,67% | -2,50% | +8,71% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 32 | 59,38% | +5,74% | +1,05% | -2,43% | +9,02% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 7 | 28,57% | +10,76% | -10,76% | -1,07% | +14,38% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 30 | 53,33% | +7,20% | +6,98% | -2,95% | +10,81% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 32 | 62,50% | +6,68% | +6,68% | -3,00% | +10,30% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 32 | 62,50% | +6,68% | +6,68% | -3,00% | +10,30% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 28 | 67,86% | +7,83% | +7,83% | -2,78% | +11,43% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 27 | 33,33% | +7,63% | +0,44% | -2,73% | +11,30% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 4 | 0,00% | +11,68% | -11,68% | -1,55% | +14,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 21 | 85,71% | +9,41% | +7,36% | -3,18% | +13,15% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 23 | 78,26% | +9,30% | +9,30% | -3,22% | +13,16% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 23 | 78,26% | +9,30% | +9,30% | -3,22% | +13,16% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 19 | 78,95% | +10,26% | +10,26% | -2,95% | +14,44% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 18 | 33,33% | +8,35% | -5,82% | -2,87% | +12,70% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 2 | 0,00% | +24,39% | -24,39% | -2,23% | +27,64% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 8 | 87,50% | +23,29% | +17,78% | -2,52% | +26,75% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 8 | 100,00% | +23,29% | +23,29% | -2,52% | +26,75% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 8 | 100,00% | +23,29% | +23,29% | -2,52% | +26,75% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 8 | 100,00% | +23,29% | +23,29% | -2,52% | +26,75% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 7 | 42,86% | +23,69% | -3,82% | -2,41% | +27,08% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 47 | 46,81% | +0,49% | +0,41% | -0,09% | +1,56% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 49 | 59,18% | +0,34% | +0,64% | -0,25% | +1,35% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 49 | 59,18% | +0,34% | +0,64% | -0,25% | +1,35% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 43 | 53,49% | +0,23% | +0,43% | -0,38% | +1,23% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 31 | 41,94% | +0,27% | -0,51% | -0,38% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +2,48% | +2,09% | +0,94% | +3,13% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 46 | 52,17% | +0,93% | +0,98% | +0,18% | +2,29% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 48 | 54,17% | +0,72% | +1,09% | -0,00% | +1,99% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 48 | 54,17% | +0,72% | +1,09% | -0,00% | +1,99% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 42 | 59,52% | +0,23% | +0,67% | -0,45% | +1,49% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +4,25% | +3,88% | +3,39% | +6,58% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 46 | 47,83% | +1,29% | +1,60% | -1,47% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 47 | 53,19% | +1,22% | +1,55% | -1,54% | +4,00% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 47 | 53,19% | +1,22% | +1,55% | -1,54% | +4,00% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 41 | 46,34% | +0,19% | +0,60% | -1,85% | +2,83% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 31 | 32,26% | +1,30% | -2,13% | -1,89% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +3,59% | +3,29% | -0,23% | +7,51% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 44 | 54,55% | +2,34% | +2,91% | -2,26% | +6,55% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 46 | 52,17% | +2,15% | +2,70% | -2,33% | +6,26% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 46 | 52,17% | +2,15% | +2,70% | -2,33% | +6,26% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 39 | 58,97% | +0,96% | +0,63% | -2,77% | +4,97% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | +2,23% | +2,00% | -1,09% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 42 | 64,29% | +3,55% | +4,60% | -2,32% | +8,90% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 44 | 61,36% | +3,28% | +4,25% | -2,42% | +8,54% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 44 | 61,36% | +3,28% | +4,25% | -2,42% | +8,54% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 37 | 62,16% | +1,84% | +1,87% | -2,90% | +6,87% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 29 | 41,38% | +3,64% | -4,44% | -2,71% | +8,78% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 50,00% | +2,08% | +1,90% | -0,18% | +10,26% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 39 | 64,10% | +4,10% | +5,69% | -2,58% | +10,40% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 41 | 63,41% | +3,81% | +5,35% | -2,67% | +9,94% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 41 | 63,41% | +3,81% | +5,35% | -2,67% | +9,94% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 34 | 67,65% | +1,53% | +2,65% | -3,26% | +7,11% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 27 | 48,15% | +3,79% | -3,79% | -2,82% | +10,40% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,56% | +2,95% | +0,53% | +11,40% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 35 | 68,57% | +4,71% | +7,37% | -3,74% | +11,39% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 37 | 72,97% | +4,34% | +6,87% | -3,79% | +10,83% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 37 | 72,97% | +4,34% | +6,87% | -3,79% | +10,83% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +4,68% | +7,18% | -3,79% | +11,19% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 32 | 68,75% | +1,06% | +1,65% | -4,20% | +7,10% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 24 | 58,33% | +2,31% | -2,31% | -4,08% | +8,48% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,47% | +2,65% | -1,31% | +16,91% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 30 | 73,33% | +5,83% | +4,51% | -4,50% | +13,89% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 32 | 84,38% | +6,10% | +9,79% | -4,50% | +14,37% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 32 | 84,38% | +6,10% | +9,79% | -4,50% | +14,37% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 30 | 86,67% | +6,59% | +10,36% | -4,55% | +15,02% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 30 | 63,33% | +5,01% | -5,01% | -4,70% | +12,46% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 22 | 68,18% | +2,23% | -2,23% | -4,78% | +9,45% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,49% | -0,95% | -1,31% | +25,23% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 22 | 72,73% | +7,84% | +0,91% | -5,55% | +16,92% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 23 | 82,61% | +8,32% | +6,34% | -5,61% | +17,80% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 23 | 82,61% | +8,32% | +6,34% | -5,61% | +17,80% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 21 | 90,48% | +6,45% | +9,60% | -5,78% | +15,95% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 23 | 52,17% | +8,32% | -8,32% | -5,61% | +17,80% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 19 | 57,89% | +6,73% | -6,73% | -5,42% | +15,48% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 8 | 0,00% | +20,70% | -20,70% | -7,00% | +35,80% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 8 | 0,00% | +20,70% | -20,70% | -7,00% | +35,80% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 8 | 0,00% | +20,70% | -20,70% | -7,00% | +35,80% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 8 | 0,00% | +20,70% | -20,70% | -7,00% | +35,80% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 8 | 0,00% | +20,70% | -20,70% | -7,00% | +35,80% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 7 | 0,00% | +21,50% | -21,50% | -6,85% | +35,88% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 43 | 58,14% | +0,81% | +0,67% | +0,18% | +1,80% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 45 | 60,00% | +0,45% | +0,44% | -0,11% | +1,41% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 48 | 58,33% | +0,49% | +0,34% | -0,08% | +1,44% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 47 | 53,19% | +0,45% | +0,42% | -0,16% | +1,35% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 31 | 54,84% | +0,75% | +0,69% | +0,01% | +1,80% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 42 | 54,76% | +1,63% | +1,46% | +0,73% | +2,80% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 44 | 50,00% | +1,16% | +0,61% | +0,24% | +2,01% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 47 | 48,94% | +1,10% | +0,55% | +0,22% | +2,06% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 46 | 45,65% | +1,03% | +0,36% | +0,19% | +2,19% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 30 | 56,67% | +1,27% | +1,24% | +0,43% | +2,33% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 41 | 60,98% | +2,65% | +2,43% | -0,90% | +4,88% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 43 | 51,16% | +2,01% | +1,33% | -1,29% | +4,24% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 46 | 50,00% | +1,90% | +1,22% | -1,29% | +4,18% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 45 | 51,11% | +1,73% | +0,27% | -1,37% | +3,88% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 29 | 58,62% | +1,86% | +1,67% | -1,15% | +4,00% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 39 | 64,10% | +4,22% | +4,08% | -1,69% | +7,36% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 41 | 56,10% | +3,33% | +2,01% | -2,08% | +6,48% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 44 | 54,55% | +3,15% | +1,82% | -2,08% | +6,31% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 43 | 48,84% | +3,17% | -0,54% | -2,26% | +6,18% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 27 | 62,96% | +2,50% | +2,29% | -2,09% | +5,27% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,53% | +1,53% | -3,22% | +5,77% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 37 | 67,57% | +5,75% | +5,89% | -1,96% | +9,31% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 39 | 61,54% | +4,70% | +3,08% | -2,39% | +8,34% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 42 | 61,90% | +4,36% | +2,86% | -2,41% | +8,02% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 41 | 39,02% | +4,32% | -1,80% | -2,61% | +7,95% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 25 | 52,00% | +2,44% | +2,51% | -2,50% | +5,84% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +3,96% | +3,96% | -2,17% | +8,29% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 34 | 67,65% | +7,40% | +7,63% | -2,45% | +11,17% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 36 | 69,44% | +6,24% | +6,84% | -2,98% | +9,77% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 39 | 66,67% | +5,74% | +6,33% | -3,02% | +9,32% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 38 | 42,11% | +4,99% | -3,86% | -3,27% | +8,77% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 22 | 54,55% | +1,00% | +1,16% | -3,42% | +4,86% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 30 | 73,33% | +7,99% | +9,20% | -3,71% | +12,91% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 33 | 84,85% | +7,69% | +8,82% | -3,89% | +11,96% | PRIMA CALIBRAZIONE |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 36 | 86,11% | +6,79% | +8,35% | -3,89% | +11,29% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 31 | 70,97% | +8,40% | +8,51% | -3,60% | +12,65% | PRIMA CALIBRAZIONE |
| SOL | 14g | Tecnico | CALIBRABILE | 35 | 31,43% | +5,22% | -5,80% | -4,08% | +9,94% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,19% | -1,19% | -4,25% | +5,07% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 25 | 68,00% | +11,00% | +9,57% | -4,96% | +16,54% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 28 | 82,14% | +11,48% | +13,48% | -4,85% | +16,29% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 31 | 83,87% | +10,11% | +12,44% | -4,97% | +15,09% | PRIMA CALIBRAZIONE |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 26 | 65,38% | +12,57% | +13,23% | -4,55% | +17,44% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 31 | 38,71% | +8,89% | -10,22% | -5,12% | +13,76% | PRIMA CALIBRAZIONE |
| SOL | 21g | Classic technical | CALIBRABILE | 21 | 38,10% | +11,18% | -11,18% | -4,64% | +15,32% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | FEEDBACK RAPIDO |

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
