# Extreme cases path report

Generato: 2026-09-16 05:32 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +90,00%       | Casi positivi 90.00% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +65,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 90.00% >= 80%**
- Casi usati nei grafici: **36**
- Return mediano 7g: **+5,23%**
- Return mediano 14g: **+15,85%**
- Return mediano 30g: **+32,78%**
- Drawdown mediano: **-2,96%**
- Max gain mediano: **+43,28%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+0,62%**
- Spike p75 prima del minimo: **+0,00%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 2**
- Scarico mediano dal picco al minimo: **-3,10%**
- Casi con almeno +5% prima del minimo: **+2,78%**
- Casi con almeno +10% prima del minimo: **+0,00%**
- Casi con almeno +15% prima del minimo: **+0,00%**
- Discesa quasi immediata: **+83,33%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10     | P25     | P50     | P75     | P90     |
|:--------|:--------|:--------|:--------|:--------|
| +11,74% | +22,44% | +32,78% | +57,53% | +73,92% |

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
| LRC-USD         | 2020-06-24 | +84,90%      | +7,85%                   |              2 | -6,93%       |               5 | -13,71%          | +47,51%      | ECCEZIONE POSITIVA            |
| INJ-USD         | 2023-11-18 | +89,72%      | +4,94%                   |              1 | -10,45%      |               3 | -14,67%          | +131,17%     | RIALZO MODESTO PRIMA DEL DUMP |
| DASH-USD        | 2020-12-16 | +85,90%      | +4,49%                   |              4 | -17,00%      |              17 | -20,57%          | +18,83%      | RIALZO MODESTO PRIMA DEL DUMP |
| ZIL-USD         | 2023-11-23 | +86,33%      | +2,25%                   |              2 | -1,34%       |               4 | -3,51%           | +21,53%      | DISCESA QUASI IMMEDIATA       |
| ZEC-USD         | 2019-04-26 | +86,72%      | +2,04%                   |              7 | -7,96%       |              13 | -9,80%           | +23,44%      | ECCEZIONE POSITIVA            |
| DOGE-USD        | 2019-04-26 | +85,46%      | +0,48%                   |              2 | -2,10%       |               3 | -2,57%           | +22,75%      | DISCESA QUASI IMMEDIATA       |
| BTC-USD         | 2019-04-27 | +87,04%      | +0,32%                   |              1 | -0,40%       |               2 | -0,71%           | +67,15%      | DISCESA QUASI IMMEDIATA       |
| BCH-USD         | 2019-04-26 | +86,64%      | +0,02%                   |              1 | -10,33%      |               3 | -10,35%          | +64,03%      | DISCESA QUASI IMMEDIATA       |
| QTUM-USD        | 2023-11-21 | +90,03%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +14,24%      | DISCESA QUASI IMMEDIATA       |
| XLM-USD         | 2020-12-16 | +89,91%      | +0,00%                   |              0 | -33,92%      |               7 | -33,92%          | +48,87%      | ECCEZIONE POSITIVA            |
| THETA-USD       | 2023-11-30 | +88,74%      | +0,00%                   |              0 | -1,35%       |               1 | -1,35%           | +24,03%      | DISCESA QUASI IMMEDIATA       |
| XRP-USD         | 2023-11-26 | +88,74%      | +0,00%                   |              0 | -2,05%       |               1 | -2,05%           | +0,90%       | DISCESA QUASI IMMEDIATA       |
| 1INCH-USD       | 2023-11-28 | +88,32%      | +0,00%                   |              0 | -0,60%       |               2 | -0,60%           | +24,79%      | DISCESA QUASI IMMEDIATA       |
| MANA-USD        | 2023-11-26 | +87,16%      | +0,00%                   |              0 | -4,09%       |               4 | -4,09%           | +24,12%      | DISCESA QUASI IMMEDIATA       |
| ALGO-USD        | 2023-11-30 | +87,15%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +66,00%      | DISCESA QUASI IMMEDIATA       |
| BNB-USD         | 2019-03-02 | +87,13%      | +0,00%                   |              0 | -2,80%       |               1 | -2,80%           | +51,23%      | DISCESA QUASI IMMEDIATA       |
| EOS-USD         | 2023-11-26 | +87,12%      | +0,00%                   |              0 | -3,46%       |               1 | -3,46%           | +24,65%      | DISCESA QUASI IMMEDIATA       |
| EGLD-USD        | 2023-11-26 | +87,10%      | +0,00%                   |              0 | -3,88%       |               4 | -3,88%           | +57,64%      | DISCESA QUASI IMMEDIATA       |
| ETC-USD         | 2023-11-26 | +86,96%      | +0,00%                   |              0 | -2,88%       |               1 | -2,88%           | +8,94%       | DISCESA QUASI IMMEDIATA       |
| AVAX-USD        | 2021-09-13 | +86,57%      | +0,00%                   |              0 | -2,88%       |               1 | -2,88%           | +3,85%       | DISCESA QUASI IMMEDIATA       |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
