# Extreme cases path report

Generato: 2026-09-13 05:32 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +85,00%       | Casi positivi 85.00% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +67,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +75,00%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 85.00% >= 80%**
- Casi usati nei grafici: **34**
- Return mediano 7g: **+3,86%**
- Return mediano 14g: **+16,22%**
- Return mediano 30g: **+40,47%**
- Drawdown mediano: **-3,67%**
- Max gain mediano: **+42,24%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+1,70%**
- Spike p75 prima del minimo: **+0,02%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 2**
- Scarico mediano dal picco al minimo: **-3,99%**
- Casi con almeno +5% prima del minimo: **+8,82%**
- Casi con almeno +10% prima del minimo: **+5,88%**
- Casi con almeno +15% prima del minimo: **+5,88%**
- Discesa quasi immediata: **+76,47%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10     | P25     | P50     | P75     | P90     |
|:--------|:--------|:--------|:--------|:--------|
| +15,04% | +22,22% | +40,47% | +58,63% | +82,65% |

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
| ADA-USD         | 2020-12-11 | +86,29%      | +20,18%                  |              5 | -2,19%       |              12 | -18,61%          | +118,64%     | ECCEZIONE POSITIVA            |
| DASH-USD        | 2020-12-11 | +87,46%      | +17,30%                  |              9 | -6,83%       |              22 | -20,57%          | +58,96%      | ECCEZIONE POSITIVA            |
| LRC-USD         | 2020-06-24 | +86,20%      | +7,85%                   |              2 | -6,93%       |               5 | -13,71%          | +47,51%      | ECCEZIONE POSITIVA            |
| INJ-USD         | 2023-11-18 | +88,80%      | +4,94%                   |              1 | -10,45%      |               3 | -14,67%          | +131,17%     | RIALZO MODESTO PRIMA DEL DUMP |
| 1INCH-USD       | 2023-11-23 | +88,90%      | +3,34%                   |              2 | -4,97%       |               7 | -8,04%           | +17,36%      | ECCEZIONE POSITIVA            |
| ZIL-USD         | 2023-11-23 | +87,22%      | +2,25%                   |              2 | -1,34%       |               4 | -3,51%           | +21,53%      | DISCESA QUASI IMMEDIATA       |
| ZEC-USD         | 2019-04-21 | +85,13%      | +1,09%                   |              1 | -17,25%      |              18 | -18,15%          | +9,64%       | ECCEZIONE POSITIVA            |
| DASH-USD        | 2019-04-21 | +85,36%      | +0,93%                   |              1 | -11,07%      |               8 | -11,89%          | +37,08%      | ECCEZIONE POSITIVA            |
| BCH-USD         | 2019-04-26 | +85,36%      | +0,02%                   |              1 | -10,33%      |               3 | -10,35%          | +64,03%      | DISCESA QUASI IMMEDIATA       |
| XLM-USD         | 2020-12-16 | +90,51%      | +0,00%                   |              0 | -33,92%      |               7 | -33,92%          | +48,87%      | ECCEZIONE POSITIVA            |
| THETA-USD       | 2023-11-25 | +88,91%      | +0,00%                   |              0 | -6,15%       |               2 | -6,15%           | +39,60%      | DISCESA QUASI IMMEDIATA       |
| BNB-USD         | 2019-03-02 | +88,78%      | +0,00%                   |              0 | -2,80%       |               1 | -2,80%           | +51,23%      | DISCESA QUASI IMMEDIATA       |
| ALGO-USD        | 2023-11-25 | +87,84%      | +0,00%                   |              0 | -6,07%       |               2 | -6,07%           | +69,64%      | DISCESA QUASI IMMEDIATA       |
| EGLD-USD        | 2023-11-26 | +87,14%      | +0,00%                   |              0 | -3,88%       |               4 | -3,88%           | +57,64%      | DISCESA QUASI IMMEDIATA       |
| ADA-USD         | 2023-11-26 | +86,98%      | +0,00%                   |              0 | -3,17%       |               4 | -3,17%           | +56,83%      | DISCESA QUASI IMMEDIATA       |
| MATIC-USD       | 2023-11-26 | +86,89%      | +0,00%                   |              0 | -2,61%       |               1 | -2,61%           | +33,08%      | DISCESA QUASI IMMEDIATA       |
| BTC-USD         | 2019-04-24 | +86,86%      | +0,00%                   |              0 | -4,65%       |               1 | -4,65%           | +46,16%      | DISCESA QUASI IMMEDIATA       |
| ETC-USD         | 2023-11-26 | +86,83%      | +0,00%                   |              0 | -2,88%       |               1 | -2,88%           | +8,94%       | DISCESA QUASI IMMEDIATA       |
| QTUM-USD        | 2023-11-21 | +86,57%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +14,24%      | DISCESA QUASI IMMEDIATA       |
| EOS-USD         | 2023-11-26 | +86,40%      | +0,00%                   |              0 | -3,46%       |               1 | -3,46%           | +24,65%      | DISCESA QUASI IMMEDIATA       |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
