# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-15T05:05:52+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **191**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **480.99 R**
- Profitto virtuale mancato: **744.61 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 259 | 0 | 25060.48 |
| DOWN_20 | 259 | 0 | 50120.95 |
| DOWN_30 | 259 | 4 | 75217.89 |
| DOWN_40 | 259 | 81 | 95233.38 |
| UP_10 | 149 | 0 | 20700.98 |
| UP_20 | 149 | 0 | 41401.97 |
| UP_30 | 149 | 0 | 62102.95 |
| UP_40 | 149 | 60 | 76820.63 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
