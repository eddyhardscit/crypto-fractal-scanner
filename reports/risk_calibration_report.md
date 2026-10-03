# Calibrazione rischio spot / leva

Generato: **2026-10-03 05:33 UTC**

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
| BTC     | 612,06 $  | Direzione più probabile a 30 giorni: | 148,15 $ / -11,19%  | 958,72 $ / -16,14%  | 261,73 $ / 16,13%  | MEDIO          | MOLTO ALTO     |
| SOL     | 119,53 $  | Direzione più probabile a 30 giorni: | 103,91 $ / -13,07%  | 93,75 $ / -21,57%   | 141,08 $ / 18,03%  | ALTO           | MOLTO ALTO     |
| DOGE    | 0.09000 $ | Direzione più probabile a 30 giorni: | 0.08000 $ / -14,68% | 0.07000 $ / -22,60% | 0.11000 $ / 12,94% | ALTO           | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato            | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:-----------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         79 |              55 |          24 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         79 |              55 |          24 | OSSERVAZIONE 30+ | 1,82%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         79 |              55 |          24 | OSSERVAZIONE 30+ | 16,36%           | 5,45%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-09-03        | DOGE    | 0.08000 $         | 0.07841 $   | 0.10528 $   | -1,99%           | 31,60%           | RISCHIO STIMATO SEVERO |
| 2026-09-03        | SOL     | 99,93 $           | 96,23 $     | 124,62 $    | -3,71%           | 24,70%           | RISCHIO STIMATO SEVERO |
| 2026-09-03        | BTC     | 185,68 $          | 74.944,59 $ | 87.363,76 $ | 40262,23%        | 46950,71%        | RISCHIO STIMATO SEVERO |
| 2026-09-02        | DOGE    | 0.08000 $         | 0.07841 $   | 0.10528 $   | -1,99%           | 31,60%           | RISCHIO STIMATO SEVERO |
| 2026-09-02        | SOL     | 100,24 $          | 96,23 $     | 124,62 $    | -4,00%           | 24,32%           | RISCHIO STIMATO SEVERO |
| 2026-09-02        | BTC     | 666,99 $          | 74.944,59 $ | 87.363,76 $ | 11136,24%        | 12998,21%        | RISCHIO STIMATO SEVERO |
| 2026-09-01        | SOL     | 103,93 $          | 96,23 $     | 124,62 $    | -7,41%           | 19,91%           | RISCHIO STIMATO SEVERO |
| 2026-09-01        | BTC     | 947,11 $          | 74.944,59 $ | 87.363,76 $ | 7812,98%         | 9124,25%         | RISCHIO STIMATO SEVERO |
| 2026-09-01        | DOGE    | 0.08000 $         | 0.07841 $   | 0.10528 $   | -1,99%           | 31,60%           | RISCHIO STIMATO SEVERO |
| 2026-08-31        | DOGE    | 0.08000 $         | 0.07841 $   | 0.10528 $   | -1,99%           | 31,60%           | RISCHIO STIMATO SEVERO |
| 2026-08-31        | SOL     | 102,67 $          | 96,23 $     | 124,62 $    | -6,28%           | 21,38%           | RISCHIO STIMATO SEVERO |
| 2026-08-31        | BTC     | 994,98 $          | 74.944,59 $ | 87.363,76 $ | 7432,27%         | 8680,45%         | RISCHIO STIMATO SEVERO |

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

