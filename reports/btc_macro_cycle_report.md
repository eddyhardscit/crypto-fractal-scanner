# Bitcoin Macro Cycle — Power Law e Four-Year Spiral

Generato: 2026-08-20 05:32 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 69.561 $ | prezzo corrente |
| Power Law centrale | 123.919 $ | deviazione -43,87% |
| Banda p10-p90 | 76.709 $ / 312.248 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 4,59% | posizione storica nel corridoio |
| Esponente β | 5,8160 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3162 cambiando finestra |
| Ultimo halving | 2024-04-19 | 853 giorni fa |
| Fase ciclo | 58,39% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-20 (4355 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.1578) × giorni^5.8160
- Prezzo centrale oggi: **123.919 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 4,59%
- Scarto dal centro: **-43,87%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8160 | 91,93% |
| 2015 | 5,8997 | 91,48% |
| 2016 | 5,5851 | 87,72% |
| 2017 | 4,8553 | 82,85% |
| 2018 | 4,5835 | 78,31% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-07 | -24,49% | -13,98% | -8,60% | +55,62% |
| 2016-07-09 → 2020-05-11 | 2018-10-06 | -2,56% | -41,45% | -25,28% | +21,25% |
| 2020-05-11 → 2024-04-19 | 2022-08-29 | -4,29% | -18,98% | +14,18% | +36,60% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 5 | 1 | 2.4056987105124605 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -4 | -1 | -3.105325587771357 | 0 |

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
