# Calibrazione pesi Global Confluence

Generato: 2026-08-03 05:15 UTC

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
| BTC | 26 | FEEDBACK RAPIDO | 25 | 0 | 0 | 0 | Famiglia statistica | 1g | 48,00% | -0,07% | feedback rapido: utile da osservare, non da pesare |
| SOL | 26 | FEEDBACK RAPIDO | 25 | 0 | 0 | 0 | Tecnico | 1g | 56,00% | +0,10% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 26 | FEEDBACK RAPIDO | 25 | 0 | 0 | 0 | Famiglia statistica | 1g | 56,00% | +0,27% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 3 | 0,00% | -0,46% | +0,46% | -0,25% | +0,77% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 25 | 48,00% | -0,07% | -0,07% | -0,38% | +0,50% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 20 | 35,00% | -0,38% | +0,15% | -0,18% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 3 | 33,33% | -0,34% | +0,34% | +0,04% | +1,41% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 24 | 41,67% | -0,05% | -0,05% | -0,54% | +0,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 19 | 42,11% | -0,33% | +0,21% | -0,27% | +1,02% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 2 | 50,00% | -0,10% | +0,10% | -0,99% | +2,40% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 23 | 47,83% | -0,12% | -0,12% | -1,54% | +1,72% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 18 | 44,44% | +0,00% | +0,40% | -1,20% | +2,20% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 2 | 50,00% | +0,90% | -0,90% | -2,08% | +2,64% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 21 | 38,10% | -0,00% | -0,00% | -2,23% | +2,43% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 17 | 52,94% | -0,12% | +0,31% | -1,94% | +2,78% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 19 | 47,37% | +0,02% | +0,02% | -2,49% | +2,79% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 15 | 46,67% | -0,20% | +0,77% | -2,10% | +3,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 16 | 50,00% | +0,26% | +0,26% | -2,69% | +3,46% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 13 | 46,15% | +0,14% | +0,78% | -2,33% | +3,91% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 12 | 58,33% | +0,54% | +0,54% | -2,40% | +4,93% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 11 | 45,45% | -0,02% | +0,39% | -2,32% | +4,94% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 5 | 40,00% | -0,08% | -0,08% | -2,65% | +5,30% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 4 | 25,00% | -0,06% | -0,29% | -2,49% | +5,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 20 | 40,00% | -0,13% | +0,13% | -0,37% | +0,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 25 | 56,00% | +0,27% | -0,21% | -0,69% | +0,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 25 | 52,00% | +0,21% | -0,21% | -0,69% | +0,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 20 | 50,00% | -0,13% | +0,13% | -0,57% | +1,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 24 | 50,00% | +0,04% | -0,35% | -1,01% | +0,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 24 | 58,33% | +0,35% | -0,35% | -1,01% | +0,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 19 | 42,11% | +0,15% | -0,15% | -2,02% | +2,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 23 | 47,83% | -0,06% | -0,61% | -2,26% | +1,80% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 23 | 52,17% | +0,61% | -0,61% | -2,26% | +1,80% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 17 | 52,94% | +0,55% | -0,55% | -2,96% | +2,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 21 | 57,14% | +0,18% | -1,04% | -3,29% | +2,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 21 | 61,90% | +1,04% | -1,04% | -3,29% | +2,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 16 | 62,50% | +1,22% | -1,22% | -3,61% | +2,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 19 | 63,16% | +0,72% | -1,53% | -3,94% | +2,35% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 19 | 68,42% | +1,53% | -1,53% | -3,94% | +2,35% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 15 | 66,67% | +1,71% | -1,71% | -4,48% | +2,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 16 | 68,75% | +1,98% | -1,98% | -4,64% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,20% | +1,20% | -1,52% | +6,93% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 16 | 68,75% | +1,98% | -1,98% | -4,64% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 11 | 81,82% | +2,83% | -2,83% | -5,62% | +2,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 12 | 83,33% | +2,97% | -2,97% | -5,79% | +2,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 12 | 83,33% | +2,97% | -2,97% | -5,79% | +2,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 5 | 100,00% | +4,35% | -4,35% | -6,73% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 5 | 100,00% | +4,35% | -4,35% | -6,73% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 5 | 100,00% | +4,35% | -4,35% | -6,73% | +2,99% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 17 | 58,82% | +0,20% | -0,20% | -0,69% | +0,39% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 21 | 57,14% | -0,17% | -0,59% | -1,00% | +0,13% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 25 | 56,00% | +0,10% | -0,24% | -0,70% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 16 | 56,25% | +0,29% | -0,29% | -0,81% | +0,26% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 20 | 40,00% | -0,53% | -0,77% | -1,48% | +0,10% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 24 | 45,83% | +0,02% | -0,50% | -1,14% | +0,56% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 15 | 53,33% | +0,34% | -0,34% | -2,27% | +1,68% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 19 | 31,58% | -0,67% | -1,07% | -2,84% | +1,41% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 23 | 52,17% | +0,26% | -0,78% | -2,44% | +1,76% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 13 | 69,23% | +0,80% | -0,80% | -3,00% | +2,50% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 17 | 41,18% | -1,04% | -1,45% | -3,72% | +2,00% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 21 | 57,14% | +0,41% | -1,19% | -3,43% | +2,35% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 11 | 72,73% | +1,84% | -1,84% | -3,95% | +2,68% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 15 | 46,67% | -0,65% | -2,18% | -4,55% | +2,17% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 19 | 52,63% | +0,64% | -1,71% | -4,19% | +2,52% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 8 | 87,50% | +2,87% | -2,87% | -4,70% | +2,98% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 12 | 41,67% | -0,62% | -2,42% | -5,20% | +2,27% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 16 | 68,75% | +1,76% | -2,06% | -4,84% | +2,66% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 5 | 100,00% | +2,94% | -2,94% | -4,86% | +4,11% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 8 | 75,00% | +1,05% | -2,37% | -4,91% | +2,92% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 12 | 58,33% | +1,00% | -2,69% | -4,83% | +3,22% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 4 | 100,00% | +4,77% | -4,77% | -6,89% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 5 | 20,00% | -3,22% | -5,02% | -6,90% | +2,26% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 24 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 23 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 25 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 8 | 25,00% | -0,32% |
| BTC | BREVE | Famiglia statistica | 72 | 45,83% | -0,08% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 57 | 40,35% | -0,24% |
| BTC | SETTIMANALE | Classic technical | 2 | 50,00% | +0,90% |
| BTC | SETTIMANALE | Famiglia statistica | 56 | 44,64% | +0,08% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 45 | 48,89% | -0,07% |
| BTC | SWING | Famiglia statistica | 17 | 52,94% | +0,36% |
| BTC | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% |
| BTC | SWING | Tecnico | 15 | 40,00% | -0,03% |
| DOGE | BREVE | Classic technical | 59 | 44,07% | -0,04% |
| DOGE | BREVE | Famiglia statistica | 72 | 51,39% | +0,09% |
| DOGE | BREVE | Microstruttura exchange | 6 | 100,00% | +3,99% |
| DOGE | BREVE | Tecnico | 72 | 54,17% | +0,39% |
| DOGE | SETTIMANALE | Classic technical | 48 | 60,42% | +1,13% |
| DOGE | SETTIMANALE | Famiglia statistica | 56 | 62,50% | +0,88% |
| DOGE | SETTIMANALE | Microstruttura exchange | 5 | 100,00% | +1,22% |
| DOGE | SETTIMANALE | Tecnico | 56 | 66,07% | +1,47% |
| DOGE | SWING | Classic technical | 16 | 87,50% | +3,30% |
| DOGE | SWING | Famiglia statistica | 17 | 88,24% | +3,37% |
| DOGE | SWING | Tecnico | 17 | 88,24% | +3,37% |
| SOL | BREVE | Classic technical | 48 | 56,25% | +0,27% |
| SOL | BREVE | Famiglia statistica | 60 | 43,33% | -0,45% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 72 | 51,39% | +0,12% |
| SOL | SETTIMANALE | Classic technical | 32 | 75,00% | +1,67% |
| SOL | SETTIMANALE | Famiglia statistica | 44 | 43,18% | -0,79% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 3 | 0,00% | -5,22% |
| SOL | SETTIMANALE | Tecnico | 56 | 58,93% | +0,87% |
| SOL | SWING | Classic technical | 5 | 100,00% | +2,94% |
| SOL | SWING | Famiglia statistica | 12 | 83,33% | +2,29% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Tecnico | 17 | 47,06% | -0,24% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 5 | in attesa di controlli maturati |
| BTC | SWING | 5 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SWING | 3 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 4 | in attesa di controlli maturati |
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
