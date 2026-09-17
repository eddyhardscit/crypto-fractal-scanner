# Calibrazione pesi Global Confluence

Generato: 2026-09-17 05:33 UTC

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
| BTC | 69 | UTILE | 68 | 18 | 8 | 0 | Famiglia statistica | 1g | 52,94% | +0,29% | campione utile, valutare con prudenza |
| SOL | 69 | UTILE | 63 | 25 | 6 | 0 | Famiglia statistica | 1g | 53,97% | +0,23% | campione utile, valutare con prudenza |
| DOGE | 69 | UTILE | 67 | 26 | 7 | 0 | Famiglia statistica | 1g | 58,21% | +0,54% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 27 | 40,74% | +0,39% | +0,67% | +0,03% | +1,19% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 68 | 52,94% | +0,29% | +0,29% | -0,15% | +0,80% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 62 | 40,32% | +0,05% | +0,39% | -0,07% | +0,90% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 26 | 46,15% | +0,65% | +0,95% | +0,37% | +1,63% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 67 | 52,24% | +0,61% | +0,61% | +0,04% | +1,25% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 62 | 43,55% | +0,07% | +0,74% | +0,18% | +1,38% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 25 | 44,00% | +0,25% | +1,67% | -0,69% | +3,22% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 66 | 51,52% | +0,93% | +0,93% | -1,12% | +2,62% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 61 | 36,07% | -0,22% | +1,16% | -0,99% | +2,84% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 24 | 50,00% | -1,14% | +3,70% | -1,03% | +5,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 64 | 46,88% | +1,63% | +1,63% | -1,70% | +4,08% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 59 | 38,98% | -1,01% | +1,86% | -1,56% | +4,36% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 24 | 45,83% | -2,81% | +4,87% | -1,33% | +8,02% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 62 | 54,84% | +2,24% | +2,24% | -2,02% | +5,11% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 57 | 38,60% | -1,84% | +2,63% | -1,87% | +5,47% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 24 | 50,00% | -3,59% | +5,20% | -1,59% | +8,77% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 59 | 59,32% | +3,01% | +3,01% | -2,25% | +6,21% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 54 | 42,59% | -1,53% | +3,40% | -2,07% | +6,67% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 23 | 30,43% | -3,56% | +4,99% | -1,60% | +9,63% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 55 | 54,55% | +4,74% | +4,74% | -2,22% | +8,57% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 50 | 50,00% | +0,50% | +5,34% | -2,00% | +9,26% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 16 | 31,25% | -9,28% | +10,06% | -1,20% | +14,82% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 48 | 68,75% | +8,70% | +8,70% | -2,25% | +12,88% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 3 | 66,67% | -0,54% | -0,54% | -2,98% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 43 | 39,53% | -1,07% | +9,52% | -1,99% | +13,82% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 8 | 0,00% | -23,09% | +23,09% | -0,83% | +29,47% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 39 | 87,18% | +14,79% | +14,79% | -2,63% | +19,43% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 34 | 38,24% | -4,50% | +15,09% | -2,36% | +20,11% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 4 | 0,00% | -21,70% | +21,70% | -1,55% | +30,01% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 26 | 100,00% | +22,09% | +22,09% | -2,98% | +27,31% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 21 | 23,81% | -11,69% | +22,36% | -2,63% | +27,78% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 11 | 100,00% | +21,91% | +21,91% | -2,62% | +29,08% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 10 | 40,00% | -5,10% | +21,77% | -2,56% | +29,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 40 | 42,50% | -0,32% | +0,10% | -0,56% | +0,80% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 67 | 58,21% | +0,54% | +0,18% | -0,49% | +1,07% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 9 | 55,56% | +1,78% | +2,13% | +0,65% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 61 | 52,46% | +0,43% | +0,09% | -0,61% | +0,96% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 39 | 46,15% | -0,88% | +0,17% | -0,59% | +1,08% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 66 | 59,09% | +0,94% | +0,37% | -0,41% | +1,49% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,61% | +2,90% | +2,02% | +4,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 60 | 56,67% | +0,65% | -0,00% | -0,77% | +1,09% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 38 | 34,21% | -1,77% | +0,44% | -2,40% | +3,63% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 65 | 56,92% | +1,34% | +0,65% | -2,12% | +3,56% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,26% | +2,49% | -0,95% | +6,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 59 | 47,46% | +0,58% | -0,12% | -2,40% | +2,70% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 36 | 38,89% | -3,75% | +1,34% | -3,35% | +6,00% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 63 | 53,97% | +2,19% | +1,35% | -3,02% | +5,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 9 | 33,33% | +0,34% | +0,52% | -2,37% | +7,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 57 | 57,89% | +0,54% | +0,34% | -3,46% | +4,86% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 34 | 35,29% | -5,01% | +1,88% | -3,79% | +7,55% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 61 | 59,02% | +2,91% | +1,87% | -3,54% | +7,66% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 9 | 44,44% | -0,49% | -0,37% | -2,97% | +7,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 55 | 54,55% | +0,82% | +0,59% | -4,07% | +6,35% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 33 | 39,39% | -4,80% | +1,41% | -4,47% | +8,76% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 58 | 53,45% | +3,18% | +2,15% | -3,89% | +9,38% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 9 | 55,56% | -1,01% | -0,68% | -4,16% | +8,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 52 | 61,54% | +1,10% | +0,36% | -4,50% | +7,35% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 31 | 48,39% | -3,87% | +3,26% | -4,53% | +11,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 54 | 74,07% | +6,01% | +3,94% | -4,03% | +12,80% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 8 | 50,00% | +1,67% | +6,58% | -3,33% | +14,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 48 | 56,25% | +0,75% | +1,11% | -4,71% | +9,16% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 31 | 48,39% | -7,22% | +5,15% | -4,78% | +14,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 47 | 80,85% | +10,79% | +8,01% | -4,13% | +18,78% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 7 | 57,14% | -0,50% | +7,18% | -3,01% | +20,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 41 | 56,10% | -3,80% | +4,94% | -4,96% | +14,35% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 26 | 42,31% | -10,69% | +10,69% | -4,15% | +23,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 39 | 89,74% | +12,74% | +13,91% | -3,86% | +28,18% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,03% | +30,85% | -1,31% | +42,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 33 | 42,42% | -9,80% | +12,15% | -4,39% | +25,43% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 20 | 0,00% | -20,53% | +20,53% | -5,27% | +38,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 26 | 38,46% | -4,50% | +19,84% | -5,24% | +38,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 26 | 0,00% | -19,84% | +19,84% | -5,24% | +38,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Classic technical | 10 | 0,00% | -17,09% | +17,09% | -6,60% | +37,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 11 | 0,00% | -16,88% | +16,88% | -6,73% | +37,18% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 11 | 0,00% | -16,88% | +16,88% | -6,73% | +37,18% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 42 | 50,00% | +0,45% | +0,49% | -0,33% | +1,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 63 | 53,97% | +0,23% | +0,25% | -0,42% | +1,08% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 60 | 48,33% | +0,23% | +0,26% | -0,46% | +1,06% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 42 | 50,00% | +0,73% | +0,75% | -0,18% | +1,69% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 62 | 43,55% | +0,24% | +0,63% | -0,30% | +1,43% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 60 | 41,67% | +0,14% | +0,65% | -0,22% | +1,72% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 42 | 52,38% | +0,88% | +1,01% | -1,83% | +3,26% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 61 | 45,90% | +0,65% | +1,14% | -1,89% | +3,53% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 60 | 46,67% | -0,07% | +1,03% | -1,90% | +3,36% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 42 | 54,76% | +1,33% | +1,47% | -2,64% | +4,74% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 59 | 49,15% | +1,20% | +2,12% | -2,57% | +5,66% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 59 | 45,76% | -0,51% | +2,19% | -2,63% | +5,53% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 42 | 47,62% | +1,40% | +1,36% | -3,24% | +5,52% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 57 | 54,39% | +1,99% | +3,11% | -3,02% | +7,27% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 59 | 38,98% | -1,36% | +2,89% | -3,15% | +7,04% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 40 | 52,50% | +1,39% | +1,30% | -3,64% | +6,22% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 54 | 57,41% | +3,86% | +4,71% | -3,29% | +9,15% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 56 | 44,64% | -2,09% | +3,92% | -3,48% | +8,49% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 36 | 44,44% | +0,94% | +2,33% | -3,75% | +7,48% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 50 | 70,00% | +7,16% | +7,97% | -3,34% | +13,25% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 52 | 36,54% | -4,19% | +6,06% | -3,60% | +11,58% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 29 | 48,28% | -6,22% | +9,98% | -3,60% | +15,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 43 | 76,74% | +15,12% | +15,19% | -3,37% | +21,48% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 45 | 40,00% | -10,81% | +12,32% | -3,82% | +18,56% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 21 | 9,52% | -26,53% | +26,53% | -4,64% | +32,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 35 | 91,43% | +25,47% | +25,77% | -4,29% | +33,22% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +22,28% | +22,28% | -5,94% | +27,20% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 37 | 10,81% | -23,02% | +22,52% | -4,69% | +29,40% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 18 | 0,00% | -36,26% | +36,26% | -5,27% | +46,97% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 22 | 63,64% | +12,45% | +33,97% | -6,09% | +43,57% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 26 | 15,38% | -26,74% | +34,31% | -6,21% | +43,40% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Classic technical | 4 | 0,00% | -31,88% | +31,88% | -6,39% | +45,71% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 8 | 12,50% | -24,83% | +32,67% | -7,77% | +43,56% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 11 | 36,36% | -8,11% | +32,76% | -7,51% | +43,97% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 65 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 68 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 78 | 43,59% | +0,43% |
| BTC | BREVE | Famiglia statistica | 201 | 52,24% | +0,61% |
| BTC | BREVE | Microstruttura exchange | 15 | 40,00% | +0,30% |
| BTC | BREVE | Tecnico | 185 | 40,00% | -0,03% |
| BTC | SETTIMANALE | Classic technical | 72 | 48,61% | -2,51% |
| BTC | SETTIMANALE | Famiglia statistica | 185 | 53,51% | +2,27% |
| BTC | SETTIMANALE | Microstruttura exchange | 15 | 33,33% | -1,25% |
| BTC | SETTIMANALE | Tecnico | 170 | 40,00% | -1,45% |
| BTC | SWING | Classic technical | 39 | 30,77% | -5,90% |
| BTC | SWING | Famiglia statistica | 103 | 61,17% | +6,58% |
| BTC | SWING | Microstruttura exchange | 6 | 50,00% | -0,28% |
| BTC | SWING | Tecnico | 93 | 45,16% | -0,23% |
| BTC | MEDIO | Classic technical | 12 | 0,00% | -22,62% |
| BTC | MEDIO | Famiglia statistica | 76 | 93,42% | +18,32% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 65 | 33,85% | -6,91% |
| DOGE | BREVE | Classic technical | 117 | 41,03% | -0,98% |
| DOGE | BREVE | Famiglia statistica | 198 | 58,08% | +0,94% |
| DOGE | BREVE | Microstruttura exchange | 27 | 48,15% | +2,22% |
| DOGE | BREVE | Tecnico | 180 | 52,22% | +0,55% |
| DOGE | SETTIMANALE | Classic technical | 103 | 37,86% | -4,50% |
| DOGE | SETTIMANALE | Famiglia statistica | 182 | 55,49% | +2,75% |
| DOGE | SETTIMANALE | Microstruttura exchange | 27 | 44,44% | -0,39% |
| DOGE | SETTIMANALE | Tecnico | 164 | 57,93% | +0,81% |
| DOGE | SWING | Classic technical | 62 | 48,39% | -5,54% |
| DOGE | SWING | Famiglia statistica | 101 | 77,23% | +8,24% |
| DOGE | SWING | Microstruttura exchange | 15 | 53,33% | +0,66% |
| DOGE | SWING | Tecnico | 89 | 56,18% | -1,35% |
| DOGE | MEDIO | Classic technical | 56 | 19,64% | -15,35% |
| DOGE | MEDIO | Famiglia statistica | 76 | 59,21% | +2,55% |
| DOGE | MEDIO | Microstruttura exchange | 6 | 83,33% | +20,07% |
| DOGE | MEDIO | Tecnico | 70 | 20,00% | -14,64% |
| SOL | BREVE | Classic technical | 126 | 50,79% | +0,69% |
| SOL | BREVE | Famiglia statistica | 186 | 47,85% | +0,37% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 180 | 45,56% | +0,10% |
| SOL | SETTIMANALE | Classic technical | 124 | 51,61% | +1,37% |
| SOL | SETTIMANALE | Famiglia statistica | 170 | 53,53% | +2,31% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 174 | 43,10% | -1,31% |
| SOL | SWING | Classic technical | 65 | 46,15% | -2,26% |
| SOL | SWING | Famiglia statistica | 93 | 73,12% | +10,84% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 97 | 38,14% | -7,26% |
| SOL | MEDIO | Classic technical | 43 | 4,65% | -31,10% |
| SOL | MEDIO | Famiglia statistica | 65 | 72,31% | +14,87% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 3 | 100,00% | +25,70% |
| SOL | MEDIO | Tecnico | 74 | 16,22% | -22,11% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 5 | in attesa di controlli maturati |
| SOL | MEDIO | 1 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 2 | in attesa di controlli maturati |
| DOGE | MEDIO | 4 | in attesa di controlli maturati |

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
