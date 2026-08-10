# Extreme cases path report

Generato: 2026-08-10 05:15 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +82,50%       | Casi positivi 82.50% >= 80%      |                  40 |
| SOL     | POSITIVO / RIALZISTA | SI        | +80,00%       | Casi positivi 80.00% >= 80%      |                  40 |
| DOGE    | NESSUNO              | NO        | +72,50%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 82.50% >= 80%**
- Casi usati nei grafici: **33**
- Return mediano 7g: **+4,71%**
- Return mediano 14g: **+7,06%**
- Return mediano 30g: **+11,93%**
- Drawdown mediano: **-0,84%**
- Max gain mediano: **+19,92%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+1,64%**
- Spike p75 prima del minimo: **+2,04%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 3**
- Scarico mediano dal picco al minimo: **-2,46%**
- Casi con almeno +5% prima del minimo: **+9,09%**
- Casi con almeno +10% prima del minimo: **+3,03%**
- Casi con almeno +15% prima del minimo: **+0,00%**
- Discesa quasi immediata: **+60,61%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25    | P50     | P75     | P90     |
|:-------|:-------|:--------|:--------|:--------|
| +5,69% | +7,39% | +11,93% | +20,26% | +40,41% |

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
| 1INCH-USD       | 2024-10-13 | +86,78%      | +13,39%                  |              7 | -11,35%      |              22 | -21,82%          | +19,12%      | SPIKE PRIMA DEL DUMP          |
| NEO-USD         | 2026-04-14 | +85,00%      | +7,69%                   |              3 | -3,53%       |              16 | -10,41%          | +11,21%      | ECCEZIONE POSITIVA            |
| DOT-USD         | 2024-10-16 | +84,94%      | +5,91%                   |              4 | -13,19%      |              19 | -18,04%          | +19,09%      | RIALZO MODESTO PRIMA DEL DUMP |
| ALGO-USD        | 2020-05-19 | +86,56%      | +4,85%                   |              1 | -3,57%       |               2 | -8,04%           | +20,67%      | ECCEZIONE POSITIVA            |
| QTUM-USD        | 2020-05-15 | +85,41%      | +4,58%                   |              3 | -0,44%       |               6 | -4,80%           | +14,94%      | ECCEZIONE POSITIVA            |
| QTUM-USD        | 2026-04-09 | +84,86%      | +3,95%                   |              8 | -6,19%       |              21 | -9,75%           | +4,54%       | ECCEZIONE POSITIVA            |
| BTC-USD         | 2026-04-13 | +85,92%      | +3,55%                   |              4 | -0,84%       |               6 | -4,24%           | +6,43%       | ECCEZIONE POSITIVA            |
| LTC-USD         | 2020-05-14 | +85,48%      | +3,27%                   |              5 | -3,44%       |              12 | -6,50%           | +2,62%       | ECCEZIONE POSITIVA            |
| LTC-USD         | 2026-04-08 | +85,27%      | +2,04%                   |              3 | -0,89%       |               4 | -2,87%           | +7,90%       | DISCESA QUASI IMMEDIATA       |
| XLM-USD         | 2020-11-11 | +90,29%      | +2,02%                   |              2 | -0,49%       |               4 | -2,46%           | +87,35%      | DISCESA QUASI IMMEDIATA       |
| BNB-USD         | 2019-01-26 | +85,06%      | +1,17%                   |              1 | -11,88%      |               4 | -12,89%          | +40,47%      | DISCESA QUASI IMMEDIATA       |
| XRP-USD         | 2026-04-09 | +88,08%      | +0,93%                   |              1 | -1,42%       |               3 | -2,33%           | +5,65%       | DISCESA QUASI IMMEDIATA       |
| ETC-USD         | 2020-11-11 | +86,95%      | +0,83%                   |              2 | -1,22%       |               4 | -2,03%           | +14,00%      | DISCESA QUASI IMMEDIATA       |
| BTC-USD         | 2019-01-25 | +88,30%      | +0,07%                   |              1 | -5,56%       |              13 | -5,63%           | +5,85%       | ECCEZIONE POSITIVA            |
| XRP-USD         | 2023-10-22 | +90,31%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +11,10%      | DISCESA QUASI IMMEDIATA       |
| ETH-USD         | 2026-04-09 | +88,99%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +6,28%       | DISCESA QUASI IMMEDIATA       |
| SAND-USD        | 2023-10-21 | +88,28%      | +0,00%                   |              0 | -0,43%       |               1 | -0,43%           | +33,23%      | DISCESA QUASI IMMEDIATA       |
| DOGE-USD        | 2020-11-11 | +88,08%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +11,20%      | DISCESA QUASI IMMEDIATA       |
| LTC-USD         | 2023-10-21 | +88,05%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +7,39%       | DISCESA QUASI IMMEDIATA       |
| ETC-USD         | 2023-10-22 | +87,97%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +14,66%      | DISCESA QUASI IMMEDIATA       |

## SOL — casi rialzisti

- Trigger: **Casi positivi 80.00% >= 80%**
- Casi usati nei grafici: **32**
- Return mediano 7g: **+3,13%**
- Return mediano 14g: **+6,58%**
- Return mediano 30g: **+15,12%**
- Drawdown mediano: **-2,24%**
- Max gain mediano: **+26,01%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+1,80%**
- Spike p75 prima del minimo: **+3,82%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 4**
- Scarico mediano dal picco al minimo: **-5,72%**
- Casi con almeno +5% prima del minimo: **+15,62%**
- Casi con almeno +10% prima del minimo: **+0,00%**
- Casi con almeno +15% prima del minimo: **+0,00%**
- Discesa quasi immediata: **+62,50%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25    | P50     | P75     | P90     |
|:-------|:-------|:--------|:--------|:--------|
| +2,71% | +6,26% | +15,12% | +28,78% | +62,42% |

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

| Asset storico   | End        | Similarity   | Spike prima del minimo   |   Giorno spike | Minimo 30g   |   Giorno minimo | Dump dal picco   | Return 30g   | Sequenza                      |
|:----------------|:-----------|:-------------|:-------------------------|---------------:|:-------------|----------------:|:-----------------|:-------------|:------------------------------|
| DASH-USD        | 2020-05-15 | +79,89%      | +7,54%                   |              5 | -0,12%       |               9 | -7,13%           | +0,71%       | ECCEZIONE POSITIVA            |
| WAVES-USD       | 2024-08-22 | +75,74%      | +7,19%                   |              2 | -14,17%      |              15 | -19,92%          | +6,69%       | RIALZO MODESTO PRIMA DEL DUMP |
| BCH-USD         | 2020-05-15 | +77,85%      | +5,23%                   |              3 | -4,54%       |               9 | -9,28%           | +1,38%       | ECCEZIONE POSITIVA            |
| HBAR-USD        | 2026-04-06 | +75,43%      | +5,21%                   |              1 | -2,75%       |               8 | -7,56%           | +4,50%       | ECCEZIONE POSITIVA            |
| ZIL-USD         | 2020-11-08 | +79,78%      | +5,19%                   |              3 | -0,48%       |               4 | -5,39%           | +62,85%      | ECCEZIONE POSITIVA            |
| NEAR-USD        | 2026-04-09 | +80,16%      | +4,97%                   |              7 | -7,58%       |              25 | -11,95%          | +14,61%      | ECCEZIONE POSITIVA            |
| ALGO-USD        | 2020-05-19 | +77,87%      | +4,85%                   |              1 | -3,57%       |               2 | -8,04%           | +20,67%      | ECCEZIONE POSITIVA            |
| BAT-USD         | 2020-05-15 | +75,43%      | +4,63%                   |              3 | -2,00%       |               9 | -6,34%           | +12,37%      | ECCEZIONE POSITIVA            |
| BTC-USD         | 2026-04-13 | +76,42%      | +3,55%                   |              4 | -0,84%       |               6 | -4,24%           | +6,43%       | ECCEZIONE POSITIVA            |
| LTC-USD         | 2020-05-14 | +76,59%      | +3,27%                   |              5 | -3,44%       |              12 | -6,50%           | +2,62%       | ECCEZIONE POSITIVA            |
| VET-USD         | 2020-05-17 | +79,45%      | +2,24%                   |              3 | -3,96%       |               4 | -6,06%           | +104,48%     | DISCESA QUASI IMMEDIATA       |
| MKR-USD         | 2020-05-16 | +76,72%      | +1,63%                   |              1 | -4,76%       |               5 | -6,29%           | +63,84%      | DISCESA QUASI IMMEDIATA       |
| LINK-USD        | 2026-04-09 | +75,94%      | +1,62%                   |              1 | -2,30%       |               3 | -3,86%           | +15,98%      | DISCESA QUASI IMMEDIATA       |
| DOT-USD         | 2026-04-09 | +75,52%      | +0,43%                   |              1 | -10,35%      |               5 | -10,73%          | +3,56%       | DISCESA QUASI IMMEDIATA       |
| ENJ-USD         | 2019-01-26 | +85,23%      | +0,00%                   |              0 | -26,20%      |              11 | -26,20%          | +130,26%     | ECCEZIONE POSITIVA            |
| BNB-USD         | 2026-04-14 | +80,30%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +10,41%      | DISCESA QUASI IMMEDIATA       |
| RUNE-USD        | 2026-04-15 | +80,18%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +20,91%      | DISCESA QUASI IMMEDIATA       |
| EOS-USD         | 2019-02-05 | +80,17%      | +0,00%                   |              0 | -1,80%       |               2 | -1,80%           | +58,60%      | DISCESA QUASI IMMEDIATA       |
| QTUM-USD        | 2019-01-26 | +79,43%      | +0,00%                   |              0 | -15,73%      |              11 | -15,73%          | +1,74%       | ECCEZIONE POSITIVA            |
| SOL-USD         | 2026-04-12 | +79,24%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +15,64%      | DISCESA QUASI IMMEDIATA       |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
