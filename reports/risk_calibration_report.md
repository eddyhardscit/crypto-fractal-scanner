# Calibrazione rischio spot / leva

Generato: **2026-08-14 10:53 UTC**

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
| BTC     | 760,22 $  | Direzione più probabile a 30 giorni: | 243,65 $ / -4,01%  | 628,01 $ / -6,58%   | 346,67 $ / 20,05%  | BASSO          | MEDIO          |
| SOL     | 75,37 $   | Direzione più probabile a 30 giorni: | 72,34 $ / -4,02%   | 70,36 $ / -6,65%    | 87,55 $ / 16,16%   | BASSO          | MEDIO          |
| DOGE    | 0.07000 $ | Direzione più probabile a 30 giorni: | 0.06000 $ / -9,45% | 0.06000 $ / -13,79% | 0.09000 $ / 23,28% | MEDIO          | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         35 |               7 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         35 |               7 |          28 | RACCOLTA DATI | 14,29%           | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         35 |               7 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio          |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:---------------------------|
| 2026-07-15        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07515 $   | -2,90%           | 7,36%            | RISCHIO STIMATO SEVERO     |
| 2026-07-15        | SOL     | 77,68 $           | 70,69 $     | 78,88 $     | -8,99%           | 1,54%            | RISCHIO NORMALE CONFERMATO |
| 2026-07-15        | BTC     | 595,85 $          | 62.226,58 $ | 66.910,06 $ | 10343,33%        | 11129,35%        | RISCHIO STIMATO SEVERO     |
| 2026-07-14        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07525 $   | -2,90%           | 7,50%            | RISCHIO STIMATO SEVERO     |
| 2026-07-14        | SOL     | 77,17 $           | 70,69 $     | 78,88 $     | -8,39%           | 2,21%            | RISCHIO STIMATO SEVERO     |
| 2026-07-14        | BTC     | 604,31 $          | 62.207,52 $ | 66.910,06 $ | 10193,98%        | 10972,14%        | RISCHIO STIMATO SEVERO     |
| 2026-07-13        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07525 $   | -2,90%           | 7,50%            | RISCHIO STIMATO SEVERO     |
| 2026-07-13        | SOL     | 76,29 $           | 70,69 $     | 78,88 $     | -7,33%           | 3,39%            | RISCHIO STIMATO SEVERO     |
| 2026-07-13        | BTC     | 681,78 $          | 61.769,00 $ | 66.910,06 $ | 8959,96%         | 9714,03%         | RISCHIO STIMATO SEVERO     |
| 2026-07-12        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07525 $   | -2,90%           | 7,50%            | RISCHIO STIMATO SEVERO     |
| 2026-07-12        | SOL     | 76,45 $           | 70,69 $     | 78,88 $     | -7,53%           | 3,18%            | RISCHIO STIMATO SEVERO     |
| 2026-07-12        | BTC     | 827,41 $          | 61.769,00 $ | 66.910,06 $ | 7365,34%         | 7986,69%         | RISCHIO STIMATO SEVERO     |

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

