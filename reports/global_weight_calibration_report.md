# Calibrazione pesi Global Confluence

Generato: 2026-08-28 08:02 UTC

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
| BTC | 49 | PRIMA CALIBRAZIONE | 48 | 15 | 0 | 0 | Famiglia statistica | 1g | 56,25% | +0,50% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 49 | PRIMA CALIBRAZIONE | 45 | 15 | 0 | 0 | Tecnico | 1g | 53,33% | +0,47% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 49 | PRIMA CALIBRAZIONE | 47 | 18 | 0 | 0 | Famiglia statistica | 1g | 57,45% | +0,61% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 16 | 37,50% | +0,55% | +1,21% | +0,46% | +1,86% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 48 | 56,25% | +0,50% | +0,50% | +0,07% | +1,09% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 43 | 39,53% | +0,19% | +0,67% | +0,21% | +1,26% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 15 | 40,00% | +0,76% | +1,78% | +1,19% | +2,61% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 47 | 57,45% | +1,03% | +1,03% | +0,45% | +1,76% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 42 | 45,24% | +0,29% | +1,28% | +0,69% | +2,01% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 14 | 42,86% | +0,16% | +2,91% | +0,06% | +4,37% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 46 | 60,87% | +1,54% | +1,54% | -0,81% | +3,15% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 41 | 39,02% | -0,08% | +1,97% | -0,57% | +3,53% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 12 | 41,67% | -2,51% | +7,17% | -0,07% | +8,71% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 44 | 52,27% | +2,67% | +2,67% | -1,35% | +4,79% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | +2,17% | +2,17% | +0,08% | +5,37% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 39 | 41,03% | -1,19% | +3,15% | -1,08% | +5,31% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 10 | 20,00% | -7,29% | +11,13% | +0,03% | +13,42% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 42 | 59,52% | +3,59% | +3,59% | -1,61% | +6,02% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 37 | 35,14% | -2,51% | +4,38% | -1,31% | +6,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 8 | 0,00% | -13,19% | +13,19% | -0,77% | +15,42% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 39 | 56,41% | +3,84% | +3,84% | -2,35% | +6,44% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 34 | 29,41% | -3,24% | +4,58% | -2,08% | +7,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 5 | 40,00% | -5,63% | +5,63% | -1,27% | +8,59% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 35 | 57,14% | +3,72% | +3,72% | -2,83% | +6,84% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 30 | 63,33% | +2,70% | +4,55% | -2,56% | +7,70% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 4 | 0,00% | -11,68% | +11,68% | -1,55% | +14,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 30 | 60,00% | +5,78% | +5,78% | -2,95% | +9,30% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 25 | 28,00% | -1,13% | +6,63% | -2,65% | +10,19% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Classic technical | 2 | 0,00% | -24,39% | +24,39% | -2,23% | +27,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 21 | 76,19% | +8,14% | +8,14% | -3,24% | +11,87% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 17 | 35,29% | -4,90% | +7,58% | -2,88% | +11,85% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 6 | 100,00% | +23,99% | +23,99% | -2,29% | +26,87% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 5 | 40,00% | -5,00% | +24,69% | -2,09% | +27,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 31 | 41,94% | -0,51% | +0,27% | -0,38% | +0,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 47 | 57,45% | +0,61% | +0,42% | -0,18% | +1,46% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 7 | 71,43% | +2,41% | +2,86% | +1,15% | +3,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 41 | 56,10% | +0,52% | +0,32% | -0,31% | +1,35% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 46 | 52,17% | +1,04% | +0,84% | +0,11% | +2,15% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 7 | 57,14% | +3,88% | +4,25% | +3,39% | +6,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 40 | 62,50% | +0,81% | +0,35% | -0,35% | +1,66% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 31 | 32,26% | -2,13% | +1,30% | -1,89% | +4,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 46 | 52,17% | +1,55% | +1,28% | -1,53% | +4,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 7 | 57,14% | +3,29% | +3,59% | -0,23% | +7,51% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 39 | 48,72% | +0,71% | +0,28% | -1,84% | +2,91% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 29 | 41,38% | -3,72% | +3,19% | -2,28% | +7,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 44 | 54,55% | +3,18% | +2,60% | -2,02% | +6,59% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 6 | 50,00% | +3,53% | +3,80% | +0,14% | +10,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 37 | 62,16% | +1,09% | +1,44% | -2,43% | +5,30% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 27 | 44,44% | -4,34% | +4,34% | -2,39% | +9,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 42 | 64,29% | +4,73% | +3,71% | -2,20% | +8,76% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,43% | +3,64% | +1,17% | +11,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 35 | 65,71% | +2,31% | +2,27% | -2,67% | +7,03% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 26 | 50,00% | -3,10% | +3,10% | -3,17% | +9,15% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 39 | 61,54% | +4,71% | +3,09% | -3,18% | +8,48% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 4 | 75,00% | +0,18% | +0,93% | -1,31% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 33 | 66,67% | +2,31% | +1,15% | -3,59% | +6,29% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 23 | 60,87% | -1,45% | +1,45% | -4,25% | +6,95% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 35 | 71,43% | +6,03% | +3,35% | -3,96% | +8,99% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 4 | 75,00% | +2,65% | +12,47% | -1,31% | +16,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 30 | 66,67% | +0,31% | -0,31% | -4,43% | +4,70% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 21 | 71,43% | -1,31% | +1,31% | -4,94% | +7,86% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 30 | 83,33% | +9,02% | +5,07% | -4,70% | +12,47% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 3 | 66,67% | -8,45% | +9,47% | -1,27% | +19,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 29 | 65,52% | -4,45% | +4,45% | -4,81% | +11,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 17 | 64,71% | -4,96% | +4,96% | -5,74% | +12,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 21 | 80,95% | +4,86% | +7,04% | -5,88% | +15,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 21 | 57,14% | -7,04% | +7,04% | -5,88% | +15,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 6 | 0,00% | -22,35% | +22,35% | -6,84% | +35,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 6 | 0,00% | -22,35% | +22,35% | -6,84% | +35,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 6 | 0,00% | -22,35% | +22,35% | -6,84% | +35,71% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 29 | 55,17% | +0,79% | +0,85% | +0,08% | +1,93% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 43 | 60,47% | +0,49% | +0,51% | -0,06% | +1,48% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 45 | 53,33% | +0,47% | +0,50% | -0,12% | +1,42% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 28 | 57,14% | +1,27% | +1,31% | +0,42% | +2,40% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 42 | 50,00% | +0,60% | +1,17% | +0,23% | +2,04% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 44 | 45,45% | +0,34% | +1,04% | +0,18% | +2,23% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 27 | 55,56% | +1,37% | +1,57% | -1,52% | +3,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 41 | 48,78% | +1,11% | +1,83% | -1,55% | +4,00% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,27% | +1,27% | -2,62% | +5,77% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 43 | 48,84% | +0,02% | +1,55% | -1,61% | +3,63% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 25 | 60,00% | +1,94% | +2,17% | -2,03% | +4,70% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 39 | 53,85% | +1,77% | +3,16% | -2,05% | +6,18% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +1,18% | +1,18% | -1,95% | +5,20% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 41 | 46,34% | -0,89% | +2,99% | -2,24% | +5,88% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 23 | 47,83% | +1,68% | +1,60% | -2,66% | +4,77% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 37 | 64,86% | +3,90% | +4,30% | -2,48% | +7,81% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +3,96% | +3,96% | -2,17% | +8,29% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 39 | 35,90% | -2,51% | +3,92% | -2,71% | +7,43% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 35 | 68,57% | +6,03% | +5,41% | -3,34% | +8,82% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 37 | 40,54% | -4,61% | +4,48% | -3,45% | +8,21% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 31 | 83,87% | +6,90% | +5,69% | -4,05% | +9,76% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 33 | 33,33% | -3,81% | +3,19% | -4,24% | +7,75% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 26 | 80,77% | +11,52% | +9,37% | -5,12% | +13,98% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 30 | 40,00% | -9,24% | +7,87% | -5,28% | +12,62% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 13 | 15,38% | -17,86% | +17,86% | -6,31% | +22,43% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 17 | 82,35% | +12,76% | +13,38% | -7,13% | +17,87% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 21 | 19,05% | -11,81% | +10,92% | -7,08% | +15,20% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 4 | 0,00% | -24,70% | +24,70% | -8,35% | +30,51% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 6 | 66,67% | +4,02% | +28,78% | -8,03% | +33,38% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 46 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 48 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 45 | 40,00% | +0,50% |
| BTC | BREVE | Famiglia statistica | 141 | 58,16% | +1,02% |
| BTC | BREVE | Microstruttura exchange | 9 | 66,67% | +1,28% |
| BTC | BREVE | Tecnico | 126 | 41,27% | +0,14% |
| BTC | SETTIMANALE | Classic technical | 30 | 23,33% | -6,95% |
| BTC | SETTIMANALE | Famiglia statistica | 125 | 56,00% | +3,35% |
| BTC | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +1,42% |
| BTC | SETTIMANALE | Tecnico | 110 | 35,45% | -2,27% |
| BTC | SWING | Classic technical | 9 | 22,22% | -8,32% |
| BTC | SWING | Famiglia statistica | 65 | 58,46% | +4,67% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 55 | 47,27% | +0,96% |
| BTC | MEDIO | Classic technical | 2 | 0,00% | -24,39% |
| BTC | MEDIO | Famiglia statistica | 27 | 81,48% | +11,66% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 22 | 36,36% | -4,92% |
| DOGE | BREVE | Classic technical | 93 | 39,78% | -1,28% |
| DOGE | BREVE | Famiglia statistica | 139 | 53,96% | +1,06% |
| DOGE | BREVE | Microstruttura exchange | 21 | 61,90% | +3,19% |
| DOGE | BREVE | Tecnico | 120 | 55,83% | +0,68% |
| DOGE | SETTIMANALE | Classic technical | 82 | 45,12% | -3,73% |
| DOGE | SETTIMANALE | Famiglia statistica | 125 | 60,00% | +4,18% |
| DOGE | SETTIMANALE | Microstruttura exchange | 15 | 60,00% | +2,60% |
| DOGE | SETTIMANALE | Tecnico | 105 | 64,76% | +1,88% |
| DOGE | SWING | Classic technical | 44 | 65,91% | -1,38% |
| DOGE | SWING | Famiglia statistica | 65 | 76,92% | +7,41% |
| DOGE | SWING | Microstruttura exchange | 7 | 71,43% | -2,11% |
| DOGE | SWING | Tecnico | 59 | 66,10% | -2,03% |
| DOGE | MEDIO | Classic technical | 23 | 47,83% | -9,50% |
| DOGE | MEDIO | Famiglia statistica | 27 | 62,96% | -1,18% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 27 | 44,44% | -10,44% |
| SOL | BREVE | Classic technical | 84 | 55,95% | +1,14% |
| SOL | BREVE | Famiglia statistica | 126 | 53,17% | +0,73% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 14 | 50,00% | +1,35% |
| SOL | BREVE | Tecnico | 132 | 49,24% | +0,28% |
| SOL | SETTIMANALE | Classic technical | 69 | 53,62% | +1,29% |
| SOL | SETTIMANALE | Famiglia statistica | 111 | 62,16% | +3,82% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | +1,41% |
| SOL | SETTIMANALE | Tecnico | 117 | 41,03% | -2,61% |
| SOL | SWING | Classic technical | 42 | 38,10% | -6,19% |
| SOL | SWING | Famiglia statistica | 57 | 82,46% | +9,01% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 3 | 33,33% | +4,53% |
| SOL | SWING | Tecnico | 63 | 36,51% | -6,40% |
| SOL | MEDIO | Classic technical | 13 | 15,38% | -17,86% |
| SOL | MEDIO | Famiglia statistica | 21 | 66,67% | +5,62% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 27 | 29,63% | -8,29% |

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
