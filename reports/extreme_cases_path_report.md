# Extreme cases path report

Generato: 2026-08-04 05:16 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +80,00%       | Casi positivi 80.00% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +72,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +57,50%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 80.00% >= 80%**
- Casi usati nei grafici: **32**
- Return mediano 7g: **+4,33%**
- Return mediano 14g: **+8,24%**
- Return mediano 30g: **+14,80%**
- Drawdown mediano: **-2,63%**
- Max gain mediano: **+25,65%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+1,06%**
- Spike p75 prima del minimo: **+0,65%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 2**
- Scarico mediano dal picco al minimo: **-3,21%**
- Casi con almeno +5% prima del minimo: **+6,25%**
- Casi con almeno +10% prima del minimo: **+3,12%**
- Casi con almeno +15% prima del minimo: **+0,00%**
- Discesa quasi immediata: **+71,88%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25    | P50     | P75     | P90     |
|:-------|:-------|:--------|:--------|:--------|
| +5,10% | +9,63% | +14,80% | +29,21% | +62,71% |

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
| 1INCH-USD       | 2024-10-08 | +85,91%      | +14,18%                  |             12 | -10,73%      |              27 | -21,82%          | +3,24%       | SPIKE PRIMA DEL DUMP    |
| BNB-USD         | 2019-01-21 | +85,42%      | +8,17%                   |              6 | -5,78%       |               9 | -12,89%          | +67,34%      | ECCEZIONE POSITIVA      |
| LTC-USD         | 2023-10-15 | +87,79%      | +2,73%                   |              1 | -2,24%       |               3 | -4,83%           | +14,56%      | DISCESA QUASI IMMEDIATA |
| NEO-USD         | 2019-01-21 | +86,38%      | +2,10%                   |              3 | -9,47%       |              16 | -11,34%          | +21,47%      | ECCEZIONE POSITIVA      |
| OMG-USD         | 2019-01-21 | +87,71%      | +1,65%                   |              1 | -19,94%      |              16 | -21,23%          | +4,30%       | ECCEZIONE POSITIVA      |
| XTZ-USD         | 2026-04-09 | +86,60%      | +1,60%                   |              1 | -3,24%       |               3 | -4,76%           | +9,66%       | DISCESA QUASI IMMEDIATA |
| BTC-USD         | 2026-04-07 | +87,03%      | +1,55%                   |              4 | -1,65%       |               5 | -3,15%           | +11,22%      | DISCESA QUASI IMMEDIATA |
| BNB-USD         | 2026-04-09 | +85,99%      | +0,76%                   |              2 | -1,76%       |               3 | -2,50%           | +7,78%       | DISCESA QUASI IMMEDIATA |
| EGLD-USD        | 2024-06-13 | +85,35%      | +0,62%                   |              3 | -14,80%      |              10 | -15,32%          | +7,25%       | ECCEZIONE POSITIVA      |
| XTZ-USD         | 2019-01-21 | +87,22%      | +0,44%                   |              2 | -14,08%      |              17 | -14,45%          | +9,53%       | ECCEZIONE POSITIVA      |
| XRP-USD         | 2026-04-04 | +89,63%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +5,81%       | DISCESA QUASI IMMEDIATA |
| ETH-USD         | 2026-04-04 | +89,60%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +13,61%      | DISCESA QUASI IMMEDIATA |
| SAND-USD        | 2023-10-16 | +89,15%      | +0,00%                   |              0 | -3,59%       |               2 | -3,59%           | +50,41%      | DISCESA QUASI IMMEDIATA |
| ONE-USD         | 2020-05-10 | +88,68%      | +0,00%                   |              0 | -0,35%       |               1 | -0,35%           | +12,97%      | DISCESA QUASI IMMEDIATA |
| FIL-USD         | 2023-10-16 | +88,35%      | +0,00%                   |              0 | -2,44%       |               2 | -2,44%           | +60,53%      | DISCESA QUASI IMMEDIATA |
| BTC-USD         | 2019-01-19 | +88,14%      | +0,00%                   |              0 | -8,83%       |              19 | -8,83%           | +5,02%       | ECCEZIONE POSITIVA      |
| XLM-USD         | 2020-11-06 | +88,10%      | +0,00%                   |              0 | -5,08%       |               1 | -5,08%           | +109,40%     | DISCESA QUASI IMMEDIATA |
| DOGE-USD        | 2020-11-06 | +87,91%      | +0,00%                   |              0 | -3,26%       |               3 | -3,26%           | +22,75%      | DISCESA QUASI IMMEDIATA |
| ETC-USD         | 2023-10-17 | +87,59%      | +0,00%                   |              0 | -1,01%       |               2 | -1,01%           | +28,95%      | DISCESA QUASI IMMEDIATA |
| XRP-USD         | 2020-01-26 | +87,22%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +9,85%       | DISCESA QUASI IMMEDIATA |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
