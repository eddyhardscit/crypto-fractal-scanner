# Calibrazione pesi Global Confluence

Generato: 2026-08-08 05:19 UTC

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
| BTC | 31 | PRIMA CALIBRAZIONE | 30 | 1 | 0 | 0 | Famiglia statistica | 1g | 53,33% | +0,06% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 31 | PRIMA CALIBRAZIONE | 30 | 1 | 0 | 0 | Tecnico | 1g | 50,00% | +0,01% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 31 | PRIMA CALIBRAZIONE | 30 | 1 | 0 | 0 | Famiglia statistica | 1g | 56,67% | +0,24% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 4 | 0,00% | -0,76% | +0,76% | +0,03% | +1,12% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 30 | 53,33% | +0,06% | +0,06% | -0,28% | +0,58% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 25 | 36,00% | -0,37% | +0,26% | -0,10% | +0,78% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 4 | 25,00% | -0,86% | +0,86% | +0,50% | +1,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 29 | 48,28% | +0,12% | +0,12% | -0,37% | +0,81% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 24 | 45,83% | -0,31% | +0,37% | -0,11% | +1,06% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 4 | 25,00% | -1,18% | +1,18% | -0,41% | +2,46% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 28 | 57,14% | +0,17% | +0,17% | -1,32% | +1,76% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 23 | 39,13% | -0,28% | +0,64% | -1,01% | +2,14% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 4 | 25,00% | -1,14% | +1,14% | -1,16% | +2,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 26 | 42,31% | +0,28% | +0,28% | -2,12% | +2,39% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 21 | 47,62% | -0,45% | +0,61% | -1,80% | +2,78% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 3 | 0,00% | -1,41% | +1,41% | -1,92% | +2,79% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 24 | 54,17% | +0,25% | +0,25% | -2,46% | +2,69% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 19 | 36,84% | -0,45% | +0,90% | -2,10% | +3,11% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Classic technical | 2 | 0,00% | -1,45% | +1,45% | -2,23% | +2,64% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 21 | 47,62% | +0,27% | +0,27% | -2,79% | +3,10% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 17 | 41,18% | -0,05% | +0,72% | -2,41% | +3,56% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 17 | 47,06% | -0,01% | -0,01% | -3,08% | +3,80% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 14 | 50,00% | +0,07% | +0,22% | -2,72% | +4,14% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 10 | 60,00% | +0,50% | +0,50% | -2,49% | +5,16% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 9 | 11,11% | -0,72% | +0,47% | -2,41% | +5,20% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 1 | 100,00% | +2,74% | +2,74% | -2,32% | +5,81% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 1 | 0,00% | -2,74% | +2,74% | -2,32% | +5,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 21 | 38,10% | -0,20% | +0,20% | -0,32% | +0,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 30 | 56,67% | +0,24% | -0,16% | -0,64% | +0,47% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,60% | +2,65% | +1,48% | +2,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 29 | 48,28% | +0,12% | -0,12% | -0,61% | +0,51% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 20 | 50,00% | -0,13% | +0,13% | -0,57% | +1,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 29 | 48,28% | -0,01% | -0,33% | -0,96% | +0,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 28 | 60,71% | +0,35% | -0,35% | -0,97% | +0,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 20 | 40,00% | +0,14% | -0,14% | -1,99% | +2,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 28 | 50,00% | -0,10% | -0,55% | -2,13% | +1,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 28 | 50,00% | +0,55% | -0,55% | -2,13% | +1,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 20 | 55,00% | +0,45% | -0,45% | -2,87% | +2,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 26 | 53,85% | +0,12% | -0,87% | -3,08% | +1,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 26 | 61,54% | +0,87% | -0,87% | -3,08% | +1,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 20 | 55,00% | +1,01% | -1,01% | -3,42% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 24 | 62,50% | +0,50% | -1,28% | -3,72% | +2,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 24 | 62,50% | +1,28% | -1,28% | -3,72% | +2,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 17 | 64,71% | +1,53% | -1,53% | -4,24% | +2,85% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 21 | 57,14% | +1,04% | -1,97% | -4,62% | +2,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 21 | 71,43% | +1,97% | -1,97% | -4,62% | +2,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 16 | 75,00% | +2,59% | -2,59% | -5,33% | +2,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 17 | 82,35% | +2,81% | -2,70% | -5,47% | +2,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 17 | 76,47% | +2,70% | -2,70% | -5,47% | +2,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 9 | 100,00% | +4,00% | -4,00% | -6,45% | +2,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 10 | 100,00% | +4,14% | -4,14% | -6,62% | +2,51% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 10 | 100,00% | +4,14% | -4,14% | -6,62% | +2,51% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 1 | 100,00% | +3,75% | -3,75% | -6,69% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 1 | 100,00% | +3,75% | -3,75% | -6,69% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 1 | 100,00% | +3,75% | -3,75% | -6,69% | +3,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 21 | 47,62% | -0,04% | +0,04% | -0,54% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 26 | 61,54% | -0,06% | -0,39% | -0,87% | +0,26% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 30 | 50,00% | +0,01% | -0,13% | -0,65% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 20 | 50,00% | +0,20% | -0,20% | -0,76% | +0,30% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 25 | 48,00% | -0,38% | -0,57% | -1,30% | +0,19% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 29 | 41,38% | -0,02% | -0,37% | -1,04% | +0,56% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 20 | 45,00% | +0,13% | -0,13% | -2,07% | +1,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 24 | 41,67% | -0,43% | -0,75% | -2,55% | +1,41% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 28 | 46,43% | +0,13% | -0,55% | -2,27% | +1,70% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 18 | 61,11% | +0,43% | -0,43% | -2,88% | +2,29% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 22 | 45,45% | -0,68% | -1,01% | -3,46% | +1,94% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 26 | 53,85% | +0,23% | -0,86% | -3,27% | +2,23% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 16 | 56,25% | +1,13% | -1,13% | -3,80% | +2,49% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 20 | 55,00% | -0,38% | -1,53% | -4,27% | +2,14% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 24 | 45,83% | +0,42% | -1,27% | -4,04% | +2,42% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 13 | 84,62% | +2,13% | -2,13% | -4,84% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 17 | 35,29% | -0,71% | -1,99% | -5,16% | +2,21% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 21 | 71,43% | +1,57% | -1,80% | -4,90% | +2,52% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 9 | 88,89% | +3,03% | -3,03% | -5,90% | +3,13% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 13 | 61,54% | +0,01% | -2,87% | -5,98% | +2,43% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 17 | 64,71% | +1,79% | -2,98% | -5,67% | +2,76% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Classic technical | 3 | 100,00% | +2,10% | -2,10% | -6,17% | +4,49% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 7 | 85,71% | +2,87% | -4,23% | -7,04% | +2,83% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 10 | 60,00% | -0,34% | -3,78% | -6,75% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 1 | 100,00% | +4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 28 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 28 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 30 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 12 | 16,67% | -0,93% |
| BTC | BREVE | Famiglia statistica | 87 | 52,87% | +0,12% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 72 | 40,28% | -0,32% |
| BTC | SETTIMANALE | Classic technical | 9 | 11,11% | -1,30% |
| BTC | SETTIMANALE | Famiglia statistica | 71 | 47,89% | +0,26% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 57 | 42,11% | -0,33% |
| BTC | SWING | Famiglia statistica | 27 | 51,85% | +0,18% |
| BTC | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% |
| BTC | SWING | Tecnico | 23 | 34,78% | -0,24% |
| BTC | MEDIO | Famiglia statistica | 1 | 100,00% | +2,74% |
| BTC | MEDIO | Tecnico | 1 | 0,00% | -2,74% |
| DOGE | BREVE | Classic technical | 61 | 42,62% | -0,07% |
| DOGE | BREVE | Famiglia statistica | 87 | 51,72% | +0,05% |
| DOGE | BREVE | Microstruttura exchange | 7 | 85,71% | +3,19% |
| DOGE | BREVE | Tecnico | 85 | 52,94% | +0,34% |
| DOGE | SETTIMANALE | Classic technical | 57 | 57,89% | +0,96% |
| DOGE | SETTIMANALE | Famiglia statistica | 71 | 57,75% | +0,52% |
| DOGE | SETTIMANALE | Microstruttura exchange | 6 | 100,00% | +1,18% |
| DOGE | SETTIMANALE | Tecnico | 71 | 64,79% | +1,33% |
| DOGE | SWING | Classic technical | 25 | 84,00% | +3,10% |
| DOGE | SWING | Famiglia statistica | 27 | 88,89% | +3,30% |
| DOGE | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% |
| DOGE | SWING | Tecnico | 27 | 85,19% | +3,24% |
| DOGE | MEDIO | Classic technical | 1 | 100,00% | +3,75% |
| DOGE | MEDIO | Famiglia statistica | 1 | 100,00% | +3,75% |
| DOGE | MEDIO | Tecnico | 1 | 100,00% | +3,75% |
| SOL | BREVE | Classic technical | 61 | 47,54% | +0,10% |
| SOL | BREVE | Famiglia statistica | 75 | 50,67% | -0,28% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 87 | 45,98% | +0,04% |
| SOL | SETTIMANALE | Classic technical | 47 | 65,96% | +1,14% |
| SOL | SETTIMANALE | Famiglia statistica | 59 | 45,76% | -0,59% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 3 | 0,00% | -5,22% |
| SOL | SETTIMANALE | Tecnico | 71 | 56,34% | +0,69% |
| SOL | SWING | Classic technical | 12 | 91,67% | +2,80% |
| SOL | SWING | Famiglia statistica | 20 | 70,00% | +1,01% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% |
| SOL | SWING | Tecnico | 27 | 62,96% | +1,00% |
| SOL | MEDIO | Famiglia statistica | 1 | 100,00% | +4,50% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Tecnico | 1 | 0,00% | -4,50% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 5 | in attesa di controlli maturati |
| BTC | MEDIO | 13 | in attesa di controlli maturati |
| SOL | SWING | 1 | in attesa di controlli maturati |
| SOL | MEDIO | 12 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 3 | in attesa di controlli maturati |
| DOGE | MEDIO | 12 | in attesa di controlli maturati |

## Come leggere le raccomandazioni

- **OSSERVA**: meno di 30 controlli, nessuna modifica.
- **PESO OK / MANTIENI**: il modulo sta aiutando, ma non serve cambiare peso.
- **NON AUMENTARE**: il modulo non dimostra ancora un vantaggio sufficiente.
- **POSSIBILE AUMENTO LEGGERO**: proposta prudente, mai automatica.
- **POSSIBILE RIDUZIONE**: modulo debole con campione già abbastanza maturo.
- **ESCLUSO**: benchmark o diagnostica già inclusa in un'altra famiglia.

Nota decisiva: **non sommare mai una modifica alla Famiglia statistica e altre modifiche separate a Scanner o Market Regime**. Scanner e Market servono soltanto a capire quale parte della famiglia sta funzionando o fallendo.

## Stato attuale

È iniziata la prima calibrazione, ma sono ammesse solo valutazioni leggere e manuali.
