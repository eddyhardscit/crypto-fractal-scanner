# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-17T05:06:02+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **44**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **2**
- Valore cumulato del filtro: **760.22 R**
- Profitto virtuale mancato: **1889.97 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 284 | 0 | 14878.15 |
| DOWN_20 | 284 | 0 | 29756.30 |
| DOWN_30 | 284 | 0 | 44634.46 |
| DOWN_40 | 284 | 71 | 56634.58 |
| UP_10 | 158 | 0 | 8991.37 |
| UP_20 | 158 | 0 | 17982.74 |
| UP_30 | 158 | 0 | 26974.11 |
| UP_40 | 158 | 81 | 32343.50 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
