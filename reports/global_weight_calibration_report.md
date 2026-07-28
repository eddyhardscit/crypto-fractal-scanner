# Calibrazione pesi Global Confluence

Generato: 2026-07-28 05:15 UTC

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
| BTC | 20 | FEEDBACK RAPIDO | 19 | 0 | 0 | 0 | Famiglia statistica | 1g | 42,11% | -0,05% | feedback rapido: utile da osservare, non da pesare |
| SOL | 20 | FEEDBACK RAPIDO | 19 | 0 | 0 | 0 | Tecnico | 1g | 57,89% | +0,11% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 20 | FEEDBACK RAPIDO | 19 | 0 | 0 | 0 | Tecnico | 1g | 57,89% | +0,27% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 19 | 42,11% | -0,05% | -0,05% | -0,30% | +0,53% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 15 | 40,00% | -0,43% | +0,13% | -0,15% | +0,68% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 18 | 44,44% | +0,15% | +0,15% | -0,35% | +1,00% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 15 | 40,00% | -0,44% | +0,29% | -0,24% | +1,10% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 17 | 58,82% | +0,20% | +0,20% | -1,32% | +1,98% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 14 | 42,86% | +0,02% | +0,62% | -1,13% | +2,20% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 15 | 46,67% | +0,52% | +0,52% | -2,08% | +2,74% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 12 | 50,00% | -0,50% | +0,81% | -1,77% | +3,10% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 13 | 69,23% | +1,15% | +1,15% | -1,93% | +3,66% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 11 | 36,36% | -0,60% | +1,68% | -1,65% | +3,92% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 10 | 80,00% | +1,94% | +1,94% | -2,01% | +4,48% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 9 | 33,33% | -0,47% | +2,10% | -1,87% | +4,69% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 6 | 100,00% | +2,03% | +2,03% | -2,22% | +5,58% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 5 | 40,00% | +0,05% | +1,98% | -2,01% | +5,75% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 16 | 50,00% | -0,05% | +0,05% | -0,35% | +0,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 19 | 52,63% | +0,36% | -0,27% | -0,70% | +0,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 19 | 57,89% | +0,27% | -0,27% | -0,70% | +0,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 16 | 50,00% | -0,16% | +0,16% | -0,56% | +1,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 18 | 55,56% | +0,27% | -0,26% | -0,92% | +0,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 18 | 55,56% | +0,26% | -0,26% | -0,92% | +0,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 16 | 43,75% | +0,22% | -0,22% | -2,05% | +2,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 17 | 52,94% | +0,41% | -0,33% | -2,07% | +2,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 17 | 47,06% | +0,33% | -0,33% | -2,07% | +2,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 14 | 64,29% | +0,87% | -0,87% | -3,47% | +2,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 15 | 66,67% | +1,01% | -1,01% | -3,50% | +2,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 15 | 66,67% | +1,01% | -1,01% | -3,50% | +2,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 12 | 66,67% | +1,23% | -1,23% | -3,76% | +2,53% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 13 | 69,23% | +1,21% | -1,21% | -3,77% | +2,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 13 | 69,23% | +1,21% | -1,21% | -3,77% | +2,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 9 | 55,56% | +1,16% | -1,16% | -4,07% | +2,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 10 | 60,00% | +1,64% | -1,64% | -4,36% | +2,50% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 10 | 60,00% | +1,64% | -1,64% | -4,36% | +2,50% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 6 | 66,67% | +2,43% | -2,43% | -5,56% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 6 | 66,67% | +2,43% | -2,43% | -5,56% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 6 | 66,67% | +2,43% | -2,43% | -5,56% | +3,21% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 11 | 63,64% | +0,27% | -0,27% | -0,61% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 15 | 60,00% | -0,21% | -0,79% | -1,06% | -0,03% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 19 | 57,89% | +0,11% | -0,30% | -0,66% | +0,44% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 10 | 50,00% | +0,03% | -0,03% | -0,41% | +0,50% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 14 | 42,86% | -0,45% | -0,78% | -1,48% | +0,20% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 18 | 38,89% | -0,22% | -0,42% | -1,02% | +0,80% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 9 | 33,33% | -0,20% | +0,20% | -1,90% | +2,11% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 13 | 38,46% | -0,44% | -1,03% | -2,84% | +1,57% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 17 | 41,18% | -0,06% | -0,65% | -2,30% | +2,01% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 7 | 57,14% | +0,03% | -0,03% | -2,61% | +2,89% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 11 | 54,55% | -0,68% | -1,32% | -3,86% | +1,98% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 15 | 46,67% | -0,11% | -0,99% | -3,42% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 5 | 40,00% | -0,11% | +0,11% | -2,46% | +4,11% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 9 | 66,67% | -0,01% | -1,32% | -4,12% | +2,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 13 | 30,77% | -0,67% | -0,90% | -3,73% | +2,99% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 3 | 66,67% | +0,56% | -0,56% | -2,74% | +4,49% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 7 | 42,86% | -0,42% | -0,83% | -4,33% | +2,83% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 10 | 50,00% | +0,16% | -0,64% | -4,06% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 4 | 75,00% | +1,36% | -1,36% | -4,84% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 6 | 16,67% | -1,33% | -2,05% | -4,61% | +2,76% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 18 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 17 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 19 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 54 | 48,15% | +0,10% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 44 | 40,91% | -0,29% |
| BTC | SETTIMANALE | Famiglia statistica | 38 | 63,16% | +1,11% |
| BTC | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | +0,81% |
| BTC | SETTIMANALE | Tecnico | 32 | 40,62% | -0,53% |
| BTC | SWING | Famiglia statistica | 6 | 100,00% | +2,03% |
| BTC | SWING | Tecnico | 5 | 40,00% | +0,05% |
| DOGE | BREVE | Classic technical | 48 | 47,92% | +0,00% |
| DOGE | BREVE | Famiglia statistica | 54 | 53,70% | +0,35% |
| DOGE | BREVE | Microstruttura exchange | 6 | 100,00% | +3,99% |
| DOGE | BREVE | Tecnico | 54 | 53,70% | +0,28% |
| DOGE | SETTIMANALE | Classic technical | 35 | 62,86% | +1,07% |
| DOGE | SETTIMANALE | Famiglia statistica | 38 | 65,79% | +1,24% |
| DOGE | SETTIMANALE | Tecnico | 38 | 65,79% | +1,24% |
| DOGE | SWING | Classic technical | 6 | 66,67% | +2,43% |
| DOGE | SWING | Famiglia statistica | 6 | 66,67% | +2,43% |
| DOGE | SWING | Tecnico | 6 | 66,67% | +2,43% |
| SOL | BREVE | Classic technical | 30 | 50,00% | +0,05% |
| SOL | BREVE | Famiglia statistica | 42 | 47,62% | -0,36% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 54 | 46,30% | -0,05% |
| SOL | SETTIMANALE | Classic technical | 15 | 53,33% | +0,09% |
| SOL | SETTIMANALE | Famiglia statistica | 27 | 55,56% | -0,39% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -5,16% |
| SOL | SETTIMANALE | Tecnico | 38 | 42,11% | -0,23% |
| SOL | SWING | Famiglia statistica | 4 | 75,00% | +1,36% |
| SOL | SWING | Frattale SOL | 1 | 0,00% | -1,13% |
| SOL | SWING | Tecnico | 6 | 16,67% | -1,33% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 6 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 7 | in attesa di controlli maturati |
| BTC | SWING | 8 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 1 | in attesa di controlli maturati |
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
