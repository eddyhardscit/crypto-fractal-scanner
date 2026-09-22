# Calibrazione pesi Global Confluence

Generato: 2026-09-22 05:33 UTC

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
| BTC | 70 | UTILE | 69 | 19 | 12 | 0 | Famiglia statistica | 3g | 53,62% | +1,15% | campione utile, valutare con prudenza |
| SOL | 70 | UTILE | 64 | 27 | 10 | 0 | Famiglia statistica | 1g | 54,69% | +0,44% | campione utile, valutare con prudenza |
| DOGE | 70 | UTILE | 68 | 28 | 11 | 0 | Famiglia statistica | 2g | 57,35% | +0,66% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 28 | 39,29% | +0,16% | +0,86% | +0,02% | +1,38% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 69 | 53,62% | +0,38% | +0,38% | -0,15% | +0,89% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 62 | 40,32% | +0,05% | +0,39% | -0,07% | +0,90% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 28 | 42,86% | +0,13% | +1,35% | +0,35% | +2,03% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 69 | 53,62% | +0,78% | +0,78% | +0,04% | +1,43% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 62 | 43,55% | +0,07% | +0,74% | +0,18% | +1,38% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 28 | 39,29% | -0,42% | +2,14% | -0,72% | +3,60% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 69 | 53,62% | +1,15% | +1,15% | -1,12% | +2,80% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 62 | 37,10% | -0,14% | +1,22% | -1,02% | +2,87% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 28 | 42,86% | -2,17% | +4,36% | -1,11% | +6,49% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 69 | 50,72% | +2,06% | +2,06% | -1,72% | +4,43% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 62 | 41,94% | -0,73% | +2,00% | -1,64% | +4,42% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 26 | 42,31% | -3,35% | +5,25% | -1,48% | +8,31% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 67 | 58,21% | +2,59% | +2,59% | -2,10% | +5,35% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 62 | 43,55% | -1,13% | +2,98% | -1,96% | +5,69% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 24 | 50,00% | -3,59% | +5,20% | -1,59% | +8,77% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 64 | 62,50% | +3,24% | +3,24% | -2,39% | +6,28% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 59 | 47,46% | -0,89% | +3,61% | -2,23% | +6,71% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 24 | 29,17% | -3,41% | +4,78% | -1,84% | +9,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 60 | 56,67% | +4,65% | +4,65% | -2,55% | +8,26% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 55 | 52,73% | +0,78% | +5,19% | -2,37% | +8,86% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 21 | 47,62% | -5,79% | +8,94% | -1,99% | +12,96% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 53 | 71,70% | +8,38% | +8,38% | -2,46% | +12,33% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 3 | 66,67% | -0,54% | -0,54% | -2,98% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 48 | 45,83% | -0,40% | +9,09% | -2,25% | +13,11% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 12 | 33,33% | -11,49% | +19,29% | -0,54% | +24,11% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 44 | 88,64% | +14,76% | +14,76% | -2,16% | +19,08% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +5,87% | +5,87% | -2,41% | +8,88% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 39 | 46,15% | -2,06% | +15,02% | -1,87% | +19,63% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 4 | 0,00% | -21,70% | +21,70% | -1,55% | +30,01% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 31 | 100,00% | +23,11% | +23,11% | -2,98% | +27,81% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 26 | 34,62% | -6,01% | +23,52% | -2,70% | +28,28% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 16 | 100,00% | +23,38% | +23,38% | -3,28% | +28,93% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 13 | 30,77% | -10,57% | +23,40% | -2,94% | +29,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 41 | 41,46% | -0,51% | +0,29% | -0,53% | +1,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 68 | 57,35% | +0,41% | +0,30% | -0,48% | +1,19% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 10 | 60,00% | +2,42% | +2,73% | +0,65% | +3,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 62 | 51,61% | +0,29% | +0,22% | -0,59% | +1,10% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 41 | 43,90% | -1,27% | +0,59% | -0,53% | +1,59% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 68 | 57,35% | +0,66% | +0,62% | -0,38% | +1,78% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 10 | 50,00% | +3,20% | +3,46% | +1,88% | +5,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 62 | 54,84% | +0,35% | +0,28% | -0,72% | +1,43% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 41 | 31,71% | -2,21% | +0,97% | -2,33% | +4,17% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 68 | 54,41% | +0,95% | +0,96% | -2,09% | +3,89% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 10 | 50,00% | +2,83% | +3,04% | -0,79% | +6,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 62 | 45,16% | +0,18% | +0,26% | -2,35% | +3,10% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 41 | 34,15% | -4,70% | +2,58% | -3,39% | +7,30% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 68 | 50,00% | +1,18% | +2,10% | -3,07% | +6,62% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 10 | 40,00% | +2,50% | +2,66% | -2,06% | +9,50% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 62 | 53,23% | -0,43% | +1,24% | -3,48% | +5,81% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 39 | 30,77% | -5,59% | +2,86% | -4,15% | +8,43% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 66 | 54,55% | +1,97% | +2,45% | -3,77% | +8,18% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 9 | 44,44% | -0,49% | -0,37% | -2,97% | +7,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 60 | 50,00% | -0,04% | +1,33% | -4,29% | +7,03% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 36 | 36,11% | -5,43% | +2,16% | -4,83% | +9,44% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 63 | 52,38% | +2,45% | +2,46% | -4,34% | +9,55% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 9 | 55,56% | -1,01% | -0,68% | -4,16% | +8,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 57 | 56,14% | +0,27% | +0,86% | -4,95% | +7,71% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 34 | 50,00% | -3,09% | +3,40% | -5,30% | +11,12% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 59 | 69,49% | +5,20% | +3,91% | -4,68% | +12,55% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 9 | 44,44% | +1,04% | +5,41% | -4,48% | +13,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 53 | 58,49% | +1,01% | +1,34% | -5,36% | +9,23% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 31 | 48,39% | -7,22% | +5,15% | -4,78% | +14,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 52 | 75,00% | +8,93% | +8,06% | -4,46% | +18,53% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 8 | 62,50% | -0,06% | +6,66% | -3,62% | +19,12% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 46 | 58,70% | -2,46% | +5,33% | -5,24% | +14,56% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 29 | 44,83% | -9,81% | +11,07% | -4,41% | +23,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 44 | 90,91% | +12,80% | +13,84% | -3,87% | +27,94% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 6 | 83,33% | +14,50% | +25,05% | -2,20% | +36,41% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 37 | 48,65% | -7,62% | +11,96% | -4,63% | +25,04% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 21 | 0,00% | -21,59% | +21,59% | -5,03% | +39,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 31 | 48,39% | +1,33% | +21,74% | -4,66% | +40,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 3 | 66,67% | +5,85% | +34,37% | -1,27% | +46,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 30 | 0,00% | -21,64% | +21,64% | -4,76% | +40,02% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 15 | 0,00% | -20,77% | +20,77% | -6,17% | +38,93% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 16 | 0,00% | -20,40% | +20,40% | -6,29% | +38,70% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +42,81% | +42,81% | -1,52% | +51,95% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 16 | 0,00% | -20,40% | +20,40% | -6,29% | +38,70% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 43 | 48,84% | +0,13% | +0,79% | -0,29% | +1,70% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 64 | 54,69% | +0,44% | +0,45% | -0,39% | +1,30% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 61 | 47,54% | +0,01% | +0,47% | -0,43% | +1,28% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 43 | 48,84% | +0,44% | +1,00% | -0,14% | +2,00% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 64 | 45,31% | +0,67% | +1,04% | -0,24% | +1,89% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 61 | 40,98% | -0,05% | +0,83% | -0,19% | +1,93% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 43 | 51,16% | +0,59% | +1,26% | -1,75% | +3,53% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 64 | 48,44% | +1,21% | +1,67% | -1,82% | +4,07% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 61 | 45,90% | -0,26% | +1,20% | -1,84% | +3,54% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 43 | 53,49% | +0,92% | +1,81% | -2,55% | +5,09% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 64 | 53,12% | +2,13% | +2,98% | -2,56% | +6,48% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 61 | 45,90% | -0,59% | +2,55% | -2,61% | +5,87% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 42 | 47,62% | +1,40% | +1,36% | -3,24% | +5,52% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 62 | 58,06% | +2,81% | +3,83% | -3,15% | +7,90% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 60 | 40,00% | -1,18% | +3,00% | -3,19% | +7,12% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 42 | 54,76% | +1,69% | +1,60% | -3,81% | +6,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 59 | 61,02% | +4,46% | +5,23% | -3,50% | +9,54% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 59 | 47,46% | -1,57% | +4,13% | -3,64% | +8,59% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 41 | 51,22% | +1,89% | +3,10% | -4,21% | +7,98% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 55 | 72,73% | +7,30% | +8,04% | -3,72% | +13,09% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 57 | 42,11% | -3,06% | +6,29% | -3,95% | +11,58% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Classic technical | 34 | 55,88% | -4,07% | +9,75% | -4,22% | +15,11% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 48 | 79,17% | +14,42% | +14,48% | -3,84% | +20,42% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 50 | 46,00% | -8,89% | +11,93% | -4,23% | +17,83% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 25 | 24,00% | -18,17% | +26,40% | -3,75% | +32,35% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 39 | 84,62% | +22,20% | +26,17% | -3,60% | +33,19% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 3 | 100,00% | +22,86% | +22,86% | -3,34% | +27,23% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 41 | 19,51% | -18,27% | +22,83% | -4,14% | +29,40% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 21 | 0,00% | -38,81% | +38,81% | -4,64% | +48,52% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 27 | 70,37% | +20,04% | +37,58% | -5,16% | +46,14% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 31 | 12,90% | -31,05% | +37,40% | -5,38% | +45,67% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 8 | 0,00% | -40,13% | +40,13% | -7,09% | +48,95% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 12 | 33,33% | -8,08% | +37,39% | -7,99% | +46,09% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +41,93% | +41,93% | -9,62% | +45,82% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 16 | 25,00% | -20,29% | +37,24% | -7,71% | +46,14% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 66 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 69 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 84 | 40,48% | -0,04% |
| BTC | BREVE | Famiglia statistica | 207 | 53,62% | +0,77% |
| BTC | BREVE | Microstruttura exchange | 15 | 40,00% | +0,30% |
| BTC | BREVE | Tecnico | 186 | 40,32% | -0,00% |
| BTC | SETTIMANALE | Classic technical | 78 | 44,87% | -3,00% |
| BTC | SETTIMANALE | Famiglia statistica | 200 | 57,00% | +2,62% |
| BTC | SETTIMANALE | Microstruttura exchange | 15 | 33,33% | -1,25% |
| BTC | SETTIMANALE | Tecnico | 183 | 44,26% | -0,92% |
| BTC | SWING | Classic technical | 45 | 37,78% | -4,52% |
| BTC | SWING | Famiglia statistica | 113 | 63,72% | +6,40% |
| BTC | SWING | Microstruttura exchange | 8 | 50,00% | -0,03% |
| BTC | SWING | Tecnico | 103 | 49,51% | +0,23% |
| BTC | MEDIO | Classic technical | 16 | 25,00% | -14,04% |
| BTC | MEDIO | Famiglia statistica | 91 | 94,51% | +19,12% |
| BTC | MEDIO | Microstruttura exchange | 4 | 100,00% | +14,55% |
| BTC | MEDIO | Tecnico | 78 | 39,74% | -4,80% |
| DOGE | BREVE | Classic technical | 123 | 39,02% | -1,33% |
| DOGE | BREVE | Famiglia statistica | 204 | 56,37% | +0,67% |
| DOGE | BREVE | Microstruttura exchange | 30 | 53,33% | +2,81% |
| DOGE | BREVE | Tecnico | 186 | 50,54% | +0,27% |
| DOGE | SETTIMANALE | Classic technical | 116 | 33,62% | -5,23% |
| DOGE | SETTIMANALE | Famiglia statistica | 197 | 52,28% | +1,85% |
| DOGE | SETTIMANALE | Microstruttura exchange | 28 | 46,43% | +0,41% |
| DOGE | SETTIMANALE | Tecnico | 179 | 53,07% | -0,08% |
| DOGE | SWING | Classic technical | 65 | 49,23% | -5,06% |
| DOGE | SWING | Famiglia statistica | 111 | 72,07% | +6,95% |
| DOGE | SWING | Microstruttura exchange | 17 | 52,94% | +0,53% |
| DOGE | SWING | Tecnico | 99 | 58,59% | -0,60% |
| DOGE | MEDIO | Classic technical | 65 | 20,00% | -16,15% |
| DOGE | MEDIO | Famiglia statistica | 91 | 60,44% | +3,05% |
| DOGE | MEDIO | Microstruttura exchange | 10 | 80,00% | +14,73% |
| DOGE | MEDIO | Tecnico | 83 | 21,69% | -15,15% |
| SOL | BREVE | Classic technical | 129 | 49,61% | +0,39% |
| SOL | BREVE | Famiglia statistica | 192 | 49,48% | +0,77% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 183 | 44,81% | -0,10% |
| SOL | SETTIMANALE | Classic technical | 127 | 51,97% | +1,34% |
| SOL | SETTIMANALE | Famiglia statistica | 185 | 57,30% | +3,10% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 180 | 44,44% | -1,11% |
| SOL | SWING | Classic technical | 75 | 53,33% | -0,81% |
| SOL | SWING | Famiglia statistica | 103 | 75,73% | +10,62% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 107 | 43,93% | -5,78% |
| SOL | MEDIO | Classic technical | 54 | 11,11% | -29,45% |
| SOL | MEDIO | Famiglia statistica | 78 | 71,79% | +16,79% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 5 | 100,00% | +28,61% |
| SOL | MEDIO | Tecnico | 88 | 18,18% | -23,14% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 4 | in attesa di controlli maturati |
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
