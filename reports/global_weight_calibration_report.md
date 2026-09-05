# Calibrazione pesi Global Confluence

Generato: 2026-09-05 08:22 UTC

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
| BTC | 57 | PRIMA CALIBRAZIONE | 56 | 16 | 0 | 0 | Famiglia statistica | 1g | 53,57% | +0,43% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 57 | PRIMA CALIBRAZIONE | 53 | 21 | 0 | 0 | Tecnico | 1g | 50,94% | +0,33% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 57 | PRIMA CALIBRAZIONE | 55 | 22 | 0 | 0 | Famiglia statistica | 1g | 58,18% | +0,56% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 24 | 37,50% | +0,37% | +0,81% | +0,13% | +1,33% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 56 | 53,57% | +0,43% | +0,43% | -0,01% | +0,97% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 4 | 50,00% | -0,20% | -0,20% | -0,66% | +0,18% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 51 | 39,22% | +0,16% | +0,57% | +0,10% | +1,10% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 23 | 43,48% | +0,63% | +1,29% | +0,68% | +2,02% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 55 | 56,36% | +0,94% | +0,94% | +0,34% | +1,63% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 50 | 46,00% | +0,31% | +1,13% | +0,53% | +1,83% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 22 | 40,91% | +0,13% | +1,88% | -0,63% | +3,40% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 54 | 57,41% | +1,33% | +1,33% | -0,96% | +2,93% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 49 | 38,78% | -0,06% | +1,66% | -0,77% | +3,23% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 20 | 45,00% | -1,53% | +4,27% | -0,94% | +6,39% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 52 | 51,92% | +2,25% | +2,25% | -1,49% | +4,50% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 47 | 42,55% | -1,00% | +2,60% | -1,28% | +4,90% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 18 | 38,89% | -3,89% | +6,35% | -0,99% | +9,27% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 50 | 60,00% | +3,08% | +3,08% | -1,72% | +5,71% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 45 | 40,00% | -2,00% | +3,67% | -1,48% | +6,22% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 15 | 46,67% | -5,57% | +8,49% | -0,79% | +11,40% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 47 | 63,83% | +4,10% | +4,10% | -1,92% | +6,92% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 42 | 42,86% | -1,61% | +4,72% | -1,65% | +7,60% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 11 | 45,45% | -6,91% | +10,96% | -0,26% | +14,63% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 43 | 65,12% | +6,20% | +6,20% | -2,06% | +9,55% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 38 | 60,53% | +0,80% | +7,18% | -1,74% | +10,59% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 6 | 0,00% | -17,01% | +17,01% | -1,17% | +19,54% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 36 | 66,67% | +8,69% | +8,69% | -2,85% | +12,28% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 31 | 35,48% | +0,01% | +9,84% | -2,59% | +13,48% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 4 | 0,00% | -24,06% | +24,06% | -1,55% | +28,48% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 29 | 82,76% | +12,27% | +12,27% | -2,97% | +16,23% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 24 | 33,33% | -6,62% | +12,18% | -2,65% | +16,52% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 14 | 100,00% | +22,63% | +22,63% | -3,07% | +26,43% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 11 | 36,36% | -6,68% | +22,95% | -2,60% | +27,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 31 | 41,94% | -0,51% | +0,27% | -0,38% | +0,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 55 | 58,18% | +0,56% | +0,32% | -0,33% | +1,26% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 8 | 62,50% | +2,09% | +2,48% | +0,94% | +3,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 49 | 53,06% | +0,40% | +0,22% | -0,45% | +1,15% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 54 | 55,56% | +0,91% | +0,69% | -0,08% | +1,92% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 8 | 50,00% | +3,05% | +3,38% | +2,44% | +5,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 48 | 56,25% | +0,65% | +0,27% | -0,49% | +1,48% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 31 | 32,26% | -2,13% | +1,30% | -1,89% | +4,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 53 | 54,72% | +1,43% | +1,02% | -1,81% | +3,75% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 8 | 50,00% | +2,64% | +2,90% | -0,79% | +6,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 47 | 44,68% | +0,46% | +0,10% | -2,12% | +2,70% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 31 | 38,71% | -3,99% | +2,48% | -2,71% | +6,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 51 | 52,94% | +2,58% | +1,79% | -2,64% | +5,97% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | +1,34% | +1,54% | -1,56% | +8,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 45 | 55,56% | +0,29% | +0,57% | -3,15% | +4,77% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 31 | 38,71% | -4,80% | +2,76% | -3,30% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 49 | 59,18% | +3,51% | +2,44% | -3,07% | +7,85% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 8 | 50,00% | +0,28% | +0,41% | -2,23% | +8,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 43 | 55,81% | +0,90% | +0,88% | -3,69% | +6,20% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 31 | 41,94% | -4,39% | +2,22% | -3,95% | +9,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 46 | 58,70% | +4,05% | +2,67% | -3,42% | +9,45% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 7 | 57,14% | -0,43% | +0,00% | -2,75% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 40 | 60,00% | +1,38% | +0,43% | -4,15% | +6,82% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 28 | 50,00% | -4,13% | +3,76% | -3,68% | +12,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 43 | 74,42% | +7,44% | +5,26% | -3,26% | +13,71% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 6 | 66,67% | +2,65% | +9,19% | -1,41% | +17,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 36 | 66,67% | +1,26% | +1,74% | -3,92% | +9,15% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 23 | 65,22% | -3,23% | +3,23% | -4,58% | +10,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 36 | 86,11% | +11,08% | +7,79% | -4,11% | +17,58% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 4 | 75,00% | -0,95% | +12,49% | -1,31% | +25,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 31 | 64,52% | -4,14% | +5,56% | -4,59% | +13,43% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 20 | 55,00% | -7,30% | +7,30% | -5,27% | +16,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 29 | 86,21% | +9,11% | +10,68% | -4,92% | +22,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 28 | 42,86% | -10,27% | +10,27% | -5,04% | +22,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 13 | 0,00% | -18,83% | +18,83% | -6,54% | +36,85% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 14 | 0,00% | -18,56% | +18,56% | -6,65% | +36,74% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 14 | 0,00% | -18,56% | +18,56% | -6,65% | +36,74% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 37 | 51,35% | +0,51% | +0,56% | -0,20% | +1,49% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 51 | 56,86% | +0,34% | +0,35% | -0,25% | +1,23% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 53 | 50,94% | +0,33% | +0,35% | -0,29% | +1,19% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 36 | 52,78% | +0,96% | +0,99% | +0,10% | +1,99% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 50 | 48,00% | +0,48% | +0,96% | +0,03% | +1,80% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 52 | 44,23% | +0,27% | +0,86% | -0,01% | +1,97% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 35 | 54,29% | +1,13% | +1,28% | -1,68% | +3,50% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 49 | 48,98% | +0,98% | +1,58% | -1,65% | +3,85% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 51 | 49,02% | +0,07% | +1,35% | -1,71% | +3,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 33 | 57,58% | +1,81% | +1,98% | -2,35% | +5,19% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 47 | 53,19% | +1,70% | +2,86% | -2,27% | +6,27% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 49 | 46,94% | -0,52% | +2,73% | -2,42% | +6,02% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 31 | 51,61% | +2,33% | +2,27% | -2,69% | +6,36% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 45 | 60,00% | +2,87% | +4,28% | -2,53% | +8,37% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 47 | 40,43% | -1,37% | +3,97% | -2,72% | +8,02% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 28 | 64,29% | +2,59% | +2,47% | -2,85% | +7,29% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 42 | 66,67% | +5,38% | +6,47% | -2,66% | +10,69% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 44 | 50,00% | -2,27% | +5,38% | -2,93% | +9,78% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 24 | 45,83% | +0,76% | +2,84% | -3,58% | +7,36% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 38 | 81,58% | +9,74% | +10,08% | -3,10% | +15,00% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 3 | 66,67% | +10,82% | +10,82% | -3,34% | +16,86% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 40 | 35,00% | -5,83% | +7,48% | -3,46% | +12,74% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 32 | 84,38% | +16,31% | +14,56% | -4,50% | +19,90% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 34 | 35,29% | -12,47% | +11,26% | -4,86% | +16,53% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 20 | 10,00% | -25,57% | +25,57% | -4,94% | +31,98% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 25 | 88,00% | +21,36% | +21,78% | -5,61% | +28,01% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 29 | 13,79% | -19,48% | +18,84% | -5,78% | +24,67% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Classic technical | 6 | 0,00% | -34,78% | +34,78% | -6,95% | +44,84% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 10 | 20,00% | -17,03% | +30,34% | -8,09% | +38,20% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 14 | 28,57% | -17,93% | +31,99% | -7,74% | +39,42% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 53 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 56 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 69 | 40,58% | +0,38% |
| BTC | BREVE | Famiglia statistica | 165 | 55,76% | +0,89% |
| BTC | BREVE | Microstruttura exchange | 10 | 60,00% | +0,99% |
| BTC | BREVE | Tecnico | 150 | 41,33% | +0,14% |
| BTC | SETTIMANALE | Classic technical | 53 | 43,40% | -3,48% |
| BTC | SETTIMANALE | Famiglia statistica | 149 | 58,39% | +3,11% |
| BTC | SETTIMANALE | Microstruttura exchange | 9 | 55,56% | +0,53% |
| BTC | SETTIMANALE | Tecnico | 134 | 41,79% | -1,53% |
| BTC | SWING | Classic technical | 17 | 29,41% | -10,48% |
| BTC | SWING | Famiglia statistica | 79 | 65,82% | +7,33% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 69 | 49,28% | +0,45% |
| BTC | MEDIO | Classic technical | 4 | 0,00% | -24,06% |
| BTC | MEDIO | Famiglia statistica | 43 | 88,37% | +15,65% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 35 | 34,29% | -6,64% |
| DOGE | BREVE | Classic technical | 93 | 39,78% | -1,28% |
| DOGE | BREVE | Famiglia statistica | 162 | 56,17% | +0,96% |
| DOGE | BREVE | Microstruttura exchange | 24 | 54,17% | +2,59% |
| DOGE | BREVE | Tecnico | 144 | 51,39% | +0,50% |
| DOGE | SETTIMANALE | Classic technical | 93 | 39,78% | -4,39% |
| DOGE | SETTIMANALE | Famiglia statistica | 146 | 56,85% | +3,35% |
| DOGE | SETTIMANALE | Microstruttura exchange | 23 | 47,83% | +0,43% |
| DOGE | SETTIMANALE | Tecnico | 128 | 57,03% | +0,84% |
| DOGE | SWING | Classic technical | 51 | 56,86% | -3,72% |
| DOGE | SWING | Famiglia statistica | 79 | 79,75% | +9,10% |
| DOGE | SWING | Microstruttura exchange | 10 | 70,00% | +1,21% |
| DOGE | SWING | Tecnico | 67 | 65,67% | -1,24% |
| DOGE | MEDIO | Classic technical | 33 | 33,33% | -11,84% |
| DOGE | MEDIO | Famiglia statistica | 43 | 58,14% | +0,10% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 42 | 28,57% | -13,03% |
| SOL | BREVE | Classic technical | 108 | 52,78% | +0,86% |
| SOL | BREVE | Famiglia statistica | 150 | 51,33% | +0,60% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 156 | 48,08% | +0,22% |
| SOL | SETTIMANALE | Classic technical | 92 | 57,61% | +2,22% |
| SOL | SETTIMANALE | Famiglia statistica | 134 | 59,70% | +3,25% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 140 | 45,71% | -1,35% |
| SOL | SWING | Classic technical | 45 | 42,22% | -4,81% |
| SOL | SWING | Famiglia statistica | 70 | 82,86% | +12,74% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 5 | 60,00% | +13,52% |
| SOL | SWING | Tecnico | 74 | 35,14% | -8,88% |
| SOL | MEDIO | Classic technical | 26 | 7,69% | -27,69% |
| SOL | MEDIO | Famiglia statistica | 35 | 68,57% | +10,39% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 2 | 100,00% | +20,54% |
| SOL | MEDIO | Tecnico | 43 | 18,60% | -18,98% |

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
