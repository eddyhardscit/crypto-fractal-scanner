# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-23T07:34:57+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **16**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **14.15 R**
- Profitto virtuale mancato: **0.00 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 114 | 0 | 17486.86 |
| DOWN_20 | 114 | 0 | 34973.73 |
| DOWN_30 | 114 | 0 | 52460.59 |
| DOWN_40 | 114 | 27 | 66168.81 |
| UP_10 | 40 | 0 | 7025.24 |
| UP_20 | 40 | 0 | 14050.49 |
| UP_30 | 40 | 0 | 21075.73 |
| UP_40 | 40 | 11 | 26900.09 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
