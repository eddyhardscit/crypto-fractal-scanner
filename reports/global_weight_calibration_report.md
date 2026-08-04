# Calibrazione pesi Global Confluence

Generato: 2026-08-04 05:17 UTC

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
| BTC | 27 | FEEDBACK RAPIDO | 26 | 0 | 0 | 0 | Famiglia statistica | 1g | 50,00% | -0,01% | feedback rapido: utile da osservare, non da pesare |
| SOL | 27 | FEEDBACK RAPIDO | 26 | 0 | 0 | 0 | Tecnico | 1g | 53,85% | +0,06% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 27 | FEEDBACK RAPIDO | 26 | 0 | 0 | 0 | Famiglia statistica | 1g | 57,69% | +0,28% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 4 | 0,00% | -0,76% | +0,76% | +0,03% | +1,12% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 26 | 50,00% | -0,01% | -0,01% | -0,33% | +0,57% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 21 | 33,33% | -0,44% | +0,22% | -0,13% | +0,81% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 3 | 33,33% | -0,34% | +0,34% | +0,04% | +1,41% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 25 | 44,00% | -0,02% | -0,02% | -0,53% | +0,75% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 20 | 40,00% | -0,34% | +0,23% | -0,26% | +1,03% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 3 | 33,33% | -0,46% | +0,46% | -0,83% | +2,15% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 24 | 50,00% | -0,06% | -0,06% | -1,50% | +1,72% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 19 | 42,11% | -0,06% | +0,44% | -1,16% | +2,18% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 2 | 50,00% | +0,90% | -0,90% | -2,08% | +2,64% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 22 | 36,36% | -0,01% | -0,01% | -2,25% | +2,42% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 18 | 55,56% | -0,10% | +0,29% | -1,98% | +2,75% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 1 | 0,00% | -0,66% | +0,66% | -1,81% | +3,07% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 20 | 50,00% | +0,06% | +0,06% | -2,46% | +2,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 16 | 43,75% | -0,22% | +0,76% | -2,09% | +3,23% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 17 | 47,06% | +0,22% | +0,22% | -2,70% | +3,40% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 14 | 50,00% | +0,16% | +0,69% | -2,37% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 13 | 53,85% | +0,30% | +0,30% | -2,60% | +4,69% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 11 | 45,45% | -0,02% | +0,39% | -2,32% | +4,94% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 6 | 50,00% | +0,27% | +0,27% | -2,29% | +5,58% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 5 | 20,00% | -0,45% | +0,17% | -2,09% | +5,75% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 20 | 40,00% | -0,13% | +0,13% | -0,37% | +0,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 26 | 57,69% | +0,28% | -0,18% | -0,66% | +0,49% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 26 | 50,00% | +0,18% | -0,18% | -0,66% | +0,49% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 20 | 50,00% | -0,13% | +0,13% | -0,57% | +1,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 25 | 48,00% | +0,04% | -0,34% | -0,99% | +0,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 25 | 60,00% | +0,34% | -0,34% | -0,99% | +0,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 20 | 40,00% | +0,14% | -0,14% | -1,99% | +2,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 24 | 50,00% | -0,06% | -0,58% | -2,22% | +1,79% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 24 | 50,00% | +0,58% | -0,58% | -2,22% | +1,79% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 18 | 50,00% | +0,48% | -0,48% | -2,93% | +2,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 22 | 59,09% | +0,21% | -0,95% | -3,25% | +2,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 22 | 59,09% | +0,95% | -0,95% | -3,25% | +2,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 17 | 58,82% | +1,13% | -1,13% | -3,57% | +2,84% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 20 | 65,00% | +0,70% | -1,44% | -3,88% | +2,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 20 | 65,00% | +1,44% | -1,44% | -3,88% | +2,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 16 | 62,50% | +1,54% | -1,54% | -4,33% | +2,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 17 | 70,59% | +1,92% | -1,80% | -4,49% | +2,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 17 | 64,71% | +1,80% | -1,80% | -4,49% | +2,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 12 | 83,33% | +2,89% | -2,89% | -5,71% | +2,55% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 13 | 84,62% | +3,02% | -3,02% | -5,86% | +2,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 13 | 84,62% | +3,02% | -3,02% | -5,86% | +2,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 6 | 100,00% | +4,06% | -4,06% | -6,55% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 6 | 100,00% | +4,06% | -4,06% | -6,55% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 6 | 100,00% | +4,06% | -4,06% | -6,55% | +3,21% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 18 | 55,56% | +0,13% | -0,13% | -0,65% | +0,44% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 22 | 59,09% | -0,12% | -0,51% | -0,94% | +0,19% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 26 | 53,85% | +0,06% | -0,20% | -0,67% | +0,49% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 17 | 52,94% | +0,25% | -0,25% | -0,80% | +0,29% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 21 | 42,86% | -0,49% | -0,71% | -1,43% | +0,13% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 25 | 44,00% | +0,00% | -0,46% | -1,11% | +0,57% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 16 | 50,00% | +0,28% | -0,28% | -2,24% | +1,66% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 20 | 35,00% | -0,60% | -0,98% | -2,78% | +1,40% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 24 | 50,00% | +0,22% | -0,72% | -2,41% | +1,74% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 14 | 64,29% | +0,72% | -0,72% | -3,06% | +2,48% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 18 | 44,44% | -0,96% | -1,36% | -3,72% | +2,02% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 22 | 54,55% | +0,37% | -1,12% | -3,45% | +2,34% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 12 | 66,67% | +1,64% | -1,64% | -3,91% | +2,67% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 16 | 50,00% | -0,57% | -2,01% | -4,48% | +2,19% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 20 | 50,00% | +0,58% | -1,59% | -4,16% | +2,52% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 9 | 88,89% | +2,62% | -2,62% | -4,70% | +3,13% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 13 | 38,46% | -0,62% | -2,29% | -5,16% | +2,43% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 17 | 70,59% | +1,70% | -1,98% | -4,84% | +2,76% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 5 | 100,00% | +2,94% | -2,94% | -4,86% | +4,11% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 9 | 66,67% | +0,29% | -2,75% | -5,44% | +2,66% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 13 | 61,54% | +1,37% | -2,93% | -5,20% | +3,02% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 4 | 100,00% | +4,77% | -4,77% | -6,89% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 6 | 33,33% | -2,40% | -4,46% | -6,69% | +2,76% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 25 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 24 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 26 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 10 | 20,00% | -0,54% |
| BTC | BREVE | Famiglia statistica | 75 | 48,00% | -0,03% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 60 | 38,33% | -0,29% |
| BTC | SETTIMANALE | Classic technical | 3 | 33,33% | +0,38% |
| BTC | SETTIMANALE | Famiglia statistica | 59 | 44,07% | +0,08% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 48 | 50,00% | -0,06% |
| BTC | SWING | Famiglia statistica | 19 | 52,63% | +0,29% |
| BTC | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% |
| BTC | SWING | Tecnico | 16 | 37,50% | -0,15% |
| DOGE | BREVE | Classic technical | 60 | 43,33% | -0,04% |
| DOGE | BREVE | Famiglia statistica | 75 | 52,00% | +0,09% |
| DOGE | BREVE | Microstruttura exchange | 6 | 100,00% | +3,99% |
| DOGE | BREVE | Tecnico | 75 | 53,33% | +0,36% |
| DOGE | SETTIMANALE | Classic technical | 51 | 56,86% | +1,03% |
| DOGE | SETTIMANALE | Famiglia statistica | 59 | 64,41% | +0,87% |
| DOGE | SETTIMANALE | Microstruttura exchange | 6 | 100,00% | +1,18% |
| DOGE | SETTIMANALE | Tecnico | 59 | 62,71% | +1,36% |
| DOGE | SWING | Classic technical | 18 | 88,89% | +3,28% |
| DOGE | SWING | Famiglia statistica | 19 | 89,47% | +3,35% |
| DOGE | SWING | Tecnico | 19 | 89,47% | +3,35% |
| SOL | BREVE | Classic technical | 51 | 52,94% | +0,22% |
| SOL | BREVE | Famiglia statistica | 63 | 46,03% | -0,39% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 75 | 49,33% | +0,09% |
| SOL | SETTIMANALE | Classic technical | 35 | 71,43% | +1,52% |
| SOL | SETTIMANALE | Famiglia statistica | 47 | 44,68% | -0,74% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 3 | 0,00% | -5,22% |
| SOL | SETTIMANALE | Tecnico | 59 | 57,63% | +0,82% |
| SOL | SWING | Classic technical | 5 | 100,00% | +2,94% |
| SOL | SWING | Famiglia statistica | 13 | 76,92% | +1,67% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% |
| SOL | SWING | Tecnico | 19 | 52,63% | +0,18% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 4 | in attesa di controlli maturati |
| BTC | SWING | 5 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SWING | 2 | in attesa di controlli maturati |
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
