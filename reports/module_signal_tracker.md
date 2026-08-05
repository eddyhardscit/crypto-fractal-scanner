# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-05 05:15 UTC

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

Segnali totali salvati: **84**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-05 | BTC | 64.252,74 | +2 | +4 | +3 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-05 | DOGE | 0.06992 | 0 | +2 | +1 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-05 | SOL | 73,88 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-04 | BTC | 63.800,01 | +5 | +4 | +3 | +3 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-04 | DOGE | 0.07017 | +1 | +2 | +1 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-04 | SOL | 73,68 | 0 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-03 | BTC | 62.745,61 | +2 | +4 | +3 | +3 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-03 | DOGE | 0.06985 | -2 | +2 | +1 | +2 | -3 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-08-03 | SOL | 72,93 | +1 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-02 | BTC | 63.392,32 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-02 | DOGE | 0.07018 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-02 | SOL | 73,42 | +1 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 28 | 27 | 26 | 25 | 23 | 21 | 18 | 14 | 7 | 0 | 0 | 0 |
| SOL | 28 | 27 | 26 | 25 | 23 | 21 | 18 | 14 | 7 | 0 | 0 | 0 |
| DOGE | 28 | 27 | 26 | 25 | 23 | 21 | 18 | 14 | 7 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-16 | 21g | 2026-08-06 | domani |
| SOL | 2026-07-16 | 21g | 2026-08-06 | domani |
| DOGE | 2026-07-16 | 21g | 2026-08-06 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 25 | 48,00% | +0,04% | -0,01% | FEEDBACK RAPIDO |
| BTC | 2g | 24 | 41,67% | +0,11% | -0,09% | FEEDBACK RAPIDO |
| BTC | 3g | 23 | 34,78% | -0,12% | -0,42% | FEEDBACK RAPIDO |
| BTC | 5g | 21 | 19,05% | -0,03% | -0,63% | FEEDBACK RAPIDO |
| BTC | 7g | 19 | 36,84% | +0,15% | -0,42% | FEEDBACK RAPIDO |
| BTC | 10g | 16 | 37,50% | +0,51% | +0,09% | FEEDBACK RAPIDO |
| BTC | 14g | 13 | 53,85% | +0,17% | +0,03% | FEEDBACK RAPIDO |
| BTC | 21g | 7 | 42,86% | +0,17% | +0,17% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 20 | 50,00% | -0,10% | -0,41% | FEEDBACK RAPIDO |
| SOL | 2g | 20 | 40,00% | -0,27% | -0,62% | FEEDBACK RAPIDO |
| SOL | 3g | 19 | 36,84% | -0,42% | -0,89% | FEEDBACK RAPIDO |
| SOL | 5g | 17 | 41,18% | -0,84% | -1,16% | FEEDBACK RAPIDO |
| SOL | 7g | 15 | 46,67% | -1,21% | -0,99% | FEEDBACK RAPIDO |
| SOL | 10g | 14 | 42,86% | -1,94% | -0,42% | FEEDBACK RAPIDO |
| SOL | 14g | 13 | 61,54% | -3,12% | +0,53% | FEEDBACK RAPIDO |
| SOL | 21g | 6 | 50,00% | -4,46% | -1,07% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 26 | 42,31% | -0,04% | -0,06% | FEEDBACK RAPIDO |
| DOGE | 2g | 25 | 44,00% | -0,21% | -0,22% | FEEDBACK RAPIDO |
| DOGE | 3g | 24 | 45,83% | -0,41% | +0,08% | FEEDBACK RAPIDO |
| DOGE | 5g | 22 | 59,09% | -0,79% | +0,37% | FEEDBACK RAPIDO |
| DOGE | 7g | 20 | 60,00% | -1,28% | +0,77% | FEEDBACK RAPIDO |
| DOGE | 10g | 18 | 61,11% | -1,97% | +1,44% | FEEDBACK RAPIDO |
| DOGE | 14g | 14 | 85,71% | -3,12% | +3,12% | FEEDBACK RAPIDO |
| DOGE | 21g | 7 | 100,00% | -4,26% | +4,26% | FEEDBACK RAPIDO |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 25 | 48,00% | +0,04% | -0,01% | -0,30% | +0,64% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 27 | 51,85% | +0,02% | +0,02% | -0,31% | +0,58% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 27 | 51,85% | +0,02% | +0,02% | -0,31% | +0,58% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 23 | 52,17% | -0,02% | -0,02% | -0,38% | +0,49% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 22 | 36,36% | +0,24% | -0,39% | -0,12% | +0,81% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 4 | 0,00% | +0,76% | -0,76% | +0,03% | +1,12% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 24 | 41,67% | +0,11% | -0,09% | -0,42% | +0,87% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 26 | 46,15% | +0,07% | +0,07% | -0,44% | +0,82% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 26 | 46,15% | +0,07% | +0,07% | -0,44% | +0,82% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 22 | 45,45% | -0,04% | -0,04% | -0,57% | +0,71% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 21 | 38,10% | +0,34% | -0,44% | -0,16% | +1,10% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 4 | 25,00% | +0,86% | -0,86% | +0,50% | +1,73% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 23 | 34,78% | -0,12% | -0,42% | -1,56% | +1,74% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 25 | 52,00% | -0,01% | -0,01% | -1,51% | +1,71% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 25 | 52,00% | -0,01% | -0,01% | -1,51% | +1,71% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 21 | 52,38% | -0,04% | -0,04% | -1,57% | +1,61% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 20 | 40,00% | +0,48% | -0,12% | -1,19% | +2,15% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 3 | 33,33% | +0,46% | -0,46% | -0,83% | +2,15% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 21 | 19,05% | -0,03% | -0,63% | -2,37% | +2,28% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 23 | 34,78% | -0,01% | -0,01% | -2,29% | +2,32% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 23 | 34,78% | -0,01% | -0,01% | -2,29% | +2,32% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 19 | 36,84% | +0,10% | +0,10% | -2,33% | +2,30% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 18 | 55,56% | +0,29% | -0,10% | -1,98% | +2,75% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 2 | 50,00% | -0,90% | +0,90% | -2,08% | +2,64% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 19 | 36,84% | +0,15% | -0,42% | -2,50% | +2,79% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 21 | 52,38% | +0,08% | +0,08% | -2,46% | +2,78% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 21 | 52,38% | +0,08% | +0,08% | -2,46% | +2,78% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 17 | 58,82% | +0,42% | +0,42% | -2,45% | +2,87% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 17 | 41,18% | +0,75% | -0,24% | -2,12% | +3,17% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 2 | 0,00% | +0,60% | -0,60% | -2,23% | +2,64% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 16 | 37,50% | +0,51% | +0,09% | -2,71% | +3,40% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 18 | 44,44% | +0,19% | +0,19% | -2,74% | +3,32% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 18 | 44,44% | +0,19% | +0,19% | -2,74% | +3,32% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | +0,83% | +0,83% | -2,55% | +3,59% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 15 | 46,67% | +0,63% | +0,13% | -2,44% | +3,68% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 13 | 53,85% | +0,17% | +0,03% | -2,92% | +4,33% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 14 | 50,00% | +0,07% | +0,07% | -2,85% | +4,36% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 14 | 50,00% | +0,07% | +0,07% | -2,85% | +4,36% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 10 | 70,00% | +1,09% | +1,09% | -2,22% | +5,16% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 11 | 45,45% | +0,39% | -0,02% | -2,32% | +4,94% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 7 | 42,86% | +0,17% | +0,17% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 7 | 42,86% | +0,17% | +0,17% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 7 | 42,86% | +0,17% | +0,17% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 7 | 42,86% | +0,17% | +0,17% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 6 | 16,67% | +0,07% | -0,44% | -2,34% | +5,40% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 26 | 42,31% | -0,04% | -0,06% | -0,51% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 27 | 55,56% | -0,19% | +0,26% | -0,66% | +0,48% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 27 | 55,56% | -0,19% | +0,26% | -0,66% | +0,48% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 25 | 56,00% | -0,05% | +0,12% | -0,55% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 27 | 51,85% | -0,19% | +0,19% | -0,66% | +0,48% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 20 | 40,00% | +0,13% | -0,13% | -0,37% | +0,71% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 25 | 44,00% | -0,21% | -0,22% | -0,84% | +0,80% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 26 | 50,00% | -0,32% | +0,04% | -0,96% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 26 | 50,00% | -0,32% | +0,04% | -0,96% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 24 | 50,00% | -0,45% | +0,15% | -1,03% | +0,61% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 26 | 57,69% | -0,32% | +0,32% | -0,96% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 20 | 50,00% | +0,13% | -0,13% | -0,57% | +1,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 24 | 45,83% | -0,41% | +0,08% | -2,09% | +1,92% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 25 | 48,00% | -0,57% | -0,07% | -2,20% | +1,75% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 25 | 48,00% | -0,57% | -0,07% | -2,20% | +1,75% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 23 | 52,17% | -0,93% | +0,24% | -2,17% | +1,56% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 25 | 52,00% | -0,57% | +0,57% | -2,20% | +1,75% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 20 | 40,00% | -0,14% | +0,14% | -1,99% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 22 | 59,09% | -0,79% | +0,37% | -3,15% | +2,31% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 23 | 56,52% | -0,92% | +0,19% | -3,24% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 23 | 56,52% | -0,92% | +0,19% | -3,24% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 21 | 57,14% | -0,96% | +0,16% | -3,30% | +1,88% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 23 | 60,87% | -0,92% | +0,92% | -3,24% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 19 | 52,63% | -0,46% | +0,46% | -2,93% | +2,63% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 20 | 60,00% | -1,28% | +0,77% | -3,73% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 21 | 61,90% | -1,42% | +0,62% | -3,88% | +2,24% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 21 | 61,90% | -1,42% | +0,62% | -3,88% | +2,24% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 19 | 63,16% | -1,45% | +0,57% | -4,00% | +2,01% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 21 | 66,67% | -1,42% | +1,42% | -3,88% | +2,24% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 17 | 58,82% | -1,13% | +1,13% | -3,57% | +2,84% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 18 | 61,11% | -1,97% | +1,44% | -4,66% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 18 | 66,67% | -1,97% | +1,55% | -4,66% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 18 | 66,67% | -1,97% | +1,55% | -4,66% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 16 | 68,75% | -2,11% | +1,63% | -4,80% | +2,37% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 18 | 66,67% | -1,97% | +1,97% | -4,66% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 16 | 62,50% | -1,54% | +1,54% | -4,33% | +2,91% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 14 | 85,71% | -3,12% | +3,12% | -5,95% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 14 | 85,71% | -3,12% | +3,12% | -5,95% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 14 | 85,71% | -3,12% | +3,12% | -5,95% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 14 | 85,71% | -3,12% | +3,12% | -5,95% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 14 | 85,71% | -3,12% | +3,12% | -5,95% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 13 | 84,62% | -3,01% | +3,01% | -5,82% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 7 | 100,00% | -4,26% | +4,26% | -6,76% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 7 | 100,00% | -4,26% | +4,26% | -6,76% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 7 | 100,00% | -4,26% | +4,26% | -6,76% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 7 | 100,00% | -4,26% | +4,26% | -6,76% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 7 | 100,00% | -4,26% | +4,26% | -6,76% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 6 | 100,00% | -4,06% | +4,06% | -6,55% | +3,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 20 | 50,00% | -0,10% | -0,41% | -0,60% | +0,66% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 23 | 60,87% | -0,48% | -0,10% | -0,92% | +0,22% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 26 | 57,69% | -0,30% | -0,22% | -0,77% | +0,41% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 21 | 52,38% | -0,26% | -0,07% | -0,86% | +0,41% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 27 | 51,85% | -0,18% | +0,04% | -0,66% | +0,51% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 19 | 52,63% | -0,11% | +0,11% | -0,63% | +0,46% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 20 | 40,00% | -0,27% | -0,62% | -0,93% | +0,73% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 22 | 45,45% | -0,62% | -0,41% | -1,34% | +0,21% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 25 | 44,00% | -0,51% | -0,40% | -1,18% | +0,52% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 20 | 40,00% | -0,55% | -0,51% | -1,27% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 26 | 42,31% | -0,39% | -0,05% | -1,04% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 18 | 50,00% | -0,17% | +0,17% | -0,72% | +0,38% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 19 | 36,84% | -0,42% | -0,89% | -2,30% | +1,81% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 21 | 38,10% | -0,91% | -0,54% | -2,74% | +1,39% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 24 | 37,50% | -0,75% | -0,51% | -2,55% | +1,64% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 19 | 36,84% | -0,80% | -0,90% | -2,56% | +1,63% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 25 | 48,00% | -0,66% | +0,19% | -2,40% | +1,72% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 17 | 47,06% | -0,22% | +0,22% | -2,22% | +1,63% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 17 | 41,18% | -0,84% | -1,16% | -3,35% | +2,40% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 19 | 42,11% | -1,30% | -0,92% | -3,76% | +1,93% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 22 | 40,91% | -1,02% | -0,89% | -3,53% | +2,20% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 17 | 35,29% | -1,56% | -1,13% | -3,66% | +2,07% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 23 | 56,52% | -1,08% | +0,37% | -3,49% | +2,26% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 15 | 66,67% | -0,68% | +0,68% | -3,15% | +2,34% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 15 | 46,67% | -1,21% | -0,99% | -4,00% | +2,73% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 17 | 52,94% | -1,86% | -0,51% | -4,44% | +2,19% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 20 | 55,00% | -1,59% | -0,42% | -4,18% | +2,45% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 15 | 40,00% | -1,60% | -1,46% | -4,34% | +2,32% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 21 | 47,62% | -1,49% | +0,52% | -4,14% | +2,50% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 13 | 61,54% | -1,47% | +1,47% | -3,90% | +2,64% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 14 | 42,86% | -1,94% | -0,42% | -4,67% | +2,77% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 14 | 35,71% | -2,24% | -0,69% | -5,21% | +2,47% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 17 | 35,29% | -1,88% | -0,53% | -4,90% | +2,72% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 12 | 16,67% | -1,74% | -2,20% | -5,08% | +2,67% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 18 | 72,22% | -1,96% | +1,69% | -4,89% | +2,77% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 10 | 90,00% | -2,52% | +2,52% | -4,82% | +3,12% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 13 | 61,54% | -3,12% | +0,53% | -5,48% | +2,97% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 10 | 70,00% | -2,98% | +0,77% | -5,81% | +2,48% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 13 | 76,92% | -3,01% | +1,30% | -5,37% | +2,81% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 8 | 12,50% | -2,91% | -2,46% | -5,15% | +2,78% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 14 | 64,29% | -3,08% | +1,63% | -5,48% | +2,86% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 6 | 100,00% | -3,29% | +3,29% | -5,57% | +3,56% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 6 | 50,00% | -4,46% | -1,07% | -7,03% | +2,76% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 5 | 80,00% | -4,77% | +2,87% | -7,28% | +2,28% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 7 | 85,71% | -4,50% | +3,14% | -7,00% | +2,58% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 6 | 33,33% | -4,46% | -1,63% | -7,03% | +2,76% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 7 | 42,86% | -4,50% | -1,38% | -7,00% | +2,58% | FEEDBACK RAPIDO |
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
