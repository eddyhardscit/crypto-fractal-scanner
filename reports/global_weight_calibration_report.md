# Calibrazione pesi Global Confluence

Generato: 2026-08-14 11:04 UTC

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
| BTC | 35 | PRIMA CALIBRAZIONE | 34 | 5 | 0 | 0 | Famiglia statistica | 1g | 50,00% | -0,02% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 35 | PRIMA CALIBRAZIONE | 32 | 8 | 0 | 0 | Tecnico | 1g | 50,00% | -0,02% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 35 | PRIMA CALIBRAZIONE | 34 | 9 | 0 | 0 | Famiglia statistica | 1g | 52,94% | +0,19% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 4 | 0,00% | -0,76% | +0,76% | +0,03% | +1,12% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 34 | 50,00% | -0,02% | -0,02% | -0,33% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 29 | 34,48% | -0,40% | +0,14% | -0,19% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 4 | 25,00% | -0,86% | +0,86% | +0,50% | +1,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 34 | 47,06% | -0,00% | -0,00% | -0,47% | +0,71% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 29 | 44,83% | -0,38% | +0,18% | -0,27% | +0,89% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 4 | 25,00% | -1,18% | +1,18% | -0,41% | +2,46% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 34 | 50,00% | -0,06% | -0,06% | -1,37% | +1,56% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 29 | 34,48% | -0,46% | +0,27% | -1,13% | +1,83% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 4 | 25,00% | -1,14% | +1,14% | -1,16% | +2,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 32 | 40,62% | +0,05% | +0,05% | -2,02% | +2,21% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 27 | 40,74% | -0,64% | +0,27% | -1,76% | +2,48% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,94% | +1,94% | -1,23% | +3,13% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 30 | 53,33% | +0,20% | +0,20% | -2,24% | +2,63% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 25 | 36,00% | -0,69% | +0,69% | -1,92% | +2,93% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,32% | +1,32% | -1,42% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 27 | 55,56% | +0,32% | +0,32% | -2,57% | +3,05% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 22 | 31,82% | -0,28% | +0,65% | -2,20% | +3,47% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Classic technical | 2 | 50,00% | -0,00% | +0,00% | -2,23% | +2,76% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 23 | 43,48% | -0,16% | -0,16% | -3,08% | +3,30% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 18 | 55,56% | +0,12% | +0,15% | -2,70% | +3,76% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 16 | 43,75% | -0,47% | -0,47% | -3,28% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 13 | 23,08% | -0,06% | -0,12% | -2,94% | +4,27% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 7 | 85,71% | +0,76% | +0,76% | -2,47% | +5,31% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 6 | 33,33% | -1,20% | +0,65% | -2,34% | +5,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 22 | 40,91% | -0,18% | +0,18% | -0,35% | +0,74% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 34 | 52,94% | +0,19% | -0,16% | -0,65% | +0,56% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,13% | +1,92% | +0,84% | +2,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 30 | 50,00% | +0,12% | -0,12% | -0,60% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 22 | 50,00% | -0,17% | +0,17% | -0,49% | +1,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 34 | 47,06% | +0,01% | -0,26% | -0,91% | +0,80% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 4 | 50,00% | +2,46% | +3,12% | +2,21% | +3,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 30 | 60,00% | +0,30% | -0,30% | -0,91% | +0,61% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 22 | 40,91% | +0,10% | -0,10% | -1,86% | +2,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 34 | 47,06% | -0,09% | -0,46% | -1,94% | +1,85% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,18% | +1,70% | -0,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 30 | 50,00% | +0,49% | -0,49% | -2,02% | +1,67% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 22 | 54,55% | +0,40% | -0,40% | -2,68% | +2,79% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 32 | 46,88% | +0,07% | -0,73% | -2,80% | +2,19% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,23% | +0,64% | -0,37% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 30 | 63,33% | +0,75% | -0,75% | -2,89% | +2,13% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,93% | -0,93% | -3,27% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 30 | 56,67% | +0,38% | -1,05% | -3,35% | +2,37% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,62% | +0,97% | -0,19% | +6,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 29 | 65,52% | +1,09% | -1,09% | -3,41% | +2,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 20 | 65,00% | +1,32% | -1,32% | -4,00% | +2,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 27 | 51,85% | +0,74% | -1,61% | -4,16% | +2,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 27 | 70,37% | +1,61% | -1,61% | -4,16% | +2,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 19 | 73,68% | +2,20% | -2,20% | -4,92% | +3,02% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 23 | 65,22% | +1,60% | -2,47% | -5,18% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 23 | 78,26% | +2,47% | -2,47% | -5,18% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 15 | 93,33% | +3,58% | -3,58% | -6,05% | +2,70% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 16 | 93,75% | +3,70% | -3,70% | -6,18% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +0,55% | +0,55% | -1,52% | +6,93% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 16 | 93,75% | +3,70% | -3,70% | -6,18% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 6 | 100,00% | +4,21% | -4,21% | -6,84% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 7 | 100,00% | +4,49% | -4,49% | -7,01% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 7 | 100,00% | +4,49% | -4,49% | -7,01% | +2,82% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 21 | 47,62% | -0,04% | +0,04% | -0,54% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 30 | 60,00% | -0,00% | -0,29% | -0,74% | +0,37% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 32 | 50,00% | -0,02% | -0,10% | -0,59% | +0,53% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 21 | 47,62% | -0,02% | +0,02% | -0,52% | +0,51% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 30 | 50,00% | -0,11% | -0,27% | -0,98% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 32 | 40,62% | -0,20% | -0,15% | -0,81% | +0,78% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 21 | 42,86% | -0,13% | +0,13% | -1,91% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 30 | 43,33% | -0,07% | -0,33% | -2,19% | +1,67% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 32 | 43,75% | -0,17% | -0,20% | -2,04% | +1,90% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 21 | 52,38% | -0,14% | +0,14% | -2,60% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 28 | 53,57% | -0,02% | -0,28% | -2,95% | +2,40% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 31 | 45,16% | -0,29% | -0,24% | -2,89% | +2,61% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 26 | 65,38% | +0,47% | -0,41% | -3,59% | +2,84% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 30 | 36,67% | -0,33% | -0,35% | -3,49% | +2,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 19 | 57,89% | +0,40% | -0,40% | -4,09% | +3,44% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 23 | 52,17% | +0,34% | -0,60% | -4,45% | +2,99% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 27 | 55,56% | +0,48% | -0,66% | -4,35% | +3,11% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 15 | 53,33% | +0,95% | -0,95% | -5,47% | +3,60% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 19 | 73,68% | +0,69% | -1,28% | -5,61% | +3,02% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 23 | 47,83% | +0,75% | -1,64% | -5,45% | +3,16% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Classic technical | 8 | 87,50% | +1,29% | -1,29% | -7,09% | +3,06% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 12 | 66,67% | +1,53% | -3,13% | -7,50% | +2,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 16 | 68,75% | +0,24% | -2,81% | -7,21% | +2,70% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 5 | 80,00% | +1,22% | -2,33% | -8,45% | +2,28% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 7 | 28,57% | -1,02% | -1,65% | -8,15% | +2,58% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 32 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 32 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 34 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 12 | 16,67% | -0,93% |
| BTC | BREVE | Famiglia statistica | 102 | 49,02% | -0,03% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 87 | 37,93% | -0,41% |
| BTC | SETTIMANALE | Classic technical | 12 | 8,33% | -1,47% |
| BTC | SETTIMANALE | Famiglia statistica | 89 | 49,44% | +0,18% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 74 | 36,49% | -0,55% |
| BTC | SWING | Classic technical | 2 | 50,00% | -0,00% |
| BTC | SWING | Famiglia statistica | 39 | 43,59% | -0,28% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 31 | 41,94% | +0,05% |
| BTC | MEDIO | Famiglia statistica | 7 | 85,71% | +0,76% |
| BTC | MEDIO | Tecnico | 6 | 33,33% | -1,20% |
| DOGE | BREVE | Classic technical | 66 | 43,94% | -0,08% |
| DOGE | BREVE | Famiglia statistica | 102 | 49,02% | +0,04% |
| DOGE | BREVE | Microstruttura exchange | 12 | 50,00% | +1,59% |
| DOGE | BREVE | Tecnico | 90 | 53,33% | +0,31% |
| DOGE | SETTIMANALE | Classic technical | 63 | 57,14% | +0,87% |
| DOGE | SETTIMANALE | Famiglia statistica | 89 | 51,69% | +0,38% |
| DOGE | SETTIMANALE | Microstruttura exchange | 9 | 66,67% | +0,55% |
| DOGE | SETTIMANALE | Tecnico | 86 | 66,28% | +1,13% |
| DOGE | SWING | Classic technical | 34 | 82,35% | +2,81% |
| DOGE | SWING | Famiglia statistica | 39 | 76,92% | +2,46% |
| DOGE | SWING | Microstruttura exchange | 3 | 100,00% | +0,49% |
| DOGE | SWING | Tecnico | 39 | 84,62% | +2,98% |
| DOGE | MEDIO | Classic technical | 6 | 100,00% | +4,21% |
| DOGE | MEDIO | Famiglia statistica | 7 | 100,00% | +4,49% |
| DOGE | MEDIO | Tecnico | 7 | 100,00% | +4,49% |
| SOL | BREVE | Classic technical | 63 | 46,03% | -0,06% |
| SOL | BREVE | Famiglia statistica | 90 | 51,11% | -0,06% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 6 | 16,67% | -0,83% |
| SOL | BREVE | Tecnico | 96 | 44,79% | -0,13% |
| SOL | SETTIMANALE | Classic technical | 61 | 50,82% | +0,09% |
| SOL | SETTIMANALE | Famiglia statistica | 77 | 57,14% | +0,25% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 4 | 0,00% | -4,09% |
| SOL | SETTIMANALE | Tecnico | 88 | 45,45% | -0,07% |
| SOL | SWING | Classic technical | 23 | 65,22% | +1,07% |
| SOL | SWING | Famiglia statistica | 31 | 70,97% | +1,02% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 2 | 0,00% | -4,49% |
| SOL | SWING | Tecnico | 39 | 56,41% | +0,54% |
| SOL | MEDIO | Famiglia statistica | 5 | 80,00% | +1,22% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Tecnico | 7 | 28,57% | -1,02% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 3 | in attesa di controlli maturati |
| BTC | MEDIO | 13 | in attesa di controlli maturati |
| SOL | MEDIO | 12 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 2 | in attesa di controlli maturati |
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
