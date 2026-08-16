# Calibrazione pesi Global Confluence

Generato: 2026-08-16 05:35 UTC

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
| BTC | 37 | PRIMA CALIBRAZIONE | 36 | 7 | 0 | 0 | Famiglia statistica | 1g | 50,00% | -0,01% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 37 | PRIMA CALIBRAZIONE | 34 | 9 | 0 | 0 | Tecnico | 1g | 52,94% | -0,01% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 37 | PRIMA CALIBRAZIONE | 36 | 10 | 0 | 0 | Famiglia statistica | 1g | 52,78% | +0,19% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 6 | 16,67% | -0,58% | +0,58% | +0,04% | +0,84% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 36 | 50,00% | -0,01% | -0,01% | -0,31% | +0,50% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 31 | 35,48% | -0,39% | +0,14% | -0,17% | +0,65% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 5 | 20,00% | -0,77% | +0,77% | +0,47% | +1,49% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 35 | 48,57% | +0,01% | +0,01% | -0,44% | +0,70% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 30 | 43,33% | -0,38% | +0,19% | -0,25% | +0,88% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 4 | 25,00% | -1,18% | +1,18% | -0,41% | +2,46% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 34 | 50,00% | -0,06% | -0,06% | -1,37% | +1,56% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 29 | 34,48% | -0,46% | +0,27% | -1,13% | +1,83% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 4 | 25,00% | -1,14% | +1,14% | -1,16% | +2,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 34 | 38,24% | -0,08% | -0,08% | -2,07% | +2,08% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 29 | 37,93% | -0,74% | +0,10% | -1,83% | +2,30% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,94% | +1,94% | -1,23% | +3,13% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 32 | 50,00% | +0,01% | +0,01% | -2,31% | +2,51% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 27 | 33,33% | -0,85% | +0,43% | -2,03% | +2,78% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,32% | +1,32% | -1,42% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 29 | 51,72% | +0,13% | +0,13% | -2,60% | +2,93% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 24 | 33,33% | -0,30% | +0,40% | -2,27% | +3,29% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Classic technical | 3 | 66,67% | -0,00% | +0,00% | -1,93% | +3,08% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 25 | 40,00% | -0,17% | -0,17% | -2,96% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 20 | 60,00% | +0,14% | +0,10% | -2,59% | +3,73% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 18 | 38,89% | -0,63% | -0,63% | -3,27% | +3,69% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 15 | 26,67% | -0,09% | -0,36% | -2,97% | +3,98% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 9 | 66,67% | +0,31% | +0,31% | -2,48% | +5,20% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 8 | 50,00% | -0,58% | +0,18% | -2,38% | +5,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 23 | 39,13% | -0,22% | +0,22% | -0,30% | +0,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 36 | 52,78% | +0,19% | -0,15% | -0,62% | +0,55% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,13% | +1,92% | +0,84% | +2,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 31 | 48,39% | +0,10% | -0,14% | -0,61% | +0,48% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 23 | 47,83% | -0,18% | +0,18% | -0,46% | +1,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 35 | 48,57% | +0,03% | -0,24% | -0,88% | +0,80% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 4 | 50,00% | +2,46% | +3,12% | +2,21% | +3,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 30 | 60,00% | +0,30% | -0,30% | -0,91% | +0,61% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 22 | 40,91% | +0,10% | -0,10% | -1,86% | +2,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 34 | 47,06% | -0,09% | -0,46% | -1,94% | +1,85% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,18% | +1,70% | -0,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 30 | 50,00% | +0,49% | -0,49% | -2,02% | +1,67% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 22 | 54,55% | +0,40% | -0,40% | -2,68% | +2,79% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 34 | 47,06% | +0,08% | -0,68% | -2,71% | +2,30% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,23% | +0,64% | -0,37% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 30 | 63,33% | +0,75% | -0,75% | -2,89% | +2,13% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 22 | 54,55% | +0,91% | -0,91% | -3,18% | +2,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 32 | 56,25% | +0,34% | -0,99% | -3,24% | +2,47% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,36% | +0,63% | -0,50% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 30 | 63,33% | +1,05% | -1,05% | -3,36% | +2,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 20 | 65,00% | +1,32% | -1,32% | -4,00% | +2,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 29 | 51,72% | +0,68% | -1,50% | -4,01% | +2,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 28 | 67,86% | +1,54% | -1,54% | -4,09% | +2,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 20 | 70,00% | +2,09% | -2,09% | -4,80% | +3,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 25 | 64,00% | +1,45% | -2,30% | -4,97% | +2,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 25 | 76,00% | +2,30% | -2,30% | -4,97% | +2,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 16 | 87,50% | +3,30% | -3,30% | -5,81% | +2,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 18 | 88,89% | +3,06% | -3,52% | -6,03% | +2,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 18 | 88,89% | +3,52% | -3,52% | -6,03% | +2,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 8 | 100,00% | +4,09% | -4,09% | -6,72% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 9 | 100,00% | +4,31% | -4,31% | -6,87% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 9 | 100,00% | +4,31% | -4,31% | -6,87% | +2,56% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 21 | 47,62% | -0,04% | +0,04% | -0,54% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 32 | 56,25% | -0,01% | -0,28% | -0,71% | +0,37% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 34 | 52,94% | -0,01% | -0,09% | -0,57% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 21 | 47,62% | -0,02% | +0,02% | -0,52% | +0,51% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 31 | 48,39% | -0,11% | -0,26% | -0,96% | +0,50% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 33 | 42,42% | -0,20% | -0,15% | -0,80% | +0,76% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 21 | 42,86% | -0,13% | +0,13% | -1,91% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 30 | 43,33% | -0,07% | -0,33% | -2,19% | +1,67% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 32 | 43,75% | -0,17% | -0,20% | -2,04% | +1,90% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 21 | 52,38% | -0,14% | +0,14% | -2,60% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 30 | 50,00% | -0,09% | -0,33% | -2,88% | +2,31% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 32 | 46,88% | -0,24% | -0,28% | -2,88% | +2,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 28 | 64,29% | +0,45% | -0,37% | -3,38% | +2,84% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 31 | 35,48% | -0,36% | -0,30% | -3,37% | +3,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 20 | 55,00% | +0,28% | -0,28% | -3,99% | +3,52% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 25 | 56,00% | +0,46% | -0,40% | -4,27% | +3,14% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 29 | 51,72% | +0,32% | -0,49% | -4,20% | +3,23% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 17 | 47,06% | +0,50% | -0,50% | -5,04% | +3,87% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 21 | 76,19% | +0,90% | -0,88% | -5,26% | +3,30% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 25 | 44,00% | +0,46% | -1,28% | -5,16% | +3,38% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Classic technical | 10 | 70,00% | +0,84% | -0,84% | -6,72% | +3,25% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 14 | 71,43% | +1,45% | -2,54% | -7,19% | +2,56% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 18 | 61,11% | +0,10% | -2,39% | -6,99% | +2,84% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 2 | 50,00% | +0,25% | -0,25% | -6,43% | +4,20% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 7 | 71,43% | +0,94% | -1,73% | -7,87% | +2,83% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 9 | 33,33% | -0,74% | -1,34% | -7,77% | +2,94% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 34 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 34 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 36 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 15 | 20,00% | -0,80% |
| BTC | BREVE | Famiglia statistica | 105 | 49,52% | -0,02% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 90 | 37,78% | -0,41% |
| BTC | SETTIMANALE | Classic technical | 12 | 8,33% | -1,47% |
| BTC | SETTIMANALE | Famiglia statistica | 95 | 46,32% | +0,02% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 80 | 35,00% | -0,65% |
| BTC | SWING | Classic technical | 3 | 66,67% | -0,00% |
| BTC | SWING | Famiglia statistica | 43 | 39,53% | -0,36% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 35 | 45,71% | +0,04% |
| BTC | MEDIO | Famiglia statistica | 9 | 66,67% | +0,31% |
| BTC | MEDIO | Tecnico | 8 | 50,00% | -0,58% |
| DOGE | BREVE | Classic technical | 68 | 42,65% | -0,10% |
| DOGE | BREVE | Famiglia statistica | 105 | 49,52% | +0,05% |
| DOGE | BREVE | Microstruttura exchange | 12 | 50,00% | +1,59% |
| DOGE | BREVE | Tecnico | 91 | 52,75% | +0,30% |
| DOGE | SETTIMANALE | Classic technical | 64 | 57,81% | +0,86% |
| DOGE | SETTIMANALE | Famiglia statistica | 95 | 51,58% | +0,35% |
| DOGE | SETTIMANALE | Microstruttura exchange | 10 | 60,00% | +0,46% |
| DOGE | SETTIMANALE | Tecnico | 88 | 64,77% | +1,10% |
| DOGE | SWING | Classic technical | 36 | 77,78% | +2,63% |
| DOGE | SWING | Famiglia statistica | 43 | 74,42% | +2,12% |
| DOGE | SWING | Microstruttura exchange | 4 | 100,00% | +0,61% |
| DOGE | SWING | Tecnico | 43 | 81,40% | +2,81% |
| DOGE | MEDIO | Classic technical | 8 | 100,00% | +4,09% |
| DOGE | MEDIO | Famiglia statistica | 9 | 100,00% | +4,31% |
| DOGE | MEDIO | Tecnico | 9 | 100,00% | +4,31% |
| SOL | BREVE | Classic technical | 63 | 46,03% | -0,06% |
| SOL | BREVE | Famiglia statistica | 93 | 49,46% | -0,06% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 6 | 16,67% | -0,83% |
| SOL | BREVE | Tecnico | 99 | 46,46% | -0,12% |
| SOL | SETTIMANALE | Classic technical | 62 | 50,00% | +0,06% |
| SOL | SETTIMANALE | Famiglia statistica | 83 | 56,63% | +0,26% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 5 | 0,00% | -3,42% |
| SOL | SETTIMANALE | Tecnico | 92 | 44,57% | -0,10% |
| SOL | SWING | Classic technical | 27 | 55,56% | +0,63% |
| SOL | SWING | Famiglia statistica | 35 | 74,29% | +1,12% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 2 | 0,00% | -4,49% |
| SOL | SWING | Tecnico | 43 | 51,16% | +0,31% |
| SOL | MEDIO | Classic technical | 2 | 50,00% | +0,25% |
| SOL | MEDIO | Famiglia statistica | 7 | 71,43% | +0,94% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Tecnico | 9 | 33,33% | -0,74% |

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
