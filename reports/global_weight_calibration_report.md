# Calibrazione pesi Global Confluence

Generato: 2026-09-29 05:33 UTC

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
| BTC | 76 | UTILE | 75 | 20 | 15 | 0 | Famiglia statistica | 1g | 52,00% | +0,34% | campione utile, valutare con prudenza |
| SOL | 76 | UTILE | 69 | 29 | 14 | 0 | Famiglia statistica | 1g | 55,07% | +0,46% | campione utile, valutare con prudenza |
| DOGE | 76 | UTILE | 74 | 29 | 14 | 0 | Famiglia statistica | 1g | 58,11% | +0,49% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 29 | 37,93% | +0,06% | +0,73% | -0,13% | +1,26% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 75 | 52,00% | +0,34% | +0,32% | -0,20% | +0,85% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 7 | 42,86% | -0,24% | -0,24% | -0,87% | +0,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 68 | 41,18% | +0,02% | +0,32% | -0,14% | +0,86% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 29 | 41,38% | +0,02% | +1,20% | +0,19% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 74 | 54,05% | +0,72% | +0,65% | -0,09% | +1,35% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 7 | 28,57% | -0,04% | -0,04% | -0,90% | +1,02% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 67 | 41,79% | -0,02% | +0,59% | +0,02% | +1,30% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 29 | 37,93% | -0,51% | +1,95% | -0,85% | +3,41% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 73 | 52,05% | +1,02% | +0,99% | -1,18% | +2,69% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 7 | 28,57% | -0,39% | -0,39% | -1,79% | +1,42% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 66 | 34,85% | -0,23% | +1,04% | -1,10% | +2,74% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 29 | 41,38% | -2,25% | +4,06% | -1,22% | +6,21% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 71 | 49,30% | +1,93% | +1,93% | -1,77% | +4,31% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 7 | 14,29% | -1,43% | -1,43% | -2,57% | +1,68% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 64 | 40,62% | -0,79% | +1,85% | -1,69% | +4,29% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Classic technical | 28 | 39,29% | -4,00% | +5,77% | -1,37% | +8,77% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 70 | 58,57% | +2,80% | +2,80% | -2,05% | +5,58% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 6 | 33,33% | -1,39% | -1,39% | -2,98% | +2,35% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 63 | 42,86% | -1,15% | +2,90% | -1,97% | +5,64% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Classic technical | 28 | 42,86% | -4,46% | +5,84% | -1,59% | +9,49% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 69 | 65,22% | +3,74% | +3,74% | -2,35% | +6,82% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 62 | 50,00% | -0,37% | +3,92% | -2,28% | +7,01% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Classic technical | 26 | 26,92% | -3,71% | +4,97% | -1,95% | +9,52% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 67 | 61,19% | +5,04% | +5,04% | -2,65% | +8,69% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 14g | SWING | Microstruttura exchange | 5 | 40,00% | +0,29% | +0,29% | -4,46% | +3,38% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 62 | 58,06% | +1,64% | +5,55% | -2,50% | +9,26% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 21g | SWING | Classic technical | 24 | 54,17% | -4,04% | +8,85% | -2,32% | +12,73% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 60 | 75,00% | +8,16% | +8,16% | -2,79% | +12,10% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| BTC | 21g | SWING | Microstruttura exchange | 5 | 80,00% | +1,57% | +1,57% | -4,51% | +6,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 55 | 52,73% | +0,47% | +8,75% | -2,64% | +12,76% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 19 | 57,89% | -4,67% | +14,77% | -2,09% | +19,29% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 51 | 90,20% | +13,70% | +13,70% | -2,52% | +17,97% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 3 | 100,00% | +5,40% | +5,40% | -4,01% | +8,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 46 | 54,35% | -0,68% | +13,81% | -2,31% | +18,32% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 6 | 0,00% | -25,15% | +25,15% | -1,17% | +32,97% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 36 | 100,00% | +24,33% | +24,33% | -2,85% | +29,06% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 31 | 38,71% | -4,03% | +24,87% | -2,59% | +29,66% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 60g | MEDIO | Classic technical | 2 | 0,00% | -32,21% | +32,21% | -2,23% | +37,27% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 23 | 100,00% | +25,76% | +25,76% | -3,22% | +31,11% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +26,03% | +26,03% | -3,06% | +28,15% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 18 | 27,78% | -13,12% | +25,82% | -2,87% | +31,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 43 | 39,53% | -0,68% | +0,09% | -0,78% | +0,85% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 74 | 58,11% | +0,49% | +0,16% | -0,65% | +1,14% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 11 | 63,64% | +2,53% | +2,82% | +0,75% | +3,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 68 | 50,00% | +0,14% | +0,07% | -0,76% | +1,05% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 43 | 41,86% | -1,35% | +0,42% | -0,82% | +1,40% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 73 | 60,27% | +0,84% | +0,35% | -0,75% | +1,65% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 11 | 45,45% | +2,65% | +2,89% | +1,08% | +5,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 67 | 50,75% | +0,08% | +0,01% | -1,10% | +1,31% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Classic technical | 43 | 30,23% | -2,36% | +0,67% | -2,59% | +3,92% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 72 | 55,56% | +1,10% | +0,71% | -2,36% | +3,74% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 11 | 54,55% | +2,62% | +2,81% | -1,35% | +6,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 66 | 43,94% | -0,05% | +0,02% | -2,63% | +2,98% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Classic technical | 42 | 33,33% | -4,80% | +2,31% | -3,56% | +7,06% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 70 | 51,43% | +1,32% | +1,87% | -3,22% | +6,48% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 11 | 36,36% | +2,02% | +2,17% | -2,50% | +9,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 64 | 51,56% | -0,60% | +1,02% | -3,64% | +5,68% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Classic technical | 41 | 29,27% | -6,44% | +3,84% | -3,92% | +9,49% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 69 | 53,62% | +1,29% | +2,93% | -3,69% | +8,77% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 11 | 45,45% | +0,78% | +0,88% | -3,00% | +9,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 63 | 47,62% | -0,85% | +1,91% | -4,17% | +7,74% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Classic technical | 41 | 31,71% | -7,07% | +4,20% | -4,70% | +11,63% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 68 | 48,53% | +0,88% | +3,66% | -4,30% | +10,86% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 10 | 60,00% | +0,96% | +1,26% | -3,68% | +10,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 62 | 51,61% | -1,27% | +2,31% | -4,85% | +9,30% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Classic technical | 39 | 43,59% | -4,49% | +4,76% | -5,47% | +12,94% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 66 | 62,12% | +3,22% | +4,93% | -5,01% | +13,72% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 14g | SWING | Microstruttura exchange | 9 | 44,44% | +1,04% | +5,41% | -4,48% | +13,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 60 | 53,33% | -0,24% | +2,76% | -5,66% | +10,90% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 21g | SWING | Classic technical | 34 | 52,94% | -6,23% | +5,05% | -5,53% | +14,31% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 59 | 66,10% | +6,51% | +8,47% | -5,06% | +18,85% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 9 | 66,67% | +0,57% | +6,54% | -4,75% | +18,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 53 | 64,15% | -0,61% | +6,15% | -5,81% | +15,44% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 31 | 48,39% | -8,72% | +10,82% | -5,10% | +22,58% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Famiglia statistica | 50 | 84,00% | +10,72% | +13,29% | -4,72% | +26,92% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 8 | 87,50% | +13,45% | +21,36% | -4,45% | +31,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 44 | 56,82% | -4,82% | +11,64% | -5,60% | +24,19% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 23 | 0,00% | -23,20% | +23,20% | -4,66% | +40,46% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 36 | 55,56% | +6,48% | +24,05% | -4,16% | +41,55% | PESO OK | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,91% | +37,31% | -1,31% | +47,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 31 | 3,23% | -19,88% | +22,00% | -4,65% | +40,34% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 60g | MEDIO | Classic technical | 19 | 0,00% | -24,44% | +24,44% | -5,42% | +41,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 23 | 30,43% | -3,11% | +25,27% | -5,61% | +41,65% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,94% | +44,94% | -1,85% | +50,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 23 | 0,00% | -25,27% | +25,27% | -5,61% | +41,65% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 49 | 46,94% | +0,07% | +0,64% | -0,41% | +1,61% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 69 | 55,07% | +0,46% | +0,39% | -0,44% | +1,28% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 67 | 46,27% | -0,02% | +0,39% | -0,51% | +1,25% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 48 | 47,92% | +0,37% | +0,87% | -0,41% | +1,93% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 69 | 49,28% | +0,75% | +0,95% | -0,42% | +1,85% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 66 | 40,91% | -0,07% | +0,75% | -0,38% | +1,89% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 47 | 51,06% | +0,57% | +1,19% | -1,88% | +3,50% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 68 | 51,47% | +1,32% | +1,60% | -1,91% | +4,02% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 65 | 46,15% | -0,22% | +1,16% | -1,93% | +3,52% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 45 | 53,33% | +0,98% | +1,82% | -2,60% | +5,07% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 66 | 53,03% | +2,13% | +2,96% | -2,59% | +6,43% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 63 | 46,03% | -0,50% | +2,54% | -2,65% | +5,83% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Classic technical | 44 | 47,73% | +0,98% | +1,74% | -3,11% | +5,91% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 65 | 60,00% | +3,32% | +4,30% | -3,00% | +8,33% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 62 | 40,32% | -1,40% | +3,21% | -3,11% | +7,34% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Classic technical | 43 | 53,49% | +1,15% | +2,06% | -3,69% | +6,79% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 64 | 64,06% | +5,66% | +6,37% | -3,41% | +10,47% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 61 | 47,54% | -1,59% | +4,62% | -3,59% | +8,98% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 14g | SWING | Classic technical | 42 | 52,38% | +2,18% | +3,36% | -4,30% | +8,14% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 62 | 75,81% | +8,45% | +9,10% | -3,90% | +13,90% | POSSIBILE AUMENTO LEGGERO | +0,50 | MEDIA / ALTA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 60 | 45,00% | -2,12% | +6,76% | -4,07% | +11,88% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 21g | SWING | Classic technical | 41 | 63,41% | -0,67% | +10,79% | -4,62% | +15,70% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Famiglia statistica | 55 | 81,82% | +14,60% | +14,66% | -4,18% | +20,18% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 57 | 52,63% | -5,85% | +12,41% | -4,51% | +17,92% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 32 | 40,62% | -10,28% | +24,55% | -4,07% | +29,78% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Famiglia statistica | 46 | 86,96% | +21,55% | +24,92% | -3,84% | +31,28% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 5 | 100,00% | +21,75% | +21,75% | -3,55% | +25,06% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 48 | 31,25% | -12,99% | +22,11% | -4,29% | +28,12% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 21 | 0,00% | -38,81% | +38,81% | -4,64% | +48,52% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 32 | 75,00% | +25,78% | +40,58% | -4,69% | +48,45% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +44,56% | +44,56% | -5,94% | +49,24% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 34 | 11,76% | -33,19% | +38,98% | -5,09% | +47,07% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 60g | MEDIO | Classic technical | 15 | 0,00% | -49,72% | +49,72% | -6,02% | +56,18% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 19 | 57,89% | +17,25% | +45,97% | -6,82% | +52,85% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Microstruttura exchange | 1 | 100,00% | +41,93% | +41,93% | -9,62% | +45,82% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 23 | 17,39% | -32,58% | +44,37% | -6,82% | +51,71% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 71 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 75 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 87 | 39,08% | -0,14% |
| BTC | BREVE | Famiglia statistica | 222 | 52,70% | +0,69% |
| BTC | BREVE | Microstruttura exchange | 21 | 33,33% | -0,22% |
| BTC | BREVE | Tecnico | 201 | 39,30% | -0,08% |
| BTC | SETTIMANALE | Classic technical | 85 | 41,18% | -3,55% |
| BTC | SETTIMANALE | Famiglia statistica | 210 | 57,62% | +2,82% |
| BTC | SETTIMANALE | Microstruttura exchange | 18 | 27,78% | -1,45% |
| BTC | SETTIMANALE | Tecnico | 189 | 44,44% | -0,77% |
| BTC | SWING | Classic technical | 50 | 40,00% | -3,87% |
| BTC | SWING | Famiglia statistica | 127 | 67,72% | +6,51% |
| BTC | SWING | Microstruttura exchange | 10 | 60,00% | +0,93% |
| BTC | SWING | Tecnico | 117 | 55,56% | +1,09% |
| BTC | MEDIO | Classic technical | 27 | 40,74% | -11,26% |
| BTC | MEDIO | Famiglia statistica | 110 | 95,45% | +19,70% |
| BTC | MEDIO | Microstruttura exchange | 5 | 100,00% | +12,53% |
| BTC | MEDIO | Tecnico | 95 | 44,21% | -4,13% |
| DOGE | BREVE | Classic technical | 129 | 37,21% | -1,46% |
| DOGE | BREVE | Famiglia statistica | 219 | 57,99% | +0,81% |
| DOGE | BREVE | Microstruttura exchange | 33 | 54,55% | +2,60% |
| DOGE | BREVE | Tecnico | 201 | 48,26% | +0,06% |
| DOGE | SETTIMANALE | Classic technical | 124 | 31,45% | -6,09% |
| DOGE | SETTIMANALE | Famiglia statistica | 207 | 51,21% | +1,17% |
| DOGE | SETTIMANALE | Microstruttura exchange | 32 | 46,88% | +1,26% |
| DOGE | SETTIMANALE | Tecnico | 189 | 50,26% | -0,90% |
| DOGE | SWING | Classic technical | 73 | 47,95% | -5,30% |
| DOGE | SWING | Famiglia statistica | 125 | 64,00% | +4,77% |
| DOGE | SWING | Microstruttura exchange | 18 | 55,56% | +0,80% |
| DOGE | SWING | Tecnico | 113 | 58,41% | -0,41% |
| DOGE | MEDIO | Classic technical | 73 | 20,55% | -17,37% |
| DOGE | MEDIO | Famiglia statistica | 109 | 63,30% | +6,40% |
| DOGE | MEDIO | Microstruttura exchange | 14 | 85,71% | +18,65% |
| DOGE | MEDIO | Tecnico | 98 | 26,53% | -14,39% |
| SOL | BREVE | Classic technical | 144 | 48,61% | +0,33% |
| SOL | BREVE | Famiglia statistica | 206 | 51,94% | +0,84% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 198 | 44,44% | -0,10% |
| SOL | SETTIMANALE | Classic technical | 132 | 51,52% | +1,04% |
| SOL | SETTIMANALE | Famiglia statistica | 195 | 58,97% | +3,69% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 186 | 44,62% | -1,16% |
| SOL | SWING | Classic technical | 83 | 57,83% | +0,77% |
| SOL | SWING | Famiglia statistica | 117 | 78,63% | +11,34% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 117 | 48,72% | -3,94% |
| SOL | MEDIO | Classic technical | 68 | 19,12% | -27,79% |
| SOL | MEDIO | Famiglia statistica | 97 | 77,32% | +22,11% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 8 | 100,00% | +29,97% |
| SOL | MEDIO | Tecnico | 105 | 21,90% | -23,82% |

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
