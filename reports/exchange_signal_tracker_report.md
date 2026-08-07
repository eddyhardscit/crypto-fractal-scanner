# Accuratezza dati exchange e microstruttura

Generato: 2026-08-07 05:16 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-07 | BTC | 64.171,90 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,41 | -1,39% | -3,15% |
| 2026-08-07 | DOGE | 0.06902 | V2.1.3 | OK | -1 | 0 | -2,75 | ALTA | 0,85 | +4,00% | -14,43% |
| 2026-08-07 | SOL | 72,63 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,37 | +5,14% | -0,85% |
| 2026-08-06 | BTC | 64.854,80 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 2,10 | +0,56% | +1,52% |
| 2026-08-06 | DOGE | 0.06996 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,34 | +4,90% | -1,75% |
| 2026-08-06 | SOL | 74,10 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 4,09 | -1,98% | +5,13% |
| 2026-08-05 | BTC | 64.293,70 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,64 | +3,99% | +3,61% |
| 2026-08-05 | DOGE | 0.06998 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,29 | +2,51% | -5,11% |
| 2026-08-05 | SOL | 74,03 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 3,59 | -1,99% | -0,08% |

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
| DOGE | 14g | 1 | +0,00% | -0,03% | -1,56% | +6,88% | FEEDBACK RAPIDO |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
