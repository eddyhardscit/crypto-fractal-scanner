# Calibrazione pesi Global Confluence

Generato: 2026-08-06 05:16 UTC

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
| BTC | 29 | FEEDBACK RAPIDO | 28 | 0 | 0 | 0 | Famiglia statistica | 1g | 53,57% | +0,05% | feedback rapido: utile da osservare, non da pesare |
| SOL | 29 | FEEDBACK RAPIDO | 28 | 0 | 0 | 0 | Tecnico | 1g | 50,00% | +0,03% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 29 | FEEDBACK RAPIDO | 28 | 0 | 0 | 0 | Famiglia statistica | 1g | 57,14% | +0,25% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 4 | 0,00% | -0,76% | +0,76% | +0,03% | +1,12% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 28 | 53,57% | +0,05% | +0,05% | -0,29% | +0,60% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 23 | 34,78% | -0,41% | +0,27% | -0,10% | +0,82% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 4 | 25,00% | -0,86% | +0,86% | +0,50% | +1,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 27 | 48,15% | +0,13% | +0,13% | -0,38% | +0,86% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 22 | 40,91% | -0,35% | +0,40% | -0,11% | +1,13% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 4 | 25,00% | -1,18% | +1,18% | -0,41% | +2,46% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 26 | 53,85% | +0,12% | +0,12% | -1,42% | +1,78% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 21 | 38,10% | -0,28% | +0,62% | -1,10% | +2,21% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 3 | 33,33% | -0,35% | +0,35% | -1,83% | +2,72% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 24 | 37,50% | +0,10% | +0,10% | -2,25% | +2,34% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 19 | 52,63% | -0,25% | +0,42% | -1,94% | +2,76% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 2 | 0,00% | -0,60% | +0,60% | -2,23% | +2,64% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 22 | 54,55% | +0,14% | +0,14% | -2,47% | +2,75% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 18 | 38,89% | -0,31% | +0,79% | -2,15% | +3,11% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 19 | 42,11% | +0,14% | +0,14% | -2,85% | +3,14% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 15 | 46,67% | +0,13% | +0,63% | -2,44% | +3,68% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 15 | 46,67% | +0,01% | +0,01% | -2,98% | +4,11% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 12 | 50,00% | +0,05% | +0,29% | -2,53% | +4,58% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 8 | 50,00% | +0,31% | +0,31% | -2,52% | +5,21% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 7 | 14,29% | -0,56% | +0,24% | -2,41% | +5,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 20 | 40,00% | -0,13% | +0,13% | -0,37% | +0,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 28 | 57,14% | +0,25% | -0,18% | -0,66% | +0,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 28 | 50,00% | +0,18% | -0,18% | -0,66% | +0,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 20 | 50,00% | -0,13% | +0,13% | -0,57% | +1,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 27 | 48,15% | +0,03% | -0,32% | -0,96% | +0,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 27 | 59,26% | +0,32% | -0,32% | -0,96% | +0,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 20 | 40,00% | +0,14% | -0,14% | -1,99% | +2,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 26 | 50,00% | -0,06% | -0,54% | -2,13% | +1,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 26 | 50,00% | +0,54% | -0,54% | -2,13% | +1,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 20 | 55,00% | +0,45% | -0,45% | -2,87% | +2,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 24 | 54,17% | +0,18% | -0,89% | -3,17% | +2,09% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 24 | 62,50% | +0,89% | -0,89% | -3,17% | +2,09% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 18 | 55,56% | +1,04% | -1,04% | -3,50% | +2,80% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 22 | 63,64% | +0,62% | -1,33% | -3,81% | +2,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 22 | 63,64% | +1,33% | -1,33% | -3,81% | +2,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 16 | 62,50% | +1,54% | -1,54% | -4,33% | +2,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 19 | 63,16% | +1,26% | -2,08% | -4,77% | +2,35% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 19 | 68,42% | +2,08% | -2,08% | -4,77% | +2,35% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 14 | 85,71% | +3,03% | -3,03% | -5,83% | +2,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 15 | 86,67% | +3,12% | -3,12% | -5,95% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 15 | 86,67% | +3,12% | -3,12% | -5,95% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 7 | 100,00% | +4,08% | -4,08% | -6,60% | +2,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 8 | 100,00% | +4,25% | -4,25% | -6,79% | +2,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 8 | 100,00% | +4,25% | -4,25% | -6,79% | +2,60% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 20 | 50,00% | +0,09% | -0,09% | -0,63% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 24 | 62,50% | -0,08% | -0,44% | -0,91% | +0,22% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 28 | 50,00% | +0,03% | -0,16% | -0,66% | +0,50% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 19 | 47,37% | +0,12% | -0,12% | -0,70% | +0,39% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 23 | 47,83% | -0,37% | -0,57% | -1,30% | +0,23% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 27 | 40,74% | -0,07% | -0,36% | -1,02% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 18 | 44,44% | +0,12% | -0,12% | -2,09% | +1,65% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 22 | 40,91% | -0,44% | -0,79% | -2,61% | +1,41% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 26 | 46,15% | +0,12% | -0,57% | -2,30% | +1,72% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 16 | 62,50% | +0,56% | -0,56% | -3,06% | +2,30% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 20 | 45,00% | -0,81% | -1,16% | -3,66% | +1,91% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 24 | 54,17% | +0,29% | -0,98% | -3,42% | +2,23% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 14 | 57,14% | +1,30% | -1,30% | -3,89% | +2,61% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 18 | 55,56% | -0,43% | -1,70% | -4,40% | +2,20% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 22 | 45,45% | +0,46% | -1,38% | -4,12% | +2,49% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 11 | 90,91% | +2,56% | -2,56% | -5,06% | +2,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 15 | 33,33% | -0,84% | -2,29% | -5,36% | +2,19% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 19 | 73,68% | +1,76% | -2,01% | -5,03% | +2,54% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 7 | 100,00% | +3,38% | -3,38% | -5,97% | +3,10% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 11 | 63,64% | +0,34% | -3,06% | -6,04% | +2,28% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 15 | 66,67% | +1,78% | -3,14% | -5,67% | +2,69% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Classic technical | 1 | 100,00% | +2,45% | -2,45% | -6,98% | +3,59% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 6 | 83,33% | +2,80% | -4,38% | -7,23% | +2,50% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 8 | 50,00% | -0,90% | -4,24% | -7,00% | +2,71% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 26 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 26 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 28 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 12 | 16,67% | -0,93% |
| BTC | BREVE | Famiglia statistica | 81 | 51,85% | +0,10% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 66 | 37,88% | -0,35% |
| BTC | SETTIMANALE | Classic technical | 5 | 20,00% | -0,45% |
| BTC | SETTIMANALE | Famiglia statistica | 65 | 44,62% | +0,13% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 52 | 46,15% | -0,16% |
| BTC | SWING | Famiglia statistica | 23 | 47,83% | +0,11% |
| BTC | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% |
| BTC | SWING | Tecnico | 19 | 36,84% | -0,17% |
| DOGE | BREVE | Classic technical | 60 | 43,33% | -0,04% |
| DOGE | BREVE | Famiglia statistica | 81 | 51,85% | +0,08% |
| DOGE | BREVE | Microstruttura exchange | 6 | 100,00% | +3,99% |
| DOGE | BREVE | Tecnico | 81 | 53,09% | +0,34% |
| DOGE | SETTIMANALE | Classic technical | 54 | 57,41% | +0,97% |
| DOGE | SETTIMANALE | Famiglia statistica | 65 | 60,00% | +0,64% |
| DOGE | SETTIMANALE | Microstruttura exchange | 6 | 100,00% | +1,18% |
| DOGE | SETTIMANALE | Tecnico | 65 | 64,62% | +1,39% |
| DOGE | SWING | Classic technical | 21 | 90,48% | +3,38% |
| DOGE | SWING | Famiglia statistica | 23 | 91,30% | +3,51% |
| DOGE | SWING | Tecnico | 23 | 91,30% | +3,51% |
| SOL | BREVE | Classic technical | 57 | 47,37% | +0,11% |
| SOL | BREVE | Famiglia statistica | 69 | 50,72% | -0,29% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 81 | 45,68% | +0,02% |
| SOL | SETTIMANALE | Classic technical | 41 | 68,29% | +1,35% |
| SOL | SETTIMANALE | Famiglia statistica | 53 | 45,28% | -0,69% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 3 | 0,00% | -5,22% |
| SOL | SETTIMANALE | Tecnico | 65 | 56,92% | +0,78% |
| SOL | SWING | Classic technical | 8 | 100,00% | +3,26% |
| SOL | SWING | Famiglia statistica | 17 | 70,59% | +1,21% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% |
| SOL | SWING | Tecnico | 23 | 60,87% | +0,85% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 4 | in attesa di controlli maturati |
| BTC | SWING | 5 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SWING | 1 | in attesa di controlli maturati |
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
