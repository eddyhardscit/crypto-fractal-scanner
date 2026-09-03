# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-03T05:05:54+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **53**
- Simulazioni completate nel ciclo: **6**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **584.45 R**
- Profitto virtuale mancato: **1497.29 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 266 | 0 | 15593.84 |
| DOWN_20 | 266 | 0 | 31187.69 |
| DOWN_30 | 266 | 1 | 46782.39 |
| DOWN_40 | 266 | 87 | 58024.22 |
| UP_10 | 131 | 0 | 10813.26 |
| UP_20 | 131 | 0 | 21626.52 |
| UP_30 | 131 | 0 | 32439.78 |
| UP_40 | 131 | 58 | 39069.46 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
