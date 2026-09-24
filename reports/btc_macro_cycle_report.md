# Bitcoin Macro Cycle — Power Law e Four-Year Spiral

Generato: 2026-09-24 05:32 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 84.116 $ | prezzo corrente |
| Power Law centrale | 125.737 $ | deviazione -33,10% |
| Banda p10-p90 | 78.110 $ / 317.060 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 17,24% | posizione storica nel corridoio |
| Esponente β | 5,7946 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3167 cambiando finestra |
| Ultimo halving | 2024-04-19 | 888 giorni fa |
| Fase ciclo | 60,78% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-09-24 (4390 osservazioni)
- Formula stimata: prezzo ≈ exp(-38.9845) × giorni^5.7946
- Prezzo centrale oggi: **125.737 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 17,24%
- Scarto dal centro: **-33,10%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,7946 | 91,93% |
| 2015 | 5,8756 | 91,48% |
| 2016 | 5,5585 | 87,75% |
| 2017 | 4,8325 | 82,98% |
| 2018 | 4,5589 | 78,52% |

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
| 2012-11-28 → 2016-07-09 | 2015-02-08 | +30,59% | +8,24% | +25,14% | +67,16% |
| 2016-07-09 → 2020-05-11 | 2018-11-08 | -46,14% | -47,10% | -9,67% | +36,43% |
| 2020-05-11 → 2024-04-19 | 2022-10-03 | +2,73% | -15,28% | +44,78% | +39,78% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 6 | 1 | 10.016027629237346 | 0 |
| DOGE | DOGE/BTC | RELATIVA MISTA / NON CONFERMATA | -2 | 0 | -1.5515997604615972 | 0 |

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
