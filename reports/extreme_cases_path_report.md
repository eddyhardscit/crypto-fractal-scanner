# Extreme cases path report

Generato: 2026-09-04 05:32 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +82,50%       | Casi positivi 82.50% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +67,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 82.50% >= 80%**
- Casi usati nei grafici: **33**
- Return mediano 7g: **-3,09%**
- Return mediano 14g: **-0,95%**
- Return mediano 30g: **+14,69%**
- Drawdown mediano: **-10,75%**
- Max gain mediano: **+25,52%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+1,67%**
- Spike massimo medio prima del minimo: **+5,55%**
- Spike p75 prima del minimo: **+4,48%**
- Giorno mediano dello spike: **giorno 2**
- Giorno mediano del minimo: **giorno 5**
- Scarico mediano dal picco al minimo: **-12,66%**
- Casi con almeno +5% prima del minimo: **+24,24%**
- Casi con almeno +10% prima del minimo: **+3,03%**
- Casi con almeno +15% prima del minimo: **+3,03%**
- Discesa quasi immediata: **+42,42%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25    | P50     | P75     | P90     |
|:-------|:-------|:--------|:--------|:--------|
| +2,37% | +8,57% | +14,69% | +37,56% | +99,95% |

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
| UNI-USD         | 2023-07-10 | +82,93%      | +100,00%                 |             10 | -2,12%       |              14 | -51,06%          | +297,17%     | ECCEZIONE POSITIVA            |
| VET-USD         | 2020-06-11 | +80,72%      | +9,75%                   |              1 | -6,61%       |               9 | -14,90%          | +109,07%     | ECCEZIONE POSITIVA            |
| XLM-USD         | 2020-12-06 | +89,37%      | +8,98%                   |             10 | -27,99%      |              17 | -33,92%          | +10,93%      | SPIKE PRIMA DEL DUMP          |
| LTC-USD         | 2019-02-19 | +82,64%      | +8,19%                   |              1 | -6,66%       |               5 | -13,72%          | +24,05%      | ECCEZIONE POSITIVA            |
| THETA-USD       | 2019-02-19 | +85,43%      | +7,84%                   |              4 | -3,49%       |               5 | -10,50%          | +29,98%      | ECCEZIONE POSITIVA            |
| EGLD-USD        | 2023-11-16 | +84,61%      | +6,62%                   |              3 | -7,93%       |               5 | -13,65%          | +39,98%      | ECCEZIONE POSITIVA            |
| ADA-USD         | 2020-12-06 | +84,00%      | +5,49%                   |             10 | -14,15%      |              17 | -18,61%          | +62,60%      | RIALZO MODESTO PRIMA DEL DUMP |
| INJ-USD         | 2023-11-08 | +84,00%      | +5,31%                   |              2 | -15,83%      |              13 | -20,08%          | +13,46%      | RIALZO MODESTO PRIMA DEL DUMP |
| BNB-USD         | 2023-11-16 | +83,08%      | +4,48%                   |              4 | -6,70%       |               5 | -10,70%          | +0,66%       | ECCEZIONE POSITIVA            |
| 1INCH-USD       | 2023-11-18 | +84,71%      | +4,43%                   |              1 | -7,24%       |               3 | -11,18%          | +2,85%       | ECCEZIONE POSITIVA            |
| DOGE-USD        | 2019-04-16 | +80,99%      | +3,92%                   |              2 | -13,02%      |              13 | -16,29%          | +11,75%      | RIALZO MODESTO PRIMA DEL DUMP |
| ADA-USD         | 2023-11-16 | +84,91%      | +3,43%                   |              3 | -3,53%       |               5 | -6,73%           | +63,44%      | ECCEZIONE POSITIVA            |
| AVAX-USD        | 2023-11-22 | +81,11%      | +2,55%                   |              3 | -2,11%       |               5 | -4,54%           | +118,51%     | DISCESA QUASI IMMEDIATA       |
| EOS-USD         | 2023-11-16 | +84,43%      | +2,53%                   |              3 | -7,84%       |               5 | -10,11%          | +14,14%      | DISCESA QUASI IMMEDIATA       |
| XTZ-USD         | 2023-11-16 | +85,70%      | +2,51%                   |              3 | -8,26%       |               5 | -10,51%          | +12,21%      | DISCESA QUASI IMMEDIATA       |
| XRP-USD         | 2023-11-16 | +88,31%      | +2,50%                   |              3 | -5,18%       |               5 | -7,50%           | +1,25%       | DISCESA QUASI IMMEDIATA       |
| ETC-USD         | 2023-11-16 | +86,05%      | +1,67%                   |              3 | -5,91%       |               5 | -7,46%           | +7,43%       | DISCESA QUASI IMMEDIATA       |
| THETA-USD       | 2023-11-15 | +86,09%      | +1,04%                   |              4 | -10,03%      |               6 | -10,95%          | +8,57%       | ECCEZIONE POSITIVA            |
| ZIL-USD         | 2023-11-18 | +82,71%      | +0,95%                   |              1 | -10,75%      |               3 | -11,60%          | +2,26%       | DISCESA QUASI IMMEDIATA       |
| MATIC-USD       | 2023-11-16 | +83,94%      | +0,79%                   |              3 | -13,46%      |               5 | -14,14%          | +0,40%       | DISCESA QUASI IMMEDIATA       |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
