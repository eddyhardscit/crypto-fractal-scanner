# Calibrazione pesi Global Confluence

Generato: 2026-07-16 10:02 UTC

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
| BTC | 8 | FEEDBACK RAPIDO | 7 | 0 | 0 | 0 | Famiglia statistica | 1g | 28,57% | +0,00% | feedback rapido: utile da osservare, non da pesare |
| SOL | 8 | FEEDBACK RAPIDO | 7 | 0 | 0 | 0 | Tecnico | 1g | 42,86% | -0,20% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 8 | FEEDBACK RAPIDO | 7 | 0 | 0 | 0 | Famiglia statistica | 1g | 71,43% | +0,17% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 7 | 28,57% | +0,00% | +0,00% | -0,21% | +0,86% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 6 | 33,33% | -0,88% | -0,04% | -0,28% | +0,94% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 6 | 50,00% | +0,40% | +0,40% | -0,56% | +2,01% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 5 | 40,00% | -0,17% | +0,50% | -0,59% | +2,23% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 5 | 60,00% | +0,00% | +0,00% | -2,03% | +2,03% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 4 | 75,00% | +1,14% | +0,43% | -2,04% | +2,31% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 3 | 33,33% | -0,02% | -0,02% | -3,05% | +2,20% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 2 | 100,00% | +0,55% | -0,55% | -2,93% | +2,27% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 1 | 100,00% | +1,26% | +1,26% | -2,32% | +3,59% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 1 | 0,00% | -1,26% | +1,26% | -2,32% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 6 | 66,67% | -0,00% | +0,00% | -0,38% | +0,78% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 7 | 71,43% | +0,17% | -0,17% | -0,57% | +0,74% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 7 | 71,43% | +0,17% | -0,17% | -0,57% | +0,74% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 6 | 50,00% | -0,07% | +0,07% | -1,03% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 6 | 50,00% | -0,07% | +0,07% | -1,03% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 6 | 50,00% | -0,07% | +0,07% | -1,03% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 5 | 60,00% | +0,45% | -0,45% | -2,22% | +2,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 5 | 60,00% | +0,45% | -0,45% | -2,22% | +2,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 5 | 60,00% | +0,45% | -0,45% | -2,22% | +2,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 3 | 66,67% | +0,78% | -0,78% | -3,54% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 3 | 66,67% | +0,78% | -0,78% | -3,54% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 3 | 66,67% | +0,78% | -0,78% | -3,54% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 1 | 0,00% | -0,26% | +0,26% | -2,58% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 1 | 0,00% | -0,26% | +0,26% | -2,58% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 1 | 0,00% | -0,26% | +0,26% | -2,58% | +3,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 5 | 60,00% | -0,00% | -0,80% | -1,16% | +0,18% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 7 | 42,86% | -0,20% | -0,31% | -0,77% | +0,65% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 4 | 75,00% | +0,58% | -0,58% | -2,02% | +1,53% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 6 | 0,00% | -1,45% | -0,46% | -1,62% | +1,93% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 4 | 75,00% | +0,69% | -0,69% | -2,70% | +2,29% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 5 | 40,00% | -1,10% | -1,29% | -3,09% | +1,89% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 2 | 100,00% | +2,07% | -2,07% | -4,75% | +1,64% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 3 | 0,00% | -2,15% | -2,15% | -4,73% | +1,55% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 1 | 100,00% | +2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 7 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 7 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 7 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 18 | 44,44% | +0,13% |
| BTC | BREVE | Tecnico | 15 | 46,67% | -0,10% |
| BTC | SETTIMANALE | Famiglia statistica | 4 | 50,00% | +0,30% |
| BTC | SETTIMANALE | Tecnico | 3 | 66,67% | -0,05% |
| DOGE | BREVE | Classic technical | 17 | 58,82% | +0,11% |
| DOGE | BREVE | Famiglia statistica | 18 | 61,11% | +0,17% |
| DOGE | BREVE | Tecnico | 18 | 61,11% | +0,17% |
| DOGE | SETTIMANALE | Classic technical | 4 | 50,00% | +0,52% |
| DOGE | SETTIMANALE | Famiglia statistica | 4 | 50,00% | +0,52% |
| DOGE | SETTIMANALE | Tecnico | 4 | 50,00% | +0,52% |
| SOL | BREVE | Famiglia statistica | 13 | 69,23% | +0,39% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Tecnico | 18 | 27,78% | -0,87% |
| SOL | SETTIMANALE | Famiglia statistica | 3 | 100,00% | +2,24% |
| SOL | SETTIMANALE | Frattale SOL | 2 | 0,00% | -3,27% |
| SOL | SETTIMANALE | Tecnico | 4 | 0,00% | -2,26% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 9 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 11 | in attesa di controlli maturati |
| BTC | SWING | 10 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | BREVE | 6 | in attesa di controlli maturati |
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
