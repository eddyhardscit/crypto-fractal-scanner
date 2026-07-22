# Calibrazione pesi Global Confluence

Generato: 2026-07-22 05:14 UTC

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
| BTC | 14 | FEEDBACK RAPIDO | 13 | 0 | 0 | 0 | Famiglia statistica | 1g | 46,15% | +0,26% | feedback rapido: utile da osservare, non da pesare |
| SOL | 14 | FEEDBACK RAPIDO | 13 | 0 | 0 | 0 | Tecnico | 1g | 53,85% | -0,30% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 14 | FEEDBACK RAPIDO | 13 | 0 | 0 | 0 | Famiglia statistica | 1g | 53,85% | +0,08% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 13 | 46,15% | +0,26% | +0,26% | +0,08% | +0,94% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 11 | 27,27% | -0,84% | +0,18% | -0,02% | +0,90% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 12 | 58,33% | +0,61% | +0,61% | +0,05% | +1,64% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 11 | 36,36% | -0,57% | +0,67% | +0,09% | +1,71% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 11 | 72,73% | +0,68% | +0,68% | -1,15% | +2,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 10 | 40,00% | -0,04% | +0,92% | -1,07% | +2,38% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 9 | 55,56% | +1,20% | +1,20% | -2,09% | +2,93% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 8 | 37,50% | -0,97% | +1,22% | -1,94% | +3,04% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 7 | 71,43% | +1,68% | +1,68% | -2,36% | +3,39% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 6 | 66,67% | +0,11% | +2,01% | -2,20% | +3,53% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 4 | 100,00% | +2,23% | +2,23% | -3,09% | +3,29% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 3 | 33,33% | -0,28% | +2,81% | -3,03% | +3,53% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 12 | 50,00% | -0,02% | +0,02% | -0,26% | +0,70% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 13 | 53,85% | +0,08% | -0,08% | -0,37% | +0,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 13 | 53,85% | +0,08% | -0,08% | -0,37% | +0,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 11 | 45,45% | -0,14% | +0,14% | -0,56% | +1,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 12 | 50,00% | +0,07% | -0,07% | -0,70% | +1,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 12 | 50,00% | +0,07% | -0,07% | -0,70% | +1,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 10 | 50,00% | +0,18% | -0,18% | -1,61% | +2,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 11 | 54,55% | +0,36% | -0,36% | -1,69% | +1,93% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 11 | 54,55% | +0,36% | -0,36% | -1,69% | +1,93% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 8 | 50,00% | +0,18% | -0,18% | -2,45% | +2,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 9 | 55,56% | +0,48% | -0,48% | -2,61% | +2,41% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 9 | 55,56% | +0,48% | -0,48% | -2,61% | +2,41% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 6 | 66,67% | +0,72% | -0,72% | -2,68% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 7 | 71,43% | +0,77% | -0,77% | -2,85% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 7 | 71,43% | +0,77% | -0,77% | -2,85% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 4 | 75,00% | +1,13% | -1,13% | -3,29% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 4 | 75,00% | +1,13% | -1,13% | -3,29% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 4 | 75,00% | +1,13% | -1,13% | -3,29% | +2,68% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 5 | 60,00% | -0,59% | +0,59% | +0,34% | +1,15% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 9 | 66,67% | +0,10% | -0,66% | -0,83% | +0,22% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 13 | 53,85% | -0,30% | +0,02% | -0,32% | +0,82% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 5 | 20,00% | -1,30% | +1,30% | +1,03% | +1,98% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 8 | 50,00% | -0,44% | -0,35% | -1,23% | +0,88% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 12 | 16,67% | -1,01% | +0,05% | -0,63% | +1,55% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 4 | 0,00% | -2,00% | +2,00% | -1,04% | +2,71% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 8 | 37,50% | -0,53% | -0,32% | -2,37% | +1,91% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 11 | 27,27% | -0,94% | -0,15% | -2,05% | +2,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 2 | 0,00% | -3,26% | +3,26% | -2,09% | +3,78% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 7 | 57,14% | -0,10% | -0,47% | -3,49% | +2,44% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 9 | 22,22% | -1,37% | -0,46% | -3,46% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 5 | 100,00% | +1,46% | -1,33% | -4,55% | +2,21% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 7 | 14,29% | -2,06% | -0,85% | -4,21% | +2,53% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 3 | 66,67% | +0,99% | -0,99% | -5,16% | +2,20% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 4 | 50,00% | -0,61% | -0,61% | -5,28% | +2,00% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 13 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 13 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 13 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 36 | 58,33% | +0,51% |
| BTC | BREVE | Microstruttura exchange | 2 | 100,00% | +2,59% |
| BTC | BREVE | Tecnico | 32 | 34,38% | -0,50% |
| BTC | SETTIMANALE | Famiglia statistica | 20 | 70,00% | +1,57% |
| BTC | SETTIMANALE | Tecnico | 17 | 47,06% | -0,47% |
| DOGE | BREVE | Classic technical | 33 | 48,48% | -0,00% |
| DOGE | BREVE | Famiglia statistica | 36 | 52,78% | +0,16% |
| DOGE | BREVE | Tecnico | 36 | 52,78% | +0,16% |
| DOGE | SETTIMANALE | Classic technical | 18 | 61,11% | +0,57% |
| DOGE | SETTIMANALE | Famiglia statistica | 20 | 65,00% | +0,71% |
| DOGE | SETTIMANALE | Tecnico | 20 | 65,00% | +0,71% |
| SOL | BREVE | Classic technical | 14 | 28,57% | -1,25% |
| SOL | BREVE | Famiglia statistica | 25 | 52,00% | -0,27% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% |
| SOL | BREVE | Tecnico | 36 | 33,33% | -0,73% |
| SOL | SETTIMANALE | Classic technical | 2 | 0,00% | -3,26% |
| SOL | SETTIMANALE | Famiglia statistica | 15 | 73,33% | +0,64% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Tecnico | 20 | 25,00% | -1,46% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 7 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 9 | in attesa di controlli maturati |
| BTC | SWING | 10 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | BREVE | 2 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 5 | in attesa di controlli maturati |
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
