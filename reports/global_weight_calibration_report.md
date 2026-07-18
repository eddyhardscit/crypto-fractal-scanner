# Calibrazione pesi Global Confluence

Generato: 2026-07-18 05:14 UTC

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
| BTC | 10 | FEEDBACK RAPIDO | 9 | 0 | 0 | 0 | Famiglia statistica | 1g | 33,33% | -0,02% | feedback rapido: utile da osservare, non da pesare |
| SOL | 10 | FEEDBACK RAPIDO | 9 | 0 | 0 | 0 | Tecnico | 1g | 55,56% | -0,00% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 10 | FEEDBACK RAPIDO | 9 | 0 | 0 | 0 | Famiglia statistica | 1g | 66,67% | +0,24% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 9 | 33,33% | -0,02% | -0,02% | -0,18% | +0,69% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 8 | 37,50% | -0,63% | -0,06% | -0,23% | +0,72% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 8 | 37,50% | +0,10% | +0,10% | -0,61% | +1,35% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 7 | 42,86% | -0,28% | +0,12% | -0,64% | +1,42% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 7 | 57,14% | +0,11% | +0,11% | -1,37% | +2,22% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 6 | 50,00% | +0,30% | +0,41% | -1,26% | +2,43% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 5 | 40,00% | +0,29% | +0,29% | -2,65% | +2,73% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 4 | 75,00% | +0,65% | +0,10% | -2,49% | +2,89% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 3 | 33,33% | +0,22% | +0,22% | -3,05% | +2,82% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 2 | 50,00% | -0,51% | +0,51% | -2,93% | +2,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 8 | 62,50% | +0,12% | -0,12% | -0,38% | +0,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 9 | 66,67% | +0,24% | -0,24% | -0,53% | +0,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 9 | 66,67% | +0,24% | -0,24% | -0,53% | +0,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 7 | 57,14% | +0,07% | -0,07% | -1,01% | +1,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 8 | 62,50% | +0,36% | -0,36% | -1,16% | +1,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 8 | 62,50% | +0,36% | -0,36% | -1,16% | +1,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 6 | 50,00% | +0,35% | -0,35% | -1,80% | +2,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 7 | 57,14% | +0,61% | -0,61% | -1,89% | +2,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 7 | 57,14% | +0,61% | -0,61% | -1,89% | +2,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 5 | 60,00% | +0,61% | -0,61% | -2,85% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 5 | 60,00% | +0,61% | -0,61% | -2,85% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 5 | 60,00% | +0,61% | -0,61% | -2,85% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 3 | 66,67% | +1,43% | -1,43% | -3,54% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 3 | 66,67% | +1,43% | -1,43% | -3,54% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 3 | 66,67% | +1,43% | -1,43% | -3,54% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 2 | 100,00% | +0,71% | -0,71% | -0,59% | -0,30% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 7 | 71,43% | +0,20% | -0,78% | -1,00% | +0,04% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 9 | 55,56% | -0,00% | -0,40% | -0,73% | +0,44% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 1 | 100,00% | +1,41% | -1,41% | -1,33% | -0,87% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 6 | 66,67% | +0,09% | -1,15% | -2,07% | +0,39% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 8 | 25,00% | -0,52% | -0,91% | -1,75% | +0,97% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 5 | 60,00% | -0,13% | -1,23% | -2,82% | +1,80% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 7 | 42,86% | -0,33% | -1,37% | -2,63% | +2,08% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 4 | 100,00% | +1,95% | -1,95% | -3,73% | +2,42% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 5 | 20,00% | -1,27% | -2,03% | -3,92% | +2,22% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 2 | 100,00% | +2,96% | -2,96% | -4,75% | +1,74% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 3 | 0,00% | -3,20% | -3,20% | -4,73% | +1,62% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 9 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 9 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 9 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 24 | 41,67% | +0,06% |
| BTC | BREVE | Tecnico | 21 | 42,86% | -0,25% |
| BTC | SETTIMANALE | Famiglia statistica | 8 | 37,50% | +0,26% |
| BTC | SETTIMANALE | Tecnico | 6 | 66,67% | +0,27% |
| DOGE | BREVE | Classic technical | 21 | 57,14% | +0,17% |
| DOGE | BREVE | Famiglia statistica | 24 | 62,50% | +0,39% |
| DOGE | BREVE | Tecnico | 24 | 62,50% | +0,39% |
| DOGE | SETTIMANALE | Classic technical | 8 | 62,50% | +0,92% |
| DOGE | SETTIMANALE | Famiglia statistica | 8 | 62,50% | +0,92% |
| DOGE | SETTIMANALE | Tecnico | 8 | 62,50% | +0,92% |
| SOL | BREVE | Classic technical | 3 | 100,00% | +0,94% |
| SOL | BREVE | Famiglia statistica | 18 | 66,67% | +0,07% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Tecnico | 24 | 41,67% | -0,27% |
| SOL | SETTIMANALE | Famiglia statistica | 6 | 100,00% | +2,29% |
| SOL | SETTIMANALE | Frattale SOL | 2 | 0,00% | -3,27% |
| SOL | SETTIMANALE | Tecnico | 8 | 12,50% | -2,00% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 9 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 11 | in attesa di controlli maturati |
| BTC | SWING | 10 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | BREVE | 4 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 9 | in attesa di controlli maturati |
| SOL | SWING | 10 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 6 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 9 | in attesa di controlli maturati |
| DOGE | SWING | 10 | in attesa di controlli maturati |
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
