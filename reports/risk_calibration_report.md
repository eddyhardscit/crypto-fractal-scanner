# Calibrazione rischio spot / leva

Generato: **2026-09-29 05:33 UTC**

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
| BTC     | 242,65 $  | Direzione più probabile a 30 giorni: | 834,51 $ / -11,30%  | 419,75 $ / -19,01%  | 212,84 $ / 17,98%  | MEDIO          | MOLTO ALTO     |
| SOL     | 117,81 $  | Direzione più probabile a 30 giorni: | 104,67 $ / -11,15%  | 91,44 $ / -22,38%   | 141,91 $ / 20,46%  | ALTO           | MOLTO ALTO     |
| DOGE    | 0.09000 $ | Direzione più probabile a 30 giorni: | 0.08000 $ / -18,79% | 0.07000 $ / -26,94% | 0.10000 $ / 10,38% | ALTO           | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato            | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:-----------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         76 |              51 |          25 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         76 |              51 |          25 | OSSERVAZIONE 30+ | 1,96%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         76 |              51 |          25 | OSSERVAZIONE 30+ | 17,65%           | 5,88%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio          |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:---------------------------|
| 2026-08-30        | DOGE    | 0.08000 $         | 0.07841 $   | 0.10528 $   | -1,99%           | 31,60%           | RISCHIO STIMATO SEVERO     |
| 2026-08-30        | SOL     | 105,06 $          | 96,23 $     | 124,62 $    | -8,41%           | 18,62%           | RISCHIO STIMATO SEVERO     |
| 2026-08-30        | BTC     | 146,53 $          | 74.944,59 $ | 87.363,76 $ | 51046,25%        | 59521,76%        | RISCHIO STIMATO SEVERO     |
| 2026-08-29        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO STIMATO SEVERO     |
| 2026-08-29        | SOL     | 104,04 $          | 96,23 $     | 122,75 $    | -7,51%           | 17,98%           | RISCHIO STIMATO SEVERO     |
| 2026-08-29        | BTC     | 658,66 $          | 74.944,59 $ | 87.363,76 $ | 11278,34%        | 13163,86%        | RISCHIO STIMATO SEVERO     |
| 2026-08-28        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO NORMALE CONFERMATO |
| 2026-08-28        | SOL     | 106,34 $          | 96,23 $     | 122,75 $    | -9,51%           | 15,43%           | RISCHIO STIMATO SEVERO     |
| 2026-08-28        | BTC     | 679,38 $          | 74.944,59 $ | 87.363,76 $ | 10931,32%        | 12759,34%        | RISCHIO STIMATO SEVERO     |
| 2026-08-27        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO NORMALE CONFERMATO |
| 2026-08-27        | SOL     | 100,99 $          | 96,23 $     | 122,21 $    | -4,72%           | 21,02%           | RISCHIO STIMATO SEVERO     |
| 2026-08-27        | BTC     | 653,26 $          | 74.944,59 $ | 87.363,76 $ | 11372,40%        | 13273,50%        | RISCHIO STIMATO SEVERO     |

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

