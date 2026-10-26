# Bitcoin Macro Cycle — Power Law e Four-Year Spiral

Generato: 2026-10-26 06:34 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 79.936 $ | prezzo corrente |
| Power Law centrale | 127.302 $ | deviazione -37,21% |
| Banda p10-p90 | 79.773 $ / 322.488 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 10,22% | posizione storica nel corridoio |
| Esponente β | 5,7764 | R² log-log 91,95% |
| Stabilità β | BASSA | range 1,3152 cambiando finestra |
| Ultimo halving | 2024-04-19 | 920 giorni fa |
| Fase ciclo | 62,97% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-10-26 (4422 osservazioni)
- Formula stimata: prezzo ≈ exp(-38.8376) × giorni^5.7764
- Prezzo centrale oggi: **127.302 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 10,22%
- Scarto dal centro: **-37,21%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,7764 | 91,95% |
| 2015 | 5,8552 | 91,49% |
| 2016 | 5,5362 | 87,79% |
| 2017 | 4,8143 | 83,12% |
| 2018 | 4,5400 | 78,74% |

### Backtest walk-forward contro prezzo invariato

| Orizzonte | Controlli | Vittorie vs naive | Errore mediano modello | Errore mediano naive |
| --- | --- | --- | --- | --- |
| 90g | 82 | 29,27% | 48,35% | 21,05% |
| 180g | 82 | 42,68% | 57,61% | 46,17% |
| 365g | 82 | 58,54% | 70,14% | 84,45% |
| 730g | 82 | 57,32% | 72,61% | 108,40% |

## Bitcoin Four-Year Spiral

Nel grafico l'angolo rappresenta il tempo dentro una finestra di quattro anni e il raggio rappresenta il prezzo in scala logaritmica. ATH, bottom storici e halving sono marker descrittivi: la spirale rende visibili le ricorrenze, ma non dimostra che il ciclo futuro debba ripetersi.

![Bitcoin Four-Year Spiral](bitcoin_four_year_spiral.png)

## Stessa fase dei cicli halving precedenti

| Ciclo | Data analoga | +30g | +90g | +180g | +365g |
| --- | --- | --- | --- | --- | --- |
| 2012-11-28 → 2016-07-09 | 2015-03-09 | -15,39% | -23,04% | -18,85% | +42,94% |
| 2016-07-09 → 2020-05-11 | 2018-12-09 | +11,53% | +9,66% | +122,56% | +104,77% |
| 2020-05-11 → 2024-04-19 | 2022-11-03 | -16,34% | +17,39% | +41,91% | +71,86% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | -1 | 0 | -12.970367847548081 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -7 | -1 | -18.498696779573322 | 0 |

## Tracker live Power Law

| Orizzonte | Controlli | Vittorie vs naive | Errore modello | Errore naive | Stato |
| --- | --- | --- | --- | --- | --- |
| 90g | 1 | 0,00% | 47,80% | 28,30% | RACCOLTA LIVE / PESO 0 |
| 180g | 0 | n/a | n/a | n/a | RACCOLTA LIVE / PESO 0 |
| 365g | 0 | n/a | n/a | n/a | RACCOLTA LIVE / PESO 0 |

Il modulo resta a peso 0 anche con un buon backtest. Prima si osserva la verifica live, poi si decide se usarlo soltanto per il rischio macro di lungo periodo. Le fotografie live della Power Law vengono salvate una sola volta per mese, così non si contano come indipendenti previsioni giornaliere quasi identiche.

## File prodotti

- `reports/btc_power_law_metrics.csv`
- `reports/btc_power_law_backtest.csv`
- `reports/btc_cycle_phase_metrics.csv`
- `reports/btc_macro_cycle_history.csv`
- `reports/btc_macro_cycle_tracker_metrics.csv`
