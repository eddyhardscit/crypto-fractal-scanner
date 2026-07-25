# Calibrazione pesi Global Confluence

Generato: 2026-07-25 05:15 UTC

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
| BTC | 17 | FEEDBACK RAPIDO | 16 | 0 | 0 | 0 | Famiglia statistica | 1g | 37,50% | +0,01% | feedback rapido: utile da osservare, non da pesare |
| SOL | 17 | FEEDBACK RAPIDO | 16 | 0 | 0 | 0 | Tecnico | 1g | 62,50% | +0,06% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 17 | FEEDBACK RAPIDO | 16 | 0 | 0 | 0 | Famiglia statistica | 1g | 56,25% | +0,38% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 16 | 37,50% | +0,01% | +0,01% | -0,21% | +0,65% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 13 | 38,46% | -0,56% | -0,00% | -0,25% | +0,63% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 15 | 46,67% | +0,25% | +0,25% | -0,27% | +1,23% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 12 | 41,67% | -0,36% | +0,45% | -0,10% | +1,41% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 14 | 64,29% | +0,42% | +0,42% | -1,13% | +2,20% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 11 | 36,36% | -0,21% | +1,01% | -0,84% | +2,54% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 12 | 58,33% | +1,15% | +1,15% | -1,75% | +3,22% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 11 | 45,45% | -0,83% | +1,16% | -1,61% | +3,33% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 10 | 80,00% | +1,68% | +1,68% | -1,90% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 9 | 44,44% | -0,49% | +1,91% | -1,75% | +3,95% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 7 | 85,71% | +2,41% | +2,41% | -2,36% | +4,35% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 6 | 33,33% | -0,29% | +2,73% | -2,20% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 3 | 100,00% | +1,92% | +1,92% | -3,05% | +5,02% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 2 | 0,00% | -1,75% | +1,75% | -2,93% | +5,15% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 15 | 53,33% | +0,32% | -0,32% | -0,58% | +0,35% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 16 | 56,25% | +0,38% | -0,38% | -0,65% | +0,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +0,68% | +0,68% | +0,59% | +1,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 16 | 56,25% | +0,38% | -0,38% | -0,65% | +0,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 14 | 57,14% | +0,62% | -0,62% | -1,21% | +0,75% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 15 | 60,00% | +0,74% | -0,74% | -1,28% | +0,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 15 | 60,00% | +0,74% | -0,74% | -1,28% | +0,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 13 | 53,85% | +0,87% | -0,87% | -2,11% | +1,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 14 | 57,14% | +0,96% | -0,96% | -2,13% | +1,80% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 14 | 57,14% | +0,96% | -0,96% | -2,13% | +1,80% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 11 | 63,64% | +0,86% | -0,86% | -2,75% | +2,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 12 | 66,67% | +1,03% | -1,03% | -2,84% | +2,35% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 12 | 66,67% | +1,03% | -1,03% | -2,84% | +2,35% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 9 | 77,78% | +1,52% | -1,52% | -3,15% | +2,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 10 | 80,00% | +1,47% | -1,47% | -3,22% | +2,49% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 10 | 80,00% | +1,47% | -1,47% | -3,22% | +2,49% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 6 | 66,67% | +1,44% | -1,44% | -3,19% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 7 | 71,43% | +2,09% | -2,09% | -3,74% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 7 | 71,43% | +2,09% | -2,09% | -3,74% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 3 | 100,00% | +4,48% | -4,48% | -5,49% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 3 | 100,00% | +4,48% | -4,48% | -5,49% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 3 | 100,00% | +4,48% | -4,48% | -5,49% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 8 | 75,00% | +0,23% | -0,23% | -0,50% | +0,38% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 12 | 58,33% | -0,17% | -0,89% | -1,10% | -0,06% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 16 | 62,50% | +0,06% | -0,28% | -0,62% | +0,50% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 7 | 42,86% | +0,00% | -0,00% | -0,33% | +0,54% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 11 | 45,45% | -0,55% | -0,97% | -1,71% | +0,14% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 15 | 33,33% | -0,28% | -0,49% | -1,10% | +0,87% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 6 | 16,67% | -0,80% | +0,80% | -1,32% | +2,54% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 10 | 40,00% | -0,27% | -1,04% | -2,77% | +1,67% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 14 | 35,71% | -0,28% | -0,57% | -2,14% | +2,17% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 5 | 40,00% | -1,33% | +1,33% | -1,45% | +3,95% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 8 | 62,50% | -0,04% | -0,46% | -3,18% | +2,58% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 12 | 33,33% | -1,04% | -0,33% | -2,85% | +2,99% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 3 | 33,33% | -0,43% | +0,43% | -1,86% | +4,49% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 7 | 71,43% | +0,71% | -0,62% | -3,85% | +2,78% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 10 | 20,00% | -1,57% | -0,46% | -3,51% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 5 | 40,00% | -0,48% | -1,26% | -4,94% | +2,28% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 7 | 42,86% | -0,02% | -0,68% | -4,63% | +2,58% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 2 | 100,00% | +1,84% | -1,84% | -5,73% | +1,74% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 3 | 0,00% | -2,78% | -2,78% | -5,70% | +1,62% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 16 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 14 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 16 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 45 | 48,89% | +0,22% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 36 | 38,89% | -0,38% |
| BTC | SETTIMANALE | Famiglia statistica | 29 | 72,41% | +1,64% |
| BTC | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% |
| BTC | SETTIMANALE | Tecnico | 26 | 42,31% | -0,59% |
| BTC | SWING | Famiglia statistica | 3 | 100,00% | +1,92% |
| BTC | SWING | Tecnico | 2 | 0,00% | -1,75% |
| DOGE | BREVE | Classic technical | 42 | 54,76% | +0,59% |
| DOGE | BREVE | Famiglia statistica | 45 | 57,78% | +0,68% |
| DOGE | BREVE | Microstruttura exchange | 1 | 100,00% | +0,68% |
| DOGE | BREVE | Tecnico | 45 | 57,78% | +0,68% |
| DOGE | SETTIMANALE | Classic technical | 26 | 69,23% | +1,22% |
| DOGE | SETTIMANALE | Famiglia statistica | 29 | 72,41% | +1,44% |
| DOGE | SETTIMANALE | Tecnico | 29 | 72,41% | +1,44% |
| DOGE | SWING | Classic technical | 3 | 100,00% | +4,48% |
| DOGE | SWING | Famiglia statistica | 3 | 100,00% | +4,48% |
| DOGE | SWING | Tecnico | 3 | 100,00% | +4,48% |
| SOL | BREVE | Classic technical | 21 | 47,62% | -0,14% |
| SOL | BREVE | Famiglia statistica | 33 | 48,48% | -0,33% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 45 | 44,44% | -0,16% |
| SOL | SETTIMANALE | Classic technical | 8 | 37,50% | -0,99% |
| SOL | SETTIMANALE | Famiglia statistica | 20 | 60,00% | +0,11% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Tecnico | 29 | 31,03% | -0,98% |
| SOL | SWING | Famiglia statistica | 2 | 100,00% | +1,84% |
| SOL | SWING | Frattale SOL | 1 | 0,00% | -1,13% |
| SOL | SWING | Tecnico | 3 | 0,00% | -2,78% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 6 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 8 | in attesa di controlli maturati |
| BTC | SWING | 8 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 4 | in attesa di controlli maturati |
| SOL | SWING | 7 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 5 | in attesa di controlli maturati |
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
