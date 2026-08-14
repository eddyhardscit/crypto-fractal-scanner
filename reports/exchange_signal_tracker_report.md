# Accuratezza dati exchange e microstruttura

Generato: 2026-08-14 10:53 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **39**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-14 | BTC | 62.903,40 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 2,18 | +7,44% | -1,76% |
| 2026-08-14 | DOGE | 0.06947 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,19 | +2,93% | +3,02% |
| 2026-08-14 | SOL | 75,51 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 2,59 | +1,63% | -3,11% |
| 2026-08-11 | BTC | 64.025,10 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,94 | +4,21% | -7,22% |
| 2026-08-11 | DOGE | 0.07002 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,86 | +1,22% | +10,68% |
| 2026-08-11 | SOL | 76,02 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,13 | +0,02% | +4,16% |
| 2026-08-10 | BTC | 65.017,50 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,64 | +1,08% | -4,44% |
| 2026-08-10 | DOGE | 0.06975 | V2.1.3 | OK | 0 | 0 | 2,62 | MEDIA | 1,96 | +1,46% | +15,23% |
| 2026-08-10 | SOL | 76,63 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,26 | -0,14% | -8,62% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 2 | +50,00% | +0,20% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 3g | 2 | +0,00% | -1,86% | -2,68% | +1,44% | FEEDBACK RAPIDO |
| SOL | 7g | 1 | +0,00% | -6,27% | -6,64% | +0,73% | FEEDBACK RAPIDO |
| SOL | 14g | 1 | +0,00% | -5,72% | -9,55% | +0,73% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 4 | +50,00% | +1,05% | +0,76% | +2,03% | FEEDBACK RAPIDO |
| DOGE | 3g | 4 | +50,00% | +1,09% | -0,86% | +4,99% | FEEDBACK RAPIDO |
| DOGE | 7g | 3 | +66,67% | +0,53% | -0,69% | +6,15% | FEEDBACK RAPIDO |
| DOGE | 14g | 2 | +50,00% | +0,35% | -1,97% | +6,44% | FEEDBACK RAPIDO |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
