# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-30T05:06:21+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **34**
- Simulazioni bloccate attive: **43**
- Simulazioni completate nel ciclo: **24**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **569.84 R**
- Profitto virtuale mancato: **1212.82 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 236 | 0 | 24630.64 |
| DOWN_20 | 236 | 0 | 49261.28 |
| DOWN_30 | 236 | 3 | 73908.09 |
| DOWN_40 | 236 | 69 | 93075.96 |
| UP_10 | 133 | 0 | 14997.61 |
| UP_20 | 133 | 0 | 29995.22 |
| UP_30 | 133 | 0 | 44992.84 |
| UP_40 | 133 | 63 | 53940.97 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
