# Calibrazione pesi Global Confluence

Generato: 2026-08-22 05:32 UTC

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
| BTC | 43 | PRIMA CALIBRAZIONE | 42 | 12 | 0 | 0 | Famiglia statistica | 1g | 57,14% | +0,49% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 43 | PRIMA CALIBRAZIONE | 39 | 13 | 0 | 0 | Tecnico | 1g | 51,28% | +0,19% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 43 | PRIMA CALIBRAZIONE | 42 | 14 | 0 | 0 | Famiglia statistica | 1g | 57,14% | +0,81% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 10 | 30,00% | +0,54% | +1,59% | +0,82% | +2,11% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 42 | 57,14% | +0,49% | +0,49% | +0,10% | +1,03% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 37 | 37,84% | +0,13% | +0,68% | +0,27% | +1,23% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 9 | 22,22% | +0,36% | +2,05% | +1,71% | +2,86% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 41 | 56,10% | +0,98% | +0,98% | +0,45% | +1,69% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 36 | 41,67% | +0,11% | +1,26% | +0,74% | +1,97% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 8 | 12,50% | -2,41% | +2,41% | -0,24% | +3,25% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 40 | 57,50% | +1,24% | +1,24% | -1,00% | +2,74% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 35 | 31,43% | -0,71% | +1,70% | -0,74% | +3,13% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 8 | 12,50% | -7,26% | +7,26% | -0,63% | +8,70% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 38 | 44,74% | +1,34% | +1,34% | -1,86% | +3,38% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 33 | 33,33% | -2,28% | +1,71% | -1,62% | +3,78% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 6 | 0,00% | -8,28% | +8,28% | -0,96% | +9,64% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 36 | 52,78% | +1,12% | +1,12% | -2,24% | +3,50% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 31 | 32,26% | -2,15% | +1,66% | -1,99% | +3,88% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,32% | +1,32% | -1,42% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 34 | 50,00% | +0,75% | +0,75% | -2,68% | +3,36% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 29 | 34,48% | +0,49% | +1,07% | -2,43% | +3,73% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Classic technical | 4 | 50,00% | -0,27% | +0,27% | -1,55% | +3,37% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 31 | 51,61% | +1,30% | +1,30% | -2,88% | +4,45% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 26 | 61,54% | +1,74% | +1,80% | -2,58% | +4,99% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Classic technical | 3 | 0,00% | -8,03% | +8,03% | -1,93% | +10,14% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 24 | 50,00% | +1,47% | +1,47% | -3,14% | +5,15% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 19 | 21,05% | -1,81% | +1,45% | -2,79% | +5,23% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 15 | 66,67% | +2,59% | +2,59% | -3,18% | +6,68% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 12 | 41,67% | -1,91% | +1,49% | -2,79% | +6,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 27 | 37,04% | -0,44% | +0,44% | -0,04% | +1,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 42 | 57,14% | +0,81% | +0,52% | +0,01% | +1,47% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +3,06% | +3,69% | +2,25% | +3,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 35 | 54,29% | +0,69% | +0,45% | -0,08% | +1,36% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 27 | 44,44% | -1,08% | +1,08% | +0,40% | +2,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 41 | 51,22% | +1,14% | +0,91% | +0,26% | +2,19% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 5 | 60,00% | +6,19% | +6,72% | +5,95% | +9,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 34 | 61,76% | +0,89% | +0,35% | -0,23% | +1,57% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 27 | 33,33% | -1,97% | +1,97% | -1,30% | +4,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 40 | 52,50% | +1,29% | +0,98% | -1,54% | +3,39% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,18% | +1,70% | -0,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 33 | 48,48% | +0,25% | -0,26% | -1,90% | +1,81% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 25 | 48,00% | -1,57% | +1,57% | -2,40% | +4,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 38 | 52,63% | +1,50% | +0,83% | -2,49% | +3,92% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,23% | +0,64% | -0,37% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 33 | 63,64% | +0,56% | +0,95% | -2,69% | +4,03% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 23 | 52,17% | +0,04% | -0,04% | -3,05% | +3,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 36 | 58,33% | +1,64% | +0,45% | -2,99% | +4,13% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,36% | +0,63% | -0,50% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 31 | 64,52% | +1,94% | -0,09% | -3,29% | +3,65% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 22 | 59,09% | +1,13% | -1,13% | -3,71% | +2,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 34 | 55,88% | +1,35% | -0,51% | -3,58% | +3,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 4 | 75,00% | +0,18% | +0,93% | -1,31% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 30 | 66,67% | +1,40% | -1,40% | -3,88% | +2,63% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 21 | 66,67% | +1,05% | -1,05% | -4,58% | +3,86% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 31 | 67,74% | +2,93% | -0,09% | -4,34% | +4,82% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 3 | 66,67% | -6,24% | +6,85% | -1,27% | +10,97% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 30 | 66,67% | +0,31% | -0,31% | -4,43% | +4,70% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 20 | 75,00% | -0,03% | +0,03% | -5,18% | +6,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 24 | 79,17% | +4,32% | -0,61% | -5,40% | +5,15% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 24 | 79,17% | +0,61% | -0,61% | -5,40% | +5,15% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 14 | 78,57% | +0,15% | -0,15% | -6,50% | +6,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 15 | 80,00% | +0,54% | -0,54% | -6,61% | +5,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 15 | 80,00% | +0,54% | -0,54% | -6,61% | +5,66% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 23 | 52,17% | +0,39% | +0,46% | -0,22% | +1,38% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 37 | 59,46% | +0,22% | +0,21% | -0,28% | +1,06% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,51% | +1,51% | +0,99% | +5,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 39 | 51,28% | +0,19% | +0,22% | -0,34% | +1,02% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 22 | 50,00% | +0,43% | +0,47% | -0,09% | +1,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 36 | 52,78% | +0,77% | +0,64% | -0,12% | +1,36% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 38 | 39,47% | -0,29% | +0,51% | -0,16% | +1,61% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 21 | 42,86% | -0,13% | +0,13% | -1,91% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 36 | 50,00% | +1,46% | +1,25% | -1,65% | +3,28% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 37 | 40,54% | -1,05% | +0,73% | -1,85% | +2,61% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 21 | 52,38% | -0,14% | +0,14% | -2,60% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 34 | 55,88% | +1,60% | +1,40% | -2,68% | +4,10% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 36 | 41,67% | -1,80% | +1,34% | -2,69% | +4,21% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 32 | 62,50% | +1,68% | +0,96% | -3,21% | +4,24% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 34 | 35,29% | -1,54% | +0,94% | -3,25% | +4,35% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 30 | 63,33% | +1,58% | +0,86% | -3,78% | +4,05% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 32 | 46,88% | -0,22% | +0,07% | -3,88% | +3,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 27 | 81,48% | +3,41% | +2,03% | -4,32% | +5,99% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 31 | 35,48% | -1,99% | +1,33% | -4,36% | +5,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 16 | 50,00% | -3,90% | +3,90% | -5,75% | +7,67% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 20 | 75,00% | +4,56% | +1,76% | -6,27% | +6,31% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 24 | 50,00% | -2,87% | +1,16% | -6,28% | +5,89% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 7 | 28,57% | -5,28% | +5,28% | -7,15% | +9,70% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 11 | 72,73% | +1,96% | +2,91% | -8,12% | +7,29% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 15 | 26,67% | -3,51% | +2,26% | -7,78% | +6,36% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 40 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 42 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 27 | 22,22% | -0,39% |
| BTC | BREVE | Famiglia statistica | 123 | 56,91% | +0,90% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 108 | 37,04% | -0,15% |
| BTC | SETTIMANALE | Classic technical | 18 | 5,56% | -6,28% |
| BTC | SETTIMANALE | Famiglia statistica | 108 | 49,07% | +1,08% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 93 | 33,33% | -1,37% |
| BTC | SWING | Classic technical | 7 | 28,57% | -3,60% |
| BTC | SWING | Famiglia statistica | 55 | 50,91% | +1,38% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 45 | 44,44% | +0,24% |
| BTC | MEDIO | Famiglia statistica | 15 | 66,67% | +2,59% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 12 | 41,67% | -1,91% |
| DOGE | BREVE | Classic technical | 81 | 38,27% | -1,16% |
| DOGE | BREVE | Famiglia statistica | 123 | 53,66% | +1,08% |
| DOGE | BREVE | Microstruttura exchange | 14 | 57,14% | +3,64% |
| DOGE | BREVE | Tecnico | 102 | 54,90% | +0,61% |
| DOGE | SETTIMANALE | Classic technical | 70 | 52,86% | -0,19% |
| DOGE | SETTIMANALE | Famiglia statistica | 108 | 55,56% | +1,50% |
| DOGE | SETTIMANALE | Microstruttura exchange | 12 | 58,33% | +0,26% |
| DOGE | SETTIMANALE | Tecnico | 94 | 64,89% | +1,28% |
| DOGE | SWING | Classic technical | 41 | 70,73% | +0,52% |
| DOGE | SWING | Famiglia statistica | 55 | 72,73% | +3,53% |
| DOGE | SWING | Microstruttura exchange | 5 | 80,00% | -3,44% |
| DOGE | SWING | Tecnico | 54 | 72,22% | +0,45% |
| DOGE | MEDIO | Classic technical | 14 | 78,57% | +0,15% |
| DOGE | MEDIO | Famiglia statistica | 15 | 80,00% | +0,54% |
| DOGE | MEDIO | Tecnico | 15 | 80,00% | +0,54% |
| SOL | BREVE | Classic technical | 66 | 48,48% | +0,24% |
| SOL | BREVE | Famiglia statistica | 109 | 54,13% | +0,81% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 7 | 28,57% | -0,12% |
| SOL | BREVE | Tecnico | 114 | 43,86% | -0,37% |
| SOL | SETTIMANALE | Classic technical | 63 | 49,21% | -0,00% |
| SOL | SETTIMANALE | Famiglia statistica | 96 | 60,42% | +1,62% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 6 | 16,67% | -2,65% |
| SOL | SETTIMANALE | Tecnico | 102 | 41,18% | -1,22% |
| SOL | SWING | Classic technical | 37 | 43,24% | -2,36% |
| SOL | SWING | Famiglia statistica | 47 | 78,72% | +3,90% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 2 | 0,00% | -4,49% |
| SOL | SWING | Tecnico | 55 | 41,82% | -2,38% |
| SOL | MEDIO | Classic technical | 7 | 28,57% | -5,28% |
| SOL | MEDIO | Famiglia statistica | 11 | 72,73% | +1,96% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 15 | 26,67% | -3,51% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 12 | in attesa di controlli maturati |
| SOL | MEDIO | 10 | in attesa di controlli maturati |
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
