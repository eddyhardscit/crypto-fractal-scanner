# Extreme cases path report

Generato: 2026-08-09 05:15 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +85,00%       | Casi positivi 85.00% >= 80%      |                  40 |
| SOL     | POSITIVO / RIALZISTA | SI        | +80,00%       | Casi positivi 80.00% >= 80%      |                  40 |
| DOGE    | NESSUNO              | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 85.00% >= 80%**
- Casi usati nei grafici: **34**
- Return mediano 7g: **+5,33%**
- Return mediano 14g: **+8,90%**
- Return mediano 30g: **+14,04%**
- Drawdown mediano: **-0,86%**
- Max gain mediano: **+19,66%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+1,17%**
- Spike p75 prima del minimo: **+0,90%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 2**
- Scarico mediano dal picco al minimo: **-2,39%**
- Casi con almeno +5% prima del minimo: **+5,88%**
- Casi con almeno +10% prima del minimo: **+2,94%**
- Casi con almeno +15% prima del minimo: **+0,00%**
- Discesa quasi immediata: **+70,59%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25    | P50     | P75     | P90     |
|:-------|:-------|:--------|:--------|:--------|
| +4,64% | +8,14% | +14,04% | +17,34% | +30,56% |

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
| 1INCH-USD       | 2024-10-13 | +86,10%      | +13,39%                  |              7 | -11,35%      |              22 | -21,82%          | +19,12%      | SPIKE PRIMA DEL DUMP    |
| LTC-USD         | 2020-05-13 | +85,63%      | +5,21%                   |              6 | -1,63%       |              13 | -6,50%           | +3,93%       | ECCEZIONE POSITIVA      |
| ALGO-USD        | 2020-05-19 | +85,83%      | +4,85%                   |              1 | -3,57%       |               2 | -8,04%           | +20,67%      | ECCEZIONE POSITIVA      |
| QTUM-USD        | 2020-05-15 | +85,94%      | +4,58%                   |              3 | -0,44%       |               6 | -4,80%           | +14,94%      | ECCEZIONE POSITIVA      |
| QTUM-USD        | 2026-04-09 | +86,46%      | +3,95%                   |              8 | -6,19%       |              21 | -9,75%           | +4,54%       | ECCEZIONE POSITIVA      |
| XLM-USD         | 2020-11-11 | +88,86%      | +2,02%                   |              2 | -0,49%       |               4 | -2,46%           | +87,35%      | DISCESA QUASI IMMEDIATA |
| MKR-USD         | 2020-05-16 | +85,92%      | +1,63%                   |              1 | -4,76%       |               5 | -6,29%           | +63,84%      | DISCESA QUASI IMMEDIATA |
| LINK-USD        | 2026-04-09 | +85,40%      | +1,62%                   |              1 | -2,30%       |               3 | -3,86%           | +15,98%      | DISCESA QUASI IMMEDIATA |
| XRP-USD         | 2026-04-09 | +90,32%      | +0,93%                   |              1 | -1,42%       |               3 | -2,33%           | +5,65%       | DISCESA QUASI IMMEDIATA |
| ETC-USD         | 2020-11-11 | +87,05%      | +0,83%                   |              2 | -1,22%       |               4 | -2,03%           | +14,00%      | DISCESA QUASI IMMEDIATA |
| BNB-USD         | 2026-04-09 | +85,76%      | +0,76%                   |              2 | -1,76%       |               3 | -2,50%           | +7,78%       | DISCESA QUASI IMMEDIATA |
| BTC-USD         | 2019-01-24 | +88,46%      | +0,04%                   |              2 | -5,59%       |              14 | -5,63%           | +15,04%      | ECCEZIONE POSITIVA      |
| XRP-USD         | 2023-10-22 | +90,61%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +11,10%      | DISCESA QUASI IMMEDIATA |
| ETH-USD         | 2026-04-09 | +90,07%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +6,28%       | DISCESA QUASI IMMEDIATA |
| SAND-USD        | 2023-10-21 | +89,35%      | +0,00%                   |              0 | -0,43%       |               1 | -0,43%           | +33,23%      | DISCESA QUASI IMMEDIATA |
| OMG-USD         | 2019-01-26 | +88,49%      | +0,00%                   |              0 | -17,83%      |              11 | -17,83%          | +6,73%       | ECCEZIONE POSITIVA      |
| FIL-USD         | 2023-10-21 | +88,27%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +40,20%      | DISCESA QUASI IMMEDIATA |
| ETC-USD         | 2023-10-22 | +88,12%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +14,66%      | DISCESA QUASI IMMEDIATA |
| LTC-USD         | 2023-10-20 | +87,88%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +11,39%      | DISCESA QUASI IMMEDIATA |
| DOGE-USD        | 2020-11-11 | +87,47%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +11,20%      | DISCESA QUASI IMMEDIATA |

## SOL — casi rialzisti

- Trigger: **Casi positivi 80.00% >= 80%**
- Casi usati nei grafici: **32**
- Return mediano 7g: **+4,63%**
- Return mediano 14g: **+8,20%**
- Return mediano 30g: **+15,12%**
- Drawdown mediano: **-2,11%**
- Max gain mediano: **+24,84%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+1,86%**
- Spike p75 prima del minimo: **+1,78%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 2**
- Scarico mediano dal picco al minimo: **-4,62%**
- Casi con almeno +5% prima del minimo: **+15,62%**
- Casi con almeno +10% prima del minimo: **+3,12%**
- Casi con almeno +15% prima del minimo: **+3,12%**
- Discesa quasi immediata: **+68,75%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25    | P50     | P75     | P90     |
|:-------|:-------|:--------|:--------|:--------|
| +3,60% | +6,62% | +15,12% | +31,47% | +62,42% |

### Grafico pulito: bande + mediana

![Extreme clean SOL](extreme_cases_SOL_positive_clean_bands.png)

### Grafico asset per asset

![Extreme asset medians SOL](extreme_cases_SOL_positive_asset_medians.png)

### Spike massimo prima della discesa

La sigla `g7` sopra una barra significa che il massimo rialzo è avvenuto al giorno 7.

![Extreme spike before dump SOL](extreme_cases_SOL_positive_spike_before_dump.png)

### Spike iniziale contro minimo successivo

![Extreme spike vs low SOL](extreme_cases_SOL_positive_spike_vs_low.png)

### Casi ordinati per risultato finale

![Extreme ranked SOL](extreme_cases_SOL_positive_ranked_returns.png)

### Casi con spike maggiore prima del dump

| Asset storico   | End        | Similarity   | Spike prima del minimo   |   Giorno spike | Minimo 30g   |   Giorno minimo | Dump dal picco   | Return 30g   | Sequenza                |
|:----------------|:-----------|:-------------|:-------------------------|---------------:|:-------------|----------------:|:-----------------|:-------------|:------------------------|
| ICP-USD         | 2024-08-20 | +75,86%      | +19,46%                  |              4 | -3,64%       |              17 | -19,33%          | +10,97%      | ECCEZIONE POSITIVA      |
| DASH-USD        | 2020-05-15 | +77,64%      | +7,54%                   |              5 | -0,12%       |               9 | -7,13%           | +0,71%       | ECCEZIONE POSITIVA      |
| BCH-USD         | 2020-05-15 | +75,47%      | +5,23%                   |              3 | -4,54%       |               9 | -9,28%           | +1,38%       | ECCEZIONE POSITIVA      |
| LTC-USD         | 2020-05-13 | +76,14%      | +5,21%                   |              6 | -1,63%       |              13 | -6,50%           | +3,93%       | ECCEZIONE POSITIVA      |
| ZIL-USD         | 2020-11-08 | +81,25%      | +5,19%                   |              3 | -0,48%       |               4 | -5,39%           | +62,85%      | ECCEZIONE POSITIVA      |
| NEAR-USD        | 2026-04-09 | +81,53%      | +4,97%                   |              7 | -7,58%       |              25 | -11,95%          | +14,61%      | ECCEZIONE POSITIVA      |
| ALGO-USD        | 2020-05-19 | +77,22%      | +4,85%                   |              1 | -3,57%       |               2 | -8,04%           | +20,67%      | ECCEZIONE POSITIVA      |
| VET-USD         | 2020-05-17 | +77,81%      | +2,24%                   |              3 | -3,96%       |               4 | -6,06%           | +104,48%     | DISCESA QUASI IMMEDIATA |
| MKR-USD         | 2020-05-16 | +78,13%      | +1,63%                   |              1 | -4,76%       |               5 | -6,29%           | +63,84%      | DISCESA QUASI IMMEDIATA |
| LINK-USD        | 2026-04-09 | +78,15%      | +1,62%                   |              1 | -2,30%       |               3 | -3,86%           | +15,98%      | DISCESA QUASI IMMEDIATA |
| BNB-USD         | 2019-01-26 | +75,42%      | +1,17%                   |              1 | -11,88%      |               4 | -12,89%          | +40,47%      | DISCESA QUASI IMMEDIATA |
| DOT-USD         | 2026-04-09 | +77,19%      | +0,43%                   |              1 | -10,35%      |               5 | -10,73%          | +3,56%       | DISCESA QUASI IMMEDIATA |
| ENJ-USD         | 2019-01-26 | +84,86%      | +0,00%                   |              0 | -26,20%      |              11 | -26,20%          | +130,26%     | ECCEZIONE POSITIVA      |
| EOS-USD         | 2019-02-05 | +80,68%      | +0,00%                   |              0 | -1,80%       |               2 | -1,80%           | +58,60%      | DISCESA QUASI IMMEDIATA |
| QTUM-USD        | 2019-01-26 | +80,14%      | +0,00%                   |              0 | -15,73%      |              11 | -15,73%          | +1,74%       | ECCEZIONE POSITIVA      |
| RUNE-USD        | 2026-04-15 | +79,49%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +20,91%      | DISCESA QUASI IMMEDIATA |
| BNB-USD         | 2026-04-14 | +79,39%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +10,41%      | DISCESA QUASI IMMEDIATA |
| SOL-USD         | 2026-04-12 | +78,36%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +15,64%      | DISCESA QUASI IMMEDIATA |
| BNB-USD         | 2020-05-15 | +78,31%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +5,72%       | DISCESA QUASI IMMEDIATA |
| ZEC-USD         | 2023-10-22 | +77,84%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +4,13%       | DISCESA QUASI IMMEDIATA |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
