# Calibrazione pesi Global Confluence

Generato: 2026-08-10 05:17 UTC

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
| BTC | 33 | PRIMA CALIBRAZIONE | 32 | 3 | 0 | 0 | Famiglia statistica | 1g | 53,12% | +0,05% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 33 | PRIMA CALIBRAZIONE | 31 | 3 | 0 | 0 | Tecnico | 1g | 48,39% | -0,05% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 33 | PRIMA CALIBRAZIONE | 32 | 5 | 0 | 0 | Famiglia statistica | 1g | 53,12% | +0,21% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 4 | 0,00% | -0,76% | +0,76% | +0,03% | +1,12% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 32 | 53,12% | +0,05% | +0,05% | -0,27% | +0,56% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 27 | 37,04% | -0,34% | +0,24% | -0,10% | +0,75% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 4 | 25,00% | -0,86% | +0,86% | +0,50% | +1,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 31 | 51,61% | +0,14% | +0,14% | -0,32% | +0,81% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 26 | 50,00% | -0,25% | +0,37% | -0,08% | +1,03% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 4 | 25,00% | -1,18% | +1,18% | -0,41% | +2,46% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 30 | 56,67% | +0,20% | +0,20% | -1,24% | +1,72% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 25 | 40,00% | -0,21% | +0,63% | -0,94% | +2,07% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 4 | 25,00% | -1,14% | +1,14% | -1,16% | +2,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 28 | 46,43% | +0,35% | +0,35% | -1,97% | +2,37% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 23 | 47,83% | -0,40% | +0,67% | -1,66% | +2,72% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,94% | +1,94% | -1,23% | +3,13% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 26 | 57,69% | +0,44% | +0,44% | -2,31% | +2,76% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 21 | 33,33% | -0,68% | +1,09% | -1,95% | +3,16% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Classic technical | 2 | 0,00% | -1,45% | +1,45% | -2,23% | +2,64% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 23 | 52,17% | +0,34% | +0,34% | -2,81% | +2,99% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 18 | 38,89% | -0,12% | +0,75% | -2,43% | +3,48% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 19 | 47,37% | -0,02% | -0,02% | -3,19% | +3,50% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 15 | 53,33% | +0,10% | +0,23% | -2,77% | +3,98% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 12 | 58,33% | +0,52% | +0,52% | -2,66% | +4,93% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 11 | 9,09% | -0,70% | +0,49% | -2,60% | +4,94% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 3 | 100,00% | +1,85% | +1,85% | -3,05% | +5,02% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 2 | 0,00% | -2,09% | +2,09% | -2,93% | +5,15% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 22 | 40,91% | -0,18% | +0,18% | -0,35% | +0,74% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 32 | 53,12% | +0,21% | -0,17% | -0,64% | +0,45% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,13% | +1,92% | +0,84% | +2,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 30 | 50,00% | +0,12% | -0,12% | -0,60% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 21 | 47,62% | -0,19% | +0,19% | -0,49% | +1,28% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 31 | 48,39% | +0,02% | -0,29% | -0,90% | +0,60% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 3 | 66,67% | +3,33% | +4,20% | +3,09% | +4,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 30 | 60,00% | +0,30% | -0,30% | -0,91% | +0,61% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 21 | 38,10% | +0,08% | -0,08% | -1,88% | +2,28% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 30 | 50,00% | -0,06% | -0,48% | -2,03% | +1,66% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,74% | +2,43% | +0,13% | +5,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 29 | 48,28% | +0,50% | -0,50% | -2,05% | +1,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 20 | 55,00% | +0,45% | -0,45% | -2,87% | +2,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 28 | 50,00% | +0,09% | -0,83% | -3,03% | +1,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 28 | 64,29% | +0,83% | -0,83% | -3,03% | +1,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 20 | 55,00% | +1,01% | -1,01% | -3,42% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 26 | 57,69% | +0,45% | -1,20% | -3,62% | +2,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 26 | 65,38% | +1,20% | -1,20% | -3,62% | +2,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 19 | 63,16% | +1,37% | -1,37% | -4,08% | +2,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 23 | 56,52% | +0,95% | -1,80% | -4,45% | +2,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 23 | 69,57% | +1,80% | -1,80% | -4,45% | +2,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 16 | 75,00% | +2,59% | -2,59% | -5,33% | +2,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 19 | 73,68% | +2,04% | -2,90% | -5,64% | +2,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 19 | 78,95% | +2,90% | -2,90% | -5,64% | +2,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 11 | 100,00% | +3,84% | -3,84% | -6,32% | +2,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 12 | 100,00% | +3,98% | -3,98% | -6,47% | +2,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 12 | 100,00% | +3,98% | -3,98% | -6,47% | +2,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 3 | 100,00% | +4,95% | -4,95% | -7,62% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 3 | 100,00% | +4,95% | -4,95% | -7,62% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 3 | 100,00% | +4,95% | -4,95% | -7,62% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 21 | 47,62% | -0,04% | +0,04% | -0,54% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 28 | 64,29% | +0,05% | -0,26% | -0,74% | +0,36% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 31 | 48,39% | -0,05% | -0,06% | -0,57% | +0,56% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 21 | 47,62% | -0,02% | +0,02% | -0,52% | +0,51% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 27 | 51,85% | -0,08% | -0,26% | -0,96% | +0,47% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 31 | 38,71% | -0,26% | -0,11% | -0,76% | +0,78% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 21 | 42,86% | -0,13% | +0,13% | -1,91% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 26 | 46,15% | -0,09% | -0,39% | -2,39% | +1,63% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 30 | 43,33% | -0,14% | -0,26% | -2,15% | +1,87% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 20 | 55,00% | +0,06% | -0,06% | -2,79% | +2,42% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 24 | 50,00% | -0,35% | -0,64% | -3,34% | +2,08% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 28 | 50,00% | -0,03% | -0,56% | -3,18% | +2,33% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 18 | 50,00% | +0,54% | -0,54% | -3,53% | +2,71% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 22 | 59,09% | +0,03% | -1,01% | -4,01% | +2,36% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 26 | 42,31% | +0,06% | -0,85% | -3,84% | +2,58% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 15 | 73,33% | +1,39% | -1,39% | -4,75% | +2,78% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 19 | 42,11% | -0,28% | -1,42% | -5,05% | +2,37% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 23 | 65,22% | +1,14% | -1,35% | -4,83% | +2,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 11 | 72,73% | +2,36% | -2,36% | -6,04% | +2,90% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 15 | 66,67% | +0,10% | -2,40% | -6,07% | +2,35% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 19 | 57,89% | +1,53% | -2,60% | -5,78% | +2,66% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Classic technical | 5 | 80,00% | +1,15% | -1,15% | -6,51% | +4,11% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 8 | 87,50% | +2,53% | -3,72% | -7,04% | +2,92% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 12 | 58,33% | -0,33% | -3,10% | -6,80% | +3,22% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 2 | 100,00% | +3,39% | -3,39% | -9,20% | +1,74% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 3 | 0,00% | -2,79% | -2,79% | -9,18% | +1,62% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 30 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 30 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 32 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 12 | 16,67% | -0,93% |
| BTC | BREVE | Famiglia statistica | 93 | 53,76% | +0,13% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 78 | 42,31% | -0,27% |
| BTC | SETTIMANALE | Classic technical | 10 | 10,00% | -1,52% |
| BTC | SETTIMANALE | Famiglia statistica | 77 | 51,95% | +0,38% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 62 | 40,32% | -0,41% |
| BTC | SWING | Famiglia statistica | 31 | 51,61% | +0,19% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 26 | 34,62% | -0,24% |
| BTC | MEDIO | Famiglia statistica | 3 | 100,00% | +1,85% |
| BTC | MEDIO | Tecnico | 2 | 0,00% | -2,09% |
| DOGE | BREVE | Classic technical | 64 | 42,19% | -0,10% |
| DOGE | BREVE | Famiglia statistica | 93 | 50,54% | +0,06% |
| DOGE | BREVE | Microstruttura exchange | 10 | 60,00% | +1,97% |
| DOGE | BREVE | Tecnico | 89 | 52,81% | +0,31% |
| DOGE | SETTIMANALE | Classic technical | 59 | 57,63% | +0,93% |
| DOGE | SETTIMANALE | Famiglia statistica | 77 | 54,55% | +0,47% |
| DOGE | SETTIMANALE | Microstruttura exchange | 6 | 100,00% | +1,18% |
| DOGE | SETTIMANALE | Tecnico | 77 | 66,23% | +1,24% |
| DOGE | SWING | Classic technical | 27 | 85,19% | +3,10% |
| DOGE | SWING | Famiglia statistica | 31 | 83,87% | +2,79% |
| DOGE | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% |
| DOGE | SWING | Tecnico | 31 | 87,10% | +3,31% |
| DOGE | MEDIO | Classic technical | 3 | 100,00% | +4,95% |
| DOGE | MEDIO | Famiglia statistica | 3 | 100,00% | +4,95% |
| DOGE | MEDIO | Tecnico | 3 | 100,00% | +4,95% |
| SOL | BREVE | Classic technical | 63 | 46,03% | -0,06% |
| SOL | BREVE | Famiglia statistica | 81 | 54,32% | -0,04% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 4 | 25,00% | -1,06% |
| SOL | BREVE | Tecnico | 92 | 43,48% | -0,15% |
| SOL | SETTIMANALE | Classic technical | 53 | 58,49% | +0,60% |
| SOL | SETTIMANALE | Famiglia statistica | 65 | 50,77% | -0,20% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 3 | 0,00% | -5,22% |
| SOL | SETTIMANALE | Tecnico | 77 | 51,95% | +0,35% |
| SOL | SWING | Classic technical | 16 | 75,00% | +1,98% |
| SOL | SWING | Famiglia statistica | 23 | 73,91% | +0,94% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% |
| SOL | SWING | Tecnico | 31 | 58,06% | +0,81% |
| SOL | MEDIO | Famiglia statistica | 2 | 100,00% | +3,39% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Tecnico | 3 | 0,00% | -2,79% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 4 | in attesa di controlli maturati |
| BTC | MEDIO | 13 | in attesa di controlli maturati |
| SOL | SWING | 1 | in attesa di controlli maturati |
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
