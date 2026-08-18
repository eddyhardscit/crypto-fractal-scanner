# Calibrazione rischio spot / leva

Generato: **2026-08-18 05:33 UTC**

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

| Asset   | Prezzo    | Direzione scanner                    | Drawdown normale   | Drawdown brutto     | Max gain normale   | Rischio spot   | Rischio leva   |
|:--------|:----------|:-------------------------------------|:-------------------|:--------------------|:-------------------|:---------------|:---------------|
| BTC     | 177,53 $  | Direzione più probabile a 30 giorni: | 506,14 $ / -4,16%  | 224,82 $ / -10,83%  | 615,49 $ / 17,82%  | BASSO          | ALTO           |
| SOL     | 75,70 $   | Direzione più probabile a 30 giorni: | 73,57 $ / -2,81%   | 70,65 $ / -6,67%    | 91,85 $ / 21,33%   | BASSO          | MEDIO          |
| DOGE    | 0.07000 $ | Direzione più probabile a 30 giorni: | 0.06000 $ / -8,15% | 0.06000 $ / -12,49% | 0.09000 $ / 24,22% | MEDIO          | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         39 |              11 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         39 |              11 |          28 | RACCOLTA DATI | 9,09%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         39 |              11 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-07-19        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07380 $   | -2,90%           | 5,43%            | RISCHIO STIMATO SEVERO |
| 2026-07-19        | SOL     | 76,00 $           | 70,69 $     | 78,73 $     | -6,98%           | 3,59%            | RISCHIO STIMATO SEVERO |
| 2026-07-19        | BTC     | 723,48 $          | 62.226,58 $ | 66.910,06 $ | 8501,01%         | 9148,36%         | RISCHIO STIMATO SEVERO |
| 2026-07-18        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07380 $   | -2,90%           | 5,43%            | RISCHIO STIMATO SEVERO |
| 2026-07-18        | SOL     | 74,93 $           | 70,69 $     | 78,73 $     | -5,65%           | 5,07%            | RISCHIO STIMATO SEVERO |
| 2026-07-18        | BTC     | 889,06 $          | 62.226,58 $ | 66.910,06 $ | 6899,14%         | 7425,93%         | RISCHIO STIMATO SEVERO |
| 2026-07-17        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07380 $   | -2,90%           | 5,43%            | RISCHIO STIMATO SEVERO |
| 2026-07-17        | SOL     | 74,46 $           | 70,69 $     | 78,73 $     | -5,06%           | 5,73%            | RISCHIO STIMATO SEVERO |
| 2026-07-17        | BTC     | 870,64 $          | 62.226,58 $ | 66.910,06 $ | 7047,22%         | 7585,16%         | RISCHIO STIMATO SEVERO |
| 2026-07-16        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07431 $   | -2,90%           | 6,16%            | RISCHIO STIMATO SEVERO |
| 2026-07-16        | SOL     | 76,30 $           | 70,69 $     | 78,73 $     | -7,35%           | 3,18%            | RISCHIO STIMATO SEVERO |
| 2026-07-16        | BTC     | 443,67 $          | 62.226,58 $ | 66.910,06 $ | 13925,42%        | 14981,04%        | RISCHIO STIMATO SEVERO |

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

