# Calibrazione pesi Global Confluence

Generato: 2026-07-10 11:50 UTC

Report completo: [global_weight_calibration_report.md](global_weight_calibration_report.md)

Questo blocco controlla se, col tempo, i moduli del Global Confluence meritano più peso, meno peso o peso invariato.

Ora legge il nuovo `module_signal_tracker_metrics.csv`, quindi include anche i nuovi orizzonti **1g / 2g / 3g / 5g / 7g / 10g / 14g / 21g / 30g / 45g / 60g** e il modulo **Classic technical**.

Regola principale:

- sotto **30 controlli**: osservazione, nessuna modifica pesi
- da **30 controlli**: prima calibrazione leggera
- da **60 controlli**: lettura utile
- da **100+ controlli**: possibile proposta prudente di modifica pesi

## Sintesi per asset

| Asset | Segnali salvati | Stato | Controlli max | Righe 30+ | Righe 60+ | Righe 100+ | Miglior modulo attuale | Orizzonte | Accuratezza | Return corretto direzione | Lettura |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 2 | FEEDBACK RAPIDO | 1 | 0 | 0 | 0 | Tecnico | 1g | 100,00% | +0,31% | feedback rapido: utile da osservare, non da pesare |
| SOL | 2 | FEEDBACK RAPIDO | 1 | 0 | 0 | 0 | Scanner | 1g | 100,00% | +0,10% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 2 | FEEDBACK RAPIDO | 1 | 0 | 0 | 0 | Global confluence | 1g | 100,00% | +0,11% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni moduli con controlli maturati

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Global confluence | 1 | 0,00% | -0,31% | -0,31% | -0,34% | -0,08% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Scanner | 1 | 0,00% | -0,31% | -0,31% | -0,34% | -0,08% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Market regime | 1 | 0,00% | -0,31% | -0,31% | -0,34% | -0,08% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 1 | 100,00% | +0,31% | -0,31% | -0,34% | -0,08% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Global confluence | 1 | 100,00% | +0,11% | -0,11% | -0,13% | +0,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Scanner | 1 | 100,00% | +0,11% | -0,11% | -0,13% | +0,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Market regime | 1 | 100,00% | +0,11% | -0,11% | -0,13% | +0,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 1 | 100,00% | +0,11% | -0,11% | -0,13% | +0,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 1 | 100,00% | +0,11% | -0,11% | -0,13% | +0,04% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Global confluence | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Scanner | 1 | 100,00% | +0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Market regime | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo | Controlli totali | Accuratezza media | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Global confluence | 1 | 0,00% | -0,31% |
| BTC | BREVE | Scanner | 1 | 0,00% | -0,31% |
| BTC | BREVE | Market regime | 1 | 0,00% | -0,31% |
| BTC | BREVE | Tecnico | 1 | 100,00% | +0,31% |
| DOGE | BREVE | Global confluence | 1 | 100,00% | +0,11% |
| DOGE | BREVE | Scanner | 1 | 100,00% | +0,11% |
| DOGE | BREVE | Market regime | 1 | 100,00% | +0,11% |
| DOGE | BREVE | Tecnico | 1 | 100,00% | +0,11% |
| DOGE | BREVE | Classic technical | 1 | 100,00% | +0,11% |
| SOL | BREVE | Global confluence | 1 | 0,00% | -0,10% |
| SOL | BREVE | Scanner | 1 | 100,00% | +0,10% |
| SOL | BREVE | Market regime | 1 | 0,00% | -0,10% |
| SOL | BREVE | Tecnico | 1 | 0,00% | -0,10% |
| SOL | BREVE | Frattale SOL | 1 | 0,00% | -0,10% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 14 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 18 | in attesa di controlli maturati |
| BTC | SWING | 12 | in attesa di controlli maturati |
| BTC | MEDIO | 18 | in attesa di controlli maturati |
| DOGE | BREVE | 13 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 18 | in attesa di controlli maturati |
| DOGE | SWING | 12 | in attesa di controlli maturati |
| DOGE | MEDIO | 18 | in attesa di controlli maturati |
| SOL | BREVE | 13 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 18 | in attesa di controlli maturati |
| SOL | SWING | 12 | in attesa di controlli maturati |
| SOL | MEDIO | 18 | in attesa di controlli maturati |

## Come leggere le raccomandazioni

- **OSSERVA**: ci sono pochi controlli, quindi il dato è rumore utile solo da monitorare.
- **PESO OK**: il modulo sta aiutando, ma non abbastanza da aumentare peso.
- **MANTIENI / OSSERVA**: risultato vicino al neutro.
- **NON AUMENTARE**: il modulo non sta ancora dimostrando abbastanza utilità.
- **POSSIBILE AUMENTO LEGGERO**: modulo buono, ma la modifica resta prudente.
- **POSSIBILE RIDUZIONE PESO**: modulo debole su quell’orizzonte, da ridurre solo con dati maturi.

Nota importante: questo file **non modifica automaticamente** `global_confluence_report.py`.
Produce solo una raccomandazione leggibile. La modifica reale dei pesi va fatta a mano, dopo abbastanza dati.

## Stato attuale

Ci sono già alcuni controlli brevi, ma siamo ancora in feedback rapido. Non bisogna modificare pesi del Global.
