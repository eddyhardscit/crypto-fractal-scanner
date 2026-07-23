# Calibrazione pesi Global Confluence

Generato: 2026-07-23 07:38 UTC

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
| BTC | 15 | FEEDBACK RAPIDO | 14 | 0 | 0 | 0 | Famiglia statistica | 1g | 42,86% | +0,16% | feedback rapido: utile da osservare, non da pesare |
| SOL | 15 | FEEDBACK RAPIDO | 14 | 0 | 0 | 0 | Tecnico | 1g | 57,14% | -0,21% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 15 | FEEDBACK RAPIDO | 14 | 0 | 0 | 0 | Famiglia statistica | 1g | 57,14% | +0,16% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 14 | 42,86% | +0,16% | +0,16% | -0,02% | +0,87% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 11 | 27,27% | -0,84% | +0,18% | -0,02% | +0,90% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 13 | 53,85% | +0,55% | +0,55% | +0,04% | +1,66% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 11 | 36,36% | -0,57% | +0,67% | +0,09% | +1,71% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 12 | 75,00% | +0,78% | +0,78% | -0,94% | +2,41% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 11 | 36,36% | -0,21% | +1,01% | -0,84% | +2,54% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 10 | 60,00% | +1,32% | +1,32% | -1,90% | +3,11% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 9 | 33,33% | -1,13% | +1,35% | -1,75% | +3,23% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 8 | 75,00% | +1,73% | +1,73% | -2,36% | +3,53% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 7 | 57,14% | -0,21% | +2,03% | -2,23% | +3,67% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 5 | 100,00% | +2,63% | +2,63% | -2,65% | +3,95% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 4 | 50,00% | +0,84% | +3,16% | -2,49% | +4,30% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 1 | 100,00% | +3,42% | +3,42% | -2,32% | +5,81% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 1 | 0,00% | -3,42% | +3,42% | -2,32% | +5,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 13 | 53,85% | +0,08% | -0,08% | -0,35% | +0,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 14 | 57,14% | +0,16% | -0,16% | -0,44% | +0,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 14 | 57,14% | +0,16% | -0,16% | -0,44% | +0,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 12 | 50,00% | -0,07% | +0,07% | -0,59% | +1,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 13 | 53,85% | +0,12% | -0,12% | -0,72% | +1,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 13 | 53,85% | +0,12% | -0,12% | -0,72% | +1,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 11 | 45,45% | +0,10% | -0,10% | -1,45% | +2,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 12 | 50,00% | +0,27% | -0,27% | -1,53% | +2,00% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 12 | 50,00% | +0,27% | -0,27% | -1,53% | +2,00% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 9 | 55,56% | +0,17% | -0,17% | -2,34% | +2,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 10 | 60,00% | +0,44% | -0,44% | -2,49% | +2,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 10 | 60,00% | +0,44% | -0,44% | -2,49% | +2,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 7 | 71,43% | +0,77% | -0,77% | -2,68% | +2,89% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 8 | 75,00% | +0,80% | -0,80% | -2,83% | +2,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 8 | 75,00% | +0,80% | -0,80% | -2,83% | +2,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 5 | 60,00% | +0,88% | -0,88% | -2,94% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 5 | 60,00% | +0,88% | -0,88% | -2,94% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 5 | 60,00% | +0,88% | -0,88% | -2,94% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 1 | 100,00% | +0,77% | -0,77% | -2,58% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 1 | 100,00% | +0,77% | -0,77% | -2,58% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 1 | 100,00% | +0,77% | -0,77% | -2,58% | +3,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 6 | 66,67% | -0,34% | +0,34% | +0,13% | +1,09% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 10 | 70,00% | +0,18% | -0,68% | -0,84% | +0,27% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 14 | 57,14% | -0,21% | -0,05% | -0,37% | +0,81% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 5 | 20,00% | -1,30% | +1,30% | +1,03% | +1,98% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 9 | 44,44% | -0,55% | -0,46% | -1,26% | +0,85% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 13 | 23,08% | -0,82% | -0,06% | -0,70% | +1,48% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 5 | 0,00% | -1,89% | +1,89% | -0,57% | +2,88% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 8 | 37,50% | -0,53% | -0,32% | -2,37% | +1,91% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 12 | 25,00% | -0,98% | -0,01% | -1,77% | +2,41% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 3 | 0,00% | -3,16% | +3,16% | -1,17% | +4,21% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 7 | 57,14% | -0,10% | -0,47% | -3,49% | +2,44% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 10 | 20,00% | -1,53% | -0,12% | -3,05% | +2,88% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 1 | 0,00% | -1,50% | +1,50% | -3,42% | +3,59% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 6 | 83,33% | +0,97% | -0,86% | -4,37% | +2,44% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 8 | 12,50% | -1,99% | -0,55% | -4,11% | +2,66% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 4 | 50,00% | +0,49% | -0,49% | -4,84% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 5 | 40,00% | -0,69% | -0,28% | -5,00% | +2,26% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 1 | 100,00% | +1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 14 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 14 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 14 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 39 | 56,41% | +0,48% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 33 | 33,33% | -0,54% |
| BTC | SETTIMANALE | Famiglia statistica | 23 | 73,91% | +1,75% |
| BTC | SETTIMANALE | Tecnico | 20 | 45,00% | -0,41% |
| BTC | SWING | Famiglia statistica | 1 | 100,00% | +3,42% |
| BTC | SWING | Tecnico | 1 | 0,00% | -3,42% |
| DOGE | BREVE | Classic technical | 36 | 50,00% | +0,03% |
| DOGE | BREVE | Famiglia statistica | 39 | 53,85% | +0,18% |
| DOGE | BREVE | Tecnico | 39 | 53,85% | +0,18% |
| DOGE | SETTIMANALE | Classic technical | 21 | 61,90% | +0,54% |
| DOGE | SETTIMANALE | Famiglia statistica | 23 | 65,22% | +0,66% |
| DOGE | SETTIMANALE | Tecnico | 23 | 65,22% | +0,66% |
| DOGE | SWING | Classic technical | 1 | 100,00% | +0,77% |
| DOGE | SWING | Famiglia statistica | 1 | 100,00% | +0,77% |
| DOGE | SWING | Tecnico | 1 | 100,00% | +0,77% |
| SOL | BREVE | Classic technical | 16 | 31,25% | -1,13% |
| SOL | BREVE | Famiglia statistica | 27 | 51,85% | -0,27% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 2 | 0,00% | -0,95% |
| SOL | BREVE | Tecnico | 39 | 35,90% | -0,65% |
| SOL | SETTIMANALE | Classic technical | 4 | 0,00% | -2,74% |
| SOL | SETTIMANALE | Famiglia statistica | 17 | 64,71% | +0,41% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Tecnico | 23 | 21,74% | -1,51% |
| SOL | SWING | Famiglia statistica | 1 | 100,00% | +1,13% |
| SOL | SWING | Frattale SOL | 1 | 0,00% | -1,13% |
| SOL | SWING | Tecnico | 1 | 0,00% | -1,13% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 6 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 9 | in attesa di controlli maturati |
| BTC | SWING | 8 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | BREVE | 1 | in attesa di controlli maturati |
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
