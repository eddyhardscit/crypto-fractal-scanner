# Bitcoin Macro Cycle — Power Law e Four-Year Spiral

Generato: 2026-08-23 05:32 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 76.281 $ | prezzo corrente |
| Power Law centrale | 123.860 $ | deviazione -38,41% |
| Banda p10-p90 | 76.832 $ / 312.861 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 9,45% | posizione storica nel corridoio |
| Esponente β | 5,8140 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3164 cambiando finestra |
| Ultimo halving | 2024-04-19 | 856 giorni fa |
| Fase ciclo | 58,59% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-23 (4358 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.1420) × giorni^5.8140
- Prezzo centrale oggi: **123.860 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 9,45%
- Scarto dal centro: **-38,41%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8140 | 91,93% |
| 2015 | 5,8975 | 91,48% |
| 2016 | 5,5827 | 87,72% |
| 2017 | 4,8531 | 82,86% |
| 2018 | 4,5811 | 78,33% |

### Backtest walk-forward contro prezzo invariato

| Orizzonte | Controlli | Vittorie vs naive | Errore mediano modello | Errore mediano naive |
| --- | --- | --- | --- | --- |
| 90g | 80 | 27,50% | 53,06% | 20,63% |
| 180g | 80 | 41,25% | 60,12% | 47,43% |
| 365g | 80 | 57,50% | 72,70% | 78,86% |
| 730g | 80 | 58,75% | 72,61% | 109,35% |

## Bitcoin Four-Year Spiral

Nel grafico l'angolo rappresenta il tempo dentro una finestra di quattro anni e il raggio rappresenta il prezzo in scala logaritmica. ATH, bottom storici e halving sono marker descrittivi: la spirale rende visibili le ricorrenze, ma non dimostra che il ciclo futuro debba ripetersi.

![Bitcoin Four-Year Spiral](bitcoin_four_year_spiral.png)

## Stessa fase dei cicli halving precedenti

| Ciclo | Data analoga | +30g | +90g | +180g | +365g |
| --- | --- | --- | --- | --- | --- |
| 2012-11-28 → 2016-07-09 | 2015-01-10 | -19,90% | -14,09% | -2,03% | +63,03% |
| 2016-07-09 → 2020-05-11 | 2018-10-08 | -1,84% | -38,72% | -23,94% | +23,70% |
| 2020-05-11 → 2024-04-19 | 2022-09-01 | -4,05% | -14,70% | +15,01% | +28,19% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 4 | 1 | 4.605483860403847 | 0 |
| DOGE | DOGE/BTC | RELATIVA MISTA / NON CONFERMATA | 0 | 0 | 11.538878428376155 | 0 |

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
