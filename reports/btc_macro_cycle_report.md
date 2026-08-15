# Bitcoin Macro Cycle — Power Law e Four-Year Spiral

Generato: 2026-08-15 05:34 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 63.058 $ | prezzo corrente |
| Power Law centrale | 123.635 $ | deviazione -49,00% |
| Banda p10-p90 | 76.612 $ / 311.327 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 0,30% | posizione storica nel corridoio |
| Esponente β | 5,8200 | R² log-log 91,94% |
| Stabilità β | BASSA | range 1,3148 cambiando finestra |
| Ultimo halving | 2024-04-19 | 848 giorni fa |
| Fase ciclo | 58,04% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-15 (4350 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.1907) × giorni^5.8200
- Prezzo centrale oggi: **123.635 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 0,30%
- Scarto dal centro: **-49,00%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8200 | 91,94% |
| 2015 | 5,9042 | 91,50% |
| 2016 | 5,5903 | 87,73% |
| 2017 | 4,8604 | 82,85% |
| 2018 | 4,5894 | 78,32% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-03 | -15,25% | -9,52% | -9,13% | +52,98% |
| 2016-07-09 → 2020-05-11 | 2018-10-01 | -4,13% | -41,33% | -37,68% | +26,61% |
| 2020-05-11 → 2024-04-19 | 2022-08-24 | -9,80% | -24,33% | +16,05% | +22,28% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | 2 | 0 | 0.1423796422559187 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -4 | -1 | -2.745817411130047 | 0 |

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
