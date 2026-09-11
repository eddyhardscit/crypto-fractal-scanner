# Calibrazione pesi Global Confluence

Generato: 2026-09-11 05:33 UTC

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
| BTC | 63 | UTILE | 62 | 17 | 3 | 0 | Famiglia statistica | 1g | 51,61% | +0,34% | campione utile, valutare con prudenza |
| SOL | 63 | PRIMA CALIBRAZIONE | 59 | 25 | 0 | 0 | Tecnico | 1g | 49,15% | +0,25% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 63 | UTILE | 61 | 25 | 2 | 0 | Famiglia statistica | 1g | 59,02% | +0,53% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 24 | 37,50% | +0,37% | +0,81% | +0,13% | +1,33% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 62 | 51,61% | +0,34% | +0,34% | -0,11% | +0,86% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 57 | 38,60% | +0,09% | +0,45% | -0,01% | +0,97% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 24 | 41,67% | +0,55% | +1,18% | +0,59% | +1,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 61 | 52,46% | +0,74% | +0,74% | +0,16% | +1,41% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 56 | 42,86% | +0,16% | +0,90% | +0,32% | +1,57% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 24 | 41,67% | +0,20% | +1,81% | -0,58% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 60 | 53,33% | +1,12% | +1,12% | -1,01% | +2,76% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 55 | 36,36% | -0,13% | +1,41% | -0,85% | +3,01% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 24 | 50,00% | -1,14% | +3,70% | -1,03% | +5,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 58 | 51,72% | +1,99% | +1,99% | -1,55% | +4,32% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 53 | 43,40% | -0,92% | +2,28% | -1,38% | +4,66% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 24 | 45,83% | -2,81% | +4,87% | -1,33% | +8,02% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 56 | 60,71% | +2,79% | +2,79% | -1,78% | +5,56% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | -0,70% | -0,70% | -2,63% | +2,73% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 51 | 43,14% | -1,71% | +3,29% | -1,59% | +5,99% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 21 | 57,14% | -3,87% | +6,18% | -1,39% | +9,51% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 53 | 66,04% | +3,68% | +3,68% | -2,03% | +6,67% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 48 | 47,92% | -1,36% | +4,18% | -1,81% | +7,24% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 17 | 41,18% | -4,34% | +7,22% | -1,20% | +11,14% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 49 | 61,22% | +5,49% | +5,49% | -2,16% | +8,96% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 44 | 56,82% | +0,75% | +6,25% | -1,90% | +9,79% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 10 | 20,00% | -13,93% | +17,02% | -0,10% | +20,53% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 42 | 71,43% | +10,16% | +10,16% | -2,13% | +13,96% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 37 | 37,84% | -0,99% | +11,32% | -1,82% | +15,19% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 4 | 0,00% | -24,06% | +24,06% | -1,55% | +28,48% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 34 | 85,29% | +13,80% | +13,80% | -3,00% | +17,88% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 29 | 44,83% | -1,57% | +13,99% | -2,74% | +18,41% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Classic technical | 1 | 0,00% | -21,57% | +21,57% | -1,82% | +29,79% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 20 | 100,00% | +22,42% | +22,42% | -3,27% | +26,67% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 16 | 31,25% | -8,73% | +22,74% | -2,90% | +27,16% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 5 | 100,00% | +23,72% | +23,72% | -2,65% | +29,47% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 4 | 50,00% | -0,95% | +23,83% | -2,49% | +29,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 34 | 41,18% | -0,49% | +0,22% | -0,44% | +0,96% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 61 | 59,02% | +0,53% | +0,26% | -0,42% | +1,18% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 9 | 55,56% | +1,78% | +2,13% | +0,65% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 55 | 52,73% | +0,41% | +0,17% | -0,54% | +1,07% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 34 | 41,18% | -1,26% | +0,45% | -0,31% | +1,41% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 60 | 56,67% | +0,86% | +0,58% | -0,21% | +1,76% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,61% | +2,90% | +2,02% | +4,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 54 | 53,70% | +0,53% | +0,19% | -0,59% | +1,35% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 34 | 29,41% | -2,31% | +0,82% | -2,19% | +3,95% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 59 | 54,24% | +1,16% | +1,04% | -1,85% | +3,89% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,26% | +2,49% | -0,95% | +6,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 53 | 45,28% | +0,54% | +0,22% | -2,13% | +2,98% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 32 | 37,50% | -4,10% | +2,16% | -2,90% | +6,52% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 57 | 49,12% | +1,87% | +2,04% | -2,62% | +6,32% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 9 | 33,33% | +0,34% | +0,52% | -2,37% | +7,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 51 | 58,82% | +0,74% | +0,99% | -3,06% | +5,30% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 31 | 38,71% | -4,80% | +2,76% | -3,30% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 55 | 54,55% | +2,49% | +2,81% | -3,02% | +8,30% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 8 | 50,00% | +0,28% | +0,41% | -2,23% | +8,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 49 | 59,18% | +1,50% | +1,48% | -3,56% | +6,91% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 31 | 41,94% | -4,39% | +2,22% | -3,95% | +9,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 52 | 51,92% | +3,11% | +2,83% | -3,67% | +9,55% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 8 | 62,50% | +0,35% | +0,72% | -3,12% | +9,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 46 | 65,22% | +1,74% | +0,91% | -4,33% | +7,27% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 31 | 48,39% | -3,87% | +3,26% | -4,53% | +11,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 48 | 72,92% | +6,67% | +4,53% | -4,01% | +12,78% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 7 | 57,14% | +2,04% | +7,65% | -2,99% | +15,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 42 | 61,90% | +0,96% | +1,37% | -4,79% | +8,62% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 27 | 55,56% | -7,10% | +7,10% | -3,69% | +15,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 42 | 88,10% | +12,69% | +9,88% | -3,27% | +20,49% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 5 | 80,00% | +2,29% | +13,05% | +0,50% | +27,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 35 | 65,71% | -3,14% | +7,10% | -3,95% | +15,94% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 22 | 50,00% | -9,38% | +9,38% | -4,86% | +19,29% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 34 | 88,24% | +11,92% | +13,27% | -4,36% | +25,97% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,03% | +30,85% | -1,31% | +42,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 30 | 40,00% | -11,60% | +11,60% | -4,76% | +23,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 17 | 0,00% | -20,63% | +20,63% | -5,74% | +38,18% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 20 | 20,00% | -11,31% | +20,33% | -5,99% | +37,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 20 | 0,00% | -20,33% | +20,33% | -5,99% | +37,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Classic technical | 5 | 0,00% | -20,35% | +20,35% | -7,07% | +36,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 5 | 0,00% | -20,35% | +20,35% | -7,07% | +36,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 5 | 0,00% | -20,35% | +20,35% | -7,07% | +36,68% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 42 | 50,00% | +0,45% | +0,49% | -0,33% | +1,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 57 | 54,39% | +0,26% | +0,27% | -0,39% | +1,13% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 59 | 49,15% | +0,25% | +0,27% | -0,43% | +1,09% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 42 | 50,00% | +0,73% | +0,75% | -0,18% | +1,69% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 56 | 46,43% | +0,36% | +0,79% | -0,17% | +1,60% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 58 | 43,10% | +0,17% | +0,70% | -0,20% | +1,76% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 41 | 53,66% | +0,96% | +1,10% | -1,74% | +3,38% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 55 | 49,09% | +0,88% | +1,41% | -1,71% | +3,72% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 57 | 49,12% | +0,06% | +1,21% | -1,75% | +3,45% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 39 | 58,97% | +1,65% | +1,79% | -2,43% | +5,03% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 53 | 54,72% | +1,60% | +2,62% | -2,33% | +6,03% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 55 | 49,09% | -0,38% | +2,52% | -2,47% | +5,82% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 37 | 54,05% | +2,08% | +2,03% | -2,89% | +6,02% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 51 | 60,78% | +2,63% | +3,88% | -2,70% | +7,89% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 53 | 43,40% | -1,12% | +3,61% | -2,86% | +7,60% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 34 | 55,88% | +2,07% | +1,97% | -3,43% | +6,65% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 48 | 60,42% | +4,66% | +5,61% | -3,09% | +9,82% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 50 | 46,00% | -2,04% | +4,69% | -3,31% | +9,05% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 30 | 53,33% | +1,59% | +3,25% | -3,42% | +8,10% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 44 | 79,55% | +8,45% | +9,37% | -3,05% | +14,46% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 46 | 41,30% | -4,43% | +7,15% | -3,37% | +12,52% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 23 | 43,48% | -8,85% | +11,57% | -4,02% | +16,26% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 37 | 83,78% | +17,93% | +17,02% | -3,60% | +22,71% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 3 | 66,67% | +15,44% | +15,44% | -3,34% | +22,79% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 39 | 35,90% | -13,07% | +13,62% | -4,11% | +19,28% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 21 | 9,52% | -26,53% | +26,53% | -4,64% | +32,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 30 | 90,00% | +24,28% | +24,63% | -4,89% | +31,11% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +22,28% | +22,28% | -5,94% | +27,20% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 32 | 12,50% | -21,52% | +20,94% | -5,31% | +26,83% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 12 | 0,00% | -36,08% | +36,08% | -6,52% | +45,51% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 16 | 50,00% | +3,38% | +32,98% | -7,34% | +41,19% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 20 | 20,00% | -23,77% | +33,61% | -7,24% | +41,45% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 4 | 0,00% | -33,00% | +33,00% | -8,35% | +42,66% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 5 | 80,00% | +21,04% | +33,20% | -8,51% | +42,41% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 59 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 62 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 72 | 40,28% | +0,37% |
| BTC | BREVE | Famiglia statistica | 183 | 52,46% | +0,73% |
| BTC | BREVE | Microstruttura exchange | 15 | 40,00% | +0,30% |
| BTC | BREVE | Tecnico | 168 | 39,29% | +0,04% |
| BTC | SETTIMANALE | Classic technical | 69 | 50,72% | -2,55% |
| BTC | SETTIMANALE | Famiglia statistica | 167 | 59,28% | +2,79% |
| BTC | SETTIMANALE | Microstruttura exchange | 12 | 41,67% | -0,51% |
| BTC | SETTIMANALE | Tecnico | 152 | 44,74% | -1,32% |
| BTC | SWING | Classic technical | 27 | 33,33% | -7,89% |
| BTC | SWING | Famiglia statistica | 91 | 65,93% | +7,64% |
| BTC | SWING | Microstruttura exchange | 4 | 50,00% | +0,28% |
| BTC | SWING | Tecnico | 81 | 48,15% | -0,05% |
| BTC | MEDIO | Classic technical | 5 | 0,00% | -23,57% |
| BTC | MEDIO | Famiglia statistica | 59 | 91,53% | +17,56% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 49 | 40,82% | -3,86% |
| DOGE | BREVE | Classic technical | 102 | 37,25% | -1,35% |
| DOGE | BREVE | Famiglia statistica | 180 | 56,67% | +0,85% |
| DOGE | BREVE | Microstruttura exchange | 27 | 48,15% | +2,22% |
| DOGE | BREVE | Tecnico | 162 | 50,62% | +0,49% |
| DOGE | SETTIMANALE | Classic technical | 94 | 39,36% | -4,43% |
| DOGE | SETTIMANALE | Famiglia statistica | 164 | 51,83% | +2,47% |
| DOGE | SETTIMANALE | Microstruttura exchange | 25 | 48,00% | +0,32% |
| DOGE | SETTIMANALE | Tecnico | 146 | 60,96% | +1,31% |
| DOGE | SWING | Classic technical | 58 | 51,72% | -5,37% |
| DOGE | SWING | Famiglia statistica | 90 | 80,00% | +9,48% |
| DOGE | SWING | Microstruttura exchange | 12 | 66,67% | +2,15% |
| DOGE | SWING | Tecnico | 77 | 63,64% | -0,90% |
| DOGE | MEDIO | Classic technical | 44 | 25,00% | -14,97% |
| DOGE | MEDIO | Famiglia statistica | 59 | 57,63% | +1,31% |
| DOGE | MEDIO | Microstruttura exchange | 6 | 83,33% | +20,07% |
| DOGE | MEDIO | Tecnico | 55 | 21,82% | -15,57% |
| SOL | BREVE | Classic technical | 125 | 51,20% | +0,71% |
| SOL | BREVE | Famiglia statistica | 168 | 50,00% | +0,49% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 174 | 47,13% | +0,16% |
| SOL | SETTIMANALE | Classic technical | 110 | 56,36% | +1,93% |
| SOL | SETTIMANALE | Famiglia statistica | 152 | 58,55% | +2,91% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 158 | 46,20% | -1,15% |
| SOL | SWING | Classic technical | 53 | 49,06% | -2,94% |
| SOL | SWING | Famiglia statistica | 81 | 81,48% | +12,78% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 8 | 75,00% | +10,89% |
| SOL | SWING | Tecnico | 85 | 38,82% | -8,39% |
| SOL | MEDIO | Classic technical | 33 | 6,06% | -30,00% |
| SOL | MEDIO | Famiglia statistica | 50 | 70,00% | +13,01% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 3 | 100,00% | +25,70% |
| SOL | MEDIO | Tecnico | 57 | 21,05% | -18,58% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 5 | in attesa di controlli maturati |
| SOL | MEDIO | 2 | in attesa di controlli maturati |
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
