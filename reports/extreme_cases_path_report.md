# Extreme cases path report

Generato: 2026-07-13 06:27 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione             | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:----------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO               | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO               | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NEGATIVO / RIBASSISTA | SI        | +82,50%       | Casi negativi 82.50% >= 80%      |                  40 |

## DOGE — casi ribassisti

- Trigger: **Casi negativi 82.50% >= 80%**
- Casi usati nei grafici: **33**
- Return mediano 7g: **-9,62%**
- Return mediano 14g: **-25,16%**
- Return mediano 30g: **-21,97%**
- Drawdown mediano: **-28,94%**
- Max gain mediano: **+3,20%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+3,20%**
- Spike massimo medio prima del minimo: **+5,61%**
- Spike p75 prima del minimo: **+7,55%**
- Giorno mediano dello spike: **giorno 2**
- Giorno mediano del minimo: **giorno 14**
- Scarico mediano dal picco al minimo: **-31,99%**
- Casi con almeno +5% prima del minimo: **+36,36%**
- Casi con almeno +10% prima del minimo: **+21,21%**
- Casi con almeno +15% prima del minimo: **+9,09%**
- Discesa quasi immediata: **+3,03%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10     | P25     | P50     | P75     | P90    |
|:--------|:--------|:--------|:--------|:-------|
| -31,26% | -25,78% | -21,97% | -13,04% | -7,07% |

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
| WAVES-USD       | 2022-05-30 | +85,21%      | +28,83%                  |              4 | -42,96%      |              17 | -55,72%          | -29,04%      | SPIKE PRIMA DEL DUMP          |
| LINK-USD        | 2022-06-04 | +84,91%      | +25,42%                  |              5 | -20,40%      |               9 | -36,54%          | -13,04%      | SPIKE PRIMA DEL DUMP          |
| ZEC-USD         | 2019-08-29 | +88,27%      | +17,47%                  |             20 | -21,74%      |              28 | -33,38%          | -9,79%       | SPIKE PRIMA DEL DUMP          |
| ADA-USD         | 2022-06-04 | +85,68%      | +13,35%                  |              4 | -20,84%      |              27 | -30,16%          | -17,03%      | SPIKE PRIMA DEL DUMP          |
| AVAX-USD        | 2025-11-21 | +86,64%      | +12,94%                  |              6 | -14,04%      |              27 | -23,89%          | -8,75%       | SPIKE PRIMA DEL DUMP          |
| OMG-USD         | 2022-06-04 | +87,58%      | +11,92%                  |              5 | -29,18%      |              14 | -36,72%          | -22,91%      | SPIKE PRIMA DEL DUMP          |
| RUNE-USD        | 2022-06-05 | +84,34%      | +10,76%                  |              1 | -44,40%      |              13 | -49,80%          | -25,64%      | SPIKE PRIMA DEL DUMP          |
| BAT-USD         | 2019-01-01 | +85,61%      | +7,93%                   |              8 | -13,95%      |              27 | -20,27%          | -13,42%      | RIALZO MODESTO PRIMA DEL DUMP |
| AVAX-USD        | 2022-06-05 | +85,64%      | +7,55%                   |              1 | -38,58%      |              13 | -42,89%          | -25,24%      | RIALZO MODESTO PRIMA DEL DUMP |
| THETA-USD       | 2022-06-08 | +85,66%      | +7,31%                   |              1 | -17,72%      |               4 | -23,32%          | -6,39%       | RIALZO MODESTO PRIMA DEL DUMP |
| CHZ-USD         | 2022-06-03 | +86,11%      | +5,97%                   |              3 | -28,71%      |              15 | -32,73%          | -19,17%      | RIALZO MODESTO PRIMA DEL DUMP |
| ENJ-USD         | 2022-06-04 | +86,46%      | +5,00%                   |              2 | -33,46%      |              14 | -36,63%          | -16,55%      | RIALZO MODESTO PRIMA DEL DUMP |
| QTUM-USD        | 2022-06-04 | +87,25%      | +4,84%                   |              2 | -33,01%      |              14 | -36,10%          | -24,73%      | RIALZO MODESTO PRIMA DEL DUMP |
| XTZ-USD         | 2026-03-15 | +86,24%      | +4,26%                   |              5 | -12,14%      |              14 | -15,73%          | -10,41%      | RIALZO MODESTO PRIMA DEL DUMP |
| NEO-USD         | 2022-05-30 | +84,51%      | +3,34%                   |              7 | -27,65%      |              19 | -29,99%          | -26,97%      | RIALZO MODESTO PRIMA DEL DUMP |
| INJ-USD         | 2022-06-01 | +86,64%      | +3,20%                   |              1 | -42,93%      |              30 | -44,70%          | -42,93%      | RIALZO MODESTO PRIMA DEL DUMP |
| ETH-USD         | 2022-06-04 | +86,27%      | +3,20%                   |              2 | -44,85%      |              14 | -46,56%          | -36,11%      | RIALZO MODESTO PRIMA DEL DUMP |
| ICP-USD         | 2023-06-27 | +84,58%      | +3,15%                   |              6 | -7,38%       |              27 | -10,21%          | -2,56%       | PERCORSO RIBASSISTA MISTO     |
| ETC-USD         | 2022-06-04 | +84,07%      | +2,52%                   |              2 | -37,57%      |              14 | -39,10%          | -29,85%      | PERCORSO RIBASSISTA MISTO     |
| DASH-USD        | 2022-06-04 | +87,60%      | +2,36%                   |              2 | -29,01%      |              14 | -30,65%          | -24,48%      | PERCORSO RIBASSISTA MISTO     |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
