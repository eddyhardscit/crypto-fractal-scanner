# SOL Spot Adaptive Range — paper trading

Generato: 2026-07-13T23:07:58.430823+00:00

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
| Equity | €39.943,60 |
| Rendimento totale | -0,14% |
| Liquidità | €16.396,55 |
| SOL detenuti | 316.025453 |
| Valore SOL | €23.547,06 |
| Peso SOL attuale | 58.95% |
| Peso SOL obiettivo | 58.96% |
| P/L realizzato | €0,00 |
| Commissioni simulate | €23,58 |
| Drawdown massimo | -0,14% |
| Operazioni simulate | 4 |

## Range adattivo corrente

| Voce | Valore |
| --- | ---: |
| Prezzo SOL | €74,51 |
| Limite inferiore | €73,99 |
| Centro | €75,88 |
| Limite superiore | €77,78 |
| Semilarghezza | 2.50% |
| ATR | €0,28 (0.37%) |
| Regime | **STRONG_DOWNTREND** |
| Trend normalizzato ATR | -4.02 |
| EUR/USDT | 1.000000 (CONFIG_FALLBACK) |

La strategia aumenta gradualmente il peso SOL nella parte bassa del range e lo riduce nella parte alta. Il range si allarga con ATR e deviazione standard e viene inclinato dal trend, senza mai usare debito o vendere SOL non posseduti.

## Movimenti di questo ciclo

- **BUY** 80.278276 SOL a €74,65; controvalore €5.993,17, fee €5,99.
- **BUY** 80.278904 SOL a €74,63; controvalore €5.991,61, fee €5,99.
- **BUY** 75.157265 SOL a €74,52; controvalore €5.601,09, fee €5,60.

## Ultime operazioni

| # | Data UTC | Lato | Quantità SOL | Prezzo | Controvalore | P/L realizzato | Regime |
| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |
| 4 | 2026-07-13T22:45:00+00:00 | BUY | 75.157265 | €74,52 | €5.601,09 | €0,00 | STRONG_DOWNTREND |
| 3 | 2026-07-13T22:30:00+00:00 | BUY | 80.278904 | €74,63 | €5.991,61 | €0,00 | STRONG_DOWNTREND |
| 2 | 2026-07-13T22:15:00+00:00 | BUY | 80.278276 | €74,65 | €5.993,17 | €0,00 | STRONG_DOWNTREND |
| 1 | 2026-07-13T22:00:00+00:00 | BUY | 80.311008 | €74,63 | €5.994,01 | €0,00 | STRONG_DOWNTREND |

## Nota metodologica

I risultati includono fee e slippage configurati, ma restano una simulazione. Non sono una promessa di rendimento e non attivano alcuna operazione sull'exchange.
