# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-08T05:05:51+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **22**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **555.06 R**
- Profitto virtuale mancato: **1738.91 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 274 | 0 | 15884.64 |
| DOWN_20 | 274 | 0 | 31769.28 |
| DOWN_30 | 274 | 2 | 47689.79 |
| DOWN_40 | 274 | 64 | 60914.89 |
| UP_10 | 133 | 0 | 13242.97 |
| UP_20 | 133 | 0 | 26485.94 |
| UP_30 | 133 | 0 | 39728.91 |
| UP_40 | 133 | 71 | 46532.19 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
