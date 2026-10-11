# Calibrazione rischio spot / leva

Generato: **2026-10-11 05:33 UTC**

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

| Asset   | Prezzo    | Direzione scanner                    | Drawdown normale    | Drawdown brutto     | Max gain normale   | Rischio spot   | Rischio leva   |
|:--------|:----------|:-------------------------------------|:--------------------|:--------------------|:-------------------|:---------------|:---------------|
| BTC     | 976,46 $  | Direzione più probabile a 30 giorni: | 534,11 $ / -13,79%  | 491,29 $ / -17,46%  | 879,57 $ / 11,93%  | ALTO           | MOLTO ALTO     |
| SOL     | 109,54 $  | Direzione più probabile a 30 giorni: | 97,97 $ / -10,56%   | 90,90 $ / -17,02%   | 123,76 $ / 12,98%  | MEDIO          | MOLTO ALTO     |
| DOGE    | 0.09000 $ | Direzione più probabile a 30 giorni: | 0.08000 $ / -10,18% | 0.07000 $ / -16,71% | 0.10000 $ / 12,42% | MEDIO          | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato                | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:---------------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         87 |              63 |          24 | CALIBRAZIONE LEGGERA | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         87 |              63 |          24 | CALIBRAZIONE LEGGERA | 1,59%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         87 |              63 |          24 | CALIBRAZIONE LEGGERA | 14,29%           | 4,76%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-09-11        | DOGE    | 0.08000 $         | 0.07841 $   | 0.10528 $   | -1,99%           | 31,60%           | RISCHIO STIMATO SEVERO |
| 2026-09-11        | SOL     | 99,61 $           | 96,23 $     | 124,62 $    | -3,40%           | 25,11%           | RISCHIO STIMATO SEVERO |
| 2026-09-11        | BTC     | 59,01 $           | 74.944,59 $ | 87.363,76 $ | 126903,21%       | 147949,07%       | RISCHIO STIMATO SEVERO |
| 2026-09-10        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO STIMATO SEVERO |
| 2026-09-10        | SOL     | 102,02 $          | 96,23 $     | 124,62 $    | -5,68%           | 22,15%           | RISCHIO STIMATO SEVERO |
| 2026-09-10        | BTC     | 456,64 $          | 74.944,59 $ | 87.363,76 $ | 16312,18%        | 19031,87%        | RISCHIO STIMATO SEVERO |
| 2026-09-09        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO STIMATO SEVERO |
| 2026-09-09        | SOL     | 104,43 $          | 96,23 $     | 124,62 $    | -7,86%           | 19,33%           | RISCHIO STIMATO SEVERO |
| 2026-09-09        | BTC     | 122,84 $          | 74.944,59 $ | 87.363,76 $ | 60909,93%        | 71019,96%        | RISCHIO STIMATO SEVERO |
| 2026-09-08        | BTC     | 780,06 $          | 74.944,59 $ | 87.363,76 $ | 9507,54%         | 11099,62%        | RISCHIO STIMATO SEVERO |
| 2026-09-08        | SOL     | 103,29 $          | 96,23 $     | 124,62 $    | -6,84%           | 20,65%           | RISCHIO STIMATO SEVERO |
| 2026-09-08        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO STIMATO SEVERO |

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

