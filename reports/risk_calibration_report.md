# Calibrazione rischio spot / leva

Generato: **2026-10-12 05:33 UTC**

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
| BTC     | 862,67 $  | Direzione più probabile a 30 giorni: | 827,42 $ / -15,54% | 677,35 $ / -20,49%  | 409,09 $ / 10,19%  | ALTO           | MOLTO ALTO     |
| SOL     | 112,60 $  | Direzione più probabile a 30 giorni: | 101,39 $ / -9,95%  | 94,56 $ / -16,02%   | 128,63 $ / 14,24%  | MEDIO          | MOLTO ALTO     |
| DOGE    | 0.09000 $ | Direzione più probabile a 30 giorni: | 0.08000 $ / -9,39% | 0.07000 $ / -14,99% | 0.10000 $ / 12,95% | MEDIO          | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato                | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:---------------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         88 |              64 |          24 | CALIBRAZIONE LEGGERA | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         88 |              64 |          24 | CALIBRAZIONE LEGGERA | 1,56%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         88 |              64 |          24 | CALIBRAZIONE LEGGERA | 14,06%           | 4,69%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-09-12        | DOGE    | 0.08000 $         | 0.07841 $   | 0.10528 $   | -1,99%           | 31,60%           | RISCHIO STIMATO SEVERO |
| 2026-09-12        | SOL     | 101,55 $          | 96,23 $     | 124,62 $    | -5,24%           | 22,72%           | RISCHIO STIMATO SEVERO |
| 2026-09-12        | BTC     | 219,04 $          | 74.944,59 $ | 87.363,76 $ | 34115,03%        | 39784,84%        | RISCHIO STIMATO SEVERO |
| 2026-09-11        | DOGE    | 0.08000 $         | 0.07841 $   | 0.10528 $   | -1,99%           | 31,60%           | RISCHIO STIMATO SEVERO |
| 2026-09-11        | SOL     | 99,61 $           | 96,23 $     | 124,62 $    | -3,40%           | 25,11%           | RISCHIO STIMATO SEVERO |
| 2026-09-11        | BTC     | 59,01 $           | 74.944,59 $ | 87.363,76 $ | 126903,21%       | 147949,07%       | RISCHIO STIMATO SEVERO |
| 2026-09-10        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO STIMATO SEVERO |
| 2026-09-10        | SOL     | 102,02 $          | 96,23 $     | 124,62 $    | -5,68%           | 22,15%           | RISCHIO STIMATO SEVERO |
| 2026-09-10        | BTC     | 456,64 $          | 74.944,59 $ | 87.363,76 $ | 16312,18%        | 19031,87%        | RISCHIO STIMATO SEVERO |
| 2026-09-09        | BTC     | 122,84 $          | 74.944,59 $ | 87.363,76 $ | 60909,93%        | 71019,96%        | RISCHIO STIMATO SEVERO |
| 2026-09-09        | SOL     | 104,43 $          | 96,23 $     | 124,62 $    | -7,86%           | 19,33%           | RISCHIO STIMATO SEVERO |
| 2026-09-09        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO STIMATO SEVERO |

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

