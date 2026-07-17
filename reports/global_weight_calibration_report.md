# Calibrazione pesi Global Confluence

Generato: 2026-07-17 00:33 UTC

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
| BTC | 9 | FEEDBACK RAPIDO | 8 | 0 | 0 | 0 | Famiglia statistica | 1g | 25,00% | -0,07% | feedback rapido: utile da osservare, non da pesare |
| SOL | 9 | FEEDBACK RAPIDO | 8 | 0 | 0 | 0 | Tecnico | 1g | 50,00% | -0,03% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 9 | FEEDBACK RAPIDO | 8 | 0 | 0 | 0 | Famiglia statistica | 1g | 75,00% | +0,30% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 8 | 25,00% | -0,07% | -0,07% | -0,24% | +0,71% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 7 | 42,86% | -0,67% | -0,12% | -0,31% | +0,75% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 7 | 42,86% | +0,15% | +0,15% | -0,66% | +1,56% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 6 | 33,33% | -0,37% | +0,18% | -0,71% | +1,67% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 6 | 66,67% | +0,29% | +0,29% | -1,38% | +2,48% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 5 | 60,00% | +0,56% | +0,70% | -1,26% | +2,79% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 4 | 25,00% | -0,09% | -0,09% | -3,09% | +2,31% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 3 | 66,67% | +0,27% | -0,46% | -3,03% | +2,40% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 2 | 50,00% | +0,45% | +0,45% | -2,80% | +3,08% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 1 | 0,00% | -1,26% | +1,26% | -2,32% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 7 | 71,43% | +0,17% | -0,17% | -0,48% | +0,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 8 | 75,00% | +0,30% | -0,30% | -0,63% | +0,53% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 8 | 75,00% | +0,30% | -0,30% | -0,63% | +0,53% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 6 | 50,00% | -0,07% | +0,07% | -1,03% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 7 | 57,14% | +0,28% | -0,28% | -1,21% | +1,65% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 7 | 57,14% | +0,28% | -0,28% | -1,21% | +1,65% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 6 | 50,00% | +0,35% | -0,35% | -1,80% | +2,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 6 | 50,00% | +0,35% | -0,35% | -1,80% | +2,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 6 | 50,00% | +0,35% | -0,35% | -1,80% | +2,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 4 | 75,00% | +0,81% | -0,81% | -3,29% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 4 | 75,00% | +0,81% | -0,81% | -3,29% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 4 | 75,00% | +0,81% | -0,81% | -3,29% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 2 | 50,00% | +1,02% | -1,02% | -3,25% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 2 | 50,00% | +1,02% | -1,02% | -3,25% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 2 | 50,00% | +1,02% | -1,02% | -3,25% | +2,87% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 1 | 100,00% | +1,17% | -1,17% | -1,02% | -0,90% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 6 | 66,67% | +0,19% | -0,86% | -1,14% | -0,00% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 8 | 50,00% | -0,03% | -0,42% | -0,80% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 5 | 60,00% | -0,17% | -1,10% | -2,21% | +0,65% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 7 | 14,29% | -0,79% | -0,84% | -1,82% | +1,24% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 4 | 75,00% | +0,69% | -0,69% | -2,70% | +2,29% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 6 | 33,33% | -0,95% | -1,03% | -2,51% | +2,45% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 3 | 100,00% | +1,98% | -1,98% | -4,18% | +2,14% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 4 | 0,00% | -2,06% | -2,06% | -4,30% | +1,95% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 2 | 100,00% | +2,96% | -2,96% | -4,75% | +1,74% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 2 | 0,00% | -2,96% | -2,96% | -4,75% | +1,74% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 8 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 8 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 8 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 21 | 42,86% | +0,10% |
| BTC | BREVE | Tecnico | 18 | 44,44% | -0,23% |
| BTC | SETTIMANALE | Famiglia statistica | 6 | 33,33% | +0,09% |
| BTC | SETTIMANALE | Tecnico | 4 | 50,00% | -0,11% |
| DOGE | BREVE | Classic technical | 19 | 57,89% | +0,15% |
| DOGE | BREVE | Famiglia statistica | 21 | 61,90% | +0,30% |
| DOGE | BREVE | Tecnico | 21 | 61,90% | +0,30% |
| DOGE | SETTIMANALE | Classic technical | 6 | 66,67% | +0,88% |
| DOGE | SETTIMANALE | Famiglia statistica | 6 | 66,67% | +0,88% |
| DOGE | SETTIMANALE | Tecnico | 6 | 66,67% | +0,88% |
| SOL | BREVE | Classic technical | 1 | 100,00% | +1,17% |
| SOL | BREVE | Famiglia statistica | 15 | 66,67% | +0,21% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Tecnico | 21 | 33,33% | -0,55% |
| SOL | SETTIMANALE | Famiglia statistica | 5 | 100,00% | +2,37% |
| SOL | SETTIMANALE | Frattale SOL | 2 | 0,00% | -3,27% |
| SOL | SETTIMANALE | Tecnico | 6 | 0,00% | -2,36% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 9 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 11 | in attesa di controlli maturati |
| BTC | SWING | 10 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | BREVE | 5 | in attesa di controlli maturati |
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
