# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-19T05:05:45+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **62**
- Simulazioni completate nel ciclo: **1**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **620.39 R**
- Profitto virtuale mancato: **908.76 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 182 | 0 | 25019.09 |
| DOWN_20 | 182 | 0 | 50038.17 |
| DOWN_30 | 182 | 2 | 75087.25 |
| DOWN_40 | 182 | 54 | 94695.81 |
| UP_10 | 155 | 0 | 21398.42 |
| UP_20 | 155 | 0 | 42796.83 |
| UP_30 | 155 | 0 | 64195.25 |
| UP_40 | 155 | 67 | 78982.61 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
