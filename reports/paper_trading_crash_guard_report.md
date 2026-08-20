# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-20T05:05:45+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **54**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **656.84 R**
- Profitto virtuale mancato: **908.76 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 160 | 0 | 20027.44 |
| DOWN_20 | 160 | 0 | 40054.88 |
| DOWN_30 | 160 | 0 | 60082.32 |
| DOWN_40 | 160 | 58 | 75018.18 |
| UP_10 | 56 | 0 | 5477.60 |
| UP_20 | 56 | 0 | 10955.19 |
| UP_30 | 56 | 0 | 16432.79 |
| UP_40 | 56 | 16 | 21294.16 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
