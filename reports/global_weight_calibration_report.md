# Calibrazione pesi Global Confluence

Generato: 2026-09-27 05:32 UTC

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
| BTC | 74 | UTILE | 73 | 19 | 14 | 0 | Famiglia statistica | 1g | 52,05% | +0,33% | campione utile, valutare con prudenza |
| SOL | 74 | UTILE | 68 | 29 | 14 | 0 | Famiglia statistica | 1g | 54,41% | +0,45% | campione utile, valutare con prudenza |
| DOGE | 74 | UTILE | 72 | 29 | 13 | 0 | Famiglia statistica | 1g | 58,33% | +0,47% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 29 | 37,93% | +0,06% | +0,73% | -0,13% | +1,26% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 73 | 52,05% | +0,33% | +0,35% | -0,18% | +0,85% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 7 | 42,86% | -0,24% | -0,24% | -0,87% | +0,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 66 | 40,91% | +0,05% | +0,36% | -0,11% | +0,86% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 29 | 41,38% | +0,02% | +1,20% | +0,19% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 72 | 52,78% | +0,70% | +0,70% | -0,05% | +1,39% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 7 | 28,57% | -0,04% | -0,04% | -0,90% | +1,02% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 65 | 43,08% | +0,02% | +0,65% | +0,06% | +1,34% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 29 | 37,93% | -0,51% | +1,95% | -0,85% | +3,41% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 71 | 52,11% | +1,05% | +1,05% | -1,18% | +2,73% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 64 | 35,94% | -0,21% | +1,11% | -1,10% | +2,79% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 28 | 42,86% | -2,17% | +4,36% | -1,11% | +6,49% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 70 | 50,00% | +2,02% | +2,02% | -1,73% | +4,40% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 6 | 16,67% | -0,95% | -0,95% | -2,27% | +2,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 63 | 41,27% | -0,74% | +1,95% | -1,65% | +4,39% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 28 | 39,29% | -4,00% | +5,77% | -1,37% | +8,77% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 69 | 59,42% | +2,88% | +2,88% | -2,04% | +5,62% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 62 | 43,55% | -1,13% | +2,98% | -1,96% | +5,69% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 28 | 42,86% | -4,46% | +5,84% | -1,59% | +9,49% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 69 | 65,22% | +3,74% | +3,74% | -2,35% | +6,82% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 62 | 50,00% | -0,37% | +3,92% | -2,28% | +7,01% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 24 | 29,17% | -3,41% | +4,78% | -1,84% | +9,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 65 | 60,00% | +4,97% | +4,97% | -2,63% | +8,57% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 60 | 56,67% | +1,45% | +5,49% | -2,48% | +9,14% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 24 | 54,17% | -4,04% | +8,85% | -2,32% | +12,73% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 58 | 74,14% | +8,27% | +8,27% | -2,70% | +12,17% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 53 | 50,94% | +0,31% | +8,90% | -2,53% | +12,86% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 17 | 52,94% | -5,99% | +15,73% | -1,89% | +20,13% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 49 | 89,80% | +13,99% | +13,99% | -2,47% | +18,21% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 3 | 100,00% | +5,40% | +5,40% | -4,01% | +8,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 44 | 52,27% | -1,01% | +14,13% | -2,24% | +18,60% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 4 | 0,00% | -21,70% | +21,70% | -1,55% | +30,01% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 34 | 100,00% | +23,88% | +23,88% | -3,00% | +28,48% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 29 | 41,38% | -2,10% | +24,37% | -2,74% | +29,02% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Classic technical | 2 | 0,00% | -32,21% | +32,21% | -2,23% | +37,27% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 21 | 100,00% | +25,40% | +25,40% | -3,24% | +30,62% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 17 | 29,41% | -12,13% | +25,58% | -2,88% | +31,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 43 | 39,53% | -0,68% | +0,09% | -0,78% | +0,85% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 72 | 58,33% | +0,47% | +0,20% | -0,61% | +1,13% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 11 | 63,64% | +2,53% | +2,82% | +0,75% | +3,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 66 | 50,00% | +0,18% | +0,12% | -0,73% | +1,03% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 43 | 41,86% | -1,35% | +0,42% | -0,82% | +1,40% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 71 | 59,15% | +0,76% | +0,46% | -0,65% | +1,72% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 11 | 45,45% | +2,65% | +2,89% | +1,08% | +5,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 65 | 52,31% | +0,19% | +0,13% | -1,01% | +1,37% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 42 | 30,95% | -2,27% | +0,84% | -2,52% | +4,00% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 70 | 54,29% | +0,98% | +0,88% | -2,27% | +3,82% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 11 | 54,55% | +2,62% | +2,81% | -1,35% | +6,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 64 | 45,31% | +0,11% | +0,18% | -2,54% | +3,05% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 41 | 34,15% | -4,70% | +2,58% | -3,39% | +7,30% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 69 | 50,72% | +1,20% | +2,03% | -3,12% | +6,61% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 11 | 36,36% | +2,02% | +2,17% | -2,50% | +9,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 63 | 52,38% | -0,47% | +1,18% | -3,53% | +5,81% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 41 | 29,27% | -6,44% | +3,84% | -3,92% | +9,49% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 68 | 52,94% | +1,23% | +3,05% | -3,64% | +8,82% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 10 | 50,00% | +1,40% | +1,51% | -2,60% | +9,95% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 62 | 48,39% | -0,78% | +2,03% | -4,13% | +7,77% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 41 | 31,71% | -7,07% | +4,20% | -4,70% | +11,63% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 68 | 48,53% | +0,88% | +3,66% | -4,30% | +10,86% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 10 | 60,00% | +0,96% | +1,26% | -3,68% | +10,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 62 | 51,61% | -1,27% | +2,31% | -4,85% | +9,30% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 37 | 45,95% | -4,10% | +4,39% | -5,44% | +12,23% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 64 | 64,06% | +3,68% | +4,72% | -4,98% | +13,33% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 9 | 44,44% | +1,04% | +5,41% | -4,48% | +13,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 58 | 55,17% | +0,15% | +2,45% | -5,64% | +10,37% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 32 | 50,00% | -6,82% | +5,16% | -5,06% | +14,16% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 57 | 68,42% | +6,85% | +8,65% | -4,78% | +18,92% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 9 | 66,67% | +0,57% | +6,54% | -4,75% | +18,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 51 | 62,75% | -0,76% | +6,26% | -5,53% | +15,38% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 31 | 48,39% | -8,72% | +10,82% | -5,10% | +22,58% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 48 | 87,50% | +11,56% | +13,45% | -4,59% | +27,05% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 7 | 85,71% | +14,05% | +23,10% | -3,96% | +33,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 42 | 54,76% | -5,50% | +11,75% | -5,49% | +24,21% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 22 | 0,00% | -22,71% | +22,71% | -4,86% | +39,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 34 | 52,94% | +4,89% | +23,50% | -4,36% | +41,00% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,91% | +37,31% | -1,31% | +47,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 30 | 0,00% | -21,64% | +21,64% | -4,76% | +40,02% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 17 | 0,00% | -23,40% | +23,40% | -5,74% | +40,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 21 | 23,81% | -6,57% | +24,51% | -5,88% | +40,79% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 21 | 0,00% | -24,51% | +24,51% | -5,88% | +40,79% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 47 | 48,94% | +0,12% | +0,72% | -0,36% | +1,63% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 68 | 54,41% | +0,45% | +0,42% | -0,43% | +1,27% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 65 | 47,69% | +0,01% | +0,44% | -0,48% | +1,26% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 46 | 50,00% | +0,47% | +0,99% | -0,33% | +2,00% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 67 | 47,76% | +0,71% | +1,04% | -0,37% | +1,90% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 64 | 42,19% | -0,01% | +0,83% | -0,32% | +1,94% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 45 | 53,33% | +0,71% | +1,35% | -1,84% | +3,57% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 66 | 50,00% | +1,28% | +1,73% | -1,88% | +4,08% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 63 | 47,62% | -0,14% | +1,27% | -1,90% | +3,57% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 44 | 54,55% | +1,00% | +1,87% | -2,54% | +5,12% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 65 | 53,85% | +2,17% | +3,01% | -2,55% | +6,48% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 62 | 46,77% | -0,51% | +2,58% | -2,61% | +5,87% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 43 | 46,51% | +0,96% | +1,74% | -3,13% | +5,86% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 64 | 59,38% | +3,35% | +4,34% | -3,01% | +8,34% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 61 | 39,34% | -1,45% | +3,24% | -3,12% | +7,34% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 43 | 53,49% | +1,15% | +2,06% | -3,69% | +6,79% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 64 | 64,06% | +5,66% | +6,37% | -3,41% | +10,47% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 61 | 47,54% | -1,59% | +4,62% | -3,59% | +8,98% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 42 | 52,38% | +2,18% | +3,36% | -4,30% | +8,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 60 | 75,00% | +8,16% | +8,84% | -3,87% | +13,61% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 60 | 45,00% | -2,12% | +6,76% | -4,07% | +11,88% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 39 | 61,54% | -1,37% | +10,67% | -4,45% | +15,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 53 | 81,13% | +14,66% | +14,71% | -4,04% | +20,24% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 55 | 50,91% | -6,54% | +12,38% | -4,39% | +17,90% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 30 | 36,67% | -11,83% | +25,32% | -3,81% | +30,55% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 44 | 86,36% | +21,94% | +25,45% | -3,66% | +31,86% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 46 | 28,26% | -14,12% | +22,51% | -4,13% | +28,54% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 21 | 0,00% | -38,81% | +38,81% | -4,64% | +48,52% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 30 | 73,33% | +23,72% | +39,51% | -4,89% | +47,41% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,56% | +44,56% | -5,94% | +49,24% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 32 | 12,50% | -31,73% | +37,88% | -5,31% | +46,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 13 | 0,00% | -48,10% | +48,10% | -6,31% | +54,40% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 17 | 52,94% | +12,20% | +44,29% | -7,13% | +51,09% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +41,93% | +41,93% | -9,62% | +45,82% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 21 | 19,05% | -29,95% | +42,86% | -7,08% | +50,18% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 69 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 73 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 87 | 39,08% | -0,14% |
| BTC | BREVE | Famiglia statistica | 216 | 52,31% | +0,69% |
| BTC | BREVE | Microstruttura exchange | 21 | 33,33% | -0,22% |
| BTC | BREVE | Tecnico | 195 | 40,00% | -0,05% |
| BTC | SETTIMANALE | Classic technical | 84 | 41,67% | -3,55% |
| BTC | SETTIMANALE | Famiglia statistica | 208 | 58,17% | +2,88% |
| BTC | SETTIMANALE | Microstruttura exchange | 16 | 31,25% | -1,22% |
| BTC | SETTIMANALE | Tecnico | 187 | 44,92% | -0,75% |
| BTC | SWING | Classic technical | 48 | 41,67% | -3,73% |
| BTC | SWING | Famiglia statistica | 123 | 66,67% | +6,53% |
| BTC | SWING | Microstruttura exchange | 10 | 60,00% | +0,93% |
| BTC | SWING | Tecnico | 113 | 53,98% | +0,92% |
| BTC | MEDIO | Classic technical | 23 | 39,13% | -11,01% |
| BTC | MEDIO | Famiglia statistica | 104 | 95,19% | +19,52% |
| BTC | MEDIO | Microstruttura exchange | 5 | 100,00% | +12,53% |
| BTC | MEDIO | Tecnico | 90 | 44,44% | -3,46% |
| DOGE | BREVE | Classic technical | 128 | 37,50% | -1,42% |
| DOGE | BREVE | Famiglia statistica | 213 | 57,28% | +0,73% |
| DOGE | BREVE | Microstruttura exchange | 33 | 54,55% | +2,60% |
| DOGE | BREVE | Tecnico | 195 | 49,23% | +0,16% |
| DOGE | SETTIMANALE | Classic technical | 123 | 31,71% | -6,07% |
| DOGE | SETTIMANALE | Famiglia statistica | 205 | 50,73% | +1,11% |
| DOGE | SETTIMANALE | Microstruttura exchange | 31 | 48,39% | +1,48% |
| DOGE | SETTIMANALE | Tecnico | 187 | 50,80% | -0,84% |
| DOGE | SWING | Classic technical | 69 | 47,83% | -5,36% |
| DOGE | SWING | Famiglia statistica | 121 | 66,12% | +5,17% |
| DOGE | SWING | Microstruttura exchange | 18 | 55,56% | +0,80% |
| DOGE | SWING | Tecnico | 109 | 58,72% | -0,28% |
| DOGE | MEDIO | Classic technical | 70 | 21,43% | -16,68% |
| DOGE | MEDIO | Famiglia statistica | 103 | 63,11% | +5,66% |
| DOGE | MEDIO | Microstruttura exchange | 13 | 84,62% | +19,38% |
| DOGE | MEDIO | Tecnico | 93 | 24,73% | -15,00% |
| SOL | BREVE | Classic technical | 138 | 50,72% | +0,43% |
| SOL | BREVE | Famiglia statistica | 201 | 50,75% | +0,81% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 192 | 45,83% | -0,04% |
| SOL | SETTIMANALE | Classic technical | 130 | 51,54% | +1,04% |
| SOL | SETTIMANALE | Famiglia statistica | 193 | 59,07% | +3,72% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 184 | 44,57% | -1,18% |
| SOL | SWING | Classic technical | 81 | 56,79% | +0,47% |
| SOL | SWING | Famiglia statistica | 113 | 77,88% | +11,21% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 115 | 47,83% | -4,23% |
| SOL | MEDIO | Classic technical | 64 | 17,19% | -28,05% |
| SOL | MEDIO | Famiglia statistica | 91 | 75,82% | +20,71% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 8 | 100,00% | +29,97% |
| SOL | MEDIO | Tecnico | 99 | 21,21% | -23,17% |

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
