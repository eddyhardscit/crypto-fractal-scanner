# Calibrazione pesi Global Confluence

Generato: 2026-10-22 05:34 UTC

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
| BTC | 97 | UTILE | 94 | 29 | 18 | 0 | Famiglia statistica | 1g | 48,94% | +0,26% | campione utile, valutare con prudenza |
| SOL | 97 | UTILE | 90 | 32 | 18 | 0 | Famiglia statistica | 1g | 53,33% | +0,40% | campione utile, valutare con prudenza |
| DOGE | 97 | UTILE | 95 | 32 | 18 | 0 | Famiglia statistica | 1g | 57,89% | +0,43% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 36 | 41,67% | -0,06% | +0,55% | -0,27% | +1,09% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 94 | 48,94% | +0,26% | +0,20% | -0,32% | +0,71% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 89 | 49,44% | +0,07% | +0,22% | -0,27% | +0,75% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 36 | 41,67% | -0,13% | +0,85% | -0,05% | +1,59% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 93 | 52,69% | +0,53% | +0,45% | -0,27% | +1,13% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 88 | 47,73% | +0,07% | +0,44% | -0,20% | +1,12% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 36 | 36,11% | -0,55% | +1,29% | -1,13% | +3,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Famiglia statistica | 92 | 51,09% | +0,81% | +0,74% | -1,35% | +2,41% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 87 | 40,23% | -0,09% | +0,75% | -1,29% | +2,42% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 36 | 36,11% | -2,16% | +2,85% | -1,73% | +5,27% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 90 | 48,89% | +1,52% | +1,41% | -1,98% | +3,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 85 | 42,35% | -0,62% | +1,28% | -1,94% | +3,66% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 36 | 33,33% | -3,63% | +4,03% | -2,13% | +7,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 89 | 58,43% | +2,22% | +2,05% | -2,34% | +4,76% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 84 | 42,86% | -0,99% | +2,00% | -2,32% | +4,71% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 35 | 37,14% | -4,05% | +4,12% | -2,39% | +7,77% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 86 | 67,44% | +3,17% | +2,78% | -2,64% | +5,87% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 9 | 33,33% | -1,34% | -1,34% | -4,20% | +1,67% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 81 | 44,44% | -0,52% | +2,73% | -2,66% | +5,88% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 34 | 20,59% | -4,14% | +3,74% | -2,59% | +8,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Famiglia statistica | 82 | 62,20% | +4,45% | +4,08% | -2,92% | +7,83% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 8 | 37,50% | -0,75% | -0,75% | -4,66% | +2,55% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 77 | 51,95% | +0,96% | +4,10% | -2,95% | +7,94% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 29 | 44,83% | -4,88% | +8,60% | -2,40% | +12,46% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 76 | 76,32% | +7,57% | +7,36% | -3,00% | +11,40% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 7 | 57,14% | +0,34% | +0,34% | -5,07% | +4,89% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 70 | 51,43% | +1,08% | +7,59% | -3,00% | +11,67% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 28 | 57,14% | -2,72% | +12,44% | -2,47% | +17,06% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 70 | 91,43% | +11,75% | +11,75% | -2,94% | +16,16% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Microstruttura exchange | 6 | 83,33% | +4,24% | +4,24% | -5,33% | +7,62% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 63 | 65,08% | +1,24% | +11,81% | -2,91% | +16,31% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Classic technical | 24 | 66,67% | -4,17% | +13,92% | -2,62% | +19,88% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 59 | 100,00% | +19,25% | +19,25% | -2,88% | +24,17% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +7,72% | +7,72% | -5,13% | +13,34% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 54 | 59,26% | -1,25% | +19,09% | -2,73% | +24,06% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 12 | 33,33% | -17,87% | +25,16% | -0,54% | +31,35% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 44 | 100,00% | +26,41% | +26,41% | -2,16% | +32,08% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +17,26% | +17,26% | -2,41% | +21,34% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 39 | 43,59% | -6,16% | +26,52% | -1,87% | +32,39% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Classic technical | 56 | 41,07% | -0,53% | -0,04% | -0,94% | +0,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 95 | 57,89% | +0,43% | -0,05% | -0,86% | +0,94% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 13 | 53,85% | +1,69% | +1,93% | +0,19% | +2,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 89 | 50,56% | +0,18% | -0,13% | -0,96% | +0,85% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 55 | 43,64% | -0,93% | +0,06% | -1,09% | +1,09% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 94 | 57,45% | +0,67% | -0,01% | -1,08% | +1,30% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 12 | 41,67% | +2,11% | +2,33% | +0,69% | +4,97% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 88 | 53,41% | +0,20% | -0,29% | -1,37% | +1,02% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 54 | 37,04% | -1,63% | +0,22% | -2,81% | +3,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 93 | 54,84% | +0,91% | +0,07% | -2,78% | +3,25% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 12 | 50,00% | +2,13% | +2,30% | -1,68% | +5,97% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 87 | 47,13% | +0,05% | -0,49% | -3,01% | +2,65% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 52 | 42,31% | -3,47% | +1,01% | -4,21% | +5,92% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 91 | 50,55% | +1,20% | +0,47% | -4,13% | +5,36% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 12 | 33,33% | +1,81% | +1,94% | -2,90% | +8,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 85 | 54,12% | -0,50% | -0,27% | -4,50% | +4,68% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 51 | 35,29% | -4,75% | +1,79% | -4,89% | +7,81% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 90 | 55,56% | +1,45% | +0,94% | -4,88% | +7,09% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 11 | 45,45% | +0,78% | +0,88% | -3,00% | +9,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 84 | 47,62% | -0,76% | +0,03% | -5,33% | +6,19% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 49 | 36,73% | -5,60% | +2,28% | -5,75% | +9,82% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 87 | 55,17% | +1,80% | +1,11% | -5,78% | +8,90% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 81 | 46,91% | -1,61% | -0,11% | -6,31% | +7,56% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 45 | 40,00% | -5,34% | +3,78% | -5,99% | +12,56% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 83 | 67,47% | +4,23% | +2,25% | -6,64% | +12,01% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 11 | 45,45% | +2,03% | +5,60% | -4,35% | +14,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 77 | 44,16% | -2,39% | +0,35% | -7,27% | +9,68% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 43 | 41,86% | -7,66% | +5,14% | -6,03% | +15,65% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 76 | 61,84% | +5,44% | +6,19% | -6,59% | +17,90% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 11 | 63,64% | -0,04% | +4,84% | -5,47% | +18,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 70 | 50,00% | -3,56% | +4,23% | -7,29% | +15,23% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Classic technical | 41 | 48,78% | -6,60% | +8,28% | -5,70% | +22,87% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 69 | 69,57% | +6,96% | +10,44% | -5,72% | +25,83% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 11 | 72,73% | +8,26% | +14,01% | -6,83% | +27,95% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 63 | 57,14% | -2,58% | +9,01% | -6,43% | +23,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 45g | MEDIO | Classic technical | 33 | 3,03% | -21,33% | +19,56% | -5,75% | +37,18% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Famiglia statistica | 58 | 67,24% | +7,91% | +17,00% | -5,34% | +36,28% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 9 | 55,56% | +8,68% | +18,19% | -5,75% | +33,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 52 | 9,62% | -12,26% | +14,04% | -6,16% | +34,21% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 29 | 0,00% | -22,84% | +21,38% | -4,58% | +42,30% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 44 | 56,82% | +8,10% | +22,93% | -4,06% | +43,66% | PESO OK | 0,0 | MEDIA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 6 | 66,67% | +12,49% | +24,97% | -2,74% | +43,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 37 | 8,11% | -22,17% | +23,07% | -4,85% | +42,31% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 1g | BREVE | Classic technical | 59 | 44,07% | -0,09% | +0,51% | -0,48% | +1,43% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 90 | 53,33% | +0,40% | +0,15% | -0,71% | +1,00% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 88 | 46,59% | -0,08% | +0,14% | -0,76% | +0,98% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 59 | 47,46% | +0,15% | +0,60% | -0,64% | +1,71% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 89 | 50,56% | +0,63% | +0,45% | -0,85% | +1,41% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 87 | 43,68% | -0,04% | +0,28% | -0,83% | +1,41% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 59 | 45,76% | +0,08% | +0,61% | -2,23% | +3,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 88 | 51,14% | +1,13% | +0,80% | -2,37% | +3,35% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 86 | 45,35% | -0,33% | +0,43% | -2,39% | +2,95% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 59 | 47,46% | -0,02% | +0,71% | -3,27% | +4,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 86 | 53,49% | +1,85% | +1,48% | -3,43% | +5,27% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 84 | 45,24% | -0,76% | +1,11% | -3,48% | +4,75% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 59 | 42,37% | -0,27% | +0,39% | -4,06% | +5,04% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 85 | 60,00% | +3,02% | +2,27% | -4,07% | +6,77% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 83 | 40,96% | -1,66% | +1,37% | -4,16% | +5,95% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 58 | 43,10% | -0,65% | +0,03% | -5,05% | +5,72% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 82 | 67,07% | +5,43% | +3,64% | -4,75% | +8,61% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 80 | 42,50% | -2,26% | +2,12% | -4,91% | +7,35% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 57 | 40,35% | -0,90% | +0,64% | -6,17% | +7,09% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 78 | 79,49% | +8,98% | +6,14% | -5,31% | +12,13% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 76 | 36,84% | -3,67% | +3,84% | -5,64% | +10,17% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 51 | 52,94% | -2,36% | +7,49% | -6,11% | +14,15% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 71 | 83,10% | +14,32% | +12,56% | -5,14% | +19,03% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 69 | 47,83% | -5,68% | +9,87% | -5,66% | +16,58% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Classic technical | 44 | 52,27% | -4,39% | +21,12% | -4,75% | +27,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 65 | 89,23% | +18,25% | +20,63% | -4,36% | +28,42% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 62 | 43,55% | -7,64% | +19,66% | -4,78% | +26,37% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 45g | MEDIO | Classic technical | 40 | 42,50% | -15,16% | +25,59% | -4,57% | +37,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 45g | MEDIO | Famiglia statistica | 54 | 75,93% | +19,32% | +31,43% | -4,25% | +41,56% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +28,91% | +28,91% | -3,55% | +37,55% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 56 | 37,50% | -19,58% | +30,54% | -4,62% | +40,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 25 | 16,00% | -42,43% | +47,84% | -3,75% | +56,65% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 39 | 71,79% | +29,82% | +46,02% | -3,60% | +57,58% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 3 | 100,00% | +37,00% | +37,00% | -3,34% | +49,68% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 41 | 19,51% | -34,83% | +44,74% | -4,14% | +55,78% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 87 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 95 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 108 | 39,81% | -0,25% |
| BTC | BREVE | Famiglia statistica | 279 | 50,90% | +0,53% |
| BTC | BREVE | Microstruttura exchange | 27 | 37,04% | -0,30% |
| BTC | BREVE | Tecnico | 264 | 45,83% | +0,02% |
| BTC | SETTIMANALE | Classic technical | 107 | 35,51% | -3,27% |
| BTC | SETTIMANALE | Famiglia statistica | 265 | 58,11% | +2,29% |
| BTC | SETTIMANALE | Microstruttura exchange | 27 | 22,22% | -1,65% |
| BTC | SETTIMANALE | Tecnico | 250 | 43,20% | -0,71% |
| BTC | SWING | Classic technical | 63 | 31,75% | -4,48% |
| BTC | SWING | Famiglia statistica | 158 | 68,99% | +5,95% |
| BTC | SWING | Microstruttura exchange | 15 | 46,67% | -0,24% |
| BTC | SWING | Tecnico | 147 | 51,70% | +1,02% |
| BTC | MEDIO | Classic technical | 64 | 56,25% | -6,10% |
| BTC | MEDIO | Famiglia statistica | 173 | 96,53% | +18,04% |
| BTC | MEDIO | Microstruttura exchange | 13 | 92,31% | +7,58% |
| BTC | MEDIO | Tecnico | 156 | 57,69% | -1,47% |
| DOGE | BREVE | Classic technical | 165 | 40,61% | -1,02% |
| DOGE | BREVE | Famiglia statistica | 282 | 56,74% | +0,67% |
| DOGE | BREVE | Microstruttura exchange | 37 | 48,65% | +1,97% |
| DOGE | BREVE | Tecnico | 264 | 50,38% | +0,14% |
| DOGE | SETTIMANALE | Classic technical | 152 | 38,16% | -4,59% |
| DOGE | SETTIMANALE | Famiglia statistica | 268 | 53,73% | +1,48% |
| DOGE | SETTIMANALE | Microstruttura exchange | 34 | 44,12% | +1,11% |
| DOGE | SETTIMANALE | Tecnico | 250 | 49,60% | -0,95% |
| DOGE | SWING | Classic technical | 88 | 40,91% | -6,48% |
| DOGE | SWING | Famiglia statistica | 159 | 64,78% | +4,81% |
| DOGE | SWING | Microstruttura exchange | 22 | 54,55% | +0,99% |
| DOGE | SWING | Tecnico | 147 | 46,94% | -2,94% |
| DOGE | MEDIO | Classic technical | 103 | 20,39% | -15,89% |
| DOGE | MEDIO | Famiglia statistica | 171 | 65,50% | +7,58% |
| DOGE | MEDIO | Microstruttura exchange | 26 | 65,38% | +9,38% |
| DOGE | MEDIO | Tecnico | 152 | 28,95% | -10,66% |
| SOL | BREVE | Classic technical | 177 | 45,76% | +0,05% |
| SOL | BREVE | Famiglia statistica | 267 | 51,69% | +0,72% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 261 | 45,21% | -0,15% |
| SOL | SETTIMANALE | Classic technical | 176 | 44,32% | -0,31% |
| SOL | SETTIMANALE | Famiglia statistica | 253 | 60,08% | +3,40% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 247 | 42,91% | -1,54% |
| SOL | SWING | Classic technical | 108 | 46,30% | -1,59% |
| SOL | SWING | Famiglia statistica | 149 | 81,21% | +11,52% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 145 | 42,07% | -4,63% |
| SOL | MEDIO | Classic technical | 109 | 40,37% | -17,07% |
| SOL | MEDIO | Famiglia statistica | 158 | 80,38% | +21,47% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 13 | 100,00% | +28,02% |
| SOL | MEDIO | Tecnico | 159 | 35,22% | -18,86% |

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
