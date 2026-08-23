# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-23T05:05:50+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **117**
- Simulazioni completate nel ciclo: **7**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **732.38 R**
- Profitto virtuale mancato: **914.92 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 225 | 0 | 11784.09 |
| DOWN_20 | 225 | 0 | 23568.18 |
| DOWN_30 | 225 | 4 | 35388.39 |
| DOWN_40 | 225 | 80 | 44084.80 |
| UP_10 | 20 | 0 | 1472.21 |
| UP_20 | 20 | 0 | 2944.41 |
| UP_30 | 20 | 0 | 4416.62 |
| UP_40 | 20 | 2 | 5835.26 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
