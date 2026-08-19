# Accuratezza dati exchange e microstruttura

Generato: 2026-08-19 05:33 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-19 | BTC | 64.333,70 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 9,10 | -1,39% | -1,10% |
| 2026-08-19 | DOGE | 0.06998 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,95 | +3,15% | -0,97% |
| 2026-08-19 | SOL | 76,86 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,89 | +18,37% | +5,45% |
| 2026-08-18 | BTC | 64.191,70 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 4,56 | +0,58% | +0,21% |
| 2026-08-18 | DOGE | 0.06989 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,51 | -1,38% | -3,78% |
| 2026-08-18 | SOL | 75,81 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 2,04 | -3,72% | -7,27% |
| 2026-08-17 | BTC | 63.443,80 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,11 | -0,53% | -3,55% |
| 2026-08-17 | DOGE | 0.07017 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 2,45 | +2,30% | -4,25% |
| 2026-08-17 | SOL | 75,44 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,31 | -4,07% | +1,92% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 2 | +50,00% | +0,20% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 3g | 2 | +0,00% | -1,86% | -2,68% | +1,44% | FEEDBACK RAPIDO |
| SOL | 7g | 2 | +0,00% | -3,56% | -4,18% | +1,44% | FEEDBACK RAPIDO |
| SOL | 14g | 1 | +0,00% | -5,72% | -9,55% | +0,73% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 4 | +50,00% | +1,05% | +0,76% | +2,03% | FEEDBACK RAPIDO |
| DOGE | 3g | 4 | +50,00% | +1,09% | -0,86% | +4,99% | FEEDBACK RAPIDO |
| DOGE | 7g | 4 | +50,00% | +0,28% | -0,90% | +5,64% | FEEDBACK RAPIDO |
| DOGE | 14g | 2 | +50,00% | +0,35% | -1,97% | +6,44% | FEEDBACK RAPIDO |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
