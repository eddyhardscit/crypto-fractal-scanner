# Calibrazione pesi Global Confluence

Generato: 2026-09-03 05:32 UTC

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
| BTC | 55 | PRIMA CALIBRAZIONE | 54 | 15 | 0 | 0 | Famiglia statistica | 1g | 53,70% | +0,39% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 55 | PRIMA CALIBRAZIONE | 51 | 20 | 0 | 0 | Tecnico | 1g | 50,98% | +0,30% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 55 | PRIMA CALIBRAZIONE | 53 | 22 | 0 | 0 | Famiglia statistica | 1g | 58,49% | +0,65% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 22 | 36,36% | +0,27% | +0,74% | +0,03% | +1,28% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 54 | 53,70% | +0,39% | +0,39% | -0,06% | +0,93% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 49 | 38,78% | +0,11% | +0,53% | +0,05% | +1,07% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 21 | 38,10% | +0,34% | +1,07% | +0,48% | +1,72% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 53 | 54,72% | +0,83% | +0,83% | +0,25% | +1,50% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 48 | 43,75% | +0,17% | +1,03% | +0,44% | +1,70% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 20 | 35,00% | -0,11% | +1,82% | -0,47% | +3,30% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 52 | 55,77% | +1,28% | +1,28% | -0,91% | +2,87% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 47 | 36,17% | -0,17% | +1,63% | -0,71% | +3,18% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 18 | 38,89% | -2,02% | +4,43% | -0,79% | +6,56% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 50 | 50,00% | +2,22% | +2,22% | -1,46% | +4,49% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 45 | 40,00% | -1,17% | +2,59% | -1,24% | +4,90% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 16 | 31,25% | -4,63% | +6,88% | -0,73% | +9,92% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 48 | 58,33% | +3,12% | +3,12% | -1,66% | +5,78% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 43 | 37,21% | -2,19% | +3,74% | -1,41% | +6,33% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 13 | 38,46% | -6,50% | +9,73% | -0,20% | +12,79% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 45 | 62,22% | +4,26% | +4,26% | -1,80% | +7,12% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | +0,69% | +0,69% | -0,88% | +5,44% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 40 | 40,00% | -1,71% | +4,93% | -1,50% | +7,86% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 9 | 33,33% | -9,68% | +12,16% | -0,19% | +16,21% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 41 | 63,41% | +6,23% | +6,23% | -2,13% | +9,65% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 36 | 58,33% | +0,54% | +7,27% | -1,80% | +10,76% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 4 | 0,00% | -11,68% | +11,68% | -1,55% | +14,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 34 | 64,71% | +7,57% | +7,57% | -3,00% | +11,24% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 29 | 37,93% | +1,92% | +8,61% | -2,74% | +12,34% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Classic technical | 4 | 0,00% | -24,06% | +24,06% | -1,55% | +28,48% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 27 | 81,48% | +11,37% | +11,37% | -2,95% | +15,45% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 22 | 31,82% | -7,08% | +11,07% | -2,60% | +15,59% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 12 | 100,00% | +22,75% | +22,75% | -2,66% | +26,79% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 11 | 36,36% | -6,68% | +22,95% | -2,60% | +27,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 31 | 41,94% | -0,51% | +0,27% | -0,38% | +0,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 53 | 58,49% | +0,65% | +0,26% | -0,39% | +1,21% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 8 | 62,50% | +2,09% | +2,48% | +0,94% | +3,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 47 | 53,19% | +0,33% | +0,15% | -0,53% | +1,08% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 52 | 57,69% | +1,14% | +0,53% | -0,24% | +1,72% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 8 | 50,00% | +3,05% | +3,38% | +2,44% | +5,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 46 | 54,35% | +0,46% | +0,06% | -0,68% | +1,23% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 31 | 32,26% | -2,13% | +1,30% | -1,89% | +4,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 51 | 56,86% | +1,65% | +0,89% | -1,79% | +3,61% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 8 | 50,00% | +2,64% | +2,90% | -0,79% | +6,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 45 | 42,22% | +0,28% | -0,09% | -2,11% | +2,49% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 31 | 38,71% | -3,99% | +2,48% | -2,71% | +6,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 49 | 55,10% | +2,80% | +1,75% | -2,57% | +5,97% | PESO OK | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | +1,34% | +1,54% | -1,56% | +8,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 43 | 53,49% | +0,17% | +0,47% | -3,09% | +4,71% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 31 | 38,71% | -4,80% | +2,76% | -3,30% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 47 | 59,57% | +3,65% | +2,55% | -2,90% | +8,06% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | +0,24% | +0,39% | -1,74% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 41 | 56,10% | +0,95% | +0,92% | -3,53% | +6,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 30 | 43,33% | -4,32% | +2,51% | -3,63% | +9,66% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 45 | 60,00% | +4,28% | +2,87% | -3,19% | +9,73% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 7 | 57,14% | -0,43% | +0,00% | -2,75% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 38 | 63,16% | +1,66% | +0,66% | -3,81% | +7,16% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 27 | 51,85% | -4,09% | +4,09% | -3,41% | +12,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 41 | 75,61% | +7,80% | +5,51% | -3,08% | +13,75% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +4,21% | +12,07% | +0,53% | +20,35% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 34 | 67,65% | +1,33% | +1,84% | -3,74% | +8,94% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 22 | 68,18% | -2,23% | +2,23% | -4,78% | +9,45% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 34 | 85,29% | +10,34% | +6,86% | -4,31% | +16,06% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 4 | 75,00% | -0,95% | +12,49% | -1,31% | +25,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 30 | 63,33% | -5,01% | +5,01% | -4,70% | +12,46% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 20 | 55,00% | -7,30% | +7,30% | -5,27% | +16,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 27 | 85,19% | +8,05% | +9,75% | -5,14% | +21,49% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 27 | 44,44% | -9,75% | +9,75% | -5,14% | +21,49% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 11 | 0,00% | -18,94% | +18,94% | -6,48% | +36,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 12 | 0,00% | -18,62% | +18,62% | -6,62% | +36,70% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 12 | 0,00% | -18,62% | +18,62% | -6,62% | +36,70% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 35 | 51,43% | +0,48% | +0,53% | -0,26% | +1,49% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 49 | 57,14% | +0,31% | +0,32% | -0,29% | +1,22% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 51 | 50,98% | +0,30% | +0,32% | -0,33% | +1,18% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 34 | 50,00% | +0,85% | +0,88% | -0,00% | +1,85% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 48 | 45,83% | +0,38% | +0,89% | -0,05% | +1,70% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 50 | 42,00% | +0,17% | +0,78% | -0,08% | +1,88% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 33 | 54,55% | +1,15% | +1,31% | -1,56% | +3,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 47 | 48,94% | +0,99% | +1,62% | -1,57% | +3,90% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 49 | 48,98% | +0,04% | +1,38% | -1,63% | +3,58% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 31 | 61,29% | +1,98% | +2,16% | -2,10% | +5,44% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 45 | 55,56% | +1,81% | +3,02% | -2,10% | +6,49% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 47 | 48,94% | -0,51% | +2,88% | -2,26% | +6,22% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 29 | 55,17% | +2,64% | +2,58% | -2,36% | +6,66% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 43 | 62,79% | +3,11% | +4,58% | -2,30% | +8,66% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 45 | 42,22% | -1,33% | +4,24% | -2,51% | +8,29% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 26 | 61,54% | +2,53% | +2,40% | -2,82% | +7,04% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 40 | 65,00% | +5,48% | +6,62% | -2,63% | +10,70% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +3,45% | +3,45% | -2,62% | +8,30% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 42 | 47,62% | -2,53% | +5,47% | -2,91% | +9,75% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 22 | 40,91% | -0,32% | +1,95% | -3,91% | +6,19% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 36 | 86,11% | +10,98% | +9,94% | -3,28% | +14,70% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 38 | 31,58% | -6,80% | +7,21% | -3,65% | +12,34% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 30 | 83,33% | +14,96% | +13,10% | -4,70% | +18,17% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 32 | 37,50% | -10,96% | +9,67% | -5,06% | +14,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 19 | 10,53% | -24,79% | +24,79% | -5,09% | +31,09% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 23 | 86,96% | +19,81% | +20,27% | -5,91% | +26,21% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 27 | 14,81% | -18,03% | +17,33% | -6,05% | +22,90% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Classic technical | 5 | 0,00% | -35,45% | +35,45% | -6,51% | +45,53% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 8 | 12,50% | -21,42% | +29,92% | -7,77% | +37,49% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 12 | 33,33% | -15,59% | +32,00% | -7,46% | +39,15% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 51 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 54 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 63 | 36,51% | +0,17% |
| BTC | BREVE | Famiglia statistica | 159 | 54,72% | +0,83% |
| BTC | BREVE | Microstruttura exchange | 9 | 66,67% | +1,28% |
| BTC | BREVE | Tecnico | 144 | 39,58% | +0,04% |
| BTC | SETTIMANALE | Classic technical | 47 | 36,17% | -4,15% |
| BTC | SETTIMANALE | Famiglia statistica | 143 | 56,64% | +3,16% |
| BTC | SETTIMANALE | Microstruttura exchange | 8 | 50,00% | +0,56% |
| BTC | SETTIMANALE | Tecnico | 128 | 39,06% | -1,68% |
| BTC | SWING | Classic technical | 13 | 23,08% | -10,30% |
| BTC | SWING | Famiglia statistica | 75 | 64,00% | +6,84% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 65 | 49,23% | +1,16% |
| BTC | MEDIO | Classic technical | 4 | 0,00% | -24,06% |
| BTC | MEDIO | Famiglia statistica | 39 | 87,18% | +14,87% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 33 | 33,33% | -6,95% |
| DOGE | BREVE | Classic technical | 93 | 39,78% | -1,28% |
| DOGE | BREVE | Famiglia statistica | 156 | 57,69% | +1,14% |
| DOGE | BREVE | Microstruttura exchange | 24 | 54,17% | +2,59% |
| DOGE | BREVE | Tecnico | 138 | 50,00% | +0,36% |
| DOGE | SETTIMANALE | Classic technical | 92 | 40,22% | -4,37% |
| DOGE | SETTIMANALE | Famiglia statistica | 141 | 58,16% | +3,56% |
| DOGE | SETTIMANALE | Microstruttura exchange | 22 | 45,45% | +0,43% |
| DOGE | SETTIMANALE | Tecnico | 122 | 57,38% | +0,90% |
| DOGE | SWING | Classic technical | 49 | 59,18% | -3,25% |
| DOGE | SWING | Famiglia statistica | 75 | 80,00% | +8,95% |
| DOGE | SWING | Microstruttura exchange | 9 | 77,78% | +1,92% |
| DOGE | SWING | Tecnico | 64 | 65,62% | -1,64% |
| DOGE | MEDIO | Classic technical | 31 | 35,48% | -11,43% |
| DOGE | MEDIO | Famiglia statistica | 39 | 58,97% | -0,16% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 39 | 30,77% | -12,48% |
| SOL | BREVE | Classic technical | 102 | 51,96% | +0,82% |
| SOL | BREVE | Famiglia statistica | 144 | 50,69% | +0,56% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 150 | 47,33% | +0,17% |
| SOL | SETTIMANALE | Classic technical | 86 | 59,30% | +2,37% |
| SOL | SETTIMANALE | Famiglia statistica | 128 | 60,94% | +3,39% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 13 | 61,54% | +3,01% |
| SOL | SETTIMANALE | Tecnico | 134 | 46,27% | -1,42% |
| SOL | SWING | Classic technical | 43 | 39,53% | -5,62% |
| SOL | SWING | Famiglia statistica | 66 | 84,85% | +12,79% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 4 | 50,00% | +12,98% |
| SOL | SWING | Tecnico | 70 | 34,29% | -8,70% |
| SOL | MEDIO | Classic technical | 24 | 8,33% | -27,01% |
| SOL | MEDIO | Famiglia statistica | 31 | 67,74% | +9,17% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 39 | 20,51% | -17,28% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 8 | in attesa di controlli maturati |
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
