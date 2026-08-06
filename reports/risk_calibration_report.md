# Calibrazione rischio spot / leva

Generato: **2026-08-06 05:16 UTC**

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
| BTC     | 847,90 $  | Direzione più probabile a 30 giorni: | 795,10 $ / -4,71%   | 424,57 $ / -12,99%  | 54,54 $ / 12,66%   | BASSO          | ALTO           |
| SOL     | 74,13 $   | Direzione più probabile a 30 giorni: | 71,22 $ / -3,92%    | 63,08 $ / -14,90%   | 83,11 $ / 12,12%   | MEDIO          | ALTO           |
| DOGE    | 0.07000 $ | Direzione più probabile a 30 giorni: | 0.06000 $ / -13,85% | 0.06000 $ / -20,32% | 0.08000 $ / 14,49% | ALTO           | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio   |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:---------------|
| BTC     |         29 |               0 |          29 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| SOL     |         29 |               0 |          29 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| DOGE    |         29 |               0 |          29 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |

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

