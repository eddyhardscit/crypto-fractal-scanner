# SOL Spot Adaptive Range — paper trading

Generato: 2026-07-14T03:40:42.017152+00:00

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
| Equity | €40.048,61 |
| Rendimento totale | +0,12% |
| Liquidità | €20.546,33 |
| SOL detenuti | 260.760540 |
| Valore SOL | €19.502,28 |
| Peso SOL attuale | 48.70% |
| Peso SOL obiettivo | 46.79% |
| P/L realizzato | €48,95 |
| Commissioni simulate | €43,12 |
| Drawdown massimo | -0,37% |
| Operazioni simulate | 12 |

## Range adattivo corrente

| Voce | Valore |
| --- | ---: |
| Prezzo SOL | €74,79 |
| Limite inferiore | €73,69 |
| Centro | €75,58 |
| Limite superiore | €77,47 |
| Semilarghezza | 2.50% |
| ATR | €0,26 (0.35%) |
| Regime | **STRONG_DOWNTREND** |
| Trend normalizzato ATR | -3.74 |
| EUR/USDT | 1.000000 (CONFIG_FALLBACK) |

La strategia aumenta gradualmente il peso SOL nella parte bassa del range e lo riduce nella parte alta. Il range si allarga con ATR e deviazione standard e viene inclinato dal trend, senza mai usare debito o vendere SOL non posseduti.

## Movimenti di questo ciclo

- **SELL** 22.193586 SOL a €75,15; controvalore €1.667,96, fee €1,67.
- **SELL** 33.887861 SOL a €75,42; controvalore €2.555,99, fee €2,56.
- **BUY** 27.144908 SOL a €75,18; controvalore €2.040,62, fee €2,04.
- **BUY** 26.300924 SOL a €74,93; controvalore €1.970,86, fee €1,97.
- **SELL** 34.597553 SOL a €75,19; controvalore €2.601,56, fee €2,60.
- **BUY** 49.136899 SOL a €74,74; controvalore €3.672,73, fee €3,67.

## Ultime operazioni

| # | Data UTC | Lato | Quantità SOL | Prezzo | Controvalore | P/L realizzato | Regime |
| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |
| 12 | 2026-07-14T03:00:00+00:00 | BUY | 49.136899 | €74,74 | €3.672,73 | €0,00 | STRONG_DOWNTREND |
| 11 | 2026-07-14T02:30:00+00:00 | SELL | 34.597553 | €75,19 | €2.601,56 | €11,59 | STRONG_DOWNTREND |
| 10 | 2026-07-14T02:15:00+00:00 | BUY | 26.300924 | €74,93 | €1.970,86 | €0,00 | STRONG_DOWNTREND |
| 9 | 2026-07-14T02:00:00+00:00 | BUY | 27.144908 | €75,18 | €2.040,62 | €0,00 | STRONG_DOWNTREND |
| 8 | 2026-07-14T00:45:00+00:00 | SELL | 33.887861 | €75,42 | €2.555,99 | €22,40 | STRONG_DOWNTREND |
| 7 | 2026-07-14T00:15:00+00:00 | SELL | 22.193586 | €75,15 | €1.667,96 | €8,69 | STRONG_DOWNTREND |
| 6 | 2026-07-13T23:45:00+00:00 | SELL | 34.020312 | €74,98 | €2.551,01 | €7,54 | STRONG_DOWNTREND |
| 5 | 2026-07-13T23:15:00+00:00 | SELL | 33.148331 | €74,73 | €2.477,01 | €-1,26 | STRONG_DOWNTREND |
| 4 | 2026-07-13T22:45:00+00:00 | BUY | 75.157265 | €74,52 | €5.601,09 | €0,00 | STRONG_DOWNTREND |
| 3 | 2026-07-13T22:30:00+00:00 | BUY | 80.278904 | €74,63 | €5.991,61 | €0,00 | STRONG_DOWNTREND |
| 2 | 2026-07-13T22:15:00+00:00 | BUY | 80.278276 | €74,65 | €5.993,17 | €0,00 | STRONG_DOWNTREND |
| 1 | 2026-07-13T22:00:00+00:00 | BUY | 80.311008 | €74,63 | €5.994,01 | €0,00 | STRONG_DOWNTREND |

## Nota metodologica

I risultati includono fee e slippage configurati, ma restano una simulazione. Non sono una promessa di rendimento e non attivano alcuna operazione sull'exchange.
