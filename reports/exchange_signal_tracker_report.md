# Accuratezza dati exchange e microstruttura

Generato: 2026-10-21 05:33 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-21 | BTC | 82.880,00 | V2.1.3 | OK | 0 | 0 | 2,50 | MEDIA | 3,60 | +1,09% | +5,13% |
| 2026-10-21 | DOGE | 0.08169 | V2.1.3 | OK | 1 | 0 | 3,00 | MEDIA | 1,16 | +4,02% | +4,30% |
| 2026-10-21 | SOL | 106,07 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,42 | +2,72% | -2,45% |
| 2026-10-20 | BTC | 81.980,50 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,64 | -0,92% | +0,20% |
| 2026-10-20 | DOGE | 0.07954 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,87 | +0,09% | +5,57% |
| 2026-10-20 | SOL | 105,03 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,86 | -0,84% | -1,61% |
| 2026-10-19 | BTC | 82.595,70 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 4,85 | -1,52% | -3,84% |
| 2026-10-19 | DOGE | 0.07944 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,11 | -2,36% | +0,54% |
| 2026-10-19 | SOL | 105,43 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,79 | -0,23% | -6,53% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 10 | +40,00% | -0,44% | -1,18% | +0,59% | FEEDBACK RAPIDO |
| BTC | 3g | 10 | +40,00% | -0,44% | -2,45% | +1,64% | FEEDBACK RAPIDO |
| BTC | 7g | 10 | +30,00% | -1,89% | -3,68% | +1,86% | FEEDBACK RAPIDO |
| BTC | 14g | 9 | +33,33% | -0,96% | -4,58% | +2,58% | FEEDBACK RAPIDO |
| BTC | 30g | 5 | +80,00% | +5,55% | -5,21% | +8,55% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 5 | +100,00% | +22,07% | -4,32% | +25,38% | FEEDBACK RAPIDO |
| DOGE | 1g | 12 | +50,00% | +1,09% | -0,60% | +2,49% | FEEDBACK RAPIDO |
| DOGE | 3g | 12 | +33,33% | +1,19% | -3,61% | +5,84% | FEEDBACK RAPIDO |
| DOGE | 7g | 11 | +45,45% | -0,13% | -4,83% | +9,23% | FEEDBACK RAPIDO |
| DOGE | 14g | 11 | +36,36% | +1,12% | -6,04% | +13,84% | FEEDBACK RAPIDO |
| DOGE | 30g | 10 | +70,00% | +9,97% | -6,58% | +29,10% | FEEDBACK RAPIDO |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
