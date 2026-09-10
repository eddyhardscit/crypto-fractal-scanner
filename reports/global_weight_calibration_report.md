# Calibrazione pesi Global Confluence

Generato: 2026-09-10 05:33 UTC

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
| BTC | 62 | UTILE | 61 | 17 | 2 | 0 | Famiglia statistica | 1g | 52,46% | +0,37% | campione utile, valutare con prudenza |
| SOL | 62 | PRIMA CALIBRAZIONE | 58 | 24 | 0 | 0 | Tecnico | 1g | 50,00% | +0,30% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 62 | UTILE | 60 | 25 | 1 | 0 | Famiglia statistica | 1g | 58,33% | +0,50% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 24 | 37,50% | +0,37% | +0,81% | +0,13% | +1,33% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 61 | 52,46% | +0,37% | +0,37% | -0,07% | +0,90% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 56 | 39,29% | +0,12% | +0,49% | +0,03% | +1,02% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 24 | 41,67% | +0,55% | +1,18% | +0,59% | +1,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 60 | 53,33% | +0,79% | +0,79% | +0,22% | +1,47% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 55 | 43,64% | +0,21% | +0,96% | +0,38% | +1,64% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 24 | 41,67% | +0,20% | +1,81% | -0,58% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 59 | 54,24% | +1,18% | +1,18% | -0,98% | +2,79% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 54 | 37,04% | -0,09% | +1,47% | -0,81% | +3,05% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 24 | 50,00% | -1,14% | +3,70% | -1,03% | +5,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 57 | 52,63% | +2,08% | +2,08% | -1,51% | +4,39% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 4 | 25,00% | -0,34% | -0,34% | -1,71% | +2,56% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 52 | 44,23% | -0,87% | +2,39% | -1,32% | +4,74% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 23 | 47,83% | -2,72% | +5,29% | -1,15% | +8,39% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 55 | 61,82% | +2,93% | +2,93% | -1,72% | +5,67% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 50 | 44,00% | -1,65% | +3,45% | -1,51% | +6,12% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 20 | 60,00% | -3,94% | +6,61% | -1,28% | +9,78% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 52 | 67,31% | +3,79% | +3,79% | -2,00% | +6,72% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 47 | 48,94% | -1,34% | +4,32% | -1,77% | +7,31% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 16 | 43,75% | -4,40% | +7,88% | -1,01% | +11,63% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 48 | 62,50% | +5,67% | +5,67% | -2,12% | +9,08% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 43 | 58,14% | +0,84% | +6,48% | -1,85% | +9,94% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 9 | 11,11% | -15,77% | +18,62% | -0,19% | +21,75% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 41 | 70,73% | +10,34% | +10,34% | -2,20% | +14,07% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 36 | 36,11% | -1,09% | +11,56% | -1,89% | +15,35% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 4 | 0,00% | -24,06% | +24,06% | -1,55% | +28,48% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 34 | 85,29% | +13,80% | +13,80% | -3,00% | +17,88% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 29 | 44,83% | -1,57% | +13,99% | -2,74% | +18,41% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 19 | 100,00% | +22,46% | +22,46% | -3,35% | +26,51% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 15 | 33,33% | -7,88% | +22,81% | -2,97% | +26,99% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 4 | 100,00% | +23,95% | +23,95% | -3,09% | +29,06% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 3 | 33,33% | -8,86% | +24,18% | -3,03% | +29,15% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 34 | 41,18% | -0,49% | +0,22% | -0,44% | +0,96% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 60 | 58,33% | +0,50% | +0,31% | -0,37% | +1,24% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 9 | 55,56% | +1,78% | +2,13% | +0,65% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 54 | 51,85% | +0,37% | +0,21% | -0,48% | +1,13% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 34 | 41,18% | -1,26% | +0,45% | -0,31% | +1,41% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 59 | 55,93% | +0,76% | +0,71% | -0,08% | +1,91% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,61% | +2,90% | +2,02% | +4,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 53 | 54,72% | +0,67% | +0,33% | -0,45% | +1,51% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 33 | 30,30% | -2,17% | +1,05% | -2,02% | +4,02% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 58 | 53,45% | +1,07% | +1,17% | -1,75% | +3,93% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,26% | +2,49% | -0,95% | +6,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 52 | 46,15% | +0,68% | +0,35% | -2,02% | +3,00% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 31 | 38,71% | -3,99% | +2,48% | -2,71% | +6,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 56 | 48,21% | +1,77% | +2,21% | -2,51% | +6,42% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | +1,34% | +1,54% | -1,56% | +8,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 50 | 60,00% | +0,91% | +1,17% | -2,95% | +5,39% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 31 | 38,71% | -4,80% | +2,76% | -3,30% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 54 | 53,70% | +2,47% | +2,92% | -2,99% | +8,30% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 8 | 50,00% | +0,28% | +0,41% | -2,23% | +8,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 48 | 60,42% | +1,61% | +1,58% | -3,54% | +6,88% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 31 | 41,94% | -4,39% | +2,22% | -3,95% | +9,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 51 | 52,94% | +3,18% | +2,88% | -3,67% | +9,48% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 8 | 62,50% | +0,35% | +0,72% | -3,12% | +9,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 45 | 64,44% | +1,77% | +0,92% | -4,34% | +7,15% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 31 | 48,39% | -3,87% | +3,26% | -4,53% | +11,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 47 | 72,34% | +6,72% | +4,71% | -3,92% | +12,89% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 7 | 57,14% | +2,04% | +7,65% | -2,99% | +15,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 41 | 63,41% | +1,09% | +1,51% | -4,70% | +8,65% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 27 | 55,56% | -7,10% | +7,10% | -3,69% | +15,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 41 | 87,80% | +12,96% | +10,08% | -3,28% | +20,47% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 5 | 80,00% | +2,29% | +13,05% | +0,50% | +27,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 34 | 64,71% | -3,28% | +7,26% | -3,99% | +15,79% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 22 | 50,00% | -9,38% | +9,38% | -4,86% | +19,29% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 34 | 88,24% | +11,92% | +13,27% | -4,36% | +25,97% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,03% | +30,85% | -1,31% | +42,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 30 | 40,00% | -11,60% | +11,60% | -4,76% | +23,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 16 | 0,00% | -20,67% | +20,67% | -5,92% | +37,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 19 | 15,79% | -12,96% | +20,35% | -6,16% | +37,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 19 | 0,00% | -20,35% | +20,35% | -6,16% | +37,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Classic technical | 4 | 0,00% | -21,40% | +21,40% | -7,38% | +36,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 4 | 0,00% | -21,40% | +21,40% | -7,38% | +36,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 4 | 0,00% | -21,40% | +21,40% | -7,38% | +36,23% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 42 | 50,00% | +0,45% | +0,49% | -0,33% | +1,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 56 | 55,36% | +0,31% | +0,32% | -0,34% | +1,18% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 58 | 50,00% | +0,30% | +0,32% | -0,38% | +1,15% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 41 | 51,22% | +0,85% | +0,88% | -0,05% | +1,84% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 55 | 47,27% | +0,44% | +0,88% | -0,08% | +1,71% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 57 | 43,86% | +0,25% | +0,79% | -0,11% | +1,86% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 40 | 55,00% | +1,08% | +1,21% | -1,67% | +3,42% | PESO OK | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 54 | 50,00% | +0,96% | +1,50% | -1,65% | +3,76% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 56 | 50,00% | +0,13% | +1,30% | -1,70% | +3,49% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 38 | 60,53% | +1,85% | +2,00% | -2,31% | +5,14% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 52 | 55,77% | +1,74% | +2,79% | -2,25% | +6,13% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 54 | 50,00% | -0,27% | +2,68% | -2,38% | +5,91% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 36 | 55,56% | +2,25% | +2,20% | -2,84% | +6,10% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 50 | 62,00% | +2,76% | +4,03% | -2,65% | +7,98% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 52 | 44,23% | -1,07% | +3,76% | -2,82% | +7,68% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 33 | 57,58% | +2,27% | +2,16% | -3,34% | +6,77% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 47 | 61,70% | +4,85% | +5,83% | -3,03% | +9,96% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 49 | 46,94% | -1,99% | +4,87% | -3,25% | +9,18% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 29 | 55,17% | +1,87% | +3,59% | -3,24% | +8,35% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 43 | 81,40% | +8,79% | +9,74% | -2,93% | +14,78% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 45 | 42,22% | -4,38% | +7,45% | -3,25% | +12,78% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Classic technical | 22 | 40,91% | -9,76% | +11,59% | -4,29% | +15,97% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 36 | 86,11% | +18,74% | +17,19% | -3,75% | +22,71% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 38 | 34,21% | -13,71% | +13,68% | -4,27% | +19,19% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 21 | 9,52% | -26,53% | +26,53% | -4,64% | +32,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 30 | 90,00% | +24,28% | +24,63% | -4,89% | +31,11% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +22,28% | +22,28% | -5,94% | +27,20% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 32 | 12,50% | -21,52% | +20,94% | -5,31% | +26,83% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 11 | 0,00% | -36,09% | +36,09% | -6,79% | +45,08% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 15 | 46,67% | +1,21% | +32,78% | -7,60% | +40,59% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 19 | 21,05% | -23,13% | +33,49% | -7,44% | +40,99% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 3 | 0,00% | -33,87% | +33,87% | -8,66% | +42,18% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 4 | 100,00% | +33,90% | +33,90% | -8,78% | +41,99% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 58 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 61 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 72 | 40,28% | +0,37% |
| BTC | BREVE | Famiglia statistica | 180 | 53,33% | +0,78% |
| BTC | BREVE | Microstruttura exchange | 15 | 40,00% | +0,30% |
| BTC | BREVE | Tecnico | 165 | 40,00% | +0,08% |
| BTC | SETTIMANALE | Classic technical | 67 | 52,24% | -2,52% |
| BTC | SETTIMANALE | Famiglia statistica | 164 | 60,37% | +2,91% |
| BTC | SETTIMANALE | Microstruttura exchange | 10 | 50,00% | +0,23% |
| BTC | SETTIMANALE | Tecnico | 149 | 45,64% | -1,28% |
| BTC | SWING | Classic technical | 25 | 32,00% | -8,49% |
| BTC | SWING | Famiglia statistica | 89 | 66,29% | +7,82% |
| BTC | SWING | Microstruttura exchange | 4 | 50,00% | +0,28% |
| BTC | SWING | Tecnico | 79 | 48,10% | -0,04% |
| BTC | MEDIO | Classic technical | 4 | 0,00% | -24,06% |
| BTC | MEDIO | Famiglia statistica | 57 | 91,23% | +17,40% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 47 | 40,43% | -4,05% |
| DOGE | BREVE | Classic technical | 101 | 37,62% | -1,30% |
| DOGE | BREVE | Famiglia statistica | 177 | 55,93% | +0,77% |
| DOGE | BREVE | Microstruttura exchange | 27 | 48,15% | +2,22% |
| DOGE | BREVE | Tecnico | 159 | 50,94% | +0,57% |
| DOGE | SETTIMANALE | Classic technical | 93 | 39,78% | -4,39% |
| DOGE | SETTIMANALE | Famiglia statistica | 161 | 51,55% | +2,45% |
| DOGE | SETTIMANALE | Microstruttura exchange | 24 | 50,00% | +0,65% |
| DOGE | SETTIMANALE | Tecnico | 143 | 61,54% | +1,41% |
| DOGE | SWING | Classic technical | 58 | 51,72% | -5,37% |
| DOGE | SWING | Famiglia statistica | 88 | 79,55% | +9,63% |
| DOGE | SWING | Microstruttura exchange | 12 | 66,67% | +2,15% |
| DOGE | SWING | Tecnico | 75 | 64,00% | -0,89% |
| DOGE | MEDIO | Classic technical | 42 | 26,19% | -14,83% |
| DOGE | MEDIO | Famiglia statistica | 57 | 57,89% | +1,29% |
| DOGE | MEDIO | Microstruttura exchange | 6 | 83,33% | +20,07% |
| DOGE | MEDIO | Tecnico | 53 | 22,64% | -15,47% |
| SOL | BREVE | Classic technical | 123 | 52,03% | +0,79% |
| SOL | BREVE | Famiglia statistica | 165 | 50,91% | +0,57% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 171 | 47,95% | +0,23% |
| SOL | SETTIMANALE | Classic technical | 107 | 57,94% | +2,11% |
| SOL | SETTIMANALE | Famiglia statistica | 149 | 59,73% | +3,07% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 155 | 47,10% | -1,08% |
| SOL | SWING | Classic technical | 51 | 49,02% | -3,15% |
| SOL | SWING | Famiglia statistica | 79 | 83,54% | +13,33% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 7 | 71,43% | +10,86% |
| SOL | SWING | Tecnico | 83 | 38,55% | -8,65% |
| SOL | MEDIO | Classic technical | 32 | 6,25% | -29,82% |
| SOL | MEDIO | Famiglia statistica | 48 | 70,83% | +13,43% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 3 | 100,00% | +25,70% |
| SOL | MEDIO | Tecnico | 55 | 21,82% | -18,05% |

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
