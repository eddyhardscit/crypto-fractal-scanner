# Bitcoin Macro Cycle — Power Law e Four-Year Spiral

Generato: 2026-08-05 05:15 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 64.253 $ | prezzo corrente |
| Power Law centrale | 123.371 $ | deviazione -47,92% |
| Banda p10-p90 | 76.478 $ / 309.644 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 1,45% | posizione storica nel corridoio |
| Esponente β | 5,8283 | R² log-log 91,96% |
| Stabilità β | BASSA | range 1,3117 cambiando finestra |
| Ultimo halving | 2024-04-19 | 838 giorni fa |
| Fase ciclo | 57,36% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-05 (4340 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.2576) × giorni^5.8283
- Prezzo centrale oggi: **123.371 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 1,45%
- Scarto dal centro: **-47,92%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8283 | 91,96% |
| 2015 | 5,9134 | 91,52% |
| 2016 | 5,6010 | 87,76% |
| 2017 | 4,8708 | 82,87% |
| 2018 | 4,6017 | 78,33% |

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
| 2012-11-28 → 2016-07-09 | 2014-12-25 | -22,31% | -22,82% | -23,42% | +42,83% |
| 2016-07-09 → 2020-05-11 | 2018-09-21 | -3,75% | -38,61% | -39,31% | +48,77% |
| 2020-05-11 → 2024-04-19 | 2022-08-14 | -16,54% | -30,92% | -10,97% | +20,93% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOTTOPERFORMA BTC | -6 | -1 | -10.296871811084118 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -5 | -1 | -11.026235741153933 | 0 |

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
