# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-18T05:05:56+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **68**
- Simulazioni completate nel ciclo: **36**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **620.33 R**
- Profitto virtuale mancato: **908.76 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 166 | 0 | 21211.89 |
| DOWN_20 | 166 | 0 | 42423.78 |
| DOWN_30 | 166 | 0 | 63635.67 |
| DOWN_40 | 166 | 49 | 81518.63 |
| UP_10 | 87 | 0 | 14343.49 |
| UP_20 | 87 | 0 | 28686.98 |
| UP_30 | 87 | 0 | 43030.47 |
| UP_40 | 87 | 34 | 53322.58 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
