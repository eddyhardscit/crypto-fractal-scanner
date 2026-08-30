# Calibrazione pesi Global Confluence

Generato: 2026-08-30 05:33 UTC

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
| BTC | 51 | PRIMA CALIBRAZIONE | 50 | 15 | 0 | 0 | Famiglia statistica | 1g | 56,00% | +0,44% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 51 | PRIMA CALIBRAZIONE | 47 | 17 | 0 | 0 | Tecnico | 1g | 53,19% | +0,42% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 51 | PRIMA CALIBRAZIONE | 49 | 20 | 0 | 0 | Famiglia statistica | 1g | 59,18% | +0,64% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 18 | 38,89% | +0,38% | +0,97% | +0,28% | +1,57% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 50 | 56,00% | +0,44% | +0,44% | +0,02% | +1,01% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 45 | 40,00% | +0,14% | +0,60% | +0,15% | +1,17% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 17 | 35,29% | +0,48% | +1,38% | +0,84% | +2,14% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 49 | 55,10% | +0,92% | +0,92% | +0,36% | +1,63% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 44 | 43,18% | +0,21% | +1,15% | +0,58% | +1,86% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 16 | 37,50% | -0,01% | +2,39% | -0,12% | +3,93% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 48 | 58,33% | +1,43% | +1,43% | -0,83% | +3,05% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 43 | 37,21% | -0,14% | +1,82% | -0,60% | +3,41% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 14 | 42,86% | -2,32% | +5,98% | -0,28% | +7,86% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 46 | 52,17% | +2,50% | +2,50% | -1,36% | +4,70% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 41 | 41,46% | -1,19% | +2,94% | -1,11% | +5,19% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 12 | 33,33% | -5,81% | +9,54% | -0,09% | +12,17% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 44 | 61,36% | +3,50% | +3,50% | -1,57% | +6,02% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +2,11% | +2,11% | -0,13% | +5,37% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 39 | 38,46% | -2,30% | +4,24% | -1,28% | +6,65% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 9 | 11,11% | -10,35% | +13,10% | -0,13% | +15,57% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 41 | 58,54% | +4,46% | +4,46% | -1,94% | +7,17% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 36 | 33,33% | -2,14% | +5,24% | -1,63% | +8,00% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 7 | 28,57% | -10,76% | +10,76% | -1,07% | +14,38% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 37 | 59,46% | +4,79% | +4,79% | -2,71% | +8,03% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 32 | 59,38% | +1,05% | +5,74% | -2,43% | +9,02% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 4 | 0,00% | -11,68% | +11,68% | -1,55% | +14,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 32 | 62,50% | +6,68% | +6,68% | -3,00% | +10,30% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 27 | 33,33% | +0,44% | +7,63% | -2,73% | +11,30% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Classic technical | 2 | 0,00% | -24,39% | +24,39% | -2,23% | +27,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 23 | 78,26% | +9,30% | +9,30% | -3,22% | +13,16% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 18 | 33,33% | -5,82% | +8,35% | -2,87% | +12,70% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 8 | 100,00% | +23,29% | +23,29% | -2,52% | +26,75% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 7 | 42,86% | -3,82% | +23,69% | -2,41% | +27,08% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 31 | 41,94% | -0,51% | +0,27% | -0,38% | +0,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 49 | 59,18% | +0,64% | +0,34% | -0,25% | +1,35% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 8 | 62,50% | +2,09% | +2,48% | +0,94% | +3,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 43 | 53,49% | +0,43% | +0,23% | -0,38% | +1,23% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 48 | 54,17% | +1,09% | +0,72% | -0,00% | +1,99% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 7 | 57,14% | +3,88% | +4,25% | +3,39% | +6,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 42 | 59,52% | +0,67% | +0,23% | -0,45% | +1,49% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 31 | 32,26% | -2,13% | +1,30% | -1,89% | +4,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 47 | 53,19% | +1,55% | +1,22% | -1,54% | +4,00% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 7 | 57,14% | +3,29% | +3,59% | -0,23% | +7,51% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 41 | 46,34% | +0,60% | +0,19% | -1,85% | +2,83% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 31 | 38,71% | -3,99% | +2,48% | -2,71% | +6,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 46 | 52,17% | +2,70% | +2,15% | -2,33% | +6,26% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | +2,00% | +2,23% | -1,09% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 39 | 58,97% | +0,63% | +0,96% | -2,77% | +4,97% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 29 | 41,38% | -4,44% | +3,64% | -2,71% | +8,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 44 | 61,36% | +4,25% | +3,28% | -2,42% | +8,54% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 6 | 50,00% | +1,90% | +2,08% | -0,18% | +10,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 37 | 62,16% | +1,87% | +1,84% | -2,90% | +6,87% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 27 | 48,15% | -3,79% | +3,79% | -2,82% | +10,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 41 | 63,41% | +5,35% | +3,81% | -2,67% | +9,94% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +2,95% | +3,56% | +0,53% | +11,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 34 | 67,65% | +2,65% | +1,53% | -3,26% | +7,11% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 24 | 58,33% | -2,31% | +2,31% | -4,08% | +8,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 37 | 72,97% | +6,87% | +4,34% | -3,79% | +10,83% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 4 | 75,00% | +2,65% | +12,47% | -1,31% | +16,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 32 | 68,75% | +1,65% | +1,06% | -4,20% | +7,10% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 22 | 68,18% | -2,23% | +2,23% | -4,78% | +9,45% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 32 | 84,38% | +9,79% | +6,10% | -4,50% | +14,37% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 4 | 75,00% | -0,95% | +12,49% | -1,31% | +25,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 30 | 63,33% | -5,01% | +5,01% | -4,70% | +12,46% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 19 | 57,89% | -6,73% | +6,73% | -5,42% | +15,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 23 | 82,61% | +6,34% | +8,32% | -5,61% | +17,80% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 23 | 52,17% | -8,32% | +8,32% | -5,61% | +17,80% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 7 | 0,00% | -21,50% | +21,50% | -6,85% | +35,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 8 | 0,00% | -20,70% | +20,70% | -7,00% | +35,80% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 8 | 0,00% | -20,70% | +20,70% | -7,00% | +35,80% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 31 | 54,84% | +0,69% | +0,75% | +0,01% | +1,80% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 45 | 60,00% | +0,44% | +0,45% | -0,11% | +1,41% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 47 | 53,19% | +0,42% | +0,45% | -0,16% | +1,35% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 30 | 56,67% | +1,24% | +1,27% | +0,43% | +2,33% | PESO OK | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 44 | 50,00% | +0,61% | +1,16% | +0,24% | +2,01% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 46 | 45,65% | +0,36% | +1,03% | +0,19% | +2,19% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 29 | 58,62% | +1,67% | +1,86% | -1,15% | +4,00% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 43 | 51,16% | +1,33% | +2,01% | -1,29% | +4,24% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 45 | 51,11% | +0,27% | +1,73% | -1,37% | +3,88% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 27 | 62,96% | +2,29% | +2,50% | -2,09% | +5,27% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 41 | 56,10% | +2,01% | +3,33% | -2,08% | +6,48% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +1,53% | +1,53% | -3,22% | +5,77% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 43 | 48,84% | -0,54% | +3,17% | -2,26% | +6,18% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 25 | 52,00% | +2,51% | +2,44% | -2,50% | +5,84% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 39 | 61,54% | +3,08% | +4,70% | -2,39% | +8,34% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +3,96% | +3,96% | -2,17% | +8,29% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 41 | 39,02% | -1,80% | +4,32% | -2,61% | +7,95% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 22 | 54,55% | +1,16% | +1,00% | -3,42% | +4,86% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 36 | 69,44% | +6,84% | +6,24% | -2,98% | +9,77% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 38 | 42,11% | -3,86% | +4,99% | -3,27% | +8,77% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 33 | 84,85% | +8,82% | +7,69% | -3,89% | +11,96% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 35 | 31,43% | -5,80% | +5,22% | -4,08% | +9,94% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 28 | 82,14% | +13,48% | +11,48% | -4,85% | +16,29% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 31 | 38,71% | -10,22% | +8,89% | -5,12% | +13,76% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 15 | 13,33% | -21,04% | +21,04% | -6,02% | +26,01% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 19 | 84,21% | +15,80% | +16,36% | -6,82% | +21,17% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 23 | 17,39% | -14,41% | +13,59% | -6,82% | +18,16% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Classic technical | 1 | 0,00% | -38,21% | +38,21% | -6,98% | +44,79% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 6 | 16,67% | -17,16% | +28,50% | -8,21% | +34,79% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 8 | 50,00% | -6,01% | +30,61% | -8,00% | +35,87% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 47 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 50 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 51 | 37,25% | +0,29% |
| BTC | BREVE | Famiglia statistica | 147 | 56,46% | +0,92% |
| BTC | BREVE | Microstruttura exchange | 9 | 66,67% | +1,28% |
| BTC | BREVE | Tecnico | 132 | 40,15% | +0,07% |
| BTC | SETTIMANALE | Classic technical | 35 | 31,43% | -5,58% |
| BTC | SETTIMANALE | Famiglia statistica | 131 | 57,25% | +3,45% |
| BTC | SETTIMANALE | Microstruttura exchange | 6 | 50,00% | +0,81% |
| BTC | SETTIMANALE | Tecnico | 116 | 37,93% | -1,86% |
| BTC | SWING | Classic technical | 11 | 18,18% | -11,09% |
| BTC | SWING | Famiglia statistica | 69 | 60,87% | +5,67% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 59 | 47,46% | +0,77% |
| BTC | MEDIO | Classic technical | 2 | 0,00% | -24,39% |
| BTC | MEDIO | Famiglia statistica | 31 | 83,87% | +12,91% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 25 | 36,00% | -5,26% |
| DOGE | BREVE | Classic technical | 93 | 39,78% | -1,28% |
| DOGE | BREVE | Famiglia statistica | 144 | 55,56% | +1,09% |
| DOGE | BREVE | Microstruttura exchange | 22 | 59,09% | +3,04% |
| DOGE | BREVE | Tecnico | 126 | 53,17% | +0,57% |
| DOGE | SETTIMANALE | Classic technical | 87 | 42,53% | -4,08% |
| DOGE | SETTIMANALE | Famiglia statistica | 131 | 58,78% | +4,05% |
| DOGE | SETTIMANALE | Microstruttura exchange | 18 | 55,56% | +2,23% |
| DOGE | SETTIMANALE | Tecnico | 110 | 62,73% | +1,67% |
| DOGE | SWING | Classic technical | 46 | 63,04% | -2,27% |
| DOGE | SWING | Famiglia statistica | 69 | 78,26% | +8,23% |
| DOGE | SWING | Microstruttura exchange | 8 | 75,00% | +0,85% |
| DOGE | SWING | Tecnico | 62 | 66,13% | -1,57% |
| DOGE | MEDIO | Classic technical | 26 | 42,31% | -10,71% |
| DOGE | MEDIO | Famiglia statistica | 31 | 61,29% | -0,64% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 31 | 38,71% | -11,52% |
| SOL | BREVE | Classic technical | 90 | 56,67% | +1,19% |
| SOL | BREVE | Famiglia statistica | 132 | 53,79% | +0,78% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 138 | 50,00% | +0,35% |
| SOL | SETTIMANALE | Classic technical | 74 | 56,76% | +2,03% |
| SOL | SETTIMANALE | Famiglia statistica | 116 | 62,07% | +3,87% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 9 | 44,44% | +1,54% |
| SOL | SETTIMANALE | Tecnico | 122 | 43,44% | -2,00% |
| SOL | SWING | Classic technical | 42 | 38,10% | -6,19% |
| SOL | SWING | Famiglia statistica | 61 | 83,61% | +10,96% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 4 | 50,00% | +12,98% |
| SOL | SWING | Tecnico | 66 | 34,85% | -7,87% |
| SOL | MEDIO | Classic technical | 16 | 12,50% | -22,12% |
| SOL | MEDIO | Famiglia statistica | 25 | 68,00% | +7,89% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 31 | 25,81% | -12,24% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 9 | in attesa di controlli maturati |
| SOL | MEDIO | 6 | in attesa di controlli maturati |
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
