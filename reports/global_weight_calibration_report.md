# Calibrazione pesi Global Confluence

Generato: 2026-09-02 05:32 UTC

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
| BTC | 54 | PRIMA CALIBRAZIONE | 53 | 15 | 0 | 0 | Famiglia statistica | 1g | 54,72% | +0,40% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 54 | PRIMA CALIBRAZIONE | 50 | 20 | 0 | 0 | Tecnico | 1g | 52,00% | +0,31% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 54 | PRIMA CALIBRAZIONE | 52 | 21 | 0 | 0 | Famiglia statistica | 1g | 59,62% | +0,68% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 21 | 38,10% | +0,30% | +0,80% | +0,07% | +1,33% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 53 | 54,72% | +0,40% | +0,40% | -0,05% | +0,95% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 48 | 39,58% | +0,12% | +0,55% | +0,07% | +1,09% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 20 | 40,00% | +0,47% | +1,23% | +0,63% | +1,88% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 52 | 55,77% | +0,89% | +0,89% | +0,30% | +1,56% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 47 | 44,68% | +0,22% | +1,10% | +0,50% | +1,77% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 19 | 36,84% | -0,06% | +1,96% | -0,39% | +3,39% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 51 | 56,86% | +1,32% | +1,32% | -0,89% | +2,90% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 46 | 36,96% | -0,15% | +1,68% | -0,68% | +3,22% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 17 | 41,18% | -2,12% | +4,72% | -0,74% | +6,82% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 49 | 51,02% | +2,28% | +2,28% | -1,45% | +4,53% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 44 | 40,91% | -1,19% | +2,66% | -1,23% | +4,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 15 | 33,33% | -4,83% | +7,45% | -0,59% | +10,35% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 47 | 59,57% | +3,22% | +3,22% | -1,63% | +5,83% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 42 | 38,10% | -2,20% | +3,87% | -1,38% | +6,39% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 12 | 33,33% | -7,08% | +10,50% | -0,15% | +13,38% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 44 | 61,36% | +4,34% | +4,34% | -1,82% | +7,15% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | +0,69% | +0,69% | -0,88% | +5,44% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 39 | 38,46% | -1,77% | +5,05% | -1,52% | +7,91% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 8 | 25,00% | -12,28% | +12,28% | -0,83% | +16,12% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 40 | 62,50% | +6,11% | +6,11% | -2,31% | +9,47% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 35 | 57,14% | +0,24% | +7,16% | -2,00% | +10,58% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 4 | 0,00% | -11,68% | +11,68% | -1,55% | +14,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 34 | 64,71% | +7,57% | +7,57% | -3,00% | +11,24% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 29 | 37,93% | +1,92% | +8,61% | -2,74% | +12,34% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Classic technical | 4 | 0,00% | -24,06% | +24,06% | -1,55% | +28,48% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 26 | 80,77% | +11,00% | +11,00% | -2,98% | +14,99% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 21 | 28,57% | -8,42% | +10,59% | -2,63% | +15,03% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 11 | 100,00% | +22,96% | +22,96% | -2,62% | +26,80% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 10 | 40,00% | -5,30% | +23,20% | -2,56% | +27,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 31 | 41,94% | -0,51% | +0,27% | -0,38% | +0,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 52 | 59,62% | +0,68% | +0,25% | -0,39% | +1,20% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 8 | 62,50% | +2,09% | +2,48% | +0,94% | +3,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 46 | 52,17% | +0,32% | +0,14% | -0,52% | +1,07% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 51 | 56,86% | +1,13% | +0,56% | -0,19% | +1,76% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 8 | 50,00% | +3,05% | +3,38% | +2,44% | +5,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 45 | 55,56% | +0,50% | +0,09% | -0,64% | +1,27% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 31 | 32,26% | -2,13% | +1,30% | -1,89% | +4,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 50 | 56,00% | +1,67% | +0,92% | -1,78% | +3,65% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 8 | 50,00% | +2,64% | +2,90% | -0,79% | +6,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 44 | 43,18% | +0,30% | -0,08% | -2,11% | +2,52% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 31 | 38,71% | -3,99% | +2,48% | -2,71% | +6,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 48 | 54,17% | +2,79% | +1,85% | -2,52% | +6,07% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | +2,00% | +2,23% | -1,09% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 42 | 54,76% | +0,25% | +0,56% | -3,05% | +4,79% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 31 | 38,71% | -4,80% | +2,76% | -3,30% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 46 | 58,70% | +3,63% | +2,70% | -2,83% | +8,13% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | +0,24% | +0,39% | -1,74% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 40 | 57,50% | +1,09% | +1,06% | -3,46% | +6,40% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 29 | 44,83% | -4,12% | +2,95% | -3,35% | +9,95% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 44 | 61,36% | +4,61% | +3,17% | -3,00% | +9,92% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 6 | 66,67% | +1,21% | +1,71% | -1,24% | +10,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 37 | 64,86% | +1,99% | +0,95% | -3,59% | +7,32% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 27 | 51,85% | -4,09% | +4,09% | -3,41% | +12,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 40 | 75,00% | +7,73% | +5,39% | -3,35% | +13,24% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 4 | 75,00% | +2,65% | +12,47% | -1,31% | +16,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 33 | 66,67% | +1,05% | +1,58% | -4,09% | +8,18% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 22 | 68,18% | -2,23% | +2,23% | -4,78% | +9,45% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 34 | 85,29% | +10,34% | +6,86% | -4,31% | +16,06% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 4 | 75,00% | -0,95% | +12,49% | -1,31% | +25,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 30 | 63,33% | -5,01% | +5,01% | -4,70% | +12,46% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 20 | 55,00% | -7,30% | +7,30% | -5,27% | +16,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 26 | 84,62% | +7,69% | +9,45% | -5,24% | +20,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 26 | 46,15% | -9,45% | +9,45% | -5,24% | +20,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 10 | 0,00% | -19,37% | +19,37% | -6,60% | +36,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 11 | 0,00% | -18,98% | +18,98% | -6,73% | +36,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 11 | 0,00% | -18,98% | +18,98% | -6,73% | +36,47% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 34 | 52,94% | +0,50% | +0,55% | -0,24% | +1,51% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 48 | 58,33% | +0,32% | +0,33% | -0,28% | +1,23% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 50 | 52,00% | +0,31% | +0,33% | -0,32% | +1,19% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 33 | 51,52% | +0,99% | +1,02% | +0,13% | +2,00% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 47 | 46,81% | +0,47% | +0,99% | +0,05% | +1,80% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 49 | 42,86% | +0,25% | +0,87% | +0,01% | +1,97% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 32 | 56,25% | +1,26% | +1,43% | -1,49% | +3,61% | PESO OK | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 46 | 50,00% | +1,06% | +1,70% | -1,52% | +3,95% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 48 | 50,00% | +0,09% | +1,45% | -1,58% | +3,62% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 30 | 63,33% | +2,16% | +2,35% | -2,00% | +5,51% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 44 | 56,82% | +1,94% | +3,18% | -2,02% | +6,57% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 46 | 50,00% | -0,44% | +3,03% | -2,20% | +6,28% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 28 | 57,14% | +2,76% | +2,69% | -2,36% | +6,58% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 42 | 64,29% | +3,20% | +4,71% | -2,30% | +8,65% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 44 | 43,18% | -1,35% | +4,35% | -2,51% | +8,28% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 25 | 60,00% | +2,37% | +2,22% | -2,99% | +6,63% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 39 | 64,10% | +5,45% | +6,62% | -2,74% | +10,53% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +3,45% | +3,45% | -2,62% | +8,30% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 41 | 46,34% | -2,76% | +5,44% | -3,02% | +9,57% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 36 | 86,11% | +10,98% | +9,94% | -3,28% | +14,70% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 37 | 29,73% | -7,47% | +6,92% | -3,83% | +11,87% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 30 | 83,33% | +14,96% | +13,10% | -4,70% | +18,17% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 32 | 37,50% | -10,96% | +9,67% | -5,06% | +14,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 18 | 11,11% | -24,17% | +24,17% | -5,27% | +30,07% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 22 | 86,36% | +19,08% | +19,56% | -6,09% | +25,16% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 26 | 15,38% | -17,34% | +16,62% | -6,21% | +21,88% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Classic technical | 4 | 0,00% | -36,37% | +36,37% | -6,39% | +45,71% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 8 | 12,50% | -21,42% | +29,92% | -7,77% | +37,49% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 11 | 36,36% | -14,12% | +32,02% | -7,51% | +38,64% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 50 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 53 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 60 | 38,33% | +0,24% |
| BTC | BREVE | Famiglia statistica | 156 | 55,77% | +0,87% |
| BTC | BREVE | Microstruttura exchange | 9 | 66,67% | +1,28% |
| BTC | BREVE | Tecnico | 141 | 40,43% | +0,06% |
| BTC | SETTIMANALE | Classic technical | 44 | 36,36% | -4,39% |
| BTC | SETTIMANALE | Famiglia statistica | 140 | 57,14% | +3,24% |
| BTC | SETTIMANALE | Microstruttura exchange | 8 | 50,00% | +0,56% |
| BTC | SETTIMANALE | Tecnico | 125 | 39,20% | -1,71% |
| BTC | SWING | Classic technical | 12 | 16,67% | -12,08% |
| BTC | SWING | Famiglia statistica | 74 | 63,51% | +6,78% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 64 | 48,44% | +1,00% |
| BTC | MEDIO | Classic technical | 4 | 0,00% | -24,06% |
| BTC | MEDIO | Famiglia statistica | 37 | 86,49% | +14,55% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 31 | 32,26% | -7,42% |
| DOGE | BREVE | Classic technical | 93 | 39,78% | -1,28% |
| DOGE | BREVE | Famiglia statistica | 153 | 57,52% | +1,16% |
| DOGE | BREVE | Microstruttura exchange | 24 | 54,17% | +2,59% |
| DOGE | BREVE | Tecnico | 135 | 50,37% | +0,38% |
| DOGE | SETTIMANALE | Classic technical | 91 | 40,66% | -4,31% |
| DOGE | SETTIMANALE | Famiglia statistica | 138 | 57,97% | +3,65% |
| DOGE | SETTIMANALE | Microstruttura exchange | 20 | 50,00% | +1,15% |
| DOGE | SETTIMANALE | Tecnico | 119 | 58,82% | +1,07% |
| DOGE | SWING | Classic technical | 49 | 59,18% | -3,25% |
| DOGE | SWING | Famiglia statistica | 74 | 79,73% | +8,93% |
| DOGE | SWING | Microstruttura exchange | 8 | 75,00% | +0,85% |
| DOGE | SWING | Tecnico | 63 | 65,08% | -1,84% |
| DOGE | MEDIO | Classic technical | 30 | 36,67% | -11,32% |
| DOGE | MEDIO | Famiglia statistica | 37 | 59,46% | -0,24% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 37 | 32,43% | -12,29% |
| SOL | BREVE | Classic technical | 99 | 53,54% | +0,91% |
| SOL | BREVE | Famiglia statistica | 141 | 51,77% | +0,61% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 147 | 48,30% | +0,22% |
| SOL | SETTIMANALE | Classic technical | 83 | 60,24% | +2,42% |
| SOL | SETTIMANALE | Famiglia statistica | 125 | 61,60% | +3,46% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 13 | 61,54% | +3,01% |
| SOL | SETTIMANALE | Tecnico | 131 | 46,56% | -1,47% |
| SOL | SWING | Classic technical | 42 | 38,10% | -6,19% |
| SOL | SWING | Famiglia statistica | 66 | 84,85% | +12,79% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 4 | 50,00% | +12,98% |
| SOL | SWING | Tecnico | 69 | 33,33% | -9,09% |
| SOL | MEDIO | Classic technical | 22 | 9,09% | -26,39% |
| SOL | MEDIO | Famiglia statistica | 30 | 66,67% | +8,28% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 37 | 21,62% | -16,38% |

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
