# Calibrazione pesi Global Confluence

Generato: 2026-09-07 05:32 UTC

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
| BTC | 59 | PRIMA CALIBRAZIONE | 58 | 17 | 0 | 0 | Famiglia statistica | 1g | 53,45% | +0,42% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 59 | PRIMA CALIBRAZIONE | 55 | 23 | 0 | 0 | Tecnico | 1g | 50,91% | +0,37% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 59 | PRIMA CALIBRAZIONE | 57 | 25 | 0 | 0 | Famiglia statistica | 1g | 57,89% | +0,44% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 24 | 37,50% | +0,37% | +0,81% | +0,13% | +1,33% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 58 | 53,45% | +0,42% | +0,42% | -0,02% | +0,95% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 53 | 39,62% | +0,16% | +0,55% | +0,09% | +1,09% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 24 | 41,67% | +0,55% | +1,18% | +0,59% | +1,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 57 | 56,14% | +0,88% | +0,88% | +0,30% | +1,57% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,27% | +1,27% | +0,55% | +1,72% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 52 | 46,15% | +0,27% | +1,07% | +0,48% | +1,76% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 24 | 41,67% | +0,20% | +1,81% | -0,58% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 56 | 57,14% | +1,31% | +1,31% | -0,93% | +2,91% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 4 | 50,00% | +0,72% | +0,72% | -0,94% | +2,21% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 51 | 39,22% | -0,02% | +1,64% | -0,74% | +3,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 22 | 50,00% | -1,22% | +4,06% | -1,06% | +6,26% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 54 | 53,70% | +2,24% | +2,24% | -1,52% | +4,52% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 49 | 44,90% | -0,88% | +2,58% | -1,32% | +4,90% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 20 | 45,00% | -3,27% | +5,94% | -1,13% | +8,88% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 52 | 61,54% | +3,05% | +3,05% | -1,74% | +5,70% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 47 | 42,55% | -1,82% | +3,61% | -1,52% | +6,19% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 17 | 52,94% | -4,82% | +7,60% | -1,13% | +10,52% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 49 | 65,31% | +3,96% | +3,96% | -1,99% | +6,79% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 44 | 45,45% | -1,50% | +4,55% | -1,74% | +7,43% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 13 | 53,85% | -5,20% | +9,92% | -0,30% | +13,51% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 45 | 66,67% | +6,11% | +6,11% | -1,99% | +9,45% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +1,23% | +1,23% | -1,55% | +6,04% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 40 | 62,50% | +0,98% | +7,03% | -1,68% | +10,43% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 8 | 0,00% | -19,34% | +19,34% | -0,83% | +22,19% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 38 | 68,42% | +9,62% | +9,62% | -2,69% | +13,22% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 33 | 33,33% | -1,59% | +10,84% | -2,43% | +14,49% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 4 | 0,00% | -24,06% | +24,06% | -1,55% | +28,48% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 31 | 83,87% | +13,01% | +13,01% | -2,98% | +16,95% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 26 | 38,46% | -4,29% | +13,07% | -2,70% | +17,36% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 16 | 100,00% | +22,58% | +22,58% | -3,28% | +26,36% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 13 | 30,77% | -9,06% | +22,83% | -2,94% | +26,83% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 1 | 100,00% | +26,24% | +26,24% | -2,32% | +30,09% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 1 | 0,00% | -26,24% | +26,24% | -2,32% | +30,09% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 32 | 40,62% | -0,51% | +0,24% | -0,42% | +0,95% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 57 | 57,89% | +0,44% | +0,41% | -0,27% | +1,35% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 9 | 55,56% | +1,78% | +2,13% | +0,65% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 51 | 52,94% | +0,49% | +0,32% | -0,38% | +1,25% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 56 | 53,57% | +0,70% | +0,85% | +0,05% | +2,07% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 8 | 50,00% | +3,05% | +3,38% | +2,44% | +5,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 50 | 58,00% | +0,83% | +0,46% | -0,32% | +1,66% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 31 | 32,26% | -2,13% | +1,30% | -1,89% | +4,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 55 | 52,73% | +1,12% | +1,25% | -1,76% | +3,97% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 8 | 50,00% | +2,64% | +2,90% | -0,79% | +6,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 49 | 46,94% | +0,73% | +0,38% | -2,05% | +2,99% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 31 | 38,71% | -3,99% | +2,48% | -2,71% | +6,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 53 | 50,94% | +2,12% | +2,08% | -2,63% | +6,21% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | +1,34% | +1,54% | -1,56% | +8,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 47 | 57,45% | +0,68% | +0,95% | -3,11% | +5,09% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 31 | 38,71% | -4,80% | +2,76% | -3,30% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 51 | 56,86% | +3,06% | +2,66% | -3,12% | +7,96% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 8 | 50,00% | +0,28% | +0,41% | -2,23% | +8,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 45 | 57,78% | +1,22% | +1,19% | -3,72% | +6,40% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 31 | 41,94% | -4,39% | +2,22% | -3,95% | +9,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 48 | 56,25% | +3,70% | +2,73% | -3,60% | +9,34% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 7 | 57,14% | -0,43% | +0,00% | -2,75% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 42 | 61,90% | +1,52% | +0,61% | -4,31% | +6,82% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 30 | 50,00% | -3,89% | +3,47% | -4,22% | +11,44% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 45 | 73,33% | +7,08% | +5,00% | -3,64% | +13,23% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 7 | 57,14% | +2,04% | +7,65% | -2,99% | +15,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 38 | 65,79% | +1,16% | +1,62% | -4,34% | +8,83% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 25 | 60,00% | -5,34% | +5,34% | -4,25% | +13,53% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 38 | 86,84% | +12,06% | +8,94% | -3,92% | +18,92% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 4 | 75,00% | -0,95% | +12,49% | -1,31% | +25,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 33 | 63,64% | -3,84% | +7,02% | -4,34% | +15,23% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 21 | 52,38% | -8,46% | +8,46% | -5,03% | +18,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 31 | 87,10% | +10,47% | +11,94% | -4,66% | +24,30% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 3 | 66,67% | +10,47% | +31,57% | -1,27% | +41,74% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 30 | 40,00% | -11,60% | +11,60% | -4,76% | +23,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 15 | 0,00% | -20,08% | +20,08% | -6,17% | +37,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 16 | 0,00% | -19,77% | +19,77% | -6,29% | +37,34% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +30,79% | +30,79% | -1,52% | +44,86% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 16 | 0,00% | -19,77% | +19,77% | -6,29% | +37,34% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Classic technical | 1 | 0,00% | -23,91% | +23,91% | -6,69% | +37,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 1 | 0,00% | -23,91% | +23,91% | -6,69% | +37,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 1 | 0,00% | -23,91% | +23,91% | -6,69% | +37,24% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 39 | 51,28% | +0,57% | +0,61% | -0,20% | +1,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 53 | 56,60% | +0,39% | +0,40% | -0,24% | +1,29% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 55 | 50,91% | +0,37% | +0,40% | -0,28% | +1,24% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 38 | 55,26% | +1,05% | +1,08% | +0,15% | +2,08% | PESO OK | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 52 | 50,00% | +0,57% | +1,03% | +0,07% | +1,87% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 54 | 46,30% | +0,36% | +0,93% | +0,03% | +2,03% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 37 | 56,76% | +1,27% | +1,42% | -1,63% | +3,57% | PESO OK | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 51 | 50,98% | +1,09% | +1,67% | -1,62% | +3,89% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 53 | 50,94% | +0,21% | +1,45% | -1,67% | +3,59% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 35 | 60,00% | +1,91% | +2,07% | -2,42% | +5,15% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 49 | 55,10% | +1,78% | +2,89% | -2,32% | +6,20% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 51 | 49,02% | -0,36% | +2,77% | -2,46% | +5,96% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 33 | 54,55% | +2,30% | +2,25% | -2,89% | +6,15% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 47 | 61,70% | +2,83% | +4,18% | -2,68% | +8,13% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 49 | 42,86% | -1,24% | +3,88% | -2,86% | +7,81% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 30 | 63,33% | +2,56% | +2,44% | -3,06% | +7,12% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 44 | 65,91% | +5,23% | +6,27% | -2,81% | +10,42% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 46 | 50,00% | -2,08% | +5,23% | -3,06% | +9,57% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 26 | 50,00% | +1,72% | +3,64% | -3,23% | +8,17% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 40 | 80,00% | +9,21% | +10,23% | -2,90% | +15,14% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 3 | 66,67% | +10,82% | +10,82% | -3,34% | +16,86% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 42 | 38,10% | -4,93% | +7,76% | -3,25% | +12,98% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 34 | 85,29% | +17,72% | +16,08% | -4,28% | +21,44% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 36 | 33,33% | -14,01% | +12,87% | -4,63% | +18,17% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 21 | 9,52% | -26,53% | +26,53% | -4,64% | +32,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 27 | 88,89% | +23,02% | +23,41% | -5,16% | +29,61% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 31 | 12,90% | -21,05% | +20,44% | -5,38% | +26,28% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 8 | 0,00% | -35,68% | +35,68% | -7,09% | +44,63% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 12 | 33,33% | -7,79% | +31,67% | -7,99% | +39,17% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 16 | 25,00% | -20,49% | +32,79% | -7,71% | +39,99% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 1 | 0,00% | -35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 55 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 58 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 72 | 40,28% | +0,37% |
| BTC | BREVE | Famiglia statistica | 171 | 55,56% | +0,87% |
| BTC | BREVE | Microstruttura exchange | 13 | 46,15% | +0,55% |
| BTC | BREVE | Tecnico | 156 | 41,67% | +0,14% |
| BTC | SETTIMANALE | Classic technical | 59 | 49,15% | -2,95% |
| BTC | SETTIMANALE | Famiglia statistica | 155 | 60,00% | +3,05% |
| BTC | SETTIMANALE | Microstruttura exchange | 9 | 55,56% | +0,53% |
| BTC | SETTIMANALE | Tecnico | 140 | 44,29% | -1,39% |
| BTC | SWING | Classic technical | 21 | 33,33% | -10,59% |
| BTC | SWING | Famiglia statistica | 83 | 67,47% | +7,72% |
| BTC | SWING | Microstruttura exchange | 3 | 66,67% | +1,23% |
| BTC | SWING | Tecnico | 73 | 49,32% | -0,18% |
| BTC | MEDIO | Classic technical | 4 | 0,00% | -24,06% |
| BTC | MEDIO | Famiglia statistica | 48 | 89,58% | +16,47% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 40 | 35,00% | -6,39% |
| DOGE | BREVE | Classic technical | 94 | 39,36% | -1,27% |
| DOGE | BREVE | Famiglia statistica | 168 | 54,76% | +0,75% |
| DOGE | BREVE | Microstruttura exchange | 25 | 52,00% | +2,46% |
| DOGE | BREVE | Tecnico | 150 | 52,67% | +0,68% |
| DOGE | SETTIMANALE | Classic technical | 93 | 39,78% | -4,39% |
| DOGE | SETTIMANALE | Famiglia statistica | 152 | 54,61% | +2,93% |
| DOGE | SETTIMANALE | Microstruttura exchange | 23 | 47,83% | +0,43% |
| DOGE | SETTIMANALE | Tecnico | 134 | 58,96% | +1,12% |
| DOGE | SWING | Classic technical | 55 | 54,55% | -4,55% |
| DOGE | SWING | Famiglia statistica | 83 | 79,52% | +9,36% |
| DOGE | SWING | Microstruttura exchange | 11 | 63,64% | +0,95% |
| DOGE | SWING | Tecnico | 71 | 64,79% | -1,16% |
| DOGE | MEDIO | Classic technical | 37 | 29,73% | -13,59% |
| DOGE | MEDIO | Famiglia statistica | 48 | 56,25% | -0,33% |
| DOGE | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,55% |
| DOGE | MEDIO | Tecnico | 47 | 25,53% | -14,64% |
| SOL | BREVE | Classic technical | 114 | 54,39% | +0,96% |
| SOL | BREVE | Famiglia statistica | 156 | 52,56% | +0,68% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 162 | 49,38% | +0,31% |
| SOL | SETTIMANALE | Classic technical | 98 | 59,18% | +2,24% |
| SOL | SETTIMANALE | Famiglia statistica | 140 | 60,71% | +3,22% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 146 | 47,26% | -1,19% |
| SOL | SWING | Classic technical | 47 | 44,68% | -4,05% |
| SOL | SWING | Famiglia statistica | 74 | 82,43% | +13,12% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 5 | 60,00% | +13,52% |
| SOL | SWING | Tecnico | 78 | 35,90% | -9,12% |
| SOL | MEDIO | Classic technical | 29 | 6,90% | -29,06% |
| SOL | MEDIO | Famiglia statistica | 40 | 70,00% | +12,32% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 2 | 100,00% | +20,54% |
| SOL | MEDIO | Tecnico | 48 | 18,75% | -19,69% |

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

È iniziata la prima calibrazione, ma sono ammesse solo valutazioni leggere e manuali.
