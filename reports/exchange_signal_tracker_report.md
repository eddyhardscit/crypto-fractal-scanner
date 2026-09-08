# Accuratezza dati exchange e microstruttura

Generato: 2026-09-08 05:33 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-08 | BTC | 78.728,60 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,33 | +0,59% | -1,63% |
| 2026-09-08 | DOGE | 0.08985 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,16 | -2,94% | +1,74% |
| 2026-09-08 | SOL | 103,18 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,63 | -2,35% | -2,79% |
| 2026-09-07 | BTC | 79.707,00 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,26 | -1,97% | +0,37% |
| 2026-09-07 | DOGE | 0.08993 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,78 | -5,60% | +5,30% |
| 2026-09-07 | SOL | 105,30 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,80 | -0,56% | +4,43% |
| 2026-09-06 | BTC | 79.834,20 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 2,30 | +0,27% | +2,73% |
| 2026-09-06 | DOGE | 0.09052 | V2.1.3 | OK | 1 | 0 | 2,75 | MEDIA | 1,44 | +5,09% | +0,28% |
| 2026-09-06 | SOL | 105,78 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 5,08 | +0,13% | +3,11% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 5 | +40,00% | -0,26% | -0,89% | +0,60% | FEEDBACK RAPIDO |
| BTC | 3g | 4 | +50,00% | +0,59% | -2,21% | +2,43% | FEEDBACK RAPIDO |
| BTC | 7g | 3 | +66,67% | +0,53% | -2,29% | +3,66% | FEEDBACK RAPIDO |
| BTC | 14g | 3 | +33,33% | -0,17% | -3,31% | +4,48% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 4 | +75,00% | +8,51% | -5,12% | +14,70% | FEEDBACK RAPIDO |
| SOL | 30g | 2 | +100,00% | +22,28% | -5,94% | +27,20% | FEEDBACK RAPIDO |
| DOGE | 1g | 9 | +44,44% | +0,77% | -0,33% | +1,78% | FEEDBACK RAPIDO |
| DOGE | 3g | 8 | +37,50% | +1,43% | -3,31% | +6,31% | FEEDBACK RAPIDO |
| DOGE | 7g | 8 | +50,00% | -0,83% | -4,47% | +8,09% | FEEDBACK RAPIDO |
| DOGE | 14g | 7 | +42,86% | +0,79% | -5,33% | +14,98% | FEEDBACK RAPIDO |
| DOGE | 30g | 4 | +75,00% | +14,93% | -1,41% | +41,94% | FEEDBACK RAPIDO |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
