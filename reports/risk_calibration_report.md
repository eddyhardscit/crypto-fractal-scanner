# Calibrazione rischio spot / leva

Generato: **2026-10-08 05:33 UTC**

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
| BTC     | 851,09 $  | Direzione più probabile a 30 giorni: | 48,41 $ / -10,62%   | 908,60 $ / -16,83%  | 76,22 $ / 18,38%   | MEDIO          | MOLTO ALTO     |
| SOL     | 115,51 $  | Direzione più probabile a 30 giorni: | 100,22 $ / -13,24%  | 94,81 $ / -17,92%   | 128,12 $ / 10,92%  | ALTO           | MOLTO ALTO     |
| DOGE    | 0.09000 $ | Direzione più probabile a 30 giorni: | 0.08000 $ / -12,81% | 0.07000 $ / -18,41% | 0.10000 $ / 13,07% | ALTO           | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato                | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:---------------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         84 |              60 |          24 | CALIBRAZIONE LEGGERA | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         84 |              60 |          24 | CALIBRAZIONE LEGGERA | 1,67%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         84 |              60 |          24 | CALIBRAZIONE LEGGERA | 15,00%           | 5,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-09-08        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO STIMATO SEVERO |
| 2026-09-08        | SOL     | 103,29 $          | 96,23 $     | 124,62 $    | -6,84%           | 20,65%           | RISCHIO STIMATO SEVERO |
| 2026-09-08        | BTC     | 780,06 $          | 74.944,59 $ | 87.363,76 $ | 9507,54%         | 11099,62%        | RISCHIO STIMATO SEVERO |
| 2026-09-07        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO STIMATO SEVERO |
| 2026-09-07        | SOL     | 105,54 $          | 96,23 $     | 124,62 $    | -8,83%           | 18,08%           | RISCHIO STIMATO SEVERO |
| 2026-09-07        | BTC     | 817,81 $          | 74.944,59 $ | 87.363,76 $ | 9064,06%         | 10582,65%        | RISCHIO STIMATO SEVERO |
| 2026-09-06        | SOL     | 106,09 $          | 96,23 $     | 124,62 $    | -9,30%           | 17,46%           | RISCHIO STIMATO SEVERO |
| 2026-09-06        | BTC     | 859,01 $          | 74.944,59 $ | 87.363,76 $ | 8624,53%         | 10070,28%        | RISCHIO STIMATO SEVERO |
| 2026-09-06        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO STIMATO SEVERO |
| 2026-09-05        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO STIMATO SEVERO |
| 2026-09-05        | SOL     | 102,31 $          | 96,23 $     | 124,62 $    | -5,95%           | 21,80%           | RISCHIO STIMATO SEVERO |
| 2026-09-05        | BTC     | 667,15 $          | 74.944,59 $ | 87.363,76 $ | 11133,54%        | 12995,07%        | RISCHIO STIMATO SEVERO |

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

