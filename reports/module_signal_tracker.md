# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-03 05:15 UTC

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

Segnali totali salvati: **78**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-03 | BTC | 62.745,61 | +2 | +4 | +3 | +3 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-03 | DOGE | 0.06985 | -2 | +2 | +1 | +2 | -3 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-08-03 | SOL | 72,93 | +1 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-02 | BTC | 63.392,32 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-02 | DOGE | 0.07018 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-02 | SOL | 73,42 | +1 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-01 | BTC | 63.058,64 | +1 | +3 | +3 | +3 | -1 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-01 | DOGE | 0.07010 | -1 | +3 | +2 | +2 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-08-01 | SOL | 73,13 | +1 | +4 | +3 | +3 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-31 | BTC | 64.349,19 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-31 | DOGE | 0.07006 | -1 | +3 | +2 | +2 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-07-31 | SOL | 74,03 | -1 | +4 | +3 | +3 | -3 | -1 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 26 | 25 | 24 | 23 | 21 | 19 | 16 | 12 | 5 | 0 | 0 | 0 |
| SOL | 26 | 25 | 24 | 23 | 21 | 19 | 16 | 12 | 5 | 0 | 0 | 0 |
| DOGE | 26 | 25 | 24 | 23 | 21 | 19 | 16 | 12 | 5 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-14 | 21g | 2026-08-04 | domani |
| SOL | 2026-07-14 | 21g | 2026-08-04 | domani |
| DOGE | 2026-07-14 | 21g | 2026-08-04 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 23 | 43,48% | -0,06% | -0,11% | FEEDBACK RAPIDO |
| BTC | 2g | 22 | 36,36% | -0,02% | -0,23% | FEEDBACK RAPIDO |
| BTC | 3g | 21 | 28,57% | -0,25% | -0,59% | FEEDBACK RAPIDO |
| BTC | 5g | 19 | 21,05% | -0,01% | -0,68% | FEEDBACK RAPIDO |
| BTC | 7g | 17 | 35,29% | +0,09% | -0,46% | FEEDBACK RAPIDO |
| BTC | 10g | 14 | 42,86% | +0,63% | +0,16% | FEEDBACK RAPIDO |
| BTC | 14g | 11 | 63,64% | +0,71% | +0,54% | FEEDBACK RAPIDO |
| BTC | 21g | 5 | 40,00% | -0,08% | -0,08% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 19 | 47,37% | -0,16% | -0,49% | FEEDBACK RAPIDO |
| SOL | 2g | 18 | 33,33% | -0,39% | -0,78% | FEEDBACK RAPIDO |
| SOL | 3g | 17 | 29,41% | -0,56% | -1,08% | FEEDBACK RAPIDO |
| SOL | 5g | 15 | 40,00% | -0,96% | -1,31% | FEEDBACK RAPIDO |
| SOL | 7g | 14 | 42,86% | -1,34% | -1,10% | FEEDBACK RAPIDO |
| SOL | 10g | 14 | 42,86% | -1,94% | -0,42% | FEEDBACK RAPIDO |
| SOL | 14g | 11 | 63,64% | -2,70% | +0,69% | FEEDBACK RAPIDO |
| SOL | 21g | 4 | 50,00% | -5,09% | -0,84% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 24 | 45,83% | -0,05% | -0,04% | FEEDBACK RAPIDO |
| DOGE | 2g | 23 | 47,83% | -0,23% | -0,23% | FEEDBACK RAPIDO |
| DOGE | 3g | 22 | 50,00% | -0,44% | +0,11% | FEEDBACK RAPIDO |
| DOGE | 5g | 20 | 55,00% | -0,90% | +0,36% | FEEDBACK RAPIDO |
| DOGE | 7g | 18 | 61,11% | -1,39% | +0,89% | FEEDBACK RAPIDO |
| DOGE | 10g | 16 | 68,75% | -1,98% | +1,98% | FEEDBACK RAPIDO |
| DOGE | 14g | 12 | 83,33% | -2,97% | +2,97% | FEEDBACK RAPIDO |
| DOGE | 21g | 5 | 100,00% | -4,35% | +4,35% | FEEDBACK RAPIDO |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 23 | 43,48% | -0,06% | -0,11% | -0,37% | +0,56% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 25 | 48,00% | -0,07% | -0,07% | -0,38% | +0,50% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 25 | 48,00% | -0,07% | -0,07% | -0,38% | +0,50% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 21 | 47,62% | -0,14% | -0,14% | -0,46% | +0,39% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 20 | 35,00% | +0,15% | -0,38% | -0,18% | +0,74% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 3 | 0,00% | +0,46% | -0,46% | -0,25% | +0,77% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 22 | 36,36% | -0,02% | -0,23% | -0,54% | +0,78% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 24 | 41,67% | -0,05% | -0,05% | -0,54% | +0,73% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 24 | 41,67% | -0,05% | -0,05% | -0,54% | +0,73% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 20 | 40,00% | -0,20% | -0,20% | -0,72% | +0,59% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 19 | 42,11% | +0,21% | -0,33% | -0,27% | +1,02% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 3 | 33,33% | +0,34% | -0,34% | +0,04% | +1,41% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 21 | 28,57% | -0,25% | -0,59% | -1,60% | +1,75% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 23 | 47,83% | -0,12% | -0,12% | -1,54% | +1,72% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 23 | 47,83% | -0,12% | -0,12% | -1,54% | +1,72% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 19 | 47,37% | -0,18% | -0,18% | -1,62% | +1,60% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 18 | 44,44% | +0,40% | +0,00% | -1,20% | +2,20% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 2 | 50,00% | +0,10% | -0,10% | -0,99% | +2,40% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 19 | 21,05% | -0,01% | -0,68% | -2,31% | +2,40% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 21 | 38,10% | -0,00% | -0,00% | -2,23% | +2,43% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 21 | 38,10% | -0,00% | -0,00% | -2,23% | +2,43% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 17 | 41,18% | +0,13% | +0,13% | -2,25% | +2,44% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 17 | 52,94% | +0,31% | -0,12% | -1,94% | +2,78% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 2 | 50,00% | -0,90% | +0,90% | -2,08% | +2,64% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 17 | 35,29% | +0,09% | -0,46% | -2,53% | +2,81% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 19 | 47,37% | +0,02% | +0,02% | -2,49% | +2,79% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 19 | 47,37% | +0,02% | +0,02% | -2,49% | +2,79% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 15 | 53,33% | +0,39% | +0,39% | -2,48% | +2,90% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 15 | 46,67% | +0,77% | -0,20% | -2,10% | +3,24% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 14 | 42,86% | +0,63% | +0,16% | -2,65% | +3,58% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 16 | 50,00% | +0,26% | +0,26% | -2,69% | +3,46% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 16 | 50,00% | +0,26% | +0,26% | -2,69% | +3,46% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 12 | 66,67% | +1,03% | +1,03% | -2,45% | +3,82% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 13 | 46,15% | +0,78% | +0,14% | -2,33% | +3,91% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 11 | 63,64% | +0,71% | +0,54% | -2,46% | +4,94% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 12 | 58,33% | +0,54% | +0,54% | -2,40% | +4,93% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 12 | 58,33% | +0,54% | +0,54% | -2,40% | +4,93% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 10 | 70,00% | +1,09% | +1,09% | -2,22% | +5,16% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 11 | 45,45% | +0,39% | -0,02% | -2,32% | +4,94% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 5 | 40,00% | -0,08% | -0,08% | -2,65% | +5,30% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 5 | 40,00% | -0,08% | -0,08% | -2,65% | +5,30% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 5 | 40,00% | -0,08% | -0,08% | -2,65% | +5,30% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 5 | 40,00% | -0,08% | -0,08% | -2,65% | +5,30% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 4 | 25,00% | -0,29% | -0,06% | -2,49% | +5,44% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 24 | 45,83% | -0,05% | -0,04% | -0,52% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 25 | 56,00% | -0,21% | +0,27% | -0,69% | +0,47% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 25 | 56,00% | -0,21% | +0,27% | -0,69% | +0,47% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 23 | 56,52% | -0,06% | +0,13% | -0,57% | +0,64% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 25 | 52,00% | -0,21% | +0,21% | -0,69% | +0,47% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 20 | 40,00% | +0,13% | -0,13% | -0,37% | +0,71% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 23 | 47,83% | -0,23% | -0,23% | -0,88% | +0,82% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 24 | 50,00% | -0,35% | +0,04% | -1,01% | +0,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 24 | 50,00% | -0,35% | +0,04% | -1,01% | +0,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 22 | 50,00% | -0,50% | +0,16% | -1,10% | +0,62% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 24 | 58,33% | -0,35% | +0,35% | -1,01% | +0,68% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 20 | 50,00% | +0,13% | -0,13% | -0,57% | +1,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 22 | 50,00% | -0,44% | +0,11% | -2,14% | +1,99% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 23 | 47,83% | -0,61% | -0,06% | -2,26% | +1,80% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 23 | 47,83% | -0,61% | -0,06% | -2,26% | +1,80% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 21 | 52,38% | -1,01% | +0,27% | -2,22% | +1,60% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 23 | 52,17% | -0,61% | +0,61% | -2,26% | +1,80% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 19 | 42,11% | -0,15% | +0,15% | -2,02% | +2,26% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 20 | 55,00% | -0,90% | +0,36% | -3,20% | +2,35% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 21 | 57,14% | -1,04% | +0,18% | -3,29% | +2,13% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 21 | 57,14% | -1,04% | +0,18% | -3,29% | +2,13% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 19 | 57,89% | -1,09% | +0,15% | -3,36% | +1,88% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 21 | 61,90% | -1,04% | +1,04% | -3,29% | +2,13% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 17 | 52,94% | -0,55% | +0,55% | -2,96% | +2,72% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 18 | 61,11% | -1,39% | +0,89% | -3,79% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 19 | 63,16% | -1,53% | +0,72% | -3,94% | +2,35% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 19 | 63,16% | -1,53% | +0,72% | -3,94% | +2,35% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 17 | 64,71% | -1,59% | +0,68% | -4,09% | +2,09% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 19 | 68,42% | -1,53% | +1,53% | -3,94% | +2,35% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 16 | 62,50% | -1,22% | +1,22% | -3,61% | +2,90% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 16 | 68,75% | -1,98% | +1,98% | -4,64% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 16 | 68,75% | -1,98% | +1,98% | -4,64% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 16 | 68,75% | -1,98% | +1,98% | -4,64% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 14 | 71,43% | -2,14% | +2,14% | -4,79% | +2,28% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 16 | 68,75% | -1,98% | +1,98% | -4,64% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 15 | 66,67% | -1,71% | +1,71% | -4,48% | +2,69% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,20% | +1,20% | -1,52% | +6,93% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 12 | 83,33% | -2,97% | +2,97% | -5,79% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 12 | 83,33% | -2,97% | +2,97% | -5,79% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 12 | 83,33% | -2,97% | +2,97% | -5,79% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 12 | 83,33% | -2,97% | +2,97% | -5,79% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 12 | 83,33% | -2,97% | +2,97% | -5,79% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 11 | 81,82% | -2,83% | +2,83% | -5,62% | +2,66% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 5 | 100,00% | -4,35% | +4,35% | -6,73% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 5 | 100,00% | -4,35% | +4,35% | -6,73% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 5 | 100,00% | -4,35% | +4,35% | -6,73% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 5 | 100,00% | -4,35% | +4,35% | -6,73% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 5 | 100,00% | -4,35% | +4,35% | -6,73% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 5 | 100,00% | -4,35% | +4,35% | -6,73% | +2,99% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 19 | 47,37% | -0,16% | -0,49% | -0,63% | +0,62% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 21 | 57,14% | -0,59% | -0,17% | -1,00% | +0,13% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 24 | 54,17% | -0,38% | -0,29% | -0,83% | +0,35% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 19 | 47,37% | -0,36% | -0,14% | -0,94% | +0,33% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 25 | 56,00% | -0,24% | +0,10% | -0,70% | +0,46% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 17 | 58,82% | -0,20% | +0,20% | -0,69% | +0,39% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 18 | 33,33% | -0,39% | -0,78% | -1,04% | +0,67% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 20 | 40,00% | -0,77% | -0,53% | -1,48% | +0,10% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 23 | 39,13% | -0,62% | -0,51% | -1,29% | +0,45% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 18 | 33,33% | -0,71% | -0,65% | -1,41% | +0,42% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 24 | 45,83% | -0,50% | +0,02% | -1,14% | +0,56% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 16 | 56,25% | -0,29% | +0,29% | -0,81% | +0,26% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 17 | 29,41% | -0,56% | -1,08% | -2,35% | +1,88% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 19 | 31,58% | -1,07% | -0,67% | -2,84% | +1,41% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 22 | 31,82% | -0,88% | -0,62% | -2,61% | +1,67% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 17 | 29,41% | -0,98% | -1,09% | -2,65% | +1,67% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 23 | 52,17% | -0,78% | +0,26% | -2,44% | +1,76% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 15 | 53,33% | -0,34% | +0,34% | -2,27% | +1,68% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 15 | 40,00% | -0,96% | -1,31% | -3,25% | +2,55% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 17 | 41,18% | -1,45% | -1,04% | -3,72% | +2,00% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 20 | 40,00% | -1,13% | -0,99% | -3,46% | +2,29% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 15 | 33,33% | -1,78% | -1,29% | -3,60% | +2,17% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 21 | 57,14% | -1,19% | +0,41% | -3,43% | +2,35% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 13 | 69,23% | -0,80% | +0,80% | -3,00% | +2,50% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 14 | 42,86% | -1,34% | -1,10% | -4,04% | +2,75% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 15 | 46,67% | -2,18% | -0,65% | -4,55% | +2,17% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 18 | 50,00% | -1,83% | -0,52% | -4,24% | +2,46% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 13 | 30,77% | -1,93% | -1,77% | -4,45% | +2,31% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 19 | 52,63% | -1,71% | +0,64% | -4,19% | +2,52% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 11 | 72,73% | -1,84% | +1,84% | -3,95% | +2,68% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 14 | 42,86% | -1,94% | -0,42% | -4,67% | +2,77% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 12 | 41,67% | -2,42% | -0,62% | -5,20% | +2,27% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 15 | 40,00% | -1,98% | -0,45% | -4,85% | +2,60% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 10 | 20,00% | -1,86% | -2,42% | -5,04% | +2,47% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 16 | 68,75% | -2,06% | +1,76% | -4,84% | +2,66% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 8 | 87,50% | -2,87% | +2,87% | -4,70% | +2,98% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 11 | 63,64% | -2,70% | +0,69% | -4,77% | +3,37% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 8 | 75,00% | -2,37% | +1,05% | -4,91% | +2,92% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 11 | 81,82% | -2,57% | +1,61% | -4,63% | +3,19% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 7 | 14,29% | -2,49% | -1,99% | -4,51% | +3,09% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 12 | 58,33% | -2,69% | +1,00% | -4,83% | +3,22% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 5 | 100,00% | -2,94% | +2,94% | -4,86% | +4,11% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 4 | 50,00% | -5,09% | -0,84% | -6,92% | +2,44% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | -4,77% | +4,77% | -6,89% | +2,47% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 5 | 100,00% | -5,02% | +5,02% | -6,90% | +2,26% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 4 | 50,00% | -5,09% | -0,84% | -6,92% | +2,44% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 5 | 20,00% | -5,02% | -3,22% | -6,90% | +2,26% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |

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
