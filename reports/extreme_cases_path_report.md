# Extreme cases path report

Generato: 2026-09-07 05:32 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +85,00%       | Casi positivi 85.00% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +65,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 85.00% >= 80%**
- Casi usati nei grafici: **34**
- Return mediano 7g: **-0,66%**
- Return mediano 14g: **+6,92%**
- Return mediano 30g: **+21,64%**
- Drawdown mediano: **-8,26%**
- Max gain mediano: **+26,53%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+4,18%**
- Spike p75 prima del minimo: **+1,92%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 1**
- Scarico mediano dal picco al minimo: **-9,52%**
- Casi con almeno +5% prima del minimo: **+14,71%**
- Casi con almeno +10% prima del minimo: **+2,94%**
- Casi con almeno +15% prima del minimo: **+2,94%**
- Discesa quasi immediata: **+67,65%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25     | P50     | P75     | P90     |
|:-------|:--------|:--------|:--------|:--------|
| +7,55% | +12,82% | +21,64% | +39,40% | +75,41% |

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
| UNI-USD         | 2023-07-10 | +83,40%      | +100,00%                 |             10 | -2,12%       |              14 | -51,06%          | +297,17%     | ECCEZIONE POSITIVA            |
| XLM-USD         | 2020-12-06 | +86,68%      | +8,98%                   |             10 | -27,99%      |              17 | -33,92%          | +10,93%      | SPIKE PRIMA DEL DUMP          |
| ADA-USD         | 2020-12-06 | +85,43%      | +5,49%                   |             10 | -14,15%      |              17 | -18,61%          | +62,60%      | RIALZO MODESTO PRIMA DEL DUMP |
| INJ-USD         | 2023-11-08 | +86,59%      | +5,31%                   |              2 | -15,83%      |              13 | -20,08%          | +13,46%      | RIALZO MODESTO PRIMA DEL DUMP |
| BTC-USD         | 2019-04-18 | +83,35%      | +5,17%                   |              5 | -1,66%       |               7 | -6,49%           | +37,23%      | ECCEZIONE POSITIVA            |
| AVAX-USD        | 2021-09-03 | +84,12%      | +4,94%                   |              2 | -19,30%      |               5 | -23,10%          | +49,67%      | RIALZO MODESTO PRIMA DEL DUMP |
| 1INCH-USD       | 2023-11-18 | +88,24%      | +4,43%                   |              1 | -7,24%       |               3 | -11,18%          | +2,85%       | ECCEZIONE POSITIVA            |
| LTC-USD         | 2019-02-22 | +84,25%      | +3,77%                   |              1 | -10,29%      |               2 | -13,55%          | +20,92%      | RIALZO MODESTO PRIMA DEL DUMP |
| DASH-USD        | 2019-04-16 | +82,68%      | +2,21%                   |              2 | -11,06%      |              13 | -12,99%          | +22,36%      | ECCEZIONE POSITIVA            |
| ZEC-USD         | 2019-04-16 | +84,50%      | +1,02%                   |              2 | -18,90%      |              23 | -19,72%          | +7,69%       | ECCEZIONE POSITIVA            |
| ZIL-USD         | 2023-11-18 | +86,19%      | +0,95%                   |              1 | -10,75%      |               3 | -11,60%          | +2,26%       | DISCESA QUASI IMMEDIATA       |
| MANA-USD        | 2023-11-16 | +84,03%      | +0,00%                   |              3 | -12,25%      |               5 | -12,26%          | +16,43%      | DISCESA QUASI IMMEDIATA       |
| THETA-USD       | 2023-11-20 | +88,88%      | +0,00%                   |              0 | -10,09%      |               1 | -10,09%          | +12,61%      | DISCESA QUASI IMMEDIATA       |
| BNB-USD         | 2019-02-25 | +86,85%      | +0,00%                   |              0 | -3,26%       |               1 | -3,26%           | +70,51%      | DISCESA QUASI IMMEDIATA       |
| THETA-USD       | 2019-02-24 | +86,56%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +25,99%      | DISCESA QUASI IMMEDIATA       |
| MATIC-USD       | 2023-11-21 | +86,41%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +11,56%      | DISCESA QUASI IMMEDIATA       |
| ALGO-USD        | 2023-11-20 | +86,07%      | +0,00%                   |              0 | -12,15%      |               1 | -12,15%          | +39,80%      | DISCESA QUASI IMMEDIATA       |
| FIL-USD         | 2023-11-20 | +86,02%      | +0,00%                   |              0 | -9,91%       |               1 | -9,91%           | +13,56%      | DISCESA QUASI IMMEDIATA       |
| EGLD-USD        | 2023-11-21 | +85,59%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +55,32%      | DISCESA QUASI IMMEDIATA       |
| SAND-USD        | 2023-11-20 | +85,45%      | +0,00%                   |              0 | -10,70%      |               1 | -10,70%          | +25,39%      | DISCESA QUASI IMMEDIATA       |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
