# Calibrazione rischio spot / leva

Generato: **2026-09-03 05:32 UTC**

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
| BTC     | 185,68 $  | Direzione più probabile a 30 giorni: | 469,07 $ / -12,59%  | 797,28 $ / -16,05%  | 560,54 $ / 16,03%  | ALTO           | MOLTO ALTO     |
| SOL     | 99,93 $   | Direzione più probabile a 30 giorni: | 88,49 $ / -11,45%   | 74,03 $ / -25,92%   | 124,57 $ / 24,66%  | ALTO           | MOLTO ALTO     |
| DOGE    | 0.08000 $ | Direzione più probabile a 30 giorni: | 0.07000 $ / -11,98% | 0.06000 $ / -24,65% | 0.10000 $ / 15,74% | ALTO           | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         55 |              27 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         55 |              27 |          28 | RACCOLTA DATI | 3,70%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         55 |              27 |          28 | RACCOLTA DATI | 7,41%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-08-04        | DOGE    | 0.07000 $         | 0.06835 $   | 0.09998 $   | -2,36%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-04        | SOL     | 73,72 $           | 72,31 $     | 110,04 $    | -1,91%           | 49,27%           | RISCHIO STIMATO SEVERO |
| 2026-08-04        | BTC     | 845,82 $          | 62.487,70 $ | 81.346,95 $ | 7287,82%         | 9517,53%         | RISCHIO STIMATO SEVERO |
| 2026-08-03        | DOGE    | 0.07000 $         | 0.06835 $   | 0.09998 $   | -2,36%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-03        | SOL     | 72,93 $           | 71,96 $     | 110,04 $    | -1,33%           | 50,88%           | RISCHIO STIMATO SEVERO |
| 2026-08-03        | BTC     | 760,36 $          | 62.226,58 $ | 81.346,95 $ | 8083,83%         | 10598,48%        | RISCHIO STIMATO SEVERO |
| 2026-08-02        | SOL     | 73,42 $           | 71,87 $     | 110,04 $    | -2,12%           | 49,88%           | RISCHIO STIMATO SEVERO |
| 2026-08-02        | BTC     | 406,07 $          | 62.226,58 $ | 81.346,95 $ | 15224,10%        | 19932,74%        | RISCHIO STIMATO SEVERO |
| 2026-08-02        | DOGE    | 0.07000 $         | 0.06835 $   | 0.09998 $   | -2,36%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-01        | DOGE    | 0.07000 $         | 0.06797 $   | 0.09998 $   | -2,90%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-01        | SOL     | 73,12 $           | 70,69 $     | 110,04 $    | -3,32%           | 50,49%           | RISCHIO STIMATO SEVERO |
| 2026-08-01        | BTC     | 65,12 $           | 62.226,58 $ | 81.346,95 $ | 95456,78%        | 124818,54%       | RISCHIO STIMATO SEVERO |

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

