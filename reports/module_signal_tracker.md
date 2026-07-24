# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-24 05:15 UTC

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

Segnali totali salvati: **48**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-24 | BTC | 65.302,77 | 0 | +2 | +2 | +3 | -2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-24 | DOGE | 0.06902 | -5 | -1 | -1 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-24 | SOL | 75,72 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-23 | BTC | 65.399,99 | +1 | +2 | +2 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-23 | DOGE | 0.07229 | -3 | -1 | -1 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-07-23 | SOL | 77,14 | +1 | +3 | +2 | +2 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-22 | BTC | 66.234,10 | +2 | +2 | +2 | 0 | 0 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-22 | DOGE | 0.07318 | -5 | -2 | -1 | -1 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-22 | SOL | 77,82 | -3 | -1 | -1 | 0 | -1 | -1 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-07-21 | BTC | 65.476,52 | +3 | +2 | +2 | 0 | 0 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-21 | DOGE | 0.07281 | -6 | -3 | -2 | -2 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-21 | SOL | 78,22 | +1 | +2 | +1 | +2 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 16 | 15 | 14 | 13 | 11 | 9 | 6 | 2 | 0 | 0 | 0 | 0 |
| SOL | 16 | 15 | 14 | 13 | 11 | 9 | 6 | 2 | 0 | 0 | 0 | 0 |
| DOGE | 16 | 15 | 14 | 13 | 11 | 9 | 6 | 2 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-11 | 14g | 2026-07-25 | domani |
| SOL | 2026-07-11 | 14g | 2026-07-25 | domani |
| DOGE | 2026-07-11 | 14g | 2026-07-25 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 14 | 35,71% | +0,05% | +0,08% | FEEDBACK RAPIDO |
| BTC | 2g | 13 | 46,15% | +0,41% | +0,18% | FEEDBACK RAPIDO |
| BTC | 3g | 12 | 50,00% | +0,55% | +0,22% | FEEDBACK RAPIDO |
| BTC | 5g | 10 | 40,00% | +1,16% | -0,10% | FEEDBACK RAPIDO |
| BTC | 7g | 9 | 55,56% | +1,83% | +0,78% | FEEDBACK RAPIDO |
| BTC | 10g | 6 | 100,00% | +2,93% | +2,93% | FEEDBACK RAPIDO |
| BTC | 14g | 2 | 100,00% | +2,84% | +2,84% | FEEDBACK RAPIDO |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 14 | 42,86% | -0,19% | -0,69% | FEEDBACK RAPIDO |
| SOL | 2g | 13 | 23,08% | -0,14% | -0,88% | FEEDBACK RAPIDO |
| SOL | 3g | 12 | 8,33% | -0,13% | -1,91% | FEEDBACK RAPIDO |
| SOL | 5g | 10 | 30,00% | -0,14% | -1,51% | FEEDBACK RAPIDO |
| SOL | 7g | 8 | 37,50% | -0,04% | -1,45% | FEEDBACK RAPIDO |
| SOL | 10g | 5 | 20,00% | +0,36% | -1,16% | FEEDBACK RAPIDO |
| SOL | 14g | 1 | 0,00% | -1,13% | -1,13% | FEEDBACK RAPIDO |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 15 | 60,00% | -0,45% | +0,45% | FEEDBACK RAPIDO |
| DOGE | 2g | 14 | 57,14% | -0,52% | +0,52% | FEEDBACK RAPIDO |
| DOGE | 3g | 13 | 53,85% | -0,65% | +0,65% | FEEDBACK RAPIDO |
| DOGE | 5g | 11 | 63,64% | -0,83% | +0,83% | FEEDBACK RAPIDO |
| DOGE | 7g | 9 | 77,78% | -1,20% | +1,20% | FEEDBACK RAPIDO |
| DOGE | 10g | 6 | 66,67% | -1,44% | +1,44% | FEEDBACK RAPIDO |
| DOGE | 14g | 2 | 100,00% | -3,67% | +3,67% | FEEDBACK RAPIDO |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 14 | 35,71% | +0,05% | +0,08% | -0,17% | +0,76% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 15 | 40,00% | +0,14% | +0,14% | -0,09% | +0,81% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 15 | 40,00% | +0,14% | +0,14% | -0,09% | +0,81% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 11 | 36,36% | +0,09% | +0,09% | -0,14% | +0,70% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 12 | 33,33% | +0,15% | -0,76% | -0,10% | +0,83% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 13 | 46,15% | +0,41% | +0,18% | -0,16% | +1,43% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 14 | 50,00% | +0,41% | +0,41% | -0,13% | +1,45% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 14 | 50,00% | +0,41% | +0,41% | -0,13% | +1,45% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 10 | 50,00% | +0,30% | +0,30% | -0,30% | +1,45% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 11 | 36,36% | +0,67% | -0,57% | +0,09% | +1,71% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 12 | 50,00% | +0,55% | +0,22% | -1,08% | +2,33% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 13 | 69,23% | +0,70% | +0,70% | -0,95% | +2,37% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 13 | 69,23% | +0,70% | +0,70% | -0,95% | +2,37% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 10 | 70,00% | +0,52% | +0,52% | -1,11% | +2,17% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 11 | 36,36% | +1,01% | -0,21% | -0,84% | +2,54% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 10 | 40,00% | +1,16% | -0,10% | -2,04% | +2,97% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 11 | 63,64% | +1,27% | +1,27% | -1,87% | +3,13% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 11 | 63,64% | +1,27% | +1,27% | -1,87% | +3,13% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +1,32% | +1,32% | -1,90% | +3,11% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 10 | 40,00% | +1,30% | -0,93% | -1,73% | +3,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 9 | 55,56% | +1,83% | +0,78% | -2,09% | +3,71% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 9 | 77,78% | +1,83% | +1,83% | -2,09% | +3,71% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 9 | 77,78% | +1,83% | +1,83% | -2,09% | +3,71% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 9 | 77,78% | +1,83% | +1,83% | -2,09% | +3,71% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 8 | 50,00% | +2,10% | -0,51% | -1,94% | +3,85% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 6 | 100,00% | +2,93% | +2,93% | -2,22% | +4,46% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 6 | 100,00% | +2,93% | +2,93% | -2,22% | +4,46% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 6 | 100,00% | +2,93% | +2,93% | -2,22% | +4,46% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 6 | 100,00% | +2,93% | +2,93% | -2,22% | +4,46% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 5 | 40,00% | +3,41% | -0,21% | -2,01% | +4,83% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 2 | 100,00% | +2,84% | +2,84% | -2,80% | +5,29% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | +2,84% | +2,84% | -2,80% | +5,29% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | +2,84% | +2,84% | -2,80% | +5,29% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 2 | 100,00% | +2,84% | +2,84% | -2,80% | +5,29% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 1 | 0,00% | +3,42% | -3,42% | -2,32% | +5,81% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 15 | 60,00% | -0,45% | +0,45% | -0,73% | +0,32% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 15 | 60,00% | -0,45% | +0,45% | -0,73% | +0,32% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 15 | 60,00% | -0,45% | +0,45% | -0,73% | +0,32% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | -0,16% | +0,16% | -0,44% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 15 | 60,00% | -0,45% | +0,45% | -0,73% | +0,32% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 14 | 57,14% | -0,39% | +0,39% | -0,66% | +0,31% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 14 | 57,14% | -0,52% | +0,52% | -1,09% | +0,85% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 14 | 57,14% | -0,52% | +0,52% | -1,09% | +0,85% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 14 | 57,14% | -0,52% | +0,52% | -1,09% | +0,85% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | -0,52% | +0,52% | -1,09% | +0,85% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 14 | 57,14% | -0,52% | +0,52% | -1,09% | +0,85% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 13 | 53,85% | -0,37% | +0,37% | -1,00% | +1,08% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 13 | 53,85% | -0,65% | +0,65% | -1,83% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 13 | 53,85% | -0,65% | +0,65% | -1,83% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 13 | 53,85% | -0,65% | +0,65% | -1,83% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 13 | 53,85% | -0,65% | +0,65% | -1,83% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 13 | 53,85% | -0,65% | +0,65% | -1,83% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 12 | 50,00% | -0,52% | +0,52% | -1,78% | +2,06% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 11 | 63,64% | -0,83% | +0,83% | -2,72% | +2,32% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 11 | 63,64% | -0,83% | +0,83% | -2,72% | +2,32% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 11 | 63,64% | -0,83% | +0,83% | -2,72% | +2,32% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 11 | 63,64% | -0,83% | +0,83% | -2,72% | +2,32% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 11 | 63,64% | -0,83% | +0,83% | -2,72% | +2,32% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 10 | 60,00% | -0,62% | +0,62% | -2,60% | +2,50% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 9 | 77,78% | -1,20% | +1,20% | -3,03% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 9 | 77,78% | -1,20% | +1,20% | -3,03% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 9 | 77,78% | -1,20% | +1,20% | -3,03% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 9 | 77,78% | -1,20% | +1,20% | -3,03% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 9 | 77,78% | -1,20% | +1,20% | -3,03% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 8 | 75,00% | -1,22% | +1,22% | -2,92% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 6 | 66,67% | -1,44% | +1,44% | -3,19% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 6 | 66,67% | -1,44% | +1,44% | -3,19% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 6 | 66,67% | -1,44% | +1,44% | -3,19% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 6 | 66,67% | -1,44% | +1,44% | -3,19% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 6 | 66,67% | -1,44% | +1,44% | -3,19% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 6 | 66,67% | -1,44% | +1,44% | -3,19% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 2 | 100,00% | -3,67% | +3,67% | -4,69% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -3,67% | +3,67% | -4,69% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | -3,67% | +3,67% | -4,69% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 2 | 100,00% | -3,67% | +3,67% | -4,69% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 2 | 100,00% | -3,67% | +3,67% | -4,69% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 2 | 100,00% | -3,67% | +3,67% | -4,69% | +2,87% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 14 | 42,86% | -0,19% | -0,69% | -0,54% | +0,67% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 11 | 63,64% | -0,79% | -0,00% | -0,98% | +0,11% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 14 | 57,14% | -0,39% | -0,24% | -0,69% | +0,48% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 9 | 44,44% | -0,36% | +0,10% | -0,85% | +0,53% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 15 | 60,00% | -0,17% | -0,08% | -0,50% | +0,66% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 7 | 71,43% | +0,03% | -0,03% | -0,23% | +0,72% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 13 | 23,08% | -0,14% | -0,88% | -0,77% | +1,19% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 10 | 50,00% | -0,69% | -0,22% | -1,46% | +0,53% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 13 | 46,15% | -0,45% | -0,25% | -1,14% | +1,05% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 8 | 37,50% | -0,53% | -0,42% | -1,31% | +1,35% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 14 | 28,57% | -0,25% | -0,57% | -0,88% | +1,20% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 6 | 33,33% | +0,64% | -0,64% | +0,32% | +1,26% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 12 | 8,33% | -0,13% | -1,91% | -1,86% | +2,36% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 9 | 33,33% | -0,64% | -0,82% | -2,52% | +1,76% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 12 | 33,33% | -0,40% | -0,70% | -2,19% | +2,17% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 8 | 37,50% | -0,84% | -1,07% | -2,35% | +2,30% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 13 | 30,77% | -0,26% | -0,66% | -1,92% | +2,27% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 5 | 0,00% | +1,89% | -1,89% | -0,57% | +2,88% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 10 | 30,00% | -0,14% | -1,51% | -2,69% | +3,10% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 8 | 62,50% | -0,46% | -0,04% | -3,18% | +2,58% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 11 | 54,55% | -0,14% | -0,22% | -2,86% | +2,94% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -1,07% | -0,02% | -3,11% | +2,85% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 11 | 27,27% | -0,14% | -1,35% | -2,86% | +2,94% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 4 | 25,00% | +2,26% | -2,26% | -1,12% | +4,04% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 8 | 37,50% | -0,04% | -1,45% | -3,64% | +3,07% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 7 | 71,43% | -0,62% | +0,71% | -3,85% | +2,78% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 9 | 66,67% | -0,40% | +0,48% | -3,74% | +2,90% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 6 | 66,67% | -0,43% | -0,08% | -4,16% | +2,70% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 9 | 11,11% | -0,40% | -1,86% | -3,74% | +2,90% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 2 | 0,00% | +1,16% | -1,16% | -2,09% | +4,20% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 5 | 20,00% | +0,36% | -1,16% | -4,30% | +3,01% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 4 | 50,00% | -0,49% | +0,49% | -4,84% | +2,47% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 6 | 33,33% | -0,06% | +0,06% | -4,51% | +2,76% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 5 | 40,00% | +0,36% | -0,74% | -4,30% | +3,01% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 6 | 33,33% | -0,06% | -0,75% | -4,51% | +2,76% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -1,84% | +1,84% | -5,73% | +1,74% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | -1,84% | +1,84% | -5,73% | +1,74% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 2 | 0,00% | -1,84% | -1,84% | -5,73% | +1,74% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |

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
