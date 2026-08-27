# Calibrazione rischio spot / leva

Generato: **2026-08-27 05:33 UTC**

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
| BTC     | 653,26 $  | Direzione più probabile a 30 giorni: | 175,56 $ / -9,51%  | 849,42 $ / -15,01%  | 525,71 $ / 17,64%  | MEDIO          | MOLTO ALTO     |
| SOL     | 100,99 $  | Direzione più probabile a 30 giorni: | 89,49 $ / -11,39%  | 85,43 $ / -15,41%   | 115,81 $ / 14,68%  | MEDIO          | MOLTO ALTO     |
| DOGE    | 0.09000 $ | Direzione più probabile a 30 giorni: | 0.08000 $ / -9,82% | 0.07000 $ / -17,78% | 0.10000 $ / 17,61% | MEDIO          | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         48 |              20 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         48 |              20 |          28 | RACCOLTA DATI | 5,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         48 |              20 |          28 | RACCOLTA DATI | 10,00%           | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio          |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:---------------------------|
| 2026-07-28        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09998 $   | -2,90%           | 42,83%           | RISCHIO STIMATO SEVERO     |
| 2026-07-28        | SOL     | 73,28 $           | 70,69 $     | 102,59 $    | -3,53%           | 39,99%           | RISCHIO STIMATO SEVERO     |
| 2026-07-28        | BTC     | 391,68 $          | 62.226,58 $ | 81.235,03 $ | 15787,10%        | 20640,15%        | RISCHIO STIMATO SEVERO     |
| 2026-07-27        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09998 $   | -2,90%           | 42,83%           | RISCHIO NORMALE CONFERMATO |
| 2026-07-27        | SOL     | 76,32 $           | 70,69 $     | 101,75 $    | -7,37%           | 33,32%           | RISCHIO STIMATO SEVERO     |
| 2026-07-27        | BTC     | 303,80 $          | 62.226,58 $ | 79.970,11 $ | 20382,74%        | 26223,27%        | RISCHIO STIMATO SEVERO     |
| 2026-07-26        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09998 $   | -2,90%           | 42,83%           | RISCHIO NORMALE CONFERMATO |
| 2026-07-26        | SOL     | 75,08 $           | 70,69 $     | 102,21 $    | -5,84%           | 36,13%           | RISCHIO STIMATO SEVERO     |
| 2026-07-26        | BTC     | 459,57 $          | 62.226,58 $ | 81.023,41 $ | 13440,17%        | 17530,27%        | RISCHIO STIMATO SEVERO     |
| 2026-07-25        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09998 $   | -2,90%           | 42,83%           | RISCHIO STIMATO SEVERO     |
| 2026-07-25        | SOL     | 74,20 $           | 70,69 $     | 101,75 $    | -4,72%           | 37,13%           | RISCHIO STIMATO SEVERO     |
| 2026-07-25        | BTC     | 91,08 $           | 62.226,58 $ | 79.463,71 $ | 68220,79%        | 87146,06%        | RISCHIO STIMATO SEVERO     |

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

