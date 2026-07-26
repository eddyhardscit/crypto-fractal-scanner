# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-26T05:08:37+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **5**
- Simulazioni bloccate attive: **72**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **22.58 R**
- Profitto virtuale mancato: **150.37 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 294 | 0 | 22393.44 |
| DOWN_20 | 294 | 0 | 44786.88 |
| DOWN_30 | 294 | 5 | 67266.80 |
| DOWN_40 | 294 | 118 | 84162.98 |
| UP_10 | 91 | 6 | 13342.81 |
| UP_20 | 91 | 9 | 26505.62 |
| UP_30 | 91 | 9 | 39424.22 |
| UP_40 | 91 | 40 | 46829.62 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
