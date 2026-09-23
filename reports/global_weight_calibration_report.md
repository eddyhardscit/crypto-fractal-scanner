# Calibrazione pesi Global Confluence

Generato: 2026-09-23 05:33 UTC

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
| BTC | 71 | UTILE | 70 | 19 | 13 | 0 | Famiglia statistica | 1g | 54,29% | +0,40% | campione utile, valutare con prudenza |
| SOL | 71 | UTILE | 65 | 27 | 12 | 0 | Famiglia statistica | 1g | 55,38% | +0,47% | campione utile, valutare con prudenza |
| DOGE | 71 | UTILE | 69 | 29 | 12 | 0 | Famiglia statistica | 1g | 56,52% | +0,35% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 28 | 39,29% | +0,16% | +0,86% | +0,02% | +1,38% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 70 | 54,29% | +0,40% | +0,40% | -0,13% | +0,91% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 6 | 50,00% | +0,17% | +0,17% | -0,29% | +0,65% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 63 | 41,27% | +0,08% | +0,41% | -0,05% | +0,93% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
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
| BTC | 7g | SETTIMANALE | Classic technical | 27 | 40,74% | -3,76% | +5,59% | -1,42% | +8,56% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 68 | 58,82% | +2,77% | +2,77% | -2,06% | +5,49% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 62 | 43,55% | -1,13% | +2,98% | -1,96% | +5,69% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 24 | 50,00% | -3,59% | +5,20% | -1,59% | +8,77% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 65 | 63,08% | +3,38% | +3,38% | -2,40% | +6,39% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 60 | 48,33% | -0,68% | +3,76% | -2,25% | +6,82% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 24 | 29,17% | -3,41% | +4,78% | -1,84% | +9,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 61 | 57,38% | +4,73% | +4,73% | -2,59% | +8,30% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 56 | 53,57% | +0,94% | +5,27% | -2,42% | +8,89% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 22 | 50,00% | -5,00% | +9,06% | -2,06% | +12,94% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 54 | 72,22% | +8,44% | +8,44% | -2,48% | +12,33% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 3 | 66,67% | -0,54% | -0,54% | -2,98% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 49 | 46,94% | -0,15% | +9,14% | -2,28% | +13,09% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 13 | 38,46% | -9,63% | +18,78% | -0,70% | +23,30% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 45 | 88,89% | +14,71% | +14,71% | -2,17% | +18,96% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +5,87% | +5,87% | -2,41% | +8,88% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 40 | 47,50% | -1,69% | +14,96% | -1,88% | +19,47% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 4 | 0,00% | -21,70% | +21,70% | -1,55% | +30,01% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 32 | 100,00% | +23,45% | +23,45% | -3,00% | +28,03% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 27 | 37,04% | -4,53% | +23,90% | -2,73% | +28,53% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 17 | 100,00% | +24,08% | +24,08% | -3,26% | +29,37% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 14 | 28,57% | -12,34% | +24,25% | -2,94% | +30,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 41 | 41,46% | -0,51% | +0,29% | -0,53% | +1,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 69 | 56,52% | +0,35% | +0,35% | -0,44% | +1,26% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 11 | 63,64% | +2,53% | +2,82% | +0,75% | +3,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 63 | 52,38% | +0,34% | +0,28% | -0,55% | +1,17% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
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
| DOGE | 7g | SETTIMANALE | Classic technical | 40 | 30,00% | -6,14% | +3,47% | -4,04% | +8,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 67 | 53,73% | +1,53% | +2,82% | -3,71% | +8,50% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 9 | 44,44% | -0,49% | -0,37% | -2,97% | +7,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 61 | 49,18% | -0,49% | +1,76% | -4,21% | +7,40% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 37 | 35,14% | -5,84% | +2,66% | -4,91% | +9,80% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 64 | 51,56% | +2,09% | +2,74% | -4,39% | +9,76% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 9 | 55,56% | -1,01% | -0,68% | -4,16% | +8,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 58 | 55,17% | -0,09% | +1,20% | -5,00% | +7,97% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 34 | 50,00% | -3,09% | +3,40% | -5,30% | +11,12% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 60 | 68,33% | +4,89% | +4,07% | -4,81% | +12,60% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 9 | 44,44% | +1,04% | +5,41% | -4,48% | +13,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 54 | 59,26% | +1,24% | +1,56% | -5,51% | +9,34% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 31 | 48,39% | -7,22% | +5,15% | -4,78% | +14,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 53 | 73,58% | +8,30% | +8,37% | -4,45% | +18,70% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 8 | 62,50% | -0,06% | +6,66% | -3,62% | +19,12% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 47 | 59,57% | -1,88% | +5,74% | -5,22% | +14,83% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 30 | 46,67% | -9,11% | +11,08% | -4,75% | +22,89% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 45 | 91,11% | +12,77% | +13,78% | -4,11% | +27,62% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 7 | 85,71% | +14,05% | +23,10% | -3,96% | +33,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 38 | 50,00% | -7,12% | +11,94% | -4,89% | +24,74% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 22 | 0,00% | -22,71% | +22,71% | -4,86% | +39,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 32 | 50,00% | +2,73% | +22,50% | -4,56% | +40,39% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,91% | +37,31% | -1,31% | +47,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 30 | 0,00% | -21,64% | +21,64% | -4,76% | +40,02% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 16 | 0,00% | -22,42% | +22,42% | -5,92% | +39,62% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 17 | 5,88% | -16,43% | +21,97% | -6,05% | +39,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 17 | 0,00% | -21,97% | +21,97% | -6,05% | +39,36% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 44 | 50,00% | +0,19% | +0,83% | -0,23% | +1,74% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 65 | 55,38% | +0,47% | +0,48% | -0,35% | +1,33% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 62 | 48,39% | +0,06% | +0,51% | -0,39% | +1,32% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
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
| SOL | 7g | SETTIMANALE | Famiglia statistica | 63 | 58,73% | +3,12% | +4,13% | -3,08% | +8,15% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 60 | 40,00% | -1,18% | +3,00% | -3,19% | +7,12% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 42 | 54,76% | +1,69% | +1,60% | -3,81% | +6,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 60 | 61,67% | +4,66% | +5,42% | -3,53% | +9,67% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 60 | 48,33% | -1,26% | +4,34% | -3,67% | +8,74% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 42 | 52,38% | +2,18% | +3,36% | -4,30% | +8,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 56 | 73,21% | +7,42% | +8,14% | -3,79% | +13,13% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 58 | 43,10% | -2,76% | +6,42% | -4,02% | +11,63% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Classic technical | 35 | 57,14% | -3,42% | +10,00% | -4,22% | +15,23% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 49 | 79,59% | +14,51% | +14,56% | -3,84% | +20,40% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 51 | 47,06% | -8,35% | +12,06% | -4,22% | +17,86% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 26 | 26,92% | -16,45% | +26,41% | -3,55% | +32,17% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 40 | 85,00% | +22,31% | +26,18% | -3,47% | +33,05% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 3 | 100,00% | +22,86% | +22,86% | -3,34% | +27,23% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 42 | 21,43% | -17,20% | +22,92% | -4,00% | +29,36% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 21 | 0,00% | -38,81% | +38,81% | -4,64% | +48,52% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 28 | 71,43% | +21,35% | +38,26% | -5,06% | +46,56% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,56% | +44,56% | -5,94% | +49,24% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 31 | 12,90% | -31,05% | +37,40% | -5,38% | +45,67% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 9 | 0,00% | -42,37% | +42,37% | -6,82% | +50,35% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 13 | 38,46% | -2,83% | +39,15% | -7,74% | +47,27% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +41,93% | +41,93% | -9,62% | +45,82% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 17 | 23,53% | -22,64% | +38,59% | -7,53% | +47,05% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 67 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 70 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 84 | 40,48% | -0,04% |
| BTC | BREVE | Famiglia statistica | 208 | 53,85% | +0,77% |
| BTC | BREVE | Microstruttura exchange | 16 | 43,75% | +0,40% |
| BTC | BREVE | Tecnico | 187 | 40,64% | +0,01% |
| BTC | SETTIMANALE | Classic technical | 79 | 44,30% | -3,15% |
| BTC | SETTIMANALE | Famiglia statistica | 202 | 57,43% | +2,72% |
| BTC | SETTIMANALE | Microstruttura exchange | 15 | 33,33% | -1,25% |
| BTC | SETTIMANALE | Tecnico | 184 | 44,57% | -0,85% |
| BTC | SWING | Classic technical | 46 | 39,13% | -4,17% |
| BTC | SWING | Famiglia statistica | 115 | 64,35% | +6,47% |
| BTC | SWING | Microstruttura exchange | 8 | 50,00% | -0,03% |
| BTC | SWING | Tecnico | 105 | 50,48% | +0,43% |
| BTC | MEDIO | Classic technical | 17 | 29,41% | -12,47% |
| BTC | MEDIO | Famiglia statistica | 94 | 94,68% | +19,38% |
| BTC | MEDIO | Microstruttura exchange | 4 | 100,00% | +14,55% |
| BTC | MEDIO | Tecnico | 81 | 40,74% | -4,48% |
| DOGE | BREVE | Classic technical | 123 | 39,02% | -1,33% |
| DOGE | BREVE | Famiglia statistica | 205 | 56,10% | +0,65% |
| DOGE | BREVE | Microstruttura exchange | 31 | 54,84% | +2,84% |
| DOGE | BREVE | Tecnico | 187 | 50,80% | +0,29% |
| DOGE | SETTIMANALE | Classic technical | 118 | 33,05% | -5,54% |
| DOGE | SETTIMANALE | Famiglia statistica | 199 | 51,76% | +1,59% |
| DOGE | SETTIMANALE | Microstruttura exchange | 28 | 46,43% | +0,41% |
| DOGE | SETTIMANALE | Tecnico | 181 | 52,49% | -0,34% |
| DOGE | SWING | Classic technical | 65 | 49,23% | -5,06% |
| DOGE | SWING | Famiglia statistica | 113 | 70,80% | +6,49% |
| DOGE | SWING | Microstruttura exchange | 17 | 52,94% | +0,53% |
| DOGE | SWING | Tecnico | 101 | 59,41% | -0,21% |
| DOGE | MEDIO | Classic technical | 68 | 20,59% | -16,64% |
| DOGE | MEDIO | Famiglia statistica | 94 | 61,70% | +4,07% |
| DOGE | MEDIO | Microstruttura exchange | 13 | 84,62% | +19,38% |
| DOGE | MEDIO | Tecnico | 85 | 22,35% | -15,21% |
| SOL | BREVE | Classic technical | 130 | 50,00% | +0,41% |
| SOL | BREVE | Famiglia statistica | 193 | 49,74% | +0,78% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 184 | 45,11% | -0,08% |
| SOL | SETTIMANALE | Classic technical | 127 | 51,97% | +1,34% |
| SOL | SETTIMANALE | Famiglia statistica | 187 | 57,75% | +3,28% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 181 | 44,75% | -1,01% |
| SOL | SWING | Classic technical | 77 | 54,55% | -0,37% |
| SOL | SWING | Famiglia statistica | 105 | 76,19% | +10,73% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 109 | 44,95% | -5,38% |
| SOL | MEDIO | Classic technical | 56 | 12,50% | -29,00% |
| SOL | MEDIO | Famiglia statistica | 81 | 72,84% | +17,95% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 6 | 100,00% | +33,27% |
| SOL | MEDIO | Tecnico | 90 | 18,89% | -23,00% |

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
