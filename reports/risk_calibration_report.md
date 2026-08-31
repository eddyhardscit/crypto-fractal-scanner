# Calibrazione rischio spot / leva

Generato: **2026-08-31 05:33 UTC**

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
| BTC     | 994,98 $  | Direzione più probabile a 30 giorni: | 256,29 $ / -12,49%  | 630,54 $ / -15,85%  | 783,98 $ / 13,83%  | ALTO           | MOLTO ALTO     |
| SOL     | 102,67 $  | Direzione più probabile a 30 giorni: | 88,69 $ / -13,61%   | 80,73 $ / -21,37%   | 125,06 $ / 21,81%  | ALTO           | MOLTO ALTO     |
| DOGE    | 0.08000 $ | Direzione più probabile a 30 giorni: | 0.07000 $ / -11,99% | 0.06000 $ / -22,33% | 0.10000 $ / 20,61% | ALTO           | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         52 |              24 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         52 |              24 |          28 | RACCOLTA DATI | 4,17%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         52 |              24 |          28 | RACCOLTA DATI | 8,33%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-08-01        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09998 $   | -2,90%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-01        | SOL     | 73,12 $           | 70,69 $     | 110,04 $    | -3,32%           | 50,49%           | RISCHIO STIMATO SEVERO |
| 2026-08-01        | BTC     | 65,12 $           | 62.226,58 $ | 81.346,95 $ | 95456,78%        | 124818,54%       | RISCHIO STIMATO SEVERO |
| 2026-07-31        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09998 $   | -2,90%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-07-31        | SOL     | 74,00 $           | 70,69 $     | 110,04 $    | -4,47%           | 48,70%           | RISCHIO STIMATO SEVERO |
| 2026-07-31        | BTC     | 329,85 $          | 62.226,58 $ | 81.235,03 $ | 18765,11%        | 24527,87%        | RISCHIO STIMATO SEVERO |
| 2026-07-30        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09998 $   | -2,90%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-07-30        | SOL     | 73,43 $           | 70,69 $     | 110,04 $    | -3,73%           | 49,86%           | RISCHIO STIMATO SEVERO |
| 2026-07-30        | BTC     | 884,80 $          | 62.226,58 $ | 81.235,03 $ | 6932,84%         | 9081,17%         | RISCHIO STIMATO SEVERO |
| 2026-07-29        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09998 $   | -2,90%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-07-29        | SOL     | 73,47 $           | 70,69 $     | 110,04 $    | -3,78%           | 49,77%           | RISCHIO STIMATO SEVERO |
| 2026-07-29        | BTC     | 921,65 $          | 62.226,58 $ | 81.235,03 $ | 6651,65%         | 8714,09%         | RISCHIO STIMATO SEVERO |

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

