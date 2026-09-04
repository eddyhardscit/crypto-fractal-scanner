# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-04T05:05:54+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **25**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **532.07 R**
- Profitto virtuale mancato: **1569.87 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 342 | 0 | 20546.70 |
| DOWN_20 | 342 | 0 | 41093.40 |
| DOWN_30 | 342 | 0 | 61640.10 |
| DOWN_40 | 342 | 111 | 75271.36 |
| UP_10 | 97 | 0 | 6112.61 |
| UP_20 | 97 | 0 | 12225.22 |
| UP_30 | 97 | 9 | 18895.52 |
| UP_40 | 97 | 44 | 22862.94 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
