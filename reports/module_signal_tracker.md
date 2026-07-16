# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-16 10:02 UTC

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

Segnali totali salvati: **24**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-16 | BTC | 64.033,70 | -1 | +1 | +1 | +3 | -1 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-07-16 | DOGE | 0.07304 | -6 | -3 | -2 | -3 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-16 | SOL | 76,00 | -6 | -1 | -1 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-15 | BTC | 64.529,99 | +5 | +3 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-15 | DOGE | 0.07394 | -5 | -4 | -3 | -3 | -1 | 0 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-15 | SOL | 77,56 | +2 | +2 | +1 | +2 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-14 | BTC | 62.544,38 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-14 | DOGE | 0.07205 | -5 | -3 | -2 | -3 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-14 | SOL | 74,93 | -1 | 0 | -1 | +1 | -2 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-07-13 | BTC | 62.759,92 | +5 | +4 | +3 | +3 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-13 | DOGE | 0.07220 | -7 | -4 | -3 | -3 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-13 | SOL | 76,37 | -5 | -3 | -2 | -1 | -2 | 0 | 0 | STAI FUORI / VENDI PARZIALE |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 8 | 7 | 6 | 5 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| SOL | 8 | 7 | 6 | 5 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOGE | 8 | 7 | 6 | 5 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-10 | 7g | 2026-07-17 | domani |
| SOL | 2026-07-10 | 7g | 2026-07-17 | domani |
| DOGE | 2026-07-10 | 7g | 2026-07-17 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 7 | 28,57% | +0,00% | +0,00% | FEEDBACK RAPIDO |
| BTC | 2g | 6 | 50,00% | +0,40% | +0,40% | FEEDBACK RAPIDO |
| BTC | 3g | 5 | 60,00% | +0,00% | +0,00% | FEEDBACK RAPIDO |
| BTC | 5g | 3 | 33,33% | -0,02% | -0,02% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | 100,00% | +1,26% | +1,26% | FEEDBACK RAPIDO |
| BTC | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 6 | 33,33% | -0,39% | -0,88% | FEEDBACK RAPIDO |
| SOL | 2g | 5 | 20,00% | -0,23% | -0,62% | FEEDBACK RAPIDO |
| SOL | 3g | 4 | 25,00% | -1,18% | -1,65% | FEEDBACK RAPIDO |
| SOL | 5g | 2 | 0,00% | -3,14% | -3,14% | FEEDBACK RAPIDO |
| SOL | 7g | 1 | 0,00% | -2,59% | -2,59% | FEEDBACK RAPIDO |
| SOL | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 7 | 71,43% | -0,17% | +0,17% | FEEDBACK RAPIDO |
| DOGE | 2g | 6 | 50,00% | +0,07% | -0,07% | FEEDBACK RAPIDO |
| DOGE | 3g | 5 | 60,00% | -0,45% | +0,45% | FEEDBACK RAPIDO |
| DOGE | 5g | 3 | 66,67% | -0,78% | +0,78% | FEEDBACK RAPIDO |
| DOGE | 7g | 1 | 0,00% | +0,26% | -0,26% | FEEDBACK RAPIDO |
| DOGE | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 7 | 28,57% | +0,00% | +0,00% | -0,21% | +0,86% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 7 | 28,57% | +0,00% | +0,00% | -0,21% | +0,86% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 7 | 28,57% | +0,00% | +0,00% | -0,21% | +0,86% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 7 | 28,57% | +0,00% | +0,00% | -0,21% | +0,86% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 6 | 33,33% | -0,04% | -0,88% | -0,28% | +0,94% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 6 | 50,00% | +0,40% | +0,40% | -0,56% | +2,01% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 6 | 50,00% | +0,40% | +0,40% | -0,56% | +2,01% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 6 | 50,00% | +0,40% | +0,40% | -0,56% | +2,01% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | +0,40% | +0,40% | -0,56% | +2,01% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 5 | 40,00% | +0,50% | -0,17% | -0,59% | +2,23% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 5 | 60,00% | +0,00% | +0,00% | -2,03% | +2,03% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 5 | 60,00% | +0,00% | +0,00% | -2,03% | +2,03% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 5 | 60,00% | +0,00% | +0,00% | -2,03% | +2,03% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 5 | 60,00% | +0,00% | +0,00% | -2,03% | +2,03% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 4 | 75,00% | +0,43% | +1,14% | -2,04% | +2,31% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 3 | 33,33% | -0,02% | -0,02% | -3,05% | +2,20% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 3 | 33,33% | -0,02% | -0,02% | -3,05% | +2,20% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 3 | 33,33% | -0,02% | -0,02% | -3,05% | +2,20% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 3 | 33,33% | -0,02% | -0,02% | -3,05% | +2,20% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 2 | 100,00% | -0,55% | +0,55% | -2,93% | +2,27% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 1 | 100,00% | +1,26% | +1,26% | -2,32% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | +1,26% | +1,26% | -2,32% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | +1,26% | +1,26% | -2,32% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 1 | 100,00% | +1,26% | +1,26% | -2,32% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 1 | 0,00% | +1,26% | -1,26% | -2,32% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 7 | 71,43% | -0,17% | +0,17% | -0,57% | +0,74% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 7 | 71,43% | -0,17% | +0,17% | -0,57% | +0,74% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 7 | 71,43% | -0,17% | +0,17% | -0,57% | +0,74% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 7 | 71,43% | -0,17% | +0,17% | -0,57% | +0,74% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 7 | 71,43% | -0,17% | +0,17% | -0,57% | +0,74% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 6 | 66,67% | +0,00% | -0,00% | -0,38% | +0,78% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 6 | 50,00% | +0,07% | -0,07% | -1,03% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 6 | 50,00% | +0,07% | -0,07% | -1,03% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 6 | 50,00% | +0,07% | -0,07% | -1,03% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | +0,07% | -0,07% | -1,03% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 6 | 50,00% | +0,07% | -0,07% | -1,03% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 6 | 50,00% | +0,07% | -0,07% | -1,03% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 5 | 60,00% | -0,45% | +0,45% | -2,22% | +2,64% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 5 | 60,00% | -0,45% | +0,45% | -2,22% | +2,64% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 5 | 60,00% | -0,45% | +0,45% | -2,22% | +2,64% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 5 | 60,00% | -0,45% | +0,45% | -2,22% | +2,64% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 5 | 60,00% | -0,45% | +0,45% | -2,22% | +2,64% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 5 | 60,00% | -0,45% | +0,45% | -2,22% | +2,64% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 3 | 66,67% | -0,78% | +0,78% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 3 | 66,67% | -0,78% | +0,78% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 3 | 66,67% | -0,78% | +0,78% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 3 | 66,67% | -0,78% | +0,78% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 3 | 66,67% | -0,78% | +0,78% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 3 | 66,67% | -0,78% | +0,78% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 1 | 0,00% | +0,26% | -0,26% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 1 | 0,00% | +0,26% | -0,26% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 1 | 0,00% | +0,26% | -0,26% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | +0,26% | -0,26% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 1 | 0,00% | +0,26% | -0,26% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 1 | 0,00% | +0,26% | -0,26% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 6 | 33,33% | -0,39% | -0,88% | -0,92% | +0,68% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 5 | 60,00% | -0,80% | -0,00% | -1,16% | +0,18% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 7 | 57,14% | -0,31% | -0,26% | -0,77% | +0,65% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | -0,39% | +0,29% | -0,92% | +0,68% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 7 | 42,86% | -0,31% | -0,20% | -0,77% | +0,65% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 5 | 20,00% | -0,23% | -0,62% | -1,47% | +2,05% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 4 | 75,00% | -0,58% | +0,58% | -2,02% | +1,53% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 6 | 66,67% | -0,46% | +0,46% | -1,62% | +1,93% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 5 | 40,00% | -0,23% | -0,04% | -1,47% | +2,05% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 6 | 0,00% | -0,46% | -1,45% | -1,62% | +1,93% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 4 | 25,00% | -1,18% | -1,65% | -3,21% | +2,03% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 4 | 75,00% | -0,69% | +0,69% | -2,70% | +2,29% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 5 | 80,00% | -1,29% | +1,29% | -3,09% | +1,89% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 4 | 25,00% | -1,18% | -1,65% | -3,21% | +2,03% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 5 | 40,00% | -1,29% | -1,10% | -3,09% | +1,89% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 2 | 0,00% | -3,14% | -3,14% | -4,81% | +1,67% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -2,07% | +2,07% | -4,75% | +1,64% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | -2,15% | +2,15% | -4,73% | +1,55% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 2 | 0,00% | -3,14% | -3,14% | -4,81% | +1,67% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 3 | 0,00% | -2,15% | -2,15% | -4,73% | +1,55% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | -2,59% | +2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | -2,59% | +2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |

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
