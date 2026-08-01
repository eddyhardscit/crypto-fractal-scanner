# Calibrazione pesi Global Confluence

Generato: 2026-08-01 05:15 UTC

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
| BTC | 24 | FEEDBACK RAPIDO | 23 | 0 | 0 | 0 | Famiglia statistica | 1g | 47,83% | -0,06% | feedback rapido: utile da osservare, non da pesare |
| SOL | 24 | FEEDBACK RAPIDO | 23 | 0 | 0 | 0 | Tecnico | 1g | 56,52% | +0,10% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 24 | FEEDBACK RAPIDO | 23 | 0 | 0 | 0 | Famiglia statistica | 1g | 56,52% | +0,31% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 2 | 0,00% | -0,42% | +0,42% | -0,14% | +0,79% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 23 | 47,83% | -0,06% | -0,06% | -0,34% | +0,51% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 18 | 33,33% | -0,45% | +0,19% | -0,11% | +0,77% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 2 | 0,00% | -0,76% | +0,76% | +0,33% | +1,77% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 22 | 45,45% | +0,04% | +0,04% | -0,46% | +0,83% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 18 | 38,89% | -0,37% | +0,25% | -0,26% | +1,04% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 2 | 50,00% | -0,10% | +0,10% | -0,99% | +2,40% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 21 | 52,38% | +0,03% | +0,03% | -1,42% | +1,84% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 17 | 41,18% | -0,05% | +0,47% | -1,13% | +2,20% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 19 | 36,84% | +0,09% | +0,09% | -2,25% | +2,40% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 15 | 53,33% | -0,25% | +0,48% | -1,92% | +2,80% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 17 | 52,94% | +0,36% | +0,36% | -2,32% | +3,01% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 14 | 50,00% | -0,09% | +0,94% | -2,03% | +3,33% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 14 | 57,14% | +0,80% | +0,80% | -2,41% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 11 | 36,36% | -0,47% | +1,56% | -1,91% | +4,53% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 10 | 70,00% | +1,09% | +1,09% | -2,22% | +5,16% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 9 | 44,44% | -0,04% | +0,96% | -2,10% | +5,20% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 3 | 66,67% | +0,10% | +0,10% | -3,05% | +5,02% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 2 | 50,00% | +0,23% | -0,23% | -2,93% | +5,15% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 19 | 42,11% | -0,13% | +0,13% | -0,32% | +0,74% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 23 | 56,52% | +0,31% | -0,21% | -0,66% | +0,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 23 | 52,17% | +0,21% | -0,21% | -0,66% | +0,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 18 | 50,00% | -0,15% | +0,15% | -0,53% | +1,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 22 | 50,00% | +0,05% | -0,38% | -1,02% | +0,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 22 | 59,09% | +0,38% | -0,38% | -1,02% | +0,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 17 | 41,18% | +0,19% | -0,19% | -2,00% | +2,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 21 | 47,62% | -0,09% | -0,69% | -2,26% | +1,85% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 21 | 52,38% | +0,69% | -0,69% | -2,26% | +1,85% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 16 | 56,25% | +0,61% | -0,61% | -3,04% | +2,79% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 19 | 57,89% | +0,24% | -1,11% | -3,35% | +2,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 19 | 63,16% | +1,11% | -1,11% | -3,35% | +2,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 16 | 62,50% | +1,22% | -1,22% | -3,61% | +2,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 17 | 70,59% | +1,31% | -1,21% | -3,63% | +2,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 17 | 64,71% | +1,21% | -1,21% | -3,63% | +2,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 13 | 69,23% | +1,84% | -1,84% | -4,62% | +2,41% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 14 | 71,43% | +2,14% | -2,14% | -4,79% | +2,28% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 14 | 71,43% | +2,14% | -2,14% | -4,79% | +2,28% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 9 | 77,78% | +2,81% | -2,81% | -5,65% | +2,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 10 | 80,00% | +2,98% | -2,98% | -5,84% | +2,51% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 10 | 80,00% | +2,98% | -2,98% | -5,84% | +2,51% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 3 | 100,00% | +4,95% | -4,95% | -7,18% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 3 | 100,00% | +4,95% | -4,95% | -7,18% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 3 | 100,00% | +4,95% | -4,95% | -7,18% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 15 | 60,00% | +0,21% | -0,21% | -0,61% | +0,41% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 19 | 57,89% | -0,18% | -0,63% | -0,96% | +0,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 23 | 56,52% | +0,10% | -0,25% | -0,65% | +0,48% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 14 | 50,00% | +0,25% | -0,25% | -0,68% | +0,33% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 18 | 44,44% | -0,53% | -0,79% | -1,45% | +0,13% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 22 | 40,91% | -0,03% | -0,49% | -1,08% | +0,63% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 13 | 46,15% | +0,28% | -0,28% | -2,11% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 17 | 35,29% | -0,66% | -1,11% | -2,78% | +1,48% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 21 | 47,62% | +0,21% | -0,78% | -2,36% | +1,85% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 11 | 72,73% | +0,89% | -0,89% | -3,03% | +2,52% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 15 | 40,00% | -1,14% | -1,61% | -3,84% | +1,95% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 19 | 57,89% | +0,42% | -1,29% | -3,49% | +2,35% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 9 | 66,67% | +1,49% | -1,49% | -3,52% | +3,13% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 13 | 53,85% | -0,23% | -1,99% | -4,34% | +2,40% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 17 | 47,06% | +0,31% | -1,51% | -3,99% | +2,74% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 6 | 83,33% | +2,41% | -2,41% | -4,03% | +3,56% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 10 | 50,00% | +0,11% | -2,05% | -4,90% | +2,48% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 14 | 64,29% | +1,41% | -1,75% | -4,57% | +2,86% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 3 | 100,00% | +2,40% | -2,40% | -3,93% | +4,49% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 7 | 71,43% | +0,71% | -2,21% | -4,83% | +2,83% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 10 | 50,00% | +0,45% | -2,48% | -4,55% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 2 | 100,00% | +5,29% | -5,29% | -7,04% | +1,74% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 3 | 0,00% | -5,53% | -5,53% | -7,02% | +1,62% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 22 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 21 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 23 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 6 | 16,67% | -0,43% |
| BTC | BREVE | Famiglia statistica | 66 | 48,48% | -0,00% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 53 | 37,74% | -0,29% |
| BTC | SETTIMANALE | Famiglia statistica | 50 | 48,00% | +0,38% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 40 | 47,50% | -0,26% |
| BTC | SWING | Famiglia statistica | 13 | 69,23% | +0,86% |
| BTC | SWING | Tecnico | 11 | 45,45% | +0,01% |
| DOGE | BREVE | Classic technical | 54 | 44,44% | -0,04% |
| DOGE | BREVE | Famiglia statistica | 66 | 51,52% | +0,10% |
| DOGE | BREVE | Microstruttura exchange | 6 | 100,00% | +3,99% |
| DOGE | BREVE | Tecnico | 66 | 54,55% | +0,42% |
| DOGE | SETTIMANALE | Classic technical | 45 | 62,22% | +1,18% |
| DOGE | SETTIMANALE | Famiglia statistica | 50 | 66,00% | +1,14% |
| DOGE | SETTIMANALE | Microstruttura exchange | 4 | 100,00% | +1,23% |
| DOGE | SETTIMANALE | Tecnico | 50 | 66,00% | +1,43% |
| DOGE | SWING | Classic technical | 12 | 83,33% | +3,34% |
| DOGE | SWING | Famiglia statistica | 13 | 84,62% | +3,43% |
| DOGE | SWING | Tecnico | 13 | 84,62% | +3,43% |
| SOL | BREVE | Classic technical | 42 | 52,38% | +0,25% |
| SOL | BREVE | Famiglia statistica | 54 | 46,30% | -0,45% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 66 | 48,48% | +0,09% |
| SOL | SETTIMANALE | Classic technical | 26 | 73,08% | +1,45% |
| SOL | SETTIMANALE | Famiglia statistica | 38 | 47,37% | -0,50% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 3 | 0,00% | -5,22% |
| SOL | SETTIMANALE | Tecnico | 50 | 56,00% | +0,66% |
| SOL | SWING | Classic technical | 3 | 100,00% | +2,40% |
| SOL | SWING | Famiglia statistica | 9 | 77,78% | +1,73% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Tecnico | 13 | 38,46% | -0,93% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 6 | in attesa di controlli maturati |
| BTC | SWING | 6 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SWING | 3 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 4 | in attesa di controlli maturati |
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
