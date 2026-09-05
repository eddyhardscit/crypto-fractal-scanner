# Calibrazione rischio spot / leva

Generato: **2026-09-05 08:22 UTC**

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
| BTC     | 667,15 $  | Direzione più probabile a 30 giorni: | 341,49 $ / -11,71%  | 411,13 $ / -17,89%  | 395,24 $ / 21,00%  | MEDIO          | MOLTO ALTO     |
| SOL     | 102,31 $  | Direzione più probabile a 30 giorni: | 89,17 $ / -12,84%   | 76,65 $ / -25,08%   | 128,93 $ / 26,02%  | ALTO           | MOLTO ALTO     |
| DOGE    | 0.09000 $ | Direzione più probabile a 30 giorni: | 0.07000 $ / -20,03% | 0.06000 $ / -30,05% | 0.09000 $ / 10,62% | MOLTO ALTO     | MOLTO ALTO     |

## Stato calibrazione rischio

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio                |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:----------------------------|
| BTC     |         57 |              29 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         57 |              29 |          28 | RACCOLTA DATI | 3,45%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         57 |              29 |          28 | RACCOLTA DATI | 6,90%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

## Ultimi controlli completati

| Data previsione   | Asset   | Prezzo iniziale   | Min reale   | Max reale   | Drawdown reale   | Max gain reale   | Risultato rischio      |
|:------------------|:--------|:------------------|:------------|:------------|:-----------------|:-----------------|:-----------------------|
| 2026-08-06        | DOGE    | 0.07000 $         | 0.06835 $   | 0.09998 $   | -2,36%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-06        | SOL     | 74,13 $           | 72,31 $     | 110,04 $    | -2,46%           | 48,44%           | RISCHIO STIMATO SEVERO |
| 2026-08-06        | BTC     | 847,90 $          | 62.487,70 $ | 82.262,21 $ | 7269,70%         | 9601,88%         | RISCHIO STIMATO SEVERO |
| 2026-08-05        | DOGE    | 0.07000 $         | 0.06835 $   | 0.09998 $   | -2,36%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-05        | SOL     | 73,91 $           | 72,31 $     | 110,04 $    | -2,17%           | 48,88%           | RISCHIO STIMATO SEVERO |
| 2026-08-05        | BTC     | 258,42 $          | 62.487,70 $ | 81.392,30 $ | 24080,67%        | 31396,13%        | RISCHIO STIMATO SEVERO |
| 2026-08-04        | SOL     | 73,72 $           | 72,31 $     | 110,04 $    | -1,91%           | 49,27%           | RISCHIO STIMATO SEVERO |
| 2026-08-04        | BTC     | 845,82 $          | 62.487,70 $ | 81.346,95 $ | 7287,82%         | 9517,53%         | RISCHIO STIMATO SEVERO |
| 2026-08-04        | DOGE    | 0.07000 $         | 0.06835 $   | 0.09998 $   | -2,36%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-03        | DOGE    | 0.07000 $         | 0.06835 $   | 0.09998 $   | -2,36%           | 42,83%           | RISCHIO STIMATO SEVERO |
| 2026-08-03        | SOL     | 72,93 $           | 71,96 $     | 110,04 $    | -1,33%           | 50,88%           | RISCHIO STIMATO SEVERO |
| 2026-08-03        | BTC     | 760,36 $          | 62.226,58 $ | 81.346,95 $ | 8083,83%         | 10598,48%        | RISCHIO STIMATO SEVERO |

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

