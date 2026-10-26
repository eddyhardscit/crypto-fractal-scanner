# Accuratezza dati exchange e microstruttura

Generato: 2026-10-26 06:33 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-26 | BTC | 80.106,50 | V2.1.3 | OK | 0 | 0 | 2,50 | MEDIA | 3,36 | +2,58% | -2,52% |
| 2026-10-26 | DOGE | 0.07702 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,65 | +0,46% | +1,82% |
| 2026-10-26 | SOL | 101,14 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 1,16 | +0,30% | +6,04% |
| 2026-10-25 | BTC | 80.554,50 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 2,78 | +0,80% | -3,82% |
| 2026-10-25 | DOGE | 0.07694 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,72 | -2,69% | -3,48% |
| 2026-10-25 | SOL | 101,76 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,87 | +0,19% | +1,05% |
| 2026-10-24 | BTC | 80.803,09 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,89 | -1,46% | +5,56% |
| 2026-10-24 | DOGE | 0.07859 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,19 | -3,56% | +2,38% |
| 2026-10-24 | SOL | 102,45 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,05 | -1,66% | -5,17% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 11 | +36,36% | -0,47% | -1,21% | +0,49% | FEEDBACK RAPIDO |
| BTC | 3g | 10 | +40,00% | -0,44% | -2,45% | +1,64% | FEEDBACK RAPIDO |
| BTC | 7g | 10 | +30,00% | -1,89% | -3,68% | +1,86% | FEEDBACK RAPIDO |
| BTC | 14g | 10 | +30,00% | -1,16% | -4,52% | +2,54% | FEEDBACK RAPIDO |
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
