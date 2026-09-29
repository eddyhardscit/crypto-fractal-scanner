# Accuratezza dati exchange e microstruttura

Generato: 2026-09-29 05:32 UTC

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-29 | BTC | 83.170,54 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,99 | +3,24% | -0,62% |
| 2026-09-29 | DOGE | 0.09305 | V2.1.3 | OK | 0 | 0 | -1,25 | BASSA | 0,67 | -1,10% | -27,14% |
| 2026-09-29 | SOL | 117,58 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,54 | -3,41% | -5,65% |
| 2026-09-28 | BTC | 83.362,82 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 9,06 | -0,85% | -5,33% |
| 2026-09-28 | DOGE | 0.09429 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,83 | +0,71% | -11,45% |
| 2026-09-28 | SOL | 119,70 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,45 | +4,77% | -6,25% |
| 2026-09-27 | BTC | 84.359,90 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,80 | -0,08% | -0,77% |
| 2026-09-27 | DOGE | 0.09583 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,22 | -2,15% | -11,70% |
| 2026-09-27 | SOL | 120,44 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,99 | +0,57% | -5,38% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 8 | +37,50% | -0,37% | -1,23% | +0,83% | FEEDBACK RAPIDO |
| BTC | 3g | 8 | +37,50% | -0,46% | -2,47% | +1,78% | FEEDBACK RAPIDO |
| BTC | 7g | 6 | +33,33% | -1,53% | -3,35% | +2,42% | FEEDBACK RAPIDO |
| BTC | 14g | 5 | +40,00% | +0,20% | -4,71% | +3,32% | FEEDBACK RAPIDO |
| BTC | 30g | 3 | +66,67% | +5,24% | -4,15% | +8,48% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 5 | +100,00% | +22,07% | -4,32% | +25,38% | FEEDBACK RAPIDO |
| DOGE | 1g | 11 | +54,55% | +1,55% | -0,29% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 3g | 11 | +36,36% | +1,63% | -3,44% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 7g | 11 | +45,45% | -0,13% | -4,83% | +9,23% | FEEDBACK RAPIDO |
| DOGE | 14g | 9 | +33,33% | +0,11% | -6,27% | +13,00% | FEEDBACK RAPIDO |
| DOGE | 30g | 8 | +75,00% | +12,16% | -6,15% | +30,59% | FEEDBACK RAPIDO |

## Regole

- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.
- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.
- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.
- Da 60 controlli: la lettura diventa più utile.
- Da 100 controlli: possibile revisione seria del peso ±1.
- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.
