# Calibrazione rischio spot / leva

Generato: **2026-08-22 05:32 UTC**

Questo report controlla se le zone di rischio previste dallo scanner vengono davvero toccate nei 30 giorni successivi.

L'obiettivo è separare meglio:

- rischio spot
- rischio leva
- rischio drawdown
- rischio di liquidazione

Questo file **non modifica ancora il Decision Report**. Per ora salva dati e misura. Le correzioni automatiche verranno considerate solo dopo abbastanza controlli.

## Regola prudente

- Sotto **30** controlli: solo raccolta dati.
- Da **30** a **59** controlli: osservazione, senza modificare il modello.
- Da **60** a **99** controlli: può suggerire correzioni leggere.
- Da **100+** controlli: può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rischio salvata

| Asset   | Prezzo    | Direzione scanner                    | Drawdown normale   | Drawdown brutto     | Max gain normale   | Rischio spot   | Rischio leva   |
|:--------|:----------|:-------------------------------------|:-------------------|:--------------------|:-------------------|:---------------|:---------------|
| BTC     | 239,39 $  | Direzione più probabile a 30 giorni: | 660,38 $ / -7,22%  | 445,04 $ / -12,68%  | 834,51 $ / 17,60%  | MEDIO          | ALTO           |
| SOL     | 93,70 $   | Direzione più probabile a 30 giorni: | 84,94 $ / -9,35%   | 81,84 $ / -12,65%   | 104,29 $ / 11,30%  | MEDIO          | MOLTO ALTO     |
| DOGE    | 0.09000 $ | Direzione più probabile a 30 giorni: | 0.08000 $ / -8,71% | 0.07000 $ / -17,46% | 0.11000 $ / 18,73% | MEDIO          | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         43 |              15 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         43 |              15 |          28 | RACCOLTA DATI | 6,67%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         43 |              15 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-07-23        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09976 $   | -2,90%           | 42,51%           | RISCHIO STIMATO SEVERO |
| 2026-07-23        | SOL     | 77,11 $           | 70,69 $     | 101,65 $    | -8,32%           | 31,82%           | RISCHIO STIMATO SEVERO |
| 2026-07-23        | BTC     | 399,99 $          | 62.226,58 $ | 78.767,34 $ | 15457,03%        | 19592,33%        | RISCHIO STIMATO SEVERO |
| 2026-07-22        | DOGE    | 0.07000 $         | 0.06797 $   | 0.08268 $   | -2,90%           | 18,11%           | RISCHIO STIMATO SEVERO |
| 2026-07-22        | SOL     | 77,84 $           | 70,69 $     | 89,94 $     | -9,18%           | 15,55%           | RISCHIO STIMATO SEVERO |
| 2026-07-22        | BTC     | 220,37 $          | 62.226,58 $ | 75.567,51 $ | 28137,32%        | 34191,20%        | RISCHIO STIMATO SEVERO |
| 2026-07-21        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07585 $   | -2,90%           | 8,36%            | RISCHIO STIMATO SEVERO |
| 2026-07-21        | SOL     | 78,18 $           | 70,69 $     | 85,63 $     | -9,58%           | 9,53%            | RISCHIO STIMATO SEVERO |
| 2026-07-21        | BTC     | 471,66 $          | 62.226,58 $ | 69.786,68 $ | 13093,10%        | 14695,97%        | RISCHIO STIMATO SEVERO |
| 2026-07-20        | BTC     | 149,77 $          | 62.226,58 $ | 66.910,06 $ | 41448,09%        | 44575,21%        | RISCHIO STIMATO SEVERO |
| 2026-07-20        | SOL     | 75,92 $           | 70,69 $     | 78,73 $     | -6,88%           | 3,70%            | RISCHIO STIMATO SEVERO |
| 2026-07-20        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07380 $   | -2,90%           | 5,43%            | RISCHIO STIMATO SEVERO |

## Come leggerlo

- **Drawdown normale hit**: quante volte il prezzo ha toccato la discesa normale prevista.
- **Drawdown brutto hit**: quante volte il prezzo ha toccato la zona brutta prevista.
- **Drawdown molto brutto hit**: quante volte è stato toccato il rischio estremo.
- Se il drawdown brutto viene toccato spesso, il rischio alto era giustificato.
- Se il drawdown normale non viene quasi mai toccato, il rischio potrebbe essere troppo severo.
- Se il drawdown molto brutto viene toccato spesso, il modello stava forse sottovalutando il rischio.

## Traduzione pratica

- Per spot, un drawdown profondo è dolore e rischio di timing, ma non liquidazione.
- Per leva, lo stesso drawdown può chiudere la posizione anche se poi il prezzo recupera.
- Per questo il report separa rischio spot e rischio leva.

