# Calibrazione pesi Global Confluence

Generato: 2026-07-20 05:14 UTC

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
| BTC | 12 | FEEDBACK RAPIDO | 11 | 0 | 0 | 0 | Famiglia statistica | 1g | 36,36% | +0,03% | feedback rapido: utile da osservare, non da pesare |
| SOL | 12 | FEEDBACK RAPIDO | 11 | 0 | 0 | 0 | Tecnico | 1g | 54,55% | -0,13% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 12 | FEEDBACK RAPIDO | 11 | 0 | 0 | 0 | Famiglia statistica | 1g | 63,64% | +0,26% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 11 | 36,36% | +0,03% | +0,03% | -0,14% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 10 | 30,00% | -0,73% | +0,00% | -0,17% | +0,77% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 10 | 50,00% | +0,30% | +0,30% | -0,30% | +1,45% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 9 | 33,33% | -0,47% | +0,34% | -0,30% | +1,51% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 9 | 66,67% | +0,30% | +0,30% | -1,30% | +2,10% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 8 | 37,50% | -0,02% | +0,56% | -1,21% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 7 | 42,86% | +0,64% | +0,64% | -2,36% | +2,73% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 6 | 50,00% | -0,24% | +0,57% | -2,20% | +2,84% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 5 | 60,00% | +0,88% | +0,88% | -2,65% | +3,10% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 4 | 75,00% | +0,68% | +1,19% | -2,49% | +3,23% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 2 | 100,00% | +1,45% | +1,45% | -2,80% | +3,08% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 1 | 0,00% | -2,40% | +2,40% | -2,32% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 10 | 60,00% | +0,17% | -0,17% | -0,39% | +0,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 11 | 63,64% | +0,26% | -0,26% | -0,51% | +0,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 11 | 63,64% | +0,26% | -0,26% | -0,51% | +0,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 9 | 55,56% | +0,10% | -0,10% | -0,84% | +1,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 10 | 60,00% | +0,33% | -0,33% | -0,98% | +1,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 10 | 60,00% | +0,33% | -0,33% | -0,98% | +1,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 8 | 62,50% | +0,43% | -0,43% | -1,74% | +2,28% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 9 | 66,67% | +0,62% | -0,62% | -1,81% | +2,09% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 9 | 66,67% | +0,62% | -0,62% | -1,81% | +2,09% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 6 | 50,00% | +0,42% | -0,42% | -2,60% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 7 | 57,14% | +0,77% | -0,77% | -2,79% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 7 | 57,14% | +0,77% | -0,77% | -2,79% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 5 | 80,00% | +1,08% | -1,08% | -2,94% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 5 | 80,00% | +1,08% | -1,08% | -2,94% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 5 | 80,00% | +1,08% | -1,08% | -2,94% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 2 | 100,00% | +1,70% | -1,70% | -3,25% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 2 | 100,00% | +1,70% | -1,70% | -3,25% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 2 | 100,00% | +1,70% | -1,70% | -3,25% | +2,87% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 4 | 75,00% | -0,01% | +0,01% | -0,13% | +0,66% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 8 | 75,00% | +0,18% | -0,68% | -0,88% | +0,20% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 11 | 54,55% | -0,13% | -0,20% | -0,54% | +0,66% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 3 | 33,33% | -0,42% | +0,42% | +0,19% | +1,21% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 7 | 57,14% | -0,10% | -0,81% | -1,71% | +0,57% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 10 | 20,00% | -0,68% | -0,46% | -1,21% | +1,23% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 2 | 0,00% | -0,63% | +0,63% | -2,09% | +1,54% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 7 | 42,86% | -0,27% | -0,70% | -2,61% | +1,72% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 9 | 33,33% | -0,40% | -0,93% | -2,51% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 5 | 80,00% | +1,16% | -1,96% | -4,05% | +1,91% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 7 | 28,57% | -0,83% | -1,52% | -3,86% | +2,31% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 4 | 100,00% | +1,74% | -1,74% | -4,35% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 5 | 20,00% | -1,94% | -2,13% | -4,42% | +2,26% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 2 | 100,00% | +2,36% | -2,36% | -5,73% | +1,74% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 2 | 0,00% | -2,36% | -2,36% | -5,73% | +1,74% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 11 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 11 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 11 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 30 | 50,00% | +0,20% |
| BTC | BREVE | Tecnico | 27 | 33,33% | -0,43% |
| BTC | SETTIMANALE | Famiglia statistica | 14 | 57,14% | +0,84% |
| BTC | SETTIMANALE | Tecnico | 11 | 54,55% | -0,10% |
| DOGE | BREVE | Classic technical | 27 | 59,26% | +0,22% |
| DOGE | BREVE | Famiglia statistica | 30 | 63,33% | +0,39% |
| DOGE | BREVE | Tecnico | 30 | 63,33% | +0,39% |
| DOGE | SETTIMANALE | Classic technical | 13 | 69,23% | +0,87% |
| DOGE | SETTIMANALE | Famiglia statistica | 14 | 71,43% | +1,01% |
| DOGE | SETTIMANALE | Tecnico | 14 | 71,43% | +1,01% |
| SOL | BREVE | Classic technical | 9 | 44,44% | -0,28% |
| SOL | BREVE | Famiglia statistica | 22 | 59,09% | -0,05% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Tecnico | 30 | 36,67% | -0,40% |
| SOL | SETTIMANALE | Famiglia statistica | 11 | 90,91% | +1,59% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Tecnico | 14 | 21,43% | -1,45% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 9 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 9 | in attesa di controlli maturati |
| BTC | SWING | 10 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | BREVE | 3 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 6 | in attesa di controlli maturati |
| SOL | SWING | 10 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 6 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 6 | in attesa di controlli maturati |
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
