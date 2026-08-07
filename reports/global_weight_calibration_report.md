# Calibrazione pesi Global Confluence

Generato: 2026-08-07 05:17 UTC

Report completo: [global_weight_calibration_report.md](global_weight_calibration_report.md)

Questo blocco controlla se, col tempo, i moduli reali del Global Confluence meritano più peso, meno peso o peso invariato.

Correzione anti-doppio-conteggio: **la Famiglia statistica Scanner + Market Regime è il modulo calibrabile**. Scanner grezzo e Market Regime grezzo restano visibili solo come diagnostica e non ricevono proposte di peso separate.

Regola principale:

- sotto **30 controlli**: osservazione, nessuna modifica pesi
- da **30 controlli**: prima calibrazione leggera
- da **60 controlli**: lettura utile
- da **100+ controlli**: possibile proposta prudente di modifica pesi

Il file continua a produrre solo raccomandazioni: **non modifica automaticamente** `global_confluence_report.py`.

## Sintesi per asset

| Asset | Segnali salvati | Stato | Controlli max | Righe 30+ | Righe 60+ | Righe 100+ | Miglior modulo calibrabile | Orizzonte | Accuratezza | Return corretto direzione | Lettura |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 30 | FEEDBACK RAPIDO | 29 | 0 | 0 | 0 | Famiglia statistica | 1g | 51,72% | +0,01% | feedback rapido: utile da osservare, non da pesare |
| SOL | 30 | FEEDBACK RAPIDO | 29 | 0 | 0 | 0 | Tecnico | 1g | 51,72% | +0,10% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 30 | FEEDBACK RAPIDO | 29 | 0 | 0 | 0 | Famiglia statistica | 1g | 55,17% | +0,19% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 4 | 0,00% | -0,76% | +0,76% | +0,03% | +1,12% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 29 | 51,72% | +0,01% | +0,01% | -0,32% | +0,55% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 24 | 33,33% | -0,44% | +0,22% | -0,14% | +0,76% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 4 | 25,00% | -0,86% | +0,86% | +0,50% | +1,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 28 | 46,43% | +0,12% | +0,12% | -0,38% | +0,83% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 23 | 43,48% | -0,33% | +0,37% | -0,11% | +1,09% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 4 | 25,00% | -1,18% | +1,18% | -0,41% | +2,46% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 27 | 55,56% | +0,14% | +0,14% | -1,36% | +1,78% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 22 | 40,91% | -0,24% | +0,62% | -1,05% | +2,19% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 3 | 33,33% | -0,35% | +0,35% | -1,83% | +2,72% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 25 | 40,00% | +0,15% | +0,15% | -2,24% | +2,34% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 20 | 50,00% | -0,30% | +0,46% | -1,94% | +2,74% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 2 | 0,00% | -0,60% | +0,60% | -2,23% | +2,64% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 23 | 52,17% | +0,12% | +0,12% | -2,51% | +2,67% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 18 | 38,89% | -0,31% | +0,79% | -2,15% | +3,11% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Classic technical | 1 | 0,00% | -1,25% | +1,25% | -1,82% | +3,07% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 20 | 45,00% | +0,20% | +0,20% | -2,80% | +3,14% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 16 | 43,75% | +0,05% | +0,67% | -2,40% | +3,64% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 16 | 43,75% | -0,10% | -0,10% | -3,09% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 13 | 53,85% | +0,18% | +0,13% | -2,70% | +4,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 9 | 55,56% | +0,37% | +0,37% | -2,48% | +5,20% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 8 | 12,50% | -0,60% | +0,32% | -2,38% | +5,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 20 | 40,00% | -0,13% | +0,13% | -0,37% | +0,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 29 | 55,17% | +0,19% | -0,22% | -0,69% | +0,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 28 | 50,00% | +0,18% | -0,18% | -0,66% | +0,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 20 | 50,00% | -0,13% | +0,13% | -0,57% | +1,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 28 | 46,43% | -0,02% | -0,35% | -0,97% | +0,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 28 | 60,71% | +0,35% | -0,35% | -0,97% | +0,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 20 | 40,00% | +0,14% | -0,14% | -1,99% | +2,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 27 | 48,15% | -0,12% | -0,58% | -2,12% | +1,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 27 | 51,85% | +0,58% | -0,58% | -2,12% | +1,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 20 | 55,00% | +0,45% | -0,45% | -2,87% | +2,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 25 | 52,00% | +0,10% | -0,92% | -3,12% | +2,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 25 | 64,00% | +0,92% | -0,92% | -3,12% | +2,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 19 | 57,89% | +1,06% | -1,06% | -3,47% | +2,74% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 23 | 60,87% | +0,52% | -1,34% | -3,77% | +2,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 23 | 65,22% | +1,34% | -1,34% | -3,77% | +2,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 17 | 64,71% | +1,53% | -1,53% | -4,24% | +2,85% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 20 | 60,00% | +1,13% | -2,04% | -4,67% | +2,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 20 | 70,00% | +2,04% | -2,04% | -4,67% | +2,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 15 | 80,00% | +2,82% | -2,82% | -5,54% | +2,70% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 16 | 81,25% | +2,93% | -2,93% | -5,67% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Microstruttura exchange | 1 | 100,00% | +0,01% | +0,01% | -1,52% | +6,93% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 16 | 81,25% | +2,93% | -2,93% | -5,67% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 8 | 100,00% | +4,11% | -4,11% | -6,51% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 9 | 100,00% | +4,26% | -4,26% | -6,68% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 9 | 100,00% | +4,26% | -4,26% | -6,68% | +2,56% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 20 | 50,00% | +0,09% | -0,09% | -0,63% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 25 | 60,00% | -0,16% | -0,51% | -0,96% | +0,14% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 29 | 51,72% | +0,10% | -0,22% | -0,71% | +0,42% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 20 | 50,00% | +0,20% | -0,20% | -0,76% | +0,30% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 24 | 45,83% | -0,42% | -0,61% | -1,32% | +0,16% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 28 | 42,86% | -0,00% | -0,40% | -1,05% | +0,55% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 19 | 47,37% | +0,19% | -0,19% | -2,07% | +1,63% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 23 | 39,13% | -0,48% | -0,82% | -2,57% | +1,41% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 27 | 48,15% | +0,16% | -0,61% | -2,27% | +1,71% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 17 | 64,71% | +0,59% | -0,59% | -3,00% | +2,26% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 21 | 42,86% | -0,82% | -1,16% | -3,58% | +1,90% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 25 | 56,00% | +0,32% | -0,98% | -3,36% | +2,21% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 15 | 60,00% | +1,34% | -1,34% | -3,93% | +2,49% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 19 | 52,63% | -0,50% | -1,71% | -4,41% | +2,13% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 23 | 47,83% | +0,52% | -1,40% | -4,14% | +2,42% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 12 | 91,67% | +2,42% | -2,42% | -4,93% | +2,67% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 16 | 31,25% | -0,85% | -2,20% | -5,25% | +2,21% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 20 | 75,00% | +1,72% | -1,96% | -4,95% | +2,54% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 8 | 100,00% | +3,47% | -3,47% | -6,05% | +2,98% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 12 | 58,33% | -0,02% | -3,15% | -6,09% | +2,27% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 16 | 68,75% | +1,93% | -3,19% | -5,73% | +2,66% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Classic technical | 2 | 100,00% | +2,87% | -2,87% | -6,43% | +4,20% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 7 | 85,71% | +2,87% | -4,23% | -7,04% | +2,83% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 9 | 55,56% | -0,44% | -4,14% | -6,87% | +2,94% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 27 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 27 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 29 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 12 | 16,67% | -0,93% |
| BTC | BREVE | Famiglia statistica | 84 | 51,19% | +0,09% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 69 | 39,13% | -0,34% |
| BTC | SETTIMANALE | Classic technical | 6 | 16,67% | -0,58% |
| BTC | SETTIMANALE | Famiglia statistica | 68 | 45,59% | +0,16% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 54 | 44,44% | -0,20% |
| BTC | SWING | Famiglia statistica | 25 | 48,00% | +0,07% |
| BTC | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% |
| BTC | SWING | Tecnico | 21 | 38,10% | -0,12% |
| DOGE | BREVE | Classic technical | 60 | 43,33% | -0,04% |
| DOGE | BREVE | Famiglia statistica | 84 | 50,00% | +0,02% |
| DOGE | BREVE | Microstruttura exchange | 6 | 100,00% | +3,99% |
| DOGE | BREVE | Tecnico | 83 | 54,22% | +0,37% |
| DOGE | SETTIMANALE | Classic technical | 56 | 58,93% | +0,98% |
| DOGE | SETTIMANALE | Famiglia statistica | 68 | 57,35% | +0,55% |
| DOGE | SETTIMANALE | Microstruttura exchange | 6 | 100,00% | +1,18% |
| DOGE | SETTIMANALE | Tecnico | 68 | 66,18% | +1,39% |
| DOGE | SWING | Classic technical | 23 | 86,96% | +3,27% |
| DOGE | SWING | Famiglia statistica | 25 | 88,00% | +3,41% |
| DOGE | SWING | Microstruttura exchange | 1 | 100,00% | +0,01% |
| DOGE | SWING | Tecnico | 25 | 88,00% | +3,41% |
| SOL | BREVE | Classic technical | 59 | 49,15% | +0,16% |
| SOL | BREVE | Famiglia statistica | 72 | 48,61% | -0,35% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 84 | 47,62% | +0,09% |
| SOL | SETTIMANALE | Classic technical | 44 | 70,45% | +1,34% |
| SOL | SETTIMANALE | Famiglia statistica | 56 | 42,86% | -0,72% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 3 | 0,00% | -5,22% |
| SOL | SETTIMANALE | Tecnico | 68 | 58,82% | +0,80% |
| SOL | SWING | Classic technical | 10 | 100,00% | +3,35% |
| SOL | SWING | Famiglia statistica | 19 | 68,42% | +1,04% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% |
| SOL | SWING | Tecnico | 25 | 64,00% | +1,08% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 5 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SWING | 1 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 3 | in attesa di controlli maturati |
| DOGE | MEDIO | 15 | in attesa di controlli maturati |

## Come leggere le raccomandazioni

- **OSSERVA**: meno di 30 controlli, nessuna modifica.
- **PESO OK / MANTIENI**: il modulo sta aiutando, ma non serve cambiare peso.
- **NON AUMENTARE**: il modulo non dimostra ancora un vantaggio sufficiente.
- **POSSIBILE AUMENTO LEGGERO**: proposta prudente, mai automatica.
- **POSSIBILE RIDUZIONE**: modulo debole con campione già abbastanza maturo.
- **ESCLUSO**: benchmark o diagnostica già inclusa in un'altra famiglia.

Nota decisiva: **non sommare mai una modifica alla Famiglia statistica e altre modifiche separate a Scanner o Market Regime**. Scanner e Market servono soltanto a capire quale parte della famiglia sta funzionando o fallendo.

## Stato attuale

Siamo ancora in feedback rapido. Non bisogna modificare i pesi del Global. La nuova struttura serve ad accumulare dati corretti senza doppio conteggio.
