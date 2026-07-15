# Extreme cases path report

Generato: 2026-07-15 07:26 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione             | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:----------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO               | NO        | +65,00%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO               | NO        | +55,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NEGATIVO / RIBASSISTA | SI        | +80,00%       | Casi negativi 80.00% >= 80%      |                  40 |

## DOGE — casi ribassisti

- Trigger: **Casi negativi 80.00% >= 80%**
- Casi usati nei grafici: **32**
- Return mediano 7g: **-14,81%**
- Return mediano 14g: **-23,05%**
- Return mediano 30g: **-20,94%**
- Drawdown mediano: **-28,98%**
- Max gain mediano: **+0,62%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,54%**
- Spike massimo medio prima del minimo: **+4,02%**
- Spike p75 prima del minimo: **+7,41%**
- Giorno mediano dello spike: **giorno 1**
- Giorno mediano del minimo: **giorno 13**
- Scarico mediano dal picco al minimo: **-32,77%**
- Casi con almeno +5% prima del minimo: **+28,12%**
- Casi con almeno +10% prima del minimo: **+15,62%**
- Casi con almeno +15% prima del minimo: **+6,25%**
- Discesa quasi immediata: **+3,12%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10     | P25     | P50     | P75     | P90    |
|:--------|:--------|:--------|:--------|:-------|
| -36,69% | -26,45% | -20,94% | -13,19% | -9,85% |

### Grafico pulito: bande + mediana

![Extreme clean DOGE](extreme_cases_DOGE_negative_clean_bands.png)

### Grafico asset per asset

![Extreme asset medians DOGE](extreme_cases_DOGE_negative_asset_medians.png)

### Spike massimo prima della discesa

La sigla `g7` sopra una barra significa che il massimo rialzo è avvenuto al giorno 7.

![Extreme spike before dump DOGE](extreme_cases_DOGE_negative_spike_before_dump.png)

### Spike iniziale contro minimo successivo

![Extreme spike vs low DOGE](extreme_cases_DOGE_negative_spike_vs_low.png)

### Casi ordinati per risultato finale

![Extreme ranked DOGE](extreme_cases_DOGE_negative_ranked_returns.png)

### Casi con spike maggiore prima del dump

| Asset storico   | End        | Similarity   | Spike prima del minimo   |   Giorno spike | Minimo 30g   |   Giorno minimo | Dump dal picco   | Return 30g   | Sequenza                      |
|:----------------|:-----------|:-------------|:-------------------------|---------------:|:-------------|----------------:|:-----------------|:-------------|:------------------------------|
| LINK-USD        | 2022-06-04 | +86,05%      | +25,42%                  |              5 | -20,40%      |               9 | -36,54%          | -13,04%      | SPIKE PRIMA DEL DUMP          |
| ZEC-USD         | 2019-08-29 | +88,48%      | +17,47%                  |             20 | -21,74%      |              28 | -33,38%          | -9,79%       | SPIKE PRIMA DEL DUMP          |
| ADA-USD         | 2022-06-04 | +85,50%      | +13,35%                  |              4 | -20,84%      |              27 | -30,16%          | -17,03%      | SPIKE PRIMA DEL DUMP          |
| OMG-USD         | 2022-06-04 | +87,67%      | +11,92%                  |              5 | -29,18%      |              14 | -36,72%          | -22,91%      | SPIKE PRIMA DEL DUMP          |
| RUNE-USD        | 2022-06-05 | +85,28%      | +10,76%                  |              1 | -44,40%      |              13 | -49,80%          | -25,64%      | SPIKE PRIMA DEL DUMP          |
| LTC-USD         | 2018-07-08 | +84,85%      | +8,99%                   |              9 | -17,27%      |              30 | -24,09%          | -17,27%      | SPIKE PRIMA DEL DUMP          |
| BAT-USD         | 2019-01-01 | +84,90%      | +7,93%                   |              8 | -13,95%      |              27 | -20,27%          | -13,42%      | RIALZO MODESTO PRIMA DEL DUMP |
| NEO-USD         | 2022-06-04 | +86,66%      | +7,71%                   |              2 | -27,58%      |              27 | -32,76%          | -23,84%      | RIALZO MODESTO PRIMA DEL DUMP |
| THETA-USD       | 2022-06-08 | +87,78%      | +7,31%                   |              1 | -17,72%      |               4 | -23,32%          | -6,39%       | RIALZO MODESTO PRIMA DEL DUMP |
| QTUM-USD        | 2022-06-04 | +88,04%      | +4,84%                   |              2 | -33,01%      |              14 | -36,10%          | -24,73%      | RIALZO MODESTO PRIMA DEL DUMP |
| XRP-USD         | 2022-06-04 | +86,29%      | +3,92%                   |              3 | -21,47%      |              14 | -24,43%          | -16,19%      | RIALZO MODESTO PRIMA DEL DUMP |
| ETC-USD         | 2022-06-04 | +85,41%      | +2,52%                   |              2 | -37,57%      |              14 | -39,10%          | -29,85%      | PERCORSO RIBASSISTA MISTO     |
| DASH-USD        | 2022-06-04 | +89,61%      | +2,36%                   |              2 | -29,01%      |              14 | -30,65%          | -24,48%      | PERCORSO RIBASSISTA MISTO     |
| WAVES-USD       | 2021-12-26 | +85,10%      | +1,67%                   |              1 | -48,10%      |              30 | -48,95%          | -48,10%      | PERCORSO RIBASSISTA MISTO     |
| DOT-USD         | 2022-06-04 | +86,25%      | +0,66%                   |              2 | -28,64%      |              27 | -29,10%          | -23,93%      | PERCORSO RIBASSISTA MISTO     |
| AVAX-USD        | 2025-11-26 | +86,89%      | +0,58%                   |              1 | -23,44%      |              22 | -23,89%          | -17,36%      | PERCORSO RIBASSISTA MISTO     |
| FIL-USD         | 2022-06-08 | +86,52%      | +0,50%                   |              1 | -28,94%      |              10 | -29,29%          | -20,21%      | PERCORSO RIBASSISTA MISTO     |
| KSM-USD         | 2024-05-12 | +84,95%      | +0,47%                   |              1 | -2,49%       |               2 | -2,95%           | -0,83%       | DISCESA QUASI IMMEDIATA       |
| VET-USD         | 2022-06-06 | +87,83%      | +0,17%                   |              3 | -31,87%      |              12 | -31,99%          | -25,78%      | PERCORSO RIBASSISTA MISTO     |
| INJ-USD         | 2022-06-06 | +87,81%      | +0,00%                   |              0 | -41,89%      |              25 | -41,89%          | -37,21%      | PERCORSO RIBASSISTA MISTO     |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
