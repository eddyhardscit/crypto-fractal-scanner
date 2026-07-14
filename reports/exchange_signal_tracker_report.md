# Accuratezza dati exchange e microstruttura

Generato: 2026-07-14 21:57 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **0**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-14 | BTC | 62.725,40 | V2.1.3 | OK | 0 | 0 | -1,25 | BASSA | 0,47 | n/a | -2,39% |
| 2026-07-14 | DOGE | 0.07231 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,24 | n/a | -3,14% |
| 2026-07-14 | SOL | 75,25 | V2.1.3 | OK | 0 | 0 | 1,25 | BASSA | 4,05 | n/a | +0,77% |
| 2026-07-13 | BTC | 62.838,58 | V2.1.3 | OK | 0 | 0 | 1,38 | BASSA | 2,14 | n/a | -6,30% |
| 2026-07-13 | DOGE | 0.07198 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,86 | n/a | -3,33% |
| 2026-07-13 | SOL | 75,84 | V2.1.3 | OK | 0 | 0 | 1,50 | BASSA | 1,09 | n/a | -7,85% |
| 2026-07-12 | BTC | 63.743,50 | V2.1.3 | OK | 0 | 0 | 1,38 | BASSA | 1,82 | n/a | -6,53% |
| 2026-07-12 | DOGE | 0.07276 | V2.1.3 | OK | 0 | 0 | 1,38 | BASSA | 1,82 | n/a | -7,68% |
| 2026-07-12 | SOL | 76,17 | V2.1.3 | OK | 0 | 0 | 0,00 | BASSA | 3,31 | n/a | -21,30% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 3g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 3g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 3g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
