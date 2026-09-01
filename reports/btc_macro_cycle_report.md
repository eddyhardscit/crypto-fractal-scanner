# Bitcoin Macro Cycle — Power Law e Four-Year Spiral

Generato: 2026-09-01 05:33 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 79.009 $ | prezzo corrente |
| Power Law centrale | 124.394 $ | deviazione -36,49% |
| Banda p10-p90 | 77.295 $ / 314.321 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 11,98% | posizione storica nel corridoio |
| Esponente β | 5,8085 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3165 cambiando finestra |
| Ultimo halving | 2024-04-19 | 865 giorni fa |
| Fase ciclo | 59,21% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-09-01 (4367 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.0975) × giorni^5.8085
- Prezzo centrale oggi: **124.394 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 11,98%
- Scarto dal centro: **-36,49%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8085 | 91,93% |
| 2015 | 5,8913 | 91,48% |
| 2016 | 5,5758 | 87,73% |
| 2017 | 4,8473 | 82,89% |
| 2018 | 4,5748 | 78,38% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-18 | +15,82% | +6,19% | +32,87% | +84,07% |
| 2016-07-09 → 2020-05-11 | 2018-10-17 | -14,80% | -44,52% | -22,57% | +23,83% |
| 2020-05-11 → 2024-04-19 | 2022-09-10 | -11,71% | -20,97% | -6,08% | +19,15% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 5 | 1 | 15.039304151553434 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -7 | -1 | -4.002727839383258 | 0 |

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
