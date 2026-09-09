# Extreme cases path report

Generato: 2026-09-09 05:32 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +80,00%       | Casi positivi 80.00% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 80.00% >= 80%**
- Casi usati nei grafici: **32**
- Return mediano 7g: **+3,17%**
- Return mediano 14g: **+10,14%**
- Return mediano 30g: **+31,31%**
- Drawdown mediano: **-2,82%**
- Max gain mediano: **+37,56%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+2,37%**
- Spike p75 prima del minimo: **+1,16%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 1**
- Scarico mediano dal picco al minimo: **-7,27%**
- Casi con almeno +5% prima del minimo: **+9,38%**
- Casi con almeno +10% prima del minimo: **+6,25%**
- Casi con almeno +15% prima del minimo: **+6,25%**
- Discesa quasi immediata: **+65,62%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25     | P50     | P75     | P90     |
|:-------|:--------|:--------|:--------|:--------|
| +9,83% | +13,71% | +31,31% | +49,52% | +88,02% |

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
| XLM-USD         | 2020-12-11 | +90,70%      | +26,60%                  |              5 | -16,34%      |              12 | -33,92%          | +91,00%      | SPIKE PRIMA DEL DUMP          |
| ADA-USD         | 2020-12-11 | +84,64%      | +20,18%                  |              5 | -2,19%       |              12 | -18,61%          | +118,64%     | ECCEZIONE POSITIVA            |
| INJ-USD         | 2023-11-13 | +88,46%      | +9,93%                   |              2 | -7,66%       |               8 | -16,00%          | +89,19%      | ECCEZIONE POSITIVA            |
| AVAX-USD        | 2021-09-03 | +83,83%      | +4,94%                   |              2 | -19,30%      |               5 | -23,10%          | +49,67%      | RIALZO MODESTO PRIMA DEL DUMP |
| BTC-USD         | 2019-04-20 | +85,70%      | +4,39%                   |              3 | -2,39%       |               5 | -6,49%           | +49,47%      | ECCEZIONE POSITIVA            |
| QTUM-USD        | 2023-11-16 | +84,64%      | +3,34%                   |              4 | -5,87%       |               5 | -8,91%           | +3,09%       | ECCEZIONE POSITIVA            |
| 1INCH-USD       | 2023-11-23 | +85,90%      | +3,34%                   |              2 | -4,97%       |               7 | -8,04%           | +17,36%      | ECCEZIONE POSITIVA            |
| DOGE-USD        | 2019-04-21 | +83,62%      | +1,38%                   |              1 | -10,65%      |               8 | -11,87%          | +11,81%      | ECCEZIONE POSITIVA            |
| ZEC-USD         | 2019-04-21 | +83,49%      | +1,09%                   |              1 | -17,25%      |              18 | -18,15%          | +9,64%       | ECCEZIONE POSITIVA            |
| BCH-USD         | 2019-04-21 | +85,88%      | +0,80%                   |              1 | -18,54%      |               8 | -19,19%          | +43,74%      | ECCEZIONE POSITIVA            |
| BNB-USD         | 2019-02-25 | +89,55%      | +0,00%                   |              0 | -3,26%       |               1 | -3,26%           | +70,51%      | DISCESA QUASI IMMEDIATA       |
| THETA-USD       | 2023-11-20 | +88,07%      | +0,00%                   |              0 | -10,09%      |               1 | -10,09%          | +12,61%      | DISCESA QUASI IMMEDIATA       |
| ADA-USD         | 2023-11-21 | +87,40%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +77,51%      | DISCESA QUASI IMMEDIATA       |
| ETC-USD         | 2023-11-21 | +86,97%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +13,76%      | DISCESA QUASI IMMEDIATA       |
| EGLD-USD        | 2023-11-21 | +86,89%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +55,32%      | DISCESA QUASI IMMEDIATA       |
| THETA-USD       | 2019-02-24 | +86,85%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +25,99%      | DISCESA QUASI IMMEDIATA       |
| XRP-USD         | 2023-11-21 | +86,35%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +7,49%       | DISCESA QUASI IMMEDIATA       |
| ALGO-USD        | 2023-11-20 | +86,15%      | +0,00%                   |              0 | -12,15%      |               1 | -12,15%          | +39,80%      | DISCESA QUASI IMMEDIATA       |
| XTZ-USD         | 2023-11-21 | +86,05%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +20,77%      | DISCESA QUASI IMMEDIATA       |
| EOS-USD         | 2023-11-21 | +85,62%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +29,79%      | DISCESA QUASI IMMEDIATA       |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
