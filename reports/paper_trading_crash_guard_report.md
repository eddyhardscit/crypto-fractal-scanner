# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-24T05:08:34+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **29**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **-25.29 R**
- Profitto virtuale mancato: **58.67 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 107 | 0 | 13397.01 |
| DOWN_20 | 107 | 0 | 26794.01 |
| DOWN_30 | 107 | 13 | 40377.29 |
| DOWN_40 | 107 | 29 | 50751.05 |
| UP_10 | 64 | 0 | 18300.64 |
| UP_20 | 64 | 0 | 36601.28 |
| UP_30 | 64 | 0 | 54901.93 |
| UP_40 | 64 | 36 | 65149.51 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
