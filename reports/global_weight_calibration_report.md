# Calibrazione pesi Global Confluence

Generato: 2026-08-20 05:32 UTC

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
| BTC | 41 | PRIMA CALIBRAZIONE | 40 | 10 | 0 | 0 | Famiglia statistica | 1g | 55,00% | +0,25% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 41 | PRIMA CALIBRAZIONE | 37 | 11 | 0 | 0 | Tecnico | 1g | 48,65% | -0,07% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 41 | PRIMA CALIBRAZIONE | 40 | 12 | 0 | 0 | Famiglia statistica | 1g | 55,00% | +0,35% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 8 | 12,50% | -0,66% | +0,66% | +0,09% | +0,94% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 40 | 55,00% | +0,25% | +0,25% | -0,08% | +0,75% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 35 | 34,29% | -0,17% | +0,42% | +0,07% | +0,91% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 8 | 12,50% | -0,95% | +0,95% | +0,58% | +1,56% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 39 | 53,85% | +0,32% | +0,32% | -0,15% | +0,99% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 34 | 38,24% | -0,69% | +0,52% | +0,07% | +1,18% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 8 | 12,50% | -2,41% | +2,41% | -0,24% | +3,25% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 38 | 55,26% | +0,33% | +0,33% | -1,23% | +1,82% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 33 | 30,30% | -0,84% | +0,68% | -1,00% | +2,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 6 | 16,67% | -2,89% | +2,89% | -0,91% | +4,25% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 36 | 41,67% | +0,28% | +0,28% | -1,98% | +2,34% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 31 | 35,48% | -1,11% | +0,50% | -1,74% | +2,60% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,94% | +1,94% | -1,23% | +3,13% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 34 | 50,00% | -0,05% | -0,05% | -2,35% | +2,37% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 29 | 34,48% | -0,86% | +0,33% | -2,10% | +2,59% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,32% | +1,32% | -1,42% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 33 | 48,48% | +0,24% | +0,24% | -2,70% | +2,91% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 28 | 32,14% | -0,12% | +0,48% | -2,43% | +3,21% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Classic technical | 4 | 50,00% | -0,27% | +0,27% | -1,55% | +3,37% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 29 | 48,28% | +0,16% | +0,16% | -2,86% | +3,41% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 24 | 58,33% | +0,40% | +0,46% | -2,53% | +3,78% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Classic technical | 2 | 0,00% | -0,90% | +0,90% | -2,23% | +2,76% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 22 | 45,45% | -0,16% | -0,16% | -3,21% | +3,70% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 18 | 22,22% | -0,67% | +0,29% | -2,87% | +4,14% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 13 | 61,54% | +0,58% | +0,58% | -2,84% | +5,05% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 11 | 45,45% | -0,46% | -0,01% | -2,60% | +4,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 27 | 37,04% | -0,44% | +0,44% | -0,04% | +1,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 40 | 55,00% | +0,35% | +0,04% | -0,41% | +0,76% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,13% | +1,92% | +0,84% | +2,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 33 | 51,52% | +0,13% | -0,13% | -0,60% | +0,48% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 26 | 46,15% | -0,42% | +0,42% | -0,16% | +1,46% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 39 | 48,72% | +0,19% | -0,05% | -0,65% | +0,97% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 4 | 50,00% | +2,46% | +3,12% | +2,21% | +3,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 33 | 60,61% | +0,28% | -0,28% | -0,87% | +0,59% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 25 | 36,00% | -0,22% | +0,22% | -1,67% | +2,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 38 | 50,00% | +0,11% | -0,22% | -1,79% | +1,95% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,18% | +1,70% | -0,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 33 | 48,48% | +0,25% | -0,26% | -1,90% | +1,81% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 23 | 52,17% | +0,35% | -0,35% | -2,57% | +2,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 36 | 50,00% | +0,27% | -0,44% | -2,60% | +2,44% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,23% | +0,64% | -0,37% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 31 | 64,52% | +0,92% | -0,52% | -2,84% | +2,32% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 22 | 54,55% | +0,91% | -0,91% | -3,18% | +2,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 34 | 55,88% | +0,33% | -0,93% | -3,12% | +2,57% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,36% | +0,63% | -0,50% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 30 | 63,33% | +1,05% | -1,05% | -3,36% | +2,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 22 | 59,09% | +1,13% | -1,13% | -3,71% | +2,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 33 | 54,55% | +0,84% | -1,08% | -3,65% | +2,91% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 4 | 75,00% | +0,18% | +0,93% | -1,31% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 30 | 66,67% | +1,40% | -1,40% | -3,88% | +2,63% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 20 | 70,00% | +2,09% | -2,09% | -4,80% | +3,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 29 | 65,52% | +1,46% | -1,77% | -4,58% | +3,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 28 | 71,43% | +2,07% | -2,07% | -4,68% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 18 | 83,33% | +2,56% | -2,56% | -5,46% | +3,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 22 | 77,27% | +2,59% | -2,79% | -5,65% | +2,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 22 | 86,36% | +2,79% | -2,79% | -5,65% | +2,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 12 | 91,67% | +3,31% | -3,31% | -6,50% | +2,79% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 13 | 92,31% | +3,53% | -3,53% | -6,62% | +2,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 13 | 92,31% | +3,53% | -3,53% | -6,62% | +2,61% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 21 | 47,62% | -0,04% | +0,04% | -0,54% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 36 | 61,11% | +0,34% | +0,10% | -0,37% | +0,72% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 37 | 48,65% | -0,07% | -0,03% | -0,52% | +0,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 21 | 47,62% | -0,02% | +0,02% | -0,52% | +0,51% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 35 | 51,43% | +0,32% | +0,19% | -0,52% | +0,91% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 37 | 37,84% | -0,57% | +0,26% | -0,40% | +1,12% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 21 | 42,86% | -0,13% | +0,13% | -1,91% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 34 | 47,06% | +0,38% | +0,15% | -2,06% | +1,97% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 36 | 41,67% | -0,57% | +0,23% | -1,94% | +2,16% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 21 | 52,38% | -0,14% | +0,14% | -2,60% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 32 | 53,12% | +0,37% | +0,15% | -2,80% | +2,66% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 34 | 44,12% | -0,65% | +0,17% | -2,80% | +2,86% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 30 | 60,00% | +0,37% | -0,40% | -3,32% | +2,72% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 32 | 37,50% | -0,30% | -0,34% | -3,35% | +2,93% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 29 | 62,07% | +1,00% | +0,25% | -3,84% | +3,54% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 32 | 46,88% | -0,22% | +0,07% | -3,88% | +3,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 20 | 40,00% | -0,08% | +0,08% | -4,53% | +4,13% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 25 | 80,00% | +1,74% | +0,24% | -4,70% | +4,06% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 29 | 37,93% | -0,45% | -0,25% | -4,69% | +4,03% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Classic technical | 14 | 57,14% | -0,98% | +0,98% | -6,13% | +4,45% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 18 | 72,22% | +2,36% | -0,75% | -6,62% | +3,65% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 22 | 54,55% | -0,92% | -0,95% | -6,56% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 5 | 40,00% | -0,15% | +0,15% | -6,51% | +4,11% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 9 | 77,78% | +1,74% | -0,46% | -7,97% | +3,64% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 13 | 30,77% | -1,26% | -0,18% | -7,63% | +3,70% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 38 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 40 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 24 | 12,50% | -1,34% |
| BTC | BREVE | Famiglia statistica | 117 | 54,70% | +0,30% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 102 | 34,31% | -0,56% |
| BTC | SETTIMANALE | Classic technical | 14 | 7,14% | -2,17% |
| BTC | SETTIMANALE | Famiglia statistica | 103 | 46,60% | +0,16% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 88 | 34,09% | -0,71% |
| BTC | SWING | Classic technical | 6 | 33,33% | -0,48% |
| BTC | SWING | Famiglia statistica | 51 | 47,06% | +0,02% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 42 | 42,86% | -0,06% |
| BTC | MEDIO | Famiglia statistica | 13 | 61,54% | +0,58% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 11 | 45,45% | -0,46% |
| DOGE | BREVE | Classic technical | 78 | 39,74% | -0,37% |
| DOGE | BREVE | Famiglia statistica | 117 | 51,28% | +0,22% |
| DOGE | BREVE | Microstruttura exchange | 12 | 50,00% | +1,59% |
| DOGE | BREVE | Tecnico | 99 | 53,54% | +0,22% |
| DOGE | SETTIMANALE | Classic technical | 67 | 55,22% | +0,79% |
| DOGE | SETTIMANALE | Famiglia statistica | 103 | 53,40% | +0,47% |
| DOGE | SETTIMANALE | Microstruttura exchange | 12 | 58,33% | +0,26% |
| DOGE | SETTIMANALE | Tecnico | 91 | 64,84% | +1,12% |
| DOGE | SWING | Classic technical | 38 | 76,32% | +2,31% |
| DOGE | SWING | Famiglia statistica | 51 | 70,59% | +1,95% |
| DOGE | SWING | Microstruttura exchange | 4 | 100,00% | +0,61% |
| DOGE | SWING | Tecnico | 50 | 78,00% | +2,39% |
| DOGE | MEDIO | Classic technical | 12 | 91,67% | +3,31% |
| DOGE | MEDIO | Famiglia statistica | 13 | 92,31% | +3,53% |
| DOGE | MEDIO | Tecnico | 13 | 92,31% | +3,53% |
| SOL | BREVE | Classic technical | 63 | 46,03% | -0,06% |
| SOL | BREVE | Famiglia statistica | 105 | 53,33% | +0,35% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 6 | 16,67% | -0,83% |
| SOL | BREVE | Tecnico | 110 | 42,73% | -0,40% |
| SOL | SETTIMANALE | Classic technical | 63 | 49,21% | -0,00% |
| SOL | SETTIMANALE | Famiglia statistica | 91 | 58,24% | +0,57% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 6 | 16,67% | -2,65% |
| SOL | SETTIMANALE | Tecnico | 98 | 42,86% | -0,39% |
| SOL | SWING | Classic technical | 34 | 47,06% | -0,45% |
| SOL | SWING | Famiglia statistica | 43 | 76,74% | +2,00% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 2 | 0,00% | -4,49% |
| SOL | SWING | Tecnico | 51 | 45,10% | -0,65% |
| SOL | MEDIO | Classic technical | 5 | 40,00% | -0,15% |
| SOL | MEDIO | Famiglia statistica | 9 | 77,78% | +1,74% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 13 | 30,77% | -1,26% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 12 | in attesa di controlli maturati |
| SOL | MEDIO | 10 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 2 | in attesa di controlli maturati |
| DOGE | MEDIO | 12 | in attesa di controlli maturati |

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
