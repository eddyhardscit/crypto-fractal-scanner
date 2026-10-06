# Calibrazione rischio spot / leva

Generato: **2026-10-06 05:33 UTC**

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
| BTC     | 668,03 $  | Direzione più probabile a 30 giorni: | 635,56 $ / -14,05%  | 749,69 $ / -20,92%  | 677,91 $ / 12,85%  | ALTO           | MOLTO ALTO     |
| SOL     | 120,12 $  | Direzione più probabile a 30 giorni: | 103,47 $ / -13,86%  | 97,82 $ / -18,57%   | 132,27 $ / 10,12%  | ALTO           | MOLTO ALTO     |
| DOGE    | 0.09000 $ | Direzione più probabile a 30 giorni: | 0.08000 $ / -15,45% | 0.07000 $ / -21,06% | 0.11000 $ / 13,02% | ALTO           | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato            | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:-----------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         82 |              58 |          24 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         82 |              58 |          24 | OSSERVAZIONE 30+ | 1,72%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         82 |              58 |          24 | OSSERVAZIONE 30+ | 15,52%           | 5,17%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-09-06        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO STIMATO SEVERO |
| 2026-09-06        | SOL     | 106,09 $          | 96,23 $     | 124,62 $    | -9,30%           | 17,46%           | RISCHIO STIMATO SEVERO |
| 2026-09-06        | BTC     | 859,01 $          | 74.944,59 $ | 87.363,76 $ | 8624,53%         | 10070,28%        | RISCHIO STIMATO SEVERO |
| 2026-09-05        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO STIMATO SEVERO |
| 2026-09-05        | SOL     | 102,31 $          | 96,23 $     | 124,62 $    | -5,95%           | 21,80%           | RISCHIO STIMATO SEVERO |
| 2026-09-05        | BTC     | 667,15 $          | 74.944,59 $ | 87.363,76 $ | 11133,54%        | 12995,07%        | RISCHIO STIMATO SEVERO |
| 2026-09-04        | DOGE    | 0.09000 $         | 0.07841 $   | 0.10528 $   | -12,88%          | 16,98%           | RISCHIO STIMATO SEVERO |
| 2026-09-04        | SOL     | 103,67 $          | 96,23 $     | 124,62 $    | -7,18%           | 20,21%           | RISCHIO STIMATO SEVERO |
| 2026-09-04        | BTC     | 955,88 $          | 74.944,59 $ | 87.363,76 $ | 7740,38%         | 9039,62%         | RISCHIO STIMATO SEVERO |
| 2026-09-03        | BTC     | 185,68 $          | 74.944,59 $ | 87.363,76 $ | 40262,23%        | 46950,71%        | RISCHIO STIMATO SEVERO |
| 2026-09-03        | SOL     | 99,93 $           | 96,23 $     | 124,62 $    | -3,71%           | 24,70%           | RISCHIO STIMATO SEVERO |
| 2026-09-03        | DOGE    | 0.08000 $         | 0.07841 $   | 0.10528 $   | -1,99%           | 31,60%           | RISCHIO STIMATO SEVERO |

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

