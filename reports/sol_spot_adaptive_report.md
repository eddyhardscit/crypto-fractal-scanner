# SOL Spot Adaptive Range — paper trading

Generato: 2026-07-14T08:25:13.299663+00:00

## Vincoli di sicurezza

- Modalità: **PAPER ONLY**
- Asset: **SOL soltanto**
- Mercato simulato: **spot SOL-USDT**
- Capitale iniziale: **€40.000**
- Leva: **1× (nessuna leva)**
- Short: **disabilitati**
- Ordini reali: **impossibili; il codice usa soltanto dati pubblici GET**

## Stato portafoglio

| Voce | Valore |
| --- | ---: |
| Equity | €40.112,88 |
| Rendimento totale | +0,28% |
| Liquidità | €25.876,25 |
| SOL detenuti | 189.720635 |
| Valore SOL | €14.236,64 |
| Peso SOL attuale | 35.49% |
| Peso SOL obiettivo | 36.79% |
| P/L realizzato | €75,90 |
| Commissioni simulate | €51,87 |
| Drawdown massimo | -0,37% |
| Operazioni simulate | 16 |

## Range adattivo corrente

| Voce | Valore |
| --- | ---: |
| Prezzo SOL | €75,04 |
| Limite inferiore | €73,48 |
| Centro | €75,36 |
| Limite superiore | €77,24 |
| Semilarghezza | 2.50% |
| ATR | €0,22 (0.30%) |
| Regime | **STRONG_DOWNTREND** |
| Trend normalizzato ATR | -3.64 |
| EUR/USDT | 1.000000 (CONFIG_FALLBACK) |

La strategia aumenta gradualmente il peso SOL nella parte bassa del range e lo riduce nella parte alta. Il range si allarga con ATR e deviazione standard e viene inclinato dal trend, senza mai usare debito o vendere SOL non posseduti.

## Movimenti di questo ciclo

- **BUY** 22.728467 SOL a €75,17; controvalore €1.708,39, fee €1,71.

## Ultime operazioni

| # | Data UTC | Lato | Quantità SOL | Prezzo | Controvalore | P/L realizzato | Regime |
| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |
| 16 | 2026-07-14T06:45:00+00:00 | BUY | 22.728467 | €75,17 | €1.708,39 | €0,00 | STRONG_DOWNTREND |
| 15 | 2026-07-14T05:00:00+00:00 | SELL | 33.475091 | €75,37 | €2.523,18 | €17,01 | STRONG_DOWNTREND |
| 14 | 2026-07-14T03:45:00+00:00 | SELL | 23.470530 | €75,13 | €1.763,46 | €6,30 | STRONG_DOWNTREND |
| 13 | 2026-07-14T03:30:00+00:00 | SELL | 36.822752 | €74,97 | €2.760,42 | €3,64 | STRONG_DOWNTREND |
| 12 | 2026-07-14T03:00:00+00:00 | BUY | 49.136899 | €74,74 | €3.672,73 | €0,00 | STRONG_DOWNTREND |
| 11 | 2026-07-14T02:30:00+00:00 | SELL | 34.597553 | €75,19 | €2.601,56 | €11,59 | STRONG_DOWNTREND |
| 10 | 2026-07-14T02:15:00+00:00 | BUY | 26.300924 | €74,93 | €1.970,86 | €0,00 | STRONG_DOWNTREND |
| 9 | 2026-07-14T02:00:00+00:00 | BUY | 27.144908 | €75,18 | €2.040,62 | €0,00 | STRONG_DOWNTREND |
| 8 | 2026-07-14T00:45:00+00:00 | SELL | 33.887861 | €75,42 | €2.555,99 | €22,40 | STRONG_DOWNTREND |
| 7 | 2026-07-14T00:15:00+00:00 | SELL | 22.193586 | €75,15 | €1.667,96 | €8,69 | STRONG_DOWNTREND |
| 6 | 2026-07-13T23:45:00+00:00 | SELL | 34.020312 | €74,98 | €2.551,01 | €7,54 | STRONG_DOWNTREND |
| 5 | 2026-07-13T23:15:00+00:00 | SELL | 33.148331 | €74,73 | €2.477,01 | €-1,26 | STRONG_DOWNTREND |

## Nota metodologica

I risultati includono fee e slippage configurati, ma restano una simulazione. Non sono una promessa di rendimento e non attivano alcuna operazione sull'exchange.
