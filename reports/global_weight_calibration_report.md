# Calibrazione pesi Global Confluence

Generato: 2026-10-18 05:33 UTC

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
| BTC | 93 | UTILE | 90 | 29 | 18 | 0 | Famiglia statistica | 2g | 51,11% | +0,53% | campione utile, valutare con prudenza |
| SOL | 93 | UTILE | 86 | 32 | 18 | 0 | Famiglia statistica | 1g | 53,49% | +0,40% | campione utile, valutare con prudenza |
| DOGE | 93 | UTILE | 91 | 32 | 18 | 0 | Famiglia statistica | 1g | 58,24% | +0,44% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 36 | 41,67% | -0,06% | +0,55% | -0,27% | +1,09% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 90 | 48,89% | +0,25% | +0,20% | -0,33% | +0,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 85 | 47,06% | +0,03% | +0,22% | -0,28% | +0,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 36 | 41,67% | -0,13% | +0,85% | -0,05% | +1,59% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 90 | 51,11% | +0,53% | +0,45% | -0,29% | +1,13% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 85 | 47,06% | +0,06% | +0,43% | -0,21% | +1,11% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 36 | 36,11% | -0,55% | +1,29% | -1,13% | +3,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Famiglia statistica | 89 | 49,44% | +0,81% | +0,74% | -1,35% | +2,43% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 84 | 40,48% | -0,10% | +0,75% | -1,29% | +2,45% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 35 | 37,14% | -2,19% | +2,90% | -1,77% | +5,36% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 87 | 48,28% | +1,56% | +1,45% | -1,97% | +3,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 82 | 42,68% | -0,63% | +1,31% | -1,93% | +3,77% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 34 | 32,35% | -3,81% | +4,23% | -2,10% | +7,38% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 85 | 58,82% | +2,31% | +2,17% | -2,28% | +4,93% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 80 | 41,25% | -1,06% | +2,12% | -2,26% | +4,89% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 34 | 35,29% | -4,21% | +4,28% | -2,33% | +7,98% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 82 | 67,07% | +3,30% | +2,95% | -2,58% | +6,08% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | -1,47% | -1,47% | -4,23% | +1,69% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 77 | 44,16% | -0,55% | +2,90% | -2,59% | +6,10% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 32 | 21,88% | -4,16% | +4,22% | -2,32% | +8,86% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Famiglia statistica | 78 | 60,26% | +4,55% | +4,41% | -2,78% | +8,19% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 8 | 37,50% | -0,75% | -0,75% | -4,66% | +2,55% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 73 | 54,79% | +1,14% | +4,46% | -2,80% | +8,33% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 29 | 44,83% | -4,88% | +8,60% | -2,40% | +12,46% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 74 | 75,68% | +7,75% | +7,59% | -2,97% | +11,58% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 67 | 53,73% | +1,17% | +7,97% | -2,95% | +11,98% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 28 | 57,14% | -2,72% | +12,44% | -2,47% | +17,06% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 69 | 92,75% | +11,96% | +11,96% | -2,89% | +16,36% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +5,65% | +5,65% | -5,13% | +8,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 62 | 66,13% | +1,30% | +12,05% | -2,85% | +16,53% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Classic technical | 23 | 65,22% | -4,44% | +14,44% | -2,41% | +20,40% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 55 | 100,00% | +20,43% | +20,43% | -2,62% | +25,26% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 3 | 100,00% | +10,96% | +10,96% | -4,01% | +16,47% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 50 | 56,00% | -1,59% | +20,37% | -2,43% | +25,26% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 8 | 0,00% | -32,27% | +32,27% | -0,83% | +38,31% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 40 | 100,00% | +27,95% | +27,95% | -2,38% | +33,54% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 35 | 37,14% | -8,12% | +28,30% | -2,09% | +34,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Classic technical | 52 | 40,38% | -0,55% | -0,07% | -1,01% | +0,63% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 91 | 58,24% | +0,44% | -0,07% | -0,89% | +0,92% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 12 | 58,33% | +2,00% | +2,27% | +0,38% | +3,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 85 | 50,59% | +0,20% | -0,15% | -1,00% | +0,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 52 | 46,15% | -0,91% | -0,01% | -1,21% | +1,01% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 91 | 56,04% | +0,65% | -0,05% | -1,14% | +1,26% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 12 | 41,67% | +2,11% | +2,33% | +0,69% | +4,97% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 85 | 55,29% | +0,25% | -0,35% | -1,45% | +0,96% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 51 | 37,25% | -1,71% | +0,23% | -2,84% | +3,45% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 90 | 54,44% | +0,94% | +0,07% | -2,80% | +3,30% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 11 | 54,55% | +2,62% | +2,81% | -1,35% | +6,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 84 | 47,62% | +0,06% | -0,52% | -3,04% | +2,67% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 50 | 40,00% | -3,63% | +1,07% | -4,14% | +6,08% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 88 | 52,27% | +1,32% | +0,56% | -4,05% | +5,53% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 11 | 36,36% | +2,02% | +2,17% | -2,50% | +9,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 82 | 52,44% | -0,60% | -0,20% | -4,43% | +4,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 48 | 33,33% | -5,36% | +2,21% | -4,67% | +8,24% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 86 | 56,98% | +1,73% | +1,20% | -4,70% | +7,42% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 11 | 45,45% | +0,78% | +0,88% | -3,00% | +9,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 80 | 46,25% | -1,03% | +0,27% | -5,15% | +6,50% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 45 | 31,11% | -6,72% | +3,10% | -5,29% | +10,57% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 83 | 57,83% | +2,23% | +1,50% | -5,52% | +9,26% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 77 | 44,16% | -2,06% | +0,24% | -6,07% | +7,88% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 44 | 38,64% | -5,67% | +4,07% | -5,83% | +12,84% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 79 | 65,82% | +3,79% | +3,01% | -6,14% | +12,62% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 11 | 45,45% | +2,03% | +5,60% | -4,35% | +14,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 73 | 43,84% | -2,33% | +1,07% | -6,76% | +10,22% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 43 | 41,86% | -7,66% | +5,14% | -6,03% | +15,65% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 73 | 60,27% | +5,08% | +7,02% | -6,13% | +18,45% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 11 | 63,64% | -0,04% | +4,84% | -5,47% | +18,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 67 | 52,24% | -3,08% | +5,06% | -6,82% | +15,71% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Classic technical | 41 | 48,78% | -6,60% | +8,28% | -5,70% | +22,87% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 68 | 69,12% | +6,79% | +10,87% | -5,47% | +26,13% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 10 | 80,00% | +10,98% | +17,31% | -5,24% | +30,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 62 | 58,06% | -2,31% | +9,46% | -6,17% | +24,12% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 45g | MEDIO | Classic technical | 31 | 3,23% | -22,01% | +21,52% | -5,10% | +38,53% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Famiglia statistica | 54 | 64,81% | +7,80% | +18,96% | -4,75% | +37,55% | PESO OK | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 8 | 62,50% | +11,03% | +21,73% | -4,45% | +35,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 48 | 10,42% | -12,50% | +15,99% | -5,56% | +35,47% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 27 | 0,00% | -23,75% | +23,75% | -3,76% | +44,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 40 | 60,00% | +9,37% | +25,69% | -3,60% | +45,49% | PESO OK | 0,0 | MEDIA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 4 | 75,00% | +19,48% | +38,20% | -1,31% | +51,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 33 | 6,06% | -24,30% | +26,42% | -4,39% | +44,35% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 1g | BREVE | Classic technical | 59 | 44,07% | -0,09% | +0,51% | -0,48% | +1,43% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 86 | 53,49% | +0,40% | +0,14% | -0,73% | +0,99% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 84 | 46,43% | -0,06% | +0,13% | -0,79% | +0,96% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 59 | 47,46% | +0,15% | +0,60% | -0,64% | +1,71% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 86 | 48,84% | +0,62% | +0,44% | -0,89% | +1,39% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 84 | 45,24% | -0,02% | +0,27% | -0,87% | +1,40% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 59 | 45,76% | +0,08% | +0,61% | -2,23% | +3,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 85 | 51,76% | +1,15% | +0,81% | -2,38% | +3,41% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 83 | 44,58% | -0,31% | +0,42% | -2,41% | +2,99% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 58 | 48,28% | +0,02% | +0,68% | -3,30% | +4,39% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 83 | 53,01% | +1,90% | +1,52% | -3,40% | +5,39% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 81 | 45,68% | -0,77% | +1,13% | -3,46% | +4,86% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 58 | 43,10% | -0,23% | +0,35% | -4,10% | +5,03% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 81 | 61,73% | +3,26% | +2,47% | -3,96% | +7,07% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 79 | 39,24% | -1,83% | +1,54% | -4,06% | +6,21% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 57 | 43,86% | -0,57% | +0,11% | -4,99% | +5,77% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 78 | 70,51% | +5,95% | +4,07% | -4,53% | +8,98% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 76 | 40,79% | -2,50% | +2,49% | -4,70% | +7,67% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 54 | 42,59% | -0,29% | +1,33% | -5,64% | +7,48% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 74 | 78,38% | +8,86% | +7,07% | -4,77% | +12,81% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 72 | 38,89% | -3,25% | +4,67% | -5,11% | +10,76% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 48 | 56,25% | -1,82% | +8,64% | -5,55% | +14,77% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 69 | 82,61% | +14,41% | +13,24% | -4,85% | +19,46% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 66 | 50,00% | -5,44% | +10,83% | -5,23% | +17,14% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Classic technical | 43 | 53,49% | -4,28% | +21,82% | -4,56% | +27,59% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 64 | 90,62% | +18,67% | +21,09% | -4,22% | +28,74% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 61 | 44,26% | -7,62% | +20,13% | -4,64% | +26,68% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 45g | MEDIO | Classic technical | 36 | 38,89% | -16,95% | +28,32% | -4,22% | +39,56% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Famiglia statistica | 50 | 76,00% | +20,79% | +33,87% | -3,97% | +43,33% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +28,91% | +28,91% | -3,55% | +37,55% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 52 | 34,62% | -21,16% | +32,82% | -4,38% | +42,33% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 21 | 0,00% | -53,73% | +53,73% | -4,64% | +60,15% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 36 | 77,78% | +33,50% | +48,66% | -3,91% | +59,43% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +47,10% | +47,10% | -5,94% | +54,98% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 37 | 10,81% | -40,42% | +47,75% | -4,69% | +57,67% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 84 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 91 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 108 | 39,81% | -0,25% |
| BTC | BREVE | Famiglia statistica | 269 | 49,81% | +0,53% |
| BTC | BREVE | Microstruttura exchange | 27 | 37,04% | -0,30% |
| BTC | BREVE | Tecnico | 254 | 44,88% | -0,00% |
| BTC | SETTIMANALE | Classic technical | 103 | 34,95% | -3,39% |
| BTC | SETTIMANALE | Famiglia statistica | 254 | 57,87% | +2,37% |
| BTC | SETTIMANALE | Microstruttura exchange | 26 | 23,08% | -1,70% |
| BTC | SETTIMANALE | Tecnico | 239 | 42,68% | -0,75% |
| BTC | SWING | Classic technical | 61 | 32,79% | -4,50% |
| BTC | SWING | Famiglia statistica | 152 | 67,76% | +6,11% |
| BTC | SWING | Microstruttura exchange | 15 | 46,67% | -0,24% |
| BTC | SWING | Tecnico | 140 | 54,29% | +1,16% |
| BTC | MEDIO | Classic technical | 59 | 52,54% | -7,40% |
| BTC | MEDIO | Famiglia statistica | 164 | 96,95% | +18,70% |
| BTC | MEDIO | Microstruttura exchange | 9 | 100,00% | +9,68% |
| BTC | MEDIO | Tecnico | 147 | 55,78% | -1,92% |
| DOGE | BREVE | Classic technical | 155 | 41,29% | -1,05% |
| DOGE | BREVE | Famiglia statistica | 272 | 56,25% | +0,67% |
| DOGE | BREVE | Microstruttura exchange | 35 | 51,43% | +2,23% |
| DOGE | BREVE | Tecnico | 254 | 51,18% | +0,17% |
| DOGE | SETTIMANALE | Classic technical | 143 | 34,97% | -5,18% |
| DOGE | SETTIMANALE | Famiglia statistica | 257 | 55,64% | +1,75% |
| DOGE | SETTIMANALE | Microstruttura exchange | 33 | 45,45% | +1,16% |
| DOGE | SETTIMANALE | Tecnico | 239 | 47,70% | -1,21% |
| DOGE | SWING | Classic technical | 87 | 40,23% | -6,65% |
| DOGE | SWING | Famiglia statistica | 152 | 63,16% | +4,41% |
| DOGE | SWING | Microstruttura exchange | 22 | 54,55% | +0,99% |
| DOGE | SWING | Tecnico | 140 | 47,86% | -2,69% |
| DOGE | MEDIO | Classic technical | 99 | 21,21% | -16,10% |
| DOGE | MEDIO | Famiglia statistica | 162 | 65,43% | +7,76% |
| DOGE | MEDIO | Microstruttura exchange | 22 | 72,73% | +12,54% |
| DOGE | MEDIO | Tecnico | 143 | 30,07% | -10,81% |
| SOL | BREVE | Classic technical | 177 | 45,76% | +0,05% |
| SOL | BREVE | Famiglia statistica | 257 | 51,36% | +0,72% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 251 | 45,42% | -0,13% |
| SOL | SETTIMANALE | Classic technical | 173 | 45,09% | -0,26% |
| SOL | SETTIMANALE | Famiglia statistica | 242 | 61,57% | +3,66% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 236 | 41,95% | -1,68% |
| SOL | SWING | Classic technical | 102 | 49,02% | -1,01% |
| SOL | SWING | Famiglia statistica | 143 | 80,42% | +11,54% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 138 | 44,20% | -4,30% |
| SOL | MEDIO | Classic technical | 100 | 37,00% | -19,23% |
| SOL | MEDIO | Famiglia statistica | 150 | 82,67% | +22,94% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 12 | 100,00% | +28,96% |
| SOL | MEDIO | Tecnico | 150 | 32,67% | -20,40% |

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
