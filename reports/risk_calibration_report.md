# Calibrazione rischio spot / leva

Generato: **2026-09-17 05:33 UTC**

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
| BTC     | 402,76 $  | Direzione più probabile a 30 giorni: | 550,32 $ / -2,42%   | 834,21 $ / -8,60%   | 233,84 $ / 35,12%  | BASSO          | MEDIO          |
| SOL     | 99,61 $   | Direzione più probabile a 30 giorni: | 93,44 $ / -6,19%    | 77,86 $ / -21,84%   | 132,91 $ / 33,43%  | MEDIO          | MOLTO ALTO     |
| DOGE    | 0.08000 $ | Direzione più probabile a 30 giorni: | 0.06000 $ / -21,88% | 0.06000 $ / -31,62% | 0.09000 $ / 10,18% | MOLTO ALTO     | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato            | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:-----------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         69 |              39 |          30 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         69 |              39 |          30 | OSSERVAZIONE 30+ | 2,56%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         69 |              39 |          30 | OSSERVAZIONE 30+ | 5,13%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-08-18        | DOGE    | 0.07000 $         | 0.06961 $   | 0.09998 $   | -0,55%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-18        | SOL     | 75,70 $           | 75,19 $     | 110,04 $    | -0,68%           | 45,36%           | RISCHIO STIMATO SEVERO |
| 2026-08-18        | BTC     | 177,53 $          | 63.980,32 $ | 82.262,21 $ | 35939,16%        | 46237,08%        | RISCHIO STIMATO SEVERO |
| 2026-08-17        | DOGE    | 0.07000 $         | 0.06946 $   | 0.09998 $   | -0,77%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-17        | SOL     | 75,42 $           | 74,40 $     | 110,04 $    | -1,35%           | 45,90%           | RISCHIO STIMATO SEVERO |
| 2026-08-17        | BTC     | 429,43 $          | 62.687,10 $ | 82.262,21 $ | 14497,75%        | 19056,14%        | RISCHIO STIMATO SEVERO |
| 2026-08-16        | DOGE    | 0.07000 $         | 0.06929 $   | 0.09998 $   | -1,02%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-16        | SOL     | 75,31 $           | 74,20 $     | 110,04 $    | -1,47%           | 46,11%           | RISCHIO STIMATO SEVERO |
| 2026-08-16        | BTC     | 0,01 $            | 62.648,57 $ | 82.262,21 $ | 626485642,19%    | 822622009,38%    | RISCHIO STIMATO SEVERO |
| 2026-08-15        | DOGE    | 0.07000 $         | 0.06929 $   | 0.09998 $   | -1,02%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-15        | SOL     | 75,39 $           | 74,20 $     | 110,04 $    | -1,57%           | 45,96%           | RISCHIO STIMATO SEVERO |
| 2026-08-15        | BTC     | 50,60 $           | 62.648,57 $ | 82.262,21 $ | 123711,41%       | 162473,54%       | RISCHIO STIMATO SEVERO |

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

