# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-21T05:05:45+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **19**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **677.39 R**
- Profitto virtuale mancato: **908.76 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 265 | 0 | 19506.99 |
| DOWN_20 | 265 | 0 | 39013.97 |
| DOWN_30 | 265 | 4 | 58562.09 |
| DOWN_40 | 265 | 92 | 73253.50 |
| UP_10 | 45 | 2 | 2845.42 |
| UP_20 | 45 | 3 | 5630.84 |
| UP_30 | 45 | 3 | 8330.66 |
| UP_40 | 45 | 18 | 10401.56 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
