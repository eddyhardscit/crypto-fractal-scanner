# Calibrazione pesi Global Confluence

Generato: 2026-08-25 05:32 UTC

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
| BTC | 46 | PRIMA CALIBRAZIONE | 45 | 13 | 0 | 0 | Famiglia statistica | 1g | 57,78% | +0,56% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 46 | PRIMA CALIBRAZIONE | 42 | 14 | 0 | 0 | Tecnico | 1g | 52,38% | +0,40% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 46 | PRIMA CALIBRAZIONE | 45 | 15 | 0 | 0 | Famiglia statistica | 1g | 60,00% | +0,82% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 13 | 38,46% | +0,78% | +1,59% | +0,75% | +2,20% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 45 | 57,78% | +0,56% | +0,56% | +0,13% | +1,13% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +1,45% | +1,45% | +1,10% | +2,07% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 40 | 40,00% | +0,24% | +0,75% | +0,29% | +1,33% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 12 | 33,33% | +0,88% | +2,14% | +1,61% | +2,98% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 44 | 56,82% | +1,08% | +1,08% | +0,51% | +1,80% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +4,54% | +4,54% | +3,15% | +5,05% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 39 | 43,59% | +0,29% | +1,35% | +0,78% | +2,08% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 11 | 36,36% | -0,21% | +3,29% | +0,27% | +4,57% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 43 | 60,47% | +1,54% | +1,54% | -0,81% | +3,11% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 38 | 36,84% | -0,21% | +2,01% | -0,55% | +3,52% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 9 | 22,22% | -4,66% | +8,25% | -0,01% | +9,57% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 41 | 48,78% | +2,58% | +2,58% | -1,43% | +4,69% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 36 | 36,11% | -1,62% | +3,09% | -1,16% | +5,24% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 8 | 0,00% | -11,51% | +11,51% | -0,67% | +13,66% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 39 | 56,41% | +2,78% | +2,78% | -2,06% | +5,22% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 34 | 29,41% | -3,97% | +3,53% | -1,80% | +5,83% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 6 | 0,00% | -9,33% | +9,33% | -1,08% | +11,39% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 36 | 52,78% | +2,11% | +2,11% | -2,56% | +4,70% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 31 | 32,26% | -1,18% | +2,64% | -2,30% | +5,27% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 4 | 50,00% | -0,27% | +0,27% | -1,55% | +3,37% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 34 | 55,88% | +3,03% | +3,03% | -2,91% | +6,17% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 29 | 65,52% | +3,72% | +3,77% | -2,64% | +6,95% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Classic technical | 4 | 0,00% | -11,68% | +11,68% | -1,55% | +14,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 27 | 55,56% | +3,89% | +3,89% | -2,95% | +7,50% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 22 | 22,73% | -2,30% | +4,41% | -2,60% | +8,11% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 18 | 72,22% | +5,61% | +5,61% | -3,27% | +9,53% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 15 | 40,00% | -2,30% | +5,34% | -2,97% | +9,75% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 3 | 100,00% | +22,42% | +22,42% | -3,05% | +25,54% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 2 | 0,00% | -23,38% | +23,38% | -2,93% | +26,09% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 30 | 43,33% | -0,30% | +0,50% | -0,13% | +1,22% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 45 | 60,00% | +0,82% | +0,55% | -0,05% | +1,57% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 7 | 71,43% | +2,41% | +2,86% | +1,15% | +3,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 38 | 57,89% | +0,72% | +0,49% | -0,15% | +1,48% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 29 | 48,28% | -0,85% | +1,15% | +0,37% | +2,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 44 | 54,55% | +1,38% | +1,16% | +0,43% | +2,50% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 6 | 66,67% | +5,43% | +5,87% | +5,07% | +8,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 37 | 64,86% | +1,19% | +0,69% | +0,01% | +1,98% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 28 | 35,71% | -1,79% | +2,01% | -1,31% | +4,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 43 | 55,81% | +2,03% | +1,73% | -1,13% | +4,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 6 | 66,67% | +4,84% | +5,19% | +0,90% | +8,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 36 | 52,78% | +1,21% | +0,74% | -1,38% | +3,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 27 | 44,44% | -3,71% | +3,71% | -1,98% | +7,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 41 | 56,10% | +3,48% | +2,86% | -1,95% | +6,37% | PESO OK | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +5,14% | +5,46% | +1,28% | +11,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 34 | 64,71% | +1,27% | +1,65% | -2,38% | +4,91% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 26 | 46,15% | -3,58% | +3,58% | -2,73% | +7,84% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 39 | 61,54% | +3,93% | +2,83% | -2,78% | +6,92% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,36% | +0,63% | -0,50% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 33 | 63,64% | +1,79% | +1,75% | -3,12% | +5,79% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 23 | 56,52% | -0,32% | +0,32% | -3,55% | +4,70% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 36 | 58,33% | +3,07% | +1,31% | -3,42% | +5,58% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 4 | 75,00% | +0,18% | +0,93% | -1,31% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 31 | 67,74% | +2,41% | -0,31% | -3,79% | +3,92% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 22 | 63,64% | -0,33% | +0,33% | -4,43% | +5,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 34 | 70,59% | +5,43% | +2,68% | -4,07% | +7,96% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 4 | 75,00% | +2,65% | +12,47% | -1,31% | +16,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 30 | 66,67% | +0,31% | -0,31% | -4,43% | +4,70% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 20 | 75,00% | -0,03% | +0,03% | -5,18% | +6,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 27 | 81,48% | +7,27% | +2,89% | -5,08% | +9,02% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 27 | 70,37% | -2,89% | +2,89% | -5,08% | +9,02% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 16 | 68,75% | -3,81% | +3,81% | -5,92% | +10,30% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 18 | 77,78% | +1,99% | +4,53% | -6,13% | +11,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 18 | 66,67% | -4,53% | +4,53% | -6,13% | +11,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 3 | 0,00% | -24,66% | +24,66% | -7,62% | +33,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 3 | 0,00% | -24,66% | +24,66% | -7,62% | +33,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 3 | 0,00% | -24,66% | +24,66% | -7,62% | +33,25% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 26 | 53,85% | +0,71% | +0,78% | -0,02% | +1,79% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 40 | 60,00% | +0,42% | +0,44% | -0,14% | +1,36% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,51% | +1,51% | +0,99% | +5,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 42 | 52,38% | +0,40% | +0,43% | -0,20% | +1,30% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 25 | 56,00% | +0,95% | +0,99% | +0,29% | +2,01% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 39 | 48,72% | +0,34% | +0,96% | +0,13% | +1,76% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 3 | 33,33% | +0,74% | +0,74% | +0,30% | +2,88% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 41 | 43,90% | +0,08% | +0,83% | +0,08% | +1,97% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 24 | 50,00% | +0,89% | +1,11% | -1,53% | +3,13% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 38 | 47,37% | +1,01% | +1,56% | -1,55% | +3,72% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 3 | 33,33% | +0,33% | +0,33% | -1,17% | +5,20% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 40 | 45,00% | -0,37% | +1,27% | -1,63% | +3,33% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 22 | 54,55% | +0,81% | +1,07% | -2,33% | +3,44% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 36 | 58,33% | +2,77% | +2,57% | -2,23% | +5,54% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 38 | 42,11% | -1,77% | +2,42% | -2,43% | +5,25% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 35 | 65,71% | +3,92% | +3,26% | -2,94% | +6,69% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 37 | 32,43% | -3,66% | +3,11% | -2,99% | +6,65% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 32 | 65,62% | +3,36% | +2,69% | -3,64% | +6,00% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 34 | 44,12% | -1,98% | +1,83% | -3,74% | +5,50% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 30 | 83,33% | +5,75% | +4,50% | -4,13% | +8,56% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 32 | 34,38% | -2,63% | +2,00% | -4,32% | +6,56% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 19 | 42,11% | -8,25% | +8,25% | -5,09% | +12,23% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 23 | 78,26% | +8,07% | +5,64% | -5,66% | +10,25% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 27 | 44,44% | -6,05% | +4,52% | -5,75% | +9,30% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 10 | 20,00% | -12,27% | +12,27% | -6,72% | +16,87% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 14 | 78,57% | +7,66% | +8,41% | -7,61% | +12,92% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 18 | 22,22% | -7,69% | +6,65% | -7,44% | +10,90% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 2 | 0,00% | -20,01% | +20,01% | -9,20% | +27,34% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 3 | 100,00% | +23,88% | +23,88% | -9,18% | +28,69% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 43 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 45 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 36 | 36,11% | +0,51% |
| BTC | BREVE | Famiglia statistica | 132 | 58,33% | +1,05% |
| BTC | BREVE | Microstruttura exchange | 5 | 100,00% | +2,77% |
| BTC | BREVE | Tecnico | 117 | 40,17% | +0,11% |
| BTC | SETTIMANALE | Classic technical | 23 | 8,70% | -8,26% |
| BTC | SETTIMANALE | Famiglia statistica | 116 | 52,59% | +2,50% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 101 | 32,67% | -2,27% |
| BTC | SWING | Classic technical | 8 | 25,00% | -5,98% |
| BTC | SWING | Famiglia statistica | 61 | 55,74% | +3,41% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 51 | 47,06% | +1,12% |
| BTC | MEDIO | Famiglia statistica | 21 | 76,19% | +8,01% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 17 | 35,29% | -4,78% |
| DOGE | BREVE | Classic technical | 87 | 42,53% | -0,96% |
| DOGE | BREVE | Famiglia statistica | 132 | 56,82% | +1,40% |
| DOGE | BREVE | Microstruttura exchange | 19 | 68,42% | +4,13% |
| DOGE | BREVE | Tecnico | 111 | 58,56% | +1,04% |
| DOGE | SETTIMANALE | Classic technical | 76 | 48,68% | -2,64% |
| DOGE | SETTIMANALE | Famiglia statistica | 116 | 58,62% | +3,50% |
| DOGE | SETTIMANALE | Microstruttura exchange | 13 | 61,54% | +2,14% |
| DOGE | SETTIMANALE | Tecnico | 98 | 65,31% | +1,80% |
| DOGE | SWING | Classic technical | 42 | 69,05% | -0,19% |
| DOGE | SWING | Famiglia statistica | 61 | 75,41% | +6,25% |
| DOGE | SWING | Microstruttura exchange | 6 | 83,33% | +2,02% |
| DOGE | SWING | Tecnico | 57 | 68,42% | -1,20% |
| DOGE | MEDIO | Classic technical | 19 | 57,89% | -7,10% |
| DOGE | MEDIO | Famiglia statistica | 21 | 66,67% | -1,82% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 21 | 57,14% | -7,40% |
| SOL | BREVE | Classic technical | 75 | 53,33% | +0,85% |
| SOL | BREVE | Famiglia statistica | 117 | 52,14% | +0,58% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 9 | 44,44% | +0,86% |
| SOL | BREVE | Tecnico | 123 | 47,15% | +0,04% |
| SOL | SETTIMANALE | Classic technical | 64 | 50,00% | +0,32% |
| SOL | SETTIMANALE | Famiglia statistica | 103 | 63,11% | +3,34% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 6 | 16,67% | -2,65% |
| SOL | SETTIMANALE | Tecnico | 109 | 39,45% | -2,48% |
| SOL | SWING | Classic technical | 40 | 40,00% | -4,54% |
| SOL | SWING | Famiglia statistica | 53 | 81,13% | +6,76% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 3 | 33,33% | +4,53% |
| SOL | SWING | Tecnico | 59 | 38,98% | -4,20% |
| SOL | MEDIO | Classic technical | 10 | 20,00% | -12,27% |
| SOL | MEDIO | Famiglia statistica | 16 | 68,75% | +4,20% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 21 | 33,33% | -3,18% |

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
