# Calibrazione pesi Global Confluence

Generato: 2026-08-05 05:15 UTC

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
| BTC | 28 | FEEDBACK RAPIDO | 27 | 0 | 0 | 0 | Famiglia statistica | 1g | 51,85% | +0,02% | feedback rapido: utile da osservare, non da pesare |
| SOL | 28 | FEEDBACK RAPIDO | 27 | 0 | 0 | 0 | Tecnico | 1g | 51,85% | +0,04% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 28 | FEEDBACK RAPIDO | 27 | 0 | 0 | 0 | Famiglia statistica | 1g | 55,56% | +0,26% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 4 | 0,00% | -0,76% | +0,76% | +0,03% | +1,12% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 27 | 51,85% | +0,02% | +0,02% | -0,31% | +0,58% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 22 | 36,36% | -0,39% | +0,24% | -0,12% | +0,81% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 4 | 25,00% | -0,86% | +0,86% | +0,50% | +1,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 26 | 46,15% | +0,07% | +0,07% | -0,44% | +0,82% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 21 | 38,10% | -0,44% | +0,34% | -0,16% | +1,10% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 3 | 33,33% | -0,46% | +0,46% | -0,83% | +2,15% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 25 | 52,00% | -0,01% | -0,01% | -1,51% | +1,71% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 20 | 40,00% | -0,12% | +0,48% | -1,19% | +2,15% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 2 | 50,00% | +0,90% | -0,90% | -2,08% | +2,64% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 23 | 34,78% | -0,01% | -0,01% | -2,29% | +2,32% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 18 | 55,56% | -0,10% | +0,29% | -1,98% | +2,75% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 2 | 0,00% | -0,60% | +0,60% | -2,23% | +2,64% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 21 | 52,38% | +0,08% | +0,08% | -2,46% | +2,78% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 17 | 41,18% | -0,24% | +0,75% | -2,12% | +3,17% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 18 | 44,44% | +0,19% | +0,19% | -2,74% | +3,32% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 15 | 46,67% | +0,13% | +0,63% | -2,44% | +3,68% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 14 | 50,00% | +0,07% | +0,07% | -2,85% | +4,36% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 11 | 45,45% | -0,02% | +0,39% | -2,32% | +4,94% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 7 | 42,86% | +0,17% | +0,17% | -2,47% | +5,31% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 6 | 16,67% | -0,44% | +0,07% | -2,34% | +5,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 20 | 40,00% | -0,13% | +0,13% | -0,37% | +0,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 27 | 55,56% | +0,26% | -0,19% | -0,66% | +0,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 27 | 51,85% | +0,19% | -0,19% | -0,66% | +0,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 20 | 50,00% | -0,13% | +0,13% | -0,57% | +1,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 26 | 50,00% | +0,04% | -0,32% | -0,96% | +0,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 26 | 57,69% | +0,32% | -0,32% | -0,96% | +0,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 20 | 40,00% | +0,14% | -0,14% | -1,99% | +2,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 25 | 48,00% | -0,07% | -0,57% | -2,20% | +1,75% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 25 | 52,00% | +0,57% | -0,57% | -2,20% | +1,75% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 19 | 52,63% | +0,46% | -0,46% | -2,93% | +2,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 23 | 56,52% | +0,19% | -0,92% | -3,24% | +2,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 23 | 60,87% | +0,92% | -0,92% | -3,24% | +2,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 17 | 58,82% | +1,13% | -1,13% | -3,57% | +2,84% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 21 | 61,90% | +0,62% | -1,42% | -3,88% | +2,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 21 | 66,67% | +1,42% | -1,42% | -3,88% | +2,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 16 | 62,50% | +1,54% | -1,54% | -4,33% | +2,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 18 | 66,67% | +1,55% | -1,97% | -4,66% | +2,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 18 | 66,67% | +1,97% | -1,97% | -4,66% | +2,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 13 | 84,62% | +3,01% | -3,01% | -5,82% | +2,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 14 | 85,71% | +3,12% | -3,12% | -5,95% | +2,29% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 14 | 85,71% | +3,12% | -3,12% | -5,95% | +2,29% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 6 | 100,00% | +4,06% | -4,06% | -6,55% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 7 | 100,00% | +4,26% | -4,26% | -6,76% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 7 | 100,00% | +4,26% | -4,26% | -6,76% | +2,82% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 19 | 52,63% | +0,11% | -0,11% | -0,63% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 23 | 60,87% | -0,10% | -0,48% | -0,92% | +0,22% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 27 | 51,85% | +0,04% | -0,18% | -0,66% | +0,51% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 18 | 50,00% | +0,17% | -0,17% | -0,72% | +0,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 22 | 45,45% | -0,41% | -0,62% | -1,34% | +0,21% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 26 | 42,31% | -0,05% | -0,39% | -1,04% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 17 | 47,06% | +0,22% | -0,22% | -2,22% | +1,63% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 21 | 38,10% | -0,54% | -0,91% | -2,74% | +1,39% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 25 | 48,00% | +0,19% | -0,66% | -2,40% | +1,72% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 15 | 66,67% | +0,68% | -0,68% | -3,15% | +2,34% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 19 | 42,11% | -0,92% | -1,30% | -3,76% | +1,93% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 23 | 56,52% | +0,37% | -1,08% | -3,49% | +2,26% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 13 | 61,54% | +1,47% | -1,47% | -3,90% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 17 | 52,94% | -0,51% | -1,86% | -4,44% | +2,19% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 21 | 47,62% | +0,52% | -1,49% | -4,14% | +2,50% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 10 | 90,00% | +2,52% | -2,52% | -4,82% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 14 | 35,71% | -0,69% | -2,24% | -5,21% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 18 | 72,22% | +1,69% | -1,96% | -4,89% | +2,77% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 6 | 100,00% | +3,29% | -3,29% | -5,57% | +3,56% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 10 | 70,00% | +0,77% | -2,98% | -5,81% | +2,48% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 14 | 64,29% | +1,63% | -3,08% | -5,48% | +2,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 5 | 80,00% | +2,87% | -4,77% | -7,28% | +2,28% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 7 | 42,86% | -1,38% | -4,50% | -7,00% | +2,58% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 26 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 25 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 27 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 11 | 18,18% | -0,71% |
| BTC | BREVE | Famiglia statistica | 78 | 50,00% | +0,03% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 63 | 38,10% | -0,32% |
| BTC | SETTIMANALE | Classic technical | 4 | 25,00% | +0,15% |
| BTC | SETTIMANALE | Famiglia statistica | 62 | 43,55% | +0,08% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 50 | 48,00% | -0,08% |
| BTC | SWING | Famiglia statistica | 21 | 47,62% | +0,10% |
| BTC | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% |
| BTC | SWING | Tecnico | 17 | 35,29% | -0,17% |
| DOGE | BREVE | Classic technical | 60 | 43,33% | -0,04% |
| DOGE | BREVE | Famiglia statistica | 78 | 51,28% | +0,08% |
| DOGE | BREVE | Microstruttura exchange | 6 | 100,00% | +3,99% |
| DOGE | BREVE | Tecnico | 78 | 53,85% | +0,36% |
| DOGE | SETTIMANALE | Classic technical | 52 | 57,69% | +1,01% |
| DOGE | SETTIMANALE | Famiglia statistica | 62 | 61,29% | +0,73% |
| DOGE | SETTIMANALE | Microstruttura exchange | 6 | 100,00% | +1,18% |
| DOGE | SETTIMANALE | Tecnico | 62 | 64,52% | +1,39% |
| DOGE | SWING | Classic technical | 19 | 89,47% | +3,34% |
| DOGE | SWING | Famiglia statistica | 21 | 90,48% | +3,50% |
| DOGE | SWING | Tecnico | 21 | 90,48% | +3,50% |
| SOL | BREVE | Classic technical | 54 | 50,00% | +0,16% |
| SOL | BREVE | Famiglia statistica | 66 | 48,48% | -0,34% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 78 | 47,44% | +0,06% |
| SOL | SETTIMANALE | Classic technical | 38 | 71,05% | +1,44% |
| SOL | SETTIMANALE | Famiglia statistica | 50 | 44,00% | -0,72% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 3 | 0,00% | -5,22% |
| SOL | SETTIMANALE | Tecnico | 62 | 58,06% | +0,80% |
| SOL | SWING | Classic technical | 6 | 100,00% | +3,29% |
| SOL | SWING | Famiglia statistica | 15 | 73,33% | +1,47% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% |
| SOL | SWING | Tecnico | 21 | 57,14% | +0,63% |

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
