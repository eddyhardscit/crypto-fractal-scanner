# Calibrazione pesi Global Confluence

Generato: 2026-09-13 05:33 UTC

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
| BTC | 65 | UTILE | 64 | 18 | 4 | 0 | Famiglia statistica | 1g | 53,12% | +0,33% | campione utile, valutare con prudenza |
| SOL | 65 | PRIMA CALIBRAZIONE | 59 | 25 | 0 | 0 | Famiglia statistica | 1g | 55,93% | +0,29% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 65 | UTILE | 63 | 25 | 3 | 0 | Famiglia statistica | 1g | 57,14% | +0,50% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 24 | 37,50% | +0,37% | +0,81% | +0,13% | +1,33% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 64 | 53,12% | +0,33% | +0,33% | -0,10% | +0,84% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 59 | 40,68% | +0,09% | +0,44% | -0,01% | +0,95% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 24 | 41,67% | +0,55% | +1,18% | +0,59% | +1,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 63 | 52,38% | +0,69% | +0,69% | +0,13% | +1,35% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 58 | 43,10% | +0,13% | +0,84% | +0,28% | +1,49% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 24 | 41,67% | +0,20% | +1,81% | -0,58% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 62 | 51,61% | +1,03% | +1,03% | -1,07% | +2,69% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 57 | 35,09% | -0,19% | +1,29% | -0,92% | +2,93% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 24 | 50,00% | -1,14% | +3,70% | -1,03% | +5,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 60 | 50,00% | +1,83% | +1,83% | -1,63% | +4,20% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 55 | 41,82% | -0,98% | +2,10% | -1,46% | +4,51% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 24 | 45,83% | -2,81% | +4,87% | -1,33% | +8,02% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 58 | 58,62% | +2,59% | +2,59% | -1,87% | +5,39% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 53 | 41,51% | -1,77% | +3,04% | -1,69% | +5,80% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 23 | 52,17% | -3,56% | +5,61% | -1,40% | +9,17% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 55 | 63,64% | +3,53% | +3,53% | -2,01% | +6,63% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 50 | 46,00% | -1,32% | +4,00% | -1,79% | +7,18% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 19 | 36,84% | -3,97% | +6,37% | -1,30% | +10,56% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 51 | 58,82% | +5,24% | +5,24% | -2,16% | +8,83% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 46 | 54,35% | +0,68% | +5,94% | -1,91% | +9,61% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 12 | 33,33% | -11,49% | +14,30% | -0,25% | +18,32% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 44 | 72,73% | +9,73% | +9,73% | -2,08% | +13,66% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | -1,61% | +6,04% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 39 | 41,03% | -0,91% | +10,77% | -1,78% | +14,79% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 5 | 0,00% | -23,88% | +23,88% | -1,27% | +29,00% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 35 | 85,71% | +14,07% | +14,07% | -2,92% | +18,26% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 30 | 43,33% | -2,29% | +14,30% | -2,66% | +18,83% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 2 | 0,00% | -21,18% | +21,18% | -2,23% | +29,25% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 22 | 100,00% | +22,27% | +22,27% | -3,21% | +26,86% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 18 | 27,78% | -10,08% | +22,53% | -2,87% | +27,34% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 7 | 100,00% | +23,11% | +23,11% | -2,47% | +29,48% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 6 | 50,00% | -1,25% | +23,08% | -2,34% | +29,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 36 | 38,89% | -0,49% | +0,24% | -0,39% | +0,95% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 63 | 57,14% | +0,50% | +0,27% | -0,40% | +1,17% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 9 | 55,56% | +1,78% | +2,13% | +0,65% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 57 | 50,88% | +0,38% | +0,18% | -0,51% | +1,07% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 35 | 40,00% | -1,26% | +0,47% | -0,28% | +1,41% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 62 | 56,45% | +0,84% | +0,55% | -0,22% | +1,70% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,61% | +2,90% | +2,02% | +4,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 56 | 53,57% | +0,53% | +0,17% | -0,59% | +1,30% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 34 | 29,41% | -2,31% | +0,82% | -2,19% | +3,95% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 61 | 55,74% | +1,25% | +0,88% | -1,98% | +3,73% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,26% | +2,49% | -0,95% | +6,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 55 | 45,45% | +0,42% | +0,07% | -2,26% | +2,83% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 34 | 35,29% | -4,23% | +1,67% | -3,21% | +6,23% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 59 | 50,85% | +2,02% | +1,76% | -2,80% | +6,16% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 9 | 33,33% | +0,34% | +0,52% | -2,37% | +7,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 53 | 56,60% | +0,48% | +0,72% | -3,25% | +5,15% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 32 | 37,50% | -4,86% | +2,47% | -3,47% | +7,93% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 57 | 56,14% | +2,55% | +2,57% | -3,13% | +8,16% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 9 | 44,44% | -0,49% | -0,37% | -2,97% | +7,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 51 | 56,86% | +1,28% | +1,26% | -3,66% | +6,80% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 31 | 41,94% | -4,39% | +2,22% | -3,95% | +9,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 54 | 50,00% | +2,88% | +2,84% | -3,54% | +9,74% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 8 | 62,50% | +0,35% | +0,72% | -3,12% | +9,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 48 | 66,67% | +1,79% | +1,00% | -4,15% | +7,58% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 31 | 48,39% | -3,87% | +3,26% | -4,53% | +11,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 50 | 74,00% | +6,43% | +4,32% | -4,08% | +12,70% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 8 | 50,00% | +1,67% | +6,58% | -3,33% | +14,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 44 | 59,09% | +0,89% | +1,29% | -4,83% | +8,72% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 29 | 51,72% | -7,05% | +6,17% | -4,21% | +14,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 44 | 84,09% | +11,83% | +9,14% | -3,63% | +19,75% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 6 | 66,67% | +0,82% | +9,78% | -1,43% | +23,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 37 | 62,16% | -3,31% | +6,37% | -4,34% | +15,31% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 23 | 47,83% | -9,94% | +9,94% | -4,66% | +20,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 35 | 88,57% | +12,22% | +13,53% | -4,24% | +26,48% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,03% | +30,85% | -1,31% | +42,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 30 | 40,00% | -11,60% | +11,60% | -4,76% | +23,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 18 | 0,00% | -20,70% | +20,70% | -5,55% | +38,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 22 | 27,27% | -8,41% | +20,35% | -5,72% | +38,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 22 | 0,00% | -20,35% | +20,35% | -5,72% | +38,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Classic technical | 6 | 0,00% | -19,80% | +19,80% | -6,84% | +37,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 7 | 0,00% | -19,08% | +19,08% | -7,01% | +36,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 7 | 0,00% | -19,08% | +19,08% | -7,01% | +36,77% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 42 | 50,00% | +0,45% | +0,49% | -0,33% | +1,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 59 | 55,93% | +0,29% | +0,30% | -0,34% | +1,15% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 59 | 49,15% | +0,25% | +0,27% | -0,43% | +1,09% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 42 | 50,00% | +0,73% | +0,75% | -0,18% | +1,69% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 58 | 46,55% | +0,38% | +0,79% | -0,14% | +1,60% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 59 | 42,37% | +0,16% | +0,68% | -0,20% | +1,73% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 42 | 52,38% | +0,88% | +1,01% | -1,83% | +3,26% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 57 | 47,37% | +0,80% | +1,31% | -1,80% | +3,62% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 59 | 47,46% | +0,01% | +1,12% | -1,84% | +3,37% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 41 | 56,10% | +1,44% | +1,58% | -2,57% | +4,83% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 55 | 52,73% | +1,44% | +2,43% | -2,45% | +5,84% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 57 | 47,37% | -0,46% | +2,34% | -2,57% | +5,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 39 | 51,28% | +1,86% | +1,81% | -3,01% | +5,86% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 53 | 58,49% | +2,45% | +3,64% | -2,79% | +7,70% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 55 | 41,82% | -1,16% | +3,40% | -2,94% | +7,43% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 36 | 58,33% | +2,04% | +1,94% | -3,32% | +6,67% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 50 | 62,00% | +4,54% | +5,45% | -3,03% | +9,70% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 52 | 48,08% | -1,90% | +4,57% | -3,24% | +8,97% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 32 | 50,00% | +1,32% | +2,88% | -3,62% | +7,75% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 46 | 76,09% | +7,96% | +8,85% | -3,21% | +13,94% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 48 | 39,58% | -4,36% | +6,74% | -3,51% | +12,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 25 | 48,00% | -7,41% | +11,38% | -3,75% | +16,41% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 39 | 79,49% | +16,55% | +16,62% | -3,45% | +22,47% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 3 | 66,67% | +15,44% | +15,44% | -3,34% | +22,79% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 41 | 39,02% | -11,99% | +13,40% | -3,94% | +19,22% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 21 | 9,52% | -26,53% | +26,53% | -4,64% | +32,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 31 | 90,32% | +24,63% | +24,97% | -4,79% | +31,59% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +22,28% | +22,28% | -5,94% | +27,20% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 33 | 12,12% | -21,93% | +21,36% | -5,20% | +27,41% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 14 | 0,00% | -36,41% | +36,41% | -6,13% | +46,12% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 18 | 55,56% | +7,27% | +33,58% | -6,94% | +42,15% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 22 | 18,18% | -25,10% | +34,05% | -6,93% | +42,20% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 5 | 20,00% | -20,14% | +32,67% | -8,45% | +42,50% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 7 | 57,14% | +5,48% | +33,27% | -8,15% | +42,97% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 61 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 64 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 72 | 40,28% | +0,37% |
| BTC | BREVE | Famiglia statistica | 189 | 52,38% | +0,68% |
| BTC | BREVE | Microstruttura exchange | 15 | 40,00% | +0,30% |
| BTC | BREVE | Tecnico | 174 | 39,66% | +0,01% |
| BTC | SETTIMANALE | Classic technical | 71 | 49,30% | -2,49% |
| BTC | SETTIMANALE | Famiglia statistica | 173 | 57,23% | +2,63% |
| BTC | SETTIMANALE | Microstruttura exchange | 13 | 38,46% | -0,72% |
| BTC | SETTIMANALE | Tecnico | 158 | 43,04% | -1,35% |
| BTC | SWING | Classic technical | 31 | 35,48% | -6,88% |
| BTC | SWING | Famiglia statistica | 95 | 65,26% | +7,32% |
| BTC | SWING | Microstruttura exchange | 5 | 60,00% | +0,49% |
| BTC | SWING | Tecnico | 85 | 48,24% | -0,05% |
| BTC | MEDIO | Classic technical | 7 | 0,00% | -23,11% |
| BTC | MEDIO | Famiglia statistica | 64 | 92,19% | +17,88% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 54 | 38,89% | -4,77% |
| DOGE | BREVE | Classic technical | 105 | 36,19% | -1,34% |
| DOGE | BREVE | Famiglia statistica | 186 | 56,45% | +0,86% |
| DOGE | BREVE | Microstruttura exchange | 27 | 48,15% | +2,22% |
| DOGE | BREVE | Tecnico | 168 | 50,00% | +0,44% |
| DOGE | SETTIMANALE | Classic technical | 97 | 38,14% | -4,49% |
| DOGE | SETTIMANALE | Famiglia statistica | 170 | 52,35% | +2,47% |
| DOGE | SETTIMANALE | Microstruttura exchange | 26 | 46,15% | +0,05% |
| DOGE | SETTIMANALE | Tecnico | 152 | 59,87% | +1,16% |
| DOGE | SWING | Classic technical | 60 | 50,00% | -5,41% |
| DOGE | SWING | Famiglia statistica | 94 | 78,72% | +8,95% |
| DOGE | SWING | Microstruttura exchange | 14 | 57,14% | +1,30% |
| DOGE | SWING | Tecnico | 81 | 60,49% | -1,03% |
| DOGE | MEDIO | Classic technical | 47 | 23,40% | -15,32% |
| DOGE | MEDIO | Famiglia statistica | 64 | 57,81% | +1,71% |
| DOGE | MEDIO | Microstruttura exchange | 6 | 83,33% | +20,07% |
| DOGE | MEDIO | Tecnico | 59 | 20,34% | -15,75% |
| SOL | BREVE | Classic technical | 126 | 50,79% | +0,69% |
| SOL | BREVE | Famiglia statistica | 174 | 50,00% | +0,48% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 177 | 46,33% | +0,14% |
| SOL | SETTIMANALE | Classic technical | 116 | 55,17% | +1,77% |
| SOL | SETTIMANALE | Famiglia statistica | 158 | 57,59% | +2,76% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 164 | 45,73% | -1,15% |
| SOL | SWING | Classic technical | 57 | 49,12% | -2,51% |
| SOL | SWING | Famiglia statistica | 85 | 77,65% | +11,90% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 8 | 75,00% | +10,89% |
| SOL | SWING | Tecnico | 89 | 39,33% | -7,87% |
| SOL | MEDIO | Classic technical | 35 | 5,71% | -30,49% |
| SOL | MEDIO | Famiglia statistica | 54 | 72,22% | +14,70% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 3 | 100,00% | +25,70% |
| SOL | MEDIO | Tecnico | 62 | 19,35% | -19,96% |

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
