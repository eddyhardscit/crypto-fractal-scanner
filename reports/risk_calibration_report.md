# Calibrazione rischio spot / leva

Generato: **2026-09-12 05:32 UTC**

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
| BTC     | 219,04 $  | Direzione più probabile a 30 giorni: | 127,22 $ / -5,30%   | 654,17 $ / -12,39%  | 822,69 $ / 39,63%  | BASSO          | ALTO           |
| SOL     | 101,55 $  | Direzione più probabile a 30 giorni: | 95,13 $ / -6,32%    | 79,21 $ / -22,00%   | 143,60 $ / 41,41%  | ALTO           | MOLTO ALTO     |
| DOGE    | 0.08000 $ | Direzione più probabile a 30 giorni: | 0.07000 $ / -17,80% | 0.06000 $ / -28,13% | 0.09000 $ / 10,90% | ALTO           | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato            | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:-----------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         64 |              34 |          30 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         64 |              34 |          30 | OSSERVAZIONE 30+ | 2,94%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         64 |              34 |          30 | OSSERVAZIONE 30+ | 5,88%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-08-11        | DOGE    | 0.07000 $         | 0.06895 $   | 0.09998 $   | -1,50%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-11        | SOL     | 75,98 $           | 74,20 $     | 110,04 $    | -2,34%           | 44,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-11        | BTC     | 976,47 $          | 62.487,70 $ | 82.262,21 $ | 6299,35%         | 8324,45%         | RISCHIO STIMATO SEVERO |
| 2026-08-10        | DOGE    | 0.07000 $         | 0.06895 $   | 0.09998 $   | -1,50%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-10        | SOL     | 76,55 $           | 74,20 $     | 110,04 $    | -3,06%           | 43,75%           | RISCHIO STIMATO SEVERO |
| 2026-08-10        | BTC     | 946,42 $          | 62.487,70 $ | 82.262,21 $ | 6502,53%         | 8591,93%         | RISCHIO STIMATO SEVERO |
| 2026-08-09        | DOGE    | 0.07000 $         | 0.06895 $   | 0.09998 $   | -1,50%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-09        | SOL     | 75,95 $           | 74,20 $     | 110,04 $    | -2,30%           | 44,88%           | RISCHIO STIMATO SEVERO |
| 2026-08-09        | BTC     | 727,53 $          | 62.487,70 $ | 82.262,21 $ | 8489,02%         | 11207,05%        | RISCHIO STIMATO SEVERO |
| 2026-08-08        | DOGE    | 0.07000 $         | 0.06895 $   | 0.09998 $   | -1,50%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-08        | SOL     | 74,58 $           | 73,57 $     | 110,04 $    | -1,36%           | 47,54%           | RISCHIO STIMATO SEVERO |
| 2026-08-08        | BTC     | 959,70 $          | 62.487,70 $ | 82.262,21 $ | 6411,17%         | 8471,66%         | RISCHIO STIMATO SEVERO |

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

