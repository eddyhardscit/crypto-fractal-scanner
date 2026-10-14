# Calibrazione pesi Global Confluence

Generato: 2026-10-14 05:33 UTC

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
| BTC | 90 | UTILE | 87 | 28 | 18 | 0 | Famiglia statistica | 1g | 49,43% | +0,29% | campione utile, valutare con prudenza |
| SOL | 90 | UTILE | 83 | 32 | 18 | 0 | Famiglia statistica | 1g | 54,22% | +0,46% | campione utile, valutare con prudenza |
| DOGE | 90 | UTILE | 88 | 32 | 17 | 0 | Famiglia statistica | 1g | 59,09% | +0,53% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 35 | 42,86% | -0,02% | +0,53% | -0,31% | +1,07% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 87 | 49,43% | +0,29% | +0,23% | -0,30% | +0,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 82 | 46,34% | +0,01% | +0,25% | -0,25% | +0,77% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 35 | 42,86% | -0,11% | +0,85% | -0,05% | +1,57% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 86 | 52,33% | +0,61% | +0,52% | -0,22% | +1,20% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 81 | 45,68% | +0,01% | +0,51% | -0,13% | +1,18% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 34 | 35,29% | -0,66% | +1,44% | -1,08% | +3,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Famiglia statistica | 85 | 49,41% | +0,84% | +0,85% | -1,29% | +2,52% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 80 | 38,75% | -0,19% | +0,87% | -1,22% | +2,54% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 34 | 35,29% | -2,33% | +3,06% | -1,68% | +5,50% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 83 | 46,99% | +1,60% | +1,62% | -1,89% | +3,96% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 78 | 42,31% | -0,69% | +1,48% | -1,85% | +3,90% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 34 | 32,35% | -3,81% | +4,23% | -2,10% | +7,38% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 81 | 56,79% | +2,36% | +2,35% | -2,24% | +5,09% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 76 | 43,42% | -1,05% | +2,31% | -2,22% | +5,05% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 32 | 37,50% | -4,17% | +4,84% | -2,09% | +8,44% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 78 | 65,38% | +3,29% | +3,28% | -2,44% | +6,35% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | -1,47% | -1,47% | -4,23% | +1,69% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 73 | 46,58% | -0,39% | +3,26% | -2,44% | +6,39% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 29 | 24,14% | -4,15% | +5,09% | -1,91% | +9,57% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 76 | 60,53% | +4,69% | +4,65% | -2,68% | +8,37% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 7 | 42,86% | -0,11% | -0,11% | -4,30% | +2,85% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 70 | 57,14% | +1,37% | +4,83% | -2,65% | +8,60% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 29 | 44,83% | -4,88% | +8,60% | -2,40% | +12,46% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 71 | 76,06% | +8,03% | +8,03% | -2,89% | +11,92% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 64 | 56,25% | +1,36% | +8,48% | -2,86% | +12,38% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 25 | 64,00% | -2,25% | +13,14% | -2,64% | +17,41% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 66 | 92,42% | +12,21% | +12,21% | -2,97% | +16,46% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 61 | 65,57% | +1,25% | +12,17% | -2,85% | +16,59% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Classic technical | 19 | 57,89% | -6,34% | +16,51% | -2,09% | +22,16% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 51 | 100,00% | +21,67% | +21,67% | -2,52% | +26,30% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 46 | 52,17% | -2,13% | +21,75% | -2,31% | +26,41% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 6 | 0,00% | -33,38% | +33,38% | -1,17% | +38,35% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 36 | 100,00% | +27,95% | +27,95% | -2,85% | +33,15% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 31 | 38,71% | -7,29% | +28,33% | -2,59% | +33,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Classic technical | 50 | 40,00% | -0,58% | -0,06% | -1,00% | +0,64% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 88 | 59,09% | +0,53% | +0,00% | -0,83% | +0,98% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 11 | 63,64% | +2,53% | +2,82% | +0,75% | +3,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 82 | 50,00% | +0,13% | -0,08% | -0,94% | +0,89% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 49 | 42,86% | -1,18% | +0,20% | -1,06% | +1,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 87 | 58,62% | +0,83% | +0,10% | -1,02% | +1,37% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 11 | 45,45% | +2,65% | +2,89% | +1,08% | +5,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 81 | 53,09% | +0,10% | -0,20% | -1,33% | +1,07% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 48 | 33,33% | -2,08% | +0,50% | -2,72% | +3,62% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 86 | 56,98% | +1,20% | +0,30% | -2,67% | +3,45% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 11 | 54,55% | +2,62% | +2,81% | -1,35% | +6,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 80 | 45,00% | -0,17% | -0,30% | -2,92% | +2,81% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 46 | 34,78% | -4,54% | +1,76% | -3,81% | +6,54% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 84 | 54,76% | +1,72% | +0,92% | -3,86% | +5,75% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 11 | 36,36% | +2,02% | +2,17% | -2,50% | +9,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 78 | 50,00% | -0,99% | +0,15% | -4,25% | +5,04% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 44 | 27,27% | -6,50% | +3,07% | -4,35% | +8,81% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 82 | 58,54% | +1,94% | +1,61% | -4,53% | +7,68% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 11 | 45,45% | +0,78% | +0,88% | -3,00% | +9,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 76 | 43,42% | -1,46% | +0,66% | -4,99% | +6,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 44 | 29,55% | -7,10% | +3,40% | -5,16% | +10,81% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 79 | 55,70% | +1,68% | +2,23% | -5,10% | +9,73% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 73 | 43,84% | -2,08% | +0,97% | -5,64% | +8,31% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 43 | 39,53% | -5,45% | +4,51% | -5,57% | +13,12% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 76 | 64,47% | +3,35% | +3,72% | -5,75% | +12,99% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 11 | 45,45% | +2,03% | +5,60% | -4,35% | +14,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 70 | 45,71% | -1,78% | +1,76% | -6,36% | +10,51% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 42 | 42,86% | -7,44% | +5,67% | -5,73% | +16,02% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 70 | 58,57% | +4,53% | +8,09% | -5,59% | +19,19% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 11 | 63,64% | -0,04% | +4,84% | -5,47% | +18,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 64 | 54,69% | -2,39% | +6,13% | -6,26% | +16,39% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Classic technical | 38 | 47,37% | -7,21% | +9,03% | -5,94% | +22,34% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 65 | 69,23% | +7,05% | +11,42% | -5,60% | +25,97% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 9 | 88,89% | +12,44% | +19,48% | -5,48% | +30,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 59 | 57,63% | -2,49% | +10,00% | -6,35% | +23,84% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 31 | 3,23% | -22,01% | +21,52% | -5,10% | +38,53% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Famiglia statistica | 50 | 62,00% | +8,17% | +20,73% | -4,72% | +38,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 8 | 62,50% | +11,03% | +21,73% | -4,45% | +35,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 44 | 11,36% | -13,34% | +17,74% | -5,60% | +36,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 23 | 0,00% | -25,36% | +25,36% | -4,66% | +43,08% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 36 | 55,56% | +8,80% | +26,93% | -4,16% | +44,90% | PESO OK | 0,0 | MEDIA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 4 | 75,00% | +19,48% | +38,20% | -1,31% | +51,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 31 | 3,23% | -25,77% | +27,11% | -4,65% | +43,94% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 1g | BREVE | Classic technical | 58 | 44,83% | -0,03% | +0,45% | -0,53% | +1,39% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 83 | 54,22% | +0,46% | +0,18% | -0,69% | +1,02% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 81 | 45,68% | -0,11% | +0,18% | -0,75% | +1,00% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 58 | 48,28% | +0,18% | +0,59% | -0,66% | +1,66% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 82 | 50,00% | +0,75% | +0,56% | -0,81% | +1,47% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 80 | 43,75% | -0,12% | +0,38% | -0,78% | +1,48% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 58 | 46,55% | +0,10% | +0,60% | -2,28% | +3,11% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 81 | 53,09% | +1,38% | +1,02% | -2,26% | +3,55% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 79 | 43,04% | -0,50% | +0,61% | -2,29% | +3,12% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 57 | 49,12% | +0,14% | +0,81% | -3,23% | +4,42% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 79 | 55,70% | +2,29% | +1,89% | -3,19% | +5,62% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 77 | 44,16% | -0,92% | +1,49% | -3,24% | +5,07% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 57 | 43,86% | -0,12% | +0,46% | -4,03% | +5,07% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 77 | 63,64% | +3,48% | +2,96% | -3,71% | +7,36% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 75 | 38,67% | -1,83% | +1,99% | -3,80% | +6,46% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 54 | 46,30% | +0,13% | +0,86% | -4,44% | +6,09% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 74 | 68,92% | +5,59% | +4,97% | -4,00% | +9,49% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 72 | 43,06% | -1,94% | +3,32% | -4,17% | +8,12% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 51 | 45,10% | +0,50% | +2,22% | -5,04% | +7,85% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 71 | 77,46% | +8,66% | +7,95% | -4,30% | +13,30% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 69 | 40,58% | -2,80% | +5,47% | -4,65% | +11,18% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 45 | 60,00% | -1,01% | +10,15% | -4,85% | +15,58% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 66 | 81,82% | +14,43% | +14,48% | -4,34% | +20,23% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 63 | 52,38% | -5,03% | +12,00% | -4,72% | +17,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Classic technical | 42 | 54,76% | -4,29% | +22,25% | -4,70% | +27,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 61 | 90,16% | +19,36% | +21,90% | -4,40% | +28,89% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 60 | 45,00% | -7,68% | +20,40% | -4,74% | +26,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 45g | MEDIO | Classic technical | 32 | 34,38% | -19,31% | +31,63% | -4,07% | +41,70% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Famiglia statistica | 46 | 76,09% | +22,43% | +36,65% | -3,84% | +45,14% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +28,91% | +28,91% | -3,55% | +37,55% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 48 | 31,25% | -23,08% | +35,40% | -4,29% | +43,98% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 21 | 0,00% | -53,73% | +53,73% | -4,64% | +60,15% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 32 | 75,00% | +33,10% | +50,15% | -4,69% | +58,81% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +47,10% | +47,10% | -5,94% | +54,98% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 34 | 11,76% | -40,68% | +48,66% | -5,09% | +57,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 81 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 88 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 104 | 40,38% | -0,26% |
| BTC | BREVE | Famiglia statistica | 258 | 50,39% | +0,58% |
| BTC | BREVE | Microstruttura exchange | 27 | 37,04% | -0,30% |
| BTC | BREVE | Tecnico | 243 | 43,62% | -0,06% |
| BTC | SETTIMANALE | Classic technical | 100 | 35,00% | -3,42% |
| BTC | SETTIMANALE | Famiglia statistica | 242 | 56,20% | +2,40% |
| BTC | SETTIMANALE | Microstruttura exchange | 24 | 25,00% | -1,73% |
| BTC | SETTIMANALE | Tecnico | 227 | 44,05% | -0,71% |
| BTC | SWING | Classic technical | 58 | 34,48% | -4,52% |
| BTC | SWING | Famiglia statistica | 147 | 68,03% | +6,30% |
| BTC | SWING | Microstruttura exchange | 14 | 50,00% | +0,11% |
| BTC | SWING | Tecnico | 134 | 56,72% | +1,36% |
| BTC | MEDIO | Classic technical | 50 | 54,00% | -7,54% |
| BTC | MEDIO | Famiglia statistica | 153 | 96,73% | +19,07% |
| BTC | MEDIO | Microstruttura exchange | 9 | 100,00% | +9,68% |
| BTC | MEDIO | Tecnico | 138 | 55,07% | -1,79% |
| DOGE | BREVE | Classic technical | 147 | 38,78% | -1,27% |
| DOGE | BREVE | Famiglia statistica | 261 | 58,24% | +0,85% |
| DOGE | BREVE | Microstruttura exchange | 33 | 54,55% | +2,60% |
| DOGE | BREVE | Tecnico | 243 | 49,38% | +0,02% |
| DOGE | SETTIMANALE | Classic technical | 134 | 30,60% | -6,03% |
| DOGE | SETTIMANALE | Famiglia statistica | 245 | 56,33% | +1,78% |
| DOGE | SETTIMANALE | Microstruttura exchange | 33 | 45,45% | +1,16% |
| DOGE | SETTIMANALE | Tecnico | 227 | 45,81% | -1,50% |
| DOGE | SWING | Classic technical | 85 | 41,18% | -6,43% |
| DOGE | SWING | Famiglia statistica | 146 | 61,64% | +3,92% |
| DOGE | SWING | Microstruttura exchange | 22 | 54,55% | +0,99% |
| DOGE | SWING | Tecnico | 134 | 50,00% | -2,07% |
| DOGE | MEDIO | Classic technical | 92 | 20,65% | -16,74% |
| DOGE | MEDIO | Famiglia statistica | 151 | 63,58% | +7,84% |
| DOGE | MEDIO | Microstruttura exchange | 21 | 76,19% | +13,25% |
| DOGE | MEDIO | Tecnico | 134 | 29,85% | -11,44% |
| SOL | BREVE | Classic technical | 174 | 46,55% | +0,08% |
| SOL | BREVE | Famiglia statistica | 246 | 52,44% | +0,86% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 240 | 44,17% | -0,24% |
| SOL | SETTIMANALE | Classic technical | 168 | 46,43% | +0,05% |
| SOL | SETTIMANALE | Famiglia statistica | 230 | 62,61% | +3,75% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 224 | 41,96% | -1,55% |
| SOL | SWING | Classic technical | 96 | 52,08% | -0,21% |
| SOL | SWING | Famiglia statistica | 137 | 79,56% | +11,44% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 132 | 46,21% | -3,86% |
| SOL | MEDIO | Classic technical | 95 | 35,79% | -20,28% |
| SOL | MEDIO | Famiglia statistica | 139 | 82,01% | +23,54% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 12 | 100,00% | +28,96% |
| SOL | MEDIO | Tecnico | 142 | 32,39% | -20,79% |

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
