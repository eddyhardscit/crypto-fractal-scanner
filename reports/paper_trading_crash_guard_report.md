# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-10T05:05:52+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **5**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **576.00 R**
- Profitto virtuale mancato: **1740.39 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 259 | 0 | 14529.21 |
| DOWN_20 | 259 | 0 | 29058.41 |
| DOWN_30 | 259 | 0 | 43587.62 |
| DOWN_40 | 259 | 61 | 55643.82 |
| UP_10 | 167 | 0 | 14539.36 |
| UP_20 | 167 | 0 | 29078.72 |
| UP_30 | 167 | 0 | 43618.08 |
| UP_40 | 167 | 97 | 51278.77 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
