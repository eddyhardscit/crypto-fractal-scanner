# Calibrazione pesi Global Confluence

Generato: 2026-09-01 05:33 UTC

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
| BTC | 53 | PRIMA CALIBRAZIONE | 52 | 15 | 0 | 0 | Famiglia statistica | 1g | 55,77% | +0,45% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 53 | PRIMA CALIBRAZIONE | 49 | 19 | 0 | 0 | Tecnico | 1g | 53,06% | +0,39% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 53 | PRIMA CALIBRAZIONE | 51 | 21 | 0 | 0 | Famiglia statistica | 1g | 58,82% | +0,65% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 20 | 40,00% | +0,40% | +0,93% | +0,22% | +1,48% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 52 | 55,77% | +0,45% | +0,45% | +0,01% | +1,00% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 47 | 40,43% | +0,16% | +0,60% | +0,13% | +1,15% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 19 | 42,11% | +0,52% | +1,32% | +0,74% | +2,00% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 51 | 56,86% | +0,92% | +0,92% | +0,34% | +1,60% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 46 | 45,65% | +0,23% | +1,13% | +0,55% | +1,81% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 18 | 38,89% | -0,03% | +2,10% | -0,31% | +3,50% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 50 | 58,00% | +1,36% | +1,36% | -0,87% | +2,93% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 45 | 37,78% | -0,14% | +1,73% | -0,66% | +3,26% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 16 | 43,75% | -2,09% | +5,17% | -0,56% | +7,27% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 48 | 52,08% | +2,38% | +2,38% | -1,41% | +4,64% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 43 | 41,86% | -1,15% | +2,78% | -1,17% | +5,09% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 14 | 35,71% | -5,04% | +8,12% | -0,42% | +10,89% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 46 | 60,87% | +3,33% | +3,33% | -1,61% | +5,90% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 41 | 39,02% | -2,21% | +4,01% | -1,34% | +6,48% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 11 | 27,27% | -7,89% | +11,29% | -0,22% | +14,00% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 43 | 60,47% | +4,40% | +4,40% | -1,88% | +7,16% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 38 | 36,84% | -1,86% | +5,13% | -1,58% | +7,94% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 8 | 25,00% | -12,28% | +12,28% | -0,83% | +16,12% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 39 | 61,54% | +5,73% | +5,73% | -2,55% | +9,03% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 34 | 55,88% | -0,37% | +6,76% | -2,27% | +10,11% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 4 | 0,00% | -11,68% | +11,68% | -1,55% | +14,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 34 | 64,71% | +7,57% | +7,57% | -3,00% | +11,24% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 29 | 37,93% | +1,92% | +8,61% | -2,74% | +12,34% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Classic technical | 3 | 0,00% | -24,16% | +24,16% | -1,93% | +28,09% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 25 | 80,00% | +10,49% | +10,49% | -3,09% | +14,40% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 20 | 30,00% | -7,66% | +9,93% | -2,74% | +14,29% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 10 | 100,00% | +23,26% | +23,26% | -2,50% | +26,92% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 9 | 33,33% | -8,11% | +23,57% | -2,41% | +27,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 31 | 41,94% | -0,51% | +0,27% | -0,38% | +0,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 51 | 58,82% | +0,65% | +0,29% | -0,32% | +1,26% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 8 | 62,50% | +2,09% | +2,48% | +0,94% | +3,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 45 | 53,33% | +0,37% | +0,18% | -0,45% | +1,14% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 50 | 56,00% | +1,13% | +0,60% | -0,14% | +1,82% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 8 | 50,00% | +3,05% | +3,38% | +2,44% | +5,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 44 | 56,82% | +0,54% | +0,12% | -0,59% | +1,32% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 31 | 32,26% | -2,13% | +1,30% | -1,89% | +4,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 49 | 55,10% | +1,63% | +1,02% | -1,71% | +3,76% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 8 | 50,00% | +2,64% | +2,90% | -0,79% | +6,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 43 | 44,19% | +0,40% | +0,00% | -2,03% | +2,61% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 31 | 38,71% | -3,99% | +2,48% | -2,71% | +6,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 47 | 53,19% | +2,71% | +2,03% | -2,40% | +6,22% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | +2,00% | +2,23% | -1,09% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 41 | 56,10% | +0,41% | +0,73% | -2,93% | +4,94% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 31 | 38,71% | -4,80% | +2,76% | -3,30% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 46 | 58,70% | +3,63% | +2,70% | -2,83% | +8,13% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | +0,24% | +0,39% | -1,74% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 39 | 58,97% | +1,26% | +1,23% | -3,36% | +6,47% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 28 | 46,43% | -3,92% | +3,39% | -3,08% | +10,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 43 | 62,79% | +4,94% | +3,46% | -2,81% | +10,07% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 6 | 66,67% | +1,21% | +1,71% | -1,24% | +10,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 36 | 66,67% | +2,30% | +1,24% | -3,39% | +7,43% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 26 | 53,85% | -3,59% | +3,59% | -3,78% | +11,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 39 | 74,36% | +7,49% | +5,09% | -3,60% | +12,48% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 4 | 75,00% | +2,65% | +12,47% | -1,31% | +16,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 33 | 66,67% | +1,05% | +1,58% | -4,09% | +8,18% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 22 | 68,18% | -2,23% | +2,23% | -4,78% | +9,45% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 34 | 85,29% | +10,34% | +6,86% | -4,31% | +16,06% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 4 | 75,00% | -0,95% | +12,49% | -1,31% | +25,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 30 | 63,33% | -5,01% | +5,01% | -4,70% | +12,46% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 20 | 55,00% | -7,30% | +7,30% | -5,27% | +16,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 25 | 84,00% | +7,31% | +9,14% | -5,36% | +19,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 25 | 48,00% | -9,14% | +9,14% | -5,36% | +19,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 9 | 0,00% | -20,07% | +20,07% | -6,65% | +36,43% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 10 | 0,00% | -19,57% | +19,57% | -6,79% | +36,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 10 | 0,00% | -19,57% | +19,57% | -6,79% | +36,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 33 | 54,55% | +0,62% | +0,68% | -0,09% | +1,66% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 47 | 59,57% | +0,40% | +0,42% | -0,18% | +1,33% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 49 | 53,06% | +0,39% | +0,41% | -0,23% | +1,28% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 32 | 53,12% | +1,09% | +1,12% | +0,25% | +2,12% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 46 | 47,83% | +0,53% | +1,06% | +0,13% | +1,88% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 48 | 43,75% | +0,30% | +0,94% | +0,08% | +2,05% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 31 | 58,06% | +1,44% | +1,62% | -1,34% | +3,73% | PESO OK | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 45 | 51,11% | +1,19% | +1,84% | -1,42% | +4,04% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 47 | 51,06% | +0,18% | +1,58% | -1,49% | +3,70% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 29 | 65,52% | +2,44% | +2,64% | -1,82% | +5,68% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 43 | 58,14% | +2,12% | +3,39% | -1,90% | +6,70% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 45 | 51,11% | -0,31% | +3,23% | -2,08% | +6,41% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 27 | 55,56% | +2,73% | +2,66% | -2,52% | +6,32% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 41 | 63,41% | +3,19% | +4,74% | -2,40% | +8,54% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +3,37% | +3,37% | -3,38% | +8,08% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 43 | 41,86% | -1,46% | +4,37% | -2,62% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 24 | 58,33% | +2,14% | +1,99% | -3,13% | +6,15% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 38 | 65,79% | +5,79% | +6,59% | -2,82% | +10,33% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +3,45% | +3,45% | -2,62% | +8,30% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 40 | 45,00% | -3,02% | +5,38% | -3,10% | +9,35% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 35 | 85,71% | +10,42% | +9,35% | -3,64% | +13,89% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 37 | 29,73% | -7,47% | +6,92% | -3,83% | +11,87% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 30 | 83,33% | +14,96% | +13,10% | -4,70% | +18,17% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 32 | 37,50% | -10,96% | +9,67% | -5,06% | +14,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 17 | 11,76% | -23,39% | +23,39% | -5,53% | +28,85% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 21 | 85,71% | +18,20% | +18,70% | -6,34% | +23,94% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 25 | 16,00% | -16,53% | +15,78% | -6,43% | +20,72% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Classic technical | 3 | 0,00% | -37,88% | +37,88% | -6,17% | +46,05% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 7 | 14,29% | -19,93% | +29,65% | -7,87% | +36,46% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 10 | 40,00% | -12,35% | +32,03% | -7,56% | +38,03% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 49 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 52 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 57 | 40,35% | +0,30% |
| BTC | BREVE | Famiglia statistica | 153 | 56,86% | +0,90% |
| BTC | BREVE | Microstruttura exchange | 9 | 66,67% | +1,28% |
| BTC | BREVE | Tecnico | 138 | 41,30% | +0,09% |
| BTC | SETTIMANALE | Classic technical | 41 | 36,59% | -4,65% |
| BTC | SETTIMANALE | Famiglia statistica | 137 | 57,66% | +3,33% |
| BTC | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 122 | 39,34% | -1,73% |
| BTC | SWING | Classic technical | 12 | 16,67% | -12,08% |
| BTC | SWING | Famiglia statistica | 73 | 63,01% | +6,59% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 63 | 47,62% | +0,69% |
| BTC | MEDIO | Classic technical | 3 | 0,00% | -24,16% |
| BTC | MEDIO | Famiglia statistica | 35 | 85,71% | +14,14% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 29 | 31,03% | -7,80% |
| DOGE | BREVE | Classic technical | 93 | 39,78% | -1,28% |
| DOGE | BREVE | Famiglia statistica | 150 | 56,67% | +1,13% |
| DOGE | BREVE | Microstruttura exchange | 24 | 54,17% | +2,59% |
| DOGE | BREVE | Tecnico | 132 | 51,52% | +0,44% |
| DOGE | SETTIMANALE | Classic technical | 90 | 41,11% | -4,25% |
| DOGE | SETTIMANALE | Famiglia statistica | 136 | 58,09% | +3,73% |
| DOGE | SETTIMANALE | Microstruttura exchange | 20 | 50,00% | +1,15% |
| DOGE | SETTIMANALE | Tecnico | 116 | 60,34% | +1,28% |
| DOGE | SWING | Classic technical | 48 | 60,42% | -2,97% |
| DOGE | SWING | Famiglia statistica | 73 | 79,45% | +8,82% |
| DOGE | SWING | Microstruttura exchange | 8 | 75,00% | +0,85% |
| DOGE | SWING | Tecnico | 63 | 65,08% | -1,84% |
| DOGE | MEDIO | Classic technical | 29 | 37,93% | -11,26% |
| DOGE | MEDIO | Famiglia statistica | 35 | 60,00% | -0,37% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 35 | 34,29% | -12,12% |
| SOL | BREVE | Classic technical | 96 | 55,21% | +1,05% |
| SOL | BREVE | Famiglia statistica | 138 | 52,90% | +0,70% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 144 | 49,31% | +0,29% |
| SOL | SETTIMANALE | Classic technical | 80 | 60,00% | +2,45% |
| SOL | SETTIMANALE | Famiglia statistica | 122 | 62,30% | +3,63% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 12 | 58,33% | +2,98% |
| SOL | SETTIMANALE | Tecnico | 128 | 46,09% | -1,54% |
| SOL | SWING | Classic technical | 42 | 38,10% | -6,19% |
| SOL | SWING | Famiglia statistica | 65 | 84,62% | +12,52% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 4 | 50,00% | +12,98% |
| SOL | SWING | Tecnico | 69 | 33,33% | -9,09% |
| SOL | MEDIO | Classic technical | 20 | 10,00% | -25,56% |
| SOL | MEDIO | Famiglia statistica | 28 | 67,86% | +8,67% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 35 | 22,86% | -15,34% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 9 | in attesa di controlli maturati |
| SOL | MEDIO | 6 | in attesa di controlli maturati |
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
