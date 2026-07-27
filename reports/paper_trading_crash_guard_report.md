# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-27T05:08:38+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **63**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **44.54 R**
- Profitto virtuale mancato: **163.76 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 327 | 0 | 37076.27 |
| DOWN_20 | 327 | 0 | 74152.54 |
| DOWN_30 | 327 | 0 | 111228.81 |
| DOWN_40 | 327 | 154 | 135583.02 |
| UP_10 | 96 | 0 | 12853.31 |
| UP_20 | 96 | 0 | 25706.61 |
| UP_30 | 96 | 0 | 38559.92 |
| UP_40 | 96 | 46 | 46134.62 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
