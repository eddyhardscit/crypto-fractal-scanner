# Calibrazione pesi Global Confluence

Generato: 2026-07-30 05:15 UTC

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
| BTC | 22 | FEEDBACK RAPIDO | 21 | 0 | 0 | 0 | Famiglia statistica | 1g | 47,62% | -0,00% | feedback rapido: utile da osservare, non da pesare |
| SOL | 22 | FEEDBACK RAPIDO | 21 | 0 | 0 | 0 | Tecnico | 1g | 57,14% | +0,08% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 22 | FEEDBACK RAPIDO | 21 | 0 | 0 | 0 | Tecnico | 1g | 57,14% | +0,27% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 2 | 0,00% | -0,42% | +0,42% | -0,14% | +0,79% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 21 | 47,62% | -0,00% | -0,00% | -0,28% | +0,55% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 17 | 35,29% | -0,43% | +0,16% | -0,14% | +0,69% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 1 | 0,00% | -0,84% | +0,84% | +0,26% | +1,41% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 20 | 45,00% | +0,07% | +0,07% | -0,44% | +0,87% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 16 | 37,50% | -0,46% | +0,32% | -0,21% | +1,12% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 19 | 52,63% | +0,02% | +0,02% | -1,46% | +1,78% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 15 | 40,00% | -0,04% | +0,52% | -1,15% | +2,18% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 17 | 41,18% | +0,32% | +0,32% | -2,12% | +2,60% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 14 | 57,14% | -0,26% | +0,52% | -1,86% | +2,87% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 15 | 60,00% | +0,61% | +0,61% | -2,22% | +3,21% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 12 | 41,67% | -0,36% | +1,35% | -1,86% | +3,64% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 12 | 66,67% | +1,47% | +1,47% | -2,02% | +4,36% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 11 | 36,36% | -0,47% | +1,56% | -1,91% | +4,53% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 8 | 75,00% | +1,38% | +1,38% | -2,36% | +5,21% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 7 | 42,86% | -0,07% | +1,25% | -2,23% | +5,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 1 | 100,00% | +1,07% | +1,07% | -2,32% | +5,81% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 1 | 0,00% | -1,07% | +1,07% | -2,32% | +5,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 17 | 47,06% | -0,11% | +0,11% | -0,33% | +0,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 21 | 52,38% | +0,31% | -0,27% | -0,70% | +0,43% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 21 | 57,14% | +0,27% | -0,27% | -0,70% | +0,43% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 17 | 52,94% | -0,12% | +0,12% | -0,55% | +1,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 20 | 50,00% | +0,06% | -0,41% | -1,05% | +0,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 20 | 60,00% | +0,41% | -0,41% | -1,05% | +0,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 16 | 43,75% | +0,22% | -0,22% | -2,05% | +2,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 19 | 47,37% | -0,07% | -0,73% | -2,36% | +1,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 19 | 52,63% | +0,73% | -0,73% | -2,36% | +1,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 16 | 56,25% | +0,61% | -0,61% | -3,04% | +2,79% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 17 | 64,71% | +0,77% | -0,74% | -3,09% | +2,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 17 | 58,82% | +0,74% | -0,74% | -3,09% | +2,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 14 | 71,43% | +1,56% | -1,56% | -4,10% | +2,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 15 | 73,33% | +1,53% | -1,53% | -4,08% | +2,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 15 | 73,33% | +1,53% | -1,53% | -4,08% | +2,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 11 | 63,64% | +1,45% | -1,45% | -4,29% | +2,65% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 12 | 66,67% | +1,83% | -1,83% | -4,52% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 12 | 66,67% | +1,83% | -1,83% | -4,52% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 7 | 71,43% | +2,75% | -2,75% | -5,69% | +2,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 8 | 75,00% | +2,97% | -2,97% | -5,93% | +2,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 8 | 75,00% | +2,97% | -2,97% | -5,93% | +2,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 1 | 100,00% | +4,41% | -4,41% | -6,26% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 1 | 100,00% | +4,41% | -4,41% | -6,26% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 1 | 100,00% | +4,41% | -4,41% | -6,26% | +3,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 13 | 61,54% | +0,21% | -0,21% | -0,60% | +0,40% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 17 | 58,82% | -0,17% | -0,68% | -1,00% | +0,08% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 21 | 57,14% | +0,08% | -0,26% | -0,65% | +0,48% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 12 | 50,00% | +0,32% | -0,32% | -0,75% | +0,24% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 16 | 43,75% | -0,62% | -0,91% | -1,59% | +0,04% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 20 | 40,00% | -0,02% | -0,56% | -1,16% | +0,61% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 11 | 45,45% | +0,38% | -0,38% | -2,30% | +1,77% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 15 | 33,33% | -0,78% | -1,29% | -3,01% | +1,39% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 19 | 47,37% | +0,27% | -0,89% | -2,50% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 9 | 66,67% | +0,46% | -0,46% | -2,72% | +2,97% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 13 | 46,15% | -0,88% | -1,42% | -3,74% | +2,17% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 17 | 52,94% | +0,13% | -1,10% | -3,38% | +2,56% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 7 | 57,14% | +1,40% | -1,40% | -3,55% | +3,10% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 11 | 63,64% | +0,06% | -2,02% | -4,51% | +2,25% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 15 | 40,00% | +0,11% | -1,47% | -4,07% | +2,67% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 5 | 80,00% | +1,68% | -1,68% | -3,43% | +4,11% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 8 | 50,00% | +0,05% | -1,14% | -4,31% | +2,92% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 12 | 58,33% | +0,69% | -1,10% | -4,13% | +3,22% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 1 | 100,00% | +3,36% | -3,36% | -4,76% | +3,59% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 6 | 66,67% | +0,59% | -2,34% | -5,03% | +2,50% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 8 | 37,50% | +0,08% | -2,62% | -4,81% | +2,71% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 1 | 100,00% | +5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 20 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 19 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 21 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 3 | 0,00% | -0,56% |
| BTC | BREVE | Famiglia statistica | 60 | 48,33% | +0,03% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 48 | 37,50% | -0,32% |
| BTC | SETTIMANALE | Famiglia statistica | 44 | 54,55% | +0,73% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 37 | 45,95% | -0,35% |
| BTC | SWING | Famiglia statistica | 9 | 77,78% | +1,35% |
| BTC | SWING | Tecnico | 8 | 37,50% | -0,20% |
| DOGE | BREVE | Classic technical | 50 | 48,00% | -0,01% |
| DOGE | BREVE | Famiglia statistica | 60 | 50,00% | +0,11% |
| DOGE | BREVE | Microstruttura exchange | 6 | 100,00% | +3,99% |
| DOGE | BREVE | Tecnico | 60 | 56,67% | +0,46% |
| DOGE | SETTIMANALE | Classic technical | 41 | 63,41% | +1,16% |
| DOGE | SETTIMANALE | Famiglia statistica | 44 | 68,18% | +1,32% |
| DOGE | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% |
| DOGE | SETTIMANALE | Tecnico | 44 | 65,91% | +1,31% |
| DOGE | SWING | Classic technical | 8 | 75,00% | +2,96% |
| DOGE | SWING | Famiglia statistica | 9 | 77,78% | +3,13% |
| DOGE | SWING | Tecnico | 9 | 77,78% | +3,13% |
| SOL | BREVE | Classic technical | 36 | 52,78% | +0,30% |
| SOL | BREVE | Famiglia statistica | 48 | 45,83% | -0,51% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 60 | 48,33% | +0,11% |
| SOL | SETTIMANALE | Classic technical | 21 | 66,67% | +1,06% |
| SOL | SETTIMANALE | Famiglia statistica | 32 | 53,12% | -0,32% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -5,16% |
| SOL | SETTIMANALE | Tecnico | 44 | 50,00% | +0,28% |
| SOL | SWING | Classic technical | 1 | 100,00% | +3,36% |
| SOL | SWING | Famiglia statistica | 7 | 71,43% | +1,34% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Tecnico | 9 | 33,33% | -0,58% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 4 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 6 | in attesa di controlli maturati |
| BTC | SWING | 6 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 1 | in attesa di controlli maturati |
| SOL | SWING | 3 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 5 | in attesa di controlli maturati |
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
