# Calibrazione pesi Global Confluence

Generato: 2026-09-14 05:33 UTC

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
| BTC | 66 | UTILE | 65 | 18 | 5 | 0 | Famiglia statistica | 1g | 53,85% | +0,33% | campione utile, valutare con prudenza |
| SOL | 66 | UTILE | 60 | 25 | 2 | 0 | Famiglia statistica | 1g | 55,00% | +0,27% | campione utile, valutare con prudenza |
| DOGE | 66 | UTILE | 64 | 26 | 4 | 0 | Famiglia statistica | 1g | 57,81% | +0,50% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 24 | 37,50% | +0,37% | +0,81% | +0,13% | +1,33% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 65 | 53,85% | +0,33% | +0,33% | -0,12% | +0,84% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 60 | 41,67% | +0,09% | +0,44% | -0,03% | +0,94% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Classic technical | 24 | 41,67% | +0,55% | +1,18% | +0,59% | +1,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 64 | 53,12% | +0,69% | +0,69% | +0,12% | +1,34% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 59 | 44,07% | +0,14% | +0,84% | +0,26% | +1,48% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 24 | 41,67% | +0,20% | +1,81% | -0,58% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 63 | 52,38% | +1,02% | +1,02% | -1,07% | +2,66% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 58 | 36,21% | -0,17% | +1,28% | -0,92% | +2,89% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 24 | 50,00% | -1,14% | +3,70% | -1,03% | +5,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 61 | 49,18% | +1,77% | +1,77% | -1,66% | +4,15% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 56 | 41,07% | -0,99% | +2,03% | -1,50% | +4,45% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 24 | 45,83% | -2,81% | +4,87% | -1,33% | +8,02% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 59 | 57,63% | +2,49% | +2,49% | -1,92% | +5,30% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 54 | 40,74% | -1,79% | +2,93% | -1,74% | +5,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 24 | 50,00% | -3,59% | +5,20% | -1,59% | +8,77% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 56 | 62,50% | +3,39% | +3,39% | -2,08% | +6,51% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | -0,67% | -0,67% | -3,33% | +2,78% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 51 | 45,10% | -1,38% | +3,84% | -1,88% | +7,03% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 20 | 35,00% | -3,81% | +6,02% | -1,36% | +10,30% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 52 | 57,69% | +5,12% | +5,12% | -2,17% | +8,76% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 47 | 53,19% | +0,65% | +5,80% | -1,92% | +9,52% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 13 | 38,46% | -10,55% | +13,25% | -0,31% | +17,44% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 45 | 73,33% | +9,53% | +9,53% | -2,06% | +13,51% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | -1,61% | +6,04% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 40 | 42,50% | -0,87% | +10,52% | -1,76% | +14,59% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 6 | 0,00% | -23,72% | +23,72% | -1,17% | +29,25% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 36 | 86,11% | +14,32% | +14,32% | -2,85% | +18,60% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 31 | 41,94% | -2,96% | +14,58% | -2,59% | +19,21% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 2 | 0,00% | -21,18% | +21,18% | -2,23% | +29,25% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 23 | 100,00% | +22,19% | +22,19% | -3,22% | +26,90% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 18 | 27,78% | -10,08% | +22,53% | -2,87% | +27,34% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 8 | 100,00% | +22,85% | +22,85% | -2,52% | +29,35% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 7 | 42,86% | -4,08% | +22,79% | -2,41% | +29,43% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 37 | 40,54% | -0,45% | +0,21% | -0,47% | +0,90% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 64 | 57,81% | +0,50% | +0,25% | -0,44% | +1,14% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 9 | 55,56% | +1,78% | +2,13% | +0,65% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 58 | 51,72% | +0,39% | +0,16% | -0,55% | +1,03% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 36 | 41,67% | -1,21% | +0,44% | -0,34% | +1,37% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 63 | 57,14% | +0,84% | +0,54% | -0,26% | +1,67% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,61% | +2,90% | +2,02% | +4,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 57 | 54,39% | +0,52% | +0,16% | -0,62% | +1,27% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 35 | 28,57% | -2,25% | +0,80% | -2,18% | +3,88% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 62 | 54,84% | +1,23% | +0,87% | -1,98% | +3,70% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,26% | +2,49% | -0,95% | +6,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 56 | 44,64% | +0,41% | +0,07% | -2,26% | +2,81% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 34 | 35,29% | -4,23% | +1,67% | -3,21% | +6,23% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 60 | 51,67% | +2,10% | +1,62% | -2,90% | +6,01% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 9 | 33,33% | +0,34% | +0,52% | -2,37% | +7,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 54 | 55,56% | +0,34% | +0,58% | -3,36% | +5,01% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 33 | 36,36% | -4,92% | +2,18% | -3,64% | +7,73% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 58 | 56,90% | +2,62% | +2,40% | -3,23% | +8,04% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 9 | 44,44% | -0,49% | -0,37% | -2,97% | +7,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 52 | 55,77% | +1,13% | +1,10% | -3,76% | +6,70% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 31 | 41,94% | -4,39% | +2,22% | -3,95% | +9,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 55 | 50,91% | +2,89% | +2,73% | -3,57% | +9,72% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 8 | 62,50% | +0,35% | +0,72% | -3,12% | +9,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 49 | 65,31% | +1,69% | +0,91% | -4,18% | +7,60% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 31 | 48,39% | -3,87% | +3,26% | -4,53% | +11,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 51 | 72,55% | +6,27% | +4,27% | -4,06% | +12,72% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 8 | 50,00% | +1,67% | +6,58% | -3,33% | +14,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 45 | 60,00% | +0,90% | +1,29% | -4,79% | +8,83% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 30 | 50,00% | -7,09% | +5,68% | -4,48% | +14,53% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 21g | SWING | Famiglia statistica | 45 | 82,22% | +11,38% | +8,75% | -3,82% | +19,37% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 7 | 57,14% | -0,50% | +7,18% | -3,01% | +20,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 38 | 60,53% | -3,45% | +5,98% | -4,56% | +14,98% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 23 | 47,83% | -9,94% | +9,94% | -4,66% | +20,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 36 | 88,89% | +12,43% | +13,70% | -4,16% | +26,93% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,03% | +30,85% | -1,31% | +42,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 31 | 41,94% | -10,58% | +11,86% | -4,65% | +24,29% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 19 | 0,00% | -20,66% | +20,66% | -5,42% | +38,70% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 23 | 30,43% | -7,17% | +20,34% | -5,61% | +38,50% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 23 | 0,00% | -20,34% | +20,34% | -5,61% | +38,50% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Classic technical | 7 | 0,00% | -19,13% | +19,13% | -6,85% | +37,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 8 | 0,00% | -18,58% | +18,58% | -7,00% | +36,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 8 | 0,00% | -18,58% | +18,58% | -7,00% | +36,78% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 42 | 50,00% | +0,45% | +0,49% | -0,33% | +1,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 60 | 55,00% | +0,27% | +0,28% | -0,38% | +1,12% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 60 | 48,33% | +0,23% | +0,26% | -0,46% | +1,06% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| SOL | 2g | BREVE | Classic technical | 42 | 50,00% | +0,73% | +0,75% | -0,18% | +1,69% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 59 | 45,76% | +0,36% | +0,77% | -0,18% | +1,57% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 59 | 42,37% | +0,16% | +0,68% | -0,20% | +1,73% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 42 | 52,38% | +0,88% | +1,01% | -1,83% | +3,26% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 58 | 48,28% | +0,81% | +1,32% | -1,77% | +3,61% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 59 | 47,46% | +0,01% | +1,12% | -1,84% | +3,37% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 42 | 54,76% | +1,33% | +1,47% | -2,64% | +4,74% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 56 | 51,79% | +1,36% | +2,33% | -2,50% | +5,76% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 58 | 46,55% | -0,50% | +2,24% | -2,62% | +5,57% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 40 | 50,00% | +1,71% | +1,66% | -3,10% | +5,71% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 54 | 57,41% | +2,32% | +3,50% | -2,86% | +7,55% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 56 | 41,07% | -1,22% | +3,26% | -3,01% | +7,29% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 37 | 56,76% | +1,92% | +1,82% | -3,36% | +6,58% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 51 | 60,78% | +4,40% | +5,29% | -3,07% | +9,57% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 53 | 47,17% | -1,91% | +4,43% | -3,27% | +8,86% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 33 | 48,48% | +1,24% | +2,75% | -3,66% | +7,65% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 47 | 74,47% | +7,76% | +8,63% | -3,25% | +13,74% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 49 | 38,78% | -4,30% | +6,57% | -3,54% | +11,95% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 26 | 50,00% | -6,83% | +11,23% | -3,55% | +16,44% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 40 | 80,00% | +16,32% | +16,39% | -3,32% | +22,34% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 3 | 66,67% | +15,44% | +15,44% | -3,34% | +22,79% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 42 | 40,48% | -11,52% | +13,26% | -3,81% | +19,17% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 21 | 9,52% | -26,53% | +26,53% | -4,64% | +32,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 32 | 90,62% | +24,92% | +25,25% | -4,69% | +32,04% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +22,28% | +22,28% | -5,94% | +27,20% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 34 | 11,76% | -22,29% | +21,74% | -5,09% | +27,95% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 15 | 0,00% | -36,42% | +36,42% | -6,02% | +46,29% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 19 | 57,89% | +8,81% | +33,73% | -6,82% | +42,49% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 23 | 17,39% | -25,59% | +34,15% | -6,82% | +42,48% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Classic technical | 1 | 0,00% | -32,91% | +32,91% | -6,98% | +44,79% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 6 | 16,67% | -22,26% | +32,71% | -8,21% | +42,88% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 8 | 50,00% | +0,68% | +33,22% | -8,00% | +43,20% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 62 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 65 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 72 | 40,28% | +0,37% |
| BTC | BREVE | Famiglia statistica | 192 | 53,12% | +0,68% |
| BTC | BREVE | Microstruttura exchange | 15 | 40,00% | +0,30% |
| BTC | BREVE | Tecnico | 177 | 40,68% | +0,02% |
| BTC | SETTIMANALE | Classic technical | 72 | 48,61% | -2,51% |
| BTC | SETTIMANALE | Famiglia statistica | 176 | 56,25% | +2,53% |
| BTC | SETTIMANALE | Microstruttura exchange | 14 | 35,71% | -0,97% |
| BTC | SETTIMANALE | Tecnico | 161 | 42,24% | -1,38% |
| BTC | SWING | Classic technical | 33 | 36,36% | -6,46% |
| BTC | SWING | Famiglia statistica | 97 | 64,95% | +7,17% |
| BTC | SWING | Microstruttura exchange | 5 | 60,00% | +0,49% |
| BTC | SWING | Tecnico | 87 | 48,28% | -0,05% |
| BTC | MEDIO | Classic technical | 8 | 0,00% | -23,08% |
| BTC | MEDIO | Famiglia statistica | 67 | 92,54% | +18,04% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 56 | 37,50% | -5,39% |
| DOGE | BREVE | Classic technical | 108 | 37,04% | -1,29% |
| DOGE | BREVE | Famiglia statistica | 189 | 56,61% | +0,85% |
| DOGE | BREVE | Microstruttura exchange | 27 | 48,15% | +2,22% |
| DOGE | BREVE | Tecnico | 171 | 50,29% | +0,44% |
| DOGE | SETTIMANALE | Classic technical | 98 | 37,76% | -4,51% |
| DOGE | SETTIMANALE | Famiglia statistica | 173 | 53,18% | +2,53% |
| DOGE | SETTIMANALE | Microstruttura exchange | 26 | 46,15% | +0,05% |
| DOGE | SETTIMANALE | Tecnico | 155 | 58,71% | +1,03% |
| DOGE | SWING | Classic technical | 61 | 49,18% | -5,45% |
| DOGE | SWING | Famiglia statistica | 96 | 77,08% | +8,66% |
| DOGE | SWING | Microstruttura exchange | 15 | 53,33% | +0,66% |
| DOGE | SWING | Tecnico | 83 | 60,24% | -1,09% |
| DOGE | MEDIO | Classic technical | 49 | 22,45% | -15,41% |
| DOGE | MEDIO | Famiglia statistica | 67 | 58,21% | +2,00% |
| DOGE | MEDIO | Microstruttura exchange | 6 | 83,33% | +20,07% |
| DOGE | MEDIO | Tecnico | 62 | 20,97% | -15,23% |
| SOL | BREVE | Classic technical | 126 | 50,79% | +0,69% |
| SOL | BREVE | Famiglia statistica | 177 | 49,72% | +0,48% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 178 | 46,07% | +0,14% |
| SOL | SETTIMANALE | Classic technical | 119 | 53,78% | +1,64% |
| SOL | SETTIMANALE | Famiglia statistica | 161 | 56,52% | +2,65% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 167 | 44,91% | -1,19% |
| SOL | SWING | Classic technical | 59 | 49,15% | -2,32% |
| SOL | SWING | Famiglia statistica | 87 | 77,01% | +11,70% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 8 | 75,00% | +10,89% |
| SOL | SWING | Tecnico | 91 | 39,56% | -7,63% |
| SOL | MEDIO | Classic technical | 37 | 5,41% | -30,71% |
| SOL | MEDIO | Famiglia statistica | 57 | 71,93% | +14,58% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 3 | 100,00% | +25,70% |
| SOL | MEDIO | Tecnico | 65 | 18,46% | -20,63% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 5 | in attesa di controlli maturati |
| SOL | MEDIO | 1 | in attesa di controlli maturati |
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
