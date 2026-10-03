# Calibrazione pesi Global Confluence

Generato: 2026-10-03 05:33 UTC

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
| BTC | 79 | UTILE | 77 | 21 | 15 | 0 | Famiglia statistica | 1g | 50,65% | +0,30% | campione utile, valutare con prudenza |
| SOL | 79 | UTILE | 72 | 29 | 14 | 0 | Famiglia statistica | 1g | 55,56% | +0,46% | campione utile, valutare con prudenza |
| DOGE | 79 | UTILE | 77 | 29 | 15 | 0 | Famiglia statistica | 1g | 57,14% | +0,50% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 30 | 36,67% | -0,01% | +0,64% | -0,21% | +1,14% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 77 | 50,65% | +0,30% | +0,29% | -0,23% | +0,81% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 8 | 37,50% | -0,49% | -0,49% | -1,07% | -0,05% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 71 | 42,25% | +0,02% | +0,31% | -0,17% | +0,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 29 | 41,38% | +0,02% | +1,20% | +0,19% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 76 | 52,63% | +0,66% | +0,66% | -0,09% | +1,36% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 7 | 28,57% | -0,04% | -0,04% | -0,90% | +1,02% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 70 | 44,29% | +0,07% | +0,66% | +0,01% | +1,36% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 29 | 37,93% | -0,51% | +1,95% | -0,85% | +3,41% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 76 | 51,32% | +0,91% | +1,02% | -1,17% | +2,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 70 | 37,14% | -0,13% | +1,08% | -1,08% | +2,74% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 29 | 41,38% | -2,25% | +4,06% | -1,22% | +6,21% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 75 | 46,67% | +1,74% | +1,89% | -1,75% | +4,21% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 7 | 14,29% | -1,43% | -1,43% | -2,57% | +1,68% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 68 | 42,65% | -0,67% | +1,82% | -1,68% | +4,18% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 29 | 37,93% | -4,00% | +5,44% | -1,49% | +8,41% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 73 | 57,53% | +2,67% | +2,69% | -2,07% | +5,40% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 7 | 28,57% | -1,74% | -1,74% | -3,24% | +1,77% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 66 | 43,94% | -1,10% | +2,77% | -2,01% | +5,44% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 29 | 41,38% | -4,39% | +5,56% | -1,70% | +9,12% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 71 | 64,79% | +3,63% | +3,63% | -2,39% | +6,64% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | -1,21% | -1,21% | -3,81% | +1,86% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 64 | 50,00% | -0,37% | +3,78% | -2,33% | +6,81% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 28 | 25,00% | -4,20% | +5,37% | -1,80% | +9,90% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 69 | 62,32% | +5,20% | +5,20% | -2,57% | +8,87% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 62 | 58,06% | +1,64% | +5,55% | -2,50% | +9,26% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 24 | 54,17% | -4,04% | +8,85% | -2,32% | +12,73% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 64 | 76,56% | +8,20% | +8,20% | -2,85% | +12,10% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 59 | 55,93% | +1,05% | +8,77% | -2,72% | +12,72% | PESO OK | 0,0 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 23 | 65,22% | -2,32% | +13,74% | -2,41% | +18,02% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 55 | 90,91% | +13,34% | +13,34% | -2,62% | +17,54% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 3 | 100,00% | +5,40% | +5,40% | -4,01% | +8,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 50 | 58,00% | +0,08% | +13,41% | -2,43% | +17,81% | PESO OK | 0,0 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 8 | 0,00% | -27,13% | +27,13% | -0,83% | +34,28% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 40 | 100,00% | +25,22% | +25,22% | -2,38% | +29,86% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 35 | 37,14% | -5,56% | +25,82% | -2,09% | +30,51% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 4 | 0,00% | -33,67% | +33,67% | -1,55% | +38,08% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 27 | 100,00% | +27,01% | +27,01% | -2,95% | +32,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 22 | 27,27% | -13,98% | +27,34% | -2,60% | +32,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 44 | 38,64% | -0,74% | +0,01% | -0,85% | +0,76% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 77 | 57,14% | +0,50% | +0,12% | -0,67% | +1,10% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 11 | 63,64% | +2,53% | +2,82% | +0,75% | +3,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 71 | 50,70% | +0,10% | +0,04% | -0,79% | +1,01% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 43 | 41,86% | -1,35% | +0,42% | -0,82% | +1,40% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 76 | 57,89% | +0,74% | +0,40% | -0,73% | +1,72% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 11 | 45,45% | +2,65% | +2,89% | +1,08% | +5,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 70 | 52,86% | +0,15% | +0,09% | -1,06% | +1,40% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 43 | 30,23% | -2,36% | +0,67% | -2,59% | +3,92% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 76 | 55,26% | +1,01% | +0,70% | -2,33% | +3,72% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 11 | 54,55% | +2,62% | +2,81% | -1,35% | +6,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 70 | 44,29% | -0,02% | +0,05% | -2,58% | +3,01% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 43 | 32,56% | -4,81% | +2,13% | -3,64% | +6,91% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 74 | 51,35% | +1,34% | +1,67% | -3,29% | +6,25% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 11 | 36,36% | +2,02% | +2,17% | -2,50% | +9,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 68 | 51,47% | -0,68% | +0,85% | -3,69% | +5,47% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 43 | 27,91% | -6,38% | +3,41% | -4,15% | +8,99% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 72 | 55,56% | +1,45% | +2,60% | -3,86% | +8,40% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 11 | 45,45% | +0,78% | +0,88% | -3,00% | +9,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 66 | 45,45% | -1,04% | +1,60% | -4,33% | +7,37% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 42 | 30,95% | -7,11% | +3,89% | -4,83% | +11,29% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 70 | 50,00% | +1,01% | +3,40% | -4,42% | +10,59% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 64 | 50,00% | -1,40% | +2,07% | -4,96% | +9,06% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 41 | 41,46% | -5,10% | +5,35% | -5,18% | +13,82% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 68 | 60,29% | +2,62% | +5,28% | -4,85% | +14,22% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 10 | 50,00% | +2,61% | +6,54% | -3,97% | +15,08% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 62 | 51,61% | -0,78% | +3,22% | -5,45% | +11,54% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 36 | 50,00% | -6,59% | +5,48% | -5,60% | +14,92% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 63 | 61,90% | +5,46% | +8,56% | -5,30% | +19,08% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 9 | 66,67% | +0,57% | +6,54% | -4,75% | +18,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 57 | 61,40% | -1,12% | +6,41% | -6,03% | +15,93% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 31 | 48,39% | -8,72% | +10,82% | -5,10% | +22,58% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 54 | 77,78% | +8,86% | +13,37% | -4,74% | +26,95% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 8 | 87,50% | +13,45% | +21,36% | -4,45% | +31,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 48 | 60,42% | -3,22% | +11,87% | -5,56% | +24,46% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 27 | 0,00% | -24,99% | +24,99% | -3,76% | +41,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 40 | 60,00% | +9,36% | +25,18% | -3,60% | +42,47% | PESO OK | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,91% | +37,31% | -1,31% | +47,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 33 | 6,06% | -18,67% | +22,77% | -4,39% | +40,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 20 | 0,00% | -24,92% | +24,92% | -5,27% | +41,80% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 27 | 40,74% | +2,52% | +26,70% | -5,14% | +42,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 27 | 0,00% | -26,70% | +26,70% | -5,14% | +42,92% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 52 | 46,15% | +0,04% | +0,58% | -0,46% | +1,51% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 72 | 55,56% | +0,46% | +0,36% | -0,48% | +1,22% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 70 | 45,71% | -0,04% | +0,36% | -0,54% | +1,20% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 51 | 50,98% | +0,41% | +0,89% | -0,44% | +1,98% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 71 | 47,89% | +0,69% | +0,96% | -0,45% | +1,91% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 69 | 43,48% | -0,01% | +0,77% | -0,40% | +1,93% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 51 | 50,98% | +0,58% | +1,15% | -1,87% | +3,43% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 71 | 50,70% | +1,22% | +1,57% | -1,90% | +3,95% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 69 | 46,38% | -0,16% | +1,13% | -1,92% | +3,47% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 49 | 53,06% | +0,85% | +1,63% | -2,64% | +4,89% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 69 | 53,62% | +2,08% | +2,79% | -2,63% | +6,26% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 67 | 46,27% | -0,50% | +2,36% | -2,67% | +5,65% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 47 | 46,81% | +0,91% | +1,62% | -3,19% | +5,75% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 68 | 61,76% | +3,19% | +4,10% | -3,06% | +8,12% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 65 | 40,00% | -1,34% | +3,06% | -3,16% | +7,17% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
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
| SOL | 21g | SWING | Famiglia statistica | 59 | 83,05% | +14,81% | +14,86% | -4,27% | +20,33% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 59 | 54,24% | -5,14% | +12,51% | -4,59% | +18,02% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 36 | 47,22% | -7,16% | +23,80% | -4,22% | +28,97% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 50 | 88,00% | +21,25% | +24,35% | -3,97% | +30,57% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 52 | 36,54% | -10,62% | +21,78% | -4,38% | +27,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 21 | 0,00% | -38,81% | +38,81% | -4,64% | +48,52% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 36 | 77,78% | +29,37% | +42,52% | -3,91% | +50,22% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,56% | +44,56% | -5,94% | +49,24% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 37 | 10,81% | -35,27% | +40,59% | -4,69% | +48,53% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 19 | 0,00% | -52,61% | +52,61% | -5,09% | +59,09% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 23 | 65,22% | +25,29% | +49,01% | -5,91% | +55,84% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +41,93% | +41,93% | -9,62% | +45,82% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 27 | 14,81% | -37,16% | +47,20% | -6,05% | +54,42% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 74 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 77 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 88 | 38,64% | -0,17% |
| BTC | BREVE | Famiglia statistica | 229 | 51,53% | +0,62% |
| BTC | BREVE | Microstruttura exchange | 22 | 31,82% | -0,31% |
| BTC | BREVE | Tecnico | 211 | 41,23% | -0,01% |
| BTC | SETTIMANALE | Classic technical | 87 | 40,23% | -3,54% |
| BTC | SETTIMANALE | Famiglia statistica | 219 | 56,16% | +2,66% |
| BTC | SETTIMANALE | Microstruttura exchange | 21 | 28,57% | -1,46% |
| BTC | SETTIMANALE | Tecnico | 198 | 45,45% | -0,72% |
| BTC | SWING | Classic technical | 52 | 38,46% | -4,13% |
| BTC | SWING | Famiglia statistica | 133 | 69,17% | +6,65% |
| BTC | SWING | Microstruttura exchange | 10 | 60,00% | +0,93% |
| BTC | SWING | Tecnico | 121 | 57,02% | +1,35% |
| BTC | MEDIO | Classic technical | 35 | 42,86% | -11,57% |
| BTC | MEDIO | Famiglia statistica | 122 | 95,90% | +20,26% |
| BTC | MEDIO | Microstruttura exchange | 5 | 100,00% | +12,53% |
| BTC | MEDIO | Tecnico | 107 | 44,86% | -4,65% |
| DOGE | BREVE | Classic technical | 130 | 36,92% | -1,48% |
| DOGE | BREVE | Famiglia statistica | 229 | 56,77% | +0,75% |
| DOGE | BREVE | Microstruttura exchange | 33 | 54,55% | +2,60% |
| DOGE | BREVE | Tecnico | 211 | 49,29% | +0,08% |
| DOGE | SETTIMANALE | Classic technical | 128 | 30,47% | -6,09% |
| DOGE | SETTIMANALE | Famiglia statistica | 216 | 52,31% | +1,27% |
| DOGE | SETTIMANALE | Microstruttura exchange | 33 | 45,45% | +1,16% |
| DOGE | SETTIMANALE | Tecnico | 198 | 48,99% | -1,03% |
| DOGE | SWING | Classic technical | 77 | 45,45% | -5,80% |
| DOGE | SWING | Famiglia statistica | 131 | 61,07% | +3,99% |
| DOGE | SWING | Microstruttura exchange | 19 | 57,89% | +1,64% |
| DOGE | SWING | Tecnico | 119 | 56,30% | -0,94% |
| DOGE | MEDIO | Classic technical | 78 | 19,23% | -18,51% |
| DOGE | MEDIO | Famiglia statistica | 121 | 63,64% | +7,61% |
| DOGE | MEDIO | Microstruttura exchange | 14 | 85,71% | +18,65% |
| DOGE | MEDIO | Tecnico | 108 | 28,70% | -13,81% |
| SOL | BREVE | Classic technical | 154 | 49,35% | +0,34% |
| SOL | BREVE | Famiglia statistica | 214 | 51,40% | +0,79% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 208 | 45,19% | -0,07% |
| SOL | SETTIMANALE | Classic technical | 141 | 51,77% | +1,00% |
| SOL | SETTIMANALE | Famiglia statistica | 203 | 60,10% | +3,59% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 195 | 45,13% | -1,09% |
| SOL | SWING | Classic technical | 85 | 57,65% | +0,70% |
| SOL | SWING | Famiglia statistica | 123 | 79,67% | +11,70% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 120 | 49,17% | -3,74% |
| SOL | MEDIO | Classic technical | 76 | 22,37% | -27,27% |
| SOL | MEDIO | Famiglia statistica | 109 | 79,82% | +24,78% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 8 | 100,00% | +29,97% |
| SOL | MEDIO | Tecnico | 116 | 23,28% | -24,66% |

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
