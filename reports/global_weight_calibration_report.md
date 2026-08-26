# Calibrazione pesi Global Confluence

Generato: 2026-08-26 05:32 UTC

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
| BTC | 47 | PRIMA CALIBRAZIONE | 46 | 13 | 0 | 0 | Famiglia statistica | 1g | 56,52% | +0,50% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 47 | PRIMA CALIBRAZIONE | 43 | 14 | 0 | 0 | Tecnico | 1g | 51,16% | +0,27% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 47 | PRIMA CALIBRAZIONE | 46 | 16 | 0 | 0 | Famiglia statistica | 1g | 58,70% | +0,66% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 14 | 35,71% | +0,58% | +1,33% | +0,48% | +1,91% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 46 | 56,52% | +0,50% | +0,50% | +0,06% | +1,06% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 41 | 39,02% | +0,18% | +0,68% | +0,21% | +1,25% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 13 | 38,46% | +1,03% | +2,19% | +1,63% | +2,98% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 45 | 57,78% | +1,12% | +1,12% | +0,54% | +1,83% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +4,54% | +4,54% | +3,15% | +5,05% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 40 | 45,00% | +0,35% | +1,39% | +0,81% | +2,10% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 12 | 41,67% | +0,11% | +3,32% | +0,29% | +4,59% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 44 | 61,36% | +1,59% | +1,59% | -0,78% | +3,15% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +2,79% | +2,79% | +0,99% | +4,54% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 39 | 38,46% | -0,11% | +2,05% | -0,53% | +3,56% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 10 | 30,00% | -3,66% | +7,96% | +0,06% | +9,26% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 42 | 50,00% | +2,64% | +2,64% | -1,38% | +4,74% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 37 | 37,84% | -1,43% | +3,15% | -1,10% | +5,27% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 8 | 0,00% | -11,51% | +11,51% | -0,67% | +13,66% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 40 | 57,50% | +3,29% | +3,29% | -1,83% | +5,70% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 35 | 31,43% | -3,20% | +4,08% | -1,55% | +6,36% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 7 | 0,00% | -11,65% | +11,65% | -1,00% | +13,61% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 37 | 54,05% | +2,75% | +2,75% | -2,50% | +5,30% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 32 | 31,25% | -1,94% | +3,36% | -2,24% | +5,94% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 4 | 50,00% | -0,27% | +0,27% | -1,55% | +3,37% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 34 | 55,88% | +3,03% | +3,03% | -2,91% | +6,17% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 29 | 65,52% | +3,72% | +3,77% | -2,64% | +6,95% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Classic technical | 4 | 0,00% | -11,68% | +11,68% | -1,55% | +14,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 28 | 57,14% | +4,57% | +4,57% | -2,94% | +8,11% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 23 | 21,74% | -3,21% | +5,23% | -2,61% | +8,82% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 19 | 73,68% | +6,43% | +6,43% | -3,35% | +10,21% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 15 | 40,00% | -2,30% | +5,34% | -2,97% | +9,75% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 4 | 100,00% | +22,81% | +22,81% | -3,09% | +25,48% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 3 | 33,33% | -7,60% | +23,57% | -3,03% | +25,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 31 | 41,94% | -0,51% | +0,27% | -0,38% | +0,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 46 | 58,70% | +0,66% | +0,39% | -0,22% | +1,39% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 7 | 71,43% | +2,41% | +2,86% | +1,15% | +3,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 39 | 56,41% | +0,53% | +0,31% | -0,35% | +1,28% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 30 | 46,67% | -1,00% | +0,94% | +0,14% | +1,89% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 45 | 53,33% | +1,23% | +1,02% | +0,27% | +2,33% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 7 | 57,14% | +3,88% | +4,25% | +3,39% | +6,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 38 | 63,16% | +1,02% | +0,53% | -0,17% | +1,79% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 29 | 34,48% | -1,87% | +1,80% | -1,45% | +4,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 44 | 54,55% | +1,89% | +1,60% | -1,22% | +4,34% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 6 | 66,67% | +4,84% | +5,19% | +0,90% | +8,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 37 | 51,35% | +1,07% | +0,61% | -1,49% | +3,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 27 | 44,44% | -3,71% | +3,71% | -1,98% | +7,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 42 | 57,14% | +3,52% | +2,91% | -1,82% | +6,72% | PESO OK | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +5,14% | +5,46% | +1,28% | +11,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 35 | 65,71% | +1,38% | +1,74% | -2,21% | +5,38% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 27 | 44,44% | -4,34% | +4,34% | -2,39% | +9,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 40 | 62,50% | +4,43% | +3,36% | -2,55% | +7,82% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,36% | +0,63% | -0,50% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 33 | 63,64% | +1,79% | +1,75% | -3,12% | +5,79% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 24 | 54,17% | -1,33% | +1,33% | -3,42% | +6,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 37 | 59,46% | +3,65% | +1,94% | -3,34% | +6,61% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 4 | 75,00% | +0,18% | +0,93% | -1,31% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 32 | 68,75% | +3,10% | +0,47% | -3,68% | +5,15% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 22 | 63,64% | -0,33% | +0,33% | -4,43% | +5,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 34 | 70,59% | +5,43% | +2,68% | -4,07% | +7,96% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 4 | 75,00% | +2,65% | +12,47% | -1,31% | +16,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 30 | 66,67% | +0,31% | -0,31% | -4,43% | +4,70% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 20 | 75,00% | -0,03% | +0,03% | -5,18% | +6,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 28 | 82,14% | +7,87% | +3,64% | -4,97% | +10,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 28 | 67,86% | -3,64% | +3,64% | -4,97% | +10,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 16 | 68,75% | -3,81% | +3,81% | -5,92% | +10,30% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 19 | 78,95% | +2,88% | +5,29% | -6,16% | +12,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 19 | 63,16% | -5,29% | +5,29% | -6,16% | +12,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 4 | 0,00% | -23,27% | +23,27% | -7,38% | +34,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 4 | 0,00% | -23,27% | +23,27% | -7,38% | +34,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 4 | 0,00% | -23,27% | +23,27% | -7,38% | +34,26% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 27 | 51,85% | +0,49% | +0,55% | -0,24% | +1,55% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 41 | 58,54% | +0,28% | +0,30% | -0,29% | +1,21% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 4 | 50,00% | -0,20% | -0,20% | -0,75% | +2,55% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 43 | 51,16% | +0,27% | +0,30% | -0,34% | +1,15% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 26 | 57,69% | +1,05% | +1,08% | +0,38% | +2,08% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 40 | 50,00% | +0,42% | +1,02% | +0,19% | +1,81% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 3 | 33,33% | +0,74% | +0,74% | +0,30% | +2,88% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 42 | 45,24% | +0,16% | +0,89% | +0,14% | +2,02% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 25 | 52,00% | +1,02% | +1,24% | -1,46% | +3,24% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 39 | 46,15% | +0,87% | +1,63% | -1,51% | +3,78% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 3 | 33,33% | +0,33% | +0,33% | -1,17% | +5,20% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 41 | 46,34% | -0,26% | +1,34% | -1,58% | +3,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 23 | 56,52% | +1,13% | +1,38% | -2,15% | +3,88% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 37 | 56,76% | +2,47% | +2,72% | -2,12% | +5,75% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +1,18% | +1,18% | -1,95% | +5,20% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 39 | 43,59% | -1,51% | +2,57% | -2,32% | +5,46% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 36 | 66,67% | +4,53% | +3,90% | -2,60% | +7,40% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 37 | 32,43% | -3,66% | +3,11% | -2,99% | +6,65% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 33 | 66,67% | +4,13% | +3,47% | -3,57% | +6,88% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 35 | 42,86% | -2,74% | +2,60% | -3,67% | +6,35% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 30 | 83,33% | +5,75% | +4,50% | -4,13% | +8,56% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 32 | 34,38% | -2,63% | +2,00% | -4,32% | +6,56% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 20 | 40,00% | -9,40% | +9,40% | -4,94% | +13,51% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 24 | 79,17% | +9,03% | +6,70% | -5,51% | +11,40% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 28 | 42,86% | -6,95% | +5,48% | -5,62% | +10,32% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 11 | 18,18% | -13,60% | +13,60% | -6,79% | +18,35% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 15 | 80,00% | +8,94% | +9,65% | -7,60% | +14,27% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 19 | 21,05% | -8,70% | +7,71% | -7,44% | +12,07% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 3 | 0,00% | -22,26% | +22,26% | -8,66% | +29,24% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 4 | 100,00% | +24,60% | +24,60% | -8,78% | +29,77% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 44 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 46 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 39 | 38,46% | +0,58% |
| BTC | BREVE | Famiglia statistica | 135 | 58,52% | +1,06% |
| BTC | BREVE | Microstruttura exchange | 7 | 85,71% | +2,21% |
| BTC | BREVE | Tecnico | 120 | 40,83% | +0,14% |
| BTC | SETTIMANALE | Classic technical | 25 | 12,00% | -8,41% |
| BTC | SETTIMANALE | Famiglia statistica | 119 | 53,78% | +2,89% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 104 | 33,65% | -2,18% |
| BTC | SWING | Classic technical | 8 | 25,00% | -5,98% |
| BTC | SWING | Famiglia statistica | 62 | 56,45% | +3,73% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 52 | 46,15% | +0,66% |
| BTC | MEDIO | Famiglia statistica | 23 | 78,26% | +9,28% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 18 | 38,89% | -3,18% |
| DOGE | BREVE | Classic technical | 90 | 41,11% | -1,11% |
| DOGE | BREVE | Famiglia statistica | 135 | 55,56% | +1,25% |
| DOGE | BREVE | Microstruttura exchange | 20 | 65,00% | +3,65% |
| DOGE | BREVE | Tecnico | 114 | 57,02% | +0,87% |
| DOGE | SETTIMANALE | Classic technical | 78 | 47,44% | -3,20% |
| DOGE | SETTIMANALE | Famiglia statistica | 119 | 59,66% | +3,86% |
| DOGE | SETTIMANALE | Microstruttura exchange | 13 | 61,54% | +2,14% |
| DOGE | SETTIMANALE | Tecnico | 100 | 66,00% | +2,06% |
| DOGE | SWING | Classic technical | 42 | 69,05% | -0,19% |
| DOGE | SWING | Famiglia statistica | 62 | 75,81% | +6,53% |
| DOGE | SWING | Microstruttura exchange | 6 | 83,33% | +2,02% |
| DOGE | SWING | Tecnico | 58 | 67,24% | -1,60% |
| DOGE | MEDIO | Classic technical | 20 | 55,00% | -7,70% |
| DOGE | MEDIO | Famiglia statistica | 23 | 65,22% | -1,66% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 23 | 52,17% | -8,42% |
| SOL | BREVE | Classic technical | 78 | 53,85% | +0,84% |
| SOL | BREVE | Famiglia statistica | 120 | 51,67% | +0,52% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 10 | 40,00% | +0,24% |
| SOL | BREVE | Tecnico | 126 | 47,62% | +0,06% |
| SOL | SETTIMANALE | Classic technical | 65 | 50,77% | +0,44% |
| SOL | SETTIMANALE | Famiglia statistica | 106 | 63,21% | +3,69% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 7 | 28,57% | -1,10% |
| SOL | SETTIMANALE | Tecnico | 111 | 39,64% | -2,62% |
| SOL | SWING | Classic technical | 41 | 39,02% | -5,20% |
| SOL | SWING | Famiglia statistica | 54 | 81,48% | +7,21% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 3 | 33,33% | +4,53% |
| SOL | SWING | Tecnico | 60 | 38,33% | -4,65% |
| SOL | MEDIO | Classic technical | 11 | 18,18% | -13,60% |
| SOL | MEDIO | Famiglia statistica | 18 | 66,67% | +3,74% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 23 | 34,78% | -2,91% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 10 | in attesa di controlli maturati |
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
