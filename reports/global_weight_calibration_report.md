# Calibrazione pesi Global Confluence

Generato: 2026-10-04 05:33 UTC

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
| BTC | 80 | UTILE | 78 | 22 | 16 | 0 | Famiglia statistica | 1g | 50,00% | +0,29% | campione utile, valutare con prudenza |
| SOL | 80 | UTILE | 73 | 29 | 16 | 0 | Famiglia statistica | 1g | 54,79% | +0,44% | campione utile, valutare con prudenza |
| DOGE | 80 | UTILE | 78 | 29 | 15 | 0 | Famiglia statistica | 1g | 57,69% | +0,50% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 31 | 38,71% | -0,01% | +0,62% | -0,20% | +1,12% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 78 | 50,00% | +0,29% | +0,29% | -0,22% | +0,80% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 8 | 37,50% | -0,49% | -0,49% | -1,07% | -0,05% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 72 | 43,06% | +0,02% | +0,31% | -0,17% | +0,82% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 30 | 40,00% | -0,05% | +1,10% | +0,11% | +1,77% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 77 | 51,95% | +0,63% | +0,63% | -0,11% | +1,32% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 8 | 25,00% | -0,28% | -0,28% | -1,06% | +0,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 71 | 43,66% | +0,04% | +0,62% | -0,02% | +1,31% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 29 | 37,93% | -0,51% | +1,95% | -0,85% | +3,41% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 76 | 51,32% | +0,91% | +1,02% | -1,17% | +2,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 70 | 37,14% | -0,13% | +1,08% | -1,08% | +2,74% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 29 | 41,38% | -2,25% | +4,06% | -1,22% | +6,21% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 76 | 46,05% | +1,69% | +1,89% | -1,73% | +4,22% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 7 | 14,29% | -1,43% | -1,43% | -2,57% | +1,68% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 69 | 43,48% | -0,63% | +1,82% | -1,66% | +4,19% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 29 | 37,93% | -4,00% | +5,44% | -1,49% | +8,41% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 74 | 56,76% | +2,62% | +2,66% | -2,07% | +5,37% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 7 | 28,57% | -1,74% | -1,74% | -3,24% | +1,77% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 67 | 44,78% | -1,07% | +2,73% | -2,01% | +5,41% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 29 | 41,38% | -4,39% | +5,56% | -1,70% | +9,12% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 71 | 64,79% | +3,63% | +3,63% | -2,39% | +6,64% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | -1,21% | -1,21% | -3,81% | +1,86% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 64 | 50,00% | -0,37% | +3,78% | -2,33% | +6,81% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 28 | 25,00% | -4,20% | +5,37% | -1,80% | +9,90% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 69 | 62,32% | +5,20% | +5,20% | -2,57% | +8,87% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 62 | 58,06% | +1,64% | +5,55% | -2,50% | +9,26% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 24 | 54,17% | -4,04% | +8,85% | -2,32% | +12,73% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 65 | 76,92% | +8,23% | +8,23% | -2,86% | +12,12% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 60 | 56,67% | +1,19% | +8,78% | -2,72% | +12,72% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 24 | 66,67% | -2,02% | +13,37% | -2,62% | +17,60% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 56 | 91,07% | +13,19% | +13,19% | -2,71% | +17,37% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 4 | 100,00% | +5,25% | +5,25% | -4,87% | +8,45% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 51 | 58,82% | +0,18% | +13,24% | -2,53% | +17,62% | PESO OK | 0,0 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 9 | 11,11% | -21,68% | +26,56% | -0,19% | +33,31% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 41 | 100,00% | +25,14% | +25,14% | -2,20% | +29,76% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 36 | 38,89% | -4,79% | +25,71% | -1,89% | +30,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 4 | 0,00% | -33,67% | +33,67% | -1,55% | +38,08% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 28 | 100,00% | +27,19% | +27,19% | -2,94% | +32,28% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 23 | 26,09% | -14,77% | +27,54% | -2,61% | +32,86% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 44 | 38,64% | -0,74% | +0,01% | -0,85% | +0,76% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 78 | 57,69% | +0,50% | +0,12% | -0,67% | +1,08% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 11 | 63,64% | +2,53% | +2,82% | +0,75% | +3,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 72 | 50,00% | +0,09% | +0,03% | -0,78% | +0,99% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 44 | 40,91% | -1,41% | +0,32% | -0,90% | +1,29% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 77 | 58,44% | +0,78% | +0,35% | -0,77% | +1,65% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 11 | 45,45% | +2,65% | +2,89% | +1,08% | +5,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 71 | 52,11% | +0,09% | +0,03% | -1,10% | +1,33% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 43 | 30,23% | -2,36% | +0,67% | -2,59% | +3,92% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 76 | 55,26% | +1,01% | +0,70% | -2,33% | +3,72% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 11 | 54,55% | +2,62% | +2,81% | -1,35% | +6,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 70 | 44,29% | -0,02% | +0,05% | -2,58% | +3,01% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 43 | 32,56% | -4,81% | +2,13% | -3,64% | +6,91% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 75 | 52,00% | +1,33% | +1,64% | -3,29% | +6,23% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 11 | 36,36% | +2,02% | +2,17% | -2,50% | +9,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 69 | 50,72% | -0,67% | +0,83% | -3,68% | +5,46% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 43 | 27,91% | -6,38% | +3,41% | -4,15% | +8,99% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 73 | 56,16% | +1,47% | +2,52% | -3,88% | +8,31% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 11 | 45,45% | +0,78% | +0,88% | -3,00% | +9,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 67 | 44,78% | -1,07% | +1,52% | -4,35% | +7,29% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 42 | 30,95% | -7,11% | +3,89% | -4,83% | +11,29% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 70 | 50,00% | +1,01% | +3,40% | -4,42% | +10,59% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 64 | 50,00% | -1,40% | +2,07% | -4,96% | +9,06% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 41 | 41,46% | -5,10% | +5,35% | -5,18% | +13,82% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 68 | 60,29% | +2,62% | +5,28% | -4,85% | +14,22% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 10 | 50,00% | +2,61% | +6,54% | -3,97% | +15,08% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 62 | 51,61% | -0,78% | +3,22% | -5,45% | +11,54% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 37 | 48,65% | -6,66% | +5,58% | -5,65% | +15,17% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 64 | 60,94% | +5,23% | +8,57% | -5,34% | +19,16% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 9 | 66,67% | +0,57% | +6,54% | -4,75% | +18,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 58 | 60,34% | -1,26% | +6,46% | -6,05% | +16,07% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 31 | 48,39% | -8,72% | +10,82% | -5,10% | +22,58% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 55 | 76,36% | +8,58% | +13,25% | -4,84% | +26,85% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 8 | 87,50% | +13,45% | +21,36% | -4,45% | +31,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 49 | 61,22% | -3,02% | +11,76% | -5,65% | +24,39% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 27 | 0,00% | -24,99% | +24,99% | -3,76% | +41,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 41 | 60,98% | +9,73% | +25,16% | -3,38% | +42,44% | PESO OK | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 5 | 80,00% | +17,62% | +34,73% | -0,01% | +46,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 34 | 8,82% | -17,40% | +22,82% | -4,11% | +40,98% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 20 | 0,00% | -24,92% | +24,92% | -5,27% | +41,80% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 28 | 42,86% | +3,60% | +26,91% | -5,04% | +43,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 28 | 0,00% | -26,91% | +26,91% | -5,04% | +43,20% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 53 | 47,17% | +0,06% | +0,59% | -0,45% | +1,51% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 73 | 54,79% | +0,44% | +0,37% | -0,47% | +1,22% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 71 | 46,48% | -0,03% | +0,36% | -0,53% | +1,20% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 52 | 50,00% | +0,39% | +0,85% | -0,46% | +1,93% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 72 | 48,61% | +0,69% | +0,94% | -0,47% | +1,87% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 70 | 42,86% | -0,03% | +0,74% | -0,43% | +1,89% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 51 | 50,98% | +0,58% | +1,15% | -1,87% | +3,43% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 71 | 50,70% | +1,22% | +1,57% | -1,90% | +3,95% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 69 | 46,38% | -0,16% | +1,13% | -1,92% | +3,47% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 50 | 54,00% | +0,89% | +1,65% | -2,60% | +4,89% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 70 | 52,86% | +2,01% | +2,79% | -2,60% | +6,25% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 68 | 47,06% | -0,46% | +2,36% | -2,64% | +5,64% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 48 | 47,92% | +0,89% | +1,59% | -3,19% | +5,68% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 69 | 60,87% | +3,15% | +4,05% | -3,06% | +8,03% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 66 | 40,91% | -1,32% | +3,01% | -3,16% | +7,09% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 45 | 55,56% | +1,24% | +2,11% | -3,69% | +6,77% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 66 | 65,15% | +5,58% | +6,27% | -3,42% | +10,34% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 63 | 49,21% | -1,44% | +4,57% | -3,60% | +8,90% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 43 | 51,16% | +1,68% | +3,73% | -4,16% | +8,54% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 64 | 76,56% | +8,84% | +9,47% | -3,73% | +14,30% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 61 | 44,26% | -2,39% | +6,96% | -3,98% | +12,10% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 42 | 64,29% | -0,31% | +10,88% | -4,69% | +15,79% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 60 | 83,33% | +14,87% | +14,92% | -4,29% | +20,36% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 60 | 55,00% | -4,74% | +12,61% | -4,60% | +18,09% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Classic technical | 37 | 48,65% | -6,52% | +23,60% | -4,30% | +28,74% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 51 | 88,24% | +21,16% | +24,19% | -4,03% | +30,37% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 53 | 37,74% | -10,11% | +21,68% | -4,43% | +27,55% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 22 | 4,55% | -35,13% | +38,96% | -4,29% | +48,44% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 36 | 77,78% | +29,37% | +42,52% | -3,91% | +50,22% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,56% | +44,56% | -5,94% | +49,24% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 38 | 13,16% | -33,24% | +40,64% | -4,48% | +48,49% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 20 | 0,00% | -53,15% | +53,15% | -4,94% | +59,57% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 24 | 66,67% | +26,88% | +49,61% | -5,75% | +56,37% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +41,93% | +41,93% | -9,62% | +45,82% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 28 | 14,29% | -38,09% | +47,78% | -5,91% | +54,93% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 75 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 78 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 90 | 38,89% | -0,18% |
| BTC | BREVE | Famiglia statistica | 231 | 51,08% | +0,61% |
| BTC | BREVE | Microstruttura exchange | 23 | 30,43% | -0,39% |
| BTC | BREVE | Tecnico | 213 | 41,31% | -0,02% |
| BTC | SETTIMANALE | Classic technical | 87 | 40,23% | -3,54% |
| BTC | SETTIMANALE | Famiglia statistica | 221 | 55,66% | +2,63% |
| BTC | SETTIMANALE | Microstruttura exchange | 21 | 28,57% | -1,46% |
| BTC | SETTIMANALE | Tecnico | 200 | 46,00% | -0,70% |
| BTC | SWING | Classic technical | 52 | 38,46% | -4,13% |
| BTC | SWING | Famiglia statistica | 134 | 69,40% | +6,67% |
| BTC | SWING | Microstruttura exchange | 10 | 60,00% | +0,93% |
| BTC | SWING | Tecnico | 122 | 57,38% | +1,42% |
| BTC | MEDIO | Classic technical | 37 | 45,95% | -10,23% |
| BTC | MEDIO | Famiglia statistica | 125 | 96,00% | +20,24% |
| BTC | MEDIO | Microstruttura exchange | 6 | 100,00% | +11,24% |
| BTC | MEDIO | Tecnico | 110 | 45,45% | -4,57% |
| DOGE | BREVE | Classic technical | 131 | 36,64% | -1,50% |
| DOGE | BREVE | Famiglia statistica | 231 | 57,14% | +0,76% |
| DOGE | BREVE | Microstruttura exchange | 33 | 54,55% | +2,60% |
| DOGE | BREVE | Tecnico | 213 | 48,83% | +0,05% |
| DOGE | SETTIMANALE | Classic technical | 128 | 30,47% | -6,09% |
| DOGE | SETTIMANALE | Famiglia statistica | 218 | 52,75% | +1,28% |
| DOGE | SETTIMANALE | Microstruttura exchange | 33 | 45,45% | +1,16% |
| DOGE | SETTIMANALE | Tecnico | 200 | 48,50% | -1,04% |
| DOGE | SWING | Classic technical | 78 | 44,87% | -5,84% |
| DOGE | SWING | Famiglia statistica | 132 | 60,61% | +3,89% |
| DOGE | SWING | Microstruttura exchange | 19 | 57,89% | +1,64% |
| DOGE | SWING | Tecnico | 120 | 55,83% | -1,01% |
| DOGE | MEDIO | Classic technical | 78 | 19,23% | -18,51% |
| DOGE | MEDIO | Famiglia statistica | 124 | 63,71% | +7,84% |
| DOGE | MEDIO | Microstruttura exchange | 15 | 86,67% | +19,04% |
| DOGE | MEDIO | Tecnico | 111 | 29,73% | -13,45% |
| SOL | BREVE | Classic technical | 156 | 49,36% | +0,34% |
| SOL | BREVE | Famiglia statistica | 216 | 51,39% | +0,78% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 210 | 45,24% | -0,07% |
| SOL | SETTIMANALE | Classic technical | 143 | 52,45% | +1,00% |
| SOL | SETTIMANALE | Famiglia statistica | 205 | 59,51% | +3,54% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 197 | 45,69% | -1,06% |
| SOL | SWING | Classic technical | 85 | 57,65% | +0,70% |
| SOL | SWING | Famiglia statistica | 124 | 79,84% | +11,76% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 121 | 49,59% | -3,56% |
| SOL | MEDIO | Classic technical | 79 | 24,05% | -26,29% |
| SOL | MEDIO | Famiglia statistica | 111 | 80,18% | +25,06% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 8 | 100,00% | +29,97% |
| SOL | MEDIO | Tecnico | 119 | 24,37% | -24,08% |

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
