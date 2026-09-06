# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-06T05:08:07+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **118**
- Simulazioni completate nel ciclo: **1**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **455.00 R**
- Profitto virtuale mancato: **1738.91 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 391 | 0 | 21826.59 |
| DOWN_20 | 391 | 0 | 43653.18 |
| DOWN_30 | 391 | 5 | 65534.06 |
| DOWN_40 | 391 | 117 | 80864.12 |
| UP_10 | 113 | 2 | 8876.44 |
| UP_20 | 113 | 3 | 17692.88 |
| UP_30 | 113 | 3 | 26416.66 |
| UP_40 | 113 | 52 | 32294.08 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
