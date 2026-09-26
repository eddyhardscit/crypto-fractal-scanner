# Calibrazione rischio spot / leva

Generato: **2026-09-26 05:32 UTC**

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
| BTC     | 922,83 $  | Direzione più probabile a 30 giorni: | 417,60 $ / -13,71%  | 785,02 $ / -20,42%  | 991,57 $ / 20,34%  | ALTO           | MOLTO ALTO     |
| SOL     | 120,40 $  | Direzione più probabile a 30 giorni: | 98,79 $ / -17,95%   | 88,89 $ / -26,17%   | 139,87 $ / 16,17%  | ALTO           | MOLTO ALTO     |
| DOGE    | 0.10000 $ | Direzione più probabile a 30 giorni: | 0.08000 $ / -20,13% | 0.07000 $ / -29,12% | 0.11000 $ / 10,04% | MOLTO ALTO     | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato            | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:-----------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         73 |              48 |          25 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         73 |              48 |          25 | OSSERVAZIONE 30+ | 2,08%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         73 |              48 |          25 | OSSERVAZIONE 30+ | 16,67%           | 6,25%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio          |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:---------------------------|
| 2026-08-27        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO NORMALE CONFERMATO |
| 2026-08-27        | SOL     | 100,99 $          | 96,23 $     | 122,21 $    | -4,72%           | 21,02%           | RISCHIO STIMATO SEVERO     |
| 2026-08-27        | BTC     | 653,26 $          | 74.944,59 $ | 87.363,76 $ | 11372,40%        | 13273,50%        | RISCHIO STIMATO SEVERO     |
| 2026-08-26        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO NORMALE CONFERMATO |
| 2026-08-26        | SOL     | 96,77 $           | 95,23 $     | 122,74 $    | -1,59%           | 26,84%           | RISCHIO STIMATO SEVERO     |
| 2026-08-26        | BTC     | 978,29 $          | 74.944,59 $ | 87.363,76 $ | 7560,77%         | 8830,25%         | RISCHIO STIMATO SEVERO     |
| 2026-08-25        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO ALTO CONFERMATO    |
| 2026-08-25        | SOL     | 102,48 $          | 95,23 $     | 119,81 $    | -7,07%           | 16,91%           | RISCHIO STIMATO SEVERO     |
| 2026-08-25        | BTC     | 567,77 $          | 74.944,59 $ | 87.363,76 $ | 13099,82%        | 15287,17%        | RISCHIO STIMATO SEVERO     |
| 2026-08-24        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10413 $   | -12,88%          | 15,70%           | RISCHIO ALTO CONFERMATO    |
| 2026-08-24        | SOL     | 94,05 $           | 93,33 $     | 119,81 $    | -0,76%           | 27,39%           | RISCHIO STIMATO SEVERO     |
| 2026-08-24        | BTC     | 28,36 $           | 74.944,59 $ | 87.363,76 $ | 264161,61%       | 307952,74%       | RISCHIO STIMATO SEVERO     |

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

