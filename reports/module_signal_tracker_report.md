# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-02 05:15 UTC

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

Segnali totali salvati: **75**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-02 | BTC | 63.392,32 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-02 | DOGE | 0.07018 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-02 | SOL | 73,42 | +1 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-01 | BTC | 63.058,64 | +1 | +3 | +3 | +3 | -1 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-01 | DOGE | 0.07010 | -1 | +3 | +2 | +2 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-08-01 | SOL | 73,13 | +1 | +4 | +3 | +3 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-31 | BTC | 64.349,19 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-31 | DOGE | 0.07006 | -1 | +3 | +2 | +2 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-07-31 | SOL | 74,03 | -1 | +4 | +3 | +3 | -3 | -1 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-07-30 | BTC | 63.914,36 | +2 | +4 | +3 | +2 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-30 | DOGE | 0.06964 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-07-30 | SOL | 73,45 | -1 | +3 | +2 | +3 | -2 | -1 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 25 | 24 | 23 | 22 | 20 | 18 | 15 | 11 | 4 | 0 | 0 | 0 |
| SOL | 25 | 24 | 23 | 22 | 20 | 18 | 15 | 11 | 4 | 0 | 0 | 0 |
| DOGE | 25 | 24 | 23 | 22 | 20 | 18 | 15 | 11 | 4 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-13 | 21g | 2026-08-03 | domani |
| SOL | 2026-07-13 | 21g | 2026-08-03 | domani |
| DOGE | 2026-07-13 | 21g | 2026-08-03 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 22 | 45,45% | -0,02% | -0,07% | FEEDBACK RAPIDO |
| BTC | 2g | 21 | 38,10% | +0,01% | -0,22% | FEEDBACK RAPIDO |
| BTC | 3g | 20 | 30,00% | -0,14% | -0,49% | FEEDBACK RAPIDO |
| BTC | 5g | 18 | 22,22% | +0,09% | -0,62% | FEEDBACK RAPIDO |
| BTC | 7g | 16 | 37,50% | +0,35% | -0,25% | FEEDBACK RAPIDO |
| BTC | 10g | 14 | 42,86% | +0,63% | +0,16% | FEEDBACK RAPIDO |
| BTC | 14g | 10 | 70,00% | +1,00% | +0,82% | FEEDBACK RAPIDO |
| BTC | 21g | 4 | 50,00% | -0,09% | -0,09% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 18 | 50,00% | -0,13% | -0,48% | FEEDBACK RAPIDO |
| SOL | 2g | 17 | 35,29% | -0,40% | -0,81% | FEEDBACK RAPIDO |
| SOL | 3g | 16 | 25,00% | -0,50% | -1,24% | FEEDBACK RAPIDO |
| SOL | 5g | 15 | 40,00% | -0,96% | -1,31% | FEEDBACK RAPIDO |
| SOL | 7g | 14 | 42,86% | -1,34% | -1,10% | FEEDBACK RAPIDO |
| SOL | 10g | 14 | 42,86% | -1,94% | -0,42% | FEEDBACK RAPIDO |
| SOL | 14g | 10 | 60,00% | -2,57% | +0,36% | FEEDBACK RAPIDO |
| SOL | 21g | 3 | 33,33% | -5,29% | -2,62% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 23 | 47,83% | -0,03% | -0,02% | FEEDBACK RAPIDO |
| DOGE | 2g | 22 | 45,45% | -0,23% | -0,26% | FEEDBACK RAPIDO |
| DOGE | 3g | 21 | 47,62% | -0,44% | +0,10% | FEEDBACK RAPIDO |
| DOGE | 5g | 19 | 57,89% | -0,89% | +0,44% | FEEDBACK RAPIDO |
| DOGE | 7g | 18 | 61,11% | -1,39% | +0,89% | FEEDBACK RAPIDO |
| DOGE | 10g | 15 | 73,33% | -2,19% | +2,19% | FEEDBACK RAPIDO |
| DOGE | 14g | 11 | 81,82% | -2,99% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 21g | 4 | 100,00% | -4,62% | +4,62% | FEEDBACK RAPIDO |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 22 | 45,45% | -0,02% | -0,07% | -0,34% | +0,58% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 24 | 50,00% | -0,03% | -0,03% | -0,35% | +0,52% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 24 | 50,00% | -0,03% | -0,03% | -0,35% | +0,52% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 20 | 50,00% | -0,09% | -0,09% | -0,43% | +0,40% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 19 | 31,58% | +0,21% | -0,45% | -0,13% | +0,77% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 3 | 0,00% | +0,46% | -0,46% | -0,25% | +0,77% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 21 | 38,10% | +0,01% | -0,22% | -0,54% | +0,78% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 23 | 43,48% | -0,03% | -0,03% | -0,54% | +0,74% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 23 | 43,48% | -0,03% | -0,03% | -0,54% | +0,74% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 19 | 42,11% | -0,18% | -0,18% | -0,73% | +0,58% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 18 | 38,89% | +0,25% | -0,37% | -0,26% | +1,04% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 2 | 0,00% | +0,76% | -0,76% | +0,33% | +1,77% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 20 | 30,00% | -0,14% | -0,49% | -1,52% | +1,91% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 22 | 50,00% | -0,01% | -0,01% | -1,46% | +1,86% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 22 | 50,00% | -0,01% | -0,01% | -1,46% | +1,86% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 18 | 50,00% | -0,05% | -0,05% | -1,52% | +1,76% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 18 | 44,44% | +0,40% | +0,00% | -1,20% | +2,20% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 2 | 50,00% | +0,10% | -0,10% | -0,99% | +2,40% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 18 | 22,22% | +0,09% | -0,62% | -2,29% | +2,41% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 20 | 40,00% | +0,09% | +0,09% | -2,21% | +2,44% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 20 | 40,00% | +0,09% | +0,09% | -2,21% | +2,44% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 16 | 43,75% | +0,25% | +0,25% | -2,23% | +2,45% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 16 | 50,00% | +0,45% | -0,24% | -1,90% | +2,82% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 1 | 0,00% | +0,02% | -0,02% | -1,53% | +3,07% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 16 | 37,50% | +0,35% | -0,25% | -2,40% | +2,99% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 18 | 50,00% | +0,25% | +0,25% | -2,36% | +2,95% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 18 | 50,00% | +0,25% | +0,25% | -2,36% | +2,95% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | +0,70% | +0,70% | -2,31% | +3,11% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 15 | 46,67% | +0,77% | -0,20% | -2,10% | +3,24% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 14 | 42,86% | +0,63% | +0,16% | -2,65% | +3,58% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 15 | 53,33% | +0,54% | +0,54% | -2,56% | +3,66% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 15 | 53,33% | +0,54% | +0,54% | -2,56% | +3,66% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 11 | 72,73% | +1,48% | +1,48% | -2,24% | +4,12% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 12 | 41,67% | +1,17% | -0,17% | -2,13% | +4,20% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 10 | 70,00% | +1,00% | +0,82% | -2,40% | +5,02% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 11 | 63,64% | +0,80% | +0,80% | -2,34% | +4,99% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 11 | 63,64% | +0,80% | +0,80% | -2,34% | +4,99% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 10 | 70,00% | +1,09% | +1,09% | -2,22% | +5,16% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 10 | 40,00% | +0,65% | -0,24% | -2,25% | +5,01% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 4 | 50,00% | -0,09% | -0,09% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 4 | 50,00% | -0,09% | -0,09% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 4 | 50,00% | -0,09% | -0,09% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 4 | 50,00% | -0,09% | -0,09% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 3 | 33,33% | -0,38% | -0,07% | -3,03% | +5,05% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 23 | 47,83% | -0,03% | -0,02% | -0,52% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 24 | 58,33% | -0,20% | +0,30% | -0,69% | +0,46% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 24 | 58,33% | -0,20% | +0,30% | -0,69% | +0,46% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 22 | 59,09% | -0,04% | +0,16% | -0,57% | +0,64% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 24 | 50,00% | -0,20% | +0,20% | -0,69% | +0,46% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 20 | 40,00% | +0,13% | -0,13% | -0,37% | +0,71% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 22 | 45,45% | -0,23% | -0,26% | -0,90% | +0,82% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 23 | 52,17% | -0,35% | +0,06% | -1,03% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 23 | 52,17% | -0,35% | +0,06% | -1,03% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 21 | 52,38% | -0,51% | +0,18% | -1,12% | +0,61% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 23 | 56,52% | -0,35% | +0,35% | -1,03% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 19 | 47,37% | +0,16% | -0,16% | -0,57% | +1,26% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 21 | 47,62% | -0,44% | +0,10% | -2,10% | +2,04% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 22 | 50,00% | -0,62% | -0,05% | -2,22% | +1,85% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 22 | 50,00% | -0,62% | -0,05% | -2,22% | +1,85% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 20 | 55,00% | -1,05% | +0,30% | -2,18% | +1,64% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 22 | 50,00% | -0,62% | +0,62% | -2,22% | +1,85% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 18 | 38,89% | -0,14% | +0,14% | -1,96% | +2,34% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 19 | 57,89% | -0,89% | +0,44% | -3,17% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 20 | 60,00% | -1,03% | +0,25% | -3,27% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 20 | 60,00% | -1,03% | +0,25% | -3,27% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 18 | 61,11% | -1,10% | +0,22% | -3,34% | +1,96% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 20 | 60,00% | -1,03% | +1,03% | -3,27% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 17 | 52,94% | -0,55% | +0,55% | -2,96% | +2,72% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 18 | 61,11% | -1,39% | +0,89% | -3,79% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 18 | 66,67% | -1,39% | +0,99% | -3,79% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 18 | 66,67% | -1,39% | +0,99% | -3,79% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 16 | 68,75% | -1,43% | +0,98% | -3,92% | +2,36% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 18 | 66,67% | -1,39% | +1,39% | -3,79% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 16 | 62,50% | -1,22% | +1,22% | -3,61% | +2,90% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 15 | 73,33% | -2,19% | +2,19% | -4,84% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 15 | 73,33% | -2,19% | +2,19% | -4,84% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 15 | 73,33% | -2,19% | +2,19% | -4,84% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 14 | 71,43% | -2,14% | +2,14% | -4,79% | +2,28% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 15 | 73,33% | -2,19% | +2,19% | -4,84% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 14 | 71,43% | -1,92% | +1,92% | -4,69% | +2,39% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 11 | 81,82% | -2,99% | +2,99% | -5,83% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 11 | 81,82% | -2,99% | +2,99% | -5,83% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 11 | 81,82% | -2,99% | +2,99% | -5,83% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 11 | 81,82% | -2,99% | +2,99% | -5,83% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 11 | 81,82% | -2,99% | +2,99% | -5,83% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 10 | 80,00% | -2,84% | +2,84% | -5,65% | +2,65% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 4 | 100,00% | -4,62% | +4,62% | -6,94% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | -4,62% | +4,62% | -6,94% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | -4,62% | +4,62% | -6,94% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 4 | 100,00% | -4,62% | +4,62% | -6,94% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 4 | 100,00% | -4,62% | +4,62% | -6,94% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 4 | 100,00% | -4,62% | +4,62% | -6,94% | +2,68% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 18 | 50,00% | -0,13% | -0,48% | -0,62% | +0,65% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 20 | 60,00% | -0,58% | -0,15% | -1,00% | +0,14% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 23 | 56,52% | -0,36% | -0,27% | -0,82% | +0,36% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 18 | 50,00% | -0,34% | -0,12% | -0,94% | +0,35% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 24 | 54,17% | -0,23% | +0,08% | -0,70% | +0,47% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 16 | 56,25% | -0,17% | +0,17% | -0,68% | +0,41% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 17 | 35,29% | -0,40% | -0,81% | -1,07% | +0,68% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 19 | 42,11% | -0,79% | -0,55% | -1,53% | +0,08% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 22 | 40,91% | -0,64% | -0,52% | -1,33% | +0,45% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 17 | 35,29% | -0,73% | -0,68% | -1,47% | +0,42% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 23 | 43,48% | -0,51% | +0,01% | -1,16% | +0,57% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 15 | 53,33% | -0,29% | +0,29% | -0,83% | +0,25% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 16 | 25,00% | -0,50% | -1,24% | -2,22% | +2,04% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 18 | 33,33% | -1,05% | -0,62% | -2,74% | +1,53% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 21 | 33,33% | -0,86% | -0,58% | -2,52% | +1,79% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 16 | 31,25% | -0,95% | -1,06% | -2,53% | +1,83% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 22 | 50,00% | -0,75% | +0,21% | -2,35% | +1,87% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 14 | 50,00% | -0,26% | +0,26% | -2,11% | +1,86% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 15 | 40,00% | -0,96% | -1,31% | -3,25% | +2,55% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 16 | 43,75% | -1,50% | -1,06% | -3,72% | +1,99% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 19 | 42,11% | -1,15% | -1,00% | -3,45% | +2,29% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 14 | 35,71% | -1,85% | -1,33% | -3,59% | +2,16% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 20 | 55,00% | -1,21% | +0,39% | -3,42% | +2,35% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 12 | 66,67% | -0,80% | +0,80% | -2,94% | +2,52% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 14 | 42,86% | -1,34% | -1,10% | -4,04% | +2,75% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 14 | 50,00% | -2,01% | -0,37% | -4,34% | +2,45% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 17 | 52,94% | -1,67% | -0,29% | -4,05% | +2,70% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 12 | 33,33% | -1,72% | -1,54% | -4,20% | +2,64% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 18 | 50,00% | -1,55% | +0,42% | -4,01% | +2,75% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 10 | 70,00% | -1,57% | +1,57% | -3,60% | +3,12% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 14 | 42,86% | -1,94% | -0,42% | -4,67% | +2,77% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 11 | 45,45% | -2,31% | -0,34% | -5,07% | +2,28% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 14 | 42,86% | -1,86% | -0,22% | -4,72% | +2,63% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 9 | 22,22% | -1,66% | -2,27% | -4,87% | +2,50% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 15 | 66,67% | -1,96% | +1,63% | -4,73% | +2,69% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 7 | 85,71% | -2,75% | +2,75% | -4,43% | +3,10% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 10 | 60,00% | -2,57% | +0,36% | -4,54% | +3,35% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 8 | 75,00% | -2,37% | +1,05% | -4,91% | +2,92% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 11 | 81,82% | -2,57% | +1,61% | -4,63% | +3,19% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 7 | 14,29% | -2,49% | -1,99% | -4,51% | +3,09% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 11 | 54,55% | -2,57% | +0,72% | -4,63% | +3,19% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 4 | 100,00% | -2,66% | +2,66% | -4,32% | +4,25% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 3 | 33,33% | -5,29% | -2,62% | -6,74% | +2,16% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | -4,86% | +4,86% | -6,70% | +2,20% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | -5,15% | +5,15% | -6,77% | +2,00% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 3 | 33,33% | -5,29% | -2,62% | -6,74% | +2,16% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 4 | 0,00% | -5,15% | -5,15% | -6,77% | +2,00% | FEEDBACK RAPIDO |
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
