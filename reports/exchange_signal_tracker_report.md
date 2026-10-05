# Accuratezza dati exchange e microstruttura

Generato: 2026-10-05 05:32 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-05 | BTC | 85.557,10 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 11,58 | -7,79% | -3,80% |
| 2026-10-05 | DOGE | 0.09532 | V2.1.3 | OK | 0 | 0 | 2,75 | MEDIA | 1,16 | +3,85% | +1,76% |
| 2026-10-05 | SOL | 120,47 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,17 | +2,11% | +11,20% |
| 2026-10-04 | BTC | 84.802,20 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 2,05 | +1,95% | -4,74% |
| 2026-10-04 | DOGE | 0.09279 | V2.1.3 | OK | 0 | 0 | -2,00 | BASSA | 0,79 | +0,52% | -9,98% |
| 2026-10-04 | SOL | 120,76 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,06 | -0,23% | +13,86% |
| 2026-10-03 | BTC | 84.535,00 | V2.1.3 | OK | 0 | 0 | -1,25 | BASSA | 0,77 | +4,45% | -6,45% |
| 2026-10-03 | DOGE | 0.09296 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,25 | -0,56% | +0,80% |
| 2026-10-03 | SOL | 119,07 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,36 | -2,40% | +7,35% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 9 | +33,33% | -0,58% | -1,37% | +0,50% | FEEDBACK RAPIDO |
| BTC | 3g | 9 | +33,33% | -0,55% | -2,54% | +1,66% | FEEDBACK RAPIDO |
| BTC | 7g | 8 | +37,50% | -1,56% | -3,39% | +2,06% | FEEDBACK RAPIDO |
| BTC | 14g | 5 | +40,00% | +0,20% | -4,71% | +3,32% | FEEDBACK RAPIDO |
| BTC | 30g | 4 | +75,00% | +5,12% | -4,99% | +8,32% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 5 | +100,00% | +22,07% | -4,32% | +25,38% | FEEDBACK RAPIDO |
| DOGE | 1g | 11 | +54,55% | +1,55% | -0,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 3g | 11 | +36,36% | +1,63% | -3,44% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 7g | 11 | +45,45% | -0,13% | -4,83% | +9,23% | FEEDBACK RAPIDO |
| DOGE | 14g | 10 | +40,00% | +1,75% | -5,70% | +14,70% | FEEDBACK RAPIDO |
| DOGE | 30g | 8 | +75,00% | +12,16% | -6,15% | +30,59% | FEEDBACK RAPIDO |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
