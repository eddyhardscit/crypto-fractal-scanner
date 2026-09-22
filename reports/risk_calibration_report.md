# Calibrazione rischio spot / leva

Generato: **2026-09-22 05:33 UTC**

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
| BTC     | 203,71 $  | Direzione più probabile a 30 giorni: | 182,04 $ / -2,37%   | 627,21 $ / -14,76%  | 652,27 $ / 27,52%  | MEDIO          | ALTO           |
| SOL     | 115,88 $  | Direzione più probabile a 30 giorni: | 101,16 $ / -12,70%  | 84,57 $ / -27,02%   | 142,31 $ / 22,81%  | ALTO           | MOLTO ALTO     |
| DOGE    | 0.10000 $ | Direzione più probabile a 30 giorni: | 0.08000 $ / -20,21% | 0.07000 $ / -27,32% | 0.11000 $ / 14,92% | MOLTO ALTO     | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato            | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:-----------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         70 |              44 |          26 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         70 |              44 |          26 | OSSERVAZIONE 30+ | 2,27%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         70 |              44 |          26 | OSSERVAZIONE 30+ | 9,09%            | 2,27%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio          |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:---------------------------|
| 2026-08-23        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10487 $   | -12,88%          | 16,53%           | RISCHIO ALTO CONFERMATO    |
| 2026-08-23        | SOL     | 93,19 $           | 91,82 $     | 119,28 $    | -1,47%           | 27,99%           | RISCHIO STIMATO SEVERO     |
| 2026-08-23        | BTC     | 328,18 $          | 74.944,59 $ | 86.597,82 $ | 22736,43%        | 26287,29%        | RISCHIO STIMATO SEVERO     |
| 2026-08-22        | DOGE    | 0.09000 $         | 0.07841 $   | 0.09998 $   | -12,88%          | 11,09%           | RISCHIO NORMALE CONFERMATO |
| 2026-08-22        | SOL     | 93,70 $           | 91,28 $     | 114,06 $    | -2,58%           | 21,73%           | RISCHIO STIMATO SEVERO     |
| 2026-08-22        | BTC     | 239,39 $          | 74.944,59 $ | 82.262,21 $ | 31206,48%        | 34263,26%        | RISCHIO STIMATO SEVERO     |
| 2026-08-21        | DOGE    | 0.08000 $         | 0.07841 $   | 0.09998 $   | -1,99%           | 24,97%           | RISCHIO STIMATO SEVERO     |
| 2026-08-21        | SOL     | 89,55 $           | 87,60 $     | 114,06 $    | -2,17%           | 27,37%           | RISCHIO STIMATO SEVERO     |
| 2026-08-21        | BTC     | 133,45 $          | 73.011,41 $ | 82.262,21 $ | 54610,69%        | 61542,72%        | RISCHIO STIMATO SEVERO     |
| 2026-08-20        | DOGE    | 0.07000 $         | 0.07447 $   | 0.09998 $   | 6,39%            | 42,83%           | RISCHIO STIMATO SEVERO     |
| 2026-08-20        | SOL     | 84,87 $           | 84,08 $     | 114,06 $    | -0,93%           | 34,39%           | RISCHIO STIMATO SEVERO     |
| 2026-08-20        | BTC     | 564,87 $          | 68.867,53 $ | 82.262,21 $ | 12091,75%        | 14463,03%        | RISCHIO STIMATO SEVERO     |

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

