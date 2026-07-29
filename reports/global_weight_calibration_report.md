# Calibrazione pesi Global Confluence

Generato: 2026-07-29 05:15 UTC

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
| BTC | 21 | FEEDBACK RAPIDO | 20 | 0 | 0 | 0 | Famiglia statistica | 1g | 45,00% | -0,00% | feedback rapido: utile da osservare, non da pesare |
| SOL | 21 | FEEDBACK RAPIDO | 20 | 0 | 0 | 0 | Tecnico | 1g | 55,00% | +0,09% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 21 | FEEDBACK RAPIDO | 20 | 0 | 0 | 0 | Famiglia statistica | 1g | 55,00% | +0,39% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 1 | 0,00% | -0,84% | +0,84% | +0,30% | +1,01% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 20 | 45,00% | -0,00% | -0,00% | -0,27% | +0,55% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 16 | 37,50% | -0,46% | +0,17% | -0,12% | +0,70% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 19 | 42,11% | +0,03% | +0,03% | -0,47% | +0,84% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 15 | 40,00% | -0,44% | +0,29% | -0,24% | +1,10% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 18 | 55,56% | +0,14% | +0,14% | -1,32% | +1,97% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 15 | 40,00% | -0,04% | +0,52% | -1,15% | +2,18% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 16 | 43,75% | +0,36% | +0,36% | -2,11% | +2,61% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 13 | 53,85% | -0,30% | +0,58% | -1,84% | +2,90% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 14 | 64,29% | +0,81% | +0,81% | -2,08% | +3,40% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 11 | 36,36% | -0,60% | +1,68% | -1,65% | +3,92% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 11 | 72,73% | +1,64% | +1,64% | -2,00% | +4,38% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 10 | 30,00% | -0,56% | +1,76% | -1,87% | +4,56% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 7 | 85,71% | +1,60% | +1,60% | -2,36% | +5,31% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 6 | 33,33% | -0,12% | +1,49% | -2,20% | +5,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 17 | 47,06% | -0,11% | +0,11% | -0,33% | +0,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 20 | 55,00% | +0,39% | -0,21% | -0,66% | +0,46% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 20 | 55,00% | +0,21% | -0,21% | -0,66% | +0,46% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 16 | 50,00% | -0,16% | +0,16% | -0,56% | +1,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 19 | 52,63% | +0,09% | -0,41% | -1,08% | +0,70% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 19 | 57,89% | +0,41% | -0,41% | -1,08% | +0,70% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 16 | 43,75% | +0,22% | -0,22% | -2,05% | +2,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 18 | 50,00% | +0,17% | -0,53% | -2,22% | +2,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 18 | 50,00% | +0,53% | -0,53% | -2,22% | +2,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 15 | 60,00% | +0,66% | -0,66% | -3,23% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 16 | 62,50% | +0,80% | -0,80% | -3,27% | +2,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +2,30% | +2,30% | +0,26% | +6,93% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 16 | 62,50% | +0,80% | -0,80% | -3,27% | +2,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 13 | 69,23% | +1,40% | -1,40% | -3,99% | +2,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 14 | 71,43% | +1,38% | -1,38% | -3,98% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 14 | 71,43% | +1,38% | -1,38% | -3,98% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 10 | 60,00% | +1,29% | -1,29% | -4,23% | +2,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 11 | 63,64% | +1,72% | -1,72% | -4,49% | +2,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 11 | 63,64% | +1,72% | -1,72% | -4,49% | +2,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 6 | 66,67% | +2,43% | -2,43% | -5,56% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 7 | 71,43% | +2,73% | -2,73% | -5,85% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 7 | 71,43% | +2,73% | -2,73% | -5,85% | +2,82% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 12 | 58,33% | +0,22% | -0,22% | -0,61% | +0,37% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 16 | 62,50% | -0,18% | -0,72% | -1,03% | +0,04% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 20 | 55,00% | +0,09% | -0,27% | -0,66% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 11 | 54,55% | +0,37% | -0,37% | -0,80% | +0,17% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 15 | 40,00% | -0,68% | -0,99% | -1,69% | -0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 19 | 42,11% | -0,00% | -0,60% | -1,21% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 10 | 40,00% | +0,03% | -0,03% | -2,00% | +2,20% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 14 | 35,71% | -0,56% | -1,11% | -2,85% | +1,68% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 18 | 44,44% | +0,07% | -0,73% | -2,34% | +2,07% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 8 | 62,50% | +0,40% | -0,40% | -2,75% | +2,81% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 12 | 50,00% | -0,87% | -1,46% | -3,85% | +2,00% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 16 | 50,00% | +0,08% | -1,11% | -3,44% | +2,45% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 6 | 50,00% | +0,83% | -0,83% | -3,11% | +3,56% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 10 | 70,00% | +0,55% | -1,75% | -4,34% | +2,44% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 14 | 35,71% | -0,22% | -1,23% | -3,92% | +2,84% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 4 | 75,00% | +1,26% | -1,26% | -3,10% | +4,25% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 8 | 50,00% | +0,05% | -1,14% | -4,31% | +2,92% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 11 | 54,55% | +0,45% | -0,89% | -4,07% | +3,19% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 5 | 60,00% | +0,04% | -2,14% | -5,08% | +2,28% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 7 | 28,57% | -0,39% | -2,51% | -4,81% | +2,58% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 19 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 18 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 20 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 1 | 0,00% | -0,84% |
| BTC | BREVE | Famiglia statistica | 57 | 47,37% | +0,05% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 46 | 39,13% | -0,31% |
| BTC | SETTIMANALE | Famiglia statistica | 41 | 58,54% | +0,86% |
| BTC | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | +0,81% |
| BTC | SETTIMANALE | Tecnico | 34 | 41,18% | -0,47% |
| BTC | SWING | Famiglia statistica | 7 | 85,71% | +1,60% |
| BTC | SWING | Tecnico | 6 | 33,33% | -0,12% |
| DOGE | BREVE | Classic technical | 49 | 46,94% | -0,02% |
| DOGE | BREVE | Famiglia statistica | 57 | 52,63% | +0,22% |
| DOGE | BREVE | Microstruttura exchange | 6 | 100,00% | +3,99% |
| DOGE | BREVE | Tecnico | 57 | 54,39% | +0,38% |
| DOGE | SETTIMANALE | Classic technical | 38 | 63,16% | +1,08% |
| DOGE | SETTIMANALE | Famiglia statistica | 41 | 65,85% | +1,24% |
| DOGE | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +2,30% |
| DOGE | SETTIMANALE | Tecnico | 41 | 65,85% | +1,24% |
| DOGE | SWING | Classic technical | 6 | 66,67% | +2,43% |
| DOGE | SWING | Famiglia statistica | 7 | 71,43% | +2,73% |
| DOGE | SWING | Tecnico | 7 | 71,43% | +2,73% |
| SOL | BREVE | Classic technical | 33 | 51,52% | +0,21% |
| SOL | BREVE | Famiglia statistica | 45 | 46,67% | -0,46% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 57 | 47,37% | +0,05% |
| SOL | SETTIMANALE | Classic technical | 18 | 61,11% | +0,73% |
| SOL | SETTIMANALE | Famiglia statistica | 30 | 56,67% | -0,15% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -5,16% |
| SOL | SETTIMANALE | Tecnico | 41 | 46,34% | +0,08% |
| SOL | SWING | Famiglia statistica | 5 | 60,00% | +0,04% |
| SOL | SWING | Frattale SOL | 1 | 0,00% | -1,13% |
| SOL | SWING | Tecnico | 7 | 28,57% | -0,39% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 5 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 7 | in attesa di controlli maturati |
| BTC | SWING | 8 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 1 | in attesa di controlli maturati |
| SOL | SWING | 7 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 5 | in attesa di controlli maturati |
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
