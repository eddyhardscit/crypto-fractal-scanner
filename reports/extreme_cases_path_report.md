# Extreme cases path report

Generato: 2026-09-11 05:32 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +85,00%       | Casi positivi 85.00% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 85.00% >= 80%**
- Casi usati nei grafici: **34**
- Return mediano 7g: **+5,62%**
- Return mediano 14g: **+17,05%**
- Return mediano 30g: **+42,70%**
- Drawdown mediano: **-2,40%**
- Max gain mediano: **+44,13%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+2,89%**
- Spike p75 prima del minimo: **+2,03%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 2**
- Scarico mediano dal picco al minimo: **-3,38%**
- Casi con almeno +5% prima del minimo: **+14,71%**
- Casi con almeno +10% prima del minimo: **+8,82%**
- Casi con almeno +15% prima del minimo: **+8,82%**
- Discesa quasi immediata: **+64,71%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10     | P25     | P50     | P75     | P90     |
|:--------|:--------|:--------|:--------|:--------|
| +12,40% | +24,42% | +42,70% | +70,29% | +97,33% |

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
| XLM-USD         | 2020-12-11 | +90,01%      | +26,60%                  |              5 | -16,34%      |              12 | -33,92%          | +91,00%      | SPIKE PRIMA DEL DUMP    |
| ADA-USD         | 2020-12-11 | +86,68%      | +20,18%                  |              5 | -2,19%       |              12 | -18,61%          | +118,64%     | ECCEZIONE POSITIVA      |
| DASH-USD        | 2020-12-11 | +86,21%      | +17,30%                  |              9 | -6,83%       |              22 | -20,57%          | +58,96%      | ECCEZIONE POSITIVA      |
| INJ-USD         | 2023-11-13 | +88,54%      | +9,93%                   |              2 | -7,66%       |               8 | -16,00%          | +89,19%      | ECCEZIONE POSITIVA      |
| LRC-USD         | 2020-06-24 | +86,35%      | +7,85%                   |              2 | -6,93%       |               5 | -13,71%          | +47,51%      | ECCEZIONE POSITIVA      |
| QTUM-USD        | 2023-11-16 | +84,27%      | +3,34%                   |              4 | -5,87%       |               5 | -8,91%           | +3,09%       | ECCEZIONE POSITIVA      |
| 1INCH-USD       | 2023-11-23 | +88,86%      | +3,34%                   |              2 | -4,97%       |               7 | -8,04%           | +17,36%      | ECCEZIONE POSITIVA      |
| BTC-USD         | 2019-04-22 | +86,80%      | +3,20%                   |              1 | -3,50%       |               3 | -6,49%           | +42,24%      | ECCEZIONE POSITIVA      |
| ZIL-USD         | 2023-11-23 | +86,34%      | +2,25%                   |              2 | -1,34%       |               4 | -3,51%           | +21,53%      | DISCESA QUASI IMMEDIATA |
| DOGE-USD        | 2019-04-21 | +85,39%      | +1,38%                   |              1 | -10,65%      |               8 | -11,87%          | +11,81%      | ECCEZIONE POSITIVA      |
| ZEC-USD         | 2019-04-21 | +86,32%      | +1,09%                   |              1 | -17,25%      |              18 | -18,15%          | +9,64%       | ECCEZIONE POSITIVA      |
| DASH-USD        | 2019-04-21 | +84,71%      | +0,93%                   |              1 | -11,07%      |               8 | -11,89%          | +37,08%      | ECCEZIONE POSITIVA      |
| BCH-USD         | 2019-04-21 | +86,62%      | +0,80%                   |              1 | -18,54%      |               8 | -19,19%          | +43,74%      | ECCEZIONE POSITIVA      |
| THETA-USD       | 2023-11-25 | +88,98%      | +0,00%                   |              0 | -6,15%       |               2 | -6,15%           | +39,60%      | DISCESA QUASI IMMEDIATA |
| BNB-USD         | 2019-02-25 | +87,71%      | +0,00%                   |              0 | -3,26%       |               1 | -3,26%           | +70,51%      | DISCESA QUASI IMMEDIATA |
| ALGO-USD        | 2023-11-25 | +87,03%      | +0,00%                   |              0 | -6,07%       |               2 | -6,07%           | +69,64%      | DISCESA QUASI IMMEDIATA |
| MATIC-USD       | 2023-11-26 | +86,92%      | +0,00%                   |              0 | -2,61%       |               1 | -2,61%           | +33,08%      | DISCESA QUASI IMMEDIATA |
| ETC-USD         | 2023-11-21 | +86,38%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +13,76%      | DISCESA QUASI IMMEDIATA |
| ADA-USD         | 2023-11-21 | +86,31%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +77,51%      | DISCESA QUASI IMMEDIATA |
| AVAX-USD        | 2023-12-02 | +86,08%      | +0,00%                   |              0 | -1,22%       |               1 | -1,22%           | +88,23%      | DISCESA QUASI IMMEDIATA |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
