# Calibrazione pesi Global Confluence

Generato: 2026-07-26 05:14 UTC

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
| BTC | 18 | FEEDBACK RAPIDO | 17 | 0 | 0 | 0 | Famiglia statistica | 1g | 41,18% | +0,04% | feedback rapido: utile da osservare, non da pesare |
| SOL | 18 | FEEDBACK RAPIDO | 17 | 0 | 0 | 0 | Tecnico | 1g | 58,82% | -0,02% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 18 | FEEDBACK RAPIDO | 17 | 0 | 0 | 0 | Famiglia statistica | 1g | 58,82% | +0,69% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 17 | 41,18% | +0,04% | +0,04% | -0,18% | +0,65% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 14 | 35,71% | -0,56% | +0,04% | -0,21% | +0,63% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 16 | 43,75% | +0,16% | +0,16% | -0,34% | +1,07% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 13 | 46,15% | -0,23% | +0,31% | -0,21% | +1,21% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 15 | 60,00% | +0,30% | +0,30% | -1,23% | +2,09% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 12 | 41,67% | -0,07% | +0,81% | -0,99% | +2,38% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 13 | 53,85% | +0,95% | +0,95% | -1,83% | +3,12% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 11 | 45,45% | -0,83% | +1,16% | -1,61% | +3,33% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 11 | 72,73% | +1,49% | +1,49% | -1,88% | +3,77% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 10 | 40,00% | -0,49% | +1,67% | -1,74% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 8 | 87,50% | +2,19% | +2,19% | -2,36% | +4,37% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 7 | 28,57% | -0,34% | +2,43% | -2,23% | +4,62% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 4 | 100,00% | +1,69% | +1,69% | -3,09% | +4,98% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 3 | 33,33% | -0,83% | +1,50% | -3,03% | +5,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 16 | 50,00% | -0,05% | +0,05% | -0,35% | +0,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 17 | 58,82% | +0,69% | -0,02% | -0,43% | +0,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 17 | 52,94% | +0,02% | -0,02% | -0,43% | +0,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 15 | 53,33% | +0,16% | -0,16% | -0,88% | +1,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 16 | 56,25% | +0,30% | -0,30% | -0,97% | +0,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +6,40% | +6,40% | +3,75% | +6,18% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 16 | 56,25% | +0,30% | -0,30% | -0,97% | +0,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 14 | 50,00% | +0,70% | -0,70% | -2,36% | +1,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 15 | 53,33% | +0,79% | -0,79% | -2,36% | +1,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 15 | 53,33% | +0,79% | -0,79% | -2,36% | +1,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 12 | 58,33% | +0,71% | -0,71% | -3,04% | +2,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 13 | 61,54% | +0,88% | -0,88% | -3,10% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 13 | 61,54% | +0,88% | -0,88% | -3,10% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 10 | 70,00% | +1,23% | -1,23% | -3,40% | +2,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 11 | 72,73% | +1,21% | -1,21% | -3,45% | +2,43% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 11 | 72,73% | +1,21% | -1,21% | -3,45% | +2,43% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 7 | 57,14% | +1,15% | -1,15% | -3,67% | +2,89% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 8 | 62,50% | +1,76% | -1,76% | -4,08% | +2,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 8 | 62,50% | +1,76% | -1,76% | -4,08% | +2,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 4 | 75,00% | +3,15% | -3,15% | -5,68% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 4 | 75,00% | +3,15% | -3,15% | -5,68% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 4 | 75,00% | +3,15% | -3,15% | -5,68% | +2,68% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 9 | 66,67% | +0,06% | -0,06% | -0,41% | +0,48% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 13 | 61,54% | -0,06% | -0,73% | -0,99% | +0,04% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 17 | 58,82% | -0,02% | -0,19% | -0,56% | +0,54% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 8 | 50,00% | +0,11% | -0,11% | -0,50% | +0,37% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 12 | 41,67% | -0,57% | -0,96% | -1,71% | +0,06% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 16 | 37,50% | -0,21% | -0,51% | -1,14% | +0,77% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 7 | 28,57% | -0,30% | +0,30% | -1,81% | +2,01% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 11 | 36,36% | -0,49% | -1,19% | -2,95% | +1,42% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 15 | 40,00% | -0,08% | -0,71% | -2,32% | +1,95% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 5 | 40,00% | -1,33% | +1,33% | -1,45% | +3,95% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 9 | 55,56% | -0,48% | -0,86% | -3,50% | +2,36% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 13 | 38,46% | -0,65% | -0,62% | -3,10% | +2,81% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 4 | 50,00% | -0,02% | +0,02% | -2,24% | +4,25% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 8 | 75,00% | +0,78% | -0,69% | -3,79% | +2,87% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 11 | 27,27% | -1,32% | -0,53% | -3,50% | +3,16% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 1 | 100,00% | +1,18% | -1,18% | -3,42% | +3,59% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 6 | 50,00% | -0,21% | -1,25% | -4,69% | +2,50% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 8 | 50,00% | +0,13% | -0,74% | -4,48% | +2,71% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 3 | 100,00% | +1,83% | -1,83% | -5,16% | +2,20% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 4 | 0,00% | -2,54% | -2,54% | -5,28% | +2,00% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 17 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 15 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 17 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 48 | 47,92% | +0,16% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 39 | 41,03% | -0,30% |
| BTC | SETTIMANALE | Famiglia statistica | 32 | 68,75% | +1,44% |
| BTC | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% |
| BTC | SETTIMANALE | Tecnico | 28 | 39,29% | -0,59% |
| BTC | SWING | Famiglia statistica | 4 | 100,00% | +1,69% |
| BTC | SWING | Tecnico | 3 | 33,33% | -0,83% |
| DOGE | BREVE | Classic technical | 45 | 51,11% | +0,25% |
| DOGE | BREVE | Famiglia statistica | 48 | 56,25% | +0,59% |
| DOGE | BREVE | Microstruttura exchange | 3 | 100,00% | +4,26% |
| DOGE | BREVE | Tecnico | 48 | 54,17% | +0,35% |
| DOGE | SETTIMANALE | Classic technical | 29 | 62,07% | +1,00% |
| DOGE | SETTIMANALE | Famiglia statistica | 32 | 65,62% | +1,21% |
| DOGE | SETTIMANALE | Tecnico | 32 | 65,62% | +1,21% |
| DOGE | SWING | Classic technical | 4 | 75,00% | +3,15% |
| DOGE | SWING | Famiglia statistica | 4 | 75,00% | +3,15% |
| DOGE | SWING | Tecnico | 4 | 75,00% | +3,15% |
| SOL | BREVE | Classic technical | 24 | 50,00% | -0,03% |
| SOL | BREVE | Famiglia statistica | 36 | 47,22% | -0,36% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 48 | 45,83% | -0,10% |
| SOL | SETTIMANALE | Classic technical | 10 | 50,00% | -0,55% |
| SOL | SETTIMANALE | Famiglia statistica | 23 | 60,87% | +0,03% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% |
| SOL | SETTIMANALE | Tecnico | 32 | 37,50% | -0,69% |
| SOL | SWING | Famiglia statistica | 3 | 100,00% | +1,83% |
| SOL | SWING | Frattale SOL | 1 | 0,00% | -1,13% |
| SOL | SWING | Tecnico | 4 | 0,00% | -2,54% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 6 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 8 | in attesa di controlli maturati |
| BTC | SWING | 8 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 2 | in attesa di controlli maturati |
| SOL | SWING | 7 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 4 | in attesa di controlli maturati |
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
