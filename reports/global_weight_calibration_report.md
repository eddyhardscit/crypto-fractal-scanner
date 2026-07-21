# Calibrazione pesi Global Confluence

Generato: 2026-07-21 05:14 UTC

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
| BTC | 13 | FEEDBACK RAPIDO | 12 | 0 | 0 | 0 | Famiglia statistica | 1g | 41,67% | +0,19% | feedback rapido: utile da osservare, non da pesare |
| SOL | 13 | FEEDBACK RAPIDO | 12 | 0 | 0 | 0 | Tecnico | 1g | 50,00% | -0,36% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 13 | FEEDBACK RAPIDO | 12 | 0 | 0 | 0 | Famiglia statistica | 1g | 58,33% | +0,12% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 12 | 41,67% | +0,19% | +0,19% | -0,00% | +0,86% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 11 | 27,27% | -0,84% | +0,18% | -0,02% | +0,90% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 11 | 54,55% | +0,38% | +0,38% | -0,22% | +1,44% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 10 | 40,00% | -0,31% | +0,42% | -0,21% | +1,49% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 10 | 70,00% | +0,52% | +0,52% | -1,11% | +2,17% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 9 | 33,33% | -0,30% | +0,77% | -1,01% | +2,31% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 8 | 50,00% | +0,84% | +0,84% | -2,36% | +2,70% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 7 | 42,86% | -0,53% | +0,81% | -2,23% | +2,79% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 6 | 66,67% | +1,52% | +1,52% | -2,22% | +3,40% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 5 | 60,00% | -0,39% | +1,89% | -2,01% | +3,57% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 3 | 100,00% | +1,72% | +1,72% | -3,05% | +2,89% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 2 | 0,00% | -2,32% | +2,32% | -2,93% | +3,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 11 | 54,55% | +0,02% | -0,02% | -0,33% | +0,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 12 | 58,33% | +0,12% | -0,12% | -0,45% | +0,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 12 | 58,33% | +0,12% | -0,12% | -0,45% | +0,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 10 | 50,00% | +0,04% | -0,04% | -0,82% | +1,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 11 | 54,55% | +0,25% | -0,25% | -0,95% | +1,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 11 | 54,55% | +0,25% | -0,25% | -0,95% | +1,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 9 | 55,56% | +0,31% | -0,31% | -1,62% | +2,10% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 10 | 60,00% | +0,50% | -0,50% | -1,70% | +1,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 10 | 60,00% | +0,50% | -0,50% | -1,70% | +1,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 7 | 57,14% | +0,40% | -0,40% | -2,62% | +2,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 8 | 62,50% | +0,71% | -0,71% | -2,77% | +2,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 8 | 62,50% | +0,71% | -0,71% | -2,77% | +2,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 6 | 66,67% | +0,72% | -0,72% | -2,68% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 6 | 66,67% | +0,72% | -0,72% | -2,68% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 6 | 66,67% | +0,72% | -0,72% | -2,68% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 3 | 100,00% | +1,67% | -1,67% | -3,54% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 3 | 100,00% | +1,67% | -1,67% | -3,54% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 3 | 100,00% | +1,67% | -1,67% | -3,54% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 5 | 60,00% | -0,59% | +0,59% | +0,34% | +1,15% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 8 | 75,00% | +0,18% | -0,68% | -0,88% | +0,20% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 12 | 50,00% | -0,36% | +0,06% | -0,31% | +0,86% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 4 | 25,00% | -1,03% | +1,03% | +0,68% | +1,67% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 8 | 50,00% | -0,44% | -0,35% | -1,23% | +0,88% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 11 | 18,18% | -0,88% | -0,16% | -0,91% | +1,40% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 3 | 0,00% | -1,88% | +1,88% | -1,17% | +2,55% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 7 | 42,86% | -0,27% | -0,70% | -2,61% | +1,72% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 10 | 30,00% | -0,80% | -0,40% | -2,19% | +2,22% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 1 | 0,00% | -2,92% | +2,92% | -3,42% | +3,10% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 6 | 66,67% | +0,48% | -1,15% | -3,95% | +2,11% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 8 | 25,00% | -1,10% | -0,97% | -3,80% | +2,41% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 4 | 100,00% | +1,74% | -1,74% | -4,35% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 6 | 16,67% | -2,35% | -1,04% | -4,02% | +2,76% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 2 | 100,00% | +2,36% | -2,36% | -5,73% | +1,74% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 3 | 33,33% | -1,39% | -1,39% | -5,70% | +1,62% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 12 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 12 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 12 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 33 | 54,55% | +0,35% |
| BTC | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% |
| BTC | BREVE | Tecnico | 30 | 33,33% | -0,50% |
| BTC | SETTIMANALE | Famiglia statistica | 17 | 64,71% | +1,23% |
| BTC | SETTIMANALE | Tecnico | 14 | 42,86% | -0,74% |
| DOGE | BREVE | Classic technical | 30 | 53,33% | +0,12% |
| DOGE | BREVE | Famiglia statistica | 33 | 57,58% | +0,28% |
| DOGE | BREVE | Tecnico | 33 | 57,58% | +0,28% |
| DOGE | SETTIMANALE | Classic technical | 16 | 68,75% | +0,76% |
| DOGE | SETTIMANALE | Famiglia statistica | 17 | 70,59% | +0,89% |
| DOGE | SETTIMANALE | Tecnico | 17 | 70,59% | +0,89% |
| SOL | BREVE | Classic technical | 12 | 33,33% | -1,06% |
| SOL | BREVE | Famiglia statistica | 23 | 56,52% | -0,17% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Tecnico | 33 | 33,33% | -0,67% |
| SOL | SETTIMANALE | Classic technical | 1 | 0,00% | -2,92% |
| SOL | SETTIMANALE | Famiglia statistica | 12 | 83,33% | +1,22% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Tecnico | 17 | 23,53% | -1,59% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 8 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 9 | in attesa di controlli maturati |
| BTC | SWING | 10 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | BREVE | 3 | in attesa di controlli maturati |
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
