# Diagnostica fonti exchange alternative — V2.1.2

Generato: **2026-07-11T09:21:40+00:00**

Questo test non modifica Global Confluence, Decision Report o previsioni. Verifica soltanto accessibilità, mercati e campi pubblici dal runner GitHub reale.

## Verdetto automatico

**PRONTO PER INTEGRAZIONE SENZA VPS** — Nucleo proposto: KuCoin + Kraken + Bitget.
Coinbase spot è utilizzabile come conferma aggiuntiva di book e flusso eseguito.

## Sintesi per fonte

| Fonte | Mercato | Asset trovati | Copertura campi | Stato asset | Lettura |
| --- | --- | ---: | ---: | --- | --- |
| Kraken | perpetual | 3/3 | 100% | OK | candidato derivati |
| Bitget | perpetual | 3/3 | 100% | OK | candidato derivati |
| Okx | perpetual | 3/3 | 86% | OK | candidato derivati |
| Coinbase | spot | 3/3 | 43% | PARZIALE | conferma spot |
| Kucoin | perpetual-control | 3/3 | 100% | OK | candidato derivati |

## Matrice asset / capacità

| Fonte | Asset | Simbolo | Stato | Prezzo | Mark | Index | Funding | OI | Trade | Book | Copertura |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| Kraken | BTC | PF_XBTUSD | OK | SI | SI | SI | SI | SI | SI | SI | 100% |
| Kraken | SOL | PF_SOLVUSD | OK | SI | SI | SI | SI | SI | SI | SI | 100% |
| Kraken | DOGE | PF_DOGEUSD | OK | SI | SI | SI | SI | SI | SI | SI | 100% |
| Bitget | BTC | BTCUSDT | OK | SI | SI | SI | SI | SI | SI | SI | 100% |
| Bitget | SOL | SOLUSDT | OK | SI | SI | SI | SI | SI | SI | SI | 100% |
| Bitget | DOGE | DOGEUSDT | OK | SI | SI | SI | SI | SI | SI | SI | 100% |
| Okx | BTC | BTC-USDT-SWAP | OK | SI | SI | NO | SI | SI | SI | SI | 86% |
| Okx | SOL | SOL-USDT-SWAP | OK | SI | SI | NO | SI | SI | SI | SI | 86% |
| Okx | DOGE | DOGE-USDT-SWAP | OK | SI | SI | NO | SI | SI | SI | SI | 86% |
| Coinbase | BTC | BTC-USD | PARZIALE | SI | NO | NO | NO | NO | SI | SI | 43% |
| Coinbase | SOL | SOL-USD | PARZIALE | SI | NO | NO | NO | NO | SI | SI | 43% |
| Coinbase | DOGE | DOGE-USD | PARZIALE | SI | NO | NO | NO | NO | SI | SI | 43% |
| Kucoin | BTC | XBTUSDTM | OK | SI | SI | SI | SI | SI | SI | SI | 100% |
| Kucoin | SOL | SOLUSDTM | OK | SI | SI | SI | SI | SI | SI | SI | 100% |
| Kucoin | DOGE | DOGEUSDTM | OK | SI | SI | SI | SI | SI | SI | SI | 100% |

## Campioni principali

| Fonte | Asset | Prezzo | Funding raw | OI raw/USD | Taker B/S | Book 0,5% | Spread bps |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Kraken | BTC | 64,193.00 | -0.10217416 | n/a | 5.624 | -0.000 | 0.16 |
| Kraken | SOL | 0.002776 | -0.00000041 | n/a | 1.050 | 0.023 | 83.16 |
| Kraken | DOGE | 0.074309 | 0.00000148 | n/a | 2.125 | 0.011 | 2.83 |
| Bitget | BTC | 64,206.90 | -0.00002100 | 34,216.84 | 5.593 | -0.014 | 0.02 |
| Bitget | SOL | 78.091000 | 0.00007400 | 4.23 mln | 0.218 | 0.073 | 0.13 |
| Bitget | DOGE | 0.074280 | 0.00010000 | 1.08 mld | 0.592 | 0.013 | 1.35 |
| Okx | BTC | 64,205.00 | -0.00002165 | 1.98 mld | 1.106 | 0.388 | 0.02 |
| Okx | SOL | 78.080000 | -0.00004761 | 242.66 mln | 0.149 | 0.092 | 1.28 |
| Okx | DOGE | 0.074290 | 0.00009711 | 69.34 mln | 0.922 | 0.033 | 1.35 |
| Coinbase | BTC | 64,191.40 | n/a | n/a | 3.716 | -0.164 | 0.00 |
| Coinbase | SOL | 78.070000 | n/a | n/a | 0.342 | -0.025 | 1.28 |
| Coinbase | DOGE | 0.074270 | n/a | n/a | 2.555 | 0.047 | 1.35 |
| Kucoin | BTC | 64,234.20 | -0.00003600 | 29,256.82 | 6.871 | 0.008 | 0.02 |
| Kucoin | SOL | 78.086000 | -0.00000800 | 4.20 mln | 0.553 | -0.012 | 0.13 |
| Kucoin | DOGE | 0.074290 | 0.00006300 | 1.29 mld | 1.858 | 0.063 | 1.35 |

## Errori e blocchi

Nessun errore HTTP/API rilevato nei test eseguiti.

## Regole per la scelta finale

- Una fonte derivati è candidata soltanto se trova BTC, SOL e DOGE e restituisce almeno prezzo, funding, OI, trade e order book.
- Kraken, Bitget e OKX possono sostituire Binance/Bybit solo dopo questo test reale sul runner GitHub.
- Coinbase resta una conferma spot: non viene contato come fonte di funding o open interest.
- KuCoin è il controllo già operativo.
- Nessun peso exchange viene attivato da questo workflow diagnostico.

File tecnici: `alternative_exchange_source_diagnostics.json`, `alternative_exchange_source_capabilities.csv`, `alternative_exchange_source_samples.json`.
