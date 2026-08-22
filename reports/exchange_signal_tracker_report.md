# Accuratezza dati exchange e microstruttura

Generato: 2026-08-22 05:32 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-22 | BTC | 78.429,65 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 3,22 | +0,83% | +1,96% |
| 2026-08-22 | DOGE | 0.09866 | V2.1.3 | OK | 1 | 0 | 3,00 | MEDIA | 1,28 | +14,08% | -2,18% |
| 2026-08-22 | SOL | 99,08 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,82 | +2,53% | -4,64% |
| 2026-08-21 | BTC | 75.096,70 | V2.1.3 | OK | 0 | 0 | 0,25 | BASSA | 1,07 | -3,95% | -2,94% |
| 2026-08-21 | DOGE | 0.08238 | V2.1.3 | OK | 0 | 0 | 3,50 | ALTA | 1,46 | +11,21% | -0,84% |
| 2026-08-21 | SOL | 89,44 | V2.1.3 | OK | 1 | 0 | 3,25 | ALTA | 1,57 | +8,30% | -6,87% |
| 2026-08-20 | BTC | 69.515,36 | V2.1.3 | OK | 0 | 0 | 2,25 | ALTA | 1,03 | +8,86% | +1,47% |
| 2026-08-20 | DOGE | 0.07482 | V2.1.3 | OK | 1 | 0 | 3,25 | ALTA | 1,31 | +2,01% | +4,59% |
| 2026-08-20 | SOL | 84,87 | V2.1.3 | OK | 0 | 0 | 2,00 | MEDIA | 1,16 | -13,35% | +3,32% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 3 | +66,67% | +1,62% | +1,05% | +5,09% | FEEDBACK RAPIDO |
| SOL | 3g | 2 | +0,00% | -1,86% | -2,68% | +1,44% | FEEDBACK RAPIDO |
| SOL | 7g | 2 | +0,00% | -3,56% | -4,18% | +1,44% | FEEDBACK RAPIDO |
| SOL | 14g | 1 | +0,00% | -5,72% | -9,55% | +0,73% | FEEDBACK RAPIDO |
| SOL | 30g | 1 | +100,00% | +8,60% | -9,55% | +9,55% | FEEDBACK RAPIDO |
| DOGE | 1g | 5 | +60,00% | +2,90% | +2,11% | +3,72% | FEEDBACK RAPIDO |
| DOGE | 3g | 4 | +50,00% | +1,09% | -0,86% | +4,99% | FEEDBACK RAPIDO |
| DOGE | 7g | 4 | +50,00% | +0,28% | -0,90% | +5,64% | FEEDBACK RAPIDO |
| DOGE | 14g | 3 | +33,33% | -6,28% | -1,38% | +10,89% | FEEDBACK RAPIDO |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
