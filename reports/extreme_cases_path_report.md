# Extreme cases path report

Generato: 2026-08-05 05:14 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +80,00%       | Casi positivi 80.00% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +72,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +55,00%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 80.00% >= 80%**
- Casi usati nei grafici: **32**
- Return mediano 7g: **+3,29%**
- Return mediano 14g: **+7,02%**
- Return mediano 30g: **+12,86%**
- Drawdown mediano: **-3,25%**
- Max gain mediano: **+16,27%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+1,47%**
- Spike p75 prima del minimo: **+1,61%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 3**
- Scarico mediano dal picco al minimo: **-4,75%**
- Casi con almeno +5% prima del minimo: **+9,38%**
- Casi con almeno +10% prima del minimo: **+3,12%**
- Casi con almeno +15% prima del minimo: **+0,00%**
- Discesa quasi immediata: **+65,62%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25    | P50     | P75     | P90     |
|:-------|:-------|:--------|:--------|:--------|
| +4,45% | +9,46% | +12,86% | +23,13% | +49,39% |

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
| 1INCH-USD       | 2024-10-08 | +86,80%      | +14,18%                  |             12 | -10,73%      |              27 | -21,82%          | +3,24%       | SPIKE PRIMA DEL DUMP    |
| HBAR-USD        | 2020-11-08 | +85,08%      | +8,68%                   |              3 | -0,34%       |              11 | -8,29%           | +20,03%      | ECCEZIONE POSITIVA      |
| BNB-USD         | 2019-01-21 | +85,74%      | +8,17%                   |              6 | -5,78%       |               9 | -12,89%          | +67,34%      | ECCEZIONE POSITIVA      |
| NEO-USD         | 2026-04-09 | +85,53%      | +3,33%                   |              2 | -2,80%       |               3 | -5,94%           | +10,08%      | ECCEZIONE POSITIVA      |
| BTC-USD         | 2026-04-08 | +87,04%      | +2,71%                   |              3 | -0,52%       |               4 | -3,15%           | +12,74%      | DISCESA QUASI IMMEDIATA |
| NEO-USD         | 2019-01-21 | +86,93%      | +2,10%                   |              3 | -9,47%       |              16 | -11,34%          | +21,47%      | ECCEZIONE POSITIVA      |
| OMG-USD         | 2019-01-21 | +87,68%      | +1,65%                   |              1 | -19,94%      |              16 | -21,23%          | +4,30%       | ECCEZIONE POSITIVA      |
| MKR-USD         | 2020-05-16 | +86,49%      | +1,63%                   |              1 | -4,76%       |               5 | -6,29%           | +63,84%      | DISCESA QUASI IMMEDIATA |
| XTZ-USD         | 2026-04-09 | +87,41%      | +1,60%                   |              1 | -3,24%       |               3 | -4,76%           | +9,66%       | DISCESA QUASI IMMEDIATA |
| ETC-USD         | 2019-01-21 | +85,50%      | +1,18%                   |              4 | -12,63%      |              16 | -13,64%          | +9,27%       | ECCEZIONE POSITIVA      |
| BNB-USD         | 2026-04-09 | +87,66%      | +0,76%                   |              2 | -1,76%       |               3 | -2,50%           | +7,78%       | DISCESA QUASI IMMEDIATA |
| EGLD-USD        | 2024-06-13 | +85,14%      | +0,62%                   |              3 | -14,80%      |              10 | -15,32%          | +7,25%       | ECCEZIONE POSITIVA      |
| XTZ-USD         | 2019-01-21 | +87,01%      | +0,44%                   |              2 | -14,08%      |              17 | -14,45%          | +9,53%       | ECCEZIONE POSITIVA      |
| BTC-USD         | 2019-01-20 | +88,53%      | +0,10%                   |              2 | -5,60%       |              18 | -5,69%           | +9,61%       | ECCEZIONE POSITIVA      |
| XLM-USD         | 2020-11-06 | +89,87%      | +0,00%                   |              0 | -5,08%       |               1 | -5,08%           | +109,40%     | DISCESA QUASI IMMEDIATA |
| ETH-USD         | 2026-04-04 | +88,77%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +13,61%      | DISCESA QUASI IMMEDIATA |
| SAND-USD        | 2023-10-16 | +88,66%      | +0,00%                   |              0 | -3,59%       |               2 | -3,59%           | +50,41%      | DISCESA QUASI IMMEDIATA |
| DOGE-USD        | 2020-11-06 | +88,42%      | +0,00%                   |              0 | -3,26%       |               3 | -3,26%           | +22,75%      | DISCESA QUASI IMMEDIATA |
| FIL-USD         | 2023-10-21 | +88,29%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +40,20%      | DISCESA QUASI IMMEDIATA |
| ONE-USD         | 2020-05-10 | +88,00%      | +0,00%                   |              0 | -0,35%       |               1 | -0,35%           | +12,97%      | DISCESA QUASI IMMEDIATA |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
