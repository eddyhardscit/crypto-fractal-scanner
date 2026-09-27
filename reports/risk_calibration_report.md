# Calibrazione rischio spot / leva

Generato: **2026-09-27 05:32 UTC**

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
| BTC     | 377,03 $  | Direzione più probabile a 30 giorni: | 809,54 $ / -13,71%  | 146,47 $ / -20,42%  | 722,03 $ / 18,19%  | ALTO           | MOLTO ALTO     |
| SOL     | 120,68 $  | Direzione più probabile a 30 giorni: | 99,88 $ / -17,24%   | 89,70 $ / -25,67%   | 142,11 $ / 17,76%  | ALTO           | MOLTO ALTO     |
| DOGE    | 0.10000 $ | Direzione più probabile a 30 giorni: | 0.08000 $ / -19,13% | 0.07000 $ / -30,57% | 0.10000 $ / 8,58%  | ALTO           | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato            | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:-----------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         74 |              49 |          25 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         74 |              49 |          25 | OSSERVAZIONE 30+ | 2,04%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         74 |              49 |          25 | OSSERVAZIONE 30+ | 18,37%           | 6,12%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio          |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:---------------------------|
| 2026-08-28        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO NORMALE CONFERMATO |
| 2026-08-28        | SOL     | 106,34 $          | 96,23 $     | 122,75 $    | -9,51%           | 15,43%           | RISCHIO STIMATO SEVERO     |
| 2026-08-28        | BTC     | 679,38 $          | 74.944,59 $ | 87.363,76 $ | 10931,32%        | 12759,34%        | RISCHIO STIMATO SEVERO     |
| 2026-08-27        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO NORMALE CONFERMATO |
| 2026-08-27        | SOL     | 100,99 $          | 96,23 $     | 122,21 $    | -4,72%           | 21,02%           | RISCHIO STIMATO SEVERO     |
| 2026-08-27        | BTC     | 653,26 $          | 74.944,59 $ | 87.363,76 $ | 11372,40%        | 13273,50%        | RISCHIO STIMATO SEVERO     |
| 2026-08-26        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO NORMALE CONFERMATO |
| 2026-08-26        | SOL     | 96,77 $           | 95,23 $     | 122,74 $    | -1,59%           | 26,84%           | RISCHIO STIMATO SEVERO     |
| 2026-08-26        | BTC     | 978,29 $          | 74.944,59 $ | 87.363,76 $ | 7560,77%         | 8830,25%         | RISCHIO STIMATO SEVERO     |
| 2026-08-25        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO ALTO CONFERMATO    |
| 2026-08-25        | SOL     | 102,48 $          | 95,23 $     | 119,81 $    | -7,07%           | 16,91%           | RISCHIO STIMATO SEVERO     |
| 2026-08-25        | BTC     | 567,77 $          | 74.944,59 $ | 87.363,76 $ | 13099,82%        | 15287,17%        | RISCHIO STIMATO SEVERO     |

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

