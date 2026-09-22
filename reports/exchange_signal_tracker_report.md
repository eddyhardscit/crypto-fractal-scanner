# Accuratezza dati exchange e microstruttura

Generato: 2026-09-22 05:32 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **57**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-22 | BTC | 85.448,20 | V2.1.3 | OK | 1 | 0 | 3,25 | ALTA | 3,84 | +9,38% | -2,93% |
| 2026-09-22 | DOGE | 0.10000 | V2.1.3 | OK | 1 | 0 | 3,50 | MEDIA | 1,33 | +7,63% | +6,45% |
| 2026-09-22 | SOL | 116,52 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 2,53 | +1,94% | +0,44% |
| 2026-09-17 | BTC | 76.462,50 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,37 | +0,81% | +0,39% |
| 2026-09-17 | DOGE | 0.08097 | V2.1.3 | OK | 1 | 0 | 2,62 | MEDIA | 1,51 | -1,67% | +9,25% |
| 2026-09-17 | SOL | 99,73 | V2.1.3 | OK | 0 | 0 | 2,25 | BASSA | 1,78 | +1,38% | +9,50% |
| 2026-09-16 | BTC | 75.680,30 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 2,19 | -0,80% | +1,55% |
| 2026-09-16 | DOGE | 0.08000 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,87 | -0,06% | +36,63% |
| 2026-09-16 | SOL | 96,85 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 0,98 | +1,06% | +9,75% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 5 | +40,00% | -0,26% | -0,89% | +0,60% | FEEDBACK RAPIDO |
| BTC | 3g | 5 | +40,00% | +0,25% | -2,11% | +2,12% | FEEDBACK RAPIDO |
| BTC | 7g | 5 | +40,00% | -1,30% | -3,40% | +2,47% | FEEDBACK RAPIDO |
| BTC | 14g | 5 | +40,00% | +0,20% | -4,71% | +3,32% | FEEDBACK RAPIDO |
| BTC | 30g | 2 | +50,00% | +5,45% | -2,78% | +8,46% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 3 | +100,00% | +22,94% | -4,64% | +27,31% | FEEDBACK RAPIDO |
| DOGE | 1g | 10 | +50,00% | +1,49% | -0,36% | +2,53% | FEEDBACK RAPIDO |
| DOGE | 3g | 10 | +40,00% | +1,88% | -2,95% | +6,44% | FEEDBACK RAPIDO |
| DOGE | 7g | 9 | +44,44% | -1,43% | -4,92% | +7,35% | FEEDBACK RAPIDO |
| DOGE | 14g | 9 | +33,33% | +0,11% | -6,27% | +13,00% | FEEDBACK RAPIDO |
| DOGE | 30g | 6 | +66,67% | +12,80% | -4,44% | +34,61% | FEEDBACK RAPIDO |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
