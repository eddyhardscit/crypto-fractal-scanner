# Accuratezza dati exchange e microstruttura

Generato: 2026-09-26 05:32 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-26 | BTC | 83.964,60 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,76 | -3,00% | -2,39% |
| 2026-09-26 | DOGE | 0.09793 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,14 | -0,20% | -5,11% |
| 2026-09-26 | SOL | 120,60 | V2.1.3 | OK | 0 | 0 | 2,50 | MEDIA | 1,14 | +3,84% | -3,36% |
| 2026-09-25 | BTC | 84.171,00 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 4,19 | +0,14% | -0,53% |
| 2026-09-25 | DOGE | 0.09510 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,47 | -2,94% | -7,62% |
| 2026-09-25 | SOL | 116,33 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,15 | +0,81% | -11,76% |
| 2026-09-24 | BTC | 84.264,30 | V2.1.3 | OK | 1 | 0 | 2,75 | MEDIA | 1,59 | -8,96% | +0,80% |
| 2026-09-24 | DOGE | 0.09480 | V2.1.3 | OK | 0 | 0 | 2,50 | BASSA | 2,24 | -4,76% | -3,20% |
| 2026-09-24 | SOL | 115,86 | V2.1.3 | OK | 0 | 0 | 1,50 | BASSA | 0,99 | -4,25% | -0,25% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 8 | +37,50% | -0,37% | -1,23% | +0,83% | FEEDBACK RAPIDO |
| BTC | 3g | 7 | +28,57% | -0,55% | -2,59% | +1,87% | FEEDBACK RAPIDO |
| BTC | 7g | 5 | +40,00% | -1,30% | -3,40% | +2,47% | FEEDBACK RAPIDO |
| BTC | 14g | 5 | +40,00% | +0,20% | -4,71% | +3,32% | FEEDBACK RAPIDO |
| BTC | 30g | 3 | +66,67% | +5,24% | -4,15% | +8,48% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 5 | +100,00% | +22,07% | -4,32% | +25,38% | FEEDBACK RAPIDO |
| DOGE | 1g | 11 | +54,55% | +1,55% | -0,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 3g | 11 | +36,36% | +1,63% | -3,44% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 7g | 10 | +50,00% | +0,54% | -4,49% | +9,62% | FEEDBACK RAPIDO |
| DOGE | 14g | 9 | +33,33% | +0,11% | -6,27% | +13,00% | FEEDBACK RAPIDO |
| DOGE | 30g | 7 | +71,43% | +12,59% | -5,89% | +31,59% | FEEDBACK RAPIDO |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
