# Accuratezza dati exchange e microstruttura

Generato: 2026-10-08 05:33 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-08 | BTC | 82.581,92 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 2,74 | -1,32% | +3,00% |
| 2026-10-08 | DOGE | 0.08745 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,28 | -2,89% | +6,45% |
| 2026-10-08 | SOL | 115,11 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,10 | +0,84% | +3,60% |
| 2026-10-07 | BTC | 84.116,40 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 4,41 | +4,77% | -4,30% |
| 2026-10-07 | DOGE | 0.08994 | V2.1.3 | OK | 0 | 0 | 1,50 | BASSA | 1,00 | -4,76% | -3,67% |
| 2026-10-07 | SOL | 118,27 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,13 | -2,27% | +1,65% |
| 2026-10-06 | BTC | 85.618,90 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 3,82 | +4,99% | -1,61% |
| 2026-10-06 | DOGE | 0.09499 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,48 | -0,85% | -0,41% |
| 2026-10-06 | SOL | 120,16 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 2,21 | -2,10% | +11,24% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 9 | +33,33% | -0,58% | -1,37% | +0,50% | FEEDBACK RAPIDO |
| BTC | 3g | 9 | +33,33% | -0,55% | -2,54% | +1,66% | FEEDBACK RAPIDO |
| BTC | 7g | 8 | +37,50% | -1,56% | -3,39% | +2,06% | FEEDBACK RAPIDO |
| BTC | 14g | 8 | +37,50% | -0,43% | -4,26% | +2,82% | FEEDBACK RAPIDO |
| BTC | 30g | 5 | +80,00% | +5,55% | -5,21% | +8,55% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 5 | +100,00% | +22,07% | -4,32% | +25,38% | FEEDBACK RAPIDO |
| DOGE | 1g | 11 | +54,55% | +1,55% | -0,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 3g | 11 | +36,36% | +1,63% | -3,44% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 7g | 11 | +45,45% | -0,13% | -4,83% | +9,23% | FEEDBACK RAPIDO |
| DOGE | 14g | 11 | +36,36% | +1,12% | -6,04% | +13,84% | FEEDBACK RAPIDO |
| DOGE | 30g | 9 | +77,78% | +11,35% | -6,95% | +29,00% | FEEDBACK RAPIDO |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
