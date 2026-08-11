# Calibrazione pesi Global Confluence

Generato: 2026-08-11 05:23 UTC

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
| BTC | 34 | PRIMA CALIBRAZIONE | 33 | 3 | 0 | 0 | Famiglia statistica | 1g | 51,52% | +0,00% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 34 | PRIMA CALIBRAZIONE | 32 | 3 | 0 | 0 | Tecnico | 1g | 50,00% | -0,02% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 34 | PRIMA CALIBRAZIONE | 33 | 6 | 0 | 0 | Famiglia statistica | 1g | 54,55% | +0,21% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 4 | 0,00% | -0,76% | +0,76% | +0,03% | +1,12% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 33 | 51,52% | +0,00% | +0,00% | -0,31% | +0,50% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 28 | 35,71% | -0,39% | +0,17% | -0,16% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 4 | 25,00% | -0,86% | +0,86% | +0,50% | +1,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 32 | 50,00% | +0,10% | +0,10% | -0,36% | +0,75% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 27 | 48,15% | -0,29% | +0,31% | -0,13% | +0,96% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 4 | 25,00% | -1,18% | +1,18% | -0,41% | +2,46% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 31 | 54,84% | +0,14% | +0,14% | -1,26% | +1,68% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 26 | 38,46% | -0,27% | +0,54% | -0,97% | +2,01% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 4 | 25,00% | -1,14% | +1,14% | -1,16% | +2,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 29 | 44,83% | +0,29% | +0,29% | -1,96% | +2,31% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 24 | 45,83% | -0,44% | +0,58% | -1,65% | +2,64% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,94% | +1,94% | -1,23% | +3,13% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 27 | 59,26% | +0,43% | +0,43% | -2,22% | +2,75% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 22 | 36,36% | -0,64% | +1,04% | -1,86% | +3,13% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Classic technical | 3 | 0,00% | -1,40% | +1,40% | -1,93% | +3,00% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 24 | 54,17% | +0,38% | +0,38% | -2,74% | +3,02% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 19 | 36,84% | -0,18% | +0,78% | -2,37% | +3,50% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Classic technical | 1 | 0,00% | -0,80% | +0,80% | -1,82% | +3,19% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 20 | 50,00% | +0,02% | +0,02% | -3,12% | +3,48% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 16 | 50,00% | +0,04% | +0,27% | -2,71% | +3,94% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 13 | 53,85% | +0,29% | +0,29% | -2,84% | +4,69% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 11 | 9,09% | -0,70% | +0,49% | -2,60% | +4,94% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 4 | 100,00% | +1,41% | +1,41% | -3,09% | +4,98% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 3 | 33,33% | -1,36% | +1,43% | -3,03% | +5,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 22 | 40,91% | -0,18% | +0,18% | -0,35% | +0,74% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 33 | 54,55% | +0,21% | -0,16% | -0,63% | +0,46% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,13% | +1,92% | +0,84% | +2,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 30 | 50,00% | +0,12% | -0,12% | -0,60% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 22 | 50,00% | -0,17% | +0,17% | -0,49% | +1,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 32 | 46,88% | +0,01% | -0,28% | -0,89% | +0,60% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 4 | 50,00% | +2,46% | +3,12% | +2,21% | +3,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 30 | 60,00% | +0,30% | -0,30% | -0,91% | +0,61% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 21 | 38,10% | +0,08% | -0,08% | -1,88% | +2,28% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 31 | 48,39% | -0,07% | -0,48% | -2,00% | +1,64% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,74% | +2,43% | +0,13% | +5,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 30 | 50,00% | +0,49% | -0,49% | -2,02% | +1,67% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 20 | 55,00% | +0,45% | -0,45% | -2,87% | +2,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 29 | 48,28% | +0,08% | -0,81% | -2,98% | +1,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 28 | 64,29% | +0,83% | -0,83% | -3,03% | +1,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 20 | 55,00% | +1,01% | -1,01% | -3,42% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 27 | 55,56% | +0,41% | -1,17% | -3,58% | +2,12% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 27 | 66,67% | +1,17% | -1,17% | -3,58% | +2,12% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 20 | 65,00% | +1,32% | -1,32% | -4,00% | +2,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 24 | 54,17% | +0,90% | -1,74% | -4,37% | +2,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 24 | 70,83% | +1,74% | -1,74% | -4,37% | +2,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 17 | 76,47% | +2,45% | -2,45% | -5,18% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 20 | 70,00% | +1,93% | -2,76% | -5,50% | +2,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 20 | 80,00% | +2,76% | -2,76% | -5,50% | +2,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 12 | 100,00% | +3,86% | -3,86% | -6,35% | +2,55% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 13 | 100,00% | +3,98% | -3,98% | -6,48% | +2,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 13 | 100,00% | +3,98% | -3,98% | -6,48% | +2,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 4 | 100,00% | +4,73% | -4,73% | -7,38% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 4 | 100,00% | +4,73% | -4,73% | -7,38% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 4 | 100,00% | +4,73% | -4,73% | -7,38% | +2,68% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 21 | 47,62% | -0,04% | +0,04% | -0,54% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 29 | 62,07% | +0,01% | -0,29% | -0,75% | +0,33% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 32 | 50,00% | -0,02% | -0,10% | -0,59% | +0,53% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 21 | 47,62% | -0,02% | +0,02% | -0,52% | +0,51% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 28 | 50,00% | -0,09% | -0,26% | -0,93% | +0,47% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 31 | 38,71% | -0,26% | -0,11% | -0,76% | +0,78% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 21 | 42,86% | -0,13% | +0,13% | -1,91% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 27 | 48,15% | -0,03% | -0,31% | -2,24% | +1,72% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 31 | 41,94% | -0,19% | -0,19% | -2,03% | +1,94% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 20 | 55,00% | +0,06% | -0,06% | -2,79% | +2,42% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 25 | 52,00% | -0,25% | -0,53% | -3,29% | +2,19% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 29 | 48,28% | -0,10% | -0,47% | -3,14% | +2,41% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 19 | 47,37% | +0,37% | -0,37% | -3,44% | +2,85% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 23 | 60,87% | +0,15% | -0,85% | -3,92% | +2,49% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 27 | 40,74% | -0,04% | -0,71% | -3,76% | +2,69% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 16 | 68,75% | +1,08% | -1,08% | -4,56% | +2,99% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 20 | 45,00% | -0,09% | -1,17% | -4,89% | +2,56% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 24 | 62,50% | +0,94% | -1,14% | -4,70% | +2,77% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 12 | 66,67% | +1,88% | -1,88% | -5,83% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 16 | 68,75% | +0,30% | -2,04% | -5,91% | +2,57% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 20 | 55,00% | +1,28% | -2,30% | -5,66% | +2,82% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Classic technical | 5 | 80,00% | +1,15% | -1,15% | -6,51% | +4,11% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 9 | 77,78% | +1,90% | -3,66% | -7,32% | +2,66% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 13 | 61,54% | -0,06% | -3,11% | -7,01% | +3,02% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 3 | 100,00% | +2,59% | -2,59% | -8,66% | +2,20% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 4 | 0,00% | -2,34% | -2,34% | -8,78% | +2,00% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 31 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 31 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 33 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 12 | 16,67% | -0,93% |
| BTC | BREVE | Famiglia statistica | 96 | 52,08% | +0,08% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 81 | 40,74% | -0,32% |
| BTC | SETTIMANALE | Classic technical | 11 | 9,09% | -1,50% |
| BTC | SETTIMANALE | Famiglia statistica | 80 | 52,50% | +0,36% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 65 | 40,00% | -0,43% |
| BTC | SWING | Classic technical | 1 | 0,00% | -0,80% |
| BTC | SWING | Famiglia statistica | 33 | 51,52% | +0,13% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 27 | 33,33% | -0,26% |
| BTC | MEDIO | Famiglia statistica | 4 | 100,00% | +1,41% |
| BTC | MEDIO | Tecnico | 3 | 33,33% | -1,36% |
| DOGE | BREVE | Classic technical | 65 | 43,08% | -0,09% |
| DOGE | BREVE | Famiglia statistica | 96 | 50,00% | +0,05% |
| DOGE | BREVE | Microstruttura exchange | 11 | 54,55% | +1,78% |
| DOGE | BREVE | Tecnico | 90 | 53,33% | +0,31% |
| DOGE | SETTIMANALE | Classic technical | 60 | 58,33% | +0,92% |
| DOGE | SETTIMANALE | Famiglia statistica | 80 | 52,50% | +0,44% |
| DOGE | SETTIMANALE | Microstruttura exchange | 6 | 100,00% | +1,18% |
| DOGE | SETTIMANALE | Tecnico | 79 | 67,09% | +1,22% |
| DOGE | SWING | Classic technical | 29 | 86,21% | +3,03% |
| DOGE | SWING | Famiglia statistica | 33 | 81,82% | +2,74% |
| DOGE | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% |
| DOGE | SWING | Tecnico | 33 | 87,88% | +3,24% |
| DOGE | MEDIO | Classic technical | 4 | 100,00% | +4,73% |
| DOGE | MEDIO | Famiglia statistica | 4 | 100,00% | +4,73% |
| DOGE | MEDIO | Tecnico | 4 | 100,00% | +4,73% |
| SOL | BREVE | Classic technical | 63 | 46,03% | -0,06% |
| SOL | BREVE | Famiglia statistica | 84 | 53,57% | -0,04% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 5 | 20,00% | -0,90% |
| SOL | BREVE | Tecnico | 94 | 43,62% | -0,15% |
| SOL | SETTIMANALE | Classic technical | 55 | 56,36% | +0,46% |
| SOL | SETTIMANALE | Famiglia statistica | 68 | 52,94% | -0,07% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 3 | 0,00% | -5,22% |
| SOL | SETTIMANALE | Tecnico | 80 | 50,00% | +0,23% |
| SOL | SWING | Classic technical | 17 | 70,59% | +1,67% |
| SOL | SWING | Famiglia statistica | 25 | 72,00% | +0,88% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 2 | 0,00% | -4,49% |
| SOL | SWING | Tecnico | 33 | 57,58% | +0,76% |
| SOL | MEDIO | Famiglia statistica | 3 | 100,00% | +2,59% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Tecnico | 4 | 0,00% | -2,34% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 3 | in attesa di controlli maturati |
| BTC | MEDIO | 13 | in attesa di controlli maturati |
| SOL | MEDIO | 12 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 3 | in attesa di controlli maturati |
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
