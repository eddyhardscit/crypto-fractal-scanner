# Calibrazione rischio spot / leva

Generato: **2026-08-19 05:33 UTC**

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
| BTC     | 305,87 $  | Direzione più probabile a 30 giorni: | 573,44 $ / -4,25%  | 133,93 $ / -11,15%  | 911,57 $ / 18,05%  | BASSO          | ALTO           |
| SOL     | 76,92 $   | Direzione più probabile a 30 giorni: | 74,30 $ / -3,41%   | 70,70 $ / -8,08%    | 89,41 $ / 16,24%   | BASSO          | MEDIO          |
| DOGE    | 0.07000 $ | Direzione più probabile a 30 giorni: | 0.06000 $ / -8,68% | 0.06000 $ / -15,02% | 0.09000 $ / 26,44% | MEDIO          | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         40 |              12 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         40 |              12 |          28 | RACCOLTA DATI | 8,33%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         40 |              12 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-07-20        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07380 $   | -2,90%           | 5,43%            | RISCHIO STIMATO SEVERO |
| 2026-07-20        | SOL     | 75,92 $           | 70,69 $     | 78,73 $     | -6,88%           | 3,70%            | RISCHIO STIMATO SEVERO |
| 2026-07-20        | BTC     | 149,77 $          | 62.226,58 $ | 66.910,06 $ | 41448,09%        | 44575,21%        | RISCHIO STIMATO SEVERO |
| 2026-07-19        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07380 $   | -2,90%           | 5,43%            | RISCHIO STIMATO SEVERO |
| 2026-07-19        | SOL     | 76,00 $           | 70,69 $     | 78,73 $     | -6,98%           | 3,59%            | RISCHIO STIMATO SEVERO |
| 2026-07-19        | BTC     | 723,48 $          | 62.226,58 $ | 66.910,06 $ | 8501,01%         | 9148,36%         | RISCHIO STIMATO SEVERO |
| 2026-07-18        | BTC     | 889,06 $          | 62.226,58 $ | 66.910,06 $ | 6899,14%         | 7425,93%         | RISCHIO STIMATO SEVERO |
| 2026-07-18        | SOL     | 74,93 $           | 70,69 $     | 78,73 $     | -5,65%           | 5,07%            | RISCHIO STIMATO SEVERO |
| 2026-07-18        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07380 $   | -2,90%           | 5,43%            | RISCHIO STIMATO SEVERO |
| 2026-07-17        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07380 $   | -2,90%           | 5,43%            | RISCHIO STIMATO SEVERO |
| 2026-07-17        | SOL     | 74,46 $           | 70,69 $     | 78,73 $     | -5,06%           | 5,73%            | RISCHIO STIMATO SEVERO |
| 2026-07-17        | BTC     | 870,64 $          | 62.226,58 $ | 66.910,06 $ | 7047,22%         | 7585,16%         | RISCHIO STIMATO SEVERO |

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

