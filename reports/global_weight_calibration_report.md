# Calibrazione pesi Global Confluence

Generato: 2026-10-24 05:34 UTC

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
| BTC | 99 | UTILE | 96 | 30 | 19 | 0 | Famiglia statistica | 1g | 47,92% | +0,23% | campione utile, valutare con prudenza |
| SOL | 99 | UTILE | 92 | 32 | 18 | 0 | Famiglia statistica | 1g | 52,17% | +0,36% | campione utile, valutare con prudenza |
| DOGE | 99 | UTILE | 97 | 33 | 19 | 0 | Famiglia statistica | 1g | 56,70% | +0,40% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 36 | 41,67% | -0,06% | +0,55% | -0,27% | +1,09% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 96 | 47,92% | +0,23% | +0,17% | -0,35% | +0,68% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 91 | 50,55% | +0,10% | +0,19% | -0,31% | +0,71% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 36 | 41,67% | -0,13% | +0,85% | -0,05% | +1,59% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 95 | 51,58% | +0,47% | +0,40% | -0,32% | +1,08% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 90 | 48,89% | +0,12% | +0,38% | -0,25% | +1,06% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 36 | 36,11% | -0,55% | +1,29% | -1,13% | +3,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Famiglia statistica | 94 | 50,00% | +0,76% | +0,69% | -1,36% | +2,41% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 89 | 40,45% | -0,06% | +0,70% | -1,30% | +2,43% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 36 | 36,11% | -2,16% | +2,85% | -1,73% | +5,27% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 92 | 48,91% | +1,46% | +1,36% | -1,97% | +3,72% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 87 | 43,68% | -0,58% | +1,22% | -1,94% | +3,66% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 36 | 33,33% | -3,63% | +4,03% | -2,13% | +7,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 90 | 57,78% | +2,19% | +2,03% | -2,33% | +4,75% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 85 | 43,53% | -0,97% | +1,97% | -2,31% | +4,69% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 35 | 37,14% | -4,05% | +4,12% | -2,39% | +7,77% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 88 | 65,91% | +3,03% | +2,66% | -2,68% | +5,77% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 9 | 33,33% | -1,34% | -1,34% | -4,20% | +1,67% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 83 | 45,78% | -0,44% | +2,60% | -2,70% | +5,77% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 34 | 20,59% | -4,14% | +3,74% | -2,59% | +8,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Famiglia statistica | 84 | 63,10% | +4,38% | +3,94% | -2,93% | +7,71% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 8 | 37,50% | -0,75% | -0,75% | -4,66% | +2,55% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 79 | 50,63% | +0,89% | +3,96% | -2,96% | +7,80% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 31 | 41,94% | -4,90% | +7,71% | -2,68% | +11,76% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 21g | SWING | Famiglia statistica | 78 | 75,64% | +7,37% | +7,04% | -3,10% | +11,15% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 8 | 50,00% | -0,41% | -0,41% | -5,42% | +4,34% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 72 | 50,00% | +0,91% | +7,24% | -3,11% | +11,39% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 29 | 55,17% | -2,82% | +11,81% | -2,66% | +16,49% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 71 | 90,14% | +11,51% | +11,51% | -3,01% | +15,94% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Microstruttura exchange | 7 | 71,43% | +2,81% | +2,81% | -5,71% | +6,60% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 64 | 64,06% | +1,13% | +11,54% | -2,99% | +16,06% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Classic technical | 24 | 66,67% | -4,17% | +13,92% | -2,62% | +19,88% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 61 | 100,00% | +18,72% | +18,72% | -2,94% | +23,73% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +7,72% | +7,72% | -5,13% | +13,34% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 56 | 60,71% | -1,10% | +18,51% | -2,81% | +23,59% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 14 | 35,71% | -14,90% | +21,98% | -1,16% | +28,42% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 46 | 97,83% | +25,39% | +25,39% | -2,28% | +31,16% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 60g | MEDIO | Microstruttura exchange | 3 | 66,67% | +11,44% | +11,44% | -4,01% | +16,95% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 41 | 43,90% | -5,72% | +25,37% | -2,01% | +31,34% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Classic technical | 58 | 43,10% | -0,47% | -0,08% | -0,97% | +0,64% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 97 | 56,70% | +0,40% | -0,07% | -0,88% | +0,90% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 13 | 53,85% | +1,69% | +1,93% | +0,19% | +2,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 91 | 51,65% | +0,20% | -0,15% | -0,98% | +0,82% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 57 | 45,61% | -0,82% | -0,02% | -1,16% | +0,99% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 96 | 56,25% | +0,61% | -0,06% | -1,12% | +1,23% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 13 | 38,46% | +1,77% | +1,97% | +0,35% | +4,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 90 | 54,44% | +0,24% | -0,33% | -1,40% | +0,95% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 56 | 37,50% | -1,50% | +0,15% | -2,80% | +3,35% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 95 | 54,74% | +0,85% | +0,03% | -2,78% | +3,24% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 13 | 46,15% | +1,64% | +1,80% | -1,90% | +5,55% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 89 | 47,19% | +0,10% | -0,52% | -3,01% | +2,65% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 54 | 42,59% | -3,33% | +0,96% | -4,10% | +5,91% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 93 | 50,54% | +1,17% | +0,45% | -4,07% | +5,37% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 12 | 33,33% | +1,81% | +1,94% | -2,90% | +8,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 87 | 54,02% | -0,48% | -0,27% | -4,43% | +4,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 52 | 36,54% | -4,60% | +1,70% | -4,94% | +7,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 91 | 54,95% | +1,40% | +0,90% | -4,91% | +7,03% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 12 | 41,67% | +0,47% | +0,56% | -3,35% | +8,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 85 | 48,24% | -0,72% | -0,00% | -5,35% | +6,14% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 50 | 38,00% | -5,38% | +2,12% | -5,84% | +9,64% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 89 | 53,93% | +1,61% | +0,93% | -5,87% | +8,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 83 | 48,19% | -1,41% | -0,27% | -6,40% | +7,37% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 47 | 42,55% | -4,77% | +3,28% | -6,21% | +12,13% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 85 | 65,88% | +3,94% | +2,01% | -6,75% | +11,79% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 11 | 45,45% | +2,03% | +5,60% | -4,35% | +14,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 79 | 45,57% | -2,12% | +0,14% | -7,37% | +9,50% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 44 | 40,91% | -7,88% | +4,63% | -6,37% | +15,31% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 78 | 62,82% | +5,73% | +5,60% | -6,93% | +17,51% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 11 | 63,64% | -0,04% | +4,84% | -5,47% | +18,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 72 | 48,61% | -3,92% | +3,65% | -7,64% | +14,89% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Classic technical | 42 | 47,62% | -6,97% | +7,56% | -6,17% | +22,27% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 70 | 70,00% | +7,18% | +9,98% | -6,00% | +25,43% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 11 | 72,73% | +8,26% | +14,01% | -6,83% | +27,95% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 64 | 56,25% | -2,88% | +8,53% | -6,73% | +23,41% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 45g | MEDIO | Classic technical | 34 | 2,94% | -21,04% | +18,65% | -6,03% | +36,58% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Famiglia statistica | 60 | 68,33% | +8,06% | +16,03% | -5,67% | +35,64% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 9 | 55,56% | +8,68% | +18,19% | -5,75% | +33,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 54 | 9,26% | -12,26% | +13,07% | -6,50% | +33,57% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 31 | 0,00% | -22,30% | +19,07% | -5,41% | +40,47% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Famiglia statistica | 46 | 54,35% | +7,12% | +21,31% | -4,64% | +42,37% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 7 | 57,14% | +8,85% | +19,54% | -4,76% | +39,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 39 | 7,69% | -21,78% | +21,15% | -5,50% | +40,85% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 1g | BREVE | Classic technical | 59 | 44,07% | -0,09% | +0,51% | -0,48% | +1,43% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 92 | 52,17% | +0,36% | +0,12% | -0,73% | +0,96% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 90 | 46,67% | -0,09% | +0,11% | -0,79% | +0,93% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 59 | 47,46% | +0,15% | +0,60% | -0,64% | +1,71% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 91 | 49,45% | +0,57% | +0,39% | -0,89% | +1,34% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 89 | 44,94% | +0,00% | +0,23% | -0,87% | +1,34% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 59 | 45,76% | +0,08% | +0,61% | -2,23% | +3,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 90 | 50,00% | +1,06% | +0,74% | -2,37% | +3,34% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 88 | 46,59% | -0,27% | +0,37% | -2,39% | +2,95% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 59 | 47,46% | -0,02% | +0,71% | -3,27% | +4,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 88 | 53,41% | +1,78% | +1,42% | -3,39% | +5,25% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 86 | 45,35% | -0,71% | +1,05% | -3,44% | +4,75% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 59 | 42,37% | -0,27% | +0,39% | -4,06% | +5,04% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 86 | 59,30% | +2,96% | +2,23% | -4,08% | +6,73% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 84 | 41,67% | -1,62% | +1,34% | -4,17% | +5,91% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 58 | 43,10% | -0,65% | +0,03% | -5,05% | +5,72% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 84 | 65,48% | +5,20% | +3,46% | -4,79% | +8,43% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 82 | 43,90% | -2,10% | +1,97% | -4,96% | +7,20% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 58 | 39,66% | -1,01% | +0,50% | -6,22% | +7,02% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 80 | 77,50% | +8,60% | +5,82% | -5,39% | +11,89% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 78 | 37,18% | -3,60% | +3,58% | -5,72% | +9,97% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 53 | 50,94% | -2,82% | +6,66% | -6,51% | +13,66% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 73 | 83,56% | +14,32% | +11,82% | -5,46% | +18,54% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 71 | 46,48% | -5,93% | +9,19% | -5,97% | +16,14% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Classic technical | 45 | 51,11% | -4,56% | +20,38% | -4,99% | +26,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 66 | 87,88% | +17,78% | +20,13% | -4,53% | +28,06% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 63 | 42,86% | -7,71% | +19,15% | -4,95% | +26,03% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 45g | MEDIO | Classic technical | 42 | 42,86% | -14,46% | +24,35% | -4,70% | +36,72% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 45g | MEDIO | Famiglia statistica | 56 | 75,00% | +18,61% | +30,29% | -4,36% | +40,79% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +28,91% | +28,91% | -3,55% | +37,55% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 58 | 37,93% | -18,92% | +29,47% | -4,71% | +39,98% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 27 | 18,52% | -38,88% | +44,71% | -3,68% | +54,48% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 41 | 70,73% | +28,63% | +44,05% | -3,56% | +56,11% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 4 | 75,00% | +27,69% | +27,69% | -4,25% | +42,68% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 43 | 20,93% | -32,95% | +42,92% | -4,07% | +54,45% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 89 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 97 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 108 | 39,81% | -0,25% |
| BTC | BREVE | Famiglia statistica | 285 | 49,82% | +0,48% |
| BTC | BREVE | Microstruttura exchange | 27 | 37,04% | -0,30% |
| BTC | BREVE | Tecnico | 270 | 46,67% | +0,05% |
| BTC | SETTIMANALE | Classic technical | 107 | 35,51% | -3,27% |
| BTC | SETTIMANALE | Famiglia statistica | 270 | 57,41% | +2,22% |
| BTC | SETTIMANALE | Microstruttura exchange | 27 | 22,22% | -1,65% |
| BTC | SETTIMANALE | Tecnico | 255 | 44,31% | -0,67% |
| BTC | SWING | Classic technical | 65 | 30,77% | -4,50% |
| BTC | SWING | Famiglia statistica | 162 | 69,14% | +5,82% |
| BTC | SWING | Microstruttura exchange | 16 | 43,75% | -0,58% |
| BTC | SWING | Tecnico | 151 | 50,33% | +0,90% |
| BTC | MEDIO | Classic technical | 67 | 55,22% | -5,83% |
| BTC | MEDIO | Famiglia statistica | 178 | 95,51% | +17,56% |
| BTC | MEDIO | Microstruttura exchange | 15 | 80,00% | +6,17% |
| BTC | MEDIO | Tecnico | 161 | 57,76% | -1,39% |
| DOGE | BREVE | Classic technical | 171 | 42,11% | -0,93% |
| DOGE | BREVE | Famiglia statistica | 288 | 55,90% | +0,62% |
| DOGE | BREVE | Microstruttura exchange | 39 | 46,15% | +1,70% |
| DOGE | BREVE | Tecnico | 270 | 51,11% | +0,18% |
| DOGE | SETTIMANALE | Classic technical | 156 | 39,10% | -4,41% |
| DOGE | SETTIMANALE | Famiglia statistica | 273 | 53,11% | +1,39% |
| DOGE | SETTIMANALE | Microstruttura exchange | 35 | 42,86% | +1,00% |
| DOGE | SETTIMANALE | Tecnico | 255 | 50,20% | -0,86% |
| DOGE | SWING | Classic technical | 91 | 41,76% | -6,28% |
| DOGE | SWING | Famiglia statistica | 163 | 64,42% | +4,80% |
| DOGE | SWING | Microstruttura exchange | 22 | 54,55% | +0,99% |
| DOGE | SWING | Tecnico | 151 | 47,02% | -2,98% |
| DOGE | MEDIO | Classic technical | 107 | 19,63% | -15,88% |
| DOGE | MEDIO | Famiglia statistica | 176 | 65,34% | +7,46% |
| DOGE | MEDIO | Microstruttura exchange | 27 | 62,96% | +8,55% |
| DOGE | MEDIO | Tecnico | 157 | 28,03% | -10,80% |
| SOL | BREVE | Classic technical | 177 | 45,76% | +0,05% |
| SOL | BREVE | Famiglia statistica | 273 | 50,55% | +0,66% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 267 | 46,07% | -0,12% |
| SOL | SETTIMANALE | Classic technical | 176 | 44,32% | -0,31% |
| SOL | SETTIMANALE | Famiglia statistica | 258 | 59,30% | +3,29% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 252 | 43,65% | -1,47% |
| SOL | SWING | Classic technical | 111 | 45,05% | -1,87% |
| SOL | SWING | Famiglia statistica | 153 | 80,39% | +11,33% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 149 | 41,61% | -4,71% |
| SOL | MEDIO | Classic technical | 114 | 40,35% | -16,34% |
| SOL | MEDIO | Famiglia statistica | 163 | 79,14% | +20,80% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 14 | 92,86% | +26,00% |
| SOL | MEDIO | Tecnico | 164 | 35,37% | -18,30% |

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
