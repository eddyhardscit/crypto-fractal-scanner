# Calibrazione pesi Global Confluence

Generato: 2026-08-29 05:33 UTC

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
| BTC | 50 | PRIMA CALIBRAZIONE | 49 | 15 | 0 | 0 | Famiglia statistica | 1g | 55,10% | +0,44% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 50 | PRIMA CALIBRAZIONE | 46 | 16 | 0 | 0 | Tecnico | 1g | 52,17% | +0,41% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 50 | PRIMA CALIBRAZIONE | 48 | 20 | 0 | 0 | Famiglia statistica | 1g | 58,33% | +0,66% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 17 | 35,29% | +0,37% | +0,99% | +0,27% | +1,62% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 49 | 55,10% | +0,44% | +0,44% | +0,01% | +1,02% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 44 | 38,64% | +0,13% | +0,60% | +0,15% | +1,18% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 16 | 37,50% | +0,64% | +1,59% | +1,03% | +2,39% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 48 | 56,25% | +0,98% | +0,98% | +0,41% | +1,70% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 43 | 44,19% | +0,26% | +1,22% | +0,64% | +1,94% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 15 | 40,00% | +0,03% | +2,59% | -0,08% | +4,22% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 47 | 59,57% | +1,47% | +1,47% | -0,83% | +3,12% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 42 | 38,10% | -0,13% | +1,88% | -0,60% | +3,50% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 13 | 46,15% | -2,25% | +6,69% | -0,01% | +8,46% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 45 | 53,33% | +2,63% | +2,63% | -1,30% | +4,81% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | +2,17% | +2,17% | +0,08% | +5,37% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 40 | 42,50% | -1,14% | +3,10% | -1,04% | +5,31% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 11 | 27,27% | -6,56% | +10,18% | -0,15% | +12,69% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 43 | 60,47% | +3,52% | +3,52% | -1,62% | +6,01% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 38 | 36,84% | -2,43% | +4,28% | -1,33% | +6,65% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 8 | 0,00% | -13,19% | +13,19% | -0,77% | +15,42% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 40 | 57,50% | +4,27% | +4,27% | -2,11% | +6,93% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 35 | 31,43% | -2,56% | +5,04% | -1,82% | +7,75% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 6 | 33,33% | -8,54% | +8,54% | -1,17% | +11,96% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 36 | 58,33% | +4,26% | +4,26% | -2,77% | +7,45% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 31 | 61,29% | +1,86% | +5,15% | -2,49% | +8,38% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 4 | 0,00% | -11,68% | +11,68% | -1,55% | +14,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 31 | 61,29% | +6,23% | +6,23% | -2,98% | +9,81% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 26 | 30,77% | -0,34% | +7,12% | -2,70% | +10,76% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Classic technical | 2 | 0,00% | -24,39% | +24,39% | -2,23% | +27,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 22 | 77,27% | +8,74% | +8,74% | -3,21% | +12,56% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 18 | 33,33% | -5,82% | +8,35% | -2,87% | +12,70% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 7 | 100,00% | +23,47% | +23,47% | -2,47% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 6 | 50,00% | -0,78% | +23,96% | -2,34% | +27,12% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 31 | 41,94% | -0,51% | +0,27% | -0,38% | +0,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 48 | 58,33% | +0,66% | +0,35% | -0,25% | +1,37% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 7 | 71,43% | +2,41% | +2,86% | +1,15% | +3,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 42 | 54,76% | +0,44% | +0,24% | -0,37% | +1,26% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 47 | 53,19% | +1,05% | +0,79% | +0,07% | +2,08% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 7 | 57,14% | +3,88% | +4,25% | +3,39% | +6,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 41 | 60,98% | +0,76% | +0,31% | -0,38% | +1,59% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 31 | 32,26% | -2,13% | +1,30% | -1,89% | +4,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 46 | 52,17% | +1,55% | +1,28% | -1,53% | +4,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 7 | 57,14% | +3,29% | +3,59% | -0,23% | +7,51% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 40 | 47,50% | +0,65% | +0,23% | -1,85% | +2,92% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 30 | 40,00% | -3,84% | +2,85% | -2,48% | +7,04% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 45 | 53,33% | +2,95% | +2,38% | -2,17% | +6,47% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | +2,00% | +2,23% | -1,09% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 38 | 60,53% | +0,88% | +1,22% | -2,59% | +5,19% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 28 | 42,86% | -4,39% | +3,98% | -2,55% | +8,97% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 43 | 62,79% | +4,49% | +3,50% | -2,31% | +8,67% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 6 | 50,00% | +1,90% | +2,08% | -0,18% | +10,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 36 | 63,89% | +2,09% | +2,05% | -2,79% | +6,97% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 27 | 48,15% | -3,79% | +3,79% | -2,82% | +10,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 40 | 62,50% | +5,14% | +3,55% | -2,94% | +9,34% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 4 | 75,00% | +0,18% | +0,93% | -1,31% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 33 | 66,67% | +2,31% | +1,15% | -3,59% | +6,29% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 23 | 60,87% | -1,45% | +1,45% | -4,25% | +6,95% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 36 | 72,22% | +6,45% | +3,85% | -3,88% | +9,92% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 4 | 75,00% | +2,65% | +12,47% | -1,31% | +16,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 31 | 67,74% | +0,99% | +0,38% | -4,33% | +5,92% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 21 | 71,43% | -1,31% | +1,31% | -4,94% | +7,86% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 31 | 83,87% | +9,42% | +5,60% | -4,60% | +13,44% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 3 | 66,67% | -8,45% | +9,47% | -1,27% | +19,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 30 | 63,33% | -5,01% | +5,01% | -4,70% | +12,46% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 18 | 61,11% | -5,92% | +5,92% | -5,55% | +13,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 22 | 81,82% | +5,65% | +7,73% | -5,72% | +16,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 22 | 54,55% | -7,73% | +7,73% | -5,72% | +16,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 6 | 0,00% | -22,35% | +22,35% | -6,84% | +35,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 7 | 0,00% | -21,32% | +21,32% | -7,01% | +35,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 7 | 0,00% | -21,32% | +21,32% | -7,01% | +35,64% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 30 | 53,33% | +0,68% | +0,74% | -0,01% | +1,80% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 44 | 59,09% | +0,42% | +0,44% | -0,13% | +1,40% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 46 | 52,17% | +0,41% | +0,44% | -0,18% | +1,35% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 29 | 58,62% | +1,34% | +1,37% | +0,50% | +2,45% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 43 | 51,16% | +0,66% | +1,22% | +0,29% | +2,08% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 45 | 46,67% | +0,40% | +1,08% | +0,24% | +2,26% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 28 | 57,14% | +1,58% | +1,77% | -1,33% | +3,98% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 42 | 50,00% | +1,26% | +1,96% | -1,42% | +4,23% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 44 | 50,00% | +0,19% | +1,68% | -1,49% | +3,85% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 26 | 61,54% | +2,28% | +2,50% | -1,90% | +5,18% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 40 | 55,00% | +1,99% | +3,35% | -1,96% | +6,46% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +1,18% | +1,18% | -1,95% | +5,20% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 42 | 47,62% | -0,61% | +3,18% | -2,15% | +6,15% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 24 | 50,00% | +2,08% | +2,00% | -2,62% | +5,32% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 38 | 63,16% | +3,50% | +4,49% | -2,46% | +8,08% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +3,96% | +3,96% | -2,17% | +8,29% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 40 | 37,50% | -2,16% | +4,11% | -2,68% | +7,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 36 | 69,44% | +6,84% | +6,24% | -2,98% | +9,77% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 37 | 40,54% | -4,61% | +4,48% | -3,45% | +8,21% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 32 | 84,38% | +7,87% | +6,70% | -3,97% | +10,90% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 34 | 32,35% | -4,81% | +4,21% | -4,16% | +8,88% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 27 | 81,48% | +12,56% | +10,49% | -4,95% | +15,23% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 31 | 38,71% | -10,22% | +8,89% | -5,12% | +13,76% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 14 | 14,29% | -19,55% | +19,55% | -6,13% | +24,39% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 18 | 83,33% | +14,35% | +14,94% | -6,94% | +19,65% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 22 | 18,18% | -13,16% | +12,31% | -6,93% | +16,77% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 5 | 20,00% | -12,96% | +26,56% | -8,45% | +32,79% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 7 | 57,14% | -1,41% | +29,53% | -8,15% | +34,59% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 46 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 49 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 48 | 37,50% | +0,35% |
| BTC | BREVE | Famiglia statistica | 144 | 56,94% | +0,96% |
| BTC | BREVE | Microstruttura exchange | 9 | 66,67% | +1,28% |
| BTC | BREVE | Tecnico | 129 | 40,31% | +0,09% |
| BTC | SETTIMANALE | Classic technical | 32 | 28,12% | -6,47% |
| BTC | SETTIMANALE | Famiglia statistica | 128 | 57,03% | +3,44% |
| BTC | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +1,42% |
| BTC | SETTIMANALE | Tecnico | 113 | 37,17% | -2,01% |
| BTC | SWING | Classic technical | 10 | 20,00% | -9,80% |
| BTC | SWING | Famiglia statistica | 67 | 59,70% | +5,17% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 57 | 47,37% | +0,86% |
| BTC | MEDIO | Classic technical | 2 | 0,00% | -24,39% |
| BTC | MEDIO | Famiglia statistica | 29 | 82,76% | +12,30% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 24 | 37,50% | -4,56% |
| DOGE | BREVE | Classic technical | 93 | 39,78% | -1,28% |
| DOGE | BREVE | Famiglia statistica | 141 | 54,61% | +1,08% |
| DOGE | BREVE | Microstruttura exchange | 21 | 61,90% | +3,19% |
| DOGE | BREVE | Tecnico | 123 | 54,47% | +0,62% |
| DOGE | SETTIMANALE | Classic technical | 85 | 43,53% | -4,00% |
| DOGE | SETTIMANALE | Famiglia statistica | 128 | 59,38% | +4,15% |
| DOGE | SETTIMANALE | Microstruttura exchange | 17 | 52,94% | +1,54% |
| DOGE | SETTIMANALE | Tecnico | 107 | 63,55% | +1,72% |
| DOGE | SWING | Classic technical | 44 | 65,91% | -1,38% |
| DOGE | SWING | Famiglia statistica | 67 | 77,61% | +7,82% |
| DOGE | SWING | Microstruttura exchange | 7 | 71,43% | -2,11% |
| DOGE | SWING | Tecnico | 61 | 65,57% | -1,96% |
| DOGE | MEDIO | Classic technical | 24 | 45,83% | -10,03% |
| DOGE | MEDIO | Famiglia statistica | 29 | 62,07% | -0,86% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 29 | 41,38% | -11,01% |
| SOL | BREVE | Classic technical | 87 | 56,32% | +1,19% |
| SOL | BREVE | Famiglia statistica | 129 | 53,49% | +0,77% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 135 | 49,63% | +0,33% |
| SOL | SETTIMANALE | Classic technical | 71 | 54,93% | +1,56% |
| SOL | SETTIMANALE | Famiglia statistica | 114 | 62,28% | +4,02% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | +1,41% |
| SOL | SETTIMANALE | Tecnico | 119 | 42,02% | -2,38% |
| SOL | SWING | Classic technical | 42 | 38,10% | -6,19% |
| SOL | SWING | Famiglia statistica | 59 | 83,05% | +10,01% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 3 | 33,33% | +4,53% |
| SOL | SWING | Tecnico | 65 | 35,38% | -7,39% |
| SOL | MEDIO | Classic technical | 14 | 14,29% | -19,55% |
| SOL | MEDIO | Famiglia statistica | 23 | 69,57% | +8,42% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 29 | 27,59% | -10,32% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 9 | in attesa di controlli maturati |
| SOL | MEDIO | 7 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 2 | in attesa di controlli maturati |
| DOGE | MEDIO | 8 | in attesa di controlli maturati |

## Come leggere le raccomandazioni

- **OSSERVA**: meno di 30 controlli, nessuna modifica.
- **PESO OK / MANTIENI**: il modulo sta aiutando, ma non serve cambiare peso.
- **NON AUMENTARE**: il modulo non dimostra ancora un vantaggio sufficiente.
- **POSSIBILE AUMENTO LEGGERO**: proposta prudente, mai automatica.
- **POSSIBILE RIDUZIONE**: modulo debole con campione già abbastanza maturo.
- **ESCLUSO**: benchmark o diagnostica già inclusa in un'altra famiglia.

Nota decisiva: **non sommare mai una modifica alla Famiglia statistica e altre modifiche separate a Scanner o Market Regime**. Scanner e Market servono soltanto a capire quale parte della famiglia sta funzionando o fallendo.

## Stato attuale

È iniziata la prima calibrazione, ma sono ammesse solo valutazioni leggere e manuali.
