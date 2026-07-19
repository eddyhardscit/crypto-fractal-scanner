# Calibrazione pesi Global Confluence

Generato: 2026-07-19 05:14 UTC

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
| BTC | 11 | FEEDBACK RAPIDO | 10 | 0 | 0 | 0 | Famiglia statistica | 1g | 40,00% | +0,11% | feedback rapido: utile da osservare, non da pesare |
| SOL | 11 | FEEDBACK RAPIDO | 10 | 0 | 0 | 0 | Tecnico | 1g | 50,00% | -0,15% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 11 | FEEDBACK RAPIDO | 10 | 0 | 0 | 0 | Famiglia statistica | 1g | 60,00% | +0,20% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 10 | 40,00% | +0,11% | +0,11% | -0,05% | +0,77% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 9 | 33,33% | -0,71% | +0,10% | -0,08% | +0,81% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 9 | 44,44% | +0,28% | +0,28% | -0,37% | +1,42% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 8 | 37,50% | -0,47% | +0,33% | -0,38% | +1,48% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 8 | 62,50% | +0,23% | +0,23% | -1,50% | +2,10% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 7 | 42,86% | +0,10% | +0,51% | -1,43% | +2,27% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 6 | 50,00% | +0,83% | +0,83% | -2,22% | +3,06% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 5 | 60,00% | -0,18% | +0,79% | -2,01% | +3,26% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 4 | 50,00% | +0,53% | +0,53% | -3,09% | +2,78% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 3 | 66,67% | +0,15% | +0,83% | -3,03% | +2,84% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 1 | 100,00% | +2,40% | +2,40% | -2,32% | +3,59% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 1 | 0,00% | -2,40% | +2,40% | -2,32% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 9 | 55,56% | +0,09% | -0,09% | -0,35% | +0,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 10 | 60,00% | +0,20% | -0,20% | -0,49% | +0,55% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 10 | 60,00% | +0,20% | -0,20% | -0,49% | +0,55% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 8 | 50,00% | +0,02% | -0,02% | -0,87% | +1,74% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 9 | 55,56% | +0,28% | -0,28% | -1,02% | +1,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 9 | 55,56% | +0,28% | -0,28% | -1,02% | +1,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 7 | 57,14% | +0,42% | -0,42% | -1,93% | +2,46% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 8 | 62,50% | +0,64% | -0,64% | -1,99% | +2,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 8 | 62,50% | +0,64% | -0,64% | -1,99% | +2,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 6 | 50,00% | +0,42% | -0,42% | -2,60% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 6 | 50,00% | +0,42% | -0,42% | -2,60% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 6 | 50,00% | +0,42% | -0,42% | -2,60% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 4 | 75,00% | +1,21% | -1,21% | -3,29% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 4 | 75,00% | +1,21% | -1,21% | -3,29% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 4 | 75,00% | +1,21% | -1,21% | -3,29% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 1 | 100,00% | +0,58% | -0,58% | -2,58% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 1 | 100,00% | +0,58% | -0,58% | -2,58% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 1 | 100,00% | +0,58% | -0,58% | -2,58% | +3,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 3 | 66,67% | -0,02% | +0,02% | -0,17% | +0,43% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 7 | 71,43% | +0,20% | -0,78% | -1,00% | +0,04% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 10 | 50,00% | -0,15% | -0,21% | -0,59% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 2 | 50,00% | +0,08% | -0,08% | -0,45% | +0,39% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 7 | 57,14% | -0,10% | -0,81% | -1,71% | +0,57% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 9 | 22,22% | -0,60% | -0,67% | -1,51% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 1 | 0,00% | -0,05% | +0,05% | -3,42% | +0,47% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 6 | 50,00% | -0,11% | -1,02% | -2,92% | +1,58% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 8 | 37,50% | -0,30% | -1,19% | -2,73% | +1,88% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 4 | 100,00% | +1,95% | -1,95% | -3,73% | +2,42% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 6 | 16,67% | -1,31% | -1,44% | -3,60% | +2,72% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 3 | 100,00% | +2,17% | -2,17% | -4,51% | +2,20% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 4 | 0,00% | -2,55% | -2,55% | -4,55% | +2,00% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 1 | 100,00% | +2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 10 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 10 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 10 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 27 | 48,15% | +0,21% |
| BTC | BREVE | Tecnico | 24 | 37,50% | -0,39% |
| BTC | SETTIMANALE | Famiglia statistica | 11 | 54,55% | +0,86% |
| BTC | SETTIMANALE | Tecnico | 9 | 55,56% | -0,32% |
| DOGE | BREVE | Classic technical | 24 | 54,17% | +0,16% |
| DOGE | BREVE | Famiglia statistica | 27 | 59,26% | +0,36% |
| DOGE | BREVE | Tecnico | 27 | 59,26% | +0,36% |
| DOGE | SETTIMANALE | Classic technical | 11 | 63,64% | +0,72% |
| DOGE | SETTIMANALE | Famiglia statistica | 11 | 63,64% | +0,72% |
| DOGE | SETTIMANALE | Tecnico | 11 | 63,64% | +0,72% |
| SOL | BREVE | Classic technical | 6 | 50,00% | +0,01% |
| SOL | BREVE | Famiglia statistica | 20 | 60,00% | +0,00% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Tecnico | 27 | 37,04% | -0,34% |
| SOL | SETTIMANALE | Famiglia statistica | 8 | 100,00% | +2,11% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Tecnico | 11 | 9,09% | -1,87% |

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
