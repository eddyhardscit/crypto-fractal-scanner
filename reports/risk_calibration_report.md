# Calibrazione rischio spot / leva

Generato: **2026-08-09 05:17 UTC**

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
| BTC     | 727,53 $  | Direzione più probabile a 30 giorni: | 630,64 $ / -1,69%  | 10,47 $ / -5,74%    | 434,88 $ / 18,09%  | BASSO          | BASSO          |
| SOL     | 75,95 $   | Direzione più probabile a 30 giorni: | 73,21 $ / -3,61%   | 67,31 $ / -11,37%   | 89,64 $ / 18,03%   | BASSO          | ALTO           |
| DOGE    | 0.07000 $ | Direzione più probabile a 30 giorni: | 0.06000 $ / -9,85% | 0.05000 $ / -21,63% | 0.09000 $ / 22,03% | MEDIO          | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         32 |               2 |          30 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         32 |               2 |          30 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         32 |               2 |          30 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
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

