# Calibrazione pesi Global Confluence

Generato: 2026-09-12 05:32 UTC

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
| BTC | 64 | UTILE | 63 | 17 | 3 | 0 | Famiglia statistica | 1g | 52,38% | +0,33% | campione utile, valutare con prudenza |
| SOL | 64 | PRIMA CALIBRAZIONE | 59 | 25 | 0 | 0 | Tecnico | 1g | 49,15% | +0,25% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 64 | UTILE | 62 | 25 | 3 | 0 | Famiglia statistica | 1g | 58,06% | +0,51% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 24 | 37,50% | +0,37% | +0,81% | +0,13% | +1,33% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 63 | 52,38% | +0,33% | +0,33% | -0,10% | +0,85% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 58 | 39,66% | +0,09% | +0,45% | -0,01% | +0,96% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 24 | 41,67% | +0,55% | +1,18% | +0,59% | +1,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 62 | 51,61% | +0,70% | +0,70% | +0,13% | +1,36% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 57 | 42,11% | +0,13% | +0,85% | +0,28% | +1,51% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 24 | 41,67% | +0,20% | +1,81% | -0,58% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 61 | 52,46% | +1,07% | +1,07% | -1,04% | +2,71% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 56 | 35,71% | -0,16% | +1,34% | -0,89% | +2,95% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 24 | 50,00% | -1,14% | +3,70% | -1,03% | +5,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 59 | 50,85% | +1,90% | +1,90% | -1,60% | +4,25% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 54 | 42,59% | -0,96% | +2,17% | -1,43% | +4,57% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 24 | 45,83% | -2,81% | +4,87% | -1,33% | +8,02% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 57 | 59,65% | +2,69% | +2,69% | -1,82% | +5,48% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | -0,70% | -0,70% | -2,63% | +2,73% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 52 | 42,31% | -1,74% | +3,17% | -1,63% | +5,90% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 22 | 54,55% | -3,72% | +5,87% | -1,40% | +9,34% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 54 | 64,81% | +3,60% | +3,60% | -2,02% | +6,66% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 49 | 46,94% | -1,34% | +4,08% | -1,80% | +7,21% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 18 | 38,89% | -4,13% | +6,79% | -1,24% | +10,85% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 50 | 60,00% | +5,36% | +5,36% | -2,16% | +8,90% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 45 | 55,56% | +0,72% | +6,10% | -1,90% | +9,70% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 11 | 27,27% | -12,65% | +15,48% | -0,26% | +19,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 43 | 72,09% | +9,92% | +9,92% | -2,13% | +13,79% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 38 | 39,47% | -0,96% | +11,02% | -1,82% | +14,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 4 | 0,00% | -24,06% | +24,06% | -1,55% | +28,48% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 34 | 85,29% | +13,80% | +13,80% | -3,00% | +17,88% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 29 | 44,83% | -1,57% | +13,99% | -2,74% | +18,41% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Classic technical | 2 | 0,00% | -21,18% | +21,18% | -2,23% | +29,25% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 21 | 100,00% | +22,34% | +22,34% | -3,24% | +26,77% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 17 | 29,41% | -9,44% | +22,62% | -2,88% | +27,25% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 6 | 100,00% | +23,67% | +23,67% | -2,29% | +29,81% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 5 | 40,00% | -5,45% | +23,75% | -2,09% | +30,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 35 | 40,00% | -0,49% | +0,23% | -0,42% | +0,95% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 62 | 58,06% | +0,51% | +0,27% | -0,41% | +1,18% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 9 | 55,56% | +1,78% | +2,13% | +0,65% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 56 | 51,79% | +0,39% | +0,17% | -0,52% | +1,07% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 34 | 41,18% | -1,26% | +0,45% | -0,31% | +1,41% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 61 | 57,38% | +0,88% | +0,54% | -0,24% | +1,71% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,61% | +2,90% | +2,02% | +4,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 55 | 54,55% | +0,56% | +0,15% | -0,61% | +1,30% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 34 | 29,41% | -2,31% | +0,82% | -2,19% | +3,95% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 60 | 55,00% | +1,25% | +0,91% | -1,96% | +3,75% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,26% | +2,49% | -0,95% | +6,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 54 | 44,44% | +0,41% | +0,09% | -2,24% | +2,84% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 33 | 36,36% | -4,18% | +1,89% | -3,06% | +6,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 58 | 50,00% | +1,95% | +1,89% | -2,71% | +6,24% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 9 | 33,33% | +0,34% | +0,52% | -2,37% | +7,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 52 | 57,69% | +0,60% | +0,85% | -3,16% | +5,22% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 31 | 38,71% | -4,80% | +2,76% | -3,30% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 56 | 55,36% | +2,48% | +2,73% | -3,02% | +8,29% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 8 | 50,00% | +0,28% | +0,41% | -2,23% | +8,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 50 | 58,00% | +1,44% | +1,42% | -3,55% | +6,92% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 31 | 41,94% | -4,39% | +2,22% | -3,95% | +9,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 53 | 50,94% | +2,99% | +2,84% | -3,61% | +9,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 8 | 62,50% | +0,35% | +0,72% | -3,12% | +9,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 47 | 65,96% | +1,76% | +0,95% | -4,26% | +7,44% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 31 | 48,39% | -3,87% | +3,26% | -4,53% | +11,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 49 | 73,47% | +6,55% | +4,42% | -4,05% | +12,74% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 8 | 50,00% | +1,67% | +6,58% | -3,33% | +14,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 43 | 60,47% | +0,91% | +1,32% | -4,81% | +8,67% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 28 | 53,57% | -7,08% | +6,61% | -3,96% | +15,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 43 | 86,05% | +12,24% | +9,49% | -3,45% | +20,12% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 6 | 66,67% | +0,82% | +9,78% | -1,43% | +23,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 36 | 63,89% | -3,23% | +6,72% | -4,15% | +15,62% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 22 | 50,00% | -9,38% | +9,38% | -4,86% | +19,29% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 34 | 88,24% | +11,92% | +13,27% | -4,36% | +25,97% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,03% | +30,85% | -1,31% | +42,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 30 | 40,00% | -11,60% | +11,60% | -4,76% | +23,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 17 | 0,00% | -20,63% | +20,63% | -5,74% | +38,18% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 21 | 23,81% | -9,85% | +20,28% | -5,88% | +38,06% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 21 | 0,00% | -20,28% | +20,28% | -5,88% | +38,06% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Classic technical | 6 | 0,00% | -19,80% | +19,80% | -6,84% | +37,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 6 | 0,00% | -19,80% | +19,80% | -6,84% | +37,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 6 | 0,00% | -19,80% | +19,80% | -6,84% | +37,03% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 42 | 50,00% | +0,45% | +0,49% | -0,33% | +1,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 58 | 55,17% | +0,29% | +0,30% | -0,35% | +1,16% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 59 | 49,15% | +0,25% | +0,27% | -0,43% | +1,09% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 42 | 50,00% | +0,73% | +0,75% | -0,18% | +1,69% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 57 | 45,61% | +0,34% | +0,77% | -0,18% | +1,58% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 59 | 42,37% | +0,16% | +0,68% | -0,20% | +1,73% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 42 | 52,38% | +0,88% | +1,01% | -1,83% | +3,26% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 56 | 48,21% | +0,81% | +1,34% | -1,77% | +3,63% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 58 | 48,28% | +0,02% | +1,15% | -1,81% | +3,37% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 40 | 57,50% | +1,51% | +1,65% | -2,53% | +4,89% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 54 | 53,70% | +1,50% | +2,50% | -2,41% | +5,91% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 56 | 48,21% | -0,44% | +2,41% | -2,54% | +5,70% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 38 | 52,63% | +2,01% | +1,96% | -2,91% | +5,99% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 52 | 59,62% | +2,57% | +3,79% | -2,71% | +7,83% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 54 | 42,59% | -1,11% | +3,53% | -2,87% | +7,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 35 | 57,14% | +2,05% | +1,95% | -3,37% | +6,66% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 49 | 61,22% | +4,59% | +5,53% | -3,06% | +9,76% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 51 | 47,06% | -1,97% | +4,62% | -3,28% | +9,01% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 31 | 51,61% | +1,46% | +3,07% | -3,51% | +7,94% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 45 | 77,78% | +8,21% | +9,11% | -3,12% | +14,21% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 47 | 40,43% | -4,39% | +6,95% | -3,43% | +12,32% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 24 | 45,83% | -8,12% | +11,46% | -3,92% | +16,33% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 38 | 81,58% | +17,23% | +16,81% | -3,55% | +22,58% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 3 | 66,67% | +15,44% | +15,44% | -3,34% | +22,79% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 40 | 37,50% | -12,52% | +13,50% | -4,05% | +19,24% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 21 | 9,52% | -26,53% | +26,53% | -4,64% | +32,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 30 | 90,00% | +24,28% | +24,63% | -4,89% | +31,11% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +22,28% | +22,28% | -5,94% | +27,20% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 32 | 12,50% | -21,52% | +20,94% | -5,31% | +26,83% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 13 | 0,00% | -36,24% | +36,24% | -6,31% | +45,83% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 17 | 52,94% | +5,42% | +33,28% | -7,13% | +41,70% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 21 | 19,05% | -24,45% | +33,83% | -7,08% | +41,84% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 4 | 0,00% | -33,00% | +33,00% | -8,35% | +42,66% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 6 | 66,67% | +11,62% | +33,59% | -8,03% | +43,15% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 60 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 63 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 72 | 40,28% | +0,37% |
| BTC | BREVE | Famiglia statistica | 186 | 52,15% | +0,70% |
| BTC | BREVE | Microstruttura exchange | 15 | 40,00% | +0,30% |
| BTC | BREVE | Tecnico | 171 | 39,18% | +0,02% |
| BTC | SETTIMANALE | Classic technical | 70 | 50,00% | -2,52% |
| BTC | SETTIMANALE | Famiglia statistica | 170 | 58,24% | +2,70% |
| BTC | SETTIMANALE | Microstruttura exchange | 12 | 41,67% | -0,51% |
| BTC | SETTIMANALE | Tecnico | 155 | 43,87% | -1,34% |
| BTC | SWING | Classic technical | 29 | 34,48% | -7,36% |
| BTC | SWING | Famiglia statistica | 93 | 65,59% | +7,47% |
| BTC | SWING | Microstruttura exchange | 4 | 50,00% | +0,28% |
| BTC | SWING | Tecnico | 83 | 48,19% | -0,05% |
| BTC | MEDIO | Classic technical | 6 | 0,00% | -23,10% |
| BTC | MEDIO | Famiglia statistica | 61 | 91,80% | +17,71% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 51 | 39,22% | -4,58% |
| DOGE | BREVE | Classic technical | 103 | 36,89% | -1,34% |
| DOGE | BREVE | Famiglia statistica | 183 | 56,83% | +0,88% |
| DOGE | BREVE | Microstruttura exchange | 27 | 48,15% | +2,22% |
| DOGE | BREVE | Tecnico | 165 | 50,30% | +0,45% |
| DOGE | SETTIMANALE | Classic technical | 95 | 38,95% | -4,45% |
| DOGE | SETTIMANALE | Famiglia statistica | 167 | 52,10% | +2,46% |
| DOGE | SETTIMANALE | Microstruttura exchange | 25 | 48,00% | +0,32% |
| DOGE | SETTIMANALE | Tecnico | 149 | 60,40% | +1,25% |
| DOGE | SWING | Classic technical | 59 | 50,85% | -5,39% |
| DOGE | SWING | Famiglia statistica | 92 | 79,35% | +9,21% |
| DOGE | SWING | Microstruttura exchange | 14 | 57,14% | +1,30% |
| DOGE | SWING | Tecnico | 79 | 62,03% | -0,98% |
| DOGE | MEDIO | Classic technical | 45 | 24,44% | -15,02% |
| DOGE | MEDIO | Famiglia statistica | 61 | 57,38% | +1,31% |
| DOGE | MEDIO | Microstruttura exchange | 6 | 83,33% | +20,07% |
| DOGE | MEDIO | Tecnico | 57 | 21,05% | -15,66% |
| SOL | BREVE | Classic technical | 126 | 50,79% | +0,69% |
| SOL | BREVE | Famiglia statistica | 171 | 49,71% | +0,48% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 176 | 46,59% | +0,14% |
| SOL | SETTIMANALE | Classic technical | 113 | 55,75% | +1,85% |
| SOL | SETTIMANALE | Famiglia statistica | 155 | 58,06% | +2,84% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 161 | 45,96% | -1,15% |
| SOL | SWING | Classic technical | 55 | 49,09% | -2,72% |
| SOL | SWING | Famiglia statistica | 83 | 79,52% | +12,34% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 8 | 75,00% | +10,89% |
| SOL | SWING | Tecnico | 87 | 39,08% | -8,13% |
| SOL | MEDIO | Classic technical | 34 | 5,88% | -30,25% |
| SOL | MEDIO | Famiglia statistica | 51 | 70,59% | +13,50% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 3 | 100,00% | +25,70% |
| SOL | MEDIO | Tecnico | 59 | 20,34% | -19,20% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 5 | in attesa di controlli maturati |
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
