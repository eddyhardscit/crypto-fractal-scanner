# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-13T05:06:02+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **35**
- Simulazioni bloccate attive: **72**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **576.00 R**
- Profitto virtuale mancato: **1740.39 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 250 | 0 | 15541.92 |
| DOWN_20 | 250 | 0 | 31083.84 |
| DOWN_30 | 250 | 3 | 46629.50 |
| DOWN_40 | 250 | 63 | 59389.39 |
| UP_10 | 150 | 0 | 11064.81 |
| UP_20 | 150 | 0 | 22129.62 |
| UP_30 | 150 | 9 | 33752.12 |
| UP_40 | 150 | 80 | 39339.02 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
