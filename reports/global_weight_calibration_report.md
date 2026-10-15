# Calibrazione pesi Global Confluence

Generato: 2026-10-15 05:34 UTC

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
| BTC | 91 | UTILE | 88 | 28 | 18 | 0 | Famiglia statistica | 1g | 48,86% | +0,25% | campione utile, valutare con prudenza |
| SOL | 91 | UTILE | 84 | 32 | 18 | 0 | Famiglia statistica | 1g | 53,57% | +0,40% | campione utile, valutare con prudenza |
| DOGE | 91 | UTILE | 89 | 32 | 18 | 0 | Famiglia statistica | 1g | 58,43% | +0,46% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 35 | 42,86% | -0,02% | +0,53% | -0,31% | +1,07% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 88 | 48,86% | +0,25% | +0,19% | -0,34% | +0,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 83 | 46,99% | +0,04% | +0,21% | -0,28% | +0,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 35 | 42,86% | -0,11% | +0,85% | -0,05% | +1,57% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 87 | 51,72% | +0,56% | +0,48% | -0,26% | +1,16% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 82 | 46,34% | +0,05% | +0,47% | -0,17% | +1,14% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 35 | 37,14% | -0,55% | +1,31% | -1,15% | +3,03% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Famiglia statistica | 86 | 50,00% | +0,87% | +0,80% | -1,32% | +2,49% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 81 | 39,51% | -0,14% | +0,82% | -1,25% | +2,52% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 34 | 35,29% | -2,33% | +3,06% | -1,68% | +5,50% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 84 | 47,62% | +1,60% | +1,57% | -1,90% | +3,94% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 8 | 12,50% | -1,59% | -1,59% | -2,65% | +1,53% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 79 | 41,77% | -0,71% | +1,44% | -1,86% | +3,88% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 34 | 32,35% | -3,81% | +4,23% | -2,10% | +7,38% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 82 | 57,32% | +2,36% | +2,29% | -2,25% | +5,04% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 8 | 25,00% | -2,12% | -2,12% | -3,55% | +1,61% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 77 | 42,86% | -1,06% | +2,25% | -2,22% | +5,01% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 33 | 36,36% | -4,21% | +4,54% | -2,21% | +8,23% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 79 | 65,82% | +3,31% | +3,17% | -2,48% | +6,29% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | -1,47% | -1,47% | -4,23% | +1,69% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 74 | 45,95% | -0,45% | +3,14% | -2,49% | +6,33% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 29 | 24,14% | -4,15% | +5,09% | -1,91% | +9,57% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 76 | 60,53% | +4,69% | +4,65% | -2,68% | +8,37% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 7 | 42,86% | -0,11% | -0,11% | -4,30% | +2,85% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 70 | 57,14% | +1,37% | +4,83% | -2,65% | +8,60% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 29 | 44,83% | -4,88% | +8,60% | -2,40% | +12,46% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 71 | 76,06% | +8,03% | +8,03% | -2,89% | +11,92% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 64 | 56,25% | +1,36% | +8,48% | -2,86% | +12,38% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 26 | 61,54% | -2,34% | +12,81% | -2,66% | +17,23% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 67 | 92,54% | +12,09% | +12,09% | -2,97% | +16,41% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 62 | 66,13% | +1,30% | +12,05% | -2,85% | +16,53% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Classic technical | 20 | 60,00% | -5,83% | +15,88% | -2,18% | +21,66% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 52 | 100,00% | +21,33% | +21,33% | -2,55% | +26,03% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 47 | 53,19% | -2,00% | +21,37% | -2,34% | +26,10% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 7 | 0,00% | -32,68% | +32,68% | -1,07% | +38,39% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 37 | 100,00% | +27,96% | +27,96% | -2,79% | +33,29% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 32 | 37,50% | -7,95% | +28,34% | -2,53% | +33,87% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Classic technical | 50 | 40,00% | -0,58% | -0,06% | -1,00% | +0,64% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 89 | 58,43% | +0,46% | -0,06% | -0,89% | +0,93% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 11 | 63,64% | +2,53% | +2,82% | +0,75% | +3,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 83 | 50,60% | +0,20% | -0,15% | -1,00% | +0,84% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 50 | 44,00% | -1,04% | +0,08% | -1,17% | +1,03% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 88 | 57,95% | +0,75% | +0,03% | -1,08% | +1,32% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 11 | 45,45% | +2,65% | +2,89% | +1,08% | +5,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 82 | 53,66% | +0,17% | -0,27% | -1,39% | +1,02% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 49 | 34,69% | -1,86% | +0,31% | -2,85% | +3,50% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 87 | 56,32% | +1,09% | +0,19% | -2,75% | +3,38% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 11 | 54,55% | +2,62% | +2,81% | -1,35% | +6,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 81 | 45,68% | -0,06% | -0,41% | -3,00% | +2,74% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 47 | 36,17% | -4,28% | +1,56% | -3,91% | +6,43% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 85 | 54,12% | +1,60% | +0,82% | -3,91% | +5,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 11 | 36,36% | +2,02% | +2,17% | -2,50% | +9,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 79 | 50,63% | -0,88% | +0,05% | -4,30% | +4,99% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 45 | 28,89% | -6,15% | +2,80% | -4,47% | +8,62% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 83 | 59,04% | +2,03% | +1,48% | -4,59% | +7,59% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 11 | 45,45% | +0,78% | +0,88% | -3,00% | +9,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 77 | 44,16% | -1,32% | +0,53% | -5,05% | +6,65% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 44 | 29,55% | -7,10% | +3,40% | -5,16% | +10,81% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 80 | 56,25% | +1,86% | +2,00% | -5,24% | +9,63% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 74 | 43,24% | -2,27% | +0,74% | -5,78% | +8,22% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 43 | 39,53% | -5,45% | +4,51% | -5,57% | +13,12% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 76 | 64,47% | +3,35% | +3,72% | -5,75% | +12,99% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 11 | 45,45% | +2,03% | +5,60% | -4,35% | +14,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 70 | 45,71% | -1,78% | +1,76% | -6,36% | +10,51% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 42 | 42,86% | -7,44% | +5,67% | -5,73% | +16,02% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 70 | 58,57% | +4,53% | +8,09% | -5,59% | +19,19% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 11 | 63,64% | -0,04% | +4,84% | -5,47% | +18,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 64 | 54,69% | -2,39% | +6,13% | -6,26% | +16,39% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Classic technical | 39 | 48,72% | -6,93% | +8,70% | -5,92% | +22,47% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 66 | 69,70% | +7,00% | +11,19% | -5,59% | +25,99% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 9 | 88,89% | +12,44% | +19,48% | -5,48% | +30,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 60 | 58,33% | -2,39% | +9,77% | -6,33% | +23,90% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 45g | MEDIO | Classic technical | 31 | 3,23% | -22,01% | +21,52% | -5,10% | +38,53% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Famiglia statistica | 51 | 62,75% | +8,08% | +20,25% | -4,73% | +38,14% | PESO OK | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 8 | 62,50% | +11,03% | +21,73% | -4,45% | +35,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 45 | 11,11% | -13,13% | +17,26% | -5,59% | +36,00% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 24 | 0,00% | -24,90% | +24,90% | -4,47% | +43,41% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 37 | 56,76% | +8,95% | +26,59% | -4,05% | +45,07% | PESO OK | 0,0 | MEDIA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 4 | 75,00% | +19,48% | +38,20% | -1,31% | +51,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 32 | 6,25% | -24,52% | +26,71% | -4,51% | +44,17% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 1g | BREVE | Classic technical | 58 | 44,83% | -0,03% | +0,45% | -0,53% | +1,39% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 84 | 53,57% | +0,40% | +0,12% | -0,74% | +0,98% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 82 | 46,34% | -0,05% | +0,11% | -0,80% | +0,95% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 58 | 48,28% | +0,18% | +0,59% | -0,66% | +1,66% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 83 | 49,40% | +0,68% | +0,49% | -0,87% | +1,41% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 81 | 44,44% | -0,05% | +0,31% | -0,84% | +1,42% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 58 | 46,55% | +0,10% | +0,60% | -2,28% | +3,11% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 82 | 52,44% | +1,25% | +0,89% | -2,35% | +3,47% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 80 | 43,75% | -0,38% | +0,49% | -2,38% | +3,05% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 58 | 48,28% | +0,02% | +0,68% | -3,30% | +4,39% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 80 | 55,00% | +2,17% | +1,78% | -3,24% | +5,59% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 78 | 43,59% | -1,00% | +1,38% | -3,30% | +5,04% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 57 | 43,86% | -0,12% | +0,46% | -4,03% | +5,07% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 78 | 64,10% | +3,59% | +2,77% | -3,82% | +7,23% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 76 | 38,16% | -1,96% | +1,81% | -3,91% | +6,35% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 55 | 45,45% | -0,14% | +0,57% | -4,63% | +6,00% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 75 | 69,33% | +5,72% | +4,70% | -4,15% | +9,38% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 73 | 42,47% | -2,12% | +3,07% | -4,32% | +8,03% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
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
| SOL | 30g | MEDIO | Famiglia statistica | 62 | 90,32% | +19,07% | +21,56% | -4,40% | +28,81% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 60 | 45,00% | -7,68% | +20,40% | -4,74% | +26,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 45g | MEDIO | Classic technical | 33 | 33,33% | -18,74% | +30,66% | -4,13% | +41,08% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Famiglia statistica | 47 | 74,47% | +21,94% | +35,86% | -3,89% | +44,64% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +28,91% | +28,91% | -3,55% | +37,55% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 49 | 30,61% | -22,62% | +34,67% | -4,33% | +43,52% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 21 | 0,00% | -53,73% | +53,73% | -4,64% | +60,15% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 33 | 75,76% | +33,17% | +49,71% | -4,58% | +59,01% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +47,10% | +47,10% | -5,94% | +54,98% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 35 | 11,43% | -40,53% | +48,28% | -4,98% | +57,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 82 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 89 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 105 | 40,95% | -0,23% |
| BTC | BREVE | Famiglia statistica | 261 | 50,19% | +0,56% |
| BTC | BREVE | Microstruttura exchange | 27 | 37,04% | -0,30% |
| BTC | BREVE | Tecnico | 246 | 44,31% | -0,02% |
| BTC | SETTIMANALE | Classic technical | 101 | 34,65% | -3,44% |
| BTC | SETTIMANALE | Famiglia statistica | 245 | 56,73% | +2,41% |
| BTC | SETTIMANALE | Microstruttura exchange | 24 | 25,00% | -1,73% |
| BTC | SETTIMANALE | Tecnico | 230 | 43,48% | -0,74% |
| BTC | SWING | Classic technical | 58 | 34,48% | -4,52% |
| BTC | SWING | Famiglia statistica | 147 | 68,03% | +6,30% |
| BTC | SWING | Microstruttura exchange | 14 | 50,00% | +0,11% |
| BTC | SWING | Tecnico | 134 | 56,72% | +1,36% |
| BTC | MEDIO | Classic technical | 53 | 52,83% | -7,66% |
| BTC | MEDIO | Famiglia statistica | 156 | 96,79% | +18,94% |
| BTC | MEDIO | Microstruttura exchange | 9 | 100,00% | +9,68% |
| BTC | MEDIO | Tecnico | 141 | 55,32% | -1,90% |
| DOGE | BREVE | Classic technical | 149 | 39,60% | -1,15% |
| DOGE | BREVE | Famiglia statistica | 264 | 57,58% | +0,76% |
| DOGE | BREVE | Microstruttura exchange | 33 | 54,55% | +2,60% |
| DOGE | BREVE | Tecnico | 246 | 50,00% | +0,10% |
| DOGE | SETTIMANALE | Classic technical | 136 | 31,62% | -5,81% |
| DOGE | SETTIMANALE | Famiglia statistica | 248 | 56,45% | +1,83% |
| DOGE | SETTIMANALE | Microstruttura exchange | 33 | 45,45% | +1,16% |
| DOGE | SETTIMANALE | Tecnico | 230 | 46,09% | -1,47% |
| DOGE | SWING | Classic technical | 85 | 41,18% | -6,43% |
| DOGE | SWING | Famiglia statistica | 146 | 61,64% | +3,92% |
| DOGE | SWING | Microstruttura exchange | 22 | 54,55% | +0,99% |
| DOGE | SWING | Tecnico | 134 | 50,00% | -2,07% |
| DOGE | MEDIO | Classic technical | 94 | 21,28% | -16,49% |
| DOGE | MEDIO | Famiglia statistica | 154 | 64,29% | +7,83% |
| DOGE | MEDIO | Microstruttura exchange | 21 | 76,19% | +13,25% |
| DOGE | MEDIO | Tecnico | 137 | 30,66% | -11,08% |
| SOL | BREVE | Classic technical | 174 | 46,55% | +0,08% |
| SOL | BREVE | Famiglia statistica | 249 | 51,81% | +0,77% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 243 | 44,86% | -0,16% |
| SOL | SETTIMANALE | Classic technical | 170 | 45,88% | -0,08% |
| SOL | SETTIMANALE | Famiglia statistica | 233 | 62,66% | +3,79% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 227 | 41,41% | -1,68% |
| SOL | SWING | Classic technical | 96 | 52,08% | -0,21% |
| SOL | SWING | Famiglia statistica | 137 | 79,56% | +11,44% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 132 | 46,21% | -3,86% |
| SOL | MEDIO | Classic technical | 96 | 35,42% | -20,07% |
| SOL | MEDIO | Famiglia statistica | 142 | 81,69% | +23,30% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 12 | 100,00% | +28,96% |
| SOL | MEDIO | Tecnico | 144 | 31,94% | -20,75% |

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
