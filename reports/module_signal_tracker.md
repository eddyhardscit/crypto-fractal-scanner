# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-04 05:17 UTC

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

Segnali totali salvati: **81**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-04 | BTC | 63.800,01 | +5 | +4 | +3 | +3 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-04 | DOGE | 0.07017 | +1 | +2 | +1 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-04 | SOL | 73,68 | 0 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-03 | BTC | 62.745,61 | +2 | +4 | +3 | +3 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-03 | DOGE | 0.06985 | -2 | +2 | +1 | +2 | -3 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-08-03 | SOL | 72,93 | +1 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-02 | BTC | 63.392,32 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-02 | DOGE | 0.07018 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-02 | SOL | 73,42 | +1 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-01 | BTC | 63.058,64 | +1 | +3 | +3 | +3 | -1 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-01 | DOGE | 0.07010 | -1 | +3 | +2 | +2 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-08-01 | SOL | 73,13 | +1 | +4 | +3 | +3 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 27 | 26 | 25 | 24 | 22 | 20 | 17 | 13 | 6 | 0 | 0 | 0 |
| SOL | 27 | 26 | 25 | 24 | 22 | 20 | 17 | 13 | 6 | 0 | 0 | 0 |
| DOGE | 27 | 26 | 25 | 24 | 22 | 20 | 17 | 13 | 6 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-15 | 21g | 2026-08-05 | domani |
| SOL | 2026-07-15 | 21g | 2026-08-05 | domani |
| DOGE | 2026-07-15 | 21g | 2026-08-05 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 24 | 45,83% | +0,01% | -0,04% | FEEDBACK RAPIDO |
| BTC | 2g | 23 | 39,13% | +0,01% | -0,19% | FEEDBACK RAPIDO |
| BTC | 3g | 22 | 31,82% | -0,19% | -0,51% | FEEDBACK RAPIDO |
| BTC | 5g | 20 | 20,00% | -0,02% | -0,66% | FEEDBACK RAPIDO |
| BTC | 7g | 18 | 33,33% | +0,13% | -0,47% | FEEDBACK RAPIDO |
| BTC | 10g | 15 | 40,00% | +0,56% | +0,12% | FEEDBACK RAPIDO |
| BTC | 14g | 12 | 58,33% | +0,44% | +0,28% | FEEDBACK RAPIDO |
| BTC | 21g | 6 | 50,00% | +0,27% | +0,27% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 20 | 50,00% | -0,10% | -0,41% | FEEDBACK RAPIDO |
| SOL | 2g | 19 | 36,84% | -0,35% | -0,72% | FEEDBACK RAPIDO |
| SOL | 3g | 18 | 33,33% | -0,48% | -0,97% | FEEDBACK RAPIDO |
| SOL | 5g | 16 | 37,50% | -0,88% | -1,25% | FEEDBACK RAPIDO |
| SOL | 7g | 15 | 46,67% | -1,21% | -0,99% | FEEDBACK RAPIDO |
| SOL | 10g | 14 | 42,86% | -1,94% | -0,42% | FEEDBACK RAPIDO |
| SOL | 14g | 12 | 58,33% | -2,96% | +0,15% | FEEDBACK RAPIDO |
| SOL | 21g | 5 | 60,00% | -4,41% | -0,34% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 25 | 44,00% | -0,03% | -0,05% | FEEDBACK RAPIDO |
| DOGE | 2g | 24 | 45,83% | -0,22% | -0,22% | FEEDBACK RAPIDO |
| DOGE | 3g | 23 | 47,83% | -0,41% | +0,10% | FEEDBACK RAPIDO |
| DOGE | 5g | 21 | 57,14% | -0,82% | +0,38% | FEEDBACK RAPIDO |
| DOGE | 7g | 19 | 63,16% | -1,30% | +0,86% | FEEDBACK RAPIDO |
| DOGE | 10g | 17 | 64,71% | -1,80% | +1,80% | FEEDBACK RAPIDO |
| DOGE | 14g | 13 | 84,62% | -3,02% | +3,02% | FEEDBACK RAPIDO |
| DOGE | 21g | 6 | 100,00% | -4,06% | +4,06% | FEEDBACK RAPIDO |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 24 | 45,83% | +0,01% | -0,04% | -0,32% | +0,63% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 26 | 50,00% | -0,01% | -0,01% | -0,33% | +0,57% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 26 | 50,00% | -0,01% | -0,01% | -0,33% | +0,57% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 22 | 50,00% | -0,06% | -0,06% | -0,40% | +0,47% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 21 | 33,33% | +0,22% | -0,44% | -0,13% | +0,81% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 4 | 0,00% | +0,76% | -0,76% | +0,03% | +1,12% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 23 | 39,13% | +0,01% | -0,19% | -0,52% | +0,79% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 25 | 44,00% | -0,02% | -0,02% | -0,53% | +0,75% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 25 | 44,00% | -0,02% | -0,02% | -0,53% | +0,75% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 21 | 42,86% | -0,16% | -0,16% | -0,69% | +0,61% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 20 | 40,00% | +0,23% | -0,34% | -0,26% | +1,03% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 3 | 33,33% | +0,34% | -0,34% | +0,04% | +1,41% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 22 | 31,82% | -0,19% | -0,51% | -1,55% | +1,75% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 24 | 50,00% | -0,06% | -0,06% | -1,50% | +1,72% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 24 | 50,00% | -0,06% | -0,06% | -1,50% | +1,72% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 20 | 50,00% | -0,11% | -0,11% | -1,56% | +1,60% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 19 | 42,11% | +0,44% | -0,06% | -1,16% | +2,18% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 3 | 33,33% | +0,46% | -0,46% | -0,83% | +2,15% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 20 | 20,00% | -0,02% | -0,66% | -2,33% | +2,39% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 22 | 36,36% | -0,01% | -0,01% | -2,25% | +2,42% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 22 | 36,36% | -0,01% | -0,01% | -2,25% | +2,42% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 18 | 38,89% | +0,11% | +0,11% | -2,27% | +2,42% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 18 | 55,56% | +0,29% | -0,10% | -1,98% | +2,75% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 2 | 50,00% | -0,90% | +0,90% | -2,08% | +2,64% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 18 | 33,33% | +0,13% | -0,47% | -2,49% | +2,82% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 20 | 50,00% | +0,06% | +0,06% | -2,46% | +2,81% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 20 | 50,00% | +0,06% | +0,06% | -2,46% | +2,81% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 16 | 56,25% | +0,41% | +0,41% | -2,43% | +2,91% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 16 | 43,75% | +0,76% | -0,22% | -2,09% | +3,23% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 1 | 0,00% | +0,66% | -0,66% | -1,81% | +3,07% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 15 | 40,00% | +0,56% | +0,12% | -2,66% | +3,50% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 17 | 47,06% | +0,22% | +0,22% | -2,70% | +3,40% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 17 | 47,06% | +0,22% | +0,22% | -2,70% | +3,40% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 13 | 61,54% | +0,92% | +0,92% | -2,48% | +3,72% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 14 | 50,00% | +0,69% | +0,16% | -2,37% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 12 | 58,33% | +0,44% | +0,28% | -2,66% | +4,69% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 13 | 53,85% | +0,30% | +0,30% | -2,60% | +4,69% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 13 | 53,85% | +0,30% | +0,30% | -2,60% | +4,69% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 10 | 70,00% | +1,09% | +1,09% | -2,22% | +5,16% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 11 | 45,45% | +0,39% | -0,02% | -2,32% | +4,94% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 6 | 50,00% | +0,27% | +0,27% | -2,29% | +5,58% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 6 | 50,00% | +0,27% | +0,27% | -2,29% | +5,58% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 6 | 50,00% | +0,27% | +0,27% | -2,29% | +5,58% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | +0,27% | +0,27% | -2,29% | +5,58% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 5 | 20,00% | +0,17% | -0,45% | -2,09% | +5,75% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 25 | 44,00% | -0,03% | -0,05% | -0,50% | +0,64% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 26 | 57,69% | -0,18% | +0,28% | -0,66% | +0,49% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 26 | 57,69% | -0,18% | +0,28% | -0,66% | +0,49% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 24 | 58,33% | -0,04% | +0,14% | -0,54% | +0,65% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 26 | 50,00% | -0,18% | +0,18% | -0,66% | +0,49% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 20 | 40,00% | +0,13% | -0,13% | -0,37% | +0,71% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 24 | 45,83% | -0,22% | -0,22% | -0,86% | +0,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 25 | 48,00% | -0,34% | +0,04% | -0,99% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 25 | 48,00% | -0,34% | +0,04% | -0,99% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 23 | 47,83% | -0,48% | +0,15% | -1,07% | +0,61% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 25 | 60,00% | -0,34% | +0,34% | -0,99% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 20 | 50,00% | +0,13% | -0,13% | -0,57% | +1,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 23 | 47,83% | -0,41% | +0,10% | -2,11% | +1,97% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 24 | 50,00% | -0,58% | -0,06% | -2,22% | +1,79% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 24 | 50,00% | -0,58% | -0,06% | -2,22% | +1,79% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 22 | 54,55% | -0,96% | +0,27% | -2,18% | +1,60% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 24 | 50,00% | -0,58% | +0,58% | -2,22% | +1,79% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 20 | 40,00% | -0,14% | +0,14% | -1,99% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 21 | 57,14% | -0,82% | +0,38% | -3,16% | +2,34% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 22 | 59,09% | -0,95% | +0,21% | -3,25% | +2,13% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 22 | 59,09% | -0,95% | +0,21% | -3,25% | +2,13% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 20 | 60,00% | -1,00% | +0,18% | -3,31% | +1,90% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 22 | 59,09% | -0,95% | +0,95% | -3,25% | +2,13% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 18 | 50,00% | -0,48% | +0,48% | -2,93% | +2,69% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 19 | 63,16% | -1,30% | +0,86% | -3,73% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 20 | 65,00% | -1,44% | +0,70% | -3,88% | +2,32% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 20 | 65,00% | -1,44% | +0,70% | -3,88% | +2,32% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 18 | 66,67% | -1,48% | +0,66% | -4,02% | +2,07% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 20 | 65,00% | -1,44% | +1,44% | -3,88% | +2,32% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 17 | 58,82% | -1,13% | +1,13% | -3,57% | +2,84% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 17 | 64,71% | -1,80% | +1,80% | -4,49% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 17 | 70,59% | -1,80% | +1,92% | -4,49% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 17 | 70,59% | -1,80% | +1,92% | -4,49% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 15 | 73,33% | -1,93% | +2,06% | -4,62% | +2,54% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 17 | 64,71% | -1,80% | +1,80% | -4,49% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 16 | 62,50% | -1,54% | +1,54% | -4,33% | +2,91% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 13 | 84,62% | -3,02% | +3,02% | -5,86% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 13 | 84,62% | -3,02% | +3,02% | -5,86% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 13 | 84,62% | -3,02% | +3,02% | -5,86% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 13 | 84,62% | -3,02% | +3,02% | -5,86% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 13 | 84,62% | -3,02% | +3,02% | -5,86% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 12 | 83,33% | -2,89% | +2,89% | -5,71% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 6 | 100,00% | -4,06% | +4,06% | -6,55% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 6 | 100,00% | -4,06% | +4,06% | -6,55% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 6 | 100,00% | -4,06% | +4,06% | -6,55% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 6 | 100,00% | -4,06% | +4,06% | -6,55% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 6 | 100,00% | -4,06% | +4,06% | -6,55% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 6 | 100,00% | -4,06% | +4,06% | -6,55% | +3,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 20 | 50,00% | -0,10% | -0,41% | -0,60% | +0,66% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 22 | 59,09% | -0,51% | -0,12% | -0,94% | +0,19% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 25 | 56,00% | -0,32% | -0,24% | -0,79% | +0,39% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 20 | 50,00% | -0,29% | -0,09% | -0,88% | +0,39% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 26 | 53,85% | -0,20% | +0,06% | -0,67% | +0,49% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 18 | 55,56% | -0,13% | +0,13% | -0,65% | +0,44% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 19 | 36,84% | -0,35% | -0,72% | -1,01% | +0,67% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 21 | 42,86% | -0,71% | -0,49% | -1,43% | +0,13% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 24 | 41,67% | -0,58% | -0,47% | -1,26% | +0,46% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 19 | 36,84% | -0,65% | -0,60% | -1,37% | +0,44% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 25 | 44,00% | -0,46% | +0,00% | -1,11% | +0,57% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 17 | 52,94% | -0,25% | +0,25% | -0,80% | +0,29% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 18 | 33,33% | -0,48% | -0,97% | -2,32% | +1,85% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 20 | 35,00% | -0,98% | -0,60% | -2,78% | +1,40% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 23 | 34,78% | -0,81% | -0,56% | -2,57% | +1,66% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 18 | 33,33% | -0,88% | -0,99% | -2,59% | +1,65% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 24 | 50,00% | -0,72% | +0,22% | -2,41% | +1,74% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 16 | 50,00% | -0,28% | +0,28% | -2,24% | +1,66% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 16 | 37,50% | -0,88% | -1,25% | -3,28% | +2,53% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 18 | 44,44% | -1,36% | -0,96% | -3,72% | +2,02% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 21 | 42,86% | -1,06% | -0,93% | -3,48% | +2,29% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 16 | 37,50% | -1,65% | -1,19% | -3,61% | +2,17% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 22 | 54,55% | -1,12% | +0,37% | -3,45% | +2,34% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 14 | 64,29% | -0,72% | +0,72% | -3,06% | +2,48% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 15 | 46,67% | -1,21% | -0,99% | -4,00% | +2,73% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 16 | 50,00% | -2,01% | -0,57% | -4,48% | +2,19% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 19 | 52,63% | -1,71% | -0,47% | -4,20% | +2,46% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 14 | 35,71% | -1,76% | -1,61% | -4,38% | +2,32% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 20 | 50,00% | -1,59% | +0,58% | -4,16% | +2,52% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 12 | 66,67% | -1,64% | +1,64% | -3,91% | +2,67% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 14 | 42,86% | -1,94% | -0,42% | -4,67% | +2,77% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 13 | 38,46% | -2,29% | -0,62% | -5,16% | +2,43% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 16 | 37,50% | -1,90% | -0,47% | -4,84% | +2,71% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 11 | 18,18% | -1,75% | -2,26% | -5,01% | +2,64% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 17 | 70,59% | -1,98% | +1,70% | -4,84% | +2,76% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 9 | 88,89% | -2,62% | +2,62% | -4,70% | +3,13% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 12 | 58,33% | -2,96% | +0,15% | -5,17% | +3,14% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 9 | 66,67% | -2,75% | +0,29% | -5,44% | +2,66% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 12 | 75,00% | -2,84% | +0,99% | -5,05% | +2,97% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 8 | 12,50% | -2,91% | -2,46% | -5,15% | +2,78% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 13 | 61,54% | -2,93% | +1,37% | -5,20% | +3,02% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 5 | 100,00% | -2,94% | +2,94% | -4,86% | +4,11% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 5 | 60,00% | -4,41% | -0,34% | -6,66% | +3,01% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | -4,77% | +4,77% | -6,89% | +2,47% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 6 | 100,00% | -4,46% | +4,46% | -6,69% | +2,76% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 5 | 40,00% | -4,41% | -1,00% | -6,66% | +3,01% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 6 | 33,33% | -4,46% | -2,40% | -6,69% | +2,76% | FEEDBACK RAPIDO |
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
