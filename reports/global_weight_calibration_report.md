# Calibrazione pesi Global Confluence

Generato: 2026-08-02 05:15 UTC

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
| BTC | 25 | FEEDBACK RAPIDO | 24 | 0 | 0 | 0 | Famiglia statistica | 1g | 50,00% | -0,03% | feedback rapido: utile da osservare, non da pesare |
| SOL | 25 | FEEDBACK RAPIDO | 24 | 0 | 0 | 0 | Tecnico | 1g | 54,17% | +0,08% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 25 | FEEDBACK RAPIDO | 24 | 0 | 0 | 0 | Famiglia statistica | 1g | 58,33% | +0,30% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 3 | 0,00% | -0,46% | +0,46% | -0,25% | +0,77% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 24 | 50,00% | -0,03% | -0,03% | -0,35% | +0,52% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 19 | 31,58% | -0,45% | +0,21% | -0,13% | +0,77% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 2 | 0,00% | -0,76% | +0,76% | +0,33% | +1,77% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 23 | 43,48% | -0,03% | -0,03% | -0,54% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 18 | 38,89% | -0,37% | +0,25% | -0,26% | +1,04% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 2 | 50,00% | -0,10% | +0,10% | -0,99% | +2,40% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 22 | 50,00% | -0,01% | -0,01% | -1,46% | +1,86% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 18 | 44,44% | +0,00% | +0,40% | -1,20% | +2,20% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 1 | 0,00% | -0,02% | +0,02% | -1,53% | +3,07% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 20 | 40,00% | +0,09% | +0,09% | -2,21% | +2,44% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 16 | 50,00% | -0,24% | +0,45% | -1,90% | +2,82% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 18 | 50,00% | +0,25% | +0,25% | -2,36% | +2,95% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 15 | 46,67% | -0,20% | +0,77% | -2,10% | +3,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 15 | 53,33% | +0,54% | +0,54% | -2,56% | +3,66% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 12 | 41,67% | -0,17% | +1,17% | -2,13% | +4,20% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 11 | 63,64% | +0,80% | +0,80% | -2,34% | +4,99% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 10 | 40,00% | -0,24% | +0,65% | -2,25% | +5,01% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 4 | 50,00% | -0,09% | -0,09% | -3,09% | +4,98% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 3 | 33,33% | -0,07% | -0,38% | -3,03% | +5,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 20 | 40,00% | -0,13% | +0,13% | -0,37% | +0,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 24 | 58,33% | +0,30% | -0,20% | -0,69% | +0,46% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 24 | 50,00% | +0,20% | -0,20% | -0,69% | +0,46% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 19 | 47,37% | -0,16% | +0,16% | -0,57% | +1,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 23 | 52,17% | +0,06% | -0,35% | -1,03% | +0,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 23 | 56,52% | +0,35% | -0,35% | -1,03% | +0,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 18 | 38,89% | +0,14% | -0,14% | -1,96% | +2,34% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 22 | 50,00% | -0,05% | -0,62% | -2,22% | +1,85% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 22 | 50,00% | +0,62% | -0,62% | -2,22% | +1,85% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 17 | 52,94% | +0,55% | -0,55% | -2,96% | +2,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 20 | 60,00% | +0,25% | -1,03% | -3,27% | +2,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 20 | 60,00% | +1,03% | -1,03% | -3,27% | +2,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 16 | 62,50% | +1,22% | -1,22% | -3,61% | +2,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 18 | 66,67% | +0,99% | -1,39% | -3,79% | +2,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 18 | 66,67% | +1,39% | -1,39% | -3,79% | +2,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 14 | 71,43% | +1,92% | -1,92% | -4,69% | +2,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 15 | 73,33% | +2,19% | -2,19% | -4,84% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 15 | 73,33% | +2,19% | -2,19% | -4,84% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 10 | 80,00% | +2,84% | -2,84% | -5,65% | +2,65% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 11 | 81,82% | +2,99% | -2,99% | -5,83% | +2,45% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 11 | 81,82% | +2,99% | -2,99% | -5,83% | +2,45% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 4 | 100,00% | +4,62% | -4,62% | -6,94% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 4 | 100,00% | +4,62% | -4,62% | -6,94% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 4 | 100,00% | +4,62% | -4,62% | -6,94% | +2,68% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 16 | 56,25% | +0,17% | -0,17% | -0,68% | +0,41% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 20 | 60,00% | -0,15% | -0,58% | -1,00% | +0,14% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 24 | 54,17% | +0,08% | -0,23% | -0,70% | +0,47% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 15 | 53,33% | +0,29% | -0,29% | -0,83% | +0,25% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 19 | 42,11% | -0,55% | -0,79% | -1,53% | +0,08% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 23 | 43,48% | +0,01% | -0,51% | -1,16% | +0,57% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 14 | 50,00% | +0,26% | -0,26% | -2,11% | +1,86% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 18 | 33,33% | -0,62% | -1,05% | -2,74% | +1,53% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 22 | 50,00% | +0,21% | -0,75% | -2,35% | +1,87% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 12 | 66,67% | +0,80% | -0,80% | -2,94% | +2,52% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 16 | 43,75% | -1,06% | -1,50% | -3,72% | +1,99% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 20 | 55,00% | +0,39% | -1,21% | -3,42% | +2,35% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 10 | 70,00% | +1,57% | -1,57% | -3,60% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 14 | 50,00% | -0,37% | -2,01% | -4,34% | +2,45% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 18 | 50,00% | +0,42% | -1,55% | -4,01% | +2,75% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 7 | 85,71% | +2,75% | -2,75% | -4,43% | +3,10% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 11 | 45,45% | -0,34% | -2,31% | -5,07% | +2,28% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 15 | 66,67% | +1,63% | -1,96% | -4,73% | +2,69% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 4 | 100,00% | +2,66% | -2,66% | -4,32% | +4,25% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 8 | 75,00% | +1,05% | -2,37% | -4,91% | +2,92% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 11 | 54,55% | +0,72% | -2,57% | -4,63% | +3,19% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 3 | 100,00% | +4,86% | -4,86% | -6,70% | +2,20% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 4 | 0,00% | -5,15% | -5,15% | -6,77% | +2,00% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 23 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 22 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 24 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 7 | 14,29% | -0,44% |
| BTC | BREVE | Famiglia statistica | 69 | 47,83% | -0,03% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 55 | 38,18% | -0,28% |
| BTC | SETTIMANALE | Classic technical | 1 | 0,00% | -0,02% |
| BTC | SETTIMANALE | Famiglia statistica | 53 | 47,17% | +0,27% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 43 | 46,51% | -0,21% |
| BTC | SWING | Famiglia statistica | 15 | 60,00% | +0,56% |
| BTC | SWING | Tecnico | 13 | 38,46% | -0,20% |
| DOGE | BREVE | Classic technical | 57 | 42,11% | -0,05% |
| DOGE | BREVE | Famiglia statistica | 69 | 53,62% | +0,11% |
| DOGE | BREVE | Microstruttura exchange | 6 | 100,00% | +3,99% |
| DOGE | BREVE | Tecnico | 69 | 52,17% | +0,39% |
| DOGE | SETTIMANALE | Classic technical | 47 | 61,70% | +1,18% |
| DOGE | SETTIMANALE | Famiglia statistica | 53 | 66,04% | +1,05% |
| DOGE | SETTIMANALE | Microstruttura exchange | 4 | 100,00% | +1,23% |
| DOGE | SETTIMANALE | Tecnico | 53 | 66,04% | +1,48% |
| DOGE | SWING | Classic technical | 14 | 85,71% | +3,35% |
| DOGE | SWING | Famiglia statistica | 15 | 86,67% | +3,43% |
| DOGE | SWING | Tecnico | 15 | 86,67% | +3,43% |
| SOL | BREVE | Classic technical | 45 | 53,33% | +0,24% |
| SOL | BREVE | Famiglia statistica | 57 | 45,61% | -0,43% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 69 | 49,28% | +0,09% |
| SOL | SETTIMANALE | Classic technical | 29 | 72,41% | +1,54% |
| SOL | SETTIMANALE | Famiglia statistica | 41 | 46,34% | -0,63% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 3 | 0,00% | -5,22% |
| SOL | SETTIMANALE | Tecnico | 53 | 56,60% | +0,75% |
| SOL | SWING | Classic technical | 4 | 100,00% | +2,66% |
| SOL | SWING | Famiglia statistica | 11 | 81,82% | +2,09% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Tecnico | 15 | 40,00% | -0,84% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 5 | in attesa di controlli maturati |
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
