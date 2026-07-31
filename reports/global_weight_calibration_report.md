# Calibrazione pesi Global Confluence

Generato: 2026-07-31 05:15 UTC

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
| BTC | 23 | FEEDBACK RAPIDO | 22 | 0 | 0 | 0 | Famiglia statistica | 1g | 50,00% | +0,03% | feedback rapido: utile da osservare, non da pesare |
| SOL | 23 | FEEDBACK RAPIDO | 22 | 0 | 0 | 0 | Tecnico | 1g | 54,55% | +0,04% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 23 | FEEDBACK RAPIDO | 22 | 0 | 0 | 0 | Famiglia statistica | 1g | 54,55% | +0,32% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 2 | 0,00% | -0,42% | +0,42% | -0,14% | +0,79% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 22 | 50,00% | +0,03% | +0,03% | -0,25% | +0,62% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 18 | 33,33% | -0,45% | +0,19% | -0,11% | +0,77% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 2 | 0,00% | -0,76% | +0,76% | +0,33% | +1,77% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 21 | 47,62% | +0,10% | +0,10% | -0,40% | +0,93% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 17 | 35,29% | -0,48% | +0,35% | -0,17% | +1,18% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 1 | 0,00% | -1,53% | +1,53% | -0,28% | +2,98% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 20 | 55,00% | +0,10% | +0,10% | -1,40% | +1,84% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 16 | 37,50% | -0,13% | +0,58% | -1,09% | +2,23% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 18 | 38,89% | +0,29% | +0,29% | -2,15% | +2,56% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 15 | 53,33% | -0,25% | +0,48% | -1,92% | +2,80% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 16 | 56,25% | +0,48% | +0,48% | -2,33% | +3,05% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 13 | 46,15% | -0,22% | +1,13% | -2,02% | +3,40% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 13 | 61,54% | +1,23% | +1,23% | -2,19% | +4,17% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 11 | 36,36% | -0,47% | +1,56% | -1,91% | +4,53% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 9 | 77,78% | +1,35% | +1,35% | -2,26% | +5,20% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 8 | 37,50% | -0,20% | +1,24% | -2,13% | +5,26% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 2 | 100,00% | +0,92% | +0,92% | -2,80% | +5,29% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 1 | 0,00% | -1,07% | +1,07% | -2,32% | +5,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 18 | 44,44% | -0,13% | +0,13% | -0,29% | +0,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 22 | 54,55% | +0,32% | -0,23% | -0,65% | +0,49% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 22 | 54,55% | +0,23% | -0,23% | -0,65% | +0,49% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 17 | 52,94% | -0,12% | +0,12% | -0,55% | +1,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 21 | 47,62% | +0,02% | -0,43% | -1,06% | +0,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 21 | 61,90% | +0,43% | -0,43% | -1,06% | +0,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 17 | 41,18% | +0,19% | -0,19% | -2,00% | +2,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 20 | 50,00% | -0,06% | -0,69% | -2,30% | +1,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 20 | 50,00% | +0,69% | -0,69% | -2,30% | +1,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 16 | 56,25% | +0,61% | -0,61% | -3,04% | +2,79% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 18 | 61,11% | +0,47% | -0,95% | -3,24% | +2,50% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 18 | 61,11% | +0,95% | -0,95% | -3,24% | +2,50% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 15 | 66,67% | +1,36% | -1,36% | -3,82% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 16 | 68,75% | +1,34% | -1,34% | -3,82% | +2,55% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,51% | +1,51% | +0,10% | +6,93% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 16 | 68,75% | +1,34% | -1,34% | -3,82% | +2,55% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 12 | 66,67% | +1,64% | -1,64% | -4,45% | +2,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 13 | 69,23% | +1,98% | -1,98% | -4,65% | +2,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 13 | 69,23% | +1,98% | -1,98% | -4,65% | +2,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 8 | 75,00% | +2,77% | -2,77% | -5,65% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 9 | 77,78% | +2,97% | -2,97% | -5,87% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 9 | 77,78% | +2,97% | -2,97% | -5,87% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 2 | 100,00% | +4,79% | -4,79% | -6,91% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 2 | 100,00% | +4,79% | -4,79% | -6,91% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 2 | 100,00% | +4,79% | -4,79% | -6,91% | +2,87% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 14 | 57,14% | +0,14% | -0,14% | -0,53% | +0,52% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 18 | 61,11% | -0,12% | -0,60% | -0,92% | +0,20% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 22 | 54,55% | +0,04% | -0,21% | -0,61% | +0,55% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 13 | 46,15% | +0,24% | -0,24% | -0,67% | +0,39% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 17 | 47,06% | -0,54% | -0,81% | -1,48% | +0,17% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 21 | 38,10% | -0,05% | -0,49% | -1,09% | +0,68% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 12 | 41,67% | +0,26% | -0,26% | -2,21% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 16 | 37,50% | -0,67% | -1,15% | -2,89% | +1,46% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 20 | 45,00% | +0,20% | -0,80% | -2,43% | +1,85% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 10 | 70,00% | +0,56% | -0,56% | -2,81% | +2,98% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 14 | 42,86% | -0,92% | -1,42% | -3,73% | +2,24% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 18 | 55,56% | +0,21% | -1,12% | -3,40% | +2,59% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 8 | 62,50% | +1,50% | -1,50% | -3,66% | +2,98% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 12 | 58,33% | -0,13% | -2,04% | -4,50% | +2,24% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 16 | 43,75% | +0,24% | -1,52% | -4,09% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 5 | 80,00% | +1,68% | -1,68% | -3,43% | +4,11% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 9 | 44,44% | -0,55% | -1,61% | -4,66% | +2,66% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 13 | 61,54% | +1,05% | -1,42% | -4,39% | +3,02% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 2 | 100,00% | +2,40% | -2,40% | -4,20% | +4,20% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 7 | 71,43% | +0,71% | -2,21% | -4,83% | +2,83% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 9 | 44,44% | +0,23% | -2,49% | -4,68% | +2,94% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 2 | 100,00% | +5,29% | -5,29% | -7,04% | +1,74% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 2 | 0,00% | -5,29% | -5,29% | -7,04% | +1,74% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 21 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 20 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 22 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 5 | 0,00% | -0,78% |
| BTC | BREVE | Famiglia statistica | 63 | 50,79% | +0,07% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 51 | 35,29% | -0,36% |
| BTC | SETTIMANALE | Famiglia statistica | 47 | 51,06% | +0,61% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 39 | 46,15% | -0,30% |
| BTC | SWING | Famiglia statistica | 11 | 81,82% | +1,27% |
| BTC | SWING | Tecnico | 9 | 33,33% | -0,30% |
| DOGE | BREVE | Classic technical | 52 | 46,15% | -0,02% |
| DOGE | BREVE | Famiglia statistica | 63 | 50,79% | +0,10% |
| DOGE | BREVE | Microstruttura exchange | 6 | 100,00% | +3,99% |
| DOGE | BREVE | Tecnico | 63 | 55,56% | +0,44% |
| DOGE | SETTIMANALE | Classic technical | 43 | 62,79% | +1,16% |
| DOGE | SETTIMANALE | Famiglia statistica | 47 | 65,96% | +1,18% |
| DOGE | SETTIMANALE | Microstruttura exchange | 3 | 100,00% | +1,34% |
| DOGE | SETTIMANALE | Tecnico | 47 | 65,96% | +1,37% |
| DOGE | SWING | Classic technical | 10 | 80,00% | +3,18% |
| DOGE | SWING | Famiglia statistica | 11 | 81,82% | +3,30% |
| DOGE | SWING | Tecnico | 11 | 81,82% | +3,30% |
| SOL | BREVE | Classic technical | 39 | 48,72% | +0,21% |
| SOL | BREVE | Famiglia statistica | 51 | 49,02% | -0,43% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 63 | 46,03% | +0,06% |
| SOL | SETTIMANALE | Classic technical | 23 | 69,57% | +1,13% |
| SOL | SETTIMANALE | Famiglia statistica | 35 | 48,57% | -0,55% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 3 | 0,00% | -5,22% |
| SOL | SETTIMANALE | Tecnico | 47 | 53,19% | +0,45% |
| SOL | SWING | Classic technical | 2 | 100,00% | +2,40% |
| SOL | SWING | Famiglia statistica | 9 | 77,78% | +1,73% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Tecnico | 11 | 36,36% | -0,77% |

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
