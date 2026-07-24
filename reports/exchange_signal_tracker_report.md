# Accuratezza dati exchange e microstruttura

Generato: 2026-07-24 05:14 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **9**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-24 | BTC | 65.326,60 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 3,29 | -1,87% | +3,07% |
| 2026-07-24 | DOGE | 0.06905 | V2.1.3 | OK | 1 | 0 | 2,88 | MEDIA | 1,88 | -10,42% | -7,48% |
| 2026-07-24 | SOL | 75,75 | V2.1.3 | OK | 0 | 0 | 0,38 | MEDIA | 7,39 | +14,43% | +2,17% |
| 2026-07-23 | BTC | 65.401,40 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,28 | -2,58% | +2,03% |
| 2026-07-23 | DOGE | 0.07229 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,72 | +5,83% | +4,06% |
| 2026-07-23 | SOL | 77,12 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 2,89 | -5,54% | -2,81% |
| 2026-07-22 | BTC | 66.242,06 | V2.1.3 | OK | 0 | 0 | 3,50 | ALTA | 1,21 | +3,44% | +1,49% |
| 2026-07-22 | DOGE | 0.07326 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,95 | +2,24% | +0,22% |
| 2026-07-22 | SOL | 77,84 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,93 | +6,24% | +6,76% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 1 | +0,00% | -0,43% | -0,39% | +0,39% | FEEDBACK RAPIDO |
| SOL | 3g | 1 | +0,00% | -3,12% | -3,63% | +0,73% | FEEDBACK RAPIDO |
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
