# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-09T05:06:28+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **16**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **577.34 R**
- Profitto virtuale mancato: **1738.91 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 312 | 0 | 18315.09 |
| DOWN_20 | 312 | 0 | 36630.18 |
| DOWN_30 | 312 | 0 | 54945.26 |
| DOWN_40 | 312 | 98 | 68502.55 |
| UP_10 | 112 | 0 | 8431.60 |
| UP_20 | 112 | 0 | 16863.21 |
| UP_30 | 112 | 15 | 26156.93 |
| UP_40 | 112 | 54 | 30977.70 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
