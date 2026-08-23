# Calibrazione pesi Global Confluence

Generato: 2026-08-23 05:32 UTC

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
| BTC | 44 | PRIMA CALIBRAZIONE | 43 | 12 | 0 | 0 | Famiglia statistica | 1g | 55,81% | +0,45% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 44 | PRIMA CALIBRAZIONE | 40 | 13 | 0 | 0 | Tecnico | 1g | 50,00% | +0,17% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 44 | PRIMA CALIBRAZIONE | 43 | 14 | 0 | 0 | Famiglia statistica | 1g | 58,14% | +0,79% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 11 | 27,27% | +0,39% | +1,35% | +0,60% | +1,95% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 43 | 55,81% | +0,45% | +0,45% | +0,06% | +1,02% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 38 | 36,84% | +0,10% | +0,64% | +0,22% | +1,21% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 10 | 30,00% | +0,48% | +2,00% | +1,65% | +2,88% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 42 | 57,14% | +0,99% | +0,99% | +0,47% | +1,72% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 37 | 43,24% | +0,15% | +1,27% | +0,74% | +2,00% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 9 | 22,22% | -1,06% | +3,21% | +0,33% | +4,47% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 41 | 58,54% | +1,44% | +1,44% | -0,85% | +3,02% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 36 | 33,33% | -0,42% | +1,92% | -0,58% | +3,44% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 8 | 12,50% | -7,26% | +7,26% | -0,63% | +8,70% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 39 | 46,15% | +1,79% | +1,79% | -1,82% | +3,91% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 34 | 32,35% | -2,77% | +2,22% | -1,58% | +4,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 7 | 0,00% | -10,11% | +10,11% | -0,89% | +11,99% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 37 | 54,05% | +1,66% | +1,66% | -2,20% | +4,11% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 32 | 31,25% | -2,75% | +2,27% | -1,94% | +4,58% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,32% | +1,32% | -1,42% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 34 | 50,00% | +0,75% | +0,75% | -2,68% | +3,36% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 29 | 34,48% | +0,49% | +1,07% | -2,43% | +3,73% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Classic technical | 4 | 50,00% | -0,27% | +0,27% | -1,55% | +3,37% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 32 | 53,12% | +1,82% | +1,82% | -2,90% | +5,02% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 27 | 62,96% | +2,33% | +2,39% | -2,61% | +5,64% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Classic technical | 3 | 0,00% | -8,03% | +8,03% | -1,93% | +10,14% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 25 | 52,00% | +2,23% | +2,23% | -3,09% | +5,96% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 20 | 20,00% | -2,73% | +2,39% | -2,74% | +6,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 16 | 68,75% | +3,48% | +3,48% | -3,28% | +7,62% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 13 | 38,46% | -3,06% | +2,66% | -2,94% | +7,42% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 1 | 100,00% | +20,63% | +20,63% | -2,32% | +25,66% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 1 | 0,00% | -20,63% | +20,63% | -2,32% | +25,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 28 | 39,29% | -0,42% | +0,43% | -0,08% | +1,15% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 43 | 58,14% | +0,79% | +0,51% | -0,01% | +1,54% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 6 | 66,67% | +2,58% | +3,11% | +1,68% | +3,93% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 36 | 55,56% | +0,68% | +0,44% | -0,11% | +1,44% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 27 | 44,44% | -1,08% | +1,08% | +0,40% | +2,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 42 | 52,38% | +1,34% | +1,11% | +0,45% | +2,47% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 5 | 60,00% | +6,19% | +6,72% | +5,95% | +9,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 35 | 62,86% | +1,14% | +0,61% | +0,01% | +1,92% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 27 | 33,33% | -1,97% | +1,97% | -1,30% | +4,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 41 | 53,66% | +1,78% | +1,47% | -1,31% | +3,95% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +5,21% | +5,63% | +1,37% | +9,34% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 34 | 50,00% | +0,87% | +0,37% | -1,61% | +2,54% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 26 | 46,15% | -2,66% | +2,66% | -2,30% | +6,12% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 39 | 53,85% | +2,23% | +1,57% | -2,42% | +4,72% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,23% | +0,64% | -0,37% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 33 | 63,64% | +0,56% | +0,95% | -2,69% | +4,03% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 24 | 50,00% | -1,20% | +1,20% | -2,94% | +4,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 37 | 59,46% | +2,40% | +1,24% | -2,91% | +4,97% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,36% | +0,63% | -0,50% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 32 | 65,62% | +2,81% | +0,84% | -3,19% | +4,64% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 22 | 59,09% | +1,13% | -1,13% | -3,71% | +2,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 34 | 55,88% | +1,35% | -0,51% | -3,58% | +3,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 4 | 75,00% | +0,18% | +0,93% | -1,31% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 30 | 66,67% | +1,40% | -1,40% | -3,88% | +2,63% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 22 | 63,64% | -0,33% | +0,33% | -4,43% | +5,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 32 | 68,75% | +3,75% | +0,82% | -4,25% | +5,76% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 4 | 75,00% | +2,65% | +12,47% | -1,31% | +16,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 30 | 66,67% | +0,31% | -0,31% | -4,43% | +4,70% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 20 | 75,00% | -0,03% | +0,03% | -5,18% | +6,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 25 | 80,00% | +5,30% | +0,56% | -5,29% | +6,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 25 | 76,00% | -0,56% | +0,56% | -5,29% | +6,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 15 | 73,33% | -1,93% | +1,93% | -6,17% | +8,06% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 16 | 75,00% | -1,43% | +1,43% | -6,29% | +7,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +31,03% | +31,03% | -1,52% | +36,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 16 | 75,00% | -1,43% | +1,43% | -6,29% | +7,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 1 | 0,00% | -24,15% | +24,15% | -6,69% | +29,34% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 1 | 0,00% | -24,15% | +24,15% | -6,69% | +29,34% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 1 | 0,00% | -24,15% | +24,15% | -6,69% | +29,34% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 24 | 50,00% | +0,36% | +0,43% | -0,27% | +1,46% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 38 | 60,53% | +0,22% | +0,20% | -0,31% | +1,13% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,51% | +1,51% | +0,99% | +5,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 40 | 50,00% | +0,17% | +0,21% | -0,36% | +1,08% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 23 | 52,17% | +0,58% | +0,62% | +0,03% | +1,66% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 37 | 51,35% | +0,65% | +0,73% | -0,04% | +1,53% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 3 | 33,33% | +0,74% | +0,74% | +0,30% | +2,88% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 39 | 41,03% | -0,19% | +0,60% | -0,08% | +1,77% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 22 | 45,45% | +0,31% | +0,56% | -1,68% | +2,36% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 36 | 50,00% | +1,46% | +1,25% | -1,65% | +3,28% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 38 | 42,11% | -0,77% | +0,96% | -1,72% | +2,90% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 21 | 52,38% | -0,14% | +0,14% | -2,60% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 35 | 57,14% | +2,22% | +2,01% | -2,57% | +4,77% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 37 | 40,54% | -2,38% | +1,93% | -2,58% | +4,84% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 33 | 63,64% | +2,34% | +1,65% | -3,15% | +4,97% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 35 | 34,29% | -2,16% | +1,58% | -3,19% | +5,03% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 30 | 63,33% | +1,58% | +0,86% | -3,78% | +4,05% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 32 | 46,88% | -0,22% | +0,07% | -3,88% | +3,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 28 | 82,14% | +4,10% | +2,76% | -4,24% | +6,75% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 31 | 35,48% | -1,99% | +1,33% | -4,36% | +5,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 17 | 47,06% | -5,25% | +5,25% | -5,53% | +9,07% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 21 | 76,19% | +5,61% | +2,95% | -6,06% | +7,50% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 25 | 48,00% | -3,83% | +2,18% | -6,10% | +6,92% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 8 | 25,00% | -7,48% | +7,48% | -7,09% | +11,93% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 12 | 75,00% | +3,70% | +4,58% | -7,99% | +8,97% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 16 | 25,00% | -4,72% | +3,55% | -7,71% | +7,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 1 | 0,00% | -19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 41 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 43 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 30 | 26,67% | -0,01% |
| BTC | BREVE | Famiglia statistica | 126 | 57,14% | +0,96% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 111 | 37,84% | -0,05% |
| BTC | SETTIMANALE | Classic technical | 19 | 5,26% | -7,06% |
| BTC | SETTIMANALE | Famiglia statistica | 110 | 50,00% | +1,42% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 95 | 32,63% | -1,76% |
| BTC | SWING | Classic technical | 7 | 28,57% | -3,60% |
| BTC | SWING | Famiglia statistica | 57 | 52,63% | +2,00% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 47 | 44,68% | +0,18% |
| BTC | MEDIO | Famiglia statistica | 17 | 70,59% | +4,48% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 14 | 35,71% | -4,31% |
| DOGE | BREVE | Classic technical | 82 | 39,02% | -1,15% |
| DOGE | BREVE | Famiglia statistica | 126 | 54,76% | +1,30% |
| DOGE | BREVE | Microstruttura exchange | 16 | 62,50% | +4,53% |
| DOGE | BREVE | Tecnico | 105 | 56,19% | +0,89% |
| DOGE | SETTIMANALE | Classic technical | 72 | 51,39% | -1,02% |
| DOGE | SETTIMANALE | Famiglia statistica | 110 | 56,36% | +2,01% |
| DOGE | SETTIMANALE | Microstruttura exchange | 12 | 58,33% | +0,26% |
| DOGE | SETTIMANALE | Tecnico | 95 | 65,26% | +1,58% |
| DOGE | SWING | Classic technical | 42 | 69,05% | -0,19% |
| DOGE | SWING | Famiglia statistica | 57 | 73,68% | +4,43% |
| DOGE | SWING | Microstruttura exchange | 6 | 83,33% | +2,02% |
| DOGE | SWING | Tecnico | 55 | 70,91% | -0,09% |
| DOGE | MEDIO | Classic technical | 16 | 68,75% | -3,32% |
| DOGE | MEDIO | Famiglia statistica | 17 | 70,59% | -2,77% |
| DOGE | MEDIO | Microstruttura exchange | 1 | 100,00% | +31,03% |
| DOGE | MEDIO | Tecnico | 17 | 70,59% | -2,77% |
| SOL | BREVE | Classic technical | 69 | 49,28% | +0,42% |
| SOL | BREVE | Famiglia statistica | 111 | 54,05% | +0,77% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 8 | 37,50% | +0,38% |
| SOL | BREVE | Tecnico | 117 | 44,44% | -0,25% |
| SOL | SETTIMANALE | Classic technical | 63 | 49,21% | -0,00% |
| SOL | SETTIMANALE | Famiglia statistica | 98 | 61,22% | +2,06% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 6 | 16,67% | -2,65% |
| SOL | SETTIMANALE | Tecnico | 104 | 40,38% | -1,64% |
| SOL | SWING | Classic technical | 38 | 42,11% | -3,00% |
| SOL | SWING | Famiglia statistica | 49 | 79,59% | +4,75% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 3 | 33,33% | +4,53% |
| SOL | SWING | Tecnico | 56 | 41,07% | -2,81% |
| SOL | MEDIO | Classic technical | 8 | 25,00% | -7,48% |
| SOL | MEDIO | Famiglia statistica | 13 | 69,23% | +1,93% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 17 | 29,41% | -3,31% |

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
