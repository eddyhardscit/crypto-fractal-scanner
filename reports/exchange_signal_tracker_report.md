# Accuratezza dati exchange e microstruttura

Generato: 2026-09-04 05:32 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-04 | BTC | 81.007,60 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 7,19 | -0,98% | +1,02% |
| 2026-09-04 | DOGE | 0.08717 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,99 | -1,57% | +7,73% |
| 2026-09-04 | SOL | 103,81 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 2,53 | -0,92% | -8,75% |
| 2026-09-03 | BTC | 77.700,30 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,07 | -3,94% | -0,43% |
| 2026-09-03 | DOGE | 0.08290 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,99 | -0,31% | +1,69% |
| 2026-09-03 | SOL | 100,71 | V2.1.3 | OK | 0 | 0 | 2,25 | BASSA | 2,05 | +1,41% | +10,07% |
| 2026-09-02 | BTC | 77.400,00 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,94 | +2,54% | -1,43% |
| 2026-09-02 | DOGE | 0.08150 | V2.1.3 | OK | 0 | 0 | 1,50 | BASSA | 1,07 | -4,77% | -1,60% |
| 2026-09-02 | SOL | 99,75 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,31 | -2,41% | +3,33% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 3 | +66,67% | +0,12% | -0,41% | +0,59% | FEEDBACK RAPIDO |
| BTC | 3g | 3 | +66,67% | +1,27% | -1,97% | +3,06% | FEEDBACK RAPIDO |
| BTC | 7g | 3 | +66,67% | +0,53% | -2,29% | +3,66% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 3 | +66,67% | +10,89% | -4,64% | +16,94% | FEEDBACK RAPIDO |
| SOL | 30g | 1 | +100,00% | +8,60% | -9,55% | +9,55% | FEEDBACK RAPIDO |
| DOGE | 1g | 8 | +50,00% | +0,90% | -0,21% | +1,91% | FEEDBACK RAPIDO |
| DOGE | 3g | 8 | +37,50% | +1,43% | -3,31% | +6,31% | FEEDBACK RAPIDO |
| DOGE | 7g | 7 | +42,86% | -1,02% | -4,29% | +8,47% | FEEDBACK RAPIDO |
| DOGE | 14g | 5 | +60,00% | +4,09% | -1,22% | +20,18% | FEEDBACK RAPIDO |
| DOGE | 30g | 2 | +100,00% | +31,38% | -1,97% | +40,03% | FEEDBACK RAPIDO |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
