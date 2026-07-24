# Calibrazione pesi Global Confluence

Generato: 2026-07-24 05:15 UTC

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
| BTC | 16 | FEEDBACK RAPIDO | 15 | 0 | 0 | 0 | Famiglia statistica | 1g | 40,00% | +0,14% | feedback rapido: utile da osservare, non da pesare |
| SOL | 16 | FEEDBACK RAPIDO | 15 | 0 | 0 | 0 | Tecnico | 1g | 60,00% | -0,08% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 16 | FEEDBACK RAPIDO | 15 | 0 | 0 | 0 | Famiglia statistica | 1g | 60,00% | +0,45% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 15 | 40,00% | +0,14% | +0,14% | -0,09% | +0,81% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 12 | 33,33% | -0,76% | +0,15% | -0,10% | +0,83% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 14 | 50,00% | +0,41% | +0,41% | -0,13% | +1,45% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 11 | 36,36% | -0,57% | +0,67% | +0,09% | +1,71% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 13 | 69,23% | +0,70% | +0,70% | -0,95% | +2,37% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 11 | 36,36% | -0,21% | +1,01% | -0,84% | +2,54% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 11 | 63,64% | +1,27% | +1,27% | -1,87% | +3,13% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 10 | 40,00% | -0,93% | +1,30% | -1,73% | +3,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 9 | 77,78% | +1,83% | +1,83% | -2,09% | +3,71% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 8 | 50,00% | -0,51% | +2,10% | -1,94% | +3,85% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 6 | 100,00% | +2,93% | +2,93% | -2,22% | +4,46% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 5 | 40,00% | -0,21% | +3,41% | -2,01% | +4,83% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 2 | 100,00% | +2,84% | +2,84% | -2,80% | +5,29% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 1 | 0,00% | -3,42% | +3,42% | -2,32% | +5,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 14 | 57,14% | +0,39% | -0,39% | -0,66% | +0,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 15 | 60,00% | +0,45% | -0,45% | -0,73% | +0,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 15 | 60,00% | +0,45% | -0,45% | -0,73% | +0,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 13 | 53,85% | +0,37% | -0,37% | -1,00% | +1,08% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 14 | 57,14% | +0,52% | -0,52% | -1,09% | +0,85% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 14 | 57,14% | +0,52% | -0,52% | -1,09% | +0,85% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 12 | 50,00% | +0,52% | -0,52% | -1,78% | +2,06% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 13 | 53,85% | +0,65% | -0,65% | -1,83% | +1,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 13 | 53,85% | +0,65% | -0,65% | -1,83% | +1,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 10 | 60,00% | +0,62% | -0,62% | -2,60% | +2,50% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 11 | 63,64% | +0,83% | -0,83% | -2,72% | +2,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 11 | 63,64% | +0,83% | -0,83% | -2,72% | +2,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 8 | 75,00% | +1,22% | -1,22% | -2,92% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 9 | 77,78% | +1,20% | -1,20% | -3,03% | +2,55% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 9 | 77,78% | +1,20% | -1,20% | -3,03% | +2,55% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 6 | 66,67% | +1,44% | -1,44% | -3,19% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 6 | 66,67% | +1,44% | -1,44% | -3,19% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 6 | 66,67% | +1,44% | -1,44% | -3,19% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 2 | 100,00% | +3,67% | -3,67% | -4,69% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 2 | 100,00% | +3,67% | -3,67% | -4,69% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 2 | 100,00% | +3,67% | -3,67% | -4,69% | +2,87% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 7 | 71,43% | -0,03% | +0,03% | -0,23% | +0,72% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 11 | 63,64% | -0,00% | -0,79% | -0,98% | +0,11% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 15 | 60,00% | -0,08% | -0,17% | -0,50% | +0,66% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 6 | 33,33% | -0,64% | +0,64% | +0,32% | +1,26% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 10 | 50,00% | -0,22% | -0,69% | -1,46% | +0,53% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 14 | 28,57% | -0,57% | -0,25% | -0,88% | +1,20% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 5 | 0,00% | -1,89% | +1,89% | -0,57% | +2,88% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 9 | 33,33% | -0,82% | -0,64% | -2,52% | +1,76% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 13 | 30,77% | -0,66% | -0,26% | -1,92% | +2,27% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 4 | 25,00% | -2,26% | +2,26% | -1,12% | +4,04% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 8 | 62,50% | -0,04% | -0,46% | -3,18% | +2,58% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 11 | 27,27% | -1,35% | -0,14% | -2,86% | +2,94% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 2 | 0,00% | -1,16% | +1,16% | -2,09% | +4,20% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 7 | 71,43% | +0,71% | -0,62% | -3,85% | +2,78% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 9 | 11,11% | -1,86% | -0,40% | -3,74% | +2,90% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 4 | 50,00% | +0,49% | -0,49% | -4,84% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 6 | 33,33% | -0,75% | -0,06% | -4,51% | +2,76% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 2 | 100,00% | +1,84% | -1,84% | -5,73% | +1,74% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 2 | 0,00% | -1,84% | -1,84% | -5,73% | +1,74% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 15 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 14 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 15 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 42 | 52,38% | +0,40% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 34 | 35,29% | -0,52% |
| BTC | SETTIMANALE | Famiglia statistica | 26 | 76,92% | +1,85% |
| BTC | SETTIMANALE | Tecnico | 23 | 43,48% | -0,63% |
| BTC | SWING | Famiglia statistica | 2 | 100,00% | +2,84% |
| BTC | SWING | Tecnico | 1 | 0,00% | -3,42% |
| DOGE | BREVE | Classic technical | 39 | 53,85% | +0,43% |
| DOGE | BREVE | Famiglia statistica | 42 | 57,14% | +0,53% |
| DOGE | BREVE | Tecnico | 42 | 57,14% | +0,53% |
| DOGE | SETTIMANALE | Classic technical | 24 | 66,67% | +1,02% |
| DOGE | SETTIMANALE | Famiglia statistica | 26 | 69,23% | +1,10% |
| DOGE | SETTIMANALE | Tecnico | 26 | 69,23% | +1,10% |
| DOGE | SWING | Classic technical | 2 | 100,00% | +3,67% |
| DOGE | SWING | Famiglia statistica | 2 | 100,00% | +3,67% |
| DOGE | SWING | Tecnico | 2 | 100,00% | +3,67% |
| SOL | BREVE | Classic technical | 18 | 38,89% | -0,75% |
| SOL | BREVE | Famiglia statistica | 30 | 50,00% | -0,32% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 42 | 40,48% | -0,42% |
| SOL | SETTIMANALE | Classic technical | 6 | 16,67% | -1,89% |
| SOL | SETTIMANALE | Famiglia statistica | 19 | 63,16% | +0,35% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Tecnico | 26 | 23,08% | -1,39% |
| SOL | SWING | Famiglia statistica | 2 | 100,00% | +1,84% |
| SOL | SWING | Frattale SOL | 1 | 0,00% | -1,13% |
| SOL | SWING | Tecnico | 2 | 0,00% | -1,84% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 6 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 9 | in attesa di controlli maturati |
| BTC | SWING | 8 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 4 | in attesa di controlli maturati |
| SOL | SWING | 7 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 6 | in attesa di controlli maturati |
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
