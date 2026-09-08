# Calibrazione rischio spot / leva

Generato: **2026-09-08 05:33 UTC**

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
| BTC     | 780,06 $  | Direzione più probabile a 30 giorni: | 30,20 $ / -9,84%    | 401,64 $ / -16,98%  | 436,66 $ / 26,22%  | MEDIO          | MOLTO ALTO     |
| SOL     | 103,29 $  | Direzione più probabile a 30 giorni: | 91,20 $ / -11,71%   | 78,90 $ / -23,61%   | 133,92 $ / 29,65%  | ALTO           | MOLTO ALTO     |
| DOGE    | 0.09000 $ | Direzione più probabile a 30 giorni: | 0.07000 $ / -18,23% | 0.06000 $ / -27,83% | 0.10000 $ / 11,15% | ALTO           | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato            | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:-----------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         60 |              32 |          28 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         60 |              32 |          28 | OSSERVAZIONE 30+ | 3,12%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         60 |              32 |          28 | OSSERVAZIONE 30+ | 6,25%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-08-09        | DOGE    | 0.07000 $         | 0.06895 $   | 0.09998 $   | -1,50%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-09        | SOL     | 75,95 $           | 74,20 $     | 110,04 $    | -2,30%           | 44,88%           | RISCHIO STIMATO SEVERO |
| 2026-08-09        | BTC     | 727,53 $          | 62.487,70 $ | 82.262,21 $ | 8489,02%         | 11207,05%        | RISCHIO STIMATO SEVERO |
| 2026-08-08        | DOGE    | 0.07000 $         | 0.06895 $   | 0.09998 $   | -1,50%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-08        | SOL     | 74,58 $           | 73,57 $     | 110,04 $    | -1,36%           | 47,54%           | RISCHIO STIMATO SEVERO |
| 2026-08-08        | BTC     | 959,70 $          | 62.487,70 $ | 82.262,21 $ | 6411,17%         | 8471,66%         | RISCHIO STIMATO SEVERO |
| 2026-08-07        | DOGE    | 0.07000 $         | 0.06887 $   | 0.09998 $   | -1,62%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-07        | SOL     | 72,65 $           | 72,47 $     | 110,04 $    | -0,25%           | 51,46%           | RISCHIO STIMATO SEVERO |
| 2026-08-07        | BTC     | 195,01 $          | 62.487,70 $ | 82.262,21 $ | 31943,33%        | 42083,59%        | RISCHIO STIMATO SEVERO |
| 2026-08-06        | BTC     | 847,90 $          | 62.487,70 $ | 82.262,21 $ | 7269,70%         | 9601,88%         | RISCHIO STIMATO SEVERO |
| 2026-08-06        | SOL     | 74,13 $           | 72,31 $     | 110,04 $    | -2,46%           | 48,44%           | RISCHIO STIMATO SEVERO |
| 2026-08-06        | DOGE    | 0.07000 $         | 0.06835 $   | 0.09998 $   | -2,36%           | 42,83%           | RISCHIO STIMATO SEVERO |

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

