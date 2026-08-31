# Calibrazione pesi Global Confluence

Generato: 2026-08-31 05:33 UTC

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
| BTC | 52 | PRIMA CALIBRAZIONE | 51 | 15 | 0 | 0 | Famiglia statistica | 1g | 54,90% | +0,43% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 52 | PRIMA CALIBRAZIONE | 48 | 18 | 0 | 0 | Tecnico | 1g | 52,08% | +0,36% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 52 | PRIMA CALIBRAZIONE | 50 | 21 | 0 | 0 | Famiglia statistica | 1g | 60,00% | +0,68% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 19 | 36,84% | +0,35% | +0,91% | +0,22% | +1,49% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 51 | 54,90% | +0,43% | +0,43% | +0,00% | +0,99% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 46 | 39,13% | +0,13% | +0,58% | +0,13% | +1,15% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 18 | 38,89% | +0,48% | +1,33% | +0,78% | +2,06% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 50 | 56,00% | +0,91% | +0,91% | +0,34% | +1,61% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 45 | 44,44% | +0,21% | +1,13% | +0,56% | +1,83% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 17 | 35,29% | -0,14% | +2,12% | -0,28% | +3,57% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 49 | 57,14% | +1,35% | +1,35% | -0,87% | +2,95% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 44 | 36,36% | -0,18% | +1,73% | -0,66% | +3,28% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 15 | 40,00% | -2,26% | +5,49% | -0,45% | +7,53% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 47 | 51,06% | +2,42% | +2,42% | -1,39% | +4,66% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 42 | 40,48% | -1,19% | +2,84% | -1,15% | +5,13% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 13 | 38,46% | -5,26% | +8,91% | -0,09% | +11,67% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 45 | 62,22% | +3,45% | +3,45% | -1,53% | +6,01% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +2,11% | +2,11% | -0,13% | +5,37% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 40 | 40,00% | -2,21% | +4,17% | -1,25% | +6,63% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 10 | 20,00% | -8,93% | +12,17% | -0,05% | +14,85% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 42 | 59,52% | +4,45% | +4,45% | -1,88% | +7,20% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 37 | 35,14% | -1,98% | +5,21% | -1,57% | +8,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 8 | 25,00% | -12,28% | +12,28% | -0,83% | +16,12% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 38 | 60,53% | +5,27% | +5,27% | -2,61% | +8,56% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 33 | 57,58% | +0,33% | +6,26% | -2,33% | +9,61% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 4 | 0,00% | -11,68% | +11,68% | -1,55% | +14,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 33 | 63,64% | +7,09% | +7,09% | -3,02% | +10,75% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 28 | 35,71% | +1,14% | +8,07% | -2,76% | +11,80% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Classic technical | 3 | 0,00% | -24,16% | +24,16% | -1,93% | +28,09% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 24 | 79,17% | +9,90% | +9,90% | -3,14% | +13,82% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 19 | 31,58% | -6,76% | +9,16% | -2,79% | +13,56% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 9 | 100,00% | +23,21% | +23,21% | -2,48% | +26,87% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 8 | 37,50% | -6,16% | +23,55% | -2,38% | +27,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 31 | 41,94% | -0,51% | +0,27% | -0,38% | +0,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 50 | 60,00% | +0,68% | +0,28% | -0,33% | +1,27% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 8 | 62,50% | +2,09% | +2,48% | +0,94% | +3,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 44 | 52,27% | +0,36% | +0,17% | -0,46% | +1,15% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 49 | 55,10% | +1,12% | +0,64% | -0,09% | +1,89% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 8 | 50,00% | +3,05% | +3,38% | +2,44% | +5,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 43 | 58,14% | +0,59% | +0,16% | -0,54% | +1,40% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 31 | 32,26% | -2,13% | +1,30% | -1,89% | +4,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 48 | 54,17% | +1,63% | +1,08% | -1,65% | +3,80% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 7 | 57,14% | +3,29% | +3,59% | -0,23% | +7,51% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 42 | 45,24% | +0,45% | +0,05% | -1,97% | +2,63% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 31 | 38,71% | -3,99% | +2,48% | -2,71% | +6,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 46 | 52,17% | +2,70% | +2,15% | -2,33% | +6,26% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | +2,00% | +2,23% | -1,09% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 40 | 57,50% | +0,50% | +0,83% | -2,85% | +4,95% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 30 | 40,00% | -4,62% | +3,19% | -2,99% | +8,53% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 45 | 60,00% | +3,94% | +2,99% | -2,61% | +8,38% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | +0,24% | +0,39% | -1,74% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 38 | 60,53% | +1,56% | +1,53% | -3,12% | +6,72% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 27 | 48,15% | -3,79% | +3,79% | -2,82% | +10,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 42 | 64,29% | +5,23% | +3,73% | -2,64% | +10,21% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +2,95% | +3,56% | +0,53% | +11,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 35 | 68,57% | +2,58% | +1,49% | -3,20% | +7,51% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 25 | 56,00% | -2,94% | +2,94% | -3,94% | +9,85% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 38 | 73,68% | +7,17% | +4,70% | -3,70% | +11,67% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 4 | 75,00% | +2,65% | +12,47% | -1,31% | +16,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 33 | 66,67% | +1,05% | +1,58% | -4,09% | +8,18% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 22 | 68,18% | -2,23% | +2,23% | -4,78% | +9,45% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 33 | 84,85% | +10,06% | +6,48% | -4,40% | +15,24% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 4 | 75,00% | -0,95% | +12,49% | -1,31% | +25,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 30 | 63,33% | -5,01% | +5,01% | -4,70% | +12,46% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 20 | 55,00% | -7,30% | +7,30% | -5,27% | +16,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 24 | 83,33% | +6,83% | +8,73% | -5,48% | +18,84% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 24 | 50,00% | -8,73% | +8,73% | -5,48% | +18,84% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 8 | 0,00% | -20,65% | +20,65% | -6,72% | +36,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 9 | 0,00% | -20,03% | +20,03% | -6,87% | +36,10% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 9 | 0,00% | -20,03% | +20,03% | -6,87% | +36,10% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 32 | 53,12% | +0,60% | +0,65% | -0,11% | +1,67% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 46 | 58,70% | +0,38% | +0,39% | -0,19% | +1,33% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 48 | 52,08% | +0,36% | +0,39% | -0,24% | +1,28% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 31 | 54,84% | +1,16% | +1,19% | +0,33% | +2,22% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 45 | 48,89% | +0,56% | +1,10% | +0,18% | +1,94% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 47 | 44,68% | +0,33% | +0,98% | +0,13% | +2,12% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 30 | 56,67% | +1,49% | +1,67% | -1,28% | +3,75% | PESO OK | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 44 | 50,00% | +1,21% | +1,88% | -1,38% | +4,06% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 46 | 50,00% | +0,19% | +1,61% | -1,45% | +3,71% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 28 | 64,29% | +2,42% | +2,62% | -1,88% | +5,56% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 42 | 57,14% | +2,10% | +3,39% | -1,94% | +6,65% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 44 | 50,00% | -0,40% | +3,23% | -2,13% | +6,35% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 26 | 53,85% | +2,78% | +2,70% | -2,35% | +6,28% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 40 | 62,50% | +3,23% | +4,82% | -2,29% | +8,56% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +3,96% | +3,96% | -2,17% | +8,29% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 42 | 40,48% | -1,53% | +4,44% | -2,51% | +8,17% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 23 | 56,52% | +1,74% | +1,58% | -3,19% | +5,64% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 37 | 67,57% | +6,26% | +6,46% | -2,85% | +10,12% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +3,45% | +3,45% | -2,62% | +8,30% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 39 | 43,59% | -3,39% | +5,23% | -3,14% | +9,13% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 34 | 85,29% | +9,62% | +8,52% | -3,78% | +12,96% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 36 | 30,56% | -6,64% | +6,07% | -3,97% | +10,94% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 29 | 82,76% | +14,18% | +12,26% | -4,79% | +17,23% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 32 | 37,50% | -10,96% | +9,67% | -5,06% | +14,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 16 | 12,50% | -22,24% | +22,24% | -5,75% | +27,54% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 20 | 85,00% | +17,02% | +17,55% | -6,56% | +22,64% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 24 | 16,67% | -15,48% | +14,70% | -6,61% | +19,50% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Classic technical | 2 | 0,00% | -37,38% | +37,38% | -6,43% | +45,65% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 7 | 14,29% | -19,93% | +29,65% | -7,87% | +36,46% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 9 | 44,44% | -9,40% | +31,27% | -7,77% | +37,05% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 48 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 51 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 54 | 37,04% | +0,24% |
| BTC | BREVE | Famiglia statistica | 150 | 56,00% | +0,89% |
| BTC | BREVE | Microstruttura exchange | 9 | 66,67% | +1,28% |
| BTC | BREVE | Tecnico | 135 | 40,00% | +0,06% |
| BTC | SETTIMANALE | Classic technical | 38 | 34,21% | -5,04% |
| BTC | SETTIMANALE | Famiglia statistica | 134 | 57,46% | +3,40% |
| BTC | SETTIMANALE | Microstruttura exchange | 6 | 50,00% | +0,81% |
| BTC | SETTIMANALE | Tecnico | 119 | 38,66% | -1,78% |
| BTC | SWING | Classic technical | 12 | 16,67% | -12,08% |
| BTC | SWING | Famiglia statistica | 71 | 61,97% | +6,11% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 61 | 47,54% | +0,70% |
| BTC | MEDIO | Classic technical | 3 | 0,00% | -24,16% |
| BTC | MEDIO | Famiglia statistica | 33 | 84,85% | +13,53% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 27 | 33,33% | -6,58% |
| DOGE | BREVE | Classic technical | 93 | 39,78% | -1,28% |
| DOGE | BREVE | Famiglia statistica | 147 | 56,46% | +1,14% |
| DOGE | BREVE | Microstruttura exchange | 23 | 56,52% | +2,79% |
| DOGE | BREVE | Tecnico | 129 | 51,94% | +0,47% |
| DOGE | SETTIMANALE | Classic technical | 88 | 42,05% | -4,14% |
| DOGE | SETTIMANALE | Famiglia statistica | 133 | 58,65% | +3,92% |
| DOGE | SETTIMANALE | Microstruttura exchange | 19 | 52,63% | +1,60% |
| DOGE | SETTIMANALE | Tecnico | 113 | 61,95% | +1,50% |
| DOGE | SWING | Classic technical | 47 | 61,70% | -2,61% |
| DOGE | SWING | Famiglia statistica | 71 | 78,87% | +8,52% |
| DOGE | SWING | Microstruttura exchange | 8 | 75,00% | +0,85% |
| DOGE | SWING | Tecnico | 63 | 65,08% | -1,84% |
| DOGE | MEDIO | Classic technical | 28 | 39,29% | -11,11% |
| DOGE | MEDIO | Famiglia statistica | 33 | 60,61% | -0,50% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 33 | 36,36% | -11,81% |
| SOL | BREVE | Classic technical | 93 | 54,84% | +1,07% |
| SOL | BREVE | Famiglia statistica | 135 | 52,59% | +0,71% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 141 | 48,94% | +0,29% |
| SOL | SETTIMANALE | Classic technical | 77 | 58,44% | +2,33% |
| SOL | SETTIMANALE | Famiglia statistica | 119 | 62,18% | +3,77% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +3,10% |
| SOL | SETTIMANALE | Tecnico | 125 | 44,80% | -1,71% |
| SOL | SWING | Classic technical | 42 | 38,10% | -6,19% |
| SOL | SWING | Famiglia statistica | 63 | 84,13% | +11,72% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 4 | 50,00% | +12,98% |
| SOL | SWING | Tecnico | 68 | 33,82% | -8,67% |
| SOL | MEDIO | Classic technical | 18 | 11,11% | -23,92% |
| SOL | MEDIO | Famiglia statistica | 27 | 66,67% | +7,44% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 33 | 24,24% | -13,82% |

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
