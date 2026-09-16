# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-16T05:06:28+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **20**
- Simulazioni bloccate attive: **70**
- Simulazioni completate nel ciclo: **24**
- Liquidazioni virtuali evitate totali: **2**
- Valore cumulato del filtro: **743.33 R**
- Profitto virtuale mancato: **1862.41 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 248 | 0 | 13917.16 |
| DOWN_20 | 248 | 0 | 27834.32 |
| DOWN_30 | 248 | 0 | 41751.48 |
| DOWN_40 | 248 | 57 | 53133.09 |
| UP_10 | 172 | 0 | 10382.23 |
| UP_20 | 172 | 0 | 20764.46 |
| UP_30 | 172 | 0 | 31146.69 |
| UP_40 | 172 | 90 | 37108.78 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
