# Extreme cases path report

Generato: 2026-09-10 05:32 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +87,50%       | Casi positivi 87.50% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +67,50%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 87.50% >= 80%**
- Casi usati nei grafici: **35**
- Return mediano 7g: **+5,48%**
- Return mediano 14g: **+14,39%**
- Return mediano 30g: **+39,60%**
- Drawdown mediano: **-1,96%**
- Max gain mediano: **+43,15%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+2,62%**
- Spike p75 prima del minimo: **+1,23%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 1**
- Scarico mediano dal picco al minimo: **-3,26%**
- Casi con almeno +5% prima del minimo: **+11,43%**
- Casi con almeno +10% prima del minimo: **+8,57%**
- Casi con almeno +15% prima del minimo: **+8,57%**
- Discesa quasi immediata: **+68,57%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10     | P25     | P50     | P75     | P90     |
|:--------|:--------|:--------|:--------|:--------|
| +12,59% | +23,68% | +39,60% | +61,15% | +90,27% |

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
| XLM-USD         | 2020-12-11 | +90,75%      | +26,60%                  |              5 | -16,34%      |              12 | -33,92%          | +91,00%      | SPIKE PRIMA DEL DUMP    |
| ADA-USD         | 2020-12-11 | +86,28%      | +20,18%                  |              5 | -2,19%       |              12 | -18,61%          | +118,64%     | ECCEZIONE POSITIVA      |
| DASH-USD        | 2020-12-11 | +84,66%      | +17,30%                  |              9 | -6,83%       |              22 | -20,57%          | +58,96%      | ECCEZIONE POSITIVA      |
| INJ-USD         | 2023-11-13 | +88,99%      | +9,93%                   |              2 | -7,66%       |               8 | -16,00%          | +89,19%      | ECCEZIONE POSITIVA      |
| BTC-USD         | 2019-04-21 | +86,56%      | +4,85%                   |              2 | -1,96%       |               4 | -6,49%           | +49,84%      | ECCEZIONE POSITIVA      |
| QTUM-USD        | 2023-11-16 | +85,17%      | +3,34%                   |              4 | -5,87%       |               5 | -8,91%           | +3,09%       | ECCEZIONE POSITIVA      |
| 1INCH-USD       | 2023-11-23 | +87,81%      | +3,34%                   |              2 | -4,97%       |               7 | -8,04%           | +17,36%      | ECCEZIONE POSITIVA      |
| ZIL-USD         | 2023-11-23 | +84,88%      | +2,25%                   |              2 | -1,34%       |               4 | -3,51%           | +21,53%      | DISCESA QUASI IMMEDIATA |
| DOGE-USD        | 2019-04-21 | +85,36%      | +1,38%                   |              1 | -10,65%      |               8 | -11,87%          | +11,81%      | ECCEZIONE POSITIVA      |
| ZEC-USD         | 2019-04-21 | +86,28%      | +1,09%                   |              1 | -17,25%      |              18 | -18,15%          | +9,64%       | ECCEZIONE POSITIVA      |
| BCH-USD         | 2019-04-21 | +87,36%      | +0,80%                   |              1 | -18,54%      |               8 | -19,19%          | +43,74%      | ECCEZIONE POSITIVA      |
| ETC-USD         | 2019-04-21 | +83,88%      | +0,49%                   |              2 | -8,95%       |               4 | -9,40%           | +25,82%      | DISCESA QUASI IMMEDIATA |
| BNB-USD         | 2019-02-25 | +88,99%      | +0,00%                   |              0 | -3,26%       |               1 | -3,26%           | +70,51%      | DISCESA QUASI IMMEDIATA |
| THETA-USD       | 2023-11-25 | +88,16%      | +0,00%                   |              0 | -6,15%       |               2 | -6,15%           | +39,60%      | DISCESA QUASI IMMEDIATA |
| ADA-USD         | 2023-11-21 | +87,50%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +77,51%      | DISCESA QUASI IMMEDIATA |
| ETC-USD         | 2023-11-21 | +87,23%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +13,76%      | DISCESA QUASI IMMEDIATA |
| EGLD-USD        | 2023-11-21 | +87,13%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +55,32%      | DISCESA QUASI IMMEDIATA |
| XRP-USD         | 2023-11-21 | +86,62%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +7,49%       | DISCESA QUASI IMMEDIATA |
| MANA-USD        | 2023-11-21 | +86,28%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +37,82%      | DISCESA QUASI IMMEDIATA |
| ALGO-USD        | 2023-11-25 | +86,16%      | +0,00%                   |              0 | -6,07%       |               2 | -6,07%           | +69,64%      | DISCESA QUASI IMMEDIATA |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
