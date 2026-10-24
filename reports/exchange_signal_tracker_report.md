# Accuratezza dati exchange e microstruttura

Generato: 2026-10-24 05:33 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-24 | BTC | 80.803,09 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,89 | -1,46% | +5,56% |
| 2026-10-24 | DOGE | 0.07859 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,19 | -3,56% | +2,38% |
| 2026-10-24 | SOL | 102,45 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,05 | -1,66% | -5,17% |
| 2026-10-23 | BTC | 81.699,50 | V2.1.3 | OK | 0 | 0 | 0,38 | MEDIA | 3,22 | +2,20% | -0,97% |
| 2026-10-23 | DOGE | 0.07955 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,14 | +0,85% | -3,30% |
| 2026-10-23 | SOL | 104,14 | V2.1.3 | OK | 0 | 0 | 0,38 | MEDIA | 1,86 | +2,40% | +1,99% |
| 2026-10-22 | BTC | 82.821,00 | V2.1.3 | OK | 0 | 0 | 2,50 | MEDIA | 1,74 | +2,22% | +1,79% |
| 2026-10-22 | DOGE | 0.08008 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,44 | -1,38% | +11,60% |
| 2026-10-22 | SOL | 105,40 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,90 | -1,78% | -5,33% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 10 | +40,00% | -0,44% | -1,18% | +0,59% | FEEDBACK RAPIDO |
| BTC | 3g | 10 | +40,00% | -0,44% | -2,45% | +1,64% | FEEDBACK RAPIDO |
| BTC | 7g | 10 | +30,00% | -1,89% | -3,68% | +1,86% | FEEDBACK RAPIDO |
| BTC | 14g | 9 | +33,33% | -0,96% | -4,58% | +2,58% | FEEDBACK RAPIDO |
| BTC | 30g | 8 | +50,00% | +1,78% | -5,80% | +6,08% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 5 | +100,00% | +22,07% | -4,32% | +25,38% | FEEDBACK RAPIDO |
| DOGE | 1g | 13 | +46,15% | +0,84% | -0,72% | +2,33% | FEEDBACK RAPIDO |
| DOGE | 3g | 13 | +30,77% | +0,78% | -3,69% | +5,57% | FEEDBACK RAPIDO |
| DOGE | 7g | 12 | +41,67% | -0,39% | -5,05% | +8,59% | FEEDBACK RAPIDO |
| DOGE | 14g | 11 | +36,36% | +1,12% | -6,04% | +13,84% | FEEDBACK RAPIDO |
| DOGE | 30g | 11 | +63,64% | +7,24% | -8,14% | +26,94% | FEEDBACK RAPIDO |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
