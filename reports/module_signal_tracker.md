# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-14 09:34 UTC

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

Segnali totali salvati: **18**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-14 | BTC | 62.544,38 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-14 | DOGE | 0.07205 | -5 | -3 | -2 | -3 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-14 | SOL | 74,93 | -1 | 0 | -1 | +1 | -2 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-07-13 | BTC | 62.759,92 | +5 | +4 | +3 | +3 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-13 | DOGE | 0.07220 | -7 | -4 | -3 | -3 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-13 | SOL | 76,37 | -5 | -3 | -2 | -1 | -2 | 0 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-12 | BTC | 63.818,10 | +5 | +4 | +3 | +3 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-12 | DOGE | 0.07283 | -7 | -4 | -3 | -3 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-12 | SOL | 76,48 | -2 | -2 | -1 | -1 | +1 | 0 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-07-11 | BTC | 64.040,99 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-11 | DOGE | 0.07401 | -8 | -4 | -3 | -3 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-11 | SOL | 77,80 | +1 | 0 | -1 | +1 | +1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 6 | 5 | 4 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| SOL | 6 | 5 | 4 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOGE | 6 | 5 | 4 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-10 | 5g | 2026-07-15 | domani |
| SOL | 2026-07-10 | 5g | 2026-07-15 | domani |
| DOGE | 2026-07-10 | 5g | 2026-07-15 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 5 | 20,00% | -0,48% | -0,48% | FEEDBACK RAPIDO |
| BTC | 2g | 4 | 25,00% | -0,70% | -0,70% | FEEDBACK RAPIDO |
| BTC | 3g | 3 | 33,33% | -1,05% | -1,05% | FEEDBACK RAPIDO |
| BTC | 5g | 1 | 0,00% | -1,09% | -1,09% | FEEDBACK RAPIDO |
| BTC | 7g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 4 | 50,00% | -0,96% | +0,06% | FEEDBACK RAPIDO |
| SOL | 2g | 3 | 33,33% | -1,38% | -0,03% | FEEDBACK RAPIDO |
| SOL | 3g | 2 | 0,00% | -2,83% | -2,83% | FEEDBACK RAPIDO |
| SOL | 5g | 1 | 0,00% | -3,96% | -3,96% | FEEDBACK RAPIDO |
| SOL | 7g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 5 | 80,00% | -0,52% | +0,52% | FEEDBACK RAPIDO |
| DOGE | 2g | 4 | 75,00% | -0,84% | +0,84% | FEEDBACK RAPIDO |
| DOGE | 3g | 3 | 100,00% | -1,65% | +1,65% | FEEDBACK RAPIDO |
| DOGE | 5g | 1 | 100,00% | -1,10% | +1,10% | FEEDBACK RAPIDO |
| DOGE | 7g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 5 | 20,00% | -0,48% | -0,48% | -0,70% | +0,25% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 5 | 20,00% | -0,48% | -0,48% | -0,70% | +0,25% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 5 | 20,00% | -0,48% | -0,48% | -0,70% | +0,25% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 5 | 20,00% | -0,48% | -0,48% | -0,70% | +0,25% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 4 | 50,00% | -0,67% | -0,34% | -0,93% | +0,21% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 4 | 25,00% | -0,70% | -0,70% | -1,15% | +0,87% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 4 | 25,00% | -0,70% | -0,70% | -1,15% | +0,87% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 4 | 25,00% | -0,70% | -0,70% | -1,15% | +0,87% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 4 | 25,00% | -0,70% | -0,70% | -1,15% | +0,87% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 3 | 33,33% | -0,91% | -0,42% | -1,42% | +0,85% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 3 | 33,33% | -1,05% | -1,05% | -2,02% | +1,21% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 3 | 33,33% | -1,05% | -1,05% | -2,02% | +1,21% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 3 | 33,33% | -1,05% | -1,05% | -2,02% | +1,21% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 3 | 33,33% | -1,05% | -1,05% | -2,02% | +1,21% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 2 | 50,00% | -0,71% | +0,71% | -2,04% | +1,36% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 1 | 0,00% | -1,09% | -1,09% | -2,32% | +2,25% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 1 | 0,00% | -1,09% | -1,09% | -2,32% | +2,25% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 1 | 0,00% | -1,09% | -1,09% | -2,32% | +2,25% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | -1,09% | -1,09% | -2,32% | +2,25% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 1 | 100,00% | -1,09% | +1,09% | -2,32% | +2,25% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 5 | 80,00% | -0,52% | +0,52% | -0,91% | +0,20% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 5 | 80,00% | -0,52% | +0,52% | -0,91% | +0,20% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 5 | 80,00% | -0,52% | +0,52% | -0,91% | +0,20% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 5 | 80,00% | -0,52% | +0,52% | -0,91% | +0,20% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 5 | 80,00% | -0,52% | +0,52% | -0,91% | +0,20% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 5 | 80,00% | -0,52% | +0,52% | -0,91% | +0,20% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 4 | 75,00% | -0,84% | +0,84% | -1,49% | +1,27% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 4 | 75,00% | -0,84% | +0,84% | -1,49% | +1,27% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 4 | 75,00% | -0,84% | +0,84% | -1,49% | +1,27% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 4 | 75,00% | -0,84% | +0,84% | -1,49% | +1,27% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 4 | 75,00% | -0,84% | +0,84% | -1,49% | +1,27% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 4 | 75,00% | -0,84% | +0,84% | -1,49% | +1,27% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 3 | 100,00% | -1,65% | +1,65% | -2,48% | +1,88% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | -1,65% | +1,65% | -2,48% | +1,88% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | -1,65% | +1,65% | -2,48% | +1,88% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 3 | 100,00% | -1,65% | +1,65% | -2,48% | +1,88% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 3 | 100,00% | -1,65% | +1,65% | -2,48% | +1,88% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 3 | 100,00% | -1,65% | +1,65% | -2,48% | +1,88% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 1 | 100,00% | -1,10% | +1,10% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | -1,10% | +1,10% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | -1,10% | +1,10% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 1 | 100,00% | -1,10% | +1,10% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 1 | 100,00% | -1,10% | +1,10% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 1 | 100,00% | -1,10% | +1,10% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 4 | 50,00% | -0,96% | +0,06% | -1,52% | -0,11% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 4 | 75,00% | -0,50% | +0,50% | -0,88% | +0,27% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 5 | 80,00% | -0,74% | +0,74% | -1,20% | +0,01% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 4 | 50,00% | -0,96% | +0,06% | -1,52% | -0,11% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 5 | 40,00% | -0,74% | +0,01% | -1,20% | +0,01% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 3 | 33,33% | -1,38% | -0,03% | -2,03% | +0,75% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | -1,29% | +1,29% | -1,89% | +1,13% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | -1,43% | +1,43% | -2,11% | +0,89% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 3 | 33,33% | -1,38% | -0,03% | -2,03% | +0,75% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 4 | 0,00% | -1,43% | -1,43% | -2,11% | +0,89% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 2 | 0,00% | -2,83% | -2,83% | -3,71% | +1,12% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -1,84% | +1,84% | -2,69% | +1,64% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | -2,46% | +2,46% | -3,35% | +1,19% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 2 | 0,00% | -2,83% | -2,83% | -3,71% | +1,12% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 3 | 0,00% | -2,46% | -2,46% | -3,35% | +1,19% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | -3,96% | +3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | -3,96% | +3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |

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
