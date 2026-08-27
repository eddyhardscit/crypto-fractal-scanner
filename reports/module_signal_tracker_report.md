# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-27 05:33 UTC

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

Segnali totali salvati: **144**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-27 | BTC | 78.624,75 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-27 | DOGE | 0.08623 | -1 | -1 | -1 | 0 | +1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-08-27 | SOL | 100,81 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-26 | BTC | 79.104,96 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-26 | DOGE | 0.08675 | +1 | 0 | 0 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-26 | SOL | 96,96 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-25 | BTC | 80.778,18 | +6 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-25 | DOGE | 0.09299 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-25 | SOL | 102,40 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-24 | BTC | 76.958,14 | +6 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-24 | DOGE | 0.09174 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-24 | SOL | 93,82 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 48 | 47 | 46 | 45 | 43 | 41 | 38 | 34 | 29 | 20 | 5 | 0 |
| SOL | 48 | 47 | 46 | 45 | 43 | 41 | 38 | 34 | 29 | 20 | 5 | 0 |
| DOGE | 48 | 47 | 46 | 45 | 43 | 41 | 38 | 34 | 29 | 20 | 5 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-14 | 45g | 2026-08-28 | domani |
| SOL | 2026-07-14 | 45g | 2026-08-28 | domani |
| DOGE | 2026-07-14 | 45g | 2026-08-28 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 44 | 52,27% | +0,52% | +0,49% | PRIMA CALIBRAZIONE |
| BTC | 2g | 43 | 53,49% | +0,93% | +0,82% | PRIMA CALIBRAZIONE |
| BTC | 3g | 42 | 52,38% | +1,25% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 5g | 40 | 42,50% | +2,34% | +2,03% | PRIMA CALIBRAZIONE |
| BTC | 7g | 38 | 50,00% | +3,15% | +2,87% | PRIMA CALIBRAZIONE |
| BTC | 10g | 36 | 50,00% | +3,62% | +3,37% | PRIMA CALIBRAZIONE |
| BTC | 14g | 32 | 56,25% | +3,32% | +3,21% | PRIMA CALIBRAZIONE |
| BTC | 21g | 27 | 48,15% | +5,61% | +5,37% | FEEDBACK RAPIDO |
| BTC | 30g | 18 | 83,33% | +7,23% | +4,83% | FEEDBACK RAPIDO |
| BTC | 45g | 5 | 100,00% | +23,30% | +23,30% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 40 | 57,50% | +0,77% | +0,61% | PRIMA CALIBRAZIONE |
| SOL | 2g | 39 | 53,85% | +1,46% | +1,28% | PRIMA CALIBRAZIONE |
| SOL | 3g | 38 | 57,89% | +2,45% | +2,21% | PRIMA CALIBRAZIONE |
| SOL | 5g | 36 | 61,11% | +3,79% | +3,64% | PRIMA CALIBRAZIONE |
| SOL | 7g | 34 | 64,71% | +4,99% | +5,14% | PRIMA CALIBRAZIONE |
| SOL | 10g | 31 | 64,52% | +4,89% | +5,14% | PRIMA CALIBRAZIONE |
| SOL | 14g | 27 | 70,37% | +4,48% | +5,83% | FEEDBACK RAPIDO |
| SOL | 21g | 22 | 63,64% | +6,83% | +5,21% | FEEDBACK RAPIDO |
| SOL | 30g | 15 | 46,67% | +4,92% | +2,85% | FEEDBACK RAPIDO |
| SOL | 45g | 4 | 50,00% | +27,42% | -1,97% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 45 | 48,89% | +0,48% | +0,47% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 44 | 50,00% | +0,98% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 43 | 48,84% | +1,60% | +1,86% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 41 | 58,54% | +2,97% | +3,58% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 39 | 66,67% | +3,96% | +5,10% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 36 | 61,11% | +2,74% | +4,46% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 32 | 65,62% | +2,98% | +5,88% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 27 | 70,37% | +3,89% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 30g | 19 | 73,68% | +5,52% | -0,26% | FEEDBACK RAPIDO |
| DOGE | 45g | 5 | 0,00% | +22,50% | -22,50% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 44 | 52,27% | +0,52% | +0,49% | +0,07% | +1,10% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 47 | 55,32% | +0,48% | +0,48% | +0,05% | +1,04% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 47 | 55,32% | +0,48% | +0,48% | +0,05% | +1,04% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 42 | 38,10% | +0,65% | +0,16% | +0,19% | +1,22% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 15 | 33,33% | +1,20% | +0,50% | +0,41% | +1,77% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 43 | 53,49% | +0,93% | +0,82% | +0,36% | +1,65% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 46 | 56,52% | +1,04% | +1,04% | +0,47% | +1,74% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 46 | 56,52% | +1,04% | +1,04% | +0,47% | +1,74% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 41 | 43,90% | +1,29% | +0,28% | +0,72% | +2,00% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 14 | 35,71% | +1,85% | +0,76% | +1,32% | +2,61% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 42 | 52,38% | +1,25% | +1,09% | -0,75% | +2,94% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 45 | 62,22% | +1,61% | +1,61% | -0,74% | +3,20% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 45 | 62,22% | +1,61% | +1,61% | -0,74% | +3,20% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 40 | 40,00% | +2,05% | -0,05% | -0,48% | +3,61% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 13 | 46,15% | +3,23% | +0,27% | +0,36% | +4,67% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +2,79% | +2,79% | +0,99% | +4,54% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 40 | 42,50% | +2,34% | +2,03% | -1,42% | +4,38% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 43 | 51,16% | +2,63% | +2,63% | -1,39% | +4,75% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 43 | 51,16% | +2,63% | +2,63% | -1,39% | +4,75% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 38 | 39,47% | +3,12% | -1,34% | -1,13% | +5,28% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 11 | 36,36% | +7,41% | -3,15% | -0,12% | +8,91% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 38 | 50,00% | +3,15% | +2,87% | -1,69% | +5,61% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 41 | 58,54% | +3,53% | +3,53% | -1,67% | +5,97% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 41 | 58,54% | +3,53% | +3,53% | -1,67% | +5,97% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 36 | 33,33% | +4,33% | -2,75% | -1,37% | +6,65% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 9 | 11,11% | +11,68% | -8,79% | -0,04% | +14,00% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 36 | 50,00% | +3,62% | +3,37% | -2,38% | +6,08% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 38 | 55,26% | +3,30% | +3,30% | -2,41% | +5,90% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 38 | 55,26% | +3,30% | +3,30% | -2,41% | +5,90% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +3,94% | +3,94% | -2,29% | +6,32% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 33 | 30,30% | +3,98% | -2,61% | -2,14% | +6,61% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 8 | 0,00% | +13,19% | -13,19% | -0,77% | +15,42% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 32 | 56,25% | +3,32% | +3,21% | -2,89% | +6,39% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 34 | 55,88% | +3,03% | +3,03% | -2,91% | +6,17% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 34 | 55,88% | +3,03% | +3,03% | -2,91% | +6,17% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 30 | 63,33% | +3,77% | +3,77% | -2,71% | +6,68% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 29 | 65,52% | +3,77% | +3,72% | -2,64% | +6,95% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 27 | 48,15% | +5,61% | +5,37% | -2,91% | +9,15% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 29 | 58,62% | +5,15% | +5,15% | -2,97% | +8,70% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 29 | 58,62% | +5,15% | +5,15% | -2,97% | +8,70% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 25 | 64,00% | +6,19% | +6,19% | -2,72% | +9,71% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 24 | 25,00% | +5,89% | -2,19% | -2,65% | +9,50% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 4 | 0,00% | +11,68% | -11,68% | -1,55% | +14,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 18 | 83,33% | +7,23% | +4,83% | -3,23% | +10,88% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 20 | 75,00% | +7,31% | +7,31% | -3,27% | +11,11% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 20 | 75,00% | +7,31% | +7,31% | -3,27% | +11,11% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 16 | 75,00% | +7,96% | +7,96% | -2,97% | +12,12% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 16 | 37,50% | +6,51% | -3,66% | -2,90% | +10,90% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 1 | 0,00% | +24,05% | -24,05% | -1,82% | +28,17% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 5 | 100,00% | +23,30% | +23,30% | -2,65% | +26,27% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 5 | 100,00% | +23,30% | +23,30% | -2,65% | +26,27% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 5 | 100,00% | +23,30% | +23,30% | -2,65% | +26,27% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 5 | 100,00% | +23,30% | +23,30% | -2,65% | +26,27% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 4 | 50,00% | +24,00% | +0,62% | -2,49% | +26,73% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 45 | 48,89% | +0,48% | +0,47% | -0,12% | +1,52% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 46 | 58,70% | +0,39% | +0,66% | -0,22% | +1,39% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 46 | 58,70% | +0,39% | +0,66% | -0,22% | +1,39% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 40 | 55,00% | +0,28% | +0,50% | -0,35% | +1,27% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 31 | 41,94% | +0,27% | -0,51% | -0,38% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +2,86% | +2,41% | +1,15% | +3,54% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 44 | 50,00% | +0,98% | +0,97% | +0,23% | +2,33% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 46 | 52,17% | +0,84% | +1,04% | +0,11% | +2,15% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 46 | 52,17% | +0,84% | +1,04% | +0,11% | +2,15% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 39 | 61,54% | +0,33% | +0,81% | -0,35% | +1,60% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +4,25% | +3,88% | +3,39% | +6,58% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 43 | 48,84% | +1,60% | +1,86% | -1,25% | +4,51% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 45 | 53,33% | +1,43% | +1,71% | -1,35% | +4,27% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 45 | 53,33% | +1,43% | +1,71% | -1,35% | +4,27% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 38 | 50,00% | +0,44% | +0,88% | -1,64% | +3,07% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 30 | 33,33% | +1,54% | -2,01% | -1,63% | +4,45% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +3,59% | +3,29% | -0,23% | +7,51% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 41 | 58,54% | +2,97% | +3,58% | -1,82% | +7,00% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 43 | 55,81% | +2,74% | +3,33% | -1,90% | +6,67% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 43 | 55,81% | +2,74% | +3,33% | -1,90% | +6,67% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 36 | 63,89% | +1,57% | +1,21% | -2,30% | +5,35% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 28 | 42,86% | +3,42% | -3,74% | -2,10% | +7,38% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 50,00% | +3,80% | +3,53% | +0,14% | +10,26% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 39 | 66,67% | +3,96% | +5,10% | -2,18% | +8,85% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 41 | 63,41% | +3,66% | +4,70% | -2,29% | +8,46% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 41 | 63,41% | +3,66% | +4,70% | -2,29% | +8,46% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 34 | 64,71% | +2,16% | +2,20% | -2,79% | +6,62% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 27 | 44,44% | +4,34% | -4,34% | -2,39% | +9,14% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,64% | +3,43% | +1,17% | +11,40% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 36 | 61,11% | +2,74% | +4,46% | -3,20% | +7,92% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 38 | 60,53% | +2,50% | +4,16% | -3,27% | +7,55% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 38 | 60,53% | +2,50% | +4,16% | -3,27% | +7,55% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 36 | 61,11% | +2,68% | +4,34% | -3,25% | +7,72% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 33 | 66,67% | +1,15% | +2,31% | -3,59% | +6,29% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 25 | 52,00% | +2,20% | -2,20% | -3,31% | +7,77% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +0,93% | +0,18% | -1,31% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 32 | 65,62% | +2,98% | +5,88% | -4,04% | +8,39% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 34 | 70,59% | +2,68% | +5,43% | -4,07% | +7,96% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 34 | 70,59% | +2,68% | +5,43% | -4,07% | +7,96% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 32 | 71,88% | +2,94% | +5,67% | -4,09% | +8,18% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 30 | 66,67% | -0,31% | +0,31% | -4,43% | +4,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 22 | 63,64% | +0,33% | -0,33% | -4,43% | +5,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,47% | +2,65% | -1,31% | +16,91% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 27 | 70,37% | +3,89% | +2,42% | -4,88% | +10,61% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 29 | 82,76% | +4,32% | +8,40% | -4,86% | +11,36% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 29 | 82,76% | +4,32% | +8,40% | -4,86% | +11,36% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 27 | 85,19% | +4,73% | +8,93% | -4,94% | +11,86% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 28 | 67,86% | +3,64% | -3,64% | -4,97% | +10,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 20 | 75,00% | +0,03% | -0,03% | -5,18% | +6,01% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 19 | 73,68% | +5,52% | -0,26% | -5,95% | +12,86% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 20 | 80,00% | +6,19% | +3,90% | -5,99% | +14,08% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 20 | 80,00% | +6,19% | +3,90% | -5,99% | +14,08% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 18 | 88,89% | +3,77% | +7,44% | -6,24% | +11,50% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 20 | 60,00% | +6,19% | -6,19% | -5,99% | +14,08% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 17 | 64,71% | +4,96% | -4,96% | -5,74% | +12,22% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 5 | 0,00% | +22,50% | -22,50% | -7,07% | +35,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 5 | 0,00% | +22,50% | -22,50% | -7,07% | +35,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 5 | 0,00% | +22,50% | -22,50% | -7,07% | +35,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 5 | 0,00% | +22,50% | -22,50% | -7,07% | +35,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 5 | 0,00% | +22,50% | -22,50% | -7,07% | +35,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 5 | 0,00% | +22,50% | -22,50% | -7,07% | +35,10% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 40 | 57,50% | +0,77% | +0,61% | +0,11% | +1,72% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 42 | 59,52% | +0,38% | +0,37% | -0,19% | +1,30% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 45 | 57,78% | +0,43% | +0,27% | -0,15% | +1,34% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 44 | 52,27% | +0,38% | +0,35% | -0,24% | +1,25% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 28 | 53,57% | +0,67% | +0,61% | -0,10% | +1,68% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 39 | 53,85% | +1,46% | +1,28% | +0,66% | +2,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 41 | 48,78% | +0,96% | +0,37% | +0,14% | +1,76% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 44 | 47,73% | +0,92% | +0,32% | +0,13% | +1,83% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 43 | 44,19% | +0,83% | +0,12% | +0,09% | +1,97% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 27 | 55,56% | +0,99% | +0,95% | +0,30% | +1,99% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 25,00% | +0,16% | +0,16% | -0,21% | +2,10% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 38 | 57,89% | +2,45% | +2,21% | -0,99% | +4,58% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 40 | 47,50% | +1,77% | +1,04% | -1,41% | +3,91% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 43 | 46,51% | +1,67% | +0,94% | -1,39% | +3,88% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 42 | 47,62% | +1,49% | -0,08% | -1,49% | +3,54% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 26 | 53,85% | +1,48% | +1,27% | -1,31% | +3,48% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,33% | +0,33% | -1,17% | +5,20% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 36 | 61,11% | +3,79% | +3,64% | -1,68% | +6,78% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 38 | 55,26% | +2,86% | +2,20% | -2,11% | +5,86% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 41 | 53,66% | +2,70% | +1,98% | -2,10% | +5,72% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 40 | 45,00% | +2,70% | -1,28% | -2,30% | +5,57% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 24 | 58,33% | +1,65% | +1,41% | -2,13% | +4,13% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +1,18% | +1,18% | -1,95% | +5,20% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 34 | 64,71% | +4,99% | +5,14% | -2,15% | +8,40% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 36 | 66,67% | +3,90% | +4,53% | -2,60% | +7,40% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 39 | 66,67% | +3,59% | +4,19% | -2,61% | +7,13% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 38 | 34,21% | +3,52% | -3,07% | -2,83% | +7,03% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 22 | 45,45% | +0,81% | +0,89% | -2,87% | +3,95% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 31 | 64,52% | +4,89% | +5,14% | -3,14% | +8,44% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 34 | 67,65% | +4,36% | +5,00% | -3,47% | +7,74% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 37 | 64,86% | +3,99% | +4,61% | -3,47% | +7,43% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 32 | 62,50% | +4,96% | +4,79% | -3,31% | +8,14% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 36 | 41,67% | +3,47% | -3,60% | -3,58% | +7,17% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,08% | +0,08% | -3,74% | +3,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 27 | 70,37% | +4,48% | +5,83% | -3,95% | +9,24% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 30 | 83,33% | +4,50% | +5,75% | -4,13% | +8,56% | PRIMA CALIBRAZIONE |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 33 | 84,85% | +3,81% | +5,51% | -4,11% | +8,14% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 28 | 67,86% | +5,06% | +5,18% | -3,82% | +9,08% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 32 | 34,38% | +2,00% | -2,63% | -4,32% | +6,56% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,19% | -1,19% | -4,25% | +5,07% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 22 | 63,64% | +6,83% | +5,21% | -5,57% | +12,24% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 25 | 80,00% | +7,87% | +10,11% | -5,38% | +12,48% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 28 | 82,14% | +6,74% | +9,32% | -5,45% | +11,56% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 23 | 60,87% | +8,79% | +9,53% | -5,08% | +13,45% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 29 | 41,38% | +6,53% | -7,95% | -5,51% | +11,28% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 20 | 40,00% | +9,40% | -9,40% | -4,94% | +13,51% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |

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
