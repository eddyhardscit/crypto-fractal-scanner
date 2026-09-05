# Extreme cases path report

Generato: 2026-09-05 08:21 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +82,50%       | Casi positivi 82.50% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +65,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 82.50% >= 80%**
- Casi usati nei grafici: **33**
- Return mediano 7g: **-1,94%**
- Return mediano 14g: **+0,85%**
- Return mediano 30g: **+16,43%**
- Drawdown mediano: **-10,70%**
- Max gain mediano: **+25,86%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+4,83%**
- Spike p75 prima del minimo: **+3,92%**
- Giorno mediano dello spike: **giorno 1**
- Giorno mediano del minimo: **giorno 5**
- Scarico mediano dal picco al minimo: **-11,60%**
- Casi con almeno +5% prima del minimo: **+18,18%**
- Casi con almeno +10% prima del minimo: **+3,03%**
- Casi con almeno +15% prima del minimo: **+3,03%**
- Discesa quasi immediata: **+57,58%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25     | P50     | P75     | P90     |
|:-------|:--------|:--------|:--------|:--------|
| +2,92% | +10,93% | +16,43% | +39,22% | +63,27% |

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
| UNI-USD         | 2023-07-10 | +83,61%      | +100,00%                 |             10 | -2,12%       |              14 | -51,06%          | +297,17%     | ECCEZIONE POSITIVA            |
| XLM-USD         | 2020-12-06 | +88,71%      | +8,98%                   |             10 | -27,99%      |              17 | -33,92%          | +10,93%      | SPIKE PRIMA DEL DUMP          |
| EGLD-USD        | 2023-11-16 | +84,04%      | +6,62%                   |              3 | -7,93%       |               5 | -13,65%          | +39,98%      | ECCEZIONE POSITIVA            |
| ADA-USD         | 2020-12-06 | +86,00%      | +5,49%                   |             10 | -14,15%      |              17 | -18,61%          | +62,60%      | RIALZO MODESTO PRIMA DEL DUMP |
| INJ-USD         | 2023-11-08 | +86,45%      | +5,31%                   |              2 | -15,83%      |              13 | -20,08%          | +13,46%      | RIALZO MODESTO PRIMA DEL DUMP |
| ETC-USD         | 2020-12-06 | +82,70%      | +5,13%                   |             11 | -17,56%      |              17 | -21,59%          | +17,65%      | RIALZO MODESTO PRIMA DEL DUMP |
| AVAX-USD        | 2021-09-03 | +83,01%      | +4,94%                   |              2 | -19,30%      |               5 | -23,10%          | +49,67%      | RIALZO MODESTO PRIMA DEL DUMP |
| 1INCH-USD       | 2023-11-18 | +87,96%      | +4,43%                   |              1 | -7,24%       |               3 | -11,18%          | +2,85%       | ECCEZIONE POSITIVA            |
| DOGE-USD        | 2019-04-16 | +83,53%      | +3,92%                   |              2 | -13,02%      |              13 | -16,29%          | +11,75%      | RIALZO MODESTO PRIMA DEL DUMP |
| ADA-USD         | 2023-11-16 | +84,70%      | +3,43%                   |              3 | -3,53%       |               5 | -6,73%           | +63,44%      | ECCEZIONE POSITIVA            |
| AVAX-USD        | 2023-11-22 | +82,86%      | +2,55%                   |              3 | -2,11%       |               5 | -4,54%           | +118,51%     | DISCESA QUASI IMMEDIATA       |
| XTZ-USD         | 2023-11-16 | +83,16%      | +2,51%                   |              3 | -8,26%       |               5 | -10,51%          | +12,21%      | DISCESA QUASI IMMEDIATA       |
| XRP-USD         | 2023-11-16 | +85,42%      | +2,50%                   |              3 | -5,18%       |               5 | -7,50%           | +1,25%       | DISCESA QUASI IMMEDIATA       |
| ETC-USD         | 2023-11-16 | +85,24%      | +1,67%                   |              3 | -5,91%       |               5 | -7,46%           | +7,43%       | DISCESA QUASI IMMEDIATA       |
| ZEC-USD         | 2019-04-16 | +84,48%      | +1,02%                   |              2 | -18,90%      |              23 | -19,72%          | +7,69%       | ECCEZIONE POSITIVA            |
| ZIL-USD         | 2023-11-18 | +85,76%      | +0,95%                   |              1 | -10,75%      |               3 | -11,60%          | +2,26%       | DISCESA QUASI IMMEDIATA       |
| MANA-USD        | 2023-11-16 | +84,95%      | +0,00%                   |              3 | -12,25%      |               5 | -12,26%          | +16,43%      | DISCESA QUASI IMMEDIATA       |
| THETA-USD       | 2023-11-20 | +87,81%      | +0,00%                   |              0 | -10,09%      |               1 | -10,09%          | +12,61%      | DISCESA QUASI IMMEDIATA       |
| BNB-USD         | 2019-02-20 | +86,70%      | +0,00%                   |              0 | -13,17%      |               6 | -13,17%          | +39,22%      | ECCEZIONE POSITIVA            |
| MATIC-USD       | 2023-11-21 | +85,73%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +11,56%      | DISCESA QUASI IMMEDIATA       |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
