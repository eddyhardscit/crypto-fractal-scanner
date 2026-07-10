<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-07-10 01:12:28 UTC

Questo report crea grafici solo quando lo scanner mostra una percentuale estrema: casi positivi o negativi almeno pari a **80%**.

Obiettivo: non guardare solo la percentuale finale, ma vedere **come si sono mossi dopo** i casi storici simili.

Fonte match: **CSV completo: latest_scanner_matches.csv**, con fallback sui file `BTC_matches.csv`, `SOL_matches.csv`, `DOGE_matches.csv`.

## Trigger estremi

| Asset   | Direzione             | Trigger   | Percentuale   | Motivo                           |   Match disponibili |   Casi usati nel grafico |
|:--------|:----------------------|:----------|:--------------|:---------------------------------|--------------------:|-------------------------:|
| BTC     | NESSUNO               | NO        | 72,50%        | Nessun lato sopra soglia estrema |                  40 |                        0 |
| SOL     | NESSUNO               | NO        | 57,50%        | Nessun lato sopra soglia estrema |                  40 |                        0 |
| DOGE    | NEGATIVO / RIBASSISTA | SI        | 87,50%        | Casi negativi 87,50% >= 80,00%   |                  40 |                       35 |

## DOGE — casi ribassisti

- Trigger: **Casi negativi 87,50% >= 80,00%**
- Casi disponibili: **40**
- Casi usati nei grafici: **35**

- Return mediano 7g: **-4,77%**
- Return mediano 14g: **-25,68%**
- Return mediano 30g: **-25,05%**
- Return medio 30g: **-22,14%**
- Drawdown mediano durante il percorso: **-29,24%**
- Max gain mediano durante il percorso: **4,26%**

### Distribuzione 30 giorni

| P10     | P25     | P50     | P75     | P90    |
|:--------|:--------|:--------|:--------|:-------|
| -37,75% | -31,63% | -25,05% | -11,06% | -3,17% |

### Grafico pulito: bande + mediana

![Extreme clean DOGE](extreme_cases_DOGE_negative_clean_bands.png)

### Grafico asset per asset

Qui non vengono più mostrate 40 linee casuali tutte insieme. Ogni linea colorata rappresenta la mediana di un asset storico. Se gli asset sono troppi, i meno importanti vengono aggregati in `ALTRI`.

![Extreme asset medians DOGE](extreme_cases_DOGE_negative_asset_medians.png)

### Grafico casi ordinati per risultato finale

![Extreme ranked DOGE](extreme_cases_DOGE_negative_ranked_returns.png)

### Tabella asset storici aggregati

| Asset storico   |   Casi | Best similarity   | Return mediano 7g   | Return mediano 14g   | Return mediano 30g   | Drawdown mediano   | Max gain mediano   |
|:----------------|-------:|:------------------|:--------------------|:---------------------|:---------------------|:-------------------|:-------------------|
| AVAX-USD        |      2 | 86,00%            | 2,50%               | -18,92%              | -22,30%              | -28,90%            | 6,47%              |
| BAT-USD         |      2 | 84,84%            | 1,37%               | -15,76%              | -3,16%               | -17,66%            | 9,33%              |
| DOT-USD         |      2 | 84,63%            | -3,88%              | -15,82%              | -17,16%              | -21,09%            | 3,01%              |
| DASH-USD        |      1 | 88,64%            | -4,77%              | -32,96%              | -29,45%              | -33,95%            | 2,32%              |
| NEAR-USD        |      1 | 88,50%            | -36,88%             | -29,95%              | -25,05%              | -39,10%            | 0,00%              |
| VET-USD         |      1 | 87,39%            | -0,81%              | -16,56%              | -27,52%              | -29,00%            | 4,39%              |
| QTUM-USD        |      1 | 87,31%            | -2,78%              | -33,37%              | -31,65%              | -37,87%            | 0,00%              |
| ZEC-USD         |      1 | 87,28%            | -10,86%             | -6,03%               | -11,71%              | -11,71%            | 5,15%              |
| 1INCH-USD       |      1 | 86,51%            | -14,13%             | -34,05%              | -31,62%              | -42,19%            | 0,00%              |
| OMG-USD         |      1 | 86,49%            | -6,66%              | -30,96%              | -32,46%              | -37,50%            | 0,00%              |
| CHZ-USD         |      1 | 86,13%            | -6,74%              | -22,27%              | -19,17%              | -28,71%            | 5,97%              |
| XTZ-USD         |      1 | 85,94%            | -2,08%              | -12,14%              | -10,41%              | -12,14%            | 4,26%              |
| ENJ-USD         |      1 | 85,77%            | -13,64%             | -33,46%              | -16,55%              | -33,46%            | 5,00%              |
| ETH-USD         |      1 | 85,35%            | -15,09%             | -44,85%              | -36,11%              | -44,85%            | 3,20%              |
| BCH-USD         |      1 | 85,29%            | -5,60%              | -35,62%              | -46,95%              | -47,58%            | 3,48%              |
| INJ-USD         |      1 | 85,21%            | -6,37%              | -27,66%              | -42,93%              | -42,93%            | 3,20%              |
| NEO-USD         |      1 | 85,19%            | 3,34%               | -16,70%              | -26,97%              | -27,65%            | 3,34%              |
| ADA-USD         |      1 | 85,15%            | 6,89%               | -18,76%              | -18,34%              | -19,98%            | 12,55%             |

### Casi contrari da non ignorare

Questi sono i casi che, nonostante il trigger ribassista, finirono positivi. Sono le eccezioni da guardare per capire perché alcune linee salivano nel vecchio grafico.

| Asset storico   | End        | Similarity   | Return 30g   | Drawdown   | Max gain   |
|:----------------|:-----------|:-------------|:-------------|:-----------|:-----------|
| XLM-USD         | 2020-01-06 | 87,24%       | 39,92%       | -5,54%     | 39,92%     |
| XRP-USD         | 2020-01-01 | 86,82%       | 24,17%       | -2,40%     | 26,46%     |
| AVAX-USD        | 2023-09-23 | 84,30%       | 18,71%       | -1,26%     | 19,74%     |
| KSM-USD         | 2024-05-07 | 84,23%       | 15,56%       | -3,55%     | 16,25%     |
| THETA-USD       | 2022-06-03 | 86,09%       | 1,59%        | -8,56%     | 23,35%     |

### Match individuali usati

| Asset storico   | Start      | End        | Similarity   | Return 30g report   | Drawdown report   | Max gain report   | Return path calcolato   |
|:----------------|:-----------|:-----------|:-------------|:--------------------|:------------------|:------------------|:------------------------|
| DASH-USD        | 2022-02-20 | 2022-05-30 | 88,64%       | -29,45%             | -33,95%           | 2,32%             | -29,45%                 |
| NEAR-USD        | 2022-03-02 | 2022-06-09 | 88,50%       | -25,05%             | -39,10%           | 0,00%             | -25,05%                 |
| VET-USD         | 2022-02-22 | 2022-06-01 | 87,39%       | -27,52%             | -29,00%           | 4,39%             | -27,52%                 |
| QTUM-USD        | 2022-02-20 | 2022-05-30 | 87,31%       | -31,65%             | -37,87%           | 0,00%             | -31,65%                 |
| ZEC-USD         | 2019-05-17 | 2019-08-24 | 87,28%       | -11,71%             | -11,71%           | 5,15%             | -11,71%                 |
| 1INCH-USD       | 2022-02-22 | 2022-06-01 | 86,51%       | -31,62%             | -42,19%           | 0,00%             | -31,62%                 |
| OMG-USD         | 2022-02-20 | 2022-05-30 | 86,49%       | -32,46%             | -37,50%           | 0,00%             | -32,46%                 |
| CHZ-USD         | 2022-02-24 | 2022-06-03 | 86,13%       | -19,17%             | -28,71%           | 5,97%             | -19,17%                 |
| AVAX-USD        | 2025-08-14 | 2025-11-21 | 86,00%       | -8,75%              | -14,04%           | 12,94%            | -8,75%                  |
| XTZ-USD         | 2025-12-06 | 2026-03-15 | 85,94%       | -10,41%             | -12,14%           | 4,26%             | -10,41%                 |
| ENJ-USD         | 2022-02-25 | 2022-06-04 | 85,77%       | -16,55%             | -33,46%           | 5,00%             | -16,55%                 |
| ETH-USD         | 2022-02-25 | 2022-06-04 | 85,35%       | -36,11%             | -44,85%           | 3,20%             | -36,11%                 |
| BCH-USD         | 2022-02-20 | 2022-05-30 | 85,29%       | -46,95%             | -47,58%           | 3,48%             | -46,95%                 |
| INJ-USD         | 2022-02-22 | 2022-06-01 | 85,21%       | -42,93%             | -42,93%           | 3,20%             | -42,93%                 |
| NEO-USD         | 2022-02-20 | 2022-05-30 | 85,19%       | -26,97%             | -27,65%           | 3,34%             | -26,97%                 |
| ADA-USD         | 2022-02-20 | 2022-05-30 | 85,15%       | -18,34%             | -19,98%           | 12,55%            | -18,34%                 |
| OP-USD          | 2025-12-02 | 2026-03-11 | 85,07%       | -4,42%              | -15,36%           | 14,28%            | -4,42%                  |
| HBAR-USD        | 2020-07-02 | 2020-10-09 | 84,96%       | -12,18%             | -17,30%           | 0,27%             | -12,18%                 |
| SOL-USD         | 2022-02-28 | 2022-06-07 | 84,91%       | -2,33%              | -28,51%           | 7,34%             | -2,33%                  |
| BAT-USD         | 2018-09-19 | 2018-12-27 | 84,84%       | -1,76%              | -6,08%            | 10,32%            | -1,76%                  |

## Come leggerlo

- **Grafico pulito**: guarda prima questo. Ti dice la traiettoria centrale senza casino.
- **Grafico asset per asset**: mostra se la discesa/salita è comune a più asset o dipende solo da pochi casi.
- **Grafico casi ordinati**: mostra quanto sono dispersi i risultati finali a 30 giorni.
- **Casi contrari**: sono le eccezioni. Servono per non trasformare una statistica forte in una certezza falsa.

Nota: questo report è visivo e diagnostico. Non modifica il Global Confluence e non autorizza leva.
<!-- EXTREME_CASES_PATH_END -->