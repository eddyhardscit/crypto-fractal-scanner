# Extreme cases path report

Generato: 2026-08-07 05:15 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +82,50%       | Casi positivi 82.50% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +57,50%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 82.50% >= 80%**
- Casi usati nei grafici: **33**
- Return mediano 7g: **+5,43%**
- Return mediano 14g: **+6,50%**
- Return mediano 30g: **+12,55%**
- Drawdown mediano: **-3,24%**
- Max gain mediano: **+15,63%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+1,26%**
- Spike p75 prima del minimo: **+0,93%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 3**
- Scarico mediano dal picco al minimo: **-3,77%**
- Casi con almeno +5% prima del minimo: **+6,06%**
- Casi con almeno +10% prima del minimo: **+3,03%**
- Casi con almeno +15% prima del minimo: **+0,00%**
- Discesa quasi immediata: **+66,67%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25    | P50     | P75     | P90     |
|:-------|:-------|:--------|:--------|:--------|
| +4,25% | +6,73% | +12,55% | +22,75% | +53,14% |

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
| 1INCH-USD       | 2024-10-08 | +86,17%      | +14,18%                  |             12 | -10,73%      |              27 | -21,82%          | +3,24%       | SPIKE PRIMA DEL DUMP    |
| BNB-USD         | 2019-01-21 | +85,17%      | +8,17%                   |              6 | -5,78%       |               9 | -12,89%          | +67,34%      | ECCEZIONE POSITIVA      |
| QTUM-USD        | 2020-05-15 | +85,64%      | +4,58%                   |              3 | -0,44%       |               6 | -4,80%           | +14,94%      | ECCEZIONE POSITIVA      |
| QTUM-USD        | 2026-04-09 | +85,93%      | +3,95%                   |              8 | -6,19%       |              21 | -9,75%           | +4,54%       | ECCEZIONE POSITIVA      |
| LTC-USD         | 2026-04-05 | +85,48%      | +2,39%                   |              2 | -1,15%       |               7 | -3,46%           | +4,18%       | ECCEZIONE POSITIVA      |
| NEO-USD         | 2019-01-21 | +85,48%      | +2,10%                   |              3 | -9,47%       |              16 | -11,34%          | +21,47%      | ECCEZIONE POSITIVA      |
| MKR-USD         | 2020-05-16 | +88,37%      | +1,63%                   |              1 | -4,76%       |               5 | -6,29%           | +63,84%      | DISCESA QUASI IMMEDIATA |
| XTZ-USD         | 2026-04-09 | +86,21%      | +1,60%                   |              1 | -3,24%       |               3 | -4,76%           | +9,66%       | DISCESA QUASI IMMEDIATA |
| XRP-USD         | 2026-04-09 | +90,13%      | +0,93%                   |              1 | -1,42%       |               3 | -2,33%           | +5,65%       | DISCESA QUASI IMMEDIATA |
| BNB-USD         | 2026-04-09 | +87,23%      | +0,76%                   |              2 | -1,76%       |               3 | -2,50%           | +7,78%       | DISCESA QUASI IMMEDIATA |
| EGLD-USD        | 2024-06-13 | +85,51%      | +0,62%                   |              3 | -14,80%      |              10 | -15,32%          | +7,25%       | ECCEZIONE POSITIVA      |
| ETC-USD         | 2026-04-09 | +85,41%      | +0,61%                   |              1 | -3,70%       |               3 | -4,28%           | +13,50%      | DISCESA QUASI IMMEDIATA |
| BTC-USD         | 2026-04-10 | +86,48%      | +0,10%                   |              1 | -3,05%       |               2 | -3,15%           | +12,55%      | DISCESA QUASI IMMEDIATA |
| XLM-USD         | 2020-11-06 | +90,26%      | +0,00%                   |              0 | -5,08%       |               1 | -5,08%           | +109,40%     | DISCESA QUASI IMMEDIATA |
| FIL-USD         | 2023-10-21 | +89,59%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +40,20%      | DISCESA QUASI IMMEDIATA |
| SAND-USD        | 2023-10-21 | +89,45%      | +0,00%                   |              0 | -0,43%       |               1 | -0,43%           | +33,23%      | DISCESA QUASI IMMEDIATA |
| ETH-USD         | 2026-04-09 | +88,92%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +6,28%       | DISCESA QUASI IMMEDIATA |
| BTC-USD         | 2019-01-22 | +88,71%      | +0,00%                   |              0 | -5,69%       |              16 | -5,69%           | +9,70%       | ECCEZIONE POSITIVA      |
| DOGE-USD        | 2020-11-06 | +88,44%      | +0,00%                   |              0 | -3,26%       |               3 | -3,26%           | +22,75%      | DISCESA QUASI IMMEDIATA |
| LTC-USD         | 2023-10-18 | +87,69%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +16,43%      | DISCESA QUASI IMMEDIATA |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
