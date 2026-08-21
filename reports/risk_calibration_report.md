# Calibrazione rischio spot / leva

Generato: **2026-08-21 05:32 UTC**

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
| BTC     | 133,45 $  | Direzione più probabile a 30 giorni: | 706,56 $ / -7,22%   | 44,26 $ / -13,43%   | 8,89 $ / 17,14%    | MEDIO          | ALTO           |
| SOL     | 89,55 $   | Direzione più probabile a 30 giorni: | 82,16 $ / -8,26%    | 78,63 $ / -12,19%   | 100,09 $ / 11,77%  | MEDIO          | MOLTO ALTO     |
| DOGE    | 0.08000 $ | Direzione più probabile a 30 giorni: | 0.07000 $ / -12,04% | 0.07000 $ / -20,96% | 0.10000 $ / 17,97% | ALTO           | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         42 |              14 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         42 |              14 |          28 | RACCOLTA DATI | 7,14%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         42 |              14 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-07-22        | DOGE    | 0.07000 $         | 0.06797 $   | 0.08268 $   | -2,90%           | 18,11%           | RISCHIO STIMATO SEVERO |
| 2026-07-22        | SOL     | 77,84 $           | 70,69 $     | 89,94 $     | -9,18%           | 15,55%           | RISCHIO STIMATO SEVERO |
| 2026-07-22        | BTC     | 220,37 $          | 62.226,58 $ | 75.567,51 $ | 28137,32%        | 34191,20%        | RISCHIO STIMATO SEVERO |
| 2026-07-21        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07585 $   | -2,90%           | 8,36%            | RISCHIO STIMATO SEVERO |
| 2026-07-21        | SOL     | 78,18 $           | 70,69 $     | 85,63 $     | -9,58%           | 9,53%            | RISCHIO STIMATO SEVERO |
| 2026-07-21        | BTC     | 471,66 $          | 62.226,58 $ | 69.786,68 $ | 13093,10%        | 14695,97%        | RISCHIO STIMATO SEVERO |
| 2026-07-20        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07380 $   | -2,90%           | 5,43%            | RISCHIO STIMATO SEVERO |
| 2026-07-20        | SOL     | 75,92 $           | 70,69 $     | 78,73 $     | -6,88%           | 3,70%            | RISCHIO STIMATO SEVERO |
| 2026-07-20        | BTC     | 149,77 $          | 62.226,58 $ | 66.910,06 $ | 41448,09%        | 44575,21%        | RISCHIO STIMATO SEVERO |
| 2026-07-19        | SOL     | 76,00 $           | 70,69 $     | 78,73 $     | -6,98%           | 3,59%            | RISCHIO STIMATO SEVERO |
| 2026-07-19        | BTC     | 723,48 $          | 62.226,58 $ | 66.910,06 $ | 8501,01%         | 9148,36%         | RISCHIO STIMATO SEVERO |
| 2026-07-19        | DOGE    | 0.07000 $         | 0.06797 $   | 0.07380 $   | -2,90%           | 5,43%            | RISCHIO STIMATO SEVERO |

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

