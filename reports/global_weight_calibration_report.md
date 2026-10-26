# Calibrazione pesi Global Confluence

Generato: 2026-10-26 06:34 UTC

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
| BTC | 101 | UTILE | 98 | 30 | 19 | 0 | Famiglia statistica | 1g | 46,94% | +0,21% | campione utile, valutare con prudenza |
| SOL | 101 | UTILE | 93 | 32 | 18 | 0 | Famiglia statistica | 1g | 51,61% | +0,36% | campione utile, valutare con prudenza |
| DOGE | 101 | UTILE | 98 | 33 | 20 | 0 | Famiglia statistica | 1g | 56,12% | +0,38% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 36 | 41,67% | -0,06% | +0,55% | -0,27% | +1,09% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 1g | BREVE | Famiglia statistica | 98 | 46,94% | +0,21% | +0,16% | -0,36% | +0,67% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 10 | 40,00% | -0,38% | -0,38% | -0,95% | +0,06% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 93 | 51,61% | +0,10% | +0,18% | -0,32% | +0,69% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 36 | 41,67% | -0,13% | +0,85% | -0,05% | +1,59% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Famiglia statistica | 97 | 50,52% | +0,44% | +0,37% | -0,34% | +1,04% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,17% | -0,17% | -1,18% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 92 | 50,00% | +0,14% | +0,35% | -0,27% | +1,02% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 36 | 36,11% | -0,55% | +1,29% | -1,13% | +3,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Famiglia statistica | 96 | 48,96% | +0,69% | +0,63% | -1,39% | +2,34% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 9 | 33,33% | -0,38% | -0,38% | -1,84% | +1,32% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 91 | 41,76% | -0,00% | +0,63% | -1,33% | +2,36% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 36 | 36,11% | -2,16% | +2,85% | -1,73% | +5,27% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 94 | 47,87% | +1,38% | +1,27% | -1,99% | +3,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 9 | 11,11% | -1,54% | -1,54% | -2,63% | +1,52% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 89 | 43,82% | -0,55% | +1,14% | -1,96% | +3,64% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 36 | 33,33% | -3,63% | +4,03% | -2,13% | +7,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 92 | 56,52% | +2,09% | +1,93% | -2,34% | +4,72% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 9 | 22,22% | -2,07% | -2,07% | -3,59% | +1,60% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 87 | 43,68% | -0,93% | +1,87% | -2,32% | +4,66% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 36 | 38,89% | -3,92% | +4,00% | -2,35% | +7,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 90 | 64,44% | +2,93% | +2,56% | -2,67% | +5,73% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 9 | 33,33% | -1,34% | -1,34% | -4,20% | +1,67% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 85 | 47,06% | -0,39% | +2,50% | -2,69% | +5,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 35 | 22,86% | -3,89% | +3,50% | -2,67% | +8,17% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Famiglia statistica | 86 | 63,95% | +4,37% | +3,76% | -2,97% | +7,57% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 9 | 33,33% | -1,00% | -1,00% | -4,58% | +2,51% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 81 | 50,62% | +0,89% | +3,77% | -3,00% | +7,66% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 33 | 39,39% | -4,95% | +6,89% | -2,93% | +11,17% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 21g | SWING | Famiglia statistica | 79 | 75,95% | +7,36% | +6,87% | -3,15% | +11,03% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 8 | 50,00% | -0,41% | -0,41% | -5,42% | +4,34% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 74 | 48,65% | +0,73% | +6,88% | -3,21% | +11,14% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Classic technical | 29 | 55,17% | -2,82% | +11,81% | -2,66% | +16,49% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 73 | 89,04% | +11,20% | +11,07% | -3,07% | +15,61% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 30g | MEDIO | Microstruttura exchange | 7 | 71,43% | +2,81% | +2,81% | -5,71% | +6,60% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 66 | 62,12% | +0,96% | +11,05% | -3,06% | +15,69% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Classic technical | 24 | 66,67% | -4,17% | +13,92% | -2,62% | +19,88% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 63 | 100,00% | +18,22% | +18,22% | -2,97% | +23,37% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +7,72% | +7,72% | -5,13% | +13,34% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 58 | 62,07% | -0,95% | +17,98% | -2,84% | +23,20% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 16 | 43,75% | -12,82% | +19,45% | -1,64% | +26,22% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 48 | 97,92% | +24,40% | +24,40% | -2,39% | +30,31% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 60g | MEDIO | Microstruttura exchange | 3 | 66,67% | +11,44% | +11,44% | -4,01% | +16,95% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 43 | 46,51% | -5,37% | +24,27% | -2,15% | +30,39% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Classic technical | 60 | 45,00% | -0,43% | -0,11% | -0,99% | +0,61% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Famiglia statistica | 98 | 56,12% | +0,38% | -0,09% | -0,89% | +0,89% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 13 | 53,85% | +1,69% | +1,93% | +0,19% | +2,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 93 | 52,69% | +0,21% | -0,17% | -0,99% | +0,80% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 59 | 47,46% | -0,70% | -0,11% | -1,23% | +0,89% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 98 | 55,10% | +0,54% | -0,11% | -1,16% | +1,17% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 13 | 38,46% | +1,77% | +1,97% | +0,35% | +4,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 92 | 55,43% | +0,30% | -0,38% | -1,44% | +0,89% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 58 | 39,66% | -1,32% | +0,02% | -2,88% | +3,23% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 97 | 53,61% | +0,76% | -0,04% | -2,82% | +3,17% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 13 | 46,15% | +1,64% | +1,80% | -1,90% | +5,55% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 91 | 48,35% | +0,18% | -0,59% | -3,05% | +2,59% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 56 | 44,64% | -3,05% | +0,76% | -4,15% | +5,80% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 95 | 49,47% | +1,05% | +0,34% | -4,10% | +5,32% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 13 | 30,77% | +1,20% | +1,33% | -3,30% | +7,79% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 89 | 55,06% | -0,37% | -0,37% | -4,46% | +4,66% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 54 | 38,89% | -4,32% | +1,53% | -4,91% | +7,61% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 93 | 53,76% | +1,31% | +0,82% | -4,89% | +7,00% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 12 | 41,67% | +0,47% | +0,56% | -3,35% | +8,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 87 | 49,43% | -0,63% | -0,07% | -5,32% | +6,12% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 52 | 40,38% | -4,98% | +1,85% | -5,86% | +9,40% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 91 | 52,75% | +1,47% | +0,80% | -5,89% | +8,58% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 12 | 50,00% | +0,07% | +0,32% | -4,37% | +9,35% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 85 | 49,41% | -1,26% | -0,38% | -6,40% | +7,28% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 49 | 44,90% | -4,13% | +2,70% | -6,46% | +11,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 87 | 64,37% | +3,60% | +1,71% | -6,88% | +11,53% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 11 | 45,45% | +2,03% | +5,60% | -4,35% | +14,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 81 | 46,91% | -1,80% | -0,14% | -7,50% | +9,28% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 44 | 40,91% | -7,88% | +4,63% | -6,37% | +15,31% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 80 | 63,75% | +6,04% | +5,01% | -7,24% | +17,15% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Microstruttura exchange | 11 | 63,64% | -0,04% | +4,84% | -5,47% | +18,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 74 | 47,30% | -4,30% | +3,07% | -7,95% | +14,56% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Classic technical | 43 | 46,51% | -7,32% | +6,87% | -6,56% | +21,76% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 72 | 70,83% | +7,58% | +9,09% | -6,47% | +24,75% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 11 | 72,73% | +8,26% | +14,01% | -6,83% | +27,95% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 66 | 54,55% | -3,45% | +7,61% | -7,22% | +22,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 45g | MEDIO | Classic technical | 35 | 5,71% | -20,19% | +17,88% | -6,16% | +36,27% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Famiglia statistica | 62 | 69,35% | +8,10% | +15,20% | -5,84% | +35,26% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 9 | 55,56% | +8,68% | +18,19% | -5,75% | +33,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 56 | 12,50% | -11,48% | +12,26% | -6,66% | +33,23% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 31 | 0,00% | -22,30% | +19,07% | -5,41% | +40,47% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Famiglia statistica | 47 | 55,32% | +7,20% | +20,62% | -4,82% | +41,94% | PESO OK | 0,0 | MEDIA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 7 | 57,14% | +8,85% | +19,54% | -4,76% | +39,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 41 | 7,32% | -21,26% | +19,57% | -5,85% | +39,92% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 1g | BREVE | Classic technical | 59 | 44,07% | -0,09% | +0,51% | -0,48% | +1,43% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 93 | 51,61% | +0,36% | +0,11% | -0,73% | +0,95% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 91 | 47,25% | -0,08% | +0,09% | -0,80% | +0,92% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 59 | 47,46% | +0,15% | +0,60% | -0,64% | +1,71% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 93 | 48,39% | +0,51% | +0,34% | -0,92% | +1,28% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 90 | 44,44% | -0,02% | +0,20% | -0,89% | +1,31% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 59 | 45,76% | +0,08% | +0,61% | -2,23% | +3,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 92 | 48,91% | +0,97% | +0,65% | -2,41% | +3,25% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 90 | 46,67% | -0,27% | +0,29% | -2,43% | +2,87% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 59 | 47,46% | -0,02% | +0,71% | -3,27% | +4,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 90 | 52,22% | +1,66% | +1,30% | -3,42% | +5,19% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 88 | 46,59% | -0,61% | +0,94% | -3,47% | +4,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 59 | 42,37% | -0,27% | +0,39% | -4,06% | +5,04% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 88 | 57,95% | +2,83% | +2,11% | -4,08% | +6,67% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 86 | 43,02% | -1,51% | +1,24% | -4,17% | +5,87% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 59 | 44,07% | -0,63% | +0,02% | -4,99% | +5,74% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 86 | 63,95% | +5,02% | +3,32% | -4,77% | +8,35% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 84 | 45,24% | -1,99% | +1,86% | -4,94% | +7,15% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 58 | 39,66% | -1,01% | +0,50% | -6,22% | +7,02% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 82 | 75,61% | +8,18% | +5,47% | -5,51% | +11,61% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 80 | 38,75% | -3,29% | +3,27% | -5,83% | +9,73% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 55 | 49,09% | -3,29% | +5,84% | -6,90% | +13,21% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 75 | 84,00% | +14,36% | +11,08% | -5,77% | +18,08% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 73 | 45,21% | -6,20% | +8,50% | -6,28% | +15,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Classic technical | 47 | 48,94% | -5,07% | +18,81% | -5,53% | +25,63% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 68 | 88,24% | +17,75% | +19,05% | -4,92% | +27,32% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 65 | 41,54% | -7,98% | +18,06% | -5,34% | +25,32% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 45g | MEDIO | Classic technical | 42 | 42,86% | -14,46% | +24,35% | -4,70% | +36,72% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 45g | MEDIO | Famiglia statistica | 58 | 74,14% | +17,99% | +29,26% | -4,36% | +40,20% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 5 | 100,00% | +28,91% | +28,91% | -3,55% | +37,55% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 59 | 37,29% | -18,61% | +28,97% | -4,73% | +39,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 29 | 20,69% | -36,03% | +41,79% | -3,61% | +52,52% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 43 | 69,77% | +27,41% | +42,11% | -3,51% | +54,71% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 5 | 80,00% | +23,15% | +23,15% | -3,55% | +39,85% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 45 | 22,22% | -31,38% | +41,12% | -4,01% | +53,19% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 90 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 98 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 108 | 39,81% | -0,25% |
| BTC | BREVE | Famiglia statistica | 291 | 48,80% | +0,45% |
| BTC | BREVE | Microstruttura exchange | 28 | 35,71% | -0,31% |
| BTC | BREVE | Tecnico | 276 | 47,83% | +0,08% |
| BTC | SETTIMANALE | Classic technical | 108 | 36,11% | -3,24% |
| BTC | SETTIMANALE | Famiglia statistica | 276 | 56,16% | +2,12% |
| BTC | SETTIMANALE | Microstruttura exchange | 27 | 22,22% | -1,65% |
| BTC | SETTIMANALE | Tecnico | 261 | 44,83% | -0,62% |
| BTC | SWING | Classic technical | 68 | 30,88% | -4,41% |
| BTC | SWING | Famiglia statistica | 165 | 69,70% | +5,80% |
| BTC | SWING | Microstruttura exchange | 17 | 41,18% | -0,72% |
| BTC | SWING | Tecnico | 155 | 49,68% | +0,81% |
| BTC | MEDIO | Classic technical | 69 | 56,52% | -5,61% |
| BTC | MEDIO | Famiglia statistica | 184 | 95,11% | +17,05% |
| BTC | MEDIO | Microstruttura exchange | 15 | 80,00% | +6,17% |
| BTC | MEDIO | Tecnico | 167 | 58,08% | -1,34% |
| DOGE | BREVE | Classic technical | 177 | 44,07% | -0,81% |
| DOGE | BREVE | Famiglia statistica | 293 | 54,95% | +0,56% |
| DOGE | BREVE | Microstruttura exchange | 39 | 46,15% | +1,70% |
| DOGE | BREVE | Tecnico | 276 | 52,17% | +0,23% |
| DOGE | SETTIMANALE | Classic technical | 162 | 41,36% | -4,09% |
| DOGE | SETTIMANALE | Famiglia statistica | 279 | 51,97% | +1,27% |
| DOGE | SETTIMANALE | Microstruttura exchange | 37 | 40,54% | +0,60% |
| DOGE | SETTIMANALE | Tecnico | 261 | 51,34% | -0,75% |
| DOGE | SWING | Classic technical | 93 | 43,01% | -5,91% |
| DOGE | SWING | Famiglia statistica | 167 | 64,07% | +4,77% |
| DOGE | SWING | Microstruttura exchange | 22 | 54,55% | +0,99% |
| DOGE | SWING | Tecnico | 155 | 47,10% | -3,00% |
| DOGE | MEDIO | Classic technical | 109 | 20,18% | -15,72% |
| DOGE | MEDIO | Famiglia statistica | 181 | 66,30% | +7,66% |
| DOGE | MEDIO | Microstruttura exchange | 27 | 62,96% | +8,55% |
| DOGE | MEDIO | Tecnico | 163 | 28,22% | -10,69% |
| SOL | BREVE | Classic technical | 177 | 45,76% | +0,05% |
| SOL | BREVE | Famiglia statistica | 278 | 49,64% | +0,61% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 271 | 46,13% | -0,12% |
| SOL | SETTIMANALE | Classic technical | 177 | 44,63% | -0,31% |
| SOL | SETTIMANALE | Famiglia statistica | 264 | 57,95% | +3,14% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 258 | 44,96% | -1,36% |
| SOL | SWING | Classic technical | 113 | 44,25% | -2,12% |
| SOL | SWING | Famiglia statistica | 157 | 79,62% | +11,13% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 153 | 41,83% | -4,68% |
| SOL | MEDIO | Classic technical | 118 | 39,83% | -16,02% |
| SOL | MEDIO | Famiglia statistica | 169 | 78,70% | +20,29% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 15 | 93,33% | +24,60% |
| SOL | MEDIO | Tecnico | 169 | 34,91% | -17,92% |

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
