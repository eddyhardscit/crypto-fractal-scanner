# Calibrazione rischio spot / leva

Generato: **2026-09-02 05:32 UTC**

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
| BTC     | 666,99 $  | Direzione più probabile a 30 giorni: | 636,28 $ / -12,92%  | 694,50 $ / -19,28%  | 689,52 $ / 15,48%  | ALTO           | MOLTO ALTO     |
| SOL     | 100,24 $  | Direzione più probabile a 30 giorni: | 87,62 $ / -12,59%   | 79,37 $ / -20,82%   | 126,04 $ / 25,74%  | ALTO           | MOLTO ALTO     |
| DOGE    | 0.08000 $ | Direzione più probabile a 30 giorni: | 0.07000 $ / -10,59% | 0.06000 $ / -23,00% | 0.10000 $ / 17,43% | ALTO           | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         54 |              26 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         54 |              26 |          28 | RACCOLTA DATI | 3,85%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         54 |              26 |          28 | RACCOLTA DATI | 7,69%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-08-03        | DOGE    | 0.07000 $         | 0.06835 $   | 0.09998 $   | -2,36%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-03        | SOL     | 72,93 $           | 71,96 $     | 110,04 $    | -1,33%           | 50,88%           | RISCHIO STIMATO SEVERO |
| 2026-08-03        | BTC     | 760,36 $          | 62.226,58 $ | 81.346,95 $ | 8083,83%         | 10598,48%        | RISCHIO STIMATO SEVERO |
| 2026-08-02        | DOGE    | 0.07000 $         | 0.06835 $   | 0.09998 $   | -2,36%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-02        | SOL     | 73,42 $           | 71,87 $     | 110,04 $    | -2,12%           | 49,88%           | RISCHIO STIMATO SEVERO |
| 2026-08-02        | BTC     | 406,07 $          | 62.226,58 $ | 81.346,95 $ | 15224,10%        | 19932,74%        | RISCHIO STIMATO SEVERO |
| 2026-08-01        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09998 $   | -2,90%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-01        | SOL     | 73,12 $           | 70,69 $     | 110,04 $    | -3,32%           | 50,49%           | RISCHIO STIMATO SEVERO |
| 2026-08-01        | BTC     | 65,12 $           | 62.226,58 $ | 81.346,95 $ | 95456,78%        | 124818,54%       | RISCHIO STIMATO SEVERO |
| 2026-07-31        | SOL     | 74,00 $           | 70,69 $     | 110,04 $    | -4,47%           | 48,70%           | RISCHIO STIMATO SEVERO |
| 2026-07-31        | BTC     | 329,85 $          | 62.226,58 $ | 81.235,03 $ | 18765,11%        | 24527,87%        | RISCHIO STIMATO SEVERO |
| 2026-07-31        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09998 $   | -2,90%           | 42,83%           | RISCHIO STIMATO SEVERO |

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

