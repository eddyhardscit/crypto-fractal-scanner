# Diagnostica fonti exchange alternative — V2.1.2b

Generato: **2026-07-11T09:35:39+00:00**

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
| Kraken | SOL | PF_SOLUSD | OK | SI | SI | SI | SI | SI | SI | SI | 100% |
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

| Fonte | Asset | Prezzo | Funding raw | OI base/raw | OI USD normalizzato | Taker B/S | Book 0,5% | Spread bps |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Kraken | BTC | 64,189.00 | -0.10217416 | 1,944.54 | 124.82 mln | 0.537 | 0.027 | 0.16 |
| Kraken | SOL | 77.930000 | -0.00006256 | 245,269.34 | 19.11 mln | 0.564 | -0.057 | 1.28 |
| Kraken | DOGE | 0.074243 | 0.00000148 | 41.97 mln | 3.12 mln | 0.948 | -0.058 | 2.56 |
| Bitget | BTC | 64,205.90 | -0.00002200 | 34,193.68 | 2.20 mld | 0.019 | 0.391 | 0.02 |
| Bitget | SOL | 77.924000 | 0.00007000 | 4.22 mln | 328.85 mln | 20.720 | -0.014 | 0.13 |
| Bitget | DOGE | 0.074230 | 0.00010000 | 1.08 mld | 79.93 mln | 0.214 | 0.159 | 1.35 |
| Okx | BTC | 64,208.60 | -0.00002012 | 30,866.86 | 1.98 mld | 4.176 | 0.004 | 0.02 |
| Okx | SOL | 77.910000 | -0.00005273 | 3.10 mln | 241.68 mln | 2.611 | 0.113 | 1.28 |
| Okx | DOGE | 0.074240 | 0.00009297 | 934.06 mln | 69.35 mln | 5.899 | 0.057 | 1.35 |
| Coinbase | BTC | 64,184.10 | n/a | n/a | n/a | 2.775 | -0.154 | 0.00 |
| Coinbase | SOL | 77.890000 | n/a | n/a | n/a | 0.164 | 0.094 | 1.28 |
| Coinbase | DOGE | 0.074220 | n/a | n/a | n/a | 0.627 | 0.211 | 1.35 |
| Kucoin | BTC | 64,232.30 | -0.00003400 | 29,284.25 | 1.88 mld | 0.237 | 0.016 | 0.02 |
| Kucoin | SOL | 77.904000 | -0.00000800 | 4.20 mln | 326.90 mln | 0.208 | 0.018 | 0.13 |
| Kucoin | DOGE | 0.074240 | 0.00006100 | 1.29 mld | 95.70 mln | 2.237 | -0.096 | 1.35 |

## Errori e blocchi

Nessun errore HTTP/API rilevato nei test eseguiti.

## Regole per la scelta finale

- Una fonte derivati è candidata soltanto se trova BTC, SOL e DOGE e restituisce almeno prezzo, funding, OI, trade e order book.
- Kraken, Bitget e OKX possono sostituire Binance/Bybit solo dopo questo test reale sul runner GitHub.
- Coinbase resta una conferma spot: non viene contato come fonte di funding o open interest.
- KuCoin è il controllo già operativo.
- Nessun peso exchange viene attivato da questo workflow diagnostico.

File tecnici: `alternative_exchange_source_diagnostics.json`, `alternative_exchange_source_capabilities.csv`, `alternative_exchange_source_samples.json`.
