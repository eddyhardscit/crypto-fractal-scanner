# Calibrazione pesi Global Confluence

Generato: 2026-09-06 05:33 UTC

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
| BTC | 58 | PRIMA CALIBRAZIONE | 57 | 17 | 0 | 0 | Famiglia statistica | 1g | 54,39% | +0,43% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 58 | PRIMA CALIBRAZIONE | 54 | 22 | 0 | 0 | Tecnico | 1g | 51,85% | +0,39% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 58 | PRIMA CALIBRAZIONE | 56 | 23 | 0 | 0 | Famiglia statistica | 1g | 57,14% | +0,44% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 24 | 37,50% | +0,37% | +0,81% | +0,13% | +1,33% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 57 | 54,39% | +0,43% | +0,43% | -0,01% | +0,96% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 4 | 50,00% | -0,20% | -0,20% | -0,66% | +0,18% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 52 | 40,38% | +0,17% | +0,56% | +0,10% | +1,09% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 24 | 41,67% | +0,55% | +1,18% | +0,59% | +1,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 56 | 55,36% | +0,89% | +0,89% | +0,31% | +1,59% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,27% | +1,27% | +0,55% | +1,72% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 51 | 45,10% | +0,27% | +1,09% | +0,50% | +1,78% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 23 | 43,48% | +0,27% | +1,94% | -0,53% | +3,49% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 55 | 58,18% | +1,36% | +1,36% | -0,91% | +2,98% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 50 | 40,00% | +0,01% | +1,70% | -0,72% | +3,28% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 21 | 47,62% | -1,41% | +4,12% | -1,07% | +6,28% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 53 | 52,83% | +2,23% | +2,23% | -1,53% | +4,49% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 48 | 43,75% | -0,95% | +2,57% | -1,33% | +4,88% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 19 | 42,11% | -3,56% | +6,13% | -1,07% | +9,06% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 51 | 60,78% | +3,06% | +3,06% | -1,73% | +5,70% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 46 | 41,30% | -1,91% | +3,64% | -1,50% | +6,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 16 | 50,00% | -5,13% | +8,06% | -0,93% | +10,98% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 48 | 64,58% | +4,04% | +4,04% | -1,94% | +6,87% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 43 | 44,19% | -1,53% | +4,65% | -1,68% | +7,53% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 12 | 50,00% | -5,94% | +10,44% | -0,24% | +14,07% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 44 | 65,91% | +6,17% | +6,17% | -2,01% | +9,51% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +1,23% | +1,23% | -1,55% | +6,04% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 39 | 61,54% | +0,90% | +7,12% | -1,70% | +10,52% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 7 | 0,00% | -18,41% | +18,41% | -1,07% | +21,11% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 37 | 67,57% | +9,18% | +9,18% | -2,79% | +12,78% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 32 | 34,38% | -0,83% | +10,37% | -2,53% | +14,02% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 4 | 0,00% | -24,06% | +24,06% | -1,55% | +28,48% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 30 | 83,33% | +12,68% | +12,68% | -2,95% | +16,63% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 25 | 36,00% | -5,38% | +12,68% | -2,65% | +16,99% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 15 | 100,00% | +22,60% | +22,60% | -3,18% | +26,39% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 12 | 33,33% | -7,97% | +22,88% | -2,79% | +26,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 31 | 41,94% | -0,51% | +0,27% | -0,38% | +0,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 56 | 57,14% | +0,44% | +0,43% | -0,24% | +1,37% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 8 | 62,50% | +2,09% | +2,48% | +0,94% | +3,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 50 | 54,00% | +0,51% | +0,34% | -0,35% | +1,27% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 55 | 54,55% | +0,81% | +0,76% | -0,02% | +1,99% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 8 | 50,00% | +3,05% | +3,38% | +2,44% | +5,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 49 | 57,14% | +0,73% | +0,36% | -0,42% | +1,56% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 31 | 32,26% | -2,13% | +1,30% | -1,89% | +4,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 54 | 53,70% | +1,21% | +1,20% | -1,74% | +3,89% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 8 | 50,00% | +2,64% | +2,90% | -0,79% | +6,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 48 | 45,83% | +0,66% | +0,31% | -2,03% | +2,88% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 31 | 38,71% | -3,99% | +2,48% | -2,71% | +6,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 52 | 51,92% | +2,36% | +1,93% | -2,66% | +6,04% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | +1,34% | +1,54% | -1,56% | +8,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 46 | 56,52% | +0,47% | +0,75% | -3,16% | +4,87% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 31 | 38,71% | -4,80% | +2,76% | -3,30% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 50 | 58,00% | +3,30% | +2,53% | -3,12% | +7,85% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 8 | 50,00% | +0,28% | +0,41% | -2,23% | +8,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 44 | 56,82% | +1,04% | +1,01% | -3,73% | +6,23% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 31 | 41,94% | -4,39% | +2,22% | -3,95% | +9,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 47 | 57,45% | +3,84% | +2,73% | -3,50% | +9,38% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 7 | 57,14% | -0,43% | +0,00% | -2,75% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 41 | 60,98% | +1,48% | +0,55% | -4,21% | +6,80% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 29 | 51,72% | -3,97% | +3,65% | -3,94% | +11,74% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 44 | 75,00% | +7,28% | +5,15% | -3,44% | +13,47% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 6 | 66,67% | +2,65% | +9,19% | -1,41% | +17,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 37 | 67,57% | +1,23% | +1,71% | -4,12% | +9,00% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 24 | 62,50% | -4,37% | +4,37% | -4,40% | +12,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 37 | 86,49% | +11,61% | +8,41% | -4,01% | +18,28% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 4 | 75,00% | -0,95% | +12,49% | -1,31% | +25,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 32 | 65,62% | -3,06% | +6,34% | -4,46% | +14,37% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 21 | 52,38% | -8,46% | +8,46% | -5,03% | +18,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 30 | 86,67% | +9,86% | +11,38% | -4,76% | +23,69% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 3 | 66,67% | +10,47% | +31,57% | -1,27% | +41,74% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 29 | 41,38% | -11,00% | +11,00% | -4,87% | +23,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 14 | 0,00% | -19,32% | +19,32% | -6,50% | +36,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 15 | 0,00% | -19,04% | +19,04% | -6,61% | +36,84% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 15 | 0,00% | -19,04% | +19,04% | -6,61% | +36,84% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 38 | 52,63% | +0,59% | +0,64% | -0,18% | +1,57% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 52 | 57,69% | +0,40% | +0,41% | -0,23% | +1,30% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 54 | 51,85% | +0,39% | +0,41% | -0,27% | +1,25% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 37 | 54,05% | +0,99% | +1,02% | +0,08% | +2,01% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 51 | 49,02% | +0,51% | +0,99% | +0,02% | +1,82% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 53 | 45,28% | +0,30% | +0,88% | -0,02% | +1,99% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 36 | 55,56% | +1,26% | +1,41% | -1,62% | +3,59% | PESO OK | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 50 | 50,00% | +1,08% | +1,67% | -1,61% | +3,91% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 52 | 50,00% | +0,18% | +1,44% | -1,67% | +3,61% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 34 | 58,82% | +1,81% | +1,98% | -2,47% | +5,11% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 48 | 54,17% | +1,71% | +2,84% | -2,35% | +6,20% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 50 | 48,00% | -0,47% | +2,71% | -2,50% | +5,95% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 32 | 53,12% | +2,28% | +2,22% | -2,83% | +6,21% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 46 | 60,87% | +2,83% | +4,21% | -2,63% | +8,22% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 48 | 41,67% | -1,32% | +3,90% | -2,81% | +7,89% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 29 | 65,52% | +2,68% | +2,56% | -2,87% | +7,35% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 43 | 67,44% | +5,37% | +6,44% | -2,68% | +10,65% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 45 | 51,11% | -2,10% | +5,37% | -2,94% | +9,77% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 25 | 48,00% | +1,28% | +3,28% | -3,42% | +7,80% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 39 | 79,49% | +9,13% | +10,17% | -3,01% | +15,08% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 3 | 66,67% | +10,82% | +10,82% | -3,34% | +16,86% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 41 | 36,59% | -5,35% | +7,64% | -3,37% | +12,87% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 33 | 84,85% | +17,05% | +15,35% | -4,40% | +20,70% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 35 | 34,29% | -13,27% | +12,10% | -4,75% | +17,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 21 | 9,52% | -26,53% | +26,53% | -4,64% | +32,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 26 | 88,46% | +22,30% | +22,70% | -5,35% | +28,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 30 | 13,33% | -20,36% | +19,74% | -5,55% | +25,57% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 7 | 0,00% | -35,14% | +35,14% | -7,15% | +44,53% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 11 | 27,27% | -12,08% | +30,97% | -8,12% | +38,61% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 15 | 26,67% | -19,23% | +32,35% | -7,78% | +39,63% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 54 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 57 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 71 | 40,85% | +0,40% |
| BTC | BREVE | Famiglia statistica | 168 | 55,95% | +0,89% |
| BTC | BREVE | Microstruttura exchange | 11 | 54,55% | +0,78% |
| BTC | BREVE | Tecnico | 153 | 41,83% | +0,15% |
| BTC | SETTIMANALE | Classic technical | 56 | 46,43% | -3,20% |
| BTC | SETTIMANALE | Famiglia statistica | 152 | 59,21% | +3,08% |
| BTC | SETTIMANALE | Microstruttura exchange | 9 | 55,56% | +0,53% |
| BTC | SETTIMANALE | Tecnico | 137 | 43,07% | -1,46% |
| BTC | SWING | Classic technical | 19 | 31,58% | -10,54% |
| BTC | SWING | Famiglia statistica | 81 | 66,67% | +7,54% |
| BTC | SWING | Microstruttura exchange | 3 | 66,67% | +1,23% |
| BTC | SWING | Tecnico | 71 | 49,30% | +0,12% |
| BTC | MEDIO | Classic technical | 4 | 0,00% | -24,06% |
| BTC | MEDIO | Famiglia statistica | 45 | 88,89% | +15,99% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 37 | 35,14% | -6,22% |
| DOGE | BREVE | Classic technical | 93 | 39,78% | -1,28% |
| DOGE | BREVE | Famiglia statistica | 165 | 55,15% | +0,81% |
| DOGE | BREVE | Microstruttura exchange | 24 | 54,17% | +2,59% |
| DOGE | BREVE | Tecnico | 147 | 52,38% | +0,64% |
| DOGE | SETTIMANALE | Classic technical | 93 | 39,78% | -4,39% |
| DOGE | SETTIMANALE | Famiglia statistica | 149 | 55,70% | +3,14% |
| DOGE | SETTIMANALE | Microstruttura exchange | 23 | 47,83% | +0,43% |
| DOGE | SETTIMANALE | Tecnico | 131 | 58,02% | +0,98% |
| DOGE | SWING | Classic technical | 53 | 56,60% | -4,15% |
| DOGE | SWING | Famiglia statistica | 81 | 80,25% | +9,26% |
| DOGE | SWING | Microstruttura exchange | 10 | 70,00% | +1,21% |
| DOGE | SWING | Tecnico | 69 | 66,67% | -0,76% |
| DOGE | MEDIO | Classic technical | 35 | 31,43% | -12,80% |
| DOGE | MEDIO | Famiglia statistica | 45 | 57,78% | +0,22% |
| DOGE | MEDIO | Microstruttura exchange | 3 | 66,67% | +10,47% |
| DOGE | MEDIO | Tecnico | 44 | 27,27% | -13,74% |
| SOL | BREVE | Classic technical | 111 | 54,05% | +0,94% |
| SOL | BREVE | Famiglia statistica | 153 | 52,29% | +0,66% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 159 | 49,06% | +0,29% |
| SOL | SETTIMANALE | Classic technical | 95 | 58,95% | +2,23% |
| SOL | SETTIMANALE | Famiglia statistica | 137 | 60,58% | +3,23% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 143 | 46,85% | -1,27% |
| SOL | SWING | Classic technical | 46 | 43,48% | -4,41% |
| SOL | SWING | Famiglia statistica | 72 | 81,94% | +12,76% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 5 | 60,00% | +13,52% |
| SOL | SWING | Tecnico | 76 | 35,53% | -9,00% |
| SOL | MEDIO | Classic technical | 28 | 7,14% | -28,69% |
| SOL | MEDIO | Famiglia statistica | 37 | 70,27% | +12,08% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 2 | 100,00% | +20,54% |
| SOL | MEDIO | Tecnico | 45 | 17,78% | -19,98% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 8 | in attesa di controlli maturati |
| SOL | MEDIO | 5 | in attesa di controlli maturati |
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
