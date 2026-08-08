# Extreme cases path report

Generato: 2026-08-08 05:17 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +87,50%       | Casi positivi 87.50% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +77,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 87.50% >= 80%**
- Casi usati nei grafici: **35**
- Return mediano 7g: **+6,49%**
- Return mediano 14g: **+6,67%**
- Return mediano 30g: **+14,08%**
- Drawdown mediano: **-1,22%**
- Max gain mediano: **+25,33%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+0,97%**
- Spike p75 prima del minimo: **+0,79%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 1**
- Scarico mediano dal picco al minimo: **-2,50%**
- Casi con almeno +5% prima del minimo: **+2,86%**
- Casi con almeno +10% prima del minimo: **+2,86%**
- Casi con almeno +15% prima del minimo: **+0,00%**
- Discesa quasi immediata: **+77,14%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25    | P50     | P75     | P90     |
|:-------|:-------|:--------|:--------|:--------|
| +5,18% | +8,72% | +14,08% | +20,91% | +38,54% |

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

| Asset storico   | End        | Similarity   | Spike prima del minimo   |   Giorno spike | Minimo 30g   |   Giorno minimo | Dump dal picco   | Return 30g   | Sequenza                |
|:----------------|:-----------|:-------------|:-------------------------|---------------:|:-------------|----------------:|:-----------------|:-------------|:------------------------|
| 1INCH-USD       | 2024-10-13 | +85,74%      | +13,39%                  |              7 | -11,35%      |              22 | -21,82%          | +19,12%      | SPIKE PRIMA DEL DUMP    |
| QTUM-USD        | 2020-05-15 | +85,92%      | +4,58%                   |              3 | -0,44%       |               6 | -4,80%           | +14,94%      | ECCEZIONE POSITIVA      |
| QTUM-USD        | 2026-04-09 | +86,87%      | +3,95%                   |              8 | -6,19%       |              21 | -9,75%           | +4,54%       | ECCEZIONE POSITIVA      |
| LTC-USD         | 2026-04-06 | +85,43%      | +3,48%                   |              1 | -0,10%       |               6 | -3,46%           | +5,87%       | ECCEZIONE POSITIVA      |
| MKR-USD         | 2020-05-16 | +87,40%      | +1,63%                   |              1 | -4,76%       |               5 | -6,29%           | +63,84%      | DISCESA QUASI IMMEDIATA |
| LINK-USD        | 2026-04-09 | +85,35%      | +1,62%                   |              1 | -2,30%       |               3 | -3,86%           | +15,98%      | DISCESA QUASI IMMEDIATA |
| XTZ-USD         | 2026-04-09 | +85,41%      | +1,60%                   |              1 | -3,24%       |               3 | -4,76%           | +9,66%       | DISCESA QUASI IMMEDIATA |
| XRP-USD         | 2026-04-09 | +91,07%      | +0,93%                   |              1 | -1,42%       |               3 | -2,33%           | +5,65%       | DISCESA QUASI IMMEDIATA |
| ETC-USD         | 2020-11-11 | +85,67%      | +0,83%                   |              2 | -1,22%       |               4 | -2,03%           | +14,00%      | DISCESA QUASI IMMEDIATA |
| BNB-USD         | 2026-04-09 | +86,84%      | +0,76%                   |              2 | -1,76%       |               3 | -2,50%           | +7,78%       | DISCESA QUASI IMMEDIATA |
| ETC-USD         | 2026-04-09 | +85,99%      | +0,61%                   |              1 | -3,70%       |               3 | -4,28%           | +13,50%      | DISCESA QUASI IMMEDIATA |
| BTC-USD         | 2019-01-23 | +88,53%      | +0,48%                   |              3 | -5,18%       |              15 | -5,63%           | +11,73%      | ECCEZIONE POSITIVA      |
| ETH-USD         | 2026-04-09 | +90,10%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +6,28%       | DISCESA QUASI IMMEDIATA |
| SAND-USD        | 2023-10-21 | +89,88%      | +0,00%                   |              0 | -0,43%       |               1 | -0,43%           | +33,23%      | DISCESA QUASI IMMEDIATA |
| FIL-USD         | 2023-10-21 | +89,45%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +40,20%      | DISCESA QUASI IMMEDIATA |
| XRP-USD         | 2023-10-22 | +89,40%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +11,10%      | DISCESA QUASI IMMEDIATA |
| XLM-USD         | 2020-11-06 | +89,01%      | +0,00%                   |              0 | -5,08%       |               1 | -5,08%           | +109,40%     | DISCESA QUASI IMMEDIATA |
| LTC-USD         | 2023-10-19 | +87,75%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +13,12%      | DISCESA QUASI IMMEDIATA |
| OMG-USD         | 2019-01-26 | +87,22%      | +0,00%                   |              0 | -17,83%      |              11 | -17,83%          | +6,73%       | ECCEZIONE POSITIVA      |
| MATIC-USD       | 2023-10-22 | +87,13%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +20,26%      | DISCESA QUASI IMMEDIATA |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
