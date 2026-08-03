# Extreme cases path report

Generato: 2026-08-03 05:14 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO              | NO        | +77,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | POSITIVO / RIALZISTA | SI        | +80,00%       | Casi positivi 80.00% >= 80%      |                  40 |
| DOGE    | NESSUNO              | NO        | +55,00%       | Nessun lato sopra soglia estrema |                  40 |

## SOL — casi rialzisti

- Trigger: **Casi positivi 80.00% >= 80%**
- Casi usati nei grafici: **32**
- Return mediano 7g: **+3,82%**
- Return mediano 14g: **+7,35%**
- Return mediano 30g: **+16,26%**
- Drawdown mediano: **-1,47%**
- Max gain mediano: **+20,16%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+1,21%**
- Spike p75 prima del minimo: **+1,76%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 1**
- Scarico mediano dal picco al minimo: **-2,80%**
- Casi con almeno +5% prima del minimo: **+6,25%**
- Casi con almeno +10% prima del minimo: **+0,00%**
- Casi con almeno +15% prima del minimo: **+0,00%**
- Discesa quasi immediata: **+71,88%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25    | P50     | P75     | P90     |
|:-------|:-------|:--------|:--------|:--------|
| +3,28% | +7,31% | +16,26% | +28,63% | +67,18% |

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
| BNB-USD         | 2019-01-21 | +75,50%      | +8,17%                   |              6 | -5,78%       |               9 | -12,89%          | +67,34%      | ECCEZIONE POSITIVA            |
| MKR-USD         | 2025-10-17 | +77,80%      | +5,66%                   |              8 | -8,23%       |              18 | -13,15%          | +2,18%       | ECCEZIONE POSITIVA            |
| RUNE-USD        | 2026-04-05 | +78,91%      | +4,71%                   |              2 | -0,37%       |               7 | -4,85%           | +41,91%      | ECCEZIONE POSITIVA            |
| ENJ-USD         | 2019-01-21 | +81,45%      | +4,11%                   |              3 | -25,10%      |              16 | -28,06%          | +11,62%      | RIALZO MODESTO PRIMA DEL DUMP |
| XRP-USD         | 2020-05-10 | +75,08%      | +3,53%                   |              8 | -2,12%       |              16 | -5,46%           | +1,94%       | ECCEZIONE POSITIVA            |
| ETH-USD         | 2019-01-31 | +74,55%      | +3,15%                   |              2 | -2,36%       |               7 | -5,34%           | +25,36%      | ECCEZIONE POSITIVA            |
| CRV-USD         | 2026-04-03 | +74,59%      | +2,41%                   |              1 | -0,51%       |               3 | -2,85%           | +11,57%      | DISCESA QUASI IMMEDIATA       |
| VET-USD         | 2023-10-14 | +76,26%      | +2,09%                   |              2 | -1,06%       |               4 | -3,09%           | +30,18%      | DISCESA QUASI IMMEDIATA       |
| OMG-USD         | 2019-01-21 | +75,51%      | +1,65%                   |              1 | -19,94%      |              16 | -21,23%          | +4,30%       | ECCEZIONE POSITIVA            |
| QTUM-USD        | 2019-01-21 | +79,84%      | +1,63%                   |              4 | -14,45%      |              16 | -15,82%          | +6,45%       | ECCEZIONE POSITIVA            |
| BCH-USD         | 2025-04-04 | +75,00%      | +0,86%                   |              1 | -10,72%      |               4 | -11,48%          | +18,22%      | DISCESA QUASI IMMEDIATA       |
| BNB-USD         | 2026-04-09 | +78,18%      | +0,76%                   |              2 | -1,76%       |               3 | -2,50%           | +7,78%       | DISCESA QUASI IMMEDIATA       |
| NEAR-USD        | 2026-04-04 | +80,96%      | +0,00%                   |              0 | -0,75%       |               1 | -0,75%           | +0,47%       | DISCESA QUASI IMMEDIATA       |
| ZIL-USD         | 2020-11-03 | +78,89%      | +0,00%                   |              0 | -0,09%       |               1 | -0,09%           | +93,69%      | DISCESA QUASI IMMEDIATA       |
| LINK-USD        | 2026-04-04 | +78,81%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +7,60%       | DISCESA QUASI IMMEDIATA       |
| EOS-USD         | 2019-01-31 | +78,51%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +51,66%      | DISCESA QUASI IMMEDIATA       |
| ONE-USD         | 2020-05-10 | +77,99%      | +0,00%                   |              0 | -0,35%       |               1 | -0,35%           | +12,97%      | DISCESA QUASI IMMEDIATA       |
| SOL-USD         | 2026-04-07 | +77,62%      | +0,00%                   |              0 | -4,80%       |               5 | -4,80%           | +3,22%       | DISCESA QUASI IMMEDIATA       |
| BTC-USD         | 2026-04-06 | +77,03%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +18,25%      | DISCESA QUASI IMMEDIATA       |
| KAVA-USD        | 2026-04-04 | +76,73%      | +0,00%                   |              0 | -2,75%       |               1 | -2,75%           | +24,96%      | DISCESA QUASI IMMEDIATA       |

## Come leggerlo

- **Grafico pulito**: mostra il percorso centrale.
- **Asset per asset**: mostra le differenze tra gli analoghi storici.
- **Spike prima della discesa**: risponde a quanto poteva salire prima di scendere.
- **Spike contro minimo**: mostra quanto rialzo iniziale è stato poi seguito da quale discesa.

Questo report è diagnostico e non modifica il Global Confluence.
