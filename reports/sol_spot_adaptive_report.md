# SOL Spot Adaptive Range — paper trading

Generato: 2026-07-13T22:16:51.516939+00:00

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
| Equity | €39.992,81 |
| Rendimento totale | -0,02% |
| Liquidità | €34.000,00 |
| SOL detenuti | 80.311008 |
| Valore SOL | €5.992,81 |
| Peso SOL attuale | 14.98% |
| Peso SOL obiettivo | 58.03% |
| P/L realizzato | €0,00 |
| Commissioni simulate | €5,99 |
| Drawdown massimo | -0,02% |
| Operazioni simulate | 1 |

## Range adattivo corrente

| Voce | Valore |
| --- | ---: |
| Prezzo SOL | €74,62 |
| Limite inferiore | €74,05 |
| Centro | €75,95 |
| Limite superiore | €77,85 |
| Semilarghezza | 2.50% |
| ATR | €0,29 (0.39%) |
| Regime | **STRONG_DOWNTREND** |
| Trend normalizzato ATR | -3.72 |
| EUR/USDT | 1.000000 (CONFIG_FALLBACK) |

La strategia aumenta gradualmente il peso SOL nella parte bassa del range e lo riduce nella parte alta. Il range si allarga con ATR e deviazione standard e viene inclinato dal trend, senza mai usare debito o vendere SOL non posseduti.

## Movimenti di questo ciclo

- **BUY** 80.311008 SOL a €74,63; controvalore €5.994,01, fee €5,99.

## Ultime operazioni

| # | Data UTC | Lato | Quantità SOL | Prezzo | Controvalore | P/L realizzato | Regime |
| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |
| 1 | 2026-07-13T22:00:00+00:00 | BUY | 80.311008 | €74,63 | €5.994,01 | €0,00 | STRONG_DOWNTREND |

## Nota metodologica

I risultati includono fee e slippage configurati, ma restano una simulazione. Non sono una promessa di rendimento e non attivano alcuna operazione sull'exchange.
