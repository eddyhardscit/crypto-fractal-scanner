# Accuratezza dati exchange e microstruttura

Generato: 2026-09-13 05:32 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-13 | BTC | 77.195,40 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 7,57 | +0,69% | +0,52% |
| 2026-09-13 | DOGE | 0.08469 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 2,19 | -2,64% | +2,48% |
| 2026-09-13 | SOL | 101,72 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,61 | -1,45% | +10,62% |
| 2026-09-12 | BTC | 77.153,40 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,38 | -7,50% | -2,19% |
| 2026-09-12 | DOGE | 0.08429 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 4,01 | -4,06% | +1,39% |
| 2026-09-12 | SOL | 101,52 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 2,94 | +0,13% | +11,01% |
| 2026-09-11 | BTC | 77.056,60 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 2,04 | -0,21% | -2,41% |
| 2026-09-11 | DOGE | 0.08400 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,48 | +0,38% | +4,35% |
| 2026-09-11 | SOL | 99,66 | V2.1.3 | OK | 0 | 0 | 2,50 | BASSA | 2,37 | -3,07% | +8,26% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 5 | +40,00% | -0,26% | -0,89% | +0,60% | FEEDBACK RAPIDO |
| BTC | 3g | 5 | +40,00% | +0,25% | -2,11% | +2,12% | FEEDBACK RAPIDO |
| BTC | 7g | 5 | +40,00% | -1,30% | -3,40% | +2,47% | FEEDBACK RAPIDO |
| BTC | 14g | 3 | +33,33% | -0,17% | -3,31% | +4,48% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 2 | +100,00% | +22,28% | -5,94% | +27,20% | FEEDBACK RAPIDO |
| DOGE | 1g | 9 | +44,44% | +0,77% | -0,33% | +1,78% | FEEDBACK RAPIDO |
| DOGE | 3g | 9 | +33,33% | +1,22% | -3,22% | +5,78% | FEEDBACK RAPIDO |
| DOGE | 7g | 9 | +44,44% | -1,43% | -4,92% | +7,35% | FEEDBACK RAPIDO |
| DOGE | 14g | 8 | +37,50% | +0,57% | -5,38% | +14,44% | FEEDBACK RAPIDO |
| DOGE | 30g | 4 | +75,00% | +14,93% | -1,41% | +41,94% | FEEDBACK RAPIDO |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
