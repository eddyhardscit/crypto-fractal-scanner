# Calibrazione pesi Global Confluence

Generato: 2026-07-15 07:27 UTC

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
| BTC | 7 | FEEDBACK RAPIDO | 6 | 0 | 0 | 0 | Famiglia statistica | 1g | 33,33% | +0,13% | feedback rapido: utile da osservare, non da pesare |
| SOL | 7 | FEEDBACK RAPIDO | 6 | 0 | 0 | 0 | Tecnico | 1g | 33,33% | -0,57% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 7 | FEEDBACK RAPIDO | 6 | 0 | 0 | 0 | Famiglia statistica | 1g | 66,67% | -0,00% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 6 | 33,33% | +0,13% | +0,13% | -0,08% | +0,91% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 5 | 40,00% | -0,90% | +0,10% | -0,14% | +1,01% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 5 | 40,00% | +0,01% | +0,01% | -1,10% | +1,47% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 4 | 50,00% | +0,39% | +0,02% | -1,28% | +1,60% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 4 | 50,00% | -0,51% | -0,51% | -2,32% | +1,44% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 3 | 66,67% | +0,84% | -0,10% | -2,43% | +1,62% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 2 | 50,00% | -0,02% | -0,02% | -2,80% | +2,16% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 1 | 100,00% | +1,09% | -1,09% | -2,32% | +2,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 6 | 66,67% | -0,00% | +0,00% | -0,38% | +0,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 6 | 66,67% | -0,00% | +0,00% | -0,38% | +0,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 6 | 66,67% | -0,00% | +0,00% | -0,38% | +0,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 5 | 60,00% | +0,19% | -0,19% | -1,41% | +1,86% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 5 | 60,00% | +0,19% | -0,19% | -1,41% | +1,86% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 5 | 60,00% | +0,19% | -0,19% | -1,41% | +1,86% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 4 | 75,00% | +0,86% | -0,86% | -2,50% | +2,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 4 | 75,00% | +0,86% | -0,86% | -2,50% | +2,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 4 | 75,00% | +0,86% | -0,86% | -2,50% | +2,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 2 | 50,00% | +0,51% | -0,51% | -3,25% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 2 | 50,00% | +0,51% | -0,51% | -3,25% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 2 | 50,00% | +0,51% | -0,51% | -3,25% | +2,87% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 4 | 75,00% | +0,50% | -0,50% | -0,88% | +0,27% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 6 | 33,33% | -0,57% | -0,03% | -0,52% | +0,79% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 4 | 75,00% | +0,58% | -0,58% | -2,02% | +1,53% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 5 | 0,00% | -1,46% | -0,83% | -2,17% | +1,26% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 3 | 66,67% | +0,76% | -0,76% | -2,81% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 4 | 25,00% | -1,49% | -1,49% | -3,27% | +1,54% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 2 | 100,00% | +2,07% | -2,07% | -4,75% | +1,64% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 2 | 0,00% | -2,07% | -2,07% | -4,75% | +1,64% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 6 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 6 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 6 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 15 | 40,00% | -0,08% |
| BTC | BREVE | Tecnico | 12 | 50,00% | -0,04% |
| BTC | SETTIMANALE | Famiglia statistica | 2 | 50,00% | -0,02% |
| BTC | SETTIMANALE | Tecnico | 1 | 100,00% | +1,09% |
| DOGE | BREVE | Classic technical | 15 | 66,67% | +0,29% |
| DOGE | BREVE | Famiglia statistica | 15 | 66,67% | +0,29% |
| DOGE | BREVE | Tecnico | 15 | 66,67% | +0,29% |
| DOGE | SETTIMANALE | Classic technical | 2 | 50,00% | +0,51% |
| DOGE | SETTIMANALE | Famiglia statistica | 2 | 50,00% | +0,51% |
| DOGE | SETTIMANALE | Tecnico | 2 | 50,00% | +0,51% |
| SOL | BREVE | Famiglia statistica | 11 | 72,73% | +0,60% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Tecnico | 15 | 20,00% | -1,11% |
| SOL | SETTIMANALE | Famiglia statistica | 2 | 100,00% | +2,07% |
| SOL | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% |
| SOL | SETTIMANALE | Tecnico | 2 | 0,00% | -2,07% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 9 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 13 | in attesa di controlli maturati |
| BTC | SWING | 10 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | BREVE | 6 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 12 | in attesa di controlli maturati |
| SOL | SWING | 10 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 6 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 12 | in attesa di controlli maturati |
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
