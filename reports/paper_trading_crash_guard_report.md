# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-07T05:06:15+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **72**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **511.56 R**
- Profitto virtuale mancato: **1738.91 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 356 | 0 | 20667.18 |
| DOWN_20 | 356 | 0 | 41334.36 |
| DOWN_30 | 356 | 3 | 62007.24 |
| DOWN_40 | 356 | 107 | 77236.78 |
| UP_10 | 104 | 0 | 7220.96 |
| UP_20 | 104 | 0 | 14441.93 |
| UP_30 | 104 | 0 | 21662.89 |
| UP_40 | 104 | 46 | 26414.02 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
