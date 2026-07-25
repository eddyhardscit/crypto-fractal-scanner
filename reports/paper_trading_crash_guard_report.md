# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-25T05:08:37+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **37**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **-21.28 R**
- Profitto virtuale mancato: **77.89 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 156 | 0 | 14412.45 |
| DOWN_20 | 156 | 0 | 28824.90 |
| DOWN_30 | 156 | 0 | 43237.35 |
| DOWN_40 | 156 | 62 | 54546.36 |
| UP_10 | 71 | 0 | 19444.58 |
| UP_20 | 71 | 0 | 38889.15 |
| UP_30 | 71 | 0 | 58333.73 |
| UP_40 | 71 | 45 | 68314.24 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
