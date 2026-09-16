# Calibrazione pesi Global Confluence

Generato: 2026-09-16 05:32 UTC

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
| BTC | 68 | UTILE | 67 | 18 | 8 | 0 | Famiglia statistica | 1g | 52,24% | +0,29% | campione utile, valutare con prudenza |
| SOL | 68 | UTILE | 62 | 25 | 6 | 0 | Famiglia statistica | 1g | 53,23% | +0,20% | campione utile, valutare con prudenza |
| DOGE | 68 | UTILE | 66 | 26 | 6 | 0 | Famiglia statistica | 1g | 59,09% | +0,56% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 26 | 42,31% | +0,43% | +0,67% | +0,02% | +1,19% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 67 | 52,24% | +0,29% | +0,29% | -0,15% | +0,80% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 62 | 40,32% | +0,05% | +0,39% | -0,07% | +0,90% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 25 | 44,00% | +0,61% | +1,05% | +0,46% | +1,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 66 | 53,03% | +0,64% | +0,64% | +0,07% | +1,29% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 61 | 44,26% | +0,10% | +0,78% | +0,21% | +1,42% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Classic technical | 24 | 41,67% | +0,20% | +1,81% | -0,58% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 65 | 52,31% | +0,96% | +0,96% | -1,09% | +2,65% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 60 | 36,67% | -0,20% | +1,21% | -0,95% | +2,87% | POSSIBILE RIDUZIONE PESO | -0,50 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Classic technical | 24 | 50,00% | -1,14% | +3,70% | -1,03% | +5,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 63 | 47,62% | +1,67% | +1,67% | -1,69% | +4,09% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 58 | 39,66% | -1,01% | +1,91% | -1,53% | +4,38% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 24 | 45,83% | -2,81% | +4,87% | -1,33% | +8,02% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 61 | 55,74% | +2,32% | +2,32% | -1,98% | +5,17% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 56 | 39,29% | -1,83% | +2,73% | -1,82% | +5,53% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 24 | 50,00% | -3,59% | +5,20% | -1,59% | +8,77% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 58 | 60,34% | +3,14% | +3,14% | -2,18% | +6,31% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,56% | -1,56% | -3,78% | +2,36% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 53 | 43,40% | -1,47% | +3,54% | -1,99% | +6,79% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 22 | 31,82% | -3,66% | +5,27% | -1,53% | +9,82% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 54 | 55,56% | +4,85% | +4,85% | -2,21% | +8,63% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 49 | 51,02% | +0,53% | +5,48% | -1,98% | +9,34% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 15 | 33,33% | -9,70% | +10,93% | -0,96% | +15,50% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 47 | 70,21% | +8,94% | +8,94% | -2,19% | +13,06% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 3 | 66,67% | -0,54% | -0,54% | -2,98% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 42 | 40,48% | -1,02% | +9,82% | -1,92% | +14,03% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 8 | 0,00% | -23,09% | +23,09% | -0,83% | +29,47% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 38 | 86,84% | +14,68% | +14,68% | -2,69% | +19,20% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 33 | 39,39% | -4,06% | +14,98% | -2,43% | +19,87% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 3 | 0,00% | -21,72% | +21,72% | -1,93% | +29,65% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 25 | 100,00% | +22,11% | +22,11% | -3,09% | +27,16% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 20 | 25,00% | -11,19% | +22,39% | -2,74% | +27,61% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 10 | 100,00% | +22,31% | +22,31% | -2,50% | +29,28% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 9 | 33,33% | -7,65% | +22,20% | -2,41% | +29,34% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 39 | 43,59% | -0,31% | +0,08% | -0,58% | +0,78% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 66 | 59,09% | +0,56% | +0,17% | -0,51% | +1,06% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 9 | 55,56% | +1,78% | +2,13% | +0,65% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 60 | 53,33% | +0,45% | +0,08% | -0,62% | +0,95% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Classic technical | 38 | 44,74% | -0,96% | +0,23% | -0,53% | +1,16% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 65 | 58,46% | +0,92% | +0,41% | -0,37% | +1,54% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,61% | +2,90% | +2,02% | +4,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 59 | 55,93% | +0,63% | +0,04% | -0,73% | +1,14% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 37 | 32,43% | -1,92% | +0,56% | -2,31% | +3,73% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 64 | 56,25% | +1,31% | +0,72% | -2,06% | +3,61% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,26% | +2,49% | -0,95% | +6,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 58 | 46,55% | +0,52% | -0,06% | -2,33% | +2,75% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 35 | 37,14% | -3,98% | +1,49% | -3,27% | +6,12% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 62 | 53,23% | +2,16% | +1,43% | -2,96% | +5,89% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 9 | 33,33% | +0,34% | +0,52% | -2,37% | +7,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 56 | 57,14% | +0,48% | +0,42% | -3,41% | +4,91% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 34 | 35,29% | -5,01% | +1,88% | -3,79% | +7,55% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 60 | 58,33% | +2,86% | +2,00% | -3,46% | +7,75% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 9 | 44,44% | -0,49% | -0,37% | -2,97% | +7,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 54 | 53,70% | +0,73% | +0,71% | -4,00% | +6,43% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 32 | 40,62% | -4,62% | +1,78% | -4,22% | +8,99% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 57 | 52,63% | +3,05% | +2,37% | -3,74% | +9,52% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 9 | 55,56% | -1,01% | -0,68% | -4,16% | +8,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 51 | 62,75% | +1,32% | +0,57% | -4,34% | +7,46% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 31 | 48,39% | -3,87% | +3,26% | -4,53% | +11,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 53 | 73,58% | +6,09% | +4,05% | -4,03% | +12,77% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 8 | 50,00% | +1,67% | +6,58% | -3,33% | +14,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 47 | 57,45% | +0,80% | +1,17% | -4,73% | +9,05% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 31 | 48,39% | -7,22% | +5,15% | -4,78% | +14,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 46 | 80,43% | +10,89% | +8,32% | -4,04% | +18,98% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 7 | 57,14% | -0,50% | +7,18% | -3,01% | +20,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 40 | 57,50% | -3,74% | +5,22% | -4,88% | +14,48% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 25 | 44,00% | -10,47% | +10,47% | -4,32% | +22,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 38 | 89,47% | +12,65% | +13,85% | -3,96% | +27,78% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,03% | +30,85% | -1,31% | +42,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 33 | 42,42% | -9,80% | +12,15% | -4,39% | +25,43% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 20 | 0,00% | -20,53% | +20,53% | -5,27% | +38,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 25 | 36,00% | -5,31% | +20,00% | -5,36% | +38,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 25 | 0,00% | -20,00% | +20,00% | -5,36% | +38,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Classic technical | 9 | 0,00% | -17,70% | +17,70% | -6,65% | +37,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 10 | 0,00% | -17,41% | +17,41% | -6,79% | +37,10% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 10 | 0,00% | -17,41% | +17,41% | -6,79% | +37,10% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 42 | 50,00% | +0,45% | +0,49% | -0,33% | +1,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 62 | 53,23% | +0,20% | +0,21% | -0,45% | +1,05% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 60 | 48,33% | +0,23% | +0,26% | -0,46% | +1,06% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 42 | 50,00% | +0,73% | +0,75% | -0,18% | +1,69% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 61 | 44,26% | +0,27% | +0,66% | -0,27% | +1,47% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 60 | 41,67% | +0,14% | +0,65% | -0,22% | +1,72% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Classic technical | 42 | 52,38% | +0,88% | +1,01% | -1,83% | +3,26% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 60 | 46,67% | +0,69% | +1,18% | -1,84% | +3,56% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 60 | 46,67% | -0,07% | +1,03% | -1,90% | +3,36% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 5g | SETTIMANALE | Classic technical | 42 | 54,76% | +1,33% | +1,47% | -2,64% | +4,74% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 58 | 50,00% | +1,25% | +2,19% | -2,53% | +5,71% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 59 | 45,76% | -0,51% | +2,19% | -2,63% | +5,53% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 42 | 47,62% | +1,40% | +1,36% | -3,24% | +5,52% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 56 | 55,36% | +2,07% | +3,21% | -2,97% | +7,34% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 58 | 39,66% | -1,34% | +2,99% | -3,11% | +7,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 39 | 53,85% | +1,57% | +1,48% | -3,51% | +6,38% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 53 | 58,49% | +4,05% | +4,91% | -3,19% | +9,32% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 55 | 45,45% | -2,02% | +4,09% | -3,38% | +8,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 35 | 45,71% | +0,98% | +2,41% | -3,75% | +7,50% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 49 | 71,43% | +7,32% | +8,15% | -3,33% | +13,38% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 51 | 37,25% | -4,26% | +6,19% | -3,60% | +11,67% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 28 | 50,00% | -6,40% | +10,38% | -3,57% | +16,02% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 42 | 78,57% | +15,51% | +15,58% | -3,35% | +21,78% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 5 | 60,00% | +8,98% | +8,98% | -3,51% | +17,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 44 | 40,91% | -11,03% | +12,63% | -3,81% | +18,78% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 21 | 9,52% | -26,53% | +26,53% | -4,64% | +32,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 34 | 91,18% | +25,29% | +25,60% | -4,46% | +32,86% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +22,28% | +22,28% | -5,94% | +27,20% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 36 | 11,11% | -22,79% | +22,27% | -4,85% | +28,95% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 17 | 0,00% | -36,25% | +36,25% | -5,53% | +46,74% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 21 | 61,90% | +11,31% | +33,86% | -6,34% | +43,22% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 25 | 16,00% | -26,35% | +34,22% | -6,43% | +43,10% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Classic technical | 3 | 0,00% | -32,23% | +32,23% | -6,17% | +46,05% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 7 | 14,29% | -23,98% | +32,93% | -7,87% | +43,40% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 10 | 40,00% | -5,83% | +32,95% | -7,56% | +43,89% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 64 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 67 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 75 | 42,67% | +0,42% |
| BTC | BREVE | Famiglia statistica | 198 | 52,53% | +0,63% |
| BTC | BREVE | Microstruttura exchange | 15 | 40,00% | +0,30% |
| BTC | BREVE | Tecnico | 183 | 40,44% | -0,01% |
| BTC | SETTIMANALE | Classic technical | 72 | 48,61% | -2,51% |
| BTC | SETTIMANALE | Famiglia statistica | 182 | 54,40% | +2,36% |
| BTC | SETTIMANALE | Microstruttura exchange | 15 | 33,33% | -1,25% |
| BTC | SETTIMANALE | Tecnico | 167 | 40,72% | -1,43% |
| BTC | SWING | Classic technical | 37 | 32,43% | -6,11% |
| BTC | SWING | Famiglia statistica | 101 | 62,38% | +6,76% |
| BTC | SWING | Microstruttura exchange | 6 | 50,00% | -0,28% |
| BTC | SWING | Tecnico | 91 | 46,15% | -0,19% |
| BTC | MEDIO | Classic technical | 11 | 0,00% | -22,71% |
| BTC | MEDIO | Famiglia statistica | 73 | 93,15% | +18,27% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 62 | 33,87% | -6,88% |
| DOGE | BREVE | Classic technical | 114 | 40,35% | -1,05% |
| DOGE | BREVE | Famiglia statistica | 195 | 57,95% | +0,92% |
| DOGE | BREVE | Microstruttura exchange | 27 | 48,15% | +2,22% |
| DOGE | BREVE | Tecnico | 177 | 51,98% | +0,53% |
| DOGE | SETTIMANALE | Classic technical | 101 | 37,62% | -4,53% |
| DOGE | SETTIMANALE | Famiglia statistica | 179 | 54,75% | +2,68% |
| DOGE | SETTIMANALE | Microstruttura exchange | 27 | 44,44% | -0,39% |
| DOGE | SETTIMANALE | Tecnico | 161 | 57,76% | +0,83% |
| DOGE | SWING | Classic technical | 62 | 48,39% | -5,54% |
| DOGE | SWING | Famiglia statistica | 99 | 76,77% | +8,32% |
| DOGE | SWING | Microstruttura exchange | 15 | 53,33% | +0,66% |
| DOGE | SWING | Tecnico | 87 | 57,47% | -1,29% |
| DOGE | MEDIO | Classic technical | 54 | 20,37% | -15,40% |
| DOGE | MEDIO | Famiglia statistica | 73 | 58,90% | +2,38% |
| DOGE | MEDIO | Microstruttura exchange | 6 | 83,33% | +20,07% |
| DOGE | MEDIO | Tecnico | 68 | 20,59% | -14,67% |
| SOL | BREVE | Classic technical | 126 | 50,79% | +0,69% |
| SOL | BREVE | Famiglia statistica | 183 | 48,09% | +0,38% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 180 | 45,56% | +0,10% |
| SOL | SETTIMANALE | Classic technical | 123 | 52,03% | +1,43% |
| SOL | SETTIMANALE | Famiglia statistica | 167 | 54,49% | +2,41% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 172 | 43,60% | -1,27% |
| SOL | SWING | Classic technical | 63 | 47,62% | -2,30% |
| SOL | SWING | Famiglia statistica | 91 | 74,73% | +11,10% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 10 | 70,00% | +8,57% |
| SOL | SWING | Tecnico | 95 | 38,95% | -7,39% |
| SOL | MEDIO | Classic technical | 41 | 4,88% | -30,98% |
| SOL | MEDIO | Famiglia statistica | 62 | 72,58% | +14,99% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 3 | 100,00% | +25,70% |
| SOL | MEDIO | Tecnico | 71 | 16,90% | -21,65% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 5 | in attesa di controlli maturati |
| SOL | MEDIO | 1 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 2 | in attesa di controlli maturati |
| DOGE | MEDIO | 4 | in attesa di controlli maturati |

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
