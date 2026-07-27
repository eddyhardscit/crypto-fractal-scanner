# Calibrazione pesi Global Confluence

Generato: 2026-07-27 05:14 UTC

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
| BTC | 19 | FEEDBACK RAPIDO | 18 | 0 | 0 | 0 | Famiglia statistica | 1g | 44,44% | +0,12% | feedback rapido: utile da osservare, non da pesare |
| SOL | 19 | FEEDBACK RAPIDO | 18 | 0 | 0 | 0 | Tecnico | 1g | 55,56% | -0,12% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 19 | FEEDBACK RAPIDO | 18 | 0 | 0 | 0 | Famiglia statistica | 1g | 55,56% | +0,61% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 18 | 44,44% | +0,12% | +0,12% | -0,12% | +0,69% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 15 | 40,00% | -0,43% | +0,13% | -0,15% | +0,68% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 17 | 47,06% | +0,26% | +0,26% | -0,24% | +1,13% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 14 | 42,86% | -0,35% | +0,43% | -0,10% | +1,26% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 16 | 62,50% | +0,28% | +0,28% | -1,30% | +1,96% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 13 | 38,46% | -0,07% | +0,75% | -1,10% | +2,20% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 14 | 50,00% | +0,78% | +0,78% | -1,97% | +2,90% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 11 | 45,45% | -0,83% | +1,16% | -1,61% | +3,33% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 12 | 75,00% | +1,51% | +1,51% | -1,79% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 11 | 36,36% | -0,60% | +1,68% | -1,65% | +3,92% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 9 | 88,89% | +2,24% | +2,24% | -2,09% | +4,45% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 8 | 25,00% | -0,63% | +2,46% | -1,94% | +4,69% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 5 | 100,00% | +2,17% | +2,17% | -2,65% | +5,30% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 4 | 50,00% | +0,40% | +2,15% | -2,49% | +5,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 16 | 50,00% | -0,05% | +0,05% | -0,35% | +0,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 18 | 55,56% | +0,61% | -0,06% | -0,48% | +0,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 18 | 55,56% | +0,06% | -0,06% | -0,48% | +0,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 16 | 50,00% | -0,16% | +0,16% | -0,56% | +1,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 17 | 58,82% | +0,57% | +0,01% | -0,66% | +1,18% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 17 | 52,94% | -0,01% | +0,01% | -0,66% | +1,18% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 15 | 46,67% | +0,28% | -0,28% | -2,18% | +2,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 16 | 50,00% | +0,39% | -0,39% | -2,20% | +2,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +5,61% | +5,61% | +0,26% | +6,46% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 16 | 50,00% | +0,39% | -0,39% | -2,20% | +2,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 13 | 61,54% | +0,69% | -0,69% | -3,32% | +2,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 14 | 64,29% | +0,85% | -0,85% | -3,36% | +2,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 14 | 64,29% | +0,85% | -0,85% | -3,36% | +2,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 11 | 63,64% | +0,98% | -0,98% | -3,54% | +2,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 12 | 66,67% | +0,98% | -0,98% | -3,57% | +2,46% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 12 | 66,67% | +0,98% | -0,98% | -3,57% | +2,46% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 8 | 50,00% | +0,89% | -0,89% | -3,88% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 9 | 55,56% | +1,46% | -1,46% | -4,23% | +2,55% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 9 | 55,56% | +1,46% | -1,46% | -4,23% | +2,55% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 5 | 60,00% | +2,33% | -2,33% | -5,62% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 5 | 60,00% | +2,33% | -2,33% | -5,62% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 5 | 60,00% | +2,33% | -2,33% | -5,62% | +2,99% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 10 | 60,00% | -0,12% | +0,12% | -0,23% | +0,63% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 14 | 64,29% | +0,06% | -0,55% | -0,82% | +0,18% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 18 | 55,56% | -0,12% | -0,09% | -0,45% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 9 | 44,44% | -0,24% | +0,24% | -0,14% | +0,70% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 13 | 46,15% | -0,30% | -0,66% | -1,37% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 17 | 35,29% | -0,37% | -0,30% | -0,92% | +0,91% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 8 | 25,00% | -0,38% | +0,38% | -1,93% | +1,91% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 12 | 41,67% | -0,37% | -1,02% | -2,94% | +1,40% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 16 | 37,50% | -0,14% | -0,61% | -2,35% | +1,90% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 6 | 50,00% | -0,80% | +0,80% | -2,14% | +3,43% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 10 | 60,00% | -0,25% | -0,95% | -3,71% | +2,21% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 14 | 42,86% | -0,48% | -0,70% | -3,28% | +2,67% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 5 | 40,00% | -0,11% | +0,11% | -2,46% | +4,11% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 8 | 75,00% | +0,78% | -0,69% | -3,79% | +2,87% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 12 | 25,00% | -1,25% | -0,45% | -3,48% | +3,19% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 2 | 50,00% | -0,27% | +0,27% | -2,80% | +4,20% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 7 | 42,86% | -0,42% | -0,83% | -4,33% | +2,83% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 9 | 44,44% | -0,07% | -0,47% | -4,22% | +2,94% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 4 | 75,00% | +1,36% | -1,36% | -4,84% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 5 | 0,00% | -2,04% | -2,02% | -5,00% | +2,26% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 18 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 16 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 18 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 51 | 50,98% | +0,22% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 42 | 40,48% | -0,29% |
| BTC | SETTIMANALE | Famiglia statistica | 35 | 68,57% | +1,41% |
| BTC | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | +0,81% |
| BTC | SETTIMANALE | Tecnico | 30 | 36,67% | -0,69% |
| BTC | SWING | Famiglia statistica | 5 | 100,00% | +2,17% |
| BTC | SWING | Tecnico | 4 | 50,00% | +0,40% |
| DOGE | BREVE | Classic technical | 47 | 48,94% | +0,02% |
| DOGE | BREVE | Famiglia statistica | 51 | 54,90% | +0,53% |
| DOGE | BREVE | Microstruttura exchange | 5 | 100,00% | +4,65% |
| DOGE | BREVE | Tecnico | 51 | 52,94% | +0,14% |
| DOGE | SETTIMANALE | Classic technical | 32 | 59,38% | +0,84% |
| DOGE | SETTIMANALE | Famiglia statistica | 35 | 62,86% | +1,05% |
| DOGE | SETTIMANALE | Tecnico | 35 | 62,86% | +1,05% |
| DOGE | SWING | Classic technical | 5 | 60,00% | +2,33% |
| DOGE | SWING | Famiglia statistica | 5 | 60,00% | +2,33% |
| DOGE | SWING | Tecnico | 5 | 60,00% | +2,33% |
| SOL | BREVE | Classic technical | 27 | 44,44% | -0,24% |
| SOL | BREVE | Famiglia statistica | 39 | 51,28% | -0,19% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 51 | 43,14% | -0,21% |
| SOL | SETTIMANALE | Classic technical | 13 | 46,15% | -0,46% |
| SOL | SETTIMANALE | Famiglia statistica | 25 | 60,00% | +0,03% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% |
| SOL | SETTIMANALE | Tecnico | 35 | 37,14% | -0,64% |
| SOL | SWING | Famiglia statistica | 4 | 75,00% | +1,36% |
| SOL | SWING | Frattale SOL | 1 | 0,00% | -1,13% |
| SOL | SWING | Tecnico | 5 | 0,00% | -2,04% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 6 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 7 | in attesa di controlli maturati |
| BTC | SWING | 8 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 2 | in attesa di controlli maturati |
| SOL | SWING | 7 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 6 | in attesa di controlli maturati |
| DOGE | SWING | 7 | in attesa di controlli maturati |
| DOGE | MEDIO | 15 | in attesa di controlli maturati |

## Come leggere le raccomandazioni

- **OSSERVA**: meno di 30 controlli, nessuna modifica.
- **PESO OK / MANTIENI**: il modulo sta aiutando, ma non serve cambiare peso.
- **NON AUMENTARE**: il modulo non dimostra ancora un vantaggio sufficiente.
- **POSSIBILE AUMENTO LEGGERO**: proposta prudente, mai automatica.
- **POSSIBILE RIDUZIONE**: modulo debole con campione già abbastanza maturo.
- **ESCLUSO**: benchmark o diagnostica già inclusa in un'altra famiglia.

Nota decisiva: **non sommare mai una modifica alla Famiglia statistica e altre modifiche separate a Scanner o Market Regime**. Scanner e Market servono soltanto a capire quale parte della famiglia sta funzionando o fallendo.

## Stato attuale

Siamo ancora in feedback rapido. Non bisogna modificare i pesi del Global. La nuova struttura serve ad accumulare dati corretti senza doppio conteggio.
