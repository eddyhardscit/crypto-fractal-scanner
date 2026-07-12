# Calibrazione pesi Global Confluence

Generato: 2026-07-12 07:40 UTC

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
| BTC | 4 | FEEDBACK RAPIDO | 3 | 0 | 0 | 0 | Famiglia statistica | 1g | 33,33% | -0,13% | feedback rapido: utile da osservare, non da pesare |
| SOL | 4 | FEEDBACK RAPIDO | 3 | 0 | 0 | 0 | Tecnico | 1g | 33,33% | -0,56% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 4 | FEEDBACK RAPIDO | 3 | 0 | 0 | 0 | Famiglia statistica | 1g | 66,67% | +0,51% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 3 | 33,33% | -0,13% | -0,13% | -0,25% | +0,18% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 2 | 100,00% | +0,33% | -0,33% | -0,49% | +0,06% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 2 | 50,00% | +0,60% | +0,60% | +0,43% | +1,16% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 1 | 0,00% | -1,27% | +1,27% | +1,22% | +1,41% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 1 | 100,00% | +0,92% | +0,92% | -0,53% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 1 | 0,00% | -0,92% | +0,92% | -0,53% | +2,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 3 | 66,67% | +0,51% | -0,51% | -0,73% | -0,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 3 | 66,67% | +0,51% | -0,51% | -0,73% | -0,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 3 | 66,67% | +0,51% | -0,51% | -0,73% | -0,16% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 2 | 50,00% | -0,09% | +0,09% | -0,24% | +1,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 2 | 50,00% | -0,09% | +0,09% | -0,24% | +1,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 2 | 50,00% | -0,09% | +0,09% | -0,24% | +1,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 1 | 100,00% | +0,03% | -0,03% | -0,58% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 1 | 100,00% | +0,03% | -0,03% | -0,58% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 1 | 100,00% | +0,03% | -0,03% | -0,58% | +3,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 2 | 50,00% | -0,01% | +0,01% | -0,05% | +0,24% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 3 | 33,33% | -0,56% | -0,56% | -0,86% | -0,19% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 2 | 100,00% | +0,93% | -0,93% | -1,33% | +0,68% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 2 | 0,00% | -0,93% | -0,93% | -1,33% | +0,68% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 1 | 100,00% | +1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 3 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 3 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 3 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 6 | 50,00% | +0,29% |
| BTC | BREVE | Tecnico | 4 | 50,00% | -0,38% |
| DOGE | BREVE | Classic technical | 6 | 66,67% | +0,23% |
| DOGE | BREVE | Famiglia statistica | 6 | 66,67% | +0,23% |
| DOGE | BREVE | Tecnico | 6 | 66,67% | +0,23% |
| SOL | BREVE | Famiglia statistica | 5 | 80,00% | +0,76% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Tecnico | 6 | 16,67% | -0,92% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 9 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 15 | in attesa di controlli maturati |
| BTC | SWING | 10 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | BREVE | 6 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 15 | in attesa di controlli maturati |
| SOL | SWING | 10 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 6 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 15 | in attesa di controlli maturati |
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
