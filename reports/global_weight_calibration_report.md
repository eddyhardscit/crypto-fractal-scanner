# Calibrazione pesi Global Confluence

Generato: 2026-09-09 05:33 UTC

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
| BTC | 61 | UTILE | 60 | 17 | 1 | 0 | Famiglia statistica | 1g | 53,33% | +0,39% | campione utile, valutare con prudenza |
| SOL | 61 | PRIMA CALIBRAZIONE | 57 | 23 | 0 | 0 | Tecnico | 1g | 50,88% | +0,34% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 61 | PRIMA CALIBRAZIONE | 59 | 25 | 0 | 0 | Famiglia statistica | 1g | 57,63% | +0,43% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 24 | 37,50% | +0,37% | +0,81% | +0,13% | +1,33% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 60 | 53,33% | +0,39% | +0,39% | -0,05% | +0,93% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 55 | 40,00% | +0,14% | +0,51% | +0,06% | +1,05% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 24 | 41,67% | +0,55% | +1,18% | +0,59% | +1,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 59 | 54,24% | +0,81% | +0,81% | +0,24% | +1,50% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 54 | 44,44% | +0,22% | +0,98% | +0,41% | +1,67% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 24 | 41,67% | +0,20% | +1,81% | -0,58% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 58 | 55,17% | +1,23% | +1,23% | -0,95% | +2,84% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 53 | 37,74% | -0,06% | +1,53% | -0,77% | +3,11% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 24 | 50,00% | -1,14% | +3,70% | -1,03% | +5,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 56 | 53,57% | +2,15% | +2,15% | -1,49% | +4,44% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 4 | 25,00% | -0,34% | -0,34% | -1,71% | +2,56% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 51 | 45,10% | -0,86% | +2,46% | -1,30% | +4,81% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 22 | 45,45% | -2,91% | +5,46% | -1,23% | +8,53% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 54 | 61,11% | +2,96% | +2,96% | -1,76% | +5,67% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 49 | 42,86% | -1,72% | +3,49% | -1,55% | +6,14% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 19 | 57,89% | -4,18% | +6,93% | -1,23% | +10,01% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 51 | 66,67% | +3,86% | +3,86% | -2,00% | +6,75% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 46 | 47,83% | -1,38% | +4,40% | -1,76% | +7,35% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 15 | 46,67% | -4,69% | +8,42% | -0,87% | +12,10% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 47 | 63,83% | +5,79% | +5,79% | -2,10% | +9,18% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 42 | 59,52% | +0,86% | +6,63% | -1,82% | +10,07% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 8 | 0,00% | -19,34% | +19,34% | -0,83% | +22,19% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 40 | 70,00% | +10,28% | +10,28% | -2,38% | +13,97% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 35 | 34,29% | -1,49% | +11,52% | -2,08% | +15,27% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 4 | 0,00% | -24,06% | +24,06% | -1,55% | +28,48% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 33 | 84,85% | +13,53% | +13,53% | -3,02% | +17,55% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 28 | 42,86% | -2,44% | +13,68% | -2,76% | +18,04% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 18 | 100,00% | +22,59% | +22,59% | -3,27% | +26,54% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 15 | 33,33% | -7,88% | +22,81% | -2,97% | +26,99% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 3 | 100,00% | +24,28% | +24,28% | -3,05% | +29,12% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 2 | 0,00% | -24,78% | +24,78% | -2,93% | +29,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 34 | 41,18% | -0,49% | +0,22% | -0,44% | +0,96% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 59 | 57,63% | +0,43% | +0,39% | -0,28% | +1,34% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 9 | 55,56% | +1,78% | +2,13% | +0,65% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 53 | 52,83% | +0,47% | +0,31% | -0,39% | +1,24% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 33 | 42,42% | -1,16% | +0,60% | -0,16% | +1,59% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 58 | 55,17% | +0,69% | +0,80% | +0,01% | +2,01% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,61% | +2,90% | +2,02% | +4,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 52 | 55,77% | +0,78% | +0,42% | -0,35% | +1,62% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 32 | 31,25% | -2,09% | +1,23% | -1,90% | +4,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 57 | 52,63% | +1,00% | +1,28% | -1,68% | +3,98% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,26% | +2,49% | -0,95% | +6,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 51 | 47,06% | +0,78% | +0,46% | -1,95% | +3,04% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 31 | 38,71% | -3,99% | +2,48% | -2,71% | +6,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 55 | 49,09% | +1,81% | +2,25% | -2,55% | +6,40% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | +1,34% | +1,54% | -1,56% | +8,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 49 | 59,18% | +0,92% | +1,18% | -3,00% | +5,35% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 31 | 38,71% | -4,80% | +2,76% | -3,30% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 53 | 54,72% | +2,60% | +2,90% | -3,09% | +8,19% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 8 | 50,00% | +0,28% | +0,41% | -2,23% | +8,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 47 | 59,57% | +1,55% | +1,52% | -3,65% | +6,72% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 31 | 41,94% | -4,39% | +2,22% | -3,95% | +9,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 50 | 54,00% | +3,32% | +2,86% | -3,68% | +9,40% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 8 | 62,50% | +0,35% | +0,72% | -3,12% | +9,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 44 | 63,64% | +1,72% | +0,85% | -4,37% | +7,00% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 31 | 48,39% | -3,87% | +3,26% | -4,53% | +11,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 46 | 71,74% | +6,86% | +4,82% | -3,86% | +12,97% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 7 | 57,14% | +2,04% | +7,65% | -2,99% | +15,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 40 | 65,00% | +1,12% | +1,56% | -4,65% | +8,64% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 27 | 55,56% | -7,10% | +7,10% | -3,69% | +15,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 40 | 87,50% | +12,91% | +9,95% | -3,56% | +20,13% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 4 | 75,00% | -0,95% | +12,49% | -1,31% | +25,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 33 | 63,64% | -3,84% | +7,02% | -4,34% | +15,23% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 22 | 50,00% | -9,38% | +9,38% | -4,86% | +19,29% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 33 | 87,88% | +11,59% | +12,97% | -4,45% | +25,44% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,03% | +30,85% | -1,31% | +42,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 30 | 40,00% | -11,60% | +11,60% | -4,76% | +23,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 16 | 0,00% | -20,67% | +20,67% | -5,92% | +37,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 18 | 11,11% | -14,67% | +20,48% | -6,13% | +37,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 18 | 0,00% | -20,48% | +20,48% | -6,13% | +37,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Classic technical | 3 | 0,00% | -22,53% | +22,53% | -7,62% | +35,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 3 | 0,00% | -22,53% | +22,53% | -7,62% | +35,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 3 | 0,00% | -22,53% | +22,53% | -7,62% | +35,88% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 41 | 51,22% | +0,51% | +0,55% | -0,25% | +1,48% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 55 | 56,36% | +0,35% | +0,36% | -0,28% | +1,24% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 57 | 50,88% | +0,34% | +0,36% | -0,32% | +1,20% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 40 | 52,50% | +0,90% | +0,93% | +0,01% | +1,91% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 54 | 48,15% | +0,48% | +0,92% | -0,03% | +1,76% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 56 | 44,64% | +0,28% | +0,83% | -0,06% | +1,92% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 39 | 56,41% | +1,19% | +1,33% | -1,60% | +3,53% | PESO OK | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 53 | 50,94% | +1,04% | +1,59% | -1,60% | +3,85% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 55 | 50,91% | +0,19% | +1,38% | -1,65% | +3,57% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 37 | 62,16% | +1,90% | +2,06% | -2,33% | +5,15% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 51 | 56,86% | +1,78% | +2,85% | -2,26% | +6,16% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 53 | 50,94% | -0,28% | +2,73% | -2,40% | +5,93% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 35 | 54,29% | +2,26% | +2,21% | -2,93% | +6,07% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 49 | 61,22% | +2,78% | +4,08% | -2,72% | +8,00% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 51 | 43,14% | -1,12% | +3,79% | -2,89% | +7,70% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 32 | 59,38% | +2,35% | +2,24% | -3,29% | +6,84% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 46 | 63,04% | +4,97% | +5,96% | -2,98% | +10,08% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 48 | 47,92% | -2,02% | +4,98% | -3,21% | +9,28% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 28 | 53,57% | +1,89% | +3,67% | -3,23% | +8,33% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 42 | 80,95% | +8,98% | +9,94% | -2,92% | +14,91% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 44 | 40,91% | -4,51% | +7,59% | -3,25% | +12,86% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 36 | 86,11% | +18,74% | +17,19% | -3,75% | +22,71% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 37 | 32,43% | -14,62% | +13,51% | -4,47% | +18,90% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 21 | 9,52% | -26,53% | +26,53% | -4,64% | +32,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 29 | 89,66% | +23,92% | +24,28% | -4,99% | +30,62% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +22,28% | +22,28% | -5,94% | +27,20% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 32 | 12,50% | -21,52% | +20,94% | -5,31% | +26,83% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 10 | 0,00% | -36,35% | +36,35% | -6,72% | +45,19% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 14 | 42,86% | -1,10% | +32,72% | -7,61% | +40,35% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 18 | 22,22% | -22,55% | +33,48% | -7,44% | +40,82% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 2 | 0,00% | -34,09% | +34,09% | -9,20% | +41,33% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 3 | 100,00% | +34,06% | +34,06% | -9,18% | +41,37% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 57 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 60 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 72 | 40,28% | +0,37% |
| BTC | BREVE | Famiglia statistica | 177 | 54,24% | +0,80% |
| BTC | BREVE | Microstruttura exchange | 15 | 40,00% | +0,30% |
| BTC | BREVE | Tecnico | 162 | 40,74% | +0,10% |
| BTC | SETTIMANALE | Classic technical | 65 | 50,77% | -2,63% |
| BTC | SETTIMANALE | Famiglia statistica | 161 | 60,25% | +2,96% |
| BTC | SETTIMANALE | Microstruttura exchange | 10 | 50,00% | +0,23% |
| BTC | SETTIMANALE | Tecnico | 146 | 45,21% | -1,31% |
| BTC | SWING | Classic technical | 23 | 30,43% | -9,78% |
| BTC | SWING | Famiglia statistica | 87 | 66,67% | +7,86% |
| BTC | SWING | Microstruttura exchange | 4 | 50,00% | +0,28% |
| BTC | SWING | Tecnico | 77 | 48,05% | -0,21% |
| BTC | MEDIO | Classic technical | 4 | 0,00% | -24,06% |
| BTC | MEDIO | Famiglia statistica | 54 | 90,74% | +17,15% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 45 | 37,78% | -5,25% |
| DOGE | BREVE | Classic technical | 99 | 38,38% | -1,23% |
| DOGE | BREVE | Famiglia statistica | 174 | 55,17% | +0,70% |
| DOGE | BREVE | Microstruttura exchange | 27 | 48,15% | +2,22% |
| DOGE | BREVE | Tecnico | 156 | 51,92% | +0,67% |
| DOGE | SETTIMANALE | Classic technical | 93 | 39,78% | -4,39% |
| DOGE | SETTIMANALE | Famiglia statistica | 158 | 52,53% | +2,55% |
| DOGE | SETTIMANALE | Microstruttura exchange | 24 | 50,00% | +0,65% |
| DOGE | SETTIMANALE | Tecnico | 140 | 60,71% | +1,38% |
| DOGE | SWING | Classic technical | 58 | 51,72% | -5,37% |
| DOGE | SWING | Famiglia statistica | 86 | 79,07% | +9,67% |
| DOGE | SWING | Microstruttura exchange | 11 | 63,64% | +0,95% |
| DOGE | SWING | Tecnico | 73 | 64,38% | -1,12% |
| DOGE | MEDIO | Classic technical | 41 | 26,83% | -14,75% |
| DOGE | MEDIO | Famiglia statistica | 54 | 57,41% | +0,94% |
| DOGE | MEDIO | Microstruttura exchange | 6 | 83,33% | +20,07% |
| DOGE | MEDIO | Tecnico | 51 | 23,53% | -15,38% |
| SOL | BREVE | Classic technical | 120 | 53,33% | +0,86% |
| SOL | BREVE | Famiglia statistica | 162 | 51,85% | +0,62% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 168 | 48,81% | +0,27% |
| SOL | SETTIMANALE | Classic technical | 104 | 58,65% | +2,16% |
| SOL | SETTIMANALE | Famiglia statistica | 146 | 60,27% | +3,12% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 152 | 47,37% | -1,11% |
| SOL | SWING | Classic technical | 49 | 46,94% | -3,71% |
| SOL | SWING | Famiglia statistica | 78 | 83,33% | +13,48% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 7 | 71,43% | +10,86% |
| SOL | SWING | Tecnico | 81 | 37,04% | -9,13% |
| SOL | MEDIO | Classic technical | 31 | 6,45% | -29,70% |
| SOL | MEDIO | Famiglia statistica | 45 | 71,11% | +13,55% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 3 | 100,00% | +25,70% |
| SOL | MEDIO | Tecnico | 53 | 20,75% | -18,72% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 6 | in attesa di controlli maturati |
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
