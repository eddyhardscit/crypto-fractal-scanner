# Accuratezza dati exchange e microstruttura

Generato: 2026-08-05 05:15 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-05 | BTC | 64.293,70 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,64 | +3,99% | +3,61% |
| 2026-08-05 | DOGE | 0.06998 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,29 | +2,51% | -5,11% |
| 2026-08-05 | SOL | 74,03 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 3,59 | -1,99% | -0,08% |
| 2026-08-04 | BTC | 63.909,20 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,91 | -2,81% | +1,62% |
| 2026-08-04 | DOGE | 0.07022 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,87 | -1,85% | +0,95% |
| 2026-08-04 | SOL | 73,75 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,29 | +1,23% | -3,33% |
| 2026-08-03 | BTC | 62.770,98 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,51 | -1,33% | +2,59% |
| 2026-08-03 | DOGE | 0.06977 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,27 | -1,69% | -0,89% |
| 2026-08-03 | SOL | 72,88 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,86 | -2,67% | +1,16% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 1 | +0,00% | -0,43% | -0,39% | +0,39% | FEEDBACK RAPIDO |
| SOL | 3g | 1 | +0,00% | -3,12% | -3,63% | +0,73% | FEEDBACK RAPIDO |
| SOL | 7g | 1 | +0,00% | -6,27% | -6,64% | +0,73% | FEEDBACK RAPIDO |
| SOL | 14g | 1 | +0,00% | -5,72% | -9,55% | +0,73% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 2 | +100,00% | +3,08% | +1,70% | +3,12% | FEEDBACK RAPIDO |
| DOGE | 3g | 2 | +100,00% | +2,99% | -0,85% | +6,21% | FEEDBACK RAPIDO |
| DOGE | 7g | 2 | +100,00% | +1,07% | -0,93% | +6,44% | FEEDBACK RAPIDO |
| DOGE | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
