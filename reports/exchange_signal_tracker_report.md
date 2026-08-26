# Accuratezza dati exchange e microstruttura

Generato: 2026-08-26 05:32 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-26 | BTC | 78.654,90 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,31 | -1,63% | -1,02% |
| 2026-08-26 | DOGE | 0.08606 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,79 | -1,68% | -1,23% |
| 2026-08-26 | SOL | 96,32 | V2.1.3 | OK | 1 | 0 | 3,25 | MEDIA | 3,71 | -4,29% | +9,82% |
| 2026-08-25 | BTC | 80.493,33 | V2.1.3 | OK | 1 | 0 | 3,00 | MEDIA | 3,56 | +2,28% | -1,39% |
| 2026-08-25 | DOGE | 0.09243 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,20 | -4,18% | -0,09% |
| 2026-08-25 | SOL | 101,92 | V2.1.3 | OK | 1 | 0 | 3,25 | ALTA | 1,32 | +7,13% | +5,91% |
| 2026-08-24 | BTC | 76.901,40 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 3,80 | +2,92% | +1,83% |
| 2026-08-24 | DOGE | 0.09180 | V2.1.3 | OK | 1 | 0 | 3,25 | MEDIA | 1,09 | +2,91% | +15,94% |
| 2026-08-24 | SOL | 93,87 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,55 | -4,62% | +13,79% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 3 | +66,67% | +0,12% | -0,41% | +0,59% | FEEDBACK RAPIDO |
| BTC | 3g | 2 | +100,00% | +2,38% | -1,18% | +4,13% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 4 | +50,00% | -0,01% | -0,59% | +2,72% | FEEDBACK RAPIDO |
| SOL | 3g | 3 | +33,33% | +0,40% | -2,47% | +5,55% | FEEDBACK RAPIDO |
| SOL | 7g | 2 | +0,00% | -3,56% | -4,18% | +1,44% | FEEDBACK RAPIDO |
| SOL | 14g | 2 | +50,00% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 30g | 1 | +100,00% | +8,60% | -9,55% | +9,55% | FEEDBACK RAPIDO |
| DOGE | 1g | 7 | +57,14% | +1,05% | -0,16% | +2,16% | FEEDBACK RAPIDO |
| DOGE | 3g | 6 | +50,00% | +3,24% | -2,45% | +7,87% | FEEDBACK RAPIDO |
| DOGE | 7g | 4 | +50,00% | +0,28% | -0,90% | +5,64% | FEEDBACK RAPIDO |
| DOGE | 14g | 4 | +50,00% | +2,59% | -1,41% | +16,82% | FEEDBACK RAPIDO |
| DOGE | 30g | 2 | +100,00% | +31,38% | -1,97% | +40,03% | FEEDBACK RAPIDO |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
