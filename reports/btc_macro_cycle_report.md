# Bitcoin Macro Cycle — Power Law e Four-Year Spiral

Generato: 2026-09-22 05:32 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 85.105 $ | prezzo corrente |
| Power Law centrale | 125.667 $ | deviazione -32,28% |
| Banda p10-p90 | 78.035 $ / 316.723 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 18,28% | posizione storica nel corridoio |
| Esponente β | 5,7956 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3169 cambiando finestra |
| Ultimo halving | 2024-04-19 | 886 giorni fa |
| Fase ciclo | 60,64% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-09-22 (4388 osservazioni)
- Formula stimata: prezzo ≈ exp(-38.9930) × giorni^5.7956
- Prezzo centrale oggi: **125.667 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 18,28%
- Scarto dal centro: **-32,28%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,7956 | 91,93% |
| 2015 | 5,8768 | 91,48% |
| 2016 | 5,5598 | 87,74% |
| 2017 | 4,8335 | 82,97% |
| 2018 | 4,5599 | 78,50% |

### Backtest walk-forward contro prezzo invariato

| Orizzonte | Controlli | Vittorie vs naive | Errore mediano modello | Errore mediano naive |
| --- | --- | --- | --- | --- |
| 90g | 81 | 28,40% | 50,97% | 20,89% |
| 180g | 81 | 41,98% | 59,41% | 47,18% |
| 365g | 81 | 58,02% | 72,28% | 81,57% |
| 730g | 81 | 58,02% | 72,72% | 108,81% |

## Bitcoin Four-Year Spiral

Nel grafico l'angolo rappresenta il tempo dentro una finestra di quattro anni e il raggio rappresenta il prezzo in scala logaritmica. ATH, bottom storici e halving sono marker descrittivi: la spirale rende visibili le ricorrenze, ma non dimostra che il ciclo futuro debba ripetersi.

![Bitcoin Four-Year Spiral](bitcoin_four_year_spiral.png)

## Stessa fase dei cicli halving precedenti

| Ciclo | Data analoga | +30g | +90g | +180g | +365g |
| --- | --- | --- | --- | --- | --- |
| 2012-11-28 → 2016-07-09 | 2015-02-06 | +23,43% | +6,78% | +26,82% | +69,40% |
| 2016-07-09 → 2020-05-11 | 2018-11-06 | -45,50% | -46,46% | -10,30% | +44,88% |
| 2020-05-11 → 2024-04-19 | 2022-10-01 | +6,13% | -14,03% | +45,16% | +44,90% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 5 | 1 | 11.494254741200516 | 0 |
| DOGE | DOGE/BTC | RELATIVA MISTA / NON CONFERMATA | -1 | 0 | -2.9360975965424307 | 0 |

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
