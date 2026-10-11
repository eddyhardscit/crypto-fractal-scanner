# Calibrazione pesi Global Confluence

Generato: 2026-10-11 05:33 UTC

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
| BTC | 87 | UTILE | 84 | 26 | 17 | 0 | Famiglia statistica | 1g | 50,00% | +0,31% | campione utile, valutare con prudenza |
| SOL | 87 | UTILE | 80 | 31 | 16 | 0 | Famiglia statistica | 1g | 55,00% | +0,50% | campione utile, valutare con prudenza |
| DOGE | 87 | UTILE | 85 | 32 | 17 | 0 | Famiglia statistica | 1g | 58,82% | +0,56% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 34 | 41,18% | -0,03% | +0,55% | -0,23% | +1,11% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 84 | 50,00% | +0,31% | +0,23% | -0,28% | +0,74% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 8 | 37,50% | -0,49% | -0,49% | -1,07% | -0,05% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 79 | 44,30% | -0,01% | +0,25% | -0,22% | +0,78% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 34 | 41,18% | -0,12% | +0,89% | -0,02% | +1,61% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 83 | 53,01% | +0,65% | +0,52% | -0,20% | +1,21% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 8 | 25,00% | -0,28% | -0,28% | -1,06% | +0,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 78 | 43,59% | -0,02% | +0,51% | -0,11% | +1,19% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 34 | 35,29% | -0,66% | +1,44% | -1,08% | +3,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Famiglia statistica | 82 | 51,22% | +0,92% | +0,84% | -1,29% | +2,55% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 8 | 25,00% | -0,50% | -0,50% | -1,88% | +1,29% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 77 | 36,36% | -0,23% | +0,86% | -1,22% | +2,57% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 34 | 35,29% | -2,33% | +3,06% | -1,68% | +5,50% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 80 | 47,50% | +1,68% | +1,66% | -1,87% | +4,07% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 75 | 41,33% | -0,74% | +1,52% | -1,82% | +4,01% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 32 | 34,38% | -3,91% | +4,64% | -1,85% | +7,80% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 78 | 55,13% | +2,38% | +2,51% | -2,11% | +5,27% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 73 | 45,21% | -1,01% | +2,48% | -2,08% | +5,24% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 29 | 41,38% | -4,39% | +5,56% | -1,70% | +9,12% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 76 | 65,79% | +3,40% | +3,42% | -2,34% | +6,48% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | -1,21% | -1,21% | -3,81% | +1,86% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 70 | 48,57% | -0,32% | +3,48% | -2,30% | +6,59% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 29 | 24,14% | -4,15% | +5,09% | -1,91% | +9,57% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 74 | 62,16% | +4,84% | +4,75% | -2,66% | +8,46% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 7 | 42,86% | -0,11% | -0,11% | -4,30% | +2,85% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 67 | 55,22% | +1,41% | +5,03% | -2,61% | +8,78% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 28 | 46,43% | -4,92% | +9,04% | -2,22% | +12,89% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 69 | 78,26% | +8,34% | +8,34% | -2,78% | +12,22% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 62 | 58,06% | +1,49% | +8,84% | -2,74% | +12,73% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 24 | 66,67% | -2,02% | +13,37% | -2,62% | +17,60% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 63 | 92,06% | +12,40% | +12,40% | -2,97% | +16,63% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 58 | 63,79% | +0,89% | +12,38% | -2,84% | +16,78% | PESO OK | 0,0 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 16 | 50,00% | -8,74% | +18,39% | -1,64% | +24,20% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 48 | 100,00% | +22,62% | +22,62% | -2,39% | +27,24% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 43 | 48,84% | -2,73% | +22,81% | -2,15% | +27,46% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 4 | 0,00% | -33,67% | +33,67% | -1,55% | +38,08% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 34 | 100,00% | +27,66% | +27,66% | -3,00% | +32,81% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 29 | 41,38% | -5,53% | +28,03% | -2,74% | +33,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 47 | 40,43% | -0,63% | -0,05% | -0,92% | +0,67% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 85 | 58,82% | +0,56% | +0,01% | -0,78% | +1,01% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 11 | 63,64% | +2,53% | +2,82% | +0,75% | +3,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 79 | 50,63% | +0,12% | -0,07% | -0,88% | +0,92% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 46 | 41,30% | -1,32% | +0,27% | -0,93% | +1,22% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 84 | 59,52% | +0,89% | +0,14% | -0,95% | +1,44% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 11 | 45,45% | +2,65% | +2,89% | +1,08% | +5,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 78 | 52,56% | +0,07% | -0,17% | -1,27% | +1,13% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 45 | 31,11% | -2,23% | +0,54% | -2,66% | +3,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 83 | 57,83% | +1,25% | +0,31% | -2,64% | +3,49% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 11 | 54,55% | +2,62% | +2,81% | -1,35% | +6,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 77 | 44,16% | -0,19% | -0,31% | -2,89% | +2,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 44 | 31,82% | -4,85% | +1,94% | -3,72% | +6,77% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 81 | 54,32% | +1,71% | +1,05% | -3,73% | +5,94% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 11 | 36,36% | +2,02% | +2,17% | -2,50% | +9,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 75 | 48,00% | -1,13% | +0,26% | -4,12% | +5,21% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 44 | 27,27% | -6,50% | +3,07% | -4,35% | +8,81% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 79 | 56,96% | +1,70% | +1,99% | -4,20% | +7,98% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 11 | 45,45% | +0,78% | +0,88% | -3,00% | +9,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 73 | 43,84% | -1,35% | +1,03% | -4,66% | +7,02% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 43 | 30,23% | -7,04% | +3,70% | -4,91% | +11,04% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 76 | 53,95% | +1,39% | +2,68% | -4,75% | +9,99% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 70 | 45,71% | -1,77% | +1,40% | -5,28% | +8,53% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 43 | 39,53% | -5,45% | +4,51% | -5,57% | +13,12% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 73 | 63,01% | +3,15% | +4,21% | -5,44% | +13,34% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 11 | 45,45% | +2,03% | +5,60% | -4,35% | +14,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 67 | 47,76% | -1,49% | +2,21% | -6,06% | +10,78% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 41 | 43,90% | -7,20% | +6,23% | -5,36% | +16,47% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 68 | 57,35% | +4,21% | +8,79% | -5,19% | +19,71% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 10 | 70,00% | +1,36% | +6,74% | -4,20% | +19,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 62 | 56,45% | -1,96% | +6,83% | -5,84% | +16,87% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Classic technical | 35 | 48,57% | -7,71% | +9,69% | -5,84% | +22,14% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 62 | 70,97% | +7,46% | +11,91% | -5,52% | +26,03% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 9 | 88,89% | +12,44% | +19,48% | -5,48% | +30,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 56 | 58,93% | -2,55% | +10,47% | -6,31% | +23,79% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 31 | 3,23% | -22,01% | +21,52% | -5,10% | +38,53% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Famiglia statistica | 47 | 59,57% | +8,66% | +22,08% | -4,46% | +39,37% | PESO OK | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 7 | 71,43% | +12,69% | +24,92% | -3,96% | +37,45% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 41 | 12,20% | -14,29% | +19,07% | -5,37% | +37,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 22 | 0,00% | -25,52% | +25,52% | -4,86% | +42,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 34 | 52,94% | +8,06% | +27,26% | -4,36% | +44,55% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 4 | 75,00% | +19,48% | +38,20% | -1,31% | +51,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 30 | 0,00% | -27,32% | +27,32% | -4,76% | +43,74% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 1g | BREVE | Classic technical | 58 | 44,83% | -0,03% | +0,45% | -0,53% | +1,39% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 80 | 55,00% | +0,50% | +0,22% | -0,61% | +1,06% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 78 | 44,87% | -0,14% | +0,21% | -0,67% | +1,04% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 57 | 47,37% | +0,14% | +0,57% | -0,69% | +1,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 79 | 50,63% | +0,83% | +0,63% | -0,71% | +1,55% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 77 | 41,56% | -0,23% | +0,45% | -0,68% | +1,56% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 57 | 47,37% | +0,14% | +0,64% | -2,20% | +3,12% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 78 | 53,85% | +1,46% | +1,09% | -2,20% | +3,59% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 76 | 43,42% | -0,51% | +0,67% | -2,22% | +3,14% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 56 | 50,00% | +0,24% | +0,92% | -3,09% | +4,53% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 76 | 55,26% | +2,26% | +2,16% | -2,97% | +5,87% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 74 | 44,59% | -0,84% | +1,75% | -3,02% | +5,30% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 54 | 46,30% | +0,35% | +0,97% | -3,56% | +5,35% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 74 | 62,16% | +3,27% | +3,43% | -3,36% | +7,65% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 72 | 40,28% | -1,54% | +2,43% | -3,44% | +6,72% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 51 | 49,02% | +0,70% | +1,47% | -3,91% | +6,38% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 71 | 67,61% | +5,43% | +5,58% | -3,60% | +9,85% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 69 | 44,93% | -1,61% | +3,88% | -3,77% | +8,42% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 48 | 47,92% | +1,02% | +2,85% | -4,62% | +8,08% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 69 | 76,81% | +8,64% | +8,45% | -4,08% | +13,57% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 66 | 42,42% | -2,57% | +6,08% | -4,32% | +11,49% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 43 | 62,79% | -0,68% | +11,00% | -4,55% | +16,01% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 64 | 84,38% | +15,14% | +15,18% | -4,12% | +20,66% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 61 | 54,10% | -4,93% | +12,66% | -4,50% | +18,21% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Classic technical | 42 | 54,76% | -4,29% | +22,25% | -4,70% | +27,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 58 | 89,66% | +19,97% | +22,63% | -4,36% | +29,21% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 59 | 44,07% | -7,91% | +20,65% | -4,73% | +26,78% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 29 | 27,59% | -21,70% | +34,51% | -3,61% | +44,10% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 43 | 74,42% | +23,73% | +38,94% | -3,51% | +47,00% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +28,91% | +28,91% | -3,55% | +37,55% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 45 | 26,67% | -24,88% | +37,50% | -4,01% | +45,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 21 | 0,00% | -53,73% | +53,73% | -4,64% | +60,15% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 30 | 73,33% | +32,45% | +50,64% | -4,89% | +58,37% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +47,10% | +47,10% | -5,94% | +54,98% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 32 | 12,50% | -40,55% | +49,02% | -5,31% | +56,49% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 79 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 85 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 102 | 39,22% | -0,27% |
| BTC | BREVE | Famiglia statistica | 249 | 51,41% | +0,62% |
| BTC | BREVE | Microstruttura exchange | 24 | 29,17% | -0,42% |
| BTC | BREVE | Tecnico | 234 | 41,45% | -0,09% |
| BTC | SETTIMANALE | Classic technical | 95 | 36,84% | -3,49% |
| BTC | SETTIMANALE | Famiglia statistica | 234 | 55,98% | +2,47% |
| BTC | SETTIMANALE | Microstruttura exchange | 23 | 26,09% | -1,66% |
| BTC | SETTIMANALE | Tecnico | 218 | 44,95% | -0,69% |
| BTC | SWING | Classic technical | 57 | 35,09% | -4,53% |
| BTC | SWING | Famiglia statistica | 143 | 69,93% | +6,53% |
| BTC | SWING | Microstruttura exchange | 12 | 58,33% | +0,59% |
| BTC | SWING | Tecnico | 129 | 56,59% | +1,45% |
| BTC | MEDIO | Classic technical | 44 | 54,55% | -7,34% |
| BTC | MEDIO | Famiglia statistica | 145 | 96,55% | +19,36% |
| BTC | MEDIO | Microstruttura exchange | 9 | 100,00% | +9,68% |
| BTC | MEDIO | Tecnico | 130 | 53,85% | -1,74% |
| DOGE | BREVE | Classic technical | 138 | 37,68% | -1,38% |
| DOGE | BREVE | Famiglia statistica | 252 | 58,73% | +0,90% |
| DOGE | BREVE | Microstruttura exchange | 33 | 54,55% | +2,60% |
| DOGE | BREVE | Tecnico | 234 | 49,15% | +0,00% |
| DOGE | SETTIMANALE | Classic technical | 131 | 29,77% | -6,12% |
| DOGE | SETTIMANALE | Famiglia statistica | 236 | 55,08% | +1,60% |
| DOGE | SETTIMANALE | Microstruttura exchange | 33 | 45,45% | +1,16% |
| DOGE | SETTIMANALE | Tecnico | 218 | 45,87% | -1,41% |
| DOGE | SWING | Classic technical | 84 | 41,67% | -6,31% |
| DOGE | SWING | Famiglia statistica | 141 | 60,28% | +3,66% |
| DOGE | SWING | Microstruttura exchange | 21 | 57,14% | +1,71% |
| DOGE | SWING | Tecnico | 129 | 51,94% | -1,72% |
| DOGE | MEDIO | Classic technical | 88 | 20,45% | -17,20% |
| DOGE | MEDIO | Famiglia statistica | 143 | 62,94% | +8,00% |
| DOGE | MEDIO | Microstruttura exchange | 20 | 80,00% | +13,94% |
| DOGE | MEDIO | Tecnico | 127 | 29,92% | -12,19% |
| SOL | BREVE | Classic technical | 172 | 46,51% | +0,08% |
| SOL | BREVE | Famiglia statistica | 237 | 53,16% | +0,93% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 231 | 43,29% | -0,29% |
| SOL | SETTIMANALE | Classic technical | 161 | 48,45% | +0,43% |
| SOL | SETTIMANALE | Famiglia statistica | 221 | 61,54% | +3,62% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 215 | 43,26% | -1,32% |
| SOL | SWING | Classic technical | 91 | 54,95% | +0,22% |
| SOL | SWING | Famiglia statistica | 133 | 80,45% | +11,77% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 127 | 48,03% | -3,70% |
| SOL | MEDIO | Classic technical | 92 | 33,70% | -21,06% |
| SOL | MEDIO | Famiglia statistica | 131 | 80,92% | +24,06% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 12 | 100,00% | +28,96% |
| SOL | MEDIO | Tecnico | 136 | 30,88% | -21,20% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 3 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 2 | in attesa di controlli maturati |
| DOGE | MEDIO | 3 | in attesa di controlli maturati |

## Come leggere le raccomandazioni

- **OSSERVA**: meno di 30 controlli, nessuna modifica.
- **PESO OK / MANTIENI**: il modulo sta aiutando, ma non serve cambiare peso.
- **NON AUMENTARE**: il modulo non dimostra ancora un vantaggio sufficiente.
- **POSSIBILE AUMENTO LEGGERO**: proposta prudente, mai automatica.
- **POSSIBILE RIDUZIONE**: modulo debole con campione già abbastanza maturo.
- **ESCLUSO**: benchmark o diagnostica già inclusa in un'altra famiglia.

Nota decisiva: **non sommare mai una modifica alla Famiglia statistica e altre modifiche separate a Scanner o Market Regime**. Scanner e Market servono soltanto a capire quale parte della famiglia sta funzionando o fallendo.

## Stato attuale

Il campione comincia a essere utile. Le proposte restano prudenti e vanno verificate tra orizzonti diversi.
