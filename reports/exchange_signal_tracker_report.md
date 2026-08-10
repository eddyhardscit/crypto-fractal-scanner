# Accuratezza dati exchange e microstruttura

Generato: 2026-08-10 05:17 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-10 | BTC | 65.017,50 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,64 | +1,08% | -4,44% |
| 2026-08-10 | DOGE | 0.06975 | V2.1.3 | OK | 0 | 0 | 2,62 | MEDIA | 1,96 | +1,46% | +15,23% |
| 2026-08-10 | SOL | 76,63 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,26 | -0,14% | -8,62% |
| 2026-08-09 | BTC | 64.760,07 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,35 | -0,59% | +1,41% |
| 2026-08-09 | DOGE | 0.07000 | V2.1.3 | OK | 1 | 0 | 2,62 | MEDIA | 1,41 | -2,68% | +10,90% |
| 2026-08-09 | SOL | 75,97 | V2.1.3 | OK | 1 | 0 | 3,25 | MEDIA | 1,61 | +6,67% | +10,58% |
| 2026-08-08 | BTC | 64.976,10 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,90 | +1,69% | +0,05% |
| 2026-08-08 | DOGE | 0.07009 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,17 | -0,78% | +0,58% |
| 2026-08-08 | SOL | 74,56 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,90 | -0,99% | -2,67% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 2 | +50,00% | +0,20% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 3g | 1 | +0,00% | -3,12% | -3,63% | +0,73% | FEEDBACK RAPIDO |
| SOL | 7g | 1 | +0,00% | -6,27% | -6,64% | +0,73% | FEEDBACK RAPIDO |
| SOL | 14g | 1 | +0,00% | -5,72% | -9,55% | +0,73% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 4 | +50,00% | +1,05% | +0,76% | +2,03% | FEEDBACK RAPIDO |
| DOGE | 3g | 3 | +66,67% | +1,64% | -0,64% | +5,29% | FEEDBACK RAPIDO |
| DOGE | 7g | 2 | +100,00% | +1,07% | -0,93% | +6,44% | FEEDBACK RAPIDO |
| DOGE | 14g | 2 | +50,00% | +0,35% | -1,97% | +6,44% | FEEDBACK RAPIDO |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
