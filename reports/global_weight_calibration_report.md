# Calibrazione pesi Global Confluence

Generato: 2026-10-25 06:34 UTC

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
| BTC | 100 | UTILE | 97 | 30 | 19 | 0 | Famiglia statistica | 1g | 47,42% | +0,22% | campione utile, valutare con prudenza |
| SOL | 100 | UTILE | 93 | 32 | 18 | 0 | Famiglia statistica | 1g | 51,61% | +0,36% | campione utile, valutare con prudenza |
| DOGE | 100 | UTILE | 98 | 33 | 19 | 0 | Famiglia statistica | 1g | 56,12% | +0,38% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 36 | 41,67% | -0,06% | +0,55% | -0,27% | +1,09% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 97 | 47,42% | +0,22% | +0,17% | -0,35% | +0,68% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 9 | 44,44% | -0,34% | -0,34% | -0,90% | +0,11% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 92 | 51,09% | +0,10% | +0,19% | -0,31% | +0,71% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 36 | 41,67% | -0,13% | +0,85% | -0,05% | +1,59% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 96 | 51,04% | +0,46% | +0,38% | -0,33% | +1,06% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 91 | 49,45% | +0,13% | +0,36% | -0,26% | +1,04% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 36 | 36,11% | -0,55% | +1,29% | -1,13% | +3,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Famiglia statistica | 95 | 49,47% | +0,72% | +0,66% | -1,37% | +2,38% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 90 | 41,11% | -0,03% | +0,66% | -1,32% | +2,39% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 36 | 36,11% | -2,16% | +2,85% | -1,73% | +5,27% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 93 | 48,39% | +1,43% | +1,32% | -1,97% | +3,72% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 88 | 43,18% | -0,59% | +1,19% | -1,93% | +3,66% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 36 | 33,33% | -3,63% | +4,03% | -2,13% | +7,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 91 | 57,14% | +2,15% | +1,99% | -2,32% | +4,74% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 86 | 43,02% | -0,98% | +1,93% | -2,30% | +4,69% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 36 | 38,89% | -3,92% | +4,00% | -2,35% | +7,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 89 | 65,17% | +2,99% | +2,62% | -2,66% | +5,76% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 9 | 33,33% | -1,34% | -1,34% | -4,20% | +1,67% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 84 | 46,43% | -0,43% | +2,56% | -2,68% | +5,76% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 34 | 20,59% | -4,14% | +3,74% | -2,59% | +8,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Famiglia statistica | 85 | 63,53% | +4,36% | +3,86% | -2,94% | +7,65% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 9 | 33,33% | -1,00% | -1,00% | -4,58% | +2,51% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 80 | 50,00% | +0,84% | +3,87% | -2,97% | +7,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 32 | 40,62% | -4,91% | +7,31% | -2,79% | +11,47% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 21g | SWING | Famiglia statistica | 78 | 75,64% | +7,37% | +7,04% | -3,10% | +11,15% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 8 | 50,00% | -0,41% | -0,41% | -5,42% | +4,34% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 73 | 49,32% | +0,83% | +7,07% | -3,15% | +11,27% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 29 | 55,17% | -2,82% | +11,81% | -2,66% | +16,49% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 72 | 88,89% | +11,29% | +11,29% | -3,04% | +15,77% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Microstruttura exchange | 7 | 71,43% | +2,81% | +2,81% | -5,71% | +6,60% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 65 | 63,08% | +1,04% | +11,29% | -3,02% | +15,87% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Classic technical | 24 | 66,67% | -4,17% | +13,92% | -2,62% | +19,88% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 62 | 100,00% | +18,46% | +18,46% | -2,97% | +23,53% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +7,72% | +7,72% | -5,13% | +13,34% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 57 | 61,40% | -1,03% | +18,23% | -2,84% | +23,37% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 15 | 40,00% | -13,78% | +20,64% | -1,43% | +27,22% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 47 | 97,87% | +24,88% | +24,88% | -2,34% | +30,71% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 60g | MEDIO | Microstruttura exchange | 3 | 66,67% | +11,44% | +11,44% | -4,01% | +16,95% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 42 | 45,24% | -5,54% | +24,81% | -2,09% | +30,84% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Classic technical | 59 | 44,07% | -0,44% | -0,10% | -0,98% | +0,62% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 98 | 56,12% | +0,38% | -0,09% | -0,89% | +0,89% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 13 | 53,85% | +1,69% | +1,93% | +0,19% | +2,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 92 | 52,17% | +0,21% | -0,17% | -0,99% | +0,80% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 58 | 46,55% | -0,75% | -0,08% | -1,20% | +0,93% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 97 | 55,67% | +0,57% | -0,09% | -1,14% | +1,20% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 13 | 38,46% | +1,77% | +1,97% | +0,35% | +4,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 91 | 54,95% | +0,28% | -0,37% | -1,43% | +0,92% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 57 | 38,60% | -1,41% | +0,08% | -2,82% | +3,31% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 96 | 54,17% | +0,81% | -0,01% | -2,79% | +3,22% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 13 | 46,15% | +1,64% | +1,80% | -1,90% | +5,55% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 90 | 47,78% | +0,13% | -0,56% | -3,01% | +2,63% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 55 | 43,64% | -3,22% | +0,89% | -4,08% | +5,90% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 94 | 50,00% | +1,13% | +0,41% | -4,06% | +5,37% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 12 | 33,33% | +1,81% | +1,94% | -2,90% | +8,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 88 | 54,55% | -0,44% | -0,31% | -4,41% | +4,71% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 53 | 37,74% | -4,47% | +1,62% | -4,89% | +7,66% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 92 | 54,35% | +1,36% | +0,86% | -4,88% | +7,02% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 12 | 41,67% | +0,47% | +0,56% | -3,35% | +8,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 86 | 48,84% | -0,68% | -0,03% | -5,32% | +6,13% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 51 | 39,22% | -5,21% | +2,01% | -5,81% | +9,55% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 90 | 53,33% | +1,56% | +0,88% | -5,85% | +8,66% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,68% | +0,96% | -3,98% | +10,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 84 | 48,81% | -1,36% | -0,31% | -6,37% | +7,35% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 48 | 43,75% | -4,47% | +3,01% | -6,31% | +11,94% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 86 | 65,12% | +3,78% | +1,87% | -6,80% | +11,68% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 11 | 45,45% | +2,03% | +5,60% | -4,35% | +14,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 80 | 46,25% | -1,97% | +0,01% | -7,41% | +9,42% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 44 | 40,91% | -7,88% | +4,63% | -6,37% | +15,31% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 79 | 63,29% | +5,87% | +5,32% | -7,07% | +17,35% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 11 | 63,64% | -0,04% | +4,84% | -5,47% | +18,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 73 | 47,95% | -4,10% | +3,37% | -7,78% | +14,74% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Classic technical | 43 | 46,51% | -7,32% | +6,87% | -6,56% | +21,76% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 71 | 70,42% | +7,39% | +9,52% | -6,24% | +25,07% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 11 | 72,73% | +8,26% | +14,01% | -6,83% | +27,95% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 65 | 55,38% | -3,18% | +8,06% | -6,98% | +23,06% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 45g | MEDIO | Classic technical | 34 | 2,94% | -21,04% | +18,65% | -6,03% | +36,58% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Famiglia statistica | 61 | 68,85% | +8,09% | +15,59% | -5,76% | +35,42% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 9 | 55,56% | +8,68% | +18,19% | -5,75% | +33,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 55 | 10,91% | -11,85% | +12,64% | -6,58% | +33,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 31 | 0,00% | -22,30% | +19,07% | -5,41% | +40,47% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Famiglia statistica | 46 | 54,35% | +7,12% | +21,31% | -4,64% | +42,37% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 7 | 57,14% | +8,85% | +19,54% | -4,76% | +39,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 40 | 7,50% | -21,51% | +20,34% | -5,67% | +40,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 1g | BREVE | Classic technical | 59 | 44,07% | -0,09% | +0,51% | -0,48% | +1,43% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 93 | 51,61% | +0,36% | +0,11% | -0,73% | +0,95% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 90 | 46,67% | -0,09% | +0,11% | -0,79% | +0,93% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 59 | 47,46% | +0,15% | +0,60% | -0,64% | +1,71% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 92 | 48,91% | +0,53% | +0,36% | -0,91% | +1,30% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 90 | 44,44% | -0,02% | +0,20% | -0,89% | +1,31% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 59 | 45,76% | +0,08% | +0,61% | -2,23% | +3,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 91 | 49,45% | +1,02% | +0,70% | -2,38% | +3,30% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 89 | 47,19% | -0,24% | +0,33% | -2,40% | +2,92% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 59 | 47,46% | -0,02% | +0,71% | -3,27% | +4,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 89 | 52,81% | +1,73% | +1,37% | -3,38% | +5,24% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 87 | 45,98% | -0,67% | +1,01% | -3,43% | +4,74% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 59 | 42,37% | -0,27% | +0,39% | -4,06% | +5,04% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 87 | 58,62% | +2,91% | +2,19% | -4,05% | +6,71% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 85 | 42,35% | -1,58% | +1,31% | -4,14% | +5,91% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 59 | 44,07% | -0,63% | +0,02% | -4,99% | +5,74% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 85 | 64,71% | +5,14% | +3,41% | -4,75% | +8,42% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 83 | 44,58% | -2,07% | +1,94% | -4,92% | +7,20% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 58 | 39,66% | -1,01% | +0,50% | -6,22% | +7,02% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 81 | 76,54% | +8,40% | +5,67% | -5,43% | +11,79% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 79 | 37,97% | -3,46% | +3,44% | -5,76% | +9,89% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 54 | 50,00% | -3,06% | +6,24% | -6,70% | +13,42% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 74 | 83,78% | +14,34% | +11,44% | -5,61% | +18,31% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 72 | 45,83% | -6,06% | +8,84% | -6,12% | +15,93% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Classic technical | 46 | 50,00% | -4,82% | +19,57% | -5,26% | +26,11% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 67 | 88,06% | +17,77% | +19,58% | -4,72% | +27,68% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 64 | 42,19% | -7,85% | +18,60% | -5,14% | +25,66% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 45g | MEDIO | Classic technical | 42 | 42,86% | -14,46% | +24,35% | -4,70% | +36,72% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 45g | MEDIO | Famiglia statistica | 57 | 73,68% | +18,28% | +29,75% | -4,38% | +40,46% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +28,91% | +28,91% | -3,55% | +37,55% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 59 | 37,29% | -18,61% | +28,97% | -4,73% | +39,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 28 | 21,43% | -37,31% | +43,29% | -3,57% | +53,55% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 42 | 71,43% | +28,07% | +43,12% | -3,49% | +55,45% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 5 | 80,00% | +23,15% | +23,15% | -3,55% | +39,85% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 44 | 22,73% | -32,09% | +42,06% | -4,00% | +53,86% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 89 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 98 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 108 | 39,81% | -0,25% |
| BTC | BREVE | Famiglia statistica | 288 | 49,31% | +0,46% |
| BTC | BREVE | Microstruttura exchange | 27 | 37,04% | -0,30% |
| BTC | BREVE | Tecnico | 273 | 47,25% | +0,07% |
| BTC | SETTIMANALE | Classic technical | 108 | 36,11% | -3,24% |
| BTC | SETTIMANALE | Famiglia statistica | 273 | 56,78% | +2,18% |
| BTC | SETTIMANALE | Microstruttura exchange | 27 | 22,22% | -1,65% |
| BTC | SETTIMANALE | Tecnico | 258 | 44,19% | -0,67% |
| BTC | SWING | Classic technical | 66 | 30,30% | -4,51% |
| BTC | SWING | Famiglia statistica | 163 | 69,33% | +5,80% |
| BTC | SWING | Microstruttura exchange | 17 | 41,18% | -0,72% |
| BTC | SWING | Tecnico | 153 | 49,67% | +0,83% |
| BTC | MEDIO | Classic technical | 68 | 55,88% | -5,72% |
| BTC | MEDIO | Famiglia statistica | 181 | 95,03% | +17,27% |
| BTC | MEDIO | Microstruttura exchange | 15 | 80,00% | +6,17% |
| BTC | MEDIO | Tecnico | 164 | 57,93% | -1,36% |
| DOGE | BREVE | Classic technical | 174 | 43,10% | -0,86% |
| DOGE | BREVE | Famiglia statistica | 291 | 55,33% | +0,58% |
| DOGE | BREVE | Microstruttura exchange | 39 | 46,15% | +1,70% |
| DOGE | BREVE | Tecnico | 273 | 51,65% | +0,21% |
| DOGE | SETTIMANALE | Classic technical | 159 | 40,25% | -4,27% |
| DOGE | SETTIMANALE | Famiglia statistica | 276 | 52,54% | +1,34% |
| DOGE | SETTIMANALE | Microstruttura exchange | 35 | 42,86% | +1,00% |
| DOGE | SETTIMANALE | Tecnico | 258 | 50,78% | -0,82% |
| DOGE | SWING | Classic technical | 92 | 42,39% | -6,10% |
| DOGE | SWING | Famiglia statistica | 165 | 64,24% | +4,78% |
| DOGE | SWING | Microstruttura exchange | 22 | 54,55% | +0,99% |
| DOGE | SWING | Tecnico | 153 | 47,06% | -2,99% |
| DOGE | MEDIO | Classic technical | 108 | 19,44% | -15,94% |
| DOGE | MEDIO | Famiglia statistica | 178 | 65,73% | +7,56% |
| DOGE | MEDIO | Microstruttura exchange | 27 | 62,96% | +8,55% |
| DOGE | MEDIO | Tecnico | 160 | 28,12% | -10,74% |
| SOL | BREVE | Classic technical | 177 | 45,76% | +0,05% |
| SOL | BREVE | Famiglia statistica | 276 | 50,00% | +0,63% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 269 | 46,10% | -0,12% |
| SOL | SETTIMANALE | Classic technical | 177 | 44,63% | -0,31% |
| SOL | SETTIMANALE | Famiglia statistica | 261 | 58,62% | +3,23% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 255 | 44,31% | -1,43% |
| SOL | SWING | Classic technical | 112 | 44,64% | -2,00% |
| SOL | SWING | Famiglia statistica | 155 | 80,00% | +11,24% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 151 | 41,72% | -4,70% |
| SOL | MEDIO | Classic technical | 116 | 40,52% | -16,16% |
| SOL | MEDIO | Famiglia statistica | 166 | 78,92% | +20,55% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 15 | 93,33% | +24,60% |
| SOL | MEDIO | Tecnico | 167 | 35,33% | -18,04% |

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
