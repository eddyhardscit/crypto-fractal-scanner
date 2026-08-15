# Calibrazione pesi Global Confluence

Generato: 2026-08-15 05:34 UTC

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
| BTC | 36 | PRIMA CALIBRAZIONE | 35 | 6 | 0 | 0 | Famiglia statistica | 1g | 51,43% | -0,01% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 36 | PRIMA CALIBRAZIONE | 33 | 8 | 0 | 0 | Tecnico | 1g | 51,52% | -0,02% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 36 | PRIMA CALIBRAZIONE | 35 | 10 | 0 | 0 | Famiglia statistica | 1g | 54,29% | +0,22% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 5 | 0,00% | -0,71% | +0,71% | +0,08% | +1,00% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 35 | 51,43% | -0,01% | -0,01% | -0,31% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 30 | 33,33% | -0,41% | +0,15% | -0,17% | +0,67% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 4 | 25,00% | -0,86% | +0,86% | +0,50% | +1,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 34 | 47,06% | -0,00% | -0,00% | -0,47% | +0,71% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 29 | 44,83% | -0,38% | +0,18% | -0,27% | +0,89% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 4 | 25,00% | -1,18% | +1,18% | -0,41% | +2,46% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 34 | 50,00% | -0,06% | -0,06% | -1,37% | +1,56% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 29 | 34,48% | -0,46% | +0,27% | -1,13% | +1,83% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 4 | 25,00% | -1,14% | +1,14% | -1,16% | +2,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 33 | 39,39% | -0,04% | -0,04% | -2,06% | +2,11% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 28 | 39,29% | -0,72% | +0,15% | -1,82% | +2,36% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,94% | +1,94% | -1,23% | +3,13% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 31 | 51,61% | +0,10% | +0,10% | -2,27% | +2,56% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 26 | 34,62% | -0,78% | +0,55% | -1,98% | +2,85% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,32% | +1,32% | -1,42% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 28 | 53,57% | +0,24% | +0,24% | -2,56% | +3,01% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 23 | 34,78% | -0,19% | +0,54% | -2,21% | +3,40% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Classic technical | 3 | 66,67% | -0,00% | +0,00% | -1,93% | +3,08% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 24 | 41,67% | -0,15% | -0,15% | -3,01% | +3,32% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 19 | 57,89% | +0,12% | +0,14% | -2,63% | +3,75% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 17 | 41,18% | -0,53% | -0,53% | -3,26% | +3,80% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 14 | 28,57% | +0,06% | -0,22% | -2,93% | +4,14% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 8 | 75,00% | +0,47% | +0,47% | -2,52% | +5,21% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 7 | 42,86% | -0,81% | +0,34% | -2,41% | +5,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 23 | 39,13% | -0,22% | +0,22% | -0,30% | +0,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 35 | 54,29% | +0,22% | -0,13% | -0,61% | +0,58% | NON AUMENTARE | 0,0 | MEDIA |
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
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 33 | 48,48% | +0,09% | -0,69% | -2,75% | +2,26% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,23% | +0,64% | -0,37% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 30 | 63,33% | +0,75% | -0,75% | -2,89% | +2,13% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,93% | -0,93% | -3,27% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 31 | 58,06% | +0,37% | -1,01% | -3,30% | +2,42% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,62% | +0,97% | -0,19% | +6,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 30 | 63,33% | +1,05% | -1,05% | -3,36% | +2,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 20 | 65,00% | +1,32% | -1,32% | -4,00% | +2,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 28 | 53,57% | +0,72% | -1,54% | -4,09% | +2,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 28 | 67,86% | +1,54% | -1,54% | -4,09% | +2,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 20 | 70,00% | +2,09% | -2,09% | -4,80% | +3,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 24 | 66,67% | +1,54% | -2,37% | -5,06% | +2,62% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 24 | 75,00% | +2,37% | -2,37% | -5,06% | +2,62% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 16 | 87,50% | +3,30% | -3,30% | -5,81% | +2,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 17 | 94,12% | +3,54% | -3,42% | -5,95% | +2,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 17 | 88,24% | +3,42% | -3,42% | -5,95% | +2,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 7 | 100,00% | +4,17% | -4,17% | -6,85% | +2,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 8 | 100,00% | +4,42% | -4,42% | -7,00% | +2,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 8 | 100,00% | +4,42% | -4,42% | -7,00% | +2,60% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 21 | 47,62% | -0,04% | +0,04% | -0,54% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 31 | 58,06% | -0,00% | -0,28% | -0,72% | +0,37% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 33 | 51,52% | -0,02% | -0,09% | -0,58% | +0,52% | NON AUMENTARE | 0,0 | MEDIA |
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
| SOL | 5g | SETTIMANALE | Famiglia statistica | 29 | 51,72% | -0,08% | -0,32% | -2,93% | +2,34% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 32 | 46,88% | -0,24% | -0,28% | -2,88% | +2,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 27 | 66,67% | +0,50% | -0,35% | -3,45% | +2,89% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 31 | 35,48% | -0,36% | -0,30% | -3,37% | +3,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 20 | 55,00% | +0,28% | -0,28% | -3,99% | +3,52% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 24 | 54,17% | +0,41% | -0,49% | -4,36% | +3,07% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 28 | 53,57% | +0,39% | -0,56% | -4,27% | +3,18% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 16 | 50,00% | +0,70% | -0,70% | -5,23% | +3,76% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 20 | 75,00% | +0,82% | -1,06% | -5,42% | +3,17% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 24 | 45,83% | +0,59% | -1,44% | -5,29% | +3,28% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Classic technical | 9 | 77,78% | +0,96% | -0,96% | -6,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 13 | 69,23% | +1,54% | -2,76% | -7,29% | +2,50% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 17 | 64,71% | +0,13% | -2,55% | -7,06% | +2,81% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 1 | 100,00% | +0,79% | -0,79% | -6,98% | +3,59% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 6 | 83,33% | +1,15% | -2,07% | -8,21% | +2,50% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 8 | 37,50% | -0,79% | -1,54% | -8,00% | +2,71% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 33 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 33 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 35 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 13 | 15,38% | -0,90% |
| BTC | BREVE | Famiglia statistica | 103 | 49,51% | -0,02% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 88 | 37,50% | -0,41% |
| BTC | SETTIMANALE | Classic technical | 12 | 8,33% | -1,47% |
| BTC | SETTIMANALE | Famiglia statistica | 92 | 47,83% | +0,09% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 77 | 36,36% | -0,58% |
| BTC | SWING | Classic technical | 3 | 66,67% | -0,00% |
| BTC | SWING | Famiglia statistica | 41 | 41,46% | -0,31% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 33 | 45,45% | +0,09% |
| BTC | MEDIO | Famiglia statistica | 8 | 75,00% | +0,47% |
| BTC | MEDIO | Tecnico | 7 | 42,86% | -0,81% |
| DOGE | BREVE | Classic technical | 67 | 43,28% | -0,10% |
| DOGE | BREVE | Famiglia statistica | 103 | 49,51% | +0,05% |
| DOGE | BREVE | Microstruttura exchange | 12 | 50,00% | +1,59% |
| DOGE | BREVE | Tecnico | 90 | 53,33% | +0,31% |
| DOGE | SETTIMANALE | Classic technical | 63 | 57,14% | +0,87% |
| DOGE | SETTIMANALE | Famiglia statistica | 92 | 53,26% | +0,38% |
| DOGE | SETTIMANALE | Microstruttura exchange | 9 | 66,67% | +0,55% |
| DOGE | SETTIMANALE | Tecnico | 88 | 64,77% | +1,10% |
| DOGE | SWING | Classic technical | 36 | 77,78% | +2,63% |
| DOGE | SWING | Famiglia statistica | 41 | 78,05% | +2,37% |
| DOGE | SWING | Microstruttura exchange | 4 | 100,00% | +0,61% |
| DOGE | SWING | Tecnico | 41 | 80,49% | +2,80% |
| DOGE | MEDIO | Classic technical | 7 | 100,00% | +4,17% |
| DOGE | MEDIO | Famiglia statistica | 8 | 100,00% | +4,42% |
| DOGE | MEDIO | Tecnico | 8 | 100,00% | +4,42% |
| SOL | BREVE | Classic technical | 63 | 46,03% | -0,06% |
| SOL | BREVE | Famiglia statistica | 91 | 50,55% | -0,06% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 6 | 16,67% | -0,83% |
| SOL | BREVE | Tecnico | 97 | 45,36% | -0,13% |
| SOL | SETTIMANALE | Classic technical | 62 | 50,00% | +0,06% |
| SOL | SETTIMANALE | Famiglia statistica | 80 | 57,50% | +0,27% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 4 | 0,00% | -4,09% |
| SOL | SETTIMANALE | Tecnico | 91 | 45,05% | -0,09% |
| SOL | SWING | Classic technical | 25 | 60,00% | +0,79% |
| SOL | SWING | Famiglia statistica | 33 | 72,73% | +1,10% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 2 | 0,00% | -4,49% |
| SOL | SWING | Tecnico | 41 | 53,66% | +0,40% |
| SOL | MEDIO | Classic technical | 1 | 100,00% | +0,79% |
| SOL | MEDIO | Famiglia statistica | 6 | 83,33% | +1,15% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Tecnico | 8 | 37,50% | -0,79% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 3 | in attesa di controlli maturati |
| BTC | MEDIO | 13 | in attesa di controlli maturati |
| SOL | MEDIO | 11 | in attesa di controlli maturati |
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
