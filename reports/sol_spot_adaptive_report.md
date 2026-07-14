# SOL Spot Adaptive Range — paper trading

Generato: 2026-07-14T00:11:12.193630+00:00

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
| Equity | €40.083,80 |
| Rendimento totale | +0,21% |
| Liquidità | €21.419,54 |
| SOL detenuti | 248.856811 |
| Valore SOL | €18.664,26 |
| Peso SOL attuale | 46.56% |
| Peso SOL obiettivo | 46.56% |
| P/L realizzato | €6,27 |
| Commissioni simulate | €28,61 |
| Drawdown massimo | -0,14% |
| Operazioni simulate | 6 |

## Range adattivo corrente

| Voce | Valore |
| --- | ---: |
| Prezzo SOL | €75,00 |
| Limite inferiore | €73,89 |
| Centro | €75,78 |
| Limite superiore | €77,68 |
| Semilarghezza | 2.50% |
| ATR | €0,27 (0.36%) |
| Regime | **STRONG_DOWNTREND** |
| Trend normalizzato ATR | -4.12 |
| EUR/USDT | 1.000000 (CONFIG_FALLBACK) |

La strategia aumenta gradualmente il peso SOL nella parte bassa del range e lo riduce nella parte alta. Il range si allarga con ATR e deviazione standard e viene inclinato dal trend, senza mai usare debito o vendere SOL non posseduti.

## Movimenti di questo ciclo

- **SELL** 33.148331 SOL a €74,73; controvalore €2.477,01, fee €2,48.
- **SELL** 34.020312 SOL a €74,98; controvalore €2.551,01, fee €2,55.

## Ultime operazioni

| # | Data UTC | Lato | Quantità SOL | Prezzo | Controvalore | P/L realizzato | Regime |
| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |
| 6 | 2026-07-13T23:45:00+00:00 | SELL | 34.020312 | €74,98 | €2.551,01 | €7,54 | STRONG_DOWNTREND |
| 5 | 2026-07-13T23:15:00+00:00 | SELL | 33.148331 | €74,73 | €2.477,01 | €-1,26 | STRONG_DOWNTREND |
| 4 | 2026-07-13T22:45:00+00:00 | BUY | 75.157265 | €74,52 | €5.601,09 | €0,00 | STRONG_DOWNTREND |
| 3 | 2026-07-13T22:30:00+00:00 | BUY | 80.278904 | €74,63 | €5.991,61 | €0,00 | STRONG_DOWNTREND |
| 2 | 2026-07-13T22:15:00+00:00 | BUY | 80.278276 | €74,65 | €5.993,17 | €0,00 | STRONG_DOWNTREND |
| 1 | 2026-07-13T22:00:00+00:00 | BUY | 80.311008 | €74,63 | €5.994,01 | €0,00 | STRONG_DOWNTREND |

## Nota metodologica

I risultati includono fee e slippage configurati, ma restano una simulazione. Non sono una promessa di rendimento e non attivano alcuna operazione sull'exchange.
