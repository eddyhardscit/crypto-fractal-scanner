# Calibrazione pesi Global Confluence

Generato: 2026-08-27 05:33 UTC

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
| BTC | 48 | PRIMA CALIBRAZIONE | 47 | 13 | 0 | 0 | Famiglia statistica | 1g | 55,32% | +0,48% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 48 | PRIMA CALIBRAZIONE | 44 | 14 | 0 | 0 | Tecnico | 1g | 52,27% | +0,35% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 48 | PRIMA CALIBRAZIONE | 46 | 17 | 0 | 0 | Famiglia statistica | 1g | 58,70% | +0,66% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 15 | 33,33% | +0,50% | +1,20% | +0,41% | +1,77% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 47 | 55,32% | +0,48% | +0,48% | +0,05% | +1,04% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 42 | 38,10% | +0,16% | +0,65% | +0,19% | +1,22% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 14 | 35,71% | +0,76% | +1,85% | +1,32% | +2,61% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 46 | 56,52% | +1,04% | +1,04% | +0,47% | +1,74% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 41 | 43,90% | +0,28% | +1,29% | +0,72% | +2,00% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 13 | 46,15% | +0,27% | +3,23% | +0,36% | +4,67% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 45 | 62,22% | +1,61% | +1,61% | -0,74% | +3,20% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +2,79% | +2,79% | +0,99% | +4,54% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 40 | 40,00% | -0,05% | +2,05% | -0,48% | +3,61% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 11 | 36,36% | -3,15% | +7,41% | -0,12% | +8,91% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 43 | 51,16% | +2,63% | +2,63% | -1,39% | +4,75% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 38 | 39,47% | -1,34% | +3,12% | -1,13% | +5,28% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 9 | 11,11% | -8,79% | +11,68% | -0,04% | +14,00% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 41 | 58,54% | +3,53% | +3,53% | -1,67% | +5,97% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 36 | 33,33% | -2,75% | +4,33% | -1,37% | +6,65% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 8 | 0,00% | -13,19% | +13,19% | -0,77% | +15,42% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 38 | 55,26% | +3,30% | +3,30% | -2,41% | +5,90% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 33 | 30,30% | -2,61% | +3,98% | -2,14% | +6,61% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 4 | 50,00% | -0,27% | +0,27% | -1,55% | +3,37% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 34 | 55,88% | +3,03% | +3,03% | -2,91% | +6,17% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 29 | 65,52% | +3,72% | +3,77% | -2,64% | +6,95% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Classic technical | 4 | 0,00% | -11,68% | +11,68% | -1,55% | +14,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 29 | 58,62% | +5,15% | +5,15% | -2,97% | +8,70% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 24 | 25,00% | -2,19% | +5,89% | -2,65% | +9,50% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Classic technical | 1 | 0,00% | -24,05% | +24,05% | -1,82% | +28,17% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 20 | 75,00% | +7,31% | +7,31% | -3,27% | +11,11% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 16 | 37,50% | -3,66% | +6,51% | -2,90% | +10,90% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 5 | 100,00% | +23,30% | +23,30% | -2,65% | +26,27% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 4 | 50,00% | +0,62% | +24,00% | -2,49% | +26,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 31 | 41,94% | -0,51% | +0,27% | -0,38% | +0,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 46 | 58,70% | +0,66% | +0,39% | -0,22% | +1,39% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 7 | 71,43% | +2,41% | +2,86% | +1,15% | +3,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 40 | 55,00% | +0,50% | +0,28% | -0,35% | +1,27% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 46 | 52,17% | +1,04% | +0,84% | +0,11% | +2,15% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 7 | 57,14% | +3,88% | +4,25% | +3,39% | +6,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 39 | 61,54% | +0,81% | +0,33% | -0,35% | +1,60% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 30 | 33,33% | -2,01% | +1,54% | -1,63% | +4,45% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 45 | 53,33% | +1,71% | +1,43% | -1,35% | +4,27% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 7 | 57,14% | +3,29% | +3,59% | -0,23% | +7,51% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 38 | 50,00% | +0,88% | +0,44% | -1,64% | +3,07% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 28 | 42,86% | -3,74% | +3,42% | -2,10% | +7,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 43 | 55,81% | +3,33% | +2,74% | -1,90% | +6,67% | PESO OK | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 6 | 50,00% | +3,53% | +3,80% | +0,14% | +10,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 36 | 63,89% | +1,21% | +1,57% | -2,30% | +5,35% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 27 | 44,44% | -4,34% | +4,34% | -2,39% | +9,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 41 | 63,41% | +4,70% | +3,66% | -2,29% | +8,46% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,43% | +3,64% | +1,17% | +11,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 34 | 64,71% | +2,20% | +2,16% | -2,79% | +6,62% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 25 | 52,00% | -2,20% | +2,20% | -3,31% | +7,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 38 | 60,53% | +4,16% | +2,50% | -3,27% | +7,55% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 4 | 75,00% | +0,18% | +0,93% | -1,31% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 33 | 66,67% | +2,31% | +1,15% | -3,59% | +6,29% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 22 | 63,64% | -0,33% | +0,33% | -4,43% | +5,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 34 | 70,59% | +5,43% | +2,68% | -4,07% | +7,96% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 4 | 75,00% | +2,65% | +12,47% | -1,31% | +16,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 30 | 66,67% | +0,31% | -0,31% | -4,43% | +4,70% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 20 | 75,00% | -0,03% | +0,03% | -5,18% | +6,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 29 | 82,76% | +8,40% | +4,32% | -4,86% | +11,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 28 | 67,86% | -3,64% | +3,64% | -4,97% | +10,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 17 | 64,71% | -4,96% | +4,96% | -5,74% | +12,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 20 | 80,00% | +3,90% | +6,19% | -5,99% | +14,08% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 20 | 60,00% | -6,19% | +6,19% | -5,99% | +14,08% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 5 | 0,00% | -22,50% | +22,50% | -7,07% | +35,10% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 5 | 0,00% | -22,50% | +22,50% | -7,07% | +35,10% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 5 | 0,00% | -22,50% | +22,50% | -7,07% | +35,10% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 28 | 53,57% | +0,61% | +0,67% | -0,10% | +1,68% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 42 | 59,52% | +0,37% | +0,38% | -0,19% | +1,30% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 44 | 52,27% | +0,35% | +0,38% | -0,24% | +1,25% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 27 | 55,56% | +0,95% | +0,99% | +0,30% | +1,99% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 41 | 48,78% | +0,37% | +0,96% | +0,14% | +1,76% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 4 | 25,00% | +0,16% | +0,16% | -0,21% | +2,10% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 43 | 44,19% | +0,12% | +0,83% | +0,09% | +1,97% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 26 | 53,85% | +1,27% | +1,48% | -1,31% | +3,48% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 40 | 47,50% | +1,04% | +1,77% | -1,41% | +3,91% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 3 | 33,33% | +0,33% | +0,33% | -1,17% | +5,20% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 42 | 47,62% | -0,08% | +1,49% | -1,49% | +3,54% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 24 | 58,33% | +1,41% | +1,65% | -2,13% | +4,13% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 38 | 55,26% | +2,20% | +2,86% | -2,11% | +5,86% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +1,18% | +1,18% | -1,95% | +5,20% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 40 | 45,00% | -1,28% | +2,70% | -2,30% | +5,57% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 22 | 45,45% | +0,89% | +0,81% | -2,87% | +3,95% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 36 | 66,67% | +4,53% | +3,90% | -2,60% | +7,40% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 38 | 34,21% | -3,07% | +3,52% | -2,83% | +7,03% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 34 | 67,65% | +5,00% | +4,36% | -3,47% | +7,74% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 36 | 41,67% | -3,60% | +3,47% | -3,58% | +7,17% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 30 | 83,33% | +5,75% | +4,50% | -4,13% | +8,56% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 32 | 34,38% | -2,63% | +2,00% | -4,32% | +6,56% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 20 | 40,00% | -9,40% | +9,40% | -4,94% | +13,51% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 25 | 80,00% | +10,11% | +7,87% | -5,38% | +12,48% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 29 | 41,38% | -7,95% | +6,53% | -5,51% | +11,28% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 12 | 16,67% | -15,60% | +15,60% | -6,52% | +20,16% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 16 | 81,25% | +10,73% | +11,39% | -7,34% | +15,88% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 20 | 20,00% | -10,14% | +9,21% | -7,24% | +13,47% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 4 | 0,00% | -24,70% | +24,70% | -8,35% | +30,51% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 5 | 80,00% | +13,28% | +26,08% | -8,51% | +30,69% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 45 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 47 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 42 | 38,10% | +0,52% |
| BTC | BREVE | Famiglia statistica | 138 | 57,97% | +1,03% |
| BTC | BREVE | Microstruttura exchange | 8 | 75,00% | +1,60% |
| BTC | BREVE | Tecnico | 123 | 40,65% | +0,13% |
| BTC | SETTIMANALE | Classic technical | 28 | 17,86% | -7,83% |
| BTC | SETTIMANALE | Famiglia statistica | 122 | 54,92% | +3,14% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 107 | 34,58% | -2,20% |
| BTC | SWING | Classic technical | 8 | 25,00% | -5,98% |
| BTC | SWING | Famiglia statistica | 63 | 57,14% | +4,01% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 53 | 47,17% | +1,04% |
| BTC | MEDIO | Classic technical | 1 | 0,00% | -24,05% |
| BTC | MEDIO | Famiglia statistica | 25 | 80,00% | +10,51% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 20 | 40,00% | -2,80% |
| DOGE | BREVE | Classic technical | 92 | 40,22% | -1,23% |
| DOGE | BREVE | Famiglia statistica | 137 | 54,74% | +1,13% |
| DOGE | BREVE | Microstruttura exchange | 21 | 61,90% | +3,19% |
| DOGE | BREVE | Tecnico | 117 | 55,56% | +0,73% |
| DOGE | SETTIMANALE | Classic technical | 80 | 46,25% | -3,46% |
| DOGE | SETTIMANALE | Famiglia statistica | 122 | 59,84% | +4,05% |
| DOGE | SETTIMANALE | Microstruttura exchange | 15 | 60,00% | +2,60% |
| DOGE | SETTIMANALE | Tecnico | 103 | 65,05% | +1,89% |
| DOGE | SWING | Classic technical | 42 | 69,05% | -0,19% |
| DOGE | SWING | Famiglia statistica | 63 | 76,19% | +6,80% |
| DOGE | SWING | Microstruttura exchange | 6 | 83,33% | +2,02% |
| DOGE | SWING | Tecnico | 58 | 67,24% | -1,60% |
| DOGE | MEDIO | Classic technical | 22 | 50,00% | -8,95% |
| DOGE | MEDIO | Famiglia statistica | 25 | 64,00% | -1,38% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 25 | 48,00% | -9,45% |
| SOL | BREVE | Classic technical | 81 | 54,32% | +0,94% |
| SOL | BREVE | Famiglia statistica | 123 | 52,03% | +0,59% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 12 | 41,67% | +0,40% |
| SOL | BREVE | Tecnico | 129 | 48,06% | +0,14% |
| SOL | SETTIMANALE | Classic technical | 67 | 52,24% | +0,83% |
| SOL | SETTIMANALE | Famiglia statistica | 108 | 62,96% | +3,86% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 7 | 28,57% | -1,10% |
| SOL | SETTIMANALE | Tecnico | 114 | 40,35% | -2,61% |
| SOL | SWING | Classic technical | 41 | 39,02% | -5,20% |
| SOL | SWING | Famiglia statistica | 55 | 81,82% | +7,73% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 3 | 33,33% | +4,53% |
| SOL | SWING | Tecnico | 61 | 37,70% | -5,16% |
| SOL | MEDIO | Classic technical | 12 | 16,67% | -15,60% |
| SOL | MEDIO | Famiglia statistica | 20 | 65,00% | +3,65% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 25 | 32,00% | -5,46% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 9 | in attesa di controlli maturati |
| SOL | MEDIO | 7 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 2 | in attesa di controlli maturati |
| DOGE | MEDIO | 8 | in attesa di controlli maturati |

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
