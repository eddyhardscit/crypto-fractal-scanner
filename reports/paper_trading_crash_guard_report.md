# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-01T05:06:20+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **6**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **712.54 R**
- Profitto virtuale mancato: **1224.73 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 245 | 0 | 16110.35 |
| DOWN_20 | 245 | 0 | 32220.70 |
| DOWN_30 | 245 | 2 | 48333.18 |
| DOWN_40 | 245 | 80 | 61174.23 |
| UP_10 | 103 | 0 | 9552.43 |
| UP_20 | 103 | 0 | 19104.87 |
| UP_30 | 103 | 0 | 28657.30 |
| UP_40 | 103 | 36 | 35617.46 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
