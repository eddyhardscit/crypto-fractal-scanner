# Accuratezza dati exchange e microstruttura

Generato: 2026-07-21 05:14 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **9**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-21 | BTC | 65.482,28 | V2.1.3 | OK | 0 | 0 | 3,50 | ALTA | 1,98 | +2,64% | +0,77% |
| 2026-07-21 | DOGE | 0.07279 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,70 | -1,89% | -0,20% |
| 2026-07-21 | SOL | 78,16 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 3,05 | +1,19% | +3,26% |
| 2026-07-20 | BTC | 64.448,63 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 1,39 | +1,07% | +4,99% |
| 2026-07-20 | DOGE | 0.07216 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,86 | +4,68% | -1,67% |
| 2026-07-20 | SOL | 76,36 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,95 | +0,11% | -2,20% |
| 2026-07-19 | BTC | 64.720,62 | V2.1.3 | OK | 0 | 0 | -0,50 | BASSA | 0,79 | -6,65% | -0,41% |
| 2026-07-19 | DOGE | 0.07239 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 4,21 | +2,17% | -2,34% |
| 2026-07-19 | SOL | 75,98 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,74 | -4,40% | +0,28% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
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
