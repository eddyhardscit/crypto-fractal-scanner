# Bitcoin Macro Cycle — Power Law e Four-Year Spiral

Generato: 2026-07-12 07:40 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 63.818 $ | prezzo corrente |
| Power Law centrale | 122.070 $ | deviazione -47,72% |
| Banda p10-p90 | 76.175 $ / 306.474 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 1,78% | posizione storica nel corridoio |
| Esponente β | 5,8472 | R² log-log 92,00% |
| Stabilità β | BASSA | range 1,3048 cambiando finestra |
| Ultimo halving | 2024-04-19 | 814 giorni fa |
| Fase ciclo | 55,72% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-07-12 (4317 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.4105) × giorni^5.8472
- Prezzo centrale oggi: **122.070 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 1,78%
- Scarto dal centro: **-47,72%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8472 | 92,00% |
| 2015 | 5,9344 | 91,57% |
| 2016 | 5,6253 | 87,81% |
| 2017 | 4,8947 | 82,89% |
| 2018 | 4,6297 | 78,36% |

### Backtest walk-forward contro prezzo invariato

| Orizzonte | Controlli | Vittorie vs naive | Errore mediano modello | Errore mediano naive |
| --- | --- | --- | --- | --- |
| 90g | 79 | 26,58% | 55,14% | 20,89% |
| 180g | 79 | 40,51% | 60,84% | 45,16% |
| 365g | 79 | 56,96% | 73,12% | 81,57% |
| 730g | 79 | 59,49% | 72,50% | 109,89% |

## Bitcoin Four-Year Spiral

Nel grafico l'angolo rappresenta il tempo dentro una finestra di quattro anni e il raggio rappresenta il prezzo in scala logaritmica. ATH, bottom storici e halving sono marker descrittivi: la spirale rende visibili le ricorrenze, ma non dimostra che il ciclo futuro debba ripetersi.

![Bitcoin Four-Year Spiral](bitcoin_four_year_spiral.png)

## Stessa fase dei cicli halving precedenti

| Ciclo | Data analoga | +30g | +90g | +180g | +365g |
| --- | --- | --- | --- | --- | --- |
| 2012-11-28 → 2016-07-09 | 2014-12-03 | -15,99% | -24,88% | -40,55% | -3,72% |
| 2016-07-09 → 2020-05-11 | 2018-08-29 | -5,72% | -45,78% | -44,90% | +34,95% |
| 2020-05-11 → 2024-04-19 | 2022-07-22 | -5,20% | -16,12% | -8,92% | +31,07% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | -1 | 0 | 14.342855996126591 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -8 | -1 | -15.643437181166664 | 0 |

## Tracker live Power Law

| Orizzonte | Controlli | Vittorie vs naive | Errore modello | Errore naive | Stato |
| --- | --- | --- | --- | --- | --- |
| 90g | 0 | n/a | n/a | n/a | RACCOLTA LIVE / PESO 0 |
| 180g | 0 | n/a | n/a | n/a | RACCOLTA LIVE / PESO 0 |
| 365g | 0 | n/a | n/a | n/a | RACCOLTA LIVE / PESO 0 |

Il modulo resta a peso 0 anche con un buon backtest. Prima si osserva la verifica live, poi si decide se usarlo soltanto per il rischio macro di lungo periodo. Le fotografie live della Power Law vengono salvate una sola volta per mese, così non si contano come indipendenti previsioni giornaliere quasi identiche.

## File prodotti

- `reports/btc_power_law_metrics.csv`
- `reports/btc_power_law_backtest.csv`
- `reports/btc_cycle_phase_metrics.csv`
- `reports/btc_macro_cycle_history.csv`
- `reports/btc_macro_cycle_tracker_metrics.csv`
