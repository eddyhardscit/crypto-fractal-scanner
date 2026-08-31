# Accuratezza dati exchange e microstruttura

Generato: 2026-08-31 05:33 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-31 | BTC | 77.627,40 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 2,70 | -5,61% | -4,10% |
| 2026-08-31 | DOGE | 0.08216 | V2.1.3 | OK | 0 | 0 | 2,50 | BASSA | 1,51 | -6,45% | -4,98% |
| 2026-08-31 | SOL | 101,54 | V2.1.3 | OK | 0 | 0 | 1,75 | MEDIA | 1,62 | -9,59% | -10,08% |
| 2026-08-30 | BTC | 78.141,70 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 2,07 | +0,16% | +4,74% |
| 2026-08-30 | DOGE | 0.08503 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,37 | +0,84% | +2,87% |
| 2026-08-30 | SOL | 105,13 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,81 | +1,51% | -0,93% |
| 2026-08-29 | BTC | 77.633,28 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 3,42 | -1,02% | -3,05% |
| 2026-08-29 | DOGE | 0.08517 | V2.1.3 | OK | 1 | 0 | 2,75 | MEDIA | 2,27 | -4,61% | -0,37% |
| 2026-08-29 | SOL | 103,95 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 2,65 | +0,10% | -4,17% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 3 | +66,67% | +0,12% | -0,41% | +0,59% | FEEDBACK RAPIDO |
| BTC | 3g | 3 | +66,67% | +1,27% | -1,97% | +3,06% | FEEDBACK RAPIDO |
| BTC | 7g | 2 | +100,00% | +1,71% | -1,21% | +4,96% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 3 | +33,33% | +4,01% | -3,47% | +8,64% | FEEDBACK RAPIDO |
| SOL | 14g | 2 | +50,00% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 30g | 1 | +100,00% | +8,60% | -9,55% | +9,55% | FEEDBACK RAPIDO |
| DOGE | 1g | 8 | +50,00% | +0,90% | -0,21% | +1,91% | FEEDBACK RAPIDO |
| DOGE | 3g | 7 | +42,86% | +1,91% | -3,12% | +7,00% | FEEDBACK RAPIDO |
| DOGE | 7g | 7 | +42,86% | -1,02% | -4,29% | +8,47% | FEEDBACK RAPIDO |
| DOGE | 14g | 4 | +50,00% | +2,59% | -1,41% | +16,82% | FEEDBACK RAPIDO |
| DOGE | 30g | 2 | +100,00% | +31,38% | -1,97% | +40,03% | FEEDBACK RAPIDO |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
