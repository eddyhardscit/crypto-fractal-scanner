# Calibrazione pesi Global Confluence

Generato: 2026-08-09 05:17 UTC

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
| BTC | 32 | PRIMA CALIBRAZIONE | 31 | 2 | 0 | 0 | Famiglia statistica | 1g | 51,61% | +0,04% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 32 | PRIMA CALIBRAZIONE | 31 | 2 | 0 | 0 | Tecnico | 1g | 48,39% | -0,05% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 32 | PRIMA CALIBRAZIONE | 31 | 3 | 0 | 0 | Famiglia statistica | 1g | 54,84% | +0,22% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 4 | 0,00% | -0,76% | +0,76% | +0,03% | +1,12% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 31 | 51,61% | +0,04% | +0,04% | -0,28% | +0,56% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 26 | 34,62% | -0,37% | +0,23% | -0,11% | +0,75% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 4 | 25,00% | -0,86% | +0,86% | +0,50% | +1,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 30 | 50,00% | +0,15% | +0,15% | -0,33% | +0,83% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 25 | 48,00% | -0,26% | +0,39% | -0,07% | +1,06% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 4 | 25,00% | -1,18% | +1,18% | -0,41% | +2,46% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 29 | 55,17% | +0,16% | +0,16% | -1,32% | +1,72% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 24 | 37,50% | -0,27% | +0,61% | -1,02% | +2,09% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 4 | 25,00% | -1,14% | +1,14% | -1,16% | +2,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 27 | 44,44% | +0,32% | +0,32% | -2,04% | +2,39% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 22 | 50,00% | -0,36% | +0,65% | -1,72% | +2,77% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 3 | 0,00% | -1,41% | +1,41% | -1,92% | +2,79% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 25 | 56,00% | +0,32% | +0,32% | -2,43% | +2,71% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 20 | 35,00% | -0,54% | +0,96% | -2,09% | +3,11% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Classic technical | 2 | 0,00% | -1,45% | +1,45% | -2,23% | +2,64% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 22 | 50,00% | +0,31% | +0,31% | -2,78% | +3,06% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 18 | 38,89% | -0,12% | +0,75% | -2,43% | +3,48% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 18 | 50,00% | +0,01% | +0,01% | -3,10% | +3,69% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 15 | 53,33% | +0,10% | +0,23% | -2,77% | +3,98% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 11 | 54,55% | +0,45% | +0,45% | -2,62% | +4,99% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 10 | 10,00% | -0,65% | +0,42% | -2,56% | +5,01% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 2 | 100,00% | +2,05% | +2,05% | -2,80% | +5,29% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 1 | 0,00% | -2,74% | +2,74% | -2,32% | +5,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 21 | 38,10% | -0,20% | +0,20% | -0,32% | +0,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 31 | 54,84% | +0,22% | -0,16% | -0,63% | +0,47% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,60% | +2,65% | +1,48% | +2,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 30 | 50,00% | +0,12% | -0,12% | -0,60% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 21 | 47,62% | -0,19% | +0,19% | -0,49% | +1,28% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 30 | 50,00% | +0,03% | -0,28% | -0,89% | +0,63% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 3 | 66,67% | +3,33% | +4,20% | +3,09% | +4,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 29 | 58,62% | +0,30% | -0,30% | -0,90% | +0,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 20 | 40,00% | +0,14% | -0,14% | -1,99% | +2,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 29 | 48,28% | -0,10% | -0,53% | -2,11% | +1,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 28 | 50,00% | +0,55% | -0,55% | -2,13% | +1,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 20 | 55,00% | +0,45% | -0,45% | -2,87% | +2,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 27 | 51,85% | +0,10% | -0,85% | -3,06% | +1,93% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 27 | 62,96% | +0,85% | -0,85% | -3,06% | +1,93% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 20 | 55,00% | +1,01% | -1,01% | -3,42% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 25 | 60,00% | +0,47% | -1,24% | -3,68% | +2,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 25 | 64,00% | +1,24% | -1,24% | -3,68% | +2,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 18 | 61,11% | +1,42% | -1,42% | -4,14% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 22 | 59,09% | +1,01% | -1,86% | -4,52% | +2,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 22 | 68,18% | +1,86% | -1,86% | -4,52% | +2,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 16 | 75,00% | +2,59% | -2,59% | -5,33% | +2,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 18 | 77,78% | +2,39% | -2,82% | -5,58% | +2,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 18 | 77,78% | +2,82% | -2,82% | -5,58% | +2,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 10 | 100,00% | +3,94% | -3,94% | -6,42% | +2,65% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 11 | 100,00% | +4,08% | -4,08% | -6,57% | +2,45% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 11 | 100,00% | +4,08% | -4,08% | -6,57% | +2,45% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 2 | 100,00% | +4,54% | -4,54% | -7,34% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 2 | 100,00% | +4,54% | -4,54% | -7,34% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 2 | 100,00% | +4,54% | -4,54% | -7,34% | +2,87% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 21 | 47,62% | -0,04% | +0,04% | -0,54% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 27 | 62,96% | +0,02% | -0,30% | -0,78% | +0,33% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 31 | 48,39% | -0,05% | -0,06% | -0,57% | +0,56% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 21 | 47,62% | -0,02% | +0,02% | -0,52% | +0,51% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 26 | 50,00% | -0,19% | -0,37% | -1,08% | +0,37% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 30 | 40,00% | -0,17% | -0,21% | -0,86% | +0,70% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 20 | 45,00% | +0,13% | -0,13% | -2,07% | +1,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 25 | 44,00% | -0,31% | -0,62% | -2,54% | +1,46% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 29 | 44,83% | +0,04% | -0,45% | -2,27% | +1,73% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 19 | 57,89% | +0,25% | -0,25% | -2,83% | +2,34% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 23 | 47,83% | -0,52% | -0,83% | -3,39% | +2,00% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 27 | 51,85% | +0,11% | -0,72% | -3,21% | +2,27% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 17 | 52,94% | +0,87% | -0,87% | -3,69% | +2,55% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 21 | 57,14% | -0,20% | -1,30% | -4,17% | +2,21% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 25 | 44,00% | +0,27% | -1,08% | -3,96% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 14 | 78,57% | +1,74% | -1,74% | -4,76% | +2,70% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 18 | 38,89% | -0,49% | -1,69% | -5,08% | +2,29% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 22 | 68,18% | +1,34% | -1,56% | -4,85% | +2,57% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 10 | 80,00% | +2,62% | -2,62% | -5,90% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 14 | 64,29% | +0,09% | -2,59% | -5,97% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 18 | 61,11% | +1,63% | -2,75% | -5,68% | +2,77% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Classic technical | 4 | 100,00% | +1,62% | -1,62% | -6,39% | +4,25% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 8 | 87,50% | +2,53% | -3,72% | -7,04% | +2,92% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 11 | 63,64% | -0,29% | -3,45% | -6,78% | +3,19% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 2 | 100,00% | +3,39% | -3,39% | -9,20% | +1,74% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 2 | 0,00% | -3,39% | -3,39% | -9,20% | +1,74% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 29 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 29 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 31 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 12 | 16,67% | -0,93% |
| BTC | BREVE | Famiglia statistica | 90 | 52,22% | +0,12% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 75 | 40,00% | -0,30% |
| BTC | SETTIMANALE | Classic technical | 9 | 11,11% | -1,30% |
| BTC | SETTIMANALE | Famiglia statistica | 74 | 50,00% | +0,32% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 60 | 41,67% | -0,35% |
| BTC | SWING | Famiglia statistica | 29 | 51,72% | +0,18% |
| BTC | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% |
| BTC | SWING | Tecnico | 25 | 36,00% | -0,20% |
| BTC | MEDIO | Famiglia statistica | 2 | 100,00% | +2,05% |
| BTC | MEDIO | Tecnico | 1 | 0,00% | -2,74% |
| DOGE | BREVE | Classic technical | 62 | 41,94% | -0,09% |
| DOGE | BREVE | Famiglia statistica | 90 | 51,11% | +0,06% |
| DOGE | BREVE | Microstruttura exchange | 8 | 75,00% | +2,63% |
| DOGE | BREVE | Tecnico | 87 | 52,87% | +0,32% |
| DOGE | SETTIMANALE | Classic technical | 58 | 56,90% | +0,94% |
| DOGE | SETTIMANALE | Famiglia statistica | 74 | 56,76% | +0,50% |
| DOGE | SETTIMANALE | Microstruttura exchange | 6 | 100,00% | +1,18% |
| DOGE | SETTIMANALE | Tecnico | 74 | 64,86% | +1,28% |
| DOGE | SWING | Classic technical | 26 | 84,62% | +3,11% |
| DOGE | SWING | Famiglia statistica | 29 | 86,21% | +3,03% |
| DOGE | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% |
| DOGE | SWING | Tecnico | 29 | 86,21% | +3,30% |
| DOGE | MEDIO | Classic technical | 2 | 100,00% | +4,54% |
| DOGE | MEDIO | Famiglia statistica | 2 | 100,00% | +4,54% |
| DOGE | MEDIO | Tecnico | 2 | 100,00% | +4,54% |
| SOL | BREVE | Classic technical | 62 | 46,77% | +0,02% |
| SOL | BREVE | Famiglia statistica | 78 | 52,56% | -0,16% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 90 | 44,44% | -0,06% |
| SOL | SETTIMANALE | Classic technical | 50 | 62,00% | +0,88% |
| SOL | SETTIMANALE | Famiglia statistica | 62 | 48,39% | -0,40% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 3 | 0,00% | -5,22% |
| SOL | SETTIMANALE | Tecnico | 74 | 54,05% | +0,53% |
| SOL | SWING | Classic technical | 14 | 85,71% | +2,33% |
| SOL | SWING | Famiglia statistica | 22 | 72,73% | +0,98% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% |
| SOL | SWING | Tecnico | 29 | 62,07% | +0,90% |
| SOL | MEDIO | Famiglia statistica | 2 | 100,00% | +3,39% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Tecnico | 2 | 0,00% | -3,39% |

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
