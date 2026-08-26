# Calibrazione rischio spot / leva

Generato: **2026-08-26 05:32 UTC**

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
| BTC     | 978,29 $  | Direzione più probabile a 30 giorni: | 133,71 $ / -8,67%  | 396,39 $ / -13,40%  | 441,73 $ / 17,05%  | MEDIO          | MOLTO ALTO     |
| SOL     | 96,77 $   | Direzione più probabile a 30 giorni: | 85,62 $ / -11,53%  | 81,35 $ / -15,93%   | 112,42 $ / 16,18%  | MEDIO          | MOLTO ALTO     |
| DOGE    | 0.09000 $ | Direzione più probabile a 30 giorni: | 0.08000 $ / -9,98% | 0.07000 $ / -17,55% | 0.10000 $ / 18,73% | MEDIO          | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         47 |              19 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         47 |              19 |          28 | RACCOLTA DATI | 5,26%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         47 |              19 |          28 | RACCOLTA DATI | 10,53%           | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio          |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:---------------------------|
| 2026-07-27        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09998 $   | -2,90%           | 42,83%           | RISCHIO NORMALE CONFERMATO |
| 2026-07-27        | SOL     | 76,32 $           | 70,69 $     | 101,75 $    | -7,37%           | 33,32%           | RISCHIO STIMATO SEVERO     |
| 2026-07-27        | BTC     | 303,80 $          | 62.226,58 $ | 79.970,11 $ | 20382,74%        | 26223,27%        | RISCHIO STIMATO SEVERO     |
| 2026-07-26        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09998 $   | -2,90%           | 42,83%           | RISCHIO NORMALE CONFERMATO |
| 2026-07-26        | SOL     | 75,08 $           | 70,69 $     | 102,21 $    | -5,84%           | 36,13%           | RISCHIO STIMATO SEVERO     |
| 2026-07-26        | BTC     | 459,57 $          | 62.226,58 $ | 81.023,41 $ | 13440,17%        | 17530,27%        | RISCHIO STIMATO SEVERO     |
| 2026-07-25        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09998 $   | -2,90%           | 42,83%           | RISCHIO STIMATO SEVERO     |
| 2026-07-25        | SOL     | 74,20 $           | 70,69 $     | 101,75 $    | -4,72%           | 37,13%           | RISCHIO STIMATO SEVERO     |
| 2026-07-25        | BTC     | 91,08 $           | 62.226,58 $ | 79.463,71 $ | 68220,79%        | 87146,06%        | RISCHIO STIMATO SEVERO     |
| 2026-07-24        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09423 $   | -2,90%           | 34,61%           | RISCHIO STIMATO SEVERO     |
| 2026-07-24        | SOL     | 75,72 $           | 70,69 $     | 96,54 $     | -6,64%           | 27,49%           | RISCHIO STIMATO SEVERO     |
| 2026-07-24        | BTC     | 307,47 $          | 62.226,58 $ | 79.463,71 $ | 20138,26%        | 25744,38%        | RISCHIO STIMATO SEVERO     |

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

