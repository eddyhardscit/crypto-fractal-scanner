# Extreme cases path report

Generato: 2026-09-17 05:32 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +87,50%       | Casi positivi 87.50% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +65,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +75,00%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 87.50% >= 80%**
- Casi usati nei grafici: **35**
- Return mediano 7g: **+9,66%**
- Return mediano 14g: **+15,21%**
- Return mediano 30g: **+26,30%**
- Drawdown mediano: **-1,35%**
- Max gain mediano: **+41,60%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+0,36%**
- Spike p75 prima del minimo: **+0,00%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 1**
- Scarico mediano dal picco al minimo: **-1,52%**
- Casi con almeno +5% prima del minimo: **+0,00%**
- Casi con almeno +10% prima del minimo: **+0,00%**
- Casi con almeno +15% prima del minimo: **+0,00%**
- Discesa quasi immediata: **+88,57%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10     | P25     | P50     | P75     | P90     |
|:--------|:--------|:--------|:--------|:--------|
| +10,29% | +19,92% | +26,30% | +58,20% | +73,09% |

### Grafico pulito: bande + mediana

![Extreme clean BTC](extreme_cases_BTC_positive_clean_bands.png)

### Grafico asset per asset

![Extreme asset medians BTC](extreme_cases_BTC_positive_asset_medians.png)

### Spike massimo prima della discesa

La sigla `g7` sopra una barra significa che il massimo rialzo è avvenuto al giorno 7.

![Extreme spike before dump BTC](extreme_cases_BTC_positive_spike_before_dump.png)

### Spike iniziale contro minimo successivo

![Extreme spike vs low BTC](extreme_cases_BTC_positive_spike_vs_low.png)

### Casi ordinati per risultato finale

![Extreme ranked BTC](extreme_cases_BTC_positive_ranked_returns.png)

### Casi con spike maggiore prima del dump

| Asset storico   | End        | Similarity   | Spike prima del minimo   |   Giorno spike | Minimo 30g   |   Giorno minimo | Dump dal picco   | Return 30g   | Sequenza                      |
|:----------------|:-----------|:-------------|:-------------------------|---------------:|:-------------|----------------:|:-----------------|:-------------|:------------------------------|
| INJ-USD         | 2023-11-18 | +88,66%      | +4,94%                   |              1 | -10,45%      |               3 | -14,67%          | +131,17%     | RIALZO MODESTO PRIMA DEL DUMP |
| DASH-USD        | 2020-12-16 | +86,53%      | +4,49%                   |              4 | -17,00%      |              17 | -20,57%          | +18,83%      | RIALZO MODESTO PRIMA DEL DUMP |
| ZEC-USD         | 2019-04-26 | +86,57%      | +2,04%                   |              7 | -7,96%       |              13 | -9,80%           | +23,44%      | ECCEZIONE POSITIVA            |
| DASH-USD        | 2019-04-26 | +85,09%      | +0,71%                   |              2 | -1,23%       |               3 | -1,93%           | +48,55%      | DISCESA QUASI IMMEDIATA       |
| LTC-USD         | 2020-12-13 | +84,79%      | +0,44%                   |              1 | -0,73%       |               2 | -1,17%           | +61,75%      | DISCESA QUASI IMMEDIATA       |
| BCH-USD         | 2019-04-26 | +85,98%      | +0,02%                   |              1 | -10,33%      |               3 | -10,35%          | +64,03%      | DISCESA QUASI IMMEDIATA       |
| THETA-USD       | 2023-11-30 | +89,12%      | +0,00%                   |              0 | -1,35%       |               1 | -1,35%           | +24,03%      | DISCESA QUASI IMMEDIATA       |
| QTUM-USD        | 2023-11-21 | +89,10%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +14,24%      | DISCESA QUASI IMMEDIATA       |
| 1INCH-USD       | 2023-11-28 | +88,81%      | +0,00%                   |              0 | -0,60%       |               2 | -0,60%           | +24,79%      | DISCESA QUASI IMMEDIATA       |
| XRP-USD         | 2023-11-26 | +88,47%      | +0,00%                   |              0 | -2,05%       |               1 | -2,05%           | +0,90%       | DISCESA QUASI IMMEDIATA       |
| XLM-USD         | 2020-12-21 | +88,19%      | +0,00%                   |              0 | -23,98%      |               2 | -23,98%          | +76,94%      | DISCESA QUASI IMMEDIATA       |
| RUNE-USD        | 2023-09-08 | +87,79%      | +0,00%                   |              0 | -8,02%       |               3 | -8,02%           | +9,23%       | DISCESA QUASI IMMEDIATA       |
| ALGO-USD        | 2023-11-30 | +87,77%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +66,00%      | DISCESA QUASI IMMEDIATA       |
| AVAX-USD        | 2021-09-13 | +87,24%      | +0,00%                   |              0 | -2,88%       |               1 | -2,88%           | +3,85%       | DISCESA QUASI IMMEDIATA       |
| EGLD-USD        | 2023-12-01 | +87,06%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +50,02%      | DISCESA QUASI IMMEDIATA       |
| BTC-USD         | 2019-04-28 | +87,06%      | +0,00%                   |              0 | -0,71%       |               1 | -0,71%           | +64,99%      | DISCESA QUASI IMMEDIATA       |
| MANA-USD        | 2023-11-26 | +86,96%      | +0,00%                   |              0 | -4,09%       |               4 | -4,09%           | +24,12%      | DISCESA QUASI IMMEDIATA       |
| ZIL-USD         | 2023-11-28 | +86,62%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +24,01%      | DISCESA QUASI IMMEDIATA       |
| ADA-USD         | 2023-12-01 | +86,46%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +54,66%      | DISCESA QUASI IMMEDIATA       |
| ADA-USD         | 2020-12-16 | +86,38%      | +0,00%                   |              0 | -18,61%      |               7 | -18,61%          | +80,52%      | ECCEZIONE POSITIVA            |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
