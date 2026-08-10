# Calibrazione rischio spot / leva

Generato: **2026-08-10 05:17 UTC**

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
| BTC     | 946,42 $  | Direzione più probabile a 30 giorni: | 667,47 $ / -1,97%  | 576,13 $ / -11,35%  | 111,26 $ / 17,19%  | BASSO          | ALTO           |
| SOL     | 76,55 $   | Direzione più probabile a 30 giorni: | 73,86 $ / -3,51%   | 68,24 $ / -10,86%   | 90,35 $ / 18,03%   | BASSO          | ALTO           |
| DOGE    | 0.07000 $ | Direzione più probabile a 30 giorni: | 0.06000 $ / -9,09% | 0.06000 $ / -16,29% | 0.09000 $ / 23,55% | MEDIO          | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         33 |               3 |          30 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         33 |               3 |          30 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         33 |               3 |          30 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-07-11        | BTC     | 273,03 $          | 61.769,00 $ | 66.910,06 $ | 22523,52%        | 24406,49%        | RISCHIO STIMATO SEVERO |
| 2026-07-11        | SOL     | 78,01 $           | 70,69 $     | 78,88 $     | -9,38%           | 1,11%            | RISCHIO STIMATO SEVERO |
| 2026-07-11        | DOGE    | 0.08000 $         | 0.06797 $   | 0.07546 $   | -15,03%          | -5,67%           | RISCHIO STIMATO SEVERO |
| 2026-07-10        | BTC     | 165,05 $          | 61.769,00 $ | 66.910,06 $ | 37324,42%        | 40439,27%        | RISCHIO STIMATO SEVERO |
| 2026-07-10        | SOL     | 78,01 $           | 70,69 $     | 79,55 $     | -9,38%           | 1,98%            | RISCHIO STIMATO SEVERO |
| 2026-07-10        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07546 $   | -2,90%           | 7,81%            | RISCHIO STIMATO SEVERO |
| 2026-07-09        | BTC     | 241,08 $          | 61.645,75 $ | 66.910,06 $ | 25470,66%        | 27654,30%        | RISCHIO STIMATO SEVERO |
| 2026-07-09        | SOL     | 78,03 $           | 70,69 $     | 79,55 $     | -9,40%           | 1,95%            | RISCHIO STIMATO SEVERO |
| 2026-07-09        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07546 $   | -2,90%           | 7,81%            | RISCHIO STIMATO SEVERO |

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

