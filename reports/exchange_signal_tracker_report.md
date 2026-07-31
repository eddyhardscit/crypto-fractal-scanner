# Accuratezza dati exchange e microstruttura

Generato: 2026-07-31 05:15 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-31 | BTC | 64.338,30 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,00 | +0,68% | +5,43% |
| 2026-07-31 | DOGE | 0.07013 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,11 | +1,78% | +2,76% |
| 2026-07-31 | SOL | 74,01 | V2.1.3 | OK | 0 | 0 | 0,00 | BASSA | 1,04 | +2,11% | +4,14% |
| 2026-07-30 | BTC | 63.972,87 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,65 | -2,61% | +5,28% |
| 2026-07-30 | DOGE | 0.06970 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,34 | -2,17% | -2,67% |
| 2026-07-30 | SOL | 73,50 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 2,18 | -2,19% | +0,21% |
| 2026-07-29 | BTC | 63.939,70 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,94 | -1,46% | +5,06% |
| 2026-07-29 | DOGE | 0.07058 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 2,01 | -0,21% | +3,11% |
| 2026-07-29 | SOL | 73,46 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 2,01 | +1,25% | +1,41% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 1 | +0,00% | -0,43% | -0,39% | +0,39% | FEEDBACK RAPIDO |
| SOL | 3g | 1 | +0,00% | -3,12% | -3,63% | +0,73% | FEEDBACK RAPIDO |
| SOL | 7g | 1 | +0,00% | -6,27% | -6,64% | +0,73% | FEEDBACK RAPIDO |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 2 | +100,00% | +3,08% | +1,70% | +3,12% | FEEDBACK RAPIDO |
| DOGE | 3g | 2 | +100,00% | +2,99% | -0,85% | +6,21% | FEEDBACK RAPIDO |
| DOGE | 7g | 1 | +100,00% | +1,46% | -1,10% | +6,88% | FEEDBACK RAPIDO |
| DOGE | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
