# Bitcoin Macro Cycle — Power Law e Four-Year Spiral

Generato: 2026-07-11 19:00 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 64.272 $ | prezzo corrente |
| Power Law centrale | 122.003 $ | deviazione -47,32% |
| Banda p10-p90 | 76.159 $ / 306.315 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 2,06% | posizione storica nel corridoio |
| Esponente β | 5,8480 | R² log-log 92,00% |
| Stabilità β | BASSA | range 1,3044 cambiando finestra |
| Ultimo halving | 2024-04-19 | 813 giorni fa |
| Fase ciclo | 55,65% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-07-11 (4316 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.4172) × giorni^5.8480
- Prezzo centrale oggi: **122.003 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 2,06%
- Scarto dal centro: **-47,32%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8480 | 92,00% |
| 2015 | 5,9354 | 91,58% |
| 2016 | 5,6264 | 87,82% |
| 2017 | 4,8958 | 82,90% |
| 2018 | 4,6309 | 78,37% |

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
| 2012-11-28 → 2016-07-09 | 2014-12-02 | -17,59% | -27,71% | -39,63% | -5,80% |
| 2016-07-09 → 2020-05-11 | 2018-08-28 | -5,91% | -46,74% | -46,30% | +37,46% |
| 2020-05-11 → 2024-04-19 | 2022-07-21 | -8,63% | -17,38% | -8,65% | +29,11% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | -1 | 0 | 15.499531957225177 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -8 | -1 | -13.500180629169979 | 0 |

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
